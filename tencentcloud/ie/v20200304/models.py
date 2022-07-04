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


class ArtifactReduction(AbstractModel):
    """去编码毛刺、伪影参数

    """

    def __init__(self):
        r"""
        :param Type: 去毛刺方式：weak,,strong
        :type Type: str
        :param Algorithm: 去毛刺算法，可选项：
edaf,
wdaf，
默认edaf。
注意：此参数已经弃用
        :type Algorithm: str
        """
        self.Type = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEnhance(AbstractModel):
    """音频音效增强，只支持无背景音的音频

    """

    def __init__(self):
        r"""
        :param Type: 音效增强种类，可选项：normal
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioInfo(AbstractModel):
    """音频参数信息

    """

    def __init__(self):
        r"""
        :param Bitrate: 音频码率，取值范围：0 和 [26, 256]，单位：kbps。
注意：当取值为 0，表示音频码率和原始音频保持一致。
        :type Bitrate: int
        :param Codec: 音频编码器，可选项：aac,mp3,ac3,flac,mp2。
        :type Codec: str
        :param Channel: 声道数，可选项：
1：单声道，
2：双声道，
6：立体声。
        :type Channel: int
        :param SampleRate: 采样率，单位：Hz。可选项：32000，44100,48000
        :type SampleRate: int
        :param Denoise: 音频降噪信息
        :type Denoise: :class:`tencentcloud.ie.v20200304.models.Denoise`
        :param EnableMuteAudio: 开启添加静音，可选项：
0：不开启，
1：开启，
默认不开启
        :type EnableMuteAudio: int
        :param LoudnessInfo: 音频响度信息
        :type LoudnessInfo: :class:`tencentcloud.ie.v20200304.models.LoudnessInfo`
        :param AudioEnhance: 音频音效增强
        :type AudioEnhance: :class:`tencentcloud.ie.v20200304.models.AudioEnhance`
        :param RemoveReverb: 去除混音
        :type RemoveReverb: :class:`tencentcloud.ie.v20200304.models.RemoveReverb`
        """
        self.Bitrate = None
        self.Codec = None
        self.Channel = None
        self.SampleRate = None
        self.Denoise = None
        self.EnableMuteAudio = None
        self.LoudnessInfo = None
        self.AudioEnhance = None
        self.RemoveReverb = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Codec = params.get("Codec")
        self.Channel = params.get("Channel")
        self.SampleRate = params.get("SampleRate")
        if params.get("Denoise") is not None:
            self.Denoise = Denoise()
            self.Denoise._deserialize(params.get("Denoise"))
        self.EnableMuteAudio = params.get("EnableMuteAudio")
        if params.get("LoudnessInfo") is not None:
            self.LoudnessInfo = LoudnessInfo()
            self.LoudnessInfo._deserialize(params.get("LoudnessInfo"))
        if params.get("AudioEnhance") is not None:
            self.AudioEnhance = AudioEnhance()
            self.AudioEnhance._deserialize(params.get("AudioEnhance"))
        if params.get("RemoveReverb") is not None:
            self.RemoveReverb = RemoveReverb()
            self.RemoveReverb._deserialize(params.get("RemoveReverb"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioInfoResultItem(AbstractModel):
    """任务结束后生成的文件音频信息

    """

    def __init__(self):
        r"""
        :param Stream: 音频流的流id。
        :type Stream: int
        :param Sample: 音频采样率 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Sample: int
        :param Channel: 音频声道数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: int
        :param Codec: 编码格式，如aac, mp3等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        :param Bitrate: 码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Duration: 音频时长，单位：ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        """
        self.Stream = None
        self.Sample = None
        self.Channel = None
        self.Codec = None
        self.Bitrate = None
        self.Duration = None


    def _deserialize(self, params):
        self.Stream = params.get("Stream")
        self.Sample = params.get("Sample")
        self.Channel = params.get("Channel")
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackInfo(AbstractModel):
    """任务结果回调地址信息

    """

    def __init__(self):
        r"""
        :param Url: 回调URL。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationEditingInfo(AbstractModel):
    """视频分类识别任务参数信息

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启视频分类识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationTaskResult(AbstractModel):
    """视频分类识别结果信息

    """

    def __init__(self):
        r"""
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 视频分类识别结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of ClassificationTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = ClassificationTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationTaskResultItem(AbstractModel):
    """视频分类识别结果项

    """

    def __init__(self):
        r"""
        :param Classification: 分类名称。
        :type Classification: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ColorEnhance(AbstractModel):
    """颜色增强参数

    """

    def __init__(self):
        r"""
        :param Type: 颜色增强类型，可选项：
