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


class AICallExtractConfigElement(AbstractModel):
    """AI 通话提取配置项

    """

    def __init__(self):
        r"""
        :param _InfoType: 配置项类型，包括
Text 文本
Selector 选项
Boolean 布尔值
Number 数字
        :type InfoType: str
        :param _InfoName: 配置项名称，不可重复
        :type InfoName: str
        :param _InfoContent: 配置项具体内容
        :type InfoContent: str
        :param _Examples: 配置项提取内容示例
        :type Examples: list of str
        :param _Choices: InfoType 为 Selector，需要配置此字段
        :type Choices: list of str
        """
        self._InfoType = None
        self._InfoName = None
        self._InfoContent = None
        self._Examples = None
        self._Choices = None

    @property
    def InfoType(self):
        """配置项类型，包括
Text 文本
Selector 选项
Boolean 布尔值
Number 数字
        :rtype: str
        """
        return self._InfoType

    @InfoType.setter
    def InfoType(self, InfoType):
        self._InfoType = InfoType

    @property
    def InfoName(self):
        """配置项名称，不可重复
        :rtype: str
        """
        return self._InfoName

    @InfoName.setter
    def InfoName(self, InfoName):
        self._InfoName = InfoName

    @property
    def InfoContent(self):
        """配置项具体内容
        :rtype: str
        """
        return self._InfoContent

    @InfoContent.setter
    def InfoContent(self, InfoContent):
        self._InfoContent = InfoContent

    @property
    def Examples(self):
        """配置项提取内容示例
        :rtype: list of str
        """
        return self._Examples

    @Examples.setter
    def Examples(self, Examples):
        self._Examples = Examples

    @property
    def Choices(self):
        """InfoType 为 Selector，需要配置此字段
        :rtype: list of str
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices


    def _deserialize(self, params):
        self._InfoType = params.get("InfoType")
        self._InfoName = params.get("InfoName")
        self._InfoContent = params.get("InfoContent")
        self._Examples = params.get("Examples")
        self._Choices = params.get("Choices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AICallExtractResultElement(AbstractModel):
    """AI 通话提取结果。

    """

    def __init__(self):
        r"""
        :param _InfoType: 提取信息的类型
Text 文本
Selector 选项
Boolean 布尔值
Number 数字
        :type InfoType: str
        :param _InfoName: 提取信息的名称
        :type InfoName: str
        :param _InfoContent: 提取信息的具体描述
        :type InfoContent: str
        :param _Result: 提取信息的具体结果
        :type Result: :class:`tencentcloud.ccc.v20200210.models.AICallExtractResultInfo`
        """
        self._InfoType = None
        self._InfoName = None
        self._InfoContent = None
        self._Result = None

    @property
    def InfoType(self):
        """提取信息的类型
