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
        :param _Type: 去毛刺方式：weak,,strong
        :type Type: str
        :param _Algorithm: 去毛刺算法，可选项：
edaf,
wdaf，
默认edaf。
注意：此参数已经弃用
        :type Algorithm: str
        """
        self._Type = None
        self._Algorithm = None

    @property
    def Type(self):
        """去毛刺方式：weak,,strong
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Algorithm(self):
        """去毛刺算法，可选项：
edaf,
wdaf，
默认edaf。
注意：此参数已经弃用
        :rtype: str
        """
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEnhance(AbstractModel):
    """音频音效增强，只支持无背景音的音频

    """

    def __init__(self):
        r"""
        :param _Type: 音效增强种类，可选项：normal
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        """音效增强种类，可选项：normal
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioInfo(AbstractModel):
    """音频参数信息

    """

    def __init__(self):
        r"""
        :param _Bitrate: 音频码率，取值范围：0 和 [26, 256]，单位：kbps。
注意：当取值为 0，表示音频码率和原始音频保持一致。
        :type Bitrate: int
        :param _Codec: 音频编码器，可选项：aac,mp3,ac3,flac,mp2。
        :type Codec: str
        :param _Channel: 声道数，可选项：
1：单声道，
2：双声道，
6：立体声。
        :type Channel: int
        :param _SampleRate: 采样率，单位：Hz。可选项：32000，44100,48000
        :type SampleRate: int
        :param _Denoise: 音频降噪信息
        :type Denoise: :class:`tencentcloud.ie.v20200304.models.Denoise`
        :param _EnableMuteAudio: 开启添加静音，可选项：
0：不开启，
1：开启，
默认不开启
        :type EnableMuteAudio: int
        :param _LoudnessInfo: 音频响度信息
        :type LoudnessInfo: :class:`tencentcloud.ie.v20200304.models.LoudnessInfo`
        :param _AudioEnhance: 音频音效增强
        :type AudioEnhance: :class:`tencentcloud.ie.v20200304.models.AudioEnhance`
        :param _RemoveReverb: 去除混音
        :type RemoveReverb: :class:`tencentcloud.ie.v20200304.models.RemoveReverb`
        """
        self._Bitrate = None
        self._Codec = None
        self._Channel = None
        self._SampleRate = None
        self._Denoise = None
        self._EnableMuteAudio = None
        self._LoudnessInfo = None
        self._AudioEnhance = None
        self._RemoveReverb = None

    @property
    def Bitrate(self):
        """音频码率，取值范围：0 和 [26, 256]，单位：kbps。
注意：当取值为 0，表示音频码率和原始音频保持一致。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Codec(self):
        """音频编码器，可选项：aac,mp3,ac3,flac,mp2。
        :rtype: str
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def Channel(self):
        """声道数，可选项：
1：单声道，
2：双声道，
6：立体声。
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def SampleRate(self):
        """采样率，单位：Hz。可选项：32000，44100,48000
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Denoise(self):
        """音频降噪信息
        :rtype: :class:`tencentcloud.ie.v20200304.models.Denoise`
        """
        return self._Denoise

    @Denoise.setter
    def Denoise(self, Denoise):
        self._Denoise = Denoise

    @property
    def EnableMuteAudio(self):
        """开启添加静音，可选项：
0：不开启，
1：开启，
默认不开启
        :rtype: int
        """
        return self._EnableMuteAudio

    @EnableMuteAudio.setter
    def EnableMuteAudio(self, EnableMuteAudio):
        self._EnableMuteAudio = EnableMuteAudio

    @property
    def LoudnessInfo(self):
        """音频响度信息
        :rtype: :class:`tencentcloud.ie.v20200304.models.LoudnessInfo`
        """
        return self._LoudnessInfo

    @LoudnessInfo.setter
    def LoudnessInfo(self, LoudnessInfo):
        self._LoudnessInfo = LoudnessInfo

    @property
    def AudioEnhance(self):
        """音频音效增强
        :rtype: :class:`tencentcloud.ie.v20200304.models.AudioEnhance`
        """
        return self._AudioEnhance

    @AudioEnhance.setter
    def AudioEnhance(self, AudioEnhance):
        self._AudioEnhance = AudioEnhance

    @property
    def RemoveReverb(self):
        """去除混音
        :rtype: :class:`tencentcloud.ie.v20200304.models.RemoveReverb`
        """
        return self._RemoveReverb

    @RemoveReverb.setter
    def RemoveReverb(self, RemoveReverb):
        self._RemoveReverb = RemoveReverb


    def _deserialize(self, params):
        self._Bitrate = params.get("Bitrate")
        self._Codec = params.get("Codec")
        self._Channel = params.get("Channel")
        self._SampleRate = params.get("SampleRate")
        if params.get("Denoise") is not None:
            self._Denoise = Denoise()
            self._Denoise._deserialize(params.get("Denoise"))
        self._EnableMuteAudio = params.get("EnableMuteAudio")
        if params.get("LoudnessInfo") is not None:
            self._LoudnessInfo = LoudnessInfo()
            self._LoudnessInfo._deserialize(params.get("LoudnessInfo"))
        if params.get("AudioEnhance") is not None:
            self._AudioEnhance = AudioEnhance()
            self._AudioEnhance._deserialize(params.get("AudioEnhance"))
        if params.get("RemoveReverb") is not None:
            self._RemoveReverb = RemoveReverb()
            self._RemoveReverb._deserialize(params.get("RemoveReverb"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioInfoResultItem(AbstractModel):
    """任务结束后生成的文件音频信息

    """

    def __init__(self):
        r"""
        :param _Stream: 音频流的流id。
        :type Stream: int
        :param _Sample: 音频采样率 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Sample: int
        :param _Channel: 音频声道数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: int
        :param _Codec: 编码格式，如aac, mp3等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        :param _Bitrate: 码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param _Duration: 音频时长，单位：ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        """
        self._Stream = None
        self._Sample = None
        self._Channel = None
        self._Codec = None
        self._Bitrate = None
        self._Duration = None

    @property
    def Stream(self):
        """音频流的流id。
        :rtype: int
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def Sample(self):
        """音频采样率 。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Sample

    @Sample.setter
    def Sample(self, Sample):
        self._Sample = Sample

    @property
    def Channel(self):
        """音频声道数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Codec(self):
        """编码格式，如aac, mp3等。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def Bitrate(self):
        """码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Duration(self):
        """音频时长，单位：ms。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Stream = params.get("Stream")
        self._Sample = params.get("Sample")
        self._Channel = params.get("Channel")
        self._Codec = params.get("Codec")
        self._Bitrate = params.get("Bitrate")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackInfo(AbstractModel):
    """任务结果回调地址信息

    """

    def __init__(self):
        r"""
        :param _Url: 回调URL。
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        """回调URL。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationEditingInfo(AbstractModel):
    """视频分类识别任务参数信息

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启视频分类识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param _CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self._Switch = None
        self._CustomInfo = None

    @property
    def Switch(self):
        """是否开启视频分类识别。0为关闭，1为开启。其他非0非1值默认为0。
        :rtype: int
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CustomInfo(self):
        """额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :rtype: str
        """
        return self._CustomInfo

    @CustomInfo.setter
    def CustomInfo(self, CustomInfo):
        self._CustomInfo = CustomInfo


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationTaskResult(AbstractModel):
    """视频分类识别结果信息

    """

    def __init__(self):
        r"""
        :param _Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param _ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param _ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param _ItemSet: 视频分类识别结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of ClassificationTaskResultItem
        """
        self._Status = None
        self._ErrCode = None
        self._ErrMsg = None
        self._ItemSet = None

    @property
    def Status(self):
        """编辑任务状态。 
1：执行中；2：成功；3：失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """编辑任务失败错误码。 
0：成功；其他值：失败。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """编辑任务失败错误描述。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ItemSet(self):
        """视频分类识别结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClassificationTaskResultItem
        """
        return self._ItemSet

    @ItemSet.setter
    def ItemSet(self, ItemSet):
        self._ItemSet = ItemSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self._ItemSet = []
            for item in params.get("ItemSet"):
                obj = ClassificationTaskResultItem()
                obj._deserialize(item)
                self._ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationTaskResultItem(AbstractModel):
    """视频分类识别结果项

    """

    def __init__(self):
        r"""
        :param _Classification: 分类名称。
        :type Classification: str
        :param _Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self._Classification = None
        self._Confidence = None

    @property
    def Classification(self):
        """分类名称。
        :rtype: str
        """
        return self._Classification

    @Classification.setter
    def Classification(self, Classification):
        self._Classification = Classification

    @property
    def Confidence(self):
        """置信度，取值范围是 0 到 100。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence


    def _deserialize(self, params):
        self._Classification = params.get("Classification")
        self._Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ColorEnhance(AbstractModel):
    """颜色增强参数

    """

    def __init__(self):
        r"""
        :param _Type: 颜色增强类型，可选项：
1.  tra；
2.  weak；
3.  normal;
4.  strong;
注意：tra不支持自适应调整，处理速度更快；weak,normal,strong支持基于画面颜色自适应，处理速度更慢。
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        """颜色增强类型，可选项：
1.  tra；
2.  weak；
3.  normal;
4.  strong;
注意：tra不支持自适应调整，处理速度更快；weak,normal,strong支持基于画面颜色自适应，处理速度更慢。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosAuthMode(AbstractModel):
    """任务视频cos授权信息

    """

    def __init__(self):
        r"""
        :param _Type: 授权类型，可选值： 
0：bucket授权，需要将对应bucket授权给本服务帐号（3020447271和100012301793），否则会读写cos失败； 
1：key托管，把cos的账号id和key托管于本服务，本服务会提供一个托管id； 
3：临时key授权。
注意：目前智能编辑还不支持临时key授权；画质重生目前只支持bucket授权
        :type Type: int
        :param _HostedId: cos账号托管id，Type等于1时必选。
        :type HostedId: str
        :param _SecretId: cos身份识别id，Type等于3时必选。
        :type SecretId: str
        :param _SecretKey: cos身份秘钥，Type等于3时必选。
        :type SecretKey: str
        :param _Token: 临时授权 token，Type等于3时必选。
        :type Token: str
        """
        self._Type = None
        self._HostedId = None
        self._SecretId = None
        self._SecretKey = None
        self._Token = None

    @property
    def Type(self):
        """授权类型，可选值： 
0：bucket授权，需要将对应bucket授权给本服务帐号（3020447271和100012301793），否则会读写cos失败； 
1：key托管，把cos的账号id和key托管于本服务，本服务会提供一个托管id； 
3：临时key授权。
注意：目前智能编辑还不支持临时key授权；画质重生目前只支持bucket授权
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HostedId(self):
        """cos账号托管id，Type等于1时必选。
        :rtype: str
        """
        return self._HostedId

    @HostedId.setter
    def HostedId(self, HostedId):
        self._HostedId = HostedId

    @property
    def SecretId(self):
        """cos身份识别id，Type等于3时必选。
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        """cos身份秘钥，Type等于3时必选。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Token(self):
        """临时授权 token，Type等于3时必选。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._HostedId = params.get("HostedId")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosInfo(AbstractModel):
    """任务视频cos信息

    """

    def __init__(self):
        r"""
        :param _Region: cos 区域值。例如：ap-beijing。
        :type Region: str
        :param _Bucket: cos 存储桶，格式为BuketName-AppId。例如：test-123456。
        :type Bucket: str
        :param _Path: cos 路径。 
对于写表示目录，例如：/test； 
对于读表示文件路径，例如：/test/test.mp4。
        :type Path: str
        :param _CosAuthMode: cos 授权信息，不填默认为公有权限。
        :type CosAuthMode: :class:`tencentcloud.ie.v20200304.models.CosAuthMode`
        """
        self._Region = None
        self._Bucket = None
        self._Path = None
        self._CosAuthMode = None

    @property
    def Region(self):
        """cos 区域值。例如：ap-beijing。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        """cos 存储桶，格式为BuketName-AppId。例如：test-123456。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Path(self):
        """cos 路径。 
对于写表示目录，例如：/test； 
对于读表示文件路径，例如：/test/test.mp4。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def CosAuthMode(self):
        """cos 授权信息，不填默认为公有权限。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CosAuthMode`
        """
        return self._CosAuthMode

    @CosAuthMode.setter
    def CosAuthMode(self, CosAuthMode):
        self._CosAuthMode = CosAuthMode


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._Path = params.get("Path")
        if params.get("CosAuthMode") is not None:
            self._CosAuthMode = CosAuthMode()
            self._CosAuthMode._deserialize(params.get("CosAuthMode"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverEditingInfo(AbstractModel):
    """智能封面任务参数信息

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启智能封面。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param _CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self._Switch = None
        self._CustomInfo = None

    @property
    def Switch(self):
        """是否开启智能封面。0为关闭，1为开启。其他非0非1值默认为0。
        :rtype: int
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CustomInfo(self):
        """额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :rtype: str
        """
        return self._CustomInfo

    @CustomInfo.setter
    def CustomInfo(self, CustomInfo):
        self._CustomInfo = CustomInfo


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverTaskResult(AbstractModel):
    """智能封面结果信息

    """

    def __init__(self):
        r"""
        :param _Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param _ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param _ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param _ItemSet: 智能封面结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of CoverTaskResultItem
        """
        self._Status = None
        self._ErrCode = None
        self._ErrMsg = None
        self._ItemSet = None

    @property
    def Status(self):
        """编辑任务状态。 
1：执行中；2：成功；3：失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """编辑任务失败错误码。 
0：成功；其他值：失败。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """编辑任务失败错误描述。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ItemSet(self):
        """智能封面结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CoverTaskResultItem
        """
        return self._ItemSet

    @ItemSet.setter
    def ItemSet(self, ItemSet):
        self._ItemSet = ItemSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self._ItemSet = []
            for item in params.get("ItemSet"):
                obj = CoverTaskResultItem()
                obj._deserialize(item)
                self._ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverTaskResultItem(AbstractModel):
    """智能封面结果项

    """

    def __init__(self):
        r"""
        :param _CoverUrl: 智能封面地址。
        :type CoverUrl: str
        :param _Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self._CoverUrl = None
        self._Confidence = None

    @property
    def CoverUrl(self):
        """智能封面地址。
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def Confidence(self):
        """置信度，取值范围是 0 到 100。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence


    def _deserialize(self, params):
        self._CoverUrl = params.get("CoverUrl")
        self._Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEditingTaskRequest(AbstractModel):
    """CreateEditingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EditingInfo: 智能编辑任务参数。
        :type EditingInfo: :class:`tencentcloud.ie.v20200304.models.EditingInfo`
        :param _DownInfo: 视频源信息。
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param _SaveInfo: 结果存储信息。对于包含智能拆条、智能集锦或者智能封面的任务必选。
        :type SaveInfo: :class:`tencentcloud.ie.v20200304.models.SaveInfo`
        :param _CallbackInfo: 任务结果回调地址信息。
        :type CallbackInfo: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        self._EditingInfo = None
        self._DownInfo = None
        self._SaveInfo = None
        self._CallbackInfo = None

    @property
    def EditingInfo(self):
        """智能编辑任务参数。
        :rtype: :class:`tencentcloud.ie.v20200304.models.EditingInfo`
        """
        return self._EditingInfo

    @EditingInfo.setter
    def EditingInfo(self, EditingInfo):
        self._EditingInfo = EditingInfo

    @property
    def DownInfo(self):
        """视频源信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        """
        return self._DownInfo

    @DownInfo.setter
    def DownInfo(self, DownInfo):
        self._DownInfo = DownInfo

    @property
    def SaveInfo(self):
        """结果存储信息。对于包含智能拆条、智能集锦或者智能封面的任务必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.SaveInfo`
        """
        return self._SaveInfo

    @SaveInfo.setter
    def SaveInfo(self, SaveInfo):
        self._SaveInfo = SaveInfo

    @property
    def CallbackInfo(self):
        """任务结果回调地址信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        return self._CallbackInfo

    @CallbackInfo.setter
    def CallbackInfo(self, CallbackInfo):
        self._CallbackInfo = CallbackInfo


    def _deserialize(self, params):
        if params.get("EditingInfo") is not None:
            self._EditingInfo = EditingInfo()
            self._EditingInfo._deserialize(params.get("EditingInfo"))
        if params.get("DownInfo") is not None:
            self._DownInfo = DownInfo()
            self._DownInfo._deserialize(params.get("DownInfo"))
        if params.get("SaveInfo") is not None:
            self._SaveInfo = SaveInfo()
            self._SaveInfo._deserialize(params.get("SaveInfo"))
        if params.get("CallbackInfo") is not None:
            self._CallbackInfo = CallbackInfo()
            self._CallbackInfo._deserialize(params.get("CallbackInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEditingTaskResponse(AbstractModel):
    """CreateEditingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 编辑任务 ID，可以通过该 ID 查询任务状态。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """编辑任务 ID，可以通过该 ID 查询任务状态。
        :rtype: str
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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateMediaProcessTaskRequest(AbstractModel):
    """CreateMediaProcessTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MediaProcessInfo: 编辑处理任务参数。
        :type MediaProcessInfo: :class:`tencentcloud.ie.v20200304.models.MediaProcessInfo`
        :param _SourceInfoSet: 编辑处理任务输入源列表。
        :type SourceInfoSet: list of MediaSourceInfo
        :param _SaveInfoSet: 结果存储信息，对于涉及存储的请求必选。部子任务支持数组备份写，具体以对应任务文档为准。
        :type SaveInfoSet: list of SaveInfo
        :param _CallbackInfoSet: 任务结果回调地址信息。部子任务支持数组备份回调，具体以对应任务文档为准。
        :type CallbackInfoSet: list of CallbackInfo
        """
        self._MediaProcessInfo = None
        self._SourceInfoSet = None
        self._SaveInfoSet = None
        self._CallbackInfoSet = None

    @property
    def MediaProcessInfo(self):
        """编辑处理任务参数。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaProcessInfo`
        """
        return self._MediaProcessInfo

    @MediaProcessInfo.setter
    def MediaProcessInfo(self, MediaProcessInfo):
        self._MediaProcessInfo = MediaProcessInfo

    @property
    def SourceInfoSet(self):
        """编辑处理任务输入源列表。
        :rtype: list of MediaSourceInfo
        """
        return self._SourceInfoSet

    @SourceInfoSet.setter
    def SourceInfoSet(self, SourceInfoSet):
        self._SourceInfoSet = SourceInfoSet

    @property
    def SaveInfoSet(self):
        """结果存储信息，对于涉及存储的请求必选。部子任务支持数组备份写，具体以对应任务文档为准。
        :rtype: list of SaveInfo
        """
        return self._SaveInfoSet

    @SaveInfoSet.setter
    def SaveInfoSet(self, SaveInfoSet):
        self._SaveInfoSet = SaveInfoSet

    @property
    def CallbackInfoSet(self):
        """任务结果回调地址信息。部子任务支持数组备份回调，具体以对应任务文档为准。
        :rtype: list of CallbackInfo
        """
        return self._CallbackInfoSet

    @CallbackInfoSet.setter
    def CallbackInfoSet(self, CallbackInfoSet):
        self._CallbackInfoSet = CallbackInfoSet


    def _deserialize(self, params):
        if params.get("MediaProcessInfo") is not None:
            self._MediaProcessInfo = MediaProcessInfo()
            self._MediaProcessInfo._deserialize(params.get("MediaProcessInfo"))
        if params.get("SourceInfoSet") is not None:
            self._SourceInfoSet = []
            for item in params.get("SourceInfoSet"):
                obj = MediaSourceInfo()
                obj._deserialize(item)
                self._SourceInfoSet.append(obj)
        if params.get("SaveInfoSet") is not None:
            self._SaveInfoSet = []
            for item in params.get("SaveInfoSet"):
                obj = SaveInfo()
                obj._deserialize(item)
                self._SaveInfoSet.append(obj)
        if params.get("CallbackInfoSet") is not None:
            self._CallbackInfoSet = []
            for item in params.get("CallbackInfoSet"):
                obj = CallbackInfo()
                obj._deserialize(item)
                self._CallbackInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaProcessTaskResponse(AbstractModel):
    """CreateMediaProcessTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 编辑任务 ID，可以通过该 ID 查询任务状态和结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """编辑任务 ID，可以通过该 ID 查询任务状态和结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateMediaQualityRestorationTaskRequest(AbstractModel):
    """CreateMediaQualityRestorationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DownInfo: 源文件地址。
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param _TransInfo: 画质重生任务参数信息。
        :type TransInfo: list of SubTaskTranscodeInfo
        :param _SaveInfo: 任务结束后文件存储信息。
        :type SaveInfo: :class:`tencentcloud.ie.v20200304.models.SaveInfo`
        :param _CallbackInfo: 任务结果回调地址信息。
        :type CallbackInfo: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        :param _TopSpeedCodecChannel: 极速高清体验馆渠道标志。
        :type TopSpeedCodecChannel: int
        """
        self._DownInfo = None
        self._TransInfo = None
        self._SaveInfo = None
        self._CallbackInfo = None
        self._TopSpeedCodecChannel = None

    @property
    def DownInfo(self):
        """源文件地址。
        :rtype: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        """
        return self._DownInfo

    @DownInfo.setter
    def DownInfo(self, DownInfo):
        self._DownInfo = DownInfo

    @property
    def TransInfo(self):
        """画质重生任务参数信息。
        :rtype: list of SubTaskTranscodeInfo
        """
        return self._TransInfo

    @TransInfo.setter
    def TransInfo(self, TransInfo):
        self._TransInfo = TransInfo

    @property
    def SaveInfo(self):
        """任务结束后文件存储信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.SaveInfo`
        """
        return self._SaveInfo

    @SaveInfo.setter
    def SaveInfo(self, SaveInfo):
        self._SaveInfo = SaveInfo

    @property
    def CallbackInfo(self):
        """任务结果回调地址信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        return self._CallbackInfo

    @CallbackInfo.setter
    def CallbackInfo(self, CallbackInfo):
        self._CallbackInfo = CallbackInfo

    @property
    def TopSpeedCodecChannel(self):
        """极速高清体验馆渠道标志。
        :rtype: int
        """
        return self._TopSpeedCodecChannel

    @TopSpeedCodecChannel.setter
    def TopSpeedCodecChannel(self, TopSpeedCodecChannel):
        self._TopSpeedCodecChannel = TopSpeedCodecChannel


    def _deserialize(self, params):
        if params.get("DownInfo") is not None:
            self._DownInfo = DownInfo()
            self._DownInfo._deserialize(params.get("DownInfo"))
        if params.get("TransInfo") is not None:
            self._TransInfo = []
            for item in params.get("TransInfo"):
                obj = SubTaskTranscodeInfo()
                obj._deserialize(item)
                self._TransInfo.append(obj)
        if params.get("SaveInfo") is not None:
            self._SaveInfo = SaveInfo()
            self._SaveInfo._deserialize(params.get("SaveInfo"))
        if params.get("CallbackInfo") is not None:
            self._CallbackInfo = CallbackInfo()
            self._CallbackInfo._deserialize(params.get("CallbackInfo"))
        self._TopSpeedCodecChannel = params.get("TopSpeedCodecChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaQualityRestorationTaskResponse(AbstractModel):
    """CreateMediaQualityRestorationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 画质重生任务ID，可以通过该ID查询任务状态。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """画质重生任务ID，可以通过该ID查询任务状态。
        :rtype: str
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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateQualityControlTaskRequest(AbstractModel):
    """CreateQualityControlTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QualityControlInfo: 质检任务参数
        :type QualityControlInfo: :class:`tencentcloud.ie.v20200304.models.QualityControlInfo`
        :param _DownInfo: 视频源信息
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param _CallbackInfo: 任务结果回调地址信息
        :type CallbackInfo: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        self._QualityControlInfo = None
        self._DownInfo = None
        self._CallbackInfo = None

    @property
    def QualityControlInfo(self):
        """质检任务参数
        :rtype: :class:`tencentcloud.ie.v20200304.models.QualityControlInfo`
        """
        return self._QualityControlInfo

    @QualityControlInfo.setter
    def QualityControlInfo(self, QualityControlInfo):
        self._QualityControlInfo = QualityControlInfo

    @property
    def DownInfo(self):
        """视频源信息
        :rtype: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        """
        return self._DownInfo

    @DownInfo.setter
    def DownInfo(self, DownInfo):
        self._DownInfo = DownInfo

    @property
    def CallbackInfo(self):
        """任务结果回调地址信息
        :rtype: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        return self._CallbackInfo

    @CallbackInfo.setter
    def CallbackInfo(self, CallbackInfo):
        self._CallbackInfo = CallbackInfo


    def _deserialize(self, params):
        if params.get("QualityControlInfo") is not None:
            self._QualityControlInfo = QualityControlInfo()
            self._QualityControlInfo._deserialize(params.get("QualityControlInfo"))
        if params.get("DownInfo") is not None:
            self._DownInfo = DownInfo()
            self._DownInfo._deserialize(params.get("DownInfo"))
        if params.get("CallbackInfo") is not None:
            self._CallbackInfo = CallbackInfo()
            self._CallbackInfo._deserialize(params.get("CallbackInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQualityControlTaskResponse(AbstractModel):
    """CreateQualityControlTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 质检任务 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """质检任务 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DarInfo(AbstractModel):
    """视频Dar信息

    """

    def __init__(self):
        r"""
        :param _FillMode: 填充模式，可选值：
1：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。
2：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“。
默认为2。
        :type FillMode: int
        """
        self._FillMode = None

    @property
    def FillMode(self):
        """填充模式，可选值：
1：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。
2：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“。
默认为2。
        :rtype: int
        """
        return self._FillMode

    @FillMode.setter
    def FillMode(self, FillMode):
        self._FillMode = FillMode


    def _deserialize(self, params):
        self._FillMode = params.get("FillMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Denoise(AbstractModel):
    """音频降噪

    """

    def __init__(self):
        r"""
        :param _Type: 音频降噪强度，可选项：
1. weak
2.normal，
3.strong
默认为weak
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        """音频降噪强度，可选项：
1. weak
2.normal，
3.strong
默认为weak
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Denoising(AbstractModel):
    """去噪参数

    """

    def __init__(self):
        r"""
        :param _Type: 去噪方式，可选项：
templ：时域降噪；
spatial：空域降噪,
fast-spatial：快速空域降噪。
注意：可选择组合方式：
1.type:"templ,spatial" ;
2.type:"templ,fast-spatial"。
        :type Type: str
        :param _TemplStrength: 时域去噪强度，可选值：0.0-1.0 。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type TemplStrength: float
        :param _SpatialStrength: 空域去噪强度，可选值：0.0-1.0 。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type SpatialStrength: float
        """
        self._Type = None
        self._TemplStrength = None
        self._SpatialStrength = None

    @property
    def Type(self):
        """去噪方式，可选项：
templ：时域降噪；
spatial：空域降噪,
fast-spatial：快速空域降噪。
注意：可选择组合方式：
1.type:"templ,spatial" ;
2.type:"templ,fast-spatial"。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TemplStrength(self):
        """时域去噪强度，可选值：0.0-1.0 。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :rtype: float
        """
        return self._TemplStrength

    @TemplStrength.setter
    def TemplStrength(self, TemplStrength):
        self._TemplStrength = TemplStrength

    @property
    def SpatialStrength(self):
        """空域去噪强度，可选值：0.0-1.0 。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :rtype: float
        """
        return self._SpatialStrength

    @SpatialStrength.setter
    def SpatialStrength(self, SpatialStrength):
        self._SpatialStrength = SpatialStrength


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TemplStrength = params.get("TemplStrength")
        self._SpatialStrength = params.get("SpatialStrength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEditingTaskResultRequest(AbstractModel):
    """DescribeEditingTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 编辑任务 ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """编辑任务 ID。
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
        


class DescribeEditingTaskResultResponse(AbstractModel):
    """DescribeEditingTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskResult: 编辑任务结果信息。
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.EditingTaskResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskResult = None
        self._RequestId = None

    @property
    def TaskResult(self):
        """编辑任务结果信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.EditingTaskResult`
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

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
        if params.get("TaskResult") is not None:
            self._TaskResult = EditingTaskResult()
            self._TaskResult._deserialize(params.get("TaskResult"))
        self._RequestId = params.get("RequestId")


class DescribeMediaProcessTaskResultRequest(AbstractModel):
    """DescribeMediaProcessTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 编辑处理任务ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """编辑处理任务ID。
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
        


class DescribeMediaProcessTaskResultResponse(AbstractModel):
    """DescribeMediaProcessTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskResult: 任务处理结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.MediaProcessTaskResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskResult = None
        self._RequestId = None

    @property
    def TaskResult(self):
        """任务处理结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaProcessTaskResult`
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

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
        if params.get("TaskResult") is not None:
            self._TaskResult = MediaProcessTaskResult()
            self._TaskResult._deserialize(params.get("TaskResult"))
        self._RequestId = params.get("RequestId")


class DescribeMediaQualityRestorationTaskRusultRequest(AbstractModel):
    """DescribeMediaQualityRestorationTaskRusult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 画质重生任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """画质重生任务ID
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
        


class DescribeMediaQualityRestorationTaskRusultResponse(AbstractModel):
    """DescribeMediaQualityRestorationTaskRusult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskResult: 画质重生任务结果信息
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.MediaQualityRestorationTaskResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskResult = None
        self._RequestId = None

    @property
    def TaskResult(self):
        """画质重生任务结果信息
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaQualityRestorationTaskResult`
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

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
        if params.get("TaskResult") is not None:
            self._TaskResult = MediaQualityRestorationTaskResult()
            self._TaskResult._deserialize(params.get("TaskResult"))
        self._RequestId = params.get("RequestId")


class DescribeQualityControlTaskResultRequest(AbstractModel):
    """DescribeQualityControlTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 质检任务 ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """质检任务 ID
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
        


class DescribeQualityControlTaskResultResponse(AbstractModel):
    """DescribeQualityControlTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskResult: 质检任务结果信息
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.QualityControlInfoTaskResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskResult = None
        self._RequestId = None

    @property
    def TaskResult(self):
        """质检任务结果信息
        :rtype: :class:`tencentcloud.ie.v20200304.models.QualityControlInfoTaskResult`
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

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
        if params.get("TaskResult") is not None:
            self._TaskResult = QualityControlInfoTaskResult()
            self._TaskResult._deserialize(params.get("TaskResult"))
        self._RequestId = params.get("RequestId")


class DownInfo(AbstractModel):
    """视频源信息

    """

    def __init__(self):
        r"""
        :param _Type: 下载类型，可选值： 
0：UrlInfo； 
1：CosInfo。
        :type Type: int
        :param _UrlInfo: Url形式下载信息，当Type等于0时必选。
        :type UrlInfo: :class:`tencentcloud.ie.v20200304.models.UrlInfo`
        :param _CosInfo: Cos形式下载信息，当Type等于1时必选。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        self._Type = None
        self._UrlInfo = None
        self._CosInfo = None

    @property
    def Type(self):
        """下载类型，可选值： 
0：UrlInfo； 
1：CosInfo。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UrlInfo(self):
        """Url形式下载信息，当Type等于0时必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.UrlInfo`
        """
        return self._UrlInfo

    @UrlInfo.setter
    def UrlInfo(self, UrlInfo):
        self._UrlInfo = UrlInfo

    @property
    def CosInfo(self):
        """Cos形式下载信息，当Type等于1时必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        return self._CosInfo

    @CosInfo.setter
    def CosInfo(self, CosInfo):
        self._CosInfo = CosInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("UrlInfo") is not None:
            self._UrlInfo = UrlInfo()
            self._UrlInfo._deserialize(params.get("UrlInfo"))
        if params.get("CosInfo") is not None:
            self._CosInfo = CosInfo()
            self._CosInfo._deserialize(params.get("CosInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicImageInfo(AbstractModel):
    """动图参数

    """

    def __init__(self):
        r"""
        :param _Quality: 画面质量，范围：1~100。
<li>对于webp格式，默认：75</li>
<li>对于gif格式，小于10为低质量，大于50为高质量，其它为普通。默认：低质量。</li>
        :type Quality: int
        """
        self._Quality = None

    @property
    def Quality(self):
        """画面质量，范围：1~100。
<li>对于webp格式，默认：75</li>
<li>对于gif格式，小于10为低质量，大于50为高质量，其它为普通。默认：低质量。</li>
        :rtype: int
        """
        return self._Quality

    @Quality.setter
    def Quality(self, Quality):
        self._Quality = Quality


    def _deserialize(self, params):
        self._Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditInfo(AbstractModel):
    """画质重生子任务视频剪辑参数

    """

    def __init__(self):
        r"""
        :param _StartTime: 剪辑开始时间，单位：ms。
        :type StartTime: int
        :param _EndTime: 剪辑结束时间，单位：ms
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """剪辑开始时间，单位：ms。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """剪辑结束时间，单位：ms
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditingInfo(AbstractModel):
    """智能编辑任务参数信息

    """

    def __init__(self):
        r"""
        :param _TagEditingInfo: 视频标签识别任务参数，不填则不开启。
        :type TagEditingInfo: :class:`tencentcloud.ie.v20200304.models.TagEditingInfo`
        :param _ClassificationEditingInfo: 视频分类识别任务参数，不填则不开启。
        :type ClassificationEditingInfo: :class:`tencentcloud.ie.v20200304.models.ClassificationEditingInfo`
        :param _StripEditingInfo: 智能拆条任务参数，不填则不开启。
        :type StripEditingInfo: :class:`tencentcloud.ie.v20200304.models.StripEditingInfo`
        :param _HighlightsEditingInfo: 智能集锦任务参数，不填则不开启。
        :type HighlightsEditingInfo: :class:`tencentcloud.ie.v20200304.models.HighlightsEditingInfo`
        :param _CoverEditingInfo: 智能封面任务参数，不填则不开启。
        :type CoverEditingInfo: :class:`tencentcloud.ie.v20200304.models.CoverEditingInfo`
        :param _OpeningEndingEditingInfo: 片头片尾识别任务参数，不填则不开启。
        :type OpeningEndingEditingInfo: :class:`tencentcloud.ie.v20200304.models.OpeningEndingEditingInfo`
        """
        self._TagEditingInfo = None
        self._ClassificationEditingInfo = None
        self._StripEditingInfo = None
        self._HighlightsEditingInfo = None
        self._CoverEditingInfo = None
        self._OpeningEndingEditingInfo = None

    @property
    def TagEditingInfo(self):
        """视频标签识别任务参数，不填则不开启。
        :rtype: :class:`tencentcloud.ie.v20200304.models.TagEditingInfo`
        """
        return self._TagEditingInfo

    @TagEditingInfo.setter
    def TagEditingInfo(self, TagEditingInfo):
        self._TagEditingInfo = TagEditingInfo

    @property
    def ClassificationEditingInfo(self):
        """视频分类识别任务参数，不填则不开启。
        :rtype: :class:`tencentcloud.ie.v20200304.models.ClassificationEditingInfo`
        """
        return self._ClassificationEditingInfo

    @ClassificationEditingInfo.setter
    def ClassificationEditingInfo(self, ClassificationEditingInfo):
        self._ClassificationEditingInfo = ClassificationEditingInfo

    @property
    def StripEditingInfo(self):
        """智能拆条任务参数，不填则不开启。
        :rtype: :class:`tencentcloud.ie.v20200304.models.StripEditingInfo`
        """
        return self._StripEditingInfo

    @StripEditingInfo.setter
    def StripEditingInfo(self, StripEditingInfo):
        self._StripEditingInfo = StripEditingInfo

    @property
    def HighlightsEditingInfo(self):
        """智能集锦任务参数，不填则不开启。
        :rtype: :class:`tencentcloud.ie.v20200304.models.HighlightsEditingInfo`
        """
        return self._HighlightsEditingInfo

    @HighlightsEditingInfo.setter
    def HighlightsEditingInfo(self, HighlightsEditingInfo):
        self._HighlightsEditingInfo = HighlightsEditingInfo

    @property
    def CoverEditingInfo(self):
        """智能封面任务参数，不填则不开启。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CoverEditingInfo`
        """
        return self._CoverEditingInfo

    @CoverEditingInfo.setter
    def CoverEditingInfo(self, CoverEditingInfo):
        self._CoverEditingInfo = CoverEditingInfo

    @property
    def OpeningEndingEditingInfo(self):
        """片头片尾识别任务参数，不填则不开启。
        :rtype: :class:`tencentcloud.ie.v20200304.models.OpeningEndingEditingInfo`
        """
        return self._OpeningEndingEditingInfo

    @OpeningEndingEditingInfo.setter
    def OpeningEndingEditingInfo(self, OpeningEndingEditingInfo):
        self._OpeningEndingEditingInfo = OpeningEndingEditingInfo


    def _deserialize(self, params):
        if params.get("TagEditingInfo") is not None:
            self._TagEditingInfo = TagEditingInfo()
            self._TagEditingInfo._deserialize(params.get("TagEditingInfo"))
        if params.get("ClassificationEditingInfo") is not None:
            self._ClassificationEditingInfo = ClassificationEditingInfo()
            self._ClassificationEditingInfo._deserialize(params.get("ClassificationEditingInfo"))
        if params.get("StripEditingInfo") is not None:
            self._StripEditingInfo = StripEditingInfo()
            self._StripEditingInfo._deserialize(params.get("StripEditingInfo"))
        if params.get("HighlightsEditingInfo") is not None:
            self._HighlightsEditingInfo = HighlightsEditingInfo()
            self._HighlightsEditingInfo._deserialize(params.get("HighlightsEditingInfo"))
        if params.get("CoverEditingInfo") is not None:
            self._CoverEditingInfo = CoverEditingInfo()
            self._CoverEditingInfo._deserialize(params.get("CoverEditingInfo"))
        if params.get("OpeningEndingEditingInfo") is not None:
            self._OpeningEndingEditingInfo = OpeningEndingEditingInfo()
            self._OpeningEndingEditingInfo._deserialize(params.get("OpeningEndingEditingInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditingTaskResult(AbstractModel):
    """智能识别任务结果信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 编辑任务 ID。
        :type TaskId: str
        :param _Status: 编辑任务状态。 
1：执行中；2：已完成。
        :type Status: int
        :param _TagTaskResult: 视频标签识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagTaskResult: :class:`tencentcloud.ie.v20200304.models.TagTaskResult`
        :param _ClassificationTaskResult: 视频分类识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationTaskResult: :class:`tencentcloud.ie.v20200304.models.ClassificationTaskResult`
        :param _StripTaskResult: 智能拆条结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type StripTaskResult: :class:`tencentcloud.ie.v20200304.models.StripTaskResult`
        :param _HighlightsTaskResult: 智能集锦结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type HighlightsTaskResult: :class:`tencentcloud.ie.v20200304.models.HighlightsTaskResult`
        :param _CoverTaskResult: 智能封面结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverTaskResult: :class:`tencentcloud.ie.v20200304.models.CoverTaskResult`
        :param _OpeningEndingTaskResult: 片头片尾识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type OpeningEndingTaskResult: :class:`tencentcloud.ie.v20200304.models.OpeningEndingTaskResult`
        """
        self._TaskId = None
        self._Status = None
        self._TagTaskResult = None
        self._ClassificationTaskResult = None
        self._StripTaskResult = None
        self._HighlightsTaskResult = None
        self._CoverTaskResult = None
        self._OpeningEndingTaskResult = None

    @property
    def TaskId(self):
        """编辑任务 ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """编辑任务状态。 
1：执行中；2：已完成。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TagTaskResult(self):
        """视频标签识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.TagTaskResult`
        """
        return self._TagTaskResult

    @TagTaskResult.setter
    def TagTaskResult(self, TagTaskResult):
        self._TagTaskResult = TagTaskResult

    @property
    def ClassificationTaskResult(self):
        """视频分类识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.ClassificationTaskResult`
        """
        return self._ClassificationTaskResult

    @ClassificationTaskResult.setter
    def ClassificationTaskResult(self, ClassificationTaskResult):
        self._ClassificationTaskResult = ClassificationTaskResult

    @property
    def StripTaskResult(self):
        """智能拆条结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.StripTaskResult`
        """
        return self._StripTaskResult

    @StripTaskResult.setter
    def StripTaskResult(self, StripTaskResult):
        self._StripTaskResult = StripTaskResult

    @property
    def HighlightsTaskResult(self):
        """智能集锦结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.HighlightsTaskResult`
        """
        return self._HighlightsTaskResult

    @HighlightsTaskResult.setter
    def HighlightsTaskResult(self, HighlightsTaskResult):
        self._HighlightsTaskResult = HighlightsTaskResult

    @property
    def CoverTaskResult(self):
        """智能封面结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CoverTaskResult`
        """
        return self._CoverTaskResult

    @CoverTaskResult.setter
    def CoverTaskResult(self, CoverTaskResult):
        self._CoverTaskResult = CoverTaskResult

    @property
    def OpeningEndingTaskResult(self):
        """片头片尾识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.OpeningEndingTaskResult`
        """
        return self._OpeningEndingTaskResult

    @OpeningEndingTaskResult.setter
    def OpeningEndingTaskResult(self, OpeningEndingTaskResult):
        self._OpeningEndingTaskResult = OpeningEndingTaskResult


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        if params.get("TagTaskResult") is not None:
            self._TagTaskResult = TagTaskResult()
            self._TagTaskResult._deserialize(params.get("TagTaskResult"))
        if params.get("ClassificationTaskResult") is not None:
            self._ClassificationTaskResult = ClassificationTaskResult()
            self._ClassificationTaskResult._deserialize(params.get("ClassificationTaskResult"))
        if params.get("StripTaskResult") is not None:
            self._StripTaskResult = StripTaskResult()
            self._StripTaskResult._deserialize(params.get("StripTaskResult"))
        if params.get("HighlightsTaskResult") is not None:
            self._HighlightsTaskResult = HighlightsTaskResult()
            self._HighlightsTaskResult._deserialize(params.get("HighlightsTaskResult"))
        if params.get("CoverTaskResult") is not None:
            self._CoverTaskResult = CoverTaskResult()
            self._CoverTaskResult._deserialize(params.get("CoverTaskResult"))
        if params.get("OpeningEndingTaskResult") is not None:
            self._OpeningEndingTaskResult = OpeningEndingTaskResult()
            self._OpeningEndingTaskResult._deserialize(params.get("OpeningEndingTaskResult"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceProtect(AbstractModel):
    """人脸保护参数

    """

    def __init__(self):
        r"""
        :param _FaceUsmRatio: 人脸区域增强强度，可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type FaceUsmRatio: float
        """
        self._FaceUsmRatio = None

    @property
    def FaceUsmRatio(self):
        """人脸区域增强强度，可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :rtype: float
        """
        return self._FaceUsmRatio

    @FaceUsmRatio.setter
    def FaceUsmRatio(self, FaceUsmRatio):
        self._FaceUsmRatio = FaceUsmRatio


    def _deserialize(self, params):
        self._FaceUsmRatio = params.get("FaceUsmRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """画质重生处理后文件的详细信息

    """

    def __init__(self):
        r"""
        :param _FileSize: 任务结束后生成的文件大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _FileType: 任务结束后生成的文件格式，例如：mp4,flv等等。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _Bitrate: 任务结束后生成的文件整体码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param _Duration: 任务结束后生成的文件时长，单位：ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _VideoInfoResult: 任务结束后生成的文件视频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoInfoResult: list of VideoInfoResultItem
        :param _AudioInfoResult: 任务结束后生成的文件音频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioInfoResult: list of AudioInfoResultItem
        """
        self._FileSize = None
        self._FileType = None
        self._Bitrate = None
        self._Duration = None
        self._VideoInfoResult = None
        self._AudioInfoResult = None

    @property
    def FileSize(self):
        """任务结束后生成的文件大小。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileType(self):
        """任务结束后生成的文件格式，例如：mp4,flv等等。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Bitrate(self):
        """任务结束后生成的文件整体码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Duration(self):
        """任务结束后生成的文件时长，单位：ms。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def VideoInfoResult(self):
        """任务结束后生成的文件视频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VideoInfoResultItem
        """
        return self._VideoInfoResult

    @VideoInfoResult.setter
    def VideoInfoResult(self, VideoInfoResult):
        self._VideoInfoResult = VideoInfoResult

    @property
    def AudioInfoResult(self):
        """任务结束后生成的文件音频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioInfoResultItem
        """
        return self._AudioInfoResult

    @AudioInfoResult.setter
    def AudioInfoResult(self, AudioInfoResult):
        self._AudioInfoResult = AudioInfoResult


    def _deserialize(self, params):
        self._FileSize = params.get("FileSize")
        self._FileType = params.get("FileType")
        self._Bitrate = params.get("Bitrate")
        self._Duration = params.get("Duration")
        if params.get("VideoInfoResult") is not None:
            self._VideoInfoResult = []
            for item in params.get("VideoInfoResult"):
                obj = VideoInfoResultItem()
                obj._deserialize(item)
                self._VideoInfoResult.append(obj)
        if params.get("AudioInfoResult") is not None:
            self._AudioInfoResult = []
            for item in params.get("AudioInfoResult"):
                obj = AudioInfoResultItem()
                obj._deserialize(item)
                self._AudioInfoResult.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagItem(AbstractModel):
    """帧标签

    """

    def __init__(self):
        r"""
        :param _StartPts: 标签起始时间戳PTS(ms)
        :type StartPts: int
        :param _EndPts: 语句结束时间戳PTS(ms)
        :type EndPts: int
        :param _Period: 字符串形式的起始结束时间
        :type Period: str
        :param _TagItems: 标签数组
        :type TagItems: list of TagItem
        """
        self._StartPts = None
        self._EndPts = None
        self._Period = None
        self._TagItems = None

    @property
    def StartPts(self):
        """标签起始时间戳PTS(ms)
        :rtype: int
        """
        return self._StartPts

    @StartPts.setter
    def StartPts(self, StartPts):
        self._StartPts = StartPts

    @property
    def EndPts(self):
        """语句结束时间戳PTS(ms)
        :rtype: int
        """
        return self._EndPts

    @EndPts.setter
    def EndPts(self, EndPts):
        self._EndPts = EndPts

    @property
    def Period(self):
        """字符串形式的起始结束时间
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TagItems(self):
        """标签数组
        :rtype: list of TagItem
        """
        return self._TagItems

    @TagItems.setter
    def TagItems(self, TagItems):
        self._TagItems = TagItems


    def _deserialize(self, params):
        self._StartPts = params.get("StartPts")
        self._EndPts = params.get("EndPts")
        self._Period = params.get("Period")
        if params.get("TagItems") is not None:
            self._TagItems = []
            for item in params.get("TagItems"):
                obj = TagItem()
                obj._deserialize(item)
                self._TagItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagRec(AbstractModel):
    """帧标签任务参数

    """

    def __init__(self):
        r"""
        :param _TagType: 标签类型：
"Common": 通用类型
"Game":游戏类型
        :type TagType: str
        :param _GameExtendType: 游戏具体类型:
"HonorOfKings_AnchorViews":王者荣耀主播视角
"HonorOfKings_GameViews":王者荣耀比赛视角
"LOL_AnchorViews":英雄联盟主播视角
"LOL_GameViews":英雄联盟比赛视角
"PUBG_AnchorViews":和平精英主播视角
"PUBG_GameViews":和平精英比赛视角
        :type GameExtendType: str
        """
        self._TagType = None
        self._GameExtendType = None

    @property
    def TagType(self):
        """标签类型：
"Common": 通用类型
"Game":游戏类型
        :rtype: str
        """
        return self._TagType

    @TagType.setter
    def TagType(self, TagType):
        self._TagType = TagType

    @property
    def GameExtendType(self):
        """游戏具体类型:
"HonorOfKings_AnchorViews":王者荣耀主播视角
"HonorOfKings_GameViews":王者荣耀比赛视角
"LOL_AnchorViews":英雄联盟主播视角
"LOL_GameViews":英雄联盟比赛视角
"PUBG_AnchorViews":和平精英主播视角
"PUBG_GameViews":和平精英比赛视角
        :rtype: str
        """
        return self._GameExtendType

    @GameExtendType.setter
    def GameExtendType(self, GameExtendType):
        self._GameExtendType = GameExtendType


    def _deserialize(self, params):
        self._TagType = params.get("TagType")
        self._GameExtendType = params.get("GameExtendType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagResult(AbstractModel):
    """帧标签结果

    """

    def __init__(self):
        r"""
        :param _FrameTagItems: 帧标签结果数组
        :type FrameTagItems: list of FrameTagItem
        """
        self._FrameTagItems = None

    @property
    def FrameTagItems(self):
        """帧标签结果数组
        :rtype: list of FrameTagItem
        """
        return self._FrameTagItems

    @FrameTagItems.setter
    def FrameTagItems(self, FrameTagItems):
        self._FrameTagItems = FrameTagItems


    def _deserialize(self, params):
        if params.get("FrameTagItems") is not None:
            self._FrameTagItems = []
            for item in params.get("FrameTagItems"):
                obj = FrameTagItem()
                obj._deserialize(item)
                self._FrameTagItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HiddenMarkInfo(AbstractModel):
    """数字水印

    """

    def __init__(self):
        r"""
        :param _Path: 数字水印路径,，如果不从Cos拉取水印，则必填
        :type Path: str
        :param _Frequency: 数字水印频率，可选值：[1,256]，默认值为30
        :type Frequency: int
        :param _Strength: 数字水印强度，可选值：[32,128]，默认值为64
        :type Strength: int
        :param _CosInfo: 数字水印的Cos 信息，从Cos上拉取图片水印时必填。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        self._Path = None
        self._Frequency = None
        self._Strength = None
        self._CosInfo = None

    @property
    def Path(self):
        """数字水印路径,，如果不从Cos拉取水印，则必填
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Frequency(self):
        """数字水印频率，可选值：[1,256]，默认值为30
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def Strength(self):
        """数字水印强度，可选值：[32,128]，默认值为64
        :rtype: int
        """
        return self._Strength

    @Strength.setter
    def Strength(self, Strength):
        self._Strength = Strength

    @property
    def CosInfo(self):
        """数字水印的Cos 信息，从Cos上拉取图片水印时必填。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        return self._CosInfo

    @CosInfo.setter
    def CosInfo(self, CosInfo):
        self._CosInfo = CosInfo


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Frequency = params.get("Frequency")
        self._Strength = params.get("Strength")
        if params.get("CosInfo") is not None:
            self._CosInfo = CosInfo()
            self._CosInfo._deserialize(params.get("CosInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsEditingInfo(AbstractModel):
    """智能集锦任务参数信息

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启智能集锦。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param _CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self._Switch = None
        self._CustomInfo = None

    @property
    def Switch(self):
        """是否开启智能集锦。0为关闭，1为开启。其他非0非1值默认为0。
        :rtype: int
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CustomInfo(self):
        """额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :rtype: str
        """
        return self._CustomInfo

    @CustomInfo.setter
    def CustomInfo(self, CustomInfo):
        self._CustomInfo = CustomInfo


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsTaskResult(AbstractModel):
    """智能集锦结果信息

    """

    def __init__(self):
        r"""
        :param _Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param _ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param _ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param _ItemSet: 智能集锦结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of HighlightsTaskResultItem
        """
        self._Status = None
        self._ErrCode = None
        self._ErrMsg = None
        self._ItemSet = None

    @property
    def Status(self):
        """编辑任务状态。 
1：执行中；2：成功；3：失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """编辑任务失败错误码。 
0：成功；其他值：失败。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """编辑任务失败错误描述。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ItemSet(self):
        """智能集锦结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of HighlightsTaskResultItem
        """
        return self._ItemSet

    @ItemSet.setter
    def ItemSet(self, ItemSet):
        self._ItemSet = ItemSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self._ItemSet = []
            for item in params.get("ItemSet"):
                obj = HighlightsTaskResultItem()
                obj._deserialize(item)
                self._ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsTaskResultItem(AbstractModel):
    """智能集锦结果项

    """

    def __init__(self):
        r"""
        :param _HighlightUrl: 智能集锦地址。
        :type HighlightUrl: str
        :param _CovImgUrl: 智能集锦封面地址。
        :type CovImgUrl: str
        :param _Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param _Duration: 智能集锦持续时间，单位：秒。
        :type Duration: float
        :param _SegmentSet: 智能集锦子片段结果集，集锦片段由这些子片段拼接生成。
        :type SegmentSet: list of HighlightsTaskResultItemSegment
        """
        self._HighlightUrl = None
        self._CovImgUrl = None
        self._Confidence = None
        self._Duration = None
        self._SegmentSet = None

    @property
    def HighlightUrl(self):
        """智能集锦地址。
        :rtype: str
        """
        return self._HighlightUrl

    @HighlightUrl.setter
    def HighlightUrl(self, HighlightUrl):
        self._HighlightUrl = HighlightUrl

    @property
    def CovImgUrl(self):
        """智能集锦封面地址。
        :rtype: str
        """
        return self._CovImgUrl

    @CovImgUrl.setter
    def CovImgUrl(self, CovImgUrl):
        self._CovImgUrl = CovImgUrl

    @property
    def Confidence(self):
        """置信度，取值范围是 0 到 100。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Duration(self):
        """智能集锦持续时间，单位：秒。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def SegmentSet(self):
        """智能集锦子片段结果集，集锦片段由这些子片段拼接生成。
        :rtype: list of HighlightsTaskResultItemSegment
        """
        return self._SegmentSet

    @SegmentSet.setter
    def SegmentSet(self, SegmentSet):
        self._SegmentSet = SegmentSet


    def _deserialize(self, params):
        self._HighlightUrl = params.get("HighlightUrl")
        self._CovImgUrl = params.get("CovImgUrl")
        self._Confidence = params.get("Confidence")
        self._Duration = params.get("Duration")
        if params.get("SegmentSet") is not None:
            self._SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = HighlightsTaskResultItemSegment()
                obj._deserialize(item)
                self._SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsTaskResultItemSegment(AbstractModel):
    """智能集锦结果片段

    """

    def __init__(self):
        r"""
        :param _Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param _StartTimeOffset: 集锦片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param _EndTimeOffset: 集锦片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        """
        self._Confidence = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None

    @property
    def Confidence(self):
        """置信度，取值范围是 0 到 100。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def StartTimeOffset(self):
        """集锦片段起始的偏移时间，单位：秒。
        :rtype: float
        """
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        """集锦片段终止的偏移时间，单位：秒。
        :rtype: float
        """
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntervalTime(AbstractModel):
    """周期时间点信息。

    """

    def __init__(self):
        r"""
        :param _Interval: 间隔周期，单位ms
        :type Interval: int
        :param _StartTime: 开始时间点，单位ms
        :type StartTime: int
        """
        self._Interval = None
        self._StartTime = None

    @property
    def Interval(self):
        """间隔周期，单位ms
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def StartTime(self):
        """开始时间点，单位ms
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoudnessInfo(AbstractModel):
    """音频响度信息

    """

    def __init__(self):
        r"""
        :param _Loudness: 音频整体响度
        :type Loudness: float
        :param _LoudnessRange: 音频响度范围
        :type LoudnessRange: float
        """
        self._Loudness = None
        self._LoudnessRange = None

    @property
    def Loudness(self):
        """音频整体响度
        :rtype: float
        """
        return self._Loudness

    @Loudness.setter
    def Loudness(self, Loudness):
        self._Loudness = Loudness

    @property
    def LoudnessRange(self):
        """音频响度范围
        :rtype: float
        """
        return self._LoudnessRange

    @LoudnessRange.setter
    def LoudnessRange(self, LoudnessRange):
        self._LoudnessRange = LoudnessRange


    def _deserialize(self, params):
        self._Loudness = params.get("Loudness")
        self._LoudnessRange = params.get("LoudnessRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowLightEnhance(AbstractModel):
    """低光照增强参数

    """

    def __init__(self):
        r"""
        :param _Type: 低光照增强类型，可选项：normal。
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        """低光照增强类型，可选项：normal。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingInfo(AbstractModel):
    """编辑处理/剪切任务信息。
    截图结果默认存在 SaveInfoSet 的第一个存储位置。

    """

    def __init__(self):
        r"""
        :param _TimeInfo: 截取时间信息。
        :type TimeInfo: :class:`tencentcloud.ie.v20200304.models.MediaCuttingTimeInfo`
        :param _TargetInfo: 输出结果信息。
        :type TargetInfo: :class:`tencentcloud.ie.v20200304.models.MediaTargetInfo`
        :param _OutForm: 截取结果形式信息。
        :type OutForm: :class:`tencentcloud.ie.v20200304.models.MediaCuttingOutForm`
        :param _ResultListSaveType: 列表文件形式，存储到用户存储服务中，可选值：
<li>NoListFile：不存储结果列表; </li>
<li>UseSaveInfo：默认，结果列表和结果存储同一位置（即SaveInfoSet 的第一个存储位置）；</li>
<li>SaveInfoSet 存储的Id：存储在指定的存储位置。</li>
        :type ResultListSaveType: str
        :param _WatermarkInfoSet: 水印信息，最多支持 10 个水印。
        :type WatermarkInfoSet: list of MediaCuttingWatermark
        :param _DropPureColor: 是否去除纯色截图，如果值为 True ，对应时间点的截图如果是纯色，将略过。
        :type DropPureColor: str
        """
        self._TimeInfo = None
        self._TargetInfo = None
        self._OutForm = None
        self._ResultListSaveType = None
        self._WatermarkInfoSet = None
        self._DropPureColor = None

    @property
    def TimeInfo(self):
        """截取时间信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaCuttingTimeInfo`
        """
        return self._TimeInfo

    @TimeInfo.setter
    def TimeInfo(self, TimeInfo):
        self._TimeInfo = TimeInfo

    @property
    def TargetInfo(self):
        """输出结果信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaTargetInfo`
        """
        return self._TargetInfo

    @TargetInfo.setter
    def TargetInfo(self, TargetInfo):
        self._TargetInfo = TargetInfo

    @property
    def OutForm(self):
        """截取结果形式信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaCuttingOutForm`
        """
        return self._OutForm

    @OutForm.setter
    def OutForm(self, OutForm):
        self._OutForm = OutForm

    @property
    def ResultListSaveType(self):
        """列表文件形式，存储到用户存储服务中，可选值：
<li>NoListFile：不存储结果列表; </li>
<li>UseSaveInfo：默认，结果列表和结果存储同一位置（即SaveInfoSet 的第一个存储位置）；</li>
<li>SaveInfoSet 存储的Id：存储在指定的存储位置。</li>
        :rtype: str
        """
        return self._ResultListSaveType

    @ResultListSaveType.setter
    def ResultListSaveType(self, ResultListSaveType):
        self._ResultListSaveType = ResultListSaveType

    @property
    def WatermarkInfoSet(self):
        """水印信息，最多支持 10 个水印。
        :rtype: list of MediaCuttingWatermark
        """
        return self._WatermarkInfoSet

    @WatermarkInfoSet.setter
    def WatermarkInfoSet(self, WatermarkInfoSet):
        self._WatermarkInfoSet = WatermarkInfoSet

    @property
    def DropPureColor(self):
        """是否去除纯色截图，如果值为 True ，对应时间点的截图如果是纯色，将略过。
        :rtype: str
        """
        return self._DropPureColor

    @DropPureColor.setter
    def DropPureColor(self, DropPureColor):
        self._DropPureColor = DropPureColor


    def _deserialize(self, params):
        if params.get("TimeInfo") is not None:
            self._TimeInfo = MediaCuttingTimeInfo()
            self._TimeInfo._deserialize(params.get("TimeInfo"))
        if params.get("TargetInfo") is not None:
            self._TargetInfo = MediaTargetInfo()
            self._TargetInfo._deserialize(params.get("TargetInfo"))
        if params.get("OutForm") is not None:
            self._OutForm = MediaCuttingOutForm()
            self._OutForm._deserialize(params.get("OutForm"))
        self._ResultListSaveType = params.get("ResultListSaveType")
        if params.get("WatermarkInfoSet") is not None:
            self._WatermarkInfoSet = []
            for item in params.get("WatermarkInfoSet"):
                obj = MediaCuttingWatermark()
                obj._deserialize(item)
                self._WatermarkInfoSet.append(obj)
        self._DropPureColor = params.get("DropPureColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingOutForm(AbstractModel):
    """编辑处理/剪切任务/输出形式信息

    """

    def __init__(self):
        r"""
        :param _Type: 输出类型，可选值：
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
        :param _FillType: 背景填充方式，可选值：
White：白色填充；
Black：黑色填充；
Stretch：拉伸；
Gaussian：高斯模糊；
默认White。
        :type FillType: str
        :param _SpriteRowCount: 【废弃】参考SpriteInfo
        :type SpriteRowCount: int
        :param _SpriteColumnCount: 【废弃】参考SpriteInfo
        :type SpriteColumnCount: int
        :param _SpriteInfo: Type=Sprite时有效，表示雪碧图参数信息。
        :type SpriteInfo: :class:`tencentcloud.ie.v20200304.models.SpriteImageInfo`
        :param _DynamicInfo: Type=Dynamic时有效，表示动图参数信息。
        :type DynamicInfo: :class:`tencentcloud.ie.v20200304.models.DynamicImageInfo`
        """
        self._Type = None
        self._FillType = None
        self._SpriteRowCount = None
        self._SpriteColumnCount = None
        self._SpriteInfo = None
        self._DynamicInfo = None

    @property
    def Type(self):
        """输出类型，可选值：
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
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FillType(self):
        """背景填充方式，可选值：
White：白色填充；
Black：黑色填充；
Stretch：拉伸；
Gaussian：高斯模糊；
默认White。
        :rtype: str
        """
        return self._FillType

    @FillType.setter
    def FillType(self, FillType):
        self._FillType = FillType

    @property
    def SpriteRowCount(self):
        """【废弃】参考SpriteInfo
        :rtype: int
        """
        return self._SpriteRowCount

    @SpriteRowCount.setter
    def SpriteRowCount(self, SpriteRowCount):
        self._SpriteRowCount = SpriteRowCount

    @property
    def SpriteColumnCount(self):
        """【废弃】参考SpriteInfo
        :rtype: int
        """
        return self._SpriteColumnCount

    @SpriteColumnCount.setter
    def SpriteColumnCount(self, SpriteColumnCount):
        self._SpriteColumnCount = SpriteColumnCount

    @property
    def SpriteInfo(self):
        """Type=Sprite时有效，表示雪碧图参数信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.SpriteImageInfo`
        """
        return self._SpriteInfo

    @SpriteInfo.setter
    def SpriteInfo(self, SpriteInfo):
        self._SpriteInfo = SpriteInfo

    @property
    def DynamicInfo(self):
        """Type=Dynamic时有效，表示动图参数信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.DynamicImageInfo`
        """
        return self._DynamicInfo

    @DynamicInfo.setter
    def DynamicInfo(self, DynamicInfo):
        self._DynamicInfo = DynamicInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._FillType = params.get("FillType")
        self._SpriteRowCount = params.get("SpriteRowCount")
        self._SpriteColumnCount = params.get("SpriteColumnCount")
        if params.get("SpriteInfo") is not None:
            self._SpriteInfo = SpriteImageInfo()
            self._SpriteInfo._deserialize(params.get("SpriteInfo"))
        if params.get("DynamicInfo") is not None:
            self._DynamicInfo = DynamicImageInfo()
            self._DynamicInfo._deserialize(params.get("DynamicInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingTaskResult(AbstractModel):
    """编辑处理/剪切任务/处理结果

    """

    def __init__(self):
        r"""
        :param _ListFile: 如果ResultListType不为NoListFile时，结果（TaskResultFile）列表文件的存储位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ListFile: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        :param _ResultCount: 结果个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCount: int
        :param _FirstFile: 第一个结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstFile: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        :param _LastFile: 最后一个结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastFile: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        :param _ImageCount: 任务结果包含的图片总数。
静态图：总数即为文件数；
雪碧图：所有小图总数；
动图、视频：不计算图片数，为 0。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCount: int
        """
        self._ListFile = None
        self._ResultCount = None
        self._FirstFile = None
        self._LastFile = None
        self._ImageCount = None

    @property
    def ListFile(self):
        """如果ResultListType不为NoListFile时，结果（TaskResultFile）列表文件的存储位置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        """
        return self._ListFile

    @ListFile.setter
    def ListFile(self, ListFile):
        self._ListFile = ListFile

    @property
    def ResultCount(self):
        """结果个数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResultCount

    @ResultCount.setter
    def ResultCount(self, ResultCount):
        self._ResultCount = ResultCount

    @property
    def FirstFile(self):
        """第一个结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        """
        return self._FirstFile

    @FirstFile.setter
    def FirstFile(self, FirstFile):
        self._FirstFile = FirstFile

    @property
    def LastFile(self):
        """最后一个结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        """
        return self._LastFile

    @LastFile.setter
    def LastFile(self, LastFile):
        self._LastFile = LastFile

    @property
    def ImageCount(self):
        """任务结果包含的图片总数。
静态图：总数即为文件数；
雪碧图：所有小图总数；
动图、视频：不计算图片数，为 0。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ImageCount

    @ImageCount.setter
    def ImageCount(self, ImageCount):
        self._ImageCount = ImageCount


    def _deserialize(self, params):
        if params.get("ListFile") is not None:
            self._ListFile = TaskResultFile()
            self._ListFile._deserialize(params.get("ListFile"))
        self._ResultCount = params.get("ResultCount")
        if params.get("FirstFile") is not None:
            self._FirstFile = TaskResultFile()
            self._FirstFile._deserialize(params.get("FirstFile"))
        if params.get("LastFile") is not None:
            self._LastFile = TaskResultFile()
            self._LastFile._deserialize(params.get("LastFile"))
        self._ImageCount = params.get("ImageCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingTimeInfo(AbstractModel):
    """编辑处理/剪切任务/时间信息

    """

    def __init__(self):
        r"""
        :param _Type: 时间类型，可选值：
PointSet：时间点集合；
IntervalPoint：周期采样点；
SectionSet：时间片段集合。
        :type Type: str
        :param _PointSet: 截取时间点集合，单位毫秒，Type=PointSet时必选。
        :type PointSet: list of int
        :param _IntervalPoint: 周期采样点信息，Type=IntervalPoint时必选。
        :type IntervalPoint: :class:`tencentcloud.ie.v20200304.models.IntervalTime`
        :param _SectionSet: 时间区间集合信息，Type=SectionSet时必选。
        :type SectionSet: list of SectionTime
        """
        self._Type = None
        self._PointSet = None
        self._IntervalPoint = None
        self._SectionSet = None

    @property
    def Type(self):
        """时间类型，可选值：
PointSet：时间点集合；
IntervalPoint：周期采样点；
SectionSet：时间片段集合。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PointSet(self):
        """截取时间点集合，单位毫秒，Type=PointSet时必选。
        :rtype: list of int
        """
        return self._PointSet

    @PointSet.setter
    def PointSet(self, PointSet):
        self._PointSet = PointSet

    @property
    def IntervalPoint(self):
        """周期采样点信息，Type=IntervalPoint时必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.IntervalTime`
        """
        return self._IntervalPoint

    @IntervalPoint.setter
    def IntervalPoint(self, IntervalPoint):
        self._IntervalPoint = IntervalPoint

    @property
    def SectionSet(self):
        """时间区间集合信息，Type=SectionSet时必选。
        :rtype: list of SectionTime
        """
        return self._SectionSet

    @SectionSet.setter
    def SectionSet(self, SectionSet):
        self._SectionSet = SectionSet


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._PointSet = params.get("PointSet")
        if params.get("IntervalPoint") is not None:
            self._IntervalPoint = IntervalTime()
            self._IntervalPoint._deserialize(params.get("IntervalPoint"))
        if params.get("SectionSet") is not None:
            self._SectionSet = []
            for item in params.get("SectionSet"):
                obj = SectionTime()
                obj._deserialize(item)
                self._SectionSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingWatermark(AbstractModel):
    """媒体剪切水印信息。

    """

    def __init__(self):
        r"""
        :param _Type: 水印类型，可选值：
<li>Image：图像水印；</li>
<li>Text：文字水印。</li>
        :type Type: str
        :param _Image: 图像水印信息，当 Type=Image 时必选。
        :type Image: :class:`tencentcloud.ie.v20200304.models.MediaCuttingWatermarkImage`
        :param _Text: 文字水印信息，当 Type=Text 时必选。
        :type Text: :class:`tencentcloud.ie.v20200304.models.MediaCuttingWatermarkText`
        """
        self._Type = None
        self._Image = None
        self._Text = None

    @property
    def Type(self):
        """水印类型，可选值：
<li>Image：图像水印；</li>
<li>Text：文字水印。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Image(self):
        """图像水印信息，当 Type=Image 时必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaCuttingWatermarkImage`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Text(self):
        """文字水印信息，当 Type=Text 时必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaCuttingWatermarkText`
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Image") is not None:
            self._Image = MediaCuttingWatermarkImage()
            self._Image._deserialize(params.get("Image"))
        if params.get("Text") is not None:
            self._Text = MediaCuttingWatermarkText()
            self._Text._deserialize(params.get("Text"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingWatermarkImage(AbstractModel):
    """媒体剪切图像水印参数。

    """

    def __init__(self):
        r"""
        :param _SourceId: 水印源的ID，对应SourceInfoSet内的源。
注意1：对应的 MediaSourceInfo.Type需要为Image。
注意2：对于动图，只取第一帧图像作为水印源。
        :type SourceId: str
        :param _PosX: 水印水平坐标，单位像素，默认：0。
        :type PosX: int
        :param _PosY: 水印垂直坐标，单位像素，默认：0。
        :type PosY: int
        :param _Width: 水印宽度，单位像素，默认：0。
        :type Width: int
        :param _Height: 水印高度，单位像素，默认：0。
注意：对于宽高符合以下规则：
1、Width>0 且 Height>0，按指定宽高拉伸；
2、Width=0 且 Height>0，以Height为基准等比缩放；
3、Width>0 且 Height=0，以Width为基准等比缩放；
4、Width=0 且 Height=0，采用源的宽高。
        :type Height: int
        :param _PosOriginType: 指定坐标原点，可选值：
<li>LeftTop：PosXY 表示水印左上点到图片左上点的相对位置</li>
<li>RightTop：PosXY 表示水印右上点到图片右上点的相对位置</li>
<li>LeftBottom：PosXY 表示水印左下点到图片左下点的相对位置</li>
<li>RightBottom：PosXY 表示水印右下点到图片右下点的相对位置</li>
<li>Center：PosXY 表示水印中心点到图片中心点的相对位置</li>
默认：LeftTop。
        :type PosOriginType: str
        """
        self._SourceId = None
        self._PosX = None
        self._PosY = None
        self._Width = None
        self._Height = None
        self._PosOriginType = None

    @property
    def SourceId(self):
        """水印源的ID，对应SourceInfoSet内的源。
注意1：对应的 MediaSourceInfo.Type需要为Image。
注意2：对于动图，只取第一帧图像作为水印源。
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def PosX(self):
        """水印水平坐标，单位像素，默认：0。
        :rtype: int
        """
        return self._PosX

    @PosX.setter
    def PosX(self, PosX):
        self._PosX = PosX

    @property
    def PosY(self):
        """水印垂直坐标，单位像素，默认：0。
        :rtype: int
        """
        return self._PosY

    @PosY.setter
    def PosY(self, PosY):
        self._PosY = PosY

    @property
    def Width(self):
        """水印宽度，单位像素，默认：0。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """水印高度，单位像素，默认：0。
注意：对于宽高符合以下规则：
1、Width>0 且 Height>0，按指定宽高拉伸；
2、Width=0 且 Height>0，以Height为基准等比缩放；
3、Width>0 且 Height=0，以Width为基准等比缩放；
4、Width=0 且 Height=0，采用源的宽高。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def PosOriginType(self):
        """指定坐标原点，可选值：
<li>LeftTop：PosXY 表示水印左上点到图片左上点的相对位置</li>
<li>RightTop：PosXY 表示水印右上点到图片右上点的相对位置</li>
<li>LeftBottom：PosXY 表示水印左下点到图片左下点的相对位置</li>
<li>RightBottom：PosXY 表示水印右下点到图片右下点的相对位置</li>
<li>Center：PosXY 表示水印中心点到图片中心点的相对位置</li>
默认：LeftTop。
        :rtype: str
        """
        return self._PosOriginType

    @PosOriginType.setter
    def PosOriginType(self, PosOriginType):
        self._PosOriginType = PosOriginType


    def _deserialize(self, params):
        self._SourceId = params.get("SourceId")
        self._PosX = params.get("PosX")
        self._PosY = params.get("PosY")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._PosOriginType = params.get("PosOriginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCuttingWatermarkText(AbstractModel):
    """媒体剪切文字水印参数。

    """

    def __init__(self):
        r"""
        :param _Text: 水印文字。
        :type Text: str
        :param _FontSize: 文字大小
        :type FontSize: int
        :param _PosX: 水印水平坐标，单位像素，默认：0。
        :type PosX: int
        :param _PosY: 水印垂直坐标，单位像素，默认：0。
        :type PosY: int
        :param _FontColor: 文字颜色，格式为：#RRGGBBAA，默认值：#000000。
        :type FontColor: str
        :param _FontAlpha: 文字透明度，范围：0~100，默认值：100。
        :type FontAlpha: int
        :param _PosOriginType: 指定坐标原点，可选值：
<li>LeftTop：PosXY 表示水印左上点到图片左上点的相对位置</li>
<li>RightTop：PosXY 表示水印右上点到图片右上点的相对位置</li>
<li>LeftBottom：PosXY 表示水印左下点到图片左下点的相对位置</li>
<li>RightBottom：PosXY 表示水印右下点到图片右下点的相对位置</li>
<li>Center：PosXY 表示水印中心点到图片中心点的相对位置</li>
默认：LeftTop。
        :type PosOriginType: str
        :param _Font: 字体，可选值：
<li>SimHei</li>
<li>SimKai</li>
<li>Arial</li>
默认 SimHei。
        :type Font: str
        """
        self._Text = None
        self._FontSize = None
        self._PosX = None
        self._PosY = None
        self._FontColor = None
        self._FontAlpha = None
        self._PosOriginType = None
        self._Font = None

    @property
    def Text(self):
        """水印文字。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def FontSize(self):
        """文字大小
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def PosX(self):
        """水印水平坐标，单位像素，默认：0。
        :rtype: int
        """
        return self._PosX

    @PosX.setter
    def PosX(self, PosX):
        self._PosX = PosX

    @property
    def PosY(self):
        """水印垂直坐标，单位像素，默认：0。
        :rtype: int
        """
        return self._PosY

    @PosY.setter
    def PosY(self, PosY):
        self._PosY = PosY

    @property
    def FontColor(self):
        """文字颜色，格式为：#RRGGBBAA，默认值：#000000。
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def FontAlpha(self):
        """文字透明度，范围：0~100，默认值：100。
        :rtype: int
        """
        return self._FontAlpha

    @FontAlpha.setter
    def FontAlpha(self, FontAlpha):
        self._FontAlpha = FontAlpha

    @property
    def PosOriginType(self):
        """指定坐标原点，可选值：
<li>LeftTop：PosXY 表示水印左上点到图片左上点的相对位置</li>
<li>RightTop：PosXY 表示水印右上点到图片右上点的相对位置</li>
<li>LeftBottom：PosXY 表示水印左下点到图片左下点的相对位置</li>
<li>RightBottom：PosXY 表示水印右下点到图片右下点的相对位置</li>
<li>Center：PosXY 表示水印中心点到图片中心点的相对位置</li>
默认：LeftTop。
        :rtype: str
        """
        return self._PosOriginType

    @PosOriginType.setter
    def PosOriginType(self, PosOriginType):
        self._PosOriginType = PosOriginType

    @property
    def Font(self):
        """字体，可选值：
<li>SimHei</li>
<li>SimKai</li>
<li>Arial</li>
默认 SimHei。
        :rtype: str
        """
        return self._Font

    @Font.setter
    def Font(self, Font):
        self._Font = Font


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._FontSize = params.get("FontSize")
        self._PosX = params.get("PosX")
        self._PosY = params.get("PosY")
        self._FontColor = params.get("FontColor")
        self._FontAlpha = params.get("FontAlpha")
        self._PosOriginType = params.get("PosOriginType")
        self._Font = params.get("Font")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaJoiningInfo(AbstractModel):
    """编辑处理/拼接任务信息

    """

    def __init__(self):
        r"""
        :param _TargetInfo: 输出目标信息，拼接只采用FileName和Format，用于指定目标文件名和格式。
其中Format只支持mp4.
        :type TargetInfo: :class:`tencentcloud.ie.v20200304.models.MediaTargetInfo`
        :param _Mode: 拼接模式：
Fast：快速；
Normal：正常；
        :type Mode: str
        """
        self._TargetInfo = None
        self._Mode = None

    @property
    def TargetInfo(self):
        """输出目标信息，拼接只采用FileName和Format，用于指定目标文件名和格式。
其中Format只支持mp4.
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaTargetInfo`
        """
        return self._TargetInfo

    @TargetInfo.setter
    def TargetInfo(self, TargetInfo):
        self._TargetInfo = TargetInfo

    @property
    def Mode(self):
        """拼接模式：
Fast：快速；
Normal：正常；
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        if params.get("TargetInfo") is not None:
            self._TargetInfo = MediaTargetInfo()
            self._TargetInfo._deserialize(params.get("TargetInfo"))
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaJoiningTaskResult(AbstractModel):
    """编辑处理/拼接任务/处理结果

    """

    def __init__(self):
        r"""
        :param _File: 拼接结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type File: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        """
        self._File = None

    @property
    def File(self):
        """拼接结果文件。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.TaskResultFile`
        """
        return self._File

    @File.setter
    def File(self, File):
        self._File = File


    def _deserialize(self, params):
        if params.get("File") is not None:
            self._File = TaskResultFile()
            self._File._deserialize(params.get("File"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessInfo(AbstractModel):
    """编辑处理/任务信息

    """

    def __init__(self):
        r"""
        :param _Type: 编辑处理任务类型，可选值：
MediaEditing：媒体编辑（待上线）；
MediaCutting：媒体剪切；
MediaJoining：媒体拼接。
MediaRecognition: 媒体识别。
        :type Type: str
        :param _MediaCuttingInfo: 视频剪切任务参数，Type=MediaCutting时必选。
        :type MediaCuttingInfo: :class:`tencentcloud.ie.v20200304.models.MediaCuttingInfo`
        :param _MediaJoiningInfo: 视频拼接任务参数，Type=MediaJoining时必选。
        :type MediaJoiningInfo: :class:`tencentcloud.ie.v20200304.models.MediaJoiningInfo`
        :param _MediaRecognitionInfo: 媒体识别任务参数，Type=MediaRecognition时必选
        :type MediaRecognitionInfo: :class:`tencentcloud.ie.v20200304.models.MediaRecognitionInfo`
        """
        self._Type = None
        self._MediaCuttingInfo = None
        self._MediaJoiningInfo = None
        self._MediaRecognitionInfo = None

    @property
    def Type(self):
        """编辑处理任务类型，可选值：
MediaEditing：媒体编辑（待上线）；
MediaCutting：媒体剪切；
MediaJoining：媒体拼接。
MediaRecognition: 媒体识别。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MediaCuttingInfo(self):
        """视频剪切任务参数，Type=MediaCutting时必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaCuttingInfo`
        """
        return self._MediaCuttingInfo

    @MediaCuttingInfo.setter
    def MediaCuttingInfo(self, MediaCuttingInfo):
        self._MediaCuttingInfo = MediaCuttingInfo

    @property
    def MediaJoiningInfo(self):
        """视频拼接任务参数，Type=MediaJoining时必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaJoiningInfo`
        """
        return self._MediaJoiningInfo

    @MediaJoiningInfo.setter
    def MediaJoiningInfo(self, MediaJoiningInfo):
        self._MediaJoiningInfo = MediaJoiningInfo

    @property
    def MediaRecognitionInfo(self):
        """媒体识别任务参数，Type=MediaRecognition时必选
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaRecognitionInfo`
        """
        return self._MediaRecognitionInfo

    @MediaRecognitionInfo.setter
    def MediaRecognitionInfo(self, MediaRecognitionInfo):
        self._MediaRecognitionInfo = MediaRecognitionInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("MediaCuttingInfo") is not None:
            self._MediaCuttingInfo = MediaCuttingInfo()
            self._MediaCuttingInfo._deserialize(params.get("MediaCuttingInfo"))
        if params.get("MediaJoiningInfo") is not None:
            self._MediaJoiningInfo = MediaJoiningInfo()
            self._MediaJoiningInfo._deserialize(params.get("MediaJoiningInfo"))
        if params.get("MediaRecognitionInfo") is not None:
            self._MediaRecognitionInfo = MediaRecognitionInfo()
            self._MediaRecognitionInfo._deserialize(params.get("MediaRecognitionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskResult(AbstractModel):
    """编辑处理/任务处理结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 编辑处理任务ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _Type: 编辑处理任务类型，取值：
MediaEditing：视频编辑（待上线）；
MediaCutting：视频剪切；
MediaJoining：视频拼接。
MediaRecognition：媒体识别；
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Progress: 处理进度，范围：[0,100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _Status: 任务状态：
1100：等待中；
1200：执行中；
2000：成功；
5000：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ErrCode: 任务错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param _ErrMsg: 任务错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _MediaCuttingTaskResult: 剪切任务处理结果，当Type=MediaCutting时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaCuttingTaskResult: :class:`tencentcloud.ie.v20200304.models.MediaCuttingTaskResult`
        :param _MediaJoiningTaskResult: 拼接任务处理结果，当Type=MediaJoining时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaJoiningTaskResult: :class:`tencentcloud.ie.v20200304.models.MediaJoiningTaskResult`
        :param _MediaRecognitionTaskResult: 媒体识别任务处理结果，当Type=MediaRecognition时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaRecognitionTaskResult: :class:`tencentcloud.ie.v20200304.models.MediaRecognitionTaskResult`
        """
        self._TaskId = None
        self._Type = None
        self._Progress = None
        self._Status = None
        self._ErrCode = None
        self._ErrMsg = None
        self._MediaCuttingTaskResult = None
        self._MediaJoiningTaskResult = None
        self._MediaRecognitionTaskResult = None

    @property
    def TaskId(self):
        """编辑处理任务ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Type(self):
        """编辑处理任务类型，取值：
MediaEditing：视频编辑（待上线）；
MediaCutting：视频剪切；
MediaJoining：视频拼接。
MediaRecognition：媒体识别；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Progress(self):
        """处理进度，范围：[0,100]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Status(self):
        """任务状态：
1100：等待中；
1200：执行中；
2000：成功；
5000：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """任务错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """任务错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def MediaCuttingTaskResult(self):
        """剪切任务处理结果，当Type=MediaCutting时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaCuttingTaskResult`
        """
        return self._MediaCuttingTaskResult

    @MediaCuttingTaskResult.setter
    def MediaCuttingTaskResult(self, MediaCuttingTaskResult):
        self._MediaCuttingTaskResult = MediaCuttingTaskResult

    @property
    def MediaJoiningTaskResult(self):
        """拼接任务处理结果，当Type=MediaJoining时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaJoiningTaskResult`
        """
        return self._MediaJoiningTaskResult

    @MediaJoiningTaskResult.setter
    def MediaJoiningTaskResult(self, MediaJoiningTaskResult):
        self._MediaJoiningTaskResult = MediaJoiningTaskResult

    @property
    def MediaRecognitionTaskResult(self):
        """媒体识别任务处理结果，当Type=MediaRecognition时才有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaRecognitionTaskResult`
        """
        return self._MediaRecognitionTaskResult

    @MediaRecognitionTaskResult.setter
    def MediaRecognitionTaskResult(self, MediaRecognitionTaskResult):
        self._MediaRecognitionTaskResult = MediaRecognitionTaskResult


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Type = params.get("Type")
        self._Progress = params.get("Progress")
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("MediaCuttingTaskResult") is not None:
            self._MediaCuttingTaskResult = MediaCuttingTaskResult()
            self._MediaCuttingTaskResult._deserialize(params.get("MediaCuttingTaskResult"))
        if params.get("MediaJoiningTaskResult") is not None:
            self._MediaJoiningTaskResult = MediaJoiningTaskResult()
            self._MediaJoiningTaskResult._deserialize(params.get("MediaJoiningTaskResult"))
        if params.get("MediaRecognitionTaskResult") is not None:
            self._MediaRecognitionTaskResult = MediaRecognitionTaskResult()
            self._MediaRecognitionTaskResult._deserialize(params.get("MediaRecognitionTaskResult"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaQualityRestorationTaskResult(AbstractModel):
    """画质重生任务结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 画质重生任务ID
        :type TaskId: str
        :param _SubTaskResult: 画质重生处理后文件的详细信息。
        :type SubTaskResult: list of SubTaskResultItem
        """
        self._TaskId = None
        self._SubTaskResult = None

    @property
    def TaskId(self):
        """画质重生任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SubTaskResult(self):
        """画质重生处理后文件的详细信息。
        :rtype: list of SubTaskResultItem
        """
        return self._SubTaskResult

    @SubTaskResult.setter
    def SubTaskResult(self, SubTaskResult):
        self._SubTaskResult = SubTaskResult


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("SubTaskResult") is not None:
            self._SubTaskResult = []
            for item in params.get("SubTaskResult"):
                obj = SubTaskResultItem()
                obj._deserialize(item)
                self._SubTaskResult.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaRecognitionInfo(AbstractModel):
    """媒体识别任务参数

    """

    def __init__(self):
        r"""
        :param _FrameTagRec: 帧标签识别
        :type FrameTagRec: :class:`tencentcloud.ie.v20200304.models.FrameTagRec`
        :param _SubtitleRec: 语音字幕识别
        :type SubtitleRec: :class:`tencentcloud.ie.v20200304.models.SubtitleRec`
        """
        self._FrameTagRec = None
        self._SubtitleRec = None

    @property
    def FrameTagRec(self):
        """帧标签识别
        :rtype: :class:`tencentcloud.ie.v20200304.models.FrameTagRec`
        """
        return self._FrameTagRec

    @FrameTagRec.setter
    def FrameTagRec(self, FrameTagRec):
        self._FrameTagRec = FrameTagRec

    @property
    def SubtitleRec(self):
        """语音字幕识别
        :rtype: :class:`tencentcloud.ie.v20200304.models.SubtitleRec`
        """
        return self._SubtitleRec

    @SubtitleRec.setter
    def SubtitleRec(self, SubtitleRec):
        self._SubtitleRec = SubtitleRec


    def _deserialize(self, params):
        if params.get("FrameTagRec") is not None:
            self._FrameTagRec = FrameTagRec()
            self._FrameTagRec._deserialize(params.get("FrameTagRec"))
        if params.get("SubtitleRec") is not None:
            self._SubtitleRec = SubtitleRec()
            self._SubtitleRec._deserialize(params.get("SubtitleRec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaRecognitionTaskResult(AbstractModel):
    """媒体识别任务处理结果

    """

    def __init__(self):
        r"""
        :param _FrameTagResults: 帧标签识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagResults: :class:`tencentcloud.ie.v20200304.models.FrameTagResult`
        :param _SubtitleResults: 语音字幕识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SubtitleResults: :class:`tencentcloud.ie.v20200304.models.SubtitleResult`
        """
        self._FrameTagResults = None
        self._SubtitleResults = None

    @property
    def FrameTagResults(self):
        """帧标签识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.FrameTagResult`
        """
        return self._FrameTagResults

    @FrameTagResults.setter
    def FrameTagResults(self, FrameTagResults):
        self._FrameTagResults = FrameTagResults

    @property
    def SubtitleResults(self):
        """语音字幕识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.SubtitleResult`
        """
        return self._SubtitleResults

    @SubtitleResults.setter
    def SubtitleResults(self, SubtitleResults):
        self._SubtitleResults = SubtitleResults


    def _deserialize(self, params):
        if params.get("FrameTagResults") is not None:
            self._FrameTagResults = FrameTagResult()
            self._FrameTagResults._deserialize(params.get("FrameTagResults"))
        if params.get("SubtitleResults") is not None:
            self._SubtitleResults = SubtitleResult()
            self._SubtitleResults._deserialize(params.get("SubtitleResults"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaResultInfo(AbstractModel):
    """结果文件媒体信息

    """

    def __init__(self):
        r"""
        :param _Duration: 媒体时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _ResultVideoInfoSet: 视频流信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultVideoInfoSet: list of ResultVideoInfo
        :param _ResultAudioInfoSet: 音频流信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultAudioInfoSet: list of ResultAudioInfo
        """
        self._Duration = None
        self._ResultVideoInfoSet = None
        self._ResultAudioInfoSet = None

    @property
    def Duration(self):
        """媒体时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ResultVideoInfoSet(self):
        """视频流信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResultVideoInfo
        """
        return self._ResultVideoInfoSet

    @ResultVideoInfoSet.setter
    def ResultVideoInfoSet(self, ResultVideoInfoSet):
        self._ResultVideoInfoSet = ResultVideoInfoSet

    @property
    def ResultAudioInfoSet(self):
        """音频流信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResultAudioInfo
        """
        return self._ResultAudioInfoSet

    @ResultAudioInfoSet.setter
    def ResultAudioInfoSet(self, ResultAudioInfoSet):
        self._ResultAudioInfoSet = ResultAudioInfoSet


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        if params.get("ResultVideoInfoSet") is not None:
            self._ResultVideoInfoSet = []
            for item in params.get("ResultVideoInfoSet"):
                obj = ResultVideoInfo()
                obj._deserialize(item)
                self._ResultVideoInfoSet.append(obj)
        if params.get("ResultAudioInfoSet") is not None:
            self._ResultAudioInfoSet = []
            for item in params.get("ResultAudioInfoSet"):
                obj = ResultAudioInfo()
                obj._deserialize(item)
                self._ResultAudioInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSourceInfo(AbstractModel):
    """编辑处理的媒体源

    """

    def __init__(self):
        r"""
        :param _DownInfo: 媒体源资源下载信息。
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param _Id: 媒体源ID标记，用于多个输入源时，请内媒体源的定位，对于多输入的任务，一般要求必选。
ID只能包含字母、数字、下划线、中划线，长读不能超过128。
        :type Id: str
        :param _Type: 媒体源类型，具体类型如下：
Video：视频
Image：图片
Audio：音频
        :type Type: str
        """
        self._DownInfo = None
        self._Id = None
        self._Type = None

    @property
    def DownInfo(self):
        """媒体源资源下载信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        """
        return self._DownInfo

    @DownInfo.setter
    def DownInfo(self, DownInfo):
        self._DownInfo = DownInfo

    @property
    def Id(self):
        """媒体源ID标记，用于多个输入源时，请内媒体源的定位，对于多输入的任务，一般要求必选。
ID只能包含字母、数字、下划线、中划线，长读不能超过128。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """媒体源类型，具体类型如下：
Video：视频
Image：图片
Audio：音频
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("DownInfo") is not None:
            self._DownInfo = DownInfo()
            self._DownInfo._deserialize(params.get("DownInfo"))
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTargetInfo(AbstractModel):
    """目标媒体信息。

    """

    def __init__(self):
        r"""
        :param _FileName: 目标文件名，不能带特殊字符（如/等），无需后缀名，最长200字符。

注1：部分子服务支持占位符，形式为： {parameter}
预设parameter有：
index：序号；
        :type FileName: str
        :param _Format: 媒体封装格式，最长5字符，具体格式支持根据子任务确定。
        :type Format: str
        :param _TargetVideoInfo: 视频流信息。
        :type TargetVideoInfo: :class:`tencentcloud.ie.v20200304.models.TargetVideoInfo`
        :param _ResultListSaveType: 【不再使用】
        :type ResultListSaveType: str
        """
        self._FileName = None
        self._Format = None
        self._TargetVideoInfo = None
        self._ResultListSaveType = None

    @property
    def FileName(self):
        """目标文件名，不能带特殊字符（如/等），无需后缀名，最长200字符。

注1：部分子服务支持占位符，形式为： {parameter}
预设parameter有：
index：序号；
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Format(self):
        """媒体封装格式，最长5字符，具体格式支持根据子任务确定。
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def TargetVideoInfo(self):
        """视频流信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.TargetVideoInfo`
        """
        return self._TargetVideoInfo

    @TargetVideoInfo.setter
    def TargetVideoInfo(self, TargetVideoInfo):
        self._TargetVideoInfo = TargetVideoInfo

    @property
    def ResultListSaveType(self):
        """【不再使用】
        :rtype: str
        """
        return self._ResultListSaveType

    @ResultListSaveType.setter
    def ResultListSaveType(self, ResultListSaveType):
        self._ResultListSaveType = ResultListSaveType


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._Format = params.get("Format")
        if params.get("TargetVideoInfo") is not None:
            self._TargetVideoInfo = TargetVideoInfo()
            self._TargetVideoInfo._deserialize(params.get("TargetVideoInfo"))
        self._ResultListSaveType = params.get("ResultListSaveType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MuxInfo(AbstractModel):
    """流封装信息

    """

    def __init__(self):
        r"""
        :param _DeleteStream: 删除流，可选项：video,audio。
        :type DeleteStream: str
        :param _FlvFlags: Flv 参数，目前支持add_keyframe_index
        :type FlvFlags: str
        """
        self._DeleteStream = None
        self._FlvFlags = None

    @property
    def DeleteStream(self):
        """删除流，可选项：video,audio。
        :rtype: str
        """
        return self._DeleteStream

    @DeleteStream.setter
    def DeleteStream(self, DeleteStream):
        self._DeleteStream = DeleteStream

    @property
    def FlvFlags(self):
        """Flv 参数，目前支持add_keyframe_index
        :rtype: str
        """
        return self._FlvFlags

    @FlvFlags.setter
    def FlvFlags(self, FlvFlags):
        self._FlvFlags = FlvFlags


    def _deserialize(self, params):
        self._DeleteStream = params.get("DeleteStream")
        self._FlvFlags = params.get("FlvFlags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpeningEndingEditingInfo(AbstractModel):
    """片头片尾识别任务参数信息

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启片头片尾识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param _CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self._Switch = None
        self._CustomInfo = None

    @property
    def Switch(self):
        """是否开启片头片尾识别。0为关闭，1为开启。其他非0非1值默认为0。
        :rtype: int
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CustomInfo(self):
        """额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :rtype: str
        """
        return self._CustomInfo

    @CustomInfo.setter
    def CustomInfo(self, CustomInfo):
        self._CustomInfo = CustomInfo


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpeningEndingTaskResult(AbstractModel):
    """片头片尾识别结果信息

    """

    def __init__(self):
        r"""
        :param _Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param _ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param _ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param _Item: 片头片尾识别结果项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: :class:`tencentcloud.ie.v20200304.models.OpeningEndingTaskResultItem`
        """
        self._Status = None
        self._ErrCode = None
        self._ErrMsg = None
        self._Item = None

    @property
    def Status(self):
        """编辑任务状态。 
1：执行中；2：成功；3：失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """编辑任务失败错误码。 
0：成功；其他值：失败。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """编辑任务失败错误描述。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Item(self):
        """片头片尾识别结果项。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.OpeningEndingTaskResultItem`
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("Item") is not None:
            self._Item = OpeningEndingTaskResultItem()
            self._Item._deserialize(params.get("Item"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpeningEndingTaskResultItem(AbstractModel):
    """片头片尾识别结果项

    """

    def __init__(self):
        r"""
        :param _OpeningTimeOffset: 视频片头的结束时间点，单位：秒。
        :type OpeningTimeOffset: float
        :param _OpeningConfidence: 片头识别置信度，取值范围是 0 到 100。
        :type OpeningConfidence: float
        :param _EndingTimeOffset: 视频片尾的开始时间点，单位：秒。
        :type EndingTimeOffset: float
        :param _EndingConfidence: 片尾识别置信度，取值范围是 0 到 100。
        :type EndingConfidence: float
        """
        self._OpeningTimeOffset = None
        self._OpeningConfidence = None
        self._EndingTimeOffset = None
        self._EndingConfidence = None

    @property
    def OpeningTimeOffset(self):
        """视频片头的结束时间点，单位：秒。
        :rtype: float
        """
        return self._OpeningTimeOffset

    @OpeningTimeOffset.setter
    def OpeningTimeOffset(self, OpeningTimeOffset):
        self._OpeningTimeOffset = OpeningTimeOffset

    @property
    def OpeningConfidence(self):
        """片头识别置信度，取值范围是 0 到 100。
        :rtype: float
        """
        return self._OpeningConfidence

    @OpeningConfidence.setter
    def OpeningConfidence(self, OpeningConfidence):
        self._OpeningConfidence = OpeningConfidence

    @property
    def EndingTimeOffset(self):
        """视频片尾的开始时间点，单位：秒。
        :rtype: float
        """
        return self._EndingTimeOffset

    @EndingTimeOffset.setter
    def EndingTimeOffset(self, EndingTimeOffset):
        self._EndingTimeOffset = EndingTimeOffset

    @property
    def EndingConfidence(self):
        """片尾识别置信度，取值范围是 0 到 100。
        :rtype: float
        """
        return self._EndingConfidence

    @EndingConfidence.setter
    def EndingConfidence(self, EndingConfidence):
        self._EndingConfidence = EndingConfidence


    def _deserialize(self, params):
        self._OpeningTimeOffset = params.get("OpeningTimeOffset")
        self._OpeningConfidence = params.get("OpeningConfidence")
        self._EndingTimeOffset = params.get("EndingTimeOffset")
        self._EndingConfidence = params.get("EndingConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PicMarkInfoItem(AbstractModel):
    """图片水印信息

    """

    def __init__(self):
        r"""
        :param _PosX: 图片水印的X坐标。
        :type PosX: int
        :param _PosY: 图片水印的Y坐标 。
        :type PosY: int
        :param _Path: 图片水印路径,，如果不从Cos拉取水印，则必填
        :type Path: str
        :param _CosInfo: 图片水印的Cos 信息，从Cos上拉取图片水印时必填。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        :param _Width: 图片水印宽度，不填为图片原始宽度。
        :type Width: int
        :param _Height: 图片水印高度，不填为图片原始高度。
        :type Height: int
        :param _StartTime: 添加图片水印的开始时间,单位：ms。
        :type StartTime: int
        :param _EndTime: 添加图片水印的结束时间,单位：ms。
        :type EndTime: int
        """
        self._PosX = None
        self._PosY = None
        self._Path = None
        self._CosInfo = None
        self._Width = None
        self._Height = None
        self._StartTime = None
        self._EndTime = None

    @property
    def PosX(self):
        """图片水印的X坐标。
        :rtype: int
        """
        return self._PosX

    @PosX.setter
    def PosX(self, PosX):
        self._PosX = PosX

    @property
    def PosY(self):
        """图片水印的Y坐标 。
        :rtype: int
        """
        return self._PosY

    @PosY.setter
    def PosY(self, PosY):
        self._PosY = PosY

    @property
    def Path(self):
        """图片水印路径,，如果不从Cos拉取水印，则必填
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def CosInfo(self):
        """图片水印的Cos 信息，从Cos上拉取图片水印时必填。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        return self._CosInfo

    @CosInfo.setter
    def CosInfo(self, CosInfo):
        self._CosInfo = CosInfo

    @property
    def Width(self):
        """图片水印宽度，不填为图片原始宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """图片水印高度，不填为图片原始高度。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def StartTime(self):
        """添加图片水印的开始时间,单位：ms。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """添加图片水印的结束时间,单位：ms。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._PosX = params.get("PosX")
        self._PosY = params.get("PosY")
        self._Path = params.get("Path")
        if params.get("CosInfo") is not None:
            self._CosInfo = CosInfo()
            self._CosInfo._deserialize(params.get("CosInfo"))
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityControlInfo(AbstractModel):
    """媒体质检任务参数信息

    """

    def __init__(self):
        r"""
        :param _Interval: 对流进行截图的间隔ms，默认1000ms
        :type Interval: int
        :param _VideoShot: 是否保存截图
        :type VideoShot: bool
        :param _Jitter: 是否检测抖动重影
        :type Jitter: bool
        :param _Blur: 是否检测模糊
        :type Blur: bool
        :param _AbnormalLighting: 是否检测低光照、过曝
        :type AbnormalLighting: bool
        :param _CrashScreen: 是否检测花屏
        :type CrashScreen: bool
        :param _BlackWhiteEdge: 是否检测黑边、白边、黑屏、白屏、绿屏
        :type BlackWhiteEdge: bool
        :param _Noise: 是否检测噪点
        :type Noise: bool
        :param _Mosaic: 是否检测马赛克
        :type Mosaic: bool
        :param _QRCode: 是否检测二维码，包括小程序码、条形码
        :type QRCode: bool
        :param _QualityEvaluation: 是否开启画面质量评价
        :type QualityEvaluation: bool
        :param _QualityEvalScore: 画面质量评价过滤阈值，结果只返回低于阈值的时间段，默认60
        :type QualityEvalScore: int
        :param _Voice: 是否检测视频音频，包含静音、低音、爆音
        :type Voice: bool
        """
        self._Interval = None
        self._VideoShot = None
        self._Jitter = None
        self._Blur = None
        self._AbnormalLighting = None
        self._CrashScreen = None
        self._BlackWhiteEdge = None
        self._Noise = None
        self._Mosaic = None
        self._QRCode = None
        self._QualityEvaluation = None
        self._QualityEvalScore = None
        self._Voice = None

    @property
    def Interval(self):
        """对流进行截图的间隔ms，默认1000ms
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def VideoShot(self):
        """是否保存截图
        :rtype: bool
        """
        return self._VideoShot

    @VideoShot.setter
    def VideoShot(self, VideoShot):
        self._VideoShot = VideoShot

    @property
    def Jitter(self):
        """是否检测抖动重影
        :rtype: bool
        """
        return self._Jitter

    @Jitter.setter
    def Jitter(self, Jitter):
        self._Jitter = Jitter

    @property
    def Blur(self):
        """是否检测模糊
        :rtype: bool
        """
        return self._Blur

    @Blur.setter
    def Blur(self, Blur):
        self._Blur = Blur

    @property
    def AbnormalLighting(self):
        """是否检测低光照、过曝
        :rtype: bool
        """
        return self._AbnormalLighting

    @AbnormalLighting.setter
    def AbnormalLighting(self, AbnormalLighting):
        self._AbnormalLighting = AbnormalLighting

    @property
    def CrashScreen(self):
        """是否检测花屏
        :rtype: bool
        """
        return self._CrashScreen

    @CrashScreen.setter
    def CrashScreen(self, CrashScreen):
        self._CrashScreen = CrashScreen

    @property
    def BlackWhiteEdge(self):
        """是否检测黑边、白边、黑屏、白屏、绿屏
        :rtype: bool
        """
        return self._BlackWhiteEdge

    @BlackWhiteEdge.setter
    def BlackWhiteEdge(self, BlackWhiteEdge):
        self._BlackWhiteEdge = BlackWhiteEdge

    @property
    def Noise(self):
        """是否检测噪点
        :rtype: bool
        """
        return self._Noise

    @Noise.setter
    def Noise(self, Noise):
        self._Noise = Noise

    @property
    def Mosaic(self):
        """是否检测马赛克
        :rtype: bool
        """
        return self._Mosaic

    @Mosaic.setter
    def Mosaic(self, Mosaic):
        self._Mosaic = Mosaic

    @property
    def QRCode(self):
        """是否检测二维码，包括小程序码、条形码
        :rtype: bool
        """
        return self._QRCode

    @QRCode.setter
    def QRCode(self, QRCode):
        self._QRCode = QRCode

    @property
    def QualityEvaluation(self):
        """是否开启画面质量评价
        :rtype: bool
        """
        return self._QualityEvaluation

    @QualityEvaluation.setter
    def QualityEvaluation(self, QualityEvaluation):
        self._QualityEvaluation = QualityEvaluation

    @property
    def QualityEvalScore(self):
        """画面质量评价过滤阈值，结果只返回低于阈值的时间段，默认60
        :rtype: int
        """
        return self._QualityEvalScore

    @QualityEvalScore.setter
    def QualityEvalScore(self, QualityEvalScore):
        self._QualityEvalScore = QualityEvalScore

    @property
    def Voice(self):
        """是否检测视频音频，包含静音、低音、爆音
        :rtype: bool
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        self._VideoShot = params.get("VideoShot")
        self._Jitter = params.get("Jitter")
        self._Blur = params.get("Blur")
        self._AbnormalLighting = params.get("AbnormalLighting")
        self._CrashScreen = params.get("CrashScreen")
        self._BlackWhiteEdge = params.get("BlackWhiteEdge")
        self._Noise = params.get("Noise")
        self._Mosaic = params.get("Mosaic")
        self._QRCode = params.get("QRCode")
        self._QualityEvaluation = params.get("QualityEvaluation")
        self._QualityEvalScore = params.get("QualityEvalScore")
        self._Voice = params.get("Voice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityControlInfoTaskResult(AbstractModel):
    """媒体质检结果信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 质检任务 ID
        :type TaskId: str
        :param _Status: 质检任务状态。
1：执行中；2：成功；3：失败
        :type Status: int
        :param _Progress: 表示处理进度百分比
        :type Progress: int
        :param _UsedTime: 处理时长(s)
        :type UsedTime: int
        :param _Duration: 计费时长(s)
        :type Duration: int
        :param _NoAudio: 为true时表示视频无音频轨
注意：此字段可能返回 null，表示取不到有效值。
        :type NoAudio: bool
        :param _NoVideo: 为true时表示视频无视频轨
注意：此字段可能返回 null，表示取不到有效值。
        :type NoVideo: bool
        :param _QualityEvaluationScore: 视频无参考质量打分，百分制
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityEvaluationScore: int
        :param _QualityEvaluationResults: 视频画面无参考评分低于阈值的时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityEvaluationResults: list of QualityControlResultItems
        :param _JitterResults: 视频画面抖动时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type JitterResults: list of QualityControlResultItems
        :param _BlurResults: 视频画面模糊时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type BlurResults: list of QualityControlResultItems
        :param _AbnormalLightingResults: 视频画面低光、过曝时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type AbnormalLightingResults: list of QualityControlResultItems
        :param _CrashScreenResults: 视频画面花屏时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type CrashScreenResults: list of QualityControlResultItems
        :param _BlackWhiteEdgeResults: 视频画面黑边、白边、黑屏、白屏、纯色屏时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackWhiteEdgeResults: list of QualityControlResultItems
        :param _NoiseResults: 视频画面有噪点时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type NoiseResults: list of QualityControlResultItems
        :param _MosaicResults: 视频画面有马赛克时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type MosaicResults: list of QualityControlResultItems
        :param _QRCodeResults: 视频画面有二维码的时间段，包括小程序码、条形码
注意：此字段可能返回 null，表示取不到有效值。
        :type QRCodeResults: list of QualityControlResultItems
        :param _VoiceResults: 视频音频异常时间段，包括静音、低音、爆音
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceResults: list of QualityControlResultItems
        :param _ErrCode: 任务错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param _ErrMsg: 任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        """
        self._TaskId = None
        self._Status = None
        self._Progress = None
        self._UsedTime = None
        self._Duration = None
        self._NoAudio = None
        self._NoVideo = None
        self._QualityEvaluationScore = None
        self._QualityEvaluationResults = None
        self._JitterResults = None
        self._BlurResults = None
        self._AbnormalLightingResults = None
        self._CrashScreenResults = None
        self._BlackWhiteEdgeResults = None
        self._NoiseResults = None
        self._MosaicResults = None
        self._QRCodeResults = None
        self._VoiceResults = None
        self._ErrCode = None
        self._ErrMsg = None

    @property
    def TaskId(self):
        """质检任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """质检任务状态。
1：执行中；2：成功；3：失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        """表示处理进度百分比
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def UsedTime(self):
        """处理时长(s)
        :rtype: int
        """
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def Duration(self):
        """计费时长(s)
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def NoAudio(self):
        """为true时表示视频无音频轨
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._NoAudio

    @NoAudio.setter
    def NoAudio(self, NoAudio):
        self._NoAudio = NoAudio

    @property
    def NoVideo(self):
        """为true时表示视频无视频轨
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._NoVideo

    @NoVideo.setter
    def NoVideo(self, NoVideo):
        self._NoVideo = NoVideo

    @property
    def QualityEvaluationScore(self):
        """视频无参考质量打分，百分制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QualityEvaluationScore

    @QualityEvaluationScore.setter
    def QualityEvaluationScore(self, QualityEvaluationScore):
        self._QualityEvaluationScore = QualityEvaluationScore

    @property
    def QualityEvaluationResults(self):
        """视频画面无参考评分低于阈值的时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._QualityEvaluationResults

    @QualityEvaluationResults.setter
    def QualityEvaluationResults(self, QualityEvaluationResults):
        self._QualityEvaluationResults = QualityEvaluationResults

    @property
    def JitterResults(self):
        """视频画面抖动时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._JitterResults

    @JitterResults.setter
    def JitterResults(self, JitterResults):
        self._JitterResults = JitterResults

    @property
    def BlurResults(self):
        """视频画面模糊时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._BlurResults

    @BlurResults.setter
    def BlurResults(self, BlurResults):
        self._BlurResults = BlurResults

    @property
    def AbnormalLightingResults(self):
        """视频画面低光、过曝时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._AbnormalLightingResults

    @AbnormalLightingResults.setter
    def AbnormalLightingResults(self, AbnormalLightingResults):
        self._AbnormalLightingResults = AbnormalLightingResults

    @property
    def CrashScreenResults(self):
        """视频画面花屏时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._CrashScreenResults

    @CrashScreenResults.setter
    def CrashScreenResults(self, CrashScreenResults):
        self._CrashScreenResults = CrashScreenResults

    @property
    def BlackWhiteEdgeResults(self):
        """视频画面黑边、白边、黑屏、白屏、纯色屏时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._BlackWhiteEdgeResults

    @BlackWhiteEdgeResults.setter
    def BlackWhiteEdgeResults(self, BlackWhiteEdgeResults):
        self._BlackWhiteEdgeResults = BlackWhiteEdgeResults

    @property
    def NoiseResults(self):
        """视频画面有噪点时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._NoiseResults

    @NoiseResults.setter
    def NoiseResults(self, NoiseResults):
        self._NoiseResults = NoiseResults

    @property
    def MosaicResults(self):
        """视频画面有马赛克时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._MosaicResults

    @MosaicResults.setter
    def MosaicResults(self, MosaicResults):
        self._MosaicResults = MosaicResults

    @property
    def QRCodeResults(self):
        """视频画面有二维码的时间段，包括小程序码、条形码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._QRCodeResults

    @QRCodeResults.setter
    def QRCodeResults(self, QRCodeResults):
        self._QRCodeResults = QRCodeResults

    @property
    def VoiceResults(self):
        """视频音频异常时间段，包括静音、低音、爆音
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QualityControlResultItems
        """
        return self._VoiceResults

    @VoiceResults.setter
    def VoiceResults(self, VoiceResults):
        self._VoiceResults = VoiceResults

    @property
    def ErrCode(self):
        """任务错误码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._UsedTime = params.get("UsedTime")
        self._Duration = params.get("Duration")
        self._NoAudio = params.get("NoAudio")
        self._NoVideo = params.get("NoVideo")
        self._QualityEvaluationScore = params.get("QualityEvaluationScore")
        if params.get("QualityEvaluationResults") is not None:
            self._QualityEvaluationResults = []
            for item in params.get("QualityEvaluationResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._QualityEvaluationResults.append(obj)
        if params.get("JitterResults") is not None:
            self._JitterResults = []
            for item in params.get("JitterResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._JitterResults.append(obj)
        if params.get("BlurResults") is not None:
            self._BlurResults = []
            for item in params.get("BlurResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._BlurResults.append(obj)
        if params.get("AbnormalLightingResults") is not None:
            self._AbnormalLightingResults = []
            for item in params.get("AbnormalLightingResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._AbnormalLightingResults.append(obj)
        if params.get("CrashScreenResults") is not None:
            self._CrashScreenResults = []
            for item in params.get("CrashScreenResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._CrashScreenResults.append(obj)
        if params.get("BlackWhiteEdgeResults") is not None:
            self._BlackWhiteEdgeResults = []
            for item in params.get("BlackWhiteEdgeResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._BlackWhiteEdgeResults.append(obj)
        if params.get("NoiseResults") is not None:
            self._NoiseResults = []
            for item in params.get("NoiseResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._NoiseResults.append(obj)
        if params.get("MosaicResults") is not None:
            self._MosaicResults = []
            for item in params.get("MosaicResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._MosaicResults.append(obj)
        if params.get("QRCodeResults") is not None:
            self._QRCodeResults = []
            for item in params.get("QRCodeResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._QRCodeResults.append(obj)
        if params.get("VoiceResults") is not None:
            self._VoiceResults = []
            for item in params.get("VoiceResults"):
                obj = QualityControlResultItems()
                obj._deserialize(item)
                self._VoiceResults.append(obj)
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityControlItem(AbstractModel):
    """质检结果项

    """

    def __init__(self):
        r"""
        :param _Confidence: 置信度，取值范围是 0 到 100
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: int
        :param _StartTimeOffset: 出现的起始时间戳，秒
        :type StartTimeOffset: float
        :param _EndTimeOffset: 出现的结束时间戳，秒
        :type EndTimeOffset: float
        :param _AreaCoordsSet: 区域坐标(px)，即左上角坐标、右下角坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCoordsSet: list of int non-negative
        """
        self._Confidence = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._AreaCoordsSet = None

    @property
    def Confidence(self):
        """置信度，取值范围是 0 到 100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def StartTimeOffset(self):
        """出现的起始时间戳，秒
        :rtype: float
        """
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        """出现的结束时间戳，秒
        :rtype: float
        """
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def AreaCoordsSet(self):
        """区域坐标(px)，即左上角坐标、右下角坐标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int non-negative
        """
        return self._AreaCoordsSet

    @AreaCoordsSet.setter
    def AreaCoordsSet(self, AreaCoordsSet):
        self._AreaCoordsSet = AreaCoordsSet


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._AreaCoordsSet = params.get("AreaCoordsSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityControlResultItems(AbstractModel):
    """质检结果项数组

    """

    def __init__(self):
        r"""
        :param _Id: 异常类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _QualityControlItems: 质检结果项
        :type QualityControlItems: list of QualityControlItem
        """
        self._Id = None
        self._QualityControlItems = None

    @property
    def Id(self):
        """异常类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def QualityControlItems(self):
        """质检结果项
        :rtype: list of QualityControlItem
        """
        return self._QualityControlItems

    @QualityControlItems.setter
    def QualityControlItems(self, QualityControlItems):
        self._QualityControlItems = QualityControlItems


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("QualityControlItems") is not None:
            self._QualityControlItems = []
            for item in params.get("QualityControlItems"):
                obj = QualityControlItem()
                obj._deserialize(item)
                self._QualityControlItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveReverb(AbstractModel):
    """音频去除混响

    """

    def __init__(self):
        r"""
        :param _Type: 去混响类型，可选项：normal
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        """去混响类型，可选项：normal
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultAudioInfo(AbstractModel):
    """结果媒体文件的视频流信息

    """

    def __init__(self):
        r"""
        :param _StreamId: 流在媒体文件中的流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamId: int
        :param _Duration: 流的时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        """
        self._StreamId = None
        self._Duration = None

    @property
    def StreamId(self):
        """流在媒体文件中的流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Duration(self):
        """流的时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._StreamId = params.get("StreamId")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultVideoInfo(AbstractModel):
    """结果媒体文件的视频流信息

    """

    def __init__(self):
        r"""
        :param _StreamId: 流在媒体文件中的流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamId: int
        :param _Duration: 流的时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _Width: 画面宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 画面高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Fps: 视频帧率，如果高于原始帧率，部分服务将无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type Fps: int
        """
        self._StreamId = None
        self._Duration = None
        self._Width = None
        self._Height = None
        self._Fps = None

    @property
    def StreamId(self):
        """流在媒体文件中的流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Duration(self):
        """流的时长，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Width(self):
        """画面宽度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """画面高度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        """视频帧率，如果高于原始帧率，部分服务将无效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps


    def _deserialize(self, params):
        self._StreamId = params.get("StreamId")
        self._Duration = params.get("Duration")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveInfo(AbstractModel):
    """任务存储信息

    """

    def __init__(self):
        r"""
        :param _Type: 存储类型，可选值： 
1：CosInfo。
        :type Type: int
        :param _CosInfo: Cos形式存储信息，当Type等于1时必选。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        :param _Id: 存储信息ID标记，用于多个输出场景。部分任务支持多输出时，一般要求必选。
ID只能包含字母、数字、下划线、中划线，长读不能超过128。
        :type Id: str
        """
        self._Type = None
        self._CosInfo = None
        self._Id = None

    @property
    def Type(self):
        """存储类型，可选值： 
1：CosInfo。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CosInfo(self):
        """Cos形式存储信息，当Type等于1时必选。
        :rtype: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        return self._CosInfo

    @CosInfo.setter
    def CosInfo(self, CosInfo):
        self._CosInfo = CosInfo

    @property
    def Id(self):
        """存储信息ID标记，用于多个输出场景。部分任务支持多输出时，一般要求必选。
ID只能包含字母、数字、下划线、中划线，长读不能超过128。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("CosInfo") is not None:
            self._CosInfo = CosInfo()
            self._CosInfo._deserialize(params.get("CosInfo"))
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScratchRepair(AbstractModel):
    """去划痕参数

    """

    def __init__(self):
        r"""
        :param _Type: 去划痕方式，取值：normal。
        :type Type: str
        :param _Ratio: 去划痕强度， 可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type Ratio: float
        """
        self._Type = None
        self._Ratio = None

    @property
    def Type(self):
        """去划痕方式，取值：normal。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Ratio(self):
        """去划痕强度， 可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SectionTime(AbstractModel):
    """时间区间。

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间点，单位ms
        :type StartTime: int
        :param _Duration: 时间区间时长，单位ms
        :type Duration: int
        """
        self._StartTime = None
        self._Duration = None

    @property
    def StartTime(self):
        """开始时间点，单位ms
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        """时间区间时长，单位ms
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentInfo(AbstractModel):
    """输出文件切片信息

    """

    def __init__(self):
        r"""
        :param _FragmentTime: 每个切片平均时长，默认10s。
        :type FragmentTime: int
        :param _SegmentType: 切片类型，可选项：hls，不填时默认hls。
        :type SegmentType: str
        :param _FragmentName: 切片文件名字。注意：
1.不填切片文件名时，默认按照按照如下格式命名：m3u8文件名{order}。
2.若填了切片文件名字，则会按照如下格式命名：用户指定文件名{order}。
        :type FragmentName: str
        """
        self._FragmentTime = None
        self._SegmentType = None
        self._FragmentName = None

    @property
    def FragmentTime(self):
        """每个切片平均时长，默认10s。
        :rtype: int
        """
        return self._FragmentTime

    @FragmentTime.setter
    def FragmentTime(self, FragmentTime):
        self._FragmentTime = FragmentTime

    @property
    def SegmentType(self):
        """切片类型，可选项：hls，不填时默认hls。
        :rtype: str
        """
        return self._SegmentType

    @SegmentType.setter
    def SegmentType(self, SegmentType):
        self._SegmentType = SegmentType

    @property
    def FragmentName(self):
        """切片文件名字。注意：
1.不填切片文件名时，默认按照按照如下格式命名：m3u8文件名{order}。
2.若填了切片文件名字，则会按照如下格式命名：用户指定文件名{order}。
        :rtype: str
        """
        return self._FragmentName

    @FragmentName.setter
    def FragmentName(self, FragmentName):
        self._FragmentName = FragmentName


    def _deserialize(self, params):
        self._FragmentTime = params.get("FragmentTime")
        self._SegmentType = params.get("SegmentType")
        self._FragmentName = params.get("FragmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sharp(AbstractModel):
    """细节增强参数

    """

    def __init__(self):
        r"""
        :param _Type: 细节增强方式,取值：normal。
        :type Type: str
        :param _Ratio: 细节增强强度，可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :type Ratio: float
        """
        self._Type = None
        self._Ratio = None

    @property
    def Type(self):
        """细节增强方式,取值：normal。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Ratio(self):
        """细节增强强度，可选项：0.0-1.0。小于0.0的默认为0.0，大于1.0的默认为1.0。
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpriteImageInfo(AbstractModel):
    """雪碧图参数信息
    注意：雪碧图大图整体的宽和高都不能大于 15000 像素。

    """

    def __init__(self):
        r"""
        :param _RowCount: 表示雪碧图行数，默认：10。
        :type RowCount: int
        :param _ColumnCount: 表示雪碧图列数，默认：10。
        :type ColumnCount: int
        :param _MarginTop: 第一行元素与顶部像素距离，默认：0。
        :type MarginTop: int
        :param _MarginBottom: 最后一行元素与底部像素距离，默认：0。
        :type MarginBottom: int
        :param _MarginLeft: 最左一行元素与左边像素距离，默认：0。
        :type MarginLeft: int
        :param _MarginRight: 最右一行元素与右边像素距离，默认：0。
        :type MarginRight: int
        :param _PaddingTop: 小图与元素顶部像素距离，默认：0。
        :type PaddingTop: int
        :param _PaddingBottom: 小图与元素底部像素距离，默认：0。
        :type PaddingBottom: int
        :param _PaddingLeft: 小图与元素左边像素距离，默认：0。
        :type PaddingLeft: int
        :param _PaddingRight: 小图与元素右边像素距离，默认：0。
        :type PaddingRight: int
        :param _BackgroundColor: 背景颜色，格式：#RRGGBB，默认：#FFFFFF。
        :type BackgroundColor: str
        """
        self._RowCount = None
        self._ColumnCount = None
        self._MarginTop = None
        self._MarginBottom = None
        self._MarginLeft = None
        self._MarginRight = None
        self._PaddingTop = None
        self._PaddingBottom = None
        self._PaddingLeft = None
        self._PaddingRight = None
        self._BackgroundColor = None

    @property
    def RowCount(self):
        """表示雪碧图行数，默认：10。
        :rtype: int
        """
        return self._RowCount

    @RowCount.setter
    def RowCount(self, RowCount):
        self._RowCount = RowCount

    @property
    def ColumnCount(self):
        """表示雪碧图列数，默认：10。
        :rtype: int
        """
        return self._ColumnCount

    @ColumnCount.setter
    def ColumnCount(self, ColumnCount):
        self._ColumnCount = ColumnCount

    @property
    def MarginTop(self):
        """第一行元素与顶部像素距离，默认：0。
        :rtype: int
        """
        return self._MarginTop

    @MarginTop.setter
    def MarginTop(self, MarginTop):
        self._MarginTop = MarginTop

    @property
    def MarginBottom(self):
        """最后一行元素与底部像素距离，默认：0。
        :rtype: int
        """
        return self._MarginBottom

    @MarginBottom.setter
    def MarginBottom(self, MarginBottom):
        self._MarginBottom = MarginBottom

    @property
    def MarginLeft(self):
        """最左一行元素与左边像素距离，默认：0。
        :rtype: int
        """
        return self._MarginLeft

    @MarginLeft.setter
    def MarginLeft(self, MarginLeft):
        self._MarginLeft = MarginLeft

    @property
    def MarginRight(self):
        """最右一行元素与右边像素距离，默认：0。
        :rtype: int
        """
        return self._MarginRight

    @MarginRight.setter
    def MarginRight(self, MarginRight):
        self._MarginRight = MarginRight

    @property
    def PaddingTop(self):
        """小图与元素顶部像素距离，默认：0。
        :rtype: int
        """
        return self._PaddingTop

    @PaddingTop.setter
    def PaddingTop(self, PaddingTop):
        self._PaddingTop = PaddingTop

    @property
    def PaddingBottom(self):
        """小图与元素底部像素距离，默认：0。
        :rtype: int
        """
        return self._PaddingBottom

    @PaddingBottom.setter
    def PaddingBottom(self, PaddingBottom):
        self._PaddingBottom = PaddingBottom

    @property
    def PaddingLeft(self):
        """小图与元素左边像素距离，默认：0。
        :rtype: int
        """
        return self._PaddingLeft

    @PaddingLeft.setter
    def PaddingLeft(self, PaddingLeft):
        self._PaddingLeft = PaddingLeft

    @property
    def PaddingRight(self):
        """小图与元素右边像素距离，默认：0。
        :rtype: int
        """
        return self._PaddingRight

    @PaddingRight.setter
    def PaddingRight(self, PaddingRight):
        self._PaddingRight = PaddingRight

    @property
    def BackgroundColor(self):
        """背景颜色，格式：#RRGGBB，默认：#FFFFFF。
        :rtype: str
        """
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor


    def _deserialize(self, params):
        self._RowCount = params.get("RowCount")
        self._ColumnCount = params.get("ColumnCount")
        self._MarginTop = params.get("MarginTop")
        self._MarginBottom = params.get("MarginBottom")
        self._MarginLeft = params.get("MarginLeft")
        self._MarginRight = params.get("MarginRight")
        self._PaddingTop = params.get("PaddingTop")
        self._PaddingBottom = params.get("PaddingBottom")
        self._PaddingLeft = params.get("PaddingLeft")
        self._PaddingRight = params.get("PaddingRight")
        self._BackgroundColor = params.get("BackgroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMediaProcessTaskRequest(AbstractModel):
    """StopMediaProcessTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 编辑处理任务ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """编辑处理任务ID。
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
        


class StopMediaProcessTaskResponse(AbstractModel):
    """StopMediaProcessTask返回参数结构体

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


class StopMediaQualityRestorationTaskRequest(AbstractModel):
    """StopMediaQualityRestorationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 要删除的画质重生任务ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """要删除的画质重生任务ID。
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
        


class StopMediaQualityRestorationTaskResponse(AbstractModel):
    """StopMediaQualityRestorationTask返回参数结构体

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


class StripEditingInfo(AbstractModel):
    """智能拆条任务参数信息

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启智能拆条。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param _CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self._Switch = None
        self._CustomInfo = None

    @property
    def Switch(self):
        """是否开启智能拆条。0为关闭，1为开启。其他非0非1值默认为0。
        :rtype: int
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CustomInfo(self):
        """额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :rtype: str
        """
        return self._CustomInfo

    @CustomInfo.setter
    def CustomInfo(self, CustomInfo):
        self._CustomInfo = CustomInfo


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StripTaskResult(AbstractModel):
    """智能拆条结果信息

    """

    def __init__(self):
        r"""
        :param _Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param _ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param _ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param _ItemSet: 智能拆条结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of StripTaskResultItem
        """
        self._Status = None
        self._ErrCode = None
        self._ErrMsg = None
        self._ItemSet = None

    @property
    def Status(self):
        """编辑任务状态。 
1：执行中；2：成功；3：失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """编辑任务失败错误码。 
0：成功；其他值：失败。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """编辑任务失败错误描述。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ItemSet(self):
        """智能拆条结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StripTaskResultItem
        """
        return self._ItemSet

    @ItemSet.setter
    def ItemSet(self, ItemSet):
        self._ItemSet = ItemSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self._ItemSet = []
            for item in params.get("ItemSet"):
                obj = StripTaskResultItem()
                obj._deserialize(item)
                self._ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StripTaskResultItem(AbstractModel):
    """智能拆条结果项

    """

    def __init__(self):
        r"""
        :param _SegmentUrl: 视频拆条片段地址。
        :type SegmentUrl: str
        :param _CovImgUrl: 拆条封面图片地址。
        :type CovImgUrl: str
        :param _Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param _StartTimeOffset: 拆条片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param _EndTimeOffset: 拆条片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        """
        self._SegmentUrl = None
        self._CovImgUrl = None
        self._Confidence = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None

    @property
    def SegmentUrl(self):
        """视频拆条片段地址。
        :rtype: str
        """
        return self._SegmentUrl

    @SegmentUrl.setter
    def SegmentUrl(self, SegmentUrl):
        self._SegmentUrl = SegmentUrl

    @property
    def CovImgUrl(self):
        """拆条封面图片地址。
        :rtype: str
        """
        return self._CovImgUrl

    @CovImgUrl.setter
    def CovImgUrl(self, CovImgUrl):
        self._CovImgUrl = CovImgUrl

    @property
    def Confidence(self):
        """置信度，取值范围是 0 到 100。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def StartTimeOffset(self):
        """拆条片段起始的偏移时间，单位：秒。
        :rtype: float
        """
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        """拆条片段终止的偏移时间，单位：秒。
        :rtype: float
        """
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset


    def _deserialize(self, params):
        self._SegmentUrl = params.get("SegmentUrl")
        self._CovImgUrl = params.get("CovImgUrl")
        self._Confidence = params.get("Confidence")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubTaskResultItem(AbstractModel):
    """画质重生子任务结果

    """

    def __init__(self):
        r"""
        :param _TaskName: 子任务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _StatusCode: 子任务状态。
0：成功；
1：执行中；
其他值：失败。
        :type StatusCode: int
        :param _StatusMsg: 子任务状态描述。
        :type StatusMsg: str
        :param _ProgressRate: 子任务进度。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgressRate: int
        :param _DownloadUrl: 画质重生处理后文件的下载地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param _Md5: 画质重生处理后文件的MD5。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param _FileInfo: 画质重生处理后文件的详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfo: :class:`tencentcloud.ie.v20200304.models.FileInfo`
        """
        self._TaskName = None
        self._StatusCode = None
        self._StatusMsg = None
        self._ProgressRate = None
        self._DownloadUrl = None
        self._Md5 = None
        self._FileInfo = None

    @property
    def TaskName(self):
        """子任务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StatusCode(self):
        """子任务状态。
0：成功；
1：执行中；
其他值：失败。
        :rtype: int
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMsg(self):
        """子任务状态描述。
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def ProgressRate(self):
        """子任务进度。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProgressRate

    @ProgressRate.setter
    def ProgressRate(self, ProgressRate):
        self._ProgressRate = ProgressRate

    @property
    def DownloadUrl(self):
        """画质重生处理后文件的下载地址。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def Md5(self):
        """画质重生处理后文件的MD5。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def FileInfo(self):
        """画质重生处理后文件的详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.FileInfo`
        """
        return self._FileInfo

    @FileInfo.setter
    def FileInfo(self, FileInfo):
        self._FileInfo = FileInfo


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._StatusCode = params.get("StatusCode")
        self._StatusMsg = params.get("StatusMsg")
        self._ProgressRate = params.get("ProgressRate")
        self._DownloadUrl = params.get("DownloadUrl")
        self._Md5 = params.get("Md5")
        if params.get("FileInfo") is not None:
            self._FileInfo = FileInfo()
            self._FileInfo._deserialize(params.get("FileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubTaskTranscodeInfo(AbstractModel):
    """画质重生子任务参数信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 子任务名称。
        :type TaskName: str
        :param _TargetInfo: 目标文件信息。
        :type TargetInfo: :class:`tencentcloud.ie.v20200304.models.TargetInfo`
        :param _EditInfo: 视频剪辑信息。注意：如果填写了EditInfo，则VideoInfo和AudioInfo必填
        :type EditInfo: :class:`tencentcloud.ie.v20200304.models.EditInfo`
        :param _VideoInfo: 视频转码信息，不填保持和源文件一致。
        :type VideoInfo: :class:`tencentcloud.ie.v20200304.models.VideoInfo`
        :param _AudioInfo: 音频转码信息，不填保持和源文件一致。
        :type AudioInfo: :class:`tencentcloud.ie.v20200304.models.AudioInfo`
        :param _MuxInfo: 指定封装信息。
        :type MuxInfo: :class:`tencentcloud.ie.v20200304.models.MuxInfo`
        """
        self._TaskName = None
        self._TargetInfo = None
        self._EditInfo = None
        self._VideoInfo = None
        self._AudioInfo = None
        self._MuxInfo = None

    @property
    def TaskName(self):
        """子任务名称。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TargetInfo(self):
        """目标文件信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.TargetInfo`
        """
        return self._TargetInfo

    @TargetInfo.setter
    def TargetInfo(self, TargetInfo):
        self._TargetInfo = TargetInfo

    @property
    def EditInfo(self):
        """视频剪辑信息。注意：如果填写了EditInfo，则VideoInfo和AudioInfo必填
        :rtype: :class:`tencentcloud.ie.v20200304.models.EditInfo`
        """
        return self._EditInfo

    @EditInfo.setter
    def EditInfo(self, EditInfo):
        self._EditInfo = EditInfo

    @property
    def VideoInfo(self):
        """视频转码信息，不填保持和源文件一致。
        :rtype: :class:`tencentcloud.ie.v20200304.models.VideoInfo`
        """
        return self._VideoInfo

    @VideoInfo.setter
    def VideoInfo(self, VideoInfo):
        self._VideoInfo = VideoInfo

    @property
    def AudioInfo(self):
        """音频转码信息，不填保持和源文件一致。
        :rtype: :class:`tencentcloud.ie.v20200304.models.AudioInfo`
        """
        return self._AudioInfo

    @AudioInfo.setter
    def AudioInfo(self, AudioInfo):
        self._AudioInfo = AudioInfo

    @property
    def MuxInfo(self):
        """指定封装信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MuxInfo`
        """
        return self._MuxInfo

    @MuxInfo.setter
    def MuxInfo(self, MuxInfo):
        self._MuxInfo = MuxInfo


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        if params.get("TargetInfo") is not None:
            self._TargetInfo = TargetInfo()
            self._TargetInfo._deserialize(params.get("TargetInfo"))
        if params.get("EditInfo") is not None:
            self._EditInfo = EditInfo()
            self._EditInfo._deserialize(params.get("EditInfo"))
        if params.get("VideoInfo") is not None:
            self._VideoInfo = VideoInfo()
            self._VideoInfo._deserialize(params.get("VideoInfo"))
        if params.get("AudioInfo") is not None:
            self._AudioInfo = AudioInfo()
            self._AudioInfo._deserialize(params.get("AudioInfo"))
        if params.get("MuxInfo") is not None:
            self._MuxInfo = MuxInfo()
            self._MuxInfo._deserialize(params.get("MuxInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleItem(AbstractModel):
    """语音字幕识别项

    """

    def __init__(self):
        r"""
        :param _Id: 语音识别结果
        :type Id: str
        :param _Zh: 中文翻译结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Zh: str
        :param _En: 英文翻译结果
注意：此字段可能返回 null，表示取不到有效值。
        :type En: str
        :param _StartPts: 语句起始时间戳PTS(ms)
        :type StartPts: int
        :param _EndPts: 语句结束时间戳PTS(ms)
        :type EndPts: int
        :param _Period: 字符串形式的起始结束时间
        :type Period: str
        :param _Confidence: 结果的置信度（百分制）
        :type Confidence: int
        :param _EndFlag: 当前语句是否结束
        :type EndFlag: bool
        :param _PuncEndTs: 语句分割时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type PuncEndTs: str
        """
        self._Id = None
        self._Zh = None
        self._En = None
        self._StartPts = None
        self._EndPts = None
        self._Period = None
        self._Confidence = None
        self._EndFlag = None
        self._PuncEndTs = None

    @property
    def Id(self):
        """语音识别结果
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Zh(self):
        """中文翻译结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zh

    @Zh.setter
    def Zh(self, Zh):
        self._Zh = Zh

    @property
    def En(self):
        """英文翻译结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._En

    @En.setter
    def En(self, En):
        self._En = En

    @property
    def StartPts(self):
        """语句起始时间戳PTS(ms)
        :rtype: int
        """
        return self._StartPts

    @StartPts.setter
    def StartPts(self, StartPts):
        self._StartPts = StartPts

    @property
    def EndPts(self):
        """语句结束时间戳PTS(ms)
        :rtype: int
        """
        return self._EndPts

    @EndPts.setter
    def EndPts(self, EndPts):
        self._EndPts = EndPts

    @property
    def Period(self):
        """字符串形式的起始结束时间
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Confidence(self):
        """结果的置信度（百分制）
        :rtype: int
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def EndFlag(self):
        """当前语句是否结束
        :rtype: bool
        """
        return self._EndFlag

    @EndFlag.setter
    def EndFlag(self, EndFlag):
        self._EndFlag = EndFlag

    @property
    def PuncEndTs(self):
        """语句分割时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PuncEndTs

    @PuncEndTs.setter
    def PuncEndTs(self, PuncEndTs):
        self._PuncEndTs = PuncEndTs


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Zh = params.get("Zh")
        self._En = params.get("En")
        self._StartPts = params.get("StartPts")
        self._EndPts = params.get("EndPts")
        self._Period = params.get("Period")
        self._Confidence = params.get("Confidence")
        self._EndFlag = params.get("EndFlag")
        self._PuncEndTs = params.get("PuncEndTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleRec(AbstractModel):
    """语音字幕任务参数

    """

    def __init__(self):
        r"""
        :param _AsrDst: 语音识别：
zh：中文
en：英文
        :type AsrDst: str
        :param _TransDst: 翻译识别：
zh：中文
en：英文
        :type TransDst: str
        """
        self._AsrDst = None
        self._TransDst = None

    @property
    def AsrDst(self):
        """语音识别：
zh：中文
en：英文
        :rtype: str
        """
        return self._AsrDst

    @AsrDst.setter
    def AsrDst(self, AsrDst):
        self._AsrDst = AsrDst

    @property
    def TransDst(self):
        """翻译识别：
zh：中文
en：英文
        :rtype: str
        """
        return self._TransDst

    @TransDst.setter
    def TransDst(self, TransDst):
        self._TransDst = TransDst


    def _deserialize(self, params):
        self._AsrDst = params.get("AsrDst")
        self._TransDst = params.get("TransDst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleResult(AbstractModel):
    """语音字幕识别结果

    """

    def __init__(self):
        r"""
        :param _SubtitleItems: 语音字幕数组
        :type SubtitleItems: list of SubtitleItem
        """
        self._SubtitleItems = None

    @property
    def SubtitleItems(self):
        """语音字幕数组
        :rtype: list of SubtitleItem
        """
        return self._SubtitleItems

    @SubtitleItems.setter
    def SubtitleItems(self, SubtitleItems):
        self._SubtitleItems = SubtitleItems


    def _deserialize(self, params):
        if params.get("SubtitleItems") is not None:
            self._SubtitleItems = []
            for item in params.get("SubtitleItems"):
                obj = SubtitleItem()
                obj._deserialize(item)
                self._SubtitleItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagEditingInfo(AbstractModel):
    """视频标签识别任务参数信息

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启视频标签识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param _CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self._Switch = None
        self._CustomInfo = None

    @property
    def Switch(self):
        """是否开启视频标签识别。0为关闭，1为开启。其他非0非1值默认为0。
        :rtype: int
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CustomInfo(self):
        """额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :rtype: str
        """
        return self._CustomInfo

    @CustomInfo.setter
    def CustomInfo(self, CustomInfo):
        self._CustomInfo = CustomInfo


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CustomInfo = params.get("CustomInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagItem(AbstractModel):
    """标签项

    """

    def __init__(self):
        r"""
        :param _Id: 标签内容
        :type Id: str
        :param _Confidence: 结果的置信度（百分制）
        :type Confidence: int
        :param _Categorys: 分级数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Categorys: list of str
        :param _Ext: 标签备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: str
        """
        self._Id = None
        self._Confidence = None
        self._Categorys = None
        self._Ext = None

    @property
    def Id(self):
        """标签内容
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Confidence(self):
        """结果的置信度（百分制）
        :rtype: int
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Categorys(self):
        """分级数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Categorys

    @Categorys.setter
    def Categorys(self, Categorys):
        self._Categorys = Categorys

    @property
    def Ext(self):
        """标签备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Confidence = params.get("Confidence")
        self._Categorys = params.get("Categorys")
        self._Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagTaskResult(AbstractModel):
    """视频标签识别结果信息

    """

    def __init__(self):
        r"""
        :param _Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param _ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param _ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param _ItemSet: 视频标签识别结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of TagTaskResultItem
        """
        self._Status = None
        self._ErrCode = None
        self._ErrMsg = None
        self._ItemSet = None

    @property
    def Status(self):
        """编辑任务状态。 
1：执行中；2：成功；3：失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """编辑任务失败错误码。 
0：成功；其他值：失败。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """编辑任务失败错误描述。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ItemSet(self):
        """视频标签识别结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagTaskResultItem
        """
        return self._ItemSet

    @ItemSet.setter
    def ItemSet(self, ItemSet):
        self._ItemSet = ItemSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self._ItemSet = []
            for item in params.get("ItemSet"):
                obj = TagTaskResultItem()
                obj._deserialize(item)
                self._ItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagTaskResultItem(AbstractModel):
    """视频标签识别结果项

    """

    def __init__(self):
        r"""
        :param _Tag: 标签名称。
        :type Tag: str
        :param _Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self._Tag = None
        self._Confidence = None

    @property
    def Tag(self):
        """标签名称。
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Confidence(self):
        """置信度，取值范围是 0 到 100。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence


    def _deserialize(self, params):
        self._Tag = params.get("Tag")
        self._Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetInfo(AbstractModel):
    """输出文件信息

    """

    def __init__(self):
        r"""
        :param _FileName: 目标文件名
        :type FileName: str
        :param _SegmentInfo: 目标文件切片信息
        :type SegmentInfo: :class:`tencentcloud.ie.v20200304.models.SegmentInfo`
        """
        self._FileName = None
        self._SegmentInfo = None

    @property
    def FileName(self):
        """目标文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def SegmentInfo(self):
        """目标文件切片信息
        :rtype: :class:`tencentcloud.ie.v20200304.models.SegmentInfo`
        """
        return self._SegmentInfo

    @SegmentInfo.setter
    def SegmentInfo(self, SegmentInfo):
        self._SegmentInfo = SegmentInfo


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        if params.get("SegmentInfo") is not None:
            self._SegmentInfo = SegmentInfo()
            self._SegmentInfo._deserialize(params.get("SegmentInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetVideoInfo(AbstractModel):
    """目标视频信息。

    """

    def __init__(self):
        r"""
        :param _Width: 视频宽度，单位像素，一般要求是偶数，否则会向下对齐。
        :type Width: int
        :param _Height: 视频高度，单位像素，一般要求是偶数，否则会向下对齐。
        :type Height: int
        :param _FrameRate: 视频帧率，范围在1到120之间
        :type FrameRate: int
        """
        self._Width = None
        self._Height = None
        self._FrameRate = None

    @property
    def Width(self):
        """视频宽度，单位像素，一般要求是偶数，否则会向下对齐。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """视频高度，单位像素，一般要求是偶数，否则会向下对齐。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def FrameRate(self):
        """视频帧率，范围在1到120之间
        :rtype: int
        """
        return self._FrameRate

    @FrameRate.setter
    def FrameRate(self, FrameRate):
        self._FrameRate = FrameRate


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._FrameRate = params.get("FrameRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResultFile(AbstractModel):
    """任务结果文件信息

    """

    def __init__(self):
        r"""
        :param _Url: 文件链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _FileSize: 文件大小，部分任务支持，单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _MediaInfo: 媒体信息，对于媒体文件，部分任务支持返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.ie.v20200304.models.MediaResultInfo`
        :param _Md5: 文件对应的md5。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        """
        self._Url = None
        self._FileSize = None
        self._MediaInfo = None
        self._Md5 = None

    @property
    def Url(self):
        """文件链接。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FileSize(self):
        """文件大小，部分任务支持，单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def MediaInfo(self):
        """媒体信息，对于媒体文件，部分任务支持返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ie.v20200304.models.MediaResultInfo`
        """
        return self._MediaInfo

    @MediaInfo.setter
    def MediaInfo(self, MediaInfo):
        self._MediaInfo = MediaInfo

    @property
    def Md5(self):
        """文件对应的md5。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._FileSize = params.get("FileSize")
        if params.get("MediaInfo") is not None:
            self._MediaInfo = MediaResultInfo()
            self._MediaInfo._deserialize(params.get("MediaInfo"))
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextMarkInfoItem(AbstractModel):
    """画质重生子任务文字水印信息

    """

    def __init__(self):
        r"""
        :param _Text: 文字内容。
        :type Text: str
        :param _PosX: 文字水印X坐标。
        :type PosX: int
        :param _PosY: 文字水印Y坐标。
        :type PosY: int
        :param _FontSize: 文字大小
        :type FontSize: int
        :param _FontFile: 字体，可选项：hei,song，simkai,arial；默认hei(黑体）。
        :type FontFile: str
        :param _FontColor: 字体颜色，颜色见附录，不填默认black。
        :type FontColor: str
        :param _FontAlpha: 文字透明度，可选值0-1。0：不透明，1：全透明。默认为0
        :type FontAlpha: float
        """
        self._Text = None
        self._PosX = None
        self._PosY = None
        self._FontSize = None
        self._FontFile = None
        self._FontColor = None
        self._FontAlpha = None

    @property
    def Text(self):
        """文字内容。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def PosX(self):
        """文字水印X坐标。
        :rtype: int
        """
        return self._PosX

    @PosX.setter
    def PosX(self, PosX):
        self._PosX = PosX

    @property
    def PosY(self):
        """文字水印Y坐标。
        :rtype: int
        """
        return self._PosY

    @PosY.setter
    def PosY(self, PosY):
        self._PosY = PosY

    @property
    def FontSize(self):
        """文字大小
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontFile(self):
        """字体，可选项：hei,song，simkai,arial；默认hei(黑体）。
        :rtype: str
        """
        return self._FontFile

    @FontFile.setter
    def FontFile(self, FontFile):
        self._FontFile = FontFile

    @property
    def FontColor(self):
        """字体颜色，颜色见附录，不填默认black。
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def FontAlpha(self):
        """文字透明度，可选值0-1。0：不透明，1：全透明。默认为0
        :rtype: float
        """
        return self._FontAlpha

    @FontAlpha.setter
    def FontAlpha(self, FontAlpha):
        self._FontAlpha = FontAlpha


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._PosX = params.get("PosX")
        self._PosY = params.get("PosY")
        self._FontSize = params.get("FontSize")
        self._FontFile = params.get("FontFile")
        self._FontColor = params.get("FontColor")
        self._FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlInfo(AbstractModel):
    """任务视频Url形式下载信息。

    """

    def __init__(self):
        r"""
        :param _Url: 视频 URL。
注意：编辑理解仅支持mp4、flv等格式的点播文件，不支持hls；
        :type Url: str
        :param _Format: 视频地址格式，可选值： 
0：音视频 ;
1：直播流。 
默认为0。其他非0非1值默认为0。画质重生任务只支持0。
        :type Format: int
        :param _Host: 【不再支持】指定请求资源时，HTTP头部host的值。
        :type Host: str
        """
        self._Url = None
        self._Format = None
        self._Host = None

    @property
    def Url(self):
        """视频 URL。
注意：编辑理解仅支持mp4、flv等格式的点播文件，不支持hls；
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Format(self):
        """视频地址格式，可选值： 
0：音视频 ;
1：直播流。 
默认为0。其他非0非1值默认为0。画质重生任务只支持0。
        :rtype: int
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Host(self):
        """【不再支持】指定请求资源时，HTTP头部host的值。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Format = params.get("Format")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEnhance(AbstractModel):
    """画质增强参数信息

    """

    def __init__(self):
        r"""
        :param _ArtifactReduction: 去编码毛刺、伪影参数。
        :type ArtifactReduction: :class:`tencentcloud.ie.v20200304.models.ArtifactReduction`
        :param _Denoising: 去噪声参数。
        :type Denoising: :class:`tencentcloud.ie.v20200304.models.Denoising`
        :param _ColorEnhance: 颜色增强参数。
        :type ColorEnhance: :class:`tencentcloud.ie.v20200304.models.ColorEnhance`
        :param _Sharp: 细节增强参数。
        :type Sharp: :class:`tencentcloud.ie.v20200304.models.Sharp`
        :param _WdSuperResolution: 超分参数，可选项：2，目前仅支持2倍超分。
注意：此参数已经弃用，超分可以使用VideoSuperResolution参数
        :type WdSuperResolution: int
        :param _FaceProtect: 人脸保护信息。
        :type FaceProtect: :class:`tencentcloud.ie.v20200304.models.FaceProtect`
        :param _WdFps: 插帧，取值范围：[0, 60]，单位：Hz。
注意：当取值为 0，表示帧率和原始视频保持一致。
        :type WdFps: int
        :param _ScratchRepair: 去划痕参数
        :type ScratchRepair: :class:`tencentcloud.ie.v20200304.models.ScratchRepair`
        :param _LowLightEnhance: 低光照增强参数
        :type LowLightEnhance: :class:`tencentcloud.ie.v20200304.models.LowLightEnhance`
        :param _VideoSuperResolution: 视频超分参数
        :type VideoSuperResolution: :class:`tencentcloud.ie.v20200304.models.VideoSuperResolution`
        :param _VideoRepair: 视频画质修复参数
        :type VideoRepair: :class:`tencentcloud.ie.v20200304.models.VideoRepair`
        """
        self._ArtifactReduction = None
        self._Denoising = None
        self._ColorEnhance = None
        self._Sharp = None
        self._WdSuperResolution = None
        self._FaceProtect = None
        self._WdFps = None
        self._ScratchRepair = None
        self._LowLightEnhance = None
        self._VideoSuperResolution = None
        self._VideoRepair = None

    @property
    def ArtifactReduction(self):
        """去编码毛刺、伪影参数。
        :rtype: :class:`tencentcloud.ie.v20200304.models.ArtifactReduction`
        """
        return self._ArtifactReduction

    @ArtifactReduction.setter
    def ArtifactReduction(self, ArtifactReduction):
        self._ArtifactReduction = ArtifactReduction

    @property
    def Denoising(self):
        """去噪声参数。
        :rtype: :class:`tencentcloud.ie.v20200304.models.Denoising`
        """
        return self._Denoising

    @Denoising.setter
    def Denoising(self, Denoising):
        self._Denoising = Denoising

    @property
    def ColorEnhance(self):
        """颜色增强参数。
        :rtype: :class:`tencentcloud.ie.v20200304.models.ColorEnhance`
        """
        return self._ColorEnhance

    @ColorEnhance.setter
    def ColorEnhance(self, ColorEnhance):
        self._ColorEnhance = ColorEnhance

    @property
    def Sharp(self):
        """细节增强参数。
        :rtype: :class:`tencentcloud.ie.v20200304.models.Sharp`
        """
        return self._Sharp

    @Sharp.setter
    def Sharp(self, Sharp):
        self._Sharp = Sharp

    @property
    def WdSuperResolution(self):
        """超分参数，可选项：2，目前仅支持2倍超分。
注意：此参数已经弃用，超分可以使用VideoSuperResolution参数
        :rtype: int
        """
        return self._WdSuperResolution

    @WdSuperResolution.setter
    def WdSuperResolution(self, WdSuperResolution):
        self._WdSuperResolution = WdSuperResolution

    @property
    def FaceProtect(self):
        """人脸保护信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.FaceProtect`
        """
        return self._FaceProtect

    @FaceProtect.setter
    def FaceProtect(self, FaceProtect):
        self._FaceProtect = FaceProtect

    @property
    def WdFps(self):
        """插帧，取值范围：[0, 60]，单位：Hz。
注意：当取值为 0，表示帧率和原始视频保持一致。
        :rtype: int
        """
        return self._WdFps

    @WdFps.setter
    def WdFps(self, WdFps):
        self._WdFps = WdFps

    @property
    def ScratchRepair(self):
        """去划痕参数
        :rtype: :class:`tencentcloud.ie.v20200304.models.ScratchRepair`
        """
        return self._ScratchRepair

    @ScratchRepair.setter
    def ScratchRepair(self, ScratchRepair):
        self._ScratchRepair = ScratchRepair

    @property
    def LowLightEnhance(self):
        """低光照增强参数
        :rtype: :class:`tencentcloud.ie.v20200304.models.LowLightEnhance`
        """
        return self._LowLightEnhance

    @LowLightEnhance.setter
    def LowLightEnhance(self, LowLightEnhance):
        self._LowLightEnhance = LowLightEnhance

    @property
    def VideoSuperResolution(self):
        """视频超分参数
        :rtype: :class:`tencentcloud.ie.v20200304.models.VideoSuperResolution`
        """
        return self._VideoSuperResolution

    @VideoSuperResolution.setter
    def VideoSuperResolution(self, VideoSuperResolution):
        self._VideoSuperResolution = VideoSuperResolution

    @property
    def VideoRepair(self):
        """视频画质修复参数
        :rtype: :class:`tencentcloud.ie.v20200304.models.VideoRepair`
        """
        return self._VideoRepair

    @VideoRepair.setter
    def VideoRepair(self, VideoRepair):
        self._VideoRepair = VideoRepair


    def _deserialize(self, params):
        if params.get("ArtifactReduction") is not None:
            self._ArtifactReduction = ArtifactReduction()
            self._ArtifactReduction._deserialize(params.get("ArtifactReduction"))
        if params.get("Denoising") is not None:
            self._Denoising = Denoising()
            self._Denoising._deserialize(params.get("Denoising"))
        if params.get("ColorEnhance") is not None:
            self._ColorEnhance = ColorEnhance()
            self._ColorEnhance._deserialize(params.get("ColorEnhance"))
        if params.get("Sharp") is not None:
            self._Sharp = Sharp()
            self._Sharp._deserialize(params.get("Sharp"))
        self._WdSuperResolution = params.get("WdSuperResolution")
        if params.get("FaceProtect") is not None:
            self._FaceProtect = FaceProtect()
            self._FaceProtect._deserialize(params.get("FaceProtect"))
        self._WdFps = params.get("WdFps")
        if params.get("ScratchRepair") is not None:
            self._ScratchRepair = ScratchRepair()
            self._ScratchRepair._deserialize(params.get("ScratchRepair"))
        if params.get("LowLightEnhance") is not None:
            self._LowLightEnhance = LowLightEnhance()
            self._LowLightEnhance._deserialize(params.get("LowLightEnhance"))
        if params.get("VideoSuperResolution") is not None:
            self._VideoSuperResolution = VideoSuperResolution()
            self._VideoSuperResolution._deserialize(params.get("VideoSuperResolution"))
        if params.get("VideoRepair") is not None:
            self._VideoRepair = VideoRepair()
            self._VideoRepair._deserialize(params.get("VideoRepair"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfo(AbstractModel):
    """视频转码信息

    """

    def __init__(self):
        r"""
        :param _Fps: 视频帧率，取值范围：[0, 60]，单位：Hz。
注意：当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param _Width: 宽度，取值范围：0 和 [128, 4096]
注意：
当 Width、Height 均为 0，则分辨率同源；
当 Width 为 0，Height 非 0，则 Width 按比例缩放；
当 Width 非 0，Height 为 0，则 Height 按比例缩放；
当 Width、Height 均非 0，则分辨率按用户指定。
        :type Width: int
        :param _Height: 高度，取值范围：0 和 [128, 4096]
注意：
当 Width、Height 均为 0，则分辨率同源；
当 Width 为 0，Height 非 0，则 Width 按比例缩放；
当 Width 非 0，Height 为 0，则 Height 按比例缩放；
当 Width、Height 均非 0，则分辨率按用户指定。
        :type Height: int
        :param _LongSide: 长边分辨率，取值范围：0 和 [128, 4096]
注意：
当 LongSide、ShortSide 均为 0，则分辨率按照Width，Height；
当 LongSide 为 0，ShortSide 非 0，则 LongSide 按比例缩放；
当 LongSide非 0，ShortSide为 0，则 ShortSide 按比例缩放；
当 LongSide、ShortSide 均非 0，则分辨率按用户指定。
长短边优先级高于Weight,Height,设置长短边则忽略宽高。
        :type LongSide: int
        :param _ShortSide: 短边分辨率，取值范围：0 和 [128, 4096]
注意：
当 LongSide、ShortSide 均为 0，则分辨率按照Width，Height；
当 LongSide 为 0，ShortSide 非 0，则 LongSide 按比例缩放；
当 LongSide非 0，ShortSide为 0，则 ShortSide 按比例缩放；
当 LongSide、ShortSide 均非 0，则分辨率按用户指定。
长短边优先级高于Weight,Height,设置长短边则忽略宽高。
        :type ShortSide: int
        :param _Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param _Gop: 固定I帧之间，视频帧数量，取值范围： [25, 2500]，如果不填，使用编码默认最优序列。
        :type Gop: int
        :param _VideoCodec: 编码器支持选项，可选值：
h264,
h265,
av1。
不填默认h264。
        :type VideoCodec: str
        :param _PicMarkInfo: 图片水印。
        :type PicMarkInfo: list of PicMarkInfoItem
        :param _DarInfo: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。
        :type DarInfo: :class:`tencentcloud.ie.v20200304.models.DarInfo`
        :param _Hdr: 支持hdr,可选项：
hdr10,
hlg。
此时，VideoCodec会强制设置为h265, 编码位深为10
        :type Hdr: str
        :param _VideoEnhance: 画质增强参数信息。
        :type VideoEnhance: :class:`tencentcloud.ie.v20200304.models.VideoEnhance`
        :param _HiddenMarkInfo: 数字水印参数信息。
        :type HiddenMarkInfo: :class:`tencentcloud.ie.v20200304.models.HiddenMarkInfo`
        :param _TextMarkInfo: 文本水印参数信息。
        :type TextMarkInfo: list of TextMarkInfoItem
        """
        self._Fps = None
        self._Width = None
        self._Height = None
        self._LongSide = None
        self._ShortSide = None
        self._Bitrate = None
        self._Gop = None
        self._VideoCodec = None
        self._PicMarkInfo = None
        self._DarInfo = None
        self._Hdr = None
        self._VideoEnhance = None
        self._HiddenMarkInfo = None
        self._TextMarkInfo = None

    @property
    def Fps(self):
        """视频帧率，取值范围：[0, 60]，单位：Hz。
注意：当取值为 0，表示帧率和原始视频保持一致。
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Width(self):
        """宽度，取值范围：0 和 [128, 4096]
注意：
当 Width、Height 均为 0，则分辨率同源；
当 Width 为 0，Height 非 0，则 Width 按比例缩放；
当 Width 非 0，Height 为 0，则 Height 按比例缩放；
当 Width、Height 均非 0，则分辨率按用户指定。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """高度，取值范围：0 和 [128, 4096]
注意：
当 Width、Height 均为 0，则分辨率同源；
当 Width 为 0，Height 非 0，则 Width 按比例缩放；
当 Width 非 0，Height 为 0，则 Height 按比例缩放；
当 Width、Height 均非 0，则分辨率按用户指定。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def LongSide(self):
        """长边分辨率，取值范围：0 和 [128, 4096]
注意：
当 LongSide、ShortSide 均为 0，则分辨率按照Width，Height；
当 LongSide 为 0，ShortSide 非 0，则 LongSide 按比例缩放；
当 LongSide非 0，ShortSide为 0，则 ShortSide 按比例缩放；
当 LongSide、ShortSide 均非 0，则分辨率按用户指定。
长短边优先级高于Weight,Height,设置长短边则忽略宽高。
        :rtype: int
        """
        return self._LongSide

    @LongSide.setter
    def LongSide(self, LongSide):
        self._LongSide = LongSide

    @property
    def ShortSide(self):
        """短边分辨率，取值范围：0 和 [128, 4096]
注意：
当 LongSide、ShortSide 均为 0，则分辨率按照Width，Height；
当 LongSide 为 0，ShortSide 非 0，则 LongSide 按比例缩放；
当 LongSide非 0，ShortSide为 0，则 ShortSide 按比例缩放；
当 LongSide、ShortSide 均非 0，则分辨率按用户指定。
长短边优先级高于Weight,Height,设置长短边则忽略宽高。
        :rtype: int
        """
        return self._ShortSide

    @ShortSide.setter
    def ShortSide(self, ShortSide):
        self._ShortSide = ShortSide

    @property
    def Bitrate(self):
        """视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。当取值为 0，表示视频码率和原始视频保持一致。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Gop(self):
        """固定I帧之间，视频帧数量，取值范围： [25, 2500]，如果不填，使用编码默认最优序列。
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop

    @property
    def VideoCodec(self):
        """编码器支持选项，可选值：
h264,
h265,
av1。
不填默认h264。
        :rtype: str
        """
        return self._VideoCodec

    @VideoCodec.setter
    def VideoCodec(self, VideoCodec):
        self._VideoCodec = VideoCodec

    @property
    def PicMarkInfo(self):
        """图片水印。
        :rtype: list of PicMarkInfoItem
        """
        return self._PicMarkInfo

    @PicMarkInfo.setter
    def PicMarkInfo(self, PicMarkInfo):
        self._PicMarkInfo = PicMarkInfo

    @property
    def DarInfo(self):
        """填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。
        :rtype: :class:`tencentcloud.ie.v20200304.models.DarInfo`
        """
        return self._DarInfo

    @DarInfo.setter
    def DarInfo(self, DarInfo):
        self._DarInfo = DarInfo

    @property
    def Hdr(self):
        """支持hdr,可选项：
hdr10,
hlg。
此时，VideoCodec会强制设置为h265, 编码位深为10
        :rtype: str
        """
        return self._Hdr

    @Hdr.setter
    def Hdr(self, Hdr):
        self._Hdr = Hdr

    @property
    def VideoEnhance(self):
        """画质增强参数信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.VideoEnhance`
        """
        return self._VideoEnhance

    @VideoEnhance.setter
    def VideoEnhance(self, VideoEnhance):
        self._VideoEnhance = VideoEnhance

    @property
    def HiddenMarkInfo(self):
        """数字水印参数信息。
        :rtype: :class:`tencentcloud.ie.v20200304.models.HiddenMarkInfo`
        """
        return self._HiddenMarkInfo

    @HiddenMarkInfo.setter
    def HiddenMarkInfo(self, HiddenMarkInfo):
        self._HiddenMarkInfo = HiddenMarkInfo

    @property
    def TextMarkInfo(self):
        """文本水印参数信息。
        :rtype: list of TextMarkInfoItem
        """
        return self._TextMarkInfo

    @TextMarkInfo.setter
    def TextMarkInfo(self, TextMarkInfo):
        self._TextMarkInfo = TextMarkInfo


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._LongSide = params.get("LongSide")
        self._ShortSide = params.get("ShortSide")
        self._Bitrate = params.get("Bitrate")
        self._Gop = params.get("Gop")
        self._VideoCodec = params.get("VideoCodec")
        if params.get("PicMarkInfo") is not None:
            self._PicMarkInfo = []
            for item in params.get("PicMarkInfo"):
                obj = PicMarkInfoItem()
                obj._deserialize(item)
                self._PicMarkInfo.append(obj)
        if params.get("DarInfo") is not None:
            self._DarInfo = DarInfo()
            self._DarInfo._deserialize(params.get("DarInfo"))
        self._Hdr = params.get("Hdr")
        if params.get("VideoEnhance") is not None:
            self._VideoEnhance = VideoEnhance()
            self._VideoEnhance._deserialize(params.get("VideoEnhance"))
        if params.get("HiddenMarkInfo") is not None:
            self._HiddenMarkInfo = HiddenMarkInfo()
            self._HiddenMarkInfo._deserialize(params.get("HiddenMarkInfo"))
        if params.get("TextMarkInfo") is not None:
            self._TextMarkInfo = []
            for item in params.get("TextMarkInfo"):
                obj = TextMarkInfoItem()
                obj._deserialize(item)
                self._TextMarkInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfoResultItem(AbstractModel):
    """任务结束后生成的文件视频信息

    """

    def __init__(self):
        r"""
        :param _Stream: 视频流的流id。
        :type Stream: int
        :param _Width: 视频宽度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 视频高度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Bitrate: 视频码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param _Fps: 视频帧率，用分数格式表示，如：25/1, 99/32等等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Fps: str
        :param _Codec: 编码格式，如h264,h265等等 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        :param _Rotate: 播放旋转角度，可选值0-360。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: int
        :param _Duration: 视频时长，单位：ms 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _PixFormat: 颜色空间，如yuv420p，yuv444p等等。
注意：此字段可能返回 null，表示取不到有效值。
        :type PixFormat: str
        """
        self._Stream = None
        self._Width = None
        self._Height = None
        self._Bitrate = None
        self._Fps = None
        self._Codec = None
        self._Rotate = None
        self._Duration = None
        self._PixFormat = None

    @property
    def Stream(self):
        """视频流的流id。
        :rtype: int
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def Width(self):
        """视频宽度。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """视频高度。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Bitrate(self):
        """视频码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Fps(self):
        """视频帧率，用分数格式表示，如：25/1, 99/32等等。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Codec(self):
        """编码格式，如h264,h265等等 。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def Rotate(self):
        """播放旋转角度，可选值0-360。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate

    @property
    def Duration(self):
        """视频时长，单位：ms 。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def PixFormat(self):
        """颜色空间，如yuv420p，yuv444p等等。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PixFormat

    @PixFormat.setter
    def PixFormat(self, PixFormat):
        self._PixFormat = PixFormat


    def _deserialize(self, params):
        self._Stream = params.get("Stream")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Bitrate = params.get("Bitrate")
        self._Fps = params.get("Fps")
        self._Codec = params.get("Codec")
        self._Rotate = params.get("Rotate")
        self._Duration = params.get("Duration")
        self._PixFormat = params.get("PixFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoRepair(AbstractModel):
    """综合画质修复，包括：去噪，去毛刺，细节增强，主观画质提升。

    """

    def __init__(self):
        r"""
        :param _Type: 画质修复类型，可选值：weak，normal，strong;
默认值: weak
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        """画质修复类型，可选值：weak，normal，strong;
默认值: weak
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoSuperResolution(AbstractModel):
    """视频超分

    """

    def __init__(self):
        r"""
        :param _Type: 超分视频类型：可选值：lq,hq
lq: 针对低清晰度有较多噪声视频的超分;
hq: 针对高清晰度视频超分;
默认取值：lq。
        :type Type: str
        :param _Size: 超分倍数，可选值：2。
注意：当前只支持两倍超分。
        :type Size: int
        """
        self._Type = None
        self._Size = None

    @property
    def Type(self):
        """超分视频类型：可选值：lq,hq
lq: 针对低清晰度有较多噪声视频的超分;
hq: 针对高清晰度视频超分;
默认取值：lq。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        """超分倍数，可选值：2。
注意：当前只支持两倍超分。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        