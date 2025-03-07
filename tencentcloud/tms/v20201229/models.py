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


class DetailResults(AbstractModel):
    """文本审核返回的详细结果

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回检测结果所对应的全部恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告；以及其他令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _Suggestion: 该字段用于返回对应当前标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Keywords: 该字段用于返回检测文本命中的关键词信息，用于标注文本违规的具体原因（如：*加我微信*）。该参数可能会有多个返回值，代表命中的多个关键词；如返回值为空且Score不为空，则代表识别结果所对应的恶意标签（Label）是来自于语义模型判断的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _Score: 该字段用于返回当前标签（Label）下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容；*色情 0*，则表明该文本不属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _LibType: 该字段用于返回自定义关键词对应的词库类型，取值为**1**（黑白库）和**2**（自定义关键词库），若未配置自定义关键词库,则默认值为1（黑白库匹配）。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibType: int
        :param _LibId: 该字段用于返回自定义库的ID，以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param _LibName: 该字段用于返回自定义库的名称,以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param _SubLabel: 该字段用于返回当前标签（Label）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _Tags: 该字段用于返回当前一级标签（Label）下的关键词、子标签及分数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _HitInfos: 该字段用于返回违规文本命中信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HitInfos: list of HitInfo
        """
        self._Label = None
        self._Suggestion = None
        self._Keywords = None
        self._Score = None
        self._LibType = None
        self._LibId = None
        self._LibName = None
        self._SubLabel = None
        self._Tags = None
        self._HitInfos = None

    @property
    def Label(self):
        """该字段用于返回检测结果所对应的全部恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告；以及其他令人反感、不安全或不适宜的内容类型。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        """该字段用于返回对应当前标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Keywords(self):
        """该字段用于返回检测文本命中的关键词信息，用于标注文本违规的具体原因（如：*加我微信*）。该参数可能会有多个返回值，代表命中的多个关键词；如返回值为空且Score不为空，则代表识别结果所对应的恶意标签（Label）是来自于语义模型判断的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Score(self):
        """该字段用于返回当前标签（Label）下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容；*色情 0*，则表明该文本不属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def LibType(self):
        """该字段用于返回自定义关键词对应的词库类型，取值为**1**（黑白库）和**2**（自定义关键词库），若未配置自定义关键词库,则默认值为1（黑白库匹配）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LibType

    @LibType.setter
    def LibType(self, LibType):
        self._LibType = LibType

    @property
    def LibId(self):
        """该字段用于返回自定义库的ID，以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        """该字段用于返回自定义库的名称,以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def SubLabel(self):
        """该字段用于返回当前标签（Label）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Tags(self):
        """该字段用于返回当前一级标签（Label）下的关键词、子标签及分数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HitInfos(self):
        """该字段用于返回违规文本命中信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of HitInfo
        """
        return self._HitInfos

    @HitInfos.setter
    def HitInfos(self, HitInfos):
        self._HitInfos = HitInfos


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Keywords = params.get("Keywords")
        self._Score = params.get("Score")
        self._LibType = params.get("LibType")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._SubLabel = params.get("SubLabel")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("HitInfos") is not None:
            self._HitInfos = []
            for item in params.get("HitInfos"):
                obj = HitInfo()
                obj._deserialize(item)
                self._HitInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    """用于表示业务用户对应的设备信息

    """

    def __init__(self):
        r"""
        :param _IP: 该字段表示业务用户对应设备的IP地址。<br>
备注:目前仅支持IPv4地址记录，不支持IPv6地址记录。
        :type IP: str
        :param _Mac: 该字段表示业务用户对应的MAC地址，以方便设备识别与管理；其格式与取值与标准MAC地址一致。
        :type Mac: str
        :param _TokenId: *内测中，敬请期待。*
        :type TokenId: str
        :param _DeviceId: *内测中，敬请期待。*
        :type DeviceId: str
        :param _IMEI: 该字段表示业务用户对应设备的**IMEI码**（国际移动设备识别码），该识别码可用于识别每一部独立的手机等移动通信设备，方便设备识别与管理。<br>备注：格式为**15-17位纯数字**。
        :type IMEI: str
        :param _IDFA: **iOS设备专用**，该字段表示业务用户对应的**IDFA**(广告标识符),这是由苹果公司提供的用于标识用户的广告标识符，由一串16进制的32位数字和字母组成。<br>