Text 文本
Selector 选项
Boolean 布尔值
Number 数字
        :rtype: str
        """
        return self._InfoType

    @InfoType.setter
    def InfoType(self, InfoType):
        self._InfoType = InfoType

    @property
    def InfoName(self):
        """提取信息的名称
        :rtype: str
        """
        return self._InfoName

    @InfoName.setter
    def InfoName(self, InfoName):
        self._InfoName = InfoName

    @property
    def InfoContent(self):
        """提取信息的具体描述
        :rtype: str
        """
        return self._InfoContent

    @InfoContent.setter
    def InfoContent(self, InfoContent):
        self._InfoContent = InfoContent

    @property
    def Result(self):
        """提取信息的具体结果
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AICallExtractResultInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._InfoType = params.get("InfoType")
        self._InfoName = params.get("InfoName")
        self._InfoContent = params.get("InfoContent")
        if params.get("Result") is not None:
            self._Result = AICallExtractResultInfo()
            self._Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AICallExtractResultInfo(AbstractModel):
    """AI 通话结果具体信息

    """

    def __init__(self):
        r"""
        :param _Text: 提取的类型是文本
        :type Text: str
        :param _Chosen: 提取的内型是选项
        :type Chosen: list of str
        :param _Boolean: 提取类型是布尔值
        :type Boolean: bool
        :param _Number: 提取类型是数字
        :type Number: float
        """
        self._Text = None
        self._Chosen = None
        self._Boolean = None
        self._Number = None

    @property
    def Text(self):
        """提取的类型是文本
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Chosen(self):
        """提取的内型是选项
        :rtype: list of str
        """
        return self._Chosen

    @Chosen.setter
    def Chosen(self, Chosen):
        self._Chosen = Chosen

    @property
    def Boolean(self):
        """提取类型是布尔值
        :rtype: bool
        """
        return self._Boolean

    @Boolean.setter
    def Boolean(self, Boolean):
        self._Boolean = Boolean

    @property
    def Number(self):
        """提取类型是数字
        :rtype: float
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Chosen = params.get("Chosen")
        self._Boolean = params.get("Boolean")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AILatencyDetail(AbstractModel):
    """AI时延明细

    """

    def __init__(self):
        r"""
        :param _RoundId: 对话ID
        :type RoundId: str
        :param _ASRLatency: asr时延（毫秒）
        :type ASRLatency: int
        :param _TTSLatency: tts时延（毫秒）
        :type TTSLatency: int
        :param _LLMLatency: llm时延（毫秒）
        :type LLMLatency: int
        :param _ETELatency: 端到端时延（毫秒）
        :type ETELatency: int
        """
        self._RoundId = None
        self._ASRLatency = None
        self._TTSLatency = None
        self._LLMLatency = None
        self._ETELatency = None

    @property
    def RoundId(self):
        """对话ID
        :rtype: str
        """
        return self._RoundId

    @RoundId.setter
    def RoundId(self, RoundId):
        self._RoundId = RoundId

    @property
    def ASRLatency(self):
        """asr时延（毫秒）
        :rtype: int
        """
        return self._ASRLatency

    @ASRLatency.setter
    def ASRLatency(self, ASRLatency):
        self._ASRLatency = ASRLatency

    @property
    def TTSLatency(self):
        """tts时延（毫秒）
        :rtype: int
        """
        return self._TTSLatency

    @TTSLatency.setter
    def TTSLatency(self, TTSLatency):
        self._TTSLatency = TTSLatency

    @property
    def LLMLatency(self):
        """llm时延（毫秒）
        :rtype: int
        """
        return self._LLMLatency

    @LLMLatency.setter
    def LLMLatency(self, LLMLatency):
        self._LLMLatency = LLMLatency

    @property
    def ETELatency(self):
        """端到端时延（毫秒）
        :rtype: int
        """
        return self._ETELatency

    @ETELatency.setter
    def ETELatency(self, ETELatency):
        self._ETELatency = ETELatency


    def _deserialize(self, params):
        self._RoundId = params.get("RoundId")
        self._ASRLatency = params.get("ASRLatency")
        self._TTSLatency = params.get("TTSLatency")
        self._LLMLatency = params.get("LLMLatency")
        self._ETELatency = params.get("ETELatency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AILatencyStatistics(AbstractModel):
    """AI时延统计

    """

    def __init__(self):
        r"""
        :param _ASRLatency: asr时延统计
        :type ASRLatency: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatisticsInfo`
        :param _TTSLatency: tts时延统计
        :type TTSLatency: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatisticsInfo`
        :param _LLMLatency: llm时延统计
        :type LLMLatency: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatisticsInfo`
        :param _ETELatency: 端到端时延统计
        :type ETELatency: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatisticsInfo`
        """
        self._ASRLatency = None
        self._TTSLatency = None
        self._LLMLatency = None
        self._ETELatency = None

    @property
    def ASRLatency(self):
        """asr时延统计
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatisticsInfo`
        """
        return self._ASRLatency

    @ASRLatency.setter
    def ASRLatency(self, ASRLatency):
        self._ASRLatency = ASRLatency

    @property
    def TTSLatency(self):
        """tts时延统计
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatisticsInfo`
        """
        return self._TTSLatency

    @TTSLatency.setter
    def TTSLatency(self, TTSLatency):
        self._TTSLatency = TTSLatency

    @property
    def LLMLatency(self):
        """llm时延统计
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatisticsInfo`
        """
        return self._LLMLatency

    @LLMLatency.setter
    def LLMLatency(self, LLMLatency):
        self._LLMLatency = LLMLatency

    @property
    def ETELatency(self):
        """端到端时延统计
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatisticsInfo`
        """
        return self._ETELatency

    @ETELatency.setter
    def ETELatency(self, ETELatency):
        self._ETELatency = ETELatency


    def _deserialize(self, params):
        if params.get("ASRLatency") is not None:
            self._ASRLatency = AILatencyStatisticsInfo()
            self._ASRLatency._deserialize(params.get("ASRLatency"))
        if params.get("TTSLatency") is not None:
            self._TTSLatency = AILatencyStatisticsInfo()
            self._TTSLatency._deserialize(params.get("TTSLatency"))
        if params.get("LLMLatency") is not None:
            self._LLMLatency = AILatencyStatisticsInfo()
            self._LLMLatency._deserialize(params.get("LLMLatency"))
        if params.get("ETELatency") is not None:
            self._ETELatency = AILatencyStatisticsInfo()
            self._ETELatency._deserialize(params.get("ETELatency"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AILatencyStatisticsInfo(AbstractModel):
    """AI时延统计

    """

    def __init__(self):
        r"""
        :param _MinLatency: 最小值
        :type MinLatency: int
        :param _MiddleLatency: 中位数
        :type MiddleLatency: int
        :param _P90Latency: p90
        :type P90Latency: int
        """
        self._MinLatency = None
        self._MiddleLatency = None
        self._P90Latency = None

    @property
    def MinLatency(self):
        """最小值
        :rtype: int
        """
        return self._MinLatency

    @MinLatency.setter
    def MinLatency(self, MinLatency):
        self._MinLatency = MinLatency

    @property
    def MiddleLatency(self):
        """中位数
        :rtype: int
        """
        return self._MiddleLatency

    @MiddleLatency.setter
    def MiddleLatency(self, MiddleLatency):
        self._MiddleLatency = MiddleLatency

    @property
    def P90Latency(self):
        """p90
        :rtype: int
        """
        return self._P90Latency

    @P90Latency.setter
    def P90Latency(self, P90Latency):
        self._P90Latency = P90Latency


    def _deserialize(self, params):
        self._MinLatency = params.get("MinLatency")
        self._MiddleLatency = params.get("MiddleLatency")
        self._P90Latency = params.get("P90Latency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AITransferItem(AbstractModel):
    """AI转人工配置项

    """

    def __init__(self):
        r"""
        :param _TransferFunctionName: 转人工的function calling 名称
        :type TransferFunctionName: str
        :param _TransferFunctionDesc: TransferFunctionEnable为true时生效；transfer_to_human function calling的desc，默认为 "Transfer to human when the user has to transfer to human (like says transfer to human) or you are instructed to do so."
        :type TransferFunctionDesc: str
        :param _TransferSkillGroupId: 转人工的技能组ID
        :type TransferSkillGroupId: int
        """
        self._TransferFunctionName = None
        self._TransferFunctionDesc = None
        self._TransferSkillGroupId = None

    @property
    def TransferFunctionName(self):
        """转人工的function calling 名称
        :rtype: str
        """
        return self._TransferFunctionName

    @TransferFunctionName.setter
    def TransferFunctionName(self, TransferFunctionName):
        self._TransferFunctionName = TransferFunctionName

    @property
    def TransferFunctionDesc(self):
        """TransferFunctionEnable为true时生效；transfer_to_human function calling的desc，默认为 "Transfer to human when the user has to transfer to human (like says transfer to human) or you are instructed to do so."
        :rtype: str
        """
        return self._TransferFunctionDesc

    @TransferFunctionDesc.setter
    def TransferFunctionDesc(self, TransferFunctionDesc):
        self._TransferFunctionDesc = TransferFunctionDesc

    @property
    def TransferSkillGroupId(self):
        """转人工的技能组ID
        :rtype: int
        """
        return self._TransferSkillGroupId

    @TransferSkillGroupId.setter
    def TransferSkillGroupId(self, TransferSkillGroupId):
        self._TransferSkillGroupId = TransferSkillGroupId


    def _deserialize(self, params):
        self._TransferFunctionName = params.get("TransferFunctionName")
        self._TransferFunctionDesc = params.get("TransferFunctionDesc")
        self._TransferSkillGroupId = params.get("TransferSkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortAgentCruiseDialingCampaignRequest(AbstractModel):
    """AbortAgentCruiseDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortAgentCruiseDialingCampaignResponse(AbstractModel):
    """AbortAgentCruiseDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AbortPredictiveDialingCampaignRequest(AbstractModel):
    """AbortPredictiveDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortPredictiveDialingCampaignResponse(AbstractModel):
    """AbortPredictiveDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ActiveCarrierPrivilegeNumber(AbstractModel):
    """生效运营商白名单号码

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 实例Id
        :type SdkAppId: int
        :param _Caller: 主叫号码
        :type Caller: str
        :param _Callee: 被叫号码
        :type Callee: str
        :param _CreateTime: 生效unix时间戳(秒)
        :type CreateTime: int
        """
        self._SdkAppId = None
        self._Caller = None
        self._Callee = None
        self._CreateTime = None

    @property
    def SdkAppId(self):
        """实例Id
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Caller(self):
        """主叫号码
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        """被叫号码
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def CreateTime(self):
        """生效unix时间戳(秒)
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrData(AbstractModel):
    """语音转文本信息

    """

    def __init__(self):
        r"""
        :param _User: 用户方
        :type User: str
        :param _Message: 消息内容
        :type Message: str
        :param _Timestamp: 时间戳
        :type Timestamp: int
        :param _Start: 句子开始时间，Unix 毫秒时间戳
        :type Start: int
        :param _End: 句子结束时间，Unix 毫秒时间戳
        :type End: int
        """
        self._User = None
        self._Message = None
        self._Timestamp = None
        self._Start = None
        self._End = None

    @property
    def User(self):
        """用户方
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Message(self):
        """消息内容
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Timestamp(self):
        warnings.warn("parameter `Timestamp` is deprecated", DeprecationWarning) 

        """时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        warnings.warn("parameter `Timestamp` is deprecated", DeprecationWarning) 

        self._Timestamp = Timestamp

    @property
    def Start(self):
        """句子开始时间，Unix 毫秒时间戳
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        """句子结束时间，Unix 毫秒时间戳
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Message = params.get("Message")
        self._Timestamp = params.get("Timestamp")
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioFileInfo(AbstractModel):
    """音频文件审核信息

    """

    def __init__(self):
        r"""
        :param _FileId: 文件ID
        :type FileId: int
        :param _CustomFileName: 文件别名
        :type CustomFileName: str
        :param _AudioFileName: 文件名
        :type AudioFileName: str
        :param _Status: 审核状态，0-未审核，1-审核通过，2-审核拒绝
        :type Status: int
        """
        self._FileId = None
        self._CustomFileName = None
        self._AudioFileName = None
        self._Status = None

    @property
    def FileId(self):
        """文件ID
        :rtype: int
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def CustomFileName(self):
        """文件别名
        :rtype: str
        """
        return self._CustomFileName

    @CustomFileName.setter
    def CustomFileName(self, CustomFileName):
        self._CustomFileName = CustomFileName

    @property
    def AudioFileName(self):
        """文件名
        :rtype: str
        """
        return self._AudioFileName

    @AudioFileName.setter
    def AudioFileName(self, AudioFileName):
        self._AudioFileName = AudioFileName

    @property
    def Status(self):
        """审核状态，0-未审核，1-审核通过，2-审核拒绝
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._CustomFileName = params.get("CustomFileName")
        self._AudioFileName = params.get("AudioFileName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoCalloutTaskCalleeInfo(AbstractModel):
    """外呼任务被叫信息

    """

    def __init__(self):
        r"""
        :param _Callee: 被叫号码
        :type Callee: str
        :param _State: 呼叫状态 0初始 1已接听 2未接听 3呼叫中 4待重试
        :type State: int
        :param _Sessions: 会话ID列表
        :type Sessions: list of str
        """
        self._Callee = None
        self._State = None
        self._Sessions = None

    @property
    def Callee(self):
        """被叫号码
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def State(self):
        """呼叫状态 0初始 1已接听 2未接听 3呼叫中 4待重试
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Sessions(self):
        """会话ID列表
        :rtype: list of str
        """
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions


    def _deserialize(self, params):
        self._Callee = params.get("Callee")
        self._State = params.get("State")
        self._Sessions = params.get("Sessions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoCalloutTaskInfo(AbstractModel):
    """自动外呼任务列表项

    """

    def __init__(self):
        r"""
        :param _Name: 任务名
        :type Name: str
        :param _CalleeCount: 被叫数量
        :type CalleeCount: int
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _NotBefore: 起始时间戳
        :type NotBefore: int
        :param _NotAfter: 结束时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type NotAfter: int
        :param _IvrId: 任务使用的IvrId
        :type IvrId: int
        :param _State: 任务状态：
0初始：任务创建，呼叫未开始
1运行中
2 已完成：任务中所有呼叫完成
3结束中：任务到期，但仍有部分呼叫未结束
4已结束：任务到期终止
        :type State: int
        :param _TaskId: 任务Id
        :type TaskId: int
        """
        self._Name = None
        self._CalleeCount = None
        self._Callers = None
        self._NotBefore = None
        self._NotAfter = None
        self._IvrId = None
        self._State = None
        self._TaskId = None

    @property
    def Name(self):
        """任务名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CalleeCount(self):
        """被叫数量
        :rtype: int
        """
        return self._CalleeCount

    @CalleeCount.setter
    def CalleeCount(self, CalleeCount):
        self._CalleeCount = CalleeCount

    @property
    def Callers(self):
        """主叫号码列表
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def NotBefore(self):
        """起始时间戳
        :rtype: int
        """
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def NotAfter(self):
        """结束时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def IvrId(self):
        """任务使用的IvrId
        :rtype: int
        """
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def State(self):
        """任务状态：
0初始：任务创建，呼叫未开始
1运行中
2 已完成：任务中所有呼叫完成
3结束中：任务到期，但仍有部分呼叫未结束
4已结束：任务到期终止
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def TaskId(self):
        """任务Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CalleeCount = params.get("CalleeCount")
        self._Callers = params.get("Callers")
        self._NotBefore = params.get("NotBefore")
        self._NotAfter = params.get("NotAfter")
        self._IvrId = params.get("IvrId")
        self._State = params.get("State")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindNumberCallOutSkillGroupRequest(AbstractModel):
    """BindNumberCallOutSkillGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Number: 待绑定的号码
        :type Number: str
        :param _SkillGroupIds: 待绑定的技能组Id列表
        :type SkillGroupIds: list of int non-negative
        """
        self._SdkAppId = None
        self._Number = None
        self._SkillGroupIds = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Number(self):
        """待绑定的号码
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def SkillGroupIds(self):
        """待绑定的技能组Id列表
        :rtype: list of int non-negative
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Number = params.get("Number")
        self._SkillGroupIds = params.get("SkillGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindNumberCallOutSkillGroupResponse(AbstractModel):
    """BindNumberCallOutSkillGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BindStaffSkillGroupListRequest(AbstractModel):
    """BindStaffSkillGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StaffEmail: 座席邮箱
        :type StaffEmail: str
        :param _SkillGroupList: 绑定技能组列表
        :type SkillGroupList: list of int
        :param _StaffSkillGroupList: 绑定技能组列表(必填)
        :type StaffSkillGroupList: list of StaffSkillGroupList
        """
        self._SdkAppId = None
        self._StaffEmail = None
        self._SkillGroupList = None
        self._StaffSkillGroupList = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffEmail(self):
        """座席邮箱
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def SkillGroupList(self):
        warnings.warn("parameter `SkillGroupList` is deprecated", DeprecationWarning) 

        """绑定技能组列表
        :rtype: list of int
        """
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        warnings.warn("parameter `SkillGroupList` is deprecated", DeprecationWarning) 

        self._SkillGroupList = SkillGroupList

    @property
    def StaffSkillGroupList(self):
        """绑定技能组列表(必填)
        :rtype: list of StaffSkillGroupList
        """
        return self._StaffSkillGroupList

    @StaffSkillGroupList.setter
    def StaffSkillGroupList(self, StaffSkillGroupList):
        self._StaffSkillGroupList = StaffSkillGroupList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffEmail = params.get("StaffEmail")
        self._SkillGroupList = params.get("SkillGroupList")
        if params.get("StaffSkillGroupList") is not None:
            self._StaffSkillGroupList = []
            for item in params.get("StaffSkillGroupList"):
                obj = StaffSkillGroupList()
                obj._deserialize(item)
                self._StaffSkillGroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindStaffSkillGroupListResponse(AbstractModel):
    """BindStaffSkillGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CallInMetrics(AbstractModel):
    """呼入实时指标

    """

    def __init__(self):
        r"""
        :param _IvrCount: IVR驻留数量
        :type IvrCount: int
        :param _QueueCount: 排队中数量
        :type QueueCount: int
        :param _RingCount: 振铃中数量
        :type RingCount: int
        :param _AcceptCount: 接通中数量
        :type AcceptCount: int
        :param _TransferOuterCount: 客服转接外线中数量
        :type TransferOuterCount: int
        :param _MaxQueueDuration: 最大排队时长
        :type MaxQueueDuration: int
        :param _AvgQueueDuration: 平均排队时长
        :type AvgQueueDuration: int
        :param _MaxRingDuration: 最大振铃时长
        :type MaxRingDuration: int
        :param _AvgRingDuration: 平均振铃时长
        :type AvgRingDuration: int
        :param _MaxAcceptDuration: 最大接通时长
        :type MaxAcceptDuration: int
        :param _AvgAcceptDuration: 平均接通时长
        :type AvgAcceptDuration: int
        """
        self._IvrCount = None
        self._QueueCount = None
        self._RingCount = None
        self._AcceptCount = None
        self._TransferOuterCount = None
        self._MaxQueueDuration = None
        self._AvgQueueDuration = None
        self._MaxRingDuration = None
        self._AvgRingDuration = None
        self._MaxAcceptDuration = None
        self._AvgAcceptDuration = None

    @property
    def IvrCount(self):
        """IVR驻留数量
        :rtype: int
        """
        return self._IvrCount

    @IvrCount.setter
    def IvrCount(self, IvrCount):
        self._IvrCount = IvrCount

    @property
    def QueueCount(self):
        """排队中数量
        :rtype: int
        """
        return self._QueueCount

    @QueueCount.setter
    def QueueCount(self, QueueCount):
        self._QueueCount = QueueCount

    @property
    def RingCount(self):
        """振铃中数量
        :rtype: int
        """
        return self._RingCount

    @RingCount.setter
    def RingCount(self, RingCount):
        self._RingCount = RingCount

    @property
    def AcceptCount(self):
        """接通中数量
        :rtype: int
        """
        return self._AcceptCount

    @AcceptCount.setter
    def AcceptCount(self, AcceptCount):
        self._AcceptCount = AcceptCount

    @property
    def TransferOuterCount(self):
        """客服转接外线中数量
        :rtype: int
        """
        return self._TransferOuterCount

    @TransferOuterCount.setter
    def TransferOuterCount(self, TransferOuterCount):
        self._TransferOuterCount = TransferOuterCount

    @property
    def MaxQueueDuration(self):
        """最大排队时长
        :rtype: int
        """
        return self._MaxQueueDuration

    @MaxQueueDuration.setter
    def MaxQueueDuration(self, MaxQueueDuration):
        self._MaxQueueDuration = MaxQueueDuration

    @property
    def AvgQueueDuration(self):
        """平均排队时长
        :rtype: int
        """
        return self._AvgQueueDuration

    @AvgQueueDuration.setter
    def AvgQueueDuration(self, AvgQueueDuration):
        self._AvgQueueDuration = AvgQueueDuration

    @property
    def MaxRingDuration(self):
        """最大振铃时长
        :rtype: int
        """
        return self._MaxRingDuration

    @MaxRingDuration.setter
    def MaxRingDuration(self, MaxRingDuration):
        self._MaxRingDuration = MaxRingDuration

    @property
    def AvgRingDuration(self):
        """平均振铃时长
        :rtype: int
        """
        return self._AvgRingDuration

    @AvgRingDuration.setter
    def AvgRingDuration(self, AvgRingDuration):
        self._AvgRingDuration = AvgRingDuration

    @property
    def MaxAcceptDuration(self):
        """最大接通时长
        :rtype: int
        """
        return self._MaxAcceptDuration

    @MaxAcceptDuration.setter
    def MaxAcceptDuration(self, MaxAcceptDuration):
        self._MaxAcceptDuration = MaxAcceptDuration

    @property
    def AvgAcceptDuration(self):
        """平均接通时长
        :rtype: int
        """
        return self._AvgAcceptDuration

    @AvgAcceptDuration.setter
    def AvgAcceptDuration(self, AvgAcceptDuration):
        self._AvgAcceptDuration = AvgAcceptDuration


    def _deserialize(self, params):
        self._IvrCount = params.get("IvrCount")
        self._QueueCount = params.get("QueueCount")
        self._RingCount = params.get("RingCount")
        self._AcceptCount = params.get("AcceptCount")
        self._TransferOuterCount = params.get("TransferOuterCount")
        self._MaxQueueDuration = params.get("MaxQueueDuration")
        self._AvgQueueDuration = params.get("AvgQueueDuration")
        self._MaxRingDuration = params.get("MaxRingDuration")
        self._AvgRingDuration = params.get("AvgRingDuration")
        self._MaxAcceptDuration = params.get("MaxAcceptDuration")
        self._AvgAcceptDuration = params.get("AvgAcceptDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInNumberMetrics(AbstractModel):
    """呼入线路维度相关指标

    """

    def __init__(self):
        r"""
        :param _Number: 线路号码
        :type Number: str
        :param _Metrics: 线路相关指标
        :type Metrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _SkillGroupMetrics: 所属技能组相关指标
        :type SkillGroupMetrics: list of CallInSkillGroupMetrics
        """
        self._Number = None
        self._Metrics = None
        self._SkillGroupMetrics = None

    @property
    def Number(self):
        """线路号码
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Metrics(self):
        """线路相关指标
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def SkillGroupMetrics(self):
        """所属技能组相关指标
        :rtype: list of CallInSkillGroupMetrics
        """
        return self._SkillGroupMetrics

    @SkillGroupMetrics.setter
    def SkillGroupMetrics(self, SkillGroupMetrics):
        self._SkillGroupMetrics = SkillGroupMetrics


    def _deserialize(self, params):
        self._Number = params.get("Number")
        if params.get("Metrics") is not None:
            self._Metrics = CallInMetrics()
            self._Metrics._deserialize(params.get("Metrics"))
        if params.get("SkillGroupMetrics") is not None:
            self._SkillGroupMetrics = []
            for item in params.get("SkillGroupMetrics"):
                obj = CallInSkillGroupMetrics()
                obj._deserialize(item)
                self._SkillGroupMetrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInSkillGroupMetrics(AbstractModel):
    """呼入技能组相关指标

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _Metrics: 数据指标
        :type Metrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _Name: 技能组名称
        :type Name: str
        """
        self._SkillGroupId = None
        self._Metrics = None
        self._Name = None

    @property
    def SkillGroupId(self):
        """技能组ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Metrics(self):
        """数据指标
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Name(self):
        """技能组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        if params.get("Metrics") is not None:
            self._Metrics = CallInMetrics()
            self._Metrics._deserialize(params.get("Metrics"))
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CalleeAttribute(AbstractModel):
    """被叫属性

    """

    def __init__(self):
        r"""
        :param _Callee: 被叫号码
        :type Callee: str
        :param _UUI: 随路数据
        :type UUI: str
        :param _Variables: 参数
        :type Variables: list of Variable
        """
        self._Callee = None
        self._UUI = None
        self._Variables = None

    @property
    def Callee(self):
        """被叫号码
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def UUI(self):
        """随路数据
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def Variables(self):
        """参数
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables


    def _deserialize(self, params):
        self._Callee = params.get("Callee")
        self._UUI = params.get("UUI")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarrierPrivilegeNumberApplicant(AbstractModel):
    """运营商白名单号码申请单

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 实例Id
        :type SdkAppId: int
        :param _ApplicantId: 申请单Id
        :type ApplicantId: int
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _Callees: 被叫号码列表
        :type Callees: list of str
        :param _Description: 描述
        :type Description: str
        :param _State: 审批状态:1 待审核、2 通过、3 拒绝
        :type State: int
        :param _CreateTime: 创建时间，unix时间戳(秒)
        :type CreateTime: int
        :param _UpdateTime: 更新时间，unix时间戳(秒)
        :type UpdateTime: int
        """
        self._SdkAppId = None
        self._ApplicantId = None
        self._Callers = None
        self._Callees = None
        self._Description = None
        self._State = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def SdkAppId(self):
        """实例Id
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ApplicantId(self):
        """申请单Id
        :rtype: int
        """
        return self._ApplicantId

    @ApplicantId.setter
    def ApplicantId(self, ApplicantId):
        self._ApplicantId = ApplicantId

    @property
    def Callers(self):
        """主叫号码列表
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Callees(self):
        """被叫号码列表
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def State(self):
        """审批状态:1 待审核、2 通过、3 拒绝
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreateTime(self):
        """创建时间，unix时间戳(秒)
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间，unix时间戳(秒)
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ApplicantId = params.get("ApplicantId")
        self._Callers = params.get("Callers")
        self._Callees = params.get("Callees")
        self._Description = params.get("Description")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompanyApplyInfo(AbstractModel):
    """企业资质申请信息

    """

    def __init__(self):
        r"""
        :param _ApplicantType: 申请人身份，0-公司法定代表人，1-经办人（受法定代表人委托）
        :type ApplicantType: int
        :param _CompanyName: 企业名称
        :type CompanyName: str
        :param _BusinessId: 统一社会信用代码
        :type BusinessId: str
        :param _BusinessIdPicUrl: 营业执照扫描件(加盖公章)。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type BusinessIdPicUrl: str
        :param _CorporationName: 法定代表人名称
        :type CorporationName: str
        :param _CorporationId: 法定代表人身份证号码
        :type CorporationId: str
        :param _CorporationIdPicUrl: 法定代表人身份证正反面扫描件。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type CorporationIdPicUrl: str
        :param _NetworkCommitmentPicUrl: 安全合规使用承诺书。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type NetworkCommitmentPicUrl: str
        :param _IsEqualTencentCloud: 是否与腾讯云账号的资质一致,0-不一致,1-一致
        :type IsEqualTencentCloud: int
        :param _CorporationMobile: 法定代表人手机号
        :type CorporationMobile: str
        :param _CorporationMobilePicUrl: 法定代表人手机号码实名认证。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type CorporationMobilePicUrl: str
        :param _UseDescribeFileUrl: 通话话术。(支持doc、docx格式的文档不超过50MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type UseDescribeFileUrl: str
        :param _CompanyAuthLetterPicUrl: 公司授权函。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type CompanyAuthLetterPicUrl: str
        :param _AcceptPicUrl: 电话受理单。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type AcceptPicUrl: str
        :param _CorporationHoldingOnIdPicUrl: 法定代表人手持身份证照，申请人类型为法定代表人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type CorporationHoldingOnIdPicUrl: str
        :param _OperatorName: 经办人名称，申请人类型为经办人时必填。
        :type OperatorName: str
        :param _OperatorId: 经办人证件号码，申请人类型为经办人时必填。
        :type OperatorId: str
        :param _OperatorIdPicUrl: 经办人身份证正反面扫描件，申请人类型为经办人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type OperatorIdPicUrl: str
        :param _OperatorHoldingOnIdPicUrl: 经办人手持身份证照，申请人类型为经办人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type OperatorHoldingOnIdPicUrl: str
        :param _CommissionPicUrl: 委托授权书，申请人类型为经办人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type CommissionPicUrl: str
        :param _OperatorMobile: 经办人手机号，申请人类型为经办人时必填。
        :type OperatorMobile: str
        :param _OperatorEmail: 经办人邮箱，申请人类型为经办人时必填。
        :type OperatorEmail: str
        :param _OperatorMobilePicUrl: 经办人手机号码实名认证，申请人类型为经办人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :type OperatorMobilePicUrl: str
        """
        self._ApplicantType = None
        self._CompanyName = None
        self._BusinessId = None
        self._BusinessIdPicUrl = None
        self._CorporationName = None
        self._CorporationId = None
        self._CorporationIdPicUrl = None
        self._NetworkCommitmentPicUrl = None
        self._IsEqualTencentCloud = None
        self._CorporationMobile = None
        self._CorporationMobilePicUrl = None
        self._UseDescribeFileUrl = None
        self._CompanyAuthLetterPicUrl = None
        self._AcceptPicUrl = None
        self._CorporationHoldingOnIdPicUrl = None
        self._OperatorName = None
        self._OperatorId = None
        self._OperatorIdPicUrl = None
        self._OperatorHoldingOnIdPicUrl = None
        self._CommissionPicUrl = None
        self._OperatorMobile = None
        self._OperatorEmail = None
        self._OperatorMobilePicUrl = None

    @property
    def ApplicantType(self):
        """申请人身份，0-公司法定代表人，1-经办人（受法定代表人委托）
        :rtype: int
        """
        return self._ApplicantType

    @ApplicantType.setter
    def ApplicantType(self, ApplicantType):
        self._ApplicantType = ApplicantType

    @property
    def CompanyName(self):
        """企业名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def BusinessId(self):
        """统一社会信用代码
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def BusinessIdPicUrl(self):
        """营业执照扫描件(加盖公章)。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._BusinessIdPicUrl

    @BusinessIdPicUrl.setter
    def BusinessIdPicUrl(self, BusinessIdPicUrl):
        self._BusinessIdPicUrl = BusinessIdPicUrl

    @property
    def CorporationName(self):
        """法定代表人名称
        :rtype: str
        """
        return self._CorporationName

    @CorporationName.setter
    def CorporationName(self, CorporationName):
        self._CorporationName = CorporationName

    @property
    def CorporationId(self):
        """法定代表人身份证号码
        :rtype: str
        """
        return self._CorporationId

    @CorporationId.setter
    def CorporationId(self, CorporationId):
        self._CorporationId = CorporationId

    @property
    def CorporationIdPicUrl(self):
        """法定代表人身份证正反面扫描件。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._CorporationIdPicUrl

    @CorporationIdPicUrl.setter
    def CorporationIdPicUrl(self, CorporationIdPicUrl):
        self._CorporationIdPicUrl = CorporationIdPicUrl

    @property
    def NetworkCommitmentPicUrl(self):
        """安全合规使用承诺书。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._NetworkCommitmentPicUrl

    @NetworkCommitmentPicUrl.setter
    def NetworkCommitmentPicUrl(self, NetworkCommitmentPicUrl):
        self._NetworkCommitmentPicUrl = NetworkCommitmentPicUrl

    @property
    def IsEqualTencentCloud(self):
        """是否与腾讯云账号的资质一致,0-不一致,1-一致
        :rtype: int
        """
        return self._IsEqualTencentCloud

    @IsEqualTencentCloud.setter
    def IsEqualTencentCloud(self, IsEqualTencentCloud):
        self._IsEqualTencentCloud = IsEqualTencentCloud

    @property
    def CorporationMobile(self):
        """法定代表人手机号
        :rtype: str
        """
        return self._CorporationMobile

    @CorporationMobile.setter
    def CorporationMobile(self, CorporationMobile):
        self._CorporationMobile = CorporationMobile

    @property
    def CorporationMobilePicUrl(self):
        """法定代表人手机号码实名认证。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._CorporationMobilePicUrl

    @CorporationMobilePicUrl.setter
    def CorporationMobilePicUrl(self, CorporationMobilePicUrl):
        self._CorporationMobilePicUrl = CorporationMobilePicUrl

    @property
    def UseDescribeFileUrl(self):
        """通话话术。(支持doc、docx格式的文档不超过50MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._UseDescribeFileUrl

    @UseDescribeFileUrl.setter
    def UseDescribeFileUrl(self, UseDescribeFileUrl):
        self._UseDescribeFileUrl = UseDescribeFileUrl

    @property
    def CompanyAuthLetterPicUrl(self):
        """公司授权函。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._CompanyAuthLetterPicUrl

    @CompanyAuthLetterPicUrl.setter
    def CompanyAuthLetterPicUrl(self, CompanyAuthLetterPicUrl):
        self._CompanyAuthLetterPicUrl = CompanyAuthLetterPicUrl

    @property
    def AcceptPicUrl(self):
        """电话受理单。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._AcceptPicUrl

    @AcceptPicUrl.setter
    def AcceptPicUrl(self, AcceptPicUrl):
        self._AcceptPicUrl = AcceptPicUrl

    @property
    def CorporationHoldingOnIdPicUrl(self):
        """法定代表人手持身份证照，申请人类型为法定代表人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._CorporationHoldingOnIdPicUrl

    @CorporationHoldingOnIdPicUrl.setter
    def CorporationHoldingOnIdPicUrl(self, CorporationHoldingOnIdPicUrl):
        self._CorporationHoldingOnIdPicUrl = CorporationHoldingOnIdPicUrl

    @property
    def OperatorName(self):
        """经办人名称，申请人类型为经办人时必填。
        :rtype: str
        """
        return self._OperatorName

    @OperatorName.setter
    def OperatorName(self, OperatorName):
        self._OperatorName = OperatorName

    @property
    def OperatorId(self):
        """经办人证件号码，申请人类型为经办人时必填。
        :rtype: str
        """
        return self._OperatorId

    @OperatorId.setter
    def OperatorId(self, OperatorId):
        self._OperatorId = OperatorId

    @property
    def OperatorIdPicUrl(self):
        """经办人身份证正反面扫描件，申请人类型为经办人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._OperatorIdPicUrl

    @OperatorIdPicUrl.setter
    def OperatorIdPicUrl(self, OperatorIdPicUrl):
        self._OperatorIdPicUrl = OperatorIdPicUrl

    @property
    def OperatorHoldingOnIdPicUrl(self):
        """经办人手持身份证照，申请人类型为经办人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._OperatorHoldingOnIdPicUrl

    @OperatorHoldingOnIdPicUrl.setter
    def OperatorHoldingOnIdPicUrl(self, OperatorHoldingOnIdPicUrl):
        self._OperatorHoldingOnIdPicUrl = OperatorHoldingOnIdPicUrl

    @property
    def CommissionPicUrl(self):
        """委托授权书，申请人类型为经办人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._CommissionPicUrl

    @CommissionPicUrl.setter
    def CommissionPicUrl(self, CommissionPicUrl):
        self._CommissionPicUrl = CommissionPicUrl

    @property
    def OperatorMobile(self):
        """经办人手机号，申请人类型为经办人时必填。
        :rtype: str
        """
        return self._OperatorMobile

    @OperatorMobile.setter
    def OperatorMobile(self, OperatorMobile):
        self._OperatorMobile = OperatorMobile

    @property
    def OperatorEmail(self):
        """经办人邮箱，申请人类型为经办人时必填。
        :rtype: str
        """
        return self._OperatorEmail

    @OperatorEmail.setter
    def OperatorEmail(self, OperatorEmail):
        self._OperatorEmail = OperatorEmail

    @property
    def OperatorMobilePicUrl(self):
        """经办人手机号码实名认证，申请人类型为经办人时必填。(支持jpg、png、gif、jpeg格式的图片，每张图片应大于50K，不超过5MB，模板参见控制台:https://console.cloud.tencent.com/ccc/enterprise/update)
        :rtype: str
        """
        return self._OperatorMobilePicUrl

    @OperatorMobilePicUrl.setter
    def OperatorMobilePicUrl(self, OperatorMobilePicUrl):
        self._OperatorMobilePicUrl = OperatorMobilePicUrl


    def _deserialize(self, params):
        self._ApplicantType = params.get("ApplicantType")
        self._CompanyName = params.get("CompanyName")
        self._BusinessId = params.get("BusinessId")
        self._BusinessIdPicUrl = params.get("BusinessIdPicUrl")
        self._CorporationName = params.get("CorporationName")
        self._CorporationId = params.get("CorporationId")
        self._CorporationIdPicUrl = params.get("CorporationIdPicUrl")
        self._NetworkCommitmentPicUrl = params.get("NetworkCommitmentPicUrl")
        self._IsEqualTencentCloud = params.get("IsEqualTencentCloud")
        self._CorporationMobile = params.get("CorporationMobile")
        self._CorporationMobilePicUrl = params.get("CorporationMobilePicUrl")
        self._UseDescribeFileUrl = params.get("UseDescribeFileUrl")
        self._CompanyAuthLetterPicUrl = params.get("CompanyAuthLetterPicUrl")
        self._AcceptPicUrl = params.get("AcceptPicUrl")
        self._CorporationHoldingOnIdPicUrl = params.get("CorporationHoldingOnIdPicUrl")
        self._OperatorName = params.get("OperatorName")
        self._OperatorId = params.get("OperatorId")
        self._OperatorIdPicUrl = params.get("OperatorIdPicUrl")
        self._OperatorHoldingOnIdPicUrl = params.get("OperatorHoldingOnIdPicUrl")
        self._CommissionPicUrl = params.get("CommissionPicUrl")
        self._OperatorMobile = params.get("OperatorMobile")
        self._OperatorEmail = params.get("OperatorEmail")
        self._OperatorMobilePicUrl = params.get("OperatorMobilePicUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompanyStateInfo(AbstractModel):
    """公司资质审核状态信息

    """

    def __init__(self):
        r"""
        :param _Id: 申请单ID
        :type Id: int
        :param _CompanyName: 公司名称
        :type CompanyName: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _CheckTime: 审核时间
        :type CheckTime: int
        :param _CheckMsg: 审核备注
        :type CheckMsg: str
        :param _State: 审核状态，1-待审核，2-审核通过，3-驳回
        :type State: int
        :param _BusinessId: 公司统一社会信用代码
        :type BusinessId: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: int
        :param _ContractNo: 合同编号
        :type ContractNo: str
        """
        self._Id = None
        self._CompanyName = None
        self._CreateTime = None
        self._CheckTime = None
        self._CheckMsg = None
        self._State = None
        self._BusinessId = None
        self._ModifyTime = None
        self._ContractNo = None

    @property
    def Id(self):
        """申请单ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CompanyName(self):
        """公司名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CheckTime(self):
        """审核时间
        :rtype: int
        """
        return self._CheckTime

    @CheckTime.setter
    def CheckTime(self, CheckTime):
        self._CheckTime = CheckTime

    @property
    def CheckMsg(self):
        """审核备注
        :rtype: str
        """
        return self._CheckMsg

    @CheckMsg.setter
    def CheckMsg(self, CheckMsg):
        self._CheckMsg = CheckMsg

    @property
    def State(self):
        """审核状态，1-待审核，2-审核通过，3-驳回
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def BusinessId(self):
        """公司统一社会信用代码
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: int
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ContractNo(self):
        """合同编号
        :rtype: str
        """
        return self._ContractNo

    @ContractNo.setter
    def ContractNo(self, ContractNo):
        self._ContractNo = ContractNo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CompanyName = params.get("CompanyName")
        self._CreateTime = params.get("CreateTime")
        self._CheckTime = params.get("CheckTime")
        self._CheckMsg = params.get("CheckMsg")
        self._State = params.get("State")
        self._BusinessId = params.get("BusinessId")
        self._ModifyTime = params.get("ModifyTime")
        self._ContractNo = params.get("ContractNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAgentCallRequest(AbstractModel):
    """CreateAIAgentCall请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _AIAgentId: AI智能体ID
        :type AIAgentId: int
        :param _Callee: 被叫号码
        :type Callee: str
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _PromptVariables: 提示词变量
        :type PromptVariables: list of Variable
        :param _Variables: 通用变量： <p>提示词变量</p> <p>欢迎语变量</p> <p> dify变量</p>  

1. dify-inputs-xxx 为dify的inputs变量
2.  dify-inputs-user 为dify的user值
3.  dify-inputs-conversation_id 为dify的conversation_id值
        :type Variables: list of Variable
        """
        self._SdkAppId = None
        self._AIAgentId = None
        self._Callee = None
        self._Callers = None
        self._PromptVariables = None
        self._Variables = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AIAgentId(self):
        """AI智能体ID
        :rtype: int
        """
        return self._AIAgentId

    @AIAgentId.setter
    def AIAgentId(self, AIAgentId):
        self._AIAgentId = AIAgentId

    @property
    def Callee(self):
        """被叫号码
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def Callers(self):
        """主叫号码列表
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def PromptVariables(self):
        """提示词变量
        :rtype: list of Variable
        """
        return self._PromptVariables

    @PromptVariables.setter
    def PromptVariables(self, PromptVariables):
        self._PromptVariables = PromptVariables

    @property
    def Variables(self):
        """通用变量： <p>提示词变量</p> <p>欢迎语变量</p> <p> dify变量</p>  

1. dify-inputs-xxx 为dify的inputs变量
2.  dify-inputs-user 为dify的user值
3.  dify-inputs-conversation_id 为dify的conversation_id值
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._AIAgentId = params.get("AIAgentId")
        self._Callee = params.get("Callee")
        self._Callers = params.get("Callers")
        if params.get("PromptVariables") is not None:
            self._PromptVariables = []
            for item in params.get("PromptVariables"):
                obj = Variable()
                obj._deserialize(item)
                self._PromptVariables.append(obj)
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAgentCallResponse(AbstractModel):
    """CreateAIAgentCall返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 新创建的会话 ID
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        """新创建的会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateAICallRequest(AbstractModel):
    """CreateAICall请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Callee: 被叫号码
        :type Callee: str
        :param _LLMType: 模型接口协议类型，目前兼容四种协议类型：

- OpenAI协议(包括GPT、混元、DeepSeek等)："openai"
- Azure协议："azure"
- Minimax协议："minimax"
- Dify协议: "dify"
        :type LLMType: str
        :param _APIKey: 模型API密钥，获取鉴权信息方式请参见各模型官网

- OpenAI协议：[GPT](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)，[混元](https://cloud.tencent.com/document/product/1729/111008)，[DeepSeek](https://api-docs.deepseek.com/zh-cn/)；

- Azure协议：[Azure GPT](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Ctypescript%2Cpython-new&pivots=programming-language-studio#key-settings)；

- Minimax：[Minimax](https://platform.minimaxi.com/document/Fast%20access?key=66701cf51d57f38758d581b2)
        :type APIKey: str
        :param _APIUrl: 模型接口地址

- OpenAI协议
GPT："https://api.openai.com/v1/"
混元："https://api.hunyuan.cloud.tencent.com/v1"
Deepseek："https://api.deepseek.com/v1"

- Azure协议
 "https://{your-resource-name}.openai.azure.com?api-version={api-version}"

- Minimax协议
"https://api.minimax.chat/v1"
        :type APIUrl: str
        :param _SystemPrompt: 用于设定AI人设、说话规则、任务等的全局提示词。示例：## 人设您是人民医院友善、和蔼的随访医生李医生，正在给患者小明的家长打电话，原因是医院要求小明2024-08-08回院复查手术恢复情况，但小明没有来。您需要按照任务流程对小明家长进行电话随访调查。## 要求简洁回复：使用简练语言，每次最多询问一个问题，不要在一个回复中询问多个问题。富有变化：尽量使表达富有变化，表达机械重复。自然亲切：使用日常语言，尽量显得专业并亲切。提到时间时使用口语表述，如下周三、6月18日。积极主动：尝试引导对话，每个回复通常以问题或下一步建议来结尾。询问清楚：如果对方部分回答了您的问题，或者回答很模糊，请通过追问来确保回答的完整明确。遵循任务：当对方的回答偏离了您的任务时，及时引导对方回到任务中。不要从头开始重复，从偏离的地方继续询问。诚实可靠：对于客户的提问，如果不确定请务必不要编造，礼貌告知对方不清楚。不要捏造患者未提及的症状史、用药史、治疗史。其他注意点：避免提到病情恶化、恢复不理想或疾病名称等使用会使患者感到紧张的表述。不要问患者已经直接或间接回答过的问题，例如患者已经说没有不适症状，那就不要再问手术部位是否有红肿疼痛症状的问题。##任务： 1.自我介绍您是人民医院负责随访的李医生，并说明致电的目的。2.询问被叫方是否是小明家长。 - 如果不是小明家长，请礼貌表达歉意，并使用 call_end 挂断电话。- 如果小明家长没空，请礼貌告诉对方稍后会重新致电，并使用 end_call 挂断电话。3.询问小明出院后水肿情况如何，较出院时是否有变化。- 如果水肿变严重，直接跳转步骤7。4.询问出院后是否给小朋友量过体温，是否出现过发烧情况。- 如果没有量过体温，请礼貌告诉家长出院后三个月内需要每天观察体温。- 如果出现过发烧，请直接跳转步骤7。5.询问出院后是否给小朋友按时服药。- 如果没有按时服药，请友善提醒家长严格按医嘱服用药物，避免影响手术效果。6.询问小朋友在饮食上是否做到低盐低脂，适量吃优质蛋白如鸡蛋、牛奶、瘦肉等。- 如果没有做到，请友善提醒家长低盐低脂和优质蛋白有助小朋友尽快恢复。7.告知家长医生要求6月18日回院复查，但没看到有相关复诊记录。提醒家长尽快前往医院体检复查血化验、尿常规。8.询问家长是否有问题需要咨询，如果没有请礼貌道别并用call_end挂断电话。
        :type SystemPrompt: str
        :param _Model: 模型名称，如

- OpenAI协议
"gpt-4o-mini","gpt-4o"，"hunyuan-standard", "hunyuan-turbo"，"deepseek-chat"；

- Azure协议
"gpt-4o-mini", "gpt-4o"；

- Minmax协议
"deepseek-chat".
        :type Model: str
        :param _VoiceType: 默认提供以下音色参数值可选择，如需自定义音色VoiceType请留空并在参数CustomTTSConfig中配置

汉语：
ZhiMei：智美，客服女声
ZhiXi： 智希 通用女声
ZhiQi：智琪 客服女声
ZhiTian：智甜 女童声
AiXiaoJing：爱小静 对话女声

英语:
WeRose：英文女声
Monika：英文女声

日语：
Nanami

韩语：
SunHi

印度尼西亚语(印度尼西亚)：
Gadis

马来语（马来西亚）:
Yasmin

 泰米尔语（马来西亚）:
Kani

泰语（泰国）:
Achara

越南语(越南):
HoaiMy


        :type VoiceType: str
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _WelcomeMessage: 用于设定AI座席欢迎语。
        :type WelcomeMessage: str
        :param _WelcomeType: 0：使用welcomeMessage(为空时，被叫先说话；不为空时，机器人先说话)
1:   使用ai根据prompt自动生成welcomeMessage并先说话
        :type WelcomeType: int
        :param _WelcomeMessagePriority: 0: 默认可打断， 1：高优先不可打断
        :type WelcomeMessagePriority: int
        :param _MaxDuration: 最大等待时长(毫秒)，默认60秒，超过这个时间用户没说话，自动挂断
        :type MaxDuration: int
        :param _Languages: 语音识别支持的语言, 默认是"zh" 中文,
填写数组,最长4个语言，第一个语言为主要识别语言，后面为可选语言，
注意:主要语言为中国方言时，可选语言无效
目前全量支持的语言如下，等号左面是语言英文名，右面是Language字段需要填写的值，该值遵循ISO639：
1. Chinese = "zh" # 中文
2. Chinese_TW = "zh-TW" # 中国台湾
3. Chinese_DIALECT = "zh-dialect" # 中国方言
4. English = "en" # 英语
5. Vietnamese = "vi" # 越南语
6. Japanese = "ja" # 日语
7. Korean = "ko" # 汉语
8. Indonesia = "id" # 印度尼西亚语
9. Thai = "th" # 泰语
10. Portuguese = "pt" # 葡萄牙语
11. Turkish = "tr" # 土耳其语
12. Arabic = "ar" # 阿拉伯语
13. Spanish = "es" # 西班牙语
14. Hindi = "hi" # 印地语
15. French = "fr" # 法语
16. Malay = "ms" # 马来语
17. Filipino = "fil" # 菲律宾语
18. German = "de" # 德语
19. Italian = "it" # 意大利语
20. Russian = "ru" # 俄语
        :type Languages: list of str
        :param _InterruptMode: 打断AI说话模式，默认为0，0表示自动打断，1表示不打断。
        :type InterruptMode: int
        :param _InterruptSpeechDuration: InterruptMode为0时使用，单位为毫秒，默认为500ms。表示服务端检测到持续InterruptSpeechDuration毫秒的人声则进行打断。
        :type InterruptSpeechDuration: int
        :param _EndFunctionEnable: 模型是否支持(或者开启)call_end function calling
        :type EndFunctionEnable: bool
        :param _EndFunctionDesc: EndFunctionEnable为true时生效；call_end function calling的desc，默认为 "End the call when user has to leave (like says bye) or you are instructed to do so."
        :type EndFunctionDesc: str
        :param _TransferFunctionEnable: 模型是否支持(或者开启)transfer_to_human function calling
        :type TransferFunctionEnable: bool
        :param _TransferItems: TransferFunctionEnable为true的时候生效: 转人工配置
        :type TransferItems: list of AITransferItem
        :param _NotifyDuration: 用户多久没说话提示时长,最小10秒,默认10秒
        :type NotifyDuration: int
        :param _NotifyMessage: 用户NotifyDuration没说话，AI提示的语句，默认是"抱歉，我没听清。您可以重复下吗？"
        :type NotifyMessage: str
        :param _NotifyMaxCount: 最大触发AI提示音次数，默认为不限制
        :type NotifyMaxCount: int
        :param _CustomTTSConfig: <p>和VoiceType字段需要选填一个，这里是使用自己自定义的TTS，VoiceType是系统内置的一些音色</p>
<ul>
<li>Tencent TTS<br>
配置请参考<a href="https://cloud.tencent.com/document/product/1073/92668#55924b56-1a73-4663-a7a1-a8dd82d6e823" target="_blank">腾讯云TTS文档链接</a></li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{ 
       &quot;TTSType&quot;: &quot;tencent&quot;, // String TTS类型, 目前支持&quot;tencent&quot; 和 “minixmax”， 其他的厂商支持中
       &quot;AppId&quot;: &quot;您的应用ID&quot;, // String 必填
       &quot;SecretId&quot;: &quot;您的密钥ID&quot;, // String 必填
       &quot;SecretKey&quot;:  &quot;您的密钥Key&quot;, // String 必填
       &quot;VoiceType&quot;: 101001, // Integer  必填，音色 ID，包括标准音色与精品音色，精品音色拟真度更高，价格不同于标准音色，请参见语音合成计费概述。完整的音色 ID 列表请参见语音合成音色列表。
       &quot;Speed&quot;: 1.25, // Integer 非必填，语速，范围：[-2，6]，分别对应不同语速： -2: 代表0.6倍 -1: 代表0.8倍 0: 代表1.0倍（默认） 1: 代表1.2倍 2: 代表1.5倍  6: 代表2.5倍  如果需要更细化的语速，可以保留小数点后 2 位，例如0.5/1.25/2.81等。 参数值与实际语速转换，可参考 语速转换
       &quot;Volume&quot;: 5, // Integer 非必填，音量大小，范围：[0，10]，分别对应11个等级的音量，默认值为0，代表正常音量。
       &quot;PrimaryLanguage&quot;: 1, // Integer 可选 主要语言 1-中文（默认） 2-英文 3-日文
       &quot;FastVoiceType&quot;: &quot;xxxx&quot;   //  可选参数， 快速声音复刻的参数 
  }
</code></pre>

  </div></div><ul>
<li>Minimax TTS<br>
配置请参考<a href="https://platform.minimaxi.com/document/T2A%20V2?key=66719005a427f0c8a5701643" target="_blank">Minimax TTS文档链接</a>。注意Minimax TTS存在频率限制，超频可能会导致回答卡顿，<a href="https://platform.minimaxi.com/document/Rate%20limits?key=66b19417290299a26b234572" target="_blank">Minimax TTS频率限制相关文档链接</a>。</li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
        &quot;TTSType&quot;: &quot;minimax&quot;,  // String TTS类型, 
        &quot;Model&quot;: &quot;speech-01-turbo&quot;,
        &quot;APIUrl&quot;: &quot;https://api.minimax.chat/v1/t2a_v2&quot;,
        &quot;APIKey&quot;: &quot;eyxxxx&quot;,
        &quot;GroupId&quot;: &quot;181000000000000&quot;,
        &quot;VoiceType&quot;:&quot;female-tianmei-jingpin&quot;,
        &quot;Speed&quot;: 1.2
}
</code></pre>
</div></div><ul>
<li>火山 TTS</li>
</ul>
<p>配置音色类型参考<a href="https://www.volcengine.com/docs/6561/162929" target="_blank">火山TTS文档链接</a><br>
语音合成音色列表–语音技术-火山引擎<br>
大模型语音合成音色列表–语音技术-火山引擎</p>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
    &quot;TTSType&quot;: &quot;volcengine&quot;,  // 必填：String TTS类型
    &quot;AppId&quot; : &quot;xxxxxxxx&quot;,   // 必填：String 火山引擎分配的Appid
    &quot;Token&quot; : &quot;TY9d4sQXHxxxxxxx&quot;, // 必填： String类型 火山引擎的访问token
    &quot;Speed&quot; : 1.0,            // 可选参数 语速，默认为1.0
    &quot;Volume&quot;: 1.0,            // 可选参数， 音量大小， 默认为1.0
    &quot;Cluster&quot; : &quot;volcano_tts&quot;, // 可选参数，业务集群, 默认是 volcano_tts
    &quot;VoiceType&quot; : &quot;zh_male_aojiaobazong_moon_bigtts&quot;   // 音色类型， 默认为大模型语音合成的音色。 如果使用普通语音合成，则需要填写对应的音色类型。 音色类型填写错误会导致没有声音。
}
</code></pre>

</div></div><ul>
<li>Azure TTS<br>
配置请参考<a href="https://docs.azure.cn/zh-cn/ai-services/speech-service/speech-synthesis-markup-voice" target="_blank">AzureTTS文档链接</a></li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
    &quot;TTSType&quot;: &quot;azure&quot;, // 必填：String TTS类型
    &quot;SubscriptionKey&quot;: &quot;xxxxxxxx&quot;, // 必填：String 订阅的Key
    &quot;Region&quot;: &quot;chinanorth3&quot;,  // 必填：String 订阅的地区
    &quot;VoiceName&quot;: &quot;zh-CN-XiaoxiaoNeural&quot;, // 必填：String 音色名必填
    &quot;Language&quot;: &quot;zh-CN&quot;, // 必填：String 合成的语言  
    &quot;Rate&quot;: 1 // 选填：float 语速  0.5～2 默认为 1
}
</code></pre>

</div></div><ul>
<li>自定义</li>
</ul>
<p>TTS<br>
具体协议规范请参考<a href="https://doc.weixin.qq.com/doc/w3_ANQAiAbdAFwHILbJBmtSqSbV1WZ3L?scode=AJEAIQdfAAo5a1xajYANQAiAbdAFw" target="_blank">腾讯文档</a></p>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
  &quot;TTSType&quot;: &quot;custom&quot;, // String 必填
  &quot;APIKey&quot;: &quot;ApiKey&quot;, // String 必填 用来鉴权
  &quot;APIUrl&quot;: &quot;http://0.0.0.0:8080/stream-audio&quot; // String，必填，TTS API URL
  &quot;AudioFormat&quot;: &quot;wav&quot;, // String, 非必填，期望输出的音频格式，如mp3， ogg_opus，pcm，wav，默认为 wav，目前只支持pcm和wav，
  &quot;SampleRate&quot;: 16000,  // Integer，非必填，音频采样率，默认为16000(16k)，推荐值为16000
  &quot;AudioChannel&quot;: 1,    // Integer，非必填，音频通道数，取值：1 或 2  默认为1  
}
</code></pre>

</div></div>
        :type CustomTTSConfig: str
        :param _PromptVariables: 提示词变量
        :type PromptVariables: list of Variable
        :param _VadSilenceTime: 语音识别vad的时间，范围为240-2000，默认为1000，单位为ms。更小的值会让语音识别分句更快。
        :type VadSilenceTime: int
        :param _ExtractConfig: 通话内容提取配置
        :type ExtractConfig: list of AICallExtractConfigElement
        :param _Temperature: 模型温度控制
        :type Temperature: float
        :param _Variables: 通用变量： <p>提示词变量</p> <p>欢迎语变量</p> <p> dify变量</p>  

1. dify-inputs-xxx 为dify的inputs变量
2.  dify-inputs-user 为dify的user值
3.  dify-inputs-conversation_id 为dify的conversation_id值
        :type Variables: list of Variable
        """
        self._SdkAppId = None
        self._Callee = None
        self._LLMType = None
        self._APIKey = None
        self._APIUrl = None
        self._SystemPrompt = None
        self._Model = None
        self._VoiceType = None
        self._Callers = None
        self._WelcomeMessage = None
        self._WelcomeType = None
        self._WelcomeMessagePriority = None
        self._MaxDuration = None
        self._Languages = None
        self._InterruptMode = None
        self._InterruptSpeechDuration = None
        self._EndFunctionEnable = None
        self._EndFunctionDesc = None
        self._TransferFunctionEnable = None
        self._TransferItems = None
        self._NotifyDuration = None
        self._NotifyMessage = None
        self._NotifyMaxCount = None
        self._CustomTTSConfig = None
        self._PromptVariables = None
        self._VadSilenceTime = None
        self._ExtractConfig = None
        self._Temperature = None
        self._Variables = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callee(self):
        """被叫号码
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def LLMType(self):
        """模型接口协议类型，目前兼容四种协议类型：

- OpenAI协议(包括GPT、混元、DeepSeek等)："openai"
- Azure协议："azure"
- Minimax协议："minimax"
- Dify协议: "dify"
        :rtype: str
        """
        return self._LLMType

    @LLMType.setter
    def LLMType(self, LLMType):
        self._LLMType = LLMType

    @property
    def APIKey(self):
        """模型API密钥，获取鉴权信息方式请参见各模型官网

- OpenAI协议：[GPT](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)，[混元](https://cloud.tencent.com/document/product/1729/111008)，[DeepSeek](https://api-docs.deepseek.com/zh-cn/)；

- Azure协议：[Azure GPT](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Ctypescript%2Cpython-new&pivots=programming-language-studio#key-settings)；

- Minimax：[Minimax](https://platform.minimaxi.com/document/Fast%20access?key=66701cf51d57f38758d581b2)
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        self._APIKey = APIKey

    @property
    def APIUrl(self):
        """模型接口地址

- OpenAI协议
GPT："https://api.openai.com/v1/"
混元："https://api.hunyuan.cloud.tencent.com/v1"
Deepseek："https://api.deepseek.com/v1"

- Azure协议
 "https://{your-resource-name}.openai.azure.com?api-version={api-version}"

- Minimax协议
"https://api.minimax.chat/v1"
        :rtype: str
        """
        return self._APIUrl

    @APIUrl.setter
    def APIUrl(self, APIUrl):
        self._APIUrl = APIUrl

    @property
    def SystemPrompt(self):
        """用于设定AI人设、说话规则、任务等的全局提示词。示例：## 人设您是人民医院友善、和蔼的随访医生李医生，正在给患者小明的家长打电话，原因是医院要求小明2024-08-08回院复查手术恢复情况，但小明没有来。您需要按照任务流程对小明家长进行电话随访调查。## 要求简洁回复：使用简练语言，每次最多询问一个问题，不要在一个回复中询问多个问题。富有变化：尽量使表达富有变化，表达机械重复。自然亲切：使用日常语言，尽量显得专业并亲切。提到时间时使用口语表述，如下周三、6月18日。积极主动：尝试引导对话，每个回复通常以问题或下一步建议来结尾。询问清楚：如果对方部分回答了您的问题，或者回答很模糊，请通过追问来确保回答的完整明确。遵循任务：当对方的回答偏离了您的任务时，及时引导对方回到任务中。不要从头开始重复，从偏离的地方继续询问。诚实可靠：对于客户的提问，如果不确定请务必不要编造，礼貌告知对方不清楚。不要捏造患者未提及的症状史、用药史、治疗史。其他注意点：避免提到病情恶化、恢复不理想或疾病名称等使用会使患者感到紧张的表述。不要问患者已经直接或间接回答过的问题，例如患者已经说没有不适症状，那就不要再问手术部位是否有红肿疼痛症状的问题。##任务： 1.自我介绍您是人民医院负责随访的李医生，并说明致电的目的。2.询问被叫方是否是小明家长。 - 如果不是小明家长，请礼貌表达歉意，并使用 call_end 挂断电话。- 如果小明家长没空，请礼貌告诉对方稍后会重新致电，并使用 end_call 挂断电话。3.询问小明出院后水肿情况如何，较出院时是否有变化。- 如果水肿变严重，直接跳转步骤7。4.询问出院后是否给小朋友量过体温，是否出现过发烧情况。- 如果没有量过体温，请礼貌告诉家长出院后三个月内需要每天观察体温。- 如果出现过发烧，请直接跳转步骤7。5.询问出院后是否给小朋友按时服药。- 如果没有按时服药，请友善提醒家长严格按医嘱服用药物，避免影响手术效果。6.询问小朋友在饮食上是否做到低盐低脂，适量吃优质蛋白如鸡蛋、牛奶、瘦肉等。- 如果没有做到，请友善提醒家长低盐低脂和优质蛋白有助小朋友尽快恢复。7.告知家长医生要求6月18日回院复查，但没看到有相关复诊记录。提醒家长尽快前往医院体检复查血化验、尿常规。8.询问家长是否有问题需要咨询，如果没有请礼貌道别并用call_end挂断电话。
        :rtype: str
        """
        return self._SystemPrompt

    @SystemPrompt.setter
    def SystemPrompt(self, SystemPrompt):
        self._SystemPrompt = SystemPrompt

    @property
    def Model(self):
        """模型名称，如

- OpenAI协议
"gpt-4o-mini","gpt-4o"，"hunyuan-standard", "hunyuan-turbo"，"deepseek-chat"；

- Azure协议
"gpt-4o-mini", "gpt-4o"；

- Minmax协议
"deepseek-chat".
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def VoiceType(self):
        """默认提供以下音色参数值可选择，如需自定义音色VoiceType请留空并在参数CustomTTSConfig中配置

汉语：
ZhiMei：智美，客服女声
ZhiXi： 智希 通用女声
ZhiQi：智琪 客服女声
ZhiTian：智甜 女童声
AiXiaoJing：爱小静 对话女声

英语:
WeRose：英文女声
Monika：英文女声

日语：
Nanami

韩语：
SunHi

印度尼西亚语(印度尼西亚)：
Gadis

马来语（马来西亚）:
Yasmin

 泰米尔语（马来西亚）:
Kani

泰语（泰国）:
Achara

越南语(越南):
HoaiMy


        :rtype: str
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def Callers(self):
        """主叫号码列表
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def WelcomeMessage(self):
        """用于设定AI座席欢迎语。
        :rtype: str
        """
        return self._WelcomeMessage

    @WelcomeMessage.setter
    def WelcomeMessage(self, WelcomeMessage):
        self._WelcomeMessage = WelcomeMessage

    @property
    def WelcomeType(self):
        """0：使用welcomeMessage(为空时，被叫先说话；不为空时，机器人先说话)
1:   使用ai根据prompt自动生成welcomeMessage并先说话
        :rtype: int
        """
        return self._WelcomeType

    @WelcomeType.setter
    def WelcomeType(self, WelcomeType):
        self._WelcomeType = WelcomeType

    @property
    def WelcomeMessagePriority(self):
        """0: 默认可打断， 1：高优先不可打断
        :rtype: int
        """
        return self._WelcomeMessagePriority

    @WelcomeMessagePriority.setter
    def WelcomeMessagePriority(self, WelcomeMessagePriority):
        self._WelcomeMessagePriority = WelcomeMessagePriority

    @property
    def MaxDuration(self):
        """最大等待时长(毫秒)，默认60秒，超过这个时间用户没说话，自动挂断
        :rtype: int
        """
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def Languages(self):
        """语音识别支持的语言, 默认是"zh" 中文,
填写数组,最长4个语言，第一个语言为主要识别语言，后面为可选语言，
注意:主要语言为中国方言时，可选语言无效
目前全量支持的语言如下，等号左面是语言英文名，右面是Language字段需要填写的值，该值遵循ISO639：
1. Chinese = "zh" # 中文
2. Chinese_TW = "zh-TW" # 中国台湾
3. Chinese_DIALECT = "zh-dialect" # 中国方言
4. English = "en" # 英语
5. Vietnamese = "vi" # 越南语
6. Japanese = "ja" # 日语
7. Korean = "ko" # 汉语
8. Indonesia = "id" # 印度尼西亚语
9. Thai = "th" # 泰语
10. Portuguese = "pt" # 葡萄牙语
11. Turkish = "tr" # 土耳其语
12. Arabic = "ar" # 阿拉伯语
13. Spanish = "es" # 西班牙语
14. Hindi = "hi" # 印地语
15. French = "fr" # 法语
16. Malay = "ms" # 马来语
17. Filipino = "fil" # 菲律宾语
18. German = "de" # 德语
19. Italian = "it" # 意大利语
20. Russian = "ru" # 俄语
        :rtype: list of str
        """
        return self._Languages

    @Languages.setter
    def Languages(self, Languages):
        self._Languages = Languages

    @property
    def InterruptMode(self):
        """打断AI说话模式，默认为0，0表示自动打断，1表示不打断。
        :rtype: int
        """
        return self._InterruptMode

    @InterruptMode.setter
    def InterruptMode(self, InterruptMode):
        self._InterruptMode = InterruptMode

    @property
    def InterruptSpeechDuration(self):
        """InterruptMode为0时使用，单位为毫秒，默认为500ms。表示服务端检测到持续InterruptSpeechDuration毫秒的人声则进行打断。
        :rtype: int
        """
        return self._InterruptSpeechDuration

    @InterruptSpeechDuration.setter
    def InterruptSpeechDuration(self, InterruptSpeechDuration):
        self._InterruptSpeechDuration = InterruptSpeechDuration

    @property
    def EndFunctionEnable(self):
        """模型是否支持(或者开启)call_end function calling
        :rtype: bool
        """
        return self._EndFunctionEnable

    @EndFunctionEnable.setter
    def EndFunctionEnable(self, EndFunctionEnable):
        self._EndFunctionEnable = EndFunctionEnable

    @property
    def EndFunctionDesc(self):
        """EndFunctionEnable为true时生效；call_end function calling的desc，默认为 "End the call when user has to leave (like says bye) or you are instructed to do so."
        :rtype: str
        """
        return self._EndFunctionDesc

    @EndFunctionDesc.setter
    def EndFunctionDesc(self, EndFunctionDesc):
        self._EndFunctionDesc = EndFunctionDesc

    @property
    def TransferFunctionEnable(self):
        """模型是否支持(或者开启)transfer_to_human function calling
        :rtype: bool
        """
        return self._TransferFunctionEnable

    @TransferFunctionEnable.setter
    def TransferFunctionEnable(self, TransferFunctionEnable):
        self._TransferFunctionEnable = TransferFunctionEnable

    @property
    def TransferItems(self):
        """TransferFunctionEnable为true的时候生效: 转人工配置
        :rtype: list of AITransferItem
        """
        return self._TransferItems

    @TransferItems.setter
    def TransferItems(self, TransferItems):
        self._TransferItems = TransferItems

    @property
    def NotifyDuration(self):
        """用户多久没说话提示时长,最小10秒,默认10秒
        :rtype: int
        """
        return self._NotifyDuration

    @NotifyDuration.setter
    def NotifyDuration(self, NotifyDuration):
        self._NotifyDuration = NotifyDuration

    @property
    def NotifyMessage(self):
        """用户NotifyDuration没说话，AI提示的语句，默认是"抱歉，我没听清。您可以重复下吗？"
        :rtype: str
        """
        return self._NotifyMessage

    @NotifyMessage.setter
    def NotifyMessage(self, NotifyMessage):
        self._NotifyMessage = NotifyMessage

    @property
    def NotifyMaxCount(self):
        """最大触发AI提示音次数，默认为不限制
        :rtype: int
        """
        return self._NotifyMaxCount

    @NotifyMaxCount.setter
    def NotifyMaxCount(self, NotifyMaxCount):
        self._NotifyMaxCount = NotifyMaxCount

    @property
    def CustomTTSConfig(self):
        """<p>和VoiceType字段需要选填一个，这里是使用自己自定义的TTS，VoiceType是系统内置的一些音色</p>
<ul>
<li>Tencent TTS<br>
配置请参考<a href="https://cloud.tencent.com/document/product/1073/92668#55924b56-1a73-4663-a7a1-a8dd82d6e823" target="_blank">腾讯云TTS文档链接</a></li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{ 
       &quot;TTSType&quot;: &quot;tencent&quot;, // String TTS类型, 目前支持&quot;tencent&quot; 和 “minixmax”， 其他的厂商支持中
       &quot;AppId&quot;: &quot;您的应用ID&quot;, // String 必填
       &quot;SecretId&quot;: &quot;您的密钥ID&quot;, // String 必填
       &quot;SecretKey&quot;:  &quot;您的密钥Key&quot;, // String 必填
       &quot;VoiceType&quot;: 101001, // Integer  必填，音色 ID，包括标准音色与精品音色，精品音色拟真度更高，价格不同于标准音色，请参见语音合成计费概述。完整的音色 ID 列表请参见语音合成音色列表。
       &quot;Speed&quot;: 1.25, // Integer 非必填，语速，范围：[-2，6]，分别对应不同语速： -2: 代表0.6倍 -1: 代表0.8倍 0: 代表1.0倍（默认） 1: 代表1.2倍 2: 代表1.5倍  6: 代表2.5倍  如果需要更细化的语速，可以保留小数点后 2 位，例如0.5/1.25/2.81等。 参数值与实际语速转换，可参考 语速转换
       &quot;Volume&quot;: 5, // Integer 非必填，音量大小，范围：[0，10]，分别对应11个等级的音量，默认值为0，代表正常音量。
       &quot;PrimaryLanguage&quot;: 1, // Integer 可选 主要语言 1-中文（默认） 2-英文 3-日文
       &quot;FastVoiceType&quot;: &quot;xxxx&quot;   //  可选参数， 快速声音复刻的参数 
  }
</code></pre>

  </div></div><ul>
<li>Minimax TTS<br>
配置请参考<a href="https://platform.minimaxi.com/document/T2A%20V2?key=66719005a427f0c8a5701643" target="_blank">Minimax TTS文档链接</a>。注意Minimax TTS存在频率限制，超频可能会导致回答卡顿，<a href="https://platform.minimaxi.com/document/Rate%20limits?key=66b19417290299a26b234572" target="_blank">Minimax TTS频率限制相关文档链接</a>。</li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
        &quot;TTSType&quot;: &quot;minimax&quot;,  // String TTS类型, 
        &quot;Model&quot;: &quot;speech-01-turbo&quot;,
        &quot;APIUrl&quot;: &quot;https://api.minimax.chat/v1/t2a_v2&quot;,
        &quot;APIKey&quot;: &quot;eyxxxx&quot;,
        &quot;GroupId&quot;: &quot;181000000000000&quot;,
        &quot;VoiceType&quot;:&quot;female-tianmei-jingpin&quot;,
        &quot;Speed&quot;: 1.2
}
</code></pre>
</div></div><ul>
<li>火山 TTS</li>
</ul>
<p>配置音色类型参考<a href="https://www.volcengine.com/docs/6561/162929" target="_blank">火山TTS文档链接</a><br>
语音合成音色列表–语音技术-火山引擎<br>
大模型语音合成音色列表–语音技术-火山引擎</p>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
    &quot;TTSType&quot;: &quot;volcengine&quot;,  // 必填：String TTS类型
    &quot;AppId&quot; : &quot;xxxxxxxx&quot;,   // 必填：String 火山引擎分配的Appid
    &quot;Token&quot; : &quot;TY9d4sQXHxxxxxxx&quot;, // 必填： String类型 火山引擎的访问token
    &quot;Speed&quot; : 1.0,            // 可选参数 语速，默认为1.0
    &quot;Volume&quot;: 1.0,            // 可选参数， 音量大小， 默认为1.0
    &quot;Cluster&quot; : &quot;volcano_tts&quot;, // 可选参数，业务集群, 默认是 volcano_tts
    &quot;VoiceType&quot; : &quot;zh_male_aojiaobazong_moon_bigtts&quot;   // 音色类型， 默认为大模型语音合成的音色。 如果使用普通语音合成，则需要填写对应的音色类型。 音色类型填写错误会导致没有声音。
}
</code></pre>

</div></div><ul>
<li>Azure TTS<br>
配置请参考<a href="https://docs.azure.cn/zh-cn/ai-services/speech-service/speech-synthesis-markup-voice" target="_blank">AzureTTS文档链接</a></li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
    &quot;TTSType&quot;: &quot;azure&quot;, // 必填：String TTS类型
    &quot;SubscriptionKey&quot;: &quot;xxxxxxxx&quot;, // 必填：String 订阅的Key
    &quot;Region&quot;: &quot;chinanorth3&quot;,  // 必填：String 订阅的地区
    &quot;VoiceName&quot;: &quot;zh-CN-XiaoxiaoNeural&quot;, // 必填：String 音色名必填
    &quot;Language&quot;: &quot;zh-CN&quot;, // 必填：String 合成的语言  
    &quot;Rate&quot;: 1 // 选填：float 语速  0.5～2 默认为 1
}
</code></pre>

</div></div><ul>
<li>自定义</li>
</ul>
<p>TTS<br>
具体协议规范请参考<a href="https://doc.weixin.qq.com/doc/w3_ANQAiAbdAFwHILbJBmtSqSbV1WZ3L?scode=AJEAIQdfAAo5a1xajYANQAiAbdAFw" target="_blank">腾讯文档</a></p>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
  &quot;TTSType&quot;: &quot;custom&quot;, // String 必填
  &quot;APIKey&quot;: &quot;ApiKey&quot;, // String 必填 用来鉴权
  &quot;APIUrl&quot;: &quot;http://0.0.0.0:8080/stream-audio&quot; // String，必填，TTS API URL
  &quot;AudioFormat&quot;: &quot;wav&quot;, // String, 非必填，期望输出的音频格式，如mp3， ogg_opus，pcm，wav，默认为 wav，目前只支持pcm和wav，
  &quot;SampleRate&quot;: 16000,  // Integer，非必填，音频采样率，默认为16000(16k)，推荐值为16000
  &quot;AudioChannel&quot;: 1,    // Integer，非必填，音频通道数，取值：1 或 2  默认为1  
}
</code></pre>

</div></div>
        :rtype: str
        """
        return self._CustomTTSConfig

    @CustomTTSConfig.setter
    def CustomTTSConfig(self, CustomTTSConfig):
        self._CustomTTSConfig = CustomTTSConfig

    @property
    def PromptVariables(self):
        """提示词变量
        :rtype: list of Variable
        """
        return self._PromptVariables

    @PromptVariables.setter
    def PromptVariables(self, PromptVariables):
        self._PromptVariables = PromptVariables

    @property
    def VadSilenceTime(self):
        """语音识别vad的时间，范围为240-2000，默认为1000，单位为ms。更小的值会让语音识别分句更快。
        :rtype: int
        """
        return self._VadSilenceTime

    @VadSilenceTime.setter
    def VadSilenceTime(self, VadSilenceTime):
        self._VadSilenceTime = VadSilenceTime

    @property
    def ExtractConfig(self):
        """通话内容提取配置
        :rtype: list of AICallExtractConfigElement
        """
        return self._ExtractConfig

    @ExtractConfig.setter
    def ExtractConfig(self, ExtractConfig):
        self._ExtractConfig = ExtractConfig

    @property
    def Temperature(self):
        """模型温度控制
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def Variables(self):
        """通用变量： <p>提示词变量</p> <p>欢迎语变量</p> <p> dify变量</p>  

1. dify-inputs-xxx 为dify的inputs变量
2.  dify-inputs-user 为dify的user值
3.  dify-inputs-conversation_id 为dify的conversation_id值
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callee = params.get("Callee")
        self._LLMType = params.get("LLMType")
        self._APIKey = params.get("APIKey")
        self._APIUrl = params.get("APIUrl")
        self._SystemPrompt = params.get("SystemPrompt")
        self._Model = params.get("Model")
        self._VoiceType = params.get("VoiceType")
        self._Callers = params.get("Callers")
        self._WelcomeMessage = params.get("WelcomeMessage")
        self._WelcomeType = params.get("WelcomeType")
        self._WelcomeMessagePriority = params.get("WelcomeMessagePriority")
        self._MaxDuration = params.get("MaxDuration")
        self._Languages = params.get("Languages")
        self._InterruptMode = params.get("InterruptMode")
        self._InterruptSpeechDuration = params.get("InterruptSpeechDuration")
        self._EndFunctionEnable = params.get("EndFunctionEnable")
        self._EndFunctionDesc = params.get("EndFunctionDesc")
        self._TransferFunctionEnable = params.get("TransferFunctionEnable")
        if params.get("TransferItems") is not None:
            self._TransferItems = []
            for item in params.get("TransferItems"):
                obj = AITransferItem()
                obj._deserialize(item)
                self._TransferItems.append(obj)
        self._NotifyDuration = params.get("NotifyDuration")
        self._NotifyMessage = params.get("NotifyMessage")
        self._NotifyMaxCount = params.get("NotifyMaxCount")
        self._CustomTTSConfig = params.get("CustomTTSConfig")
        if params.get("PromptVariables") is not None:
            self._PromptVariables = []
            for item in params.get("PromptVariables"):
                obj = Variable()
                obj._deserialize(item)
                self._PromptVariables.append(obj)
        self._VadSilenceTime = params.get("VadSilenceTime")
        if params.get("ExtractConfig") is not None:
            self._ExtractConfig = []
            for item in params.get("ExtractConfig"):
                obj = AICallExtractConfigElement()
                obj._deserialize(item)
                self._ExtractConfig.append(obj)
        self._Temperature = params.get("Temperature")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAICallResponse(AbstractModel):
    """CreateAICall返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 新创建的会话 ID
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        """新创建的会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateAdminURLRequest(AbstractModel):
    """CreateAdminURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SeatUserId: 管理员账号
        :type SeatUserId: str
        """
        self._SdkAppId = None
        self._SeatUserId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SeatUserId(self):
        """管理员账号
        :rtype: str
        """
        return self._SeatUserId

    @SeatUserId.setter
    def SeatUserId(self, SeatUserId):
        self._SeatUserId = SeatUserId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SeatUserId = params.get("SeatUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAdminURLResponse(AbstractModel):
    """CreateAdminURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _URL: 登录链接
        :type URL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._URL = None
        self._RequestId = None

    @property
    def URL(self):
        """登录链接
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._RequestId = params.get("RequestId")


class CreateAgentCruiseDialingCampaignRequest(AbstractModel):
    """CreateAgentCruiseDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Name: 任务名称
        :type Name: str
        :param _Agent: 座席账号
        :type Agent: str
        :param _ConcurrencyNumber: 单轮并发呼叫量 1-20
        :type ConcurrencyNumber: int
        :param _StartTime: 任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :type StartTime: int
        :param _EndTime: 任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :type EndTime: int
        :param _Callees: 被叫列表，支持 E.164 或不带国家码形式的号码
        :type Callees: list of str
        :param _Callers: 主叫列表，使用管理端展示的号码格式
        :type Callers: list of str
        :param _CallOrder: 被叫呼叫顺序 0 随机 1 顺序
        :type CallOrder: int
        :param _UUI: 调用方自定义数据，最大长度 1024
        :type UUI: str
        """
        self._SdkAppId = None
        self._Name = None
        self._Agent = None
        self._ConcurrencyNumber = None
        self._StartTime = None
        self._EndTime = None
        self._Callees = None
        self._Callers = None
        self._CallOrder = None
        self._UUI = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Agent(self):
        """座席账号
        :rtype: str
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ConcurrencyNumber(self):
        """单轮并发呼叫量 1-20
        :rtype: int
        """
        return self._ConcurrencyNumber

    @ConcurrencyNumber.setter
    def ConcurrencyNumber(self, ConcurrencyNumber):
        self._ConcurrencyNumber = ConcurrencyNumber

    @property
    def StartTime(self):
        """任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Callees(self):
        """被叫列表，支持 E.164 或不带国家码形式的号码
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        """主叫列表，使用管理端展示的号码格式
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def CallOrder(self):
        """被叫呼叫顺序 0 随机 1 顺序
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def UUI(self):
        """调用方自定义数据，最大长度 1024
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._Agent = params.get("Agent")
        self._ConcurrencyNumber = params.get("ConcurrencyNumber")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._CallOrder = params.get("CallOrder")
        self._UUI = params.get("UUI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentCruiseDialingCampaignResponse(AbstractModel):
    """CreateAgentCruiseDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CampaignId: 生成的任务 ID
        :type CampaignId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CampaignId = None
        self._RequestId = None

    @property
    def CampaignId(self):
        """生成的任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CampaignId = params.get("CampaignId")
        self._RequestId = params.get("RequestId")


class CreateAutoCalloutTaskRequest(AbstractModel):
    """CreateAutoCalloutTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _NotBefore: 任务起始时间戳，Unix 秒级时间戳
        :type NotBefore: int
        :param _Callees: 被叫号码列表
        :type Callees: list of str
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _IvrId: 呼叫使用的 IVR Id，不填时需要填写 AIAgentId
        :type IvrId: int
        :param _Name: 任务名
        :type Name: str
        :param _Description: 任务描述
        :type Description: str
        :param _NotAfter: 任务停止时间戳，Unix 秒级时间戳
        :type NotAfter: int
        :param _Tries: 最大尝试次数，1-3 次
        :type Tries: int
        :param _Variables: 自定义变量（仅高级版支持）
        :type Variables: list of Variable
        :param _UUI: UUI
        :type UUI: str
        :param _CalleeAttributes: 被叫属性
        :type CalleeAttributes: list of CalleeAttribute
        :param _TimeZone: IANA 时区名称，参考 https://datatracker.ietf.org/doc/html/draft-ietf-netmod-iana-timezones
        :type TimeZone: str
        :param _AvailableTime: 可用时间段
        :type AvailableTime: list of TimeRange
        :param _AIAgentId: 智能体 ID，不填写时需要填写 IvrId
        :type AIAgentId: int
        """
        self._SdkAppId = None
        self._NotBefore = None
        self._Callees = None
        self._Callers = None
        self._IvrId = None
        self._Name = None
        self._Description = None
        self._NotAfter = None
        self._Tries = None
        self._Variables = None
        self._UUI = None
        self._CalleeAttributes = None
        self._TimeZone = None
        self._AvailableTime = None
        self._AIAgentId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def NotBefore(self):
        """任务起始时间戳，Unix 秒级时间戳
        :rtype: int
        """
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def Callees(self):
        """被叫号码列表
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        """主叫号码列表
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def IvrId(self):
        """呼叫使用的 IVR Id，不填时需要填写 AIAgentId
        :rtype: int
        """
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def Name(self):
        """任务名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NotAfter(self):
        """任务停止时间戳，Unix 秒级时间戳
        :rtype: int
        """
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def Tries(self):
        """最大尝试次数，1-3 次
        :rtype: int
        """
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def Variables(self):
        """自定义变量（仅高级版支持）
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        """UUI
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def CalleeAttributes(self):
        """被叫属性
        :rtype: list of CalleeAttribute
        """
        return self._CalleeAttributes

    @CalleeAttributes.setter
    def CalleeAttributes(self, CalleeAttributes):
        self._CalleeAttributes = CalleeAttributes

    @property
    def TimeZone(self):
        """IANA 时区名称，参考 https://datatracker.ietf.org/doc/html/draft-ietf-netmod-iana-timezones
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def AvailableTime(self):
        """可用时间段
        :rtype: list of TimeRange
        """
        return self._AvailableTime

    @AvailableTime.setter
    def AvailableTime(self, AvailableTime):
        self._AvailableTime = AvailableTime

    @property
    def AIAgentId(self):
        """智能体 ID，不填写时需要填写 IvrId
        :rtype: int
        """
        return self._AIAgentId

    @AIAgentId.setter
    def AIAgentId(self, AIAgentId):
        self._AIAgentId = AIAgentId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._NotBefore = params.get("NotBefore")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._IvrId = params.get("IvrId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._NotAfter = params.get("NotAfter")
        self._Tries = params.get("Tries")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        if params.get("CalleeAttributes") is not None:
            self._CalleeAttributes = []
            for item in params.get("CalleeAttributes"):
                obj = CalleeAttribute()
                obj._deserialize(item)
                self._CalleeAttributes.append(obj)
        self._TimeZone = params.get("TimeZone")
        if params.get("AvailableTime") is not None:
            self._AvailableTime = []
            for item in params.get("AvailableTime"):
                obj = TimeRange()
                obj._deserialize(item)
                self._AvailableTime.append(obj)
        self._AIAgentId = params.get("AIAgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoCalloutTaskResponse(AbstractModel):
    """CreateAutoCalloutTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCCCSkillGroupRequest(AbstractModel):
    """CreateCCCSkillGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param _SkillGroupType: 技能组类型0-电话，1-在线，3-音频，4-视频
        :type SkillGroupType: int
        :param _MaxConcurrency: 技能组接待人数上限（该技能组中1个座席可接待的人数上限）默认为1。1、若技能组类型为在线，则接待上限可设置为1及以上
2、若技能组类型为电话、音频、视频，则接待上线必须只能为1
        :type MaxConcurrency: int
        """
        self._SdkAppId = None
        self._SkillGroupName = None
        self._SkillGroupType = None
        self._MaxConcurrency = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SkillGroupName(self):
        """技能组名称
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def SkillGroupType(self):
        """技能组类型0-电话，1-在线，3-音频，4-视频
        :rtype: int
        """
        return self._SkillGroupType

    @SkillGroupType.setter
    def SkillGroupType(self, SkillGroupType):
        self._SkillGroupType = SkillGroupType

    @property
    def MaxConcurrency(self):
        """技能组接待人数上限（该技能组中1个座席可接待的人数上限）默认为1。1、若技能组类型为在线，则接待上限可设置为1及以上
2、若技能组类型为电话、音频、视频，则接待上线必须只能为1
        :rtype: int
        """
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._SkillGroupType = params.get("SkillGroupType")
        self._MaxConcurrency = params.get("MaxConcurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCCSkillGroupResponse(AbstractModel):
    """CreateCCCSkillGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SkillGroupId = None
        self._RequestId = None

    @property
    def SkillGroupId(self):
        """技能组ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._RequestId = params.get("RequestId")


class CreateCallOutSessionRequest(AbstractModel):
    """CreateCallOutSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID
        :type SdkAppId: int
        :param _UserId: 客服用户 ID，一般为客服邮箱，确保已经绑定了手机号 https://cloud.tencent.com/document/product/679/76067#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E5.AE.8C.E5.96.84.E8.B4.A6.E5.8F.B7.E4.BF.A1.E6.81.AF
        :type UserId: str
        :param _Callee: 被叫号码，须带 0086 前缀
        :type Callee: str
        :param _Caller: 主叫号码（废弃，使用Callers），须带 0086 前缀
        :type Caller: str
        :param _Callers: 指定主叫号码列表，如果前面的号码失败了会自动换成下一个号码，须带 0086 前缀
        :type Callers: list of str
        :param _IsForceUseMobile: 是否强制使用手机外呼，当前只支持 true，若为 true 请确保已配置白名单 https://cloud.tencent.com/document/product/679/76744#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4
        :type IsForceUseMobile: bool
        :param _Uui: 自定义数据，长度限制 1024 字节
        :type Uui: str
        :param _UUI: 自定义数据，长度限制 1024 字节
        :type UUI: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._Callee = None
        self._Caller = None
        self._Callers = None
        self._IsForceUseMobile = None
        self._Uui = None
        self._UUI = None

    @property
    def SdkAppId(self):
        """应用 ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        """客服用户 ID，一般为客服邮箱，确保已经绑定了手机号 https://cloud.tencent.com/document/product/679/76067#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E5.AE.8C.E5.96.84.E8.B4.A6.E5.8F.B7.E4.BF.A1.E6.81.AF
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Callee(self):
        """被叫号码，须带 0086 前缀
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def Caller(self):
        """主叫号码（废弃，使用Callers），须带 0086 前缀
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callers(self):
        """指定主叫号码列表，如果前面的号码失败了会自动换成下一个号码，须带 0086 前缀
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def IsForceUseMobile(self):
        """是否强制使用手机外呼，当前只支持 true，若为 true 请确保已配置白名单 https://cloud.tencent.com/document/product/679/76744#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4
        :rtype: bool
        """
        return self._IsForceUseMobile

    @IsForceUseMobile.setter
    def IsForceUseMobile(self, IsForceUseMobile):
        self._IsForceUseMobile = IsForceUseMobile

    @property
    def Uui(self):
        warnings.warn("parameter `Uui` is deprecated", DeprecationWarning) 

        """自定义数据，长度限制 1024 字节
        :rtype: str
        """
        return self._Uui

    @Uui.setter
    def Uui(self, Uui):
        warnings.warn("parameter `Uui` is deprecated", DeprecationWarning) 

        self._Uui = Uui

    @property
    def UUI(self):
        """自定义数据，长度限制 1024 字节
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._Callee = params.get("Callee")
        self._Caller = params.get("Caller")
        self._Callers = params.get("Callers")
        self._IsForceUseMobile = params.get("IsForceUseMobile")
        self._Uui = params.get("Uui")
        self._UUI = params.get("UUI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCallOutSessionResponse(AbstractModel):
    """CreateCallOutSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 新创建的会话 ID
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        """新创建的会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateCarrierPrivilegeNumberApplicantRequest(AbstractModel):
    """CreateCarrierPrivilegeNumberApplicant请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Callers: 主叫号码，必须为实例中存在的号码，格式为0086xxxx（暂时只支持国内号码）
        :type Callers: list of str
        :param _Callees: 被叫号码，必须为实例中坐席绑定的手机号码，格式为0086xxxx（暂时只支持国内号码）
        :type Callees: list of str
        :param _Description: 描述
        :type Description: str
        """
        self._SdkAppId = None
        self._Callers = None
        self._Callees = None
        self._Description = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callers(self):
        """主叫号码，必须为实例中存在的号码，格式为0086xxxx（暂时只支持国内号码）
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Callees(self):
        """被叫号码，必须为实例中坐席绑定的手机号码，格式为0086xxxx（暂时只支持国内号码）
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callers = params.get("Callers")
        self._Callees = params.get("Callees")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCarrierPrivilegeNumberApplicantResponse(AbstractModel):
    """CreateCarrierPrivilegeNumberApplicant返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicantId: 申请单Id
        :type ApplicantId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicantId = None
        self._RequestId = None

    @property
    def ApplicantId(self):
        """申请单Id
        :rtype: int
        """
        return self._ApplicantId

    @ApplicantId.setter
    def ApplicantId(self, ApplicantId):
        self._ApplicantId = ApplicantId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicantId = params.get("ApplicantId")
        self._RequestId = params.get("RequestId")


class CreateCompanyApplyRequest(AbstractModel):
    """CreateCompanyApply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyInfo: 企业资质信息
        :type CompanyInfo: :class:`tencentcloud.ccc.v20200210.models.CompanyApplyInfo`
        """
        self._CompanyInfo = None

    @property
    def CompanyInfo(self):
        """企业资质信息
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CompanyApplyInfo`
        """
        return self._CompanyInfo

    @CompanyInfo.setter
    def CompanyInfo(self, CompanyInfo):
        self._CompanyInfo = CompanyInfo


    def _deserialize(self, params):
        if params.get("CompanyInfo") is not None:
            self._CompanyInfo = CompanyApplyInfo()
            self._CompanyInfo._deserialize(params.get("CompanyInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCompanyApplyResponse(AbstractModel):
    """CreateCompanyApply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 申请单ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """申请单ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateExtensionRequest(AbstractModel):
    """CreateExtension请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        :param _ExtensionName: 分机名称
        :type ExtensionName: str
        :param _SkillGroupIds: 绑定的技能组列表
        :type SkillGroupIds: list of int non-negative
        :param _Relation: 绑定的坐席邮箱
        :type Relation: str
        """
        self._SdkAppId = None
        self._ExtensionId = None
        self._ExtensionName = None
        self._SkillGroupIds = None
        self._Relation = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """分机号
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionName(self):
        """分机名称
        :rtype: str
        """
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def SkillGroupIds(self):
        """绑定的技能组列表
        :rtype: list of int non-negative
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def Relation(self):
        """绑定的坐席邮箱
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionName = params.get("ExtensionName")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExtensionResponse(AbstractModel):
    """CreateExtension返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateIVRSessionRequest(AbstractModel):
    """CreateIVRSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Callee: 被叫
        :type Callee: str
        :param _IVRId: 指定的 IVR Id，目前支持呼入和自动外呼两种类型
        :type IVRId: int
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _Variables: 自定义变量
        :type Variables: list of Variable
        :param _UUI: 用户数据
        :type UUI: str
        """
        self._SdkAppId = None
        self._Callee = None
        self._IVRId = None
        self._Callers = None
        self._Variables = None
        self._UUI = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callee(self):
        """被叫
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def IVRId(self):
        """指定的 IVR Id，目前支持呼入和自动外呼两种类型
        :rtype: int
        """
        return self._IVRId

    @IVRId.setter
    def IVRId(self, IVRId):
        self._IVRId = IVRId

    @property
    def Callers(self):
        """主叫号码列表
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Variables(self):
        """自定义变量
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        """用户数据
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callee = params.get("Callee")
        self._IVRId = params.get("IVRId")
        self._Callers = params.get("Callers")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIVRSessionResponse(AbstractModel):
    """CreateIVRSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 新创建的会话 ID
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        """新创建的会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateOwnNumberApplyRequest(AbstractModel):
    """CreateOwnNumberApply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SipTrunkId: SIP通道ID
        :type SipTrunkId: int
        :param _DetailList: 线路相关参数
        :type DetailList: list of OwnNumberApplyDetailItem
        :param _Prefix: 送号前缀
        :type Prefix: str
        """
        self._SdkAppId = None
        self._SipTrunkId = None
        self._DetailList = None
        self._Prefix = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SipTrunkId(self):
        """SIP通道ID
        :rtype: int
        """
        return self._SipTrunkId

    @SipTrunkId.setter
    def SipTrunkId(self, SipTrunkId):
        self._SipTrunkId = SipTrunkId

    @property
    def DetailList(self):
        """线路相关参数
        :rtype: list of OwnNumberApplyDetailItem
        """
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def Prefix(self):
        """送号前缀
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SipTrunkId = params.get("SipTrunkId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = OwnNumberApplyDetailItem()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._Prefix = params.get("Prefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOwnNumberApplyResponse(AbstractModel):
    """CreateOwnNumberApply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyId: 审批单号
        :type ApplyId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplyId = None
        self._RequestId = None

    @property
    def ApplyId(self):
        """审批单号
        :rtype: int
        """
        return self._ApplyId

    @ApplyId.setter
    def ApplyId(self, ApplyId):
        self._ApplyId = ApplyId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplyId = params.get("ApplyId")
        self._RequestId = params.get("RequestId")


class CreatePredictiveDialingCampaignRequest(AbstractModel):
    """CreatePredictiveDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Name: 任务名称
        :type Name: str
        :param _Callees: 被叫列表，支持 E.164 或不带国家码形式的号码
        :type Callees: list of str
        :param _Callers: 主叫列表，使用管理端展示的号码格式
        :type Callers: list of str
        :param _CallOrder: 被叫呼叫顺序 0 随机 1 顺序
        :type CallOrder: int
        :param _SkillGroupId: 使用的座席技能组 ID
        :type SkillGroupId: int
        :param _Priority: 相同应用内多个任务运行优先级，从高到底 1 - 5
        :type Priority: int
        :param _ExpectedAbandonRate: 预期呼损率，百分比，5 - 50
        :type ExpectedAbandonRate: int
        :param _RetryInterval: 呼叫重试间隔时间，单位秒，60 - 86400
        :type RetryInterval: int
        :param _StartTime: 任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :type StartTime: int
        :param _EndTime: 任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :type EndTime: int
        :param _IVRId: 指定的 IVR Id
        :type IVRId: int
        :param _RetryTimes: 呼叫重试次数，0 - 2
        :type RetryTimes: int
        :param _Variables: 自定义变量
        :type Variables: list of Variable
        :param _UUI: UUI
        :type UUI: str
        :param _CalleeAttributes: 被叫属性
        :type CalleeAttributes: list of CalleeAttribute
        :param _TimeZone: IANA 时区名称，参考 https://datatracker.ietf.org/doc/html/draft-ietf-netmod-iana-timezones
        :type TimeZone: str
        :param _AvailableTime: 可用时间段
        :type AvailableTime: list of TimeRange
        """
        self._SdkAppId = None
        self._Name = None
        self._Callees = None
        self._Callers = None
        self._CallOrder = None
        self._SkillGroupId = None
        self._Priority = None
        self._ExpectedAbandonRate = None
        self._RetryInterval = None
        self._StartTime = None
        self._EndTime = None
        self._IVRId = None
        self._RetryTimes = None
        self._Variables = None
        self._UUI = None
        self._CalleeAttributes = None
        self._TimeZone = None
        self._AvailableTime = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Callees(self):
        """被叫列表，支持 E.164 或不带国家码形式的号码
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        """主叫列表，使用管理端展示的号码格式
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def CallOrder(self):
        """被叫呼叫顺序 0 随机 1 顺序
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def SkillGroupId(self):
        """使用的座席技能组 ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Priority(self):
        """相同应用内多个任务运行优先级，从高到底 1 - 5
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def ExpectedAbandonRate(self):
        """预期呼损率，百分比，5 - 50
        :rtype: int
        """
        return self._ExpectedAbandonRate

    @ExpectedAbandonRate.setter
    def ExpectedAbandonRate(self, ExpectedAbandonRate):
        self._ExpectedAbandonRate = ExpectedAbandonRate

    @property
    def RetryInterval(self):
        """呼叫重试间隔时间，单位秒，60 - 86400
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def StartTime(self):
        """任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IVRId(self):
        """指定的 IVR Id
        :rtype: int
        """
        return self._IVRId

    @IVRId.setter
    def IVRId(self, IVRId):
        self._IVRId = IVRId

    @property
    def RetryTimes(self):
        """呼叫重试次数，0 - 2
        :rtype: int
        """
        return self._RetryTimes

    @RetryTimes.setter
    def RetryTimes(self, RetryTimes):
        self._RetryTimes = RetryTimes

    @property
    def Variables(self):
        """自定义变量
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        """UUI
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def CalleeAttributes(self):
        """被叫属性
        :rtype: list of CalleeAttribute
        """
        return self._CalleeAttributes

    @CalleeAttributes.setter
    def CalleeAttributes(self, CalleeAttributes):
        self._CalleeAttributes = CalleeAttributes

    @property
    def TimeZone(self):
        """IANA 时区名称，参考 https://datatracker.ietf.org/doc/html/draft-ietf-netmod-iana-timezones
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def AvailableTime(self):
        """可用时间段
        :rtype: list of TimeRange
        """
        return self._AvailableTime

    @AvailableTime.setter
    def AvailableTime(self, AvailableTime):
        self._AvailableTime = AvailableTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._CallOrder = params.get("CallOrder")
        self._SkillGroupId = params.get("SkillGroupId")
        self._Priority = params.get("Priority")
        self._ExpectedAbandonRate = params.get("ExpectedAbandonRate")
        self._RetryInterval = params.get("RetryInterval")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IVRId = params.get("IVRId")
        self._RetryTimes = params.get("RetryTimes")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        if params.get("CalleeAttributes") is not None:
            self._CalleeAttributes = []
            for item in params.get("CalleeAttributes"):
                obj = CalleeAttribute()
                obj._deserialize(item)
                self._CalleeAttributes.append(obj)
        self._TimeZone = params.get("TimeZone")
        if params.get("AvailableTime") is not None:
            self._AvailableTime = []
            for item in params.get("AvailableTime"):
                obj = TimeRange()
                obj._deserialize(item)
                self._AvailableTime.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePredictiveDialingCampaignResponse(AbstractModel):
    """CreatePredictiveDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CampaignId: 生成的任务 ID
        :type CampaignId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CampaignId = None
        self._RequestId = None

    @property
    def CampaignId(self):
        """生成的任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CampaignId = params.get("CampaignId")
        self._RequestId = params.get("RequestId")


class CreateSDKLoginTokenRequest(AbstractModel):
    """CreateSDKLoginToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SeatUserId: 座席账号。
        :type SeatUserId: str
        :param _OnlyOnce: 生成的token是否一次性校验
        :type OnlyOnce: bool
        """
        self._SdkAppId = None
        self._SeatUserId = None
        self._OnlyOnce = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SeatUserId(self):
        """座席账号。
        :rtype: str
        """
        return self._SeatUserId

    @SeatUserId.setter
    def SeatUserId(self, SeatUserId):
        self._SeatUserId = SeatUserId

    @property
    def OnlyOnce(self):
        """生成的token是否一次性校验
        :rtype: bool
        """
        return self._OnlyOnce

    @OnlyOnce.setter
    def OnlyOnce(self, OnlyOnce):
        self._OnlyOnce = OnlyOnce


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SeatUserId = params.get("SeatUserId")
        self._OnlyOnce = params.get("OnlyOnce")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSDKLoginTokenResponse(AbstractModel):
    """CreateSDKLoginToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: SDK 登录 Token。
        :type Token: str
        :param _ExpiredTime: 过期时间戳，Unix 时间戳。
        :type ExpiredTime: int
        :param _SdkURL: SDK 加载路径会随着 SDK 的发布而变动。
        :type SdkURL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._ExpiredTime = None
        self._SdkURL = None
        self._RequestId = None

    @property
    def Token(self):
        """SDK 登录 Token。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiredTime(self):
        """过期时间戳，Unix 时间戳。
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def SdkURL(self):
        """SDK 加载路径会随着 SDK 的发布而变动。
        :rtype: str
        """
        return self._SdkURL

    @SdkURL.setter
    def SdkURL(self, SdkURL):
        self._SdkURL = SdkURL

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._ExpiredTime = params.get("ExpiredTime")
        self._SdkURL = params.get("SdkURL")
        self._RequestId = params.get("RequestId")


class CreateStaffRequest(AbstractModel):
    """CreateStaff请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Staffs: 客服信息，个数不超过 10
        :type Staffs: list of SeatUserInfo
        :param _SendPassword: 是否发送密码邮件，默认true
        :type SendPassword: bool
        """
        self._SdkAppId = None
        self._Staffs = None
        self._SendPassword = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Staffs(self):
        """客服信息，个数不超过 10
        :rtype: list of SeatUserInfo
        """
        return self._Staffs

    @Staffs.setter
    def Staffs(self, Staffs):
        self._Staffs = Staffs

    @property
    def SendPassword(self):
        """是否发送密码邮件，默认true
        :rtype: bool
        """
        return self._SendPassword

    @SendPassword.setter
    def SendPassword(self, SendPassword):
        self._SendPassword = SendPassword


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Staffs") is not None:
            self._Staffs = []
            for item in params.get("Staffs"):
                obj = SeatUserInfo()
                obj._deserialize(item)
                self._Staffs.append(obj)
        self._SendPassword = params.get("SendPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStaffResponse(AbstractModel):
    """CreateStaff返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorStaffList: 错误坐席列表及错误信息
        :type ErrorStaffList: list of ErrStaffItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorStaffList = None
        self._RequestId = None

    @property
    def ErrorStaffList(self):
        """错误坐席列表及错误信息
        :rtype: list of ErrStaffItem
        """
        return self._ErrorStaffList

    @ErrorStaffList.setter
    def ErrorStaffList(self, ErrorStaffList):
        self._ErrorStaffList = ErrorStaffList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorStaffList") is not None:
            self._ErrorStaffList = []
            for item in params.get("ErrorStaffList"):
                obj = ErrStaffItem()
                obj._deserialize(item)
                self._ErrorStaffList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateUserSigRequest(AbstractModel):
    """CreateUserSig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Uid: 用户 ID，该值必须与 ClientData 字段中 Uid 的值一致
        :type Uid: str
        :param _ExpiredTime: 有效期，单位秒，不超过 1 小时
        :type ExpiredTime: int
        :param _ClientData: 用户签名数据，必填字段，为标准 JSON 格式
        :type ClientData: str
        """
        self._SdkAppId = None
        self._Uid = None
        self._ExpiredTime = None
        self._ClientData = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Uid(self):
        """用户 ID，该值必须与 ClientData 字段中 Uid 的值一致
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def ExpiredTime(self):
        """有效期，单位秒，不超过 1 小时
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def ClientData(self):
        """用户签名数据，必填字段，为标准 JSON 格式
        :rtype: str
        """
        return self._ClientData

    @ClientData.setter
    def ClientData(self, ClientData):
        self._ClientData = ClientData


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Uid = params.get("Uid")
        self._ExpiredTime = params.get("ExpiredTime")
        self._ClientData = params.get("ClientData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserSigResponse(AbstractModel):
    """CreateUserSig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserSig: 签名结果
        :type UserSig: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserSig = None
        self._RequestId = None

    @property
    def UserSig(self):
        """签名结果
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserSig = params.get("UserSig")
        self._RequestId = params.get("RequestId")


class DeleteExtensionRequest(AbstractModel):
    """DeleteExtension请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """分机号
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExtensionResponse(AbstractModel):
    """DeleteExtension返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePredictiveDialingCampaignRequest(AbstractModel):
    """DeletePredictiveDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePredictiveDialingCampaignResponse(AbstractModel):
    """DeletePredictiveDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteStaffRequest(AbstractModel):
    """DeleteStaff请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StaffList: 待删除客服邮箱列表，一次最大支持200个。
        :type StaffList: list of str
        """
        self._SdkAppId = None
        self._StaffList = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffList(self):
        """待删除客服邮箱列表，一次最大支持200个。
        :rtype: list of str
        """
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffList = params.get("StaffList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStaffResponse(AbstractModel):
    """DeleteStaff返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OnlineStaffList: 无法删除的状态为在线的客服列表
        :type OnlineStaffList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OnlineStaffList = None
        self._RequestId = None

    @property
    def OnlineStaffList(self):
        """无法删除的状态为在线的客服列表
        :rtype: list of str
        """
        return self._OnlineStaffList

    @OnlineStaffList.setter
    def OnlineStaffList(self, OnlineStaffList):
        self._OnlineStaffList = OnlineStaffList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OnlineStaffList = params.get("OnlineStaffList")
        self._RequestId = params.get("RequestId")


class DescribeAICallExtractResultRequest(AbstractModel):
    """DescribeAICallExtractResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SessionId: 会话 ID
        :type SessionId: str
        :param _StartTime: 查找起始时间
        :type StartTime: int
        :param _EndTime: 查找结束时间
        :type EndTime: int
        """
        self._SdkAppId = None
        self._SessionId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def StartTime(self):
        """查找起始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查找结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAICallExtractResultResponse(AbstractModel):
    """DescribeAICallExtractResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultList: 结果列表
        :type ResultList: list of AICallExtractResultElement
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultList = None
        self._RequestId = None

    @property
    def ResultList(self):
        """结果列表
        :rtype: list of AICallExtractResultElement
        """
        return self._ResultList

    @ResultList.setter
    def ResultList(self, ResultList):
        self._ResultList = ResultList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResultList") is not None:
            self._ResultList = []
            for item in params.get("ResultList"):
                obj = AICallExtractResultElement()
                obj._deserialize(item)
                self._ResultList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAILatencyRequest(AbstractModel):
    """DescribeAILatency请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SessionId: 会话 ID
        :type SessionId: str
        :param _StartTime: 查找起始时间	
        :type StartTime: int
        :param _EndTime: 1737350008
        :type EndTime: int
        """
        self._SdkAppId = None
        self._SessionId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def StartTime(self):
        """查找起始时间	
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """1737350008
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAILatencyResponse(AbstractModel):
    """DescribeAILatency返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AILatencyDetail: 时延明细数据
 -1表示无对应数据
        :type AILatencyDetail: list of AILatencyDetail
        :param _AILatencyStatistics: 时延统计数据
 -1表示无对应数据
        :type AILatencyStatistics: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatistics`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AILatencyDetail = None
        self._AILatencyStatistics = None
        self._RequestId = None

    @property
    def AILatencyDetail(self):
        """时延明细数据
 -1表示无对应数据
        :rtype: list of AILatencyDetail
        """
        return self._AILatencyDetail

    @AILatencyDetail.setter
    def AILatencyDetail(self, AILatencyDetail):
        self._AILatencyDetail = AILatencyDetail

    @property
    def AILatencyStatistics(self):
        """时延统计数据
 -1表示无对应数据
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AILatencyStatistics`
        """
        return self._AILatencyStatistics

    @AILatencyStatistics.setter
    def AILatencyStatistics(self, AILatencyStatistics):
        self._AILatencyStatistics = AILatencyStatistics

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AILatencyDetail") is not None:
            self._AILatencyDetail = []
            for item in params.get("AILatencyDetail"):
                obj = AILatencyDetail()
                obj._deserialize(item)
                self._AILatencyDetail.append(obj)
        if params.get("AILatencyStatistics") is not None:
            self._AILatencyStatistics = AILatencyStatistics()
            self._AILatencyStatistics._deserialize(params.get("AILatencyStatistics"))
        self._RequestId = params.get("RequestId")


class DescribeActiveCarrierPrivilegeNumberRequest(AbstractModel):
    """DescribeActiveCarrierPrivilegeNumber请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageNumber: 默认0
        :type PageNumber: int
        :param _PageSize: 默认10，最大100
        :type PageSize: int
        :param _Filters: 筛选条件 Name支持PhoneNumber(按号码模糊查找)
        :type Filters: list of Filter
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        """默认0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """默认10，最大100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        """筛选条件 Name支持PhoneNumber(按号码模糊查找)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
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
        


class DescribeActiveCarrierPrivilegeNumberResponse(AbstractModel):
    """DescribeActiveCarrierPrivilegeNumber返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _ActiveCarrierPrivilegeNumbers: 生效列表
        :type ActiveCarrierPrivilegeNumbers: list of ActiveCarrierPrivilegeNumber
        :param _PendingApplicantIds: 待审核单号
        :type PendingApplicantIds: list of int non-negative
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ActiveCarrierPrivilegeNumbers = None
        self._PendingApplicantIds = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ActiveCarrierPrivilegeNumbers(self):
        """生效列表
        :rtype: list of ActiveCarrierPrivilegeNumber
        """
        return self._ActiveCarrierPrivilegeNumbers

    @ActiveCarrierPrivilegeNumbers.setter
    def ActiveCarrierPrivilegeNumbers(self, ActiveCarrierPrivilegeNumbers):
        self._ActiveCarrierPrivilegeNumbers = ActiveCarrierPrivilegeNumbers

    @property
    def PendingApplicantIds(self):
        """待审核单号
        :rtype: list of int non-negative
        """
        return self._PendingApplicantIds

    @PendingApplicantIds.setter
    def PendingApplicantIds(self, PendingApplicantIds):
        self._PendingApplicantIds = PendingApplicantIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ActiveCarrierPrivilegeNumbers") is not None:
            self._ActiveCarrierPrivilegeNumbers = []
            for item in params.get("ActiveCarrierPrivilegeNumbers"):
                obj = ActiveCarrierPrivilegeNumber()
                obj._deserialize(item)
                self._ActiveCarrierPrivilegeNumbers.append(obj)
        self._PendingApplicantIds = params.get("PendingApplicantIds")
        self._RequestId = params.get("RequestId")


class DescribeAgentCruiseDialingCampaignRequest(AbstractModel):
    """DescribeAgentCruiseDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentCruiseDialingCampaignResponse(AbstractModel):
    """DescribeAgentCruiseDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _Agent: 座席账号
        :type Agent: str
        :param _ConcurrencyNumber: 单轮并发呼叫量 1-20
        :type ConcurrencyNumber: int
        :param _StartTime: 任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :type StartTime: int
        :param _EndTime: 任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :type EndTime: int
        :param _CallOrder: 被叫呼叫顺序 0 随机 1 顺序
        :type CallOrder: int
        :param _UUI: 调用方自定义数据，最大长度 1024
        :type UUI: str
        :param _State: 任务状态 0 未启动 1 运行中 2 已完成 3 已终止
        :type State: int
        :param _TotalCalleeCount: 被叫总数
        :type TotalCalleeCount: int
        :param _CalledCalleeCount: 已呼被叫数
        :type CalledCalleeCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Agent = None
        self._ConcurrencyNumber = None
        self._StartTime = None
        self._EndTime = None
        self._CallOrder = None
        self._UUI = None
        self._State = None
        self._TotalCalleeCount = None
        self._CalledCalleeCount = None
        self._RequestId = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Agent(self):
        """座席账号
        :rtype: str
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ConcurrencyNumber(self):
        """单轮并发呼叫量 1-20
        :rtype: int
        """
        return self._ConcurrencyNumber

    @ConcurrencyNumber.setter
    def ConcurrencyNumber(self, ConcurrencyNumber):
        self._ConcurrencyNumber = ConcurrencyNumber

    @property
    def StartTime(self):
        """任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CallOrder(self):
        """被叫呼叫顺序 0 随机 1 顺序
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def UUI(self):
        """调用方自定义数据，最大长度 1024
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def State(self):
        """任务状态 0 未启动 1 运行中 2 已完成 3 已终止
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def TotalCalleeCount(self):
        """被叫总数
        :rtype: int
        """
        return self._TotalCalleeCount

    @TotalCalleeCount.setter
    def TotalCalleeCount(self, TotalCalleeCount):
        self._TotalCalleeCount = TotalCalleeCount

    @property
    def CalledCalleeCount(self):
        """已呼被叫数
        :rtype: int
        """
        return self._CalledCalleeCount

    @CalledCalleeCount.setter
    def CalledCalleeCount(self, CalledCalleeCount):
        self._CalledCalleeCount = CalledCalleeCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Agent = params.get("Agent")
        self._ConcurrencyNumber = params.get("ConcurrencyNumber")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CallOrder = params.get("CallOrder")
        self._UUI = params.get("UUI")
        self._State = params.get("State")
        self._TotalCalleeCount = params.get("TotalCalleeCount")
        self._CalledCalleeCount = params.get("CalledCalleeCount")
        self._RequestId = params.get("RequestId")


class DescribeAutoCalloutTaskRequest(AbstractModel):
    """DescribeAutoCalloutTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _TaskId: 任务Id
        :type TaskId: int
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """任务Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoCalloutTaskResponse(AbstractModel):
    """DescribeAutoCalloutTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 任务名
        :type Name: str
        :param _Description: 任务描述
        :type Description: str
        :param _NotBefore: 任务起始时间戳
        :type NotBefore: int
        :param _NotAfter: 任务结束时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type NotAfter: int
        :param _Callers: 主叫列表
        :type Callers: list of str
        :param _Callees: 被叫信息列表
        :type Callees: list of AutoCalloutTaskCalleeInfo
        :param _IvrId: 任务使用的IvrId
        :type IvrId: int
        :param _State: 任务状态 0初始 1运行中 2已完成 3结束中 4已终止
        :type State: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Description = None
        self._NotBefore = None
        self._NotAfter = None
        self._Callers = None
        self._Callees = None
        self._IvrId = None
        self._State = None
        self._RequestId = None

    @property
    def Name(self):
        """任务名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NotBefore(self):
        """任务起始时间戳
        :rtype: int
        """
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def NotAfter(self):
        """任务结束时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def Callers(self):
        """主叫列表
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Callees(self):
        """被叫信息列表
        :rtype: list of AutoCalloutTaskCalleeInfo
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def IvrId(self):
        """任务使用的IvrId
        :rtype: int
        """
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def State(self):
        """任务状态 0初始 1运行中 2已完成 3结束中 4已终止
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._NotBefore = params.get("NotBefore")
        self._NotAfter = params.get("NotAfter")
        self._Callers = params.get("Callers")
        if params.get("Callees") is not None:
            self._Callees = []
            for item in params.get("Callees"):
                obj = AutoCalloutTaskCalleeInfo()
                obj._deserialize(item)
                self._Callees.append(obj)
        self._IvrId = params.get("IvrId")
        self._State = params.get("State")
        self._RequestId = params.get("RequestId")


class DescribeAutoCalloutTasksRequest(AbstractModel):
    """DescribeAutoCalloutTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """页数
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoCalloutTasksResponse(AbstractModel):
    """DescribeAutoCalloutTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Tasks: 任务列表
        :type Tasks: list of AutoCalloutTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        """任务列表
        :rtype: list of AutoCalloutTaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = AutoCalloutTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCCBuyInfoListRequest(AbstractModel):
    """DescribeCCCBuyInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppIds: 应用ID列表，不传时查询所有应用
        :type SdkAppIds: list of int
        """
        self._SdkAppIds = None

    @property
    def SdkAppIds(self):
        """应用ID列表，不传时查询所有应用
        :rtype: list of int
        """
        return self._SdkAppIds

    @SdkAppIds.setter
    def SdkAppIds(self, SdkAppIds):
        self._SdkAppIds = SdkAppIds


    def _deserialize(self, params):
        self._SdkAppIds = params.get("SdkAppIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCCBuyInfoListResponse(AbstractModel):
    """DescribeCCCBuyInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 应用总数
        :type TotalCount: int
        :param _SdkAppIdBuyList: 应用购买信息列表
        :type SdkAppIdBuyList: list of SdkAppIdBuyInfo
        :param _PackageBuyList: 套餐包购买信息列表
        :type PackageBuyList: list of PackageBuyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SdkAppIdBuyList = None
        self._PackageBuyList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """应用总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SdkAppIdBuyList(self):
        """应用购买信息列表
        :rtype: list of SdkAppIdBuyInfo
        """
        return self._SdkAppIdBuyList

    @SdkAppIdBuyList.setter
    def SdkAppIdBuyList(self, SdkAppIdBuyList):
        self._SdkAppIdBuyList = SdkAppIdBuyList

    @property
    def PackageBuyList(self):
        """套餐包购买信息列表
        :rtype: list of PackageBuyInfo
        """
        return self._PackageBuyList

    @PackageBuyList.setter
    def PackageBuyList(self, PackageBuyList):
        self._PackageBuyList = PackageBuyList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SdkAppIdBuyList") is not None:
            self._SdkAppIdBuyList = []
            for item in params.get("SdkAppIdBuyList"):
                obj = SdkAppIdBuyInfo()
                obj._deserialize(item)
                self._SdkAppIdBuyList.append(obj)
        if params.get("PackageBuyList") is not None:
            self._PackageBuyList = []
            for item in params.get("PackageBuyList"):
                obj = PackageBuyInfo()
                obj._deserialize(item)
                self._PackageBuyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCallInMetricsRequest(AbstractModel):
    """DescribeCallInMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _EnabledSkillGroup: 是否返回技能组维度信息，默认“是”
        :type EnabledSkillGroup: bool
        :param _EnabledNumber: 是否返回线路维度信息，默认“否”
        :type EnabledNumber: bool
        :param _GroupIdList: 筛选技能组列表
        :type GroupIdList: list of int
        """
        self._SdkAppId = None
        self._EnabledSkillGroup = None
        self._EnabledNumber = None
        self._GroupIdList = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def EnabledSkillGroup(self):
        """是否返回技能组维度信息，默认“是”
        :rtype: bool
        """
        return self._EnabledSkillGroup

    @EnabledSkillGroup.setter
    def EnabledSkillGroup(self, EnabledSkillGroup):
        self._EnabledSkillGroup = EnabledSkillGroup

    @property
    def EnabledNumber(self):
        """是否返回线路维度信息，默认“否”
        :rtype: bool
        """
        return self._EnabledNumber

    @EnabledNumber.setter
    def EnabledNumber(self, EnabledNumber):
        self._EnabledNumber = EnabledNumber

    @property
    def GroupIdList(self):
        """筛选技能组列表
        :rtype: list of int
        """
        return self._GroupIdList

    @GroupIdList.setter
    def GroupIdList(self, GroupIdList):
        self._GroupIdList = GroupIdList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._EnabledSkillGroup = params.get("EnabledSkillGroup")
        self._EnabledNumber = params.get("EnabledNumber")
        self._GroupIdList = params.get("GroupIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallInMetricsResponse(AbstractModel):
    """DescribeCallInMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Timestamp: 时间戳
        :type Timestamp: int
        :param _TotalMetrics: 总体指标
        :type TotalMetrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _NumberMetrics: 线路维度指标
        :type NumberMetrics: list of CallInNumberMetrics
        :param _SkillGroupMetrics: 技能组维度指标
        :type SkillGroupMetrics: list of CallInSkillGroupMetrics
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Timestamp = None
        self._TotalMetrics = None
        self._NumberMetrics = None
        self._SkillGroupMetrics = None
        self._RequestId = None

    @property
    def Timestamp(self):
        """时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def TotalMetrics(self):
        """总体指标
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        """
        return self._TotalMetrics

    @TotalMetrics.setter
    def TotalMetrics(self, TotalMetrics):
        self._TotalMetrics = TotalMetrics

    @property
    def NumberMetrics(self):
        """线路维度指标
        :rtype: list of CallInNumberMetrics
        """
        return self._NumberMetrics

    @NumberMetrics.setter
    def NumberMetrics(self, NumberMetrics):
        self._NumberMetrics = NumberMetrics

    @property
    def SkillGroupMetrics(self):
        """技能组维度指标
        :rtype: list of CallInSkillGroupMetrics
        """
        return self._SkillGroupMetrics

    @SkillGroupMetrics.setter
    def SkillGroupMetrics(self, SkillGroupMetrics):
        self._SkillGroupMetrics = SkillGroupMetrics

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        if params.get("TotalMetrics") is not None:
            self._TotalMetrics = CallInMetrics()
            self._TotalMetrics._deserialize(params.get("TotalMetrics"))
        if params.get("NumberMetrics") is not None:
            self._NumberMetrics = []
            for item in params.get("NumberMetrics"):
                obj = CallInNumberMetrics()
                obj._deserialize(item)
                self._NumberMetrics.append(obj)
        if params.get("SkillGroupMetrics") is not None:
            self._SkillGroupMetrics = []
            for item in params.get("SkillGroupMetrics"):
                obj = CallInSkillGroupMetrics()
                obj._deserialize(item)
                self._SkillGroupMetrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCarrierPrivilegeNumberApplicantsRequest(AbstractModel):
    """DescribeCarrierPrivilegeNumberApplicants请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageNumber: 默认0，从0开始
        :type PageNumber: int
        :param _PageSize: 默认10，最大100
        :type PageSize: int
        :param _Filters: 筛选条件,Name支持ApplicantId,PhoneNumber(按号码模糊查找)
        :type Filters: list of Filter
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        """默认0，从0开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """默认10，最大100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        """筛选条件,Name支持ApplicantId,PhoneNumber(按号码模糊查找)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
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
        


class DescribeCarrierPrivilegeNumberApplicantsResponse(AbstractModel):
    """DescribeCarrierPrivilegeNumberApplicants返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 筛选出的总申请单数量
        :type TotalCount: int
        :param _Applicants: 申请单列表
        :type Applicants: list of CarrierPrivilegeNumberApplicant
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Applicants = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """筛选出的总申请单数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Applicants(self):
        """申请单列表
        :rtype: list of CarrierPrivilegeNumberApplicant
        """
        return self._Applicants

    @Applicants.setter
    def Applicants(self, Applicants):
        self._Applicants = Applicants

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Applicants") is not None:
            self._Applicants = []
            for item in params.get("Applicants"):
                obj = CarrierPrivilegeNumberApplicant()
                obj._deserialize(item)
                self._Applicants.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChatMessagesRequest(AbstractModel):
    """DescribeChatMessages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID，可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _InstanceId: 实例 ID（废弃）
        :type InstanceId: int
        :param _CdrId: 服务记录ID（废弃）
        :type CdrId: str
        :param _Limit: 返回记录条数，最大为100 默认20
        :type Limit: int
        :param _Offset: 返回记录偏移，默认为 0
        :type Offset: int
        :param _Order: 1为从早到晚，2为从晚到早，默认为2
        :type Order: int
        :param _SessionId: 服务记录 SessionID
        :type SessionId: str
        """
        self._SdkAppId = None
        self._InstanceId = None
        self._CdrId = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        """应用 ID，可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def InstanceId(self):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        """实例 ID（废弃）
        :rtype: int
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        self._InstanceId = InstanceId

    @property
    def CdrId(self):
        warnings.warn("parameter `CdrId` is deprecated", DeprecationWarning) 

        """服务记录ID（废弃）
        :rtype: str
        """
        return self._CdrId

    @CdrId.setter
    def CdrId(self, CdrId):
        warnings.warn("parameter `CdrId` is deprecated", DeprecationWarning) 

        self._CdrId = CdrId

    @property
    def Limit(self):
        """返回记录条数，最大为100 默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回记录偏移，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        """1为从早到晚，2为从晚到早，默认为2
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SessionId(self):
        """服务记录 SessionID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._InstanceId = params.get("InstanceId")
        self._CdrId = params.get("CdrId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChatMessagesResponse(AbstractModel):
    """DescribeChatMessages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _Messages: 消息列表
        :type Messages: list of MessageBody
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Messages = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Messages(self):
        """消息列表
        :rtype: list of MessageBody
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = MessageBody()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCompanyListRequest(AbstractModel):
    """DescribeCompanyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 分页尺寸，上限 100
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param _CompanyName: 公司名称
        :type CompanyName: list of str
        :param _State: 审核状态，1-待审核，2-审核通过，3-驳回
        :type State: list of int
        :param _ApplyID: 申请ID
        :type ApplyID: list of int
        """
        self._PageSize = None
        self._PageNumber = None
        self._CompanyName = None
        self._State = None
        self._ApplyID = None

    @property
    def PageSize(self):
        """分页尺寸，上限 100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """分页页码，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def CompanyName(self):
        """公司名称
        :rtype: list of str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def State(self):
        """审核状态，1-待审核，2-审核通过，3-驳回
        :rtype: list of int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ApplyID(self):
        """申请ID
        :rtype: list of int
        """
        return self._ApplyID

    @ApplyID.setter
    def ApplyID(self, ApplyID):
        self._ApplyID = ApplyID


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._CompanyName = params.get("CompanyName")
        self._State = params.get("State")
        self._ApplyID = params.get("ApplyID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompanyListResponse(AbstractModel):
    """DescribeCompanyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _CompanyInfo: 企业资质审核信息
        :type CompanyInfo: list of CompanyStateInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CompanyInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CompanyInfo(self):
        """企业资质审核信息
        :rtype: list of CompanyStateInfo
        """
        return self._CompanyInfo

    @CompanyInfo.setter
    def CompanyInfo(self, CompanyInfo):
        self._CompanyInfo = CompanyInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CompanyInfo") is not None:
            self._CompanyInfo = []
            for item in params.get("CompanyInfo"):
                obj = CompanyStateInfo()
                obj._deserialize(item)
                self._CompanyInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtensionRequest(AbstractModel):
    """DescribeExtension请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """分机号
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtensionResponse(AbstractModel):
    """DescribeExtension返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        :param _ExtensionDomain: 域名
        :type ExtensionDomain: str
        :param _Password: 注册密码
        :type Password: str
        :param _OutboundProxy: 代理服务器地址
        :type OutboundProxy: str
        :param _Transport: 传输协议
        :type Transport: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExtensionId = None
        self._ExtensionDomain = None
        self._Password = None
        self._OutboundProxy = None
        self._Transport = None
        self._RequestId = None

    @property
    def ExtensionId(self):
        """分机号
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionDomain(self):
        """域名
        :rtype: str
        """
        return self._ExtensionDomain

    @ExtensionDomain.setter
    def ExtensionDomain(self, ExtensionDomain):
        self._ExtensionDomain = ExtensionDomain

    @property
    def Password(self):
        """注册密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def OutboundProxy(self):
        """代理服务器地址
        :rtype: str
        """
        return self._OutboundProxy

    @OutboundProxy.setter
    def OutboundProxy(self, OutboundProxy):
        self._OutboundProxy = OutboundProxy

    @property
    def Transport(self):
        """传输协议
        :rtype: str
        """
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionDomain = params.get("ExtensionDomain")
        self._Password = params.get("Password")
        self._OutboundProxy = params.get("OutboundProxy")
        self._Transport = params.get("Transport")
        self._RequestId = params.get("RequestId")


class DescribeExtensionsRequest(AbstractModel):
    """DescribeExtensions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageNumber: 分页页号（从0开始）
        :type PageNumber: int
        :param _ExtensionIds: 筛选分机号列表
        :type ExtensionIds: list of str
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _FuzzingKeyWord: 模糊查询字段（模糊查询分机号、分机名称、坐席邮箱、坐席名称）
        :type FuzzingKeyWord: str
        :param _IsNeedStatus: 是否需要返回话机当前状态
        :type IsNeedStatus: bool
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._ExtensionIds = None
        self._PageSize = None
        self._FuzzingKeyWord = None
        self._IsNeedStatus = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        """分页页号（从0开始）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def ExtensionIds(self):
        """筛选分机号列表
        :rtype: list of str
        """
        return self._ExtensionIds

    @ExtensionIds.setter
    def ExtensionIds(self, ExtensionIds):
        self._ExtensionIds = ExtensionIds

    @property
    def PageSize(self):
        """分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def FuzzingKeyWord(self):
        """模糊查询字段（模糊查询分机号、分机名称、坐席邮箱、坐席名称）
        :rtype: str
        """
        return self._FuzzingKeyWord

    @FuzzingKeyWord.setter
    def FuzzingKeyWord(self, FuzzingKeyWord):
        self._FuzzingKeyWord = FuzzingKeyWord

    @property
    def IsNeedStatus(self):
        """是否需要返回话机当前状态
        :rtype: bool
        """
        return self._IsNeedStatus

    @IsNeedStatus.setter
    def IsNeedStatus(self, IsNeedStatus):
        self._IsNeedStatus = IsNeedStatus


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._ExtensionIds = params.get("ExtensionIds")
        self._PageSize = params.get("PageSize")
        self._FuzzingKeyWord = params.get("FuzzingKeyWord")
        self._IsNeedStatus = params.get("IsNeedStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtensionsResponse(AbstractModel):
    """DescribeExtensions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 查询总数
        :type Total: int
        :param _ExtensionList: 话机信息列表
        :type ExtensionList: list of ExtensionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ExtensionList = None
        self._RequestId = None

    @property
    def Total(self):
        """查询总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ExtensionList(self):
        """话机信息列表
        :rtype: list of ExtensionInfo
        """
        return self._ExtensionList

    @ExtensionList.setter
    def ExtensionList(self, ExtensionList):
        self._ExtensionList = ExtensionList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ExtensionList") is not None:
            self._ExtensionList = []
            for item in params.get("ExtensionList"):
                obj = ExtensionInfo()
                obj._deserialize(item)
                self._ExtensionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIMCdrListRequest(AbstractModel):
    """DescribeIMCdrList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StartTimestamp: 起始时间（必填），Unix 秒级时间戳
        :type StartTimestamp: int
        :param _EndTimestamp: 结束时间（必填），Unix 秒级时间戳
        :type EndTimestamp: int
        :param _Limit: 返回记录条数，最大为100默认20
        :type Limit: int
        :param _Offset: 返回记录偏移，默认为 0
        :type Offset: int
        :param _Type: 1为全媒体，2为文本客服，不填则查询全部
        :type Type: int
        """
        self._SdkAppId = None
        self._StartTimestamp = None
        self._EndTimestamp = None
        self._Limit = None
        self._Offset = None
        self._Type = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTimestamp(self):
        """起始时间（必填），Unix 秒级时间戳
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def EndTimestamp(self):
        """结束时间（必填），Unix 秒级时间戳
        :rtype: int
        """
        return self._EndTimestamp

    @EndTimestamp.setter
    def EndTimestamp(self, EndTimestamp):
        self._EndTimestamp = EndTimestamp

    @property
    def Limit(self):
        """返回记录条数，最大为100默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回记录偏移，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Type(self):
        """1为全媒体，2为文本客服，不填则查询全部
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTimestamp = params.get("StartTimestamp")
        self._EndTimestamp = params.get("EndTimestamp")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIMCdrListResponse(AbstractModel):
    """DescribeIMCdrList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _IMCdrList: 服务记录列表
        :type IMCdrList: list of IMCdrInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._IMCdrList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IMCdrList(self):
        """服务记录列表
        :rtype: list of IMCdrInfo
        """
        return self._IMCdrList

    @IMCdrList.setter
    def IMCdrList(self, IMCdrList):
        self._IMCdrList = IMCdrList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("IMCdrList") is not None:
            self._IMCdrList = []
            for item in params.get("IMCdrList"):
                obj = IMCdrInfo()
                obj._deserialize(item)
                self._IMCdrList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIMCdrsRequest(AbstractModel):
    """DescribeIMCdrs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimestamp: 起始时间（必填），Unix 秒级时间戳
        :type StartTimestamp: int
        :param _EndTimestamp: 结束时间（必填），Unix 秒级时间戳
        :type EndTimestamp: int
        :param _InstanceId: 实例 ID（废弃）
        :type InstanceId: int
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Limit: 返回记录条数，最大为100默认20
        :type Limit: int
        :param _Offset: 返回记录偏移，默认为 0
        :type Offset: int
        :param _Type: 1为全媒体，2为文本客服，不填则查询全部
        :type Type: int
        """
        self._StartTimestamp = None
        self._EndTimestamp = None
        self._InstanceId = None
        self._SdkAppId = None
        self._Limit = None
        self._Offset = None
        self._Type = None

    @property
    def StartTimestamp(self):
        """起始时间（必填），Unix 秒级时间戳
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def EndTimestamp(self):
        """结束时间（必填），Unix 秒级时间戳
        :rtype: int
        """
        return self._EndTimestamp

    @EndTimestamp.setter
    def EndTimestamp(self, EndTimestamp):
        self._EndTimestamp = EndTimestamp

    @property
    def InstanceId(self):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        """实例 ID（废弃）
        :rtype: int
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        self._InstanceId = InstanceId

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Limit(self):
        """返回记录条数，最大为100默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回记录偏移，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Type(self):
        """1为全媒体，2为文本客服，不填则查询全部
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._StartTimestamp = params.get("StartTimestamp")
        self._EndTimestamp = params.get("EndTimestamp")
        self._InstanceId = params.get("InstanceId")
        self._SdkAppId = params.get("SdkAppId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIMCdrsResponse(AbstractModel):
    """DescribeIMCdrs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _IMCdrs: 服务记录列表
        :type IMCdrs: list of IMCdrInfo
        :param _IMCdrList: 服务记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IMCdrList: list of IMCdrInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._IMCdrs = None
        self._IMCdrList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IMCdrs(self):
        warnings.warn("parameter `IMCdrs` is deprecated", DeprecationWarning) 

        """服务记录列表
        :rtype: list of IMCdrInfo
        """
        return self._IMCdrs

    @IMCdrs.setter
    def IMCdrs(self, IMCdrs):
        warnings.warn("parameter `IMCdrs` is deprecated", DeprecationWarning) 

        self._IMCdrs = IMCdrs

    @property
    def IMCdrList(self):
        """服务记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IMCdrInfo
        """
        return self._IMCdrList

    @IMCdrList.setter
    def IMCdrList(self, IMCdrList):
        self._IMCdrList = IMCdrList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("IMCdrs") is not None:
            self._IMCdrs = []
            for item in params.get("IMCdrs"):
                obj = IMCdrInfo()
                obj._deserialize(item)
                self._IMCdrs.append(obj)
        if params.get("IMCdrList") is not None:
            self._IMCdrList = []
            for item in params.get("IMCdrList"):
                obj = IMCdrInfo()
                obj._deserialize(item)
                self._IMCdrList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIvrAudioListRequest(AbstractModel):
    """DescribeIvrAudioList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸，上限 50
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param _CustomFileName: 文件别名
        :type CustomFileName: list of str
        :param _AudioFileName: 文件名
        :type AudioFileName: list of str
        :param _FileId: 文件ID
        :type FileId: list of int non-negative
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._CustomFileName = None
        self._AudioFileName = None
        self._FileId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """分页尺寸，上限 50
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """分页页码，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def CustomFileName(self):
        """文件别名
        :rtype: list of str
        """
        return self._CustomFileName

    @CustomFileName.setter
    def CustomFileName(self, CustomFileName):
        self._CustomFileName = CustomFileName

    @property
    def AudioFileName(self):
        """文件名
        :rtype: list of str
        """
        return self._AudioFileName

    @AudioFileName.setter
    def AudioFileName(self, AudioFileName):
        self._AudioFileName = AudioFileName

    @property
    def FileId(self):
        """文件ID
        :rtype: list of int non-negative
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._CustomFileName = params.get("CustomFileName")
        self._AudioFileName = params.get("AudioFileName")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIvrAudioListResponse(AbstractModel):
    """DescribeIvrAudioList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _FileInfo: 文件信息
        :type FileInfo: list of AudioFileInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._FileInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def FileInfo(self):
        """文件信息
        :rtype: list of AudioFileInfo
        """
        return self._FileInfo

    @FileInfo.setter
    def FileInfo(self, FileInfo):
        self._FileInfo = FileInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("FileInfo") is not None:
            self._FileInfo = []
            for item in params.get("FileInfo"):
                obj = AudioFileInfo()
                obj._deserialize(item)
                self._FileInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNumbersRequest(AbstractModel):
    """DescribeNumbers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageNumber: 页数，从0开始
        :type PageNumber: int
        :param _PageSize: 分页大小，默认20
        :type PageSize: int
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        """页数，从0开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """分页大小，默认20
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNumbersResponse(AbstractModel):
    """DescribeNumbers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _Numbers: 号码列表
        :type Numbers: list of NumberInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Numbers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Numbers(self):
        """号码列表
        :rtype: list of NumberInfo
        """
        return self._Numbers

    @Numbers.setter
    def Numbers(self, Numbers):
        self._Numbers = Numbers

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Numbers") is not None:
            self._Numbers = []
            for item in params.get("Numbers"):
                obj = NumberInfo()
                obj._deserialize(item)
                self._Numbers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePSTNActiveSessionListRequest(AbstractModel):
    """DescribePSTNActiveSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Offset: 数据偏移
        :type Offset: int
        :param _Limit: 返回的数据条数，最大 25
        :type Limit: int
        """
        self._SdkAppId = None
        self._Offset = None
        self._Limit = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Offset(self):
        """数据偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回的数据条数，最大 25
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePSTNActiveSessionListResponse(AbstractModel):
    """DescribePSTNActiveSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 列表总条数
        :type Total: int
        :param _Sessions: 列表内容
        :type Sessions: list of PSTNSessionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Sessions = None
        self._RequestId = None

    @property
    def Total(self):
        """列表总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Sessions(self):
        """列表内容
        :rtype: list of PSTNSessionInfo
        """
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Sessions") is not None:
            self._Sessions = []
            for item in params.get("Sessions"):
                obj = PSTNSessionInfo()
                obj._deserialize(item)
                self._Sessions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePredictiveDialingCampaignRequest(AbstractModel):
    """DescribePredictiveDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePredictiveDialingCampaignResponse(AbstractModel):
    """DescribePredictiveDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        :param _Name: 任务名称
        :type Name: str
        :param _CallOrder: 被叫呼叫顺序 0 随机 1 顺序
        :type CallOrder: int
        :param _SkillGroupId: 使用的座席技能组 ID
        :type SkillGroupId: int
        :param _IVRId: 指定的 IVR ID
        :type IVRId: int
        :param _Priority: 相同应用内多个任务运行优先级，从高到底 1 - 5
        :type Priority: int
        :param _ExpectedAbandonRate: 预期呼损率，百分比，5 - 50
        :type ExpectedAbandonRate: int
        :param _RetryTimes: 呼叫重试次数，0 - 2
        :type RetryTimes: int
        :param _RetryInterval: 呼叫重试间隔时间，单位秒，60 - 86400
        :type RetryInterval: int
        :param _StartTime: 任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :type StartTime: int
        :param _EndTime: 任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :type EndTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CampaignId = None
        self._Name = None
        self._CallOrder = None
        self._SkillGroupId = None
        self._IVRId = None
        self._Priority = None
        self._ExpectedAbandonRate = None
        self._RetryTimes = None
        self._RetryInterval = None
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CallOrder(self):
        """被叫呼叫顺序 0 随机 1 顺序
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def SkillGroupId(self):
        """使用的座席技能组 ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def IVRId(self):
        """指定的 IVR ID
        :rtype: int
        """
        return self._IVRId

    @IVRId.setter
    def IVRId(self, IVRId):
        self._IVRId = IVRId

    @property
    def Priority(self):
        """相同应用内多个任务运行优先级，从高到底 1 - 5
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def ExpectedAbandonRate(self):
        """预期呼损率，百分比，5 - 50
        :rtype: int
        """
        return self._ExpectedAbandonRate

    @ExpectedAbandonRate.setter
    def ExpectedAbandonRate(self, ExpectedAbandonRate):
        self._ExpectedAbandonRate = ExpectedAbandonRate

    @property
    def RetryTimes(self):
        """呼叫重试次数，0 - 2
        :rtype: int
        """
        return self._RetryTimes

    @RetryTimes.setter
    def RetryTimes(self, RetryTimes):
        self._RetryTimes = RetryTimes

    @property
    def RetryInterval(self):
        """呼叫重试间隔时间，单位秒，60 - 86400
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def StartTime(self):
        """任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CampaignId = params.get("CampaignId")
        self._Name = params.get("Name")
        self._CallOrder = params.get("CallOrder")
        self._SkillGroupId = params.get("SkillGroupId")
        self._IVRId = params.get("IVRId")
        self._Priority = params.get("Priority")
        self._ExpectedAbandonRate = params.get("ExpectedAbandonRate")
        self._RetryTimes = params.get("RetryTimes")
        self._RetryInterval = params.get("RetryInterval")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribePredictiveDialingCampaignsElement(AbstractModel):
    """查询预测式外呼任务列表元素

    """

    def __init__(self):
        r"""
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        :param _Name: 任务名称
        :type Name: str
        :param _Status: 任务状态 0 待开始 1 进行中 2 已暂停 3 已终止 4 已完成
        :type Status: int
        :param _StatusReason: 任务状态原因 0 正常 1 手动结束 2 超时结束
        :type StatusReason: int
        :param _CalleeCount: 被叫号码个数
        :type CalleeCount: int
        :param _FinishedCalleeCount: 已完成的被叫个数
        :type FinishedCalleeCount: int
        :param _Priority: 相同应用内多个任务运行优先级，从高到底 1 - 5
        :type Priority: int
        :param _SkillGroupId: 使用的座席技能组 ID
        :type SkillGroupId: int
        """
        self._CampaignId = None
        self._Name = None
        self._Status = None
        self._StatusReason = None
        self._CalleeCount = None
        self._FinishedCalleeCount = None
        self._Priority = None
        self._SkillGroupId = None

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """任务状态 0 待开始 1 进行中 2 已暂停 3 已终止 4 已完成
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusReason(self):
        """任务状态原因 0 正常 1 手动结束 2 超时结束
        :rtype: int
        """
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def CalleeCount(self):
        """被叫号码个数
        :rtype: int
        """
        return self._CalleeCount

    @CalleeCount.setter
    def CalleeCount(self, CalleeCount):
        self._CalleeCount = CalleeCount

    @property
    def FinishedCalleeCount(self):
        """已完成的被叫个数
        :rtype: int
        """
        return self._FinishedCalleeCount

    @FinishedCalleeCount.setter
    def FinishedCalleeCount(self, FinishedCalleeCount):
        self._FinishedCalleeCount = FinishedCalleeCount

    @property
    def Priority(self):
        """相同应用内多个任务运行优先级，从高到底 1 - 5
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def SkillGroupId(self):
        """使用的座席技能组 ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId


    def _deserialize(self, params):
        self._CampaignId = params.get("CampaignId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._StatusReason = params.get("StatusReason")
        self._CalleeCount = params.get("CalleeCount")
        self._FinishedCalleeCount = params.get("FinishedCalleeCount")
        self._Priority = params.get("Priority")
        self._SkillGroupId = params.get("SkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePredictiveDialingCampaignsRequest(AbstractModel):
    """DescribePredictiveDialingCampaigns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸，最大为 100
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param _Name: 查询任务列表名称关键字
        :type Name: str
        :param _SkillGroupId: 查询任务列表技能组 ID
        :type SkillGroupId: int
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._Name = None
        self._SkillGroupId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """分页尺寸，最大为 100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """分页页码，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Name(self):
        """查询任务列表名称关键字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SkillGroupId(self):
        """查询任务列表技能组 ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Name = params.get("Name")
        self._SkillGroupId = params.get("SkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePredictiveDialingCampaignsResponse(AbstractModel):
    """DescribePredictiveDialingCampaigns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据总量
        :type TotalCount: int
        :param _CampaignList: 数据
        :type CampaignList: list of DescribePredictiveDialingCampaignsElement
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CampaignList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """数据总量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CampaignList(self):
        """数据
        :rtype: list of DescribePredictiveDialingCampaignsElement
        """
        return self._CampaignList

    @CampaignList.setter
    def CampaignList(self, CampaignList):
        self._CampaignList = CampaignList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CampaignList") is not None:
            self._CampaignList = []
            for item in params.get("CampaignList"):
                obj = DescribePredictiveDialingCampaignsElement()
                obj._deserialize(item)
                self._CampaignList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePredictiveDialingSessionsRequest(AbstractModel):
    """DescribePredictiveDialingSessions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 生成的任务 ID
        :type CampaignId: int
        :param _PageSize: 分页尺寸，最大为 1000
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        """
        self._SdkAppId = None
        self._CampaignId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """生成的任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def PageSize(self):
        """分页尺寸，最大为 1000
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """分页页码，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePredictiveDialingSessionsResponse(AbstractModel):
    """DescribePredictiveDialingSessions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据总量
        :type TotalCount: int
        :param _SessionList: 呼叫的 session id 列表，通过 https://cloud.tencent.com/document/product/679/47714 可以批量获取呼叫详细话单
        :type SessionList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SessionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """数据总量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SessionList(self):
        """呼叫的 session id 列表，通过 https://cloud.tencent.com/document/product/679/47714 可以批量获取呼叫详细话单
        :rtype: list of str
        """
        return self._SessionList

    @SessionList.setter
    def SessionList(self, SessionList):
        self._SessionList = SessionList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._SessionList = params.get("SessionList")
        self._RequestId = params.get("RequestId")


class DescribeProtectedTelCdrRequest(AbstractModel):
    """DescribeProtectedTelCdr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 起始时间戳，Unix 秒级时间戳
        :type StartTimeStamp: int
        :param _EndTimeStamp: 结束时间戳，Unix 秒级时间戳
        :type EndTimeStamp: int
        :param _SdkAppId: 应用 ID，可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸，上限 100
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def StartTimeStamp(self):
        """起始时间戳，Unix 秒级时间戳
        :rtype: int
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        """结束时间戳，Unix 秒级时间戳
        :rtype: int
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def SdkAppId(self):
        """应用 ID，可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """分页尺寸，上限 100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """分页页码，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectedTelCdrResponse(AbstractModel):
    """DescribeProtectedTelCdr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 话单记录总数
        :type TotalCount: int
        :param _TelCdrs: 话单记录
        :type TelCdrs: list of TelCdrInfo
        :param _TelCdrList: 话单记录
        :type TelCdrList: list of TelCdrInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TelCdrs = None
        self._TelCdrList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """话单记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TelCdrs(self):
        warnings.warn("parameter `TelCdrs` is deprecated", DeprecationWarning) 

        """话单记录
        :rtype: list of TelCdrInfo
        """
        return self._TelCdrs

    @TelCdrs.setter
    def TelCdrs(self, TelCdrs):
        warnings.warn("parameter `TelCdrs` is deprecated", DeprecationWarning) 

        self._TelCdrs = TelCdrs

    @property
    def TelCdrList(self):
        """话单记录
        :rtype: list of TelCdrInfo
        """
        return self._TelCdrList

    @TelCdrList.setter
    def TelCdrList(self, TelCdrList):
        self._TelCdrList = TelCdrList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TelCdrs") is not None:
            self._TelCdrs = []
            for item in params.get("TelCdrs"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrs.append(obj)
        if params.get("TelCdrList") is not None:
            self._TelCdrList = []
            for item in params.get("TelCdrList"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSkillGroupInfoListRequest(AbstractModel):
    """DescribeSkillGroupInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸，上限 100
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param _SkillGroupId: 技能组ID，查询单个技能组时使用
        :type SkillGroupId: int
        :param _ModifiedTime: 查询修改时间大于等于ModifiedTime的技能组时使用
        :type ModifiedTime: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._SkillGroupId = None
        self._ModifiedTime = None
        self._SkillGroupName = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """分页尺寸，上限 100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """分页页码，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def SkillGroupId(self):
        """技能组ID，查询单个技能组时使用
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def ModifiedTime(self):
        """查询修改时间大于等于ModifiedTime的技能组时使用
        :rtype: int
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SkillGroupName(self):
        """技能组名称
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._SkillGroupId = params.get("SkillGroupId")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SkillGroupName = params.get("SkillGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSkillGroupInfoListResponse(AbstractModel):
    """DescribeSkillGroupInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 技能组总数
        :type TotalCount: int
        :param _SkillGroupList: 技能组信息列表
        :type SkillGroupList: list of SkillGroupInfoItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SkillGroupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """技能组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SkillGroupList(self):
        """技能组信息列表
        :rtype: list of SkillGroupInfoItem
        """
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SkillGroupList") is not None:
            self._SkillGroupList = []
            for item in params.get("SkillGroupList"):
                obj = SkillGroupInfoItem()
                obj._deserialize(item)
                self._SkillGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStaffInfoListRequest(AbstractModel):
    """DescribeStaffInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸，上限 9999
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param _StaffMail: 坐席账号，查询单个坐席时使用
        :type StaffMail: str
        :param _ModifiedTime: 查询修改时间大于等于ModifiedTime的坐席时使用
        :type ModifiedTime: int
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._StaffMail = None
        self._ModifiedTime = None
        self._SkillGroupId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """分页尺寸，上限 9999
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """分页页码，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def StaffMail(self):
        """坐席账号，查询单个坐席时使用
        :rtype: str
        """
        return self._StaffMail

    @StaffMail.setter
    def StaffMail(self, StaffMail):
        self._StaffMail = StaffMail

    @property
    def ModifiedTime(self):
        """查询修改时间大于等于ModifiedTime的坐席时使用
        :rtype: int
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SkillGroupId(self):
        """技能组ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._StaffMail = params.get("StaffMail")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SkillGroupId = params.get("SkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStaffInfoListResponse(AbstractModel):
    """DescribeStaffInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 坐席用户总数
        :type TotalCount: int
        :param _StaffList: 坐席用户信息列表
        :type StaffList: list of StaffInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._StaffList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """坐席用户总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StaffList(self):
        """坐席用户信息列表
        :rtype: list of StaffInfo
        """
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("StaffList") is not None:
            self._StaffList = []
            for item in params.get("StaffList"):
                obj = StaffInfo()
                obj._deserialize(item)
                self._StaffList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStaffStatusMetricsRequest(AbstractModel):
    """DescribeStaffStatusMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StaffList: 筛选坐席列表，默认不传返回全部坐席信息
        :type StaffList: list of str
        :param _GroupIdList: 筛选技能组ID列表
        :type GroupIdList: list of int
        :param _StatusList: 筛选坐席状态列表 座席状态 free 示闲 | busy 忙碌 | rest 小休 | notReady 示忙 | afterCallWork 话后调整 | offline 离线 
        :type StatusList: list of str
        """
        self._SdkAppId = None
        self._StaffList = None
        self._GroupIdList = None
        self._StatusList = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffList(self):
        """筛选坐席列表，默认不传返回全部坐席信息
        :rtype: list of str
        """
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList

    @property
    def GroupIdList(self):
        """筛选技能组ID列表
        :rtype: list of int
        """
        return self._GroupIdList

    @GroupIdList.setter
    def GroupIdList(self, GroupIdList):
        self._GroupIdList = GroupIdList

    @property
    def StatusList(self):
        """筛选坐席状态列表 座席状态 free 示闲 | busy 忙碌 | rest 小休 | notReady 示忙 | afterCallWork 话后调整 | offline 离线 
        :rtype: list of str
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffList = params.get("StaffList")
        self._GroupIdList = params.get("GroupIdList")
        self._StatusList = params.get("StatusList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStaffStatusMetricsResponse(AbstractModel):
    """DescribeStaffStatusMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metrics: 坐席状态实时信息
        :type Metrics: list of StaffStatusMetrics
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metrics = None
        self._RequestId = None

    @property
    def Metrics(self):
        """坐席状态实时信息
        :rtype: list of StaffStatusMetrics
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = StaffStatusMetrics()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTelCallInfoRequest(AbstractModel):
    """DescribeTelCallInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 起始时间戳，Unix 时间戳(查询维度仅支持天，例如查询5月1日应该传startTime:"2023-05-01 00:00:00","endTime":"2023-05-01 23:59:59"的时间戳,查5月1日和5月2日的应该传startTime:"2023-05-01 00:00:00","endTime":"2023-05-02 23:59:59"的时间戳)
        :type StartTimeStamp: int
        :param _EndTimeStamp: 结束时间戳，Unix 时间戳，查询时间范围最大为90天(查询维度仅支持天，例如查询5月1日应该传startTime:"2023-05-01 00:00:00","endTime":"2023-05-01 23:59:59"的时间戳,查5月1日和5月2日的应该传startTime:"2023-05-01 00:00:00","endTime":"2023-05-02 23:59:59"的时间戳)
        :type EndTimeStamp: int
        :param _SdkAppIdList: 应用ID列表，多个ID时，返回值为多个ID使用总和
        :type SdkAppIdList: list of int
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._SdkAppIdList = None

    @property
    def StartTimeStamp(self):
        """起始时间戳，Unix 时间戳(查询维度仅支持天，例如查询5月1日应该传startTime:"2023-05-01 00:00:00","endTime":"2023-05-01 23:59:59"的时间戳,查5月1日和5月2日的应该传startTime:"2023-05-01 00:00:00","endTime":"2023-05-02 23:59:59"的时间戳)
        :rtype: int
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        """结束时间戳，Unix 时间戳，查询时间范围最大为90天(查询维度仅支持天，例如查询5月1日应该传startTime:"2023-05-01 00:00:00","endTime":"2023-05-01 23:59:59"的时间戳,查5月1日和5月2日的应该传startTime:"2023-05-01 00:00:00","endTime":"2023-05-02 23:59:59"的时间戳)
        :rtype: int
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def SdkAppIdList(self):
        """应用ID列表，多个ID时，返回值为多个ID使用总和
        :rtype: list of int
        """
        return self._SdkAppIdList

    @SdkAppIdList.setter
    def SdkAppIdList(self, SdkAppIdList):
        self._SdkAppIdList = SdkAppIdList


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._SdkAppIdList = params.get("SdkAppIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelCallInfoResponse(AbstractModel):
    """DescribeTelCallInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TelCallOutCount: 呼出套餐包消耗分钟数
        :type TelCallOutCount: int
        :param _TelCallInCount: 呼入套餐包消耗分钟数
        :type TelCallInCount: int
        :param _SeatUsedCount: 坐席使用统计个数
        :type SeatUsedCount: int
        :param _VoipCallInCount: 音频套餐包消耗分钟数
        :type VoipCallInCount: int
        :param _VOIPCallInCount: 音频套餐包消耗分钟数
        :type VOIPCallInCount: int
        :param _AsrOfflineCount: 离线语音转文字套餐包消耗分钟数
        :type AsrOfflineCount: int
        :param _AsrRealtimeCount: 实时语音转文字套餐包消耗分钟数
        :type AsrRealtimeCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TelCallOutCount = None
        self._TelCallInCount = None
        self._SeatUsedCount = None
        self._VoipCallInCount = None
        self._VOIPCallInCount = None
        self._AsrOfflineCount = None
        self._AsrRealtimeCount = None
        self._RequestId = None

    @property
    def TelCallOutCount(self):
        """呼出套餐包消耗分钟数
        :rtype: int
        """
        return self._TelCallOutCount

    @TelCallOutCount.setter
    def TelCallOutCount(self, TelCallOutCount):
        self._TelCallOutCount = TelCallOutCount

    @property
    def TelCallInCount(self):
        """呼入套餐包消耗分钟数
        :rtype: int
        """
        return self._TelCallInCount

    @TelCallInCount.setter
    def TelCallInCount(self, TelCallInCount):
        self._TelCallInCount = TelCallInCount

    @property
    def SeatUsedCount(self):
        """坐席使用统计个数
        :rtype: int
        """
        return self._SeatUsedCount

    @SeatUsedCount.setter
    def SeatUsedCount(self, SeatUsedCount):
        self._SeatUsedCount = SeatUsedCount

    @property
    def VoipCallInCount(self):
        warnings.warn("parameter `VoipCallInCount` is deprecated", DeprecationWarning) 

        """音频套餐包消耗分钟数
        :rtype: int
        """
        return self._VoipCallInCount

    @VoipCallInCount.setter
    def VoipCallInCount(self, VoipCallInCount):
        warnings.warn("parameter `VoipCallInCount` is deprecated", DeprecationWarning) 

        self._VoipCallInCount = VoipCallInCount

    @property
    def VOIPCallInCount(self):
        """音频套餐包消耗分钟数
        :rtype: int
        """
        return self._VOIPCallInCount

    @VOIPCallInCount.setter
    def VOIPCallInCount(self, VOIPCallInCount):
        self._VOIPCallInCount = VOIPCallInCount

    @property
    def AsrOfflineCount(self):
        """离线语音转文字套餐包消耗分钟数
        :rtype: int
        """
        return self._AsrOfflineCount

    @AsrOfflineCount.setter
    def AsrOfflineCount(self, AsrOfflineCount):
        self._AsrOfflineCount = AsrOfflineCount

    @property
    def AsrRealtimeCount(self):
        """实时语音转文字套餐包消耗分钟数
        :rtype: int
        """
        return self._AsrRealtimeCount

    @AsrRealtimeCount.setter
    def AsrRealtimeCount(self, AsrRealtimeCount):
        self._AsrRealtimeCount = AsrRealtimeCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TelCallOutCount = params.get("TelCallOutCount")
        self._TelCallInCount = params.get("TelCallInCount")
        self._SeatUsedCount = params.get("SeatUsedCount")
        self._VoipCallInCount = params.get("VoipCallInCount")
        self._VOIPCallInCount = params.get("VOIPCallInCount")
        self._AsrOfflineCount = params.get("AsrOfflineCount")
        self._AsrRealtimeCount = params.get("AsrRealtimeCount")
        self._RequestId = params.get("RequestId")


class DescribeTelCdrRequest(AbstractModel):
    """DescribeTelCdr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 起始时间戳，Unix 秒级时间戳，最大支持近180天。
        :type StartTimeStamp: int
        :param _EndTimeStamp: 结束时间戳，Unix 秒级时间戳，结束时间与开始时间的区间范围小于90天。
        :type EndTimeStamp: int
        :param _InstanceId: 实例 ID（废弃）
        :type InstanceId: int
        :param _Limit: 返回数据条数，上限（废弃）
        :type Limit: int
        :param _Offset: 偏移（废弃）
        :type Offset: int
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸（必填），上限 100
        :type PageSize: int
        :param _PageNumber: 分页页码（必填），从 0 开始
        :type PageNumber: int
        :param _Phones: 按手机号筛选
        :type Phones: list of str
        :param _SessionIds: 按SessionId筛选
        :type SessionIds: list of str
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._Phones = None
        self._SessionIds = None

    @property
    def StartTimeStamp(self):
        """起始时间戳，Unix 秒级时间戳，最大支持近180天。
        :rtype: int
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        """结束时间戳，Unix 秒级时间戳，结束时间与开始时间的区间范围小于90天。
        :rtype: int
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def InstanceId(self):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        """实例 ID（废弃）
        :rtype: int
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """返回数据条数，上限（废弃）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移（废弃）
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """分页尺寸（必填），上限 100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """分页页码（必填），从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Phones(self):
        """按手机号筛选
        :rtype: list of str
        """
        return self._Phones

    @Phones.setter
    def Phones(self, Phones):
        self._Phones = Phones

    @property
    def SessionIds(self):
        """按SessionId筛选
        :rtype: list of str
        """
        return self._SessionIds

    @SessionIds.setter
    def SessionIds(self, SessionIds):
        self._SessionIds = SessionIds


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Phones = params.get("Phones")
        self._SessionIds = params.get("SessionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelCdrResponse(AbstractModel):
    """DescribeTelCdr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 话单记录总数
        :type TotalCount: int
        :param _TelCdrs: 话单记录
        :type TelCdrs: list of TelCdrInfo
        :param _TelCdrList: 话单记录
        :type TelCdrList: list of TelCdrInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TelCdrs = None
        self._TelCdrList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """话单记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TelCdrs(self):
        warnings.warn("parameter `TelCdrs` is deprecated", DeprecationWarning) 

        """话单记录
        :rtype: list of TelCdrInfo
        """
        return self._TelCdrs

    @TelCdrs.setter
    def TelCdrs(self, TelCdrs):
        warnings.warn("parameter `TelCdrs` is deprecated", DeprecationWarning) 

        self._TelCdrs = TelCdrs

    @property
    def TelCdrList(self):
        """话单记录
        :rtype: list of TelCdrInfo
        """
        return self._TelCdrList

    @TelCdrList.setter
    def TelCdrList(self, TelCdrList):
        self._TelCdrList = TelCdrList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TelCdrs") is not None:
            self._TelCdrs = []
            for item in params.get("TelCdrs"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrs.append(obj)
        if params.get("TelCdrList") is not None:
            self._TelCdrList = []
            for item in params.get("TelCdrList"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTelRecordAsrRequest(AbstractModel):
    """DescribeTelRecordAsr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SessionId: 会话 ID
        :type SessionId: str
        """
        self._SdkAppId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelRecordAsrResponse(AbstractModel):
    """DescribeTelRecordAsr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsrDataList: 录音转文本信息
        :type AsrDataList: list of AsrData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsrDataList = None
        self._RequestId = None

    @property
    def AsrDataList(self):
        """录音转文本信息
        :rtype: list of AsrData
        """
        return self._AsrDataList

    @AsrDataList.setter
    def AsrDataList(self, AsrDataList):
        self._AsrDataList = AsrDataList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AsrDataList") is not None:
            self._AsrDataList = []
            for item in params.get("AsrDataList"):
                obj = AsrData()
                obj._deserialize(item)
                self._AsrDataList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTelSessionRequest(AbstractModel):
    """DescribeTelSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SessionId: 会话 ID
        :type SessionId: str
        """
        self._SdkAppId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelSessionResponse(AbstractModel):
    """DescribeTelSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Session: 会话信息
        :type Session: :class:`tencentcloud.ccc.v20200210.models.PSTNSession`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        """会话信息
        :rtype: :class:`tencentcloud.ccc.v20200210.models.PSTNSession`
        """
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Session") is not None:
            self._Session = PSTNSession()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class DisableCCCPhoneNumberRequest(AbstractModel):
    """DisableCCCPhoneNumber请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PhoneNumbers: 号码列表，0086开头
        :type PhoneNumbers: list of str
        :param _Disabled: 停用开关，0启用 1停用
        :type Disabled: int
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        """
        self._PhoneNumbers = None
        self._Disabled = None
        self._SdkAppId = None

    @property
    def PhoneNumbers(self):
        """号码列表，0086开头
        :rtype: list of str
        """
        return self._PhoneNumbers

    @PhoneNumbers.setter
    def PhoneNumbers(self, PhoneNumbers):
        self._PhoneNumbers = PhoneNumbers

    @property
    def Disabled(self):
        """停用开关，0启用 1停用
        :rtype: int
        """
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def SdkAppId(self):
        """TCCC 实例应用 ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._PhoneNumbers = params.get("PhoneNumbers")
        self._Disabled = params.get("Disabled")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCCCPhoneNumberResponse(AbstractModel):
    """DisableCCCPhoneNumber返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ErrStaffItem(AbstractModel):
    """批量添加客服时，返回出错客服的信息

    """

    def __init__(self):
        r"""
        :param _StaffEmail: 座席邮箱地址
        :type StaffEmail: str
        :param _Code: 错误码
        :type Code: str
        :param _Message: 错误描述
        :type Message: str
        """
        self._StaffEmail = None
        self._Code = None
        self._Message = None

    @property
    def StaffEmail(self):
        """座席邮箱地址
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def Code(self):
        """错误码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """错误描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._StaffEmail = params.get("StaffEmail")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionInfo(AbstractModel):
    """话机信息

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 实例ID
        :type SdkAppId: int
        :param _FullExtensionId: 分机全名
        :type FullExtensionId: str
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        :param _SkillGroupId: 所属技能组列表
        :type SkillGroupId: str
        :param _ExtensionName: 分机名称
        :type ExtensionName: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _ModifyTime: 最后修改时间
        :type ModifyTime: int
        :param _Status: 话机状态(0 离线、100 空闲、200忙碌）
        :type Status: int
        :param _Register: 是否注册
        :type Register: bool
        :param _Relation: 绑定座席邮箱
        :type Relation: str
        :param _RelationName: 绑定座席名称
        :type RelationName: str
        """
        self._SdkAppId = None
        self._FullExtensionId = None
        self._ExtensionId = None
        self._SkillGroupId = None
        self._ExtensionName = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Status = None
        self._Register = None
        self._Relation = None
        self._RelationName = None

    @property
    def SdkAppId(self):
        """实例ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def FullExtensionId(self):
        """分机全名
        :rtype: str
        """
        return self._FullExtensionId

    @FullExtensionId.setter
    def FullExtensionId(self, FullExtensionId):
        self._FullExtensionId = FullExtensionId

    @property
    def ExtensionId(self):
        """分机号
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def SkillGroupId(self):
        """所属技能组列表
        :rtype: str
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def ExtensionName(self):
        """分机名称
        :rtype: str
        """
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """最后修改时间
        :rtype: int
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Status(self):
        """话机状态(0 离线、100 空闲、200忙碌）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Register(self):
        """是否注册
        :rtype: bool
        """
        return self._Register

    @Register.setter
    def Register(self, Register):
        self._Register = Register

    @property
    def Relation(self):
        """绑定座席邮箱
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation

    @property
    def RelationName(self):
        """绑定座席名称
        :rtype: str
        """
        return self._RelationName

    @RelationName.setter
    def RelationName(self, RelationName):
        self._RelationName = RelationName


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._FullExtensionId = params.get("FullExtensionId")
        self._ExtensionId = params.get("ExtensionId")
        self._SkillGroupId = params.get("SkillGroupId")
        self._ExtensionName = params.get("ExtensionName")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Status = params.get("Status")
        self._Register = params.get("Register")
        self._Relation = params.get("Relation")
        self._RelationName = params.get("RelationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """筛选条件

    """

    def __init__(self):
        r"""
        :param _Name: 筛选字段名
        :type Name: str
        :param _Values: 筛选条件值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """筛选字段名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """筛选条件值
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
        


class ForceMemberOfflineRequest(AbstractModel):
    """ForceMemberOffline请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _UserId: 客服ID
        :type UserId: str
        """
        self._SdkAppId = None
        self._UserId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        """客服ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceMemberOfflineResponse(AbstractModel):
    """ForceMemberOffline返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class HangUpCallRequest(AbstractModel):
    """HangUpCall请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SessionId: 会话ID
        :type SessionId: str
        """
        self._SdkAppId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HangUpCallResponse(AbstractModel):
    """HangUpCall返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class IMCdrInfo(AbstractModel):
    """文本会话服务记录信息

    """

    def __init__(self):
        r"""
        :param _Id: 服务记录ID
        :type Id: str
        :param _Duration: 服务时长秒数
        :type Duration: int
        :param _EndStatus: 结束状态
0 异常结束
1 正常结束
3 无座席在线
17 座席放弃接听
100 黑名单
101 座席手动转接
102 IVR阶段放弃
108 用户超时自动结束
109 用户主动结束
        :type EndStatus: int
        :param _Nickname: 用户昵称
        :type Nickname: str
        :param _Type: 服务类型 1为全媒体，2为文本客服
        :type Type: int
        :param _StaffId: 客服ID
        :type StaffId: str
        :param _Timestamp: 服务时间戳
        :type Timestamp: int
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: str
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param _Satisfaction: 满意度
注意：此字段可能返回 null，表示取不到有效值。
        :type Satisfaction: :class:`tencentcloud.ccc.v20200210.models.IMSatisfaction`
        :param _ClientUserId: 用户ID
        :type ClientUserId: str
        """
        self._Id = None
        self._Duration = None
        self._EndStatus = None
        self._Nickname = None
        self._Type = None
        self._StaffId = None
        self._Timestamp = None
        self._SessionId = None
        self._SkillGroupId = None
        self._SkillGroupName = None
        self._Satisfaction = None
        self._ClientUserId = None

    @property
    def Id(self):
        """服务记录ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Duration(self):
        """服务时长秒数
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def EndStatus(self):
        """结束状态
0 异常结束
1 正常结束
3 无座席在线
17 座席放弃接听
100 黑名单
101 座席手动转接
102 IVR阶段放弃
108 用户超时自动结束
109 用户主动结束
        :rtype: int
        """
        return self._EndStatus

    @EndStatus.setter
    def EndStatus(self, EndStatus):
        self._EndStatus = EndStatus

    @property
    def Nickname(self):
        """用户昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Type(self):
        """服务类型 1为全媒体，2为文本客服
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StaffId(self):
        """客服ID
        :rtype: str
        """
        return self._StaffId

    @StaffId.setter
    def StaffId(self, StaffId):
        self._StaffId = StaffId

    @property
    def Timestamp(self):
        """服务时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SessionId(self):
        """会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SkillGroupId(self):
        """技能组ID
        :rtype: str
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def SkillGroupName(self):
        """技能组名称
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def Satisfaction(self):
        """满意度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ccc.v20200210.models.IMSatisfaction`
        """
        return self._Satisfaction

    @Satisfaction.setter
    def Satisfaction(self, Satisfaction):
        self._Satisfaction = Satisfaction

    @property
    def ClientUserId(self):
        """用户ID
        :rtype: str
        """
        return self._ClientUserId

    @ClientUserId.setter
    def ClientUserId(self, ClientUserId):
        self._ClientUserId = ClientUserId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Duration = params.get("Duration")
        self._EndStatus = params.get("EndStatus")
        self._Nickname = params.get("Nickname")
        self._Type = params.get("Type")
        self._StaffId = params.get("StaffId")
        self._Timestamp = params.get("Timestamp")
        self._SessionId = params.get("SessionId")
        self._SkillGroupId = params.get("SkillGroupId")
        self._SkillGroupName = params.get("SkillGroupName")
        if params.get("Satisfaction") is not None:
            self._Satisfaction = IMSatisfaction()
            self._Satisfaction._deserialize(params.get("Satisfaction"))
        self._ClientUserId = params.get("ClientUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IMSatisfaction(AbstractModel):
    """IM满意度

    """

    def __init__(self):
        r"""
        :param _Id: 满意度值
        :type Id: int
        :param _Label: 满意度标签
        :type Label: str
        """
        self._Id = None
        self._Label = None

    @property
    def Id(self):
        """满意度值
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Label(self):
        """满意度标签
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IVRKeyPressedElement(AbstractModel):
    """ivr 按键信息

    """

    def __init__(self):
        r"""
        :param _Key: 命中的关键字或者按键
        :type Key: str
        :param _Label: 按键关联的标签
        :type Label: str
        :param _Timestamp: Unix 毫秒时间戳
        :type Timestamp: int
        :param _NodeLabel: 节点标签
        :type NodeLabel: str
        :param _OriginalContent: 用户原始输入
        :type OriginalContent: str
        :param _TTSPrompt: TTS 提示音内容
        :type TTSPrompt: str
        """
        self._Key = None
        self._Label = None
        self._Timestamp = None
        self._NodeLabel = None
        self._OriginalContent = None
        self._TTSPrompt = None

    @property
    def Key(self):
        """命中的关键字或者按键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Label(self):
        """按键关联的标签
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Timestamp(self):
        """Unix 毫秒时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def NodeLabel(self):
        """节点标签
        :rtype: str
        """
        return self._NodeLabel

    @NodeLabel.setter
    def NodeLabel(self, NodeLabel):
        self._NodeLabel = NodeLabel

    @property
    def OriginalContent(self):
        """用户原始输入
        :rtype: str
        """
        return self._OriginalContent

    @OriginalContent.setter
    def OriginalContent(self, OriginalContent):
        self._OriginalContent = OriginalContent

    @property
    def TTSPrompt(self):
        """TTS 提示音内容
        :rtype: str
        """
        return self._TTSPrompt

    @TTSPrompt.setter
    def TTSPrompt(self, TTSPrompt):
        self._TTSPrompt = TTSPrompt


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Label = params.get("Label")
        self._Timestamp = params.get("Timestamp")
        self._NodeLabel = params.get("NodeLabel")
        self._OriginalContent = params.get("OriginalContent")
        self._TTSPrompt = params.get("TTSPrompt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Message(AbstractModel):
    """单条消息

    """

    def __init__(self):
        r"""
        :param _Type: 消息类型
        :type Type: str
        :param _Content: 消息内容
        :type Content: str
        """
        self._Type = None
        self._Content = None

    @property
    def Type(self):
        """消息类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Content(self):
        """消息内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageBody(AbstractModel):
    """聊天消息

    """

    def __init__(self):
        r"""
        :param _Timestamp: 消息时间戳
        :type Timestamp: int
        :param _From: 发消息的用户ID
        :type From: str
        :param _Messages: 消息列表
        :type Messages: list of Message
        """
        self._Timestamp = None
        self._From = None
        self._Messages = None

    @property
    def Timestamp(self):
        """消息时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def From(self):
        """发消息的用户ID
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Messages(self):
        """消息列表
        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._From = params.get("From")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompanyApplyRequest(AbstractModel):
    """ModifyCompanyApply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyId: 申请单ID(只能修改状态为“驳回”或者“待审核”的申请单)
        :type ApplyId: int
        :param _CompanyInfo: 企业资质信息
        :type CompanyInfo: :class:`tencentcloud.ccc.v20200210.models.CompanyApplyInfo`
        """
        self._ApplyId = None
        self._CompanyInfo = None

    @property
    def ApplyId(self):
        """申请单ID(只能修改状态为“驳回”或者“待审核”的申请单)
        :rtype: int
        """
        return self._ApplyId

    @ApplyId.setter
    def ApplyId(self, ApplyId):
        self._ApplyId = ApplyId

    @property
    def CompanyInfo(self):
        """企业资质信息
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CompanyApplyInfo`
        """
        return self._CompanyInfo

    @CompanyInfo.setter
    def CompanyInfo(self, CompanyInfo):
        self._CompanyInfo = CompanyInfo


    def _deserialize(self, params):
        self._ApplyId = params.get("ApplyId")
        if params.get("CompanyInfo") is not None:
            self._CompanyInfo = CompanyApplyInfo()
            self._CompanyInfo._deserialize(params.get("CompanyInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompanyApplyResponse(AbstractModel):
    """ModifyCompanyApply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyExtensionRequest(AbstractModel):
    """ModifyExtension请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        :param _ExtensionName: 分机名称
        :type ExtensionName: str
        :param _SkillGroupIds: 所属技能组列表
        :type SkillGroupIds: list of int
        :param _Relation: 绑定坐席邮箱账号
        :type Relation: str
        """
        self._SdkAppId = None
        self._ExtensionId = None
        self._ExtensionName = None
        self._SkillGroupIds = None
        self._Relation = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """分机号
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionName(self):
        """分机名称
        :rtype: str
        """
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def SkillGroupIds(self):
        """所属技能组列表
        :rtype: list of int
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def Relation(self):
        """绑定坐席邮箱账号
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionName = params.get("ExtensionName")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExtensionResponse(AbstractModel):
    """ModifyExtension返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyOwnNumberApplyRequest(AbstractModel):
    """ModifyOwnNumberApply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _DetailList: 线路相关参数
        :type DetailList: list of OwnNumberApplyDetailItem
        :param _ApplyId: 审批单号
        :type ApplyId: int
        :param _Prefix: 送号前缀
        :type Prefix: str
        """
        self._SdkAppId = None
        self._DetailList = None
        self._ApplyId = None
        self._Prefix = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def DetailList(self):
        """线路相关参数
        :rtype: list of OwnNumberApplyDetailItem
        """
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def ApplyId(self):
        """审批单号
        :rtype: int
        """
        return self._ApplyId

    @ApplyId.setter
    def ApplyId(self, ApplyId):
        self._ApplyId = ApplyId

    @property
    def Prefix(self):
        """送号前缀
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = OwnNumberApplyDetailItem()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._ApplyId = params.get("ApplyId")
        self._Prefix = params.get("Prefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOwnNumberApplyResponse(AbstractModel):
    """ModifyOwnNumberApply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyStaffPasswordRequest(AbstractModel):
    """ModifyStaffPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Email: 座席邮箱
        :type Email: str
        :param _Password: 设置的密码
        :type Password: str
        """
        self._SdkAppId = None
        self._Email = None
        self._Password = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Email(self):
        """座席邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Password(self):
        """设置的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Email = params.get("Email")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStaffPasswordResponse(AbstractModel):
    """ModifyStaffPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyStaffRequest(AbstractModel):
    """ModifyStaff请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Email: 座席账户
        :type Email: str
        :param _Name: 座席名称
        :type Name: str
        :param _Phone: 座席手机号（带0086前缀,示例：008618011111111）
        :type Phone: str
        :param _Nick: 座席昵称
        :type Nick: str
        :param _StaffNo: 座席工号
        :type StaffNo: str
        :param _SkillGroupIds: 绑定技能组ID列表
        :type SkillGroupIds: list of int
        :param _UseMobileCallOut: 是否开启手机外呼开关
        :type UseMobileCallOut: bool
        :param _UseMobileAccept: 手机接听模式 0 - 关闭 | 1 - 仅离线 | 2 - 始终
        :type UseMobileAccept: int
        :param _ExtensionNumber: 座席分机号（1 到 8 打头，4 - 6 位）
        :type ExtensionNumber: str
        """
        self._SdkAppId = None
        self._Email = None
        self._Name = None
        self._Phone = None
        self._Nick = None
        self._StaffNo = None
        self._SkillGroupIds = None
        self._UseMobileCallOut = None
        self._UseMobileAccept = None
        self._ExtensionNumber = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Email(self):
        """座席账户
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Name(self):
        """座席名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        """座席手机号（带0086前缀,示例：008618011111111）
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        """座席昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def StaffNo(self):
        """座席工号
        :rtype: str
        """
        return self._StaffNo

    @StaffNo.setter
    def StaffNo(self, StaffNo):
        self._StaffNo = StaffNo

    @property
    def SkillGroupIds(self):
        """绑定技能组ID列表
        :rtype: list of int
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def UseMobileCallOut(self):
        """是否开启手机外呼开关
        :rtype: bool
        """
        return self._UseMobileCallOut

    @UseMobileCallOut.setter
    def UseMobileCallOut(self, UseMobileCallOut):
        self._UseMobileCallOut = UseMobileCallOut

    @property
    def UseMobileAccept(self):
        """手机接听模式 0 - 关闭 | 1 - 仅离线 | 2 - 始终
        :rtype: int
        """
        return self._UseMobileAccept

    @UseMobileAccept.setter
    def UseMobileAccept(self, UseMobileAccept):
        self._UseMobileAccept = UseMobileAccept

    @property
    def ExtensionNumber(self):
        """座席分机号（1 到 8 打头，4 - 6 位）
        :rtype: str
        """
        return self._ExtensionNumber

    @ExtensionNumber.setter
    def ExtensionNumber(self, ExtensionNumber):
        self._ExtensionNumber = ExtensionNumber


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Email = params.get("Email")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._StaffNo = params.get("StaffNo")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._UseMobileCallOut = params.get("UseMobileCallOut")
        self._UseMobileAccept = params.get("UseMobileAccept")
        self._ExtensionNumber = params.get("ExtensionNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStaffResponse(AbstractModel):
    """ModifyStaff返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NumberInfo(AbstractModel):
    """号码信息

    """

    def __init__(self):
        r"""
        :param _Number: 号码
        :type Number: str
        :param _CallOutSkillGroupIds: 绑定的外呼技能组
        :type CallOutSkillGroupIds: list of int non-negative
        :param _State: 号码状态，1-正常，2-欠费停用，4-管理员停用，5-违规停用
        :type State: int
        """
        self._Number = None
        self._CallOutSkillGroupIds = None
        self._State = None

    @property
    def Number(self):
        """号码
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def CallOutSkillGroupIds(self):
        """绑定的外呼技能组
        :rtype: list of int non-negative
        """
        return self._CallOutSkillGroupIds

    @CallOutSkillGroupIds.setter
    def CallOutSkillGroupIds(self, CallOutSkillGroupIds):
        self._CallOutSkillGroupIds = CallOutSkillGroupIds

    @property
    def State(self):
        """号码状态，1-正常，2-欠费停用，4-管理员停用，5-违规停用
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._Number = params.get("Number")
        self._CallOutSkillGroupIds = params.get("CallOutSkillGroupIds")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OwnNumberApplyDetailItem(AbstractModel):
    """用户自带号码审批明细数据类型

    """

    def __init__(self):
        r"""
        :param _CallType: 号码类型：0-呼入|1-呼出|2-呼入呼出
        :type CallType: int
        :param _PhoneNumber: 线路号码
        :type PhoneNumber: str
        :param _MaxCallCount: 最大并发呼叫数
        :type MaxCallCount: int
        :param _MaxCallPSec: 每秒最大并发数
        :type MaxCallPSec: int
        :param _OutboundCalleeFormat: 呼出被叫格式，使用 {+E.164} 或 {E.164}, 
        :type OutboundCalleeFormat: str
        """
        self._CallType = None
        self._PhoneNumber = None
        self._MaxCallCount = None
        self._MaxCallPSec = None
        self._OutboundCalleeFormat = None

    @property
    def CallType(self):
        """号码类型：0-呼入|1-呼出|2-呼入呼出
        :rtype: int
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def PhoneNumber(self):
        """线路号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def MaxCallCount(self):
        """最大并发呼叫数
        :rtype: int
        """
        return self._MaxCallCount

    @MaxCallCount.setter
    def MaxCallCount(self, MaxCallCount):
        self._MaxCallCount = MaxCallCount

    @property
    def MaxCallPSec(self):
        """每秒最大并发数
        :rtype: int
        """
        return self._MaxCallPSec

    @MaxCallPSec.setter
    def MaxCallPSec(self, MaxCallPSec):
        self._MaxCallPSec = MaxCallPSec

    @property
    def OutboundCalleeFormat(self):
        """呼出被叫格式，使用 {+E.164} 或 {E.164}, 
        :rtype: str
        """
        return self._OutboundCalleeFormat

    @OutboundCalleeFormat.setter
    def OutboundCalleeFormat(self, OutboundCalleeFormat):
        self._OutboundCalleeFormat = OutboundCalleeFormat


    def _deserialize(self, params):
        self._CallType = params.get("CallType")
        self._PhoneNumber = params.get("PhoneNumber")
        self._MaxCallCount = params.get("MaxCallCount")
        self._MaxCallPSec = params.get("MaxCallPSec")
        self._OutboundCalleeFormat = params.get("OutboundCalleeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PSTNSession(AbstractModel):
    """PSTN 会话类型。

    """

    def __init__(self):
        r"""
        :param _SessionID: 会话 ID
        :type SessionID: str
        :param _RoomID: 会话临时房间 ID
        :type RoomID: str
        :param _Caller: 主叫
        :type Caller: str
        :param _Callee: 被叫
        :type Callee: str
        :param _StartTimestamp: 开始时间，Unix 时间戳
        :type StartTimestamp: int
        :param _RingTimestamp: 振铃时间，Unix 时间戳
        :type RingTimestamp: int
        :param _AcceptTimestamp: 接听时间，Unix 时间戳
        :type AcceptTimestamp: int
        :param _StaffEmail: 座席邮箱
        :type StaffEmail: str
        :param _StaffNumber: 座席工号
        :type StaffNumber: str
        :param _SessionStatus: 会话状态
ringing 振铃中
seatJoining  等待座席接听
inProgress 进行中
finished 已完成
        :type SessionStatus: str
        :param _Direction: 会话呼叫方向， 0 呼入 | 1 - 呼出
        :type Direction: int
        :param _OutBoundCaller: 转外线使用的号码（转外线主叫）
        :type OutBoundCaller: str
        :param _OutBoundCallee: 转外线被叫
        :type OutBoundCallee: str
        :param _ProtectedCaller: 主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
        :type ProtectedCaller: str
        :param _ProtectedCallee: 被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
        :type ProtectedCallee: str
        """
        self._SessionID = None
        self._RoomID = None
        self._Caller = None
        self._Callee = None
        self._StartTimestamp = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._StaffEmail = None
        self._StaffNumber = None
        self._SessionStatus = None
        self._Direction = None
        self._OutBoundCaller = None
        self._OutBoundCallee = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None

    @property
    def SessionID(self):
        """会话 ID
        :rtype: str
        """
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID

    @property
    def RoomID(self):
        """会话临时房间 ID
        :rtype: str
        """
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID

    @property
    def Caller(self):
        """主叫
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        """被叫
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def StartTimestamp(self):
        """开始时间，Unix 时间戳
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def RingTimestamp(self):
        """振铃时间，Unix 时间戳
        :rtype: int
        """
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        """接听时间，Unix 时间戳
        :rtype: int
        """
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def StaffEmail(self):
        """座席邮箱
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def StaffNumber(self):
        """座席工号
        :rtype: str
        """
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def SessionStatus(self):
        """会话状态
ringing 振铃中
seatJoining  等待座席接听
inProgress 进行中
finished 已完成
        :rtype: str
        """
        return self._SessionStatus

    @SessionStatus.setter
    def SessionStatus(self, SessionStatus):
        self._SessionStatus = SessionStatus

    @property
    def Direction(self):
        """会话呼叫方向， 0 呼入 | 1 - 呼出
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def OutBoundCaller(self):
        """转外线使用的号码（转外线主叫）
        :rtype: str
        """
        return self._OutBoundCaller

    @OutBoundCaller.setter
    def OutBoundCaller(self, OutBoundCaller):
        self._OutBoundCaller = OutBoundCaller

    @property
    def OutBoundCallee(self):
        """转外线被叫
        :rtype: str
        """
        return self._OutBoundCallee

    @OutBoundCallee.setter
    def OutBoundCallee(self, OutBoundCallee):
        self._OutBoundCallee = OutBoundCallee

    @property
    def ProtectedCaller(self):
        """主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
        :rtype: str
        """
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        """被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
        :rtype: str
        """
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee


    def _deserialize(self, params):
        self._SessionID = params.get("SessionID")
        self._RoomID = params.get("RoomID")
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._StartTimestamp = params.get("StartTimestamp")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._StaffEmail = params.get("StaffEmail")
        self._StaffNumber = params.get("StaffNumber")
        self._SessionStatus = params.get("SessionStatus")
        self._Direction = params.get("Direction")
        self._OutBoundCaller = params.get("OutBoundCaller")
        self._OutBoundCallee = params.get("OutBoundCallee")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PSTNSessionInfo(AbstractModel):
    """PSTN 会话信息

    """

    def __init__(self):
        r"""
        :param _SessionID: 会话 ID
        :type SessionID: str
        :param _RoomID: 会话临时房间 ID
        :type RoomID: str
        :param _Caller: 主叫
        :type Caller: str
        :param _Callee: 被叫
        :type Callee: str
        :param _StartTimestamp: 开始时间，Unix 时间戳
        :type StartTimestamp: str
        :param _AcceptTimestamp: 接听时间，Unix 时间戳
        :type AcceptTimestamp: str
        :param _StaffEmail: 座席邮箱
        :type StaffEmail: str
        :param _StaffNumber: 座席工号
        :type StaffNumber: str
        :param _SessionStatus: 座席状态 inProgress 进行中
        :type SessionStatus: str
        :param _Direction: 会话呼叫方向， 0 呼入 | 1 - 呼出
        :type Direction: int
        :param _RingTimestamp: 振铃时间，Unix 时间戳
        :type RingTimestamp: int
        :param _ProtectedCaller: 主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
        :type ProtectedCaller: str
        :param _ProtectedCallee: 被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
        :type ProtectedCallee: str
        """
        self._SessionID = None
        self._RoomID = None
        self._Caller = None
        self._Callee = None
        self._StartTimestamp = None
        self._AcceptTimestamp = None
        self._StaffEmail = None
        self._StaffNumber = None
        self._SessionStatus = None
        self._Direction = None
        self._RingTimestamp = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None

    @property
    def SessionID(self):
        """会话 ID
        :rtype: str
        """
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID

    @property
    def RoomID(self):
        """会话临时房间 ID
        :rtype: str
        """
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID

    @property
    def Caller(self):
        """主叫
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        """被叫
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def StartTimestamp(self):
        """开始时间，Unix 时间戳
        :rtype: str
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def AcceptTimestamp(self):
        """接听时间，Unix 时间戳
        :rtype: str
        """
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def StaffEmail(self):
        """座席邮箱
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def StaffNumber(self):
        """座席工号
        :rtype: str
        """
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def SessionStatus(self):
        """座席状态 inProgress 进行中
        :rtype: str
        """
        return self._SessionStatus

    @SessionStatus.setter
    def SessionStatus(self, SessionStatus):
        self._SessionStatus = SessionStatus

    @property
    def Direction(self):
        """会话呼叫方向， 0 呼入 | 1 - 呼出
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RingTimestamp(self):
        """振铃时间，Unix 时间戳
        :rtype: int
        """
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def ProtectedCaller(self):
        """主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
        :rtype: str
        """
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        """被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
        :rtype: str
        """
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee


    def _deserialize(self, params):
        self._SessionID = params.get("SessionID")
        self._RoomID = params.get("RoomID")
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._StartTimestamp = params.get("StartTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._StaffEmail = params.get("StaffEmail")
        self._StaffNumber = params.get("StaffNumber")
        self._SessionStatus = params.get("SessionStatus")
        self._Direction = params.get("Direction")
        self._RingTimestamp = params.get("RingTimestamp")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageBuyInfo(AbstractModel):
    """套餐包购买信息

    """

    def __init__(self):
        r"""
        :param _PackageId: 套餐包Id
        :type PackageId: str
        :param _Type: 套餐包类型，0-外呼套餐包|1-400呼入套餐包
        :type Type: int
        :param _CapacitySize: 套餐包总量
        :type CapacitySize: int
        :param _CapacityRemain: 套餐包剩余量
        :type CapacityRemain: int
        :param _BuyTime: 购买时间戳
        :type BuyTime: int
        :param _EndTime: 截止时间戳
        :type EndTime: int
        """
        self._PackageId = None
        self._Type = None
        self._CapacitySize = None
        self._CapacityRemain = None
        self._BuyTime = None
        self._EndTime = None

    @property
    def PackageId(self):
        """套餐包Id
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Type(self):
        """套餐包类型，0-外呼套餐包|1-400呼入套餐包
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CapacitySize(self):
        """套餐包总量
        :rtype: int
        """
        return self._CapacitySize

    @CapacitySize.setter
    def CapacitySize(self, CapacitySize):
        self._CapacitySize = CapacitySize

    @property
    def CapacityRemain(self):
        """套餐包剩余量
        :rtype: int
        """
        return self._CapacityRemain

    @CapacityRemain.setter
    def CapacityRemain(self, CapacityRemain):
        self._CapacityRemain = CapacityRemain

    @property
    def BuyTime(self):
        """购买时间戳
        :rtype: int
        """
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def EndTime(self):
        """截止时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._Type = params.get("Type")
        self._CapacitySize = params.get("CapacitySize")
        self._CapacityRemain = params.get("CapacityRemain")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PausePredictiveDialingCampaignRequest(AbstractModel):
    """PausePredictiveDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PausePredictiveDialingCampaignResponse(AbstractModel):
    """PausePredictiveDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PhoneNumBuyInfo(AbstractModel):
    """号码购买信息

    """

    def __init__(self):
        r"""
        :param _PhoneNum: 电话号码
        :type PhoneNum: str
        :param _Type: 号码类型，0-固话|1-虚商号码|2-运营商号码|3-400号码
        :type Type: int
        :param _CallType: 号码呼叫类型，1-呼入|2-呼出|3-呼入呼出
        :type CallType: int
        :param _BuyTime: 购买时间戳
        :type BuyTime: int
        :param _EndTime: 截止时间戳
        :type EndTime: int
        :param _State: 号码状态，1正常|2欠费停用|4管理员停用|5违规停用
        :type State: int
        """
        self._PhoneNum = None
        self._Type = None
        self._CallType = None
        self._BuyTime = None
        self._EndTime = None
        self._State = None

    @property
    def PhoneNum(self):
        """电话号码
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def Type(self):
        """号码类型，0-固话|1-虚商号码|2-运营商号码|3-400号码
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CallType(self):
        """号码呼叫类型，1-呼入|2-呼出|3-呼入呼出
        :rtype: int
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def BuyTime(self):
        """购买时间戳
        :rtype: int
        """
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def EndTime(self):
        """截止时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def State(self):
        """号码状态，1正常|2欠费停用|4管理员停用|5违规停用
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._PhoneNum = params.get("PhoneNum")
        self._Type = params.get("Type")
        self._CallType = params.get("CallType")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetExtensionPasswordRequest(AbstractModel):
    """ResetExtensionPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """分机号
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetExtensionPasswordResponse(AbstractModel):
    """ResetExtensionPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Password: 重置后密码
        :type Password: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Password = None
        self._RequestId = None

    @property
    def Password(self):
        """重置后密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._RequestId = params.get("RequestId")


class RestoreMemberOnlineRequest(AbstractModel):
    """RestoreMemberOnline请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _UserId: 客服ID
        :type UserId: str
        """
        self._SdkAppId = None
        self._UserId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        """客服ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreMemberOnlineResponse(AbstractModel):
    """RestoreMemberOnline返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResumePredictiveDialingCampaignRequest(AbstractModel):
    """ResumePredictiveDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 任务 ID
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumePredictiveDialingCampaignResponse(AbstractModel):
    """ResumePredictiveDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SdkAppIdBuyInfo(AbstractModel):
    """应用购买信息

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID
        :type SdkAppId: int
        :param _Name: 应用名称
        :type Name: str
        :param _StaffBuyNum: 座席购买数（还在有效期内）
        :type StaffBuyNum: int
        :param _StaffBuyList: 座席购买列表 （还在有效期内）
        :type StaffBuyList: list of StaffBuyInfo
        :param _PhoneNumBuyList: 号码购买列表
        :type PhoneNumBuyList: list of PhoneNumBuyInfo
        :param _SipBuyNum: 办公电话购买数（还在有效期内）
        :type SipBuyNum: int
        """
        self._SdkAppId = None
        self._Name = None
        self._StaffBuyNum = None
        self._StaffBuyList = None
        self._PhoneNumBuyList = None
        self._SipBuyNum = None

    @property
    def SdkAppId(self):
        """应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        """应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StaffBuyNum(self):
        """座席购买数（还在有效期内）
        :rtype: int
        """
        return self._StaffBuyNum

    @StaffBuyNum.setter
    def StaffBuyNum(self, StaffBuyNum):
        self._StaffBuyNum = StaffBuyNum

    @property
    def StaffBuyList(self):
        """座席购买列表 （还在有效期内）
        :rtype: list of StaffBuyInfo
        """
        return self._StaffBuyList

    @StaffBuyList.setter
    def StaffBuyList(self, StaffBuyList):
        self._StaffBuyList = StaffBuyList

    @property
    def PhoneNumBuyList(self):
        """号码购买列表
        :rtype: list of PhoneNumBuyInfo
        """
        return self._PhoneNumBuyList

    @PhoneNumBuyList.setter
    def PhoneNumBuyList(self, PhoneNumBuyList):
        self._PhoneNumBuyList = PhoneNumBuyList

    @property
    def SipBuyNum(self):
        """办公电话购买数（还在有效期内）
        :rtype: int
        """
        return self._SipBuyNum

    @SipBuyNum.setter
    def SipBuyNum(self, SipBuyNum):
        self._SipBuyNum = SipBuyNum


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._StaffBuyNum = params.get("StaffBuyNum")
        if params.get("StaffBuyList") is not None:
            self._StaffBuyList = []
            for item in params.get("StaffBuyList"):
                obj = StaffBuyInfo()
                obj._deserialize(item)
                self._StaffBuyList.append(obj)
        if params.get("PhoneNumBuyList") is not None:
            self._PhoneNumBuyList = []
            for item in params.get("PhoneNumBuyList"):
                obj = PhoneNumBuyInfo()
                obj._deserialize(item)
                self._PhoneNumBuyList.append(obj)
        self._SipBuyNum = params.get("SipBuyNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeatUserInfo(AbstractModel):
    """座席用户信息

    """

    def __init__(self):
        r"""
        :param _Name: 座席名称
        :type Name: str
        :param _Mail: 座席邮箱
        :type Mail: str
        :param _StaffNumber: 工号
        :type StaffNumber: str
        :param _Phone: 座席电话号码（带0086前缀）
        :type Phone: str
        :param _Nick: 座席昵称
        :type Nick: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _SkillGroupNameList: 座席关联的技能组列表
        :type SkillGroupNameList: list of str
        :param _Role: 1:管理员
2:质检员
3:普通座席
else:自定义角色ID
        :type Role: int
        :param _ExtensionNumber: 座席分机号（1 到 8 打头，4 - 6 位）
        :type ExtensionNumber: str
        """
        self._Name = None
        self._Mail = None
        self._StaffNumber = None
        self._Phone = None
        self._Nick = None
        self._UserId = None
        self._SkillGroupNameList = None
        self._Role = None
        self._ExtensionNumber = None

    @property
    def Name(self):
        """座席名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        """座席邮箱
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def StaffNumber(self):
        """工号
        :rtype: str
        """
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def Phone(self):
        """座席电话号码（带0086前缀）
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        """座席昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def UserId(self):
        """用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SkillGroupNameList(self):
        """座席关联的技能组列表
        :rtype: list of str
        """
        return self._SkillGroupNameList

    @SkillGroupNameList.setter
    def SkillGroupNameList(self, SkillGroupNameList):
        self._SkillGroupNameList = SkillGroupNameList

    @property
    def Role(self):
        """1:管理员
2:质检员
3:普通座席
else:自定义角色ID
        :rtype: int
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def ExtensionNumber(self):
        """座席分机号（1 到 8 打头，4 - 6 位）
        :rtype: str
        """
        return self._ExtensionNumber

    @ExtensionNumber.setter
    def ExtensionNumber(self, ExtensionNumber):
        self._ExtensionNumber = ExtensionNumber


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        self._StaffNumber = params.get("StaffNumber")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._UserId = params.get("UserId")
        self._SkillGroupNameList = params.get("SkillGroupNameList")
        self._Role = params.get("Role")
        self._ExtensionNumber = params.get("ExtensionNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServeParticipant(AbstractModel):
    """参与者信息

    """

    def __init__(self):
        r"""
        :param _Mail: 座席邮箱
        :type Mail: str
        :param _Phone: 座席电话
        :type Phone: str
        :param _RingTimestamp: 振铃时间戳，Unix 秒级时间戳
        :type RingTimestamp: int
        :param _AcceptTimestamp: 接听时间戳，Unix 秒级时间戳
        :type AcceptTimestamp: int
        :param _EndedTimestamp: 结束时间戳，Unix 秒级时间戳
        :type EndedTimestamp: int
        :param _RecordId: 录音 ID，能够索引到座席侧的录音
        :type RecordId: str
        :param _Type: 参与者类型，"staffSeat", "outboundSeat", "staffPhoneSeat"
        :type Type: str
        :param _TransferFrom: 转接来源座席信息
        :type TransferFrom: str
        :param _TransferFromType: 转接来源参与者类型，取值与 Type 一致
        :type TransferFromType: str
        :param _TransferTo: 转接去向座席信息
        :type TransferTo: str
        :param _TransferToType: 转接去向参与者类型，取值与 Type 一致
        :type TransferToType: str
        :param _SkillGroupId: 技能组 ID
        :type SkillGroupId: int
        :param _EndStatusString: 结束状态
        :type EndStatusString: str
        :param _RecordURL: 录音 URL
        :type RecordURL: str
        :param _Sequence: 参与者序号，从 0 开始
        :type Sequence: int
        :param _StartTimestamp: 开始时间戳，Unix 秒级时间戳
        :type StartTimestamp: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param _CustomRecordURL: 录音转存第三方COS地址
        :type CustomRecordURL: str
        """
        self._Mail = None
        self._Phone = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._EndedTimestamp = None
        self._RecordId = None
        self._Type = None
        self._TransferFrom = None
        self._TransferFromType = None
        self._TransferTo = None
        self._TransferToType = None
        self._SkillGroupId = None
        self._EndStatusString = None
        self._RecordURL = None
        self._Sequence = None
        self._StartTimestamp = None
        self._SkillGroupName = None
        self._CustomRecordURL = None

    @property
    def Mail(self):
        """座席邮箱
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Phone(self):
        """座席电话
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def RingTimestamp(self):
        """振铃时间戳，Unix 秒级时间戳
        :rtype: int
        """
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        """接听时间戳，Unix 秒级时间戳
        :rtype: int
        """
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def EndedTimestamp(self):
        """结束时间戳，Unix 秒级时间戳
        :rtype: int
        """
        return self._EndedTimestamp

    @EndedTimestamp.setter
    def EndedTimestamp(self, EndedTimestamp):
        self._EndedTimestamp = EndedTimestamp

    @property
    def RecordId(self):
        """录音 ID，能够索引到座席侧的录音
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Type(self):
        """参与者类型，"staffSeat", "outboundSeat", "staffPhoneSeat"
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TransferFrom(self):
        """转接来源座席信息
        :rtype: str
        """
        return self._TransferFrom

    @TransferFrom.setter
    def TransferFrom(self, TransferFrom):
        self._TransferFrom = TransferFrom

    @property
    def TransferFromType(self):
        """转接来源参与者类型，取值与 Type 一致
        :rtype: str
        """
        return self._TransferFromType

    @TransferFromType.setter
    def TransferFromType(self, TransferFromType):
        self._TransferFromType = TransferFromType

    @property
    def TransferTo(self):
        """转接去向座席信息
        :rtype: str
        """
        return self._TransferTo

    @TransferTo.setter
    def TransferTo(self, TransferTo):
        self._TransferTo = TransferTo

    @property
    def TransferToType(self):
        """转接去向参与者类型，取值与 Type 一致
        :rtype: str
        """
        return self._TransferToType

    @TransferToType.setter
    def TransferToType(self, TransferToType):
        self._TransferToType = TransferToType

    @property
    def SkillGroupId(self):
        """技能组 ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def EndStatusString(self):
        """结束状态
        :rtype: str
        """
        return self._EndStatusString

    @EndStatusString.setter
    def EndStatusString(self, EndStatusString):
        self._EndStatusString = EndStatusString

    @property
    def RecordURL(self):
        """录音 URL
        :rtype: str
        """
        return self._RecordURL

    @RecordURL.setter
    def RecordURL(self, RecordURL):
        self._RecordURL = RecordURL

    @property
    def Sequence(self):
        """参与者序号，从 0 开始
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def StartTimestamp(self):
        """开始时间戳，Unix 秒级时间戳
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def SkillGroupName(self):
        """技能组名称
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def CustomRecordURL(self):
        """录音转存第三方COS地址
        :rtype: str
        """
        return self._CustomRecordURL

    @CustomRecordURL.setter
    def CustomRecordURL(self, CustomRecordURL):
        self._CustomRecordURL = CustomRecordURL


    def _deserialize(self, params):
        self._Mail = params.get("Mail")
        self._Phone = params.get("Phone")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._EndedTimestamp = params.get("EndedTimestamp")
        self._RecordId = params.get("RecordId")
        self._Type = params.get("Type")
        self._TransferFrom = params.get("TransferFrom")
        self._TransferFromType = params.get("TransferFromType")
        self._TransferTo = params.get("TransferTo")
        self._TransferToType = params.get("TransferToType")
        self._SkillGroupId = params.get("SkillGroupId")
        self._EndStatusString = params.get("EndStatusString")
        self._RecordURL = params.get("RecordURL")
        self._Sequence = params.get("Sequence")
        self._StartTimestamp = params.get("StartTimestamp")
        self._SkillGroupName = params.get("SkillGroupName")
        self._CustomRecordURL = params.get("CustomRecordURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillGroupInfoItem(AbstractModel):
    """技能组信息

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param _Type: （废弃）类型：IM、TEL、ALL（全媒体）
        :type Type: str
        :param _RoutePolicy: 会话分配策略
        :type RoutePolicy: str
        :param _UsingLastSeat: 会话分配是否优先上次服务座席
        :type UsingLastSeat: int
        :param _MaxConcurrency: 单客服最大并发数（电话类型默认1）
        :type MaxConcurrency: int
        :param _LastModifyTimestamp: 最后修改时间
        :type LastModifyTimestamp: int
        :param _SkillGroupType: 技能组类型0-电话，1-在线，3-音频，4-视频	
        :type SkillGroupType: int
        :param _Alias: 技能组内线号码
        :type Alias: str
        """
        self._SkillGroupId = None
        self._SkillGroupName = None
        self._Type = None
        self._RoutePolicy = None
        self._UsingLastSeat = None
        self._MaxConcurrency = None
        self._LastModifyTimestamp = None
        self._SkillGroupType = None
        self._Alias = None

    @property
    def SkillGroupId(self):
        """技能组ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def SkillGroupName(self):
        """技能组名称
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def Type(self):
        """（废弃）类型：IM、TEL、ALL（全媒体）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RoutePolicy(self):
        """会话分配策略
        :rtype: str
        """
        return self._RoutePolicy

    @RoutePolicy.setter
    def RoutePolicy(self, RoutePolicy):
        self._RoutePolicy = RoutePolicy

    @property
    def UsingLastSeat(self):
        """会话分配是否优先上次服务座席
        :rtype: int
        """
        return self._UsingLastSeat

    @UsingLastSeat.setter
    def UsingLastSeat(self, UsingLastSeat):
        self._UsingLastSeat = UsingLastSeat

    @property
    def MaxConcurrency(self):
        """单客服最大并发数（电话类型默认1）
        :rtype: int
        """
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def LastModifyTimestamp(self):
        """最后修改时间
        :rtype: int
        """
        return self._LastModifyTimestamp

    @LastModifyTimestamp.setter
    def LastModifyTimestamp(self, LastModifyTimestamp):
        self._LastModifyTimestamp = LastModifyTimestamp

    @property
    def SkillGroupType(self):
        """技能组类型0-电话，1-在线，3-音频，4-视频	
        :rtype: int
        """
        return self._SkillGroupType

    @SkillGroupType.setter
    def SkillGroupType(self, SkillGroupType):
        self._SkillGroupType = SkillGroupType

    @property
    def Alias(self):
        """技能组内线号码
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._Type = params.get("Type")
        self._RoutePolicy = params.get("RoutePolicy")
        self._UsingLastSeat = params.get("UsingLastSeat")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._LastModifyTimestamp = params.get("LastModifyTimestamp")
        self._SkillGroupType = params.get("SkillGroupType")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillGroupItem(AbstractModel):
    """技能组信息

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param _Priority: 优先级
        :type Priority: int
        :param _Type: 类型：IM、TEL、ALL（全媒体）
        :type Type: str
        """
        self._SkillGroupId = None
        self._SkillGroupName = None
        self._Priority = None
        self._Type = None

    @property
    def SkillGroupId(self):
        """技能组ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def SkillGroupName(self):
        """技能组名称
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def Priority(self):
        """优先级
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Type(self):
        """类型：IM、TEL、ALL（全媒体）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._Priority = params.get("Priority")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffBuyInfo(AbstractModel):
    """座席购买信息

    """

    def __init__(self):
        r"""
        :param _Num: 购买座席数量
        :type Num: int
        :param _BuyTime: 购买时间戳
        :type BuyTime: int
        :param _EndTime: 截止时间戳
        :type EndTime: int
        :param _SipNum: 购买办公电话数量
        :type SipNum: int
        """
        self._Num = None
        self._BuyTime = None
        self._EndTime = None
        self._SipNum = None

    @property
    def Num(self):
        """购买座席数量
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def BuyTime(self):
        """购买时间戳
        :rtype: int
        """
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def EndTime(self):
        """截止时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SipNum(self):
        """购买办公电话数量
        :rtype: int
        """
        return self._SipNum

    @SipNum.setter
    def SipNum(self, SipNum):
        self._SipNum = SipNum


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        self._SipNum = params.get("SipNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffInfo(AbstractModel):
    """带有技能组优先级的座席信息

    """

    def __init__(self):
        r"""
        :param _Name: 座席名称
        :type Name: str
        :param _Mail: 座席邮箱
        :type Mail: str
        :param _Phone: 座席电话号码
        :type Phone: str
        :param _Nick: 座席昵称
        :type Nick: str
        :param _StaffNumber: 座席工号
        :type StaffNumber: str
        :param _RoleId: 用户角色id
一个用户绑定了多个角色时以RoleIdList为准
        :type RoleId: int
        :param _RoleIdList: 用户角色id列表
        :type RoleIdList: int
        :param _SkillGroupList: 所属技能组列表
        :type SkillGroupList: list of SkillGroupItem
        :param _LastModifyTimestamp: 最后修改时间
        :type LastModifyTimestamp: int
        :param _ExtensionNumber: 座席分机号（1 到 8 打头，4 - 6 位）
        :type ExtensionNumber: str
        """
        self._Name = None
        self._Mail = None
        self._Phone = None
        self._Nick = None
        self._StaffNumber = None
        self._RoleId = None
        self._RoleIdList = None
        self._SkillGroupList = None
        self._LastModifyTimestamp = None
        self._ExtensionNumber = None

    @property
    def Name(self):
        """座席名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        """座席邮箱
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Phone(self):
        """座席电话号码
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        """座席昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def StaffNumber(self):
        """座席工号
        :rtype: str
        """
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def RoleId(self):
        warnings.warn("parameter `RoleId` is deprecated", DeprecationWarning) 

        """用户角色id
一个用户绑定了多个角色时以RoleIdList为准
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        warnings.warn("parameter `RoleId` is deprecated", DeprecationWarning) 

        self._RoleId = RoleId

    @property
    def RoleIdList(self):
        """用户角色id列表
        :rtype: int
        """
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def SkillGroupList(self):
        """所属技能组列表
        :rtype: list of SkillGroupItem
        """
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList

    @property
    def LastModifyTimestamp(self):
        """最后修改时间
        :rtype: int
        """
        return self._LastModifyTimestamp

    @LastModifyTimestamp.setter
    def LastModifyTimestamp(self, LastModifyTimestamp):
        self._LastModifyTimestamp = LastModifyTimestamp

    @property
    def ExtensionNumber(self):
        """座席分机号（1 到 8 打头，4 - 6 位）
        :rtype: str
        """
        return self._ExtensionNumber

    @ExtensionNumber.setter
    def ExtensionNumber(self, ExtensionNumber):
        self._ExtensionNumber = ExtensionNumber


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._StaffNumber = params.get("StaffNumber")
        self._RoleId = params.get("RoleId")
        self._RoleIdList = params.get("RoleIdList")
        if params.get("SkillGroupList") is not None:
            self._SkillGroupList = []
            for item in params.get("SkillGroupList"):
                obj = SkillGroupItem()
                obj._deserialize(item)
                self._SkillGroupList.append(obj)
        self._LastModifyTimestamp = params.get("LastModifyTimestamp")
        self._ExtensionNumber = params.get("ExtensionNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffSkillGroupList(AbstractModel):
    """座席绑定技能组列表

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _Priority: 座席在技能组中的优先级（1为最高，5最低，默认3）
        :type Priority: int
        """
        self._SkillGroupId = None
        self._Priority = None

    @property
    def SkillGroupId(self):
        """技能组ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Priority(self):
        """座席在技能组中的优先级（1为最高，5最低，默认3）
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffStatusExtra(AbstractModel):
    """座席状态补充信息

    """

    def __init__(self):
        r"""
        :param _Type: im - 文本 | tel - 电话 | all - 全媒体
        :type Type: str
        :param _Direct: in - 呼入 | out - 呼出
        :type Direct: str
        """
        self._Type = None
        self._Direct = None

    @property
    def Type(self):
        """im - 文本 | tel - 电话 | all - 全媒体
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Direct(self):
        """in - 呼入 | out - 呼出
        :rtype: str
        """
        return self._Direct

    @Direct.setter
    def Direct(self, Direct):
        self._Direct = Direct


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Direct = params.get("Direct")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffStatusMetrics(AbstractModel):
    """座席状态相关信息

    """

    def __init__(self):
        r"""
        :param _Email: 座席邮箱
        :type Email: str
        :param _Status: 座席状态 free 示闲 | busy 忙碌 | rest 小休 | notReady 示忙 | afterCallWork 话后调整 | offline 离线
        :type Status: str
        :param _StatusExtra: 座席状态补充信息
        :type StatusExtra: :class:`tencentcloud.ccc.v20200210.models.StaffStatusExtra`
        :param _OnlineDuration: 当天在线总时长
        :type OnlineDuration: int
        :param _FreeDuration: 当天示闲总时长
        :type FreeDuration: int
        :param _BusyDuration: 当天忙碌总时长
        :type BusyDuration: int
        :param _NotReadyDuration: 当天示忙总时长
        :type NotReadyDuration: int
        :param _RestDuration: 当天小休总时长
        :type RestDuration: int
        :param _AfterCallWorkDuration: 当天话后调整总时长
        :type AfterCallWorkDuration: int
        :param _Reason: 小休原因
        :type Reason: str
        :param _ReserveRest: 是否预约小休
        :type ReserveRest: bool
        :param _ReserveNotReady: 是否预约示忙
        :type ReserveNotReady: bool
        :param _UseMobileAccept: 手机接听模式： 0 - 关闭 | 1 - 仅离线 | 2- 始终
        :type UseMobileAccept: int
        :param _UseMobileCallOut: 手机外呼开关
        :type UseMobileCallOut: bool
        :param _LastOnlineTimestamp: 最近一次上线时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOnlineTimestamp: int
        :param _LastStatusTimestamp: 最近一次状态时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type LastStatusTimestamp: int
        """
        self._Email = None
        self._Status = None
        self._StatusExtra = None
        self._OnlineDuration = None
        self._FreeDuration = None
        self._BusyDuration = None
        self._NotReadyDuration = None
        self._RestDuration = None
        self._AfterCallWorkDuration = None
        self._Reason = None
        self._ReserveRest = None
        self._ReserveNotReady = None
        self._UseMobileAccept = None
        self._UseMobileCallOut = None
        self._LastOnlineTimestamp = None
        self._LastStatusTimestamp = None

    @property
    def Email(self):
        """座席邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        """座席状态 free 示闲 | busy 忙碌 | rest 小休 | notReady 示忙 | afterCallWork 话后调整 | offline 离线
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusExtra(self):
        """座席状态补充信息
        :rtype: :class:`tencentcloud.ccc.v20200210.models.StaffStatusExtra`
        """
        return self._StatusExtra

    @StatusExtra.setter
    def StatusExtra(self, StatusExtra):
        self._StatusExtra = StatusExtra

    @property
    def OnlineDuration(self):
        """当天在线总时长
        :rtype: int
        """
        return self._OnlineDuration

    @OnlineDuration.setter
    def OnlineDuration(self, OnlineDuration):
        self._OnlineDuration = OnlineDuration

    @property
    def FreeDuration(self):
        """当天示闲总时长
        :rtype: int
        """
        return self._FreeDuration

    @FreeDuration.setter
    def FreeDuration(self, FreeDuration):
        self._FreeDuration = FreeDuration

    @property
    def BusyDuration(self):
        """当天忙碌总时长
        :rtype: int
        """
        return self._BusyDuration

    @BusyDuration.setter
    def BusyDuration(self, BusyDuration):
        self._BusyDuration = BusyDuration

    @property
    def NotReadyDuration(self):
        """当天示忙总时长
        :rtype: int
        """
        return self._NotReadyDuration

    @NotReadyDuration.setter
    def NotReadyDuration(self, NotReadyDuration):
        self._NotReadyDuration = NotReadyDuration

    @property
    def RestDuration(self):
        """当天小休总时长
        :rtype: int
        """
        return self._RestDuration

    @RestDuration.setter
    def RestDuration(self, RestDuration):
        self._RestDuration = RestDuration

    @property
    def AfterCallWorkDuration(self):
        """当天话后调整总时长
        :rtype: int
        """
        return self._AfterCallWorkDuration

    @AfterCallWorkDuration.setter
    def AfterCallWorkDuration(self, AfterCallWorkDuration):
        self._AfterCallWorkDuration = AfterCallWorkDuration

    @property
    def Reason(self):
        """小休原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ReserveRest(self):
        """是否预约小休
        :rtype: bool
        """
        return self._ReserveRest

    @ReserveRest.setter
    def ReserveRest(self, ReserveRest):
        self._ReserveRest = ReserveRest

    @property
    def ReserveNotReady(self):
        """是否预约示忙
        :rtype: bool
        """
        return self._ReserveNotReady

    @ReserveNotReady.setter
    def ReserveNotReady(self, ReserveNotReady):
        self._ReserveNotReady = ReserveNotReady

    @property
    def UseMobileAccept(self):
        """手机接听模式： 0 - 关闭 | 1 - 仅离线 | 2- 始终
        :rtype: int
        """
        return self._UseMobileAccept

    @UseMobileAccept.setter
    def UseMobileAccept(self, UseMobileAccept):
        self._UseMobileAccept = UseMobileAccept

    @property
    def UseMobileCallOut(self):
        """手机外呼开关
        :rtype: bool
        """
        return self._UseMobileCallOut

    @UseMobileCallOut.setter
    def UseMobileCallOut(self, UseMobileCallOut):
        self._UseMobileCallOut = UseMobileCallOut

    @property
    def LastOnlineTimestamp(self):
        """最近一次上线时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastOnlineTimestamp

    @LastOnlineTimestamp.setter
    def LastOnlineTimestamp(self, LastOnlineTimestamp):
        self._LastOnlineTimestamp = LastOnlineTimestamp

    @property
    def LastStatusTimestamp(self):
        """最近一次状态时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastStatusTimestamp

    @LastStatusTimestamp.setter
    def LastStatusTimestamp(self, LastStatusTimestamp):
        self._LastStatusTimestamp = LastStatusTimestamp


    def _deserialize(self, params):
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        if params.get("StatusExtra") is not None:
            self._StatusExtra = StaffStatusExtra()
            self._StatusExtra._deserialize(params.get("StatusExtra"))
        self._OnlineDuration = params.get("OnlineDuration")
        self._FreeDuration = params.get("FreeDuration")
        self._BusyDuration = params.get("BusyDuration")
        self._NotReadyDuration = params.get("NotReadyDuration")
        self._RestDuration = params.get("RestDuration")
        self._AfterCallWorkDuration = params.get("AfterCallWorkDuration")
        self._Reason = params.get("Reason")
        self._ReserveRest = params.get("ReserveRest")
        self._ReserveNotReady = params.get("ReserveNotReady")
        self._UseMobileAccept = params.get("UseMobileAccept")
        self._UseMobileCallOut = params.get("UseMobileCallOut")
        self._LastOnlineTimestamp = params.get("LastOnlineTimestamp")
        self._LastStatusTimestamp = params.get("LastStatusTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAutoCalloutTaskRequest(AbstractModel):
    """StopAutoCalloutTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _TaskId: 任务Id
        :type TaskId: int
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """任务Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAutoCalloutTaskResponse(AbstractModel):
    """StopAutoCalloutTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TelCdrInfo(AbstractModel):
    """电话话单信息

    """

    def __init__(self):
        r"""
        :param _Caller: 主叫号码
        :type Caller: str
        :param _Callee: 被叫号码
        :type Callee: str
        :param _Time: 呼叫发起时间戳，Unix 时间戳
        :type Time: int
        :param _Direction: 呼入呼出方向 0 呼入 1 呼出
        :type Direction: int
        :param _Duration: 通话时长
        :type Duration: int
        :param _RecordURL: 录音信息
        :type RecordURL: str
        :param _RecordId: 录音 ID
        :type RecordId: str
        :param _SeatUser: 座席信息
        :type SeatUser: :class:`tencentcloud.ccc.v20200210.models.SeatUserInfo`
        :param _EndStatus: EndStatus与EndStatusString一一对应，具体枚举如下：

**场景	         EndStatus	EndStatusString	状态说明**

电话呼入&呼出	1	        ok	                        正常结束

电话呼入&呼出	0	        error	                系统错误

电话呼入	             102	        ivrGiveUp	        IVR 期间用户放弃

电话呼入	             103	        waitingGiveUp	       会话排队期间用户放弃

电话呼入	             104	        ringingGiveUp	       会话振铃期间用户放弃

电话呼入	             105	        noSeatOnline	       无座席在线

电话呼入              106	       notWorkTime	       非工作时间   

电话呼入	            107	       ivrEnd	               IVR 后直接结束

电话呼入	            100	      blackList 呼入黑名单 

电话呼出               2	              unconnected	未接通

电话呼出             108	        restrictedCallee	被叫因高风险受限

电话呼出             109	        tooManyRequest	    超频

电话呼出             110	        restrictedArea	    外呼盲区

电话呼出             111	        restrictedTime	外呼时间限制
                         
电话呼出             201            unknown	未知状态

电话呼出             202            notAnswer	未接听

电话呼出            203	    userReject	拒接挂断

电话呼出	          204	    powerOff	关机

电话呼出           205            numberNotExist	空号

电话呼出	         206	           busy	通话中

电话呼出   	        207	           outOfCredit	欠费

电话呼出	         208	           operatorError	运营商线路异常

电话呼出         	209	           callerCancel	主叫取消

电话呼出	        210	           notInService	不在服务区

电话呼入&呼出	211    clientError    客户端错误
电话呼出        212     carrierBlocked      运营商拦截
        :type EndStatus: int
        :param _SkillGroup: 技能组名称
        :type SkillGroup: str
        :param _CallerLocation: 主叫归属地
        :type CallerLocation: str
        :param _IVRDuration: IVR 阶段耗时
        :type IVRDuration: int
        :param _RingTimestamp: 振铃时间戳，UNIX 秒级时间戳
        :type RingTimestamp: int
        :param _AcceptTimestamp: 接听时间戳，UNIX 秒级时间戳
        :type AcceptTimestamp: int
        :param _EndedTimestamp: 结束时间戳，UNIX 秒级时间戳
        :type EndedTimestamp: int
        :param _IVRKeyPressed: IVR 按键信息 ，e.g. ["1","2","3"]
        :type IVRKeyPressed: list of str
        :param _HungUpSide: 挂机方 seat 座席 user 用户 system 系统
        :type HungUpSide: str
        :param _ServeParticipants: 服务参与者列表
        :type ServeParticipants: list of ServeParticipant
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _EndStatusString: EndStatus与EndStatusString一一对应，具体枚举如下：

**场景	         EndStatus	EndStatusString	状态说明**

电话呼入&呼出	1	        ok	                        正常结束

电话呼入&呼出	0	        error	                系统错误

电话呼入	             102	        ivrGiveUp	        IVR 期间用户放弃

电话呼入	             103	        waitingGiveUp	       会话排队期间用户放弃

电话呼入	             104	        ringingGiveUp	       会话振铃期间用户放弃

电话呼入	             105	        noSeatOnline	       无座席在线

电话呼入              106	       notWorkTime	       非工作时间   

电话呼入	            107	       ivrEnd	               IVR 后直接结束

电话呼入	            100	      blackList 呼入黑名单 

电话呼出               2	              unconnected	未接通

电话呼出             108	        restrictedCallee	被叫因高风险受限

电话呼出             109	        tooManyRequest	    超频

电话呼出             110	        restrictedArea	    外呼盲区

电话呼出             111	        restrictedTime	外呼时间限制
                         
电话呼出             201            unknown	未知状态

电话呼出             202            notAnswer	未接听

电话呼出            203	    userReject	拒接挂断

电话呼出	          204	    powerOff	关机

电话呼出           205            numberNotExist	空号

电话呼出	         206	           busy	通话中

电话呼出   	        207	           outOfCredit	欠费

电话呼出	         208	           operatorError	运营商线路异常

电话呼出         	209	           callerCancel	主叫取消

电话呼出	        210	           notInService	不在服务区

电话呼入&呼出	211    clientError    客户端错误
电话呼出        212     carrierBlocked      运营商拦截
        :type EndStatusString: str
        :param _StartTimestamp: 会话开始时间戳，UNIX 秒级时间戳
        :type StartTimestamp: int
        :param _QueuedTimestamp: 进入排队时间，Unix 秒级时间戳
        :type QueuedTimestamp: int
        :param _PostIVRKeyPressed: 后置IVR按键信息（e.g. [{"Key":"1","Label":"非常满意"}]）
        :type PostIVRKeyPressed: list of IVRKeyPressedElement
        :param _QueuedSkillGroupId: 排队技能组Id
        :type QueuedSkillGroupId: int
        :param _SessionId: 会话 ID
        :type SessionId: str
        :param _ProtectedCaller: 主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
        :type ProtectedCaller: str
        :param _ProtectedCallee: 被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
        :type ProtectedCallee: str
        :param _Uui: 客户自定义数据（User-to-User Interface）
注意：此字段可能返回 null，表示取不到有效值。
        :type Uui: str
        :param _UUI: 客户自定义数据（User-to-User Interface）
        :type UUI: str
        :param _IVRKeyPressedEx: IVR按键信息（e.g. [{"Key":"1","Label":"非常满意"}]）
        :type IVRKeyPressedEx: list of IVRKeyPressedElement
        :param _AsrUrl: 获取录音ASR文本信息地址
        :type AsrUrl: str
        :param _AsrStatus: AsrUrl的状态：Complete
已完成;
Processing
正在生成中;
NotExists
无记录(未开启生成离线asr或者无套餐包)
        :type AsrStatus: str
        :param _CustomRecordURL: 录音转存第三方COS地址
        :type CustomRecordURL: str
        :param _Remark: 备注
        :type Remark: str
        :param _QueuedSkillGroupName: 排队技能组名称
        :type QueuedSkillGroupName: str
        :param _VoicemailRecordURL: 通话中语音留言录音URL
        :type VoicemailRecordURL: list of str
        :param _VoicemailAsrURL: 通话中语音留言ASR文本信息地址
        :type VoicemailAsrURL: list of str
        """
        self._Caller = None
        self._Callee = None
        self._Time = None
        self._Direction = None
        self._Duration = None
        self._RecordURL = None
        self._RecordId = None
        self._SeatUser = None
        self._EndStatus = None
        self._SkillGroup = None
        self._CallerLocation = None
        self._IVRDuration = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._EndedTimestamp = None
        self._IVRKeyPressed = None
        self._HungUpSide = None
        self._ServeParticipants = None
        self._SkillGroupId = None
        self._EndStatusString = None
        self._StartTimestamp = None
        self._QueuedTimestamp = None
        self._PostIVRKeyPressed = None
        self._QueuedSkillGroupId = None
        self._SessionId = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None
        self._Uui = None
        self._UUI = None
        self._IVRKeyPressedEx = None
        self._AsrUrl = None
        self._AsrStatus = None
        self._CustomRecordURL = None
        self._Remark = None
        self._QueuedSkillGroupName = None
        self._VoicemailRecordURL = None
        self._VoicemailAsrURL = None

    @property
    def Caller(self):
        """主叫号码
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        """被叫号码
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def Time(self):
        """呼叫发起时间戳，Unix 时间戳
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Direction(self):
        """呼入呼出方向 0 呼入 1 呼出
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Duration(self):
        """通话时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RecordURL(self):
        """录音信息
        :rtype: str
        """
        return self._RecordURL

    @RecordURL.setter
    def RecordURL(self, RecordURL):
        self._RecordURL = RecordURL

    @property
    def RecordId(self):
        """录音 ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def SeatUser(self):
        """座席信息
        :rtype: :class:`tencentcloud.ccc.v20200210.models.SeatUserInfo`
        """
        return self._SeatUser

    @SeatUser.setter
    def SeatUser(self, SeatUser):
        self._SeatUser = SeatUser

    @property
    def EndStatus(self):
        """EndStatus与EndStatusString一一对应，具体枚举如下：

**场景	         EndStatus	EndStatusString	状态说明**

电话呼入&呼出	1	        ok	                        正常结束

电话呼入&呼出	0	        error	                系统错误

电话呼入	             102	        ivrGiveUp	        IVR 期间用户放弃

电话呼入	             103	        waitingGiveUp	       会话排队期间用户放弃

电话呼入	             104	        ringingGiveUp	       会话振铃期间用户放弃

电话呼入	             105	        noSeatOnline	       无座席在线

电话呼入              106	       notWorkTime	       非工作时间   

电话呼入	            107	       ivrEnd	               IVR 后直接结束

电话呼入	            100	      blackList 呼入黑名单 

电话呼出               2	              unconnected	未接通

电话呼出             108	        restrictedCallee	被叫因高风险受限

电话呼出             109	        tooManyRequest	    超频

电话呼出             110	        restrictedArea	    外呼盲区

电话呼出             111	        restrictedTime	外呼时间限制
                         
电话呼出             201            unknown	未知状态

电话呼出             202            notAnswer	未接听

电话呼出            203	    userReject	拒接挂断

电话呼出	          204	    powerOff	关机

电话呼出           205            numberNotExist	空号

电话呼出	         206	           busy	通话中

电话呼出   	        207	           outOfCredit	欠费

电话呼出	         208	           operatorError	运营商线路异常

电话呼出         	209	           callerCancel	主叫取消

电话呼出	        210	           notInService	不在服务区

电话呼入&呼出	211    clientError    客户端错误
电话呼出        212     carrierBlocked      运营商拦截
        :rtype: int
        """
        return self._EndStatus

    @EndStatus.setter
    def EndStatus(self, EndStatus):
        self._EndStatus = EndStatus

    @property
    def SkillGroup(self):
        """技能组名称
        :rtype: str
        """
        return self._SkillGroup

    @SkillGroup.setter
    def SkillGroup(self, SkillGroup):
        self._SkillGroup = SkillGroup

    @property
    def CallerLocation(self):
        """主叫归属地
        :rtype: str
        """
        return self._CallerLocation

    @CallerLocation.setter
    def CallerLocation(self, CallerLocation):
        self._CallerLocation = CallerLocation

    @property
    def IVRDuration(self):
        """IVR 阶段耗时
        :rtype: int
        """
        return self._IVRDuration

    @IVRDuration.setter
    def IVRDuration(self, IVRDuration):
        self._IVRDuration = IVRDuration

    @property
    def RingTimestamp(self):
        """振铃时间戳，UNIX 秒级时间戳
        :rtype: int
        """
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        """接听时间戳，UNIX 秒级时间戳
        :rtype: int
        """
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def EndedTimestamp(self):
        """结束时间戳，UNIX 秒级时间戳
        :rtype: int
        """
        return self._EndedTimestamp

    @EndedTimestamp.setter
    def EndedTimestamp(self, EndedTimestamp):
        self._EndedTimestamp = EndedTimestamp

    @property
    def IVRKeyPressed(self):
        """IVR 按键信息 ，e.g. ["1","2","3"]
        :rtype: list of str
        """
        return self._IVRKeyPressed

    @IVRKeyPressed.setter
    def IVRKeyPressed(self, IVRKeyPressed):
        self._IVRKeyPressed = IVRKeyPressed

    @property
    def HungUpSide(self):
        """挂机方 seat 座席 user 用户 system 系统
        :rtype: str
        """
        return self._HungUpSide

    @HungUpSide.setter
    def HungUpSide(self, HungUpSide):
        self._HungUpSide = HungUpSide

    @property
    def ServeParticipants(self):
        """服务参与者列表
        :rtype: list of ServeParticipant
        """
        return self._ServeParticipants

    @ServeParticipants.setter
    def ServeParticipants(self, ServeParticipants):
        self._ServeParticipants = ServeParticipants

    @property
    def SkillGroupId(self):
        """技能组ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def EndStatusString(self):
        """EndStatus与EndStatusString一一对应，具体枚举如下：

**场景	         EndStatus	EndStatusString	状态说明**

电话呼入&呼出	1	        ok	                        正常结束

电话呼入&呼出	0	        error	                系统错误

电话呼入	             102	        ivrGiveUp	        IVR 期间用户放弃

电话呼入	             103	        waitingGiveUp	       会话排队期间用户放弃

电话呼入	             104	        ringingGiveUp	       会话振铃期间用户放弃

电话呼入	             105	        noSeatOnline	       无座席在线

电话呼入              106	       notWorkTime	       非工作时间   

电话呼入	            107	       ivrEnd	               IVR 后直接结束

电话呼入	            100	      blackList 呼入黑名单 

电话呼出               2	              unconnected	未接通

电话呼出             108	        restrictedCallee	被叫因高风险受限

电话呼出             109	        tooManyRequest	    超频

电话呼出             110	        restrictedArea	    外呼盲区

电话呼出             111	        restrictedTime	外呼时间限制
                         
电话呼出             201            unknown	未知状态

电话呼出             202            notAnswer	未接听

电话呼出            203	    userReject	拒接挂断

电话呼出	          204	    powerOff	关机

电话呼出           205            numberNotExist	空号

电话呼出	         206	           busy	通话中

电话呼出   	        207	           outOfCredit	欠费

电话呼出	         208	           operatorError	运营商线路异常

电话呼出         	209	           callerCancel	主叫取消

电话呼出	        210	           notInService	不在服务区

电话呼入&呼出	211    clientError    客户端错误
电话呼出        212     carrierBlocked      运营商拦截
        :rtype: str
        """
        return self._EndStatusString

    @EndStatusString.setter
    def EndStatusString(self, EndStatusString):
        self._EndStatusString = EndStatusString

    @property
    def StartTimestamp(self):
        """会话开始时间戳，UNIX 秒级时间戳
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def QueuedTimestamp(self):
        """进入排队时间，Unix 秒级时间戳
        :rtype: int
        """
        return self._QueuedTimestamp

    @QueuedTimestamp.setter
    def QueuedTimestamp(self, QueuedTimestamp):
        self._QueuedTimestamp = QueuedTimestamp

    @property
    def PostIVRKeyPressed(self):
        """后置IVR按键信息（e.g. [{"Key":"1","Label":"非常满意"}]）
        :rtype: list of IVRKeyPressedElement
        """
        return self._PostIVRKeyPressed

    @PostIVRKeyPressed.setter
    def PostIVRKeyPressed(self, PostIVRKeyPressed):
        self._PostIVRKeyPressed = PostIVRKeyPressed

    @property
    def QueuedSkillGroupId(self):
        """排队技能组Id
        :rtype: int
        """
        return self._QueuedSkillGroupId

    @QueuedSkillGroupId.setter
    def QueuedSkillGroupId(self, QueuedSkillGroupId):
        self._QueuedSkillGroupId = QueuedSkillGroupId

    @property
    def SessionId(self):
        """会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ProtectedCaller(self):
        """主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
        :rtype: str
        """
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        """被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
        :rtype: str
        """
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee

    @property
    def Uui(self):
        warnings.warn("parameter `Uui` is deprecated", DeprecationWarning) 

        """客户自定义数据（User-to-User Interface）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uui

    @Uui.setter
    def Uui(self, Uui):
        warnings.warn("parameter `Uui` is deprecated", DeprecationWarning) 

        self._Uui = Uui

    @property
    def UUI(self):
        """客户自定义数据（User-to-User Interface）
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def IVRKeyPressedEx(self):
        """IVR按键信息（e.g. [{"Key":"1","Label":"非常满意"}]）
        :rtype: list of IVRKeyPressedElement
        """
        return self._IVRKeyPressedEx

    @IVRKeyPressedEx.setter
    def IVRKeyPressedEx(self, IVRKeyPressedEx):
        self._IVRKeyPressedEx = IVRKeyPressedEx

    @property
    def AsrUrl(self):
        """获取录音ASR文本信息地址
        :rtype: str
        """
        return self._AsrUrl

    @AsrUrl.setter
    def AsrUrl(self, AsrUrl):
        self._AsrUrl = AsrUrl

    @property
    def AsrStatus(self):
        """AsrUrl的状态：Complete
已完成;
Processing
正在生成中;
NotExists
无记录(未开启生成离线asr或者无套餐包)
        :rtype: str
        """
        return self._AsrStatus

    @AsrStatus.setter
    def AsrStatus(self, AsrStatus):
        self._AsrStatus = AsrStatus

    @property
    def CustomRecordURL(self):
        """录音转存第三方COS地址
        :rtype: str
        """
        return self._CustomRecordURL

    @CustomRecordURL.setter
    def CustomRecordURL(self, CustomRecordURL):
        self._CustomRecordURL = CustomRecordURL

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def QueuedSkillGroupName(self):
        """排队技能组名称
        :rtype: str
        """
        return self._QueuedSkillGroupName

    @QueuedSkillGroupName.setter
    def QueuedSkillGroupName(self, QueuedSkillGroupName):
        self._QueuedSkillGroupName = QueuedSkillGroupName

    @property
    def VoicemailRecordURL(self):
        """通话中语音留言录音URL
        :rtype: list of str
        """
        return self._VoicemailRecordURL

    @VoicemailRecordURL.setter
    def VoicemailRecordURL(self, VoicemailRecordURL):
        self._VoicemailRecordURL = VoicemailRecordURL

    @property
    def VoicemailAsrURL(self):
        """通话中语音留言ASR文本信息地址
        :rtype: list of str
        """
        return self._VoicemailAsrURL

    @VoicemailAsrURL.setter
    def VoicemailAsrURL(self, VoicemailAsrURL):
        self._VoicemailAsrURL = VoicemailAsrURL


    def _deserialize(self, params):
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._Time = params.get("Time")
        self._Direction = params.get("Direction")
        self._Duration = params.get("Duration")
        self._RecordURL = params.get("RecordURL")
        self._RecordId = params.get("RecordId")
        if params.get("SeatUser") is not None:
            self._SeatUser = SeatUserInfo()
            self._SeatUser._deserialize(params.get("SeatUser"))
        self._EndStatus = params.get("EndStatus")
        self._SkillGroup = params.get("SkillGroup")
        self._CallerLocation = params.get("CallerLocation")
        self._IVRDuration = params.get("IVRDuration")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._EndedTimestamp = params.get("EndedTimestamp")
        self._IVRKeyPressed = params.get("IVRKeyPressed")
        self._HungUpSide = params.get("HungUpSide")
        if params.get("ServeParticipants") is not None:
            self._ServeParticipants = []
            for item in params.get("ServeParticipants"):
                obj = ServeParticipant()
                obj._deserialize(item)
                self._ServeParticipants.append(obj)
        self._SkillGroupId = params.get("SkillGroupId")
        self._EndStatusString = params.get("EndStatusString")
        self._StartTimestamp = params.get("StartTimestamp")
        self._QueuedTimestamp = params.get("QueuedTimestamp")
        if params.get("PostIVRKeyPressed") is not None:
            self._PostIVRKeyPressed = []
            for item in params.get("PostIVRKeyPressed"):
                obj = IVRKeyPressedElement()
                obj._deserialize(item)
                self._PostIVRKeyPressed.append(obj)
        self._QueuedSkillGroupId = params.get("QueuedSkillGroupId")
        self._SessionId = params.get("SessionId")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        self._Uui = params.get("Uui")
        self._UUI = params.get("UUI")
        if params.get("IVRKeyPressedEx") is not None:
            self._IVRKeyPressedEx = []
            for item in params.get("IVRKeyPressedEx"):
                obj = IVRKeyPressedElement()
                obj._deserialize(item)
                self._IVRKeyPressedEx.append(obj)
        self._AsrUrl = params.get("AsrUrl")
        self._AsrStatus = params.get("AsrStatus")
        self._CustomRecordURL = params.get("CustomRecordURL")
        self._Remark = params.get("Remark")
        self._QueuedSkillGroupName = params.get("QueuedSkillGroupName")
        self._VoicemailRecordURL = params.get("VoicemailRecordURL")
        self._VoicemailAsrURL = params.get("VoicemailAsrURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeRange(AbstractModel):
    """时间范围，24 小时制，格式为 09:00:00

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
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
        


class TransferToManualRequest(AbstractModel):
    """TransferToManual请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _SkillGroupId: 技能组Id
        :type SkillGroupId: int
        """
        self._SdkAppId = None
        self._SessionId = None
        self._SkillGroupId = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SkillGroupId(self):
        """技能组Id
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        self._SkillGroupId = params.get("SkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferToManualResponse(AbstractModel):
    """TransferToManual返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UnbindNumberCallOutSkillGroupRequest(AbstractModel):
    """UnbindNumberCallOutSkillGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Number: 待解绑的号码
        :type Number: str
        :param _SkillGroupIds: 待解绑的技能组Id列表
        :type SkillGroupIds: list of int non-negative
        """
        self._SdkAppId = None
        self._Number = None
        self._SkillGroupIds = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Number(self):
        """待解绑的号码
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def SkillGroupIds(self):
        """待解绑的技能组Id列表
        :rtype: list of int non-negative
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Number = params.get("Number")
        self._SkillGroupIds = params.get("SkillGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindNumberCallOutSkillGroupResponse(AbstractModel):
    """UnbindNumberCallOutSkillGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UnbindStaffSkillGroupListRequest(AbstractModel):
    """UnbindStaffSkillGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StaffEmail: 客服邮箱
        :type StaffEmail: str
        :param _SkillGroupList: 解绑技能组列表
        :type SkillGroupList: list of int
        """
        self._SdkAppId = None
        self._StaffEmail = None
        self._SkillGroupList = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffEmail(self):
        """客服邮箱
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def SkillGroupList(self):
        """解绑技能组列表
        :rtype: list of int
        """
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffEmail = params.get("StaffEmail")
        self._SkillGroupList = params.get("SkillGroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindStaffSkillGroupListResponse(AbstractModel):
    """UnbindStaffSkillGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateCCCSkillGroupRequest(AbstractModel):
    """UpdateCCCSkillGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SkillGroupID: 技能组ID
        :type SkillGroupID: int
        :param _SkillGroupName: 修改后的技能组名字
        :type SkillGroupName: str
        :param _MaxConcurrency: 修改后的最大并发数,同振最大为2
        :type MaxConcurrency: int
        :param _RingAll: true同振，false顺振
        :type RingAll: bool
        """
        self._SdkAppId = None
        self._SkillGroupID = None
        self._SkillGroupName = None
        self._MaxConcurrency = None
        self._RingAll = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SkillGroupID(self):
        """技能组ID
        :rtype: int
        """
        return self._SkillGroupID

    @SkillGroupID.setter
    def SkillGroupID(self, SkillGroupID):
        self._SkillGroupID = SkillGroupID

    @property
    def SkillGroupName(self):
        """修改后的技能组名字
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def MaxConcurrency(self):
        """修改后的最大并发数,同振最大为2
        :rtype: int
        """
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def RingAll(self):
        """true同振，false顺振
        :rtype: bool
        """
        return self._RingAll

    @RingAll.setter
    def RingAll(self, RingAll):
        self._RingAll = RingAll


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SkillGroupID = params.get("SkillGroupID")
        self._SkillGroupName = params.get("SkillGroupName")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._RingAll = params.get("RingAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCCCSkillGroupResponse(AbstractModel):
    """UpdateCCCSkillGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdatePredictiveDialingCampaignRequest(AbstractModel):
    """UpdatePredictiveDialingCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CampaignId: 生成的任务 ID
        :type CampaignId: int
        :param _Name: 任务名称
        :type Name: str
        :param _Callees: 被叫列表，支持 E.164 或不带国家码形式的号码
        :type Callees: list of str
        :param _Callers: 主叫列表，使用管理端展示的号码格式
        :type Callers: list of str
        :param _CallOrder: 被叫呼叫顺序 0 随机 1 顺序
        :type CallOrder: int
        :param _SkillGroupId: 使用的座席技能组 ID
        :type SkillGroupId: int
        :param _Priority: 相同应用内多个任务运行优先级，从高到底 1 - 5
        :type Priority: int
        :param _ExpectedAbandonRate: 预期呼损率，百分比，5 - 50	
        :type ExpectedAbandonRate: int
        :param _RetryInterval: 呼叫重试间隔时间，单位秒，60 - 86400
        :type RetryInterval: int
        :param _StartTime: 任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :type StartTime: int
        :param _EndTime: 任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :type EndTime: int
        :param _IVRId: 指定的 IVR ID
        :type IVRId: int
        :param _RetryTimes: 呼叫重试次数，0 - 2
        :type RetryTimes: int
        :param _Variables: 自定义变量
        :type Variables: list of Variable
        :param _UUI: 	UUI
        :type UUI: str
        :param _CalleeAttributes: 被叫属性
        :type CalleeAttributes: list of CalleeAttribute
        """
        self._SdkAppId = None
        self._CampaignId = None
        self._Name = None
        self._Callees = None
        self._Callers = None
        self._CallOrder = None
        self._SkillGroupId = None
        self._Priority = None
        self._ExpectedAbandonRate = None
        self._RetryInterval = None
        self._StartTime = None
        self._EndTime = None
        self._IVRId = None
        self._RetryTimes = None
        self._Variables = None
        self._UUI = None
        self._CalleeAttributes = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """生成的任务 ID
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Callees(self):
        """被叫列表，支持 E.164 或不带国家码形式的号码
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        """主叫列表，使用管理端展示的号码格式
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def CallOrder(self):
        """被叫呼叫顺序 0 随机 1 顺序
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def SkillGroupId(self):
        """使用的座席技能组 ID
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Priority(self):
        """相同应用内多个任务运行优先级，从高到底 1 - 5
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def ExpectedAbandonRate(self):
        """预期呼损率，百分比，5 - 50	
        :rtype: int
        """
        return self._ExpectedAbandonRate

    @ExpectedAbandonRate.setter
    def ExpectedAbandonRate(self, ExpectedAbandonRate):
        self._ExpectedAbandonRate = ExpectedAbandonRate

    @property
    def RetryInterval(self):
        """呼叫重试间隔时间，单位秒，60 - 86400
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def StartTime(self):
        """任务启动时间，Unix 时间戳，到此时间后会自动启动任务
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间，Unix 时间戳，到此时间后会自动终止任务
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IVRId(self):
        """指定的 IVR ID
        :rtype: int
        """
        return self._IVRId

    @IVRId.setter
    def IVRId(self, IVRId):
        self._IVRId = IVRId

    @property
    def RetryTimes(self):
        """呼叫重试次数，0 - 2
        :rtype: int
        """
        return self._RetryTimes

    @RetryTimes.setter
    def RetryTimes(self, RetryTimes):
        self._RetryTimes = RetryTimes

    @property
    def Variables(self):
        """自定义变量
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        """	UUI
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def CalleeAttributes(self):
        """被叫属性
        :rtype: list of CalleeAttribute
        """
        return self._CalleeAttributes

    @CalleeAttributes.setter
    def CalleeAttributes(self, CalleeAttributes):
        self._CalleeAttributes = CalleeAttributes


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        self._Name = params.get("Name")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._CallOrder = params.get("CallOrder")
        self._SkillGroupId = params.get("SkillGroupId")
        self._Priority = params.get("Priority")
        self._ExpectedAbandonRate = params.get("ExpectedAbandonRate")
        self._RetryInterval = params.get("RetryInterval")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IVRId = params.get("IVRId")
        self._RetryTimes = params.get("RetryTimes")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        if params.get("CalleeAttributes") is not None:
            self._CalleeAttributes = []
            for item in params.get("CalleeAttributes"):
                obj = CalleeAttribute()
                obj._deserialize(item)
                self._CalleeAttributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePredictiveDialingCampaignResponse(AbstractModel):
    """UpdatePredictiveDialingCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UploadAudioInfo(AbstractModel):
    """上传音频文件信息

    """

    def __init__(self):
        r"""
        :param _CustomFileName: 文件别名（可重复）
        :type CustomFileName: str
        :param _AudioUrl: 音频文件链接。(支持mp3和wav格式，文件不超过5MB)
        :type AudioUrl: str
        """
        self._CustomFileName = None
        self._AudioUrl = None

    @property
    def CustomFileName(self):
        """文件别名（可重复）
        :rtype: str
        """
        return self._CustomFileName

    @CustomFileName.setter
    def CustomFileName(self, CustomFileName):
        self._CustomFileName = CustomFileName

    @property
    def AudioUrl(self):
        """音频文件链接。(支持mp3和wav格式，文件不超过5MB)
        :rtype: str
        """
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl


    def _deserialize(self, params):
        self._CustomFileName = params.get("CustomFileName")
        self._AudioUrl = params.get("AudioUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadIvrAudioFailedInfo(AbstractModel):
    """上传音频文件失败信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名
        :type FileName: str
        :param _FailedMsg: 失败原因
        :type FailedMsg: str
        """
        self._FileName = None
        self._FailedMsg = None

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FailedMsg(self):
        """失败原因
        :rtype: str
        """
        return self._FailedMsg

    @FailedMsg.setter
    def FailedMsg(self, FailedMsg):
        self._FailedMsg = FailedMsg


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FailedMsg = params.get("FailedMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadIvrAudioRequest(AbstractModel):
    """UploadIvrAudio请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _AudioList: 音频文件列表
        :type AudioList: list of UploadAudioInfo
        """
        self._SdkAppId = None
        self._AudioList = None

    @property
    def SdkAppId(self):
        """应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AudioList(self):
        """音频文件列表
        :rtype: list of UploadAudioInfo
        """
        return self._AudioList

    @AudioList.setter
    def AudioList(self, AudioList):
        self._AudioList = AudioList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("AudioList") is not None:
            self._AudioList = []
            for item in params.get("AudioList"):
                obj = UploadAudioInfo()
                obj._deserialize(item)
                self._AudioList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadIvrAudioResponse(AbstractModel):
    """UploadIvrAudio返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedFileList: 上传失败的文件列表
        :type FailedFileList: list of UploadIvrAudioFailedInfo
        :param _SuccessFileList: 上传成功文件列表
        :type SuccessFileList: list of AudioFileInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedFileList = None
        self._SuccessFileList = None
        self._RequestId = None

    @property
    def FailedFileList(self):
        """上传失败的文件列表
        :rtype: list of UploadIvrAudioFailedInfo
        """
        return self._FailedFileList

    @FailedFileList.setter
    def FailedFileList(self, FailedFileList):
        self._FailedFileList = FailedFileList

    @property
    def SuccessFileList(self):
        """上传成功文件列表
        :rtype: list of AudioFileInfo
        """
        return self._SuccessFileList

    @SuccessFileList.setter
    def SuccessFileList(self, SuccessFileList):
        self._SuccessFileList = SuccessFileList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FailedFileList") is not None:
            self._FailedFileList = []
            for item in params.get("FailedFileList"):
                obj = UploadIvrAudioFailedInfo()
                obj._deserialize(item)
                self._FailedFileList.append(obj)
        if params.get("SuccessFileList") is not None:
            self._SuccessFileList = []
            for item in params.get("SuccessFileList"):
                obj = AudioFileInfo()
                obj._deserialize(item)
                self._SuccessFileList.append(obj)
        self._RequestId = params.get("RequestId")


class Variable(AbstractModel):
    """变量

    """

    def __init__(self):
        r"""
        :param _Key: 变量名
        :type Key: str
        :param _Value: 变量值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """变量名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """变量值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        