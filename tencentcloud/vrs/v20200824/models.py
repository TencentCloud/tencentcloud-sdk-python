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


class CancelVRSTaskRequest(AbstractModel):
    """CancelVRSTask请求参数结构体

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
        


class CancelVRSTaskResponse(AbstractModel):
    """CancelVRSTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务ID
        :type Data: :class:`tencentcloud.vrs.v20200824.models.CancelVRSTaskRsp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CancelVRSTaskRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CancelVRSTaskRsp(AbstractModel):
    """取消任务响应

    """


class CreateVRSTaskRequest(AbstractModel):
    """CreateVRSTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 唯一请求 ID
        :type SessionId: str
        :param _VoiceName: 音色名称
        :type VoiceName: str
        :param _SampleRate: 音频采样率：

16000：16k
        :type SampleRate: int
        :param _VoiceGender: 音色性别:

1-male

2-female
        :type VoiceGender: int
        :param _VoiceLanguage: 语言类型：

1-中文
        :type VoiceLanguage: int
        :param _Codec: 音频格式，音频类型(wav,mp3,aac,m4a)
        :type Codec: str
        :param _AudioIdList: 音频ID集合
        :type AudioIdList: list of str
        :param _CallbackUrl: 回调 URL，用户自行搭建的用于接收结果的服务URL。如果用户使用轮询方式获取识别结果，则无需提交该参数。
回调采用POST请求方式，Content-Type为application/json，回调数据格式如下:{"TaskId":"xxxxxxxxxxxxxx","Status":2,"StatusStr":"success","VoiceType":xxxxx,"ErrorMsg":""}
        :type CallbackUrl: str
        :param _ModelType: 模型类型 1:在线 2:离线  默认为1
        :type ModelType: int
        :param _TaskType: 任务类型 0:轻量版复刻
默认为0
        :type TaskType: int
        :param _VPRAudioId: 校验音频ID
        :type VPRAudioId: str
        """
        self._SessionId = None
        self._VoiceName = None
        self._SampleRate = None
        self._VoiceGender = None
        self._VoiceLanguage = None
        self._Codec = None
        self._AudioIdList = None
        self._CallbackUrl = None
        self._ModelType = None
        self._TaskType = None
        self._VPRAudioId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def VoiceName(self):
        return self._VoiceName

    @VoiceName.setter
    def VoiceName(self, VoiceName):
        self._VoiceName = VoiceName

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def VoiceGender(self):
        return self._VoiceGender

    @VoiceGender.setter
    def VoiceGender(self, VoiceGender):
        self._VoiceGender = VoiceGender

    @property
    def VoiceLanguage(self):
        return self._VoiceLanguage

    @VoiceLanguage.setter
    def VoiceLanguage(self, VoiceLanguage):
        self._VoiceLanguage = VoiceLanguage

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def AudioIdList(self):
        return self._AudioIdList

    @AudioIdList.setter
    def AudioIdList(self, AudioIdList):
        self._AudioIdList = AudioIdList

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def ModelType(self):
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def VPRAudioId(self):
        return self._VPRAudioId

    @VPRAudioId.setter
    def VPRAudioId(self, VPRAudioId):
        self._VPRAudioId = VPRAudioId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._VoiceName = params.get("VoiceName")
        self._SampleRate = params.get("SampleRate")
        self._VoiceGender = params.get("VoiceGender")
        self._VoiceLanguage = params.get("VoiceLanguage")
        self._Codec = params.get("Codec")
        self._AudioIdList = params.get("AudioIdList")
        self._CallbackUrl = params.get("CallbackUrl")
        self._ModelType = params.get("ModelType")
        self._TaskType = params.get("TaskType")
        self._VPRAudioId = params.get("VPRAudioId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVRSTaskRespData(AbstractModel):
    """声音复刻任务创建响应

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
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
        


class CreateVRSTaskResponse(AbstractModel):
    """CreateVRSTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建任务结果
        :type Data: :class:`tencentcloud.vrs.v20200824.models.CreateVRSTaskRespData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateVRSTaskRespData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVRSTaskStatusRequest(AbstractModel):
    """DescribeVRSTaskStatus请求参数结构体

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
        


class DescribeVRSTaskStatusRespData(AbstractModel):
    """任务结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _Status: 任务状态码，0：任务等待，1：任务执行中，2：任务成功，3：任务失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusStr: 任务状态，waiting：任务等待，doing：任务执行中，success：任务成功，failed：任务失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusStr: str
        :param _VoiceType: 音色id
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceType: int
        :param _ErrorMsg: 失败原因说明。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        """
        self._TaskId = None
        self._Status = None
        self._StatusStr = None
        self._VoiceType = None
        self._ErrorMsg = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusStr(self):
        return self._StatusStr

    @StatusStr.setter
    def StatusStr(self, StatusStr):
        self._StatusStr = StatusStr

    @property
    def VoiceType(self):
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._StatusStr = params.get("StatusStr")
        self._VoiceType = params.get("VoiceType")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVRSTaskStatusResponse(AbstractModel):
    """DescribeVRSTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 声音复刻任务结果
        :type Data: :class:`tencentcloud.vrs.v20200824.models.DescribeVRSTaskStatusRespData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeVRSTaskStatusRespData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DetectEnvAndSoundQualityRequest(AbstractModel):
    """DetectEnvAndSoundQuality请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TextId: 标注文本信息 ID
        :type TextId: str
        :param _AudioData: 语音数据 要使用base64编码(采用python语言时注意读取文件时需要转成base64字符串编码，例如：str(base64.b64encode(open("input.aac", mode="rb").read()), encoding='utf-8') )。
        :type AudioData: str
        :param _Codec: 音频格式，音频类型(wav,mp3,aac,m4a)
        :type Codec: str
        :param _TypeId: 1:环境检测 2:音质检测
        :type TypeId: int
        :param _SampleRate: 音频采样率：

16000：16k（默认）
        :type SampleRate: int
        """
        self._TextId = None
        self._AudioData = None
        self._Codec = None
        self._TypeId = None
        self._SampleRate = None

    @property
    def TextId(self):
        return self._TextId

    @TextId.setter
    def TextId(self, TextId):
        self._TextId = TextId

    @property
    def AudioData(self):
        return self._AudioData

    @AudioData.setter
    def AudioData(self, AudioData):
        self._AudioData = AudioData

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def TypeId(self):
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate


    def _deserialize(self, params):
        self._TextId = params.get("TextId")
        self._AudioData = params.get("AudioData")
        self._Codec = params.get("Codec")
        self._TypeId = params.get("TypeId")
        self._SampleRate = params.get("SampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectEnvAndSoundQualityResponse(AbstractModel):
    """DetectEnvAndSoundQuality返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 检测结果
        :type Data: :class:`tencentcloud.vrs.v20200824.models.DetectionEnvAndSoundQualityRespData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DetectionEnvAndSoundQualityRespData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DetectionEnvAndSoundQualityRespData(AbstractModel):
    """环境检测和音频检测响应

    """

    def __init__(self):
        r"""
        :param _AudioId: 音频ID （用于创建任务接口AudioIds）,环境检测该值为空，仅在音质检测情况下返回
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioId: str
        :param _DetectionCode: 检测code 

0 表示当前语音通过
-1 表示检测失败，需要重试
-2 表示语音检测不通过，提示用户再重新录制一下（通常漏读，错读，或多读）
-3 表示语音中噪声较大，不通过
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionCode: int
        :param _DetectionMsg: 检测提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionMsg: str
        :param _DetectionTip: 检测提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionTip: list of Words
        """
        self._AudioId = None
        self._DetectionCode = None
        self._DetectionMsg = None
        self._DetectionTip = None

    @property
    def AudioId(self):
        return self._AudioId

    @AudioId.setter
    def AudioId(self, AudioId):
        self._AudioId = AudioId

    @property
    def DetectionCode(self):
        return self._DetectionCode

    @DetectionCode.setter
    def DetectionCode(self, DetectionCode):
        self._DetectionCode = DetectionCode

    @property
    def DetectionMsg(self):
        return self._DetectionMsg

    @DetectionMsg.setter
    def DetectionMsg(self, DetectionMsg):
        self._DetectionMsg = DetectionMsg

    @property
    def DetectionTip(self):
        return self._DetectionTip

    @DetectionTip.setter
    def DetectionTip(self, DetectionTip):
        self._DetectionTip = DetectionTip


    def _deserialize(self, params):
        self._AudioId = params.get("AudioId")
        self._DetectionCode = params.get("DetectionCode")
        self._DetectionMsg = params.get("DetectionMsg")
        if params.get("DetectionTip") is not None:
            self._DetectionTip = []
            for item in params.get("DetectionTip"):
                obj = Words()
                obj._deserialize(item)
                self._DetectionTip.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadVRSModelRequest(AbstractModel):
    """DownloadVRSModel请求参数结构体

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
        


class DownloadVRSModelResponse(AbstractModel):
    """DownloadVRSModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 响应
        :type Data: :class:`tencentcloud.vrs.v20200824.models.DownloadVRSModelRsp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DownloadVRSModelRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DownloadVRSModelRsp(AbstractModel):
    """离线声音复刻模型下载响应

    """

    def __init__(self):
        r"""
        :param _Model: 模型cos地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: str
        :param _VoiceName: 音色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceName: str
        :param _VoiceGender: 音色性别:
1-male
2-female
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceGender: int
        :param _VoiceLanguage: 语言类型：
1-中文
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceLanguage: int
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._Model = None
        self._VoiceName = None
        self._VoiceGender = None
        self._VoiceLanguage = None
        self._TaskId = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def VoiceName(self):
        return self._VoiceName

    @VoiceName.setter
    def VoiceName(self, VoiceName):
        self._VoiceName = VoiceName

    @property
    def VoiceGender(self):
        return self._VoiceGender

    @VoiceGender.setter
    def VoiceGender(self, VoiceGender):
        self._VoiceGender = VoiceGender

    @property
    def VoiceLanguage(self):
        return self._VoiceLanguage

    @VoiceLanguage.setter
    def VoiceLanguage(self, VoiceLanguage):
        self._VoiceLanguage = VoiceLanguage

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._VoiceName = params.get("VoiceName")
        self._VoiceGender = params.get("VoiceGender")
        self._VoiceLanguage = params.get("VoiceLanguage")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _Data: 文本列表
        :type Data: :class:`tencentcloud.vrs.v20200824.models.TrainingTexts`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TrainingTexts()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetVRSVoiceTypesRequest(AbstractModel):
    """GetVRSVoiceTypes请求参数结构体

    """


class GetVRSVoiceTypesResponse(AbstractModel):
    """GetVRSVoiceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 复刻音色信息
        :type Data: :class:`tencentcloud.vrs.v20200824.models.VoiceTypeListData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = VoiceTypeListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class TrainingText(AbstractModel):
    """训练文本

    """

    def __init__(self):
        r"""
        :param _TextId: 文本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TextId: str
        :param _Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
        self._TextId = None
        self._Text = None

    @property
    def TextId(self):
        return self._TextId

    @TextId.setter
    def TextId(self, TextId):
        self._TextId = TextId

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._TextId = params.get("TextId")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingTexts(AbstractModel):
    """训练文本列表

    """

    def __init__(self):
        r"""
        :param _TrainingTextList: 训练文本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingTextList: list of TrainingText
        """
        self._TrainingTextList = None

    @property
    def TrainingTextList(self):
        return self._TrainingTextList

    @TrainingTextList.setter
    def TrainingTextList(self, TrainingTextList):
        self._TrainingTextList = TrainingTextList


    def _deserialize(self, params):
        if params.get("TrainingTextList") is not None:
            self._TrainingTextList = []
            for item in params.get("TrainingTextList"):
                obj = TrainingText()
                obj._deserialize(item)
                self._TrainingTextList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceTypeInfo(AbstractModel):
    """复刻音色详情

    """

    def __init__(self):
        r"""
        :param _VoiceType: 音色id
        :type VoiceType: int
        :param _VoiceName: 音色名称
        :type VoiceName: str
        :param _VoiceGender: 音色性别: 1-male 2-female
        :type VoiceGender: int
        :param _TaskType: 复刻类型: 0-轻量版复刻 1-基础版复刻
        :type TaskType: int
        :param _TaskID: 复刻任务 ID
        :type TaskID: str
        :param _DateCreated: 创建时间
        :type DateCreated: str
        :param _IsDeployed: 部署状态。若已部署，则可通过语音合成接口调用该音色
        :type IsDeployed: bool
        """
        self._VoiceType = None
        self._VoiceName = None
        self._VoiceGender = None
        self._TaskType = None
        self._TaskID = None
        self._DateCreated = None
        self._IsDeployed = None

    @property
    def VoiceType(self):
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def VoiceName(self):
        return self._VoiceName

    @VoiceName.setter
    def VoiceName(self, VoiceName):
        self._VoiceName = VoiceName

    @property
    def VoiceGender(self):
        return self._VoiceGender

    @VoiceGender.setter
    def VoiceGender(self, VoiceGender):
        self._VoiceGender = VoiceGender

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def DateCreated(self):
        return self._DateCreated

    @DateCreated.setter
    def DateCreated(self, DateCreated):
        self._DateCreated = DateCreated

    @property
    def IsDeployed(self):
        return self._IsDeployed

    @IsDeployed.setter
    def IsDeployed(self, IsDeployed):
        self._IsDeployed = IsDeployed


    def _deserialize(self, params):
        self._VoiceType = params.get("VoiceType")
        self._VoiceName = params.get("VoiceName")
        self._VoiceGender = params.get("VoiceGender")
        self._TaskType = params.get("TaskType")
        self._TaskID = params.get("TaskID")
        self._DateCreated = params.get("DateCreated")
        self._IsDeployed = params.get("IsDeployed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceTypeListData(AbstractModel):
    """音色信息列表

    """

    def __init__(self):
        r"""
        :param _VoiceTypeList: 音色信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceTypeList: list of VoiceTypeInfo
        """
        self._VoiceTypeList = None

    @property
    def VoiceTypeList(self):
        return self._VoiceTypeList

    @VoiceTypeList.setter
    def VoiceTypeList(self, VoiceTypeList):
        self._VoiceTypeList = VoiceTypeList


    def _deserialize(self, params):
        if params.get("VoiceTypeList") is not None:
            self._VoiceTypeList = []
            for item in params.get("VoiceTypeList"):
                obj = VoiceTypeInfo()
                obj._deserialize(item)
                self._VoiceTypeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Words(AbstractModel):
    """音频检测提示信息：
    1.检测字是否存在多读、 少读、 错读等
    2.检测准确度和流畅度

    """

    def __init__(self):
        r"""
        :param _PronAccuracy: 准确度 (<75则认为不合格)
注意：此字段可能返回 null，表示取不到有效值。
        :type PronAccuracy: float
        :param _PronFluency: 流畅度 (<0.95则认为不合格)
注意：此字段可能返回 null，表示取不到有效值。
        :type PronFluency: float
        :param _Tag: tag: 
0: match  匹配
1: insert   多读
2: delete  少读
3: replace 错读
4: oov  待评估字不在发音评估的词库
5: unknown 未知错误
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: int
        :param _Word: 字
注意：此字段可能返回 null，表示取不到有效值。
        :type Word: str
        """
        self._PronAccuracy = None
        self._PronFluency = None
        self._Tag = None
        self._Word = None

    @property
    def PronAccuracy(self):
        return self._PronAccuracy

    @PronAccuracy.setter
    def PronAccuracy(self, PronAccuracy):
        self._PronAccuracy = PronAccuracy

    @property
    def PronFluency(self):
        return self._PronFluency

    @PronFluency.setter
    def PronFluency(self, PronFluency):
        self._PronFluency = PronFluency

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word


    def _deserialize(self, params):
        self._PronAccuracy = params.get("PronAccuracy")
        self._PronFluency = params.get("PronFluency")
        self._Tag = params.get("Tag")
        self._Word = params.get("Word")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        