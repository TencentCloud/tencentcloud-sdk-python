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
        :param Name: 自动化规则名称
        :type Name: str
        :param Type: 规则类型：用量类(101 当月|102有效期内)、位置类(201行政区|202移动距离)、网络质量类(301网络盲点)
        :type Type: int
        :param IsActive: 是否激活
        :type IsActive: bool
        :param Notice: 触发动作：1 邮件 2 API请求 3 微信 4 停卡 5 地图标识为盲点
        :type Notice: int
        :param Email: 邮箱
        :type Email: str
        :param Url: 推送的API地址
        :type Url: str
        :param DataThreshold: 用量阈值
        :type DataThreshold: int
        :param District: 行政区类型：1. 省份 2. 城市 3. 区
        :type District: int
        :param Distance: 心跳移动距离阈值
        :type Distance: int
        :param SignalStrength: 信号强度阈值
        :type SignalStrength: int
        :param LostDay: 盲点时间阈值，天
        :type LostDay: int
        :param TagIDs: 标签ID集合
        :type TagIDs: list of int
        :param SalePlan: 资费计划
        :type SalePlan: str
        """
        self.Name = None
        self.Type = None
        self.IsActive = None
        self.Notice = None
        self.Email = None
        self.Url = None
        self.DataThreshold = None
        self.District = None
        self.Distance = None
        self.SignalStrength = None
        self.LostDay = None
        self.TagIDs = None
        self.SalePlan = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.IsActive = params.get("IsActive")
        self.Notice = params.get("Notice")
        self.Email = params.get("Email")
        self.Url = params.get("Url")
        self.DataThreshold = params.get("DataThreshold")
        self.District = params.get("District")
        self.Distance = params.get("Distance")
        self.SignalStrength = params.get("SignalStrength")
        self.LostDay = params.get("LostDay")
        self.TagIDs = params.get("TagIDs")
        self.SalePlan = params.get("SalePlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTacticRequest(AbstractModel):
    """CreateTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 策略名称
        :type Name: str
        :param IsAuto: 是否自动执行
        :type IsAuto: int
        :param PingInterval: 心跳上报间隔(s)
        :type PingInterval: int
        :param IsWeak: 是否开启弱信号检测
        :type IsWeak: int
        :param WeakThreshold: 弱信号阈值（-dbm）
        :type WeakThreshold: int
        :param IsDelay: 是否开启时延切换
        :type IsDelay: int
        :param DelayThreshold: 网络时延阈值（ms）
        :type DelayThreshold: int
        :param IsFake: 是否开启假信号检测
        :type IsFake: int
        :param FakeIP: 假信号检测IP字符串，用逗号分隔
        :type FakeIP: str
        :param FakeInterval: 假信号检测间隔（s）
        :type FakeInterval: int
        :param IsNet: 是否开启网络制式检测
        :type IsNet: int
        :param Network: 网络回落制式 1 2G、 2 3G 、 3 2/3G
        :type Network: int
        :param IsMove: 是否开启移动检测
        :type IsMove: int
        :param IsPriorityTele: 是否开启最优先运营商
        :type IsPriorityTele: int
        :param PriorityTele: 最优先运营商 1 移动、 2 联通、 3 电信 4 上次在线运营商
        :type PriorityTele: int
        :param IsBottomTele: 是否开启最不优先运营商
        :type IsBottomTele: int
        :param BottomTele: 最不优先运营商 1 移动、 2 联通、 3 电信
        :type BottomTele: int
        :param IsBestSignal: 最优先信号选取策略
        :type IsBestSignal: int
        """
        self.Name = None
        self.IsAuto = None
        self.PingInterval = None
        self.IsWeak = None
        self.WeakThreshold = None
        self.IsDelay = None
        self.DelayThreshold = None
        self.IsFake = None
        self.FakeIP = None
        self.FakeInterval = None
        self.IsNet = None
        self.Network = None
        self.IsMove = None
        self.IsPriorityTele = None
        self.PriorityTele = None
        self.IsBottomTele = None
        self.BottomTele = None
        self.IsBestSignal = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IsAuto = params.get("IsAuto")
        self.PingInterval = params.get("PingInterval")
        self.IsWeak = params.get("IsWeak")
        self.WeakThreshold = params.get("WeakThreshold")
        self.IsDelay = params.get("IsDelay")
        self.DelayThreshold = params.get("DelayThreshold")
        self.IsFake = params.get("IsFake")
        self.FakeIP = params.get("FakeIP")
        self.FakeInterval = params.get("FakeInterval")
        self.IsNet = params.get("IsNet")
        self.Network = params.get("Network")
        self.IsMove = params.get("IsMove")
        self.IsPriorityTele = params.get("IsPriorityTele")
        self.PriorityTele = params.get("PriorityTele")
        self.IsBottomTele = params.get("IsBottomTele")
        self.BottomTele = params.get("BottomTele")
        self.IsBestSignal = params.get("IsBestSignal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTacticResponse(AbstractModel):
    """CreateTactic返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRequest(AbstractModel):
    """CreateTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Comment: 备注
        :type Comment: str
        """
        self.Name = None
        self.Comment = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagResponse(AbstractModel):
    """CreateTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleID: 自动化规则ID
        :type RuleID: int
        """
        self.RuleID = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTacticRequest(AbstractModel):
    """DeleteTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param TacticID: 策略ID
        :type TacticID: int
        """
        self.TacticID = None


    def _deserialize(self, params):
        self.TacticID = params.get("TacticID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTacticResponse(AbstractModel):
    """DeleteTactic返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagRequest(AbstractModel):
    """DeleteTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param TagID: 标签ID
        :type TagID: int
        """
        self.TagID = None


    def _deserialize(self, params):
        self.TagID = params.get("TagID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagResponse(AbstractModel):
    """DeleteTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeLinkRequest(AbstractModel):
    """DescribeLink请求参数结构体

    """

    def __init__(self):
        r"""
        :param LinkID: 云兔卡ID
        :type LinkID: int
        :param UinAccount: 具体的账号
        :type UinAccount: str
        """
        self.LinkID = None
        self.UinAccount = None


    def _deserialize(self, params):
        self.LinkID = params.get("LinkID")
        self.UinAccount = params.get("UinAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLinkResponse(AbstractModel):
    """DescribeLink返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 云兔连接详细信息
        :type Data: :class:`tencentcloud.hasim.v20210716.models.LinkDetailInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = LinkDetailInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeLinksRequest(AbstractModel):
    """DescribeLinks请求参数结构体

    """

    def __init__(self):
        r"""
        :param LinkID: 云兔卡ID
        :type LinkID: int
        :param ICCID: 运营商ICCID
        :type ICCID: str
        :param IMEI: 设备码
        :type IMEI: str
        :param Status: 卡片状态
        :type Status: int
        :param TeleOperator: 运营商 1移动 2联通 3电信
        :type TeleOperator: int
        :param TagID: 标签ID
        :type TagID: int
        :param TacticID: 策略ID
        :type TacticID: int
        :param LinkedState: 设备在线状态 0 未激活 1 在线 2 离线
        :type LinkedState: int
        :param TagIDs: 标签ID 集合
        :type TagIDs: list of int
        :param Limit: 翻页大小, 默认翻页大小为10，最大数量为500
        :type Limit: int
        :param Offset: 翻页起始
        :type Offset: int
        """
        self.LinkID = None
        self.ICCID = None
        self.IMEI = None
        self.Status = None
        self.TeleOperator = None
        self.TagID = None
        self.TacticID = None
        self.LinkedState = None
        self.TagIDs = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LinkID = params.get("LinkID")
        self.ICCID = params.get("ICCID")
        self.IMEI = params.get("IMEI")
        self.Status = params.get("Status")
        self.TeleOperator = params.get("TeleOperator")
        self.TagID = params.get("TagID")
        self.TacticID = params.get("TacticID")
        self.LinkedState = params.get("LinkedState")
        self.TagIDs = params.get("TagIDs")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLinksResponse(AbstractModel):
    """DescribeLinks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 云兔连接响应信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.hasim.v20210716.models.LinkInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = LinkInfos()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 子订单ID
        :type DealName: str
        :param AuditStatus: 审批状态 0全部 1通过 2驳回 3待审核
        :type AuditStatus: int
        :param Limit: 翻页大小
        :type Limit: int
        :param Offset: 翻页偏移
        :type Offset: int
        :param BeginTime: 开始时间,例如2022-06-30 00:00:00
        :type BeginTime: str
        :param EndTime: 结束时间,例如2022-06-30 00:00:00
        :type EndTime: str
        """
        self.DealName = None
        self.AuditStatus = None
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.AuditStatus = params.get("AuditStatus")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 订单列表
        :type Data: :class:`tencentcloud.hasim.v20210716.models.Orders`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = Orders()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleRequest(AbstractModel):
    """DescribeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleID: 自动化规则ID
        :type RuleID: int
        """
        self.RuleID = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleResponse(AbstractModel):
    """DescribeRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 策略信息
        :type Data: :class:`tencentcloud.hasim.v20210716.models.RuleDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleDetail()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleID: 自动化规则ID
        :type RuleID: int
        :param RuleIDs: 自动化规则ID
        :type RuleIDs: list of int
        :param Name: 名称
        :type Name: str
        :param Type: 类型
        :type Type: int
        :param IsActive: 是否激活
        :type IsActive: int
        :param Limit: 翻页大小
        :type Limit: int
        :param Offset: 翻页偏移
        :type Offset: int
        """
        self.RuleID = None
        self.RuleIDs = None
        self.Name = None
        self.Type = None
        self.IsActive = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.RuleIDs = params.get("RuleIDs")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.IsActive = params.get("IsActive")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 自动化规则列表集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.hasim.v20210716.models.RuleInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleInfos()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTacticRequest(AbstractModel):
    """DescribeTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param TacticID: 策略ID
        :type TacticID: int
        """
        self.TacticID = None


    def _deserialize(self, params):
        self.TacticID = params.get("TacticID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTacticResponse(AbstractModel):
    """DescribeTactic返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 策略信息
        :type Data: :class:`tencentcloud.hasim.v20210716.models.Tactic`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = Tactic()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTacticsRequest(AbstractModel):
    """DescribeTactics请求参数结构体

    """

    def __init__(self):
        r"""
        :param TacticID: 策略ID
        :type TacticID: int
        :param Name: 策略名称
        :type Name: str
        """
        self.TacticID = None
        self.Name = None


    def _deserialize(self, params):
        self.TacticID = params.get("TacticID")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTacticsResponse(AbstractModel):
    """DescribeTactics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 策略集合信息
        :type Data: :class:`tencentcloud.hasim.v20210716.models.TacticInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TacticInfos()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 标签名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 列表
        :type Data: :class:`tencentcloud.hasim.v20210716.models.TagInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TagInfos()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DeviceReport(AbstractModel):
    """设备上报信息

    """

    def __init__(self):
        r"""
        :param Imei: 移动设备ID
        :type Imei: str
        :param Lng: 经度
注意：此字段可能返回 null，表示取不到有效值。
        :type Lng: str
        :param Lat: 维度
注意：此字段可能返回 null，表示取不到有效值。
        :type Lat: str
        :param Lac: 运营商基站ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Lac: str
        :param Cell: 小区CellID
注意：此字段可能返回 null，表示取不到有效值。
        :type Cell: str
        :param Iccid: 当前上报运营商ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Iccid: str
        :param Rss: 信号强度
注意：此字段可能返回 null，表示取不到有效值。
        :type Rss: int
        :param Tele: 运营商: 1 移动 2 联通 3 电信
注意：此字段可能返回 null，表示取不到有效值。
        :type Tele: int
        :param Tid: 当前设备策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Tid: int
        :param Ping: 心跳间隔,单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Ping: int
        :param Delay: 网络延迟,单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Delay: int
        :param Log: 高级日志启停状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: int
        :param DevType: 设备型号
注意：此字段可能返回 null，表示取不到有效值。
        :type DevType: str
        :param DevModel: 设备型号
注意：此字段可能返回 null，表示取不到有效值。
        :type DevModel: str
        :param Version: 设备版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param UploadTime: 设备刷新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadTime: str
        :param Status: 网络环境: 0 正常 1 弱网
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param MonthFirstTime: 每月第一次上报心跳时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthFirstTime: str
        """
        self.Imei = None
        self.Lng = None
        self.Lat = None
        self.Lac = None
        self.Cell = None
        self.Iccid = None
        self.Rss = None
        self.Tele = None
        self.Tid = None
        self.Ping = None
        self.Delay = None
        self.Log = None
        self.DevType = None
        self.DevModel = None
        self.Version = None
        self.UploadTime = None
        self.Status = None
        self.MonthFirstTime = None


    def _deserialize(self, params):
        self.Imei = params.get("Imei")
        self.Lng = params.get("Lng")
        self.Lat = params.get("Lat")
        self.Lac = params.get("Lac")
        self.Cell = params.get("Cell")
        self.Iccid = params.get("Iccid")
        self.Rss = params.get("Rss")
        self.Tele = params.get("Tele")
        self.Tid = params.get("Tid")
        self.Ping = params.get("Ping")
        self.Delay = params.get("Delay")
        self.Log = params.get("Log")
        self.DevType = params.get("DevType")
        self.DevModel = params.get("DevModel")
        self.Version = params.get("Version")
        self.UploadTime = params.get("UploadTime")
        self.Status = params.get("Status")
        self.MonthFirstTime = params.get("MonthFirstTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkDetailInfo(AbstractModel):
    """云兔连接详细信息

    """

    def __init__(self):
        r"""
        :param ID: 云兔连接ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param Status: 卡片状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param ActiveTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: str
        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DataUse: 数据用量
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUse: float
        :param AudioUse: 语音用量
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioUse: int
        :param SmsUse: 短信用量
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsUse: int
        :param LinkedState: 在线状态 0 未激活 1 在线 2 离线
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkedState: int
        :param TacticID: 预期策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticID: int
        :param TacticStatus: 策略下发状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticStatus: int
        :param TacticExpireTime: 策略下发成功过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticExpireTime: str
        :param IsActiveLog: 高级日志预期状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActiveLog: bool
        :param TeleOperator: 运营商 1移动 2联通 3电信
注意：此字段可能返回 null，表示取不到有效值。
        :type TeleOperator: int
        :param Report: 设备最新上报信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Report: :class:`tencentcloud.hasim.v20210716.models.DeviceReport`
        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Cards: 运营商ICCID信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Cards: list of TeleOperatorCard
        :param CardID: 云兔实际卡片ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CardID: str
        """
        self.ID = None
        self.Status = None
        self.ActiveTime = None
        self.ExpireTime = None
        self.DataUse = None
        self.AudioUse = None
        self.SmsUse = None
        self.LinkedState = None
        self.TacticID = None
        self.TacticStatus = None
        self.TacticExpireTime = None
        self.IsActiveLog = None
        self.TeleOperator = None
        self.Report = None
        self.Tags = None
        self.Cards = None
        self.CardID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Status = params.get("Status")
        self.ActiveTime = params.get("ActiveTime")
        self.ExpireTime = params.get("ExpireTime")
        self.DataUse = params.get("DataUse")
        self.AudioUse = params.get("AudioUse")
        self.SmsUse = params.get("SmsUse")
        self.LinkedState = params.get("LinkedState")
        self.TacticID = params.get("TacticID")
        self.TacticStatus = params.get("TacticStatus")
        self.TacticExpireTime = params.get("TacticExpireTime")
        self.IsActiveLog = params.get("IsActiveLog")
        self.TeleOperator = params.get("TeleOperator")
        if params.get("Report") is not None:
            self.Report = DeviceReport()
            self.Report._deserialize(params.get("Report"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Cards") is not None:
            self.Cards = []
            for item in params.get("Cards"):
                obj = TeleOperatorCard()
                obj._deserialize(item)
                self.Cards.append(obj)
        self.CardID = params.get("CardID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkInfo(AbstractModel):
    """云兔连接基本信息

    """

    def __init__(self):
        r"""
        :param ID: 云兔连接ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param Status: 卡片状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param ActiveTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: str
        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DataUse: 数据用量
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUse: float
        :param AudioUse: 语音用量
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioUse: int
        :param SmsUse: 短信用量
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsUse: int
        :param LinkedState: 在线状态 0 未激活 1 在线 2 离线
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkedState: int
        :param TacticID: 预期策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticID: int
        :param TacticStatus: 策略下发状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticStatus: int
        :param TacticExpireTime: 策略下发成功过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TacticExpireTime: str
        :param IsActiveLog: 高级日志预期状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActiveLog: bool
        :param TeleOperator: 运营商 1移动 2联通 3电信
注意：此字段可能返回 null，表示取不到有效值。
        :type TeleOperator: int
        :param Report: 设备最新上报信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Report: :class:`tencentcloud.hasim.v20210716.models.DeviceReport`
        """
        self.ID = None
        self.Status = None
        self.ActiveTime = None
        self.ExpireTime = None
        self.DataUse = None
        self.AudioUse = None
        self.SmsUse = None
        self.LinkedState = None
        self.TacticID = None
        self.TacticStatus = None
        self.TacticExpireTime = None
        self.IsActiveLog = None
        self.TeleOperator = None
        self.Report = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Status = params.get("Status")
        self.ActiveTime = params.get("ActiveTime")
        self.ExpireTime = params.get("ExpireTime")
        self.DataUse = params.get("DataUse")
        self.AudioUse = params.get("AudioUse")
        self.SmsUse = params.get("SmsUse")
        self.LinkedState = params.get("LinkedState")
        self.TacticID = params.get("TacticID")
        self.TacticStatus = params.get("TacticStatus")
        self.TacticExpireTime = params.get("TacticExpireTime")
        self.IsActiveLog = params.get("IsActiveLog")
        self.TeleOperator = params.get("TeleOperator")
        if params.get("Report") is not None:
            self.Report = DeviceReport()
            self.Report._deserialize(params.get("Report"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkInfos(AbstractModel):
    """云兔连接信息集合

    """

    def __init__(self):
        r"""
        :param Total: 总量
        :type Total: int
        :param List: 云兔连接列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of LinkInfo
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = LinkInfo()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLinkAdvancedLogRequest(AbstractModel):
    """ModifyLinkAdvancedLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param LinkID: 云兔ID
        :type LinkID: int
        :param IsAdLog: 是否激活高级日志 0 关闭 1激活
        :type IsAdLog: int
        """
        self.LinkID = None
        self.IsAdLog = None


    def _deserialize(self, params):
        self.LinkID = params.get("LinkID")
        self.IsAdLog = params.get("IsAdLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLinkAdvancedLogResponse(AbstractModel):
    """ModifyLinkAdvancedLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLinkTacticRequest(AbstractModel):
    """ModifyLinkTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param LinkID: 云兔ID
        :type LinkID: int
        :param TacticID: 策略ID
        :type TacticID: int
        """
        self.LinkID = None
        self.TacticID = None


    def _deserialize(self, params):
        self.LinkID = params.get("LinkID")
        self.TacticID = params.get("TacticID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLinkTacticResponse(AbstractModel):
    """ModifyLinkTactic返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLinkTeleRequest(AbstractModel):
    """ModifyLinkTele请求参数结构体

    """

    def __init__(self):
        r"""
        :param LinkID: 云兔ID
        :type LinkID: int
        :param TeleOperator: 运营商 1 移动 2 联通 3 电信
        :type TeleOperator: int
        """
        self.LinkID = None
        self.TeleOperator = None


    def _deserialize(self, params):
        self.LinkID = params.get("LinkID")
        self.TeleOperator = params.get("TeleOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLinkTeleResponse(AbstractModel):
    """ModifyLinkTele返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 自动化规则名称
        :type Name: str
        :param Type: 规则类型：用量类(101 当月|102有效期内)、位置类(201行政区|202移动距离)、网络质量类(301网络盲点)
        :type Type: int
        :param IsActive: 是否激活
        :type IsActive: bool
        :param Notice: 触发动作：1 邮件 2 API请求 3 微信 4 停卡 5 地图标识为盲点
        :type Notice: int
        :param RuleID: 自动化规则ID
        :type RuleID: int
        :param Email: 邮箱
        :type Email: str
        :param Url: 推送的API地址
        :type Url: str
        :param DataThreshold: 用量阈值
        :type DataThreshold: int
        :param District: 行政区类型：1. 省份 2. 城市 3. 区
        :type District: int
        :param Distance: 心跳移动距离阈值
        :type Distance: int
        :param SignalStrength: 信号强度阈值
        :type SignalStrength: int
        :param TagIDs: 标签ID集合
        :type TagIDs: list of int
        :param SalePlan: 资费计划
        :type SalePlan: str
        :param UinAccount: 具体的账号
        :type UinAccount: str
        """
        self.Name = None
        self.Type = None
        self.IsActive = None
        self.Notice = None
        self.RuleID = None
        self.Email = None
        self.Url = None
        self.DataThreshold = None
        self.District = None
        self.Distance = None
        self.SignalStrength = None
        self.TagIDs = None
        self.SalePlan = None
        self.UinAccount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.IsActive = params.get("IsActive")
        self.Notice = params.get("Notice")
        self.RuleID = params.get("RuleID")
        self.Email = params.get("Email")
        self.Url = params.get("Url")
        self.DataThreshold = params.get("DataThreshold")
        self.District = params.get("District")
        self.Distance = params.get("Distance")
        self.SignalStrength = params.get("SignalStrength")
        self.TagIDs = params.get("TagIDs")
        self.SalePlan = params.get("SalePlan")
        self.UinAccount = params.get("UinAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleStatusRequest(AbstractModel):
    """ModifyRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleID: 自动化规则ID
        :type RuleID: int
        :param IsActive: 是否激活
        :type IsActive: bool
        """
        self.RuleID = None
        self.IsActive = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.IsActive = params.get("IsActive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleStatusResponse(AbstractModel):
    """ModifyRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTacticRequest(AbstractModel):
    """ModifyTactic请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 策略名称
        :type Name: str
        :param IsAuto: 是否自动执行
        :type IsAuto: int
        :param PingInterval: 心跳上报间隔(s)
        :type PingInterval: int
        :param IsWeak: 是否开启弱信号检测
        :type IsWeak: int
        :param WeakThreshold: 弱信号阈值（-dbm）
        :type WeakThreshold: int
        :param IsDelay: 是否开启时延切换
        :type IsDelay: int
        :param DelayThreshold: 网络时延阈值（ms）
        :type DelayThreshold: int
        :param IsFake: 是否开启假信号检测
        :type IsFake: int
        :param FakeInterval: 假信号检测间隔（s）
        :type FakeInterval: int
        :param IsNet: 是否开启网络制式检测
        :type IsNet: int
        :param Network: 网络回落制式 1 2G、 2 3G 、 3 2/3G
        :type Network: int
        :param IsMove: 是否开启移动检测
        :type IsMove: int
        :param TacticID: 策略ID
        :type TacticID: int
        :param IsPriorityTele: 是否开启最优先运营商
        :type IsPriorityTele: int
        :param PriorityTele: 最优先运营商 1 移动、 2 联通、 3 电信 4 上次在线运营商
        :type PriorityTele: int
        :param IsBottomTele: 是否开启最不优先运营商
        :type IsBottomTele: int
        :param BottomTele: 最不优先运营商 1 移动、 2 联通、 3 电信
        :type BottomTele: int
        :param IsBestSignal: 是否最优先信号选取策略
        :type IsBestSignal: int
        :param FakeIP: 假信号检测IP字符串，用逗号分隔
        :type FakeIP: str
        """
        self.Name = None
        self.IsAuto = None
        self.PingInterval = None
        self.IsWeak = None
        self.WeakThreshold = None
        self.IsDelay = None
        self.DelayThreshold = None
        self.IsFake = None
        self.FakeInterval = None
        self.IsNet = None
        self.Network = None
        self.IsMove = None
        self.TacticID = None
        self.IsPriorityTele = None
        self.PriorityTele = None
        self.IsBottomTele = None
        self.BottomTele = None
        self.IsBestSignal = None
        self.FakeIP = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IsAuto = params.get("IsAuto")
        self.PingInterval = params.get("PingInterval")
        self.IsWeak = params.get("IsWeak")
        self.WeakThreshold = params.get("WeakThreshold")
        self.IsDelay = params.get("IsDelay")
        self.DelayThreshold = params.get("DelayThreshold")
        self.IsFake = params.get("IsFake")
        self.FakeInterval = params.get("FakeInterval")
        self.IsNet = params.get("IsNet")
        self.Network = params.get("Network")
        self.IsMove = params.get("IsMove")
        self.TacticID = params.get("TacticID")
        self.IsPriorityTele = params.get("IsPriorityTele")
        self.PriorityTele = params.get("PriorityTele")
        self.IsBottomTele = params.get("IsBottomTele")
        self.BottomTele = params.get("BottomTele")
        self.IsBestSignal = params.get("IsBestSignal")
        self.FakeIP = params.get("FakeIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTacticResponse(AbstractModel):
    """ModifyTactic返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTagRequest(AbstractModel):
    """ModifyTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param TagID: 标签ID
        :type TagID: int
        :param Comment: 备注
        :type Comment: str
        """
        self.Name = None
        self.TagID = None
        self.Comment = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TagID = params.get("TagID")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTagResponse(AbstractModel):
    """ModifyTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrderInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        r"""
        :param DealName: 子订单ID
        :type DealName: str
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param Uin: 订单账户
        :type Uin: str
        :param BuyNum: 购买数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BuyNum: int
        :param IndustryCode: 行业代码
注意：此字段可能返回 null，表示取不到有效值。
        :type IndustryCode: str
        :param Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param Contact: 联系人
注意：此字段可能返回 null，表示取不到有效值。
        :type Contact: str
        :param Msisdn: 电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param Specification: 卡片规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param Comment: 用户订单备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param BigDealId: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealId: str
        :param AuditStatus: 审批状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditStatus: str
        :param FlowStatus: 发货状态
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowStatus: str
        :param Remark: 审批备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param RefundBigDealId: 退费订单
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundBigDealId: str
        """
        self.DealName = None
        self.CreatedAt = None
        self.Uin = None
        self.BuyNum = None
        self.IndustryCode = None
        self.Address = None
        self.Contact = None
        self.Msisdn = None
        self.Specification = None
        self.Comment = None
        self.BigDealId = None
        self.AuditStatus = None
        self.FlowStatus = None
        self.Remark = None
        self.RefundBigDealId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.CreatedAt = params.get("CreatedAt")
        self.Uin = params.get("Uin")
        self.BuyNum = params.get("BuyNum")
        self.IndustryCode = params.get("IndustryCode")
        self.Address = params.get("Address")
        self.Contact = params.get("Contact")
        self.Msisdn = params.get("Msisdn")
        self.Specification = params.get("Specification")
        self.Comment = params.get("Comment")
        self.BigDealId = params.get("BigDealId")
        self.AuditStatus = params.get("AuditStatus")
        self.FlowStatus = params.get("FlowStatus")
        self.Remark = params.get("Remark")
        self.RefundBigDealId = params.get("RefundBigDealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Orders(AbstractModel):
    """订单列表

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param List: 订单集合
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of OrderInfo
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = OrderInfo()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewLinkInfoRequest(AbstractModel):
    """RenewLinkInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param LinkID: 云兔ID
        :type LinkID: int
        :param UinAccount: 具体的账号
        :type UinAccount: str
        """
        self.LinkID = None
        self.UinAccount = None


    def _deserialize(self, params):
        self.LinkID = params.get("LinkID")
        self.UinAccount = params.get("UinAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewLinkInfoResponse(AbstractModel):
    """RenewLinkInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Rule(AbstractModel):
    """自动化规则

    """

    def __init__(self):
        r"""
        :param Name: 规则名称
        :type Name: str
        :param ID: 规则ID
        :type ID: int
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param DeletedAt: 删除时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletedAt: str
        :param Type: 规则类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param IsActive: 是否激活
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActive: bool
        :param Notice: 触发动作：1 邮件 2 API请求 5 停卡 6 地图标识为盲点
注意：此字段可能返回 null，表示取不到有效值。
        :type Notice: int
        :param Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param Url: 回调API地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param DataThreshold: 用量类：用量阈值,单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :type DataThreshold: int
        :param District: 行政区类型：1. 省份 2. 城市 3. 区
注意：此字段可能返回 null，表示取不到有效值。
        :type District: int
        :param Distance: 移动距离阈值，单位KM
注意：此字段可能返回 null，表示取不到有效值。
        :type Distance: int
        :param SignalStrength: 信号强度阈值(-dbm）
注意：此字段可能返回 null，表示取不到有效值。
        :type SignalStrength: int
        :param LostDay: 盲点阈值天数
注意：此字段可能返回 null，表示取不到有效值。
        :type LostDay: int
        :param TagIDs: 绑定的标签ID集合
注意：此字段可能返回 null，表示取不到有效值。
        :type TagIDs: list of int non-negative
        :param SalePlan: 绑定的资费计划
注意：此字段可能返回 null，表示取不到有效值。
        :type SalePlan: str
        """
        self.Name = None
        self.ID = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.DeletedAt = None
        self.Type = None
        self.IsActive = None
        self.Notice = None
        self.Email = None
        self.Url = None
        self.DataThreshold = None
        self.District = None
        self.Distance = None
        self.SignalStrength = None
        self.LostDay = None
        self.TagIDs = None
        self.SalePlan = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ID = params.get("ID")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.DeletedAt = params.get("DeletedAt")
        self.Type = params.get("Type")
        self.IsActive = params.get("IsActive")
        self.Notice = params.get("Notice")
        self.Email = params.get("Email")
        self.Url = params.get("Url")
        self.DataThreshold = params.get("DataThreshold")
        self.District = params.get("District")
        self.Distance = params.get("Distance")
        self.SignalStrength = params.get("SignalStrength")
        self.LostDay = params.get("LostDay")
        self.TagIDs = params.get("TagIDs")
        self.SalePlan = params.get("SalePlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleDetail(AbstractModel):
    """自动化规则详细信息

    """

    def __init__(self):
        r"""
        :param Name: 规则名称
        :type Name: str
        :param ID: 规则ID
        :type ID: int
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param DeletedAt: 删除时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletedAt: str
        :param Type: 规则类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param IsActive: 是否激活
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActive: bool
        :param Notice: 触发动作：1 邮件 2 API请求 5 停卡 6 地图标识为盲点
注意：此字段可能返回 null，表示取不到有效值。
        :type Notice: int
        :param Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param Url: 回调API地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param DataThreshold: 用量类：用量阈值,单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :type DataThreshold: int
        :param District: 行政区类型：1. 省份 2. 城市 3. 区
注意：此字段可能返回 null，表示取不到有效值。
        :type District: int
        :param Distance: 移动距离阈值，单位KM
注意：此字段可能返回 null，表示取不到有效值。
        :type Distance: int
        :param SignalStrength: 信号强度阈值(-dbm）
注意：此字段可能返回 null，表示取不到有效值。
        :type SignalStrength: int
        :param LostDay: 盲点阈值天数
注意：此字段可能返回 null，表示取不到有效值。
        :type LostDay: int
        :param TagIDs: 标签ID集合
注意：此字段可能返回 null，表示取不到有效值。
        :type TagIDs: list of int
        :param SalePlan: 资费信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SalePlan: str
        """
        self.Name = None
        self.ID = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.DeletedAt = None
        self.Type = None
        self.IsActive = None
        self.Notice = None
        self.Email = None
        self.Url = None
        self.DataThreshold = None
        self.District = None
        self.Distance = None
        self.SignalStrength = None
        self.LostDay = None
        self.TagIDs = None
        self.SalePlan = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ID = params.get("ID")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.DeletedAt = params.get("DeletedAt")
        self.Type = params.get("Type")
        self.IsActive = params.get("IsActive")
        self.Notice = params.get("Notice")
        self.Email = params.get("Email")
        self.Url = params.get("Url")
        self.DataThreshold = params.get("DataThreshold")
        self.District = params.get("District")
        self.Distance = params.get("Distance")
        self.SignalStrength = params.get("SignalStrength")
        self.LostDay = params.get("LostDay")
        self.TagIDs = params.get("TagIDs")
        self.SalePlan = params.get("SalePlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfos(AbstractModel):
    """自动化规则集合

    """

    def __init__(self):
        r"""
        :param Total: 总量
        :type Total: int
        :param List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Rule
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Rule()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tactic(AbstractModel):
    """策略信息

    """

    def __init__(self):
        r"""
        :param ID: 策略ID
        :type ID: int
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param IsAuto: 是否自动执行策略
        :type IsAuto: int
        :param PingInterval: 设备上报信息间隔
注意：此字段可能返回 null，表示取不到有效值。
        :type PingInterval: int
        :param IsWeak: 是否开启弱信号检查
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWeak: int
        :param WeakThreshold: 弱信号阈值（-dbm）
注意：此字段可能返回 null，表示取不到有效值。
        :type WeakThreshold: int
        :param IsDelay: 忘了时延切换
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDelay: int
        :param DelayThreshold: 时延阈值（ms）
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayThreshold: int
        :param IsFake: 是否开启假信号检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFake: int
        :param FakeIP: 假信号检测IP字符串，用逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeIP: str
        :param FakeInterval: 假信号检测间隔（s）
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeInterval: int
        :param IsNet: 是否开启网络制式检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNet: int
        :param Network: 网络回落制式 1: 2G、 2: 3G 、 3: 2/3G
注意：此字段可能返回 null，表示取不到有效值。
        :type Network: int
        :param IsMove: 是否开启移动检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMove: int
        :param Name: 策略名称
        :type Name: str
        :param IsPriorityTele: 是否开启最优先运营商
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPriorityTele: int
        :param PriorityTele: 最优先运营商 1 移动、 2 联通、 3 电信 4 上次在线运营商
注意：此字段可能返回 null，表示取不到有效值。
        :type PriorityTele: int
        :param IsBottomTele: 是否开启最不优先运营商
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBottomTele: int
        :param BottomTele: 最不优先运营商 1 移动、 2 联通、 3 电信
注意：此字段可能返回 null，表示取不到有效值。
        :type BottomTele: int
        :param IsBestSignal: 是否开启最优先信号选取策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBestSignal: int
        """
        self.ID = None
        self.CreatedAt = None
        self.IsAuto = None
        self.PingInterval = None
        self.IsWeak = None
        self.WeakThreshold = None
        self.IsDelay = None
        self.DelayThreshold = None
        self.IsFake = None
        self.FakeIP = None
        self.FakeInterval = None
        self.IsNet = None
        self.Network = None
        self.IsMove = None
        self.Name = None
        self.IsPriorityTele = None
        self.PriorityTele = None
        self.IsBottomTele = None
        self.BottomTele = None
        self.IsBestSignal = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.CreatedAt = params.get("CreatedAt")
        self.IsAuto = params.get("IsAuto")
        self.PingInterval = params.get("PingInterval")
        self.IsWeak = params.get("IsWeak")
        self.WeakThreshold = params.get("WeakThreshold")
        self.IsDelay = params.get("IsDelay")
        self.DelayThreshold = params.get("DelayThreshold")
        self.IsFake = params.get("IsFake")
        self.FakeIP = params.get("FakeIP")
        self.FakeInterval = params.get("FakeInterval")
        self.IsNet = params.get("IsNet")
        self.Network = params.get("Network")
        self.IsMove = params.get("IsMove")
        self.Name = params.get("Name")
        self.IsPriorityTele = params.get("IsPriorityTele")
        self.PriorityTele = params.get("PriorityTele")
        self.IsBottomTele = params.get("IsBottomTele")
        self.BottomTele = params.get("BottomTele")
        self.IsBestSignal = params.get("IsBestSignal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TacticInfos(AbstractModel):
    """策略信息集合

    """

    def __init__(self):
        r"""
        :param Total: 总量
        :type Total: int
        :param List: 策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Tactic
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Tactic()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """云兔标签信息

    """

    def __init__(self):
        r"""
        :param Name: 标签名称
        :type Name: str
        :param ID: 标签ID
        :type ID: int
        :param Comment: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 更改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self.Name = None
        self.ID = None
        self.Comment = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ID = params.get("ID")
        self.Comment = params.get("Comment")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfos(AbstractModel):
    """标签列表集合

    """

    def __init__(self):
        r"""
        :param Total: 总量
        :type Total: int
        :param List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Tag
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Tag()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeleOperatorCard(AbstractModel):
    """运营商卡片信息

    """

    def __init__(self):
        r"""
        :param AccountTime: 开户时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountTime: str
        :param ActiveTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: str
        :param ICCID: 运营商ICCID
        :type ICCID: str
        :param LinkID: 云兔卡ID
        :type LinkID: int
        :param Msisdn: 电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param IMSI: 移动用户识别码
注意：此字段可能返回 null，表示取不到有效值。
        :type IMSI: str
        :param TeleOperator: 运营商: 1 移动 2 联通 3 电信
        :type TeleOperator: int
        """
        self.AccountTime = None
        self.ActiveTime = None
        self.ICCID = None
        self.LinkID = None
        self.Msisdn = None
        self.IMSI = None
        self.TeleOperator = None


    def _deserialize(self, params):
        self.AccountTime = params.get("AccountTime")
        self.ActiveTime = params.get("ActiveTime")
        self.ICCID = params.get("ICCID")
        self.LinkID = params.get("LinkID")
        self.Msisdn = params.get("Msisdn")
        self.IMSI = params.get("IMSI")
        self.TeleOperator = params.get("TeleOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        