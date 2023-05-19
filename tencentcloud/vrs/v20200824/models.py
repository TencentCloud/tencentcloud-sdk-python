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


class CreateVRSTaskRequest(AbstractModel):
    """CreateVRSTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: 唯一请求 ID
        :type SessionId: str
        :param VoiceName: 音色名称
        :type VoiceName: str
        :param SampleRate: 音频采样率：

16000：16k
        :type SampleRate: int
        :param VoiceGender: 音色性别:

1-male

2-female
        :type VoiceGender: int
        :param VoiceLanguage: 语言类型：

1-中文
        :type VoiceLanguage: int
        :param Codec: 音频格式，音频类型(wav,mp3,aac,m4a)
        :type Codec: str
        :param AudioIdList: 音频ID集合
        :type AudioIdList: list of str
        :param CallbackUrl: 回调 URL，用户自行搭建的用于接收结果的服务URL。如果用户使用轮询方式获取识别结果，则无需提交该参数。
回调采用POST请求方式，Content-Type为application/json，回调数据格式如下:{"TaskId":"xxxxxxxxxxxxxx","Status":2,"StatusStr":"success","VoiceType":xxxxx,"ErrorMsg":""}
        :type CallbackUrl: str
        """
        self.SessionId = None
        self.VoiceName = None
        self.SampleRate = None
        self.VoiceGender = None
        self.VoiceLanguage = None
        self.Codec = None
        self.AudioIdList = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.VoiceName = params.get("VoiceName")
        self.SampleRate = params.get("SampleRate")
        self.VoiceGender = params.get("VoiceGender")
        self.VoiceLanguage = params.get("VoiceLanguage")
        self.Codec = params.get("Codec")
        self.AudioIdList = params.get("AudioIdList")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVRSTaskRespData(AbstractModel):
    """声音复刻任务创建响应

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
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
        


class CreateVRSTaskResponse(AbstractModel):
    """CreateVRSTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 创建任务结果
        :type Data: :class:`tencentcloud.vrs.v20200824.models.CreateVRSTaskRespData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CreateVRSTaskRespData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeVRSTaskStatusRequest(AbstractModel):
    """DescribeVRSTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
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
        


class DescribeVRSTaskStatusRespData(AbstractModel):
    """任务结果

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param Status: 任务状态码，0：任务等待，1：任务执行中，2：任务成功，3：任务失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusStr: 任务状态，waiting：任务等待，doing：任务执行中，success：任务成功，failed：任务失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusStr: str
        :param VoiceType: 音色id
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceType: int
        :param ErrorMsg: 失败原因说明。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        """
        self.TaskId = None
        self.Status = None
        self.StatusStr = None
        self.VoiceType = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.StatusStr = params.get("StatusStr")
        self.VoiceType = params.get("VoiceType")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVRSTaskStatusResponse(AbstractModel):
    """DescribeVRSTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 声音复刻任务结果
        :type Data: :class:`tencentcloud.vrs.v20200824.models.DescribeVRSTaskStatusRespData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeVRSTaskStatusRespData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DetectEnvAndSoundQualityRequest(AbstractModel):
    """DetectEnvAndSoundQuality请求参数结构体

    """

    def __init__(self):
        r"""
        :param TextId: 标注文本信息 ID
        :type TextId: str
        :param AudioData: 语音数据 要使用base64编码(采用python语言时注意读取文件时需要转成base64字符串编码，例如：str(base64.b64encode(open("input.aac", mode="rb").read()), encoding='utf-8') )。
        :type AudioData: str
        :param Codec: 音频格式，音频类型(wav,mp3,aac,m4a)
        :type Codec: str
        :param TypeId: 1:环境检测 2:音质检测
        :type TypeId: int
        :param SampleRate: 音频采样率：

16000：16k（默认）
        :type SampleRate: int
        """
        self.TextId = None
        self.AudioData = None
        self.Codec = None
        self.TypeId = None
        self.SampleRate = None


    def _deserialize(self, params):
        self.TextId = params.get("TextId")
        self.AudioData = params.get("AudioData")
        self.Codec = params.get("Codec")
        self.TypeId = params.get("TypeId")
        self.SampleRate = params.get("SampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectEnvAndSoundQualityResponse(AbstractModel):
    """DetectEnvAndSoundQuality返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 检测结果
        :type Data: :class:`tencentcloud.vrs.v20200824.models.DetectionEnvAndSoundQualityRespData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DetectionEnvAndSoundQualityRespData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DetectionEnvAndSoundQualityRespData(AbstractModel):
    """环境检测和音频检测响应

    """

    def __init__(self):
        r"""
        :param AudioId: 音频ID （用于创建任务接口AudioIds）,环境检测该值为空，仅在音质检测情况下返回
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioId: str
        :param DetectionCode: 检测code 

0 表示当前语音通过
-1 表示检测失败，需要重试
-2 表示语音检测不通过，提示用户再重新录制一下（通常漏读，错读，或多读）
-3 表示语音中噪声较大，不通过
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionCode: int
        :param DetectionMsg: 检测提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionMsg: str
        :param DetectionTip: 检测提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionTip: list of Words
        """
        self.AudioId = None
        self.DetectionCode = None
        self.DetectionMsg = None
        self.DetectionTip = None


    def _deserialize(self, params):
        self.AudioId = params.get("AudioId")
        self.DetectionCode = params.get("DetectionCode")
        self.DetectionMsg = params.get("DetectionMsg")
        if params.get("DetectionTip") is not None:
            self.DetectionTip = []
            for item in params.get("DetectionTip"):
                obj = Words()
                obj._deserialize(item)
                self.DetectionTip.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTrainingTextRequest(AbstractModel):
    """GetTrainingText请求参数结构体

    """


class GetTrainingTextResponse(AbstractModel):
    """GetTrainingText返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 文本列表
        :type Data: :class:`tencentcloud.vrs.v20200824.models.TrainingTexts`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TrainingTexts()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class TrainingText(AbstractModel):
    """训练文本

    """

    def __init__(self):
        r"""
        :param TextId: 文本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TextId: str
        :param Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
        self.TextId = None
        self.Text = None


    def _deserialize(self, params):
        self.TextId = params.get("TextId")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingTexts(AbstractModel):
    """训练文本列表

    """

    def __init__(self):
        r"""
        :param TrainingTextList: 训练文本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingTextList: list of TrainingText
        """
        self.TrainingTextList = None


    def _deserialize(self, params):
        if params.get("TrainingTextList") is not None:
            self.TrainingTextList = []
            for item in params.get("TrainingTextList"):
                obj = TrainingText()
                obj._deserialize(item)
                self.TrainingTextList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Words(AbstractModel):
    """音频检测提示信息：
    1.检测字是否存在多读、 少读、 错读等
    2.检测准确度和流畅度

    """

    def __init__(self):
        r"""
        :param PronAccuracy: 准确度 (<75则认为不合格)
注意：此字段可能返回 null，表示取不到有效值。
        :type PronAccuracy: float
        :param PronFluency: 流畅度 (<0.95则认为不合格)
注意：此字段可能返回 null，表示取不到有效值。
        :type PronFluency: float
        :param Tag: tag: 
0: match  匹配
1: insert   多读
2: delete  少读
3: replace 错读
4: oov  待评估字不在发音评估的词库
5: unknown 未知错误
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: int
        :param Word: 字
注意：此字段可能返回 null，表示取不到有效值。
        :type Word: str
        """
        self.PronAccuracy = None
        self.PronFluency = None
        self.Tag = None
        self.Word = None


    def _deserialize(self, params):
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.Tag = params.get("Tag")
        self.Word = params.get("Word")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        