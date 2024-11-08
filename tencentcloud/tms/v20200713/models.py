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


class AccountTipoffAccessRequest(AbstractModel):
    """AccountTipoffAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportedAccount: 被举报账号，长度低于 128 个字符
        :type ReportedAccount: str
        :param _ReportedAccountType: 被举报账号类型(1-手机号 2-QQ号 3-微信号 4-QQ群号 5-微信openid 6-QQopenid 0-其它)
        :type ReportedAccountType: int
        :param _EvilType: 被举报账号所属恶意类型(1-诈骗，2-骚扰，3-广告，4-违法违规，5-赌博传销，0-其他)
        :type EvilType: int
        :param _SenderAccount: 举报者账号，长度低于 128 个字符
        :type SenderAccount: str
        :param _SenderAccountType: 举报者账号类型(1-手机号 2-QQ号 3-微信号 4-QQ群号 5-微信openid 6-QQopenid 0-其它)
        :type SenderAccountType: int
        :param _SenderIP: 举报者IP地址
        :type SenderIP: str
        :param _EvilContent: 包含被举报账号的恶意内容（比如文本、图片链接，长度低于1024个字符）
        :type EvilContent: str
        """
        self._ReportedAccount = None
        self._ReportedAccountType = None
        self._EvilType = None
        self._SenderAccount = None
        self._SenderAccountType = None
        self._SenderIP = None
        self._EvilContent = None

    @property
    def ReportedAccount(self):
        """被举报账号，长度低于 128 个字符
        :rtype: str
        """
        return self._ReportedAccount

    @ReportedAccount.setter
    def ReportedAccount(self, ReportedAccount):
        self._ReportedAccount = ReportedAccount

    @property
    def ReportedAccountType(self):
        """被举报账号类型(1-手机号 2-QQ号 3-微信号 4-QQ群号 5-微信openid 6-QQopenid 0-其它)
        :rtype: int
        """
        return self._ReportedAccountType

    @ReportedAccountType.setter
    def ReportedAccountType(self, ReportedAccountType):
        self._ReportedAccountType = ReportedAccountType

    @property
    def EvilType(self):
        """被举报账号所属恶意类型(1-诈骗，2-骚扰，3-广告，4-违法违规，5-赌博传销，0-其他)
        :rtype: int
        """
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def SenderAccount(self):
        """举报者账号，长度低于 128 个字符
        :rtype: str
        """
        return self._SenderAccount

    @SenderAccount.setter
    def SenderAccount(self, SenderAccount):
        self._SenderAccount = SenderAccount

    @property
    def SenderAccountType(self):
        """举报者账号类型(1-手机号 2-QQ号 3-微信号 4-QQ群号 5-微信openid 6-QQopenid 0-其它)
        :rtype: int
        """
        return self._SenderAccountType

    @SenderAccountType.setter
    def SenderAccountType(self, SenderAccountType):
        self._SenderAccountType = SenderAccountType

    @property
    def SenderIP(self):
        """举报者IP地址
        :rtype: str
        """
        return self._SenderIP

    @SenderIP.setter
    def SenderIP(self, SenderIP):
        self._SenderIP = SenderIP

    @property
    def EvilContent(self):
        """包含被举报账号的恶意内容（比如文本、图片链接，长度低于1024个字符）
        :rtype: str
        """
        return self._EvilContent

    @EvilContent.setter
    def EvilContent(self, EvilContent):
        self._EvilContent = EvilContent


    def _deserialize(self, params):
        self._ReportedAccount = params.get("ReportedAccount")
        self._ReportedAccountType = params.get("ReportedAccountType")
        self._EvilType = params.get("EvilType")
        self._SenderAccount = params.get("SenderAccount")
        self._SenderAccountType = params.get("SenderAccountType")
        self._SenderIP = params.get("SenderIP")
        self._EvilContent = params.get("EvilContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountTipoffAccessResponse(AbstractModel):
    """AccountTipoffAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 举报接口响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.tms.v20200713.models.TipoffResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """举报接口响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tms.v20200713.models.TipoffResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TipoffResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTextLibRequest(AbstractModel):
    """DescribeTextLib请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyType: 内容类型 text: 1; image: 2; audio: 3; video: 4
        :type StrategyType: int
        """
        self._StrategyType = None

    @property
    def StrategyType(self):
        """内容类型 text: 1; image: 2; audio: 3; video: 4
        :rtype: int
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType


    def _deserialize(self, params):
        self._StrategyType = params.get("StrategyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTextLibResponse(AbstractModel):
    """DescribeTextLib返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextLib: 文本库id和name列表
        :type TextLib: list of TextLib
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextLib = None
        self._RequestId = None

    @property
    def TextLib(self):
        """文本库id和name列表
        :rtype: list of TextLib
        """
        return self._TextLib

    @TextLib.setter
    def TextLib(self, TextLib):
        self._TextLib = TextLib

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
        if params.get("TextLib") is not None:
            self._TextLib = []
            for item in params.get("TextLib"):
                obj = TextLib()
                obj._deserialize(item)
                self._TextLib.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTextStatRequest(AbstractModel):
    """DescribeTextStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditType: 审核类型 1: 机器审核; 2: 人工审核
        :type AuditType: int
        :param _Filters: 查询条件
        :type Filters: list of Filters
        """
        self._AuditType = None
        self._Filters = None

    @property
    def AuditType(self):
        """审核类型 1: 机器审核; 2: 人工审核
        :rtype: int
        """
        return self._AuditType

    @AuditType.setter
    def AuditType(self, AuditType):
        self._AuditType = AuditType

    @property
    def Filters(self):
        """查询条件
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AuditType = params.get("AuditType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTextStatResponse(AbstractModel):
    """DescribeTextStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Overview: 识别结果统计
        :type Overview: :class:`tencentcloud.tms.v20200713.models.Overview`
        :param _TrendCount: 识别量统计
        :type TrendCount: list of TrendCount
        :param _EvilCount: 违规数据分布
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilCount: list of EvilCount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Overview = None
        self._TrendCount = None
        self._EvilCount = None
        self._RequestId = None

    @property
    def Overview(self):
        """识别结果统计
        :rtype: :class:`tencentcloud.tms.v20200713.models.Overview`
        """
        return self._Overview

    @Overview.setter
    def Overview(self, Overview):
        self._Overview = Overview

    @property
    def TrendCount(self):
        """识别量统计
        :rtype: list of TrendCount
        """
        return self._TrendCount

    @TrendCount.setter
    def TrendCount(self, TrendCount):
        self._TrendCount = TrendCount

    @property
    def EvilCount(self):
        """违规数据分布
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EvilCount
        """
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

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
        if params.get("Overview") is not None:
            self._Overview = Overview()
            self._Overview._deserialize(params.get("Overview"))
        if params.get("TrendCount") is not None:
            self._TrendCount = []
            for item in params.get("TrendCount"):
                obj = TrendCount()
                obj._deserialize(item)
                self._TrendCount.append(obj)
        if params.get("EvilCount") is not None:
            self._EvilCount = []
            for item in params.get("EvilCount"):
                obj = EvilCount()
                obj._deserialize(item)
                self._EvilCount.append(obj)
        self._RequestId = params.get("RequestId")


class DetailResults(AbstractModel):
    """文本返回的详细结果

    """

    def __init__(self):
        r"""
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Keywords: 该标签下命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _Score: 该标签模型命中的分值
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _LibType: 仅当Label为Custom自定义关键词时有效，表示自定义关键词库类型，1:黑白库，2：自定义库
注意：此字段可能返回 null，表示取不到有效值。
        :type LibType: int
        :param _LibId: 仅当Label为Custom自定义关键词时有效，表示自定义库id
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param _LibName: 仅当Labe为Custom自定义关键词时有效，表示自定义库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        """
        self._Label = None
        self._Suggestion = None
        self._Keywords = None
        self._Score = None
        self._LibType = None
        self._LibId = None
        self._LibName = None

    @property
    def Label(self):
        """恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        """建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Keywords(self):
        """该标签下命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Score(self):
        """该标签模型命中的分值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def LibType(self):
        """仅当Label为Custom自定义关键词时有效，表示自定义关键词库类型，1:黑白库，2：自定义库
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LibType

    @LibType.setter
    def LibType(self, LibType):
        self._LibType = LibType

    @property
    def LibId(self):
        """仅当Label为Custom自定义关键词时有效，表示自定义库id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        """仅当Labe为Custom自定义关键词时有效，表示自定义库名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Keywords = params.get("Keywords")
        self._Score = params.get("Score")
        self._LibType = params.get("LibType")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    """设备信息

    """

    def __init__(self):
        r"""
        :param _IP: 用户IP
        :type IP: str
        :param _Mac: Mac地址
        :type Mac: str
        :param _TokenId: 设备指纹Token
        :type TokenId: str
        :param _DeviceId: 设备指纹ID
        :type DeviceId: str
        :param _IMEI: 设备序列号
        :type IMEI: str
        :param _IDFA: IOS设备，Identifier For Advertising（广告标识符）
        :type IDFA: str
        :param _IDFV: IOS设备，IDFV - Identifier For Vendor（应用开发商标识符）
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
        """用户IP
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Mac(self):
        """Mac地址
        :rtype: str
        """
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def TokenId(self):
        """设备指纹Token
        :rtype: str
        """
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def DeviceId(self):
        """设备指纹ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def IMEI(self):
        """设备序列号
        :rtype: str
        """
        return self._IMEI

    @IMEI.setter
    def IMEI(self, IMEI):
        self._IMEI = IMEI

    @property
    def IDFA(self):
        """IOS设备，Identifier For Advertising（广告标识符）
        :rtype: str
        """
        return self._IDFA

    @IDFA.setter
    def IDFA(self, IDFA):
        self._IDFA = IDFA

    @property
    def IDFV(self):
        """IOS设备，IDFV - Identifier For Vendor（应用开发商标识符）
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
        


class EvilCount(AbstractModel):
    """违规数据分布

    """

    def __init__(self):
        r"""
        :param _EvilType: ----非必选，该参数功能暂未对外开放
        :type EvilType: str
        :param _Count: 分布类型总量
        :type Count: int
        """
        self._EvilType = None
        self._Count = None

    @property
    def EvilType(self):
        """----非必选，该参数功能暂未对外开放
        :rtype: str
        """
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def Count(self):
        """分布类型总量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """文本过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 查询字段：
策略BizType
子账号SubUin
日期区间DateRange
        :type Name: str
        :param _Values: 查询值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """查询字段：
策略BizType
子账号SubUin
日期区间DateRange
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """查询值
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
        


class Overview(AbstractModel):
    """识别结果统计

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总调用量
        :type TotalCount: int
        :param _TotalHour: 总调用时长
        :type TotalHour: int
        :param _PassCount: 通过量
        :type PassCount: int
        :param _PassHour: 通过时长
        :type PassHour: int
        :param _EvilCount: 违规量
        :type EvilCount: int
        :param _EvilHour: 违规时长
        :type EvilHour: int
        :param _SuspectCount: 疑似违规量
        :type SuspectCount: int
        :param _SuspectHour: 疑似违规时长
        :type SuspectHour: int
        """
        self._TotalCount = None
        self._TotalHour = None
        self._PassCount = None
        self._PassHour = None
        self._EvilCount = None
        self._EvilHour = None
        self._SuspectCount = None
        self._SuspectHour = None

    @property
    def TotalCount(self):
        """总调用量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalHour(self):
        """总调用时长
        :rtype: int
        """
        return self._TotalHour

    @TotalHour.setter
    def TotalHour(self, TotalHour):
        self._TotalHour = TotalHour

    @property
    def PassCount(self):
        """通过量
        :rtype: int
        """
        return self._PassCount

    @PassCount.setter
    def PassCount(self, PassCount):
        self._PassCount = PassCount

    @property
    def PassHour(self):
        """通过时长
        :rtype: int
        """
        return self._PassHour

    @PassHour.setter
    def PassHour(self, PassHour):
        self._PassHour = PassHour

    @property
    def EvilCount(self):
        """违规量
        :rtype: int
        """
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

    @property
    def EvilHour(self):
        """违规时长
        :rtype: int
        """
        return self._EvilHour

    @EvilHour.setter
    def EvilHour(self, EvilHour):
        self._EvilHour = EvilHour

    @property
    def SuspectCount(self):
        """疑似违规量
        :rtype: int
        """
        return self._SuspectCount

    @SuspectCount.setter
    def SuspectCount(self, SuspectCount):
        self._SuspectCount = SuspectCount

    @property
    def SuspectHour(self):
        """疑似违规时长
        :rtype: int
        """
        return self._SuspectHour

    @SuspectHour.setter
    def SuspectHour(self, SuspectHour):
        self._SuspectHour = SuspectHour


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalHour = params.get("TotalHour")
        self._PassCount = params.get("PassCount")
        self._PassHour = params.get("PassHour")
        self._EvilCount = params.get("EvilCount")
        self._EvilHour = params.get("EvilHour")
        self._SuspectCount = params.get("SuspectCount")
        self._SuspectHour = params.get("SuspectHour")
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
        :param _Label: 风险类别，RiskAccount，RiskIP, RiskIMEI
        :type Label: str
        :param _Level: 风险等级，1:疑似，2：恶意
        :type Level: int
        """
        self._Label = None
        self._Level = None

    @property
    def Label(self):
        """风险类别，RiskAccount，RiskIP, RiskIMEI
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Level(self):
        """风险等级，1:疑似，2：恶意
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
        


class TextLib(AbstractModel):
    """自定义库列表

    """

    def __init__(self):
        r"""
        :param _LibId: 库id
        :type LibId: int
        :param _LibName: 库名
        :type LibName: str
        """
        self._LibId = None
        self._LibName = None

    @property
    def LibId(self):
        """库id
        :rtype: int
        """
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        """库名
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName


    def _deserialize(self, params):
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
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
        :param _Content: 文本内容Base64编码。限制原文长度不能超过10000个unicode字符
        :type Content: str
        :param _BizType: 该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略
        :type BizType: str
        :param _DataId: 数据ID，英文字母、下划线、-组成，不超过64个字符
        :type DataId: str
        :param _User: 账号相关信息字段，填入后可识别违规风险账号
        :type User: :class:`tencentcloud.tms.v20200713.models.User`
        :param _Device: 设备相关信息字段，填入后可识别违规风险设备
        :type Device: :class:`tencentcloud.tms.v20200713.models.Device`
        """
        self._Content = None
        self._BizType = None
        self._DataId = None
        self._User = None
        self._Device = None

    @property
    def Content(self):
        """文本内容Base64编码。限制原文长度不能超过10000个unicode字符
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def BizType(self):
        """该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DataId(self):
        """数据ID，英文字母、下划线、-组成，不超过64个字符
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def User(self):
        """账号相关信息字段，填入后可识别违规风险账号
        :rtype: :class:`tencentcloud.tms.v20200713.models.User`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Device(self):
        """设备相关信息字段，填入后可识别违规风险设备
        :rtype: :class:`tencentcloud.tms.v20200713.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device


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
        :param _BizType: 您在入参时所填入的Biztype参数
        :type BizType: str
        :param _EvilFlag: 数据是否属于恶意类型，0：正常 1：可疑
        :type EvilFlag: int
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库，以及令人反感、不安全或不适宜的内容类型
        :type Label: str
        :param _Suggestion: 建议您拿到判断结果后的执行操作
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _Keywords: 文本命中的关键词信息，用于提示您文本违规的具体原因，可能会返回多个命中的关键词。（如：加我微信）
如返回值为空，Score不为空，即识别结果（Label）是来自于语义模型判断的返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _Score: 机器判断当前分类的置信度，取值范围：0.00~100.00。分数越高，表示越有可能属于当前分类。
（如：色情 99.99，则该样本属于色情的置信度非常高。）
        :type Score: int
        :param _DetailResults: 接口识别样本后返回的详细结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailResults: list of DetailResults
        :param _RiskDetails: 接口识别样本中存在违规账号风险的检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskDetails: list of RiskDetails
        :param _Extra: 扩展字段，用于特定信息返回，不同客户/Biztype下返回信息不同
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _DataId: 请求参数中的DataId
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BizType = None
        self._EvilFlag = None
        self._Label = None
        self._Suggestion = None
        self._Keywords = None
        self._Score = None
        self._DetailResults = None
        self._RiskDetails = None
        self._Extra = None
        self._DataId = None
        self._RequestId = None

    @property
    def BizType(self):
        """您在入参时所填入的Biztype参数
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def EvilFlag(self):
        """数据是否属于恶意类型，0：正常 1：可疑
        :rtype: int
        """
        return self._EvilFlag

    @EvilFlag.setter
    def EvilFlag(self, EvilFlag):
        self._EvilFlag = EvilFlag

    @property
    def Label(self):
        """恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库，以及令人反感、不安全或不适宜的内容类型
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        """建议您拿到判断结果后的执行操作
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Keywords(self):
        """文本命中的关键词信息，用于提示您文本违规的具体原因，可能会返回多个命中的关键词。（如：加我微信）
如返回值为空，Score不为空，即识别结果（Label）是来自于语义模型判断的返回值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Score(self):
        """机器判断当前分类的置信度，取值范围：0.00~100.00。分数越高，表示越有可能属于当前分类。
（如：色情 99.99，则该样本属于色情的置信度非常高。）
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def DetailResults(self):
        """接口识别样本后返回的详细结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DetailResults
        """
        return self._DetailResults

    @DetailResults.setter
    def DetailResults(self, DetailResults):
        self._DetailResults = DetailResults

    @property
    def RiskDetails(self):
        """接口识别样本中存在违规账号风险的检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RiskDetails
        """
        return self._RiskDetails

    @RiskDetails.setter
    def RiskDetails(self, RiskDetails):
        self._RiskDetails = RiskDetails

    @property
    def Extra(self):
        """扩展字段，用于特定信息返回，不同客户/Biztype下返回信息不同
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def DataId(self):
        """请求参数中的DataId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

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
        self._BizType = params.get("BizType")
        self._EvilFlag = params.get("EvilFlag")
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
        self._RequestId = params.get("RequestId")


class TipoffResponse(AbstractModel):
    """举报接口响应数据

    """

    def __init__(self):
        r"""
        :param _ResultCode: 举报结果， "0-举报数据提交成功  99-举报数据提交失败"
        :type ResultCode: int
        :param _ResultMsg: 结果描述
        :type ResultMsg: str
        """
        self._ResultCode = None
        self._ResultMsg = None

    @property
    def ResultCode(self):
        """举报结果， "0-举报数据提交成功  99-举报数据提交失败"
        :rtype: int
        """
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultMsg(self):
        """结果描述
        :rtype: str
        """
        return self._ResultMsg

    @ResultMsg.setter
    def ResultMsg(self, ResultMsg):
        self._ResultMsg = ResultMsg


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._ResultMsg = params.get("ResultMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrendCount(AbstractModel):
    """识别量统计

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总调用量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalHour: 总调用时长
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalHour: int
        :param _PassCount: 通过量
注意：此字段可能返回 null，表示取不到有效值。
        :type PassCount: int
        :param _PassHour: 通过时长
注意：此字段可能返回 null，表示取不到有效值。
        :type PassHour: int
        :param _EvilCount: 违规量
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilCount: int
        :param _EvilHour: 违规时长
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilHour: int
        :param _SuspectCount: 疑似违规量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuspectCount: int
        :param _SuspectHour: 疑似违规时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SuspectHour: int
        :param _Date: 日期
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        """
        self._TotalCount = None
        self._TotalHour = None
        self._PassCount = None
        self._PassHour = None
        self._EvilCount = None
        self._EvilHour = None
        self._SuspectCount = None
        self._SuspectHour = None
        self._Date = None

    @property
    def TotalCount(self):
        """总调用量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalHour(self):
        """总调用时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalHour

    @TotalHour.setter
    def TotalHour(self, TotalHour):
        self._TotalHour = TotalHour

    @property
    def PassCount(self):
        """通过量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PassCount

    @PassCount.setter
    def PassCount(self, PassCount):
        self._PassCount = PassCount

    @property
    def PassHour(self):
        """通过时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PassHour

    @PassHour.setter
    def PassHour(self, PassHour):
        self._PassHour = PassHour

    @property
    def EvilCount(self):
        """违规量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

    @property
    def EvilHour(self):
        """违规时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EvilHour

    @EvilHour.setter
    def EvilHour(self, EvilHour):
        self._EvilHour = EvilHour

    @property
    def SuspectCount(self):
        """疑似违规量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuspectCount

    @SuspectCount.setter
    def SuspectCount(self, SuspectCount):
        self._SuspectCount = SuspectCount

    @property
    def SuspectHour(self):
        """疑似违规时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuspectHour

    @SuspectHour.setter
    def SuspectHour(self, SuspectHour):
        self._SuspectHour = SuspectHour

    @property
    def Date(self):
        """日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalHour = params.get("TotalHour")
        self._PassCount = params.get("PassCount")
        self._PassHour = params.get("PassHour")
        self._EvilCount = params.get("EvilCount")
        self._EvilHour = params.get("EvilHour")
        self._SuspectCount = params.get("SuspectCount")
        self._SuspectHour = params.get("SuspectHour")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户相关信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户账号ID，如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :type UserId: str
        :param _Nickname: 用户昵称
        :type Nickname: str
        :param _AccountType: 账号类别，"1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :type AccountType: int
        :param _Gender: 性别 默认0 未知 1 男性 2 女性
        :type Gender: int
        :param _Age: 年龄 默认0 未知
        :type Age: int
        :param _Level: 用户等级，默认0 未知 1 低 2 中 3 高
        :type Level: int
        :param _Phone: 手机号
        :type Phone: str
        """
        self._UserId = None
        self._Nickname = None
        self._AccountType = None
        self._Gender = None
        self._Age = None
        self._Level = None
        self._Phone = None

    @property
    def UserId(self):
        """用户账号ID，如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

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
    def AccountType(self):
        """账号类别，"1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Gender(self):
        """性别 默认0 未知 1 男性 2 女性
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        """年龄 默认0 未知
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Level(self):
        """用户等级，默认0 未知 1 低 2 中 3 高
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Phone(self):
        """手机号
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Nickname = params.get("Nickname")
        self._AccountType = params.get("AccountType")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._Level = params.get("Level")
        self._Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        