备注：苹果公司自2021年iOS14更新后允许用户手动关闭或者开启IDFA，故此字符串标记有效性可能有所降低。
        :type IDFA: str
        :param _IDFV: **iOS设备专用**，该字段表示业务用户对应的**IDFV**(应用开发商标识符),这是由苹果公司提供的用于标注应用开发商的标识符，由一串16进制的32位数字和字母组成，可被用于唯一标识设备。
        :type IDFV: str
        """
        self._IP = None
        self._Mac = None
        self._TokenId = None
        self._DeviceId = None
        self._IMEI = None
        self._IDFA = None
        self._IDFV = None

    @property
    def IP(self):
        """该字段表示业务用户对应设备的IP地址。<br>
备注:目前仅支持IPv4地址记录，不支持IPv6地址记录。
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Mac(self):
        """该字段表示业务用户对应的MAC地址，以方便设备识别与管理；其格式与取值与标准MAC地址一致。
        :rtype: str
        """
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def TokenId(self):
        """*内测中，敬请期待。*
        :rtype: str
        """
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def DeviceId(self):
        """*内测中，敬请期待。*
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def IMEI(self):
        """该字段表示业务用户对应设备的**IMEI码**（国际移动设备识别码），该识别码可用于识别每一部独立的手机等移动通信设备，方便设备识别与管理。<br>备注：格式为**15-17位纯数字**。
        :rtype: str
        """
        return self._IMEI

    @IMEI.setter
    def IMEI(self, IMEI):
        self._IMEI = IMEI

    @property
    def IDFA(self):
        """**iOS设备专用**，该字段表示业务用户对应的**IDFA**(广告标识符),这是由苹果公司提供的用于标识用户的广告标识符，由一串16进制的32位数字和字母组成。<br>
备注：苹果公司自2021年iOS14更新后允许用户手动关闭或者开启IDFA，故此字符串标记有效性可能有所降低。
        :rtype: str
        """
        return self._IDFA

    @IDFA.setter
    def IDFA(self, IDFA):
        self._IDFA = IDFA

    @property
    def IDFV(self):
        """**iOS设备专用**，该字段表示业务用户对应的**IDFV**(应用开发商标识符),这是由苹果公司提供的用于标注应用开发商的标识符，由一串16进制的32位数字和字母组成，可被用于唯一标识设备。
        :rtype: str
        """
        return self._IDFV

    @IDFV.setter
    def IDFV(self, IDFV):
        self._IDFV = IDFV


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Mac = params.get("Mac")
        self._TokenId = params.get("TokenId")
        self._DeviceId = params.get("DeviceId")
        self._IMEI = params.get("IMEI")
        self._IDFA = params.get("IDFA")
        self._IDFV = params.get("IDFV")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HitInfo(AbstractModel):
    """关键词命中位置信息

    """

    def __init__(self):
        r"""
        :param _Type: 标识模型命中还是关键词命中
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Keyword: 命中关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keyword: str
        :param _LibName: 自定义词库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param _Positions: 位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Positions: list of Positions
        """
        self._Type = None
        self._Keyword = None
        self._LibName = None
        self._Positions = None

    @property
    def Type(self):
        """标识模型命中还是关键词命中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Keyword(self):
        """命中关键词
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def LibName(self):
        """自定义词库名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Positions(self):
        """位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Positions
        """
        return self._Positions

    @Positions.setter
    def Positions(self, Positions):
        self._Positions = Positions


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Keyword = params.get("Keyword")
        self._LibName = params.get("LibName")
        if params.get("Positions") is not None:
            self._Positions = []
            for item in params.get("Positions"):
                obj = Positions()
                obj._deserialize(item)
                self._Positions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Positions(AbstractModel):
    """标识命中的违规关键词位置信息

    """

    def __init__(self):
        r"""
        :param _Start: 关键词起始位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Start: int
        :param _End: 关键词结束位置
注意：此字段可能返回 null，表示取不到有效值。
        :type End: int
        """
        self._Start = None
        self._End = None

    @property
    def Start(self):
        """关键词起始位置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        """关键词结束位置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDetails(AbstractModel):
    """账号风险检测结果

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回账号信息检测对应的风险类别，取值为：**RiskAccount**（账号存在风险）、**RiskIP**（IP地址存在风险）、**RiskIMEI**（移动设备识别码存在风险）。
        :type Label: str
        :param _Level: 该字段用于返回账号信息检测对应的风险等级，取值为：**1**（疑似存在风险）和**2**（存在恶意风险）。
        :type Level: int
        """
        self._Label = None
        self._Level = None

    @property
    def Label(self):
        """该字段用于返回账号信息检测对应的风险类别，取值为：**RiskAccount**（账号存在风险）、**RiskIP**（IP地址存在风险）、**RiskIMEI**（移动设备识别码存在风险）。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Level(self):
        """该字段用于返回账号信息检测对应的风险等级，取值为：**1**（疑似存在风险）和**2**（存在恶意风险）。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentimentAnalysis(AbstractModel):
    """情感分析结果

    """

    def __init__(self):
        r"""
        :param _Label: 情感标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Score: 标签分数，取值范围0到100
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Detail: 情感分析明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: :class:`tencentcloud.tms.v20201229.models.SentimentDetail`
        :param _Code: 响应码，成功为"OK"，失败为"InternalError"
        :type Code: str
        :param _Message: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._Label = None
        self._Score = None
        self._Detail = None
        self._Code = None
        self._Message = None

    @property
    def Label(self):
        """情感标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        """标签分数，取值范围0到100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Detail(self):
        """情感分析明细
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tms.v20201229.models.SentimentDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Code(self):
        """响应码，成功为"OK"，失败为"InternalError"
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Score = params.get("Score")
        if params.get("Detail") is not None:
            self._Detail = SentimentDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentimentDetail(AbstractModel):
    """情感分析明细

    """

    def __init__(self):
        r"""
        :param _Positive: 正向分数，取值范围0到100
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: int
        :param _Negative: 负向分数，取值范围0到100
