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


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 自动化规则名称
        :type Name: str
        :param _Type: 规则类型：用量类(101 当月|102有效期内)、位置类(201行政区|202移动距离)、网络质量类(301网络盲点)
        :type Type: int
        :param _IsActive: 是否激活
        :type IsActive: bool
        :param _Notice: 触发动作：1 邮件 2 API请求 3 微信 4 停卡 5 地图标识为盲点
        :type Notice: int
        :param _Email: 邮箱
        :type Email: str
        :param _Url: 推送的API地址
        :type Url: str
        :param _DataThreshold: 用量阈值
        :type DataThreshold: int
        :param _District: 行政区类型：1. 省份 2. 城市 3. 区
        :type District: int
        :param _Distance: 心跳移动距离阈值
        :type Distance: int
        :param _SignalStrength: 信号强度阈值
        :type SignalStrength: int
        :param _LostDay: 盲点时间阈值，天
        :type LostDay: int
        :param _TagIDs: 标签ID集合
        :type TagIDs: list of int
        :param _SalePlan: 资费计划
        :type SalePlan: str
        """
        self._Name = None
        self._Type = None
        self._IsActive = None
        self._Notice = None
        self._Email = None
        self._Url = None
        self._DataThreshold = None
        self._District = None
        self._Distance = None
        self._SignalStrength = None
        self._LostDay = None
        self._TagIDs = None
        self._SalePlan = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsActive(self):
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive

    @property
    def Notice(self):
        return self._Notice

    @Notice.setter
    def Notice(self, Notice):
        self._Notice = Notice

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def DataThreshold(self):
        return self._DataThreshold

    @DataThreshold.setter
    def DataThreshold(self, DataThreshold):
        self._DataThreshold = DataThreshold

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Distance(self):
        return self._Distance

    @Distance.setter
    def Distance(self, Distance):
        self._Distance = Distance

    @property
    def SignalStrength(self):
        return self._SignalStrength

    @SignalStrength.setter
    def SignalStrength(self, SignalStrength):
        self._SignalStrength = SignalStrength

    @property
    def LostDay(self):
        return self._LostDay

    @LostDay.setter
    def LostDay(self, LostDay):
        self._LostDay = LostDay

    @property
    def TagIDs(self):
        return self._TagIDs

    @TagIDs.setter
    def TagIDs(self, TagIDs):
        self._TagIDs = TagIDs

    @property
    def SalePlan(self):
        return self._SalePlan

    @SalePlan.setter
    def SalePlan(self, SalePlan):
        self._SalePlan = SalePlan


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._IsActive = params.get("IsActive")
        self._Notice = params.get("Notice")
        self._Email = params.get("Email")
        self._Url = params.get("Url")
        self._DataThreshold = params.get("DataThreshold")
        self._District = params.get("District")
        self._Distance = params.get("Distance")
        self._SignalStrength = params.get("SignalStrength")
        self._LostDay = params.get("LostDay")
        self._TagIDs = params.get("TagIDs")
        self._SalePlan = params.get("SalePlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

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


class CreateTacticRequest(AbstractModel):
    """CreateTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 策略名称
        :type Name: str
        :param _IsAuto: 是否自动执行
        :type IsAuto: int
        :param _PingInterval: 心跳上报间隔(s)
        :type PingInterval: int
        :param _IsWeak: 是否开启弱信号检测
        :type IsWeak: int
        :param _WeakThreshold: 弱信号阈值（-dbm）
        :type WeakThreshold: int
        :param _IsDelay: 是否开启时延切换
        :type IsDelay: int
        :param _DelayThreshold: 网络时延阈值（ms）
        :type DelayThreshold: int
        :param _IsFake: 是否开启假信号检测
        :type IsFake: int
        :param _FakeIP: 假信号检测IP字符串，用逗号分隔
        :type FakeIP: str
        :param _FakeInterval: 假信号检测间隔（s）
        :type FakeInterval: int
        :param _IsNet: 是否开启网络制式检测
        :type IsNet: int
        :param _Network: 网络回落制式 1 2G、 2 3G 、 3 2/3G
        :type Network: int
        :param _IsMove: 是否开启移动检测
        :type IsMove: int
        :param _IsPriorityTele: 是否开启最优先运营商
        :type IsPriorityTele: int
        :param _PriorityTele: 最优先运营商 1 移动、 2 联通、 3 电信 4 上次在线运营商
        :type PriorityTele: int
        :param _IsBottomTele: 是否开启最不优先运营商
        :type IsBottomTele: int
        :param _BottomTele: 最不优先运营商 1 移动、 2 联通、 3 电信
        :type BottomTele: int
        :param _IsBestSignal: 最优先信号选取策略
        :type IsBestSignal: int
        """
        self._Name = None
        self._IsAuto = None
        self._PingInterval = None
        self._IsWeak = None
        self._WeakThreshold = None
        self._IsDelay = None
        self._DelayThreshold = None
        self._IsFake = None
        self._FakeIP = None
        self._FakeInterval = None
        self._IsNet = None
        self._Network = None
        self._IsMove = None
        self._IsPriorityTele = None
        self._PriorityTele = None
        self._IsBottomTele = None
        self._BottomTele = None
        self._IsBestSignal = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsAuto(self):
        return self._IsAuto

    @IsAuto.setter
    def IsAuto(self, IsAuto):
        self._IsAuto = IsAuto

    @property
    def PingInterval(self):
        return self._PingInterval

    @PingInterval.setter
    def PingInterval(self, PingInterval):
        self._PingInterval = PingInterval

    @property
    def IsWeak(self):
        return self._IsWeak

    @IsWeak.setter
    def IsWeak(self, IsWeak):
        self._IsWeak = IsWeak

    @property
    def WeakThreshold(self):
        return self._WeakThreshold

    @WeakThreshold.setter
    def WeakThreshold(self, WeakThreshold):
        self._WeakThreshold = WeakThreshold

    @property
    def IsDelay(self):
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay

    @property
    def DelayThreshold(self):
        return self._DelayThreshold

    @DelayThreshold.setter
    def DelayThreshold(self, DelayThreshold):
        self._DelayThreshold = DelayThreshold

    @property
    def IsFake(self):
        return self._IsFake

    @IsFake.setter
    def IsFake(self, IsFake):
        self._IsFake = IsFake

    @property
    def FakeIP(self):
        return self._FakeIP

    @FakeIP.setter
    def FakeIP(self, FakeIP):
        self._FakeIP = FakeIP

    @property
    def FakeInterval(self):
        return self._FakeInterval

    @FakeInterval.setter
    def FakeInterval(self, FakeInterval):
        self._FakeInterval = FakeInterval

    @property
    def IsNet(self):
        return self._IsNet

    @IsNet.setter
    def IsNet(self, IsNet):
        self._IsNet = IsNet

    @property
    def Network(self):
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def IsMove(self):
        return self._IsMove

    @IsMove.setter
    def IsMove(self, IsMove):
        self._IsMove = IsMove

    @property
    def IsPriorityTele(self):
        return self._IsPriorityTele

    @IsPriorityTele.setter
    def IsPriorityTele(self, IsPriorityTele):
        self._IsPriorityTele = IsPriorityTele

    @property
    def PriorityTele(self):
        return self._PriorityTele

    @PriorityTele.setter
    def PriorityTele(self, PriorityTele):
        self._PriorityTele = PriorityTele

    @property
    def IsBottomTele(self):
        return self._IsBottomTele

    @IsBottomTele.setter
    def IsBottomTele(self, IsBottomTele):
        self._IsBottomTele = IsBottomTele

    @property
    def BottomTele(self):
        return self._BottomTele

    @BottomTele.setter
    def BottomTele(self, BottomTele):
        self._BottomTele = BottomTele

    @property
    def IsBestSignal(self):
        return self._IsBestSignal

    @IsBestSignal.setter
    def IsBestSignal(self, IsBestSignal):
        self._IsBestSignal = IsBestSignal


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IsAuto = params.get("IsAuto")
        self._PingInterval = params.get("PingInterval")
        self._IsWeak = params.get("IsWeak")
        self._WeakThreshold = params.get("WeakThreshold")
        self._IsDelay = params.get("IsDelay")
        self._DelayThreshold = params.get("DelayThreshold")
        self._IsFake = params.get("IsFake")
        self._FakeIP = params.get("FakeIP")
        self._FakeInterval = params.get("FakeInterval")
        self._IsNet = params.get("IsNet")
        self._Network = params.get("Network")
        self._IsMove = params.get("IsMove")
        self._IsPriorityTele = params.get("IsPriorityTele")
        self._PriorityTele = params.get("PriorityTele")
        self._IsBottomTele = params.get("IsBottomTele")
        self._BottomTele = params.get("BottomTele")
        self._IsBestSignal = params.get("IsBestSignal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTacticResponse(AbstractModel):
    """CreateTactic返回参数结构体

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


