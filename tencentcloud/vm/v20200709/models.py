# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""音频输出参数

    """

    def __init__(self):
        r"""
        :param _HitFlag: 是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Label: 命中的标签
Porn 色情
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
Moan 呻吟
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _Extra: 拓展字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _TextResults: 文本审核结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TextResults: list of AudioResultDetailTextResult
        :param _MoanResults: 音频呻吟审核结果
注意：此字段可能返回 null，表示取不到有效值。
        :type MoanResults: list of AudioResultDetailMoanResult
        :param _LanguageResults: 音频语种检测结果
注意：此字段可能返回 null，表示取不到有效值。
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
        r"""是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Label(self):
        r"""命中的标签
Porn 色情
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
Moan 呻吟
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        r"""审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        r"""得分，0-100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Text(self):
        r"""音频ASR文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Url(self):
        r"""音频片段存储URL，有效期为1天
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Duration(self):
        r"""音频时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Extra(self):
        r"""拓展字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def TextResults(self):
        r"""文本审核结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioResultDetailTextResult
        """
        return self._TextResults

    @TextResults.setter
    def TextResults(self, TextResults):
        self._TextResults = TextResults

    @property
    def MoanResults(self):
        r"""音频呻吟审核结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioResultDetailMoanResult
        """
        return self._MoanResults

    @MoanResults.setter
    def MoanResults(self, MoanResults):
        self._MoanResults = MoanResults

    @property
    def LanguageResults(self):
        r"""音频语种检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioResultDetailLanguageResult
        """
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
    r"""音频小语种检测结果

    """

    def __init__(self):
        r"""
        :param _Label: 语种
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
        r"""语种
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        r"""得分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        r"""开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubLabelCode(self):
        r"""子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
    r"""音频呻吟审核结果

    """

    def __init__(self):
        r"""
        :param _Label: 固定为Moan
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
        r"""固定为Moan
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        r"""分数
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: float
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubLabelCode(self):
        r"""子标签码
        :rtype: str
        """
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
    r"""音频ASR文本审核结果

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
        :param _LibType: 词库类型 1 黑白库 2 自定义库
注意：此字段可能返回 null，表示取不到有效值。
        :type LibType: int
        :param _Suggestion: 审核建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        """
        self._Label = None
        self._Keywords = None
        self._LibId = None
        self._LibName = None
        self._Score = None
        self._LibType = None
        self._Suggestion = None

    @property
    def Label(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Keywords(self):
        r"""命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def LibId(self):
        r"""命中的LibId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        r"""命中的LibName
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Score(self):
        r"""得分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def LibType(self):
        r"""词库类型 1 黑白库 2 自定义库
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LibType

    @LibType.setter
    def LibType(self, LibType):
        self._LibType = LibType

    @property
    def Suggestion(self):
        r"""审核建议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Keywords = params.get("Keywords")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Score = params.get("Score")
        self._LibType = params.get("LibType")
        self._Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSegments(AbstractModel):
    r"""声音段信息

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
        :type Result: :class:`tencentcloud.vm.v20200709.models.AudioResult`
        """
        self._OffsetTime = None
        self._Result = None

    @property
    def OffsetTime(self):
        r"""截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def Result(self):
        r"""结果集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vm.v20200709.models.AudioResult`
        """
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
    r"""文件桶信息
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
        r"""腾讯云对象存储，存储桶名称
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Object(self):
        r"""对象Key
        :rtype: str
        """
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
    r"""CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
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
    r"""CancelTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBizConfigRequest(AbstractModel):
    r"""CreateBizConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 业务ID，仅限英文字母、数字和下划线（_）组成，长度不超过8位
        :type BizType: str
        :param _MediaModeration: 审核分类信息
        :type MediaModeration: :class:`tencentcloud.vm.v20200709.models.MediaModerationConfig`
        :param _BizName: 业务名称，用于标识业务场景，长度不超过32位
        :type BizName: str
        :param _ModerationCategories: 审核内容，可选：Polity (政治); Porn (色情); Illegal(违法);Abuse (谩骂); Terror (暴恐); Ad (广告); Custom (自定义);
        :type ModerationCategories: list of str
        """
        self._BizType = None
        self._MediaModeration = None
        self._BizName = None
        self._ModerationCategories = None

    @property
    def BizType(self):
        r"""业务ID，仅限英文字母、数字和下划线（_）组成，长度不超过8位
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def MediaModeration(self):
        r"""审核分类信息
        :rtype: :class:`tencentcloud.vm.v20200709.models.MediaModerationConfig`
        """
        return self._MediaModeration

    @MediaModeration.setter
    def MediaModeration(self, MediaModeration):
        self._MediaModeration = MediaModeration

    @property
    def BizName(self):
        r"""业务名称，用于标识业务场景，长度不超过32位
        :rtype: str
        """
        return self._BizName

    @BizName.setter
    def BizName(self, BizName):
        self._BizName = BizName

    @property
    def ModerationCategories(self):
        r"""审核内容，可选：Polity (政治); Porn (色情); Illegal(违法);Abuse (谩骂); Terror (暴恐); Ad (广告); Custom (自定义);
        :rtype: list of str
        """
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
    r"""CreateBizConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateVideoModerationTaskRequest(AbstractModel):
    r"""CreateVideoModerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 业务类型, 定义 模版策略，输出存储配置。如果没有BizType，可以先参考 【创建业务配置】接口进行创建
        :type BizType: str
        :param _Type: 任务类型：可选VIDEO（点播视频），LIVE_VIDEO（直播视频）
        :type Type: str
        :param _Tasks: 输入的任务信息，最多可以同时创建10个任务
        :type Tasks: list of TaskInput
        :param _Seed: 回调签名key，具体可以查看签名文档。
        :type Seed: str
        :param _CallbackUrl: 接收审核信息回调地址，如果设置，则审核过程中产生的违规音频片段和画面截帧发送此接口
        :type CallbackUrl: str
        :param _Priority: 审核排队优先级。当您有多个视频审核任务排队时，可以根据这个参数控制排队优先级。用于处理插队等逻辑。默认该参数为0
        :type Priority: int
        """
        self._BizType = None
        self._Type = None
        self._Tasks = None
        self._Seed = None
        self._CallbackUrl = None
        self._Priority = None

    @property
    def BizType(self):
        r"""业务类型, 定义 模版策略，输出存储配置。如果没有BizType，可以先参考 【创建业务配置】接口进行创建
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Type(self):
        r"""任务类型：可选VIDEO（点播视频），LIVE_VIDEO（直播视频）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tasks(self):
        r"""输入的任务信息，最多可以同时创建10个任务
        :rtype: list of TaskInput
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Seed(self):
        r"""回调签名key，具体可以查看签名文档。
        :rtype: str
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def CallbackUrl(self):
        r"""接收审核信息回调地址，如果设置，则审核过程中产生的违规音频片段和画面截帧发送此接口
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Priority(self):
        r"""审核排队优先级。当您有多个视频审核任务排队时，可以根据这个参数控制排队优先级。用于处理插队等逻辑。默认该参数为0
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._Type = params.get("Type")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInput()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Seed = params.get("Seed")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoModerationTaskResponse(AbstractModel):
    r"""CreateVideoModerationTask返回参数结构体

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
        r"""任务创建结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeTaskDetailRequest(AbstractModel):
    r"""DescribeTaskDetail请求参数结构体

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
        r"""任务ID，创建任务后返回的TaskId字段
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ShowAllSegments(self):
        r"""是否展示所有分片，默认只展示命中规则的分片
        :rtype: bool
        """
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
    r"""DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _DataId: 审核时传入的数据Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param _BizType: 业务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param _Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: 状态，可选值：
FINISH 已完成
PENDING 等待中
RUNNING 进行中
ERROR 出错
CANCELLED 已取消
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Suggestion: 审核建议
可选：
Pass 通过
Reveiw 建议复审
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Labels: 审核结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param _MediaInfo: 媒体解码信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.vm.v20200709.models.MediaInfo`
        :param _InputInfo: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.vm.v20200709.models.InputInfo`
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _TryInSeconds: 在秒后重试
注意：此字段可能返回 null，表示取不到有效值。
        :type TryInSeconds: int
        :param _ImageSegments: 图片结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSegments: list of ImageSegments
        :param _AudioSegments: 音频结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioSegments: list of AudioSegments
        :param _ErrorType: 如果返回的状态为ERROR，该字段会标记错误类型。
可选值：：
DECODE_ERROR: 解码失败。（输入资源中可能包含无法解码的视频）
URL_ERROR：下载地址验证失败。
TIMEOUT_ERROR：处理超时。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorType: str
        :param _ErrorDescription: 审核任务错误日志。当Error不为空时，会展示该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDescription: str
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
        self._ImageSegments = None
        self._AudioSegments = None
        self._ErrorType = None
        self._ErrorDescription = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DataId(self):
        r"""审核时传入的数据Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def BizType(self):
        r"""业务类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Name(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""状态，可选值：
FINISH 已完成
PENDING 等待中
RUNNING 进行中
ERROR 出错
CANCELLED 已取消
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Suggestion(self):
        r"""审核建议
可选：
Pass 通过
Reveiw 建议复审
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Labels(self):
        r"""审核结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def MediaInfo(self):
        r"""媒体解码信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vm.v20200709.models.MediaInfo`
        """
        return self._MediaInfo

    @MediaInfo.setter
    def MediaInfo(self, MediaInfo):
        self._MediaInfo = MediaInfo

    @property
    def InputInfo(self):
        r"""任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vm.v20200709.models.InputInfo`
        """
        return self._InputInfo

    @InputInfo.setter
    def InputInfo(self, InputInfo):
        self._InputInfo = InputInfo

    @property
    def CreatedAt(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def TryInSeconds(self):
        r"""在秒后重试
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TryInSeconds

    @TryInSeconds.setter
    def TryInSeconds(self, TryInSeconds):
        self._TryInSeconds = TryInSeconds

    @property
    def ImageSegments(self):
        r"""图片结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImageSegments
        """
        return self._ImageSegments

    @ImageSegments.setter
    def ImageSegments(self, ImageSegments):
        self._ImageSegments = ImageSegments

    @property
    def AudioSegments(self):
        r"""音频结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioSegments
        """
        return self._AudioSegments

    @AudioSegments.setter
    def AudioSegments(self, AudioSegments):
        self._AudioSegments = AudioSegments

    @property
    def ErrorType(self):
        r"""如果返回的状态为ERROR，该字段会标记错误类型。
可选值：：
DECODE_ERROR: 解码失败。（输入资源中可能包含无法解码的视频）
URL_ERROR：下载地址验证失败。
TIMEOUT_ERROR：处理超时。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorType

    @ErrorType.setter
    def ErrorType(self, ErrorType):
        self._ErrorType = ErrorType

    @property
    def ErrorDescription(self):
        r"""审核任务错误日志。当Error不为空时，会展示该字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorDescription

    @ErrorDescription.setter
    def ErrorDescription(self, ErrorDescription):
        self._ErrorDescription = ErrorDescription

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        if params.get("ImageSegments") is not None:
            self._ImageSegments = []
            for item in params.get("ImageSegments"):
                obj = ImageSegments()
                obj._deserialize(item)
                self._ImageSegments.append(obj)
        if params.get("AudioSegments") is not None:
            self._AudioSegments = []
            for item in params.get("AudioSegments"):
                obj = AudioSegments()
                obj._deserialize(item)
                self._AudioSegments.append(obj)
        self._ErrorType = params.get("ErrorType")
        self._ErrorDescription = params.get("ErrorDescription")
        self._RequestId = params.get("RequestId")


class DescribeVideoStatRequest(AbstractModel):
    r"""DescribeVideoStat请求参数结构体

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
        r"""审核类型 1: 机器审核; 2: 人工审核
        :rtype: int
        """
        return self._AuditType

    @AuditType.setter
    def AuditType(self, AuditType):
        self._AuditType = AuditType

    @property
    def Filters(self):
        r"""查询条件
        :rtype: list of Filters
        """
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
        


class DescribeVideoStatResponse(AbstractModel):
    r"""DescribeVideoStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Overview: 识别结果统计
        :type Overview: :class:`tencentcloud.vm.v20200709.models.Overview`
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
        r"""识别结果统计
        :rtype: :class:`tencentcloud.vm.v20200709.models.Overview`
        """
        return self._Overview

    @Overview.setter
    def Overview(self, Overview):
        self._Overview = Overview

    @property
    def TrendCount(self):
        r"""识别量统计
        :rtype: list of TrendCount
        """
        return self._TrendCount

    @TrendCount.setter
    def TrendCount(self, TrendCount):
        self._TrendCount = TrendCount

    @property
    def EvilCount(self):
        r"""违规数据分布
        :rtype: list of EvilCount
        """
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class EvilCount(AbstractModel):
    r"""违规数据分布

    """

    def __init__(self):
        r"""
        :param _EvilType: 违规类型：
Terror	24001
Porn	20002
Polity	20001
Ad	20105
Abuse	20007	
Illegal	20006	
Spam	25001	
Moan	26001
        :type EvilType: str
        :param _Count: 分布类型总量
        :type Count: int
        """
        self._EvilType = None
        self._Count = None

    @property
    def EvilType(self):
        r"""违规类型：
Terror	24001
Porn	20002
Polity	20001
Ad	20105
Abuse	20007	
Illegal	20006	
Spam	25001	
Moan	26001
        :rtype: str
        """
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def Count(self):
        r"""分布类型总量
        :rtype: int
        """
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
    r"""Cos FileOutput

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
        r"""存储的Bucket
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""Cos Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ObjectPrefix(self):
        r"""对象前缀
        :rtype: str
        """
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
        


class Filters(AbstractModel):
    r"""视频过滤条件

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
        r"""查询字段：
策略BizType
子账号SubUin
日期区间DateRange
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""查询值
        :rtype: list of str
        """
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
    r"""Result结果详情

    """

    def __init__(self):
        r"""
        :param _HitFlag: 违规标志
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Label: 命中的标签
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Results: 画面截帧图片结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of ImageResultResult
        :param _Url: 图片URL地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Extra: 附加字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        """
        self._HitFlag = None
        self._Label = None
        self._Suggestion = None
        self._Score = None
        self._Results = None
        self._Url = None
        self._Extra = None

    @property
    def HitFlag(self):
        r"""违规标志
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Label(self):
        r"""命中的标签
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        r"""审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        r"""得分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Results(self):
        r"""画面截帧图片结果集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImageResultResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def Url(self):
        r"""图片URL地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Extra(self):
        r"""附加字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._HitFlag = params.get("HitFlag")
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
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
    r"""图片输出结果的子结果

    """

    def __init__(self):
        r"""
        :param _Scene: 场景
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Scene: str
        :param _HitFlag: 是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Names: list of str
        :param _Text: 图片OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Details: 其他详情
注意：此字段可能返回 null，表示取不到有效值。
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
        r"""场景
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def HitFlag(self):
        r"""是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Suggestion(self):
        r"""审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        r"""子标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        r"""分数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Names(self):
        r"""如果命中场景为涉政，则该数据为人物姓名列表，否则null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Text(self):
        r"""图片OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Details(self):
        r"""其他详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImageResultsResultDetail
        """
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
    r"""具体场景下的图片识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Text: OCR识别文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Location: 位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: :class:`tencentcloud.vm.v20200709.models.ImageResultsResultDetailLocation`
        :param _Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
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
        self._Name = None
        self._Text = None
        self._Location = None
        self._Label = None
        self._LibId = None
        self._LibName = None
        self._Keywords = None
        self._Suggestion = None
        self._Score = None
        self._SubLabelCode = None

    @property
    def Name(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Text(self):
        r"""OCR识别文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Location(self):
        r"""位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vm.v20200709.models.ImageResultsResultDetailLocation`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Label(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def LibId(self):
        r"""库ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        r"""库名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Keywords(self):
        r"""命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Suggestion(self):
        r"""建议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        r"""得分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def SubLabelCode(self):
        r"""子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubLabelCode

    @SubLabelCode.setter
    def SubLabelCode(self, SubLabelCode):
        self._SubLabelCode = SubLabelCode


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Text = params.get("Text")
        if params.get("Location") is not None:
            self._Location = ImageResultsResultDetailLocation()
            self._Location._deserialize(params.get("Location"))
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
    r"""图片详情位置信息

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
        r"""x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""宽度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""高度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Rotate(self):
        r"""旋转角度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
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
    r"""图片段信息

    """

    def __init__(self):
        r"""
        :param _OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
        :type OffsetTime: str
        :param _Result: 画面截帧结果详情
        :type Result: :class:`tencentcloud.vm.v20200709.models.ImageResult`
        """
        self._OffsetTime = None
        self._Result = None

    @property
    def OffsetTime(self):
        r"""截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
        :rtype: str
        """
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def Result(self):
        r"""画面截帧结果详情
        :rtype: :class:`tencentcloud.vm.v20200709.models.ImageResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self._Result = ImageResult()
            self._Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    r"""输入信息详情

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
        :type BucketInfo: str
        """
        self._Type = None
        self._Url = None
        self._BucketInfo = None

    @property
    def Type(self):
        r"""传入的类型可选：URL，COS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""Url地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BucketInfo(self):
        r"""桶信息。当输入当时COS时，该字段不为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BucketInfo

    @BucketInfo.setter
    def BucketInfo(self, BucketInfo):
        self._BucketInfo = BucketInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._BucketInfo = params.get("BucketInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    r"""媒体类型

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
        """
        self._Codecs = None
        self._Duration = None
        self._Width = None
        self._Height = None

    @property
    def Codecs(self):
        r"""编码格式
        :rtype: str
        """
        return self._Codecs

    @Codecs.setter
    def Codecs(self, Codecs):
        self._Codecs = Codecs

    @property
    def Duration(self):
        r"""流检测时分片时长
注意：此字段可能返回 0，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Width(self):
        r"""宽，单位为像素
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""高，单位为像素
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._Codecs = params.get("Codecs")
        self._Duration = params.get("Duration")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaModerationConfig(AbstractModel):
    r"""媒体审核配置

    """

    def __init__(self):
        r"""
        :param _UseOCR: 是否使用OCR，默认为true
        :type UseOCR: bool
        :param _UseAudio: 是否使用音频，默认为true。视频场景下，默认为 false
        :type UseAudio: bool
        :param _ImageFrequency: 图片取帧频率, 单位（秒/帧），默认 5， 可选 1 ～ 300
        :type ImageFrequency: int
        :param _AudioFrequency: 音频片段长度。单位为：秒
        :type AudioFrequency: int
        :param _SegmentOutput: 临时文件存储位置
        :type SegmentOutput: :class:`tencentcloud.vm.v20200709.models.FileOutput`
        :param _CallbackUrl: 回调地址
        :type CallbackUrl: str
        """
        self._UseOCR = None
        self._UseAudio = None
        self._ImageFrequency = None
        self._AudioFrequency = None
        self._SegmentOutput = None
        self._CallbackUrl = None

    @property
    def UseOCR(self):
        r"""是否使用OCR，默认为true
        :rtype: bool
        """
        return self._UseOCR

    @UseOCR.setter
    def UseOCR(self, UseOCR):
        self._UseOCR = UseOCR

    @property
    def UseAudio(self):
        r"""是否使用音频，默认为true。视频场景下，默认为 false
        :rtype: bool
        """
        return self._UseAudio

    @UseAudio.setter
    def UseAudio(self, UseAudio):
        self._UseAudio = UseAudio

    @property
    def ImageFrequency(self):
        r"""图片取帧频率, 单位（秒/帧），默认 5， 可选 1 ～ 300
        :rtype: int
        """
        return self._ImageFrequency

    @ImageFrequency.setter
    def ImageFrequency(self, ImageFrequency):
        self._ImageFrequency = ImageFrequency

    @property
    def AudioFrequency(self):
        r"""音频片段长度。单位为：秒
        :rtype: int
        """
        return self._AudioFrequency

    @AudioFrequency.setter
    def AudioFrequency(self, AudioFrequency):
        self._AudioFrequency = AudioFrequency

    @property
    def SegmentOutput(self):
        r"""临时文件存储位置
        :rtype: :class:`tencentcloud.vm.v20200709.models.FileOutput`
        """
        return self._SegmentOutput

    @SegmentOutput.setter
    def SegmentOutput(self, SegmentOutput):
        self._SegmentOutput = SegmentOutput

    @property
    def CallbackUrl(self):
        r"""回调地址
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._UseOCR = params.get("UseOCR")
        self._UseAudio = params.get("UseAudio")
        self._ImageFrequency = params.get("ImageFrequency")
        self._AudioFrequency = params.get("AudioFrequency")
        if params.get("SegmentOutput") is not None:
            self._SegmentOutput = FileOutput()
            self._SegmentOutput._deserialize(params.get("SegmentOutput"))
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Overview(AbstractModel):
    r"""识别结果统计

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
        r"""总调用量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalHour(self):
        r"""总调用时长
        :rtype: int
        """
        return self._TotalHour

    @TotalHour.setter
    def TotalHour(self, TotalHour):
        self._TotalHour = TotalHour

    @property
    def PassCount(self):
        r"""通过量
        :rtype: int
        """
        return self._PassCount

    @PassCount.setter
    def PassCount(self, PassCount):
        self._PassCount = PassCount

    @property
    def PassHour(self):
        r"""通过时长
        :rtype: int
        """
        return self._PassHour

    @PassHour.setter
    def PassHour(self, PassHour):
        self._PassHour = PassHour

    @property
    def EvilCount(self):
        r"""违规量
        :rtype: int
        """
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

    @property
    def EvilHour(self):
        r"""违规时长
        :rtype: int
        """
        return self._EvilHour

    @EvilHour.setter
    def EvilHour(self, EvilHour):
        self._EvilHour = EvilHour

    @property
    def SuspectCount(self):
        r"""疑似违规量
        :rtype: int
        """
        return self._SuspectCount

    @SuspectCount.setter
    def SuspectCount(self, SuspectCount):
        self._SuspectCount = SuspectCount

    @property
    def SuspectHour(self):
        r"""疑似违规时长
        :rtype: int
        """
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
    r"""数据存储信息

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
        :type BucketInfo: :class:`tencentcloud.vm.v20200709.models.BucketInfo`
        """
        self._Type = None
        self._Url = None
        self._BucketInfo = None

    @property
    def Type(self):
        r"""类型 可选：
URL 资源链接类型
COS 腾讯云对象存储类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""资源链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BucketInfo(self):
        r"""腾讯云存储桶信息
        :rtype: :class:`tencentcloud.vm.v20200709.models.BucketInfo`
        """
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
    r"""音视频任务结构

    """

    def __init__(self):
        r"""
        :param _DataId: 数据ID
        :type DataId: str
        :param _Name: 任务名
        :type Name: str
        :param _Input: 任务输入
        :type Input: :class:`tencentcloud.vm.v20200709.models.StorageInfo`
        """
        self._DataId = None
        self._Name = None
        self._Input = None

    @property
    def DataId(self):
        r"""数据ID
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Name(self):
        r"""任务名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Input(self):
        r"""任务输入
        :rtype: :class:`tencentcloud.vm.v20200709.models.StorageInfo`
        """
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
    r"""任务输出标签

    """

    def __init__(self):
        r"""
        :param _Label: 命中的标签
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
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
        r"""命中的标签
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        r"""审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        r"""得分，分数是 0 ～ 100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
    r"""创建任务时的返回结果

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
        r"""请求时传入的DataId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def TaskId(self):
        r"""TaskId，任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Code(self):
        r"""错误码。如果code为OK，则表示创建成功，其他则参考公共错误码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""如果错误，该字段表示错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
    r"""识别量统计

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
        r"""总调用量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalHour(self):
        r"""总调用时长
        :rtype: int
        """
        return self._TotalHour

    @TotalHour.setter
    def TotalHour(self, TotalHour):
        self._TotalHour = TotalHour

    @property
    def PassCount(self):
        r"""通过量
        :rtype: int
        """
        return self._PassCount

    @PassCount.setter
    def PassCount(self, PassCount):
        self._PassCount = PassCount

    @property
    def PassHour(self):
        r"""通过时长
        :rtype: int
        """
        return self._PassHour

    @PassHour.setter
    def PassHour(self, PassHour):
        self._PassHour = PassHour

    @property
    def EvilCount(self):
        r"""违规量
        :rtype: int
        """
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

    @property
    def EvilHour(self):
        r"""违规时长
        :rtype: int
        """
        return self._EvilHour

    @EvilHour.setter
    def EvilHour(self, EvilHour):
        self._EvilHour = EvilHour

    @property
    def SuspectCount(self):
        r"""疑似违规量
        :rtype: int
        """
        return self._SuspectCount

    @SuspectCount.setter
    def SuspectCount(self, SuspectCount):
        self._SuspectCount = SuspectCount

    @property
    def SuspectHour(self):
        r"""疑似违规时长
        :rtype: int
        """
        return self._SuspectHour

    @SuspectHour.setter
    def SuspectHour(self, SuspectHour):
        self._SuspectHour = SuspectHour

    @property
    def Date(self):
        r"""日期
        :rtype: str
        """
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
        