注意：此字段可能返回 null，表示取不到有效值。
        :type Negative: int
        """
        self._Positive = None
        self._Negative = None

    @property
    def Positive(self):
        """正向分数，取值范围0到100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Negative(self):
        """负向分数，取值范围0到100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Negative

    @Negative.setter
    def Negative(self, Negative):
        self._Negative = Negative


    def _deserialize(self, params):
        self._Positive = params.get("Positive")
        self._Negative = params.get("Negative")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """该字段用于返回审核结果明细字段的标签及分数

    """

    def __init__(self):
        r"""
        :param _Keyword: 该字段用于返回命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keyword: str
        :param _SubLabel: 该字段用于返回子标签
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _Score: 该字段用于返回子标签对应的分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        """
        self._Keyword = None
        self._SubLabel = None
        self._Score = None

    @property
    def Keyword(self):
        """该字段用于返回命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def SubLabel(self):
        """该字段用于返回子标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        """该字段用于返回子标签对应的分数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationRequest(AbstractModel):
    """TextModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 该字段表示待检测对象的文本内容，文本需要按utf-8格式编码，长度不能超过10000个字符（按unicode编码计算），并进行 Base64加密
        :type Content: str
        :param _BizType: 该字段表示策略的具体编号，用于接口调度，在内容安全控制台中可配置。若不传入Biztype参数（留空），则代表采用默认的识别策略；传入则会在审核时根据业务场景采取不同的审核策略。<br>备注：Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype
        :type BizType: str
        :param _DataId: 该字段表示您为待检测对象分配的数据ID，传入后可方便您对文件进行标识和管理。<br>取值：由英文字母（大小写均可）、数字及四个特殊符号（_，-，@，#）组成，**长度不超过64个字符**
        :type DataId: str
        :param _User: 该字段表示待检测对象对应的用户相关信息，传入后可便于甄别相应违规风险用户
        :type User: :class:`tencentcloud.tms.v20201229.models.User`
        :param _Device: 该字段表示待检测对象对应的设备相关信息，传入后可便于甄别相应违规风险设备
        :type Device: :class:`tencentcloud.tms.v20201229.models.Device`
        :param _SourceLanguage: Content的原始语种，比如en,zh
        :type SourceLanguage: str
        """
        self._Content = None
        self._BizType = None
        self._DataId = None
        self._User = None
        self._Device = None
        self._SourceLanguage = None

    @property
    def Content(self):
        """该字段表示待检测对象的文本内容，文本需要按utf-8格式编码，长度不能超过10000个字符（按unicode编码计算），并进行 Base64加密
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def BizType(self):
        """该字段表示策略的具体编号，用于接口调度，在内容安全控制台中可配置。若不传入Biztype参数（留空），则代表采用默认的识别策略；传入则会在审核时根据业务场景采取不同的审核策略。<br>备注：Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DataId(self):
        """该字段表示您为待检测对象分配的数据ID，传入后可方便您对文件进行标识和管理。<br>取值：由英文字母（大小写均可）、数字及四个特殊符号（_，-，@，#）组成，**长度不超过64个字符**
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def User(self):
        """该字段表示待检测对象对应的用户相关信息，传入后可便于甄别相应违规风险用户
        :rtype: :class:`tencentcloud.tms.v20201229.models.User`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Device(self):
        """该字段表示待检测对象对应的设备相关信息，传入后可便于甄别相应违规风险设备
        :rtype: :class:`tencentcloud.tms.v20201229.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def SourceLanguage(self):
        """Content的原始语种，比如en,zh
        :rtype: str
        """
        return self._SourceLanguage

    @SourceLanguage.setter
    def SourceLanguage(self, SourceLanguage):
        self._SourceLanguage = SourceLanguage


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._BizType = params.get("BizType")
        self._DataId = params.get("DataId")
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        self._SourceLanguage = params.get("SourceLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationResponse(AbstractModel):
    """TextModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 该字段用于返回请求参数中的BizType参数
        :type BizType: str
        :param _Label: 该字段用于返回检测结果（DetailResults）中所对应的**优先级最高的恶意标签**，表示模型推荐的审核结果，建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告；以及其他令人反感、不安全或不适宜的内容类型
        :type Label: str
        :param _Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        :param _Keywords: 该字段用于返回当前标签（Label）下被检测文本命中的关键词信息，用于标注文本违规的具体原因（如：*加我微信*）。该参数可能会有多个返回值，代表命中的多个关键词；如返回值为空且Score不为空，则代表识别结果所对应的恶意标签（Label）是来自于语义模型判断的返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _Score: 该字段用于返回当前标签（Label）下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容；*色情 0*，则表明该文本不属于色情内容
        :type Score: int
        :param _DetailResults: 该字段用于返回基于文本风险库审核的详细结果，返回值信息可参阅对应数据结构（DetailResults）的详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailResults: list of DetailResults
        :param _RiskDetails: 该字段用于返回文本检测中存在违规风险的账号检测结果，主要包括违规风险类别和风险等级信息，具体内容可参阅对应数据结构（RiskDetails）的详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskDetails: list of RiskDetails
        :param _Extra: 该字段用于返回根据您的需求配置的额外附加信息（Extra），如未配置则默认返回值为空。<br>备注：不同客户或Biztype下返回信息不同，如需配置该字段请提交工单咨询或联系售后专员处理
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _DataId: 该字段用于返回检测对象对应请求参数中的DataId，与输入的DataId字段中的内容对应
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param _SubLabel: 该字段用于返回当前标签（Label）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _ContextText: 该字段用于返回上下文关联文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextText: str
        :param _SentimentAnalysis: 情感分析结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SentimentAnalysis: :class:`tencentcloud.tms.v20201229.models.SentimentAnalysis`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BizType = None
        self._Label = None
        self._Suggestion = None
        self._Keywords = None
        self._Score = None
        self._DetailResults = None
        self._RiskDetails = None
        self._Extra = None
        self._DataId = None
        self._SubLabel = None
        self._ContextText = None
        self._SentimentAnalysis = None
        self._RequestId = None

    @property
    def BizType(self):
        """该字段用于返回请求参数中的BizType参数
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Label(self):
        """该字段用于返回检测结果（DetailResults）中所对应的**优先级最高的恶意标签**，表示模型推荐的审核结果，建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告；以及其他令人反感、不安全或不适宜的内容类型
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        """该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Keywords(self):
        """该字段用于返回当前标签（Label）下被检测文本命中的关键词信息，用于标注文本违规的具体原因（如：*加我微信*）。该参数可能会有多个返回值，代表命中的多个关键词；如返回值为空且Score不为空，则代表识别结果所对应的恶意标签（Label）是来自于语义模型判断的返回值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Score(self):
        """该字段用于返回当前标签（Label）下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容；*色情 0*，则表明该文本不属于色情内容
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def DetailResults(self):
        """该字段用于返回基于文本风险库审核的详细结果，返回值信息可参阅对应数据结构（DetailResults）的详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DetailResults
        """
        return self._DetailResults

    @DetailResults.setter
    def DetailResults(self, DetailResults):
        self._DetailResults = DetailResults

    @property
    def RiskDetails(self):
        """该字段用于返回文本检测中存在违规风险的账号检测结果，主要包括违规风险类别和风险等级信息，具体内容可参阅对应数据结构（RiskDetails）的详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RiskDetails
        """
        return self._RiskDetails

    @RiskDetails.setter
    def RiskDetails(self, RiskDetails):
        self._RiskDetails = RiskDetails

    @property
    def Extra(self):
        """该字段用于返回根据您的需求配置的额外附加信息（Extra），如未配置则默认返回值为空。<br>备注：不同客户或Biztype下返回信息不同，如需配置该字段请提交工单咨询或联系售后专员处理
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def DataId(self):
        """该字段用于返回检测对象对应请求参数中的DataId，与输入的DataId字段中的内容对应
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def SubLabel(self):
        """该字段用于返回当前标签（Label）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def ContextText(self):
        """该字段用于返回上下文关联文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContextText

    @ContextText.setter
    def ContextText(self, ContextText):
        self._ContextText = ContextText

    @property
    def SentimentAnalysis(self):
        """情感分析结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tms.v20201229.models.SentimentAnalysis`
        """
        return self._SentimentAnalysis

    @SentimentAnalysis.setter
    def SentimentAnalysis(self, SentimentAnalysis):
        self._SentimentAnalysis = SentimentAnalysis

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
        self._BizType = params.get("BizType")
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Keywords = params.get("Keywords")
        self._Score = params.get("Score")
        if params.get("DetailResults") is not None:
            self._DetailResults = []
            for item in params.get("DetailResults"):
                obj = DetailResults()
                obj._deserialize(item)
                self._DetailResults.append(obj)
        if params.get("RiskDetails") is not None:
            self._RiskDetails = []
            for item in params.get("RiskDetails"):
                obj = RiskDetails()
                obj._deserialize(item)
                self._RiskDetails.append(obj)
        self._Extra = params.get("Extra")
        self._DataId = params.get("DataId")
        self._SubLabel = params.get("SubLabel")
        self._ContextText = params.get("ContextText")
        if params.get("SentimentAnalysis") is not None:
            self._SentimentAnalysis = SentimentAnalysis()
            self._SentimentAnalysis._deserialize(params.get("SentimentAnalysis"))
        self._RequestId = params.get("RequestId")


class User(AbstractModel):
    """用于表示业务用户的账号相关信息

    """

    def __init__(self):
        r"""
        :param _UserId: 该字段表示业务用户ID,填写后，系统可根据账号过往违规历史优化审核结果判定，有利于存在可疑违规风险时的辅助判断。<br>
备注：该字段可传入微信openid、QQopenid、字符串等账号信息，与账号类别参数（AccountType）配合使用可确定唯一账号。
        :type UserId: str
        :param _Nickname: 该字段表示业务用户对应的账号昵称信息。
        :type Nickname: str
        :param _AccountType: 该字段表示业务用户ID对应的账号类型，取值：**1**-微信uin，**2**-QQ号，**3**-微信群uin，**4**-qq群号，**5**-微信openid，**6**-QQopenid，**7**-其它string。<br>
该字段与账号ID参数（UserId）配合使用可确定唯一账号。
        :type AccountType: int
        :param _Gender: 该字段表示业务用户对应账号的性别信息。<br>
取值：**0**（默认值，代表性别未知）、**1**（男性）、**2**（女性）。
        :type Gender: int
        :param _Age: 该字段表示业务用户对应账号的年龄信息。<br>
取值：**0**（默认值，代表年龄未知）-（**自定义年龄上限**）之间的整数。
        :type Age: int
        :param _Level: 该字段表示业务用户对应账号的等级信息。<br>
取值：**0**（默认值，代表等级未知）、**1**（等级较低）、**2**（等级中等）、**3**（等级较高），目前**暂不支持自定义等级**。
        :type Level: int
        :param _Phone: 该字段表示业务用户对应账号的手机号信息，支持全球各地区手机号的记录。<br>
备注：请保持手机号格式的统一，如区号格式（086/+86）等。
        :type Phone: str
        :param _HeadUrl: 该字段表示业务用户头像图片的访问链接(URL)，支持PNG、JPG、JPEG、BMP、GIF、WEBP格式。
备注：头像图片大小不超过5MB，建议分辨率不低于256x256；图片下载时间限制为3秒，超过则会返回下载超时。
        :type HeadUrl: str
        :param _Desc: 该字段表示业务用户的简介信息，支持汉字、英文及特殊符号，长度不超过5000个汉字字符。
        :type Desc: str
        :param _RoomId: 该字段表示业务群聊场景时的房间ID。
        :type RoomId: str
        :param _ReceiverId: 该字段表示消息接受者ID
        :type ReceiverId: str
        :param _SendTime: 消息生成时间，精确到毫秒
        :type SendTime: int
        """
        self._UserId = None
        self._Nickname = None
        self._AccountType = None
        self._Gender = None
        self._Age = None
        self._Level = None
        self._Phone = None
        self._HeadUrl = None
        self._Desc = None
        self._RoomId = None
        self._ReceiverId = None
        self._SendTime = None

    @property
    def UserId(self):
        """该字段表示业务用户ID,填写后，系统可根据账号过往违规历史优化审核结果判定，有利于存在可疑违规风险时的辅助判断。<br>
备注：该字段可传入微信openid、QQopenid、字符串等账号信息，与账号类别参数（AccountType）配合使用可确定唯一账号。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Nickname(self):
        """该字段表示业务用户对应的账号昵称信息。
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def AccountType(self):
        """该字段表示业务用户ID对应的账号类型，取值：**1**-微信uin，**2**-QQ号，**3**-微信群uin，**4**-qq群号，**5**-微信openid，**6**-QQopenid，**7**-其它string。<br>
该字段与账号ID参数（UserId）配合使用可确定唯一账号。
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Gender(self):
        """该字段表示业务用户对应账号的性别信息。<br>
取值：**0**（默认值，代表性别未知）、**1**（男性）、**2**（女性）。
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        """该字段表示业务用户对应账号的年龄信息。<br>
取值：**0**（默认值，代表年龄未知）-（**自定义年龄上限**）之间的整数。
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Level(self):
        """该字段表示业务用户对应账号的等级信息。<br>
取值：**0**（默认值，代表等级未知）、**1**（等级较低）、**2**（等级中等）、**3**（等级较高），目前**暂不支持自定义等级**。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Phone(self):
        """该字段表示业务用户对应账号的手机号信息，支持全球各地区手机号的记录。<br>
备注：请保持手机号格式的统一，如区号格式（086/+86）等。
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def HeadUrl(self):
        """该字段表示业务用户头像图片的访问链接(URL)，支持PNG、JPG、JPEG、BMP、GIF、WEBP格式。
备注：头像图片大小不超过5MB，建议分辨率不低于256x256；图片下载时间限制为3秒，超过则会返回下载超时。
        :rtype: str
        """
        return self._HeadUrl

    @HeadUrl.setter
    def HeadUrl(self, HeadUrl):
        self._HeadUrl = HeadUrl

    @property
    def Desc(self):
        """该字段表示业务用户的简介信息，支持汉字、英文及特殊符号，长度不超过5000个汉字字符。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def RoomId(self):
        """该字段表示业务群聊场景时的房间ID。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def ReceiverId(self):
        """该字段表示消息接受者ID
        :rtype: str
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def SendTime(self):
        """消息生成时间，精确到毫秒
        :rtype: int
        """
        return self._SendTime

    @SendTime.setter
    def SendTime(self, SendTime):
        self._SendTime = SendTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Nickname = params.get("Nickname")
        self._AccountType = params.get("AccountType")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._Level = params.get("Level")
        self._Phone = params.get("Phone")
        self._HeadUrl = params.get("HeadUrl")
        self._Desc = params.get("Desc")
        self._RoomId = params.get("RoomId")
        self._ReceiverId = params.get("ReceiverId")
        self._SendTime = params.get("SendTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        