class CreateTagRequest(AbstractModel):
    """CreateTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Comment: 备注
        :type Comment: str
        """
        self._Name = None
        self._Comment = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagResponse(AbstractModel):
    """CreateTag返回参数结构体

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


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleID: 自动化规则ID
        :type RuleID: int
        """
        self._RuleID = None

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

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


class DeleteTacticRequest(AbstractModel):
    """DeleteTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TacticID: 策略ID
        :type TacticID: int
        """
        self._TacticID = None

    @property
    def TacticID(self):
        return self._TacticID

    @TacticID.setter
    def TacticID(self, TacticID):
        self._TacticID = TacticID


    def _deserialize(self, params):
        self._TacticID = params.get("TacticID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTacticResponse(AbstractModel):
    """DeleteTactic返回参数结构体

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


class DeleteTagRequest(AbstractModel):
    """DeleteTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagID: 标签ID
        :type TagID: int
        """
        self._TagID = None

    @property
    def TagID(self):
        return self._TagID

    @TagID.setter
    def TagID(self, TagID):
        self._TagID = TagID


    def _deserialize(self, params):
        self._TagID = params.get("TagID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagResponse(AbstractModel):
    """DeleteTag返回参数结构体

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


class DescribeLinkRequest(AbstractModel):
    """DescribeLink请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LinkID: 云兔卡ID
        :type LinkID: int
        :param _UinAccount: 具体的账号
        :type UinAccount: str
        """
        self._LinkID = None
        self._UinAccount = None

    @property
    def LinkID(self):
        return self._LinkID

    @LinkID.setter
    def LinkID(self, LinkID):
        self._LinkID = LinkID

    @property
    def UinAccount(self):
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount


    def _deserialize(self, params):
        self._LinkID = params.get("LinkID")
        self._UinAccount = params.get("UinAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLinkResponse(AbstractModel):
    """DescribeLink返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 云兔连接详细信息
        :type Data: :class:`tencentcloud.hasim.v20210716.models.LinkDetailInfo`
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
            self._Data = LinkDetailInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeLinksRequest(AbstractModel):
    """DescribeLinks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LinkID: 云兔卡ID
        :type LinkID: int
        :param _ICCID: 运营商ICCID
        :type ICCID: str
        :param _IMEI: 设备码
        :type IMEI: str
        :param _Status: 卡片状态
        :type Status: int
        :param _TeleOperator: 运营商 1移动 2联通 3电信
        :type TeleOperator: int
        :param _TagID: 标签ID
        :type TagID: int
        :param _TacticID: 策略ID
        :type TacticID: int
        :param _LinkedState: 设备在线状态 0 未激活 1 在线 2 离线
        :type LinkedState: int
        :param _TagIDs: 标签ID 集合
        :type TagIDs: list of int
        :param _Limit: 翻页大小, 默认翻页大小为10，最大数量为500
        :type Limit: int
        :param _Offset: 翻页起始
        :type Offset: int
        """
        self._LinkID = None
        self._ICCID = None
        self._IMEI = None
        self._Status = None
        self._TeleOperator = None
        self._TagID = None
        self._TacticID = None
        self._LinkedState = None
        self._TagIDs = None
        self._Limit = None
        self._Offset = None

    @property
    def LinkID(self):
        return self._LinkID

    @LinkID.setter
    def LinkID(self, LinkID):
        self._LinkID = LinkID

    @property
    def ICCID(self):
        return self._ICCID

    @ICCID.setter
    def ICCID(self, ICCID):
        self._ICCID = ICCID

    @property
    def IMEI(self):
        return self._IMEI

    @IMEI.setter
    def IMEI(self, IMEI):
        self._IMEI = IMEI

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TeleOperator(self):
        return self._TeleOperator

    @TeleOperator.setter
    def TeleOperator(self, TeleOperator):
        self._TeleOperator = TeleOperator

    @property
    def TagID(self):
        return self._TagID

    @TagID.setter
    def TagID(self, TagID):
        self._TagID = TagID

    @property
    def TacticID(self):
        return self._TacticID

    @TacticID.setter
    def TacticID(self, TacticID):
        self._TacticID = TacticID

    @property
    def LinkedState(self):
        return self._LinkedState

    @LinkedState.setter
    def LinkedState(self, LinkedState):
        self._LinkedState = LinkedState

    @property
    def TagIDs(self):
        return self._TagIDs

    @TagIDs.setter
    def TagIDs(self, TagIDs):
        self._TagIDs = TagIDs

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
        self._LinkID = params.get("LinkID")
        self._ICCID = params.get("ICCID")
        self._IMEI = params.get("IMEI")
        self._Status = params.get("Status")
        self._TeleOperator = params.get("TeleOperator")
        self._TagID = params.get("TagID")
        self._TacticID = params.get("TacticID")
        self._LinkedState = params.get("LinkedState")
        self._TagIDs = params.get("TagIDs")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLinksResponse(AbstractModel):
    """DescribeLinks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 云兔连接响应信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.hasim.v20210716.models.LinkInfos`
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
            self._Data = LinkInfos()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 子订单ID
        :type DealName: str
        :param _AuditStatus: 审批状态 0全部 1通过 2驳回 3待审核
        :type AuditStatus: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _Offset: 翻页偏移
        :type Offset: int
        :param _BeginTime: 开始时间,例如2022-06-30 00:00:00
        :type BeginTime: str
        :param _EndTime: 结束时间,例如2022-06-30 00:00:00
        :type EndTime: str
        """
        self._DealName = None
        self._AuditStatus = None
        self._Limit = None
        self._Offset = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def AuditStatus(self):
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

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

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._AuditStatus = params.get("AuditStatus")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 订单列表
        :type Data: :class:`tencentcloud.hasim.v20210716.models.Orders`
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
            self._Data = Orders()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRuleRequest(AbstractModel):
    """DescribeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleID: 自动化规则ID
        :type RuleID: int
        """
        self._RuleID = None

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleResponse(AbstractModel):
    """DescribeRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 策略信息
        :type Data: :class:`tencentcloud.hasim.v20210716.models.RuleDetail`
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
            self._Data = RuleDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleID: 自动化规则ID
        :type RuleID: int
        :param _RuleIDs: 自动化规则ID
        :type RuleIDs: list of int
        :param _Name: 名称
        :type Name: str
        :param _Type: 类型
        :type Type: int
        :param _IsActive: 是否激活
        :type IsActive: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _Offset: 翻页偏移
        :type Offset: int
        """
        self._RuleID = None
        self._RuleIDs = None
        self._Name = None
        self._Type = None
        self._IsActive = None
        self._Limit = None
        self._Offset = None

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def RuleIDs(self):
        return self._RuleIDs

    @RuleIDs.setter
    def RuleIDs(self, RuleIDs):
        self._RuleIDs = RuleIDs

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsActive(self):
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive

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
        self._RuleID = params.get("RuleID")
        self._RuleIDs = params.get("RuleIDs")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._IsActive = params.get("IsActive")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 自动化规则列表集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.hasim.v20210716.models.RuleInfos`
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
            self._Data = RuleInfos()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTacticRequest(AbstractModel):
    """DescribeTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TacticID: 策略ID
        :type TacticID: int
        """
        self._TacticID = None

    @property
    def TacticID(self):
        return self._TacticID

    @TacticID.setter
    def TacticID(self, TacticID):
        self._TacticID = TacticID


    def _deserialize(self, params):
        self._TacticID = params.get("TacticID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTacticResponse(AbstractModel):
    """DescribeTactic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 策略信息
        :type Data: :class:`tencentcloud.hasim.v20210716.models.Tactic`
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
            self._Data = Tactic()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTacticsRequest(AbstractModel):
    """DescribeTactics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TacticID: 策略ID
        :type TacticID: int
        :param _Name: 策略名称
        :type Name: str
        """
        self._TacticID = None
        self._Name = None

    @property
    def TacticID(self):
        return self._TacticID

    @TacticID.setter
    def TacticID(self, TacticID):
        self._TacticID = TacticID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._TacticID = params.get("TacticID")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTacticsResponse(AbstractModel):
    """DescribeTactics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 策略集合信息
        :type Data: :class:`tencentcloud.hasim.v20210716.models.TacticInfos`
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
            self._Data = TacticInfos()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 标签名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: :class:`tencentcloud.hasim.v20210716.models.TagInfos`
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
            self._Data = TagInfos()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeviceReport(AbstractModel):
    """设备上报信息

    """

    def __init__(self):
        r"""
        :param _Imei: 移动设备ID
        :type Imei: str
        :param _Lng: 经度
注意：此字段可能返回 null，表示取不到有效值。
        :type Lng: str
        :param _Lat: 维度
注意：此字段可能返回 null，表示取不到有效值。
        :type Lat: str
        :param _Lac: 运营商基站ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Lac: str
        :param _Cell: 小区CellID
注意：此字段可能返回 null，表示取不到有效值。
        :type Cell: str
        :param _Iccid: 当前上报运营商ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Iccid: str
        :param _Rss: 信号强度
注意：此字段可能返回 null，表示取不到有效值。
        :type Rss: int
        :param _Tele: 运营商: 1 移动 2 联通 3 电信
注意：此字段可能返回 null，表示取不到有效值。
        :type Tele: int
        :param _Tid: 当前设备策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Tid: int
        :param _Ping: 心跳间隔,单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Ping: int
        :param _Delay: 网络延迟,单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Delay: int
        :param _Log: 高级日志启停状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: int
        :param _DevType: 设备型号
注意：此字段可能返回 null，表示取不到有效值。
        :type DevType: str
        :param _DevModel: 设备型号
注意：此字段可能返回 null，表示取不到有效值。
        :type DevModel: str
        :param _Version: 设备版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _UploadTime: 设备刷新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadTime: str
        :param _Status: 网络环境: 0 正常 1 弱网
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _MonthFirstTime: 每月第一次上报心跳时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthFirstTime: str
        """
        self._Imei = None
        self._Lng = None
        self._Lat = None
        self._Lac = None
        self._Cell = None
        self._Iccid = None
        self._Rss = None
        self._Tele = None
        self._Tid = None
        self._Ping = None
        self._Delay = None
        self._Log = None
        self._DevType = None
        self._DevModel = None
        self._Version = None
        self._UploadTime = None
        self._Status = None
        self._MonthFirstTime = None

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Lng(self):
        return self._Lng

    @Lng.setter
    def Lng(self, Lng):
        self._Lng = Lng

    @property
    def Lat(self):
        return self._Lat

    @Lat.setter
    def Lat(self, Lat):
        self._Lat = Lat

    @property
    def Lac(self):
        return self._Lac

    @Lac.setter
    def Lac(self, Lac):
        self._Lac = Lac

    @property
    def Cell(self):
        return self._Cell

    @Cell.setter
    def Cell(self, Cell):
        self._Cell = Cell

    @property
    def Iccid(self):
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def Rss(self):
        return self._Rss

    @Rss.setter
    def Rss(self, Rss):
        self._Rss = Rss

    @property
    def Tele(self):
        return self._Tele

    @Tele.setter
    def Tele(self, Tele):
        self._Tele = Tele

    @property
    def Tid(self):
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Ping(self):
        return self._Ping

    @Ping.setter
    def Ping(self, Ping):
        self._Ping = Ping

    @property
    def Delay(self):
        return self._Delay

    @Delay.setter
    def Delay(self, Delay):
        self._Delay = Delay

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def DevType(self):
        return self._DevType

    @DevType.setter
    def DevType(self, DevType):
        self._DevType = DevType

    @property
    def DevModel(self):
        return self._DevModel

    @DevModel.setter
    def DevModel(self, DevModel):
        self._DevModel = DevModel

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UploadTime(self):
        return self._UploadTime

    @UploadTime.setter
    def UploadTime(self, UploadTime):
        self._UploadTime = UploadTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MonthFirstTime(self):
        return self._MonthFirstTime

    @MonthFirstTime.setter
    def MonthFirstTime(self, MonthFirstTime):
        self._MonthFirstTime = MonthFirstTime


    def _deserialize(self, params):
        self._Imei = params.get("Imei")
        self._Lng = params.get("Lng")
        self._Lat = params.get("Lat")
        self._Lac = params.get("Lac")
        self._Cell = params.get("Cell")
        self._Iccid = params.get("Iccid")
        self._Rss = params.get("Rss")
        self._Tele = params.get("Tele")
        self._Tid = params.get("Tid")
        self._Ping = params.get("Ping")
        self._Delay = params.get("Delay")
        self._Log = params.get("Log")
        self._DevType = params.get("DevType")
        self._DevModel = params.get("DevModel")
        self._Version = params.get("Version")
        self._UploadTime = params.get("UploadTime")
        self._Status = params.get("Status")
        self._MonthFirstTime = params.get("MonthFirstTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkDetailInfo(AbstractModel):
    """云兔连接详细信息

    """

    def __init__(self):
        r"""
        :param _ID: 云兔连接ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _Status: 卡片状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ActiveTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _DataUse: 数据用量
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUse: float
        :param _AudioUse: 语音用量
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioUse: int
        :param _SmsUse: 短信用量
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsUse: int
        :param _LinkedState: 在线状态 0 未激活 1 在线 2 离线
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkedState: int
        :param _TacticID: 预期策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticID: int
        :param _TacticStatus: 策略下发状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticStatus: int
        :param _TacticExpireTime: 策略下发成功过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticExpireTime: str
        :param _IsActiveLog: 高级日志预期状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActiveLog: bool
        :param _TeleOperator: 运营商 1移动 2联通 3电信
注意：此字段可能返回 null，表示取不到有效值。
        :type TeleOperator: int
        :param _Report: 设备最新上报信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Report: :class:`tencentcloud.hasim.v20210716.models.DeviceReport`
        :param _Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Cards: 运营商ICCID信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Cards: list of TeleOperatorCard
        :param _CardID: 云兔实际卡片ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CardID: str
        """
        self._ID = None
        self._Status = None
        self._ActiveTime = None
        self._ExpireTime = None
        self._DataUse = None
        self._AudioUse = None
        self._SmsUse = None
        self._LinkedState = None
        self._TacticID = None
        self._TacticStatus = None
        self._TacticExpireTime = None
        self._IsActiveLog = None
        self._TeleOperator = None
        self._Report = None
        self._Tags = None
        self._Cards = None
        self._CardID = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ActiveTime(self):
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DataUse(self):
        return self._DataUse

    @DataUse.setter
    def DataUse(self, DataUse):
        self._DataUse = DataUse

    @property
    def AudioUse(self):
        return self._AudioUse

    @AudioUse.setter
    def AudioUse(self, AudioUse):
        self._AudioUse = AudioUse

    @property
    def SmsUse(self):
        return self._SmsUse

    @SmsUse.setter
    def SmsUse(self, SmsUse):
        self._SmsUse = SmsUse

    @property
    def LinkedState(self):
        return self._LinkedState

    @LinkedState.setter
    def LinkedState(self, LinkedState):
        self._LinkedState = LinkedState

    @property
    def TacticID(self):
        return self._TacticID

    @TacticID.setter
    def TacticID(self, TacticID):
        self._TacticID = TacticID

    @property
    def TacticStatus(self):
        return self._TacticStatus

    @TacticStatus.setter
    def TacticStatus(self, TacticStatus):
        self._TacticStatus = TacticStatus

    @property
    def TacticExpireTime(self):
        return self._TacticExpireTime

    @TacticExpireTime.setter
    def TacticExpireTime(self, TacticExpireTime):
        self._TacticExpireTime = TacticExpireTime

    @property
    def IsActiveLog(self):
        return self._IsActiveLog

    @IsActiveLog.setter
    def IsActiveLog(self, IsActiveLog):
        self._IsActiveLog = IsActiveLog

    @property
    def TeleOperator(self):
        return self._TeleOperator

    @TeleOperator.setter
    def TeleOperator(self, TeleOperator):
        self._TeleOperator = TeleOperator

    @property
    def Report(self):
        return self._Report

    @Report.setter
    def Report(self, Report):
        self._Report = Report

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Cards(self):
        return self._Cards

    @Cards.setter
    def Cards(self, Cards):
        self._Cards = Cards

    @property
    def CardID(self):
        return self._CardID

    @CardID.setter
    def CardID(self, CardID):
        self._CardID = CardID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Status = params.get("Status")
        self._ActiveTime = params.get("ActiveTime")
        self._ExpireTime = params.get("ExpireTime")
        self._DataUse = params.get("DataUse")
        self._AudioUse = params.get("AudioUse")
        self._SmsUse = params.get("SmsUse")
        self._LinkedState = params.get("LinkedState")
        self._TacticID = params.get("TacticID")
        self._TacticStatus = params.get("TacticStatus")
        self._TacticExpireTime = params.get("TacticExpireTime")
        self._IsActiveLog = params.get("IsActiveLog")
        self._TeleOperator = params.get("TeleOperator")
        if params.get("Report") is not None:
            self._Report = DeviceReport()
            self._Report._deserialize(params.get("Report"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Cards") is not None:
            self._Cards = []
            for item in params.get("Cards"):
                obj = TeleOperatorCard()
                obj._deserialize(item)
                self._Cards.append(obj)
        self._CardID = params.get("CardID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkInfo(AbstractModel):
    """云兔连接基本信息

    """

    def __init__(self):
        r"""
        :param _ID: 云兔连接ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _Status: 卡片状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ActiveTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _DataUse: 数据用量
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUse: float
        :param _AudioUse: 语音用量
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioUse: int
        :param _SmsUse: 短信用量
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsUse: int
        :param _LinkedState: 在线状态 0 未激活 1 在线 2 离线
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkedState: int
        :param _TacticID: 预期策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticID: int
        :param _TacticStatus: 策略下发状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticStatus: int
        :param _TacticExpireTime: 策略下发成功过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticExpireTime: str
        :param _IsActiveLog: 高级日志预期状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActiveLog: bool
        :param _TeleOperator: 运营商 1移动 2联通 3电信
注意：此字段可能返回 null，表示取不到有效值。
        :type TeleOperator: int
        :param _Report: 设备最新上报信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Report: :class:`tencentcloud.hasim.v20210716.models.DeviceReport`
        """
        self._ID = None
        self._Status = None
        self._ActiveTime = None
        self._ExpireTime = None
        self._DataUse = None
        self._AudioUse = None
        self._SmsUse = None
        self._LinkedState = None
        self._TacticID = None
        self._TacticStatus = None
        self._TacticExpireTime = None
        self._IsActiveLog = None
        self._TeleOperator = None
        self._Report = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ActiveTime(self):
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DataUse(self):
        return self._DataUse

    @DataUse.setter
    def DataUse(self, DataUse):
        self._DataUse = DataUse

    @property
    def AudioUse(self):
        return self._AudioUse

    @AudioUse.setter
    def AudioUse(self, AudioUse):
        self._AudioUse = AudioUse

    @property
    def SmsUse(self):
        return self._SmsUse

    @SmsUse.setter
    def SmsUse(self, SmsUse):
        self._SmsUse = SmsUse

    @property
    def LinkedState(self):
        return self._LinkedState

    @LinkedState.setter
    def LinkedState(self, LinkedState):
        self._LinkedState = LinkedState

    @property
    def TacticID(self):
        return self._TacticID

    @TacticID.setter
    def TacticID(self, TacticID):
        self._TacticID = TacticID

    @property
    def TacticStatus(self):
        return self._TacticStatus

    @TacticStatus.setter
    def TacticStatus(self, TacticStatus):
        self._TacticStatus = TacticStatus

    @property
    def TacticExpireTime(self):
        return self._TacticExpireTime

    @TacticExpireTime.setter
    def TacticExpireTime(self, TacticExpireTime):
        self._TacticExpireTime = TacticExpireTime

    @property
    def IsActiveLog(self):
        return self._IsActiveLog

    @IsActiveLog.setter
    def IsActiveLog(self, IsActiveLog):
        self._IsActiveLog = IsActiveLog

    @property
    def TeleOperator(self):
        return self._TeleOperator

    @TeleOperator.setter
    def TeleOperator(self, TeleOperator):
        self._TeleOperator = TeleOperator

    @property
    def Report(self):
        return self._Report

    @Report.setter
    def Report(self, Report):
        self._Report = Report


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Status = params.get("Status")
        self._ActiveTime = params.get("ActiveTime")
        self._ExpireTime = params.get("ExpireTime")
        self._DataUse = params.get("DataUse")
        self._AudioUse = params.get("AudioUse")
        self._SmsUse = params.get("SmsUse")
        self._LinkedState = params.get("LinkedState")
        self._TacticID = params.get("TacticID")
        self._TacticStatus = params.get("TacticStatus")
        self._TacticExpireTime = params.get("TacticExpireTime")
        self._IsActiveLog = params.get("IsActiveLog")
        self._TeleOperator = params.get("TeleOperator")
        if params.get("Report") is not None:
            self._Report = DeviceReport()
            self._Report._deserialize(params.get("Report"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkInfos(AbstractModel):
    """云兔连接信息集合

    """

    def __init__(self):
        r"""
        :param _Total: 总量
        :type Total: int
        :param _List: 云兔连接列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of LinkInfo
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = LinkInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLinkAdvancedLogRequest(AbstractModel):
    """ModifyLinkAdvancedLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LinkID: 云兔ID
        :type LinkID: int
        :param _IsAdLog: 是否激活高级日志 0 关闭 1激活
        :type IsAdLog: int
        """
        self._LinkID = None
        self._IsAdLog = None

    @property
    def LinkID(self):
        return self._LinkID

    @LinkID.setter
    def LinkID(self, LinkID):
        self._LinkID = LinkID

    @property
    def IsAdLog(self):
        return self._IsAdLog

    @IsAdLog.setter
    def IsAdLog(self, IsAdLog):
        self._IsAdLog = IsAdLog


    def _deserialize(self, params):
        self._LinkID = params.get("LinkID")
        self._IsAdLog = params.get("IsAdLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLinkAdvancedLogResponse(AbstractModel):
    """ModifyLinkAdvancedLog返回参数结构体

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


class ModifyLinkTacticRequest(AbstractModel):
    """ModifyLinkTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LinkID: 云兔ID
        :type LinkID: int
        :param _TacticID: 策略ID
        :type TacticID: int
        """
        self._LinkID = None
        self._TacticID = None

    @property
    def LinkID(self):
        return self._LinkID

    @LinkID.setter
    def LinkID(self, LinkID):
        self._LinkID = LinkID

    @property
    def TacticID(self):
        return self._TacticID

    @TacticID.setter
    def TacticID(self, TacticID):
        self._TacticID = TacticID


    def _deserialize(self, params):
        self._LinkID = params.get("LinkID")
        self._TacticID = params.get("TacticID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLinkTacticResponse(AbstractModel):
    """ModifyLinkTactic返回参数结构体

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


class ModifyLinkTeleRequest(AbstractModel):
    """ModifyLinkTele请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LinkID: 云兔ID
        :type LinkID: int
        :param _TeleOperator: 运营商 1 移动 2 联通 3 电信
        :type TeleOperator: int
        """
        self._LinkID = None
        self._TeleOperator = None

    @property
    def LinkID(self):
        return self._LinkID

    @LinkID.setter
    def LinkID(self, LinkID):
        self._LinkID = LinkID

    @property
    def TeleOperator(self):
        return self._TeleOperator

    @TeleOperator.setter
    def TeleOperator(self, TeleOperator):
        self._TeleOperator = TeleOperator


    def _deserialize(self, params):
        self._LinkID = params.get("LinkID")
        self._TeleOperator = params.get("TeleOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLinkTeleResponse(AbstractModel):
    """ModifyLinkTele返回参数结构体

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


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 自动化规则名称
        :type Name: str
        :param _Type: 规则类型：用量类(101 当月|102有效期内)、位置类(201行政区|202移动距离)、网络质量类(301网络盲点)
        :type Type: int
        :param _IsActive: 是否激活
        :type IsActive: bool
        :param _Notice: 触发动作：1 邮件 2 API请求 3 微信 4 停卡 5 地图标识为盲点
        :type Notice: int
        :param _RuleID: 自动化规则ID
        :type RuleID: int
        :param _Email: 邮箱
        :type Email: str
        :param _Url: 推送的API地址
        :type Url: str
        :param _DataThreshold: 用量阈值
        :type DataThreshold: int
        :param _District: 行政区类型：1. 省份 2. 城市 3. 区
        :type District: int
        :param _Distance: 心跳移动距离阈值
        :type Distance: int
        :param _SignalStrength: 信号强度阈值
        :type SignalStrength: int
        :param _TagIDs: 标签ID集合
        :type TagIDs: list of int
        :param _SalePlan: 资费计划
        :type SalePlan: str
        :param _UinAccount: 具体的账号
        :type UinAccount: str
        """
        self._Name = None
        self._Type = None
        self._IsActive = None
        self._Notice = None
        self._RuleID = None
        self._Email = None
        self._Url = None
        self._DataThreshold = None
        self._District = None
        self._Distance = None
        self._SignalStrength = None
        self._TagIDs = None
        self._SalePlan = None
        self._UinAccount = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsActive(self):
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive

    @property
    def Notice(self):
        return self._Notice

    @Notice.setter
    def Notice(self, Notice):
        self._Notice = Notice

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def DataThreshold(self):
        return self._DataThreshold

    @DataThreshold.setter
    def DataThreshold(self, DataThreshold):
        self._DataThreshold = DataThreshold

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Distance(self):
        return self._Distance

    @Distance.setter
    def Distance(self, Distance):
        self._Distance = Distance

    @property
    def SignalStrength(self):
        return self._SignalStrength

    @SignalStrength.setter
    def SignalStrength(self, SignalStrength):
        self._SignalStrength = SignalStrength

    @property
    def TagIDs(self):
        return self._TagIDs

    @TagIDs.setter
    def TagIDs(self, TagIDs):
        self._TagIDs = TagIDs

    @property
    def SalePlan(self):
        return self._SalePlan

    @SalePlan.setter
    def SalePlan(self, SalePlan):
        self._SalePlan = SalePlan

    @property
    def UinAccount(self):
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._IsActive = params.get("IsActive")
        self._Notice = params.get("Notice")
        self._RuleID = params.get("RuleID")
        self._Email = params.get("Email")
        self._Url = params.get("Url")
        self._DataThreshold = params.get("DataThreshold")
        self._District = params.get("District")
        self._Distance = params.get("Distance")
        self._SignalStrength = params.get("SignalStrength")
        self._TagIDs = params.get("TagIDs")
        self._SalePlan = params.get("SalePlan")
        self._UinAccount = params.get("UinAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回参数结构体

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


class ModifyRuleStatusRequest(AbstractModel):
    """ModifyRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleID: 自动化规则ID
        :type RuleID: int
        :param _IsActive: 是否激活
        :type IsActive: bool
        """
        self._RuleID = None
        self._IsActive = None

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def IsActive(self):
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        self._IsActive = params.get("IsActive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleStatusResponse(AbstractModel):
    """ModifyRuleStatus返回参数结构体

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


class ModifyTacticRequest(AbstractModel):
    """ModifyTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 策略名称
        :type Name: str
        :param _IsAuto: 是否自动执行
        :type IsAuto: int
        :param _PingInterval: 心跳上报间隔(s)
        :type PingInterval: int
        :param _IsWeak: 是否开启弱信号检测
        :type IsWeak: int
        :param _WeakThreshold: 弱信号阈值（-dbm）
        :type WeakThreshold: int
        :param _IsDelay: 是否开启时延切换
        :type IsDelay: int
        :param _DelayThreshold: 网络时延阈值（ms）
        :type DelayThreshold: int
        :param _IsFake: 是否开启假信号检测
        :type IsFake: int
        :param _FakeInterval: 假信号检测间隔（s）
        :type FakeInterval: int
        :param _IsNet: 是否开启网络制式检测
        :type IsNet: int
        :param _Network: 网络回落制式 1 2G、 2 3G 、 3 2/3G
        :type Network: int
        :param _IsMove: 是否开启移动检测
        :type IsMove: int
        :param _TacticID: 策略ID
        :type TacticID: int
        :param _IsPriorityTele: 是否开启最优先运营商
        :type IsPriorityTele: int
        :param _PriorityTele: 最优先运营商 1 移动、 2 联通、 3 电信 4 上次在线运营商
        :type PriorityTele: int
        :param _IsBottomTele: 是否开启最不优先运营商
        :type IsBottomTele: int
        :param _BottomTele: 最不优先运营商 1 移动、 2 联通、 3 电信
        :type BottomTele: int
        :param _IsBestSignal: 是否最优先信号选取策略
        :type IsBestSignal: int
        :param _FakeIP: 假信号检测IP字符串，用逗号分隔
        :type FakeIP: str
        """
        self._Name = None
        self._IsAuto = None
        self._PingInterval = None
        self._IsWeak = None
        self._WeakThreshold = None
        self._IsDelay = None
        self._DelayThreshold = None
        self._IsFake = None
        self._FakeInterval = None
        self._IsNet = None
        self._Network = None
        self._IsMove = None
        self._TacticID = None
        self._IsPriorityTele = None
        self._PriorityTele = None
        self._IsBottomTele = None
        self._BottomTele = None
        self._IsBestSignal = None
        self._FakeIP = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsAuto(self):
        return self._IsAuto

    @IsAuto.setter
    def IsAuto(self, IsAuto):
        self._IsAuto = IsAuto

    @property
    def PingInterval(self):
        return self._PingInterval

    @PingInterval.setter
    def PingInterval(self, PingInterval):
        self._PingInterval = PingInterval

    @property
    def IsWeak(self):
        return self._IsWeak

    @IsWeak.setter
    def IsWeak(self, IsWeak):
        self._IsWeak = IsWeak

    @property
    def WeakThreshold(self):
        return self._WeakThreshold

    @WeakThreshold.setter
    def WeakThreshold(self, WeakThreshold):
        self._WeakThreshold = WeakThreshold

    @property
    def IsDelay(self):
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay

    @property
    def DelayThreshold(self):
        return self._DelayThreshold

    @DelayThreshold.setter
    def DelayThreshold(self, DelayThreshold):
        self._DelayThreshold = DelayThreshold

    @property
    def IsFake(self):
        return self._IsFake

    @IsFake.setter
    def IsFake(self, IsFake):
        self._IsFake = IsFake

    @property
    def FakeInterval(self):
        return self._FakeInterval

    @FakeInterval.setter
    def FakeInterval(self, FakeInterval):
        self._FakeInterval = FakeInterval

    @property
    def IsNet(self):
        return self._IsNet

    @IsNet.setter
    def IsNet(self, IsNet):
        self._IsNet = IsNet

    @property
    def Network(self):
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def IsMove(self):
        return self._IsMove

    @IsMove.setter
    def IsMove(self, IsMove):
        self._IsMove = IsMove

    @property
    def TacticID(self):
        return self._TacticID

    @TacticID.setter
    def TacticID(self, TacticID):
        self._TacticID = TacticID

    @property
    def IsPriorityTele(self):
        return self._IsPriorityTele

    @IsPriorityTele.setter
    def IsPriorityTele(self, IsPriorityTele):
        self._IsPriorityTele = IsPriorityTele

    @property
    def PriorityTele(self):
        return self._PriorityTele

    @PriorityTele.setter
    def PriorityTele(self, PriorityTele):
        self._PriorityTele = PriorityTele

    @property
    def IsBottomTele(self):
        return self._IsBottomTele

    @IsBottomTele.setter
    def IsBottomTele(self, IsBottomTele):
        self._IsBottomTele = IsBottomTele

    @property
    def BottomTele(self):
        return self._BottomTele

    @BottomTele.setter
    def BottomTele(self, BottomTele):
        self._BottomTele = BottomTele

    @property
    def IsBestSignal(self):
        return self._IsBestSignal

    @IsBestSignal.setter
    def IsBestSignal(self, IsBestSignal):
        self._IsBestSignal = IsBestSignal

    @property
    def FakeIP(self):
        return self._FakeIP

    @FakeIP.setter
    def FakeIP(self, FakeIP):
        self._FakeIP = FakeIP


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IsAuto = params.get("IsAuto")
        self._PingInterval = params.get("PingInterval")
        self._IsWeak = params.get("IsWeak")
        self._WeakThreshold = params.get("WeakThreshold")
        self._IsDelay = params.get("IsDelay")
        self._DelayThreshold = params.get("DelayThreshold")
        self._IsFake = params.get("IsFake")
        self._FakeInterval = params.get("FakeInterval")
        self._IsNet = params.get("IsNet")
        self._Network = params.get("Network")
        self._IsMove = params.get("IsMove")
        self._TacticID = params.get("TacticID")
        self._IsPriorityTele = params.get("IsPriorityTele")
        self._PriorityTele = params.get("PriorityTele")
        self._IsBottomTele = params.get("IsBottomTele")
        self._BottomTele = params.get("BottomTele")
        self._IsBestSignal = params.get("IsBestSignal")
        self._FakeIP = params.get("FakeIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTacticResponse(AbstractModel):
    """ModifyTactic返回参数结构体

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


class ModifyTagRequest(AbstractModel):
    """ModifyTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _TagID: 标签ID
        :type TagID: int
        :param _Comment: 备注
        :type Comment: str
        """
        self._Name = None
        self._TagID = None
        self._Comment = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TagID(self):
        return self._TagID

    @TagID.setter
    def TagID(self, TagID):
        self._TagID = TagID

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TagID = params.get("TagID")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTagResponse(AbstractModel):
    """ModifyTag返回参数结构体

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


class OrderInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        r"""
        :param _DealName: 子订单ID
        :type DealName: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _Uin: 订单账户
        :type Uin: str
        :param _BuyNum: 购买数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BuyNum: int
        :param _IndustryCode: 行业代码
注意：此字段可能返回 null，表示取不到有效值。
        :type IndustryCode: str
        :param _Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _Contact: 联系人
注意：此字段可能返回 null，表示取不到有效值。
        :type Contact: str
        :param _Msisdn: 电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param _Specification: 卡片规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param _Comment: 用户订单备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _BigDealId: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealId: str
        :param _AuditStatus: 审批状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditStatus: str
        :param _FlowStatus: 发货状态
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowStatus: str
        :param _Remark: 审批备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _RefundBigDealId: 退费订单
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundBigDealId: str
        """
        self._DealName = None
        self._CreatedAt = None
        self._Uin = None
        self._BuyNum = None
        self._IndustryCode = None
        self._Address = None
        self._Contact = None
        self._Msisdn = None
        self._Specification = None
        self._Comment = None
        self._BigDealId = None
        self._AuditStatus = None
        self._FlowStatus = None
        self._Remark = None
        self._RefundBigDealId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def BuyNum(self):
        return self._BuyNum

    @BuyNum.setter
    def BuyNum(self, BuyNum):
        self._BuyNum = BuyNum

    @property
    def IndustryCode(self):
        return self._IndustryCode

    @IndustryCode.setter
    def IndustryCode(self, IndustryCode):
        self._IndustryCode = IndustryCode

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Contact(self):
        return self._Contact

    @Contact.setter
    def Contact(self, Contact):
        self._Contact = Contact

    @property
    def Msisdn(self):
        return self._Msisdn

    @Msisdn.setter
    def Msisdn(self, Msisdn):
        self._Msisdn = Msisdn

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def BigDealId(self):
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def AuditStatus(self):
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def FlowStatus(self):
        return self._FlowStatus

    @FlowStatus.setter
    def FlowStatus(self, FlowStatus):
        self._FlowStatus = FlowStatus

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RefundBigDealId(self):
        return self._RefundBigDealId

    @RefundBigDealId.setter
    def RefundBigDealId(self, RefundBigDealId):
        self._RefundBigDealId = RefundBigDealId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._CreatedAt = params.get("CreatedAt")
        self._Uin = params.get("Uin")
        self._BuyNum = params.get("BuyNum")
        self._IndustryCode = params.get("IndustryCode")
        self._Address = params.get("Address")
        self._Contact = params.get("Contact")
        self._Msisdn = params.get("Msisdn")
        self._Specification = params.get("Specification")
        self._Comment = params.get("Comment")
        self._BigDealId = params.get("BigDealId")
        self._AuditStatus = params.get("AuditStatus")
        self._FlowStatus = params.get("FlowStatus")
        self._Remark = params.get("Remark")
        self._RefundBigDealId = params.get("RefundBigDealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Orders(AbstractModel):
    """订单列表

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 订单集合
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of OrderInfo
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = OrderInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewLinkInfoRequest(AbstractModel):
    """RenewLinkInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LinkID: 云兔ID
        :type LinkID: int
        :param _UinAccount: 具体的账号
        :type UinAccount: str
        """
        self._LinkID = None
        self._UinAccount = None

    @property
    def LinkID(self):
        return self._LinkID

    @LinkID.setter
    def LinkID(self, LinkID):
        self._LinkID = LinkID

    @property
    def UinAccount(self):
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount


    def _deserialize(self, params):
        self._LinkID = params.get("LinkID")
        self._UinAccount = params.get("UinAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewLinkInfoResponse(AbstractModel):
    """RenewLinkInfo返回参数结构体

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


class Rule(AbstractModel):
    """自动化规则

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _ID: 规则ID
        :type ID: int
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _DeletedAt: 删除时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletedAt: str
        :param _Type: 规则类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _IsActive: 是否激活
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActive: bool
        :param _Notice: 触发动作：1 邮件 2 API请求 5 停卡 6 地图标识为盲点
注意：此字段可能返回 null，表示取不到有效值。
        :type Notice: int
        :param _Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Url: 回调API地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _DataThreshold: 用量类：用量阈值,单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :type DataThreshold: int
        :param _District: 行政区类型：1. 省份 2. 城市 3. 区
注意：此字段可能返回 null，表示取不到有效值。
        :type District: int
        :param _Distance: 移动距离阈值，单位KM
注意：此字段可能返回 null，表示取不到有效值。
        :type Distance: int
        :param _SignalStrength: 信号强度阈值(-dbm）
注意：此字段可能返回 null，表示取不到有效值。
        :type SignalStrength: int
        :param _LostDay: 盲点阈值天数
注意：此字段可能返回 null，表示取不到有效值。
        :type LostDay: int
        :param _TagIDs: 绑定的标签ID集合
注意：此字段可能返回 null，表示取不到有效值。
        :type TagIDs: list of int non-negative
        :param _SalePlan: 绑定的资费计划
注意：此字段可能返回 null，表示取不到有效值。
        :type SalePlan: str
        """
        self._Name = None
        self._ID = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._DeletedAt = None
        self._Type = None
        self._IsActive = None
        self._Notice = None
        self._Email = None
        self._Url = None
        self._DataThreshold = None
        self._District = None
        self._Distance = None
        self._SignalStrength = None
        self._LostDay = None
        self._TagIDs = None
        self._SalePlan = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def DeletedAt(self):
        return self._DeletedAt

    @DeletedAt.setter
    def DeletedAt(self, DeletedAt):
        self._DeletedAt = DeletedAt

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsActive(self):
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive

    @property
    def Notice(self):
        return self._Notice

    @Notice.setter
    def Notice(self, Notice):
        self._Notice = Notice

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def DataThreshold(self):
        return self._DataThreshold

    @DataThreshold.setter
    def DataThreshold(self, DataThreshold):
        self._DataThreshold = DataThreshold

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Distance(self):
        return self._Distance

    @Distance.setter
    def Distance(self, Distance):
        self._Distance = Distance

    @property
    def SignalStrength(self):
        return self._SignalStrength

    @SignalStrength.setter
    def SignalStrength(self, SignalStrength):
        self._SignalStrength = SignalStrength

    @property
    def LostDay(self):
        return self._LostDay

    @LostDay.setter
    def LostDay(self, LostDay):
        self._LostDay = LostDay

    @property
    def TagIDs(self):
        return self._TagIDs

    @TagIDs.setter
    def TagIDs(self, TagIDs):
        self._TagIDs = TagIDs

    @property
    def SalePlan(self):
        return self._SalePlan

    @SalePlan.setter
    def SalePlan(self, SalePlan):
        self._SalePlan = SalePlan


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ID = params.get("ID")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._DeletedAt = params.get("DeletedAt")
        self._Type = params.get("Type")
        self._IsActive = params.get("IsActive")
        self._Notice = params.get("Notice")
        self._Email = params.get("Email")
        self._Url = params.get("Url")
        self._DataThreshold = params.get("DataThreshold")
        self._District = params.get("District")
        self._Distance = params.get("Distance")
        self._SignalStrength = params.get("SignalStrength")
        self._LostDay = params.get("LostDay")
        self._TagIDs = params.get("TagIDs")
        self._SalePlan = params.get("SalePlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleDetail(AbstractModel):
    """自动化规则详细信息

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _ID: 规则ID
        :type ID: int
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _DeletedAt: 删除时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletedAt: str
        :param _Type: 规则类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _IsActive: 是否激活
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActive: bool
        :param _Notice: 触发动作：1 邮件 2 API请求 5 停卡 6 地图标识为盲点
注意：此字段可能返回 null，表示取不到有效值。
        :type Notice: int
        :param _Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Url: 回调API地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _DataThreshold: 用量类：用量阈值,单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :type DataThreshold: int
        :param _District: 行政区类型：1. 省份 2. 城市 3. 区
注意：此字段可能返回 null，表示取不到有效值。
        :type District: int
        :param _Distance: 移动距离阈值，单位KM
注意：此字段可能返回 null，表示取不到有效值。
        :type Distance: int
        :param _SignalStrength: 信号强度阈值(-dbm）
注意：此字段可能返回 null，表示取不到有效值。
        :type SignalStrength: int
        :param _LostDay: 盲点阈值天数
注意：此字段可能返回 null，表示取不到有效值。
        :type LostDay: int
        :param _TagIDs: 标签ID集合
注意：此字段可能返回 null，表示取不到有效值。
        :type TagIDs: list of int
        :param _SalePlan: 资费信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SalePlan: str
        """
        self._Name = None
        self._ID = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._DeletedAt = None
        self._Type = None
        self._IsActive = None
        self._Notice = None
        self._Email = None
        self._Url = None
        self._DataThreshold = None
        self._District = None
        self._Distance = None
        self._SignalStrength = None
        self._LostDay = None
        self._TagIDs = None
        self._SalePlan = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def DeletedAt(self):
        return self._DeletedAt

    @DeletedAt.setter
    def DeletedAt(self, DeletedAt):
        self._DeletedAt = DeletedAt

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsActive(self):
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive

    @property
    def Notice(self):
        return self._Notice

    @Notice.setter
    def Notice(self, Notice):
        self._Notice = Notice

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def DataThreshold(self):
        return self._DataThreshold

    @DataThreshold.setter
    def DataThreshold(self, DataThreshold):
        self._DataThreshold = DataThreshold

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Distance(self):
        return self._Distance

    @Distance.setter
    def Distance(self, Distance):
        self._Distance = Distance

    @property
    def SignalStrength(self):
        return self._SignalStrength

    @SignalStrength.setter
    def SignalStrength(self, SignalStrength):
        self._SignalStrength = SignalStrength

    @property
    def LostDay(self):
        return self._LostDay

    @LostDay.setter
    def LostDay(self, LostDay):
        self._LostDay = LostDay

    @property
    def TagIDs(self):
        return self._TagIDs

    @TagIDs.setter
    def TagIDs(self, TagIDs):
        self._TagIDs = TagIDs

    @property
    def SalePlan(self):
        return self._SalePlan

    @SalePlan.setter
    def SalePlan(self, SalePlan):
        self._SalePlan = SalePlan


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ID = params.get("ID")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._DeletedAt = params.get("DeletedAt")
        self._Type = params.get("Type")
        self._IsActive = params.get("IsActive")
        self._Notice = params.get("Notice")
        self._Email = params.get("Email")
        self._Url = params.get("Url")
        self._DataThreshold = params.get("DataThreshold")
        self._District = params.get("District")
        self._Distance = params.get("Distance")
        self._SignalStrength = params.get("SignalStrength")
        self._LostDay = params.get("LostDay")
        self._TagIDs = params.get("TagIDs")
        self._SalePlan = params.get("SalePlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfos(AbstractModel):
    """自动化规则集合

    """

    def __init__(self):
        r"""
        :param _Total: 总量
        :type Total: int
        :param _List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Rule
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Rule()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tactic(AbstractModel):
    """策略信息

    """

    def __init__(self):
        r"""
        :param _ID: 策略ID
        :type ID: int
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _IsAuto: 是否自动执行策略
        :type IsAuto: int
        :param _PingInterval: 设备上报信息间隔
注意：此字段可能返回 null，表示取不到有效值。
        :type PingInterval: int
        :param _IsWeak: 是否开启弱信号检查
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWeak: int
        :param _WeakThreshold: 弱信号阈值（-dbm）
注意：此字段可能返回 null，表示取不到有效值。
        :type WeakThreshold: int
        :param _IsDelay: 忘了时延切换
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDelay: int
        :param _DelayThreshold: 时延阈值（ms）
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayThreshold: int
        :param _IsFake: 是否开启假信号检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFake: int
        :param _FakeIP: 假信号检测IP字符串，用逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeIP: str
        :param _FakeInterval: 假信号检测间隔（s）
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeInterval: int
        :param _IsNet: 是否开启网络制式检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNet: int
        :param _Network: 网络回落制式 1: 2G、 2: 3G 、 3: 2/3G
注意：此字段可能返回 null，表示取不到有效值。
        :type Network: int
        :param _IsMove: 是否开启移动检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMove: int
        :param _Name: 策略名称
        :type Name: str
        :param _IsPriorityTele: 是否开启最优先运营商
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPriorityTele: int
        :param _PriorityTele: 最优先运营商 1 移动、 2 联通、 3 电信 4 上次在线运营商
注意：此字段可能返回 null，表示取不到有效值。
        :type PriorityTele: int
        :param _IsBottomTele: 是否开启最不优先运营商
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBottomTele: int
        :param _BottomTele: 最不优先运营商 1 移动、 2 联通、 3 电信
注意：此字段可能返回 null，表示取不到有效值。
        :type BottomTele: int
        :param _IsBestSignal: 是否开启最优先信号选取策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBestSignal: int
        """
        self._ID = None
        self._CreatedAt = None
        self._IsAuto = None
        self._PingInterval = None
        self._IsWeak = None
        self._WeakThreshold = None
        self._IsDelay = None
        self._DelayThreshold = None
        self._IsFake = None
        self._FakeIP = None
        self._FakeInterval = None
        self._IsNet = None
        self._Network = None
        self._IsMove = None
        self._Name = None
        self._IsPriorityTele = None
        self._PriorityTele = None
        self._IsBottomTele = None
        self._BottomTele = None
        self._IsBestSignal = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def IsAuto(self):
        return self._IsAuto

    @IsAuto.setter
    def IsAuto(self, IsAuto):
        self._IsAuto = IsAuto

    @property
    def PingInterval(self):
        return self._PingInterval

    @PingInterval.setter
    def PingInterval(self, PingInterval):
        self._PingInterval = PingInterval

    @property
    def IsWeak(self):
        return self._IsWeak

    @IsWeak.setter
    def IsWeak(self, IsWeak):
        self._IsWeak = IsWeak

    @property
    def WeakThreshold(self):
        return self._WeakThreshold

    @WeakThreshold.setter
    def WeakThreshold(self, WeakThreshold):
        self._WeakThreshold = WeakThreshold

    @property
    def IsDelay(self):
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay

    @property
    def DelayThreshold(self):
        return self._DelayThreshold

    @DelayThreshold.setter
    def DelayThreshold(self, DelayThreshold):
        self._DelayThreshold = DelayThreshold

    @property
    def IsFake(self):
        return self._IsFake

    @IsFake.setter
    def IsFake(self, IsFake):
        self._IsFake = IsFake

    @property
    def FakeIP(self):
        return self._FakeIP

    @FakeIP.setter
    def FakeIP(self, FakeIP):
        self._FakeIP = FakeIP

    @property
    def FakeInterval(self):
        return self._FakeInterval

    @FakeInterval.setter
    def FakeInterval(self, FakeInterval):
        self._FakeInterval = FakeInterval

    @property
    def IsNet(self):
        return self._IsNet

    @IsNet.setter
    def IsNet(self, IsNet):
        self._IsNet = IsNet

    @property
    def Network(self):
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def IsMove(self):
        return self._IsMove

    @IsMove.setter
    def IsMove(self, IsMove):
        self._IsMove = IsMove

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsPriorityTele(self):
        return self._IsPriorityTele

    @IsPriorityTele.setter
    def IsPriorityTele(self, IsPriorityTele):
        self._IsPriorityTele = IsPriorityTele

    @property
    def PriorityTele(self):
        return self._PriorityTele

    @PriorityTele.setter
    def PriorityTele(self, PriorityTele):
        self._PriorityTele = PriorityTele

    @property
    def IsBottomTele(self):
        return self._IsBottomTele

    @IsBottomTele.setter
    def IsBottomTele(self, IsBottomTele):
        self._IsBottomTele = IsBottomTele

    @property
    def BottomTele(self):
        return self._BottomTele

    @BottomTele.setter
    def BottomTele(self, BottomTele):
        self._BottomTele = BottomTele

    @property
    def IsBestSignal(self):
        return self._IsBestSignal

    @IsBestSignal.setter
    def IsBestSignal(self, IsBestSignal):
        self._IsBestSignal = IsBestSignal


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._CreatedAt = params.get("CreatedAt")
        self._IsAuto = params.get("IsAuto")
        self._PingInterval = params.get("PingInterval")
        self._IsWeak = params.get("IsWeak")
        self._WeakThreshold = params.get("WeakThreshold")
        self._IsDelay = params.get("IsDelay")
        self._DelayThreshold = params.get("DelayThreshold")
        self._IsFake = params.get("IsFake")
        self._FakeIP = params.get("FakeIP")
        self._FakeInterval = params.get("FakeInterval")
        self._IsNet = params.get("IsNet")
        self._Network = params.get("Network")
        self._IsMove = params.get("IsMove")
        self._Name = params.get("Name")
        self._IsPriorityTele = params.get("IsPriorityTele")
        self._PriorityTele = params.get("PriorityTele")
        self._IsBottomTele = params.get("IsBottomTele")
        self._BottomTele = params.get("BottomTele")
        self._IsBestSignal = params.get("IsBestSignal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TacticInfos(AbstractModel):
    """策略信息集合

    """

    def __init__(self):
        r"""
        :param _Total: 总量
        :type Total: int
        :param _List: 策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Tactic
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Tactic()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """云兔标签信息

    """

    def __init__(self):
        r"""
        :param _Name: 标签名称
        :type Name: str
        :param _ID: 标签ID
        :type ID: int
        :param _Comment: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self._Name = None
        self._ID = None
        self._Comment = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ID = params.get("ID")
        self._Comment = params.get("Comment")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfos(AbstractModel):
    """标签列表集合

    """

    def __init__(self):
        r"""
        :param _Total: 总量
        :type Total: int
        :param _List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Tag
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Tag()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeleOperatorCard(AbstractModel):
    """运营商卡片信息

    """

    def __init__(self):
        r"""
        :param _AccountTime: 开户时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountTime: str
        :param _ActiveTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: str
        :param _ICCID: 运营商ICCID
        :type ICCID: str
        :param _LinkID: 云兔卡ID
        :type LinkID: int
        :param _Msisdn: 电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param _IMSI: 移动用户识别码
注意：此字段可能返回 null，表示取不到有效值。
        :type IMSI: str
        :param _TeleOperator: 运营商: 1 移动 2 联通 3 电信
        :type TeleOperator: int
        """
        self._AccountTime = None
        self._ActiveTime = None
        self._ICCID = None
        self._LinkID = None
        self._Msisdn = None
        self._IMSI = None
        self._TeleOperator = None

    @property
    def AccountTime(self):
        return self._AccountTime

    @AccountTime.setter
    def AccountTime(self, AccountTime):
        self._AccountTime = AccountTime

    @property
    def ActiveTime(self):
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def ICCID(self):
        return self._ICCID

    @ICCID.setter
    def ICCID(self, ICCID):
        self._ICCID = ICCID

    @property
    def LinkID(self):
        return self._LinkID

    @LinkID.setter
    def LinkID(self, LinkID):
        self._LinkID = LinkID

    @property
    def Msisdn(self):
        return self._Msisdn

    @Msisdn.setter
    def Msisdn(self, Msisdn):
        self._Msisdn = Msisdn

    @property
    def IMSI(self):
        return self._IMSI

    @IMSI.setter
    def IMSI(self, IMSI):
        self._IMSI = IMSI

    @property
    def TeleOperator(self):
        return self._TeleOperator

    @TeleOperator.setter
    def TeleOperator(self, TeleOperator):
        self._TeleOperator = TeleOperator


    def _deserialize(self, params):
        self._AccountTime = params.get("AccountTime")
        self._ActiveTime = params.get("ActiveTime")
        self._ICCID = params.get("ICCID")
        self._LinkID = params.get("LinkID")
        self._Msisdn = params.get("Msisdn")
        self._IMSI = params.get("IMSI")
        self._TeleOperator = params.get("TeleOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        