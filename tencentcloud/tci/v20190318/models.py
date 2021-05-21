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


class AIAssistantRequest(AbstractModel):
    """AIAssistant请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，audio_url: 音频文件，picture：图片二进制数据的BASE64编码
        :type FileType: str
        :param Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param LibrarySet: 查询人员库列表
        :type LibrarySet: list of str
        :param MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param Template: 标准化模板选择：0：AI助教基础版本，1：AI评教基础版本，2：AI评教标准版本。AI 助教基础版本功能包括：人脸检索、人脸检测、人脸表情识别、学生动作选项，音频信息分析，微笑识别。AI 评教基础版本功能包括：人脸检索、人脸检测、人脸表情识别、音频信息分析。AI 评教标准版功能包括人脸检索、人脸检测、人脸表情识别、手势识别、音频信息分析、音频关键词分析、视频精彩集锦分析。
        :type Template: int
        :param VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :type VocabLibNameList: list of str
        :param VoiceEncodeType: 语音编码类型 1:pcm
        :type VoiceEncodeType: int
        :param VoiceFileType: 语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）
        :type VoiceFileType: int
        """
        self.FileContent = None
        self.FileType = None
        self.Lang = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.Template = None
        self.VocabLibNameList = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.Lang = params.get("Lang")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.Template = params.get("Template")
        self.VocabLibNameList = params.get("VocabLibNameList")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AIAssistantResponse(AbstractModel):
    """AIAssistant返回参数结构体

    """

    def __init__(self):
        """
        :param ImageResults: 图像任务直接返回结果
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ASRStat(AbstractModel):
    """当前音频的统计结果

    """

    def __init__(self):
        """
        :param AvgSpeed: 当前音频的平均语速
        :type AvgSpeed: float
        :param AvgVolume: Vad的平均音量
        :type AvgVolume: float
        :param MaxVolume: Vad的最大音量
        :type MaxVolume: float
        :param MinVolume: Vad的最小音量
        :type MinVolume: float
        :param MuteDuration: 当前音频的非发音时长
        :type MuteDuration: int
        :param SoundDuration: 当前音频的发音时长
        :type SoundDuration: int
        :param TotalDuration: 当前音频的总时长
        :type TotalDuration: int
        :param VadNum: 当前音频的句子总数
        :type VadNum: int
        :param WordNum: 当前音频的单词总数
        :type WordNum: int
        """
        self.AvgSpeed = None
        self.AvgVolume = None
        self.MaxVolume = None
        self.MinVolume = None
        self.MuteDuration = None
        self.SoundDuration = None
        self.TotalDuration = None
        self.VadNum = None
        self.WordNum = None


    def _deserialize(self, params):
        self.AvgSpeed = params.get("AvgSpeed")
        self.AvgVolume = params.get("AvgVolume")
        self.MaxVolume = params.get("MaxVolume")
        self.MinVolume = params.get("MinVolume")
        self.MuteDuration = params.get("MuteDuration")
        self.SoundDuration = params.get("SoundDuration")
        self.TotalDuration = params.get("TotalDuration")
        self.VadNum = params.get("VadNum")
        self.WordNum = params.get("WordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AbsenceInfo(AbstractModel):
    """缺勤人员信息

    """

    def __init__(self):
        """
        :param LibraryIds: 识别到的人员所在的库id
        :type LibraryIds: str
        :param PersonId: 识别到的人员id
        :type PersonId: str
        """
        self.LibraryIds = None
        self.PersonId = None


    def _deserialize(self, params):
        self.LibraryIds = params.get("LibraryIds")
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ActionCountStatistic(AbstractModel):
    """数量统计结果

    """

    def __init__(self):
        """
        :param Count: 数量
        :type Count: int
        :param Name: 名称
        :type Name: str
        """
        self.Count = None
        self.Name = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ActionDurationRatioStatistic(AbstractModel):
    """时长占比统计结果

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Ratio: 比例
        :type Ratio: float
        """
        self.Name = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ActionDurationStatistic(AbstractModel):
    """时长统计结果

    """

    def __init__(self):
        """
        :param Duration: 时长
        :type Duration: int
        :param Name: 名称
        :type Name: str
        """
        self.Duration = None
        self.Name = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ActionInfo(AbstractModel):
    """大教室场景肢体动作识别信息

    """

    def __init__(self):
        """
        :param BodyPosture: 躯体动作识别结果，包含坐着（sit）、站立（stand）和趴睡（sleep）
        :type BodyPosture: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param Handup: 举手识别结果，包含举手（hand）和未检测到举手（nothand）
        :type Handup: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param LookHead: 是否低头识别结果，包含抬头（lookingahead）和未检测到抬头（notlookingahead）
        :type LookHead: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param Writing: 是否写字识别结果，包含写字（write）和未检测到写字（notlookingahead）
        :type Writing: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param Height: 动作图像高度
        :type Height: int
        :param Left: 动作出现图像的左侧起始坐标位置
        :type Left: int
        :param Top: 动作出现图像的上侧起始侧坐标位置
        :type Top: int
        :param Width: 动作图像宽度
        :type Width: int
        """
        self.BodyPosture = None
        self.Handup = None
        self.LookHead = None
        self.Writing = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        if params.get("BodyPosture") is not None:
            self.BodyPosture = ActionType()
            self.BodyPosture._deserialize(params.get("BodyPosture"))
        if params.get("Handup") is not None:
            self.Handup = ActionType()
            self.Handup._deserialize(params.get("Handup"))
        if params.get("LookHead") is not None:
            self.LookHead = ActionType()
            self.LookHead._deserialize(params.get("LookHead"))
        if params.get("Writing") is not None:
            self.Writing = ActionType()
            self.Writing._deserialize(params.get("Writing"))
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ActionStatistic(AbstractModel):
    """统计结果

    """

    def __init__(self):
        """
        :param ActionCount: 数量统计
        :type ActionCount: list of ActionCountStatistic
        :param ActionDuration: 时长统计
        :type ActionDuration: list of ActionDurationStatistic
        :param ActionDurationRatio: 时长比例统计
        :type ActionDurationRatio: list of ActionDurationRatioStatistic
        """
        self.ActionCount = None
        self.ActionDuration = None
        self.ActionDurationRatio = None


    def _deserialize(self, params):
        if params.get("ActionCount") is not None:
            self.ActionCount = []
            for item in params.get("ActionCount"):
                obj = ActionCountStatistic()
                obj._deserialize(item)
                self.ActionCount.append(obj)
        if params.get("ActionDuration") is not None:
            self.ActionDuration = []
            for item in params.get("ActionDuration"):
                obj = ActionDurationStatistic()
                obj._deserialize(item)
                self.ActionDuration.append(obj)
        if params.get("ActionDurationRatio") is not None:
            self.ActionDurationRatio = []
            for item in params.get("ActionDurationRatio"):
                obj = ActionDurationRatioStatistic()
                obj._deserialize(item)
                self.ActionDurationRatio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ActionType(AbstractModel):
    """动作行为子类型

    """

    def __init__(self):
        """
        :param Confidence: 置信度
        :type Confidence: float
        :param Type: 动作类别
        :type Type: str
        """
        self.Confidence = None
        self.Type = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AllMuteSlice(AbstractModel):
    """如果请求中开启了静音检测开关，则会返回所有的静音片段（静音时长超过阈值的片段）。

    """

    def __init__(self):
        """
        :param MuteSlice: 所有静音片段。
        :type MuteSlice: list of MuteSlice
        :param MuteRatio: 静音时长占比。
        :type MuteRatio: float
        :param TotalMuteDuration: 静音总时长。
        :type TotalMuteDuration: int
        """
        self.MuteSlice = None
        self.MuteRatio = None
        self.TotalMuteDuration = None


    def _deserialize(self, params):
        if params.get("MuteSlice") is not None:
            self.MuteSlice = []
            for item in params.get("MuteSlice"):
                obj = MuteSlice()
                obj._deserialize(item)
                self.MuteSlice.append(obj)
        self.MuteRatio = params.get("MuteRatio")
        self.TotalMuteDuration = params.get("TotalMuteDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AttendanceInfo(AbstractModel):
    """识别到的人员信息

    """

    def __init__(self):
        """
        :param Face: 识别到的人员信息
        :type Face: :class:`tencentcloud.tci.v20190318.models.FrameInfo`
        :param PersonId: 识别到的人员id
        :type PersonId: str
        """
        self.Face = None
        self.PersonId = None


    def _deserialize(self, params):
        if params.get("Face") is not None:
            self.Face = FrameInfo()
            self.Face._deserialize(params.get("Face"))
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BodyMovementResult(AbstractModel):
    """老师肢体动作识别结果

    """

    def __init__(self):
        """
        :param Confidence: 置信度
        :type Confidence: float
        :param Height: 识别结果高度
        :type Height: int
        :param Left: 识别结果左坐标
        :type Left: int
        :param Movements: 老师动作识别结果，包含
