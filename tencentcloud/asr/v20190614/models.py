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


class AsyncRecognitionTaskInfo(AbstractModel):
    r"""[音频流异步识别](https://cloud.tencent.com/document/api/1093/37824#AsyncRecognitionTasks)任务信息

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
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        r"""音频流Url
        :rtype: str
        """
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
    r"""[音频流异步识别任务列表](https://cloud.tencent.com/document/product/1093/52060#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)

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
        r"""任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AsyncRecognitionTaskInfo
        """
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
    r"""CloseAsyncRecognitionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 语音流异步识别任务的唯一标识，在创建任务时会返回
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""语音流异步识别任务的唯一标识，在创建任务时会返回
        :rtype: int
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
        


class CloseAsyncRecognitionTaskResponse(AbstractModel):
    r"""CloseAsyncRecognitionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateAsrKeyWordLibRequest(AbstractModel):
    r"""CreateAsrKeyWordLib请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 词表名称，长度在1-20之间
仅限中英文数字-_
        :type Name: str
        :param _KeyWordFile: 词文件（纯文本文件）的二进制base64编码，以行分隔
格式要求：TXT
每行只有一个词，不满足格式则报错无法上传
每个词限制**5个汉字，15个字符**，单个词库最多不超过100个词
注意不要有空行，尤其是最后一行
        :type KeyWordFile: str
        """
        self._Name = None
        self._KeyWordFile = None

    @property
    def Name(self):
        r"""词表名称，长度在1-20之间
仅限中英文数字-_
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KeyWordFile(self):
        r"""词文件（纯文本文件）的二进制base64编码，以行分隔
格式要求：TXT
每行只有一个词，不满足格式则报错无法上传
每个词限制**5个汉字，15个字符**，单个词库最多不超过100个词
注意不要有空行，尤其是最后一行
        :rtype: str
        """
        return self._KeyWordFile

    @KeyWordFile.setter
    def KeyWordFile(self, KeyWordFile):
        self._KeyWordFile = KeyWordFile


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._KeyWordFile = params.get("KeyWordFile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAsrKeyWordLibResponse(AbstractModel):
    r"""CreateAsrKeyWordLib返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 词表ID数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.KeyWordLibIdData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""词表ID数据
        :rtype: :class:`tencentcloud.asr.v20190614.models.KeyWordLibIdData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = KeyWordLibIdData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateAsrVocabRequest(AbstractModel):
    r"""CreateAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 热词表名称，长度在1-255之间
        :type Name: str
        :param _Description: 热词表描述，长度在0-1000之间
        :type Description: str
        :param _WordWeights: 词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10个汉字或30个英文字符，权重为[1,11]之间整数或者100，数组长度不大于1000
注意: 
- 热词权重设置为11时，当前热词将升级为超级热词，建议仅将重要且必须生效的热词设置到11，设置过多权重为11的热词将影响整体字准率。
- 热词权重设置为100时，当前热词开启热词增强同音替换功能（仅支持8k_zh,16k_zh），举例：热词配置“蜜制|100”时，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。建议仅将重要且必须生效的热词设置到100，设置过多权重为100的热词将影响整体字准率。
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
        r"""热词表名称，长度在1-255之间
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""热词表描述，长度在0-1000之间
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WordWeights(self):
        r"""词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10个汉字或30个英文字符，权重为[1,11]之间整数或者100，数组长度不大于1000
注意: 
- 热词权重设置为11时，当前热词将升级为超级热词，建议仅将重要且必须生效的热词设置到11，设置过多权重为11的热词将影响整体字准率。
- 热词权重设置为100时，当前热词开启热词增强同音替换功能（仅支持8k_zh,16k_zh），举例：热词配置“蜜制|100”时，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。建议仅将重要且必须生效的热词设置到100，设置过多权重为100的热词将影响整体字准率。
        :rtype: list of HotWord
        """
        return self._WordWeights

    @WordWeights.setter
    def WordWeights(self, WordWeights):
        self._WordWeights = WordWeights

    @property
    def WordWeightStr(self):
        r"""词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。
当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略
        :rtype: str
        """
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
    r"""CreateAsrVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 词表ID，可用于获取词表信息
        :type VocabId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabId = None
        self._RequestId = None

    @property
    def VocabId(self):
        r"""词表ID，可用于获取词表信息
        :rtype: str
        """
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._RequestId = params.get("RequestId")


class CreateAsyncRecognitionTaskRequest(AbstractModel):
    r"""CreateAsyncRecognitionTask请求参数结构体

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
• 16k_ar：阿拉伯语；
• 16k_es：西班牙语；
• 16k_hi：印地语；
• 16k_fr：法语；
• 16k_de：德语；
        :type EngineType: str
        :param _Url: 语音流地址，支持rtmp、rtsp等流媒体协议，以及各类基于http协议的直播流(不支持hls, m3u8)
        :type Url: str
        :param _CallbackUrl: 支持HTTP和HTTPS协议，用于接收识别结果，您需要自行搭建公网可调用的服务。回调格式&内容详见：[语音流异步识别回调说明](https://cloud.tencent.com/document/product/1093/52633)
        :type CallbackUrl: str
        :param _SignToken: 用于生成回调通知中的签名
        :type SignToken: str
        :param _FilterDirty: 是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0
        :type FilterDirty: int
        :param _FilterModal: 是否过滤语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0
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
        r"""引擎模型类型。
• 16k_zh：中文普通话通用；
• 16k_en：英语；
• 16k_yue：粤语；
• 16k_id：印度尼西亚语；
• 16k_fil：菲律宾语；
• 16k_th：泰语；
• 16k_pt：葡萄牙语；
• 16k_tr：土耳其语；
• 16k_ar：阿拉伯语；
• 16k_es：西班牙语；
• 16k_hi：印地语；
• 16k_fr：法语；
• 16k_de：德语；
        :rtype: str
        """
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Url(self):
        r"""语音流地址，支持rtmp、rtsp等流媒体协议，以及各类基于http协议的直播流(不支持hls, m3u8)
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CallbackUrl(self):
        r"""支持HTTP和HTTPS协议，用于接收识别结果，您需要自行搭建公网可调用的服务。回调格式&内容详见：[语音流异步识别回调说明](https://cloud.tencent.com/document/product/1093/52633)
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def SignToken(self):
        r"""用于生成回调通知中的签名
        :rtype: str
        """
        return self._SignToken

    @SignToken.setter
    def SignToken(self, SignToken):
        self._SignToken = SignToken

    @property
    def FilterDirty(self):
        r"""是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0
        :rtype: int
        """
        return self._FilterDirty

    @FilterDirty.setter
    def FilterDirty(self, FilterDirty):
        self._FilterDirty = FilterDirty

    @property
    def FilterModal(self):
        r"""是否过滤语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0
        :rtype: int
        """
        return self._FilterModal

    @FilterModal.setter
    def FilterModal(self, FilterModal):
        self._FilterModal = FilterModal

    @property
    def FilterPunc(self):
        r"""是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认为0
        :rtype: int
        """
        return self._FilterPunc

    @FilterPunc.setter
    def FilterPunc(self, FilterPunc):
        self._FilterPunc = FilterPunc

    @property
    def ConvertNumMode(self):
        r"""是否进行阿拉伯数字智能转换。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1
        :rtype: int
        """
        return self._ConvertNumMode

    @ConvertNumMode.setter
    def ConvertNumMode(self, ConvertNumMode):
        self._ConvertNumMode = ConvertNumMode

    @property
    def WordInfo(self):
        r"""是否显示词级别时间戳。0：不显示；1：显示，不包含标点时间戳，2：显示，包含标点时间戳。默认为0
        :rtype: int
        """
        return self._WordInfo

    @WordInfo.setter
    def WordInfo(self, WordInfo):
        self._WordInfo = WordInfo

    @property
    def HotwordId(self):
        r"""热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
        :rtype: str
        """
        return self._HotwordId

    @HotwordId.setter
    def HotwordId(self, HotwordId):
        self._HotwordId = HotwordId

    @property
    def AudioData(self):
        r"""回调数据中，是否需要对应音频数据。
        :rtype: bool
        """
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
    r"""CreateAsyncRecognitionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 请求返回结果，包含本次的任务ID(TaskId)
        :type Data: :class:`tencentcloud.asr.v20190614.models.Task`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""请求返回结果，包含本次的任务ID(TaskId)
        :rtype: :class:`tencentcloud.asr.v20190614.models.Task`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""CreateCustomization请求参数结构体

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
        r"""自学习模型名称，需在1-20字符之间
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def TextUrl(self):
        r"""文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :rtype: str
        """
        return self._TextUrl

    @TextUrl.setter
    def TextUrl(self, TextUrl):
        self._TextUrl = TextUrl

    @property
    def ModelType(self):
        r"""自学习模型类型，填写8k或者16k
        :rtype: str
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def TagInfos(self):
        warnings.warn("parameter `TagInfos` is deprecated", DeprecationWarning) 

        r"""标签信息
        :rtype: list of str
        """
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        warnings.warn("parameter `TagInfos` is deprecated", DeprecationWarning) 

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
    r"""CreateCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelId = None
        self._RequestId = None

    @property
    def ModelId(self):
        r"""模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._RequestId = params.get("RequestId")


class CreateRecTaskRequest(AbstractModel):
    r"""CreateRecTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineModelType: 引擎模型类型
识别引擎采用分级计费方案，标记为“大模型版”的引擎适用大模型计费方案，[点击这里](https://cloud.tencent.com/document/product/1093/35686) 查看产品计费说明

电话通讯场景引擎：
**注意：电话通讯场景，请务必使用以下8k引擎**
• 8k_zh：中文电话通讯；
• 8k_en：英文电话通讯；
• 8k_zh_large：中文电话场景专用大模型引擎【大模型版】。通过显著提升模型参数规模与语言建模能力，实现对电话音频中复杂场景（如口音干扰、背景噪声）的高精度识别，识别准确率较常规版本大幅提升。[点击这里](https://console.cloud.tencent.com/asr/demonstrate) 对比常规版本与普方大模型效果；

注意：如您有电话通讯场景识别需求，但发现需求语种仅支持16k，可将8k音频传入下方16k引擎，亦能获取识别结果。但**16k引擎并非基于电话通讯数据训练，无法承诺此种调用方式的识别效果，需由您自行验证识别结果是否可用**

通用场景引擎：
**注意：除电话通讯场景以外的其它识别场景，请务必使用以下16k引擎**
• **16k_zh_en**：中英粤+7种方言大模型引擎【大模型版】。当前模型同时支持中文、英语、粤语、四川、陕西、河南、上海、湖南、湖北和安徽方言识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升;
• **16k_zh_large：**普方英大模型引擎【大模型版】。当前模型同时支持中文、英文、[多种中文方言](https://cloud.tencent.com/document/product/1093/35682)等语言的识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升，[点击这里](https://console.cloud.tencent.com/asr/demonstrate) 对比中文普通话常规版本与普方英大模型版本的识别效果；
• **16k_multi_lang：**多语种大模型引擎【大模型版】。当前模型同时支持英语、日语、韩语、阿拉伯语、菲律宾语、法语、印地语、印尼语、马来语、葡萄牙语、西班牙语、泰语、土耳其语、越南语、德语的识别，可实现15个语种的自动识别(句子/段落级别)；
• **16k_zh：**中文普通话通用引擎，支持中文普通话和少量英语，使用丰富的中文普通话语料训练，覆盖场景广泛，适用于除电话通讯外的所有中文普通话识别场景；
• **16k_en：**英语；
• **16k_yue：**粤语；
• **16k_zh-PY：**中英粤混合引擎，使用一个引擎同时识别中文普通话、英语、粤语三个语言;
• **16k_zh-TW**：中文繁体；
• **16k_ja：**日语；
• **16k_ko：**韩语；
• **16k_vi：**越南语；
• **16k_ms：**马来语；
• **16k_id：**印度尼西亚语；
• **16k_fil：**菲律宾语；
• **16k_th：**泰语；
• **16k_pt：**葡萄牙语；
• **16k_tr：**土耳其语；
• **16k_ar：**阿拉伯语；
• **16k_es：**西班牙语；
• **16k_hi：**印地语；
• **16k_fr：**法语；
• **16k_zh_medical：**中文医疗引擎；
• **16k_de：**德语；
        :type EngineModelType: str
        :param _ChannelNum: 识别声道数
1：单声道（16k音频仅支持单声道，**请勿**设置为双声道）；
2：双声道（仅支持8k电话音频，且双声道应分别为通话双方）

注意：
• 16k音频：仅支持单声道识别，**需设置ChannelNum=1**；
• 8k电话音频：支持单声道、双声道识别，**建议设置ChannelNum=2，即双声道**。双声道能够物理区分说话人、避免说话双方重叠产生的识别错误，能达到最好的说话人分离效果和识别效果。设置双声道后，将自动区分说话人，因此**无需再开启说话人分离功能**，相关参数（**SpeakerDiarization、SpeakerNumber**）使用默认值即可，返回的ResultDetail中的speakerId的值为0代表左声道，值为1代表右声道。
        :type ChannelNum: int
        :param _ResTextFormat: 识别结果返回样式
0：基础识别结果（仅包含有效人声时间戳，无词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)）；
1：基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值，**不含标点**）；
2：基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值和标点）；
3：基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值和标点），且识别结果按标点符号分段，**适用字幕场景**；
4：**【增值付费功能】**基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值和标点），且识别结果按nlp语义分段，**适用会议、庭审记录转写等场景**，仅支持8k_zh/16k_zh引擎
5：**【增值付费功能】**基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值和标点），并输出口语转书面语转写结果，该结果去除语气词、重复词、精简冗余表达，并修正发言人口误，实现口语转书面语的效果，**适用于线上、线下会议直接总结为书面会议纪要的场景**，仅支持8k_zh/16k_zh引擎

注意：
以下引擎仅支持参数值设置为0：16k_multi_lang、16k_ja、16k_ko、16k_vi、16k_ms、16k_id、16k_fil、16k_th、16k_pt、16k_tr、16k_ar、16k_es、16k_hi、16k_fr、16k_zh_medical、16k_de
如果传入参数值4，需确保账号已购买[语义分段资源包](https://cloud.tencent.com/document/product/1093/35686#97ae4aa0-29a0-4066-9f07-ccaf8856a16b)，或账号开启后付费；**若当前账号已开启后付费功能，并传入参数值4，将[自动计费](https://cloud.tencent.com/document/product/1093/35686#d912167d-ffd5-41a9-8b1c-2e89845a6852)**
如果传入参数值5，需确保账号已购买[口语转书面语资源包](https://cloud.tencent.com/document/product/1093/35686#97ae4aa0-29a0-4066-9f07-ccaf8856a16b)，或账号开启后付费；**若当前账号已开启后付费功能，并传入参数值5，将自动计费[自动计费](https://cloud.tencent.com/document/product/1093/35686#d912167d-ffd5-41a9-8b1c-2e89845a6852)**
        :type ResTextFormat: int
        :param _SourceType: 音频数据来源
0：音频URL；
1：音频数据（post body）
        :type SourceType: int
        :param _Data: 音频数据base64编码
**当 SourceType 值为 1 时须填写该字段，为 0 时不需要填写**

注意：音频数据要小于5MB（含）
        :type Data: str
        :param _DataLen: 数据长度（此数据长度为数据未进行base64编码时的长度）
        :type DataLen: int
        :param _Url: 音频URL的地址（需要公网环境浏览器可下载）
**当 SourceType 值为 0 时须填写该字段，为 1 时不需要填写**

注意：
1. 请确保录音文件时长在5个小时（含）之内，否则可能识别失败；
2. 请保证文件的下载速度，否则可能下载失败
        :type Url: str
        :param _CallbackUrl: 回调 URL
用户自行搭建的用于接收识别结果的服务URL
回调格式和内容详见：[录音识别回调说明](https://cloud.tencent.com/document/product/1093/52632)

注意：

- 如果用户使用轮询方式获取识别结果，则无需提交该参数
- 建议在回调URL中带上您的业务ID等信息，以便处理业务逻辑
        :type CallbackUrl: str
        :param _SpeakerDiarization: 是否开启说话人分离
0：不开启；
1：开启（仅支持以下引擎：8k_zh/16k_zh/16k_ms/16k_en/16k_id/16k_zh_large/16k_zh_dialect/16k_zh_en，且ChannelNum=1时可用）；
默认值为 0

注意：
8k双声道电话音频请按 **ChannelNum 识别声道数** 的参数描述使用默认值
        :type SpeakerDiarization: int
        :param _SpeakerNumber: 说话人分离人数
**需配合开启说话人分离使用，不开启无效**，取值范围：0-10
0：自动分离（最多分离出20个人）；
1-10：指定人数分离；
默认值为 0
注:16k引擎不支持指定人数分离
        :type SpeakerNumber: int
        :param _HotwordId: 热词表id
如不设置该参数，将自动生效默认热词表；
如设置该参数，将生效对应id的热词表；
点击这里查看[热词表配置方法](https://cloud.tencent.com/document/product/1093/40996)
        :type HotwordId: str
        :param _ReinforceHotword: 热词增强功能（目前仅支持8k_zh/16k_zh引擎）
1：开启热词增强功能

注意：热词增强功能开启后，将对传入的热词表id开启同音替换功能，可以在这里查看[热词表配置方法](https://cloud.tencent.com/document/product/1093/40996)。效果举例：在热词表中配置“蜜制”一词，并开启增强功能，与“蜜制”（mìzhì）同音同调的“秘制”（mìzhì）的识别结果会被强制替换成“蜜制”。**建议客户根据实际的业务需求开启该功能**
        :type ReinforceHotword: int
        :param _CustomizationId: 自学习定制模型 id
如设置了该参数，将生效对应id的自学习定制模型；
点击这里查看[自学习定制模型配置方法](https://cloud.tencent.com/document/product/1093/38416)
        :type CustomizationId: str
        :param _EmotionRecognition: **【增值付费功能】**情绪识别能力（目前仅支持16k_zh,8k_zh）
0：不开启；
1：开启情绪识别，但不在文本展示情绪标签；
2：开启情绪识别，并且在文本展示情绪标签（**该功能需要设置ResTextFormat 大于0**）
默认值为0
支持的情绪分类为：高兴、伤心、愤怒

注意：
1. **本功能为增值服务**，需将参数设置为1或2时方可按对应方式生效；
2. 如果传入参数值1或2，需确保账号已购买[情绪识别资源包](https://cloud.tencent.com/document/product/1093/35686#97ae4aa0-29a0-4066-9f07-ccaf8856a16b)，或账号开启后付费；**若当前账号已开启后付费功能，并传入参数值1或2，将[自动计费](https://cloud.tencent.com/document/product/1093/35686#d912167d-ffd5-41a9-8b1c-2e89845a6852)）**；
3. 参数设置为0时，无需购买资源包，也不会消耗情绪识别对应资源
        :type EmotionRecognition: int
        :param _EmotionalEnergy: 情绪能量值
取值为音量分贝值/10，取值范围：[1,10]，值越高情绪越强烈
0：不开启；
1：开启；
默认值为0
        :type EmotionalEnergy: int
        :param _ConvertNumMode: 阿拉伯数字智能转换（目前支持中文普通话引擎）
0：不转换，直接输出中文数字；
1：根据场景智能转换为阿拉伯数字；
3：打开数学相关数字转换（如：阿尔法转写为α）；
默认值为 1
        :type ConvertNumMode: int
        :param _FilterDirty: 脏词过滤（目前支持中文普通话引擎）
0：不过滤脏词；
1：过滤脏词；
2：将脏词替换为 * ；
默认值为 0
        :type FilterDirty: int
        :param _FilterPunc: 标点符号过滤（目前支持中文普通话引擎）
0：不过滤标点；
1：过滤句末标点；
2：过滤所有标点；
默认值为 0
        :type FilterPunc: int
        :param _FilterModal: 语气词过滤（目前支持中文普通话引擎）
0：不过滤语气词；
1：过滤部分语气词；
2：严格过滤语气词；
默认值为 0
        :type FilterModal: int
        :param _SentenceMaxLength: 单标点最多字数（目前支持中文普通话引擎）
**可控制单行字幕最大字数，适用于字幕生成场景**，取值范围：[6，40]
0：不开启该功能；
默认值为0

注意：需设置ResTextFormat为3，解析返回的ResultDetail列表，通过结构中FinalSentence获取单个标点断句结果
        :type SentenceMaxLength: int
        :param _Extra: 附加参数**（该参数无意义，忽略即可）**
        :type Extra: str
        :param _HotwordList: 临时热词表：该参数用于提升识别准确率。

- 单个热词限制："热词|权重"，单个热词不超过30个字符（最多10个汉字），权重[1-11]或者100，如：“腾讯云|5” 或“ASR|11”；

- 临时热词表限制：多个热词用英文逗号分割，最多支持128个热词，如：“腾讯云|10,语音识别|5,ASR|11”；

- 参数 hotword_id（热词表） 与 hotword_list（临时热词表） 区别：

    - hotword_id：热词表。需要先在控制台或接口创建热词表，获得对应hotword_id传入参数来使用热词功能；

    - hotword_list：临时热词表。每次请求时直接传入临时热词表来使用热词功能，云端不保留临时热词表。适用于有极大量热词需求的用户；

注意：

- 如果同时传入了 hotword_id 和 hotword_list，只有hotword_list 生效；

- 热词权重设置为11时，当前热词将升级为超级热词，建议仅将重要且必须生效的热词设置到11，设置过多权重为11的热词将影响整体字准率。

- 热词权重设置为100时，当前热词开启热词增强同音替换功能（仅支持8k_zh,16k_zh），举例：热词配置“蜜制|100”时，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。建议仅将重要且必须生效的热词设置到100，设置过多权重为100的热词将影响整体字准率。
        :type HotwordList: str
        :param _KeyWordLibIdList: 关键词识别ID列表，默认空为不进行识别，最多10个

        :type KeyWordLibIdList: list of str
        :param _ReplaceTextId: 替换词汇表id,  适用于热词和自学习场景也无法解决的极端case词组,  会对识别结果强制替换。具体可参考[配置控制台](https://console.cloud.tencent.com/asr/replaceword);强制替换功能可能会影响正常识别结果，请谨慎使用

注意：
1. 本功能配置完成后，预计在10分钟后生效

        :type ReplaceTextId: str
        """
        self._EngineModelType = None
        self._ChannelNum = None
        self._ResTextFormat = None
        self._SourceType = None
        self._Data = None
        self._DataLen = None
        self._Url = None
        self._CallbackUrl = None
        self._SpeakerDiarization = None
        self._SpeakerNumber = None
        self._HotwordId = None
        self._ReinforceHotword = None
        self._CustomizationId = None
        self._EmotionRecognition = None
        self._EmotionalEnergy = None
        self._ConvertNumMode = None
        self._FilterDirty = None
        self._FilterPunc = None
        self._FilterModal = None
        self._SentenceMaxLength = None
        self._Extra = None
        self._HotwordList = None
        self._KeyWordLibIdList = None
        self._ReplaceTextId = None

    @property
    def EngineModelType(self):
        r"""引擎模型类型
识别引擎采用分级计费方案，标记为“大模型版”的引擎适用大模型计费方案，[点击这里](https://cloud.tencent.com/document/product/1093/35686) 查看产品计费说明

电话通讯场景引擎：
**注意：电话通讯场景，请务必使用以下8k引擎**
• 8k_zh：中文电话通讯；
• 8k_en：英文电话通讯；
• 8k_zh_large：中文电话场景专用大模型引擎【大模型版】。通过显著提升模型参数规模与语言建模能力，实现对电话音频中复杂场景（如口音干扰、背景噪声）的高精度识别，识别准确率较常规版本大幅提升。[点击这里](https://console.cloud.tencent.com/asr/demonstrate) 对比常规版本与普方大模型效果；

注意：如您有电话通讯场景识别需求，但发现需求语种仅支持16k，可将8k音频传入下方16k引擎，亦能获取识别结果。但**16k引擎并非基于电话通讯数据训练，无法承诺此种调用方式的识别效果，需由您自行验证识别结果是否可用**

通用场景引擎：
**注意：除电话通讯场景以外的其它识别场景，请务必使用以下16k引擎**
• **16k_zh_en**：中英粤+7种方言大模型引擎【大模型版】。当前模型同时支持中文、英语、粤语、四川、陕西、河南、上海、湖南、湖北和安徽方言识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升;
• **16k_zh_large：**普方英大模型引擎【大模型版】。当前模型同时支持中文、英文、[多种中文方言](https://cloud.tencent.com/document/product/1093/35682)等语言的识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升，[点击这里](https://console.cloud.tencent.com/asr/demonstrate) 对比中文普通话常规版本与普方英大模型版本的识别效果；
• **16k_multi_lang：**多语种大模型引擎【大模型版】。当前模型同时支持英语、日语、韩语、阿拉伯语、菲律宾语、法语、印地语、印尼语、马来语、葡萄牙语、西班牙语、泰语、土耳其语、越南语、德语的识别，可实现15个语种的自动识别(句子/段落级别)；
• **16k_zh：**中文普通话通用引擎，支持中文普通话和少量英语，使用丰富的中文普通话语料训练，覆盖场景广泛，适用于除电话通讯外的所有中文普通话识别场景；
• **16k_en：**英语；
• **16k_yue：**粤语；
• **16k_zh-PY：**中英粤混合引擎，使用一个引擎同时识别中文普通话、英语、粤语三个语言;
• **16k_zh-TW**：中文繁体；
• **16k_ja：**日语；
• **16k_ko：**韩语；
• **16k_vi：**越南语；
• **16k_ms：**马来语；
• **16k_id：**印度尼西亚语；
• **16k_fil：**菲律宾语；
• **16k_th：**泰语；
• **16k_pt：**葡萄牙语；
• **16k_tr：**土耳其语；
• **16k_ar：**阿拉伯语；
• **16k_es：**西班牙语；
• **16k_hi：**印地语；
• **16k_fr：**法语；
• **16k_zh_medical：**中文医疗引擎；
• **16k_de：**德语；
        :rtype: str
        """
        return self._EngineModelType

    @EngineModelType.setter
    def EngineModelType(self, EngineModelType):
        self._EngineModelType = EngineModelType

    @property
    def ChannelNum(self):
        r"""识别声道数
1：单声道（16k音频仅支持单声道，**请勿**设置为双声道）；
2：双声道（仅支持8k电话音频，且双声道应分别为通话双方）

注意：
• 16k音频：仅支持单声道识别，**需设置ChannelNum=1**；
• 8k电话音频：支持单声道、双声道识别，**建议设置ChannelNum=2，即双声道**。双声道能够物理区分说话人、避免说话双方重叠产生的识别错误，能达到最好的说话人分离效果和识别效果。设置双声道后，将自动区分说话人，因此**无需再开启说话人分离功能**，相关参数（**SpeakerDiarization、SpeakerNumber**）使用默认值即可，返回的ResultDetail中的speakerId的值为0代表左声道，值为1代表右声道。
        :rtype: int
        """
        return self._ChannelNum

    @ChannelNum.setter
    def ChannelNum(self, ChannelNum):
        self._ChannelNum = ChannelNum

    @property
    def ResTextFormat(self):
        r"""识别结果返回样式
0：基础识别结果（仅包含有效人声时间戳，无词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)）；
1：基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值，**不含标点**）；
2：基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值和标点）；
3：基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值和标点），且识别结果按标点符号分段，**适用字幕场景**；
4：**【增值付费功能】**基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值和标点），且识别结果按nlp语义分段，**适用会议、庭审记录转写等场景**，仅支持8k_zh/16k_zh引擎
5：**【增值付费功能】**基础识别结果之上，增加词粒度的[详细识别结果](https://cloud.tencent.com/document/api/1093/37824#SentenceDetail)（包含词级别时间戳、语速值和标点），并输出口语转书面语转写结果，该结果去除语气词、重复词、精简冗余表达，并修正发言人口误，实现口语转书面语的效果，**适用于线上、线下会议直接总结为书面会议纪要的场景**，仅支持8k_zh/16k_zh引擎

注意：
以下引擎仅支持参数值设置为0：16k_multi_lang、16k_ja、16k_ko、16k_vi、16k_ms、16k_id、16k_fil、16k_th、16k_pt、16k_tr、16k_ar、16k_es、16k_hi、16k_fr、16k_zh_medical、16k_de
如果传入参数值4，需确保账号已购买[语义分段资源包](https://cloud.tencent.com/document/product/1093/35686#97ae4aa0-29a0-4066-9f07-ccaf8856a16b)，或账号开启后付费；**若当前账号已开启后付费功能，并传入参数值4，将[自动计费](https://cloud.tencent.com/document/product/1093/35686#d912167d-ffd5-41a9-8b1c-2e89845a6852)**
如果传入参数值5，需确保账号已购买[口语转书面语资源包](https://cloud.tencent.com/document/product/1093/35686#97ae4aa0-29a0-4066-9f07-ccaf8856a16b)，或账号开启后付费；**若当前账号已开启后付费功能，并传入参数值5，将自动计费[自动计费](https://cloud.tencent.com/document/product/1093/35686#d912167d-ffd5-41a9-8b1c-2e89845a6852)**
        :rtype: int
        """
        return self._ResTextFormat

    @ResTextFormat.setter
    def ResTextFormat(self, ResTextFormat):
        self._ResTextFormat = ResTextFormat

    @property
    def SourceType(self):
        r"""音频数据来源
0：音频URL；
1：音频数据（post body）
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Data(self):
        r"""音频数据base64编码
**当 SourceType 值为 1 时须填写该字段，为 0 时不需要填写**

注意：音频数据要小于5MB（含）
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DataLen(self):
        r"""数据长度（此数据长度为数据未进行base64编码时的长度）
        :rtype: int
        """
        return self._DataLen

    @DataLen.setter
    def DataLen(self, DataLen):
        self._DataLen = DataLen

    @property
    def Url(self):
        r"""音频URL的地址（需要公网环境浏览器可下载）
**当 SourceType 值为 0 时须填写该字段，为 1 时不需要填写**

注意：
1. 请确保录音文件时长在5个小时（含）之内，否则可能识别失败；
2. 请保证文件的下载速度，否则可能下载失败
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CallbackUrl(self):
        r"""回调 URL
用户自行搭建的用于接收识别结果的服务URL
回调格式和内容详见：[录音识别回调说明](https://cloud.tencent.com/document/product/1093/52632)

注意：

- 如果用户使用轮询方式获取识别结果，则无需提交该参数
- 建议在回调URL中带上您的业务ID等信息，以便处理业务逻辑
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def SpeakerDiarization(self):
        r"""是否开启说话人分离
0：不开启；
1：开启（仅支持以下引擎：8k_zh/16k_zh/16k_ms/16k_en/16k_id/16k_zh_large/16k_zh_dialect/16k_zh_en，且ChannelNum=1时可用）；
默认值为 0

注意：
8k双声道电话音频请按 **ChannelNum 识别声道数** 的参数描述使用默认值
        :rtype: int
        """
        return self._SpeakerDiarization

    @SpeakerDiarization.setter
    def SpeakerDiarization(self, SpeakerDiarization):
        self._SpeakerDiarization = SpeakerDiarization

    @property
    def SpeakerNumber(self):
        r"""说话人分离人数
**需配合开启说话人分离使用，不开启无效**，取值范围：0-10
0：自动分离（最多分离出20个人）；
1-10：指定人数分离；
默认值为 0
注:16k引擎不支持指定人数分离
        :rtype: int
        """
        return self._SpeakerNumber

    @SpeakerNumber.setter
    def SpeakerNumber(self, SpeakerNumber):
        self._SpeakerNumber = SpeakerNumber

    @property
    def HotwordId(self):
        r"""热词表id
如不设置该参数，将自动生效默认热词表；
如设置该参数，将生效对应id的热词表；
点击这里查看[热词表配置方法](https://cloud.tencent.com/document/product/1093/40996)
        :rtype: str
        """
        return self._HotwordId

    @HotwordId.setter
    def HotwordId(self, HotwordId):
        self._HotwordId = HotwordId

    @property
    def ReinforceHotword(self):
        warnings.warn("parameter `ReinforceHotword` is deprecated", DeprecationWarning) 

        r"""热词增强功能（目前仅支持8k_zh/16k_zh引擎）
1：开启热词增强功能

注意：热词增强功能开启后，将对传入的热词表id开启同音替换功能，可以在这里查看[热词表配置方法](https://cloud.tencent.com/document/product/1093/40996)。效果举例：在热词表中配置“蜜制”一词，并开启增强功能，与“蜜制”（mìzhì）同音同调的“秘制”（mìzhì）的识别结果会被强制替换成“蜜制”。**建议客户根据实际的业务需求开启该功能**
        :rtype: int
        """
        return self._ReinforceHotword

    @ReinforceHotword.setter
    def ReinforceHotword(self, ReinforceHotword):
        warnings.warn("parameter `ReinforceHotword` is deprecated", DeprecationWarning) 

        self._ReinforceHotword = ReinforceHotword

    @property
    def CustomizationId(self):
        r"""自学习定制模型 id
如设置了该参数，将生效对应id的自学习定制模型；
点击这里查看[自学习定制模型配置方法](https://cloud.tencent.com/document/product/1093/38416)
        :rtype: str
        """
        return self._CustomizationId

    @CustomizationId.setter
    def CustomizationId(self, CustomizationId):
        self._CustomizationId = CustomizationId

    @property
    def EmotionRecognition(self):
        r"""**【增值付费功能】**情绪识别能力（目前仅支持16k_zh,8k_zh）
0：不开启；
1：开启情绪识别，但不在文本展示情绪标签；
2：开启情绪识别，并且在文本展示情绪标签（**该功能需要设置ResTextFormat 大于0**）
默认值为0
支持的情绪分类为：高兴、伤心、愤怒

注意：
1. **本功能为增值服务**，需将参数设置为1或2时方可按对应方式生效；
2. 如果传入参数值1或2，需确保账号已购买[情绪识别资源包](https://cloud.tencent.com/document/product/1093/35686#97ae4aa0-29a0-4066-9f07-ccaf8856a16b)，或账号开启后付费；**若当前账号已开启后付费功能，并传入参数值1或2，将[自动计费](https://cloud.tencent.com/document/product/1093/35686#d912167d-ffd5-41a9-8b1c-2e89845a6852)）**；
3. 参数设置为0时，无需购买资源包，也不会消耗情绪识别对应资源
        :rtype: int
        """
        return self._EmotionRecognition

    @EmotionRecognition.setter
    def EmotionRecognition(self, EmotionRecognition):
        self._EmotionRecognition = EmotionRecognition

    @property
    def EmotionalEnergy(self):
        r"""情绪能量值
取值为音量分贝值/10，取值范围：[1,10]，值越高情绪越强烈
0：不开启；
1：开启；
默认值为0
        :rtype: int
        """
        return self._EmotionalEnergy

    @EmotionalEnergy.setter
    def EmotionalEnergy(self, EmotionalEnergy):
        self._EmotionalEnergy = EmotionalEnergy

    @property
    def ConvertNumMode(self):
        r"""阿拉伯数字智能转换（目前支持中文普通话引擎）
0：不转换，直接输出中文数字；
1：根据场景智能转换为阿拉伯数字；
3：打开数学相关数字转换（如：阿尔法转写为α）；
默认值为 1
        :rtype: int
        """
        return self._ConvertNumMode

    @ConvertNumMode.setter
    def ConvertNumMode(self, ConvertNumMode):
        self._ConvertNumMode = ConvertNumMode

    @property
    def FilterDirty(self):
        r"""脏词过滤（目前支持中文普通话引擎）
0：不过滤脏词；
1：过滤脏词；
2：将脏词替换为 * ；
默认值为 0
        :rtype: int
        """
        return self._FilterDirty

    @FilterDirty.setter
    def FilterDirty(self, FilterDirty):
        self._FilterDirty = FilterDirty

    @property
    def FilterPunc(self):
        r"""标点符号过滤（目前支持中文普通话引擎）
0：不过滤标点；
1：过滤句末标点；
2：过滤所有标点；
默认值为 0
        :rtype: int
        """
        return self._FilterPunc

    @FilterPunc.setter
    def FilterPunc(self, FilterPunc):
        self._FilterPunc = FilterPunc

    @property
    def FilterModal(self):
        r"""语气词过滤（目前支持中文普通话引擎）
0：不过滤语气词；
1：过滤部分语气词；
2：严格过滤语气词；
默认值为 0
        :rtype: int
        """
        return self._FilterModal

    @FilterModal.setter
    def FilterModal(self, FilterModal):
        self._FilterModal = FilterModal

    @property
    def SentenceMaxLength(self):
        r"""单标点最多字数（目前支持中文普通话引擎）
**可控制单行字幕最大字数，适用于字幕生成场景**，取值范围：[6，40]
0：不开启该功能；
默认值为0

注意：需设置ResTextFormat为3，解析返回的ResultDetail列表，通过结构中FinalSentence获取单个标点断句结果
        :rtype: int
        """
        return self._SentenceMaxLength

    @SentenceMaxLength.setter
    def SentenceMaxLength(self, SentenceMaxLength):
        self._SentenceMaxLength = SentenceMaxLength

    @property
    def Extra(self):
        r"""附加参数**（该参数无意义，忽略即可）**
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def HotwordList(self):
        r"""临时热词表：该参数用于提升识别准确率。

- 单个热词限制："热词|权重"，单个热词不超过30个字符（最多10个汉字），权重[1-11]或者100，如：“腾讯云|5” 或“ASR|11”；

- 临时热词表限制：多个热词用英文逗号分割，最多支持128个热词，如：“腾讯云|10,语音识别|5,ASR|11”；

- 参数 hotword_id（热词表） 与 hotword_list（临时热词表） 区别：

    - hotword_id：热词表。需要先在控制台或接口创建热词表，获得对应hotword_id传入参数来使用热词功能；

    - hotword_list：临时热词表。每次请求时直接传入临时热词表来使用热词功能，云端不保留临时热词表。适用于有极大量热词需求的用户；

注意：

- 如果同时传入了 hotword_id 和 hotword_list，只有hotword_list 生效；

- 热词权重设置为11时，当前热词将升级为超级热词，建议仅将重要且必须生效的热词设置到11，设置过多权重为11的热词将影响整体字准率。

- 热词权重设置为100时，当前热词开启热词增强同音替换功能（仅支持8k_zh,16k_zh），举例：热词配置“蜜制|100”时，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。建议仅将重要且必须生效的热词设置到100，设置过多权重为100的热词将影响整体字准率。
        :rtype: str
        """
        return self._HotwordList

    @HotwordList.setter
    def HotwordList(self, HotwordList):
        self._HotwordList = HotwordList

    @property
    def KeyWordLibIdList(self):
        r"""关键词识别ID列表，默认空为不进行识别，最多10个

        :rtype: list of str
        """
        return self._KeyWordLibIdList

    @KeyWordLibIdList.setter
    def KeyWordLibIdList(self, KeyWordLibIdList):
        self._KeyWordLibIdList = KeyWordLibIdList

    @property
    def ReplaceTextId(self):
        r"""替换词汇表id,  适用于热词和自学习场景也无法解决的极端case词组,  会对识别结果强制替换。具体可参考[配置控制台](https://console.cloud.tencent.com/asr/replaceword);强制替换功能可能会影响正常识别结果，请谨慎使用

注意：
1. 本功能配置完成后，预计在10分钟后生效

        :rtype: str
        """
        return self._ReplaceTextId

    @ReplaceTextId.setter
    def ReplaceTextId(self, ReplaceTextId):
        self._ReplaceTextId = ReplaceTextId


    def _deserialize(self, params):
        self._EngineModelType = params.get("EngineModelType")
        self._ChannelNum = params.get("ChannelNum")
        self._ResTextFormat = params.get("ResTextFormat")
        self._SourceType = params.get("SourceType")
        self._Data = params.get("Data")
        self._DataLen = params.get("DataLen")
        self._Url = params.get("Url")
        self._CallbackUrl = params.get("CallbackUrl")
        self._SpeakerDiarization = params.get("SpeakerDiarization")
        self._SpeakerNumber = params.get("SpeakerNumber")
        self._HotwordId = params.get("HotwordId")
        self._ReinforceHotword = params.get("ReinforceHotword")
        self._CustomizationId = params.get("CustomizationId")
        self._EmotionRecognition = params.get("EmotionRecognition")
        self._EmotionalEnergy = params.get("EmotionalEnergy")
        self._ConvertNumMode = params.get("ConvertNumMode")
        self._FilterDirty = params.get("FilterDirty")
        self._FilterPunc = params.get("FilterPunc")
        self._FilterModal = params.get("FilterModal")
        self._SentenceMaxLength = params.get("SentenceMaxLength")
        self._Extra = params.get("Extra")
        self._HotwordList = params.get("HotwordList")
        self._KeyWordLibIdList = params.get("KeyWordLibIdList")
        self._ReplaceTextId = params.get("ReplaceTextId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecTaskResponse(AbstractModel):
    r"""CreateRecTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 录音文件识别的请求返回结果，包含结果查询需要的TaskId。
**注意：TaskId有效期为24小时，不同日期可能出现重复TaskId，请不要依赖TaskId作为您业务系统里的唯一ID。**

        :type Data: :class:`tencentcloud.asr.v20190614.models.Task`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""录音文件识别的请求返回结果，包含结果查询需要的TaskId。
**注意：TaskId有效期为24小时，不同日期可能出现重复TaskId，请不要依赖TaskId作为您业务系统里的唯一ID。**

        :rtype: :class:`tencentcloud.asr.v20190614.models.Task`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteAsrKeyWordLibRequest(AbstractModel):
    r"""DeleteAsrKeyWordLib请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyWordLibId: 关键词表ID
        :type KeyWordLibId: str
        """
        self._KeyWordLibId = None

    @property
    def KeyWordLibId(self):
        r"""关键词表ID
        :rtype: str
        """
        return self._KeyWordLibId

    @KeyWordLibId.setter
    def KeyWordLibId(self, KeyWordLibId):
        self._KeyWordLibId = KeyWordLibId


    def _deserialize(self, params):
        self._KeyWordLibId = params.get("KeyWordLibId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAsrKeyWordLibResponse(AbstractModel):
    r"""DeleteAsrKeyWordLib返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAsrVocabRequest(AbstractModel):
    r"""DeleteAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表Id
        :type VocabId: str
        """
        self._VocabId = None

    @property
    def VocabId(self):
        r"""热词表Id
        :rtype: str
        """
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
    r"""DeleteAsrVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCustomizationRequest(AbstractModel):
    r"""DeleteCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 要删除的模型ID
        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        r"""要删除的模型ID
        :rtype: str
        """
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
    r"""DeleteCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAsyncRecognitionTasksRequest(AbstractModel):
    r"""DescribeAsyncRecognitionTasks请求参数结构体

    """


class DescribeAsyncRecognitionTasksResponse(AbstractModel):
    r"""DescribeAsyncRecognitionTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.asr.v20190614.models.AsyncRecognitionTasks`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.asr.v20190614.models.AsyncRecognitionTasks`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 从CreateRecTask接口获取的TaskId，用于获取任务状态与结果。
**注意：TaskId有效期为24小时，超过24小时的TaskId请不要再查询。**
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""从CreateRecTask接口获取的TaskId，用于获取任务状态与结果。
**注意：TaskId有效期为24小时，超过24小时的TaskId请不要再查询。**
        :rtype: int
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
        


class DescribeTaskStatusResponse(AbstractModel):
    r"""DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 录音文件识别的请求返回结果。
        :type Data: :class:`tencentcloud.asr.v20190614.models.TaskStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""录音文件识别的请求返回结果。
        :rtype: :class:`tencentcloud.asr.v20190614.models.TaskStatus`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""DownloadAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 词表ID。
        :type VocabId: str
        """
        self._VocabId = None

    @property
    def VocabId(self):
        r"""词表ID。
        :rtype: str
        """
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
    r"""DownloadAsrVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 词表ID。
        :type VocabId: str
        :param _WordWeightStr: 词表权重文件形式的base64值。
        :type WordWeightStr: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabId = None
        self._WordWeightStr = None
        self._RequestId = None

    @property
    def VocabId(self):
        r"""词表ID。
        :rtype: str
        """
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def WordWeightStr(self):
        r"""词表权重文件形式的base64值。
        :rtype: str
        """
        return self._WordWeightStr

    @WordWeightStr.setter
    def WordWeightStr(self, WordWeightStr):
        self._WordWeightStr = WordWeightStr

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._WordWeightStr = params.get("WordWeightStr")
        self._RequestId = params.get("RequestId")


class DownloadCustomizationRequest(AbstractModel):
    r"""DownloadCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 自学习模型ID
        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        r"""自学习模型ID
        :rtype: str
        """
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
    r"""DownloadCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        r"""下载地址
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class GetAsrKeyWordLibListRequest(AbstractModel):
    r"""GetAsrKeyWordLibList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页Offset
        :type Offset: int
        :param _Limit: 分页Limit
        :type Limit: int
        :param _SpecifyNames: 词库名称或者UIN检索
        :type SpecifyNames: list of str
        :param _OnlySelf: 只看用户自己创建的
        :type OnlySelf: bool
        """
        self._Offset = None
        self._Limit = None
        self._SpecifyNames = None
        self._OnlySelf = None

    @property
    def Offset(self):
        r"""分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SpecifyNames(self):
        r"""词库名称或者UIN检索
        :rtype: list of str
        """
        return self._SpecifyNames

    @SpecifyNames.setter
    def SpecifyNames(self, SpecifyNames):
        self._SpecifyNames = SpecifyNames

    @property
    def OnlySelf(self):
        r"""只看用户自己创建的
        :rtype: bool
        """
        return self._OnlySelf

    @OnlySelf.setter
    def OnlySelf(self, OnlySelf):
        self._OnlySelf = OnlySelf


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SpecifyNames = params.get("SpecifyNames")
        self._OnlySelf = params.get("OnlySelf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAsrKeyWordLibListResponse(AbstractModel):
    r"""GetAsrKeyWordLibList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 关键词列表返回数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.KeyWordLibListData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""关键词列表返回数据
        :rtype: :class:`tencentcloud.asr.v20190614.models.KeyWordLibListData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = KeyWordLibListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetAsrVocabListRequest(AbstractModel):
    r"""GetAsrVocabList请求参数结构体

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
        warnings.warn("parameter `TagInfos` is deprecated", DeprecationWarning) 

        r"""标签信息，格式为“$TagKey : $TagValue ”，中间分隔符为“空格”+“:”+“空格”
        :rtype: list of str
        """
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        warnings.warn("parameter `TagInfos` is deprecated", DeprecationWarning) 

        self._TagInfos = TagInfos

    @property
    def Offset(self):
        r"""分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页Limit
        :rtype: int
        """
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
    r"""GetAsrVocabList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabList: 热词表列表
        :type VocabList: list of Vocab
        :param _TotalCount: 热词列表总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def VocabList(self):
        r"""热词表列表
        :rtype: list of Vocab
        """
        return self._VocabList

    @VocabList.setter
    def VocabList(self, VocabList):
        self._VocabList = VocabList

    @property
    def TotalCount(self):
        r"""热词列表总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID
        :type VocabId: str
        """
        self._VocabId = None

    @property
    def VocabId(self):
        r"""热词表ID
        :rtype: str
        """
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
    r"""GetAsrVocab返回参数结构体

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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        r"""热词表名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""热词表描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VocabId(self):
        r"""热词表ID
        :rtype: str
        """
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def WordWeights(self):
        r"""词权重列表
        :rtype: list of HotWord
        """
        return self._WordWeights

    @WordWeights.setter
    def WordWeights(self, WordWeights):
        self._WordWeights = WordWeights

    @property
    def CreateTime(self):
        r"""词表创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""词表更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def State(self):
        r"""热词表状态，1为默认状态即在识别时默认加载该热词表进行识别，0为初始状态
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetCustomizationList请求参数结构体

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
        warnings.warn("parameter `TagInfos` is deprecated", DeprecationWarning) 

        r"""标签信息，格式为“$TagKey : $TagValue ”，中间分隔符为“空格”+“:”+“空格”
        :rtype: list of str
        """
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        warnings.warn("parameter `TagInfos` is deprecated", DeprecationWarning) 

        self._TagInfos = TagInfos

    @property
    def Limit(self):
        r"""分页大小，默认1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页offset，默认0
        :rtype: int
        """
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
    r"""GetCustomizationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 自学习模型数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of Model
        :param _TotalCount: 自学习模型总量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        r"""自学习模型数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Model
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""自学习模型总量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetModelInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型id
        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        r"""模型id
        :rtype: str
        """
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
    r"""GetModelInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 模型信息
        :type Data: :class:`tencentcloud.asr.v20190614.models.Model`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""模型信息
        :rtype: :class:`tencentcloud.asr.v20190614.models.Model`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = Model()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetUsageByDateRequest(AbstractModel):
    r"""GetUsageByDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizNameList: 需要查询的业务类型名字列表
- asr_rt 实时识别
- asr_rec 录音文件识别
        :type BizNameList: list of str
        :param _StartDate: 查询开始时间
开始时间包含当天，支持 YYYY-MM-DD 日期以国内时区为准
开始时间到结束时间需要在3个月以内
        :type StartDate: str
        :param _EndDate: 查询结束时间
结束时间包含当天，，支持 YYYY-MM-DD 日期以国内时区为准
开始时间到结束时间需要在3个月以内
        :type EndDate: str
        """
        self._BizNameList = None
        self._StartDate = None
        self._EndDate = None

    @property
    def BizNameList(self):
        r"""需要查询的业务类型名字列表
- asr_rt 实时识别
- asr_rec 录音文件识别
        :rtype: list of str
        """
        return self._BizNameList

    @BizNameList.setter
    def BizNameList(self, BizNameList):
        self._BizNameList = BizNameList

    @property
    def StartDate(self):
        r"""查询开始时间
开始时间包含当天，支持 YYYY-MM-DD 日期以国内时区为准
开始时间到结束时间需要在3个月以内
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""查询结束时间
结束时间包含当天，，支持 YYYY-MM-DD 日期以国内时区为准
开始时间到结束时间需要在3个月以内
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BizNameList = params.get("BizNameList")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUsageByDateResponse(AbstractModel):
    r"""GetUsageByDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 用量次数
        :type Data: :class:`tencentcloud.asr.v20190614.models.UsageByDateInfoData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""用量次数
        :rtype: :class:`tencentcloud.asr.v20190614.models.UsageByDateInfoData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UsageByDateInfoData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class HotWord(AbstractModel):
    r"""[热词的词和权重](https://cloud.tencent.com/document/product/1093/41111#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0)

    """

    def __init__(self):
        r"""
        :param _Word: 热词
注意：此字段可能返回 null，表示取不到有效值。
        :type Word: str
        :param _Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        """
        self._Word = None
        self._Weight = None

    @property
    def Word(self):
        r"""热词
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def Weight(self):
        r"""权重
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
        


class KeyWordLib(AbstractModel):
    r"""关键词表信息

    """

    def __init__(self):
        r"""
        :param _KeyWordLibId: 关键词表ID
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordLibId: str
        :param _Name: 关键词表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _KeyWordList: 关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordList: list of str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._KeyWordLibId = None
        self._Name = None
        self._KeyWordList = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def KeyWordLibId(self):
        r"""关键词表ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeyWordLibId

    @KeyWordLibId.setter
    def KeyWordLibId(self, KeyWordLibId):
        self._KeyWordLibId = KeyWordLibId

    @property
    def Name(self):
        r"""关键词表名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KeyWordList(self):
        r"""关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._KeyWordList

    @KeyWordList.setter
    def KeyWordList(self, KeyWordList):
        self._KeyWordList = KeyWordList

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._KeyWordLibId = params.get("KeyWordLibId")
        self._Name = params.get("Name")
        self._KeyWordList = params.get("KeyWordList")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyWordLibIdData(AbstractModel):
    r"""关键词ID

    """

    def __init__(self):
        r"""
        :param _KeyWordLibId: 关键词ID
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordLibId: str
        """
        self._KeyWordLibId = None

    @property
    def KeyWordLibId(self):
        r"""关键词ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeyWordLibId

    @KeyWordLibId.setter
    def KeyWordLibId(self, KeyWordLibId):
        self._KeyWordLibId = KeyWordLibId


    def _deserialize(self, params):
        self._KeyWordLibId = params.get("KeyWordLibId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyWordLibListData(AbstractModel):
    r"""查询列表返回数据

    """

    def __init__(self):
        r"""
        :param _KeyWordLibList: 关键词表列表
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordLibList: list of KeyWordLib
        :param _TotalCount: 关键词列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._KeyWordLibList = None
        self._TotalCount = None

    @property
    def KeyWordLibList(self):
        r"""关键词表列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KeyWordLib
        """
        return self._KeyWordLibList

    @KeyWordLibList.setter
    def KeyWordLibList(self, KeyWordLibList):
        self._KeyWordLibList = KeyWordLibList

    @property
    def TotalCount(self):
        r"""关键词列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("KeyWordLibList") is not None:
            self._KeyWordLibList = []
            for item in params.get("KeyWordLibList"):
                obj = KeyWordLib()
                obj._deserialize(item)
                self._KeyWordLibList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyWordResult(AbstractModel):
    r"""关键字识别结果

    """

    def __init__(self):
        r"""
        :param _KeyWordLibID: 关键词库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordLibID: str
        :param _KeyWordLibName: 关键词库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordLibName: str
        :param _KeyWords: 匹配到的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWords: list of str
        """
        self._KeyWordLibID = None
        self._KeyWordLibName = None
        self._KeyWords = None

    @property
    def KeyWordLibID(self):
        r"""关键词库ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeyWordLibID

    @KeyWordLibID.setter
    def KeyWordLibID(self, KeyWordLibID):
        self._KeyWordLibID = KeyWordLibID

    @property
    def KeyWordLibName(self):
        r"""关键词库名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeyWordLibName

    @KeyWordLibName.setter
    def KeyWordLibName(self, KeyWordLibName):
        self._KeyWordLibName = KeyWordLibName

    @property
    def KeyWords(self):
        r"""匹配到的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords


    def _deserialize(self, params):
        self._KeyWordLibID = params.get("KeyWordLibID")
        self._KeyWordLibName = params.get("KeyWordLibName")
        self._KeyWords = params.get("KeyWords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Model(AbstractModel):
    r"""[自学习模型信息](https://cloud.tencent.com/document/product/1093/90813#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)

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
        r"""模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def DictName(self):
        r"""模型文件名称
        :rtype: str
        """
        return self._DictName

    @DictName.setter
    def DictName(self, DictName):
        self._DictName = DictName

    @property
    def ModelId(self):
        r"""模型Id
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelType(self):
        r"""模型类型，“8k”或者”16k“
        :rtype: str
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def ServiceType(self):
        r"""服务类型
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ModelState(self):
        r"""模型状态：
-2：模型训练失败；
-1：已下线；
0：训练中；
1：已上线；
3：上线中；
4：下线中；
        :rtype: int
        """
        return self._ModelState

    @ModelState.setter
    def ModelState(self, ModelState):
        self._ModelState = ModelState

    @property
    def AtUpdated(self):
        r"""最后更新时间
        :rtype: str
        """
        return self._AtUpdated

    @AtUpdated.setter
    def AtUpdated(self, AtUpdated):
        self._AtUpdated = AtUpdated

    @property
    def TagInfos(self):
        warnings.warn("parameter `TagInfos` is deprecated", DeprecationWarning) 

        r"""标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TagInfos

    @TagInfos.setter
    def TagInfos(self, TagInfos):
        warnings.warn("parameter `TagInfos` is deprecated", DeprecationWarning) 

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
    r"""ModifyCustomization请求参数结构体

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
        r"""要修改的模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        r"""要修改的模型名称，长度需在1-20个字符之间
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelType(self):
        r"""要修改的模型类型，为8k或者16k
        :rtype: str
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def TextUrl(self):
        r"""要修改的模型语料的下载地址，目前仅支持腾讯云cos
        :rtype: str
        """
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
    r"""ModifyCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCustomizationStateRequest(AbstractModel):
    r"""ModifyCustomizationState请求参数结构体

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
        r"""自学习模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ToState(self):
        r"""想要变换的模型状态，-1代表下线，1代表上线
        :rtype: int
        """
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
    r"""ModifyCustomizationState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 自学习模型ID
        :type ModelId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelId = None
        self._RequestId = None

    @property
    def ModelId(self):
        r"""自学习模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._RequestId = params.get("RequestId")


class SentenceDetail(AbstractModel):
    r"""单句的详细识别结果，包含单个词的时间偏移，一般用于生成字幕的场景。

    """

    def __init__(self):
        r"""
        :param _FinalSentence: 单句最终识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalSentence: str
        :param _SliceSentence: 单句中间识别结果，使用空格拆分为多个词
注意：此字段可能返回 null，表示取不到有效值。
        :type SliceSentence: str
        :param _WrittenText: 口语转书面语结果，开启改功能才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type WrittenText: str
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
单声道话者分离时不同的值代表不同的说话人； 8k双声道话者分离时speakerId的值为0代表左声道，值为1代表右声道。
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeakerId: int
        :param _EmotionalEnergy: 情绪能量值，取值为音量分贝值/10。取值范围：[1,10]。值越高情绪越强烈。
注意：此字段可能返回 null，表示取不到有效值。
        :type EmotionalEnergy: float
        :param _SilenceTime: 本句与上一句之间的静音时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SilenceTime: int
        :param _EmotionType: 情绪类型（可能为空，有2种情况 1、没有对应资源包；2、情绪跟语音效果相关，如果情绪不够强烈时可能无法识别）
注意：此字段可能返回 null，表示取不到有效值。
        :type EmotionType: list of str
        :param _KeyWordResults: 关键词识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordResults: list of KeyWordResult
        """
        self._FinalSentence = None
        self._SliceSentence = None
        self._WrittenText = None
        self._StartMs = None
        self._EndMs = None
        self._WordsNum = None
        self._Words = None
        self._SpeechSpeed = None
        self._SpeakerId = None
        self._EmotionalEnergy = None
        self._SilenceTime = None
        self._EmotionType = None
        self._KeyWordResults = None

    @property
    def FinalSentence(self):
        r"""单句最终识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FinalSentence

    @FinalSentence.setter
    def FinalSentence(self, FinalSentence):
        self._FinalSentence = FinalSentence

    @property
    def SliceSentence(self):
        r"""单句中间识别结果，使用空格拆分为多个词
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SliceSentence

    @SliceSentence.setter
    def SliceSentence(self, SliceSentence):
        self._SliceSentence = SliceSentence

    @property
    def WrittenText(self):
        r"""口语转书面语结果，开启改功能才有值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WrittenText

    @WrittenText.setter
    def WrittenText(self, WrittenText):
        self._WrittenText = WrittenText

    @property
    def StartMs(self):
        r"""单句开始时间（毫秒）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StartMs

    @StartMs.setter
    def StartMs(self, StartMs):
        self._StartMs = StartMs

    @property
    def EndMs(self):
        r"""单句结束时间（毫秒）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EndMs

    @EndMs.setter
    def EndMs(self, EndMs):
        self._EndMs = EndMs

    @property
    def WordsNum(self):
        r"""单句中词个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WordsNum

    @WordsNum.setter
    def WordsNum(self, WordsNum):
        self._WordsNum = WordsNum

    @property
    def Words(self):
        r"""单句中词详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SentenceWords
        """
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def SpeechSpeed(self):
        r"""单句语速，单位：字数/秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._SpeechSpeed

    @SpeechSpeed.setter
    def SpeechSpeed(self, SpeechSpeed):
        self._SpeechSpeed = SpeechSpeed

    @property
    def SpeakerId(self):
        r"""声道或说话人 Id（请求中如果设置了 speaker_diarization或者ChannelNum为双声道，可区分说话人或声道）
单声道话者分离时不同的值代表不同的说话人； 8k双声道话者分离时speakerId的值为0代表左声道，值为1代表右声道。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SpeakerId

    @SpeakerId.setter
    def SpeakerId(self, SpeakerId):
        self._SpeakerId = SpeakerId

    @property
    def EmotionalEnergy(self):
        r"""情绪能量值，取值为音量分贝值/10。取值范围：[1,10]。值越高情绪越强烈。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._EmotionalEnergy

    @EmotionalEnergy.setter
    def EmotionalEnergy(self, EmotionalEnergy):
        self._EmotionalEnergy = EmotionalEnergy

    @property
    def SilenceTime(self):
        r"""本句与上一句之间的静音时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SilenceTime

    @SilenceTime.setter
    def SilenceTime(self, SilenceTime):
        self._SilenceTime = SilenceTime

    @property
    def EmotionType(self):
        r"""情绪类型（可能为空，有2种情况 1、没有对应资源包；2、情绪跟语音效果相关，如果情绪不够强烈时可能无法识别）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._EmotionType

    @EmotionType.setter
    def EmotionType(self, EmotionType):
        self._EmotionType = EmotionType

    @property
    def KeyWordResults(self):
        r"""关键词识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KeyWordResult
        """
        return self._KeyWordResults

    @KeyWordResults.setter
    def KeyWordResults(self, KeyWordResults):
        self._KeyWordResults = KeyWordResults


    def _deserialize(self, params):
        self._FinalSentence = params.get("FinalSentence")
        self._SliceSentence = params.get("SliceSentence")
        self._WrittenText = params.get("WrittenText")
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
        if params.get("KeyWordResults") is not None:
            self._KeyWordResults = []
            for item in params.get("KeyWordResults"):
                obj = KeyWordResult()
                obj._deserialize(item)
                self._KeyWordResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceRecognitionRequest(AbstractModel):
    r"""SentenceRecognition请求参数结构体

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
• 16k_ar：阿拉伯语；
• 16k_es：西班牙语；
• 16k_hi：印地语；
• 16k_fr：法语；
• 16k_de：德语；
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

注意：推荐使用 [腾讯云COS](https://cloud.tencent.com/document/product/436/38484) 来存储音频、生成URL并提交请求，此种方式会走内网下载音频，极大降低整体请求时延；并且不会产生外网和流量下行费用，可节约成本（COS桶权限需要设置公有读私有写，或URL设置时效访问签名）
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
        :param _FilterModal: 是否过滤语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0。
        :type FilterModal: int
        :param _FilterPunc: 是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认值为 0。
        :type FilterPunc: int
        :param _ConvertNumMode: 是否进行阿拉伯数字智能转换。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1。
        :type ConvertNumMode: int
        :param _HotwordId: 热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
        :type HotwordId: str
        :param _CustomizationId: 自学习模型 id。如设置了该参数，将生效对应的自学习模型。
        :type CustomizationId: str
        :param _ReinforceHotword: 热词增强功能。1:开启后（仅支持8k_zh,16k_zh），将开启同音替换功能，同音字、词在热词中配置。举例：热词配置“蜜制”并开启增强功能后，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。
        :type ReinforceHotword: int
        :param _HotwordList: 临时热词表：该参数用于提升识别准确率。
单个热词限制："热词|权重"，单个热词不超过30个字符（最多10个汉字），权重1-11或者100，如：“腾讯云|5” 或 “ASR|11”；
临时热词表限制：多个热词用英文逗号分割，最多支持128个热词，如：“腾讯云|10,语音识别|5,ASR|11”；
参数 hotword_list（临时热词表） 与 hotword_id（热词表） 区别：
hotword_id：热词表。需要先在控制台或接口创建热词表，获得对应hotword_id传入参数来使用热词功能；
hotword_list：临时热词表。每次请求时直接传入临时热词表来使用热词功能，云端不保留临时热词表。适用于有极大量热词需求的用户；
注意：
• 如果同时传入了 hotword_id 和 hotword_list，会优先使用 hotword_list；
• 热词权重设置为11时，当前热词将升级为超级热词，建议仅将重要且必须生效的热词设置到11，设置过多权重为11的热词将影响整体字准率。
• 热词权重设置为100时，当前热词开启热词增强同音替换功能（仅支持8k_zh,16k_zh），举例：热词配置“蜜制|100”时，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。建议仅将重要且必须生效的热词设置到100，设置过多权重为100的热词将影响整体字准率。
        :type HotwordList: str
        :param _InputSampleRate: 支持pcm格式的8k音频在与引擎采样率不匹配的情况下升采样到16k后识别，能有效提升识别准确率。仅支持：8000。如：传入 8000 ，则pcm音频采样率为8k，当引擎选用16k_zh， 那么该8k采样率的pcm音频可以在16k_zh引擎下正常识别。 注：此参数仅适用于pcm格式音频，不传入值将维持默认状态，即默认调用的引擎采样率等于pcm音频采样率。
        :type InputSampleRate: int
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
        self._InputSampleRate = None

    @property
    def EngSerViceType(self):
        r"""引擎模型类型。
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
• 16k_ar：阿拉伯语；
• 16k_es：西班牙语；
• 16k_hi：印地语；
• 16k_fr：法语；
• 16k_de：德语；
• 16k_zh_dialect：多方言，支持23种方言（上海话、四川话、武汉话、贵阳话、昆明话、西安话、郑州话、太原话、兰州话、银川话、西宁话、南京话、合肥话、南昌话、长沙话、苏州话、杭州话、济南话、天津话、石家庄话、黑龙江话、吉林话、辽宁话）；
        :rtype: str
        """
        return self._EngSerViceType

    @EngSerViceType.setter
    def EngSerViceType(self, EngSerViceType):
        self._EngSerViceType = EngSerViceType

    @property
    def SourceType(self):
        r"""语音数据来源。0：语音 URL；1：语音数据（post body）。
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def VoiceFormat(self):
        r"""识别音频的音频格式，支持wav、pcm、ogg-opus、speex、silk、mp3、m4a、aac、amr。
        :rtype: str
        """
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def ProjectId(self):
        warnings.warn("parameter `ProjectId` is deprecated", DeprecationWarning) 

        r"""腾讯云项目 ID，废弃参数，填写0即可。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        warnings.warn("parameter `ProjectId` is deprecated", DeprecationWarning) 

        self._ProjectId = ProjectId

    @property
    def SubServiceType(self):
        warnings.warn("parameter `SubServiceType` is deprecated", DeprecationWarning) 

        r"""子服务类型。2： 一句话识别。
        :rtype: int
        """
        return self._SubServiceType

    @SubServiceType.setter
    def SubServiceType(self, SubServiceType):
        warnings.warn("parameter `SubServiceType` is deprecated", DeprecationWarning) 

        self._SubServiceType = SubServiceType

    @property
    def Url(self):
        r"""语音的URL地址，需要公网环境浏览器可下载。当 SourceType 值为 0时须填写该字段，为 1 时不填。音频时长不能超过60s，音频文件大小不能超过3MB。

注意：推荐使用 [腾讯云COS](https://cloud.tencent.com/document/product/436/38484) 来存储音频、生成URL并提交请求，此种方式会走内网下载音频，极大降低整体请求时延；并且不会产生外网和流量下行费用，可节约成本（COS桶权限需要设置公有读私有写，或URL设置时效访问签名）
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def UsrAudioKey(self):
        warnings.warn("parameter `UsrAudioKey` is deprecated", DeprecationWarning) 

        r"""废弃参数，填写任意字符串即可。
        :rtype: str
        """
        return self._UsrAudioKey

    @UsrAudioKey.setter
    def UsrAudioKey(self, UsrAudioKey):
        warnings.warn("parameter `UsrAudioKey` is deprecated", DeprecationWarning) 

        self._UsrAudioKey = UsrAudioKey

    @property
    def Data(self):
        r"""语音数据，当SourceType 值为1（本地语音数据上传）时必须填写，当SourceType 值为0（语音 URL上传）可不写。要使用base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频时长不能超过60s，音频文件大小不能超过3MB（Base64后）。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DataLen(self):
        r"""数据长度，单位为字节。当 SourceType 值为1（本地语音数据上传）时必须填写，当 SourceType 值为0（语音 URL上传）可不写（此数据长度为数据未进行base64编码时的数据长度）。
        :rtype: int
        """
        return self._DataLen

    @DataLen.setter
    def DataLen(self, DataLen):
        self._DataLen = DataLen

    @property
    def WordInfo(self):
        r"""是否显示词级别时间戳。0：不显示；1：显示，不包含标点时间戳，2：显示，包含标点时间戳。默认值为 0。
        :rtype: int
        """
        return self._WordInfo

    @WordInfo.setter
    def WordInfo(self, WordInfo):
        self._WordInfo = WordInfo

    @property
    def FilterDirty(self):
        r"""是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0。
        :rtype: int
        """
        return self._FilterDirty

    @FilterDirty.setter
    def FilterDirty(self, FilterDirty):
        self._FilterDirty = FilterDirty

    @property
    def FilterModal(self):
        r"""是否过滤语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0。
        :rtype: int
        """
        return self._FilterModal

    @FilterModal.setter
    def FilterModal(self, FilterModal):
        self._FilterModal = FilterModal

    @property
    def FilterPunc(self):
        r"""是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认值为 0。
        :rtype: int
        """
        return self._FilterPunc

    @FilterPunc.setter
    def FilterPunc(self, FilterPunc):
        self._FilterPunc = FilterPunc

    @property
    def ConvertNumMode(self):
        r"""是否进行阿拉伯数字智能转换。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1。
        :rtype: int
        """
        return self._ConvertNumMode

    @ConvertNumMode.setter
    def ConvertNumMode(self, ConvertNumMode):
        self._ConvertNumMode = ConvertNumMode

    @property
    def HotwordId(self):
        r"""热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
        :rtype: str
        """
        return self._HotwordId

    @HotwordId.setter
    def HotwordId(self, HotwordId):
        self._HotwordId = HotwordId

    @property
    def CustomizationId(self):
        r"""自学习模型 id。如设置了该参数，将生效对应的自学习模型。
        :rtype: str
        """
        return self._CustomizationId

    @CustomizationId.setter
    def CustomizationId(self, CustomizationId):
        self._CustomizationId = CustomizationId

    @property
    def ReinforceHotword(self):
        warnings.warn("parameter `ReinforceHotword` is deprecated", DeprecationWarning) 

        r"""热词增强功能。1:开启后（仅支持8k_zh,16k_zh），将开启同音替换功能，同音字、词在热词中配置。举例：热词配置“蜜制”并开启增强功能后，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。
        :rtype: int
        """
        return self._ReinforceHotword

    @ReinforceHotword.setter
    def ReinforceHotword(self, ReinforceHotword):
        warnings.warn("parameter `ReinforceHotword` is deprecated", DeprecationWarning) 

        self._ReinforceHotword = ReinforceHotword

    @property
    def HotwordList(self):
        r"""临时热词表：该参数用于提升识别准确率。
单个热词限制："热词|权重"，单个热词不超过30个字符（最多10个汉字），权重1-11或者100，如：“腾讯云|5” 或 “ASR|11”；
临时热词表限制：多个热词用英文逗号分割，最多支持128个热词，如：“腾讯云|10,语音识别|5,ASR|11”；
参数 hotword_list（临时热词表） 与 hotword_id（热词表） 区别：
hotword_id：热词表。需要先在控制台或接口创建热词表，获得对应hotword_id传入参数来使用热词功能；
hotword_list：临时热词表。每次请求时直接传入临时热词表来使用热词功能，云端不保留临时热词表。适用于有极大量热词需求的用户；
注意：
• 如果同时传入了 hotword_id 和 hotword_list，会优先使用 hotword_list；
• 热词权重设置为11时，当前热词将升级为超级热词，建议仅将重要且必须生效的热词设置到11，设置过多权重为11的热词将影响整体字准率。
• 热词权重设置为100时，当前热词开启热词增强同音替换功能（仅支持8k_zh,16k_zh），举例：热词配置“蜜制|100”时，与“蜜制”同拼音（mizhi）的“秘制”的识别结果会被强制替换成“蜜制”。因此建议客户根据自己的实际情况开启该功能。建议仅将重要且必须生效的热词设置到100，设置过多权重为100的热词将影响整体字准率。
        :rtype: str
        """
        return self._HotwordList

    @HotwordList.setter
    def HotwordList(self, HotwordList):
        self._HotwordList = HotwordList

    @property
    def InputSampleRate(self):
        r"""支持pcm格式的8k音频在与引擎采样率不匹配的情况下升采样到16k后识别，能有效提升识别准确率。仅支持：8000。如：传入 8000 ，则pcm音频采样率为8k，当引擎选用16k_zh， 那么该8k采样率的pcm音频可以在16k_zh引擎下正常识别。 注：此参数仅适用于pcm格式音频，不传入值将维持默认状态，即默认调用的引擎采样率等于pcm音频采样率。
        :rtype: int
        """
        return self._InputSampleRate

    @InputSampleRate.setter
    def InputSampleRate(self, InputSampleRate):
        self._InputSampleRate = InputSampleRate


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
        self._InputSampleRate = params.get("InputSampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceRecognitionResponse(AbstractModel):
    r"""SentenceRecognition返回参数结构体

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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._AudioDuration = None
        self._WordSize = None
        self._WordList = None
        self._RequestId = None

    @property
    def Result(self):
        r"""识别结果。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def AudioDuration(self):
        r"""请求的音频时长，单位为ms
        :rtype: int
        """
        return self._AudioDuration

    @AudioDuration.setter
    def AudioDuration(self, AudioDuration):
        self._AudioDuration = AudioDuration

    @property
    def WordSize(self):
        r"""词时间戳列表的长度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WordSize

    @WordSize.setter
    def WordSize(self, WordSize):
        self._WordSize = WordSize

    @property
    def WordList(self):
        r"""词时间戳列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SentenceWord
        """
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""[一句话识别](https://cloud.tencent.com/document/product/1093/35646#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)返回的词时间戳

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
        r"""词结果
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def StartTime(self):
        r"""词在音频中的开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""词在音频中的结束时间
        :rtype: int
        """
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
    r"""识别结果中词文本，以及对应时间偏移

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
        r"""词文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def OffsetStartMs(self):
        r"""在句子中的开始时间偏移量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OffsetStartMs

    @OffsetStartMs.setter
    def OffsetStartMs(self, OffsetStartMs):
        self._OffsetStartMs = OffsetStartMs

    @property
    def OffsetEndMs(self):
        r"""在句子中的结束时间偏移量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
    r"""SetVocabState请求参数结构体

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
        r"""热词表ID。
        :rtype: str
        """
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def State(self):
        r"""热词表状态，1：设为默认状态；0：设为非默认状态。
        :rtype: int
        """
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
    r"""SetVocabState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID
        :type VocabId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabId = None
        self._RequestId = None

    @property
    def VocabId(self):
        r"""热词表ID
        :rtype: str
        """
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._RequestId = params.get("RequestId")


class Task(AbstractModel):
    r"""[录音文件识别](https://cloud.tencent.com/document/product/1093/37823#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)、[实时语音异步识别](https://cloud.tencent.com/document/product/1093/52061#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)请求的返回数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可通过此ID在轮询接口获取识别状态与结果。TaskId数据类型为**uint64**。
**注意：TaskId有效期为24小时，不同日期可能出现重复TaskId，请不要依赖TaskId作为您业务系统里的唯一ID。**
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID，可通过此ID在轮询接口获取识别状态与结果。TaskId数据类型为**uint64**。
**注意：TaskId有效期为24小时，不同日期可能出现重复TaskId，请不要依赖TaskId作为您业务系统里的唯一ID。**
        :rtype: int
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
        


class TaskStatus(AbstractModel):
    r"""[获取录音识别结果的返回参数](https://cloud.tencent.com/document/product/1093/37822#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)

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
        r"""任务标识。注意：TaskId数据类型为uint64。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""任务状态码，0：任务等待，1：任务执行中，2：任务成功，3：任务失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusStr(self):
        r"""任务状态，waiting：任务等待，doing：任务执行中，success：任务成功，failed：任务失败。
        :rtype: str
        """
        return self._StatusStr

    @StatusStr.setter
    def StatusStr(self, StatusStr):
        self._StatusStr = StatusStr

    @property
    def Result(self):
        r"""识别结果。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrorMsg(self):
        r"""失败原因说明。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ResultDetail(self):
        r"""识别结果详情，包含每个句子中的词时间偏移，一般用于生成字幕的场景。(录音识别请求中ResTextFormat=1时该字段不为空)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SentenceDetail
        """
        return self._ResultDetail

    @ResultDetail.setter
    def ResultDetail(self, ResultDetail):
        self._ResultDetail = ResultDetail

    @property
    def AudioDuration(self):
        r"""音频时长(秒)。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
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
        


class UpdateAsrKeyWordLibRequest(AbstractModel):
    r"""UpdateAsrKeyWordLib请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyWordLibId: 关键词表ID
        :type KeyWordLibId: str
        :param _Name: 词表名称，长度在1-20之间
仅限中英文数字-_
        :type Name: str
        :param _KeyWordFile: - 词文件（纯文本文件）以行分隔 ，进行二进制base64编码
- 格式要求：TXT 每行只有一个词，不满足格式则报错无法上传 
- 每个词最多5个汉字或15个字符，单个词库最多不超过100个词
- 此参数为空则只更新词表名称
        :type KeyWordFile: str
        """
        self._KeyWordLibId = None
        self._Name = None
        self._KeyWordFile = None

    @property
    def KeyWordLibId(self):
        r"""关键词表ID
        :rtype: str
        """
        return self._KeyWordLibId

    @KeyWordLibId.setter
    def KeyWordLibId(self, KeyWordLibId):
        self._KeyWordLibId = KeyWordLibId

    @property
    def Name(self):
        r"""词表名称，长度在1-20之间
仅限中英文数字-_
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KeyWordFile(self):
        r"""- 词文件（纯文本文件）以行分隔 ，进行二进制base64编码
- 格式要求：TXT 每行只有一个词，不满足格式则报错无法上传 
- 每个词最多5个汉字或15个字符，单个词库最多不超过100个词
- 此参数为空则只更新词表名称
        :rtype: str
        """
        return self._KeyWordFile

    @KeyWordFile.setter
    def KeyWordFile(self, KeyWordFile):
        self._KeyWordFile = KeyWordFile


    def _deserialize(self, params):
        self._KeyWordLibId = params.get("KeyWordLibId")
        self._Name = params.get("Name")
        self._KeyWordFile = params.get("KeyWordFile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAsrKeyWordLibResponse(AbstractModel):
    r"""UpdateAsrKeyWordLib返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 关键词表ID数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.KeyWordLibIdData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""关键词表ID数据
        :rtype: :class:`tencentcloud.asr.v20190614.models.KeyWordLibIdData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = KeyWordLibIdData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateAsrVocabRequest(AbstractModel):
    r"""UpdateAsrVocab请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID
        :type VocabId: str
        :param _Name: 热词表名称，长度在1-255之间
        :type Name: str
        :param _WordWeights: 词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10个汉字或30个英文字符，权重为[1,11]之间整数或100，数组长度不大于1000 (注意：如果仅更新热词表名称或者描述字段，请求不用带本参数）
        :type WordWeights: list of HotWord
        :param _WordWeightStr: 词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。
当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略
 (注意：如果仅更新热词表名称或者描述字段，请求不用带本参数）
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
        r"""热词表ID
        :rtype: str
        """
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def Name(self):
        r"""热词表名称，长度在1-255之间
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def WordWeights(self):
        r"""词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10个汉字或30个英文字符，权重为[1,11]之间整数或100，数组长度不大于1000 (注意：如果仅更新热词表名称或者描述字段，请求不用带本参数）
        :rtype: list of HotWord
        """
        return self._WordWeights

    @WordWeights.setter
    def WordWeights(self, WordWeights):
        self._WordWeights = WordWeights

    @property
    def WordWeightStr(self):
        r"""词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。
当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略
 (注意：如果仅更新热词表名称或者描述字段，请求不用带本参数）
        :rtype: str
        """
        return self._WordWeightStr

    @WordWeightStr.setter
    def WordWeightStr(self, WordWeightStr):
        self._WordWeightStr = WordWeightStr

    @property
    def Description(self):
        r"""热词表描述，长度在0-1000之间
        :rtype: str
        """
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
    r"""UpdateAsrVocab返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VocabId: 热词表ID
        :type VocabId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VocabId = None
        self._RequestId = None

    @property
    def VocabId(self):
        r"""热词表ID
        :rtype: str
        """
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VocabId = params.get("VocabId")
        self._RequestId = params.get("RequestId")


class UsageByDateInfo(AbstractModel):
    r"""用户用量信息

    """

    def __init__(self):
        r"""
        :param _BizName: 业务类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BizName: str
        :param _Count: 识别次数
单位：次
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Duration: 识别时长
单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        """
        self._BizName = None
        self._Count = None
        self._Duration = None

    @property
    def BizName(self):
        r"""业务类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BizName

    @BizName.setter
    def BizName(self, BizName):
        self._BizName = BizName

    @property
    def Count(self):
        r"""识别次数
单位：次
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Duration(self):
        r"""识别时长
单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._BizName = params.get("BizName")
        self._Count = params.get("Count")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageByDateInfoData(AbstractModel):
    r"""用户用量信息

    """

    def __init__(self):
        r"""
        :param _UsageByDateInfoList: 用量信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UsageByDateInfoList: list of UsageByDateInfo
        """
        self._UsageByDateInfoList = None

    @property
    def UsageByDateInfoList(self):
        r"""用量信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UsageByDateInfo
        """
        return self._UsageByDateInfoList

    @UsageByDateInfoList.setter
    def UsageByDateInfoList(self, UsageByDateInfoList):
        self._UsageByDateInfoList = UsageByDateInfoList


    def _deserialize(self, params):
        if params.get("UsageByDateInfoList") is not None:
            self._UsageByDateInfoList = []
            for item in params.get("UsageByDateInfoList"):
                obj = UsageByDateInfo()
                obj._deserialize(item)
                self._UsageByDateInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyTop(AbstractModel):
    r"""声纹组对比结果top数据

    """

    def __init__(self):
        r"""
        :param _Score: 相似度打分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: str
        :param _VoicePrintId: 说话人id
注意：此字段可能返回 null，表示取不到有效值。
        :type VoicePrintId: str
        :param _SpeakerId: 说话人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeakerId: str
        """
        self._Score = None
        self._VoicePrintId = None
        self._SpeakerId = None

    @property
    def Score(self):
        r"""相似度打分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def VoicePrintId(self):
        r"""说话人id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def SpeakerId(self):
        r"""说话人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpeakerId

    @SpeakerId.setter
    def SpeakerId(self, SpeakerId):
        self._SpeakerId = SpeakerId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._VoicePrintId = params.get("VoicePrintId")
        self._SpeakerId = params.get("SpeakerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyTopResult(AbstractModel):
    r"""说话人验证1:N返回结果

    """

    def __init__(self):
        r"""
        :param _VerifyTops: 对比打分结果，按照打分降序排列返回
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTops: list of VerifyTop
        """
        self._VerifyTops = None

    @property
    def VerifyTops(self):
        r"""对比打分结果，按照打分降序排列返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VerifyTop
        """
        return self._VerifyTops

    @VerifyTops.setter
    def VerifyTops(self, VerifyTops):
        self._VerifyTops = VerifyTops


    def _deserialize(self, params):
        if params.get("VerifyTops") is not None:
            self._VerifyTops = []
            for item in params.get("VerifyTops"):
                obj = VerifyTop()
                obj._deserialize(item)
                self._VerifyTops.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vocab(AbstractModel):
    r"""[词表内容](https://cloud.tencent.com/document/product/1093/41484#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)

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
        r"""热词表名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""热词表描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VocabId(self):
        r"""热词表ID
        :rtype: str
        """
        return self._VocabId

    @VocabId.setter
    def VocabId(self, VocabId):
        self._VocabId = VocabId

    @property
    def WordWeights(self):
        r"""词权重列表
        :rtype: list of HotWord
        """
        return self._WordWeights

    @WordWeights.setter
    def WordWeights(self, WordWeights):
        self._WordWeights = WordWeights

    @property
    def CreateTime(self):
        r"""词表创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""词表更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def State(self):
        r"""热词表状态，1为默认状态即在识别时默认加载该热词表进行识别，0为初始状态
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def TagInfos(self):
        r"""标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
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
    r"""[说话人基础数据](https://cloud.tencent.com/document/product/1093/94483#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)，包括说话人id和说话人昵称

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
        r"""说话人id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def SpeakerNick(self):
        r"""说话人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class VoicePrintCompareData(AbstractModel):
    r"""音频声纹比对结果，包含比对分数

    """

    def __init__(self):
        r"""
        :param _Score: 匹配度 取值范围(0.0 - 100.0)
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: str
        :param _Decision: 验证结果 0: 未通过 1: 通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Decision: int
        """
        self._Score = None
        self._Decision = None

    @property
    def Score(self):
        r"""匹配度 取值范围(0.0 - 100.0)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Decision(self):
        r"""验证结果 0: 未通过 1: 通过
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Decision

    @Decision.setter
    def Decision(self, Decision):
        self._Decision = Decision


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._Decision = params.get("Decision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintCompareRequest(AbstractModel):
    r"""VoicePrintCompare请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoiceFormat: 音频格式 0: pcm, 1: wav；pcm和wav音频无损压缩，识别准确度更高
        :type VoiceFormat: int
        :param _SampleRate: 音频采样率，目前仅支持16k，请填写16000
        :type SampleRate: int
        :param _SrcAudioData: 对比源音频数据, 音频要求：base64 编码,16k采样率， 16bit位深，pcm或者wav格式， 单声道，音频时长不超过30秒的音频，base64编码数据大小不超过2M
        :type SrcAudioData: str
        :param _DestAudioData: 对比目标音频数据, 音频要求：base64 编码,16k采样率， 16bit位深，pcm或者wav格式， 单声道，音频时长不超过30秒的音频，base64编码数据大小不超过2M
        :type DestAudioData: str
        """
        self._VoiceFormat = None
        self._SampleRate = None
        self._SrcAudioData = None
        self._DestAudioData = None

    @property
    def VoiceFormat(self):
        r"""音频格式 0: pcm, 1: wav；pcm和wav音频无损压缩，识别准确度更高
        :rtype: int
        """
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def SampleRate(self):
        r"""音频采样率，目前仅支持16k，请填写16000
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def SrcAudioData(self):
        r"""对比源音频数据, 音频要求：base64 编码,16k采样率， 16bit位深，pcm或者wav格式， 单声道，音频时长不超过30秒的音频，base64编码数据大小不超过2M
        :rtype: str
        """
        return self._SrcAudioData

    @SrcAudioData.setter
    def SrcAudioData(self, SrcAudioData):
        self._SrcAudioData = SrcAudioData

    @property
    def DestAudioData(self):
        r"""对比目标音频数据, 音频要求：base64 编码,16k采样率， 16bit位深，pcm或者wav格式， 单声道，音频时长不超过30秒的音频，base64编码数据大小不超过2M
        :rtype: str
        """
        return self._DestAudioData

    @DestAudioData.setter
    def DestAudioData(self, DestAudioData):
        self._DestAudioData = DestAudioData


    def _deserialize(self, params):
        self._VoiceFormat = params.get("VoiceFormat")
        self._SampleRate = params.get("SampleRate")
        self._SrcAudioData = params.get("SrcAudioData")
        self._DestAudioData = params.get("DestAudioData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintCompareResponse(AbstractModel):
    r"""VoicePrintCompare返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 音频声纹比对结果，包含相似度打分
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintCompareData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""音频声纹比对结果，包含相似度打分
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintCompareData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = VoicePrintCompareData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VoicePrintCountData(AbstractModel):
    r"""统计返回[说话人注册数量](https://cloud.tencent.com/document/product/1093/96061#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _VoicePrintList: 说话人id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VoicePrintList: list of VoicePrintBaseData
        """
        self._Total = None
        self._VoicePrintList = None

    @property
    def Total(self):
        r"""总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def VoicePrintList(self):
        r"""说话人id列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VoicePrintBaseData
        """
        return self._VoicePrintList

    @VoicePrintList.setter
    def VoicePrintList(self, VoicePrintList):
        self._VoicePrintList = VoicePrintList


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("VoicePrintList") is not None:
            self._VoicePrintList = []
            for item in params.get("VoicePrintList"):
                obj = VoicePrintBaseData()
                obj._deserialize(item)
                self._VoicePrintList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintCountRequest(AbstractModel):
    r"""VoicePrintCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID,仅支持大小写字母和下划线的组合，不超过128个字符
        :type GroupId: str
        :param _CountMod: 统计模式
0: 统计所有声纹数量
1: 统计指定分组下的声纹数量
        :type CountMod: int
        """
        self._GroupId = None
        self._CountMod = None

    @property
    def GroupId(self):
        r"""分组ID,仅支持大小写字母和下划线的组合，不超过128个字符
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def CountMod(self):
        r"""统计模式
0: 统计所有声纹数量
1: 统计指定分组下的声纹数量
        :rtype: int
        """
        return self._CountMod

    @CountMod.setter
    def CountMod(self, CountMod):
        self._CountMod = CountMod


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._CountMod = params.get("CountMod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintCountResponse(AbstractModel):
    r"""VoicePrintCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 统计数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintCountData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""统计数据
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintCountData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = VoicePrintCountData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VoicePrintDeleteRequest(AbstractModel):
    r"""VoicePrintDelete请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoicePrintId: 说话人id，说话人唯一标识
        :type VoicePrintId: str
        :param _GroupId: 说话人分组ID,仅支持大小写字母和下划线的组合，不超过128个字符
        :type GroupId: str
        :param _DelMod: 删除模式: 
0.默认值，删除该条声纹
1.从分组中删除该条声纹，声纹本身不删除
2.从声纹库中删除分组，仅删除分组信息，不会真正删除分组中的声纹
        :type DelMod: int
        """
        self._VoicePrintId = None
        self._GroupId = None
        self._DelMod = None

    @property
    def VoicePrintId(self):
        r"""说话人id，说话人唯一标识
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def GroupId(self):
        r"""说话人分组ID,仅支持大小写字母和下划线的组合，不超过128个字符
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DelMod(self):
        r"""删除模式: 
0.默认值，删除该条声纹
1.从分组中删除该条声纹，声纹本身不删除
2.从声纹库中删除分组，仅删除分组信息，不会真正删除分组中的声纹
        :rtype: int
        """
        return self._DelMod

    @DelMod.setter
    def DelMod(self, DelMod):
        self._DelMod = DelMod


    def _deserialize(self, params):
        self._VoicePrintId = params.get("VoicePrintId")
        self._GroupId = params.get("GroupId")
        self._DelMod = params.get("DelMod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintDeleteResponse(AbstractModel):
    r"""VoicePrintDelete返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 说话人基本信息
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""说话人基本信息
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""VoicePrintEnroll请求参数结构体

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
        :param _GroupId: 分组id, 仅支持大小写字母和下划线的组合，不超过128个字符
        :type GroupId: str
        """
        self._VoiceFormat = None
        self._SampleRate = None
        self._Data = None
        self._SpeakerNick = None
        self._GroupId = None

    @property
    def VoiceFormat(self):
        r"""音频格式 0: pcm, 1: wav
        :rtype: int
        """
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def SampleRate(self):
        r"""音频采样率，目前支持16000，单位：Hz，必填
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Data(self):
        r"""音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SpeakerNick(self):
        r"""说话人昵称  不超过32字节
        :rtype: str
        """
        return self._SpeakerNick

    @SpeakerNick.setter
    def SpeakerNick(self, SpeakerNick):
        self._SpeakerNick = SpeakerNick

    @property
    def GroupId(self):
        r"""分组id, 仅支持大小写字母和下划线的组合，不超过128个字符
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._VoiceFormat = params.get("VoiceFormat")
        self._SampleRate = params.get("SampleRate")
        self._Data = params.get("Data")
        self._SpeakerNick = params.get("SpeakerNick")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintEnrollResponse(AbstractModel):
    r"""VoicePrintEnroll返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 说话人基本数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""说话人基本数据
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = VoicePrintBaseData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VoicePrintGroupVerifyRequest(AbstractModel):
    r"""VoicePrintGroupVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoiceFormat: 音频格式 0: pcm, 1: wav
        :type VoiceFormat: int
        :param _SampleRate: 音频采样率，目前支持16000，单位：Hz，必填
        :type SampleRate: int
        :param _Data: 音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M
        :type Data: str
        :param _GroupId: 分组id, 支持数字，字母，下划线，长度不超过128
        :type GroupId: str
        :param _TopN: 返回打分结果降序排列topN, TopN大于0， 小于可创建声纹最大数量
        :type TopN: int
        """
        self._VoiceFormat = None
        self._SampleRate = None
        self._Data = None
        self._GroupId = None
        self._TopN = None

    @property
    def VoiceFormat(self):
        r"""音频格式 0: pcm, 1: wav
        :rtype: int
        """
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def SampleRate(self):
        r"""音频采样率，目前支持16000，单位：Hz，必填
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Data(self):
        r"""音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def GroupId(self):
        r"""分组id, 支持数字，字母，下划线，长度不超过128
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TopN(self):
        r"""返回打分结果降序排列topN, TopN大于0， 小于可创建声纹最大数量
        :rtype: int
        """
        return self._TopN

    @TopN.setter
    def TopN(self, TopN):
        self._TopN = TopN


    def _deserialize(self, params):
        self._VoiceFormat = params.get("VoiceFormat")
        self._SampleRate = params.get("SampleRate")
        self._Data = params.get("Data")
        self._GroupId = params.get("GroupId")
        self._TopN = params.get("TopN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintGroupVerifyResponse(AbstractModel):
    r"""VoicePrintGroupVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TopN 返回结果;系统建议打分70分以上为同一个人音色，评分也取决于音频质量、长度等其他原因影响，您可以按照业务需求适当提高或降低分数要求
        :type Data: :class:`tencentcloud.asr.v20190614.models.VerifyTopResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TopN 返回结果;系统建议打分70分以上为同一个人音色，评分也取决于音频质量、长度等其他原因影响，您可以按照业务需求适当提高或降低分数要求
        :rtype: :class:`tencentcloud.asr.v20190614.models.VerifyTopResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = VerifyTopResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VoicePrintUpdateRequest(AbstractModel):
    r"""VoicePrintUpdate请求参数结构体

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
        r"""音频格式 0: pcm, 1: wav
        :rtype: int
        """
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def SampleRate(self):
        r"""音频采样率 目前仅支持16000 单位Hz
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def VoicePrintId(self):
        r"""说话人id， 说话人唯一标识
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def Data(self):
        r"""音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M	
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SpeakerNick(self):
        r"""说话人昵称  不超过32字节
        :rtype: str
        """
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
    r"""VoicePrintUpdate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 说话人基础数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""说话人基础数据
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintBaseData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""[说话人验证数据](https://cloud.tencent.com/document/product/1093/94481#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)

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
        r"""说话人id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def Score(self):
        r"""匹配度 取值范围(0.0 - 100.0)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Decision(self):
        r"""验证结果 0: 未通过 1: 通过
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
    r"""VoicePrintVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoiceFormat: 音频格式 0: pcm, 1: wav
        :type VoiceFormat: int
        :param _SampleRate: 音频采样率，目前支持16000，单位：Hz，必填
        :type SampleRate: int
        :param _Data: 音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M	
        :type Data: str
        :param _VoicePrintId: 说话人id, 说话人唯一标识
        :type VoicePrintId: str
        """
        self._VoiceFormat = None
        self._SampleRate = None
        self._Data = None
        self._VoicePrintId = None

    @property
    def VoiceFormat(self):
        r"""音频格式 0: pcm, 1: wav
        :rtype: int
        """
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def SampleRate(self):
        r"""音频采样率，目前支持16000，单位：Hz，必填
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Data(self):
        r"""音频数据, base64 编码, 音频时长不能超过30s，数据大小不超过2M	
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def VoicePrintId(self):
        r"""说话人id, 说话人唯一标识
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId


    def _deserialize(self, params):
        self._VoiceFormat = params.get("VoiceFormat")
        self._SampleRate = params.get("SampleRate")
        self._Data = params.get("Data")
        self._VoicePrintId = params.get("VoicePrintId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintVerifyResponse(AbstractModel):
    r"""VoicePrintVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 说话人验证数据
        :type Data: :class:`tencentcloud.asr.v20190614.models.VoicePrintVerifyData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""说话人验证数据
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintVerifyData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = VoicePrintVerifyData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")