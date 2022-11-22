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


class CaptchaOperDataInterceptUnit(AbstractModel):
    """DescribeCaptchaOperData方法 拦截情况type = 2 返回的数据结构

    """

    def __init__(self):
        r"""
        :param DateKey: 时间
        :type DateKey: str
        :param AllStopCnt: 停止验证数量
        :type AllStopCnt: float
        :param PicStopCnt: 图片停止加载数量
        :type PicStopCnt: float
        :param StrategyStopCnt: 策略拦截数量
        :type StrategyStopCnt: float
        """
        self.DateKey = None
        self.AllStopCnt = None
        self.PicStopCnt = None
        self.StrategyStopCnt = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.AllStopCnt = params.get("AllStopCnt")
        self.PicStopCnt = params.get("PicStopCnt")
        self.StrategyStopCnt = params.get("StrategyStopCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaOperDataLoadTimeUnit(AbstractModel):
    """操作数据查询方法DescribeCaptchaOperData 的返回结果，安全验证码加载耗时type = 1

    """

    def __init__(self):
        r"""
        :param DateKey: 时间
        :type DateKey: str
        :param MarketLoadTime: Market加载时间
        :type MarketLoadTime: float
        :param AppIdLoadTime: AppId加载时间
        :type AppIdLoadTime: float
        """
        self.DateKey = None
        self.MarketLoadTime = None
        self.AppIdLoadTime = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.MarketLoadTime = params.get("MarketLoadTime")
        self.AppIdLoadTime = params.get("AppIdLoadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaOperDataRes(AbstractModel):
    """DescribeCaptchaOperData 接口 返回数据类型集合

    """

    def __init__(self):
        r"""
        :param OperDataLoadTimeUnitArray: 验证码加载耗时数据返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OperDataLoadTimeUnitArray: list of CaptchaOperDataLoadTimeUnit
        :param OperDataInterceptUnitArray: 验证码拦截情况数据返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OperDataInterceptUnitArray: list of CaptchaOperDataInterceptUnit
        :param OperDataTryTimesUnitArray: 验证码尝试次数数据返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OperDataTryTimesUnitArray: list of CaptchaOperDataTryTimesUnit
        :param OperDataTryTimesDistributeUnitArray: 验证码尝试次数分布数据返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OperDataTryTimesDistributeUnitArray: list of CaptchaOperDataTryTimesDistributeUnit
        """
        self.OperDataLoadTimeUnitArray = None
        self.OperDataInterceptUnitArray = None
        self.OperDataTryTimesUnitArray = None
        self.OperDataTryTimesDistributeUnitArray = None


    def _deserialize(self, params):
        if params.get("OperDataLoadTimeUnitArray") is not None:
            self.OperDataLoadTimeUnitArray = []
            for item in params.get("OperDataLoadTimeUnitArray"):
                obj = CaptchaOperDataLoadTimeUnit()
                obj._deserialize(item)
                self.OperDataLoadTimeUnitArray.append(obj)
        if params.get("OperDataInterceptUnitArray") is not None:
            self.OperDataInterceptUnitArray = []
            for item in params.get("OperDataInterceptUnitArray"):
                obj = CaptchaOperDataInterceptUnit()
                obj._deserialize(item)
                self.OperDataInterceptUnitArray.append(obj)
        if params.get("OperDataTryTimesUnitArray") is not None:
            self.OperDataTryTimesUnitArray = []
            for item in params.get("OperDataTryTimesUnitArray"):
                obj = CaptchaOperDataTryTimesUnit()
                obj._deserialize(item)
                self.OperDataTryTimesUnitArray.append(obj)
        if params.get("OperDataTryTimesDistributeUnitArray") is not None:
            self.OperDataTryTimesDistributeUnitArray = []
            for item in params.get("OperDataTryTimesDistributeUnitArray"):
                obj = CaptchaOperDataTryTimesDistributeUnit()
                obj._deserialize(item)
                self.OperDataTryTimesDistributeUnitArray.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaOperDataTryTimesDistributeUnit(AbstractModel):
    """DescribeCaptchaOperData方法 尝试次数分布 type = 4

    """

    def __init__(self):
        r"""
        :param TryCount: 尝试次数
        :type TryCount: int
        :param UserCount: 用户请求数量
        :type UserCount: int
        """
        self.TryCount = None
        self.UserCount = None


    def _deserialize(self, params):
        self.TryCount = params.get("TryCount")
        self.UserCount = params.get("UserCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaOperDataTryTimesUnit(AbstractModel):
    """DescribeCaptchaOperData操作数据查询尝试次数 type = 3

    """

    def __init__(self):
        r"""
        :param DateKey: 时间
        :type DateKey: str
        :param CntPerPass: 平均尝试次数
        :type CntPerPass: list of float
        :param MarketCntPerPass: market平均尝试次数
        :type MarketCntPerPass: float
        """
        self.DateKey = None
        self.CntPerPass = None
        self.MarketCntPerPass = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.CntPerPass = params.get("CntPerPass")
        self.MarketCntPerPass = params.get("MarketCntPerPass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaQueryData(AbstractModel):
    """该类型为DescribeCaptchaData 方法返回数据类型

    """

    def __init__(self):
        r"""
        :param Cnt: 数量
        :type Cnt: int
        :param Date: 时间
        :type Date: str
        """
        self.Cnt = None
        self.Date = None


    def _deserialize(self, params):
        self.Cnt = params.get("Cnt")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaStatisticObj(AbstractModel):
    """验证码统计图Obj

    """

    def __init__(self):
        r"""
        :param ActionTotal: 请求总量
        :type ActionTotal: int
        :param VerifyTotal: 验证总量
        :type VerifyTotal: int
        :param VerifyThroughTotal: 验证通过总量
        :type VerifyThroughTotal: int
        :param VerifyInterceptTotal: 验证拦截总量
        :type VerifyInterceptTotal: int
        :param TicketTotal: 票据校验总量
        :type TicketTotal: int
        :param TicketThroughTotal: 票据通过总量
        :type TicketThroughTotal: int
        :param TicketInterceptTotal: 票据拦截总量
        :type TicketInterceptTotal: int
        :param RequestTrend: 请求趋势图
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestTrend: list of RequestTrendObj
        :param InterceptPerTrend: 拦截率趋势图
注意：此字段可能返回 null，表示取不到有效值。
        :type InterceptPerTrend: list of InterceptPerTrendObj
        :param TicketCheckTrend: 票据校验趋势图
注意：此字段可能返回 null，表示取不到有效值。
        :type TicketCheckTrend: list of TicketCheckTrendObj
        """
        self.ActionTotal = None
        self.VerifyTotal = None
        self.VerifyThroughTotal = None
        self.VerifyInterceptTotal = None
        self.TicketTotal = None
        self.TicketThroughTotal = None
        self.TicketInterceptTotal = None
        self.RequestTrend = None
        self.InterceptPerTrend = None
        self.TicketCheckTrend = None


    def _deserialize(self, params):
        self.ActionTotal = params.get("ActionTotal")
        self.VerifyTotal = params.get("VerifyTotal")
        self.VerifyThroughTotal = params.get("VerifyThroughTotal")
        self.VerifyInterceptTotal = params.get("VerifyInterceptTotal")
        self.TicketTotal = params.get("TicketTotal")
        self.TicketThroughTotal = params.get("TicketThroughTotal")
        self.TicketInterceptTotal = params.get("TicketInterceptTotal")
        if params.get("RequestTrend") is not None:
            self.RequestTrend = []
            for item in params.get("RequestTrend"):
                obj = RequestTrendObj()
                obj._deserialize(item)
                self.RequestTrend.append(obj)
        if params.get("InterceptPerTrend") is not None:
            self.InterceptPerTrend = []
            for item in params.get("InterceptPerTrend"):
                obj = InterceptPerTrendObj()
                obj._deserialize(item)
                self.InterceptPerTrend.append(obj)
        if params.get("TicketCheckTrend") is not None:
            self.TicketCheckTrend = []
            for item in params.get("TicketCheckTrend"):
                obj = TicketCheckTrendObj()
                obj._deserialize(item)
                self.TicketCheckTrend.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaTicketDataRes(AbstractModel):
    """DescribeCaptchaTicketData 接口 返回数据类型集合

    """

    def __init__(self):
        r"""
        :param TicketAmountArray: 票据验证总量返回
        :type TicketAmountArray: list of TicketAmountUnit
        :param TicketThroughArray: 票据验证通过量返回
        :type TicketThroughArray: list of TicketThroughUnit
        :param TicketInterceptArray: 票据验证拦截量返回
        :type TicketInterceptArray: list of TicketInterceptUnit
        """
        self.TicketAmountArray = None
        self.TicketThroughArray = None
        self.TicketInterceptArray = None


    def _deserialize(self, params):
        if params.get("TicketAmountArray") is not None:
            self.TicketAmountArray = []
            for item in params.get("TicketAmountArray"):
                obj = TicketAmountUnit()
                obj._deserialize(item)
                self.TicketAmountArray.append(obj)
        if params.get("TicketThroughArray") is not None:
            self.TicketThroughArray = []
            for item in params.get("TicketThroughArray"):
                obj = TicketThroughUnit()
                obj._deserialize(item)
                self.TicketThroughArray.append(obj)
        if params.get("TicketInterceptArray") is not None:
            self.TicketInterceptArray = []
            for item in params.get("TicketInterceptArray"):
                obj = TicketInterceptUnit()
                obj._deserialize(item)
                self.TicketInterceptArray.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaUserAllAppId(AbstractModel):
    """用户注册的APPID和应用名称对象

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param AppName: 注册应用名称
        :type AppName: str
        :param TcAppId: 腾讯云APPID
        :type TcAppId: int
        :param ChannelInfo: 渠道信息
        :type ChannelInfo: str
        """
        self.CaptchaAppId = None
        self.AppName = None
        self.TcAppId = None
        self.ChannelInfo = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppName = params.get("AppName")
        self.TcAppId = params.get("TcAppId")
        self.ChannelInfo = params.get("ChannelInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaAppIdInfoRequest(AbstractModel):
    """DescribeCaptchaAppIdInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用注册APPID
        :type CaptchaAppId: int
        """
        self.CaptchaAppId = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaAppIdInfoResponse(AbstractModel):
    """DescribeCaptchaAppIdInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param SchemeColor: 界面风格
        :type SchemeColor: str
        :param Language: 语言
        :type Language: int
        :param SceneType: 场景
        :type SceneType: int
        :param EvilInterceptGrade: 防控风险等级
        :type EvilInterceptGrade: int
        :param SmartVerify: 智能验证
        :type SmartVerify: int
        :param SmartEngine: 智能引擎
        :type SmartEngine: int
        :param CapType: 验证码类型
        :type CapType: int
        :param AppName: 应用名称
        :type AppName: str
        :param DomainLimit: 域名限制
        :type DomainLimit: str
        :param MailAlarm: 邮件告警
注意：此字段可能返回 null，表示取不到有效值。
        :type MailAlarm: list of str
        :param TrafficThreshold: 流量控制
        :type TrafficThreshold: int
        :param EncryptKey: 加密key
        :type EncryptKey: str
        :param TopFullScreen: 是否全屏
        :type TopFullScreen: int
        :param CaptchaCode: 成功返回0 其它失败
        :type CaptchaCode: int
        :param CaptchaMsg: 返回操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SchemeColor = None
        self.Language = None
        self.SceneType = None
        self.EvilInterceptGrade = None
        self.SmartVerify = None
        self.SmartEngine = None
        self.CapType = None
        self.AppName = None
        self.DomainLimit = None
        self.MailAlarm = None
        self.TrafficThreshold = None
        self.EncryptKey = None
        self.TopFullScreen = None
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SchemeColor = params.get("SchemeColor")
        self.Language = params.get("Language")
        self.SceneType = params.get("SceneType")
        self.EvilInterceptGrade = params.get("EvilInterceptGrade")
        self.SmartVerify = params.get("SmartVerify")
        self.SmartEngine = params.get("SmartEngine")
        self.CapType = params.get("CapType")
        self.AppName = params.get("AppName")
        self.DomainLimit = params.get("DomainLimit")
        self.MailAlarm = params.get("MailAlarm")
        self.TrafficThreshold = params.get("TrafficThreshold")
        self.EncryptKey = params.get("EncryptKey")
        self.TopFullScreen = params.get("TopFullScreen")
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaDataRequest(AbstractModel):
    """DescribeCaptchaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param Start: 查询开始时间
        :type Start: int
        :param End: 查询结束时间
        :type End: int
        :param Type: 查询类型
        :type Type: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.End = None
        self.Type = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.End = params.get("End")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaDataResponse(AbstractModel):
    """DescribeCaptchaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 返回码 0 成功 其它失败
        :type CaptchaCode: int
        :param Data: 数据数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CaptchaQueryData
        :param CaptchaMsg: 返回信息描述
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.Data = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CaptchaQueryData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaDataSumRequest(AbstractModel):
    """DescribeCaptchaDataSum请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param Start: 查询开始时间
        :type Start: int
        :param End: 查询结束时间
        :type End: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.End = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaDataSumResponse(AbstractModel):
    """DescribeCaptchaDataSum返回参数结构体

    """

    def __init__(self):
        r"""
        :param GetSum: 请求总量
        :type GetSum: int
        :param VfySuccSum: 请求验证成功量
        :type VfySuccSum: int
        :param VfySum: 请求验证量
        :type VfySum: int
        :param AttackSum: 拦截攻击量
        :type AttackSum: int
        :param CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param CaptchaCode: 成功返回0  其它失败
        :type CaptchaCode: int
        :param CheckTicketSum: 票据校验总量
        :type CheckTicketSum: int
        :param TicketThroughputSum: 票据验证通过量
        :type TicketThroughputSum: int
        :param TicketInterceptSum: 票据验证拦截量
        :type TicketInterceptSum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GetSum = None
        self.VfySuccSum = None
        self.VfySum = None
        self.AttackSum = None
        self.CaptchaMsg = None
        self.CaptchaCode = None
        self.CheckTicketSum = None
        self.TicketThroughputSum = None
        self.TicketInterceptSum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GetSum = params.get("GetSum")
        self.VfySuccSum = params.get("VfySuccSum")
        self.VfySum = params.get("VfySum")
        self.AttackSum = params.get("AttackSum")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.CaptchaCode = params.get("CaptchaCode")
        self.CheckTicketSum = params.get("CheckTicketSum")
        self.TicketThroughputSum = params.get("TicketThroughputSum")
        self.TicketInterceptSum = params.get("TicketInterceptSum")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaMiniDataRequest(AbstractModel):
    """DescribeCaptchaMiniData请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param Start: 查询开始时间 例如：2019112900
        :type Start: int
        :param End: 查询结束时间 例如：2019112902
        :type End: int
        :param Type: 查询类型 安全验证码小程序插件分类查询数据接口，请求量type=0、通过量type=1、验证量type=2、拦截量type=3 小时级查询（五小时左右延迟）
        :type Type: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.End = None
        self.Type = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.End = params.get("End")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniDataResponse(AbstractModel):
    """DescribeCaptchaMiniData返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 返回码 0 成功 其它失败
        :type CaptchaCode: int
        :param Data: 数据数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CaptchaQueryData
        :param CaptchaMsg: 返回信息描述
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.Data = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CaptchaQueryData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaMiniDataSumRequest(AbstractModel):
    """DescribeCaptchaMiniDataSum请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param Start: 查询开始时间
        :type Start: int
        :param End: 查询结束时间
        :type End: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.End = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniDataSumResponse(AbstractModel):
    """DescribeCaptchaMiniDataSum返回参数结构体

    """

    def __init__(self):
        r"""
        :param GetSum: 请求总量
注意：此字段可能返回 null，表示取不到有效值。
        :type GetSum: int
        :param VfySuccSum: 请求验证成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type VfySuccSum: int
        :param VfySum: 请求验证量
注意：此字段可能返回 null，表示取不到有效值。
        :type VfySum: int
        :param AttackSum: 拦截攻击量
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackSum: int
        :param CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param CaptchaCode: 成功返回0  其它失败
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaCode: int
        :param CheckTicketSum: 票据校验总量
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckTicketSum: int
        :param TicketThroughputSum: 票据验证通过量
注意：此字段可能返回 null，表示取不到有效值。
        :type TicketThroughputSum: int
        :param TicketInterceptSum: 票据验证拦截量
注意：此字段可能返回 null，表示取不到有效值。
        :type TicketInterceptSum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GetSum = None
        self.VfySuccSum = None
        self.VfySum = None
        self.AttackSum = None
        self.CaptchaMsg = None
        self.CaptchaCode = None
        self.CheckTicketSum = None
        self.TicketThroughputSum = None
        self.TicketInterceptSum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GetSum = params.get("GetSum")
        self.VfySuccSum = params.get("VfySuccSum")
        self.VfySum = params.get("VfySum")
        self.AttackSum = params.get("AttackSum")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.CaptchaCode = params.get("CaptchaCode")
        self.CheckTicketSum = params.get("CheckTicketSum")
        self.TicketThroughputSum = params.get("TicketThroughputSum")
        self.TicketInterceptSum = params.get("TicketInterceptSum")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaMiniOperDataRequest(AbstractModel):
    """DescribeCaptchaMiniOperData请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param Start: 查询开始时间
        :type Start: int
        :param Type: 查询类型
        :type Type: int
        :param End: 查询结束时间
        :type End: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.Type = None
        self.End = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.Type = params.get("Type")
        self.End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniOperDataResponse(AbstractModel):
    """DescribeCaptchaMiniOperData返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 成功返回 0 其它失败
        :type CaptchaCode: int
        :param CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param Data: 用户操作数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaOperDataRes`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        if params.get("Data") is not None:
            self.Data = CaptchaOperDataRes()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCaptchaMiniResultRequest(AbstractModel):
    """DescribeCaptchaMiniResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaType: 固定填值：9（滑块验证码）
        :type CaptchaType: int
        :param Ticket: 验证码返回给用户的票据
        :type Ticket: str
        :param UserIp: 业务侧获取到的验证码使用者的外网IP
        :type UserIp: str
        :param CaptchaAppId: 验证码应用ID。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到CaptchaAppId。
        :type CaptchaAppId: int
        :param AppSecretKey: 验证码应用密钥。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到AppSecretKey。AppSecretKey属于服务器端校验验证码票据的密钥，请妥善保密，请勿泄露给第三方。
        :type AppSecretKey: str
        :param BusinessId: 业务 ID，网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据
        :type BusinessId: int
        :param SceneId: 场景 ID，网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据
        :type SceneId: int
        :param MacAddress: mac 地址或设备唯一标识
        :type MacAddress: str
        :param Imei: 手机设备号
        :type Imei: str
        """
        self.CaptchaType = None
        self.Ticket = None
        self.UserIp = None
        self.CaptchaAppId = None
        self.AppSecretKey = None
        self.BusinessId = None
        self.SceneId = None
        self.MacAddress = None
        self.Imei = None


    def _deserialize(self, params):
        self.CaptchaType = params.get("CaptchaType")
        self.Ticket = params.get("Ticket")
        self.UserIp = params.get("UserIp")
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppSecretKey = params.get("AppSecretKey")
        self.BusinessId = params.get("BusinessId")
        self.SceneId = params.get("SceneId")
        self.MacAddress = params.get("MacAddress")
        self.Imei = params.get("Imei")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniResultResponse(AbstractModel):
    """DescribeCaptchaMiniResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 1       ticket verification succeeded     票据验证成功
7       CaptchaAppId does not match     票据与验证码应用APPID不匹配
8       ticket expired     票据超时
10     ticket format error     票据格式不正确
15     ticket decryption failed     票据解密失败
16     CaptchaAppId wrong format     检查验证码应用APPID错误
21     ticket error     票据验证错误
25     invalid ticket     无效票据
26     system internal error     系统内部错误
31 	   UnauthorizedOperation.Unauthorized	无有效套餐包/账户已欠费
100   param err     参数校验错误
        :type CaptchaCode: int
        :param CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaMiniRiskResultRequest(AbstractModel):
    """DescribeCaptchaMiniRiskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaType: 固定填值：9（滑块验证码）
        :type CaptchaType: int
        :param Ticket: 验证码返回给用户的票据
        :type Ticket: str
        :param UserIp: 业务侧获取到的验证码使用者的外网IP
        :type UserIp: str
        :param CaptchaAppId: 验证码应用APPID
        :type CaptchaAppId: int
        :param AppSecretKey: 用于服务器端校验验证码票据的验证密钥，请妥善保密，请勿泄露给第三方
        :type AppSecretKey: str
        :param BusinessId: 业务 ID，网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据
        :type BusinessId: int
        :param SceneId: 场景 ID，网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据
        :type SceneId: int
        :param MacAddress: mac 地址或设备唯一标识
        :type MacAddress: str
        :param Imei: 手机设备号
        :type Imei: str
        :param SceneCode: 验证场景：1 活动防刷场景，2 登录保护场景，3 注册保护场景。根据需求选择场景参数。
        :type SceneCode: int
        :param WeChatOpenId: 用户操作来源的微信开放账号
        :type WeChatOpenId: str
        """
        self.CaptchaType = None
        self.Ticket = None
        self.UserIp = None
        self.CaptchaAppId = None
        self.AppSecretKey = None
        self.BusinessId = None
        self.SceneId = None
        self.MacAddress = None
        self.Imei = None
        self.SceneCode = None
        self.WeChatOpenId = None


    def _deserialize(self, params):
        self.CaptchaType = params.get("CaptchaType")
        self.Ticket = params.get("Ticket")
        self.UserIp = params.get("UserIp")
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppSecretKey = params.get("AppSecretKey")
        self.BusinessId = params.get("BusinessId")
        self.SceneId = params.get("SceneId")
        self.MacAddress = params.get("MacAddress")
        self.Imei = params.get("Imei")
        self.SceneCode = params.get("SceneCode")
        self.WeChatOpenId = params.get("WeChatOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniRiskResultResponse(AbstractModel):
    """DescribeCaptchaMiniRiskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 1 ticket verification succeeded 票据验证成功
7 CaptchaAppId does not match 票据与验证码应用APPID不匹配
8 ticket expired 票据超时
10 ticket format error 票据格式不正确
15 ticket decryption failed 票据解密失败
16 CaptchaAppId wrong format 检查验证码应用APPID错误
21 ticket error 票据验证错误
25 bad visitor 策略拦截
26 system internal error 系统内部错误
100 param err 参数校验错误
        :type CaptchaCode: int
        :param CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param ManageMarketingRiskValue: 拦截策略返回信息
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ManageMarketingRiskValue: :class:`tencentcloud.captcha.v20190722.models.OutputManageMarketingRiskValue`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.ManageMarketingRiskValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        if params.get("ManageMarketingRiskValue") is not None:
            self.ManageMarketingRiskValue = OutputManageMarketingRiskValue()
            self.ManageMarketingRiskValue._deserialize(params.get("ManageMarketingRiskValue"))
        self.RequestId = params.get("RequestId")


class DescribeCaptchaOperDataRequest(AbstractModel):
    """DescribeCaptchaOperData请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param Start: 查询开始时间
        :type Start: int
        :param Type: 查询类型
        :type Type: int
        :param End: 查询结束时间
        :type End: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.Type = None
        self.End = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.Type = params.get("Type")
        self.End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaOperDataResponse(AbstractModel):
    """DescribeCaptchaOperData返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 成功返回 0 其它失败
        :type CaptchaCode: int
        :param CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param Data: 用户操作数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaOperDataRes`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        if params.get("Data") is not None:
            self.Data = CaptchaOperDataRes()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCaptchaResultRequest(AbstractModel):
    """DescribeCaptchaResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaType: 固定填值：9。可在控制台配置不同验证码类型。
        :type CaptchaType: int
        :param Ticket: 前端回调函数返回的用户验证票据
        :type Ticket: str
        :param UserIp: 业务侧获取到的验证码使用者的外网IP
        :type UserIp: str
        :param Randstr: 前端回调函数返回的随机字符串
        :type Randstr: str
        :param CaptchaAppId: 验证码应用ID。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到CaptchaAppId。
        :type CaptchaAppId: int
        :param AppSecretKey: 验证码应用密钥。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到AppSecretKey。AppSecretKey属于服务器端校验验证码票据的密钥，请妥善保密，请勿泄露给第三方。
        :type AppSecretKey: str
        :param BusinessId: 业务 ID，网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据
        :type BusinessId: int
        :param SceneId: 场景 ID，网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据
        :type SceneId: int
        :param MacAddress: mac 地址或设备唯一标识
        :type MacAddress: str
        :param Imei: 手机设备号
        :type Imei: str
        :param NeedGetCaptchaTime: 是否返回前端获取验证码时间，取值1：需要返回
        :type NeedGetCaptchaTime: int
        """
        self.CaptchaType = None
        self.Ticket = None
        self.UserIp = None
        self.Randstr = None
        self.CaptchaAppId = None
        self.AppSecretKey = None
        self.BusinessId = None
        self.SceneId = None
        self.MacAddress = None
        self.Imei = None
        self.NeedGetCaptchaTime = None


    def _deserialize(self, params):
        self.CaptchaType = params.get("CaptchaType")
        self.Ticket = params.get("Ticket")
        self.UserIp = params.get("UserIp")
        self.Randstr = params.get("Randstr")
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppSecretKey = params.get("AppSecretKey")
        self.BusinessId = params.get("BusinessId")
        self.SceneId = params.get("SceneId")
        self.MacAddress = params.get("MacAddress")
        self.Imei = params.get("Imei")
        self.NeedGetCaptchaTime = params.get("NeedGetCaptchaTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaResultResponse(AbstractModel):
    """DescribeCaptchaResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 1 OK 验证通过
7 captcha no match 传入的Randstr不合法，请检查Randstr是否与前端返回的Randstr一致
8 ticket expired 传入的Ticket已过期（Ticket有效期5分钟），请重新生成Ticket、Randstr进行校验
9 ticket reused 传入的Ticket被重复使用，请重新生成Ticket、Randstr进行校验
15 decrypt fail 传入的Ticket不合法，请检查Ticket是否与前端返回的Ticket一致
16 appid-ticket mismatch 传入的CaptchaAppId错误，请检查CaptchaAppId是否与前端传入的CaptchaAppId一致，并且保障CaptchaAppId是从验证码控制台【验证管理】->【基础配置】中获取
21 diff 票据校验异常，可能的原因是（1）若Ticket包含terror前缀，一般是由于用户网络较差，导致前端自动容灾，而生成了容灾票据，业务侧可根据需要进行跳过或二次处理。（2）若Ticket不包含terror前缀，则是由于验证码风控系统发现请求有安全风险，业务侧可根据需要进行拦截。
100 appid-secretkey-ticket mismatch 参数校验错误，（1）请检查CaptchaAppId与AppSecretKey是否正确，CaptchaAppId、AppSecretKey需要在验证码控制台【验证管理】>【基础配置】中获取（2）请检查传入的Ticket是否由传入的CaptchaAppId生成
        :type CaptchaCode: int
        :param CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param EvilLevel: 无感验证模式下，该参数返回验证结果：
EvilLevel=0 请求无恶意
EvilLevel=100 请求有恶意
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilLevel: int
        :param GetCaptchaTime: 前端获取验证码时间，时间戳格式
注意：此字段可能返回 null，表示取不到有效值。
        :type GetCaptchaTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.EvilLevel = None
        self.GetCaptchaTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.EvilLevel = params.get("EvilLevel")
        self.GetCaptchaTime = params.get("GetCaptchaTime")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaTicketDataRequest(AbstractModel):
    """DescribeCaptchaTicketData请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param Start: 查询开始时间 例如：20200909
        :type Start: int
        :param End: 查询结束时间 例如：20220314
        :type End: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.End = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaTicketDataResponse(AbstractModel):
    """DescribeCaptchaTicketData返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 成功返回 0 其它失败
        :type CaptchaCode: int
        :param CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param Data: 验证码票据信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaTicketDataRes`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        if params.get("Data") is not None:
            self.Data = CaptchaTicketDataRes()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCaptchaUserAllAppIdRequest(AbstractModel):
    """DescribeCaptchaUserAllAppId请求参数结构体

    """


class DescribeCaptchaUserAllAppIdResponse(AbstractModel):
    """DescribeCaptchaUserAllAppId返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 用户注册的所有Appid和应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CaptchaUserAllAppId
        :param CaptchaCode: 成功返回 0  其它失败
        :type CaptchaCode: int
        :param CaptchaMsg: 返回操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CaptchaUserAllAppId()
                obj._deserialize(item)
                self.Data.append(obj)
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class GetTicketStatisticsRequest(AbstractModel):
    """GetTicketStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码AppId
        :type CaptchaAppId: str
        :param StartTimeStr: 开始时间字符串
        :type StartTimeStr: str
        :param EndTimeStr: 结束时间字符串
        :type EndTimeStr: str
        :param Dimension: 查询粒度
        :type Dimension: str
        """
        self.CaptchaAppId = None
        self.StartTimeStr = None
        self.EndTimeStr = None
        self.Dimension = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.StartTimeStr = params.get("StartTimeStr")
        self.EndTimeStr = params.get("EndTimeStr")
        self.Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTicketStatisticsResponse(AbstractModel):
    """GetTicketStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 查询后数据块
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaStatisticObj`
        :param CaptchaCode: 验证码返回码
        :type CaptchaCode: int
        :param CaptchaMsg: 验证码返回信息
        :type CaptchaMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CaptchaStatisticObj()
            self.Data._deserialize(params.get("Data"))
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class GetTotalTicketStatisticsRequest(AbstractModel):
    """GetTotalTicketStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTimeStr: 开始时间
        :type StartTimeStr: str
        :param EndTimeStr: 结束时间
        :type EndTimeStr: str
        :param Dimension: 查询粒度
分钟：“1”
小时：“2”
天：“3”
        :type Dimension: str
        """
        self.StartTimeStr = None
        self.EndTimeStr = None
        self.Dimension = None


    def _deserialize(self, params):
        self.StartTimeStr = params.get("StartTimeStr")
        self.EndTimeStr = params.get("EndTimeStr")
        self.Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTotalTicketStatisticsResponse(AbstractModel):
    """GetTotalTicketStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaStatisticObj`
        :param CaptchaCode: 返回码
        :type CaptchaCode: int
        :param CaptchaMsg: 返回信息
        :type CaptchaMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CaptchaStatisticObj()
            self.Data._deserialize(params.get("Data"))
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class InterceptPerTrendObj(AbstractModel):
    """拦截率趋势obj

    """

    def __init__(self):
        r"""
        :param Ftime: 时间参数
        :type Ftime: str
        :param RequestInterceptPer: 拦截率
        :type RequestInterceptPer: float
        :param AnswerInterceptPer: 答案拦截率
        :type AnswerInterceptPer: float
        :param PolicyInterceptPer: 策略拦截率
        :type PolicyInterceptPer: float
        """
        self.Ftime = None
        self.RequestInterceptPer = None
        self.AnswerInterceptPer = None
        self.PolicyInterceptPer = None


    def _deserialize(self, params):
        self.Ftime = params.get("Ftime")
        self.RequestInterceptPer = params.get("RequestInterceptPer")
        self.AnswerInterceptPer = params.get("AnswerInterceptPer")
        self.PolicyInterceptPer = params.get("PolicyInterceptPer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputManageMarketingRiskValue(AbstractModel):
    """拦截策略返回信息

    """

    def __init__(self):
        r"""
        :param UserId: 账号 ID。对应输入参数： AccountType 是 1 时，对应 QQ 的 OpenID。
AccountType 是 2 时，对应微信的 OpenID/UnionID。
AccountType 是 4 时，对应手机号。
AccountType 是 8 时，对应 imei、idfa、imeiMD5 或者 idfaMD5。
AccountType 是 0 时，对应账号信息。
AccountType 是 10004 时，对应手机号的 MD5。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param PostTime: 操作时间戳，单位秒（对应输入参数）。 
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: int
        :param AssociateAccount: 对应输入参数，AccountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录 后关联业务自身的账号 ID。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param UserIp: 业务详情。 注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param RiskLevel: 风险值 pass : 无恶意
review：需要人工审核
reject：拒绝，高风险恶意
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param RiskType: 风险类型，请查看下面详细说明 注意：此字段可能返回 null，表示取不到有效值。
账号风险	
        账号信用低	1	账号近期存在因恶意被处罚历史，网络低活跃，被举报等因素
	疑似 低活跃账号	11	账号活跃度与正常用户有差异
	垃圾账号	2	疑似批量注册小号，近期存在严重违规或大量举报
	疑似小号	21	账号有疑似线上养号，小号等行为
	疑似 违规账号	22	账号曾有违规行为、曾被举报过、曾因违规被处罚过等
	无效账号	3	送检账号参数无法成功解析，请检查微信 openid 是否有
	黑名单	4	该账号在业务侧有过拉黑记录
	白名单 	5	业务自行有添加过白名单记录
行为风险	
        批量操作	101	存在 ip/设备/环境等因素的聚集性异常
	疑似 IP 属性聚集 	1011	出现 IP 聚集
	疑似 设备属性聚集 	1012	出现设备聚集
	自动机 	103	疑似自动机批量请求
	微信登录态无效 	104	检查 wxtoken 参数，是否已经失效
环境风险	
        环境异常 	201	操作 ip/设备/环境存在异常。当前 ip 为非常用 ip 或恶意 ip 段
	疑似 非常用IP请求 	2011	当前请求 IP 非该账号常用 IP
	疑似 IP 异常 	2012	使用 idc 机房 ip 或 使用代理 ip 或 使用恶意 ip 
	非公网有效 ip 	205	传进来的 IP 地址为内网 ip 地址或者 ip 保留地
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskType: list of int
        """
        self.UserId = None
        self.PostTime = None
        self.AssociateAccount = None
        self.UserIp = None
        self.RiskLevel = None
        self.RiskType = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.PostTime = params.get("PostTime")
        self.AssociateAccount = params.get("AssociateAccount")
        self.UserIp = params.get("UserIp")
        self.RiskLevel = params.get("RiskLevel")
        self.RiskType = params.get("RiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestTrendObj(AbstractModel):
    """验证码请求趋势图obj

    """

    def __init__(self):
        r"""
        :param Ftime: 时间参数
        :type Ftime: str
        :param RequestAction: 请求量
        :type RequestAction: int
        :param RequestVerify: 验证量
        :type RequestVerify: int
        :param RequestThroughput: 通过量
        :type RequestThroughput: int
        :param RequestIntercept: 拦截量
        :type RequestIntercept: int
        """
        self.Ftime = None
        self.RequestAction = None
        self.RequestVerify = None
        self.RequestThroughput = None
        self.RequestIntercept = None


    def _deserialize(self, params):
        self.Ftime = params.get("Ftime")
        self.RequestAction = params.get("RequestAction")
        self.RequestVerify = params.get("RequestVerify")
        self.RequestThroughput = params.get("RequestThroughput")
        self.RequestIntercept = params.get("RequestIntercept")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketAmountUnit(AbstractModel):
    """DescribeCaptchaTicketData 返回的数据结构

    """

    def __init__(self):
        r"""
        :param DateKey: 时间
        :type DateKey: str
        :param Amount: 票据验证总量
        :type Amount: int
        """
        self.DateKey = None
        self.Amount = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.Amount = params.get("Amount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketCheckTrendObj(AbstractModel):
    """验证码票据校验趋势obj

    """

    def __init__(self):
        r"""
        :param Ftime: 时间参数
        :type Ftime: str
        :param TicketCount: 票据校验量
        :type TicketCount: int
        :param TicketThroughput: 票据通过量
        :type TicketThroughput: int
        :param TicketIntercept: 票据拦截量
        :type TicketIntercept: int
        """
        self.Ftime = None
        self.TicketCount = None
        self.TicketThroughput = None
        self.TicketIntercept = None


    def _deserialize(self, params):
        self.Ftime = params.get("Ftime")
        self.TicketCount = params.get("TicketCount")
        self.TicketThroughput = params.get("TicketThroughput")
        self.TicketIntercept = params.get("TicketIntercept")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketInterceptUnit(AbstractModel):
    """DescribeCaptchaTicketData 返回的数据结构

    """

    def __init__(self):
        r"""
        :param DateKey: 时间
        :type DateKey: str
        :param Intercept: 票据验证拦截量
        :type Intercept: int
        """
        self.DateKey = None
        self.Intercept = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.Intercept = params.get("Intercept")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketThroughUnit(AbstractModel):
    """DescribeCaptchaTicketData 返回的数据结构

    """

    def __init__(self):
        r"""
        :param DateKey: 时间
        :type DateKey: str
        :param Through: 票据验证的通过量
        :type Through: int
        """
        self.DateKey = None
        self.Through = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.Through = params.get("Through")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCaptchaAppIdInfoRequest(AbstractModel):
    """UpdateCaptchaAppIdInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param AppName: 应用名
        :type AppName: str
        :param DomainLimit: 域名限制
        :type DomainLimit: str
        :param SceneType: 场景类型
        :type SceneType: int
        :param CapType: 验证码类型
        :type CapType: int
        :param EvilInterceptGrade: 风险级别
        :type EvilInterceptGrade: int
        :param SmartVerify: 智能检测
        :type SmartVerify: int
        :param SmartEngine: 开启智能引擎
        :type SmartEngine: int
        :param SchemeColor: web风格
        :type SchemeColor: str
        :param CaptchaLanguage: 语言
        :type CaptchaLanguage: int
        :param MailAlarm: 告警邮箱
        :type MailAlarm: str
        :param TopFullScreen: 是否全屏
        :type TopFullScreen: int
        :param TrafficThreshold: 流量限制
        :type TrafficThreshold: int
        """
        self.CaptchaAppId = None
        self.AppName = None
        self.DomainLimit = None
        self.SceneType = None
        self.CapType = None
        self.EvilInterceptGrade = None
        self.SmartVerify = None
        self.SmartEngine = None
        self.SchemeColor = None
        self.CaptchaLanguage = None
        self.MailAlarm = None
        self.TopFullScreen = None
        self.TrafficThreshold = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppName = params.get("AppName")
        self.DomainLimit = params.get("DomainLimit")
        self.SceneType = params.get("SceneType")
        self.CapType = params.get("CapType")
        self.EvilInterceptGrade = params.get("EvilInterceptGrade")
        self.SmartVerify = params.get("SmartVerify")
        self.SmartEngine = params.get("SmartEngine")
        self.SchemeColor = params.get("SchemeColor")
        self.CaptchaLanguage = params.get("CaptchaLanguage")
        self.MailAlarm = params.get("MailAlarm")
        self.TopFullScreen = params.get("TopFullScreen")
        self.TrafficThreshold = params.get("TrafficThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCaptchaAppIdInfoResponse(AbstractModel):
    """UpdateCaptchaAppIdInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CaptchaCode: 返回码 0 成功，其它失败
        :type CaptchaCode: int
        :param CaptchaMsg: 返回操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")