1.  tra；
2.  weak；
3.  normal;
4.  strong;
注意：tra不支持自适应调整，处理速度更快；weak,normal,strong支持基于画面颜色自适应，处理速度更慢。
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosAuthMode(AbstractModel):
    """任务视频cos授权信息

    """

    def __init__(self):
        r"""
        :param Type: 授权类型，可选值： 
0：bucket授权，需要将对应bucket授权给本服务帐号（3020447271和100012301793），否则会读写cos失败； 
1：key托管，把cos的账号id和key托管于本服务，本服务会提供一个托管id； 
3：临时key授权。
注意：目前智能编辑还不支持临时key授权；画质重生目前只支持bucket授权
        :type Type: int
        :param HostedId: cos账号托管id，Type等于1时必选。
        :type HostedId: str
        :param SecretId: cos身份识别id，Type等于3时必选。
        :type SecretId: str
        :param SecretKey: cos身份秘钥，Type等于3时必选。
        :type SecretKey: str
        :param Token: 临时授权 token，Type等于3时必选。
        :type Token: str
        """
        self.Type = None
        self.HostedId = None
        self.SecretId = None
        self.SecretKey = None
        self.Token = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.HostedId = params.get("HostedId")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosInfo(AbstractModel):
    """任务视频cos信息

    """

    def __init__(self):
        r"""
        :param Region: cos 区域值。例如：ap-beijing。
        :type Region: str
        :param Bucket: cos 存储桶，格式为BuketName-AppId。例如：test-123456。
        :type Bucket: str
        :param Path: cos 路径。 
对于写表示目录，例如：/test； 
对于读表示文件路径，例如：/test/test.mp4。
        :type Path: str
        :param CosAuthMode: cos 授权信息，不填默认为公有权限。
        :type CosAuthMode: :class:`tencentcloud.ie.v20200304.models.CosAuthMode`
        """
        self.Region = None
        self.Bucket = None
        self.Path = None
        self.CosAuthMode = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.Path = params.get("Path")
        if params.get("CosAuthMode") is not None:
            self.CosAuthMode = CosAuthMode()
            self.CosAuthMode._deserialize(params.get("CosAuthMode"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverEditingInfo(AbstractModel):
    """智能封面任务参数信息

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启智能封面。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverTaskResult(AbstractModel):
    """智能封面结果信息

    """

    def __init__(self):
        r"""
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 智能封面结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of CoverTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = CoverTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverTaskResultItem(AbstractModel):
    """智能封面结果项

    """

    def __init__(self):
        r"""
        :param CoverUrl: 智能封面地址。
        :type CoverUrl: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.CoverUrl = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEditingTaskRequest(AbstractModel):
    """CreateEditingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param EditingInfo: 智能编辑任务参数。
        :type EditingInfo: :class:`tencentcloud.ie.v20200304.models.EditingInfo`
        :param DownInfo: 视频源信息。
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param SaveInfo: 结果存储信息。对于包含智能拆条、智能集锦或者智能封面的任务必选。
        :type SaveInfo: :class:`tencentcloud.ie.v20200304.models.SaveInfo`
        :param CallbackInfo: 任务结果回调地址信息。
        :type CallbackInfo: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        self.EditingInfo = None
        self.DownInfo = None
        self.SaveInfo = None
        self.CallbackInfo = None


    def _deserialize(self, params):
        if params.get("EditingInfo") is not None:
            self.EditingInfo = EditingInfo()
            self.EditingInfo._deserialize(params.get("EditingInfo"))
        if params.get("DownInfo") is not None:
            self.DownInfo = DownInfo()
            self.DownInfo._deserialize(params.get("DownInfo"))
        if params.get("SaveInfo") is not None:
            self.SaveInfo = SaveInfo()
            self.SaveInfo._deserialize(params.get("SaveInfo"))
        if params.get("CallbackInfo") is not None:
            self.CallbackInfo = CallbackInfo()
            self.CallbackInfo._deserialize(params.get("CallbackInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEditingTaskResponse(AbstractModel):
    """CreateEditingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 编辑任务 ID，可以通过该 ID 查询任务状态。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateMediaProcessTaskRequest(AbstractModel):
    """CreateMediaProcessTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param MediaProcessInfo: 编辑处理任务参数。
        :type MediaProcessInfo: :class:`tencentcloud.ie.v20200304.models.MediaProcessInfo`
        :param SourceInfoSet: 编辑处理任务输入源列表。
        :type SourceInfoSet: list of MediaSourceInfo
        :param SaveInfoSet: 结果存储信息，对于涉及存储的请求必选。部子任务支持数组备份写，具体以对应任务文档为准。
        :type SaveInfoSet: list of SaveInfo
        :param CallbackInfoSet: 任务结果回调地址信息。部子任务支持数组备份回调，具体以对应任务文档为准。
        :type CallbackInfoSet: list of CallbackInfo
        """
        self.MediaProcessInfo = None
        self.SourceInfoSet = None
        self.SaveInfoSet = None
        self.CallbackInfoSet = None


    def _deserialize(self, params):
        if params.get("MediaProcessInfo") is not None:
            self.MediaProcessInfo = MediaProcessInfo()
            self.MediaProcessInfo._deserialize(params.get("MediaProcessInfo"))
        if params.get("SourceInfoSet") is not None:
            self.SourceInfoSet = []
            for item in params.get("SourceInfoSet"):
                obj = MediaSourceInfo()
                obj._deserialize(item)
                self.SourceInfoSet.append(obj)
        if params.get("SaveInfoSet") is not None:
            self.SaveInfoSet = []
            for item in params.get("SaveInfoSet"):
                obj = SaveInfo()
                obj._deserialize(item)
                self.SaveInfoSet.append(obj)
        if params.get("CallbackInfoSet") is not None:
            self.CallbackInfoSet = []
            for item in params.get("CallbackInfoSet"):
                obj = CallbackInfo()
                obj._deserialize(item)
                self.CallbackInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaProcessTaskResponse(AbstractModel):
    """CreateMediaProcessTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 编辑任务 ID，可以通过该 ID 查询任务状态和结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateMediaQualityRestorationTaskRequest(AbstractModel):
    """CreateMediaQualityRestorationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param DownInfo: 源文件地址。
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param TransInfo: 画质重生任务参数信息。
        :type TransInfo: list of SubTaskTranscodeInfo
        :param SaveInfo: 任务结束后文件存储信息。
        :type SaveInfo: :class:`tencentcloud.ie.v20200304.models.SaveInfo`
        :param CallbackInfo: 任务结果回调地址信息。
        :type CallbackInfo: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        self.DownInfo = None
        self.TransInfo = None
        self.SaveInfo = None
        self.CallbackInfo = None


    def _deserialize(self, params):
        if params.get("DownInfo") is not None:
            self.DownInfo = DownInfo()
            self.DownInfo._deserialize(params.get("DownInfo"))
        if params.get("TransInfo") is not None:
            self.TransInfo = []
            for item in params.get("TransInfo"):
                obj = SubTaskTranscodeInfo()
                obj._deserialize(item)
                self.TransInfo.append(obj)
        if params.get("SaveInfo") is not None:
            self.SaveInfo = SaveInfo()
            self.SaveInfo._deserialize(params.get("SaveInfo"))
        if params.get("CallbackInfo") is not None:
            self.CallbackInfo = CallbackInfo()
            self.CallbackInfo._deserialize(params.get("CallbackInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaQualityRestorationTaskResponse(AbstractModel):
    """CreateMediaQualityRestorationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 画质重生任务ID，可以通过该ID查询任务状态。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateQualityControlTaskRequest(AbstractModel):
    """CreateQualityControlTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param QualityControlInfo: 质检任务参数
        :type QualityControlInfo: :class:`tencentcloud.ie.v20200304.models.QualityControlInfo`
        :param DownInfo: 视频源信息
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param CallbackInfo: 任务结果回调地址信息
        :type CallbackInfo: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        self.QualityControlInfo = None
        self.DownInfo = None
        self.CallbackInfo = None


    def _deserialize(self, params):
        if params.get("QualityControlInfo") is not None:
            self.QualityControlInfo = QualityControlInfo()
            self.QualityControlInfo._deserialize(params.get("QualityControlInfo"))
        if params.get("DownInfo") is not None:
            self.DownInfo = DownInfo()
            self.DownInfo._deserialize(params.get("DownInfo"))
        if params.get("CallbackInfo") is not None:
            self.CallbackInfo = CallbackInfo()
            self.CallbackInfo._deserialize(params.get("CallbackInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQualityControlTaskResponse(AbstractModel):
    """CreateQualityControlTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 质检任务 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DarInfo(AbstractModel):
    """视频Dar信息

    """

    def __init__(self):
        r"""
        :param FillMode: 填充模式，可选值：
1：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。
2：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“。
默认为2。
        :type FillMode: int
        """
        self.FillMode = None


    def _deserialize(self, params):
        self.FillMode = params.get("FillMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Denoise(AbstractModel):
    """音频降噪

    """

    def __init__(self):
        r"""
        :param Type: 音频降噪强度，可选项：
1. weak
2.normal，
3.strong
默认为weak
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Denoising(AbstractModel):
    """去噪参数

    """

    def __init__(self):
        r"""
        :param Type: 去噪方式，可选项：
templ：时域降噪；
spatial：空域降噪,
fast-spatial：快速空域降噪。
注意：可选择组合方式：
1.type:"templ,spatial" ;
2.type:"templ,fast-spatial"。
        :type Type: str
        :param TemplStrength: 时域去噪强度，可选值：0.0-1.0 。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type TemplStrength: float
        :param SpatialStrength: 空域去噪强度，可选值：0.0-1.0 。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type SpatialStrength: float
        """
        self.Type = None
        self.TemplStrength = None
        self.SpatialStrength = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TemplStrength = params.get("TemplStrength")
        self.SpatialStrength = params.get("SpatialStrength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEditingTaskResultRequest(AbstractModel):
    """DescribeEditingTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 编辑任务 ID。
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
        


class DescribeEditingTaskResultResponse(AbstractModel):
    """DescribeEditingTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskResult: 编辑任务结果信息。
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.EditingTaskResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskResult") is not None:
            self.TaskResult = EditingTaskResult()
            self.TaskResult._deserialize(params.get("TaskResult"))
        self.RequestId = params.get("RequestId")


class DescribeMediaProcessTaskResultRequest(AbstractModel):
    """DescribeMediaProcessTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 编辑处理任务ID。
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
        


class DescribeMediaProcessTaskResultResponse(AbstractModel):
    """DescribeMediaProcessTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskResult: 任务处理结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.MediaProcessTaskResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskResult") is not None:
            self.TaskResult = MediaProcessTaskResult()
            self.TaskResult._deserialize(params.get("TaskResult"))
        self.RequestId = params.get("RequestId")


class DescribeMediaQualityRestorationTaskRusultRequest(AbstractModel):
    """DescribeMediaQualityRestorationTaskRusult请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 画质重生任务ID
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
        


class DescribeMediaQualityRestorationTaskRusultResponse(AbstractModel):
    """DescribeMediaQualityRestorationTaskRusult返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskResult: 画质重生任务结果信息
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.MediaQualityRestorationTaskResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskResult") is not None:
            self.TaskResult = MediaQualityRestorationTaskResult()
            self.TaskResult._deserialize(params.get("TaskResult"))
        self.RequestId = params.get("RequestId")


class DescribeQualityControlTaskResultRequest(AbstractModel):
    """DescribeQualityControlTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 质检任务 ID
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
        


class DescribeQualityControlTaskResultResponse(AbstractModel):
    """DescribeQualityControlTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskResult: 质检任务结果信息
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.QualityControlInfoTaskResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskResult") is not None:
            self.TaskResult = QualityControlInfoTaskResult()
            self.TaskResult._deserialize(params.get("TaskResult"))
        self.RequestId = params.get("RequestId")


class DownInfo(AbstractModel):
    """视频源信息

    """

    def __init__(self):
        r"""
        :param Type: 下载类型，可选值： 
0：UrlInfo； 
1：CosInfo。
        :type Type: int
        :param UrlInfo: Url形式下载信息，当Type等于0时必选。
        :type UrlInfo: :class:`tencentcloud.ie.v20200304.models.UrlInfo`
        :param CosInfo: Cos形式下载信息，当Type等于1时必选。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        self.Type = None
        self.UrlInfo = None
        self.CosInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("UrlInfo") is not None:
            self.UrlInfo = UrlInfo()
            self.UrlInfo._deserialize(params.get("UrlInfo"))
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicImageInfo(AbstractModel):
    """动图参数

    """

    def __init__(self):
        r"""
        :param Quality: 画面质量，范围：1~100。
<li>对于webp格式，默认：75</li>
<li>对于gif格式，小于10为低质量，大于50为高质量，其它为普通。默认：低质量。</li>
        :type Quality: int
        """
        self.Quality = None


    def _deserialize(self, params):
        self.Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditInfo(AbstractModel):
    """画质重生子任务视频剪辑参数

    """

    def __init__(self):
        r"""
        :param StartTime: 剪辑开始时间，单位：ms。
        :type StartTime: int
        :param EndTime: 剪辑结束时间，单位：ms
        :type EndTime: int
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditingInfo(AbstractModel):
    """智能编辑任务参数信息

    """

    def __init__(self):
        r"""
        :param TagEditingInfo: 视频标签识别任务参数，不填则不开启。
        :type TagEditingInfo: :class:`tencentcloud.ie.v20200304.models.TagEditingInfo`
        :param ClassificationEditingInfo: 视频分类识别任务参数，不填则不开启。
        :type ClassificationEditingInfo: :class:`tencentcloud.ie.v20200304.models.ClassificationEditingInfo`
        :param StripEditingInfo: 智能拆条任务参数，不填则不开启。
        :type StripEditingInfo: :class:`tencentcloud.ie.v20200304.models.StripEditingInfo`
        :param HighlightsEditingInfo: 智能集锦任务参数，不填则不开启。
        :type HighlightsEditingInfo: :class:`tencentcloud.ie.v20200304.models.HighlightsEditingInfo`
        :param CoverEditingInfo: 智能封面任务参数，不填则不开启。
        :type CoverEditingInfo: :class:`tencentcloud.ie.v20200304.models.CoverEditingInfo`
        :param OpeningEndingEditingInfo: 片头片尾识别任务参数，不填则不开启。
        :type OpeningEndingEditingInfo: :class:`tencentcloud.ie.v20200304.models.OpeningEndingEditingInfo`
        """
        self.TagEditingInfo = None
        self.ClassificationEditingInfo = None
        self.StripEditingInfo = None
        self.HighlightsEditingInfo = None
        self.CoverEditingInfo = None
        self.OpeningEndingEditingInfo = None


    def _deserialize(self, params):
        if params.get("TagEditingInfo") is not None:
            self.TagEditingInfo = TagEditingInfo()
            self.TagEditingInfo._deserialize(params.get("TagEditingInfo"))
        if params.get("ClassificationEditingInfo") is not None:
            self.ClassificationEditingInfo = ClassificationEditingInfo()
            self.ClassificationEditingInfo._deserialize(params.get("ClassificationEditingInfo"))
        if params.get("StripEditingInfo") is not None:
            self.StripEditingInfo = StripEditingInfo()
            self.StripEditingInfo._deserialize(params.get("StripEditingInfo"))
        if params.get("HighlightsEditingInfo") is not None:
            self.HighlightsEditingInfo = HighlightsEditingInfo()
            self.HighlightsEditingInfo._deserialize(params.get("HighlightsEditingInfo"))
        if params.get("CoverEditingInfo") is not None:
            self.CoverEditingInfo = CoverEditingInfo()
            self.CoverEditingInfo._deserialize(params.get("CoverEditingInfo"))
        if params.get("OpeningEndingEditingInfo") is not None:
            self.OpeningEndingEditingInfo = OpeningEndingEditingInfo()
            self.OpeningEndingEditingInfo._deserialize(params.get("OpeningEndingEditingInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditingTaskResult(AbstractModel):
    """智能识别任务结果信息

    """

    def __init__(self):
        r"""
        :param TaskId: 编辑任务 ID。
        :type TaskId: str
        :param Status: 编辑任务状态。 
1：执行中；2：已完成。
        :type Status: int
        :param TagTaskResult: 视频标签识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagTaskResult: :class:`tencentcloud.ie.v20200304.models.TagTaskResult`
        :param ClassificationTaskResult: 视频分类识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationTaskResult: :class:`tencentcloud.ie.v20200304.models.ClassificationTaskResult`
        :param StripTaskResult: 智能拆条结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type StripTaskResult: :class:`tencentcloud.ie.v20200304.models.StripTaskResult`
        :param HighlightsTaskResult: 智能集锦结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type HighlightsTaskResult: :class:`tencentcloud.ie.v20200304.models.HighlightsTaskResult`
        :param CoverTaskResult: 智能封面结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverTaskResult: :class:`tencentcloud.ie.v20200304.models.CoverTaskResult`
        :param OpeningEndingTaskResult: 片头片尾识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type OpeningEndingTaskResult: :class:`tencentcloud.ie.v20200304.models.OpeningEndingTaskResult`
        """
        self.TaskId = None
        self.Status = None
        self.TagTaskResult = None
        self.ClassificationTaskResult = None
        self.StripTaskResult = None
        self.HighlightsTaskResult = None
        self.CoverTaskResult = None
        self.OpeningEndingTaskResult = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        if params.get("TagTaskResult") is not None:
            self.TagTaskResult = TagTaskResult()
            self.TagTaskResult._deserialize(params.get("TagTaskResult"))
        if params.get("ClassificationTaskResult") is not None:
            self.ClassificationTaskResult = ClassificationTaskResult()
            self.ClassificationTaskResult._deserialize(params.get("ClassificationTaskResult"))
        if params.get("StripTaskResult") is not None:
            self.StripTaskResult = StripTaskResult()
            self.StripTaskResult._deserialize(params.get("StripTaskResult"))
        if params.get("HighlightsTaskResult") is not None:
            self.HighlightsTaskResult = HighlightsTaskResult()
            self.HighlightsTaskResult._deserialize(params.get("HighlightsTaskResult"))
        if params.get("CoverTaskResult") is not None:
            self.CoverTaskResult = CoverTaskResult()
            self.CoverTaskResult._deserialize(params.get("CoverTaskResult"))
        if params.get("OpeningEndingTaskResult") is not None:
            self.OpeningEndingTaskResult = OpeningEndingTaskResult()
            self.OpeningEndingTaskResult._deserialize(params.get("OpeningEndingTaskResult"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceProtect(AbstractModel):
    """人脸保护参数

    """

    def __init__(self):
        r"""
        :param FaceUsmRatio: 人脸区域增强强度，可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type FaceUsmRatio: float
        """
        self.FaceUsmRatio = None


    def _deserialize(self, params):
        self.FaceUsmRatio = params.get("FaceUsmRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """画质重生处理后文件的详细信息

    """

    def __init__(self):
        r"""
        :param FileSize: 任务结束后生成的文件大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param FileType: 任务结束后生成的文件格式，例如：mp4,flv等等。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param Bitrate: 任务结束后生成的文件整体码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Duration: 任务结束后生成的文件时长，单位：ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param VideoInfoResult: 任务结束后生成的文件视频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoInfoResult: list of VideoInfoResultItem
        :param AudioInfoResult: 任务结束后生成的文件音频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioInfoResult: list of AudioInfoResultItem
        """
        self.FileSize = None
        self.FileType = None
        self.Bitrate = None
        self.Duration = None
        self.VideoInfoResult = None
        self.AudioInfoResult = None


    def _deserialize(self, params):
        self.FileSize = params.get("FileSize")
        self.FileType = params.get("FileType")
        self.Bitrate = params.get("Bitrate")
        self.Duration = params.get("Duration")
        if params.get("VideoInfoResult") is not None:
            self.VideoInfoResult = []
            for item in params.get("VideoInfoResult"):
                obj = VideoInfoResultItem()
                obj._deserialize(item)
                self.VideoInfoResult.append(obj)
        if params.get("AudioInfoResult") is not None:
            self.AudioInfoResult = []
            for item in params.get("AudioInfoResult"):
                obj = AudioInfoResultItem()
                obj._deserialize(item)
                self.AudioInfoResult.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagItem(AbstractModel):
    """帧标签

    """

    def __init__(self):
        r"""
        :param StartPts: 标签起始时间戳PTS(ms)
        :type StartPts: int
        :param EndPts: 语句结束时间戳PTS(ms)
        :type EndPts: int
        :param Period: 字符串形式的起始结束时间
        :type Period: str
        :param TagItems: 标签数组
        :type TagItems: list of TagItem
        """
        self.StartPts = None
        self.EndPts = None
        self.Period = None
        self.TagItems = None


    def _deserialize(self, params):
        self.StartPts = params.get("StartPts")
        self.EndPts = params.get("EndPts")
        self.Period = params.get("Period")
        if params.get("TagItems") is not None:
            self.TagItems = []
            for item in params.get("TagItems"):
                obj = TagItem()
                obj._deserialize(item)
                self.TagItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagRec(AbstractModel):
    """帧标签任务参数

    """

    def __init__(self):
        r"""
        :param TagType: 标签类型：
"Common": 通用类型
"Game":游戏类型
        :type TagType: str
        :param GameExtendType: 游戏具体类型:
"HonorOfKings_AnchorViews":王者荣耀主播视角
"HonorOfKings_GameViews":王者荣耀比赛视角
"LOL_AnchorViews":英雄联盟主播视角
"LOL_GameViews":英雄联盟比赛视角
"PUBG_AnchorViews":和平精英主播视角
"PUBG_GameViews":和平精英比赛视角
        :type GameExtendType: str
        """
        self.TagType = None
        self.GameExtendType = None


    def _deserialize(self, params):
        self.TagType = params.get("TagType")
        self.GameExtendType = params.get("GameExtendType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagResult(AbstractModel):
    """帧标签结果

    """

    def __init__(self):
        r"""
        :param FrameTagItems: 帧标签结果数组
        :type FrameTagItems: list of FrameTagItem
        """
        self.FrameTagItems = None


    def _deserialize(self, params):
        if params.get("FrameTagItems") is not None:
            self.FrameTagItems = []
            for item in params.get("FrameTagItems"):
                obj = FrameTagItem()
                obj._deserialize(item)
                self.FrameTagItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HiddenMarkInfo(AbstractModel):
    """数字水印

    """

    def __init__(self):
        r"""
        :param Path: 数字水印路径,，如果不从Cos拉取水印，则必填
        :type Path: str
        :param Frequency: 数字水印频率，可选值：[1,256]，默认值为30
        :type Frequency: int
        :param Strength: 数字水印强度，可选值：[32,128]，默认值为64
        :type Strength: int
        :param CosInfo: 数字水印的Cos 信息，从Cos上拉取图片水印时必填。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        self.Path = None
        self.Frequency = None
        self.Strength = None
        self.CosInfo = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Frequency = params.get("Frequency")
        self.Strength = params.get("Strength")
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsEditingInfo(AbstractModel):
    """智能集锦任务参数信息

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启智能集锦。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsTaskResult(AbstractModel):
    """智能集锦结果信息

    """

    def __init__(self):
        r"""
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 智能集锦结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of HighlightsTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = HighlightsTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsTaskResultItem(AbstractModel):
    """智能集锦结果项

    """

    def __init__(self):
        r"""
        :param HighlightUrl: 智能集锦地址。
        :type HighlightUrl: str
        :param CovImgUrl: 智能集锦封面地址。
        :type CovImgUrl: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param Duration: 智能集锦持续时间，单位：秒。
        :type Duration: float
        :param SegmentSet: 智能集锦子片段结果集，集锦片段由这些子片段拼接生成。
        :type SegmentSet: list of HighlightsTaskResultItemSegment
        """
        self.HighlightUrl = None
        self.CovImgUrl = None
        self.Confidence = None
        self.Duration = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.HighlightUrl = params.get("HighlightUrl")
        self.CovImgUrl = params.get("CovImgUrl")
        self.Confidence = params.get("Confidence")
        self.Duration = params.get("Duration")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = HighlightsTaskResultItemSegment()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsTaskResultItemSegment(AbstractModel):
    """智能集锦结果片段

    """

    def __init__(self):
        r"""
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param StartTimeOffset: 集锦片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 集锦片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntervalTime(AbstractModel):
    """周期时间点信息。

    """

    def __init__(self):
        r"""
        :param Interval: 间隔周期，单位ms
        :type Interval: int
        :param StartTime: 开始时间点，单位ms
        :type StartTime: int
        """
        self.Interval = None
        self.StartTime = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        self.StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoudnessInfo(AbstractModel):
    """音频响度信息

    """

    def __init__(self):
        r"""
        :param Loudness: 音频整体响度
        :type Loudness: float
        :param LoudnessRange: 音频响度范围
        :type LoudnessRange: float
        """
        self.Loudness = None
        self.LoudnessRange = None


    def _deserialize(self, params):
        self.Loudness = params.get("Loudness")
        self.LoudnessRange = params.get("LoudnessRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowLightEnhance(AbstractModel):
    """低光照增强参数

    """

    def __init__(self):
        r"""
        :param Type: 低光照增强类型，可选项：normal。
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingInfo(AbstractModel):
    """编辑处理/剪切任务信息。
    截图结果默认存在 SaveInfoSet 的第一个存储位置。

    """

    def __init__(self):
        r"""
        :param TimeInfo: 截取时间信息。
        :type TimeInfo: :class:`tencentcloud.ie.v20200304.models.MediaCuttingTimeInfo`
        :param TargetInfo: 输出结果信息。
        :type TargetInfo: :class:`tencentcloud.ie.v20200304.models.MediaTargetInfo`
        :param OutForm: 截取结果形式信息。
        :type OutForm: :class:`tencentcloud.ie.v20200304.models.MediaCuttingOutForm`
        :param ResultListSaveType: 列表文件形式，存储到用户存储服务中，可选值：
<li>NoListFile：不存储结果列表; </li>
<li>UseSaveInfo：默认，结果列表和结果存储同一位置（即SaveInfoSet 的第一个存储位置）；</li>
<li>SaveInfoSet 存储的Id：存储在指定的存储位置。</li>
        :type ResultListSaveType: str
        :param WatermarkInfoSet: 水印信息，最多支持 10 个水印。
        :type WatermarkInfoSet: list of MediaCuttingWatermark
        :param DropPureColor: 是否去除纯色截图，如果值为 True ，对应时间点的截图如果是纯色，将略过。
        :type DropPureColor: str
        """
        self.TimeInfo = None
        self.TargetInfo = None
        self.OutForm = None
        self.ResultListSaveType = None
        self.WatermarkInfoSet = None
        self.DropPureColor = None


    def _deserialize(self, params):
        if params.get("TimeInfo") is not None:
            self.TimeInfo = MediaCuttingTimeInfo()
            self.TimeInfo._deserialize(params.get("TimeInfo"))
        if params.get("TargetInfo") is not None:
            self.TargetInfo = MediaTargetInfo()
            self.TargetInfo._deserialize(params.get("TargetInfo"))
        if params.get("OutForm") is not None:
            self.OutForm = MediaCuttingOutForm()
            self.OutForm._deserialize(params.get("OutForm"))
        self.ResultListSaveType = params.get("ResultListSaveType")
        if params.get("WatermarkInfoSet") is not None:
            self.WatermarkInfoSet = []
            for item in params.get("WatermarkInfoSet"):
                obj = MediaCuttingWatermark()
                obj._deserialize(item)
                self.WatermarkInfoSet.append(obj)
        self.DropPureColor = params.get("DropPureColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingOutForm(AbstractModel):
    """编辑处理/剪切任务/输出形式信息

    """

    def __init__(self):
        r"""
        :param Type: 输出类型，可选值：
Static：静态图；
Dynamic：动态图；
Sprite：雪碧图；
Video：视频。

注1：不同类型时，对应的 TargetInfo.Format 格式支持如下：
Static：jpg、png；
Dynamic：gif；
Sprite：jpg、png；
Video：mp4。

注2：当 Type=Sprite时，TargetInfo指定的尺寸表示小图的大小，最终结果尺寸以输出为准。
        :type Type: str
        :param FillType: 背景填充方式，可选值：
White：白色填充；
Black：黑色填充；
Stretch：拉伸；
Gaussian：高斯模糊；
默认White。
        :type FillType: str
        :param SpriteRowCount: 【废弃】参考SpriteInfo
        :type SpriteRowCount: int
        :param SpriteColumnCount: 【废弃】参考SpriteInfo
        :type SpriteColumnCount: int
        :param SpriteInfo: Type=Sprite时有效，表示雪碧图参数信息。
        :type SpriteInfo: :class:`tencentcloud.ie.v20200304.models.SpriteImageInfo`
        :param DynamicInfo: Type=Dynamic时有效，表示动图参数信息。
        :type DynamicInfo: :class:`tencentcloud.ie.v20200304.models.DynamicImageInfo`
        """
        self.Type = None
        self.FillType = None
        self.SpriteRowCount = None
        self.SpriteColumnCount = None
        self.SpriteInfo = None
        self.DynamicInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.FillType = params.get("FillType")
        self.SpriteRowCount = params.get("SpriteRowCount")
        self.SpriteColumnCount = params.get("SpriteColumnCount")
        if params.get("SpriteInfo") is not None:
            self.SpriteInfo = SpriteImageInfo()
            self.SpriteInfo._deserialize(params.get("SpriteInfo"))
        if params.get("DynamicInfo") is not None:
            self.DynamicInfo = DynamicImageInfo()
            self.DynamicInfo._deserialize(params.get("DynamicInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingTaskResult(AbstractModel):
    """编辑处理/剪切任务/处理结果

    """

    def __init__(self):
        r"""
        :param ListFile: 如果ResultListType不为NoListFile时，结果（TaskResultFile）列表文件的存储位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ListFile: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        :param ResultCount: 结果个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCount: int
        :param FirstFile: 第一个结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstFile: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        :param LastFile: 最后一个结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastFile: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        :param ImageCount: 任务结果包含的图片总数。
静态图：总数即为文件数；
雪碧图：所有小图总数；
动图、视频：不计算图片数，为 0。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCount: int
        """
        self.ListFile = None
        self.ResultCount = None
        self.FirstFile = None
        self.LastFile = None
        self.ImageCount = None


    def _deserialize(self, params):
        if params.get("ListFile") is not None:
            self.ListFile = TaskResultFile()
            self.ListFile._deserialize(params.get("ListFile"))
        self.ResultCount = params.get("ResultCount")
        if params.get("FirstFile") is not None:
            self.FirstFile = TaskResultFile()
            self.FirstFile._deserialize(params.get("FirstFile"))
        if params.get("LastFile") is not None:
            self.LastFile = TaskResultFile()
            self.LastFile._deserialize(params.get("LastFile"))
        self.ImageCount = params.get("ImageCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingTimeInfo(AbstractModel):
    """编辑处理/剪切任务/时间信息

    """

    def __init__(self):
        r"""
        :param Type: 时间类型，可选值：
PointSet：时间点集合；
IntervalPoint：周期采样点；
SectionSet：时间片段集合。
        :type Type: str
        :param PointSet: 截取时间点集合，单位毫秒，Type=PointSet时必选。
        :type PointSet: list of int
        :param IntervalPoint: 周期采样点信息，Type=IntervalPoint时必选。
        :type IntervalPoint: :class:`tencentcloud.ie.v20200304.models.IntervalTime`
        :param SectionSet: 时间区间集合信息，Type=SectionSet时必选。
        :type SectionSet: list of SectionTime
        """
        self.Type = None
        self.PointSet = None
        self.IntervalPoint = None
        self.SectionSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PointSet = params.get("PointSet")
        if params.get("IntervalPoint") is not None:
            self.IntervalPoint = IntervalTime()
            self.IntervalPoint._deserialize(params.get("IntervalPoint"))
        if params.get("SectionSet") is not None:
            self.SectionSet = []
            for item in params.get("SectionSet"):
                obj = SectionTime()
                obj._deserialize(item)
                self.SectionSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingWatermark(AbstractModel):
    """媒体剪切水印信息。

    """

    def __init__(self):
        r"""
        :param Type: 水印类型，可选值：
<li>Image：图像水印；</li>
<li>Text：文字水印。</li>
        :type Type: str
        :param Image: 图像水印信息，当 Type=Image 时必选。
        :type Image: :class:`tencentcloud.ie.v20200304.models.MediaCuttingWatermarkImage`
        :param Text: 文字水印信息，当 Type=Text 时必选。
        :type Text: :class:`tencentcloud.ie.v20200304.models.MediaCuttingWatermarkText`
        """
        self.Type = None
        self.Image = None
        self.Text = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("Image") is not None:
            self.Image = MediaCuttingWatermarkImage()
            self.Image._deserialize(params.get("Image"))
        if params.get("Text") is not None:
            self.Text = MediaCuttingWatermarkText()
            self.Text._deserialize(params.get("Text"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingWatermarkImage(AbstractModel):
    """媒体剪切图像水印参数。

    """

    def __init__(self):
        r"""
        :param SourceId: 水印源的ID，对应SourceInfoSet内的源。
注意1：对应的 MediaSourceInfo.Type需要为Image。
注意2：对于动图，只取第一帧图像作为水印源。
        :type SourceId: str
        :param PosX: 水印水平坐标，单位像素，默认：0。
        :type PosX: int
        :param PosY: 水印垂直坐标，单位像素，默认：0。
        :type PosY: int
        :param Width: 水印宽度，单位像素，默认：0。
        :type Width: int
        :param Height: 水印高度，单位像素，默认：0。
注意：对于宽高符合以下规则：
1、Width>0 且 Height>0，按指定宽高拉伸；
2、Width=0 且 Height>0，以Height为基准等比缩放；
3、Width>0 且 Height=0，以Width为基准等比缩放；
4、Width=0 且 Height=0，采用源的宽高。
        :type Height: int
        :param PosOriginType: 指定坐标原点，可选值：
<li>LeftTop：PosXY 表示水印左上点到图片左上点的相对位置</li>
<li>RightTop：PosXY 表示水印右上点到图片右上点的相对位置</li>
<li>LeftBottom：PosXY 表示水印左下点到图片左下点的相对位置</li>
<li>RightBottom：PosXY 表示水印右下点到图片右下点的相对位置</li>
<li>Center：PosXY 表示水印中心点到图片中心点的相对位置</li>
默认：LeftTop。
        :type PosOriginType: str
        """
        self.SourceId = None
        self.PosX = None
        self.PosY = None
        self.Width = None
        self.Height = None
        self.PosOriginType = None


    def _deserialize(self, params):
        self.SourceId = params.get("SourceId")
        self.PosX = params.get("PosX")
        self.PosY = params.get("PosY")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PosOriginType = params.get("PosOriginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingWatermarkText(AbstractModel):
    """媒体剪切文字水印参数。

    """

    def __init__(self):
        r"""
        :param Text: 水印文字。
        :type Text: str
        :param FontSize: 文字大小
        :type FontSize: int
        :param PosX: 水印水平坐标，单位像素，默认：0。
        :type PosX: int
        :param PosY: 水印垂直坐标，单位像素，默认：0。
        :type PosY: int
        :param FontColor: 文字颜色，格式为：#RRGGBBAA，默认值：#000000。
        :type FontColor: str
        :param FontAlpha: 文字透明度，范围：0~100，默认值：100。
        :type FontAlpha: int
        :param PosOriginType: 指定坐标原点，可选值：
<li>LeftTop：PosXY 表示水印左上点到图片左上点的相对位置</li>
<li>RightTop：PosXY 表示水印右上点到图片右上点的相对位置</li>
<li>LeftBottom：PosXY 表示水印左下点到图片左下点的相对位置</li>
<li>RightBottom：PosXY 表示水印右下点到图片右下点的相对位置</li>
<li>Center：PosXY 表示水印中心点到图片中心点的相对位置</li>
默认：LeftTop。
        :type PosOriginType: str
        :param Font: 字体，可选值：
<li>SimHei</li>
<li>SimKai</li>
<li>Arial</li>
默认 SimHei。
        :type Font: str
        """
        self.Text = None
        self.FontSize = None
        self.PosX = None
        self.PosY = None
        self.FontColor = None
        self.FontAlpha = None
        self.PosOriginType = None
        self.Font = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.FontSize = params.get("FontSize")
        self.PosX = params.get("PosX")
        self.PosY = params.get("PosY")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        self.PosOriginType = params.get("PosOriginType")
        self.Font = params.get("Font")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaJoiningInfo(AbstractModel):
    """编辑处理/拼接任务信息

    """

    def __init__(self):
        r"""
        :param TargetInfo: 输出目标信息，拼接只采用FileName和Format，用于指定目标文件名和格式。
其中Format只支持mp4.
        :type TargetInfo: :class:`tencentcloud.ie.v20200304.models.MediaTargetInfo`
        :param Mode: 拼接模式：
Fast：快速；
Normal：正常；
        :type Mode: str
        """
        self.TargetInfo = None
        self.Mode = None


    def _deserialize(self, params):
        if params.get("TargetInfo") is not None:
            self.TargetInfo = MediaTargetInfo()
            self.TargetInfo._deserialize(params.get("TargetInfo"))
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaJoiningTaskResult(AbstractModel):
    """编辑处理/拼接任务/处理结果

    """

    def __init__(self):
        r"""
        :param File: 拼接结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type File: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        """
        self.File = None


    def _deserialize(self, params):
        if params.get("File") is not None:
            self.File = TaskResultFile()
            self.File._deserialize(params.get("File"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessInfo(AbstractModel):
    """编辑处理/任务信息

    """

    def __init__(self):
        r"""
        :param Type: 编辑处理任务类型，可选值：
MediaEditing：媒体编辑（待上线）；
MediaCutting：媒体剪切；
MediaJoining：媒体拼接。
MediaRecognition: 媒体识别。
        :type Type: str
        :param MediaCuttingInfo: 视频剪切任务参数，Type=MediaCutting时必选。
        :type MediaCuttingInfo: :class:`tencentcloud.ie.v20200304.models.MediaCuttingInfo`
        :param MediaJoiningInfo: 视频拼接任务参数，Type=MediaJoining时必选。
        :type MediaJoiningInfo: :class:`tencentcloud.ie.v20200304.models.MediaJoiningInfo`
        :param MediaRecognitionInfo: 媒体识别任务参数，Type=MediaRecognition时必选
        :type MediaRecognitionInfo: :class:`tencentcloud.ie.v20200304.models.MediaRecognitionInfo`
        """
        self.Type = None
        self.MediaCuttingInfo = None
        self.MediaJoiningInfo = None
        self.MediaRecognitionInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("MediaCuttingInfo") is not None:
            self.MediaCuttingInfo = MediaCuttingInfo()
            self.MediaCuttingInfo._deserialize(params.get("MediaCuttingInfo"))
        if params.get("MediaJoiningInfo") is not None:
            self.MediaJoiningInfo = MediaJoiningInfo()
            self.MediaJoiningInfo._deserialize(params.get("MediaJoiningInfo"))
        if params.get("MediaRecognitionInfo") is not None:
            self.MediaRecognitionInfo = MediaRecognitionInfo()
            self.MediaRecognitionInfo._deserialize(params.get("MediaRecognitionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskResult(AbstractModel):
    """编辑处理/任务处理结果

    """

    def __init__(self):
        r"""
        :param TaskId: 编辑处理任务ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param Type: 编辑处理任务类型，取值：
MediaEditing：视频编辑（待上线）；
MediaCutting：视频剪切；
MediaJoining：视频拼接。
MediaRecognition：媒体识别；
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Progress: 处理进度，范围：[0,100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param Status: 任务状态：
1100：等待中；
1200：执行中；
2000：成功；
5000：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param ErrCode: 任务错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param ErrMsg: 任务错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param MediaCuttingTaskResult: 剪切任务处理结果，当Type=MediaCutting时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaCuttingTaskResult: :class:`tencentcloud.ie.v20200304.models.MediaCuttingTaskResult`
        :param MediaJoiningTaskResult: 拼接任务处理结果，当Type=MediaJoining时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaJoiningTaskResult: :class:`tencentcloud.ie.v20200304.models.MediaJoiningTaskResult`
        :param MediaRecognitionTaskResult: 媒体识别任务处理结果，当Type=MediaRecognition时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaRecognitionTaskResult: :class:`tencentcloud.ie.v20200304.models.MediaRecognitionTaskResult`
        """
        self.TaskId = None
        self.Type = None
        self.Progress = None
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.MediaCuttingTaskResult = None
        self.MediaJoiningTaskResult = None
        self.MediaRecognitionTaskResult = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Type = params.get("Type")
        self.Progress = params.get("Progress")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("MediaCuttingTaskResult") is not None:
            self.MediaCuttingTaskResult = MediaCuttingTaskResult()
            self.MediaCuttingTaskResult._deserialize(params.get("MediaCuttingTaskResult"))
        if params.get("MediaJoiningTaskResult") is not None:
            self.MediaJoiningTaskResult = MediaJoiningTaskResult()
            self.MediaJoiningTaskResult._deserialize(params.get("MediaJoiningTaskResult"))
        if params.get("MediaRecognitionTaskResult") is not None:
            self.MediaRecognitionTaskResult = MediaRecognitionTaskResult()
            self.MediaRecognitionTaskResult._deserialize(params.get("MediaRecognitionTaskResult"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaQualityRestorationTaskResult(AbstractModel):
    """画质重生任务结果

    """

    def __init__(self):
        r"""
        :param TaskId: 画质重生任务ID
        :type TaskId: str
        :param SubTaskResult: 画质重生处理后文件的详细信息。
        :type SubTaskResult: list of SubTaskResultItem
        """
        self.TaskId = None
        self.SubTaskResult = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("SubTaskResult") is not None:
            self.SubTaskResult = []
            for item in params.get("SubTaskResult"):
                obj = SubTaskResultItem()
                obj._deserialize(item)
                self.SubTaskResult.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaRecognitionInfo(AbstractModel):
    """媒体识别任务参数

    """

    def __init__(self):
        r"""
        :param FrameTagRec: 帧标签识别
        :type FrameTagRec: :class:`tencentcloud.ie.v20200304.models.FrameTagRec`
        :param SubtitleRec: 语音字幕识别
        :type SubtitleRec: :class:`tencentcloud.ie.v20200304.models.SubtitleRec`
        """
        self.FrameTagRec = None
        self.SubtitleRec = None


    def _deserialize(self, params):
        if params.get("FrameTagRec") is not None:
            self.FrameTagRec = FrameTagRec()
            self.FrameTagRec._deserialize(params.get("FrameTagRec"))
        if params.get("SubtitleRec") is not None:
            self.SubtitleRec = SubtitleRec()
            self.SubtitleRec._deserialize(params.get("SubtitleRec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaRecognitionTaskResult(AbstractModel):
    """媒体识别任务处理结果

    """

    def __init__(self):
        r"""
        :param FrameTagResults: 帧标签识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagResults: :class:`tencentcloud.ie.v20200304.models.FrameTagResult`
        :param SubtitleResults: 语音字幕识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SubtitleResults: :class:`tencentcloud.ie.v20200304.models.SubtitleResult`
        """
        self.FrameTagResults = None
        self.SubtitleResults = None


    def _deserialize(self, params):
        if params.get("FrameTagResults") is not None:
            self.FrameTagResults = FrameTagResult()
            self.FrameTagResults._deserialize(params.get("FrameTagResults"))
        if params.get("SubtitleResults") is not None:
            self.SubtitleResults = SubtitleResult()
            self.SubtitleResults._deserialize(params.get("SubtitleResults"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaResultInfo(AbstractModel):
    """结果文件媒体信息

    """

    def __init__(self):
        r"""
        :param Duration: 媒体时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param ResultVideoInfoSet: 视频流信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultVideoInfoSet: list of ResultVideoInfo
        :param ResultAudioInfoSet: 音频流信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultAudioInfoSet: list of ResultAudioInfo
        """
        self.Duration = None
        self.ResultVideoInfoSet = None
        self.ResultAudioInfoSet = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        if params.get("ResultVideoInfoSet") is not None:
            self.ResultVideoInfoSet = []
            for item in params.get("ResultVideoInfoSet"):
                obj = ResultVideoInfo()
                obj._deserialize(item)
                self.ResultVideoInfoSet.append(obj)
        if params.get("ResultAudioInfoSet") is not None:
            self.ResultAudioInfoSet = []
            for item in params.get("ResultAudioInfoSet"):
                obj = ResultAudioInfo()
                obj._deserialize(item)
                self.ResultAudioInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSourceInfo(AbstractModel):
    """编辑处理的媒体源

    """

    def __init__(self):
        r"""
        :param DownInfo: 媒体源资源下载信息。
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param Id: 媒体源ID标记，用于多个输入源时，请内媒体源的定位，对于多输入的任务，一般要求必选。
ID只能包含字母、数字、下划线、中划线，长读不能超过128。
        :type Id: str
        :param Type: 媒体源类型，具体类型如下：
Video：视频
Image：图片
Audio：音频
        :type Type: str
        """
        self.DownInfo = None
        self.Id = None
        self.Type = None


    def _deserialize(self, params):
        if params.get("DownInfo") is not None:
            self.DownInfo = DownInfo()
            self.DownInfo._deserialize(params.get("DownInfo"))
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTargetInfo(AbstractModel):
    """目标媒体信息。

    """

    def __init__(self):
        r"""
        :param FileName: 目标文件名，不能带特殊字符（如/等），无需后缀名，最长200字符。

注1：部分子服务支持占位符，形式为： {parameter}
预设parameter有：
index：序号；
        :type FileName: str
        :param Format: 媒体封装格式，最长5字符，具体格式支持根据子任务确定。
        :type Format: str
        :param TargetVideoInfo: 视频流信息。
        :type TargetVideoInfo: :class:`tencentcloud.ie.v20200304.models.TargetVideoInfo`
        :param ResultListSaveType: 【不再使用】
        :type ResultListSaveType: str
        """
        self.FileName = None
        self.Format = None
        self.TargetVideoInfo = None
        self.ResultListSaveType = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Format = params.get("Format")
        if params.get("TargetVideoInfo") is not None:
            self.TargetVideoInfo = TargetVideoInfo()
            self.TargetVideoInfo._deserialize(params.get("TargetVideoInfo"))
        self.ResultListSaveType = params.get("ResultListSaveType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MuxInfo(AbstractModel):
    """流封装信息

    """

    def __init__(self):
        r"""
        :param DeleteStream: 删除流，可选项：video,audio。
        :type DeleteStream: str
        :param FlvFlags: Flv 参数，目前支持add_keyframe_index
        :type FlvFlags: str
        """
        self.DeleteStream = None
        self.FlvFlags = None


    def _deserialize(self, params):
        self.DeleteStream = params.get("DeleteStream")
        self.FlvFlags = params.get("FlvFlags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpeningEndingEditingInfo(AbstractModel):
    """片头片尾识别任务参数信息

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启片头片尾识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpeningEndingTaskResult(AbstractModel):
    """片头片尾识别结果信息

    """

    def __init__(self):
        r"""
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param Item: 片头片尾识别结果项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: :class:`tencentcloud.ie.v20200304.models.OpeningEndingTaskResultItem`
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.Item = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("Item") is not None:
            self.Item = OpeningEndingTaskResultItem()
            self.Item._deserialize(params.get("Item"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpeningEndingTaskResultItem(AbstractModel):
    """片头片尾识别结果项

    """

    def __init__(self):
        r"""
        :param OpeningTimeOffset: 视频片头的结束时间点，单位：秒。
        :type OpeningTimeOffset: float
        :param OpeningConfidence: 片头识别置信度，取值范围是 0 到 100。
        :type OpeningConfidence: float
        :param EndingTimeOffset: 视频片尾的开始时间点，单位：秒。
        :type EndingTimeOffset: float
        :param EndingConfidence: 片尾识别置信度，取值范围是 0 到 100。
        :type EndingConfidence: float
        """
        self.OpeningTimeOffset = None
        self.OpeningConfidence = None
        self.EndingTimeOffset = None
        self.EndingConfidence = None


    def _deserialize(self, params):
        self.OpeningTimeOffset = params.get("OpeningTimeOffset")
        self.OpeningConfidence = params.get("OpeningConfidence")
        self.EndingTimeOffset = params.get("EndingTimeOffset")
        self.EndingConfidence = params.get("EndingConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PicMarkInfoItem(AbstractModel):
    """图片水印信息

    """

    def __init__(self):
        r"""
        :param PosX: 图片水印的X坐标。
        :type PosX: int
        :param PosY: 图片水印的Y坐标 。
        :type PosY: int
        :param Path: 图片水印路径,，如果不从Cos拉取水印，则必填
        :type Path: str
        :param CosInfo: 图片水印的Cos 信息，从Cos上拉取图片水印时必填。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        :param Width: 图片水印宽度，不填为图片原始宽度。
        :type Width: int
        :param Height: 图片水印高度，不填为图片原始高度。
        :type Height: int
        :param StartTime: 添加图片水印的开始时间,单位：ms。
        :type StartTime: int
        :param EndTime: 添加图片水印的结束时间,单位：ms。
        :type EndTime: int
        """
        self.PosX = None
        self.PosY = None
        self.Path = None
        self.CosInfo = None
        self.Width = None
        self.Height = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PosX = params.get("PosX")
        self.PosY = params.get("PosY")
        self.Path = params.get("Path")
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityControlInfo(AbstractModel):
    """媒体质检任务参数信息

    """

    def __init__(self):
        r"""
        :param Interval: 对流进行截图的间隔ms，默认1000ms
        :type Interval: int
        :param VideoShot: 是否保存截图
        :type VideoShot: bool
        :param Jitter: 是否检测抖动重影
        :type Jitter: bool
        :param Blur: 是否检测模糊
        :type Blur: bool
        :param AbnormalLighting: 是否检测低光照、过曝
        :type AbnormalLighting: bool
        :param CrashScreen: 是否检测花屏
        :type CrashScreen: bool
        :param BlackWhiteEdge: 是否检测黑边、白边、黑屏、白屏、绿屏
        :type BlackWhiteEdge: bool
        :param Noise: 是否检测噪点
        :type Noise: bool
        :param Mosaic: 是否检测马赛克
        :type Mosaic: bool
        :param QRCode: 是否检测二维码，包括小程序码、条形码
        :type QRCode: bool
        :param QualityEvaluation: 是否开启画面质量评价
        :type QualityEvaluation: bool
        :param QualityEvalScore: 画面质量评价过滤阈值，结果只返回低于阈值的时间段，默认60
        :type QualityEvalScore: int
        :param Voice: 是否检测视频音频，包含静音、低音、爆音
        :type Voice: bool
        """
        self.Interval = None
        self.VideoShot = None
        self.Jitter = None
        self.Blur = None
        self.AbnormalLighting = None
        self.CrashScreen = None
        self.BlackWhiteEdge = None
        self.Noise = None
        self.Mosaic = None
        self.QRCode = None
        self.QualityEvaluation = None
        self.QualityEvalScore = None
        self.Voice = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        self.VideoShot = params.get("VideoShot")
        self.Jitter = params.get("Jitter")
        self.Blur = params.get("Blur")
        self.AbnormalLighting = params.get("AbnormalLighting")
        self.CrashScreen = params.get("CrashScreen")
        self.BlackWhiteEdge = params.get("BlackWhiteEdge")
        self.Noise = params.get("Noise")
        self.Mosaic = params.get("Mosaic")
        self.QRCode = params.get("QRCode")
        self.QualityEvaluation = params.get("QualityEvaluation")
        self.QualityEvalScore = params.get("QualityEvalScore")
        self.Voice = params.get("Voice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityControlInfoTaskResult(AbstractModel):
    """媒体质检结果信息

    """

    def __init__(self):
        r"""
        :param TaskId: 质检任务 ID
        :type TaskId: str
        :param Status: 质检任务状态。
1：执行中；2：成功；3：失败
        :type Status: int
        :param Progress: 表示处理进度百分比
        :type Progress: int
        :param UsedTime: 处理时长(s)
        :type UsedTime: int
        :param Duration: 计费时长(s)
        :type Duration: int
        :param NoAudio: 为true时表示视频无音频轨
注意：此字段可能返回 null，表示取不到有效值。
        :type NoAudio: bool
        :param NoVideo: 为true时表示视频无视频轨
注意：此字段可能返回 null，表示取不到有效值。
        :type NoVideo: bool
        :param QualityEvaluationScore: 视频无参考质量打分，百分制
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityEvaluationScore: int
        :param QualityEvaluationResults: 视频画面无参考评分低于阈值的时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityEvaluationResults: list of QualityControlResultItems
        :param JitterResults: 视频画面抖动时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type JitterResults: list of QualityControlResultItems
        :param BlurResults: 视频画面模糊时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type BlurResults: list of QualityControlResultItems
        :param AbnormalLightingResults: 视频画面低光、过曝时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type AbnormalLightingResults: list of QualityControlResultItems
        :param CrashScreenResults: 视频画面花屏时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type CrashScreenResults: list of QualityControlResultItems
        :param BlackWhiteEdgeResults: 视频画面黑边、白边、黑屏、白屏、纯色屏时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackWhiteEdgeResults: list of QualityControlResultItems
        :param NoiseResults: 视频画面有噪点时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type NoiseResults: list of QualityControlResultItems
        :param MosaicResults: 视频画面有马赛克时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type MosaicResults: list of QualityControlResultItems
        :param QRCodeResults: 视频画面有二维码的时间段，包括小程序码、条形码
注意：此字段可能返回 null，表示取不到有效值。
        :type QRCodeResults: list of QualityControlResultItems
        :param VoiceResults: 视频音频异常时间段，包括静音、低音、爆音
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceResults: list of QualityControlResultItems
        :param ErrCode: 任务错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param ErrMsg: 任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        """
        self.TaskId = None
        self.Status = None
        self.Progress = None
        self.UsedTime = None
        self.Duration = None
        self.NoAudio = None
        self.NoVideo = None
        self.QualityEvaluationScore = None
        self.QualityEvaluationResults = None
        self.JitterResults = None
        self.BlurResults = None
        self.AbnormalLightingResults = None
        self.CrashScreenResults = None
        self.BlackWhiteEdgeResults = None
        self.NoiseResults = None
        self.MosaicResults = None
        self.QRCodeResults = None
        self.VoiceResults = None
        self.ErrCode = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.UsedTime = params.get("UsedTime")
        self.Duration = params.get("Duration")
        self.NoAudio = params.get("NoAudio")
        self.NoVideo = params.get("NoVideo")
        self.QualityEvaluationScore = params.get("QualityEvaluationScore")
        if params.get("QualityEvaluationResults") is not None:
            self.QualityEvaluationResults = []
            for item in params.get("QualityEvaluationResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.QualityEvaluationResults.append(obj)
        if params.get("JitterResults") is not None:
            self.JitterResults = []
            for item in params.get("JitterResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.JitterResults.append(obj)
        if params.get("BlurResults") is not None:
            self.BlurResults = []
            for item in params.get("BlurResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.BlurResults.append(obj)
        if params.get("AbnormalLightingResults") is not None:
            self.AbnormalLightingResults = []
            for item in params.get("AbnormalLightingResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.AbnormalLightingResults.append(obj)
        if params.get("CrashScreenResults") is not None:
            self.CrashScreenResults = []
            for item in params.get("CrashScreenResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.CrashScreenResults.append(obj)
        if params.get("BlackWhiteEdgeResults") is not None:
            self.BlackWhiteEdgeResults = []
            for item in params.get("BlackWhiteEdgeResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.BlackWhiteEdgeResults.append(obj)
        if params.get("NoiseResults") is not None:
            self.NoiseResults = []
            for item in params.get("NoiseResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.NoiseResults.append(obj)
        if params.get("MosaicResults") is not None:
            self.MosaicResults = []
            for item in params.get("MosaicResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.MosaicResults.append(obj)
        if params.get("QRCodeResults") is not None:
            self.QRCodeResults = []
            for item in params.get("QRCodeResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.QRCodeResults.append(obj)
        if params.get("VoiceResults") is not None:
            self.VoiceResults = []
            for item in params.get("VoiceResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self.VoiceResults.append(obj)
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityControlItem(AbstractModel):
    """质检结果项

    """

    def __init__(self):
        r"""
        :param Confidence: 置信度，取值范围是 0 到 100
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: int
        :param StartTimeOffset: 出现的起始时间戳，秒
        :type StartTimeOffset: float
        :param EndTimeOffset: 出现的结束时间戳，秒
        :type EndTimeOffset: float
        :param AreaCoordsSet: 区域坐标(px)，即左上角坐标、右下角坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCoordsSet: list of int non-negative
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.AreaCoordsSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.AreaCoordsSet = params.get("AreaCoordsSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityControlResultItems(AbstractModel):
    """质检结果项数组

    """

    def __init__(self):
        r"""
        :param Id: 异常类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param QualityControlItems: 质检结果项
        :type QualityControlItems: list of QualityControlItem
        """
        self.Id = None
        self.QualityControlItems = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("QualityControlItems") is not None:
            self.QualityControlItems = []
            for item in params.get("QualityControlItems"):
                obj = QualityControlItem()
                obj._deserialize(item)
                self.QualityControlItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveReverb(AbstractModel):
    """音频去除混响

    """

    def __init__(self):
        r"""
        :param Type: 去混响类型，可选项：normal
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultAudioInfo(AbstractModel):
    """结果媒体文件的视频流信息

    """

    def __init__(self):
        r"""
        :param StreamId: 流在媒体文件中的流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamId: int
        :param Duration: 流的时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        """
        self.StreamId = None
        self.Duration = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultVideoInfo(AbstractModel):
    """结果媒体文件的视频流信息

    """

    def __init__(self):
        r"""
        :param StreamId: 流在媒体文件中的流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamId: int
        :param Duration: 流的时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param Width: 画面宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 画面高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Fps: 视频帧率，如果高于原始帧率，部分服务将无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type Fps: int
        """
        self.StreamId = None
        self.Duration = None
        self.Width = None
        self.Height = None
        self.Fps = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.Duration = params.get("Duration")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveInfo(AbstractModel):
    """任务存储信息

    """

    def __init__(self):
        r"""
        :param Type: 存储类型，可选值： 
1：CosInfo。
        :type Type: int
        :param CosInfo: Cos形式存储信息，当Type等于1时必选。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        :param Id: 存储信息ID标记，用于多个输出场景。部分任务支持多输出时，一般要求必选。
ID只能包含字母、数字、下划线、中划线，长读不能超过128。
        :type Id: str
        """
        self.Type = None
        self.CosInfo = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScratchRepair(AbstractModel):
    """去划痕参数

    """

    def __init__(self):
        r"""
        :param Type: 去划痕方式，取值：normal。
        :type Type: str
        :param Ratio: 去划痕强度， 可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type Ratio: float
        """
        self.Type = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SectionTime(AbstractModel):
    """时间区间。

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间点，单位ms
        :type StartTime: int
        :param Duration: 时间区间时长，单位ms
        :type Duration: int
        """
        self.StartTime = None
        self.Duration = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentInfo(AbstractModel):
    """输出文件切片信息

    """

    def __init__(self):
        r"""
        :param FragmentTime: 每个切片平均时长，默认10s。
        :type FragmentTime: int
        :param SegmentType: 切片类型，可选项：hls，不填时默认hls。
        :type SegmentType: str
        :param FragmentName: 切片文件名字。注意：
1.不填切片文件名时，默认按照按照如下格式命名：m3u8文件名{order}。
2.若填了切片文件名字，则会按照如下格式命名：用户指定文件名{order}。
        :type FragmentName: str
        """
        self.FragmentTime = None
        self.SegmentType = None
        self.FragmentName = None


    def _deserialize(self, params):
        self.FragmentTime = params.get("FragmentTime")
        self.SegmentType = params.get("SegmentType")
        self.FragmentName = params.get("FragmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sharp(AbstractModel):
    """细节增强参数

    """

    def __init__(self):
        r"""
        :param Type: 细节增强方式,取值：normal。
        :type Type: str
        :param Ratio: 细节增强强度，可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type Ratio: float
        """
        self.Type = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpriteImageInfo(AbstractModel):
    """雪碧图参数信息
    注意：雪碧图大图整体的宽和高都不能大于 65000 像素。

    """

    def __init__(self):
        r"""
        :param RowCount: 表示雪碧图行数，默认：10。
        :type RowCount: int
        :param ColumnCount: 表示雪碧图列数，默认：10。
        :type ColumnCount: int
        :param MarginTop: 第一行元素与顶部像素距离，默认：0。
        :type MarginTop: int
        :param MarginBottom: 最后一行元素与底部像素距离，默认：0。
        :type MarginBottom: int
        :param MarginLeft: 最左一行元素与左边像素距离，默认：0。
        :type MarginLeft: int
        :param MarginRight: 最右一行元素与右边像素距离，默认：0。
        :type MarginRight: int
        :param PaddingTop: 小图与元素顶部像素距离，默认：0。
        :type PaddingTop: int
        :param PaddingBottom: 小图与元素底部像素距离，默认：0。
        :type PaddingBottom: int
        :param PaddingLeft: 小图与元素左边像素距离，默认：0。
        :type PaddingLeft: int
        :param PaddingRight: 小图与元素右边像素距离，默认：0。
        :type PaddingRight: int
        :param BackgroundColor: 背景颜色，格式：#RRGGBB，默认：#FFFFFF。
        :type BackgroundColor: str
        """
        self.RowCount = None
        self.ColumnCount = None
        self.MarginTop = None
        self.MarginBottom = None
        self.MarginLeft = None
        self.MarginRight = None
        self.PaddingTop = None
        self.PaddingBottom = None
        self.PaddingLeft = None
        self.PaddingRight = None
        self.BackgroundColor = None


    def _deserialize(self, params):
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.MarginTop = params.get("MarginTop")
        self.MarginBottom = params.get("MarginBottom")
        self.MarginLeft = params.get("MarginLeft")
        self.MarginRight = params.get("MarginRight")
        self.PaddingTop = params.get("PaddingTop")
        self.PaddingBottom = params.get("PaddingBottom")
        self.PaddingLeft = params.get("PaddingLeft")
        self.PaddingRight = params.get("PaddingRight")
        self.BackgroundColor = params.get("BackgroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMediaProcessTaskRequest(AbstractModel):
    """StopMediaProcessTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 编辑处理任务ID。
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
        


class StopMediaProcessTaskResponse(AbstractModel):
    """StopMediaProcessTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMediaQualityRestorationTaskRequest(AbstractModel):
    """StopMediaQualityRestorationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 要删除的画质重生任务ID。
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
        


class StopMediaQualityRestorationTaskResponse(AbstractModel):
    """StopMediaQualityRestorationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StripEditingInfo(AbstractModel):
    """智能拆条任务参数信息

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启智能拆条。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StripTaskResult(AbstractModel):
    """智能拆条结果信息

    """

    def __init__(self):
        r"""
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 智能拆条结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of StripTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = StripTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StripTaskResultItem(AbstractModel):
    """智能拆条结果项

    """

    def __init__(self):
        r"""
        :param SegmentUrl: 视频拆条片段地址。
        :type SegmentUrl: str
        :param CovImgUrl: 拆条封面图片地址。
        :type CovImgUrl: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param StartTimeOffset: 拆条片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 拆条片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        """
        self.SegmentUrl = None
        self.CovImgUrl = None
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.SegmentUrl = params.get("SegmentUrl")
        self.CovImgUrl = params.get("CovImgUrl")
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubTaskResultItem(AbstractModel):
    """画质重生子任务结果

    """

    def __init__(self):
        r"""
        :param TaskName: 子任务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param StatusCode: 子任务状态。
0：成功；
1：执行中；
其他值：失败。
        :type StatusCode: int
        :param StatusMsg: 子任务状态描述。
        :type StatusMsg: str
        :param ProgressRate: 子任务进度。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgressRate: int
        :param DownloadUrl: 画质重生处理后文件的下载地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param Md5: 画质重生处理后文件的MD5。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param FileInfo: 画质重生处理后文件的详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfo: :class:`tencentcloud.ie.v20200304.models.FileInfo`
        """
        self.TaskName = None
        self.StatusCode = None
        self.StatusMsg = None
        self.ProgressRate = None
        self.DownloadUrl = None
        self.Md5 = None
        self.FileInfo = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.StatusCode = params.get("StatusCode")
        self.StatusMsg = params.get("StatusMsg")
        self.ProgressRate = params.get("ProgressRate")
        self.DownloadUrl = params.get("DownloadUrl")
        self.Md5 = params.get("Md5")
        if params.get("FileInfo") is not None:
            self.FileInfo = FileInfo()
            self.FileInfo._deserialize(params.get("FileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubTaskTranscodeInfo(AbstractModel):
    """画质重生子任务参数信息

    """

    def __init__(self):
        r"""
        :param TaskName: 子任务名称。
        :type TaskName: str
        :param TargetInfo: 目标文件信息。
        :type TargetInfo: :class:`tencentcloud.ie.v20200304.models.TargetInfo`
        :param EditInfo: 视频剪辑信息。注意：如果填写了EditInfo，则VideoInfo和AudioInfo必填
        :type EditInfo: :class:`tencentcloud.ie.v20200304.models.EditInfo`
        :param VideoInfo: 视频转码信息，不填保持和源文件一致。
        :type VideoInfo: :class:`tencentcloud.ie.v20200304.models.VideoInfo`
        :param AudioInfo: 音频转码信息，不填保持和源文件一致。
        :type AudioInfo: :class:`tencentcloud.ie.v20200304.models.AudioInfo`
        :param MuxInfo: 指定封装信息。
        :type MuxInfo: :class:`tencentcloud.ie.v20200304.models.MuxInfo`
        """
        self.TaskName = None
        self.TargetInfo = None
        self.EditInfo = None
        self.VideoInfo = None
        self.AudioInfo = None
        self.MuxInfo = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        if params.get("TargetInfo") is not None:
            self.TargetInfo = TargetInfo()
            self.TargetInfo._deserialize(params.get("TargetInfo"))
        if params.get("EditInfo") is not None:
            self.EditInfo = EditInfo()
            self.EditInfo._deserialize(params.get("EditInfo"))
        if params.get("VideoInfo") is not None:
            self.VideoInfo = VideoInfo()
            self.VideoInfo._deserialize(params.get("VideoInfo"))
        if params.get("AudioInfo") is not None:
            self.AudioInfo = AudioInfo()
            self.AudioInfo._deserialize(params.get("AudioInfo"))
        if params.get("MuxInfo") is not None:
            self.MuxInfo = MuxInfo()
            self.MuxInfo._deserialize(params.get("MuxInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleItem(AbstractModel):
    """语音字幕识别项

    """

    def __init__(self):
        r"""
        :param Id: 语音识别结果
        :type Id: str
        :param Zh: 中文翻译结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Zh: str
        :param En: 英文翻译结果
注意：此字段可能返回 null，表示取不到有效值。
        :type En: str
        :param StartPts: 语句起始时间戳PTS(ms)
        :type StartPts: int
        :param EndPts: 语句结束时间戳PTS(ms)
        :type EndPts: int
        :param Period: 字符串形式的起始结束时间
        :type Period: str
        :param Confidence: 结果的置信度（百分制）
        :type Confidence: int
        :param EndFlag: 当前语句是否结束
        :type EndFlag: bool
        :param PuncEndTs: 语句分割时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type PuncEndTs: str
        """
        self.Id = None
        self.Zh = None
        self.En = None
        self.StartPts = None
        self.EndPts = None
        self.Period = None
        self.Confidence = None
        self.EndFlag = None
        self.PuncEndTs = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Zh = params.get("Zh")
        self.En = params.get("En")
        self.StartPts = params.get("StartPts")
        self.EndPts = params.get("EndPts")
        self.Period = params.get("Period")
        self.Confidence = params.get("Confidence")
        self.EndFlag = params.get("EndFlag")
        self.PuncEndTs = params.get("PuncEndTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleRec(AbstractModel):
    """语音字幕任务参数

    """

    def __init__(self):
        r"""
        :param AsrDst: 语音识别：
zh：中文
en：英文
        :type AsrDst: str
        :param TransDst: 翻译识别：
zh：中文
en：英文
        :type TransDst: str
        """
        self.AsrDst = None
        self.TransDst = None


    def _deserialize(self, params):
        self.AsrDst = params.get("AsrDst")
        self.TransDst = params.get("TransDst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleResult(AbstractModel):
    """语音字幕识别结果

    """

    def __init__(self):
        r"""
        :param SubtitleItems: 语音字幕数组
        :type SubtitleItems: list of SubtitleItem
        """
        self.SubtitleItems = None


    def _deserialize(self, params):
        if params.get("SubtitleItems") is not None:
            self.SubtitleItems = []
            for item in params.get("SubtitleItems"):
                obj = SubtitleItem()
                obj._deserialize(item)
                self.SubtitleItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagEditingInfo(AbstractModel):
    """视频标签识别任务参数信息

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启视频标签识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagItem(AbstractModel):
    """标签项

    """

    def __init__(self):
        r"""
        :param Id: 标签内容
        :type Id: str
        :param Confidence: 结果的置信度（百分制）
        :type Confidence: int
        :param Categorys: 分级数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Categorys: list of str
        :param Ext: 标签备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: str
        """
        self.Id = None
        self.Confidence = None
        self.Categorys = None
        self.Ext = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Confidence = params.get("Confidence")
        self.Categorys = params.get("Categorys")
        self.Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagTaskResult(AbstractModel):
    """视频标签识别结果信息

    """

    def __init__(self):
        r"""
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 视频标签识别结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of TagTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = TagTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagTaskResultItem(AbstractModel):
    """视频标签识别结果项

    """

    def __init__(self):
        r"""
        :param Tag: 标签名称。
        :type Tag: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetInfo(AbstractModel):
    """输出文件信息

    """

    def __init__(self):
        r"""
        :param FileName: 目标文件名
        :type FileName: str
        :param SegmentInfo: 目标文件切片信息
        :type SegmentInfo: :class:`tencentcloud.ie.v20200304.models.SegmentInfo`
        """
        self.FileName = None
        self.SegmentInfo = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        if params.get("SegmentInfo") is not None:
            self.SegmentInfo = SegmentInfo()
            self.SegmentInfo._deserialize(params.get("SegmentInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetVideoInfo(AbstractModel):
    """目标视频信息。

    """

    def __init__(self):
        r"""
        :param Width: 视频宽度，单位像素，一般要求是偶数，否则会向下对齐。
        :type Width: int
        :param Height: 视频高度，单位像素，一般要求是偶数，否则会向下对齐。
        :type Height: int
        :param FrameRate: 视频帧率，范围在1到120之间
        :type FrameRate: int
        """
        self.Width = None
        self.Height = None
        self.FrameRate = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.FrameRate = params.get("FrameRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResultFile(AbstractModel):
    """任务结果文件信息

    """

    def __init__(self):
        r"""
        :param Url: 文件链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param FileSize: 文件大小，部分任务支持，单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param MediaInfo: 媒体信息，对于媒体文件，部分任务支持返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.ie.v20200304.models.MediaResultInfo`
        :param Md5: 文件对应的md5。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        """
        self.Url = None
        self.FileSize = None
        self.MediaInfo = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileSize = params.get("FileSize")
        if params.get("MediaInfo") is not None:
            self.MediaInfo = MediaResultInfo()
            self.MediaInfo._deserialize(params.get("MediaInfo"))
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextMarkInfoItem(AbstractModel):
    """画质重生子任务文字水印信息

    """

    def __init__(self):
        r"""
        :param Text: 文字内容。
        :type Text: str
        :param PosX: 文字水印X坐标。
        :type PosX: int
        :param PosY: 文字水印Y坐标。
        :type PosY: int
        :param FontSize: 文字大小
        :type FontSize: int
        :param FontFile: 字体，可选项：hei,song，simkai,arial；默认hei(黑体）。
        :type FontFile: str
        :param FontColor: 字体颜色，颜色见附录，不填默认black。
        :type FontColor: str
        :param FontAlpha: 文字透明度，可选值0-1。0：不透明，1：全透明。默认为0
        :type FontAlpha: float
        """
        self.Text = None
        self.PosX = None
        self.PosY = None
        self.FontSize = None
        self.FontFile = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.PosX = params.get("PosX")
        self.PosY = params.get("PosY")
        self.FontSize = params.get("FontSize")
        self.FontFile = params.get("FontFile")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlInfo(AbstractModel):
    """任务视频Url形式下载信息。

    """

    def __init__(self):
        r"""
        :param Url: 视频 URL。
注意：编辑理解仅支持mp4、flv等格式的点播文件，不支持hls；
        :type Url: str
        :param Format: 视频地址格式，可选值： 
0：音视频 ;
1：直播流。 
默认为0。其他非0非1值默认为0。画质重生任务只支持0。
        :type Format: int
        :param Host: 【不再支持】指定请求资源时，HTTP头部host的值。
        :type Host: str
        """
        self.Url = None
        self.Format = None
        self.Host = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Format = params.get("Format")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEnhance(AbstractModel):
    """画质增强参数信息

    """

    def __init__(self):
        r"""
        :param ArtifactReduction: 去编码毛刺、伪影参数。
        :type ArtifactReduction: :class:`tencentcloud.ie.v20200304.models.ArtifactReduction`
        :param Denoising: 去噪声参数。
        :type Denoising: :class:`tencentcloud.ie.v20200304.models.Denoising`
        :param ColorEnhance: 颜色增强参数。
        :type ColorEnhance: :class:`tencentcloud.ie.v20200304.models.ColorEnhance`
        :param Sharp: 细节增强参数。
        :type Sharp: :class:`tencentcloud.ie.v20200304.models.Sharp`
        :param WdSuperResolution: 超分参数，可选项：2，目前仅支持2倍超分。
注意：此参数已经弃用，超分可以使用VideoSuperResolution参数
        :type WdSuperResolution: int
        :param FaceProtect: 人脸保护信息。
        :type FaceProtect: :class:`tencentcloud.ie.v20200304.models.FaceProtect`
        :param WdFps: 插帧，取值范围：[0, 60]，单位：Hz。
注意：当取值为 0，表示帧率和原始视频保持一致。
        :type WdFps: int
        :param ScratchRepair: 去划痕参数
        :type ScratchRepair: :class:`tencentcloud.ie.v20200304.models.ScratchRepair`
        :param LowLightEnhance: 低光照增强参数
        :type LowLightEnhance: :class:`tencentcloud.ie.v20200304.models.LowLightEnhance`
        :param VideoSuperResolution: 视频超分参数
        :type VideoSuperResolution: :class:`tencentcloud.ie.v20200304.models.VideoSuperResolution`
        :param VideoRepair: 视频画质修复参数
        :type VideoRepair: :class:`tencentcloud.ie.v20200304.models.VideoRepair`
        """
        self.ArtifactReduction = None
        self.Denoising = None
        self.ColorEnhance = None
        self.Sharp = None
        self.WdSuperResolution = None
        self.FaceProtect = None
        self.WdFps = None
        self.ScratchRepair = None
        self.LowLightEnhance = None
        self.VideoSuperResolution = None
        self.VideoRepair = None


    def _deserialize(self, params):
        if params.get("ArtifactReduction") is not None:
            self.ArtifactReduction = ArtifactReduction()
            self.ArtifactReduction._deserialize(params.get("ArtifactReduction"))
        if params.get("Denoising") is not None:
            self.Denoising = Denoising()
            self.Denoising._deserialize(params.get("Denoising"))
        if params.get("ColorEnhance") is not None:
            self.ColorEnhance = ColorEnhance()
            self.ColorEnhance._deserialize(params.get("ColorEnhance"))
        if params.get("Sharp") is not None:
            self.Sharp = Sharp()
            self.Sharp._deserialize(params.get("Sharp"))
        self.WdSuperResolution = params.get("WdSuperResolution")
        if params.get("FaceProtect") is not None:
            self.FaceProtect = FaceProtect()
            self.FaceProtect._deserialize(params.get("FaceProtect"))
        self.WdFps = params.get("WdFps")
        if params.get("ScratchRepair") is not None:
            self.ScratchRepair = ScratchRepair()
            self.ScratchRepair._deserialize(params.get("ScratchRepair"))
        if params.get("LowLightEnhance") is not None:
            self.LowLightEnhance = LowLightEnhance()
            self.LowLightEnhance._deserialize(params.get("LowLightEnhance"))
        if params.get("VideoSuperResolution") is not None:
            self.VideoSuperResolution = VideoSuperResolution()
            self.VideoSuperResolution._deserialize(params.get("VideoSuperResolution"))
        if params.get("VideoRepair") is not None:
            self.VideoRepair = VideoRepair()
            self.VideoRepair._deserialize(params.get("VideoRepair"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfo(AbstractModel):
    """视频转码信息

    """

    def __init__(self):
        r"""
        :param Fps: 视频帧率，取值范围：[0, 60]，单位：Hz。
注意：当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param Width: 宽度，取值范围：0 和 [128, 4096]
注意：
当 Width、Height 均为 0，则分辨率同源；
当 Width 为 0，Height 非 0，则 Width 按比例缩放；
当 Width 非 0，Height 为 0，则 Height 按比例缩放；
当 Width、Height 均非 0，则分辨率按用户指定。
        :type Width: int
        :param Height: 高度，取值范围：0 和 [128, 4096]
注意：
当 Width、Height 均为 0，则分辨率同源；
当 Width 为 0，Height 非 0，则 Width 按比例缩放；
当 Width 非 0，Height 为 0，则 Height 按比例缩放；
当 Width、Height 均非 0，则分辨率按用户指定。
        :type Height: int
        :param LongSide: 长边分辨率，取值范围：0 和 [128, 4096]
注意：
当 LongSide、ShortSide 均为 0，则分辨率按照Width，Height；
当 LongSide 为 0，ShortSide 非 0，则 LongSide 按比例缩放；
当 LongSide非 0，ShortSide为 0，则 ShortSide 按比例缩放；
当 LongSide、ShortSide 均非 0，则分辨率按用户指定。
长短边优先级高于Weight,Height,设置长短边则忽略宽高。
        :type LongSide: int
        :param ShortSide: 短边分辨率，取值范围：0 和 [128, 4096]
注意：
当 LongSide、ShortSide 均为 0，则分辨率按照Width，Height；
当 LongSide 为 0，ShortSide 非 0，则 LongSide 按比例缩放；
当 LongSide非 0，ShortSide为 0，则 ShortSide 按比例缩放；
当 LongSide、ShortSide 均非 0，则分辨率按用户指定。
长短边优先级高于Weight,Height,设置长短边则忽略宽高。
        :type ShortSide: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param Gop: 固定I帧之间，视频帧数量，取值范围： [25, 2500]，如果不填，使用编码默认最优序列。
        :type Gop: int
        :param VideoCodec: 编码器支持选项，可选值：
h264,
h265,
av1。
不填默认h264。
        :type VideoCodec: str
        :param PicMarkInfo: 图片水印。
        :type PicMarkInfo: list of PicMarkInfoItem
        :param DarInfo: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。
        :type DarInfo: :class:`tencentcloud.ie.v20200304.models.DarInfo`
        :param Hdr: 支持hdr,可选项：
hdr10,
hlg。
此时，VideoCodec会强制设置为h265, 编码位深为10
        :type Hdr: str
        :param VideoEnhance: 画质增强参数信息。
        :type VideoEnhance: :class:`tencentcloud.ie.v20200304.models.VideoEnhance`
        :param HiddenMarkInfo: 数字水印参数信息。
        :type HiddenMarkInfo: :class:`tencentcloud.ie.v20200304.models.HiddenMarkInfo`
        :param TextMarkInfo: 文本水印参数信息。
        :type TextMarkInfo: list of TextMarkInfoItem
        """
        self.Fps = None
        self.Width = None
        self.Height = None
        self.LongSide = None
        self.ShortSide = None
        self.Bitrate = None
        self.Gop = None
        self.VideoCodec = None
        self.PicMarkInfo = None
        self.DarInfo = None
        self.Hdr = None
        self.VideoEnhance = None
        self.HiddenMarkInfo = None
        self.TextMarkInfo = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.LongSide = params.get("LongSide")
        self.ShortSide = params.get("ShortSide")
        self.Bitrate = params.get("Bitrate")
        self.Gop = params.get("Gop")
        self.VideoCodec = params.get("VideoCodec")
        if params.get("PicMarkInfo") is not None:
            self.PicMarkInfo = []
            for item in params.get("PicMarkInfo"):
                obj = PicMarkInfoItem()
                obj._deserialize(item)
                self.PicMarkInfo.append(obj)
        if params.get("DarInfo") is not None:
            self.DarInfo = DarInfo()
            self.DarInfo._deserialize(params.get("DarInfo"))
        self.Hdr = params.get("Hdr")
        if params.get("VideoEnhance") is not None:
            self.VideoEnhance = VideoEnhance()
            self.VideoEnhance._deserialize(params.get("VideoEnhance"))
        if params.get("HiddenMarkInfo") is not None:
            self.HiddenMarkInfo = HiddenMarkInfo()
            self.HiddenMarkInfo._deserialize(params.get("HiddenMarkInfo"))
        if params.get("TextMarkInfo") is not None:
            self.TextMarkInfo = []
            for item in params.get("TextMarkInfo"):
                obj = TextMarkInfoItem()
                obj._deserialize(item)
                self.TextMarkInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfoResultItem(AbstractModel):
    """任务结束后生成的文件视频信息

    """

    def __init__(self):
        r"""
        :param Stream: 视频流的流id。
        :type Stream: int
        :param Width: 视频宽度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 视频高度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Bitrate: 视频码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Fps: 视频帧率，用分数格式表示，如：25/1, 99/32等等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Fps: str
        :param Codec: 编码格式，如h264,h265等等 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        :param Rotate: 播放旋转角度，可选值0-360。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: int
        :param Duration: 视频时长，单位：ms 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param PixFormat: 颜色空间，如yuv420p，yuv444p等等。
注意：此字段可能返回 null，表示取不到有效值。
        :type PixFormat: str
        """
        self.Stream = None
        self.Width = None
        self.Height = None
        self.Bitrate = None
        self.Fps = None
        self.Codec = None
        self.Rotate = None
        self.Duration = None
        self.PixFormat = None


    def _deserialize(self, params):
        self.Stream = params.get("Stream")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Bitrate = params.get("Bitrate")
        self.Fps = params.get("Fps")
        self.Codec = params.get("Codec")
        self.Rotate = params.get("Rotate")
        self.Duration = params.get("Duration")
        self.PixFormat = params.get("PixFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoRepair(AbstractModel):
    """综合画质修复，包括：去噪，去毛刺，细节增强，主观画质提升。

    """

    def __init__(self):
        r"""
        :param Type: 画质修复类型，可选值：weak，normal，strong;
默认值: weak
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoSuperResolution(AbstractModel):
    """视频超分

    """

    def __init__(self):
        r"""
        :param Type: 超分视频类型：可选值：lq,hq
lq: 针对低清晰度有较多噪声视频的超分;
hq: 针对高清晰度视频超分;
默认取值：lq。
        :type Type: str
        :param Size: 超分倍数，可选值：2。
注意：当前只支持两倍超分。
        :type Size: int
        """
        self.Type = None
        self.Size = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        