1、teach_on_positive_attitude 正面讲解
2、point_to_the_blackboard 指黑板
3、writing_blackboard 写板书
4、other 其他
        :type Movements: str
        :param Top: 识别结果顶坐标
        :type Top: int
        :param Width: 识别结果宽度
        :type Width: int
        """
        self.Confidence = None
        self.Height = None
        self.Left = None
        self.Movements = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Movements = params.get("Movements")
        self.Top = params.get("Top")
        self.Width = params.get("Width")
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
        :param JobId: 待取消任务标志符。
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
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
        :param JobId: 取消任务标志符。
        :type JobId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CheckFacePhotoRequest(AbstractModel):
    """CheckFacePhoto请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容
        :type FileContent: str
        :param FileType: 输入分析对象类型，picture_url:图片地址
        :type FileType: str
        """
        self.FileContent = None
        self.FileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CheckFacePhotoResponse(AbstractModel):
    """CheckFacePhoto返回参数结构体

    """

    def __init__(self):
        """
        :param CheckResult: 人脸检查结果，0：通过检查，1：图片模糊
        :type CheckResult: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckResult = params.get("CheckResult")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateFaceRequest(AbstractModel):
    """CreateFace请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param Images: 图片数据 base64 字符串，与 Urls 参数选择一个输入
        :type Images: list of str
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param Urls: 图片下载地址，与 Images 参数选择一个输入
        :type Urls: list of str
        """
        self.PersonId = None
        self.Images = None
        self.LibraryId = None
        self.Urls = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Images = params.get("Images")
        self.LibraryId = params.get("LibraryId")
        self.Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateFaceResponse(AbstractModel):
    """CreateFace返回参数结构体

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人脸操作结果信息
        :type FaceInfoSet: list of FaceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLibraryRequest(AbstractModel):
    """CreateLibrary请求参数结构体

    """

    def __init__(self):
        """
        :param LibraryName: 人员库名称
        :type LibraryName: str
        :param LibraryId: 人员库唯一标志符，为空则系统自动生成。
        :type LibraryId: str
        """
        self.LibraryName = None
        self.LibraryId = None


    def _deserialize(self, params):
        self.LibraryName = params.get("LibraryName")
        self.LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLibraryResponse(AbstractModel):
    """CreateLibrary返回参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param LibraryName: 人员库名称
        :type LibraryName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LibraryId = None
        self.LibraryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePersonRequest(AbstractModel):
    """CreatePerson请求参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param PersonName: 人员名称
        :type PersonName: str
        :param Images: 图片数据 base64 字符串，与 Urls 参数选择一个输入
        :type Images: list of str
        :param JobNumber: 人员工作号码
        :type JobNumber: str
        :param Mail: 人员邮箱
        :type Mail: str
        :param Male: 人员性别，0：未知 1：男性，2：女性
        :type Male: int
        :param PersonId: 自定义人员 ID，注意不能使用 tci_person_ 前缀
        :type PersonId: str
        :param PhoneNumber: 人员电话号码
        :type PhoneNumber: str
        :param StudentNumber: 人员学生号码
        :type StudentNumber: str
        :param Urls: 图片下载地址，与 Images 参数选择一个输入
        :type Urls: list of str
        """
        self.LibraryId = None
        self.PersonName = None
        self.Images = None
        self.JobNumber = None
        self.Mail = None
        self.Male = None
        self.PersonId = None
        self.PhoneNumber = None
        self.StudentNumber = None
        self.Urls = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonName = params.get("PersonName")
        self.Images = params.get("Images")
        self.JobNumber = params.get("JobNumber")
        self.Mail = params.get("Mail")
        self.Male = params.get("Male")
        self.PersonId = params.get("PersonId")
        self.PhoneNumber = params.get("PhoneNumber")
        self.StudentNumber = params.get("StudentNumber")
        self.Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回参数结构体

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人脸操作结果信息
        :type FaceInfoSet: list of FaceInfo
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param PersonName: 人员名称
        :type PersonName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.LibraryId = None
        self.PersonId = None
        self.PersonName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateVocabLibRequest(AbstractModel):
    """CreateVocabLib请求参数结构体

    """

    def __init__(self):
        """
        :param VocabLibName: 词汇库名称
        :type VocabLibName: str
        """
        self.VocabLibName = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateVocabLibResponse(AbstractModel):
    """CreateVocabLib返回参数结构体

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
        


class CreateVocabRequest(AbstractModel):
    """CreateVocab请求参数结构体

    """

    def __init__(self):
        """
        :param VocabLibName: 要添加词汇的词汇库名
        :type VocabLibName: str
        :param VocabList: 要添加的词汇列表
        :type VocabList: list of str
        """
        self.VocabLibName = None
        self.VocabList = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")
        self.VocabList = params.get("VocabList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateVocabResponse(AbstractModel):
    """CreateVocab返回参数结构体

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
        


class DeleteFaceRequest(AbstractModel):
    """DeleteFace请求参数结构体

    """

    def __init__(self):
        """
        :param FaceIdSet: 人脸标识符数组
        :type FaceIdSet: list of str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        """
        self.FaceIdSet = None
        self.PersonId = None
        self.LibraryId = None


    def _deserialize(self, params):
        self.FaceIdSet = params.get("FaceIdSet")
        self.PersonId = params.get("PersonId")
        self.LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteFaceResponse(AbstractModel):
    """DeleteFace返回参数结构体

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人脸操作结果
        :type FaceInfoSet: list of FaceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLibraryRequest(AbstractModel):
    """DeleteLibrary请求参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        """
        self.LibraryId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLibraryResponse(AbstractModel):
    """DeleteLibrary返回参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param LibraryName: 人员库名称
        :type LibraryName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LibraryId = None
        self.LibraryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePersonRequest(AbstractModel):
    """DeletePerson请求参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        """
        self.LibraryId = None
        self.PersonId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回参数结构体

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人脸信息
        :type FaceInfoSet: list of FaceInfo
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param PersonName: 人员名称
        :type PersonName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.LibraryId = None
        self.PersonId = None
        self.PersonName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteVocabLibRequest(AbstractModel):
    """DeleteVocabLib请求参数结构体

    """

    def __init__(self):
        """
        :param VocabLibName: 词汇库名称
        :type VocabLibName: str
        """
        self.VocabLibName = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteVocabLibResponse(AbstractModel):
    """DeleteVocabLib返回参数结构体

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
        


class DeleteVocabRequest(AbstractModel):
    """DeleteVocab请求参数结构体

    """

    def __init__(self):
        """
        :param VocabLibName: 要删除词汇的词汇库名
        :type VocabLibName: str
        :param VocabList: 要删除的词汇列表
        :type VocabList: list of str
        """
        self.VocabLibName = None
        self.VocabList = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")
        self.VocabList = params.get("VocabList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteVocabResponse(AbstractModel):
    """DeleteVocab返回参数结构体

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
        


class DescribeAITaskResultRequest(AbstractModel):
    """DescribeAITaskResult请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务唯一标识符。在URL方式时提交请求后会返回一个任务标识符，后续查询该url的结果时使用这个标识符进行查询。
        :type TaskId: int
        :param Limit: 限制数目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.TaskId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAITaskResultResponse(AbstractModel):
    """DescribeAITaskResult返回参数结构体

    """

    def __init__(self):
        """
        :param AudioResult: 音频分析结果
        :type AudioResult: :class:`tencentcloud.tci.v20190318.models.StandardAudioResult`
        :param ImageResult: 图像分析结果
        :type ImageResult: :class:`tencentcloud.tci.v20190318.models.StandardImageResult`
        :param VideoResult: 视频分析结果
        :type VideoResult: :class:`tencentcloud.tci.v20190318.models.StandardVideoResult`
        :param Status: 任务状态
        :type Status: str
        :param TaskId: 任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AudioResult = None
        self.ImageResult = None
        self.VideoResult = None
        self.Status = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AudioResult") is not None:
            self.AudioResult = StandardAudioResult()
            self.AudioResult._deserialize(params.get("AudioResult"))
        if params.get("ImageResult") is not None:
            self.ImageResult = StandardImageResult()
            self.ImageResult._deserialize(params.get("ImageResult"))
        if params.get("VideoResult") is not None:
            self.VideoResult = StandardVideoResult()
            self.VideoResult._deserialize(params.get("VideoResult"))
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAttendanceResultRequest(AbstractModel):
    """DescribeAttendanceResult请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 任务唯一标识符
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAttendanceResultResponse(AbstractModel):
    """DescribeAttendanceResult返回参数结构体

    """

    def __init__(self):
        """
        :param AbsenceSetInLibs: 缺失人员的ID列表(只针对请求中的libids字段)
        :type AbsenceSetInLibs: list of AbsenceInfo
        :param AttendanceSet: 确定出勤人员列表
        :type AttendanceSet: list of AttendanceInfo
        :param SuspectedSet: 疑似出勤人员列表
        :type SuspectedSet: list of SuspectedInfo
        :param AbsenceSet: 缺失人员的ID列表(只针对请求中的personids字段)
        :type AbsenceSet: list of str
        :param Progress: 请求处理进度
        :type Progress: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AbsenceSetInLibs = None
        self.AttendanceSet = None
        self.SuspectedSet = None
        self.AbsenceSet = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AbsenceSetInLibs") is not None:
            self.AbsenceSetInLibs = []
            for item in params.get("AbsenceSetInLibs"):
                obj = AbsenceInfo()
                obj._deserialize(item)
                self.AbsenceSetInLibs.append(obj)
        if params.get("AttendanceSet") is not None:
            self.AttendanceSet = []
            for item in params.get("AttendanceSet"):
                obj = AttendanceInfo()
                obj._deserialize(item)
                self.AttendanceSet.append(obj)
        if params.get("SuspectedSet") is not None:
            self.SuspectedSet = []
            for item in params.get("SuspectedSet"):
                obj = SuspectedInfo()
                obj._deserialize(item)
                self.SuspectedSet.append(obj)
        self.AbsenceSet = params.get("AbsenceSet")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAudioTaskRequest(AbstractModel):
    """DescribeAudioTask请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param Limit: 限制数目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.JobId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAudioTaskResponse(AbstractModel):
    """DescribeAudioTask返回参数结构体

    """

    def __init__(self):
        """
        :param AllMuteSlice: 如果请求中开启了静音检测开关，则会返回所有的静音片段（静音时长超过阈值的片段）。
        :type AllMuteSlice: :class:`tencentcloud.tci.v20190318.models.AllMuteSlice`
        :param AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :type Texts: list of WholeTextItem
        :param VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param AllTexts: 返回音频全部文本。
        :type AllTexts: str
        :param JobId: 音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param Progress: 返回的当前处理进度。
        :type Progress: float
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllMuteSlice = None
        self.AsrStat = None
        self.Texts = None
        self.VocabAnalysisDetailInfo = None
        self.VocabAnalysisStatInfo = None
        self.AllTexts = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AllMuteSlice") is not None:
            self.AllMuteSlice = AllMuteSlice()
            self.AllMuteSlice._deserialize(params.get("AllMuteSlice"))
        if params.get("AsrStat") is not None:
            self.AsrStat = ASRStat()
            self.AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self.Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self.Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self.VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self.VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self.VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self.VocabAnalysisStatInfo.append(obj)
        self.AllTexts = params.get("AllTexts")
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeConversationTaskRequest(AbstractModel):
    """DescribeConversationTask请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param Identity: 要查询明细的流的身份，1 老师 2 学生
        :type Identity: int
        :param Limit: 限制数目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.JobId = None
        self.Identity = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Identity = params.get("Identity")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeConversationTaskResponse(AbstractModel):
    """DescribeConversationTask返回参数结构体

    """

    def __init__(self):
        """
        :param AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :type Texts: list of WholeTextItem
        :param VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param AllTexts: 整个音频流的全部文本
        :type AllTexts: str
        :param JobId: 音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param Progress: 返回的当前处理进度。
        :type Progress: float
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsrStat = None
        self.Texts = None
        self.VocabAnalysisDetailInfo = None
        self.VocabAnalysisStatInfo = None
        self.AllTexts = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self.AsrStat = ASRStat()
            self.AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self.Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self.Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self.VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self.VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self.VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self.VocabAnalysisStatInfo.append(obj)
        self.AllTexts = params.get("AllTexts")
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeHighlightResultRequest(AbstractModel):
    """DescribeHighlightResult请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 精彩集锦任务唯一id。在URL方式时提交请求后会返回一个JobId，后续查询该url的结果时使用这个JobId进行查询。
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeHighlightResultResponse(AbstractModel):
    """DescribeHighlightResult返回参数结构体

    """

    def __init__(self):
        """
        :param HighlightsInfo: 精彩集锦详细信息。
        :type HighlightsInfo: list of HighlightsInfomation
        :param JobId: 精彩集锦任务唯一id。在URL方式时提交请求后会返回一个JobId，后续查询该url的结果时使用这个JobId进行查询。
        :type JobId: int
        :param Progress: 任务的进度百分比，100表示任务已完成。
        :type Progress: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HighlightsInfo = None
        self.JobId = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HighlightsInfo") is not None:
            self.HighlightsInfo = []
            for item in params.get("HighlightsInfo"):
                obj = HighlightsInfomation()
                obj._deserialize(item)
                self.HighlightsInfo.append(obj)
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageTaskRequest(AbstractModel):
    """DescribeImageTask请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 任务标识符
        :type JobId: int
        :param Limit: 限制数目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.JobId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageTaskResponse(AbstractModel):
    """DescribeImageTask返回参数结构体

    """

    def __init__(self):
        """
        :param ResultSet: 任务处理结果
        :type ResultSet: list of ImageTaskResult
        :param JobId: 任务唯一标识
        :type JobId: int
        :param Progress: 任务执行进度
        :type Progress: int
        :param TotalCount: 任务结果数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultSet = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageTaskStatisticRequest(AbstractModel):
    """DescribeImageTaskStatistic请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 图像任务标识符
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageTaskStatisticResponse(AbstractModel):
    """DescribeImageTaskStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param Statistic: 任务统计信息
        :type Statistic: :class:`tencentcloud.tci.v20190318.models.ImageTaskStatistic`
        :param JobId: 图像任务唯一标识符
        :type JobId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Statistic = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Statistic") is not None:
            self.Statistic = ImageTaskStatistic()
            self.Statistic._deserialize(params.get("Statistic"))
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLibrariesRequest(AbstractModel):
    """DescribeLibraries请求参数结构体

    """


