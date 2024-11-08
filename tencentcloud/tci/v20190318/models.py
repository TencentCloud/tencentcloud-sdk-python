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


class AIAssistantRequest(AbstractModel):
    """AIAssistant请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param _FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，audio_url: 音频文件，picture：图片二进制数据的BASE64编码
        :type FileType: str
        :param _Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param _LibrarySet: 查询人员库列表
        :type LibrarySet: list of str
        :param _MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param _Template: 标准化模板选择：0：AI助教基础版本，1：AI评教基础版本，2：AI评教标准版本。AI 助教基础版本功能包括：人脸检索、人脸检测、人脸表情识别、学生动作选项，音频信息分析，微笑识别。AI 评教基础版本功能包括：人脸检索、人脸检测、人脸表情识别、音频信息分析。AI 评教标准版功能包括人脸检索、人脸检测、人脸表情识别、手势识别、音频信息分析、音频关键词分析、视频精彩集锦分析。
        :type Template: int
        :param _VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :type VocabLibNameList: list of str
        :param _VoiceEncodeType: 语音编码类型 1:pcm
        :type VoiceEncodeType: int
        :param _VoiceFileType: 语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）
        :type VoiceFileType: int
        """
        self._FileContent = None
        self._FileType = None
        self._Lang = None
        self._LibrarySet = None
        self._MaxVideoDuration = None
        self._Template = None
        self._VocabLibNameList = None
        self._VoiceEncodeType = None
        self._VoiceFileType = None

    @property
    def FileContent(self):
        """输入分析对象内容，输入数据格式参考FileType参数释义
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，audio_url: 音频文件，picture：图片二进制数据的BASE64编码
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Lang(self):
        """音频源的语言，默认0为英文，1为中文
        :rtype: int
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def LibrarySet(self):
        """查询人员库列表
        :rtype: list of str
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def MaxVideoDuration(self):
        """视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration

    @property
    def Template(self):
        """标准化模板选择：0：AI助教基础版本，1：AI评教基础版本，2：AI评教标准版本。AI 助教基础版本功能包括：人脸检索、人脸检测、人脸表情识别、学生动作选项，音频信息分析，微笑识别。AI 评教基础版本功能包括：人脸检索、人脸检测、人脸表情识别、音频信息分析。AI 评教标准版功能包括人脸检索、人脸检测、人脸表情识别、手势识别、音频信息分析、音频关键词分析、视频精彩集锦分析。
        :rtype: int
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def VocabLibNameList(self):
        """识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :rtype: list of str
        """
        return self._VocabLibNameList

    @VocabLibNameList.setter
    def VocabLibNameList(self, VocabLibNameList):
        self._VocabLibNameList = VocabLibNameList

    @property
    def VoiceEncodeType(self):
        """语音编码类型 1:pcm
        :rtype: int
        """
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def VoiceFileType(self):
        """语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）
        :rtype: int
        """
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._Lang = params.get("Lang")
        self._LibrarySet = params.get("LibrarySet")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        self._Template = params.get("Template")
        self._VocabLibNameList = params.get("VocabLibNameList")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._VoiceFileType = params.get("VoiceFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIAssistantResponse(AbstractModel):
    """AIAssistant返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageResults: 图像任务直接返回结果
        :type ImageResults: list of ImageTaskResult
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageResults = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ImageResults(self):
        """图像任务直接返回结果
        :rtype: list of ImageTaskResult
        """
        return self._ImageResults

    @ImageResults.setter
    def ImageResults(self, ImageResults):
        self._ImageResults = ImageResults

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self._ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ImageResults.append(obj)
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ASRStat(AbstractModel):
    """当前音频的统计结果

    """

    def __init__(self):
        r"""
        :param _AvgSpeed: 当前音频的平均语速
        :type AvgSpeed: float
        :param _AvgVolume: Vad的平均音量
        :type AvgVolume: float
        :param _MaxVolume: Vad的最大音量
        :type MaxVolume: float
        :param _MinVolume: Vad的最小音量
        :type MinVolume: float
        :param _MuteDuration: 当前音频的非发音时长
        :type MuteDuration: int
        :param _SoundDuration: 当前音频的发音时长
        :type SoundDuration: int
        :param _TotalDuration: 当前音频的总时长
        :type TotalDuration: int
        :param _VadNum: 当前音频的句子总数
        :type VadNum: int
        :param _WordNum: 当前音频的单词总数
        :type WordNum: int
        """
        self._AvgSpeed = None
        self._AvgVolume = None
        self._MaxVolume = None
        self._MinVolume = None
        self._MuteDuration = None
        self._SoundDuration = None
        self._TotalDuration = None
        self._VadNum = None
        self._WordNum = None

    @property
    def AvgSpeed(self):
        """当前音频的平均语速
        :rtype: float
        """
        return self._AvgSpeed

    @AvgSpeed.setter
    def AvgSpeed(self, AvgSpeed):
        self._AvgSpeed = AvgSpeed

    @property
    def AvgVolume(self):
        """Vad的平均音量
        :rtype: float
        """
        return self._AvgVolume

    @AvgVolume.setter
    def AvgVolume(self, AvgVolume):
        self._AvgVolume = AvgVolume

    @property
    def MaxVolume(self):
        """Vad的最大音量
        :rtype: float
        """
        return self._MaxVolume

    @MaxVolume.setter
    def MaxVolume(self, MaxVolume):
        self._MaxVolume = MaxVolume

    @property
    def MinVolume(self):
        """Vad的最小音量
        :rtype: float
        """
        return self._MinVolume

    @MinVolume.setter
    def MinVolume(self, MinVolume):
        self._MinVolume = MinVolume

    @property
    def MuteDuration(self):
        """当前音频的非发音时长
        :rtype: int
        """
        return self._MuteDuration

    @MuteDuration.setter
    def MuteDuration(self, MuteDuration):
        self._MuteDuration = MuteDuration

    @property
    def SoundDuration(self):
        """当前音频的发音时长
        :rtype: int
        """
        return self._SoundDuration

    @SoundDuration.setter
    def SoundDuration(self, SoundDuration):
        self._SoundDuration = SoundDuration

    @property
    def TotalDuration(self):
        """当前音频的总时长
        :rtype: int
        """
        return self._TotalDuration

    @TotalDuration.setter
    def TotalDuration(self, TotalDuration):
        self._TotalDuration = TotalDuration

    @property
    def VadNum(self):
        """当前音频的句子总数
        :rtype: int
        """
        return self._VadNum

    @VadNum.setter
    def VadNum(self, VadNum):
        self._VadNum = VadNum

    @property
    def WordNum(self):
        """当前音频的单词总数
        :rtype: int
        """
        return self._WordNum

    @WordNum.setter
    def WordNum(self, WordNum):
        self._WordNum = WordNum


    def _deserialize(self, params):
        self._AvgSpeed = params.get("AvgSpeed")
        self._AvgVolume = params.get("AvgVolume")
        self._MaxVolume = params.get("MaxVolume")
        self._MinVolume = params.get("MinVolume")
        self._MuteDuration = params.get("MuteDuration")
        self._SoundDuration = params.get("SoundDuration")
        self._TotalDuration = params.get("TotalDuration")
        self._VadNum = params.get("VadNum")
        self._WordNum = params.get("WordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbsenceInfo(AbstractModel):
    """缺勤人员信息

    """

    def __init__(self):
        r"""
        :param _LibraryIds: 识别到的人员所在的库id
        :type LibraryIds: str
        :param _PersonId: 识别到的人员id
        :type PersonId: str
        """
        self._LibraryIds = None
        self._PersonId = None

    @property
    def LibraryIds(self):
        """识别到的人员所在的库id
        :rtype: str
        """
        return self._LibraryIds

    @LibraryIds.setter
    def LibraryIds(self, LibraryIds):
        self._LibraryIds = LibraryIds

    @property
    def PersonId(self):
        """识别到的人员id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._LibraryIds = params.get("LibraryIds")
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionCountStatistic(AbstractModel):
    """数量统计结果

    """

    def __init__(self):
        r"""
        :param _Count: 数量
        :type Count: int
        :param _Name: 名称
        :type Name: str
        """
        self._Count = None
        self._Name = None

    @property
    def Count(self):
        """数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionDurationRatioStatistic(AbstractModel):
    """时长占比统计结果

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Ratio: 比例
        :type Ratio: float
        """
        self._Name = None
        self._Ratio = None

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Ratio(self):
        """比例
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionDurationStatistic(AbstractModel):
    """时长统计结果

    """

    def __init__(self):
        r"""
        :param _Duration: 时长
        :type Duration: int
        :param _Name: 名称
        :type Name: str
        """
        self._Duration = None
        self._Name = None

    @property
    def Duration(self):
        """时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionInfo(AbstractModel):
    """大教室场景肢体动作识别信息

    """

    def __init__(self):
        r"""
        :param _BodyPosture: 躯体动作识别结果，包含坐着（sit）、站立（stand）和趴睡（sleep）
        :type BodyPosture: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param _Handup: 举手识别结果，包含举手（hand）和未检测到举手（nothand）
        :type Handup: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param _LookHead: 是否低头识别结果，包含抬头（lookingahead）和未检测到抬头（notlookingahead）
        :type LookHead: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param _Writing: 是否写字识别结果，包含写字（write）和未检测到写字（notlookingahead）
        :type Writing: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param _Height: 动作图像高度
        :type Height: int
        :param _Left: 动作出现图像的左侧起始坐标位置
        :type Left: int
        :param _Top: 动作出现图像的上侧起始侧坐标位置
        :type Top: int
        :param _Width: 动作图像宽度
        :type Width: int
        """
        self._BodyPosture = None
        self._Handup = None
        self._LookHead = None
        self._Writing = None
        self._Height = None
        self._Left = None
        self._Top = None
        self._Width = None

    @property
    def BodyPosture(self):
        """躯体动作识别结果，包含坐着（sit）、站立（stand）和趴睡（sleep）
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionType`
        """
        return self._BodyPosture

    @BodyPosture.setter
    def BodyPosture(self, BodyPosture):
        self._BodyPosture = BodyPosture

    @property
    def Handup(self):
        """举手识别结果，包含举手（hand）和未检测到举手（nothand）
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionType`
        """
        return self._Handup

    @Handup.setter
    def Handup(self, Handup):
        self._Handup = Handup

    @property
    def LookHead(self):
        """是否低头识别结果，包含抬头（lookingahead）和未检测到抬头（notlookingahead）
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionType`
        """
        return self._LookHead

    @LookHead.setter
    def LookHead(self, LookHead):
        self._LookHead = LookHead

    @property
    def Writing(self):
        """是否写字识别结果，包含写字（write）和未检测到写字（notlookingahead）
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionType`
        """
        return self._Writing

    @Writing.setter
    def Writing(self, Writing):
        self._Writing = Writing

    @property
    def Height(self):
        """动作图像高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Left(self):
        """动作出现图像的左侧起始坐标位置
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Top(self):
        """动作出现图像的上侧起始侧坐标位置
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Width(self):
        """动作图像宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width


    def _deserialize(self, params):
        if params.get("BodyPosture") is not None:
            self._BodyPosture = ActionType()
            self._BodyPosture._deserialize(params.get("BodyPosture"))
        if params.get("Handup") is not None:
            self._Handup = ActionType()
            self._Handup._deserialize(params.get("Handup"))
        if params.get("LookHead") is not None:
            self._LookHead = ActionType()
            self._LookHead._deserialize(params.get("LookHead"))
        if params.get("Writing") is not None:
            self._Writing = ActionType()
            self._Writing._deserialize(params.get("Writing"))
        self._Height = params.get("Height")
        self._Left = params.get("Left")
        self._Top = params.get("Top")
        self._Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionStatistic(AbstractModel):
    """统计结果

    """

    def __init__(self):
        r"""
        :param _ActionCount: 数量统计
        :type ActionCount: list of ActionCountStatistic
        :param _ActionDuration: 时长统计
        :type ActionDuration: list of ActionDurationStatistic
        :param _ActionDurationRatio: 时长比例统计
        :type ActionDurationRatio: list of ActionDurationRatioStatistic
        """
        self._ActionCount = None
        self._ActionDuration = None
        self._ActionDurationRatio = None

    @property
    def ActionCount(self):
        """数量统计
        :rtype: list of ActionCountStatistic
        """
        return self._ActionCount

    @ActionCount.setter
    def ActionCount(self, ActionCount):
        self._ActionCount = ActionCount

    @property
    def ActionDuration(self):
        """时长统计
        :rtype: list of ActionDurationStatistic
        """
        return self._ActionDuration

    @ActionDuration.setter
    def ActionDuration(self, ActionDuration):
        self._ActionDuration = ActionDuration

    @property
    def ActionDurationRatio(self):
        """时长比例统计
        :rtype: list of ActionDurationRatioStatistic
        """
        return self._ActionDurationRatio

    @ActionDurationRatio.setter
    def ActionDurationRatio(self, ActionDurationRatio):
        self._ActionDurationRatio = ActionDurationRatio


    def _deserialize(self, params):
        if params.get("ActionCount") is not None:
            self._ActionCount = []
            for item in params.get("ActionCount"):
                obj = ActionCountStatistic()
                obj._deserialize(item)
                self._ActionCount.append(obj)
        if params.get("ActionDuration") is not None:
            self._ActionDuration = []
            for item in params.get("ActionDuration"):
                obj = ActionDurationStatistic()
                obj._deserialize(item)
                self._ActionDuration.append(obj)
        if params.get("ActionDurationRatio") is not None:
            self._ActionDurationRatio = []
            for item in params.get("ActionDurationRatio"):
                obj = ActionDurationRatioStatistic()
                obj._deserialize(item)
                self._ActionDurationRatio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionType(AbstractModel):
    """动作行为子类型

    """

    def __init__(self):
        r"""
        :param _Confidence: 置信度
        :type Confidence: float
        :param _Type: 动作类别
        :type Type: str
        """
        self._Confidence = None
        self._Type = None

    @property
    def Confidence(self):
        """置信度
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Type(self):
        """动作类别
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllMuteSlice(AbstractModel):
    """如果请求中开启了静音检测开关，则会返回所有的静音片段（静音时长超过阈值的片段）。

    """

    def __init__(self):
        r"""
        :param _MuteSlice: 所有静音片段。
        :type MuteSlice: list of MuteSlice
        :param _MuteRatio: 静音时长占比。
        :type MuteRatio: float
        :param _TotalMuteDuration: 静音总时长。
        :type TotalMuteDuration: int
        """
        self._MuteSlice = None
        self._MuteRatio = None
        self._TotalMuteDuration = None

    @property
    def MuteSlice(self):
        """所有静音片段。
        :rtype: list of MuteSlice
        """
        return self._MuteSlice

    @MuteSlice.setter
    def MuteSlice(self, MuteSlice):
        self._MuteSlice = MuteSlice

    @property
    def MuteRatio(self):
        """静音时长占比。
        :rtype: float
        """
        return self._MuteRatio

    @MuteRatio.setter
    def MuteRatio(self, MuteRatio):
        self._MuteRatio = MuteRatio

    @property
    def TotalMuteDuration(self):
        """静音总时长。
        :rtype: int
        """
        return self._TotalMuteDuration

    @TotalMuteDuration.setter
    def TotalMuteDuration(self, TotalMuteDuration):
        self._TotalMuteDuration = TotalMuteDuration


    def _deserialize(self, params):
        if params.get("MuteSlice") is not None:
            self._MuteSlice = []
            for item in params.get("MuteSlice"):
                obj = MuteSlice()
                obj._deserialize(item)
                self._MuteSlice.append(obj)
        self._MuteRatio = params.get("MuteRatio")
        self._TotalMuteDuration = params.get("TotalMuteDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttendanceInfo(AbstractModel):
    """识别到的人员信息

    """

    def __init__(self):
        r"""
        :param _Face: 识别到的人员信息
        :type Face: :class:`tencentcloud.tci.v20190318.models.FrameInfo`
        :param _PersonId: 识别到的人员id
        :type PersonId: str
        """
        self._Face = None
        self._PersonId = None

    @property
    def Face(self):
        """识别到的人员信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.FrameInfo`
        """
        return self._Face

    @Face.setter
    def Face(self, Face):
        self._Face = Face

    @property
    def PersonId(self):
        """识别到的人员id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        if params.get("Face") is not None:
            self._Face = FrameInfo()
            self._Face._deserialize(params.get("Face"))
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyMovementResult(AbstractModel):
    """老师肢体动作识别结果

    """

    def __init__(self):
        r"""
        :param _Confidence: 置信度
        :type Confidence: float
        :param _Height: 识别结果高度
        :type Height: int
        :param _Left: 识别结果左坐标
        :type Left: int
        :param _Movements: 老师动作识别结果，包含
1、teach_on_positive_attitude 正面讲解
2、point_to_the_blackboard 指黑板
3、writing_blackboard 写板书
4、other 其他
        :type Movements: str
        :param _Top: 识别结果顶坐标
        :type Top: int
        :param _Width: 识别结果宽度
        :type Width: int
        """
        self._Confidence = None
        self._Height = None
        self._Left = None
        self._Movements = None
        self._Top = None
        self._Width = None

    @property
    def Confidence(self):
        """置信度
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Height(self):
        """识别结果高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Left(self):
        """识别结果左坐标
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Movements(self):
        """老师动作识别结果，包含
1、teach_on_positive_attitude 正面讲解
2、point_to_the_blackboard 指黑板
3、writing_blackboard 写板书
4、other 其他
        :rtype: str
        """
        return self._Movements

    @Movements.setter
    def Movements(self, Movements):
        self._Movements = Movements

    @property
    def Top(self):
        """识别结果顶坐标
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Width(self):
        """识别结果宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Height = params.get("Height")
        self._Left = params.get("Left")
        self._Movements = params.get("Movements")
        self._Top = params.get("Top")
        self._Width = params.get("Width")
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
        :param _JobId: 待取消任务标志符。
        :type JobId: int
        """
        self._JobId = None

    @property
    def JobId(self):
        """待取消任务标志符。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
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
        :param _JobId: 取消任务标志符。
        :type JobId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """取消任务标志符。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CheckFacePhotoRequest(AbstractModel):
    """CheckFacePhoto请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容
        :type FileContent: str
        :param _FileType: 输入分析对象类型，picture_url:图片地址
        :type FileType: str
        """
        self._FileContent = None
        self._FileType = None

    @property
    def FileContent(self):
        """输入分析对象内容
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture_url:图片地址
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckFacePhotoResponse(AbstractModel):
    """CheckFacePhoto返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckResult: 人脸检查结果，0：通过检查，1：图片模糊
        :type CheckResult: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckResult = None
        self._RequestId = None

    @property
    def CheckResult(self):
        """人脸检查结果，0：通过检查，1：图片模糊
        :rtype: int
        """
        return self._CheckResult

    @CheckResult.setter
    def CheckResult(self, CheckResult):
        self._CheckResult = CheckResult

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CheckResult = params.get("CheckResult")
        self._RequestId = params.get("RequestId")


class CreateFaceRequest(AbstractModel):
    """CreateFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _Images: 图片数据 base64 字符串，与 Urls 参数选择一个输入
        :type Images: list of str
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _Urls: 图片下载地址，与 Images 参数选择一个输入
        :type Urls: list of str
        """
        self._PersonId = None
        self._Images = None
        self._LibraryId = None
        self._Urls = None

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Images(self):
        """图片数据 base64 字符串，与 Urls 参数选择一个输入
        :rtype: list of str
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Urls(self):
        """图片下载地址，与 Images 参数选择一个输入
        :rtype: list of str
        """
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Images = params.get("Images")
        self._LibraryId = params.get("LibraryId")
        self._Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFaceResponse(AbstractModel):
    """CreateFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceInfoSet: 人脸操作结果信息
        :type FaceInfoSet: list of FaceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceInfoSet = None
        self._RequestId = None

    @property
    def FaceInfoSet(self):
        """人脸操作结果信息
        :rtype: list of FaceInfo
        """
        return self._FaceInfoSet

    @FaceInfoSet.setter
    def FaceInfoSet(self, FaceInfoSet):
        self._FaceInfoSet = FaceInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self._FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self._FaceInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateLibraryRequest(AbstractModel):
    """CreateLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryName: 人员库名称
        :type LibraryName: str
        :param _LibraryId: 人员库唯一标志符，为空则系统自动生成。
        :type LibraryId: str
        """
        self._LibraryName = None
        self._LibraryId = None

    @property
    def LibraryName(self):
        """人员库名称
        :rtype: str
        """
        return self._LibraryName

    @LibraryName.setter
    def LibraryName(self, LibraryName):
        self._LibraryName = LibraryName

    @property
    def LibraryId(self):
        """人员库唯一标志符，为空则系统自动生成。
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId


    def _deserialize(self, params):
        self._LibraryName = params.get("LibraryName")
        self._LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLibraryResponse(AbstractModel):
    """CreateLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _LibraryName: 人员库名称
        :type LibraryName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LibraryId = None
        self._LibraryName = None
        self._RequestId = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def LibraryName(self):
        """人员库名称
        :rtype: str
        """
        return self._LibraryName

    @LibraryName.setter
    def LibraryName(self, LibraryName):
        self._LibraryName = LibraryName

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._LibraryName = params.get("LibraryName")
        self._RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _Images: 图片数据 base64 字符串，与 Urls 参数选择一个输入
        :type Images: list of str
        :param _JobNumber: 人员工作号码
        :type JobNumber: str
        :param _Mail: 人员邮箱
        :type Mail: str
        :param _Male: 人员性别，0：未知 1：男性，2：女性
        :type Male: int
        :param _PersonId: 自定义人员 ID，注意不能使用 tci_person_ 前缀
        :type PersonId: str
        :param _PhoneNumber: 人员电话号码
        :type PhoneNumber: str
        :param _StudentNumber: 人员学生号码
        :type StudentNumber: str
        :param _Urls: 图片下载地址，与 Images 参数选择一个输入
        :type Urls: list of str
        """
        self._LibraryId = None
        self._PersonName = None
        self._Images = None
        self._JobNumber = None
        self._Mail = None
        self._Male = None
        self._PersonId = None
        self._PhoneNumber = None
        self._StudentNumber = None
        self._Urls = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonName(self):
        """人员名称
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def Images(self):
        """图片数据 base64 字符串，与 Urls 参数选择一个输入
        :rtype: list of str
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def JobNumber(self):
        """人员工作号码
        :rtype: str
        """
        return self._JobNumber

    @JobNumber.setter
    def JobNumber(self, JobNumber):
        self._JobNumber = JobNumber

    @property
    def Mail(self):
        """人员邮箱
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Male(self):
        """人员性别，0：未知 1：男性，2：女性
        :rtype: int
        """
        return self._Male

    @Male.setter
    def Male(self, Male):
        self._Male = Male

    @property
    def PersonId(self):
        """自定义人员 ID，注意不能使用 tci_person_ 前缀
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PhoneNumber(self):
        """人员电话号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def StudentNumber(self):
        """人员学生号码
        :rtype: str
        """
        return self._StudentNumber

    @StudentNumber.setter
    def StudentNumber(self, StudentNumber):
        self._StudentNumber = StudentNumber

    @property
    def Urls(self):
        """图片下载地址，与 Images 参数选择一个输入
        :rtype: list of str
        """
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._PersonName = params.get("PersonName")
        self._Images = params.get("Images")
        self._JobNumber = params.get("JobNumber")
        self._Mail = params.get("Mail")
        self._Male = params.get("Male")
        self._PersonId = params.get("PersonId")
        self._PhoneNumber = params.get("PhoneNumber")
        self._StudentNumber = params.get("StudentNumber")
        self._Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceInfoSet: 人脸操作结果信息
        :type FaceInfoSet: list of FaceInfo
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceInfoSet = None
        self._LibraryId = None
        self._PersonId = None
        self._PersonName = None
        self._RequestId = None

    @property
    def FaceInfoSet(self):
        """人脸操作结果信息
        :rtype: list of FaceInfo
        """
        return self._FaceInfoSet

    @FaceInfoSet.setter
    def FaceInfoSet(self, FaceInfoSet):
        self._FaceInfoSet = FaceInfoSet

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonName(self):
        """人员名称
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self._FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self._FaceInfoSet.append(obj)
        self._LibraryId = params.get("LibraryId")
        self._PersonId = params.get("PersonId")
        self._PersonName = params.get("PersonName")
        self._RequestId = params.get("RequestId")


class CreateVocabLibRequest(AbstractModel):
    """CreateVocabLib请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabLibName: 词汇库名称
        :type VocabLibName: str
        """
        self._VocabLibName = None

    @property
    def VocabLibName(self):
        """词汇库名称
        :rtype: str
        """
        return self._VocabLibName

    @VocabLibName.setter
    def VocabLibName(self, VocabLibName):
        self._VocabLibName = VocabLibName


    def _deserialize(self, params):
        self._VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVocabLibResponse(AbstractModel):
    """CreateVocabLib返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateVocabRequest(AbstractModel):
    """CreateVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabLibName: 要添加词汇的词汇库名
        :type VocabLibName: str
        :param _VocabList: 要添加的词汇列表
        :type VocabList: list of str
        """
        self._VocabLibName = None
        self._VocabList = None

    @property
    def VocabLibName(self):
        """要添加词汇的词汇库名
        :rtype: str
        """
        return self._VocabLibName

    @VocabLibName.setter
    def VocabLibName(self, VocabLibName):
        self._VocabLibName = VocabLibName

    @property
    def VocabList(self):
        """要添加的词汇列表
        :rtype: list of str
        """
        return self._VocabList

    @VocabList.setter
    def VocabList(self, VocabList):
        self._VocabList = VocabList


    def _deserialize(self, params):
        self._VocabLibName = params.get("VocabLibName")
        self._VocabList = params.get("VocabList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVocabResponse(AbstractModel):
    """CreateVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteFaceRequest(AbstractModel):
    """DeleteFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceIdSet: 人脸标识符数组
        :type FaceIdSet: list of str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        """
        self._FaceIdSet = None
        self._PersonId = None
        self._LibraryId = None

    @property
    def FaceIdSet(self):
        """人脸标识符数组
        :rtype: list of str
        """
        return self._FaceIdSet

    @FaceIdSet.setter
    def FaceIdSet(self, FaceIdSet):
        self._FaceIdSet = FaceIdSet

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId


    def _deserialize(self, params):
        self._FaceIdSet = params.get("FaceIdSet")
        self._PersonId = params.get("PersonId")
        self._LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFaceResponse(AbstractModel):
    """DeleteFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceInfoSet: 人脸操作结果
        :type FaceInfoSet: list of FaceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceInfoSet = None
        self._RequestId = None

    @property
    def FaceInfoSet(self):
        """人脸操作结果
        :rtype: list of FaceInfo
        """
        return self._FaceInfoSet

    @FaceInfoSet.setter
    def FaceInfoSet(self, FaceInfoSet):
        self._FaceInfoSet = FaceInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self._FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self._FaceInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteLibraryRequest(AbstractModel):
    """DeleteLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        """
        self._LibraryId = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLibraryResponse(AbstractModel):
    """DeleteLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _LibraryName: 人员库名称
        :type LibraryName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LibraryId = None
        self._LibraryName = None
        self._RequestId = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def LibraryName(self):
        """人员库名称
        :rtype: str
        """
        return self._LibraryName

    @LibraryName.setter
    def LibraryName(self, LibraryName):
        self._LibraryName = LibraryName

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._LibraryName = params.get("LibraryName")
        self._RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        """
        self._LibraryId = None
        self._PersonId = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceInfoSet: 人脸信息
        :type FaceInfoSet: list of FaceInfo
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceInfoSet = None
        self._LibraryId = None
        self._PersonId = None
        self._PersonName = None
        self._RequestId = None

    @property
    def FaceInfoSet(self):
        """人脸信息
        :rtype: list of FaceInfo
        """
        return self._FaceInfoSet

    @FaceInfoSet.setter
    def FaceInfoSet(self, FaceInfoSet):
        self._FaceInfoSet = FaceInfoSet

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonName(self):
        """人员名称
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self._FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self._FaceInfoSet.append(obj)
        self._LibraryId = params.get("LibraryId")
        self._PersonId = params.get("PersonId")
        self._PersonName = params.get("PersonName")
        self._RequestId = params.get("RequestId")


class DeleteVocabLibRequest(AbstractModel):
    """DeleteVocabLib请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabLibName: 词汇库名称
        :type VocabLibName: str
        """
        self._VocabLibName = None

    @property
    def VocabLibName(self):
        """词汇库名称
        :rtype: str
        """
        return self._VocabLibName

    @VocabLibName.setter
    def VocabLibName(self, VocabLibName):
        self._VocabLibName = VocabLibName


    def _deserialize(self, params):
        self._VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVocabLibResponse(AbstractModel):
    """DeleteVocabLib返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteVocabRequest(AbstractModel):
    """DeleteVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabLibName: 要删除词汇的词汇库名
        :type VocabLibName: str
        :param _VocabList: 要删除的词汇列表
        :type VocabList: list of str
        """
        self._VocabLibName = None
        self._VocabList = None

    @property
    def VocabLibName(self):
        """要删除词汇的词汇库名
        :rtype: str
        """
        return self._VocabLibName

    @VocabLibName.setter
    def VocabLibName(self, VocabLibName):
        self._VocabLibName = VocabLibName

    @property
    def VocabList(self):
        """要删除的词汇列表
        :rtype: list of str
        """
        return self._VocabList

    @VocabList.setter
    def VocabList(self, VocabList):
        self._VocabList = VocabList


    def _deserialize(self, params):
        self._VocabLibName = params.get("VocabLibName")
        self._VocabList = params.get("VocabList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVocabResponse(AbstractModel):
    """DeleteVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAITaskResultRequest(AbstractModel):
    """DescribeAITaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一标识符。在URL方式时提交请求后会返回一个任务标识符，后续查询该url的结果时使用这个标识符进行查询。
        :type TaskId: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None

    @property
    def TaskId(self):
        """任务唯一标识符。在URL方式时提交请求后会返回一个任务标识符，后续查询该url的结果时使用这个标识符进行查询。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAITaskResultResponse(AbstractModel):
    """DescribeAITaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AudioResult: 音频分析结果
        :type AudioResult: :class:`tencentcloud.tci.v20190318.models.StandardAudioResult`
        :param _ImageResult: 图像分析结果
        :type ImageResult: :class:`tencentcloud.tci.v20190318.models.StandardImageResult`
        :param _VideoResult: 视频分析结果
        :type VideoResult: :class:`tencentcloud.tci.v20190318.models.StandardVideoResult`
        :param _Status: 任务状态
        :type Status: str
        :param _TaskId: 任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AudioResult = None
        self._ImageResult = None
        self._VideoResult = None
        self._Status = None
        self._TaskId = None
        self._RequestId = None

    @property
    def AudioResult(self):
        """音频分析结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.StandardAudioResult`
        """
        return self._AudioResult

    @AudioResult.setter
    def AudioResult(self, AudioResult):
        self._AudioResult = AudioResult

    @property
    def ImageResult(self):
        """图像分析结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.StandardImageResult`
        """
        return self._ImageResult

    @ImageResult.setter
    def ImageResult(self, ImageResult):
        self._ImageResult = ImageResult

    @property
    def VideoResult(self):
        """视频分析结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.StandardVideoResult`
        """
        return self._VideoResult

    @VideoResult.setter
    def VideoResult(self, VideoResult):
        self._VideoResult = VideoResult

    @property
    def Status(self):
        """任务状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        """任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AudioResult") is not None:
            self._AudioResult = StandardAudioResult()
            self._AudioResult._deserialize(params.get("AudioResult"))
        if params.get("ImageResult") is not None:
            self._ImageResult = StandardImageResult()
            self._ImageResult._deserialize(params.get("ImageResult"))
        if params.get("VideoResult") is not None:
            self._VideoResult = StandardVideoResult()
            self._VideoResult._deserialize(params.get("VideoResult"))
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeAttendanceResultRequest(AbstractModel):
    """DescribeAttendanceResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务唯一标识符
        :type JobId: int
        """
        self._JobId = None

    @property
    def JobId(self):
        """任务唯一标识符
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttendanceResultResponse(AbstractModel):
    """DescribeAttendanceResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AbsenceSetInLibs: 缺失人员的ID列表(只针对请求中的libids字段)
        :type AbsenceSetInLibs: list of AbsenceInfo
        :param _AttendanceSet: 确定出勤人员列表
        :type AttendanceSet: list of AttendanceInfo
        :param _SuspectedSet: 疑似出勤人员列表
        :type SuspectedSet: list of SuspectedInfo
        :param _AbsenceSet: 缺失人员的ID列表(只针对请求中的personids字段)
        :type AbsenceSet: list of str
        :param _Progress: 请求处理进度
        :type Progress: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AbsenceSetInLibs = None
        self._AttendanceSet = None
        self._SuspectedSet = None
        self._AbsenceSet = None
        self._Progress = None
        self._RequestId = None

    @property
    def AbsenceSetInLibs(self):
        """缺失人员的ID列表(只针对请求中的libids字段)
        :rtype: list of AbsenceInfo
        """
        return self._AbsenceSetInLibs

    @AbsenceSetInLibs.setter
    def AbsenceSetInLibs(self, AbsenceSetInLibs):
        self._AbsenceSetInLibs = AbsenceSetInLibs

    @property
    def AttendanceSet(self):
        """确定出勤人员列表
        :rtype: list of AttendanceInfo
        """
        return self._AttendanceSet

    @AttendanceSet.setter
    def AttendanceSet(self, AttendanceSet):
        self._AttendanceSet = AttendanceSet

    @property
    def SuspectedSet(self):
        """疑似出勤人员列表
        :rtype: list of SuspectedInfo
        """
        return self._SuspectedSet

    @SuspectedSet.setter
    def SuspectedSet(self, SuspectedSet):
        self._SuspectedSet = SuspectedSet

    @property
    def AbsenceSet(self):
        """缺失人员的ID列表(只针对请求中的personids字段)
        :rtype: list of str
        """
        return self._AbsenceSet

    @AbsenceSet.setter
    def AbsenceSet(self, AbsenceSet):
        self._AbsenceSet = AbsenceSet

    @property
    def Progress(self):
        """请求处理进度
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AbsenceSetInLibs") is not None:
            self._AbsenceSetInLibs = []
            for item in params.get("AbsenceSetInLibs"):
                obj = AbsenceInfo()
                obj._deserialize(item)
                self._AbsenceSetInLibs.append(obj)
        if params.get("AttendanceSet") is not None:
            self._AttendanceSet = []
            for item in params.get("AttendanceSet"):
                obj = AttendanceInfo()
                obj._deserialize(item)
                self._AttendanceSet.append(obj)
        if params.get("SuspectedSet") is not None:
            self._SuspectedSet = []
            for item in params.get("SuspectedSet"):
                obj = SuspectedInfo()
                obj._deserialize(item)
                self._SuspectedSet.append(obj)
        self._AbsenceSet = params.get("AbsenceSet")
        self._Progress = params.get("Progress")
        self._RequestId = params.get("RequestId")


class DescribeAudioTaskRequest(AbstractModel):
    """DescribeAudioTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._JobId = None
        self._Limit = None
        self._Offset = None

    @property
    def JobId(self):
        """音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAudioTaskResponse(AbstractModel):
    """DescribeAudioTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllMuteSlice: 如果请求中开启了静音检测开关，则会返回所有的静音片段（静音时长超过阈值的片段）。
        :type AllMuteSlice: :class:`tencentcloud.tci.v20190318.models.AllMuteSlice`
        :param _AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param _Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :type Texts: list of WholeTextItem
        :param _VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param _VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param _AllTexts: 返回音频全部文本。
        :type AllTexts: str
        :param _JobId: 音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param _Progress: 返回的当前处理进度。
        :type Progress: float
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllMuteSlice = None
        self._AsrStat = None
        self._Texts = None
        self._VocabAnalysisDetailInfo = None
        self._VocabAnalysisStatInfo = None
        self._AllTexts = None
        self._JobId = None
        self._Progress = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AllMuteSlice(self):
        """如果请求中开启了静音检测开关，则会返回所有的静音片段（静音时长超过阈值的片段）。
        :rtype: :class:`tencentcloud.tci.v20190318.models.AllMuteSlice`
        """
        return self._AllMuteSlice

    @AllMuteSlice.setter
    def AllMuteSlice(self, AllMuteSlice):
        self._AllMuteSlice = AllMuteSlice

    @property
    def AsrStat(self):
        """返回的当前音频的统计信息。当进度为100时返回。
        :rtype: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        """
        return self._AsrStat

    @AsrStat.setter
    def AsrStat(self, AsrStat):
        self._AsrStat = AsrStat

    @property
    def Texts(self):
        """返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :rtype: list of WholeTextItem
        """
        return self._Texts

    @Texts.setter
    def Texts(self, Texts):
        self._Texts = Texts

    @property
    def VocabAnalysisDetailInfo(self):
        """返回词汇库中的单词出现的详细时间信息。
        :rtype: list of VocabDetailInfomation
        """
        return self._VocabAnalysisDetailInfo

    @VocabAnalysisDetailInfo.setter
    def VocabAnalysisDetailInfo(self, VocabAnalysisDetailInfo):
        self._VocabAnalysisDetailInfo = VocabAnalysisDetailInfo

    @property
    def VocabAnalysisStatInfo(self):
        """返回词汇库中的单词出现的次数信息。
        :rtype: list of VocabStatInfomation
        """
        return self._VocabAnalysisStatInfo

    @VocabAnalysisStatInfo.setter
    def VocabAnalysisStatInfo(self, VocabAnalysisStatInfo):
        self._VocabAnalysisStatInfo = VocabAnalysisStatInfo

    @property
    def AllTexts(self):
        """返回音频全部文本。
        :rtype: str
        """
        return self._AllTexts

    @AllTexts.setter
    def AllTexts(self, AllTexts):
        self._AllTexts = AllTexts

    @property
    def JobId(self):
        """音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Progress(self):
        """返回的当前处理进度。
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TotalCount(self):
        """结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AllMuteSlice") is not None:
            self._AllMuteSlice = AllMuteSlice()
            self._AllMuteSlice._deserialize(params.get("AllMuteSlice"))
        if params.get("AsrStat") is not None:
            self._AsrStat = ASRStat()
            self._AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self._Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self._Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self._VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self._VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self._VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self._VocabAnalysisStatInfo.append(obj)
        self._AllTexts = params.get("AllTexts")
        self._JobId = params.get("JobId")
        self._Progress = params.get("Progress")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConversationTaskRequest(AbstractModel):
    """DescribeConversationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param _Identity: 要查询明细的流的身份，1 老师 2 学生
        :type Identity: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._JobId = None
        self._Identity = None
        self._Limit = None
        self._Offset = None

    @property
    def JobId(self):
        """音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Identity(self):
        """要查询明细的流的身份，1 老师 2 学生
        :rtype: int
        """
        return self._Identity

    @Identity.setter
    def Identity(self, Identity):
        self._Identity = Identity

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Identity = params.get("Identity")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConversationTaskResponse(AbstractModel):
    """DescribeConversationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param _Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :type Texts: list of WholeTextItem
        :param _VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param _VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param _AllTexts: 整个音频流的全部文本
        :type AllTexts: str
        :param _JobId: 音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param _Progress: 返回的当前处理进度。
        :type Progress: float
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsrStat = None
        self._Texts = None
        self._VocabAnalysisDetailInfo = None
        self._VocabAnalysisStatInfo = None
        self._AllTexts = None
        self._JobId = None
        self._Progress = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AsrStat(self):
        """返回的当前音频的统计信息。当进度为100时返回。
        :rtype: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        """
        return self._AsrStat

    @AsrStat.setter
    def AsrStat(self, AsrStat):
        self._AsrStat = AsrStat

    @property
    def Texts(self):
        """返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :rtype: list of WholeTextItem
        """
        return self._Texts

    @Texts.setter
    def Texts(self, Texts):
        self._Texts = Texts

    @property
    def VocabAnalysisDetailInfo(self):
        """返回词汇库中的单词出现的详细时间信息。
        :rtype: list of VocabDetailInfomation
        """
        return self._VocabAnalysisDetailInfo

    @VocabAnalysisDetailInfo.setter
    def VocabAnalysisDetailInfo(self, VocabAnalysisDetailInfo):
        self._VocabAnalysisDetailInfo = VocabAnalysisDetailInfo

    @property
    def VocabAnalysisStatInfo(self):
        """返回词汇库中的单词出现的次数信息。
        :rtype: list of VocabStatInfomation
        """
        return self._VocabAnalysisStatInfo

    @VocabAnalysisStatInfo.setter
    def VocabAnalysisStatInfo(self, VocabAnalysisStatInfo):
        self._VocabAnalysisStatInfo = VocabAnalysisStatInfo

    @property
    def AllTexts(self):
        """整个音频流的全部文本
        :rtype: str
        """
        return self._AllTexts

    @AllTexts.setter
    def AllTexts(self, AllTexts):
        self._AllTexts = AllTexts

    @property
    def JobId(self):
        """音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Progress(self):
        """返回的当前处理进度。
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TotalCount(self):
        """结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self._AsrStat = ASRStat()
            self._AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self._Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self._Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self._VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self._VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self._VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self._VocabAnalysisStatInfo.append(obj)
        self._AllTexts = params.get("AllTexts")
        self._JobId = params.get("JobId")
        self._Progress = params.get("Progress")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHighlightResultRequest(AbstractModel):
    """DescribeHighlightResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 精彩集锦任务唯一id。在URL方式时提交请求后会返回一个JobId，后续查询该url的结果时使用这个JobId进行查询。
        :type JobId: int
        """
        self._JobId = None

    @property
    def JobId(self):
        """精彩集锦任务唯一id。在URL方式时提交请求后会返回一个JobId，后续查询该url的结果时使用这个JobId进行查询。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHighlightResultResponse(AbstractModel):
    """DescribeHighlightResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HighlightsInfo: 精彩集锦详细信息。
        :type HighlightsInfo: list of HighlightsInfomation
        :param _JobId: 精彩集锦任务唯一id。在URL方式时提交请求后会返回一个JobId，后续查询该url的结果时使用这个JobId进行查询。
        :type JobId: int
        :param _Progress: 任务的进度百分比，100表示任务已完成。
        :type Progress: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HighlightsInfo = None
        self._JobId = None
        self._Progress = None
        self._RequestId = None

    @property
    def HighlightsInfo(self):
        """精彩集锦详细信息。
        :rtype: list of HighlightsInfomation
        """
        return self._HighlightsInfo

    @HighlightsInfo.setter
    def HighlightsInfo(self, HighlightsInfo):
        self._HighlightsInfo = HighlightsInfo

    @property
    def JobId(self):
        """精彩集锦任务唯一id。在URL方式时提交请求后会返回一个JobId，后续查询该url的结果时使用这个JobId进行查询。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Progress(self):
        """任务的进度百分比，100表示任务已完成。
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HighlightsInfo") is not None:
            self._HighlightsInfo = []
            for item in params.get("HighlightsInfo"):
                obj = HighlightsInfomation()
                obj._deserialize(item)
                self._HighlightsInfo.append(obj)
        self._JobId = params.get("JobId")
        self._Progress = params.get("Progress")
        self._RequestId = params.get("RequestId")


class DescribeImageTaskRequest(AbstractModel):
    """DescribeImageTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务标识符
        :type JobId: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._JobId = None
        self._Limit = None
        self._Offset = None

    @property
    def JobId(self):
        """任务标识符
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageTaskResponse(AbstractModel):
    """DescribeImageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultSet: 任务处理结果
        :type ResultSet: list of ImageTaskResult
        :param _JobId: 任务唯一标识
        :type JobId: int
        :param _Progress: 任务执行进度
        :type Progress: int
        :param _TotalCount: 任务结果数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultSet = None
        self._JobId = None
        self._Progress = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ResultSet(self):
        """任务处理结果
        :rtype: list of ImageTaskResult
        """
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def JobId(self):
        """任务唯一标识
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Progress(self):
        """任务执行进度
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TotalCount(self):
        """任务结果数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self._ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ResultSet.append(obj)
        self._JobId = params.get("JobId")
        self._Progress = params.get("Progress")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeImageTaskStatisticRequest(AbstractModel):
    """DescribeImageTaskStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 图像任务标识符
        :type JobId: int
        """
        self._JobId = None

    @property
    def JobId(self):
        """图像任务标识符
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageTaskStatisticResponse(AbstractModel):
    """DescribeImageTaskStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Statistic: 任务统计信息
        :type Statistic: :class:`tencentcloud.tci.v20190318.models.ImageTaskStatistic`
        :param _JobId: 图像任务唯一标识符
        :type JobId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Statistic = None
        self._JobId = None
        self._RequestId = None

    @property
    def Statistic(self):
        """任务统计信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.ImageTaskStatistic`
        """
        return self._Statistic

    @Statistic.setter
    def Statistic(self, Statistic):
        self._Statistic = Statistic

    @property
    def JobId(self):
        """图像任务唯一标识符
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Statistic") is not None:
            self._Statistic = ImageTaskStatistic()
            self._Statistic._deserialize(params.get("Statistic"))
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class DescribeLibrariesRequest(AbstractModel):
    """DescribeLibraries请求参数结构体

    """


class DescribeLibrariesResponse(AbstractModel):
    """DescribeLibraries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LibrarySet: 人员库列表
        :type LibrarySet: list of Library
        :param _TotalCount: 人员库总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LibrarySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LibrarySet(self):
        """人员库列表
        :rtype: list of Library
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def TotalCount(self):
        """人员库总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LibrarySet") is not None:
            self._LibrarySet = []
            for item in params.get("LibrarySet"):
                obj = Library()
                obj._deserialize(item)
                self._LibrarySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePersonRequest(AbstractModel):
    """DescribePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        """
        self._LibraryId = None
        self._PersonId = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonResponse(AbstractModel):
    """DescribePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceSet: 人员人脸列表
        :type FaceSet: list of Face
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _JobNumber: 工作号码
        :type JobNumber: str
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _Mail: 邮箱
        :type Mail: str
        :param _Male: 性别
        :type Male: int
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _PhoneNumber: 电话号码
        :type PhoneNumber: str
        :param _StudentNumber: 学生号码
        :type StudentNumber: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceSet = None
        self._CreateTime = None
        self._JobNumber = None
        self._LibraryId = None
        self._Mail = None
        self._Male = None
        self._PersonId = None
        self._PersonName = None
        self._PhoneNumber = None
        self._StudentNumber = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def FaceSet(self):
        """人员人脸列表
        :rtype: list of Face
        """
        return self._FaceSet

    @FaceSet.setter
    def FaceSet(self, FaceSet):
        self._FaceSet = FaceSet

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def JobNumber(self):
        """工作号码
        :rtype: str
        """
        return self._JobNumber

    @JobNumber.setter
    def JobNumber(self, JobNumber):
        self._JobNumber = JobNumber

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Mail(self):
        """邮箱
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Male(self):
        """性别
        :rtype: int
        """
        return self._Male

    @Male.setter
    def Male(self, Male):
        self._Male = Male

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonName(self):
        """人员名称
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def PhoneNumber(self):
        """电话号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def StudentNumber(self):
        """学生号码
        :rtype: str
        """
        return self._StudentNumber

    @StudentNumber.setter
    def StudentNumber(self, StudentNumber):
        self._StudentNumber = StudentNumber

    @property
    def UpdateTime(self):
        """修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FaceSet") is not None:
            self._FaceSet = []
            for item in params.get("FaceSet"):
                obj = Face()
                obj._deserialize(item)
                self._FaceSet.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._JobNumber = params.get("JobNumber")
        self._LibraryId = params.get("LibraryId")
        self._Mail = params.get("Mail")
        self._Male = params.get("Male")
        self._PersonId = params.get("PersonId")
        self._PersonName = params.get("PersonName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._StudentNumber = params.get("StudentNumber")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class DescribePersonsRequest(AbstractModel):
    """DescribePersons请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _Limit: 限制数目
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._LibraryId = None
        self._Limit = None
        self._Offset = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonsResponse(AbstractModel):
    """DescribePersons返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonSet: 人员列表
        :type PersonSet: list of Person
        :param _TotalCount: 人员总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PersonSet(self):
        """人员列表
        :rtype: list of Person
        """
        return self._PersonSet

    @PersonSet.setter
    def PersonSet(self, PersonSet):
        self._PersonSet = PersonSet

    @property
    def TotalCount(self):
        """人员总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PersonSet") is not None:
            self._PersonSet = []
            for item in params.get("PersonSet"):
                obj = Person()
                obj._deserialize(item)
                self._PersonSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeVocabLibRequest(AbstractModel):
    """DescribeVocabLib请求参数结构体

    """


class DescribeVocabLibResponse(AbstractModel):
    """DescribeVocabLib返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabLibNameSet: 返回该appid下的所有词汇库名
        :type VocabLibNameSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabLibNameSet = None
        self._RequestId = None

    @property
    def VocabLibNameSet(self):
        """返回该appid下的所有词汇库名
        :rtype: list of str
        """
        return self._VocabLibNameSet

    @VocabLibNameSet.setter
    def VocabLibNameSet(self, VocabLibNameSet):
        self._VocabLibNameSet = VocabLibNameSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabLibNameSet = params.get("VocabLibNameSet")
        self._RequestId = params.get("RequestId")


class DescribeVocabRequest(AbstractModel):
    """DescribeVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabLibName: 要查询词汇的词汇库名
        :type VocabLibName: str
        """
        self._VocabLibName = None

    @property
    def VocabLibName(self):
        """要查询词汇的词汇库名
        :rtype: str
        """
        return self._VocabLibName

    @VocabLibName.setter
    def VocabLibName(self, VocabLibName):
        self._VocabLibName = VocabLibName


    def _deserialize(self, params):
        self._VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVocabResponse(AbstractModel):
    """DescribeVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabNameSet: 词汇列表
        :type VocabNameSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabNameSet = None
        self._RequestId = None

    @property
    def VocabNameSet(self):
        """词汇列表
        :rtype: list of str
        """
        return self._VocabNameSet

    @VocabNameSet.setter
    def VocabNameSet(self, VocabNameSet):
        self._VocabNameSet = VocabNameSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabNameSet = params.get("VocabNameSet")
        self._RequestId = params.get("RequestId")


class DetailInfo(AbstractModel):
    """单词出现的那个句子的起始时间和结束时间信息

    """

    def __init__(self):
        r"""
        :param _Value: 单词出现在该音频中的那个句子的时间戳，出现了几次， 就返回对应次数的起始和结束时间戳
        :type Value: list of WordTimePair
        :param _Keyword: 词汇库中的单词
        :type Keyword: str
        """
        self._Value = None
        self._Keyword = None

    @property
    def Value(self):
        """单词出现在该音频中的那个句子的时间戳，出现了几次， 就返回对应次数的起始和结束时间戳
        :rtype: list of WordTimePair
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Keyword(self):
        """词汇库中的单词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = WordTimePair()
                obj._deserialize(item)
                self._Value.append(obj)
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DoubleVideoFunction(AbstractModel):
    """双路混流视频集锦开关项

    """

    def __init__(self):
        r"""
        :param _EnableCoverPictures: 片头片尾增加图片开关
        :type EnableCoverPictures: bool
        """
        self._EnableCoverPictures = None

    @property
    def EnableCoverPictures(self):
        """片头片尾增加图片开关
        :rtype: bool
        """
        return self._EnableCoverPictures

    @EnableCoverPictures.setter
    def EnableCoverPictures(self, EnableCoverPictures):
        self._EnableCoverPictures = EnableCoverPictures


    def _deserialize(self, params):
        self._EnableCoverPictures = params.get("EnableCoverPictures")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpressRatioStatistic(AbstractModel):
    """表情比例统计

    """

    def __init__(self):
        r"""
        :param _Count: 出现次数
        :type Count: int
        :param _Express: 表情
        :type Express: str
        :param _Ratio: 该表情时长占所有表情时长的比例
        :type Ratio: float
        :param _RatioUseDuration: 该表情时长占视频总时长的比例
        :type RatioUseDuration: float
        """
        self._Count = None
        self._Express = None
        self._Ratio = None
        self._RatioUseDuration = None

    @property
    def Count(self):
        """出现次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Express(self):
        """表情
        :rtype: str
        """
        return self._Express

    @Express.setter
    def Express(self, Express):
        self._Express = Express

    @property
    def Ratio(self):
        """该表情时长占所有表情时长的比例
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def RatioUseDuration(self):
        """该表情时长占视频总时长的比例
        :rtype: float
        """
        return self._RatioUseDuration

    @RatioUseDuration.setter
    def RatioUseDuration(self, RatioUseDuration):
        self._RatioUseDuration = RatioUseDuration


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Express = params.get("Express")
        self._Ratio = params.get("Ratio")
        self._RatioUseDuration = params.get("RatioUseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Face(AbstractModel):
    """人脸描述

    """

    def __init__(self):
        r"""
        :param _FaceId: 人脸唯一标识符
        :type FaceId: str
        :param _FaceUrl: 人脸图片 URL
        :type FaceUrl: str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        """
        self._FaceId = None
        self._FaceUrl = None
        self._PersonId = None

    @property
    def FaceId(self):
        """人脸唯一标识符
        :rtype: str
        """
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def FaceUrl(self):
        """人脸图片 URL
        :rtype: str
        """
        return self._FaceUrl

    @FaceUrl.setter
    def FaceUrl(self, FaceUrl):
        self._FaceUrl = FaceUrl

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._FaceId = params.get("FaceId")
        self._FaceUrl = params.get("FaceUrl")
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceAttrResult(AbstractModel):
    """FaceAttrResult

    """

    def __init__(self):
        r"""
        :param _Age: 年龄
        :type Age: int
        :param _Sex: 性别
        :type Sex: str
        """
        self._Age = None
        self._Sex = None

    @property
    def Age(self):
        """年龄
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Sex(self):
        """性别
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex


    def _deserialize(self, params):
        self._Age = params.get("Age")
        self._Sex = params.get("Sex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceDetectStatistic(AbstractModel):
    """人脸监测统计信息

    """

    def __init__(self):
        r"""
        :param _FaceSizeRatio: 人脸大小占画面平均占比
        :type FaceSizeRatio: float
        :param _FrontalFaceCount: 检测到正脸次数
        :type FrontalFaceCount: int
        :param _FrontalFaceRatio: 正脸时长占比
        :type FrontalFaceRatio: float
        :param _FrontalFaceRealRatio: 正脸时长在总出现时常占比
        :type FrontalFaceRealRatio: float
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _SideFaceCount: 检测到侧脸次数
        :type SideFaceCount: int
        :param _SideFaceRatio: 侧脸时长占比
        :type SideFaceRatio: float
        :param _SideFaceRealRatio: 侧脸时长在总出现时常占比
        :type SideFaceRealRatio: float
        """
        self._FaceSizeRatio = None
        self._FrontalFaceCount = None
        self._FrontalFaceRatio = None
        self._FrontalFaceRealRatio = None
        self._PersonId = None
        self._SideFaceCount = None
        self._SideFaceRatio = None
        self._SideFaceRealRatio = None

    @property
    def FaceSizeRatio(self):
        """人脸大小占画面平均占比
        :rtype: float
        """
        return self._FaceSizeRatio

    @FaceSizeRatio.setter
    def FaceSizeRatio(self, FaceSizeRatio):
        self._FaceSizeRatio = FaceSizeRatio

    @property
    def FrontalFaceCount(self):
        """检测到正脸次数
        :rtype: int
        """
        return self._FrontalFaceCount

    @FrontalFaceCount.setter
    def FrontalFaceCount(self, FrontalFaceCount):
        self._FrontalFaceCount = FrontalFaceCount

    @property
    def FrontalFaceRatio(self):
        """正脸时长占比
        :rtype: float
        """
        return self._FrontalFaceRatio

    @FrontalFaceRatio.setter
    def FrontalFaceRatio(self, FrontalFaceRatio):
        self._FrontalFaceRatio = FrontalFaceRatio

    @property
    def FrontalFaceRealRatio(self):
        """正脸时长在总出现时常占比
        :rtype: float
        """
        return self._FrontalFaceRealRatio

    @FrontalFaceRealRatio.setter
    def FrontalFaceRealRatio(self, FrontalFaceRealRatio):
        self._FrontalFaceRealRatio = FrontalFaceRealRatio

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def SideFaceCount(self):
        """检测到侧脸次数
        :rtype: int
        """
        return self._SideFaceCount

    @SideFaceCount.setter
    def SideFaceCount(self, SideFaceCount):
        self._SideFaceCount = SideFaceCount

    @property
    def SideFaceRatio(self):
        """侧脸时长占比
        :rtype: float
        """
        return self._SideFaceRatio

    @SideFaceRatio.setter
    def SideFaceRatio(self, SideFaceRatio):
        self._SideFaceRatio = SideFaceRatio

    @property
    def SideFaceRealRatio(self):
        """侧脸时长在总出现时常占比
        :rtype: float
        """
        return self._SideFaceRealRatio

    @SideFaceRealRatio.setter
    def SideFaceRealRatio(self, SideFaceRealRatio):
        self._SideFaceRealRatio = SideFaceRealRatio


    def _deserialize(self, params):
        self._FaceSizeRatio = params.get("FaceSizeRatio")
        self._FrontalFaceCount = params.get("FrontalFaceCount")
        self._FrontalFaceRatio = params.get("FrontalFaceRatio")
        self._FrontalFaceRealRatio = params.get("FrontalFaceRealRatio")
        self._PersonId = params.get("PersonId")
        self._SideFaceCount = params.get("SideFaceCount")
        self._SideFaceRatio = params.get("SideFaceRatio")
        self._SideFaceRealRatio = params.get("SideFaceRealRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceExpressStatistic(AbstractModel):
    """人脸表情统计结果

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _ExpressRatio: 表情统计结果
        :type ExpressRatio: list of ExpressRatioStatistic
        """
        self._PersonId = None
        self._ExpressRatio = None

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def ExpressRatio(self):
        """表情统计结果
        :rtype: list of ExpressRatioStatistic
        """
        return self._ExpressRatio

    @ExpressRatio.setter
    def ExpressRatio(self, ExpressRatio):
        self._ExpressRatio = ExpressRatio


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        if params.get("ExpressRatio") is not None:
            self._ExpressRatio = []
            for item in params.get("ExpressRatio"):
                obj = ExpressRatioStatistic()
                obj._deserialize(item)
                self._ExpressRatio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceExpressionResult(AbstractModel):
    """FaceExpressionResult

    """

    def __init__(self):
        r"""
        :param _Confidence: 表情置信度
        :type Confidence: float
        :param _Expression: 表情识别结果，包括"neutral":中性,"happiness":开心，"angry":"生气"，"disgust":厌恶，"fear":"恐惧"，"sadness":"悲伤"，"surprise":"惊讶"，"contempt":"蔑视"
        :type Expression: str
        """
        self._Confidence = None
        self._Expression = None

    @property
    def Confidence(self):
        """表情置信度
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Expression(self):
        """表情识别结果，包括"neutral":中性,"happiness":开心，"angry":"生气"，"disgust":厌恶，"fear":"恐惧"，"sadness":"悲伤"，"surprise":"惊讶"，"contempt":"蔑视"
        :rtype: str
        """
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceIdentifyResult(AbstractModel):
    """FaceIdentifyResult

    """

    def __init__(self):
        r"""
        :param _FaceId: 人脸标识符
        :type FaceId: str
        :param _LibraryId: 人员库标识符
        :type LibraryId: str
        :param _PersonId: 人员标识符
        :type PersonId: str
        :param _Similarity: 相似度
        :type Similarity: float
        """
        self._FaceId = None
        self._LibraryId = None
        self._PersonId = None
        self._Similarity = None

    @property
    def FaceId(self):
        """人脸标识符
        :rtype: str
        """
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def LibraryId(self):
        """人员库标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonId(self):
        """人员标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Similarity(self):
        """相似度
        :rtype: float
        """
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity


    def _deserialize(self, params):
        self._FaceId = params.get("FaceId")
        self._LibraryId = params.get("LibraryId")
        self._PersonId = params.get("PersonId")
        self._Similarity = params.get("Similarity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceIdentifyStatistic(AbstractModel):
    """人员检索统计结果

    """

    def __init__(self):
        r"""
        :param _Duration: 持续时间
        :type Duration: int
        :param _EndTs: 结束时间
        :type EndTs: int
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _Similarity: 相似度
        :type Similarity: float
        :param _StartTs: 开始时间
        :type StartTs: int
        """
        self._Duration = None
        self._EndTs = None
        self._PersonId = None
        self._Similarity = None
        self._StartTs = None

    @property
    def Duration(self):
        """持续时间
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def EndTs(self):
        """结束时间
        :rtype: int
        """
        return self._EndTs

    @EndTs.setter
    def EndTs(self, EndTs):
        self._EndTs = EndTs

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Similarity(self):
        """相似度
        :rtype: float
        """
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def StartTs(self):
        """开始时间
        :rtype: int
        """
        return self._StartTs

    @StartTs.setter
    def StartTs(self, StartTs):
        self._StartTs = StartTs


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._EndTs = params.get("EndTs")
        self._PersonId = params.get("PersonId")
        self._Similarity = params.get("Similarity")
        self._StartTs = params.get("StartTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceInfo(AbstractModel):
    """人脸操作信息

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 人脸操作错误码
        :type ErrorCode: str
        :param _ErrorMsg: 人脸操作结果信息
        :type ErrorMsg: str
        :param _FaceId: 人脸唯一标识符
        :type FaceId: str
        :param _FaceUrl: 人脸保存地址
        :type FaceUrl: str
        :param _PersonId: 人员唯一标识
        :type PersonId: str
        """
        self._ErrorCode = None
        self._ErrorMsg = None
        self._FaceId = None
        self._FaceUrl = None
        self._PersonId = None

    @property
    def ErrorCode(self):
        """人脸操作错误码
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        """人脸操作结果信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def FaceId(self):
        """人脸唯一标识符
        :rtype: str
        """
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def FaceUrl(self):
        """人脸保存地址
        :rtype: str
        """
        return self._FaceUrl

    @FaceUrl.setter
    def FaceUrl(self, FaceUrl):
        self._FaceUrl = FaceUrl

    @property
    def PersonId(self):
        """人员唯一标识
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        self._FaceId = params.get("FaceId")
        self._FaceUrl = params.get("FaceUrl")
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceInfoResult(AbstractModel):
    """FaceInfoResult

    """

    def __init__(self):
        r"""
        :param _FaceRatio: 人脸尺寸的占比
        :type FaceRatio: float
        :param _FrameHeight: 帧高度
        :type FrameHeight: int
        :param _FrameWidth: 帧宽度
        :type FrameWidth: int
        :param _Height: 人脸高度
        :type Height: int
        :param _Left: 人脸左坐标
        :type Left: int
        :param _Top: 人脸顶坐标
        :type Top: int
        :param _Width: 人脸宽度
        :type Width: int
        """
        self._FaceRatio = None
        self._FrameHeight = None
        self._FrameWidth = None
        self._Height = None
        self._Left = None
        self._Top = None
        self._Width = None

    @property
    def FaceRatio(self):
        """人脸尺寸的占比
        :rtype: float
        """
        return self._FaceRatio

    @FaceRatio.setter
    def FaceRatio(self, FaceRatio):
        self._FaceRatio = FaceRatio

    @property
    def FrameHeight(self):
        """帧高度
        :rtype: int
        """
        return self._FrameHeight

    @FrameHeight.setter
    def FrameHeight(self, FrameHeight):
        self._FrameHeight = FrameHeight

    @property
    def FrameWidth(self):
        """帧宽度
        :rtype: int
        """
        return self._FrameWidth

    @FrameWidth.setter
    def FrameWidth(self, FrameWidth):
        self._FrameWidth = FrameWidth

    @property
    def Height(self):
        """人脸高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Left(self):
        """人脸左坐标
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Top(self):
        """人脸顶坐标
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Width(self):
        """人脸宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width


    def _deserialize(self, params):
        self._FaceRatio = params.get("FaceRatio")
        self._FrameHeight = params.get("FrameHeight")
        self._FrameWidth = params.get("FrameWidth")
        self._Height = params.get("Height")
        self._Left = params.get("Left")
        self._Top = params.get("Top")
        self._Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FacePoseResult(AbstractModel):
    """FacePoseResult

    """

    def __init__(self):
        r"""
        :param _Direction: 正脸或侧脸的消息
        :type Direction: str
        :param _Pitch: 围绕Z轴旋转角度，俯仰角
        :type Pitch: float
        :param _Roll: 围绕X轴旋转角度，翻滚角
        :type Roll: float
        :param _Yaw: 围绕Y轴旋转角度，偏航角
        :type Yaw: float
        """
        self._Direction = None
        self._Pitch = None
        self._Roll = None
        self._Yaw = None

    @property
    def Direction(self):
        """正脸或侧脸的消息
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Pitch(self):
        """围绕Z轴旋转角度，俯仰角
        :rtype: float
        """
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch

    @property
    def Roll(self):
        """围绕X轴旋转角度，翻滚角
        :rtype: float
        """
        return self._Roll

    @Roll.setter
    def Roll(self, Roll):
        self._Roll = Roll

    @property
    def Yaw(self):
        """围绕Y轴旋转角度，偏航角
        :rtype: float
        """
        return self._Yaw

    @Yaw.setter
    def Yaw(self, Yaw):
        self._Yaw = Yaw


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._Pitch = params.get("Pitch")
        self._Roll = params.get("Roll")
        self._Yaw = params.get("Yaw")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameInfo(AbstractModel):
    """人员信息

    """

    def __init__(self):
        r"""
        :param _Similarity: 相似度
        :type Similarity: float
        :param _SnapshotUrl: 截图的存储地址
        :type SnapshotUrl: str
        :param _Ts: 相对于视频起始时间的时间戳，单位秒
        :type Ts: int
        """
        self._Similarity = None
        self._SnapshotUrl = None
        self._Ts = None

    @property
    def Similarity(self):
        """相似度
        :rtype: float
        """
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def SnapshotUrl(self):
        """截图的存储地址
        :rtype: str
        """
        return self._SnapshotUrl

    @SnapshotUrl.setter
    def SnapshotUrl(self, SnapshotUrl):
        self._SnapshotUrl = SnapshotUrl

    @property
    def Ts(self):
        """相对于视频起始时间的时间戳，单位秒
        :rtype: int
        """
        return self._Ts

    @Ts.setter
    def Ts(self, Ts):
        self._Ts = Ts


    def _deserialize(self, params):
        self._Similarity = params.get("Similarity")
        self._SnapshotUrl = params.get("SnapshotUrl")
        self._Ts = params.get("Ts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Function(AbstractModel):
    """功能开关列表，表示是否需要打开相应的功能，返回相应的信息

    """

    def __init__(self):
        r"""
        :param _EnableAllText: 输出全部文本标识，当该值设置为true时，会输出当前音频的全部文本
        :type EnableAllText: bool
        :param _EnableKeyword: 输出关键词信息标识，当该值设置为true时，会输出当前音频的关键词信息。
        :type EnableKeyword: bool
        :param _EnableMuteDetect: 静音检测标识，当设置为 true 时，需要设置静音时间阈值字段mute_threshold，统计结果中会返回静音片段。
        :type EnableMuteDetect: bool
        :param _EnableVadInfo: 输出音频统计信息标识，当设置为 true 时，任务查询结果会输出音频的统计信息（AsrStat）
        :type EnableVadInfo: bool
        :param _EnableVolume: 输出音频音量信息标识，当设置为 true 时，会输出当前音频音量信息。
        :type EnableVolume: bool
        """
        self._EnableAllText = None
        self._EnableKeyword = None
        self._EnableMuteDetect = None
        self._EnableVadInfo = None
        self._EnableVolume = None

    @property
    def EnableAllText(self):
        """输出全部文本标识，当该值设置为true时，会输出当前音频的全部文本
        :rtype: bool
        """
        return self._EnableAllText

    @EnableAllText.setter
    def EnableAllText(self, EnableAllText):
        self._EnableAllText = EnableAllText

    @property
    def EnableKeyword(self):
        """输出关键词信息标识，当该值设置为true时，会输出当前音频的关键词信息。
        :rtype: bool
        """
        return self._EnableKeyword

    @EnableKeyword.setter
    def EnableKeyword(self, EnableKeyword):
        self._EnableKeyword = EnableKeyword

    @property
    def EnableMuteDetect(self):
        """静音检测标识，当设置为 true 时，需要设置静音时间阈值字段mute_threshold，统计结果中会返回静音片段。
        :rtype: bool
        """
        return self._EnableMuteDetect

    @EnableMuteDetect.setter
    def EnableMuteDetect(self, EnableMuteDetect):
        self._EnableMuteDetect = EnableMuteDetect

    @property
    def EnableVadInfo(self):
        """输出音频统计信息标识，当设置为 true 时，任务查询结果会输出音频的统计信息（AsrStat）
        :rtype: bool
        """
        return self._EnableVadInfo

    @EnableVadInfo.setter
    def EnableVadInfo(self, EnableVadInfo):
        self._EnableVadInfo = EnableVadInfo

    @property
    def EnableVolume(self):
        """输出音频音量信息标识，当设置为 true 时，会输出当前音频音量信息。
        :rtype: bool
        """
        return self._EnableVolume

    @EnableVolume.setter
    def EnableVolume(self, EnableVolume):
        self._EnableVolume = EnableVolume


    def _deserialize(self, params):
        self._EnableAllText = params.get("EnableAllText")
        self._EnableKeyword = params.get("EnableKeyword")
        self._EnableMuteDetect = params.get("EnableMuteDetect")
        self._EnableVadInfo = params.get("EnableVadInfo")
        self._EnableVolume = params.get("EnableVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GestureResult(AbstractModel):
    """GestureResult

    """

    def __init__(self):
        r"""
        :param _Class: 识别结果，包含"USPEAK":听你说，"LISTEN":听我说，"GOOD":GOOD，"TOOLS":拿教具，"OTHERS":其他
        :type Class: str
        :param _Confidence: 置信度
        :type Confidence: float
        :param _Height: 识别结果高度
        :type Height: int
        :param _Left: 识别结果左坐标
        :type Left: int
        :param _Top: 识别结果顶坐标
        :type Top: int
        :param _Width: 识别结果宽度
        :type Width: int
        """
        self._Class = None
        self._Confidence = None
        self._Height = None
        self._Left = None
        self._Top = None
        self._Width = None

    @property
    def Class(self):
        """识别结果，包含"USPEAK":听你说，"LISTEN":听我说，"GOOD":GOOD，"TOOLS":拿教具，"OTHERS":其他
        :rtype: str
        """
        return self._Class

    @Class.setter
    def Class(self, Class):
        self._Class = Class

    @property
    def Confidence(self):
        """置信度
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Height(self):
        """识别结果高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Left(self):
        """识别结果左坐标
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Top(self):
        """识别结果顶坐标
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Width(self):
        """识别结果宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width


    def _deserialize(self, params):
        self._Class = params.get("Class")
        self._Confidence = params.get("Confidence")
        self._Height = params.get("Height")
        self._Left = params.get("Left")
        self._Top = params.get("Top")
        self._Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HLFunction(AbstractModel):
    """检索配置开关项

    """

    def __init__(self):
        r"""
        :param _EnableFaceDetect: 是否开启人脸检测
        :type EnableFaceDetect: bool
        :param _EnableFaceExpression: 是否开启表情识别
        :type EnableFaceExpression: bool
        :param _EnableFaceIdent: 是否开启人脸检索
        :type EnableFaceIdent: bool
        :param _EnableKeywordWonderfulTime: 是否开启视频集锦-老师关键字识别
        :type EnableKeywordWonderfulTime: bool
        :param _EnableSmileWonderfulTime: 是否开启视频集锦-微笑识别
        :type EnableSmileWonderfulTime: bool
        """
        self._EnableFaceDetect = None
        self._EnableFaceExpression = None
        self._EnableFaceIdent = None
        self._EnableKeywordWonderfulTime = None
        self._EnableSmileWonderfulTime = None

    @property
    def EnableFaceDetect(self):
        """是否开启人脸检测
        :rtype: bool
        """
        return self._EnableFaceDetect

    @EnableFaceDetect.setter
    def EnableFaceDetect(self, EnableFaceDetect):
        self._EnableFaceDetect = EnableFaceDetect

    @property
    def EnableFaceExpression(self):
        """是否开启表情识别
        :rtype: bool
        """
        return self._EnableFaceExpression

    @EnableFaceExpression.setter
    def EnableFaceExpression(self, EnableFaceExpression):
        self._EnableFaceExpression = EnableFaceExpression

    @property
    def EnableFaceIdent(self):
        """是否开启人脸检索
        :rtype: bool
        """
        return self._EnableFaceIdent

    @EnableFaceIdent.setter
    def EnableFaceIdent(self, EnableFaceIdent):
        self._EnableFaceIdent = EnableFaceIdent

    @property
    def EnableKeywordWonderfulTime(self):
        """是否开启视频集锦-老师关键字识别
        :rtype: bool
        """
        return self._EnableKeywordWonderfulTime

    @EnableKeywordWonderfulTime.setter
    def EnableKeywordWonderfulTime(self, EnableKeywordWonderfulTime):
        self._EnableKeywordWonderfulTime = EnableKeywordWonderfulTime

    @property
    def EnableSmileWonderfulTime(self):
        """是否开启视频集锦-微笑识别
        :rtype: bool
        """
        return self._EnableSmileWonderfulTime

    @EnableSmileWonderfulTime.setter
    def EnableSmileWonderfulTime(self, EnableSmileWonderfulTime):
        self._EnableSmileWonderfulTime = EnableSmileWonderfulTime


    def _deserialize(self, params):
        self._EnableFaceDetect = params.get("EnableFaceDetect")
        self._EnableFaceExpression = params.get("EnableFaceExpression")
        self._EnableFaceIdent = params.get("EnableFaceIdent")
        self._EnableKeywordWonderfulTime = params.get("EnableKeywordWonderfulTime")
        self._EnableSmileWonderfulTime = params.get("EnableSmileWonderfulTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandTrackingResult(AbstractModel):
    """HandTrackingResult

    """

    def __init__(self):
        r"""
        :param _Class: 识别结果
        :type Class: str
        :param _Confidence: 置信度
        :type Confidence: float
        :param _Height: 识别结果高度
        :type Height: int
        :param _Left: 识别结果左坐标
        :type Left: int
        :param _Top: 识别结果顶坐标
        :type Top: int
        :param _Width: 识别结果宽度
        :type Width: int
        """
        self._Class = None
        self._Confidence = None
        self._Height = None
        self._Left = None
        self._Top = None
        self._Width = None

    @property
    def Class(self):
        """识别结果
        :rtype: str
        """
        return self._Class

    @Class.setter
    def Class(self, Class):
        self._Class = Class

    @property
    def Confidence(self):
        """置信度
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Height(self):
        """识别结果高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Left(self):
        """识别结果左坐标
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Top(self):
        """识别结果顶坐标
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Width(self):
        """识别结果宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width


    def _deserialize(self, params):
        self._Class = params.get("Class")
        self._Confidence = params.get("Confidence")
        self._Height = params.get("Height")
        self._Left = params.get("Left")
        self._Top = params.get("Top")
        self._Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsInfomation(AbstractModel):
    """精彩集锦信息

    """

    def __init__(self):
        r"""
        :param _Concentration: 专注的起始与终止时间信息。
        :type Concentration: list of TimeType
        :param _Smile: 微笑的起始与终止时间信息。
        :type Smile: list of TimeType
        :param _HighlightsUrl: 高光集锦视频地址，保存剪辑好的视频地址。
        :type HighlightsUrl: str
        :param _PersonId: 片段中识别出来的人脸ID。
        :type PersonId: str
        """
        self._Concentration = None
        self._Smile = None
        self._HighlightsUrl = None
        self._PersonId = None

    @property
    def Concentration(self):
        """专注的起始与终止时间信息。
        :rtype: list of TimeType
        """
        return self._Concentration

    @Concentration.setter
    def Concentration(self, Concentration):
        self._Concentration = Concentration

    @property
    def Smile(self):
        """微笑的起始与终止时间信息。
        :rtype: list of TimeType
        """
        return self._Smile

    @Smile.setter
    def Smile(self, Smile):
        self._Smile = Smile

    @property
    def HighlightsUrl(self):
        """高光集锦视频地址，保存剪辑好的视频地址。
        :rtype: str
        """
        return self._HighlightsUrl

    @HighlightsUrl.setter
    def HighlightsUrl(self, HighlightsUrl):
        self._HighlightsUrl = HighlightsUrl

    @property
    def PersonId(self):
        """片段中识别出来的人脸ID。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        if params.get("Concentration") is not None:
            self._Concentration = []
            for item in params.get("Concentration"):
                obj = TimeType()
                obj._deserialize(item)
                self._Concentration.append(obj)
        if params.get("Smile") is not None:
            self._Smile = []
            for item in params.get("Smile"):
                obj = TimeType()
                obj._deserialize(item)
                self._Smile.append(obj)
        self._HighlightsUrl = params.get("HighlightsUrl")
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTaskFunction(AbstractModel):
    """图像任务控制选项

    """

    def __init__(self):
        r"""
        :param _EnableActionClass: 大教室场景学生肢体动作识别选项
        :type EnableActionClass: bool
        :param _EnableFaceDetect: 人脸检测选项（默认为true，目前不可编辑）
        :type EnableFaceDetect: bool
        :param _EnableFaceExpression: 人脸表情识别选项
        :type EnableFaceExpression: bool
        :param _EnableFaceIdentify: 人脸检索选项（默认为true，目前不可编辑）
        :type EnableFaceIdentify: bool
        :param _EnableGesture: 手势选项
        :type EnableGesture: bool
        :param _EnableHandTracking: 优图手势选项（该功能尚未支持）
        :type EnableHandTracking: bool
        :param _EnableLightJudge: 光照选项
        :type EnableLightJudge: bool
        :param _EnableStudentBodyMovements: 小班课场景学生肢体动作识别选项
        :type EnableStudentBodyMovements: bool
        :param _EnableTeacherBodyMovements: 教师动作选项（该功能尚未支持）
        :type EnableTeacherBodyMovements: bool
        :param _EnableTeacherOutScreen: 判断老师是否在屏幕中（该功能尚未支持）
        :type EnableTeacherOutScreen: bool
        """
        self._EnableActionClass = None
        self._EnableFaceDetect = None
        self._EnableFaceExpression = None
        self._EnableFaceIdentify = None
        self._EnableGesture = None
        self._EnableHandTracking = None
        self._EnableLightJudge = None
        self._EnableStudentBodyMovements = None
        self._EnableTeacherBodyMovements = None
        self._EnableTeacherOutScreen = None

    @property
    def EnableActionClass(self):
        """大教室场景学生肢体动作识别选项
        :rtype: bool
        """
        return self._EnableActionClass

    @EnableActionClass.setter
    def EnableActionClass(self, EnableActionClass):
        self._EnableActionClass = EnableActionClass

    @property
    def EnableFaceDetect(self):
        """人脸检测选项（默认为true，目前不可编辑）
        :rtype: bool
        """
        return self._EnableFaceDetect

    @EnableFaceDetect.setter
    def EnableFaceDetect(self, EnableFaceDetect):
        self._EnableFaceDetect = EnableFaceDetect

    @property
    def EnableFaceExpression(self):
        """人脸表情识别选项
        :rtype: bool
        """
        return self._EnableFaceExpression

    @EnableFaceExpression.setter
    def EnableFaceExpression(self, EnableFaceExpression):
        self._EnableFaceExpression = EnableFaceExpression

    @property
    def EnableFaceIdentify(self):
        """人脸检索选项（默认为true，目前不可编辑）
        :rtype: bool
        """
        return self._EnableFaceIdentify

    @EnableFaceIdentify.setter
    def EnableFaceIdentify(self, EnableFaceIdentify):
        self._EnableFaceIdentify = EnableFaceIdentify

    @property
    def EnableGesture(self):
        """手势选项
        :rtype: bool
        """
        return self._EnableGesture

    @EnableGesture.setter
    def EnableGesture(self, EnableGesture):
        self._EnableGesture = EnableGesture

    @property
    def EnableHandTracking(self):
        """优图手势选项（该功能尚未支持）
        :rtype: bool
        """
        return self._EnableHandTracking

    @EnableHandTracking.setter
    def EnableHandTracking(self, EnableHandTracking):
        self._EnableHandTracking = EnableHandTracking

    @property
    def EnableLightJudge(self):
        """光照选项
        :rtype: bool
        """
        return self._EnableLightJudge

    @EnableLightJudge.setter
    def EnableLightJudge(self, EnableLightJudge):
        self._EnableLightJudge = EnableLightJudge

    @property
    def EnableStudentBodyMovements(self):
        """小班课场景学生肢体动作识别选项
        :rtype: bool
        """
        return self._EnableStudentBodyMovements

    @EnableStudentBodyMovements.setter
    def EnableStudentBodyMovements(self, EnableStudentBodyMovements):
        self._EnableStudentBodyMovements = EnableStudentBodyMovements

    @property
    def EnableTeacherBodyMovements(self):
        """教师动作选项（该功能尚未支持）
        :rtype: bool
        """
        return self._EnableTeacherBodyMovements

    @EnableTeacherBodyMovements.setter
    def EnableTeacherBodyMovements(self, EnableTeacherBodyMovements):
        self._EnableTeacherBodyMovements = EnableTeacherBodyMovements

    @property
    def EnableTeacherOutScreen(self):
        """判断老师是否在屏幕中（该功能尚未支持）
        :rtype: bool
        """
        return self._EnableTeacherOutScreen

    @EnableTeacherOutScreen.setter
    def EnableTeacherOutScreen(self, EnableTeacherOutScreen):
        self._EnableTeacherOutScreen = EnableTeacherOutScreen


    def _deserialize(self, params):
        self._EnableActionClass = params.get("EnableActionClass")
        self._EnableFaceDetect = params.get("EnableFaceDetect")
        self._EnableFaceExpression = params.get("EnableFaceExpression")
        self._EnableFaceIdentify = params.get("EnableFaceIdentify")
        self._EnableGesture = params.get("EnableGesture")
        self._EnableHandTracking = params.get("EnableHandTracking")
        self._EnableLightJudge = params.get("EnableLightJudge")
        self._EnableStudentBodyMovements = params.get("EnableStudentBodyMovements")
        self._EnableTeacherBodyMovements = params.get("EnableTeacherBodyMovements")
        self._EnableTeacherOutScreen = params.get("EnableTeacherOutScreen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTaskResult(AbstractModel):
    """图像任务结果

    """

    def __init__(self):
        r"""
        :param _ActionInfo: 大教室场景学生肢体动作识别信息
        :type ActionInfo: :class:`tencentcloud.tci.v20190318.models.ActionInfo`
        :param _FaceAttr: 属性识别结果
        :type FaceAttr: :class:`tencentcloud.tci.v20190318.models.FaceAttrResult`
        :param _FaceExpression: 表情识别结果
        :type FaceExpression: :class:`tencentcloud.tci.v20190318.models.FaceExpressionResult`
        :param _FaceIdentify: 人脸检索结果
        :type FaceIdentify: :class:`tencentcloud.tci.v20190318.models.FaceIdentifyResult`
        :param _FaceInfo: 人脸检测结果
        :type FaceInfo: :class:`tencentcloud.tci.v20190318.models.FaceInfoResult`
        :param _FacePose: 姿势识别结果
        :type FacePose: :class:`tencentcloud.tci.v20190318.models.FacePoseResult`
        :param _Gesture: 动作分类结果
        :type Gesture: :class:`tencentcloud.tci.v20190318.models.GestureResult`
        :param _HandTracking: 手势分类结果
        :type HandTracking: :class:`tencentcloud.tci.v20190318.models.HandTrackingResult`
        :param _Light: 光照识别结果
        :type Light: :class:`tencentcloud.tci.v20190318.models.LightResult`
        :param _StudentBodyMovement: 学生肢体动作识别结果
        :type StudentBodyMovement: :class:`tencentcloud.tci.v20190318.models.StudentBodyMovementResult`
        :param _TeacherBodyMovement: 老师肢体动作识别结果
        :type TeacherBodyMovement: :class:`tencentcloud.tci.v20190318.models.BodyMovementResult`
        :param _TeacherOutScreen: 教师是否在屏幕内判断结果
        :type TeacherOutScreen: :class:`tencentcloud.tci.v20190318.models.TeacherOutScreenResult`
        :param _TimeInfo: 时间统计结果
        :type TimeInfo: :class:`tencentcloud.tci.v20190318.models.TimeInfoResult`
        """
        self._ActionInfo = None
        self._FaceAttr = None
        self._FaceExpression = None
        self._FaceIdentify = None
        self._FaceInfo = None
        self._FacePose = None
        self._Gesture = None
        self._HandTracking = None
        self._Light = None
        self._StudentBodyMovement = None
        self._TeacherBodyMovement = None
        self._TeacherOutScreen = None
        self._TimeInfo = None

    @property
    def ActionInfo(self):
        """大教室场景学生肢体动作识别信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionInfo`
        """
        return self._ActionInfo

    @ActionInfo.setter
    def ActionInfo(self, ActionInfo):
        self._ActionInfo = ActionInfo

    @property
    def FaceAttr(self):
        """属性识别结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.FaceAttrResult`
        """
        return self._FaceAttr

    @FaceAttr.setter
    def FaceAttr(self, FaceAttr):
        self._FaceAttr = FaceAttr

    @property
    def FaceExpression(self):
        """表情识别结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.FaceExpressionResult`
        """
        return self._FaceExpression

    @FaceExpression.setter
    def FaceExpression(self, FaceExpression):
        self._FaceExpression = FaceExpression

    @property
    def FaceIdentify(self):
        """人脸检索结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.FaceIdentifyResult`
        """
        return self._FaceIdentify

    @FaceIdentify.setter
    def FaceIdentify(self, FaceIdentify):
        self._FaceIdentify = FaceIdentify

    @property
    def FaceInfo(self):
        """人脸检测结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.FaceInfoResult`
        """
        return self._FaceInfo

    @FaceInfo.setter
    def FaceInfo(self, FaceInfo):
        self._FaceInfo = FaceInfo

    @property
    def FacePose(self):
        """姿势识别结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.FacePoseResult`
        """
        return self._FacePose

    @FacePose.setter
    def FacePose(self, FacePose):
        self._FacePose = FacePose

    @property
    def Gesture(self):
        """动作分类结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.GestureResult`
        """
        return self._Gesture

    @Gesture.setter
    def Gesture(self, Gesture):
        self._Gesture = Gesture

    @property
    def HandTracking(self):
        """手势分类结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.HandTrackingResult`
        """
        return self._HandTracking

    @HandTracking.setter
    def HandTracking(self, HandTracking):
        self._HandTracking = HandTracking

    @property
    def Light(self):
        """光照识别结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.LightResult`
        """
        return self._Light

    @Light.setter
    def Light(self, Light):
        self._Light = Light

    @property
    def StudentBodyMovement(self):
        """学生肢体动作识别结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.StudentBodyMovementResult`
        """
        return self._StudentBodyMovement

    @StudentBodyMovement.setter
    def StudentBodyMovement(self, StudentBodyMovement):
        self._StudentBodyMovement = StudentBodyMovement

    @property
    def TeacherBodyMovement(self):
        """老师肢体动作识别结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.BodyMovementResult`
        """
        return self._TeacherBodyMovement

    @TeacherBodyMovement.setter
    def TeacherBodyMovement(self, TeacherBodyMovement):
        self._TeacherBodyMovement = TeacherBodyMovement

    @property
    def TeacherOutScreen(self):
        """教师是否在屏幕内判断结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.TeacherOutScreenResult`
        """
        return self._TeacherOutScreen

    @TeacherOutScreen.setter
    def TeacherOutScreen(self, TeacherOutScreen):
        self._TeacherOutScreen = TeacherOutScreen

    @property
    def TimeInfo(self):
        """时间统计结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.TimeInfoResult`
        """
        return self._TimeInfo

    @TimeInfo.setter
    def TimeInfo(self, TimeInfo):
        self._TimeInfo = TimeInfo


    def _deserialize(self, params):
        if params.get("ActionInfo") is not None:
            self._ActionInfo = ActionInfo()
            self._ActionInfo._deserialize(params.get("ActionInfo"))
        if params.get("FaceAttr") is not None:
            self._FaceAttr = FaceAttrResult()
            self._FaceAttr._deserialize(params.get("FaceAttr"))
        if params.get("FaceExpression") is not None:
            self._FaceExpression = FaceExpressionResult()
            self._FaceExpression._deserialize(params.get("FaceExpression"))
        if params.get("FaceIdentify") is not None:
            self._FaceIdentify = FaceIdentifyResult()
            self._FaceIdentify._deserialize(params.get("FaceIdentify"))
        if params.get("FaceInfo") is not None:
            self._FaceInfo = FaceInfoResult()
            self._FaceInfo._deserialize(params.get("FaceInfo"))
        if params.get("FacePose") is not None:
            self._FacePose = FacePoseResult()
            self._FacePose._deserialize(params.get("FacePose"))
        if params.get("Gesture") is not None:
            self._Gesture = GestureResult()
            self._Gesture._deserialize(params.get("Gesture"))
        if params.get("HandTracking") is not None:
            self._HandTracking = HandTrackingResult()
            self._HandTracking._deserialize(params.get("HandTracking"))
        if params.get("Light") is not None:
            self._Light = LightResult()
            self._Light._deserialize(params.get("Light"))
        if params.get("StudentBodyMovement") is not None:
            self._StudentBodyMovement = StudentBodyMovementResult()
            self._StudentBodyMovement._deserialize(params.get("StudentBodyMovement"))
        if params.get("TeacherBodyMovement") is not None:
            self._TeacherBodyMovement = BodyMovementResult()
            self._TeacherBodyMovement._deserialize(params.get("TeacherBodyMovement"))
        if params.get("TeacherOutScreen") is not None:
            self._TeacherOutScreen = TeacherOutScreenResult()
            self._TeacherOutScreen._deserialize(params.get("TeacherOutScreen"))
        if params.get("TimeInfo") is not None:
            self._TimeInfo = TimeInfoResult()
            self._TimeInfo._deserialize(params.get("TimeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTaskStatistic(AbstractModel):
    """图像任务统计结果

    """

    def __init__(self):
        r"""
        :param _FaceDetect: 人员检测统计信息
        :type FaceDetect: list of FaceDetectStatistic
        :param _FaceExpression: 人脸表情统计信息
        :type FaceExpression: list of FaceExpressStatistic
        :param _FaceIdentify: 人脸检索统计信息
        :type FaceIdentify: list of FaceIdentifyStatistic
        :param _Gesture: 姿势识别统计信息
        :type Gesture: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param _Handtracking: 手势识别统计信息
        :type Handtracking: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param _Light: 光照统计信息
        :type Light: :class:`tencentcloud.tci.v20190318.models.LightStatistic`
        :param _StudentMovement: 学生动作统计信息
        :type StudentMovement: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param _TeacherMovement: 教师动作统计信息
        :type TeacherMovement: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        """
        self._FaceDetect = None
        self._FaceExpression = None
        self._FaceIdentify = None
        self._Gesture = None
        self._Handtracking = None
        self._Light = None
        self._StudentMovement = None
        self._TeacherMovement = None

    @property
    def FaceDetect(self):
        """人员检测统计信息
        :rtype: list of FaceDetectStatistic
        """
        return self._FaceDetect

    @FaceDetect.setter
    def FaceDetect(self, FaceDetect):
        self._FaceDetect = FaceDetect

    @property
    def FaceExpression(self):
        """人脸表情统计信息
        :rtype: list of FaceExpressStatistic
        """
        return self._FaceExpression

    @FaceExpression.setter
    def FaceExpression(self, FaceExpression):
        self._FaceExpression = FaceExpression

    @property
    def FaceIdentify(self):
        """人脸检索统计信息
        :rtype: list of FaceIdentifyStatistic
        """
        return self._FaceIdentify

    @FaceIdentify.setter
    def FaceIdentify(self, FaceIdentify):
        self._FaceIdentify = FaceIdentify

    @property
    def Gesture(self):
        """姿势识别统计信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        """
        return self._Gesture

    @Gesture.setter
    def Gesture(self, Gesture):
        self._Gesture = Gesture

    @property
    def Handtracking(self):
        """手势识别统计信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        """
        return self._Handtracking

    @Handtracking.setter
    def Handtracking(self, Handtracking):
        self._Handtracking = Handtracking

    @property
    def Light(self):
        """光照统计信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.LightStatistic`
        """
        return self._Light

    @Light.setter
    def Light(self, Light):
        self._Light = Light

    @property
    def StudentMovement(self):
        """学生动作统计信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        """
        return self._StudentMovement

    @StudentMovement.setter
    def StudentMovement(self, StudentMovement):
        self._StudentMovement = StudentMovement

    @property
    def TeacherMovement(self):
        """教师动作统计信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        """
        return self._TeacherMovement

    @TeacherMovement.setter
    def TeacherMovement(self, TeacherMovement):
        self._TeacherMovement = TeacherMovement


    def _deserialize(self, params):
        if params.get("FaceDetect") is not None:
            self._FaceDetect = []
            for item in params.get("FaceDetect"):
                obj = FaceDetectStatistic()
                obj._deserialize(item)
                self._FaceDetect.append(obj)
        if params.get("FaceExpression") is not None:
            self._FaceExpression = []
            for item in params.get("FaceExpression"):
                obj = FaceExpressStatistic()
                obj._deserialize(item)
                self._FaceExpression.append(obj)
        if params.get("FaceIdentify") is not None:
            self._FaceIdentify = []
            for item in params.get("FaceIdentify"):
                obj = FaceIdentifyStatistic()
                obj._deserialize(item)
                self._FaceIdentify.append(obj)
        if params.get("Gesture") is not None:
            self._Gesture = ActionStatistic()
            self._Gesture._deserialize(params.get("Gesture"))
        if params.get("Handtracking") is not None:
            self._Handtracking = ActionStatistic()
            self._Handtracking._deserialize(params.get("Handtracking"))
        if params.get("Light") is not None:
            self._Light = LightStatistic()
            self._Light._deserialize(params.get("Light"))
        if params.get("StudentMovement") is not None:
            self._StudentMovement = ActionStatistic()
            self._StudentMovement._deserialize(params.get("StudentMovement"))
        if params.get("TeacherMovement") is not None:
            self._TeacherMovement = ActionStatistic()
            self._TeacherMovement._deserialize(params.get("TeacherMovement"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Library(AbstractModel):
    """人员库描述

    """

    def __init__(self):
        r"""
        :param _CreateTime: 人员库创建时间
        :type CreateTime: str
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _LibraryName: 人员库名称
        :type LibraryName: str
        :param _PersonCount: 人员库人员数量
        :type PersonCount: int
        :param _UpdateTime: 人员库修改时间
        :type UpdateTime: str
        """
        self._CreateTime = None
        self._LibraryId = None
        self._LibraryName = None
        self._PersonCount = None
        self._UpdateTime = None

    @property
    def CreateTime(self):
        """人员库创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def LibraryName(self):
        """人员库名称
        :rtype: str
        """
        return self._LibraryName

    @LibraryName.setter
    def LibraryName(self, LibraryName):
        self._LibraryName = LibraryName

    @property
    def PersonCount(self):
        """人员库人员数量
        :rtype: int
        """
        return self._PersonCount

    @PersonCount.setter
    def PersonCount(self, PersonCount):
        self._PersonCount = PersonCount

    @property
    def UpdateTime(self):
        """人员库修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._LibraryId = params.get("LibraryId")
        self._LibraryName = params.get("LibraryName")
        self._PersonCount = params.get("PersonCount")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LightDistributionStatistic(AbstractModel):
    """光照强度统计结果

    """

    def __init__(self):
        r"""
        :param _Time: 时间点
        :type Time: int
        :param _Value: 光线值
        :type Value: int
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        """时间点
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """光线值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LightLevelRatioStatistic(AbstractModel):
    """光照强度比例统计结果

    """

    def __init__(self):
        r"""
        :param _Level: 名称
        :type Level: str
        :param _Ratio: 比例
        :type Ratio: float
        """
        self._Level = None
        self._Ratio = None

    @property
    def Level(self):
        """名称
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Ratio(self):
        """比例
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LightResult(AbstractModel):
    """LightResult

    """

    def __init__(self):
        r"""
        :param _LightLevel: 光照程度，参考提交任务时的LightStandard指定的Name参数
        :type LightLevel: str
        :param _LightValue: 光照亮度
        :type LightValue: float
        """
        self._LightLevel = None
        self._LightValue = None

    @property
    def LightLevel(self):
        """光照程度，参考提交任务时的LightStandard指定的Name参数
        :rtype: str
        """
        return self._LightLevel

    @LightLevel.setter
    def LightLevel(self, LightLevel):
        self._LightLevel = LightLevel

    @property
    def LightValue(self):
        """光照亮度
        :rtype: float
        """
        return self._LightValue

    @LightValue.setter
    def LightValue(self, LightValue):
        self._LightValue = LightValue


    def _deserialize(self, params):
        self._LightLevel = params.get("LightLevel")
        self._LightValue = params.get("LightValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LightStandard(AbstractModel):
    """光照标准，结构的相关示例为：
    {
        "Name":"dark"，
        "Range":[0,30]
    }
    当光照的区间落入在0到30的范围时，就会命中dark的光照标准

    """

    def __init__(self):
        r"""
        :param _Name: 光照名称
        :type Name: str
        :param _Range: 范围
        :type Range: list of float
        """
        self._Name = None
        self._Range = None

    @property
    def Name(self):
        """光照名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Range(self):
        """范围
        :rtype: list of float
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LightStatistic(AbstractModel):
    """光照统计结果

    """

    def __init__(self):
        r"""
        :param _LightDistribution: 各个时间点的光线值
        :type LightDistribution: list of LightDistributionStatistic
        :param _LightLevelRatio: 光照程度比例统计结果
        :type LightLevelRatio: list of LightLevelRatioStatistic
        """
        self._LightDistribution = None
        self._LightLevelRatio = None

    @property
    def LightDistribution(self):
        """各个时间点的光线值
        :rtype: list of LightDistributionStatistic
        """
        return self._LightDistribution

    @LightDistribution.setter
    def LightDistribution(self, LightDistribution):
        self._LightDistribution = LightDistribution

    @property
    def LightLevelRatio(self):
        """光照程度比例统计结果
        :rtype: list of LightLevelRatioStatistic
        """
        return self._LightLevelRatio

    @LightLevelRatio.setter
    def LightLevelRatio(self, LightLevelRatio):
        self._LightLevelRatio = LightLevelRatio


    def _deserialize(self, params):
        if params.get("LightDistribution") is not None:
            self._LightDistribution = []
            for item in params.get("LightDistribution"):
                obj = LightDistributionStatistic()
                obj._deserialize(item)
                self._LightDistribution.append(obj)
        if params.get("LightLevelRatio") is not None:
            self._LightLevelRatio = []
            for item in params.get("LightLevelRatio"):
                obj = LightLevelRatioStatistic()
                obj._deserialize(item)
                self._LightLevelRatio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLibraryRequest(AbstractModel):
    """ModifyLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _LibraryName: 人员库名称
        :type LibraryName: str
        """
        self._LibraryId = None
        self._LibraryName = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def LibraryName(self):
        """人员库名称
        :rtype: str
        """
        return self._LibraryName

    @LibraryName.setter
    def LibraryName(self, LibraryName):
        self._LibraryName = LibraryName


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._LibraryName = params.get("LibraryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLibraryResponse(AbstractModel):
    """ModifyLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _LibraryName: 人员库名称
        :type LibraryName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LibraryId = None
        self._LibraryName = None
        self._RequestId = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def LibraryName(self):
        """人员库名称
        :rtype: str
        """
        return self._LibraryName

    @LibraryName.setter
    def LibraryName(self, LibraryName):
        self._LibraryName = LibraryName

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._LibraryName = params.get("LibraryName")
        self._RequestId = params.get("RequestId")


class ModifyPersonRequest(AbstractModel):
    """ModifyPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _JobNumber: 人员工作号码
        :type JobNumber: str
        :param _Mail: 人员邮箱
        :type Mail: str
        :param _Male: 人员性别
        :type Male: int
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _PhoneNumber: 人员电话号码
        :type PhoneNumber: str
        :param _StudentNumber: 人员学生号码
        :type StudentNumber: str
        """
        self._LibraryId = None
        self._PersonId = None
        self._JobNumber = None
        self._Mail = None
        self._Male = None
        self._PersonName = None
        self._PhoneNumber = None
        self._StudentNumber = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def JobNumber(self):
        """人员工作号码
        :rtype: str
        """
        return self._JobNumber

    @JobNumber.setter
    def JobNumber(self, JobNumber):
        self._JobNumber = JobNumber

    @property
    def Mail(self):
        """人员邮箱
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Male(self):
        """人员性别
        :rtype: int
        """
        return self._Male

    @Male.setter
    def Male(self, Male):
        self._Male = Male

    @property
    def PersonName(self):
        """人员名称
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def PhoneNumber(self):
        """人员电话号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def StudentNumber(self):
        """人员学生号码
        :rtype: str
        """
        return self._StudentNumber

    @StudentNumber.setter
    def StudentNumber(self, StudentNumber):
        self._StudentNumber = StudentNumber


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._PersonId = params.get("PersonId")
        self._JobNumber = params.get("JobNumber")
        self._Mail = params.get("Mail")
        self._Male = params.get("Male")
        self._PersonName = params.get("PersonName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._StudentNumber = params.get("StudentNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonResponse(AbstractModel):
    """ModifyPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceInfoSet: 人脸信息
        :type FaceInfoSet: list of FaceInfo
        :param _LibraryId: 人员所属人员库标识符
        :type LibraryId: str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceInfoSet = None
        self._LibraryId = None
        self._PersonId = None
        self._PersonName = None
        self._RequestId = None

    @property
    def FaceInfoSet(self):
        """人脸信息
        :rtype: list of FaceInfo
        """
        return self._FaceInfoSet

    @FaceInfoSet.setter
    def FaceInfoSet(self, FaceInfoSet):
        self._FaceInfoSet = FaceInfoSet

    @property
    def LibraryId(self):
        """人员所属人员库标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonName(self):
        """人员名称
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self._FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self._FaceInfoSet.append(obj)
        self._LibraryId = params.get("LibraryId")
        self._PersonId = params.get("PersonId")
        self._PersonName = params.get("PersonName")
        self._RequestId = params.get("RequestId")


class MuteSlice(AbstractModel):
    """所有静音片段。

    """

    def __init__(self):
        r"""
        :param _MuteBtm: 起始时间。
        :type MuteBtm: int
        :param _MuteEtm: 终止时间。
        :type MuteEtm: int
        """
        self._MuteBtm = None
        self._MuteEtm = None

    @property
    def MuteBtm(self):
        """起始时间。
        :rtype: int
        """
        return self._MuteBtm

    @MuteBtm.setter
    def MuteBtm(self, MuteBtm):
        self._MuteBtm = MuteBtm

    @property
    def MuteEtm(self):
        """终止时间。
        :rtype: int
        """
        return self._MuteEtm

    @MuteEtm.setter
    def MuteEtm(self, MuteEtm):
        self._MuteEtm = MuteEtm


    def _deserialize(self, params):
        self._MuteBtm = params.get("MuteBtm")
        self._MuteEtm = params.get("MuteEtm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Person(AbstractModel):
    """人员描述

    """

    def __init__(self):
        r"""
        :param _LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param _PersonId: 人员唯一标识符
        :type PersonId: str
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _JobNumber: 工作号码
        :type JobNumber: str
        :param _Mail: 邮箱
        :type Mail: str
        :param _Male: 性别
        :type Male: int
        :param _PhoneNumber: 电话号码
        :type PhoneNumber: str
        :param _StudentNumber: 学生号码
        :type StudentNumber: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self._LibraryId = None
        self._PersonId = None
        self._PersonName = None
        self._CreateTime = None
        self._JobNumber = None
        self._Mail = None
        self._Male = None
        self._PhoneNumber = None
        self._StudentNumber = None
        self._UpdateTime = None

    @property
    def LibraryId(self):
        """人员库唯一标识符
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def PersonId(self):
        """人员唯一标识符
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonName(self):
        """人员名称
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def JobNumber(self):
        """工作号码
        :rtype: str
        """
        return self._JobNumber

    @JobNumber.setter
    def JobNumber(self, JobNumber):
        self._JobNumber = JobNumber

    @property
    def Mail(self):
        """邮箱
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Male(self):
        """性别
        :rtype: int
        """
        return self._Male

    @Male.setter
    def Male(self, Male):
        self._Male = Male

    @property
    def PhoneNumber(self):
        """电话号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def StudentNumber(self):
        """学生号码
        :rtype: str
        """
        return self._StudentNumber

    @StudentNumber.setter
    def StudentNumber(self, StudentNumber):
        self._StudentNumber = StudentNumber

    @property
    def UpdateTime(self):
        """修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._PersonId = params.get("PersonId")
        self._PersonName = params.get("PersonName")
        self._CreateTime = params.get("CreateTime")
        self._JobNumber = params.get("JobNumber")
        self._Mail = params.get("Mail")
        self._Male = params.get("Male")
        self._PhoneNumber = params.get("PhoneNumber")
        self._StudentNumber = params.get("StudentNumber")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    """人员信息

    """

    def __init__(self):
        r"""
        :param _PersonId: 需要匹配的人员的ID列表。
        :type PersonId: str
        :param _CoverBeginUrl: 视频集锦开始封面照片。
        :type CoverBeginUrl: str
        :param _CoverEndUrl: 视频集锦结束封面照片。
        :type CoverEndUrl: str
        """
        self._PersonId = None
        self._CoverBeginUrl = None
        self._CoverEndUrl = None

    @property
    def PersonId(self):
        """需要匹配的人员的ID列表。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def CoverBeginUrl(self):
        """视频集锦开始封面照片。
        :rtype: str
        """
        return self._CoverBeginUrl

    @CoverBeginUrl.setter
    def CoverBeginUrl(self, CoverBeginUrl):
        self._CoverBeginUrl = CoverBeginUrl

    @property
    def CoverEndUrl(self):
        """视频集锦结束封面照片。
        :rtype: str
        """
        return self._CoverEndUrl

    @CoverEndUrl.setter
    def CoverEndUrl(self, CoverEndUrl):
        self._CoverEndUrl = CoverEndUrl


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._CoverBeginUrl = params.get("CoverBeginUrl")
        self._CoverEndUrl = params.get("CoverEndUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardAudioResult(AbstractModel):
    """标准化接口图像分析结果

    """

    def __init__(self):
        r"""
        :param _AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param _Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :type Texts: list of WholeTextItem
        :param _VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param _VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param _Message: 状态描述
        :type Message: str
        :param _Status: 任务状态
        :type Status: str
        :param _TotalCount: 结果数量
        :type TotalCount: int
        """
        self._AsrStat = None
        self._Texts = None
        self._VocabAnalysisDetailInfo = None
        self._VocabAnalysisStatInfo = None
        self._Message = None
        self._Status = None
        self._TotalCount = None

    @property
    def AsrStat(self):
        """返回的当前音频的统计信息。当进度为100时返回。
        :rtype: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        """
        return self._AsrStat

    @AsrStat.setter
    def AsrStat(self, AsrStat):
        self._AsrStat = AsrStat

    @property
    def Texts(self):
        """返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :rtype: list of WholeTextItem
        """
        return self._Texts

    @Texts.setter
    def Texts(self, Texts):
        self._Texts = Texts

    @property
    def VocabAnalysisDetailInfo(self):
        """返回词汇库中的单词出现的详细时间信息。
        :rtype: list of VocabDetailInfomation
        """
        return self._VocabAnalysisDetailInfo

    @VocabAnalysisDetailInfo.setter
    def VocabAnalysisDetailInfo(self, VocabAnalysisDetailInfo):
        self._VocabAnalysisDetailInfo = VocabAnalysisDetailInfo

    @property
    def VocabAnalysisStatInfo(self):
        """返回词汇库中的单词出现的次数信息。
        :rtype: list of VocabStatInfomation
        """
        return self._VocabAnalysisStatInfo

    @VocabAnalysisStatInfo.setter
    def VocabAnalysisStatInfo(self, VocabAnalysisStatInfo):
        self._VocabAnalysisStatInfo = VocabAnalysisStatInfo

    @property
    def Message(self):
        """状态描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Status(self):
        """任务状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalCount(self):
        """结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self._AsrStat = ASRStat()
            self._AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self._Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self._Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self._VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self._VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self._VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self._VocabAnalysisStatInfo.append(obj)
        self._Message = params.get("Message")
        self._Status = params.get("Status")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardImageResult(AbstractModel):
    """标准化接口图像分析结果

    """

    def __init__(self):
        r"""
        :param _ResultSet: 详细结果
        :type ResultSet: list of ImageTaskResult
        :param _Statistic: 分析完成后的统计结果
        :type Statistic: :class:`tencentcloud.tci.v20190318.models.ImageTaskStatistic`
        :param _Message: 状态描述
        :type Message: str
        :param _Status: 任务状态
        :type Status: str
        :param _TotalCount: 结果总数
        :type TotalCount: int
        """
        self._ResultSet = None
        self._Statistic = None
        self._Message = None
        self._Status = None
        self._TotalCount = None

    @property
    def ResultSet(self):
        """详细结果
        :rtype: list of ImageTaskResult
        """
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def Statistic(self):
        """分析完成后的统计结果
        :rtype: :class:`tencentcloud.tci.v20190318.models.ImageTaskStatistic`
        """
        return self._Statistic

    @Statistic.setter
    def Statistic(self, Statistic):
        self._Statistic = Statistic

    @property
    def Message(self):
        """状态描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Status(self):
        """任务状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalCount(self):
        """结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self._ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ResultSet.append(obj)
        if params.get("Statistic") is not None:
            self._Statistic = ImageTaskStatistic()
            self._Statistic._deserialize(params.get("Statistic"))
        self._Message = params.get("Message")
        self._Status = params.get("Status")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardVideoResult(AbstractModel):
    """标准化接口图像分析结果

    """

    def __init__(self):
        r"""
        :param _HighlightsInfo: 分析完成后的统计结果
        :type HighlightsInfo: list of HighlightsInfomation
        :param _Message: 状态描述
        :type Message: str
        :param _Status: 任务状态
        :type Status: str
        """
        self._HighlightsInfo = None
        self._Message = None
        self._Status = None

    @property
    def HighlightsInfo(self):
        """分析完成后的统计结果
        :rtype: list of HighlightsInfomation
        """
        return self._HighlightsInfo

    @HighlightsInfo.setter
    def HighlightsInfo(self, HighlightsInfo):
        self._HighlightsInfo = HighlightsInfo

    @property
    def Message(self):
        """状态描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Status(self):
        """任务状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("HighlightsInfo") is not None:
            self._HighlightsInfo = []
            for item in params.get("HighlightsInfo"):
                obj = HighlightsInfomation()
                obj._deserialize(item)
                self._HighlightsInfo.append(obj)
        self._Message = params.get("Message")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatInfo(AbstractModel):
    """单词出现的次数信息

    """

    def __init__(self):
        r"""
        :param _Keyword: 词汇库中的单词
        :type Keyword: str
        :param _Value: 单词出现在该音频中总次数
        :type Value: int
        """
        self._Keyword = None
        self._Value = None

    @property
    def Keyword(self):
        """词汇库中的单词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Value(self):
        """单词出现在该音频中总次数
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StudentBodyMovementResult(AbstractModel):
    """学生肢体动作结果

    """

    def __init__(self):
        r"""
        :param _Confidence: 置信度（已废弃）
        :type Confidence: float
        :param _HandupConfidence: 举手识别结果置信度
        :type HandupConfidence: float
        :param _HandupStatus: 举手识别结果，包含举手（handup）和未举手（nothandup）
        :type HandupStatus: str
        :param _Height: 识别结果高度
        :type Height: int
        :param _Left: 识别结果左坐标
        :type Left: int
        :param _Movements: 动作识别结果（已废弃）
        :type Movements: str
        :param _StandConfidence: 站立识别结果置信度
        :type StandConfidence: float
        :param _StandStatus: 站立识别结果，包含站立（stand）和坐着（sit）
        :type StandStatus: str
        :param _Top: 识别结果顶坐标
        :type Top: int
        :param _Width: 识别结果宽度
        :type Width: int
        """
        self._Confidence = None
        self._HandupConfidence = None
        self._HandupStatus = None
        self._Height = None
        self._Left = None
        self._Movements = None
        self._StandConfidence = None
        self._StandStatus = None
        self._Top = None
        self._Width = None

    @property
    def Confidence(self):
        """置信度（已废弃）
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def HandupConfidence(self):
        """举手识别结果置信度
        :rtype: float
        """
        return self._HandupConfidence

    @HandupConfidence.setter
    def HandupConfidence(self, HandupConfidence):
        self._HandupConfidence = HandupConfidence

    @property
    def HandupStatus(self):
        """举手识别结果，包含举手（handup）和未举手（nothandup）
        :rtype: str
        """
        return self._HandupStatus

    @HandupStatus.setter
    def HandupStatus(self, HandupStatus):
        self._HandupStatus = HandupStatus

    @property
    def Height(self):
        """识别结果高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Left(self):
        """识别结果左坐标
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Movements(self):
        """动作识别结果（已废弃）
        :rtype: str
        """
        return self._Movements

    @Movements.setter
    def Movements(self, Movements):
        self._Movements = Movements

    @property
    def StandConfidence(self):
        """站立识别结果置信度
        :rtype: float
        """
        return self._StandConfidence

    @StandConfidence.setter
    def StandConfidence(self, StandConfidence):
        self._StandConfidence = StandConfidence

    @property
    def StandStatus(self):
        """站立识别结果，包含站立（stand）和坐着（sit）
        :rtype: str
        """
        return self._StandStatus

    @StandStatus.setter
    def StandStatus(self, StandStatus):
        self._StandStatus = StandStatus

    @property
    def Top(self):
        """识别结果顶坐标
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Width(self):
        """识别结果宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._HandupConfidence = params.get("HandupConfidence")
        self._HandupStatus = params.get("HandupStatus")
        self._Height = params.get("Height")
        self._Left = params.get("Left")
        self._Movements = params.get("Movements")
        self._StandConfidence = params.get("StandConfidence")
        self._StandStatus = params.get("StandStatus")
        self._Top = params.get("Top")
        self._Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAudioTaskRequest(AbstractModel):
    """SubmitAudioTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param _Url: 音频URL。客户请求为URL方式时必须带此字段指名音频的url。
        :type Url: str
        :param _VoiceEncodeType: 语音编码类型 1:pcm
        :type VoiceEncodeType: int
        :param _VoiceFileType: 语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）
        :type VoiceFileType: int
        :param _Functions: 功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param _FileType: 视频文件类型，默认点播，直播填 live_url
        :type FileType: str
        :param _MuteThreshold: 静音阈值设置，如果静音检测开关开启，则静音时间超过这个阈值认为是静音片段，在结果中会返回, 没给的话默认值为3s
        :type MuteThreshold: int
        :param _VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :type VocabLibNameList: list of str
        """
        self._Lang = None
        self._Url = None
        self._VoiceEncodeType = None
        self._VoiceFileType = None
        self._Functions = None
        self._FileType = None
        self._MuteThreshold = None
        self._VocabLibNameList = None

    @property
    def Lang(self):
        """音频源的语言，默认0为英文，1为中文
        :rtype: int
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def Url(self):
        """音频URL。客户请求为URL方式时必须带此字段指名音频的url。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def VoiceEncodeType(self):
        """语音编码类型 1:pcm
        :rtype: int
        """
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def VoiceFileType(self):
        """语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）
        :rtype: int
        """
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType

    @property
    def Functions(self):
        """功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.Function`
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def FileType(self):
        """视频文件类型，默认点播，直播填 live_url
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def MuteThreshold(self):
        """静音阈值设置，如果静音检测开关开启，则静音时间超过这个阈值认为是静音片段，在结果中会返回, 没给的话默认值为3s
        :rtype: int
        """
        return self._MuteThreshold

    @MuteThreshold.setter
    def MuteThreshold(self, MuteThreshold):
        self._MuteThreshold = MuteThreshold

    @property
    def VocabLibNameList(self):
        """识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :rtype: list of str
        """
        return self._VocabLibNameList

    @VocabLibNameList.setter
    def VocabLibNameList(self, VocabLibNameList):
        self._VocabLibNameList = VocabLibNameList


    def _deserialize(self, params):
        self._Lang = params.get("Lang")
        self._Url = params.get("Url")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._VoiceFileType = params.get("VoiceFileType")
        if params.get("Functions") is not None:
            self._Functions = Function()
            self._Functions._deserialize(params.get("Functions"))
        self._FileType = params.get("FileType")
        self._MuteThreshold = params.get("MuteThreshold")
        self._VocabLibNameList = params.get("VocabLibNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAudioTaskResponse(AbstractModel):
    """SubmitAudioTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 	查询结果时指名的jobid。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """	查询结果时指名的jobid。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitCheckAttendanceTaskPlusRequest(AbstractModel):
    """SubmitCheckAttendanceTaskPlus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入数据
        :type FileContent: list of str
        :param _FileType: 视频流类型，vod_url表示点播URL，live_url表示直播URL，默认vod_url
        :type FileType: str
        :param _LibraryIds: 人员库 ID列表
        :type LibraryIds: list of str
        :param _AttendanceThreshold: 确定出勤阈值；默认为0.92
        :type AttendanceThreshold: float
        :param _EnableStranger: 是否开启陌生人模式，陌生人模式是指在任务中发现的非注册人脸库中的人脸也返回相关统计信息，默认不开启
        :type EnableStranger: bool
        :param _EndTime: 考勤结束时间（到视频的第几秒结束考勤），单位秒；默认为900 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间往后12小时
        :type EndTime: int
        :param _NoticeUrl: 通知回调地址，要求方法为post，application/json格式
        :type NoticeUrl: str
        :param _StartTime: 考勤开始时间（从视频的第几秒开始考勤），单位秒；默认为0 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间
        :type StartTime: int
        :param _Threshold: 识别阈值；默认为0.8
        :type Threshold: float
        """
        self._FileContent = None
        self._FileType = None
        self._LibraryIds = None
        self._AttendanceThreshold = None
        self._EnableStranger = None
        self._EndTime = None
        self._NoticeUrl = None
        self._StartTime = None
        self._Threshold = None

    @property
    def FileContent(self):
        """输入数据
        :rtype: list of str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """视频流类型，vod_url表示点播URL，live_url表示直播URL，默认vod_url
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def LibraryIds(self):
        """人员库 ID列表
        :rtype: list of str
        """
        return self._LibraryIds

    @LibraryIds.setter
    def LibraryIds(self, LibraryIds):
        self._LibraryIds = LibraryIds

    @property
    def AttendanceThreshold(self):
        """确定出勤阈值；默认为0.92
        :rtype: float
        """
        return self._AttendanceThreshold

    @AttendanceThreshold.setter
    def AttendanceThreshold(self, AttendanceThreshold):
        self._AttendanceThreshold = AttendanceThreshold

    @property
    def EnableStranger(self):
        """是否开启陌生人模式，陌生人模式是指在任务中发现的非注册人脸库中的人脸也返回相关统计信息，默认不开启
        :rtype: bool
        """
        return self._EnableStranger

    @EnableStranger.setter
    def EnableStranger(self, EnableStranger):
        self._EnableStranger = EnableStranger

    @property
    def EndTime(self):
        """考勤结束时间（到视频的第几秒结束考勤），单位秒；默认为900 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间往后12小时
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NoticeUrl(self):
        """通知回调地址，要求方法为post，application/json格式
        :rtype: str
        """
        return self._NoticeUrl

    @NoticeUrl.setter
    def NoticeUrl(self, NoticeUrl):
        self._NoticeUrl = NoticeUrl

    @property
    def StartTime(self):
        """考勤开始时间（从视频的第几秒开始考勤），单位秒；默认为0 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Threshold(self):
        """识别阈值；默认为0.8
        :rtype: float
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._LibraryIds = params.get("LibraryIds")
        self._AttendanceThreshold = params.get("AttendanceThreshold")
        self._EnableStranger = params.get("EnableStranger")
        self._EndTime = params.get("EndTime")
        self._NoticeUrl = params.get("NoticeUrl")
        self._StartTime = params.get("StartTime")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCheckAttendanceTaskPlusResponse(AbstractModel):
    """SubmitCheckAttendanceTaskPlus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务标识符
        :type JobId: int
        :param _NotRegisteredSet: 没有注册的人的ID列表
        :type NotRegisteredSet: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._NotRegisteredSet = None
        self._RequestId = None

    @property
    def JobId(self):
        """任务标识符
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NotRegisteredSet(self):
        """没有注册的人的ID列表
        :rtype: str
        """
        return self._NotRegisteredSet

    @NotRegisteredSet.setter
    def NotRegisteredSet(self, NotRegisteredSet):
        self._NotRegisteredSet = NotRegisteredSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._NotRegisteredSet = params.get("NotRegisteredSet")
        self._RequestId = params.get("RequestId")


class SubmitCheckAttendanceTaskRequest(AbstractModel):
    """SubmitCheckAttendanceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入数据
        :type FileContent: str
        :param _FileType: 视频流类型，vod_url表示点播URL，live_url表示直播URL，默认vod_url
        :type FileType: str
        :param _LibraryIds: 人员库 ID列表
        :type LibraryIds: list of str
        :param _AttendanceThreshold: 确定出勤阈值；默认为0.92
        :type AttendanceThreshold: float
        :param _EnableStranger: 是否开启陌生人模式，陌生人模式是指在任务中发现的非注册人脸库中的人脸也返回相关统计信息，默认不开启
        :type EnableStranger: bool
        :param _EndTime: 考勤结束时间（到视频的第几秒结束考勤），单位秒；默认为900 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间往后12小时
        :type EndTime: int
        :param _NoticeUrl: 通知回调地址，要求方法为post，application/json格式
        :type NoticeUrl: str
        :param _StartTime: 考勤开始时间（从视频的第几秒开始考勤），单位秒；默认为0 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间
        :type StartTime: int
        :param _Threshold: 识别阈值；默认为0.8
        :type Threshold: float
        """
        self._FileContent = None
        self._FileType = None
        self._LibraryIds = None
        self._AttendanceThreshold = None
        self._EnableStranger = None
        self._EndTime = None
        self._NoticeUrl = None
        self._StartTime = None
        self._Threshold = None

    @property
    def FileContent(self):
        """输入数据
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """视频流类型，vod_url表示点播URL，live_url表示直播URL，默认vod_url
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def LibraryIds(self):
        """人员库 ID列表
        :rtype: list of str
        """
        return self._LibraryIds

    @LibraryIds.setter
    def LibraryIds(self, LibraryIds):
        self._LibraryIds = LibraryIds

    @property
    def AttendanceThreshold(self):
        """确定出勤阈值；默认为0.92
        :rtype: float
        """
        return self._AttendanceThreshold

    @AttendanceThreshold.setter
    def AttendanceThreshold(self, AttendanceThreshold):
        self._AttendanceThreshold = AttendanceThreshold

    @property
    def EnableStranger(self):
        """是否开启陌生人模式，陌生人模式是指在任务中发现的非注册人脸库中的人脸也返回相关统计信息，默认不开启
        :rtype: bool
        """
        return self._EnableStranger

    @EnableStranger.setter
    def EnableStranger(self, EnableStranger):
        self._EnableStranger = EnableStranger

    @property
    def EndTime(self):
        """考勤结束时间（到视频的第几秒结束考勤），单位秒；默认为900 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间往后12小时
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NoticeUrl(self):
        """通知回调地址，要求方法为post，application/json格式
        :rtype: str
        """
        return self._NoticeUrl

    @NoticeUrl.setter
    def NoticeUrl(self, NoticeUrl):
        self._NoticeUrl = NoticeUrl

    @property
    def StartTime(self):
        """考勤开始时间（从视频的第几秒开始考勤），单位秒；默认为0 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Threshold(self):
        """识别阈值；默认为0.8
        :rtype: float
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._LibraryIds = params.get("LibraryIds")
        self._AttendanceThreshold = params.get("AttendanceThreshold")
        self._EnableStranger = params.get("EnableStranger")
        self._EndTime = params.get("EndTime")
        self._NoticeUrl = params.get("NoticeUrl")
        self._StartTime = params.get("StartTime")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCheckAttendanceTaskResponse(AbstractModel):
    """SubmitCheckAttendanceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务标识符
        :type JobId: int
        :param _NotRegisteredSet: 没有注册的人的ID列表
        :type NotRegisteredSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._NotRegisteredSet = None
        self._RequestId = None

    @property
    def JobId(self):
        """任务标识符
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NotRegisteredSet(self):
        """没有注册的人的ID列表
        :rtype: list of str
        """
        return self._NotRegisteredSet

    @NotRegisteredSet.setter
    def NotRegisteredSet(self, NotRegisteredSet):
        self._NotRegisteredSet = NotRegisteredSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._NotRegisteredSet = params.get("NotRegisteredSet")
        self._RequestId = params.get("RequestId")


class SubmitConversationTaskRequest(AbstractModel):
    """SubmitConversationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param _StudentUrl: 学生音频流
        :type StudentUrl: str
        :param _TeacherUrl: 教师音频流
        :type TeacherUrl: str
        :param _VoiceEncodeType: 语音编码类型 1:pcm
        :type VoiceEncodeType: int
        :param _VoiceFileType: 语音文件类型 1:raw, 2:wav, 3:mp3（三种格式目前仅支持16k采样率16bit）
        :type VoiceFileType: int
        :param _Functions: 功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param _VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :type VocabLibNameList: list of str
        """
        self._Lang = None
        self._StudentUrl = None
        self._TeacherUrl = None
        self._VoiceEncodeType = None
        self._VoiceFileType = None
        self._Functions = None
        self._VocabLibNameList = None

    @property
    def Lang(self):
        """音频源的语言，默认0为英文，1为中文
        :rtype: int
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def StudentUrl(self):
        """学生音频流
        :rtype: str
        """
        return self._StudentUrl

    @StudentUrl.setter
    def StudentUrl(self, StudentUrl):
        self._StudentUrl = StudentUrl

    @property
    def TeacherUrl(self):
        """教师音频流
        :rtype: str
        """
        return self._TeacherUrl

    @TeacherUrl.setter
    def TeacherUrl(self, TeacherUrl):
        self._TeacherUrl = TeacherUrl

    @property
    def VoiceEncodeType(self):
        """语音编码类型 1:pcm
        :rtype: int
        """
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def VoiceFileType(self):
        """语音文件类型 1:raw, 2:wav, 3:mp3（三种格式目前仅支持16k采样率16bit）
        :rtype: int
        """
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType

    @property
    def Functions(self):
        """功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.Function`
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def VocabLibNameList(self):
        """识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :rtype: list of str
        """
        return self._VocabLibNameList

    @VocabLibNameList.setter
    def VocabLibNameList(self, VocabLibNameList):
        self._VocabLibNameList = VocabLibNameList


    def _deserialize(self, params):
        self._Lang = params.get("Lang")
        self._StudentUrl = params.get("StudentUrl")
        self._TeacherUrl = params.get("TeacherUrl")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._VoiceFileType = params.get("VoiceFileType")
        if params.get("Functions") is not None:
            self._Functions = Function()
            self._Functions._deserialize(params.get("Functions"))
        self._VocabLibNameList = params.get("VocabLibNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitConversationTaskResponse(AbstractModel):
    """SubmitConversationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 	查询结果时指名的jobid。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """	查询结果时指名的jobid。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitDoubleVideoHighlightsRequest(AbstractModel):
    """SubmitDoubleVideoHighlights请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 学生视频url
        :type FileContent: str
        :param _LibIds: 需要检索的人脸合集库，不在库中的人脸将不参与精彩集锦；目前仅支持输入一个人脸库。
        :type LibIds: list of str
        :param _Functions: 详细功能开关配置项
        :type Functions: :class:`tencentcloud.tci.v20190318.models.DoubleVideoFunction`
        :param _PersonInfoList: 需要匹配的人员信息列表。
        :type PersonInfoList: list of PersonInfo
        :param _FrameInterval: 视频处理的抽帧间隔，单位毫秒。建议留空。
        :type FrameInterval: int
        :param _PersonIds: 旧版本需要匹配的人员信息列表。
        :type PersonIds: list of str
        :param _SimThreshold: 人脸检索的相似度阈值，默认值0.89。建议留空。
        :type SimThreshold: float
        :param _TeacherFileContent: 老师视频url
        :type TeacherFileContent: str
        """
        self._FileContent = None
        self._LibIds = None
        self._Functions = None
        self._PersonInfoList = None
        self._FrameInterval = None
        self._PersonIds = None
        self._SimThreshold = None
        self._TeacherFileContent = None

    @property
    def FileContent(self):
        """学生视频url
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def LibIds(self):
        """需要检索的人脸合集库，不在库中的人脸将不参与精彩集锦；目前仅支持输入一个人脸库。
        :rtype: list of str
        """
        return self._LibIds

    @LibIds.setter
    def LibIds(self, LibIds):
        self._LibIds = LibIds

    @property
    def Functions(self):
        """详细功能开关配置项
        :rtype: :class:`tencentcloud.tci.v20190318.models.DoubleVideoFunction`
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def PersonInfoList(self):
        """需要匹配的人员信息列表。
        :rtype: list of PersonInfo
        """
        return self._PersonInfoList

    @PersonInfoList.setter
    def PersonInfoList(self, PersonInfoList):
        self._PersonInfoList = PersonInfoList

    @property
    def FrameInterval(self):
        """视频处理的抽帧间隔，单位毫秒。建议留空。
        :rtype: int
        """
        return self._FrameInterval

    @FrameInterval.setter
    def FrameInterval(self, FrameInterval):
        self._FrameInterval = FrameInterval

    @property
    def PersonIds(self):
        """旧版本需要匹配的人员信息列表。
        :rtype: list of str
        """
        return self._PersonIds

    @PersonIds.setter
    def PersonIds(self, PersonIds):
        self._PersonIds = PersonIds

    @property
    def SimThreshold(self):
        """人脸检索的相似度阈值，默认值0.89。建议留空。
        :rtype: float
        """
        return self._SimThreshold

    @SimThreshold.setter
    def SimThreshold(self, SimThreshold):
        self._SimThreshold = SimThreshold

    @property
    def TeacherFileContent(self):
        """老师视频url
        :rtype: str
        """
        return self._TeacherFileContent

    @TeacherFileContent.setter
    def TeacherFileContent(self, TeacherFileContent):
        self._TeacherFileContent = TeacherFileContent


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._LibIds = params.get("LibIds")
        if params.get("Functions") is not None:
            self._Functions = DoubleVideoFunction()
            self._Functions._deserialize(params.get("Functions"))
        if params.get("PersonInfoList") is not None:
            self._PersonInfoList = []
            for item in params.get("PersonInfoList"):
                obj = PersonInfo()
                obj._deserialize(item)
                self._PersonInfoList.append(obj)
        self._FrameInterval = params.get("FrameInterval")
        self._PersonIds = params.get("PersonIds")
        self._SimThreshold = params.get("SimThreshold")
        self._TeacherFileContent = params.get("TeacherFileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitDoubleVideoHighlightsResponse(AbstractModel):
    """SubmitDoubleVideoHighlights返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频拆条任务ID，用来唯一标识视频拆条任务。
        :type JobId: int
        :param _NotRegistered: 未注册的人员ID列表。若出现此项，代表评估出现了问题，输入的PersonId中有不在库中的人员ID。
        :type NotRegistered: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._NotRegistered = None
        self._RequestId = None

    @property
    def JobId(self):
        """视频拆条任务ID，用来唯一标识视频拆条任务。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NotRegistered(self):
        """未注册的人员ID列表。若出现此项，代表评估出现了问题，输入的PersonId中有不在库中的人员ID。
        :rtype: list of str
        """
        return self._NotRegistered

    @NotRegistered.setter
    def NotRegistered(self, NotRegistered):
        self._NotRegistered = NotRegistered

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._NotRegistered = params.get("NotRegistered")
        self._RequestId = params.get("RequestId")


class SubmitFullBodyClassTaskRequest(AbstractModel):
    """SubmitFullBodyClassTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param _FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :type FileType: str
        :param _Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param _LibrarySet: 查询人员库列表，可填写老师的注册照所在人员库
        :type LibrarySet: list of str
        :param _MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param _VocabLibNameList: 识别词库名列表，这些词汇库用来维护关键词，评估老师授课过程中，对这些关键词的使用情况
        :type VocabLibNameList: list of str
        :param _VoiceEncodeType: 语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :type VoiceEncodeType: int
        :param _VoiceFileType: 语音文件类型 10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :type VoiceFileType: int
        """
        self._FileContent = None
        self._FileType = None
        self._Lang = None
        self._LibrarySet = None
        self._MaxVideoDuration = None
        self._VocabLibNameList = None
        self._VoiceEncodeType = None
        self._VoiceFileType = None

    @property
    def FileContent(self):
        """输入分析对象内容，输入数据格式参考FileType参数释义
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Lang(self):
        """音频源的语言，默认0为英文，1为中文
        :rtype: int
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def LibrarySet(self):
        """查询人员库列表，可填写老师的注册照所在人员库
        :rtype: list of str
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def MaxVideoDuration(self):
        """视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration

    @property
    def VocabLibNameList(self):
        """识别词库名列表，这些词汇库用来维护关键词，评估老师授课过程中，对这些关键词的使用情况
        :rtype: list of str
        """
        return self._VocabLibNameList

    @VocabLibNameList.setter
    def VocabLibNameList(self, VocabLibNameList):
        self._VocabLibNameList = VocabLibNameList

    @property
    def VoiceEncodeType(self):
        """语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :rtype: int
        """
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def VoiceFileType(self):
        """语音文件类型 10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :rtype: int
        """
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._Lang = params.get("Lang")
        self._LibrarySet = params.get("LibrarySet")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        self._VocabLibNameList = params.get("VocabLibNameList")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._VoiceFileType = params.get("VoiceFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitFullBodyClassTaskResponse(AbstractModel):
    """SubmitFullBodyClassTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageResults: 图像任务直接返回结果，包括： FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 TeacherBodyMovement、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageResults = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ImageResults(self):
        """图像任务直接返回结果，包括： FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 TeacherBodyMovement、TimeInfo
        :rtype: list of ImageTaskResult
        """
        return self._ImageResults

    @ImageResults.setter
    def ImageResults(self, ImageResults):
        self._ImageResults = ImageResults

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self._ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ImageResults.append(obj)
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SubmitHighlightsRequest(AbstractModel):
    """SubmitHighlights请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Functions: 表情配置开关项。
        :type Functions: :class:`tencentcloud.tci.v20190318.models.HLFunction`
        :param _FileContent: 视频url。
        :type FileContent: str
        :param _FileType: 视频类型及来源，目前只支持点播类型："vod_url"。
        :type FileType: str
        :param _LibIds: 需要检索的人脸合集库，不在库中的人脸将不参与精彩集锦。
        :type LibIds: list of str
        :param _FrameInterval: 视频处理的抽帧间隔，单位毫秒。建议留空。
        :type FrameInterval: int
        :param _KeywordsLanguage: 关键词语言类型，0为英文，1为中文。
        :type KeywordsLanguage: int
        :param _KeywordsStrings: 关键词数组，当且仅当Funtions中的EnableKeywordWonderfulTime为true时有意义，匹配相应的关键字。
        :type KeywordsStrings: list of str
        :param _MaxVideoDuration: 处理视频的总时长，单位毫秒。该值为0或未设置时，默认值两小时生效；当该值大于视频实际时长时，视频实际时长生效；当该值小于视频实际时长时，该值生效；当获取视频实际时长失败时，若该值设置则生效，否则默认值生效。建议留空。
        :type MaxVideoDuration: int
        :param _SimThreshold: 人脸检索的相似度阈值，默认值0.89。建议留空。
        :type SimThreshold: float
        """
        self._Functions = None
        self._FileContent = None
        self._FileType = None
        self._LibIds = None
        self._FrameInterval = None
        self._KeywordsLanguage = None
        self._KeywordsStrings = None
        self._MaxVideoDuration = None
        self._SimThreshold = None

    @property
    def Functions(self):
        """表情配置开关项。
        :rtype: :class:`tencentcloud.tci.v20190318.models.HLFunction`
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def FileContent(self):
        """视频url。
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """视频类型及来源，目前只支持点播类型："vod_url"。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def LibIds(self):
        """需要检索的人脸合集库，不在库中的人脸将不参与精彩集锦。
        :rtype: list of str
        """
        return self._LibIds

    @LibIds.setter
    def LibIds(self, LibIds):
        self._LibIds = LibIds

    @property
    def FrameInterval(self):
        """视频处理的抽帧间隔，单位毫秒。建议留空。
        :rtype: int
        """
        return self._FrameInterval

    @FrameInterval.setter
    def FrameInterval(self, FrameInterval):
        self._FrameInterval = FrameInterval

    @property
    def KeywordsLanguage(self):
        """关键词语言类型，0为英文，1为中文。
        :rtype: int
        """
        return self._KeywordsLanguage

    @KeywordsLanguage.setter
    def KeywordsLanguage(self, KeywordsLanguage):
        self._KeywordsLanguage = KeywordsLanguage

    @property
    def KeywordsStrings(self):
        """关键词数组，当且仅当Funtions中的EnableKeywordWonderfulTime为true时有意义，匹配相应的关键字。
        :rtype: list of str
        """
        return self._KeywordsStrings

    @KeywordsStrings.setter
    def KeywordsStrings(self, KeywordsStrings):
        self._KeywordsStrings = KeywordsStrings

    @property
    def MaxVideoDuration(self):
        """处理视频的总时长，单位毫秒。该值为0或未设置时，默认值两小时生效；当该值大于视频实际时长时，视频实际时长生效；当该值小于视频实际时长时，该值生效；当获取视频实际时长失败时，若该值设置则生效，否则默认值生效。建议留空。
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration

    @property
    def SimThreshold(self):
        """人脸检索的相似度阈值，默认值0.89。建议留空。
        :rtype: float
        """
        return self._SimThreshold

    @SimThreshold.setter
    def SimThreshold(self, SimThreshold):
        self._SimThreshold = SimThreshold


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self._Functions = HLFunction()
            self._Functions._deserialize(params.get("Functions"))
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._LibIds = params.get("LibIds")
        self._FrameInterval = params.get("FrameInterval")
        self._KeywordsLanguage = params.get("KeywordsLanguage")
        self._KeywordsStrings = params.get("KeywordsStrings")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        self._SimThreshold = params.get("SimThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHighlightsResponse(AbstractModel):
    """SubmitHighlights返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频拆条任务ID，用来唯一标识视频拆条任务。
        :type JobId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """视频拆条任务ID，用来唯一标识视频拆条任务。
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitImageTaskPlusRequest(AbstractModel):
    """SubmitImageTaskPlus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: list of str
        :param _FileType: 输入分析对象类型，picture：二进制图片的 base64 编码字符串，picture_url:图片地址，vod_url：视频地址，live_url：直播地址
        :type FileType: str
        :param _Functions: 任务控制选项
        :type Functions: :class:`tencentcloud.tci.v20190318.models.ImageTaskFunction`
        :param _LightStandardSet: 光照标准列表
        :type LightStandardSet: list of LightStandard
        :param _FrameInterval: 抽帧的时间间隔，单位毫秒，默认值1000，保留字段，当前不支持填写。
        :type FrameInterval: int
        :param _LibrarySet: 查询人员库列表
        :type LibrarySet: list of str
        :param _MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param _SimThreshold: 人脸识别中的相似度阈值，默认值为0.89，保留字段，当前不支持填写。
        :type SimThreshold: float
        """
        self._FileContent = None
        self._FileType = None
        self._Functions = None
        self._LightStandardSet = None
        self._FrameInterval = None
        self._LibrarySet = None
        self._MaxVideoDuration = None
        self._SimThreshold = None

    @property
    def FileContent(self):
        """输入分析对象内容，输入数据格式参考FileType参数释义
        :rtype: list of str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture：二进制图片的 base64 编码字符串，picture_url:图片地址，vod_url：视频地址，live_url：直播地址
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Functions(self):
        """任务控制选项
        :rtype: :class:`tencentcloud.tci.v20190318.models.ImageTaskFunction`
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def LightStandardSet(self):
        """光照标准列表
        :rtype: list of LightStandard
        """
        return self._LightStandardSet

    @LightStandardSet.setter
    def LightStandardSet(self, LightStandardSet):
        self._LightStandardSet = LightStandardSet

    @property
    def FrameInterval(self):
        """抽帧的时间间隔，单位毫秒，默认值1000，保留字段，当前不支持填写。
        :rtype: int
        """
        return self._FrameInterval

    @FrameInterval.setter
    def FrameInterval(self, FrameInterval):
        self._FrameInterval = FrameInterval

    @property
    def LibrarySet(self):
        """查询人员库列表
        :rtype: list of str
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def MaxVideoDuration(self):
        """视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration

    @property
    def SimThreshold(self):
        """人脸识别中的相似度阈值，默认值为0.89，保留字段，当前不支持填写。
        :rtype: float
        """
        return self._SimThreshold

    @SimThreshold.setter
    def SimThreshold(self, SimThreshold):
        self._SimThreshold = SimThreshold


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        if params.get("Functions") is not None:
            self._Functions = ImageTaskFunction()
            self._Functions._deserialize(params.get("Functions"))
        if params.get("LightStandardSet") is not None:
            self._LightStandardSet = []
            for item in params.get("LightStandardSet"):
                obj = LightStandard()
                obj._deserialize(item)
                self._LightStandardSet.append(obj)
        self._FrameInterval = params.get("FrameInterval")
        self._LibrarySet = params.get("LibrarySet")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        self._SimThreshold = params.get("SimThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageTaskPlusResponse(AbstractModel):
    """SubmitImageTaskPlus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultSet: 识别结果
        :type ResultSet: list of ImageTaskResult
        :param _JobId: 任务标识符
        :type JobId: int
        :param _Progress: 任务进度
        :type Progress: int
        :param _TotalCount: 结果总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultSet = None
        self._JobId = None
        self._Progress = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ResultSet(self):
        """识别结果
        :rtype: list of ImageTaskResult
        """
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def JobId(self):
        """任务标识符
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Progress(self):
        """任务进度
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TotalCount(self):
        """结果总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self._ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ResultSet.append(obj)
        self._JobId = params.get("JobId")
        self._Progress = params.get("Progress")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class SubmitImageTaskRequest(AbstractModel):
    """SubmitImageTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param _FileType: 输入分析对象类型，picture：二进制图片的 base64 编码字符串，picture_url:图片地址，vod_url：视频地址，live_url：直播地址
        :type FileType: str
        :param _Functions: 任务控制选项
        :type Functions: :class:`tencentcloud.tci.v20190318.models.ImageTaskFunction`
        :param _LightStandardSet: 光照标准列表
        :type LightStandardSet: list of LightStandard
        :param _EventsCallBack: 结果更新回调地址。
        :type EventsCallBack: str
        :param _FrameInterval: 抽帧的时间间隔，单位毫秒，默认值1000，保留字段，当前不支持填写。
        :type FrameInterval: int
        :param _LibrarySet: 查询人员库列表
        :type LibrarySet: list of str
        :param _MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param _SimThreshold: 人脸识别中的相似度阈值，默认值为0.89，保留字段，当前不支持填写。
        :type SimThreshold: float
        """
        self._FileContent = None
        self._FileType = None
        self._Functions = None
        self._LightStandardSet = None
        self._EventsCallBack = None
        self._FrameInterval = None
        self._LibrarySet = None
        self._MaxVideoDuration = None
        self._SimThreshold = None

    @property
    def FileContent(self):
        """输入分析对象内容，输入数据格式参考FileType参数释义
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture：二进制图片的 base64 编码字符串，picture_url:图片地址，vod_url：视频地址，live_url：直播地址
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Functions(self):
        """任务控制选项
        :rtype: :class:`tencentcloud.tci.v20190318.models.ImageTaskFunction`
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def LightStandardSet(self):
        """光照标准列表
        :rtype: list of LightStandard
        """
        return self._LightStandardSet

    @LightStandardSet.setter
    def LightStandardSet(self, LightStandardSet):
        self._LightStandardSet = LightStandardSet

    @property
    def EventsCallBack(self):
        """结果更新回调地址。
        :rtype: str
        """
        return self._EventsCallBack

    @EventsCallBack.setter
    def EventsCallBack(self, EventsCallBack):
        self._EventsCallBack = EventsCallBack

    @property
    def FrameInterval(self):
        """抽帧的时间间隔，单位毫秒，默认值1000，保留字段，当前不支持填写。
        :rtype: int
        """
        return self._FrameInterval

    @FrameInterval.setter
    def FrameInterval(self, FrameInterval):
        self._FrameInterval = FrameInterval

    @property
    def LibrarySet(self):
        """查询人员库列表
        :rtype: list of str
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def MaxVideoDuration(self):
        """视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration

    @property
    def SimThreshold(self):
        """人脸识别中的相似度阈值，默认值为0.89，保留字段，当前不支持填写。
        :rtype: float
        """
        return self._SimThreshold

    @SimThreshold.setter
    def SimThreshold(self, SimThreshold):
        self._SimThreshold = SimThreshold


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        if params.get("Functions") is not None:
            self._Functions = ImageTaskFunction()
            self._Functions._deserialize(params.get("Functions"))
        if params.get("LightStandardSet") is not None:
            self._LightStandardSet = []
            for item in params.get("LightStandardSet"):
                obj = LightStandard()
                obj._deserialize(item)
                self._LightStandardSet.append(obj)
        self._EventsCallBack = params.get("EventsCallBack")
        self._FrameInterval = params.get("FrameInterval")
        self._LibrarySet = params.get("LibrarySet")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        self._SimThreshold = params.get("SimThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageTaskResponse(AbstractModel):
    """SubmitImageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultSet: 识别结果
        :type ResultSet: list of ImageTaskResult
        :param _JobId: 任务标识符
        :type JobId: int
        :param _Progress: 任务进度
        :type Progress: int
        :param _TotalCount: 结果总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultSet = None
        self._JobId = None
        self._Progress = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ResultSet(self):
        """识别结果
        :rtype: list of ImageTaskResult
        """
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def JobId(self):
        """任务标识符
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Progress(self):
        """任务进度
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TotalCount(self):
        """结果总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self._ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ResultSet.append(obj)
        self._JobId = params.get("JobId")
        self._Progress = params.get("Progress")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class SubmitOneByOneClassTaskRequest(AbstractModel):
    """SubmitOneByOneClassTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param _FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :type FileType: str
        :param _Lang: 音频源的语言，默认0为英文，1为中文 
        :type Lang: int
        :param _LibrarySet: 查询人员库列表，可填写学生的注册照所在人员库
        :type LibrarySet: list of str
        :param _MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param _VocabLibNameList: 识别词库名列表，这些词汇库用来维护关键词，评估学生对这些关键词的使用情况
        :type VocabLibNameList: list of str
        :param _VoiceEncodeType: 语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :type VoiceEncodeType: int
        :param _VoiceFileType: 语音文件类型10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :type VoiceFileType: int
        """
        self._FileContent = None
        self._FileType = None
        self._Lang = None
        self._LibrarySet = None
        self._MaxVideoDuration = None
        self._VocabLibNameList = None
        self._VoiceEncodeType = None
        self._VoiceFileType = None

    @property
    def FileContent(self):
        """输入分析对象内容，输入数据格式参考FileType参数释义
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Lang(self):
        """音频源的语言，默认0为英文，1为中文 
        :rtype: int
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def LibrarySet(self):
        """查询人员库列表，可填写学生的注册照所在人员库
        :rtype: list of str
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def MaxVideoDuration(self):
        """视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration

    @property
    def VocabLibNameList(self):
        """识别词库名列表，这些词汇库用来维护关键词，评估学生对这些关键词的使用情况
        :rtype: list of str
        """
        return self._VocabLibNameList

    @VocabLibNameList.setter
    def VocabLibNameList(self, VocabLibNameList):
        self._VocabLibNameList = VocabLibNameList

    @property
    def VoiceEncodeType(self):
        """语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :rtype: int
        """
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def VoiceFileType(self):
        """语音文件类型10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :rtype: int
        """
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._Lang = params.get("Lang")
        self._LibrarySet = params.get("LibrarySet")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        self._VocabLibNameList = params.get("VocabLibNameList")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._VoiceFileType = params.get("VoiceFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitOneByOneClassTaskResponse(AbstractModel):
    """SubmitOneByOneClassTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageResults: 图像任务直接返回结果，包括：FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageResults = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ImageResults(self):
        """图像任务直接返回结果，包括：FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、TimeInfo
        :rtype: list of ImageTaskResult
        """
        return self._ImageResults

    @ImageResults.setter
    def ImageResults(self, ImageResults):
        self._ImageResults = ImageResults

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self._ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ImageResults.append(obj)
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SubmitOpenClassTaskRequest(AbstractModel):
    """SubmitOpenClassTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param _FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址,picture: 图片二进制数据的BASE64编码
        :type FileType: str
        :param _LibrarySet: 查询人员库列表，可填写学生们的注册照所在人员库
        :type LibrarySet: list of str
        :param _MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        """
        self._FileContent = None
        self._FileType = None
        self._LibrarySet = None
        self._MaxVideoDuration = None

    @property
    def FileContent(self):
        """输入分析对象内容，输入数据格式参考FileType参数释义
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址,picture: 图片二进制数据的BASE64编码
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def LibrarySet(self):
        """查询人员库列表，可填写学生们的注册照所在人员库
        :rtype: list of str
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def MaxVideoDuration(self):
        """视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._LibrarySet = params.get("LibrarySet")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitOpenClassTaskResponse(AbstractModel):
    """SubmitOpenClassTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageResults: 图像任务直接返回结果，包括：FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 StudentBodyMovement、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageResults = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ImageResults(self):
        """图像任务直接返回结果，包括：FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 StudentBodyMovement、TimeInfo
        :rtype: list of ImageTaskResult
        """
        return self._ImageResults

    @ImageResults.setter
    def ImageResults(self, ImageResults):
        self._ImageResults = ImageResults

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self._ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ImageResults.append(obj)
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SubmitPartialBodyClassTaskRequest(AbstractModel):
    """SubmitPartialBodyClassTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param _FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :type FileType: str
        :param _Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param _LibrarySet: 查询人员库列表，可填写老师的注册照所在人员库
        :type LibrarySet: list of str
        :param _MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param _VocabLibNameList: 识别词库名列表，这些词汇库用来维护关键词，评估老师授课过程中，对这些关键词的使用情况
        :type VocabLibNameList: list of str
        :param _VoiceEncodeType: 语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :type VoiceEncodeType: int
        :param _VoiceFileType: 语音文件类型 10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :type VoiceFileType: int
        """
        self._FileContent = None
        self._FileType = None
        self._Lang = None
        self._LibrarySet = None
        self._MaxVideoDuration = None
        self._VocabLibNameList = None
        self._VoiceEncodeType = None
        self._VoiceFileType = None

    @property
    def FileContent(self):
        """输入分析对象内容，输入数据格式参考FileType参数释义
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Lang(self):
        """音频源的语言，默认0为英文，1为中文
        :rtype: int
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def LibrarySet(self):
        """查询人员库列表，可填写老师的注册照所在人员库
        :rtype: list of str
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def MaxVideoDuration(self):
        """视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration

    @property
    def VocabLibNameList(self):
        """识别词库名列表，这些词汇库用来维护关键词，评估老师授课过程中，对这些关键词的使用情况
        :rtype: list of str
        """
        return self._VocabLibNameList

    @VocabLibNameList.setter
    def VocabLibNameList(self, VocabLibNameList):
        self._VocabLibNameList = VocabLibNameList

    @property
    def VoiceEncodeType(self):
        """语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :rtype: int
        """
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def VoiceFileType(self):
        """语音文件类型 10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :rtype: int
        """
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._Lang = params.get("Lang")
        self._LibrarySet = params.get("LibrarySet")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        self._VocabLibNameList = params.get("VocabLibNameList")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._VoiceFileType = params.get("VoiceFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitPartialBodyClassTaskResponse(AbstractModel):
    """SubmitPartialBodyClassTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageResults: 图像任务直接返回结果，包括： FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 Gesture 、 Light、 TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageResults = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ImageResults(self):
        """图像任务直接返回结果，包括： FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 Gesture 、 Light、 TimeInfo
        :rtype: list of ImageTaskResult
        """
        return self._ImageResults

    @ImageResults.setter
    def ImageResults(self, ImageResults):
        self._ImageResults = ImageResults

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self._ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ImageResults.append(obj)
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SubmitTraditionalClassTaskRequest(AbstractModel):
    """SubmitTraditionalClassTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param _FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture：图片二进制数据的BASE64编码
        :type FileType: str
        :param _LibrarySet: 查询人员库列表，可填写学生们的注册照所在人员库
        :type LibrarySet: list of str
        :param _MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        """
        self._FileContent = None
        self._FileType = None
        self._LibrarySet = None
        self._MaxVideoDuration = None

    @property
    def FileContent(self):
        """输入分析对象内容，输入数据格式参考FileType参数释义
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileType(self):
        """输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture：图片二进制数据的BASE64编码
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def LibrarySet(self):
        """查询人员库列表，可填写学生们的注册照所在人员库
        :rtype: list of str
        """
        return self._LibrarySet

    @LibrarySet.setter
    def LibrarySet(self, LibrarySet):
        self._LibrarySet = LibrarySet

    @property
    def MaxVideoDuration(self):
        """视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :rtype: int
        """
        return self._MaxVideoDuration

    @MaxVideoDuration.setter
    def MaxVideoDuration(self, MaxVideoDuration):
        self._MaxVideoDuration = MaxVideoDuration


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._FileType = params.get("FileType")
        self._LibrarySet = params.get("LibrarySet")
        self._MaxVideoDuration = params.get("MaxVideoDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTraditionalClassTaskResponse(AbstractModel):
    """SubmitTraditionalClassTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageResults: 图像任务直接返回结果，包括： ActionInfo、FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageResults = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ImageResults(self):
        """图像任务直接返回结果，包括： ActionInfo、FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 TimeInfo
        :rtype: list of ImageTaskResult
        """
        return self._ImageResults

    @ImageResults.setter
    def ImageResults(self, ImageResults):
        self._ImageResults = ImageResults

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self._ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self._ImageResults.append(obj)
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SuspectedInfo(AbstractModel):
    """疑似出席人员

    """

    def __init__(self):
        r"""
        :param _FaceSet: TopN匹配信息列表
        :type FaceSet: list of FrameInfo
        :param _PersonId: 识别到的人员id
        :type PersonId: str
        """
        self._FaceSet = None
        self._PersonId = None

    @property
    def FaceSet(self):
        """TopN匹配信息列表
        :rtype: list of FrameInfo
        """
        return self._FaceSet

    @FaceSet.setter
    def FaceSet(self, FaceSet):
        self._FaceSet = FaceSet

    @property
    def PersonId(self):
        """识别到的人员id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        if params.get("FaceSet") is not None:
            self._FaceSet = []
            for item in params.get("FaceSet"):
                obj = FrameInfo()
                obj._deserialize(item)
                self._FaceSet.append(obj)
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeacherOutScreenResult(AbstractModel):
    """教师是否在屏幕内判断结果

    """

    def __init__(self):
        r"""
        :param _Class: 动作识别结果，InScreen：在屏幕内
OutScreen：不在屏幕内
        :type Class: str
        :param _Height: 识别结果高度
        :type Height: int
        :param _Left: 识别结果左坐标
        :type Left: int
        :param _Top: 识别结果顶坐标
        :type Top: int
        :param _Width: 识别结果宽度
        :type Width: int
        """
        self._Class = None
        self._Height = None
        self._Left = None
        self._Top = None
        self._Width = None

    @property
    def Class(self):
        """动作识别结果，InScreen：在屏幕内
OutScreen：不在屏幕内
        :rtype: str
        """
        return self._Class

    @Class.setter
    def Class(self, Class):
        self._Class = Class

    @property
    def Height(self):
        """识别结果高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Left(self):
        """识别结果左坐标
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Top(self):
        """识别结果顶坐标
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Width(self):
        """识别结果宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width


    def _deserialize(self, params):
        self._Class = params.get("Class")
        self._Height = params.get("Height")
        self._Left = params.get("Left")
        self._Top = params.get("Top")
        self._Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextItem(AbstractModel):
    """当前句子的信息

    """

    def __init__(self):
        r"""
        :param _Words: 当前句子包含的所有单词信息
        :type Words: list of Word
        :param _Confidence: 当前句子的置信度
        :type Confidence: float
        :param _Mbtm: 当前句子语音的起始时间点，单位为ms
        :type Mbtm: int
        :param _Metm: 当前句子语音的终止时间点，单位为ms
        :type Metm: int
        :param _Tag: 保留参数，暂无意义
        :type Tag: int
        :param _Text: 当前句子
        :type Text: str
        :param _TextSize: 当前句子的字节数
        :type TextSize: int
        """
        self._Words = None
        self._Confidence = None
        self._Mbtm = None
        self._Metm = None
        self._Tag = None
        self._Text = None
        self._TextSize = None

    @property
    def Words(self):
        """当前句子包含的所有单词信息
        :rtype: list of Word
        """
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def Confidence(self):
        """当前句子的置信度
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Mbtm(self):
        """当前句子语音的起始时间点，单位为ms
        :rtype: int
        """
        return self._Mbtm

    @Mbtm.setter
    def Mbtm(self, Mbtm):
        self._Mbtm = Mbtm

    @property
    def Metm(self):
        """当前句子语音的终止时间点，单位为ms
        :rtype: int
        """
        return self._Metm

    @Metm.setter
    def Metm(self, Metm):
        self._Metm = Metm

    @property
    def Tag(self):
        """保留参数，暂无意义
        :rtype: int
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Text(self):
        """当前句子
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TextSize(self):
        """当前句子的字节数
        :rtype: int
        """
        return self._TextSize

    @TextSize.setter
    def TextSize(self, TextSize):
        self._TextSize = TextSize


    def _deserialize(self, params):
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = Word()
                obj._deserialize(item)
                self._Words.append(obj)
        self._Confidence = params.get("Confidence")
        self._Mbtm = params.get("Mbtm")
        self._Metm = params.get("Metm")
        self._Tag = params.get("Tag")
        self._Text = params.get("Text")
        self._TextSize = params.get("TextSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeInfoResult(AbstractModel):
    """TimeInfoResult

    """

    def __init__(self):
        r"""
        :param _Duration: 持续时间，单位毫秒
        :type Duration: int
        :param _EndTs: 结束时间戳，单位毫秒
        :type EndTs: int
        :param _StartTs: 开始时间戳，单位毫秒
        :type StartTs: int
        """
        self._Duration = None
        self._EndTs = None
        self._StartTs = None

    @property
    def Duration(self):
        """持续时间，单位毫秒
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def EndTs(self):
        """结束时间戳，单位毫秒
        :rtype: int
        """
        return self._EndTs

    @EndTs.setter
    def EndTs(self, EndTs):
        self._EndTs = EndTs

    @property
    def StartTs(self):
        """开始时间戳，单位毫秒
        :rtype: int
        """
        return self._StartTs

    @StartTs.setter
    def StartTs(self, StartTs):
        self._StartTs = StartTs


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._EndTs = params.get("EndTs")
        self._StartTs = params.get("StartTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeType(AbstractModel):
    """起止时间

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间戳
        :type EndTime: int
        :param _StartTime: 起始时间戳
        :type StartTime: int
        """
        self._EndTime = None
        self._StartTime = None

    @property
    def EndTime(self):
        """结束时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        """起始时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransmitAudioStreamRequest(AbstractModel):
    """TransmitAudioStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Functions: 功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param _SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义。
        :type SeqId: int
        :param _SessionId: 语音段唯一标识，一个完整语音一个SessionId。
        :type SessionId: str
        :param _UserVoiceData: 当前数据包数据, 流式模式下数据包大小可以按需设置，在网络良好的情况下，建议设置为0.5k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。
        :type UserVoiceData: str
        :param _VoiceEncodeType: 语音编码类型 1:pcm。
        :type VoiceEncodeType: int
        :param _VoiceFileType: 语音文件类型 	1: raw, 2: wav, 3: mp3 (语言文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败)。
        :type VoiceFileType: int
        :param _IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param _Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param _StorageMode: 是否临时保存 音频链接
        :type StorageMode: int
        :param _VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :type VocabLibNameList: list of str
        """
        self._Functions = None
        self._SeqId = None
        self._SessionId = None
        self._UserVoiceData = None
        self._VoiceEncodeType = None
        self._VoiceFileType = None
        self._IsEnd = None
        self._Lang = None
        self._StorageMode = None
        self._VocabLibNameList = None

    @property
    def Functions(self):
        """功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.Function`
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def SeqId(self):
        """流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义。
        :rtype: int
        """
        return self._SeqId

    @SeqId.setter
    def SeqId(self, SeqId):
        self._SeqId = SeqId

    @property
    def SessionId(self):
        """语音段唯一标识，一个完整语音一个SessionId。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def UserVoiceData(self):
        """当前数据包数据, 流式模式下数据包大小可以按需设置，在网络良好的情况下，建议设置为0.5k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。
        :rtype: str
        """
        return self._UserVoiceData

    @UserVoiceData.setter
    def UserVoiceData(self, UserVoiceData):
        self._UserVoiceData = UserVoiceData

    @property
    def VoiceEncodeType(self):
        """语音编码类型 1:pcm。
        :rtype: int
        """
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def VoiceFileType(self):
        """语音文件类型 	1: raw, 2: wav, 3: mp3 (语言文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败)。
        :rtype: int
        """
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType

    @property
    def IsEnd(self):
        """是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :rtype: int
        """
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd

    @property
    def Lang(self):
        """音频源的语言，默认0为英文，1为中文
        :rtype: int
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def StorageMode(self):
        """是否临时保存 音频链接
        :rtype: int
        """
        return self._StorageMode

    @StorageMode.setter
    def StorageMode(self, StorageMode):
        self._StorageMode = StorageMode

    @property
    def VocabLibNameList(self):
        """识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :rtype: list of str
        """
        return self._VocabLibNameList

    @VocabLibNameList.setter
    def VocabLibNameList(self, VocabLibNameList):
        self._VocabLibNameList = VocabLibNameList


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self._Functions = Function()
            self._Functions._deserialize(params.get("Functions"))
        self._SeqId = params.get("SeqId")
        self._SessionId = params.get("SessionId")
        self._UserVoiceData = params.get("UserVoiceData")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._VoiceFileType = params.get("VoiceFileType")
        self._IsEnd = params.get("IsEnd")
        self._Lang = params.get("Lang")
        self._StorageMode = params.get("StorageMode")
        self._VocabLibNameList = params.get("VocabLibNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransmitAudioStreamResponse(AbstractModel):
    """TransmitAudioStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param _Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :type Texts: list of WholeTextItem
        :param _VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param _VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param _AllTexts: 音频全部文本。
        :type AllTexts: str
        :param _AudioUrl: 临时保存的音频链接
        :type AudioUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsrStat = None
        self._Texts = None
        self._VocabAnalysisDetailInfo = None
        self._VocabAnalysisStatInfo = None
        self._AllTexts = None
        self._AudioUrl = None
        self._RequestId = None

    @property
    def AsrStat(self):
        """返回的当前音频的统计信息。当进度为100时返回。
        :rtype: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        """
        return self._AsrStat

    @AsrStat.setter
    def AsrStat(self, AsrStat):
        self._AsrStat = AsrStat

    @property
    def Texts(self):
        """返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :rtype: list of WholeTextItem
        """
        return self._Texts

    @Texts.setter
    def Texts(self, Texts):
        self._Texts = Texts

    @property
    def VocabAnalysisDetailInfo(self):
        """返回词汇库中的单词出现的详细时间信息。
        :rtype: list of VocabDetailInfomation
        """
        return self._VocabAnalysisDetailInfo

    @VocabAnalysisDetailInfo.setter
    def VocabAnalysisDetailInfo(self, VocabAnalysisDetailInfo):
        self._VocabAnalysisDetailInfo = VocabAnalysisDetailInfo

    @property
    def VocabAnalysisStatInfo(self):
        """返回词汇库中的单词出现的次数信息。
        :rtype: list of VocabStatInfomation
        """
        return self._VocabAnalysisStatInfo

    @VocabAnalysisStatInfo.setter
    def VocabAnalysisStatInfo(self, VocabAnalysisStatInfo):
        self._VocabAnalysisStatInfo = VocabAnalysisStatInfo

    @property
    def AllTexts(self):
        """音频全部文本。
        :rtype: str
        """
        return self._AllTexts

    @AllTexts.setter
    def AllTexts(self, AllTexts):
        self._AllTexts = AllTexts

    @property
    def AudioUrl(self):
        """临时保存的音频链接
        :rtype: str
        """
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self._AsrStat = ASRStat()
            self._AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self._Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self._Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self._VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self._VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self._VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self._VocabAnalysisStatInfo.append(obj)
        self._AllTexts = params.get("AllTexts")
        self._AudioUrl = params.get("AudioUrl")
        self._RequestId = params.get("RequestId")


class VocabDetailInfomation(AbstractModel):
    """词汇库中的单词出现在音频中的那个句子的起始时间和结束时间信息

    """

    def __init__(self):
        r"""
        :param _VocabDetailInfo: 词汇库中的单词出现在该音频中的那个句子的时间戳，出现了几次，就返回对应次数的起始和结束时间戳
        :type VocabDetailInfo: list of DetailInfo
        :param _VocabLibName: 词汇库名
        :type VocabLibName: str
        """
        self._VocabDetailInfo = None
        self._VocabLibName = None

    @property
    def VocabDetailInfo(self):
        """词汇库中的单词出现在该音频中的那个句子的时间戳，出现了几次，就返回对应次数的起始和结束时间戳
        :rtype: list of DetailInfo
        """
        return self._VocabDetailInfo

    @VocabDetailInfo.setter
    def VocabDetailInfo(self, VocabDetailInfo):
        self._VocabDetailInfo = VocabDetailInfo

    @property
    def VocabLibName(self):
        """词汇库名
        :rtype: str
        """
        return self._VocabLibName

    @VocabLibName.setter
    def VocabLibName(self, VocabLibName):
        self._VocabLibName = VocabLibName


    def _deserialize(self, params):
        if params.get("VocabDetailInfo") is not None:
            self._VocabDetailInfo = []
            for item in params.get("VocabDetailInfo"):
                obj = DetailInfo()
                obj._deserialize(item)
                self._VocabDetailInfo.append(obj)
        self._VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VocabStatInfomation(AbstractModel):
    """词汇库中的单词出现在音频中的总次数信息

    """

    def __init__(self):
        r"""
        :param _VocabDetailInfo: 单词出现在该音频中总次数
        :type VocabDetailInfo: list of StatInfo
        :param _VocabLibName: 词汇库名称
        :type VocabLibName: str
        """
        self._VocabDetailInfo = None
        self._VocabLibName = None

    @property
    def VocabDetailInfo(self):
        """单词出现在该音频中总次数
        :rtype: list of StatInfo
        """
        return self._VocabDetailInfo

    @VocabDetailInfo.setter
    def VocabDetailInfo(self, VocabDetailInfo):
        self._VocabDetailInfo = VocabDetailInfo

    @property
    def VocabLibName(self):
        """词汇库名称
        :rtype: str
        """
        return self._VocabLibName

    @VocabLibName.setter
    def VocabLibName(self, VocabLibName):
        self._VocabLibName = VocabLibName


    def _deserialize(self, params):
        if params.get("VocabDetailInfo") is not None:
            self._VocabDetailInfo = []
            for item in params.get("VocabDetailInfo"):
                obj = StatInfo()
                obj._deserialize(item)
                self._VocabDetailInfo.append(obj)
        self._VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WholeTextItem(AbstractModel):
    """含有语速的句子信息

    """

    def __init__(self):
        r"""
        :param _TextItem: 当前句子的信息
        :type TextItem: :class:`tencentcloud.tci.v20190318.models.TextItem`
        :param _AvgVolume: Vad的平均音量
        :type AvgVolume: float
        :param _MaxVolume: Vad的最大音量
        :type MaxVolume: float
        :param _MinVolume: Vad的最小音量
        :type MinVolume: float
        :param _Speed: 当前句子的语速
        :type Speed: float
        """
        self._TextItem = None
        self._AvgVolume = None
        self._MaxVolume = None
        self._MinVolume = None
        self._Speed = None

    @property
    def TextItem(self):
        """当前句子的信息
        :rtype: :class:`tencentcloud.tci.v20190318.models.TextItem`
        """
        return self._TextItem

    @TextItem.setter
    def TextItem(self, TextItem):
        self._TextItem = TextItem

    @property
    def AvgVolume(self):
        """Vad的平均音量
        :rtype: float
        """
        return self._AvgVolume

    @AvgVolume.setter
    def AvgVolume(self, AvgVolume):
        self._AvgVolume = AvgVolume

    @property
    def MaxVolume(self):
        """Vad的最大音量
        :rtype: float
        """
        return self._MaxVolume

    @MaxVolume.setter
    def MaxVolume(self, MaxVolume):
        self._MaxVolume = MaxVolume

    @property
    def MinVolume(self):
        """Vad的最小音量
        :rtype: float
        """
        return self._MinVolume

    @MinVolume.setter
    def MinVolume(self, MinVolume):
        self._MinVolume = MinVolume

    @property
    def Speed(self):
        """当前句子的语速
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed


    def _deserialize(self, params):
        if params.get("TextItem") is not None:
            self._TextItem = TextItem()
            self._TextItem._deserialize(params.get("TextItem"))
        self._AvgVolume = params.get("AvgVolume")
        self._MaxVolume = params.get("MaxVolume")
        self._MinVolume = params.get("MinVolume")
        self._Speed = params.get("Speed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Word(AbstractModel):
    """当前句子包含的所有单词信息

    """

    def __init__(self):
        r"""
        :param _Confidence: 当前词的置信度
        :type Confidence: float
        :param _Mbtm: 当前单词语音的起始时间点，单位为ms
        :type Mbtm: int
        :param _Metm: 当前单词语音的终止时间点，单位为ms
        :type Metm: int
        :param _Text: 当前词
        :type Text: str
        :param _Wsize: 当前词的字节数
        :type Wsize: int
        """
        self._Confidence = None
        self._Mbtm = None
        self._Metm = None
        self._Text = None
        self._Wsize = None

    @property
    def Confidence(self):
        """当前词的置信度
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Mbtm(self):
        """当前单词语音的起始时间点，单位为ms
        :rtype: int
        """
        return self._Mbtm

    @Mbtm.setter
    def Mbtm(self, Mbtm):
        self._Mbtm = Mbtm

    @property
    def Metm(self):
        """当前单词语音的终止时间点，单位为ms
        :rtype: int
        """
        return self._Metm

    @Metm.setter
    def Metm(self, Metm):
        self._Metm = Metm

    @property
    def Text(self):
        """当前词
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Wsize(self):
        """当前词的字节数
        :rtype: int
        """
        return self._Wsize

    @Wsize.setter
    def Wsize(self, Wsize):
        self._Wsize = Wsize


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Mbtm = params.get("Mbtm")
        self._Metm = params.get("Metm")
        self._Text = params.get("Text")
        self._Wsize = params.get("Wsize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordTimePair(AbstractModel):
    """单词出现的那个句子的起始时间和结束时间信息

    """

    def __init__(self):
        r"""
        :param _Mbtm: 单词出现的那个句子的起始时间
        :type Mbtm: int
        :param _Metm: 	单词出现的那个句子的结束时间
        :type Metm: int
        """
        self._Mbtm = None
        self._Metm = None

    @property
    def Mbtm(self):
        """单词出现的那个句子的起始时间
        :rtype: int
        """
        return self._Mbtm

    @Mbtm.setter
    def Mbtm(self, Mbtm):
        self._Mbtm = Mbtm

    @property
    def Metm(self):
        """	单词出现的那个句子的结束时间
        :rtype: int
        """
        return self._Metm

    @Metm.setter
    def Metm(self, Metm):
        self._Metm = Metm


    def _deserialize(self, params):
        self._Mbtm = params.get("Mbtm")
        self._Metm = params.get("Metm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        