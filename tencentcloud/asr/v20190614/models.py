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


class AsyncRecognitionTaskInfo(AbstractModel):
    """音频流异步识别任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _Url: 音频流Url
        :type Url: str
        """
        self._TaskId = None
        self._Url = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncRecognitionTasks(AbstractModel):
    """音频流异步识别任务列表

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of AsyncRecognitionTaskInfo
        """
        self._Tasks = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = AsyncRecognitionTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseAsyncRecognitionTaskRequest(AbstractModel):
    """CloseAsyncRecognitionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 语音流异步识别任务的唯一标识，在创建任务时会返回
        :type TaskId: int
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
        


class CloseAsyncRecognitionTaskResponse(AbstractModel):
    """CloseAsyncRecognitionTask返回参数结构体

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


class CreateAsrVocabRequest(AbstractModel):
    """CreateAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 热词表名称，长度在1-255之间
        :type Name: str
        :param _Description: 热词表描述，长度在0-1000之间
        :type Description: str
        :param _WordWeights: 词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10，权重为[1,10]之间整数，数组长度不大于128
        :type WordWeights: list of HotWord
        :param _WordWeightStr: 词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。
当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略
        :type WordWeightStr: str
        """
        self._Name = None
        self._Description = None
        self._WordWeights = None
        self._WordWeightStr = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WordWeights(self):
        return self._WordWeights

    @WordWeights.setter
    def WordWeights(self, WordWeights):
        self._WordWeights = WordWeights

    @property
    def WordWeightStr(self):
        return self._WordWeightStr

    @WordWeightStr.setter
    def WordWeightStr(self, WordWeightStr):
        self._WordWeightStr = WordWeightStr


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("WordWeights") is not None:
            self._WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self._WordWeights.append(obj)
        self._WordWeightStr = params.get("WordWeightStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAsrVocabResponse(AbstractModel):
    """CreateAsrVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 词表ID，可用于获取词表信息
        :type VocabId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabId = None
        self._RequestId = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._RequestId = params.get("RequestId")


class CreateAsyncRecognitionTaskRequest(AbstractModel):
    """CreateAsyncRecognitionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineType: 引擎模型类型。
• 16k_zh：中文普通话通用；
• 16k_en：英语；
• 16k_yue：粤语；
• 16k_id：印度尼西亚语；
• 16k_fil：菲律宾语；
• 16k_th：泰语；
• 16k_pt：葡萄牙语；
• 16k_tr：土耳其语；
        :type EngineType: str
        :param _Url: 语音流地址，支持rtmp、rtsp等流媒体协议，以及各类基于http协议的直播流(不支持hls, m3u8)
        :type Url: str
        :param _CallbackUrl: 支持HTTP和HTTPS协议，用于接收识别结果，您需要自行搭建公网可调用的服务。回调格式&内容详见：[语音流异步识别回调说明](https://cloud.tencent.com/document/product/1093/52633)
        :type CallbackUrl: str
        :param _SignToken: 用于生成回调通知中的签名
        :type SignToken: str
        :param _FilterDirty: 是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0
        :type FilterDirty: int
        :param _FilterModal: 是否过语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0
        :type FilterModal: int
        :param _FilterPunc: 是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认为0
        :type FilterPunc: int
        :param _ConvertNumMode: 是否进行阿拉伯数字智能转换。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1
        :type ConvertNumMode: int
        :param _WordInfo: 是否显示词级别时间戳。0：不显示；1：显示，不包含标点时间戳，2：显示，包含标点时间戳。默认为0
        :type WordInfo: int
        :param _HotwordId: 热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
        :type HotwordId: str
        :param _AudioData: 回调数据中，是否需要对应音频数据。
        :type AudioData: bool
        """
        self._EngineType = None
        self._Url = None
        self._CallbackUrl = None
        self._SignToken = None
        self._FilterDirty = None
        self._FilterModal = None
        self._FilterPunc = None
        self._ConvertNumMode = None
        self._WordInfo = None
        self._HotwordId = None
        self._AudioData = None

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def SignToken(self):
        return self._SignToken

    @SignToken.setter
    def SignToken(self, SignToken):
        self._SignToken = SignToken

    @property
    def FilterDirty(self):
        return self._FilterDirty

    @FilterDirty.setter
    def FilterDirty(self, FilterDirty):
        self._FilterDirty = FilterDirty

    @property
    def FilterModal(self):
        return self._FilterModal

    @FilterModal.setter
    def FilterModal(self, FilterModal):
        self._FilterModal = FilterModal

    @property
    def FilterPunc(self):
        return self._FilterPunc

    @FilterPunc.setter
    def FilterPunc(self, FilterPunc):
        self._FilterPunc = FilterPunc

    @property
    def ConvertNumMode(self):
        return self._ConvertNumMode

    @ConvertNumMode.setter
    def ConvertNumMode(self, ConvertNumMode):
        self._ConvertNumMode = ConvertNumMode

    @property
    def WordInfo(self):
        return self._WordInfo

    @WordInfo.setter
    def WordInfo(self, WordInfo):
        self._WordInfo = WordInfo

    @property
    def HotwordId(self):
        return self._HotwordId

    @HotwordId.setter
    def HotwordId(self, HotwordId):
        self._HotwordId = HotwordId

    @property
    def AudioData(self):
        return self._AudioData

    @AudioData.setter
    def AudioData(self, AudioData):
        self._AudioData = AudioData


    def _deserialize(self, params):
        self._EngineType = params.get("EngineType")
        self._Url = params.get("Url")
        self._CallbackUrl = params.get("CallbackUrl")
        self._SignToken = params.get("SignToken")
        self._FilterDirty = params.get("FilterDirty")
        self._FilterModal = params.get("FilterModal")
        self._FilterPunc = params.get("FilterPunc")
        self._ConvertNumMode = params.get("ConvertNumMode")
        self._WordInfo = params.get("WordInfo")
        self._HotwordId = params.get("HotwordId")
        self._AudioData = params.get("AudioData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAsyncRecognitionTaskResponse(AbstractModel):
    """CreateAsyncRecognitionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 请求返回结果，包含本次的任务ID(TaskId)
        :type Data: :class:`tencentcloud.asr.v20190614.models.Task`
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
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateCustomizationRequest(AbstractModel):
    """CreateCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 自学习模型名称，需在1-20字符之间
        :type ModelName: str
        :param _TextUrl: 文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :type TextUrl: str
        :param _ModelType: 自学习模型类型，填写8k或者16k
        :type ModelType: str
        :param _TagInfos: 标签信息
        :type TagInfos: list of str
        """
        self._ModelName = None
        self._TextUrl = None
        self._ModelType = None
        self._TagInfos = None

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def TextUrl(self):
        return self._TextUrl

    @TextUrl.setter
    def TextUrl(self, TextUrl):
        self._TextUrl = TextUrl

    @property
    def ModelType(self):
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def TagInfos(self):
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        self._TagInfos = TagInfos


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._TextUrl = params.get("TextUrl")
        self._ModelType = params.get("ModelType")
        self._TagInfos = params.get("TagInfos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomizationResponse(AbstractModel):
    """CreateCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelId = None
        self._RequestId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._RequestId = params.get("RequestId")


class CreateRecTaskRequest(AbstractModel):
    """CreateRecTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineModelType: 引擎模型类型。注意：非电话场景请务必使用16k的引擎。
电话场景：
• 8k_zh：中文电话通用；
• 8k_en：英文电话通用；

非电话场景：
• 16k_zh：中文通用；
• 16k_zh-PY：中英粤;
• 16k_zh_medical：中文医疗；
• 16k_en：英语；
• 16k_yue：粤语；
• 16k_ja：日语；
• 16k_ko：韩语；
• 16k_vi：越南语；
• 16k_ms：马来语；
• 16k_id：印度尼西亚语；
• 16k_fil：菲律宾语；
• 16k_th：泰语；
• 16k_pt：葡萄牙语；
• 16k_tr：土耳其语；
• 16k_zh_dialect：多方言，支持23种方言（上海话、四川话、武汉话、贵阳话、昆明话、西安话、郑州话、太原话、兰州话、银川话、西宁话、南京话、合肥话、南昌话、长沙话、苏州话、杭州话、济南话、天津话、石家庄话、黑龙江话、吉林话、辽宁话）；
        :type EngineModelType: str
        :param _ChannelNum: 识别声道数。1：单声道（非电话场景，直接选择单声道即可，忽略音频声道数）；2：双声道（仅支持8k_zh电话场景，双声道应分别对应通话双方）。注意：双声道的电话音频已物理分离说话人，无需再开启说话人分离功能。
        :type ChannelNum: int
        :param _ResTextFormat: 识别结果返回形式。0： 识别结果文本(含分段时间戳)； 1：词级别粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)(不含标点，含语速值)；2：词级别粒度的详细识别结果（包含标点、语速值）；3: 标点符号分段，包含每段时间戳，特别适用于字幕场景（包含词级时间、标点、语速值）。4：【付费功能】将对ASR结果按照语义分段，并展示词级别粒度的详细识别结果（注意：如果开启后付费，将[自动计费](https://cloud.tencent.com/document/product/1093/35686)）
        :type ResTextFormat: int
        :param _SourceType: 语音数据来源。0：语音 URL；1：语音数据（post body）。
        :type SourceType: int
        :param _SpeakerDiarization: 是否开启说话人分离，0：不开启，1：开启(仅支持8k_zh/16k_zh，ChannelNum=1时可用)，默认值为 0。
注意：8k电话场景建议使用双声道来区分通话双方，设置ChannelNum=2即可，不用开启说话人分离，如果设置了ChannelNum=1，后台会先转码成单声道，说话人分离结果可能产生偏差。
        :type SpeakerDiarization: int
        :param _SpeakerNumber: 说话人分离人数（需配合开启说话人分离使用），取值范围：0-10，0代表自动分离（目前仅支持≤6个人），1-10代表指定说话人数分离。默认值为 0。
注：此功能结果仅供参考，请根据您的需要谨慎使用。
        :type SpeakerNumber: int
        :param _CallbackUrl: 回调 URL，用户自行搭建的用于接收识别结果的服务URL。如果用户使用轮询方式获取识别结果，则无需提交该参数。回调格式&内容详见：[录音识别回调说明](https://cloud.tencent.com/document/product/1093/52632)
        :type CallbackUrl: str
        :param _Url: 语音的URL地址，需要公网环境浏览器可下载。当 SourceType 值为 0 时须填写该字段，为 1 时不需要填写。注意：请确保录音文件时长在5个小时之内，否则可能识别失败。请保证文件的下载速度，否则可能下载失败。
        :type Url: str
        :param _Data: 语音数据base64编码，当SourceType 值为1时必须填写，为0可不写。音频数据要小于5MB。
        :type Data: str
        :param _DataLen: 数据长度，非必填（此数据长度为数据未进行base64编码时的数据长度）。
        :type DataLen: int
        :param _ConvertNumMode: 是否进行阿拉伯数字智能转换（目前支持中文普通话引擎）。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字，3: 打开数学相关数字转换。默认值为 1。
        :type ConvertNumMode: int
        :param _FilterDirty: 是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0。
        :type FilterDirty: int
        :param _HotwordId: 热词表id。如不设置该参数，自动生效默认热词表；如设置了该参数，那么将生效对应的热词表。
        :type HotwordId: str
        :param _CustomizationId: 自学习模型 id。如设置了该参数，将生效对应的自学习模型。
        :type CustomizationId: str
        :param _Extra: 附加参数(该参数无意义，忽略即可)
        :type Extra: str
        :param _FilterPunc: 是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认值为 0。
        :type FilterPunc: int
        :param _FilterModal: 是否过滤语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0。
        :type FilterModal: int
        :param _EmotionalEnergy: 情绪能量值，取值为音量分贝值/10。取值范围：[1,10]。值越高情绪越强烈。0:不开启，1:开启
        :type EmotionalEnergy: int
        :param _ReinforceHotword: 热词增强功能。1:开启后（仅支持8k_zh,16k_zh），将开启同音替换功能，同音字、词在热词中配置。举例：热词配置“蜜制”并开启增强功能后，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。
        :type ReinforceHotword: int
        :param _SentenceMaxLength: 单标点最多字数，取值范围：[6，40]。默认为0，不开启该功能。该参数可用于字幕生成场景，控制单行字幕最大字数（设置ResTextFormat为3，解析返回的ResultDetail列表，通过结构中FinalSentence获取单个标点断句结果）。
        :type SentenceMaxLength: int
        :param _EmotionRecognition: 情绪识别能力(目前支持16k_zh) 默认为0，不开启。 1：开启情绪识别但是不会在文本展示“情绪标签”， 2：开启情绪识别并且在文本展示“情绪标签”。（该功能需要设置ResTextFormat 大于0）
注意：本功能为增值服务，购买对应套餐包后，将参数设置为1或2时方可按对应方式生效，并消耗套餐包对应资源。参数设置为0时无需购买套餐包，也不会消耗对应资源。
        :type EmotionRecognition: int
        """
        self._EngineModelType = None
        self._ChannelNum = None
        self._ResTextFormat = None
        self._SourceType = None
        self._SpeakerDiarization = None
        self._SpeakerNumber = None
        self._CallbackUrl = None
        self._Url = None
        self._Data = None
        self._DataLen = None
        self._ConvertNumMode = None
        self._FilterDirty = None
        self._HotwordId = None
        self._CustomizationId = None
        self._Extra = None
        self._FilterPunc = None
        self._FilterModal = None
        self._EmotionalEnergy = None
        self._ReinforceHotword = None
        self._SentenceMaxLength = None
        self._EmotionRecognition = None

    @property
    def EngineModelType(self):
        return self._EngineModelType

    @EngineModelType.setter
    def EngineModelType(self, EngineModelType):
        self._EngineModelType = EngineModelType

    @property
    def ChannelNum(self):
        return self._ChannelNum

    @ChannelNum.setter
    def ChannelNum(self, ChannelNum):
        self._ChannelNum = ChannelNum

    @property
    def ResTextFormat(self):
        return self._ResTextFormat

    @ResTextFormat.setter
    def ResTextFormat(self, ResTextFormat):
        self._ResTextFormat = ResTextFormat

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SpeakerDiarization(self):
        return self._SpeakerDiarization

    @SpeakerDiarization.setter
    def SpeakerDiarization(self, SpeakerDiarization):
        self._SpeakerDiarization = SpeakerDiarization

    @property
    def SpeakerNumber(self):
        return self._SpeakerNumber

    @SpeakerNumber.setter
    def SpeakerNumber(self, SpeakerNumber):
        self._SpeakerNumber = SpeakerNumber

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DataLen(self):
        return self._DataLen

    @DataLen.setter
    def DataLen(self, DataLen):
        self._DataLen = DataLen

    @property
    def ConvertNumMode(self):
        return self._ConvertNumMode

    @ConvertNumMode.setter
    def ConvertNumMode(self, ConvertNumMode):
        self._ConvertNumMode = ConvertNumMode

    @property
    def FilterDirty(self):
        return self._FilterDirty

    @FilterDirty.setter
    def FilterDirty(self, FilterDirty):
        self._FilterDirty = FilterDirty

    @property
    def HotwordId(self):
        return self._HotwordId

    @HotwordId.setter
    def HotwordId(self, HotwordId):
        self._HotwordId = HotwordId

    @property
    def CustomizationId(self):
        return self._CustomizationId

    @CustomizationId.setter
    def CustomizationId(self, CustomizationId):
        self._CustomizationId = CustomizationId

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def FilterPunc(self):
        return self._FilterPunc

    @FilterPunc.setter
    def FilterPunc(self, FilterPunc):
        self._FilterPunc = FilterPunc

    @property
    def FilterModal(self):
        return self._FilterModal

    @FilterModal.setter
    def FilterModal(self, FilterModal):
        self._FilterModal = FilterModal

    @property
    def EmotionalEnergy(self):
        return self._EmotionalEnergy

    @EmotionalEnergy.setter
    def EmotionalEnergy(self, EmotionalEnergy):
        self._EmotionalEnergy = EmotionalEnergy

    @property
    def ReinforceHotword(self):
        return self._ReinforceHotword

    @ReinforceHotword.setter
    def ReinforceHotword(self, ReinforceHotword):
        self._ReinforceHotword = ReinforceHotword

    @property
    def SentenceMaxLength(self):
        return self._SentenceMaxLength

    @SentenceMaxLength.setter
    def SentenceMaxLength(self, SentenceMaxLength):
        self._SentenceMaxLength = SentenceMaxLength

    @property
    def EmotionRecognition(self):
        return self._EmotionRecognition

    @EmotionRecognition.setter
    def EmotionRecognition(self, EmotionRecognition):
        self._EmotionRecognition = EmotionRecognition


    def _deserialize(self, params):
        self._EngineModelType = params.get("EngineModelType")
        self._ChannelNum = params.get("ChannelNum")
        self._ResTextFormat = params.get("ResTextFormat")
        self._SourceType = params.get("SourceType")
        self._SpeakerDiarization = params.get("SpeakerDiarization")
        self._SpeakerNumber = params.get("SpeakerNumber")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Url = params.get("Url")
        self._Data = params.get("Data")
        self._DataLen = params.get("DataLen")
        self._ConvertNumMode = params.get("ConvertNumMode")
        self._FilterDirty = params.get("FilterDirty")
        self._HotwordId = params.get("HotwordId")
        self._CustomizationId = params.get("CustomizationId")
        self._Extra = params.get("Extra")
        self._FilterPunc = params.get("FilterPunc")
        self._FilterModal = params.get("FilterModal")
        self._EmotionalEnergy = params.get("EmotionalEnergy")
        self._ReinforceHotword = params.get("ReinforceHotword")
        self._SentenceMaxLength = params.get("SentenceMaxLength")
        self._EmotionRecognition = params.get("EmotionRecognition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecTaskResponse(AbstractModel):
    """CreateRecTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 录音文件识别的请求返回结果，包含结果查询需要的TaskId
        :type Data: :class:`tencentcloud.asr.v20190614.models.Task`
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
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteAsrVocabRequest(AbstractModel):
    """DeleteAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表Id
        :type VocabId: str
        """
        self._VocabId = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAsrVocabResponse(AbstractModel):
    """DeleteAsrVocab返回参数结构体

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


class DeleteCustomizationRequest(AbstractModel):
    """DeleteCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 要删除的模型ID
        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizationResponse(AbstractModel):
    """DeleteCustomization返回参数结构体

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


class DescribeAsyncRecognitionTasksRequest(AbstractModel):
    """DescribeAsyncRecognitionTasks请求参数结构体

    """


class DescribeAsyncRecognitionTasksResponse(AbstractModel):
    """DescribeAsyncRecognitionTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.asr.v20190614.models.AsyncRecognitionTasks`
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
            self._Data = AsyncRecognitionTasks()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 从CreateRecTask接口获取的TaskId，用于获取任务状态与结果。
        :type TaskId: int
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
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 录音文件识别的请求返回结果。
        :type Data: :class:`tencentcloud.asr.v20190614.models.TaskStatus`
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
            self._Data = TaskStatus()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DownloadAsrVocabRequest(AbstractModel):
    """DownloadAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 词表ID。
        :type VocabId: str
        """
        self._VocabId = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadAsrVocabResponse(AbstractModel):
    """DownloadAsrVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 词表ID。
        :type VocabId: str
        :param _WordWeightStr: 词表权重文件形式的base64值。
        :type WordWeightStr: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabId = None
        self._WordWeightStr = None
        self._RequestId = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def WordWeightStr(self):
        return self._WordWeightStr

    @WordWeightStr.setter
    def WordWeightStr(self, WordWeightStr):
        self._WordWeightStr = WordWeightStr

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._WordWeightStr = params.get("WordWeightStr")
        self._RequestId = params.get("RequestId")


class DownloadCustomizationRequest(AbstractModel):
    """DownloadCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 自学习模型ID
        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCustomizationResponse(AbstractModel):
    """DownloadCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class GetAsrVocabListRequest(AbstractModel):
    """GetAsrVocabList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagInfos: 标签信息，格式为“$TagKey : $TagValue ”，中间分隔符为“空格”+“:”+“空格”
        :type TagInfos: list of str
        :param _Offset: 分页Offset
        :type Offset: int
        :param _Limit: 分页Limit
        :type Limit: int
        """
        self._TagInfos = None
        self._Offset = None
        self._Limit = None

    @property
    def TagInfos(self):
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        self._TagInfos = TagInfos

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TagInfos = params.get("TagInfos")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAsrVocabListResponse(AbstractModel):
    """GetAsrVocabList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabList: 热词表列表
        :type VocabList: list of Vocab
        :param _TotalCount: 热词列表总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def VocabList(self):
        return self._VocabList

    @VocabList.setter
    def VocabList(self, VocabList):
        self._VocabList = VocabList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VocabList") is not None:
            self._VocabList = []
            for item in params.get("VocabList"):
                obj = Vocab()
                obj._deserialize(item)
                self._VocabList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetAsrVocabRequest(AbstractModel):
    """GetAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID
        :type VocabId: str
        """
        self._VocabId = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAsrVocabResponse(AbstractModel):
    """GetAsrVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 热词表名称
        :type Name: str
        :param _Description: 热词表描述
        :type Description: str
        :param _VocabId: 热词表ID
        :type VocabId: str
        :param _WordWeights: 词权重列表
        :type WordWeights: list of HotWord
        :param _CreateTime: 词表创建时间
        :type CreateTime: str
        :param _UpdateTime: 词表更新时间
        :type UpdateTime: str
        :param _State: 热词表状态，1为默认状态即在识别时默认加载该热词表进行识别，0为初始状态
        :type State: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Description = None
        self._VocabId = None
        self._WordWeights = None
        self._CreateTime = None
        self._UpdateTime = None
        self._State = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def WordWeights(self):
        return self._WordWeights

    @WordWeights.setter
    def WordWeights(self, WordWeights):
        self._WordWeights = WordWeights

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._VocabId = params.get("VocabId")
        if params.get("WordWeights") is not None:
            self._WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self._WordWeights.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._State = params.get("State")
        self._RequestId = params.get("RequestId")


class GetCustomizationListRequest(AbstractModel):
    """GetCustomizationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagInfos: 标签信息，格式为“$TagKey : $TagValue ”，中间分隔符为“空格”+“:”+“空格”
        :type TagInfos: list of str
        :param _Limit: 分页大小，默认1000
        :type Limit: int
        :param _Offset: 分页offset，默认0
        :type Offset: int
        """
        self._TagInfos = None
        self._Limit = None
        self._Offset = None

    @property
    def TagInfos(self):
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        self._TagInfos = TagInfos

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._TagInfos = params.get("TagInfos")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomizationListResponse(AbstractModel):
    """GetCustomizationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 自学习模型数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of Model
        :param _TotalCount: 自学习模型总量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Model()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetModelInfoRequest(AbstractModel):
    """GetModelInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型id
        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetModelInfoResponse(AbstractModel):
    """GetModelInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 模型信息
        :type Data: :class:`tencentcloud.asr.v20190614.models.Model`
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
            self._Data = Model()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class HotWord(AbstractModel):
    """热词的词和权重

    """

    def __init__(self):
        r"""
        :param _Word: 热词
        :type Word: str
        :param _Weight: 权重
        :type Weight: int
        """
        self._Word = None
        self._Weight = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Model(AbstractModel):
    """自学习模型信息

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _DictName: 模型文件名称
        :type DictName: str
        :param _ModelId: 模型Id
        :type ModelId: str
        :param _ModelType: 模型类型，“8k”或者”16k“
        :type ModelType: str
        :param _ServiceType: 服务类型
        :type ServiceType: str
        :param _ModelState: 模型状态：
-2：模型训练失败；
-1：已下线；
0：训练中；
1：已上线；
3：上线中；
4：下线中；
        :type ModelState: int
        :param _AtUpdated: 最后更新时间
        :type AtUpdated: str
        :param _TagInfos: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfos: list of str
        """
        self._ModelName = None
        self._DictName = None
        self._ModelId = None
        self._ModelType = None
        self._ServiceType = None
        self._ModelState = None
        self._AtUpdated = None
        self._TagInfos = None

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def DictName(self):
        return self._DictName

    @DictName.setter
    def DictName(self, DictName):
        self._DictName = DictName

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelType(self):
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ModelState(self):
        return self._ModelState

    @ModelState.setter
    def ModelState(self, ModelState):
        self._ModelState = ModelState

    @property
    def AtUpdated(self):
        return self._AtUpdated

    @AtUpdated.setter
    def AtUpdated(self, AtUpdated):
        self._AtUpdated = AtUpdated

    @property
    def TagInfos(self):
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        self._TagInfos = TagInfos


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._DictName = params.get("DictName")
        self._ModelId = params.get("ModelId")
        self._ModelType = params.get("ModelType")
        self._ServiceType = params.get("ServiceType")
        self._ModelState = params.get("ModelState")
        self._AtUpdated = params.get("AtUpdated")
        self._TagInfos = params.get("TagInfos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizationRequest(AbstractModel):
    """ModifyCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 要修改的模型ID
        :type ModelId: str
        :param _ModelName: 要修改的模型名称，长度需在1-20个字符之间
        :type ModelName: str
        :param _ModelType: 要修改的模型类型，为8k或者16k
        :type ModelType: str
        :param _TextUrl: 要修改的模型语料的下载地址，目前仅支持腾讯云cos
        :type TextUrl: str
        """
        self._ModelId = None
        self._ModelName = None
        self._ModelType = None
        self._TextUrl = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelType(self):
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def TextUrl(self):
        return self._TextUrl

    @TextUrl.setter
    def TextUrl(self, TextUrl):
        self._TextUrl = TextUrl


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        self._ModelType = params.get("ModelType")
        self._TextUrl = params.get("TextUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizationResponse(AbstractModel):
    """ModifyCustomization返回参数结构体

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


class ModifyCustomizationStateRequest(AbstractModel):
    """ModifyCustomizationState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 自学习模型ID
        :type ModelId: str
        :param _ToState: 想要变换的模型状态，-1代表下线，1代表上线
        :type ToState: int
        """
        self._ModelId = None
        self._ToState = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ToState(self):
        return self._ToState

    @ToState.setter
    def ToState(self, ToState):
        self._ToState = ToState


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ToState = params.get("ToState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizationStateResponse(AbstractModel):
    """ModifyCustomizationState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 自学习模型ID
        :type ModelId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelId = None
        self._RequestId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._RequestId = params.get("RequestId")


class SentenceDetail(AbstractModel):
    """单句的详细识别结果，包含单个词的时间偏移，一般用于生成字幕的场景。

    """

    def __init__(self):
        r"""
        :param _FinalSentence: 单句最终识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalSentence: str
        :param _SliceSentence: 单句中间识别结果，使用空格拆分为多个词
注意：此字段可能返回 null，表示取不到有效值。
        :type SliceSentence: str
        :param _StartMs: 单句开始时间（毫秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type StartMs: int
        :param _EndMs: 单句结束时间（毫秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndMs: int
        :param _WordsNum: 单句中词个数
注意：此字段可能返回 null，表示取不到有效值。
        :type WordsNum: int
        :param _Words: 单句中词详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Words: list of SentenceWords
        :param _SpeechSpeed: 单句语速，单位：字数/秒
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeechSpeed: float
        :param _SpeakerId: 声道或说话人 Id（请求中如果设置了 speaker_diarization或者ChannelNum为双声道，可区分说话人或声道）
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeakerId: int
        :param _EmotionalEnergy: 情绪能量值，取值为音量分贝值/10。取值范围：[1,10]。值越高情绪越强烈。
注意：此字段可能返回 null，表示取不到有效值。
        :type EmotionalEnergy: float
        :param _SilenceTime: 本句与上一句之间的静音时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SilenceTime: int
        :param _EmotionType: 情绪类型（可能为空）
注意：此字段可能返回 null，表示取不到有效值。
        :type EmotionType: list of str
        """
        self._FinalSentence = None
        self._SliceSentence = None
        self._StartMs = None
        self._EndMs = None
        self._WordsNum = None
        self._Words = None
        self._SpeechSpeed = None
        self._SpeakerId = None
        self._EmotionalEnergy = None
        self._SilenceTime = None
        self._EmotionType = None

    @property
    def FinalSentence(self):
        return self._FinalSentence

    @FinalSentence.setter
    def FinalSentence(self, FinalSentence):
        self._FinalSentence = FinalSentence

    @property
    def SliceSentence(self):
        return self._SliceSentence

    @SliceSentence.setter
    def SliceSentence(self, SliceSentence):
        self._SliceSentence = SliceSentence

    @property
    def StartMs(self):
        return self._StartMs

    @StartMs.setter
    def StartMs(self, StartMs):
        self._StartMs = StartMs

    @property
    def EndMs(self):
        return self._EndMs

    @EndMs.setter
    def EndMs(self, EndMs):
        self._EndMs = EndMs

    @property
    def WordsNum(self):
        return self._WordsNum

    @WordsNum.setter
    def WordsNum(self, WordsNum):
        self._WordsNum = WordsNum

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def SpeechSpeed(self):
        return self._SpeechSpeed

    @SpeechSpeed.setter
    def SpeechSpeed(self, SpeechSpeed):
        self._SpeechSpeed = SpeechSpeed

    @property
    def SpeakerId(self):
        return self._SpeakerId

    @SpeakerId.setter
    def SpeakerId(self, SpeakerId):
        self._SpeakerId = SpeakerId

    @property
    def EmotionalEnergy(self):
        return self._EmotionalEnergy

    @EmotionalEnergy.setter
    def EmotionalEnergy(self, EmotionalEnergy):
        self._EmotionalEnergy = EmotionalEnergy

    @property
    def SilenceTime(self):
        return self._SilenceTime

    @SilenceTime.setter
    def SilenceTime(self, SilenceTime):
        self._SilenceTime = SilenceTime

    @property
    def EmotionType(self):
        return self._EmotionType

    @EmotionType.setter
    def EmotionType(self, EmotionType):
        self._EmotionType = EmotionType


    def _deserialize(self, params):
        self._FinalSentence = params.get("FinalSentence")
        self._SliceSentence = params.get("SliceSentence")
        self._StartMs = params.get("StartMs")
        self._EndMs = params.get("EndMs")
        self._WordsNum = params.get("WordsNum")
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = SentenceWords()
                obj._deserialize(item)
                self._Words.append(obj)
        self._SpeechSpeed = params.get("SpeechSpeed")
        self._SpeakerId = params.get("SpeakerId")
        self._EmotionalEnergy = params.get("EmotionalEnergy")
        self._SilenceTime = params.get("SilenceTime")
        self._EmotionType = params.get("EmotionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceRecognitionRequest(AbstractModel):
    """SentenceRecognition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngSerViceType: 引擎模型类型。
电话场景：
• 8k_zh：中文电话通用；
• 8k_en：英文电话通用；

非电话场景：
• 16k_zh：中文通用；
• 16k_zh-PY：中英粤;
• 16k_zh_medical：中文医疗；
• 16k_en：英语；
• 16k_yue：粤语；
• 16k_ja：日语；
• 16k_ko：韩语；
• 16k_vi：越南语；
• 16k_ms：马来语；
• 16k_id：印度尼西亚语；
• 16k_fil：菲律宾语；
• 16k_th：泰语；
• 16k_pt：葡萄牙语；
• 16k_tr：土耳其语；
• 16k_zh_dialect：多方言，支持23种方言（上海话、四川话、武汉话、贵阳话、昆明话、西安话、郑州话、太原话、兰州话、银川话、西宁话、南京话、合肥话、南昌话、长沙话、苏州话、杭州话、济南话、天津话、石家庄话、黑龙江话、吉林话、辽宁话）；
        :type EngSerViceType: str
        :param _SourceType: 语音数据来源。0：语音 URL；1：语音数据（post body）。
        :type SourceType: int
        :param _VoiceFormat: 识别音频的音频格式，支持wav、pcm、ogg-opus、speex、silk、mp3、m4a、aac、amr。
        :type VoiceFormat: str
        :param _ProjectId: 腾讯云项目 ID，废弃参数，填写0即可。
        :type ProjectId: int
        :param _SubServiceType: 子服务类型。2： 一句话识别。
        :type SubServiceType: int
        :param _Url: 语音的URL地址，需要公网环境浏览器可下载。当 SourceType 值为 0时须填写该字段，为 1 时不填。音频时长不能超过60s，音频文件大小不能超过3MB。
        :type Url: str
        :param _UsrAudioKey: 废弃参数，填写任意字符串即可。
        :type UsrAudioKey: str
        :param _Data: 语音数据，当SourceType 值为1（本地语音数据上传）时必须填写，当SourceType 值为0（语音 URL上传）可不写。要使用base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频时长不能超过60s，音频文件大小不能超过3MB（Base64后）。
        :type Data: str
        :param _DataLen: 数据长度，单位为字节。当 SourceType 值为1（本地语音数据上传）时必须填写，当 SourceType 值为0（语音 URL上传）可不写（此数据长度为数据未进行base64编码时的数据长度）。
        :type DataLen: int
        :param _WordInfo: 是否显示词级别时间戳。0：不显示；1：显示，不包含标点时间戳，2：显示，包含标点时间戳。默认值为 0。
        :type WordInfo: int
        :param _FilterDirty: 是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0。
        :type FilterDirty: int
        :param _FilterModal: 是否过语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0。
        :type FilterModal: int
        :param _FilterPunc: 是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认值为 0。
        :type FilterPunc: int
        :param _ConvertNumMode: 是否进行阿拉伯数字智能转换。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1。
        :type ConvertNumMode: int
        :param _HotwordId: 热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
        :type HotwordId: str
        :param _CustomizationId: 自学习模型 id。如设置了该参数，将生效对应的自学习模型。
        :type CustomizationId: str
        :param _ReinforceHotword: 热词增强功能。1:开启后（仅支持8k_zh,16k_zh），将开启同音替换功能，同音字、词在热词中配置。举例：热词配置“蜜制”并开启增强功能后，与“蜜制”同拼音（mizhi）的“秘制”、“蜜汁”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。
        :type ReinforceHotword: int
        :param _HotwordList: 临时热词：用于提升识别准确率，临时热词规则：“热词|权重”，热词不超过30个字符（最多10个汉字），权重1-10，最多传入128个热词。举例："腾讯云|10,语音识别|5,ASR|10"。
“临时热词”和“热词id”的区别：热词id需要先在控制台或通过接口创建热词表，得到热词表id后才可以使用热词功能，本字段可以在每次请求时直接传入热词使用，但每次请求后云端不会保留相关的热词数据，需要客户自行维护相关数据
        :type HotwordList: str
        """
        self._EngSerViceType = None
        self._SourceType = None
        self._VoiceFormat = None
        self._ProjectId = None
        self._SubServiceType = None
        self._Url = None
        self._UsrAudioKey = None
        self._Data = None
        self._DataLen = None
        self._WordInfo = None
        self._FilterDirty = None
        self._FilterModal = None
        self._FilterPunc = None
        self._ConvertNumMode = None
        self._HotwordId = None
        self._CustomizationId = None
        self._ReinforceHotword = None
        self._HotwordList = None

    @property
    def EngSerViceType(self):
        return self._EngSerViceType

    @EngSerViceType.setter
    def EngSerViceType(self, EngSerViceType):
        self._EngSerViceType = EngSerViceType

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def VoiceFormat(self):
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def ProjectId(self):
        warnings.warn("parameter `ProjectId` is deprecated", DeprecationWarning) 

        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        warnings.warn("parameter `ProjectId` is deprecated", DeprecationWarning) 

        self._ProjectId = ProjectId

    @property
    def SubServiceType(self):
        warnings.warn("parameter `SubServiceType` is deprecated", DeprecationWarning) 

        return self._SubServiceType

    @SubServiceType.setter
    def SubServiceType(self, SubServiceType):
        warnings.warn("parameter `SubServiceType` is deprecated", DeprecationWarning) 

        self._SubServiceType = SubServiceType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def UsrAudioKey(self):
        warnings.warn("parameter `UsrAudioKey` is deprecated", DeprecationWarning) 

        return self._UsrAudioKey

    @UsrAudioKey.setter
    def UsrAudioKey(self, UsrAudioKey):
        warnings.warn("parameter `UsrAudioKey` is deprecated", DeprecationWarning) 

        self._UsrAudioKey = UsrAudioKey

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DataLen(self):
        return self._DataLen

    @DataLen.setter
    def DataLen(self, DataLen):
        self._DataLen = DataLen

    @property
    def WordInfo(self):
        return self._WordInfo

    @WordInfo.setter
    def WordInfo(self, WordInfo):
        self._WordInfo = WordInfo

    @property
    def FilterDirty(self):
        return self._FilterDirty

    @FilterDirty.setter
    def FilterDirty(self, FilterDirty):
        self._FilterDirty = FilterDirty

    @property
    def FilterModal(self):
        return self._FilterModal

    @FilterModal.setter
    def FilterModal(self, FilterModal):
        self._FilterModal = FilterModal

    @property
    def FilterPunc(self):
        return self._FilterPunc

    @FilterPunc.setter
    def FilterPunc(self, FilterPunc):
        self._FilterPunc = FilterPunc

    @property
    def ConvertNumMode(self):
        return self._ConvertNumMode

    @ConvertNumMode.setter
    def ConvertNumMode(self, ConvertNumMode):
        self._ConvertNumMode = ConvertNumMode

    @property
    def HotwordId(self):
        return self._HotwordId

    @HotwordId.setter
    def HotwordId(self, HotwordId):
        self._HotwordId = HotwordId

    @property
    def CustomizationId(self):
        return self._CustomizationId

    @CustomizationId.setter
    def CustomizationId(self, CustomizationId):
        self._CustomizationId = CustomizationId

    @property
    def ReinforceHotword(self):
        return self._ReinforceHotword

    @ReinforceHotword.setter
    def ReinforceHotword(self, ReinforceHotword):
        self._ReinforceHotword = ReinforceHotword

    @property
    def HotwordList(self):
        return self._HotwordList

    @HotwordList.setter
    def HotwordList(self, HotwordList):
        self._HotwordList = HotwordList


    def _deserialize(self, params):
        self._EngSerViceType = params.get("EngSerViceType")
        self._SourceType = params.get("SourceType")
        self._VoiceFormat = params.get("VoiceFormat")
        self._ProjectId = params.get("ProjectId")
        self._SubServiceType = params.get("SubServiceType")
        self._Url = params.get("Url")
        self._UsrAudioKey = params.get("UsrAudioKey")
        self._Data = params.get("Data")
        self._DataLen = params.get("DataLen")
        self._WordInfo = params.get("WordInfo")
        self._FilterDirty = params.get("FilterDirty")
        self._FilterModal = params.get("FilterModal")
        self._FilterPunc = params.get("FilterPunc")
        self._ConvertNumMode = params.get("ConvertNumMode")
        self._HotwordId = params.get("HotwordId")
        self._CustomizationId = params.get("CustomizationId")
        self._ReinforceHotword = params.get("ReinforceHotword")
        self._HotwordList = params.get("HotwordList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceRecognitionResponse(AbstractModel):
    """SentenceRecognition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 识别结果。
        :type Result: str
        :param _AudioDuration: 请求的音频时长，单位为ms
        :type AudioDuration: int
        :param _WordSize: 词时间戳列表的长度
注意：此字段可能返回 null，表示取不到有效值。
        :type WordSize: int
        :param _WordList: 词时间戳列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WordList: list of SentenceWord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._AudioDuration = None
        self._WordSize = None
        self._WordList = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def AudioDuration(self):
        return self._AudioDuration

    @AudioDuration.setter
    def AudioDuration(self, AudioDuration):
        self._AudioDuration = AudioDuration

    @property
    def WordSize(self):
        return self._WordSize

    @WordSize.setter
    def WordSize(self, WordSize):
        self._WordSize = WordSize

    @property
    def WordList(self):
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._AudioDuration = params.get("AudioDuration")
        self._WordSize = params.get("WordSize")
        if params.get("WordList") is not None:
            self._WordList = []
            for item in params.get("WordList"):
                obj = SentenceWord()
                obj._deserialize(item)
                self._WordList.append(obj)
        self._RequestId = params.get("RequestId")


class SentenceWord(AbstractModel):
    """一句话识别返回的词时间戳

    """

    def __init__(self):
        r"""
        :param _Word: 词结果
        :type Word: str
        :param _StartTime: 词在音频中的开始时间
        :type StartTime: int
        :param _EndTime: 词在音频中的结束时间
        :type EndTime: int
        """
        self._Word = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

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


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceWords(AbstractModel):
    """识别结果中词文本，以及对应时间偏移

    """

    def __init__(self):
        r"""
        :param _Word: 词文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Word: str
        :param _OffsetStartMs: 在句子中的开始时间偏移量
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetStartMs: int
        :param _OffsetEndMs: 在句子中的结束时间偏移量
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetEndMs: int
        """
        self._Word = None
        self._OffsetStartMs = None
        self._OffsetEndMs = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def OffsetStartMs(self):
        return self._OffsetStartMs

    @OffsetStartMs.setter
    def OffsetStartMs(self, OffsetStartMs):
        self._OffsetStartMs = OffsetStartMs

    @property
    def OffsetEndMs(self):
        return self._OffsetEndMs

    @OffsetEndMs.setter
    def OffsetEndMs(self, OffsetEndMs):
        self._OffsetEndMs = OffsetEndMs


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._OffsetStartMs = params.get("OffsetStartMs")
        self._OffsetEndMs = params.get("OffsetEndMs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVocabStateRequest(AbstractModel):
    """SetVocabState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID。
        :type VocabId: str
        :param _State: 热词表状态，1：设为默认状态；0：设为非默认状态。
        :type State: int
        """
        self._VocabId = None
        self._State = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVocabStateResponse(AbstractModel):
    """SetVocabState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID
        :type VocabId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabId = None
        self._RequestId = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._RequestId = params.get("RequestId")


class Task(AbstractModel):
    """录音文件识别、实时语音异步识别请求的返回数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可通过此ID在轮询接口获取识别状态与结果。注意：TaskId数据类型为uint64
        :type TaskId: int
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
        


class TaskStatus(AbstractModel):
    """获取录音识别结果的返回参数

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务标识。注意：TaskId数据类型为uint64。
        :type TaskId: int
        :param _Status: 任务状态码，0：任务等待，1：任务执行中，2：任务成功，3：任务失败。
        :type Status: int
        :param _StatusStr: 任务状态，waiting：任务等待，doing：任务执行中，success：任务成功，failed：任务失败。
        :type StatusStr: str
        :param _Result: 识别结果。
        :type Result: str
        :param _ErrorMsg: 失败原因说明。
        :type ErrorMsg: str
        :param _ResultDetail: 识别结果详情，包含每个句子中的词时间偏移，一般用于生成字幕的场景。(录音识别请求中ResTextFormat=1时该字段不为空)
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultDetail: list of SentenceDetail
        :param _AudioDuration: 音频时长(秒)。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioDuration: float
        """
        self._TaskId = None
        self._Status = None
        self._StatusStr = None
        self._Result = None
        self._ErrorMsg = None
        self._ResultDetail = None
        self._AudioDuration = None

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
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ResultDetail(self):
        return self._ResultDetail

    @ResultDetail.setter
    def ResultDetail(self, ResultDetail):
        self._ResultDetail = ResultDetail

    @property
    def AudioDuration(self):
        return self._AudioDuration

    @AudioDuration.setter
    def AudioDuration(self, AudioDuration):
        self._AudioDuration = AudioDuration


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._StatusStr = params.get("StatusStr")
        self._Result = params.get("Result")
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("ResultDetail") is not None:
            self._ResultDetail = []
            for item in params.get("ResultDetail"):
                obj = SentenceDetail()
                obj._deserialize(item)
                self._ResultDetail.append(obj)
        self._AudioDuration = params.get("AudioDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAsrVocabRequest(AbstractModel):
    """UpdateAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID
        :type VocabId: str
        :param _Name: 热词表名称，长度在1-255之间
        :type Name: str
        :param _WordWeights: 词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10，权重为[1,10]之间整数，数组长度不大于128
        :type WordWeights: list of HotWord
        :param _WordWeightStr: 词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。
当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略
        :type WordWeightStr: str
        :param _Description: 热词表描述，长度在0-1000之间
        :type Description: str
        """
        self._VocabId = None
        self._Name = None
        self._WordWeights = None
        self._WordWeightStr = None
        self._Description = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def WordWeights(self):
        return self._WordWeights

    @WordWeights.setter
    def WordWeights(self, WordWeights):
        self._WordWeights = WordWeights

    @property
    def WordWeightStr(self):
        return self._WordWeightStr

    @WordWeightStr.setter
    def WordWeightStr(self, WordWeightStr):
        self._WordWeightStr = WordWeightStr

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._Name = params.get("Name")
        if params.get("WordWeights") is not None:
            self._WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self._WordWeights.append(obj)
        self._WordWeightStr = params.get("WordWeightStr")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAsrVocabResponse(AbstractModel):
    """UpdateAsrVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID
        :type VocabId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabId = None
        self._RequestId = None

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._RequestId = params.get("RequestId")


class Vocab(AbstractModel):
    """词表内容

    """

    def __init__(self):
        r"""
        :param _Name: 热词表名称
        :type Name: str
        :param _Description: 热词表描述
        :type Description: str
        :param _VocabId: 热词表ID
        :type VocabId: str
        :param _WordWeights: 词权重列表
        :type WordWeights: list of HotWord
        :param _CreateTime: 词表创建时间
        :type CreateTime: str
        :param _UpdateTime: 词表更新时间
        :type UpdateTime: str
        :param _State: 热词表状态，1为默认状态即在识别时默认加载该热词表进行识别，0为初始状态
        :type State: int
        :param _TagInfos: 标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfos: list of str
        """
        self._Name = None
        self._Description = None
        self._VocabId = None
        self._WordWeights = None
        self._CreateTime = None
        self._UpdateTime = None
        self._State = None
        self._TagInfos = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VocabId(self):
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def WordWeights(self):
        return self._WordWeights

    @WordWeights.setter
    def WordWeights(self, WordWeights):
        self._WordWeights = WordWeights

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def TagInfos(self):
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        self._TagInfos = TagInfos


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._VocabId = params.get("VocabId")
        if params.get("WordWeights") is not None:
            self._WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self._WordWeights.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._State = params.get("State")
        self._TagInfos = params.get("TagInfos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintBaseData(AbstractModel):
    """说话人基础数据，包括说话人id和说话人昵称

    """

    def __init__(self):
        r"""
        :param _VoicePrintId: 说话人id
注意：此字段可能返回 null，表示取不到有效值。
        :type VoicePrintId: str
        :param _SpeakerNick: 说话人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeakerNick: str
        """
        self._VoicePrintId = None
        self._SpeakerNick = None

    @property
    def VoicePrintId(self):
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def SpeakerNick(self):
        return self._SpeakerNick

    @SpeakerNick.setter
    def SpeakerNick(self, SpeakerNick):
        self._SpeakerNick = SpeakerNick


    def _deserialize(self, params):
        self._VoicePrintId = params.get("VoicePrintId")
        self._SpeakerNick = params.get("SpeakerNick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintDeleteRequest(AbstractModel):
    """VoicePrintDelete请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoicePrintId: 说话人id，说话人唯一标识
        :type VoicePrintId: str
        """
        self._VoicePrintId = None

    @property
    def VoicePrintId(self):
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId


    def _deserialize(self, params):
        self._VoicePrintId = params.get("VoicePrintId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintDeleteResponse(AbstractModel):
    """VoicePrintDelete返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 说话人基本信息
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
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
            self._Data = VoicePrintBaseData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VoicePrintEnrollRequest(AbstractModel):
    """VoicePrintEnroll请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoiceFormat: 音频格式 0: pcm, 1: wav
        :type VoiceFormat: int
        :param _SampleRate: 音频采样率，目前支持16000，单位：Hz，必填
        :type SampleRate: int
        :param _Data: 音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M
        :type Data: str
        :param _SpeakerNick: 说话人昵称  不超过32字节
        :type SpeakerNick: str
        """
        self._VoiceFormat = None
        self._SampleRate = None
        self._Data = None
        self._SpeakerNick = None

    @property
    def VoiceFormat(self):
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SpeakerNick(self):
        return self._SpeakerNick

    @SpeakerNick.setter
    def SpeakerNick(self, SpeakerNick):
        self._SpeakerNick = SpeakerNick


    def _deserialize(self, params):
        self._VoiceFormat = params.get("VoiceFormat")
        self._SampleRate = params.get("SampleRate")
        self._Data = params.get("Data")
        self._SpeakerNick = params.get("SpeakerNick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintEnrollResponse(AbstractModel):
    """VoicePrintEnroll返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 说话人基本数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
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
            self._Data = VoicePrintBaseData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VoicePrintUpdateRequest(AbstractModel):
    """VoicePrintUpdate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoiceFormat: 音频格式 0: pcm, 1: wav
        :type VoiceFormat: int
        :param _SampleRate: 音频采样率 目前仅支持16000 单位Hz
        :type SampleRate: int
        :param _VoicePrintId: 说话人id， 说话人唯一标识
        :type VoicePrintId: str
        :param _Data: 音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M	
        :type Data: str
        :param _SpeakerNick: 说话人昵称  不超过32字节
        :type SpeakerNick: str
        """
        self._VoiceFormat = None
        self._SampleRate = None
        self._VoicePrintId = None
        self._Data = None
        self._SpeakerNick = None

    @property
    def VoiceFormat(self):
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def VoicePrintId(self):
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SpeakerNick(self):
        return self._SpeakerNick

    @SpeakerNick.setter
    def SpeakerNick(self, SpeakerNick):
        self._SpeakerNick = SpeakerNick


    def _deserialize(self, params):
        self._VoiceFormat = params.get("VoiceFormat")
        self._SampleRate = params.get("SampleRate")
        self._VoicePrintId = params.get("VoicePrintId")
        self._Data = params.get("Data")
        self._SpeakerNick = params.get("SpeakerNick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintUpdateResponse(AbstractModel):
    """VoicePrintUpdate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 说话人基础数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
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
            self._Data = VoicePrintBaseData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VoicePrintVerifyData(AbstractModel):
    """说话人验证数据

    """

    def __init__(self):
        r"""
        :param _VoicePrintId: 说话人id
注意：此字段可能返回 null，表示取不到有效值。
        :type VoicePrintId: str
        :param _Score: 匹配度 取值范围(0.0 - 100.0)
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: str
        :param _Decision: 验证结果 0: 未通过 1: 通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Decision: int
        """
        self._VoicePrintId = None
        self._Score = None
        self._Decision = None

    @property
    def VoicePrintId(self):
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Decision(self):
        return self._Decision

    @Decision.setter
    def Decision(self, Decision):
        self._Decision = Decision


    def _deserialize(self, params):
        self._VoicePrintId = params.get("VoicePrintId")
        self._Score = params.get("Score")
        self._Decision = params.get("Decision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintVerifyRequest(AbstractModel):
    """VoicePrintVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoiceFormat: 音频格式 0: pcm, 1: wav
        :type VoiceFormat: int
        :param _SampleRate: 音频采样率，目前支持16000，单位：Hz，必填
        :type SampleRate: int
        :param _VoicePrintId: 说话人id, 说话人唯一标识
        :type VoicePrintId: str
        :param _Data: 音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M	
        :type Data: str
        """
        self._VoiceFormat = None
        self._SampleRate = None
        self._VoicePrintId = None
        self._Data = None

    @property
    def VoiceFormat(self):
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def VoicePrintId(self):
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._VoiceFormat = params.get("VoiceFormat")
        self._SampleRate = params.get("SampleRate")
        self._VoicePrintId = params.get("VoicePrintId")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintVerifyResponse(AbstractModel):
    """VoicePrintVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 说话人验证数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintVerifyData`
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
            self._Data = VoicePrintVerifyData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")