class DescribeLibrariesResponse(AbstractModel):
    """DescribeLibraries返回参数结构体

    """

    def __init__(self):
        """
        :param LibrarySet: 人员库列表
        :type LibrarySet: list of Library
        :param TotalCount: 人员库总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LibrarySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LibrarySet") is not None:
            self.LibrarySet = []
            for item in params.get("LibrarySet"):
                obj = Library()
                obj._deserialize(item)
                self.LibrarySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePersonRequest(AbstractModel):
    """DescribePerson请求参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        """
        self.LibraryId = None
        self.PersonId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePersonResponse(AbstractModel):
    """DescribePerson返回参数结构体

    """

    def __init__(self):
        """
        :param FaceSet: 人员人脸列表
        :type FaceSet: list of Face
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param JobNumber: 工作号码
        :type JobNumber: str
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param Mail: 邮箱
        :type Mail: str
        :param Male: 性别
        :type Male: int
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param PersonName: 人员名称
        :type PersonName: str
        :param PhoneNumber: 电话号码
        :type PhoneNumber: str
        :param StudentNumber: 学生号码
        :type StudentNumber: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceSet = None
        self.CreateTime = None
        self.JobNumber = None
        self.LibraryId = None
        self.Mail = None
        self.Male = None
        self.PersonId = None
        self.PersonName = None
        self.PhoneNumber = None
        self.StudentNumber = None
        self.UpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceSet") is not None:
            self.FaceSet = []
            for item in params.get("FaceSet"):
                obj = Face()
                obj._deserialize(item)
                self.FaceSet.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.JobNumber = params.get("JobNumber")
        self.LibraryId = params.get("LibraryId")
        self.Mail = params.get("Mail")
        self.Male = params.get("Male")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.StudentNumber = params.get("StudentNumber")
        self.UpdateTime = params.get("UpdateTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePersonsRequest(AbstractModel):
    """DescribePersons请求参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param Limit: 限制数目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.LibraryId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePersonsResponse(AbstractModel):
    """DescribePersons返回参数结构体

    """

    def __init__(self):
        """
        :param PersonSet: 人员列表
        :type PersonSet: list of Person
        :param TotalCount: 人员总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = Person()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeVocabLibRequest(AbstractModel):
    """DescribeVocabLib请求参数结构体

    """


class DescribeVocabLibResponse(AbstractModel):
    """DescribeVocabLib返回参数结构体

    """

    def __init__(self):
        """
        :param VocabLibNameSet: 返回该appid下的所有词汇库名
        :type VocabLibNameSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VocabLibNameSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabLibNameSet = params.get("VocabLibNameSet")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeVocabRequest(AbstractModel):
    """DescribeVocab请求参数结构体

    """

    def __init__(self):
        """
        :param VocabLibName: 要查询词汇的词汇库名
        :type VocabLibName: str
        """
        self.VocabLibName = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeVocabResponse(AbstractModel):
    """DescribeVocab返回参数结构体

    """

    def __init__(self):
        """
        :param VocabNameSet: 词汇列表
        :type VocabNameSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VocabNameSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabNameSet = params.get("VocabNameSet")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DetailInfo(AbstractModel):
    """单词出现的那个句子的起始时间和结束时间信息

    """

    def __init__(self):
        """
        :param Value: 单词出现在该音频中的那个句子的时间戳，出现了几次， 就返回对应次数的起始和结束时间戳
        :type Value: list of WordTimePair
        :param Keyword: 词汇库中的单词
        :type Keyword: str
        """
        self.Value = None
        self.Keyword = None


    def _deserialize(self, params):
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = WordTimePair()
                obj._deserialize(item)
                self.Value.append(obj)
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DoubleVideoFunction(AbstractModel):
    """双路混流视频集锦开关项

    """

    def __init__(self):
        """
        :param EnableCoverPictures: 片头片尾增加图片开关
        :type EnableCoverPictures: bool
        """
        self.EnableCoverPictures = None


    def _deserialize(self, params):
        self.EnableCoverPictures = params.get("EnableCoverPictures")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExpressRatioStatistic(AbstractModel):
    """表情比例统计

    """

    def __init__(self):
        """
        :param Count: 出现次数
        :type Count: int
        :param Express: 表情
        :type Express: str
        :param Ratio: 该表情时长占所有表情时长的比例
        :type Ratio: float
        :param RatioUseDuration: 该表情时长占视频总时长的比例
        :type RatioUseDuration: float
        """
        self.Count = None
        self.Express = None
        self.Ratio = None
        self.RatioUseDuration = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Express = params.get("Express")
        self.Ratio = params.get("Ratio")
        self.RatioUseDuration = params.get("RatioUseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Face(AbstractModel):
    """人脸描述

    """

    def __init__(self):
        """
        :param FaceId: 人脸唯一标识符
        :type FaceId: str
        :param FaceUrl: 人脸图片 URL
        :type FaceUrl: str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        """
        self.FaceId = None
        self.FaceUrl = None
        self.PersonId = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.FaceUrl = params.get("FaceUrl")
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceAttrResult(AbstractModel):
    """FaceAttrResult

    """

    def __init__(self):
        """
        :param Age: 年龄
        :type Age: int
        :param Sex: 性别
        :type Sex: str
        """
        self.Age = None
        self.Sex = None


    def _deserialize(self, params):
        self.Age = params.get("Age")
        self.Sex = params.get("Sex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceDetectStatistic(AbstractModel):
    """人脸监测统计信息

    """

    def __init__(self):
        """
        :param FaceSizeRatio: 人脸大小占画面平均占比
        :type FaceSizeRatio: float
        :param FrontalFaceCount: 检测到正脸次数
        :type FrontalFaceCount: int
        :param FrontalFaceRatio: 正脸时长占比
        :type FrontalFaceRatio: float
        :param FrontalFaceRealRatio: 正脸时长在总出现时常占比
        :type FrontalFaceRealRatio: float
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param SideFaceCount: 检测到侧脸次数
        :type SideFaceCount: int
        :param SideFaceRatio: 侧脸时长占比
        :type SideFaceRatio: float
        :param SideFaceRealRatio: 侧脸时长在总出现时常占比
        :type SideFaceRealRatio: float
        """
        self.FaceSizeRatio = None
        self.FrontalFaceCount = None
        self.FrontalFaceRatio = None
        self.FrontalFaceRealRatio = None
        self.PersonId = None
        self.SideFaceCount = None
        self.SideFaceRatio = None
        self.SideFaceRealRatio = None


    def _deserialize(self, params):
        self.FaceSizeRatio = params.get("FaceSizeRatio")
        self.FrontalFaceCount = params.get("FrontalFaceCount")
        self.FrontalFaceRatio = params.get("FrontalFaceRatio")
        self.FrontalFaceRealRatio = params.get("FrontalFaceRealRatio")
        self.PersonId = params.get("PersonId")
        self.SideFaceCount = params.get("SideFaceCount")
        self.SideFaceRatio = params.get("SideFaceRatio")
        self.SideFaceRealRatio = params.get("SideFaceRealRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceExpressStatistic(AbstractModel):
    """人脸表情统计结果

    """

    def __init__(self):
        """
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param ExpressRatio: 表情统计结果
        :type ExpressRatio: list of ExpressRatioStatistic
        """
        self.PersonId = None
        self.ExpressRatio = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        if params.get("ExpressRatio") is not None:
            self.ExpressRatio = []
            for item in params.get("ExpressRatio"):
                obj = ExpressRatioStatistic()
                obj._deserialize(item)
                self.ExpressRatio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceExpressionResult(AbstractModel):
    """FaceExpressionResult

    """

    def __init__(self):
        """
        :param Confidence: 表情置信度
        :type Confidence: float
        :param Expression: 表情识别结果，包括"neutral":中性,"happiness":开心，"angry":"生气"，"disgust":厌恶，"fear":"恐惧"，"sadness":"悲伤"，"surprise":"惊讶"，"contempt":"蔑视"
        :type Expression: str
        """
        self.Confidence = None
        self.Expression = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceIdentifyResult(AbstractModel):
    """FaceIdentifyResult

    """

    def __init__(self):
        """
        :param FaceId: 人脸标识符
        :type FaceId: str
        :param LibraryId: 人员库标识符
        :type LibraryId: str
        :param PersonId: 人员标识符
        :type PersonId: str
        :param Similarity: 相似度
        :type Similarity: float
        """
        self.FaceId = None
        self.LibraryId = None
        self.PersonId = None
        self.Similarity = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.Similarity = params.get("Similarity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceIdentifyStatistic(AbstractModel):
    """人员检索统计结果

    """

    def __init__(self):
        """
        :param Duration: 持续时间
        :type Duration: int
        :param EndTs: 结束时间
        :type EndTs: int
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param Similarity: 相似度
        :type Similarity: float
        :param StartTs: 开始时间
        :type StartTs: int
        """
        self.Duration = None
        self.EndTs = None
        self.PersonId = None
        self.Similarity = None
        self.StartTs = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.EndTs = params.get("EndTs")
        self.PersonId = params.get("PersonId")
        self.Similarity = params.get("Similarity")
        self.StartTs = params.get("StartTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceInfo(AbstractModel):
    """人脸操作信息

    """

    def __init__(self):
        """
        :param ErrorCode: 人脸操作错误码
        :type ErrorCode: str
        :param ErrorMsg: 人脸操作结果信息
        :type ErrorMsg: str
        :param FaceId: 人脸唯一标识符
        :type FaceId: str
        :param FaceUrl: 人脸保存地址
        :type FaceUrl: str
        :param PersonId: 人员唯一标识
        :type PersonId: str
        """
        self.ErrorCode = None
        self.ErrorMsg = None
        self.FaceId = None
        self.FaceUrl = None
        self.PersonId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        self.FaceId = params.get("FaceId")
        self.FaceUrl = params.get("FaceUrl")
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceInfoResult(AbstractModel):
    """FaceInfoResult

    """

    def __init__(self):
        """
        :param FaceRatio: 人脸尺寸的占比
        :type FaceRatio: float
        :param FrameHeight: 帧高度
        :type FrameHeight: int
        :param FrameWidth: 帧宽度
        :type FrameWidth: int
        :param Height: 人脸高度
        :type Height: int
        :param Left: 人脸左坐标
        :type Left: int
        :param Top: 人脸顶坐标
        :type Top: int
        :param Width: 人脸宽度
        :type Width: int
        """
        self.FaceRatio = None
        self.FrameHeight = None
        self.FrameWidth = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.FaceRatio = params.get("FaceRatio")
        self.FrameHeight = params.get("FrameHeight")
        self.FrameWidth = params.get("FrameWidth")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FacePoseResult(AbstractModel):
    """FacePoseResult

    """

    def __init__(self):
        """
        :param Direction: 正脸或侧脸的消息
        :type Direction: str
        :param Pitch: 围绕Z轴旋转角度，俯仰角
        :type Pitch: float
        :param Roll: 围绕X轴旋转角度，翻滚角
        :type Roll: float
        :param Yaw: 围绕Y轴旋转角度，偏航角
        :type Yaw: float
        """
        self.Direction = None
        self.Pitch = None
        self.Roll = None
        self.Yaw = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.Pitch = params.get("Pitch")
        self.Roll = params.get("Roll")
        self.Yaw = params.get("Yaw")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FrameInfo(AbstractModel):
    """人员信息

    """

    def __init__(self):
        """
        :param Similarity: 相似度
        :type Similarity: float
        :param SnapshotUrl: 截图的存储地址
        :type SnapshotUrl: str
        :param Ts: 相对于视频起始时间的时间戳，单位秒
        :type Ts: int
        """
        self.Similarity = None
        self.SnapshotUrl = None
        self.Ts = None


    def _deserialize(self, params):
        self.Similarity = params.get("Similarity")
        self.SnapshotUrl = params.get("SnapshotUrl")
        self.Ts = params.get("Ts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Function(AbstractModel):
    """功能开关列表，表示是否需要打开相应的功能，返回相应的信息

    """

    def __init__(self):
        """
        :param EnableAllText: 输出全部文本标识，当该值设置为true时，会输出当前音频的全部文本
        :type EnableAllText: bool
        :param EnableKeyword: 输出关键词信息标识，当该值设置为true时，会输出当前音频的关键词信息。
        :type EnableKeyword: bool
        :param EnableMuteDetect: 静音检测标识，当设置为 true 时，需要设置静音时间阈值字段mute_threshold，统计结果中会返回静音片段。
        :type EnableMuteDetect: bool
        :param EnableVadInfo: 输出音频统计信息标识，当设置为 true 时，任务查询结果会输出音频的统计信息（AsrStat）
        :type EnableVadInfo: bool
        :param EnableVolume: 输出音频音量信息标识，当设置为 true 时，会输出当前音频音量信息。
        :type EnableVolume: bool
        """
        self.EnableAllText = None
        self.EnableKeyword = None
        self.EnableMuteDetect = None
        self.EnableVadInfo = None
        self.EnableVolume = None


    def _deserialize(self, params):
        self.EnableAllText = params.get("EnableAllText")
        self.EnableKeyword = params.get("EnableKeyword")
        self.EnableMuteDetect = params.get("EnableMuteDetect")
        self.EnableVadInfo = params.get("EnableVadInfo")
        self.EnableVolume = params.get("EnableVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GestureResult(AbstractModel):
    """GestureResult

    """

    def __init__(self):
        """
        :param Class: 识别结果，包含"USPEAK":听你说，"LISTEN":听我说，"GOOD":GOOD，"TOOLS":拿教具，"OTHERS":其他
        :type Class: str
        :param Confidence: 置信度
        :type Confidence: float
        :param Height: 识别结果高度
        :type Height: int
        :param Left: 识别结果左坐标
        :type Left: int
        :param Top: 识别结果顶坐标
        :type Top: int
        :param Width: 识别结果宽度
        :type Width: int
        """
        self.Class = None
        self.Confidence = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Class = params.get("Class")
        self.Confidence = params.get("Confidence")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HLFunction(AbstractModel):
    """检索配置开关项

    """

    def __init__(self):
        """
        :param EnableFaceDetect: 是否开启人脸检测
        :type EnableFaceDetect: bool
        :param EnableFaceExpression: 是否开启表情识别
        :type EnableFaceExpression: bool
        :param EnableFaceIdent: 是否开启人脸检索
        :type EnableFaceIdent: bool
        :param EnableKeywordWonderfulTime: 是否开启视频集锦-老师关键字识别
        :type EnableKeywordWonderfulTime: bool
        :param EnableSmileWonderfulTime: 是否开启视频集锦-微笑识别
        :type EnableSmileWonderfulTime: bool
        """
        self.EnableFaceDetect = None
        self.EnableFaceExpression = None
        self.EnableFaceIdent = None
        self.EnableKeywordWonderfulTime = None
        self.EnableSmileWonderfulTime = None


    def _deserialize(self, params):
        self.EnableFaceDetect = params.get("EnableFaceDetect")
        self.EnableFaceExpression = params.get("EnableFaceExpression")
        self.EnableFaceIdent = params.get("EnableFaceIdent")
        self.EnableKeywordWonderfulTime = params.get("EnableKeywordWonderfulTime")
        self.EnableSmileWonderfulTime = params.get("EnableSmileWonderfulTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HandTrackingResult(AbstractModel):
    """HandTrackingResult

    """

    def __init__(self):
        """
        :param Class: 识别结果
        :type Class: str
        :param Confidence: 置信度
        :type Confidence: float
        :param Height: 识别结果高度
        :type Height: int
        :param Left: 识别结果左坐标
        :type Left: int
        :param Top: 识别结果顶坐标
        :type Top: int
        :param Width: 识别结果宽度
        :type Width: int
        """
        self.Class = None
        self.Confidence = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Class = params.get("Class")
        self.Confidence = params.get("Confidence")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HighlightsInfomation(AbstractModel):
    """精彩集锦信息

    """

    def __init__(self):
        """
        :param Concentration: 专注的起始与终止时间信息。
        :type Concentration: list of TimeType
        :param Smile: 微笑的起始与终止时间信息。
        :type Smile: list of TimeType
        :param HighlightsUrl: 高光集锦视频地址，保存剪辑好的视频地址。
        :type HighlightsUrl: str
        :param PersonId: 片段中识别出来的人脸ID。
        :type PersonId: str
        """
        self.Concentration = None
        self.Smile = None
        self.HighlightsUrl = None
        self.PersonId = None


    def _deserialize(self, params):
        if params.get("Concentration") is not None:
            self.Concentration = []
            for item in params.get("Concentration"):
                obj = TimeType()
                obj._deserialize(item)
                self.Concentration.append(obj)
        if params.get("Smile") is not None:
            self.Smile = []
            for item in params.get("Smile"):
                obj = TimeType()
                obj._deserialize(item)
                self.Smile.append(obj)
        self.HighlightsUrl = params.get("HighlightsUrl")
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImageTaskFunction(AbstractModel):
    """图像任务控制选项

    """

    def __init__(self):
        """
        :param EnableActionClass: 大教室场景学生肢体动作识别选项
        :type EnableActionClass: bool
        :param EnableFaceDetect: 人脸检测选项（默认为true，目前不可编辑）
        :type EnableFaceDetect: bool
        :param EnableFaceExpression: 人脸表情识别选项
        :type EnableFaceExpression: bool
        :param EnableFaceIdentify: 人脸检索选项（默认为true，目前不可编辑）
        :type EnableFaceIdentify: bool
        :param EnableGesture: 手势选项
        :type EnableGesture: bool
        :param EnableHandTracking: 优图手势选项（该功能尚未支持）
        :type EnableHandTracking: bool
        :param EnableLightJudge: 光照选项
        :type EnableLightJudge: bool
        :param EnableStudentBodyMovements: 小班课场景学生肢体动作识别选项
        :type EnableStudentBodyMovements: bool
        :param EnableTeacherBodyMovements: 教师动作选项（该功能尚未支持）
        :type EnableTeacherBodyMovements: bool
        :param EnableTeacherOutScreen: 判断老师是否在屏幕中（该功能尚未支持）
        :type EnableTeacherOutScreen: bool
        """
        self.EnableActionClass = None
        self.EnableFaceDetect = None
        self.EnableFaceExpression = None
        self.EnableFaceIdentify = None
        self.EnableGesture = None
        self.EnableHandTracking = None
        self.EnableLightJudge = None
        self.EnableStudentBodyMovements = None
        self.EnableTeacherBodyMovements = None
        self.EnableTeacherOutScreen = None


    def _deserialize(self, params):
        self.EnableActionClass = params.get("EnableActionClass")
        self.EnableFaceDetect = params.get("EnableFaceDetect")
        self.EnableFaceExpression = params.get("EnableFaceExpression")
        self.EnableFaceIdentify = params.get("EnableFaceIdentify")
        self.EnableGesture = params.get("EnableGesture")
        self.EnableHandTracking = params.get("EnableHandTracking")
        self.EnableLightJudge = params.get("EnableLightJudge")
        self.EnableStudentBodyMovements = params.get("EnableStudentBodyMovements")
        self.EnableTeacherBodyMovements = params.get("EnableTeacherBodyMovements")
        self.EnableTeacherOutScreen = params.get("EnableTeacherOutScreen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImageTaskResult(AbstractModel):
    """图像任务结果

    """

    def __init__(self):
        """
        :param ActionInfo: 大教室场景学生肢体动作识别信息
        :type ActionInfo: :class:`tencentcloud.tci.v20190318.models.ActionInfo`
        :param FaceAttr: 属性识别结果
        :type FaceAttr: :class:`tencentcloud.tci.v20190318.models.FaceAttrResult`
        :param FaceExpression: 表情识别结果
        :type FaceExpression: :class:`tencentcloud.tci.v20190318.models.FaceExpressionResult`
        :param FaceIdentify: 人脸检索结果
        :type FaceIdentify: :class:`tencentcloud.tci.v20190318.models.FaceIdentifyResult`
        :param FaceInfo: 人脸检测结果
        :type FaceInfo: :class:`tencentcloud.tci.v20190318.models.FaceInfoResult`
        :param FacePose: 姿势识别结果
        :type FacePose: :class:`tencentcloud.tci.v20190318.models.FacePoseResult`
        :param Gesture: 动作分类结果
        :type Gesture: :class:`tencentcloud.tci.v20190318.models.GestureResult`
        :param HandTracking: 手势分类结果
        :type HandTracking: :class:`tencentcloud.tci.v20190318.models.HandTrackingResult`
        :param Light: 光照识别结果
        :type Light: :class:`tencentcloud.tci.v20190318.models.LightResult`
        :param StudentBodyMovement: 学生肢体动作识别结果
        :type StudentBodyMovement: :class:`tencentcloud.tci.v20190318.models.StudentBodyMovementResult`
        :param TeacherBodyMovement: 老师肢体动作识别结果
        :type TeacherBodyMovement: :class:`tencentcloud.tci.v20190318.models.BodyMovementResult`
        :param TeacherOutScreen: 教师是否在屏幕内判断结果
        :type TeacherOutScreen: :class:`tencentcloud.tci.v20190318.models.TeacherOutScreenResult`
        :param TimeInfo: 时间统计结果
        :type TimeInfo: :class:`tencentcloud.tci.v20190318.models.TimeInfoResult`
        """
        self.ActionInfo = None
        self.FaceAttr = None
        self.FaceExpression = None
        self.FaceIdentify = None
        self.FaceInfo = None
        self.FacePose = None
        self.Gesture = None
        self.HandTracking = None
        self.Light = None
        self.StudentBodyMovement = None
        self.TeacherBodyMovement = None
        self.TeacherOutScreen = None
        self.TimeInfo = None


    def _deserialize(self, params):
        if params.get("ActionInfo") is not None:
            self.ActionInfo = ActionInfo()
            self.ActionInfo._deserialize(params.get("ActionInfo"))
        if params.get("FaceAttr") is not None:
            self.FaceAttr = FaceAttrResult()
            self.FaceAttr._deserialize(params.get("FaceAttr"))
        if params.get("FaceExpression") is not None:
            self.FaceExpression = FaceExpressionResult()
            self.FaceExpression._deserialize(params.get("FaceExpression"))
        if params.get("FaceIdentify") is not None:
            self.FaceIdentify = FaceIdentifyResult()
            self.FaceIdentify._deserialize(params.get("FaceIdentify"))
        if params.get("FaceInfo") is not None:
            self.FaceInfo = FaceInfoResult()
            self.FaceInfo._deserialize(params.get("FaceInfo"))
        if params.get("FacePose") is not None:
            self.FacePose = FacePoseResult()
            self.FacePose._deserialize(params.get("FacePose"))
        if params.get("Gesture") is not None:
            self.Gesture = GestureResult()
            self.Gesture._deserialize(params.get("Gesture"))
        if params.get("HandTracking") is not None:
            self.HandTracking = HandTrackingResult()
            self.HandTracking._deserialize(params.get("HandTracking"))
        if params.get("Light") is not None:
            self.Light = LightResult()
            self.Light._deserialize(params.get("Light"))
        if params.get("StudentBodyMovement") is not None:
            self.StudentBodyMovement = StudentBodyMovementResult()
            self.StudentBodyMovement._deserialize(params.get("StudentBodyMovement"))
        if params.get("TeacherBodyMovement") is not None:
            self.TeacherBodyMovement = BodyMovementResult()
            self.TeacherBodyMovement._deserialize(params.get("TeacherBodyMovement"))
        if params.get("TeacherOutScreen") is not None:
            self.TeacherOutScreen = TeacherOutScreenResult()
            self.TeacherOutScreen._deserialize(params.get("TeacherOutScreen"))
        if params.get("TimeInfo") is not None:
            self.TimeInfo = TimeInfoResult()
            self.TimeInfo._deserialize(params.get("TimeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImageTaskStatistic(AbstractModel):
    """图像任务统计结果

    """

    def __init__(self):
        """
        :param FaceDetect: 人员检测统计信息
        :type FaceDetect: list of FaceDetectStatistic
        :param FaceExpression: 人脸表情统计信息
        :type FaceExpression: list of FaceExpressStatistic
        :param FaceIdentify: 人脸检索统计信息
        :type FaceIdentify: list of FaceIdentifyStatistic
        :param Gesture: 姿势识别统计信息
        :type Gesture: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param Handtracking: 手势识别统计信息
        :type Handtracking: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param Light: 光照统计信息
        :type Light: :class:`tencentcloud.tci.v20190318.models.LightStatistic`
        :param StudentMovement: 学生动作统计信息
        :type StudentMovement: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param TeacherMovement: 教师动作统计信息
        :type TeacherMovement: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        """
        self.FaceDetect = None
        self.FaceExpression = None
        self.FaceIdentify = None
        self.Gesture = None
        self.Handtracking = None
        self.Light = None
        self.StudentMovement = None
        self.TeacherMovement = None


    def _deserialize(self, params):
        if params.get("FaceDetect") is not None:
            self.FaceDetect = []
            for item in params.get("FaceDetect"):
                obj = FaceDetectStatistic()
                obj._deserialize(item)
                self.FaceDetect.append(obj)
        if params.get("FaceExpression") is not None:
            self.FaceExpression = []
            for item in params.get("FaceExpression"):
                obj = FaceExpressStatistic()
                obj._deserialize(item)
                self.FaceExpression.append(obj)
        if params.get("FaceIdentify") is not None:
            self.FaceIdentify = []
            for item in params.get("FaceIdentify"):
                obj = FaceIdentifyStatistic()
                obj._deserialize(item)
                self.FaceIdentify.append(obj)
        if params.get("Gesture") is not None:
            self.Gesture = ActionStatistic()
            self.Gesture._deserialize(params.get("Gesture"))
        if params.get("Handtracking") is not None:
            self.Handtracking = ActionStatistic()
            self.Handtracking._deserialize(params.get("Handtracking"))
        if params.get("Light") is not None:
            self.Light = LightStatistic()
            self.Light._deserialize(params.get("Light"))
        if params.get("StudentMovement") is not None:
            self.StudentMovement = ActionStatistic()
            self.StudentMovement._deserialize(params.get("StudentMovement"))
        if params.get("TeacherMovement") is not None:
            self.TeacherMovement = ActionStatistic()
            self.TeacherMovement._deserialize(params.get("TeacherMovement"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Library(AbstractModel):
    """人员库描述

    """

    def __init__(self):
        """
        :param CreateTime: 人员库创建时间
        :type CreateTime: str
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param LibraryName: 人员库名称
        :type LibraryName: str
        :param PersonCount: 人员库人员数量
        :type PersonCount: int
        :param UpdateTime: 人员库修改时间
        :type UpdateTime: str
        """
        self.CreateTime = None
        self.LibraryId = None
        self.LibraryName = None
        self.PersonCount = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        self.PersonCount = params.get("PersonCount")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LightDistributionStatistic(AbstractModel):
    """光照强度统计结果

    """

    def __init__(self):
        """
        :param Time: 时间点
        :type Time: int
        :param Value: 光线值
        :type Value: int
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LightLevelRatioStatistic(AbstractModel):
    """光照强度比例统计结果

    """

    def __init__(self):
        """
        :param Level: 名称
        :type Level: str
        :param Ratio: 比例
        :type Ratio: float
        """
        self.Level = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Level = params.get("Level")
        self.Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LightResult(AbstractModel):
    """LightResult

    """

    def __init__(self):
        """
        :param LightLevel: 光照程度，参考提交任务时的LightStandard指定的Name参数
        :type LightLevel: str
        :param LightValue: 光照亮度
        :type LightValue: float
        """
        self.LightLevel = None
        self.LightValue = None


    def _deserialize(self, params):
        self.LightLevel = params.get("LightLevel")
        self.LightValue = params.get("LightValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LightStandard(AbstractModel):
    """光照标准，结构的相关示例为：
    {
        "Name":"dark"，
        "Range":[0,30]
    }
    当光照的区间落入在0到30的范围时，就会命中dark的光照标准

    """

    def __init__(self):
        """
        :param Name: 光照名称
        :type Name: str
        :param Range: 范围
        :type Range: list of float
        """
        self.Name = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LightStatistic(AbstractModel):
    """光照统计结果

    """

    def __init__(self):
        """
        :param LightDistribution: 各个时间点的光线值
        :type LightDistribution: list of LightDistributionStatistic
        :param LightLevelRatio: 光照程度比例统计结果
        :type LightLevelRatio: list of LightLevelRatioStatistic
        """
        self.LightDistribution = None
        self.LightLevelRatio = None


    def _deserialize(self, params):
        if params.get("LightDistribution") is not None:
            self.LightDistribution = []
            for item in params.get("LightDistribution"):
                obj = LightDistributionStatistic()
                obj._deserialize(item)
                self.LightDistribution.append(obj)
        if params.get("LightLevelRatio") is not None:
            self.LightLevelRatio = []
            for item in params.get("LightLevelRatio"):
                obj = LightLevelRatioStatistic()
                obj._deserialize(item)
                self.LightLevelRatio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLibraryRequest(AbstractModel):
    """ModifyLibrary请求参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param LibraryName: 人员库名称
        :type LibraryName: str
        """
        self.LibraryId = None
        self.LibraryName = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLibraryResponse(AbstractModel):
    """ModifyLibrary返回参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param LibraryName: 人员库名称
        :type LibraryName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LibraryId = None
        self.LibraryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPersonRequest(AbstractModel):
    """ModifyPerson请求参数结构体

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param JobNumber: 人员工作号码
        :type JobNumber: str
        :param Mail: 人员邮箱
        :type Mail: str
        :param Male: 人员性别
        :type Male: int
        :param PersonName: 人员名称
        :type PersonName: str
        :param PhoneNumber: 人员电话号码
        :type PhoneNumber: str
        :param StudentNumber: 人员学生号码
        :type StudentNumber: str
        """
        self.LibraryId = None
        self.PersonId = None
        self.JobNumber = None
        self.Mail = None
        self.Male = None
        self.PersonName = None
        self.PhoneNumber = None
        self.StudentNumber = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.JobNumber = params.get("JobNumber")
        self.Mail = params.get("Mail")
        self.Male = params.get("Male")
        self.PersonName = params.get("PersonName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.StudentNumber = params.get("StudentNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPersonResponse(AbstractModel):
    """ModifyPerson返回参数结构体

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人脸信息
        :type FaceInfoSet: list of FaceInfo
        :param LibraryId: 人员所属人员库标识符
        :type LibraryId: str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param PersonName: 人员名称
        :type PersonName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.LibraryId = None
        self.PersonId = None
        self.PersonName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MuteSlice(AbstractModel):
    """所有静音片段。

    """

    def __init__(self):
        """
        :param MuteBtm: 起始时间。
        :type MuteBtm: int
        :param MuteEtm: 终止时间。
        :type MuteEtm: int
        """
        self.MuteBtm = None
        self.MuteEtm = None


    def _deserialize(self, params):
        self.MuteBtm = params.get("MuteBtm")
        self.MuteEtm = params.get("MuteEtm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Person(AbstractModel):
    """人员描述

    """

    def __init__(self):
        """
        :param LibraryId: 人员库唯一标识符
        :type LibraryId: str
        :param PersonId: 人员唯一标识符
        :type PersonId: str
        :param PersonName: 人员名称
        :type PersonName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param JobNumber: 工作号码
        :type JobNumber: str
        :param Mail: 邮箱
        :type Mail: str
        :param Male: 性别
        :type Male: int
        :param PhoneNumber: 电话号码
        :type PhoneNumber: str
        :param StudentNumber: 学生号码
        :type StudentNumber: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self.LibraryId = None
        self.PersonId = None
        self.PersonName = None
        self.CreateTime = None
        self.JobNumber = None
        self.Mail = None
        self.Male = None
        self.PhoneNumber = None
        self.StudentNumber = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.CreateTime = params.get("CreateTime")
        self.JobNumber = params.get("JobNumber")
        self.Mail = params.get("Mail")
        self.Male = params.get("Male")
        self.PhoneNumber = params.get("PhoneNumber")
        self.StudentNumber = params.get("StudentNumber")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PersonInfo(AbstractModel):
    """人员信息

    """

    def __init__(self):
        """
        :param PersonId: 需要匹配的人员的ID列表。
        :type PersonId: str
        :param CoverBeginUrl: 视频集锦开始封面照片。
        :type CoverBeginUrl: str
        :param CoverEndUrl: 视频集锦结束封面照片。
        :type CoverEndUrl: str
        """
        self.PersonId = None
        self.CoverBeginUrl = None
        self.CoverEndUrl = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.CoverBeginUrl = params.get("CoverBeginUrl")
        self.CoverEndUrl = params.get("CoverEndUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StandardAudioResult(AbstractModel):
    """标准化接口图像分析结果

    """

    def __init__(self):
        """
        :param AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :type Texts: list of WholeTextItem
        :param VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param Message: 状态描述
        :type Message: str
        :param Status: 任务状态
        :type Status: str
        :param TotalCount: 结果数量
        :type TotalCount: int
        """
        self.AsrStat = None
        self.Texts = None
        self.VocabAnalysisDetailInfo = None
        self.VocabAnalysisStatInfo = None
        self.Message = None
        self.Status = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self.AsrStat = ASRStat()
            self.AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self.Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self.Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self.VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self.VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self.VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self.VocabAnalysisStatInfo.append(obj)
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StandardImageResult(AbstractModel):
    """标准化接口图像分析结果

    """

    def __init__(self):
        """
        :param ResultSet: 详细结果
        :type ResultSet: list of ImageTaskResult
        :param Statistic: 分析完成后的统计结果
        :type Statistic: :class:`tencentcloud.tci.v20190318.models.ImageTaskStatistic`
        :param Message: 状态描述
        :type Message: str
        :param Status: 任务状态
        :type Status: str
        :param TotalCount: 结果总数
        :type TotalCount: int
        """
        self.ResultSet = None
        self.Statistic = None
        self.Message = None
        self.Status = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        if params.get("Statistic") is not None:
            self.Statistic = ImageTaskStatistic()
            self.Statistic._deserialize(params.get("Statistic"))
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StandardVideoResult(AbstractModel):
    """标准化接口图像分析结果

    """

    def __init__(self):
        """
        :param HighlightsInfo: 分析完成后的统计结果
        :type HighlightsInfo: list of HighlightsInfomation
        :param Message: 状态描述
        :type Message: str
        :param Status: 任务状态
        :type Status: str
        """
        self.HighlightsInfo = None
        self.Message = None
        self.Status = None


    def _deserialize(self, params):
        if params.get("HighlightsInfo") is not None:
            self.HighlightsInfo = []
            for item in params.get("HighlightsInfo"):
                obj = HighlightsInfomation()
                obj._deserialize(item)
                self.HighlightsInfo.append(obj)
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StatInfo(AbstractModel):
    """单词出现的次数信息

    """

    def __init__(self):
        """
        :param Keyword: 词汇库中的单词
        :type Keyword: str
        :param Value: 单词出现在该音频中总次数
        :type Value: int
        """
        self.Keyword = None
        self.Value = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StudentBodyMovementResult(AbstractModel):
    """学生肢体动作结果

    """

    def __init__(self):
        """
        :param Confidence: 置信度（已废弃）
        :type Confidence: float
        :param HandupConfidence: 举手识别结果置信度
        :type HandupConfidence: float
        :param HandupStatus: 举手识别结果，包含举手（handup）和未举手（nothandup）
        :type HandupStatus: str
        :param Height: 识别结果高度
        :type Height: int
        :param Left: 识别结果左坐标
        :type Left: int
        :param Movements: 动作识别结果（已废弃）
        :type Movements: str
        :param StandConfidence: 站立识别结果置信度
        :type StandConfidence: float
        :param StandStatus: 站立识别结果，包含站立（stand）和坐着（sit）
        :type StandStatus: str
        :param Top: 识别结果顶坐标
        :type Top: int
        :param Width: 识别结果宽度
        :type Width: int
        """
        self.Confidence = None
        self.HandupConfidence = None
        self.HandupStatus = None
        self.Height = None
        self.Left = None
        self.Movements = None
        self.StandConfidence = None
        self.StandStatus = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.HandupConfidence = params.get("HandupConfidence")
        self.HandupStatus = params.get("HandupStatus")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Movements = params.get("Movements")
        self.StandConfidence = params.get("StandConfidence")
        self.StandStatus = params.get("StandStatus")
        self.Top = params.get("Top")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitAudioTaskRequest(AbstractModel):
    """SubmitAudioTask请求参数结构体

    """

    def __init__(self):
        """
        :param Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param Url: 音频URL。客户请求为URL方式时必须带此字段指名音频的url。
        :type Url: str
        :param VoiceEncodeType: 语音编码类型 1:pcm
        :type VoiceEncodeType: int
        :param VoiceFileType: 语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）
        :type VoiceFileType: int
        :param Functions: 功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param FileType: 视频文件类型，默认点播，直播填 live_url
        :type FileType: str
        :param MuteThreshold: 静音阈值设置，如果静音检测开关开启，则静音时间超过这个阈值认为是静音片段，在结果中会返回, 没给的话默认值为3s
        :type MuteThreshold: int
        :param VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :type VocabLibNameList: list of str
        """
        self.Lang = None
        self.Url = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None
        self.Functions = None
        self.FileType = None
        self.MuteThreshold = None
        self.VocabLibNameList = None


    def _deserialize(self, params):
        self.Lang = params.get("Lang")
        self.Url = params.get("Url")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        if params.get("Functions") is not None:
            self.Functions = Function()
            self.Functions._deserialize(params.get("Functions"))
        self.FileType = params.get("FileType")
        self.MuteThreshold = params.get("MuteThreshold")
        self.VocabLibNameList = params.get("VocabLibNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitAudioTaskResponse(AbstractModel):
    """SubmitAudioTask返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 	查询结果时指名的jobid。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitCheckAttendanceTaskPlusRequest(AbstractModel):
    """SubmitCheckAttendanceTaskPlus请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入数据
        :type FileContent: list of str
        :param FileType: 视频流类型，vod_url表示点播URL，live_url表示直播URL，默认vod_url
        :type FileType: str
        :param LibraryIds: 人员库 ID列表
        :type LibraryIds: list of str
        :param AttendanceThreshold: 确定出勤阈值；默认为0.92
        :type AttendanceThreshold: float
        :param EnableStranger: 是否开启陌生人模式，陌生人模式是指在任务中发现的非注册人脸库中的人脸也返回相关统计信息，默认不开启
        :type EnableStranger: bool
        :param EndTime: 考勤结束时间（到视频的第几秒结束考勤），单位秒；默认为900 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间往后12小时
        :type EndTime: int
        :param NoticeUrl: 通知回调地址，要求方法为post，application/json格式
        :type NoticeUrl: str
        :param StartTime: 考勤开始时间（从视频的第几秒开始考勤），单位秒；默认为0 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间
        :type StartTime: int
        :param Threshold: 识别阈值；默认为0.8
        :type Threshold: float
        """
        self.FileContent = None
        self.FileType = None
        self.LibraryIds = None
        self.AttendanceThreshold = None
        self.EnableStranger = None
        self.EndTime = None
        self.NoticeUrl = None
        self.StartTime = None
        self.Threshold = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibraryIds = params.get("LibraryIds")
        self.AttendanceThreshold = params.get("AttendanceThreshold")
        self.EnableStranger = params.get("EnableStranger")
        self.EndTime = params.get("EndTime")
        self.NoticeUrl = params.get("NoticeUrl")
        self.StartTime = params.get("StartTime")
        self.Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitCheckAttendanceTaskPlusResponse(AbstractModel):
    """SubmitCheckAttendanceTaskPlus返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 任务标识符
        :type JobId: int
        :param NotRegisteredSet: 没有注册的人的ID列表
        :type NotRegisteredSet: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.NotRegisteredSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NotRegisteredSet = params.get("NotRegisteredSet")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitCheckAttendanceTaskRequest(AbstractModel):
    """SubmitCheckAttendanceTask请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入数据
        :type FileContent: str
        :param FileType: 视频流类型，vod_url表示点播URL，live_url表示直播URL，默认vod_url
        :type FileType: str
        :param LibraryIds: 人员库 ID列表
        :type LibraryIds: list of str
        :param AttendanceThreshold: 确定出勤阈值；默认为0.92
        :type AttendanceThreshold: float
        :param EnableStranger: 是否开启陌生人模式，陌生人模式是指在任务中发现的非注册人脸库中的人脸也返回相关统计信息，默认不开启
        :type EnableStranger: bool
        :param EndTime: 考勤结束时间（到视频的第几秒结束考勤），单位秒；默认为900 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间往后12小时
        :type EndTime: int
        :param NoticeUrl: 通知回调地址，要求方法为post，application/json格式
        :type NoticeUrl: str
        :param StartTime: 考勤开始时间（从视频的第几秒开始考勤），单位秒；默认为0 
对于直播场景，使用绝对时间戳，单位秒，默认当前时间
        :type StartTime: int
        :param Threshold: 识别阈值；默认为0.8
        :type Threshold: float
        """
        self.FileContent = None
        self.FileType = None
        self.LibraryIds = None
        self.AttendanceThreshold = None
        self.EnableStranger = None
        self.EndTime = None
        self.NoticeUrl = None
        self.StartTime = None
        self.Threshold = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibraryIds = params.get("LibraryIds")
        self.AttendanceThreshold = params.get("AttendanceThreshold")
        self.EnableStranger = params.get("EnableStranger")
        self.EndTime = params.get("EndTime")
        self.NoticeUrl = params.get("NoticeUrl")
        self.StartTime = params.get("StartTime")
        self.Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitCheckAttendanceTaskResponse(AbstractModel):
    """SubmitCheckAttendanceTask返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 任务标识符
        :type JobId: int
        :param NotRegisteredSet: 没有注册的人的ID列表
        :type NotRegisteredSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.NotRegisteredSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NotRegisteredSet = params.get("NotRegisteredSet")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitConversationTaskRequest(AbstractModel):
    """SubmitConversationTask请求参数结构体

    """

    def __init__(self):
        """
        :param Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param StudentUrl: 学生音频流
        :type StudentUrl: str
        :param TeacherUrl: 教师音频流
        :type TeacherUrl: str
        :param VoiceEncodeType: 语音编码类型 1:pcm
        :type VoiceEncodeType: int
        :param VoiceFileType: 语音文件类型 1:raw, 2:wav, 3:mp3（三种格式目前仅支持16k采样率16bit）
        :type VoiceFileType: int
        :param Functions: 功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :type VocabLibNameList: list of str
        """
        self.Lang = None
        self.StudentUrl = None
        self.TeacherUrl = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None
        self.Functions = None
        self.VocabLibNameList = None


    def _deserialize(self, params):
        self.Lang = params.get("Lang")
        self.StudentUrl = params.get("StudentUrl")
        self.TeacherUrl = params.get("TeacherUrl")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        if params.get("Functions") is not None:
            self.Functions = Function()
            self.Functions._deserialize(params.get("Functions"))
        self.VocabLibNameList = params.get("VocabLibNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitConversationTaskResponse(AbstractModel):
    """SubmitConversationTask返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 	查询结果时指名的jobid。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。
        :type JobId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitDoubleVideoHighlightsRequest(AbstractModel):
    """SubmitDoubleVideoHighlights请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 学生视频url
        :type FileContent: str
        :param LibIds: 需要检索的人脸合集库，不在库中的人脸将不参与精彩集锦；目前仅支持输入一个人脸库。
        :type LibIds: list of str
        :param Functions: 详细功能开关配置项
        :type Functions: :class:`tencentcloud.tci.v20190318.models.DoubleVideoFunction`
        :param PersonInfoList: 需要匹配的人员信息列表。
        :type PersonInfoList: list of PersonInfo
        :param FrameInterval: 视频处理的抽帧间隔，单位毫秒。建议留空。
        :type FrameInterval: int
        :param PersonIds: 旧版本需要匹配的人员信息列表。
        :type PersonIds: list of str
        :param SimThreshold: 人脸检索的相似度阈值，默认值0.89。建议留空。
        :type SimThreshold: float
        :param TeacherFileContent: 老师视频url
        :type TeacherFileContent: str
        """
        self.FileContent = None
        self.LibIds = None
        self.Functions = None
        self.PersonInfoList = None
        self.FrameInterval = None
        self.PersonIds = None
        self.SimThreshold = None
        self.TeacherFileContent = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.LibIds = params.get("LibIds")
        if params.get("Functions") is not None:
            self.Functions = DoubleVideoFunction()
            self.Functions._deserialize(params.get("Functions"))
        if params.get("PersonInfoList") is not None:
            self.PersonInfoList = []
            for item in params.get("PersonInfoList"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfoList.append(obj)
        self.FrameInterval = params.get("FrameInterval")
        self.PersonIds = params.get("PersonIds")
        self.SimThreshold = params.get("SimThreshold")
        self.TeacherFileContent = params.get("TeacherFileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitDoubleVideoHighlightsResponse(AbstractModel):
    """SubmitDoubleVideoHighlights返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 视频拆条任务ID，用来唯一标识视频拆条任务。
        :type JobId: int
        :param NotRegistered: 未注册的人员ID列表。若出现此项，代表评估出现了问题，输入的PersonId中有不在库中的人员ID。
        :type NotRegistered: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.NotRegistered = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NotRegistered = params.get("NotRegistered")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitFullBodyClassTaskRequest(AbstractModel):
    """SubmitFullBodyClassTask请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :type FileType: str
        :param Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param LibrarySet: 查询人员库列表，可填写老师的注册照所在人员库
        :type LibrarySet: list of str
        :param MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param VocabLibNameList: 识别词库名列表，这些词汇库用来维护关键词，评估老师授课过程中，对这些关键词的使用情况
        :type VocabLibNameList: list of str
        :param VoiceEncodeType: 语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :type VoiceEncodeType: int
        :param VoiceFileType: 语音文件类型 10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :type VoiceFileType: int
        """
        self.FileContent = None
        self.FileType = None
        self.Lang = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.VocabLibNameList = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.Lang = params.get("Lang")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.VocabLibNameList = params.get("VocabLibNameList")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitFullBodyClassTaskResponse(AbstractModel):
    """SubmitFullBodyClassTask返回参数结构体

    """

    def __init__(self):
        """
        :param ImageResults: 图像任务直接返回结果，包括： FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 TeacherBodyMovement、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitHighlightsRequest(AbstractModel):
    """SubmitHighlights请求参数结构体

    """

    def __init__(self):
        """
        :param Functions: 表情配置开关项。
        :type Functions: :class:`tencentcloud.tci.v20190318.models.HLFunction`
        :param FileContent: 视频url。
        :type FileContent: str
        :param FileType: 视频类型及来源，目前只支持点播类型："vod_url"。
        :type FileType: str
        :param LibIds: 需要检索的人脸合集库，不在库中的人脸将不参与精彩集锦。
        :type LibIds: list of str
        :param FrameInterval: 视频处理的抽帧间隔，单位毫秒。建议留空。
        :type FrameInterval: int
        :param KeywordsLanguage: 关键词语言类型，0为英文，1为中文。
        :type KeywordsLanguage: int
        :param KeywordsStrings: 关键词数组，当且仅当Funtions中的EnableKeywordWonderfulTime为true时有意义，匹配相应的关键字。
        :type KeywordsStrings: list of str
        :param MaxVideoDuration: 处理视频的总时长，单位毫秒。该值为0或未设置时，默认值两小时生效；当该值大于视频实际时长时，视频实际时长生效；当该值小于视频实际时长时，该值生效；当获取视频实际时长失败时，若该值设置则生效，否则默认值生效。建议留空。
        :type MaxVideoDuration: int
        :param SimThreshold: 人脸检索的相似度阈值，默认值0.89。建议留空。
        :type SimThreshold: float
        """
        self.Functions = None
        self.FileContent = None
        self.FileType = None
        self.LibIds = None
        self.FrameInterval = None
        self.KeywordsLanguage = None
        self.KeywordsStrings = None
        self.MaxVideoDuration = None
        self.SimThreshold = None


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self.Functions = HLFunction()
            self.Functions._deserialize(params.get("Functions"))
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibIds = params.get("LibIds")
        self.FrameInterval = params.get("FrameInterval")
        self.KeywordsLanguage = params.get("KeywordsLanguage")
        self.KeywordsStrings = params.get("KeywordsStrings")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.SimThreshold = params.get("SimThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitHighlightsResponse(AbstractModel):
    """SubmitHighlights返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 视频拆条任务ID，用来唯一标识视频拆条任务。
        :type JobId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitImageTaskPlusRequest(AbstractModel):
    """SubmitImageTaskPlus请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: list of str
        :param FileType: 输入分析对象类型，picture：二进制图片的 base64 编码字符串，picture_url:图片地址，vod_url：视频地址，live_url：直播地址
        :type FileType: str
        :param Functions: 任务控制选项
        :type Functions: :class:`tencentcloud.tci.v20190318.models.ImageTaskFunction`
        :param LightStandardSet: 光照标准列表
        :type LightStandardSet: list of LightStandard
        :param FrameInterval: 抽帧的时间间隔，单位毫秒，默认值1000，保留字段，当前不支持填写。
        :type FrameInterval: int
        :param LibrarySet: 查询人员库列表
        :type LibrarySet: list of str
        :param MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param SimThreshold: 人脸识别中的相似度阈值，默认值为0.89，保留字段，当前不支持填写。
        :type SimThreshold: float
        """
        self.FileContent = None
        self.FileType = None
        self.Functions = None
        self.LightStandardSet = None
        self.FrameInterval = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.SimThreshold = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        if params.get("Functions") is not None:
            self.Functions = ImageTaskFunction()
            self.Functions._deserialize(params.get("Functions"))
        if params.get("LightStandardSet") is not None:
            self.LightStandardSet = []
            for item in params.get("LightStandardSet"):
                obj = LightStandard()
                obj._deserialize(item)
                self.LightStandardSet.append(obj)
        self.FrameInterval = params.get("FrameInterval")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.SimThreshold = params.get("SimThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitImageTaskPlusResponse(AbstractModel):
    """SubmitImageTaskPlus返回参数结构体

    """

    def __init__(self):
        """
        :param ResultSet: 识别结果
        :type ResultSet: list of ImageTaskResult
        :param JobId: 任务标识符
        :type JobId: int
        :param Progress: 任务进度
        :type Progress: int
        :param TotalCount: 结果总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultSet = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitImageTaskRequest(AbstractModel):
    """SubmitImageTask请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param FileType: 输入分析对象类型，picture：二进制图片的 base64 编码字符串，picture_url:图片地址，vod_url：视频地址，live_url：直播地址
        :type FileType: str
        :param Functions: 任务控制选项
        :type Functions: :class:`tencentcloud.tci.v20190318.models.ImageTaskFunction`
        :param LightStandardSet: 光照标准列表
        :type LightStandardSet: list of LightStandard
        :param EventsCallBack: 结果更新回调地址。
        :type EventsCallBack: str
        :param FrameInterval: 抽帧的时间间隔，单位毫秒，默认值1000，保留字段，当前不支持填写。
        :type FrameInterval: int
        :param LibrarySet: 查询人员库列表
        :type LibrarySet: list of str
        :param MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param SimThreshold: 人脸识别中的相似度阈值，默认值为0.89，保留字段，当前不支持填写。
        :type SimThreshold: float
        """
        self.FileContent = None
        self.FileType = None
        self.Functions = None
        self.LightStandardSet = None
        self.EventsCallBack = None
        self.FrameInterval = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.SimThreshold = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        if params.get("Functions") is not None:
            self.Functions = ImageTaskFunction()
            self.Functions._deserialize(params.get("Functions"))
        if params.get("LightStandardSet") is not None:
            self.LightStandardSet = []
            for item in params.get("LightStandardSet"):
                obj = LightStandard()
                obj._deserialize(item)
                self.LightStandardSet.append(obj)
        self.EventsCallBack = params.get("EventsCallBack")
        self.FrameInterval = params.get("FrameInterval")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.SimThreshold = params.get("SimThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitImageTaskResponse(AbstractModel):
    """SubmitImageTask返回参数结构体

    """

    def __init__(self):
        """
        :param ResultSet: 识别结果
        :type ResultSet: list of ImageTaskResult
        :param JobId: 任务标识符
        :type JobId: int
        :param Progress: 任务进度
        :type Progress: int
        :param TotalCount: 结果总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultSet = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitOneByOneClassTaskRequest(AbstractModel):
    """SubmitOneByOneClassTask请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :type FileType: str
        :param Lang: 音频源的语言，默认0为英文，1为中文 
        :type Lang: int
        :param LibrarySet: 查询人员库列表，可填写学生的注册照所在人员库
        :type LibrarySet: list of str
        :param MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param VocabLibNameList: 识别词库名列表，这些词汇库用来维护关键词，评估学生对这些关键词的使用情况
        :type VocabLibNameList: list of str
        :param VoiceEncodeType: 语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :type VoiceEncodeType: int
        :param VoiceFileType: 语音文件类型10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :type VoiceFileType: int
        """
        self.FileContent = None
        self.FileType = None
        self.Lang = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.VocabLibNameList = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.Lang = params.get("Lang")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.VocabLibNameList = params.get("VocabLibNameList")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitOneByOneClassTaskResponse(AbstractModel):
    """SubmitOneByOneClassTask返回参数结构体

    """

    def __init__(self):
        """
        :param ImageResults: 图像任务直接返回结果，包括：FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitOpenClassTaskRequest(AbstractModel):
    """SubmitOpenClassTask请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址,picture: 图片二进制数据的BASE64编码
        :type FileType: str
        :param LibrarySet: 查询人员库列表，可填写学生们的注册照所在人员库
        :type LibrarySet: list of str
        :param MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        """
        self.FileContent = None
        self.FileType = None
        self.LibrarySet = None
        self.MaxVideoDuration = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitOpenClassTaskResponse(AbstractModel):
    """SubmitOpenClassTask返回参数结构体

    """

    def __init__(self):
        """
        :param ImageResults: 图像任务直接返回结果，包括：FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 StudentBodyMovement、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitPartialBodyClassTaskRequest(AbstractModel):
    """SubmitPartialBodyClassTask请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码
        :type FileType: str
        :param Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param LibrarySet: 查询人员库列表，可填写老师的注册照所在人员库
        :type LibrarySet: list of str
        :param MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        :param VocabLibNameList: 识别词库名列表，这些词汇库用来维护关键词，评估老师授课过程中，对这些关键词的使用情况
        :type VocabLibNameList: list of str
        :param VoiceEncodeType: 语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填
        :type VoiceEncodeType: int
        :param VoiceFileType: 语音文件类型 10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填
        :type VoiceFileType: int
        """
        self.FileContent = None
        self.FileType = None
        self.Lang = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.VocabLibNameList = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.Lang = params.get("Lang")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.VocabLibNameList = params.get("VocabLibNameList")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitPartialBodyClassTaskResponse(AbstractModel):
    """SubmitPartialBodyClassTask返回参数结构体

    """

    def __init__(self):
        """
        :param ImageResults: 图像任务直接返回结果，包括： FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 Gesture 、 Light、 TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitTraditionalClassTaskRequest(AbstractModel):
    """SubmitTraditionalClassTask请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 输入分析对象内容，输入数据格式参考FileType参数释义
        :type FileContent: str
        :param FileType: 输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture：图片二进制数据的BASE64编码
        :type FileType: str
        :param LibrarySet: 查询人员库列表，可填写学生们的注册照所在人员库
        :type LibrarySet: list of str
        :param MaxVideoDuration: 视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束
        :type MaxVideoDuration: int
        """
        self.FileContent = None
        self.FileType = None
        self.LibrarySet = None
        self.MaxVideoDuration = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubmitTraditionalClassTaskResponse(AbstractModel):
    """SubmitTraditionalClassTask返回参数结构体

    """

    def __init__(self):
        """
        :param ImageResults: 图像任务直接返回结果，包括： ActionInfo、FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SuspectedInfo(AbstractModel):
    """疑似出席人员

    """

    def __init__(self):
        """
        :param FaceSet: TopN匹配信息列表
        :type FaceSet: list of FrameInfo
        :param PersonId: 识别到的人员id
        :type PersonId: str
        """
        self.FaceSet = None
        self.PersonId = None


    def _deserialize(self, params):
        if params.get("FaceSet") is not None:
            self.FaceSet = []
            for item in params.get("FaceSet"):
                obj = FrameInfo()
                obj._deserialize(item)
                self.FaceSet.append(obj)
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TeacherOutScreenResult(AbstractModel):
    """教师是否在屏幕内判断结果

    """

    def __init__(self):
        """
        :param Class: 动作识别结果，InScreen：在屏幕内
OutScreen：不在屏幕内
        :type Class: str
        :param Height: 识别结果高度
        :type Height: int
        :param Left: 识别结果左坐标
        :type Left: int
        :param Top: 识别结果顶坐标
        :type Top: int
        :param Width: 识别结果宽度
        :type Width: int
        """
        self.Class = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Class = params.get("Class")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TextItem(AbstractModel):
    """当前句子的信息

    """

    def __init__(self):
        """
        :param Words: 当前句子包含的所有单词信息
        :type Words: list of Word
        :param Confidence: 当前句子的置信度
        :type Confidence: float
        :param Mbtm: 当前句子语音的起始时间点，单位为ms
        :type Mbtm: int
        :param Metm: 当前句子语音的终止时间点，单位为ms
        :type Metm: int
        :param Tag: 保留参数，暂无意义
        :type Tag: int
        :param Text: 当前句子
        :type Text: str
        :param TextSize: 当前句子的字节数
        :type TextSize: int
        """
        self.Words = None
        self.Confidence = None
        self.Mbtm = None
        self.Metm = None
        self.Tag = None
        self.Text = None
        self.TextSize = None


    def _deserialize(self, params):
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = Word()
                obj._deserialize(item)
                self.Words.append(obj)
        self.Confidence = params.get("Confidence")
        self.Mbtm = params.get("Mbtm")
        self.Metm = params.get("Metm")
        self.Tag = params.get("Tag")
        self.Text = params.get("Text")
        self.TextSize = params.get("TextSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TimeInfoResult(AbstractModel):
    """TimeInfoResult

    """

    def __init__(self):
        """
        :param Duration: 持续时间，单位毫秒
        :type Duration: int
        :param EndTs: 结束时间戳，单位毫秒
        :type EndTs: int
        :param StartTs: 开始时间戳，单位毫秒
        :type StartTs: int
        """
        self.Duration = None
        self.EndTs = None
        self.StartTs = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.EndTs = params.get("EndTs")
        self.StartTs = params.get("StartTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TimeType(AbstractModel):
    """起止时间

    """

    def __init__(self):
        """
        :param EndTime: 结束时间戳
        :type EndTime: int
        :param StartTime: 起始时间戳
        :type StartTime: int
        """
        self.EndTime = None
        self.StartTime = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TransmitAudioStreamRequest(AbstractModel):
    """TransmitAudioStream请求参数结构体

    """

    def __init__(self):
        """
        :param Functions: 功能开关列表，表示是否需要打开相应的功能，返回相应的信息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义。
        :type SeqId: int
        :param SessionId: 语音段唯一标识，一个完整语音一个SessionId。
        :type SessionId: str
        :param UserVoiceData: 当前数据包数据, 流式模式下数据包大小可以按需设置，在网络良好的情况下，建议设置为0.5k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。
        :type UserVoiceData: str
        :param VoiceEncodeType: 语音编码类型 1:pcm。
        :type VoiceEncodeType: int
        :param VoiceFileType: 语音文件类型 	1: raw, 2: wav, 3: mp3 (语言文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败)。
        :type VoiceFileType: int
        :param IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param Lang: 音频源的语言，默认0为英文，1为中文
        :type Lang: int
        :param StorageMode: 是否临时保存 音频链接
        :type StorageMode: int
        :param VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
        :type VocabLibNameList: list of str
        """
        self.Functions = None
        self.SeqId = None
        self.SessionId = None
        self.UserVoiceData = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None
        self.IsEnd = None
        self.Lang = None
        self.StorageMode = None
        self.VocabLibNameList = None


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self.Functions = Function()
            self.Functions._deserialize(params.get("Functions"))
        self.SeqId = params.get("SeqId")
        self.SessionId = params.get("SessionId")
        self.UserVoiceData = params.get("UserVoiceData")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        self.IsEnd = params.get("IsEnd")
        self.Lang = params.get("Lang")
        self.StorageMode = params.get("StorageMode")
        self.VocabLibNameList = params.get("VocabLibNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TransmitAudioStreamResponse(AbstractModel):
    """TransmitAudioStream返回参数结构体

    """

    def __init__(self):
        """
        :param AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
        :type Texts: list of WholeTextItem
        :param VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param AllTexts: 音频全部文本。
        :type AllTexts: str
        :param AudioUrl: 临时保存的音频链接
        :type AudioUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsrStat = None
        self.Texts = None
        self.VocabAnalysisDetailInfo = None
        self.VocabAnalysisStatInfo = None
        self.AllTexts = None
        self.AudioUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self.AsrStat = ASRStat()
            self.AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self.Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self.Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self.VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self.VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self.VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self.VocabAnalysisStatInfo.append(obj)
        self.AllTexts = params.get("AllTexts")
        self.AudioUrl = params.get("AudioUrl")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VocabDetailInfomation(AbstractModel):
    """词汇库中的单词出现在音频中的那个句子的起始时间和结束时间信息

    """

    def __init__(self):
        """
        :param VocabDetailInfo: 词汇库中的单词出现在该音频中的那个句子的时间戳，出现了几次，就返回对应次数的起始和结束时间戳
        :type VocabDetailInfo: list of DetailInfo
        :param VocabLibName: 词汇库名
        :type VocabLibName: str
        """
        self.VocabDetailInfo = None
        self.VocabLibName = None


    def _deserialize(self, params):
        if params.get("VocabDetailInfo") is not None:
            self.VocabDetailInfo = []
            for item in params.get("VocabDetailInfo"):
                obj = DetailInfo()
                obj._deserialize(item)
                self.VocabDetailInfo.append(obj)
        self.VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VocabStatInfomation(AbstractModel):
    """词汇库中的单词出现在音频中的总次数信息

    """

    def __init__(self):
        """
        :param VocabDetailInfo: 单词出现在该音频中总次数
        :type VocabDetailInfo: list of StatInfo
        :param VocabLibName: 词汇库名称
        :type VocabLibName: str
        """
        self.VocabDetailInfo = None
        self.VocabLibName = None


    def _deserialize(self, params):
        if params.get("VocabDetailInfo") is not None:
            self.VocabDetailInfo = []
            for item in params.get("VocabDetailInfo"):
                obj = StatInfo()
                obj._deserialize(item)
                self.VocabDetailInfo.append(obj)
        self.VocabLibName = params.get("VocabLibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class WholeTextItem(AbstractModel):
    """含有语速的句子信息

    """

    def __init__(self):
        """
        :param TextItem: 当前句子的信息
        :type TextItem: :class:`tencentcloud.tci.v20190318.models.TextItem`
        :param AvgVolume: Vad的平均音量
        :type AvgVolume: float
        :param MaxVolume: Vad的最大音量
        :type MaxVolume: float
        :param MinVolume: Vad的最小音量
        :type MinVolume: float
        :param Speed: 当前句子的语速
        :type Speed: float
        """
        self.TextItem = None
        self.AvgVolume = None
        self.MaxVolume = None
        self.MinVolume = None
        self.Speed = None


    def _deserialize(self, params):
        if params.get("TextItem") is not None:
            self.TextItem = TextItem()
            self.TextItem._deserialize(params.get("TextItem"))
        self.AvgVolume = params.get("AvgVolume")
        self.MaxVolume = params.get("MaxVolume")
        self.MinVolume = params.get("MinVolume")
        self.Speed = params.get("Speed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Word(AbstractModel):
    """当前句子包含的所有单词信息

    """

    def __init__(self):
        """
        :param Confidence: 当前词的置信度
        :type Confidence: float
        :param Mbtm: 当前单词语音的起始时间点，单位为ms
        :type Mbtm: int
        :param Metm: 当前单词语音的终止时间点，单位为ms
        :type Metm: int
        :param Text: 当前词
        :type Text: str
        :param Wsize: 当前词的字节数
        :type Wsize: int
        """
        self.Confidence = None
        self.Mbtm = None
        self.Metm = None
        self.Text = None
        self.Wsize = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Mbtm = params.get("Mbtm")
        self.Metm = params.get("Metm")
        self.Text = params.get("Text")
        self.Wsize = params.get("Wsize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class WordTimePair(AbstractModel):
    """单词出现的那个句子的起始时间和结束时间信息

    """

    def __init__(self):
        """
        :param Mbtm: 单词出现的那个句子的起始时间
        :type Mbtm: int
        :param Metm: 	单词出现的那个句子的结束时间
        :type Metm: int
        """
        self.Mbtm = None
        self.Metm = None


    def _deserialize(self, params):
        self.Mbtm = params.get("Mbtm")
        self.Metm = params.get("Metm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        