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
        :param _DateKey: 时间
        :type DateKey: str
        :param _AllStopCnt: 停止验证数量
        :type AllStopCnt: float
        :param _PicStopCnt: 图片停止加载数量
        :type PicStopCnt: float
        :param _StrategyStopCnt: 策略拦截数量
        :type StrategyStopCnt: float
        """
        self._DateKey = None
        self._AllStopCnt = None
        self._PicStopCnt = None
        self._StrategyStopCnt = None

    @property
    def DateKey(self):
        return self._DateKey

    @DateKey.setter
    def DateKey(self, DateKey):
        self._DateKey = DateKey

    @property
    def AllStopCnt(self):
        return self._AllStopCnt

    @AllStopCnt.setter
    def AllStopCnt(self, AllStopCnt):
        self._AllStopCnt = AllStopCnt

    @property
    def PicStopCnt(self):
        return self._PicStopCnt

    @PicStopCnt.setter
    def PicStopCnt(self, PicStopCnt):
        self._PicStopCnt = PicStopCnt

    @property
    def StrategyStopCnt(self):
        return self._StrategyStopCnt

    @StrategyStopCnt.setter
    def StrategyStopCnt(self, StrategyStopCnt):
        self._StrategyStopCnt = StrategyStopCnt


    def _deserialize(self, params):
        self._DateKey = params.get("DateKey")
        self._AllStopCnt = params.get("AllStopCnt")
        self._PicStopCnt = params.get("PicStopCnt")
        self._StrategyStopCnt = params.get("StrategyStopCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaOperDataLoadTimeUnit(AbstractModel):
    """操作数据查询方法DescribeCaptchaOperData 的返回结果，安全验证码加载耗时type = 1

    """

    def __init__(self):
        r"""
        :param _DateKey: 时间
        :type DateKey: str
        :param _MarketLoadTime: Market加载时间
        :type MarketLoadTime: float
        :param _AppIdLoadTime: AppId加载时间
        :type AppIdLoadTime: float
        """
        self._DateKey = None
        self._MarketLoadTime = None
        self._AppIdLoadTime = None

    @property
    def DateKey(self):
        return self._DateKey

    @DateKey.setter
    def DateKey(self, DateKey):
        self._DateKey = DateKey

    @property
    def MarketLoadTime(self):
        return self._MarketLoadTime

    @MarketLoadTime.setter
    def MarketLoadTime(self, MarketLoadTime):
        self._MarketLoadTime = MarketLoadTime

    @property
    def AppIdLoadTime(self):
        return self._AppIdLoadTime

    @AppIdLoadTime.setter
    def AppIdLoadTime(self, AppIdLoadTime):
        self._AppIdLoadTime = AppIdLoadTime


    def _deserialize(self, params):
        self._DateKey = params.get("DateKey")
        self._MarketLoadTime = params.get("MarketLoadTime")
        self._AppIdLoadTime = params.get("AppIdLoadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaOperDataRes(AbstractModel):
    """DescribeCaptchaOperData 接口 返回数据类型集合

    """

    def __init__(self):
        r"""
        :param _OperDataLoadTimeUnitArray: 验证码加载耗时数据返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OperDataLoadTimeUnitArray: list of CaptchaOperDataLoadTimeUnit
        :param _OperDataInterceptUnitArray: 验证码拦截情况数据返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OperDataInterceptUnitArray: list of CaptchaOperDataInterceptUnit
        :param _OperDataTryTimesUnitArray: 验证码尝试次数数据返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OperDataTryTimesUnitArray: list of CaptchaOperDataTryTimesUnit
        :param _OperDataTryTimesDistributeUnitArray: 验证码尝试次数分布数据返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OperDataTryTimesDistributeUnitArray: list of CaptchaOperDataTryTimesDistributeUnit
        """
        self._OperDataLoadTimeUnitArray = None
        self._OperDataInterceptUnitArray = None
        self._OperDataTryTimesUnitArray = None
        self._OperDataTryTimesDistributeUnitArray = None

    @property
    def OperDataLoadTimeUnitArray(self):
        return self._OperDataLoadTimeUnitArray

    @OperDataLoadTimeUnitArray.setter
    def OperDataLoadTimeUnitArray(self, OperDataLoadTimeUnitArray):
        self._OperDataLoadTimeUnitArray = OperDataLoadTimeUnitArray

    @property
    def OperDataInterceptUnitArray(self):
        return self._OperDataInterceptUnitArray

    @OperDataInterceptUnitArray.setter
    def OperDataInterceptUnitArray(self, OperDataInterceptUnitArray):
        self._OperDataInterceptUnitArray = OperDataInterceptUnitArray

    @property
    def OperDataTryTimesUnitArray(self):
        return self._OperDataTryTimesUnitArray

    @OperDataTryTimesUnitArray.setter
    def OperDataTryTimesUnitArray(self, OperDataTryTimesUnitArray):
        self._OperDataTryTimesUnitArray = OperDataTryTimesUnitArray

    @property
    def OperDataTryTimesDistributeUnitArray(self):
        return self._OperDataTryTimesDistributeUnitArray

    @OperDataTryTimesDistributeUnitArray.setter
    def OperDataTryTimesDistributeUnitArray(self, OperDataTryTimesDistributeUnitArray):
        self._OperDataTryTimesDistributeUnitArray = OperDataTryTimesDistributeUnitArray


    def _deserialize(self, params):
        if params.get("OperDataLoadTimeUnitArray") is not None:
            self._OperDataLoadTimeUnitArray = []
            for item in params.get("OperDataLoadTimeUnitArray"):
                obj = CaptchaOperDataLoadTimeUnit()
                obj._deserialize(item)
                self._OperDataLoadTimeUnitArray.append(obj)
        if params.get("OperDataInterceptUnitArray") is not None:
            self._OperDataInterceptUnitArray = []
            for item in params.get("OperDataInterceptUnitArray"):
                obj = CaptchaOperDataInterceptUnit()
                obj._deserialize(item)
                self._OperDataInterceptUnitArray.append(obj)
        if params.get("OperDataTryTimesUnitArray") is not None:
            self._OperDataTryTimesUnitArray = []
            for item in params.get("OperDataTryTimesUnitArray"):
                obj = CaptchaOperDataTryTimesUnit()
                obj._deserialize(item)
                self._OperDataTryTimesUnitArray.append(obj)
        if params.get("OperDataTryTimesDistributeUnitArray") is not None:
            self._OperDataTryTimesDistributeUnitArray = []
            for item in params.get("OperDataTryTimesDistributeUnitArray"):
                obj = CaptchaOperDataTryTimesDistributeUnit()
                obj._deserialize(item)
                self._OperDataTryTimesDistributeUnitArray.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaOperDataTryTimesDistributeUnit(AbstractModel):
    """DescribeCaptchaOperData方法 尝试次数分布 type = 4

    """

    def __init__(self):
        r"""
        :param _TryCount: 尝试次数
        :type TryCount: int
        :param _UserCount: 用户请求数量
        :type UserCount: int
        """
        self._TryCount = None
        self._UserCount = None

    @property
    def TryCount(self):
        return self._TryCount

    @TryCount.setter
    def TryCount(self, TryCount):
        self._TryCount = TryCount

    @property
    def UserCount(self):
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount


    def _deserialize(self, params):
        self._TryCount = params.get("TryCount")
        self._UserCount = params.get("UserCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaOperDataTryTimesUnit(AbstractModel):
    """DescribeCaptchaOperData操作数据查询尝试次数 type = 3

    """

    def __init__(self):
        r"""
        :param _DateKey: 时间
        :type DateKey: str
        :param _CntPerPass: 平均尝试次数
        :type CntPerPass: list of float
        :param _MarketCntPerPass: market平均尝试次数
        :type MarketCntPerPass: float
        """
        self._DateKey = None
        self._CntPerPass = None
        self._MarketCntPerPass = None

    @property
    def DateKey(self):
        return self._DateKey

    @DateKey.setter
    def DateKey(self, DateKey):
        self._DateKey = DateKey

    @property
    def CntPerPass(self):
        return self._CntPerPass

    @CntPerPass.setter
    def CntPerPass(self, CntPerPass):
        self._CntPerPass = CntPerPass

    @property
    def MarketCntPerPass(self):
        return self._MarketCntPerPass

    @MarketCntPerPass.setter
    def MarketCntPerPass(self, MarketCntPerPass):
        self._MarketCntPerPass = MarketCntPerPass


    def _deserialize(self, params):
        self._DateKey = params.get("DateKey")
        self._CntPerPass = params.get("CntPerPass")
        self._MarketCntPerPass = params.get("MarketCntPerPass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaQueryData(AbstractModel):
    """该类型为DescribeCaptchaData 方法返回数据类型

    """

    def __init__(self):
        r"""
        :param _Cnt: 数量
        :type Cnt: int
        :param _Date: 时间
        :type Date: str
        """
        self._Cnt = None
        self._Date = None

    @property
    def Cnt(self):
        return self._Cnt

    @Cnt.setter
    def Cnt(self, Cnt):
        self._Cnt = Cnt

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._Cnt = params.get("Cnt")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaStatisticObj(AbstractModel):
    """验证码统计图Obj

    """

    def __init__(self):
        r"""
        :param _ActionTotal: 请求总量
        :type ActionTotal: int
        :param _VerifyTotal: 验证总量
        :type VerifyTotal: int
        :param _VerifyThroughTotal: 验证通过总量
        :type VerifyThroughTotal: int
        :param _VerifyInterceptTotal: 验证拦截总量
        :type VerifyInterceptTotal: int
        :param _TicketTotal: 票据校验总量
        :type TicketTotal: int
        :param _TicketThroughTotal: 票据通过总量
        :type TicketThroughTotal: int
        :param _TicketInterceptTotal: 票据拦截总量
        :type TicketInterceptTotal: int
        :param _RequestTrend: 请求趋势图
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestTrend: list of RequestTrendObj
        :param _InterceptPerTrend: 拦截率趋势图
注意：此字段可能返回 null，表示取不到有效值。
        :type InterceptPerTrend: list of InterceptPerTrendObj
        :param _TicketCheckTrend: 票据校验趋势图
注意：此字段可能返回 null，表示取不到有效值。
        :type TicketCheckTrend: list of TicketCheckTrendObj
        """
        self._ActionTotal = None
        self._VerifyTotal = None
        self._VerifyThroughTotal = None
        self._VerifyInterceptTotal = None
        self._TicketTotal = None
        self._TicketThroughTotal = None
        self._TicketInterceptTotal = None
        self._RequestTrend = None
        self._InterceptPerTrend = None
        self._TicketCheckTrend = None

    @property
    def ActionTotal(self):
        return self._ActionTotal

    @ActionTotal.setter
    def ActionTotal(self, ActionTotal):
        self._ActionTotal = ActionTotal

    @property
    def VerifyTotal(self):
        return self._VerifyTotal

    @VerifyTotal.setter
    def VerifyTotal(self, VerifyTotal):
        self._VerifyTotal = VerifyTotal

    @property
    def VerifyThroughTotal(self):
        return self._VerifyThroughTotal

    @VerifyThroughTotal.setter
    def VerifyThroughTotal(self, VerifyThroughTotal):
        self._VerifyThroughTotal = VerifyThroughTotal

    @property
    def VerifyInterceptTotal(self):
        return self._VerifyInterceptTotal

    @VerifyInterceptTotal.setter
    def VerifyInterceptTotal(self, VerifyInterceptTotal):
        self._VerifyInterceptTotal = VerifyInterceptTotal

    @property
    def TicketTotal(self):
        return self._TicketTotal

    @TicketTotal.setter
    def TicketTotal(self, TicketTotal):
        self._TicketTotal = TicketTotal

    @property
    def TicketThroughTotal(self):
        return self._TicketThroughTotal

    @TicketThroughTotal.setter
    def TicketThroughTotal(self, TicketThroughTotal):
        self._TicketThroughTotal = TicketThroughTotal

    @property
    def TicketInterceptTotal(self):
        return self._TicketInterceptTotal

    @TicketInterceptTotal.setter
    def TicketInterceptTotal(self, TicketInterceptTotal):
        self._TicketInterceptTotal = TicketInterceptTotal

    @property
    def RequestTrend(self):
        return self._RequestTrend

    @RequestTrend.setter
    def RequestTrend(self, RequestTrend):
        self._RequestTrend = RequestTrend

    @property
    def InterceptPerTrend(self):
        return self._InterceptPerTrend

    @InterceptPerTrend.setter
    def InterceptPerTrend(self, InterceptPerTrend):
        self._InterceptPerTrend = InterceptPerTrend

    @property
    def TicketCheckTrend(self):
        return self._TicketCheckTrend

    @TicketCheckTrend.setter
    def TicketCheckTrend(self, TicketCheckTrend):
        self._TicketCheckTrend = TicketCheckTrend


    def _deserialize(self, params):
        self._ActionTotal = params.get("ActionTotal")
        self._VerifyTotal = params.get("VerifyTotal")
        self._VerifyThroughTotal = params.get("VerifyThroughTotal")
        self._VerifyInterceptTotal = params.get("VerifyInterceptTotal")
        self._TicketTotal = params.get("TicketTotal")
        self._TicketThroughTotal = params.get("TicketThroughTotal")
        self._TicketInterceptTotal = params.get("TicketInterceptTotal")
        if params.get("RequestTrend") is not None:
            self._RequestTrend = []
            for item in params.get("RequestTrend"):
                obj = RequestTrendObj()
                obj._deserialize(item)
                self._RequestTrend.append(obj)
        if params.get("InterceptPerTrend") is not None:
            self._InterceptPerTrend = []
            for item in params.get("InterceptPerTrend"):
                obj = InterceptPerTrendObj()
                obj._deserialize(item)
                self._InterceptPerTrend.append(obj)
        if params.get("TicketCheckTrend") is not None:
            self._TicketCheckTrend = []
            for item in params.get("TicketCheckTrend"):
                obj = TicketCheckTrendObj()
                obj._deserialize(item)
                self._TicketCheckTrend.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaTicketDataRes(AbstractModel):
    """DescribeCaptchaTicketData 接口 返回数据类型集合

    """

    def __init__(self):
        r"""
        :param _TicketAmountArray: 票据验证总量返回
        :type TicketAmountArray: list of TicketAmountUnit
        :param _TicketThroughArray: 票据验证通过量返回
        :type TicketThroughArray: list of TicketThroughUnit
        :param _TicketInterceptArray: 票据验证拦截量返回
        :type TicketInterceptArray: list of TicketInterceptUnit
        """
        self._TicketAmountArray = None
        self._TicketThroughArray = None
        self._TicketInterceptArray = None

    @property
    def TicketAmountArray(self):
        return self._TicketAmountArray

    @TicketAmountArray.setter
    def TicketAmountArray(self, TicketAmountArray):
        self._TicketAmountArray = TicketAmountArray

    @property
    def TicketThroughArray(self):
        return self._TicketThroughArray

    @TicketThroughArray.setter
    def TicketThroughArray(self, TicketThroughArray):
        self._TicketThroughArray = TicketThroughArray

    @property
    def TicketInterceptArray(self):
        return self._TicketInterceptArray

    @TicketInterceptArray.setter
    def TicketInterceptArray(self, TicketInterceptArray):
        self._TicketInterceptArray = TicketInterceptArray


    def _deserialize(self, params):
        if params.get("TicketAmountArray") is not None:
            self._TicketAmountArray = []
            for item in params.get("TicketAmountArray"):
                obj = TicketAmountUnit()
                obj._deserialize(item)
                self._TicketAmountArray.append(obj)
        if params.get("TicketThroughArray") is not None:
            self._TicketThroughArray = []
            for item in params.get("TicketThroughArray"):
                obj = TicketThroughUnit()
                obj._deserialize(item)
                self._TicketThroughArray.append(obj)
        if params.get("TicketInterceptArray") is not None:
            self._TicketInterceptArray = []
            for item in params.get("TicketInterceptArray"):
                obj = TicketInterceptUnit()
                obj._deserialize(item)
                self._TicketInterceptArray.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptchaUserAllAppId(AbstractModel):
    """用户注册的APPID和应用名称对象

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _AppName: 注册应用名称
        :type AppName: str
        :param _TcAppId: 腾讯云APPID
        :type TcAppId: int
        :param _ChannelInfo: 渠道信息
        :type ChannelInfo: str
        """
        self._CaptchaAppId = None
        self._AppName = None
        self._TcAppId = None
        self._ChannelInfo = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def TcAppId(self):
        return self._TcAppId

    @TcAppId.setter
    def TcAppId(self, TcAppId):
        self._TcAppId = TcAppId

    @property
    def ChannelInfo(self):
        return self._ChannelInfo

    @ChannelInfo.setter
    def ChannelInfo(self, ChannelInfo):
        self._ChannelInfo = ChannelInfo


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppName = params.get("AppName")
        self._TcAppId = params.get("TcAppId")
        self._ChannelInfo = params.get("ChannelInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaAppIdInfoRequest(AbstractModel):
    """DescribeCaptchaAppIdInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用注册APPID
        :type CaptchaAppId: int
        """
        self._CaptchaAppId = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaAppIdInfoResponse(AbstractModel):
    """DescribeCaptchaAppIdInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SchemeColor: 界面风格
        :type SchemeColor: str
        :param _Language: 语言
        :type Language: int
        :param _SceneType: 场景
        :type SceneType: int
        :param _EvilInterceptGrade: 防控风险等级
        :type EvilInterceptGrade: int
        :param _SmartVerify: 智能验证
        :type SmartVerify: int
        :param _SmartEngine: 智能引擎
        :type SmartEngine: int
        :param _CapType: 验证码类型
        :type CapType: int
        :param _AppName: 应用名称
        :type AppName: str
        :param _DomainLimit: 域名限制
        :type DomainLimit: str
        :param _MailAlarm: 邮件告警
注意：此字段可能返回 null，表示取不到有效值。
        :type MailAlarm: list of str
        :param _TrafficThreshold: 流量控制
        :type TrafficThreshold: int
        :param _EncryptKey: 加密key
        :type EncryptKey: str
        :param _TopFullScreen: 是否全屏
        :type TopFullScreen: int
        :param _CaptchaCode: 成功返回0 其它失败
        :type CaptchaCode: int
        :param _CaptchaMsg: 返回操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SchemeColor = None
        self._Language = None
        self._SceneType = None
        self._EvilInterceptGrade = None
        self._SmartVerify = None
        self._SmartEngine = None
        self._CapType = None
        self._AppName = None
        self._DomainLimit = None
        self._MailAlarm = None
        self._TrafficThreshold = None
        self._EncryptKey = None
        self._TopFullScreen = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def SchemeColor(self):
        return self._SchemeColor

    @SchemeColor.setter
    def SchemeColor(self, SchemeColor):
        self._SchemeColor = SchemeColor

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def SceneType(self):
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def EvilInterceptGrade(self):
        return self._EvilInterceptGrade

    @EvilInterceptGrade.setter
    def EvilInterceptGrade(self, EvilInterceptGrade):
        self._EvilInterceptGrade = EvilInterceptGrade

    @property
    def SmartVerify(self):
        return self._SmartVerify

    @SmartVerify.setter
    def SmartVerify(self, SmartVerify):
        self._SmartVerify = SmartVerify

    @property
    def SmartEngine(self):
        return self._SmartEngine

    @SmartEngine.setter
    def SmartEngine(self, SmartEngine):
        self._SmartEngine = SmartEngine

    @property
    def CapType(self):
        return self._CapType

    @CapType.setter
    def CapType(self, CapType):
        self._CapType = CapType

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainLimit(self):
        return self._DomainLimit

    @DomainLimit.setter
    def DomainLimit(self, DomainLimit):
        self._DomainLimit = DomainLimit

    @property
    def MailAlarm(self):
        return self._MailAlarm

    @MailAlarm.setter
    def MailAlarm(self, MailAlarm):
        self._MailAlarm = MailAlarm

    @property
    def TrafficThreshold(self):
        return self._TrafficThreshold

    @TrafficThreshold.setter
    def TrafficThreshold(self, TrafficThreshold):
        self._TrafficThreshold = TrafficThreshold

    @property
    def EncryptKey(self):
        return self._EncryptKey

    @EncryptKey.setter
    def EncryptKey(self, EncryptKey):
        self._EncryptKey = EncryptKey

    @property
    def TopFullScreen(self):
        return self._TopFullScreen

    @TopFullScreen.setter
    def TopFullScreen(self, TopFullScreen):
        self._TopFullScreen = TopFullScreen

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SchemeColor = params.get("SchemeColor")
        self._Language = params.get("Language")
        self._SceneType = params.get("SceneType")
        self._EvilInterceptGrade = params.get("EvilInterceptGrade")
        self._SmartVerify = params.get("SmartVerify")
        self._SmartEngine = params.get("SmartEngine")
        self._CapType = params.get("CapType")
        self._AppName = params.get("AppName")
        self._DomainLimit = params.get("DomainLimit")
        self._MailAlarm = params.get("MailAlarm")
        self._TrafficThreshold = params.get("TrafficThreshold")
        self._EncryptKey = params.get("EncryptKey")
        self._TopFullScreen = params.get("TopFullScreen")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaDataRequest(AbstractModel):
    """DescribeCaptchaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _Start: 查询开始时间
        :type Start: int
        :param _End: 查询结束时间
        :type End: int
        :param _Type: 查询类型
        :type Type: int
        """
        self._CaptchaAppId = None
        self._Start = None
        self._End = None
        self._Type = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaDataResponse(AbstractModel):
    """DescribeCaptchaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 返回码 0 成功 其它失败
        :type CaptchaCode: int
        :param _Data: 数据数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CaptchaQueryData
        :param _CaptchaMsg: 返回信息描述
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._Data = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaptchaCode = params.get("CaptchaCode")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CaptchaQueryData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaDataSumRequest(AbstractModel):
    """DescribeCaptchaDataSum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _Start: 查询开始时间
        :type Start: int
        :param _End: 查询结束时间
        :type End: int
        """
        self._CaptchaAppId = None
        self._Start = None
        self._End = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaDataSumResponse(AbstractModel):
    """DescribeCaptchaDataSum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GetSum: 请求总量
        :type GetSum: int
        :param _VfySuccSum: 请求验证成功量
        :type VfySuccSum: int
        :param _VfySum: 请求验证量
        :type VfySum: int
        :param _AttackSum: 拦截攻击量
        :type AttackSum: int
        :param _CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _CaptchaCode: 成功返回0  其它失败
        :type CaptchaCode: int
        :param _CheckTicketSum: 票据校验总量
        :type CheckTicketSum: int
        :param _TicketThroughputSum: 票据验证通过量
        :type TicketThroughputSum: int
        :param _TicketInterceptSum: 票据验证拦截量
        :type TicketInterceptSum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GetSum = None
        self._VfySuccSum = None
        self._VfySum = None
        self._AttackSum = None
        self._CaptchaMsg = None
        self._CaptchaCode = None
        self._CheckTicketSum = None
        self._TicketThroughputSum = None
        self._TicketInterceptSum = None
        self._RequestId = None

    @property
    def GetSum(self):
        return self._GetSum

    @GetSum.setter
    def GetSum(self, GetSum):
        self._GetSum = GetSum

    @property
    def VfySuccSum(self):
        return self._VfySuccSum

    @VfySuccSum.setter
    def VfySuccSum(self, VfySuccSum):
        self._VfySuccSum = VfySuccSum

    @property
    def VfySum(self):
        return self._VfySum

    @VfySum.setter
    def VfySum(self, VfySum):
        self._VfySum = VfySum

    @property
    def AttackSum(self):
        return self._AttackSum

    @AttackSum.setter
    def AttackSum(self, AttackSum):
        self._AttackSum = AttackSum

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CheckTicketSum(self):
        return self._CheckTicketSum

    @CheckTicketSum.setter
    def CheckTicketSum(self, CheckTicketSum):
        self._CheckTicketSum = CheckTicketSum

    @property
    def TicketThroughputSum(self):
        return self._TicketThroughputSum

    @TicketThroughputSum.setter
    def TicketThroughputSum(self, TicketThroughputSum):
        self._TicketThroughputSum = TicketThroughputSum

    @property
    def TicketInterceptSum(self):
        return self._TicketInterceptSum

    @TicketInterceptSum.setter
    def TicketInterceptSum(self, TicketInterceptSum):
        self._TicketInterceptSum = TicketInterceptSum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GetSum = params.get("GetSum")
        self._VfySuccSum = params.get("VfySuccSum")
        self._VfySum = params.get("VfySum")
        self._AttackSum = params.get("AttackSum")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CheckTicketSum = params.get("CheckTicketSum")
        self._TicketThroughputSum = params.get("TicketThroughputSum")
        self._TicketInterceptSum = params.get("TicketInterceptSum")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaMiniDataRequest(AbstractModel):
    """DescribeCaptchaMiniData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _Start: 查询开始时间 例如：2019112900
        :type Start: int
        :param _End: 查询结束时间 例如：2019112902
        :type End: int
        :param _Type: 查询类型 安全验证码小程序插件分类查询数据接口，请求量type=0、通过量type=1、验证量type=2、拦截量type=3 小时级查询（五小时左右延迟）
        :type Type: int
        """
        self._CaptchaAppId = None
        self._Start = None
        self._End = None
        self._Type = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniDataResponse(AbstractModel):
    """DescribeCaptchaMiniData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 返回码 0 成功 其它失败
        :type CaptchaCode: int
        :param _Data: 数据数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CaptchaQueryData
        :param _CaptchaMsg: 返回信息描述
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._Data = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaptchaCode = params.get("CaptchaCode")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CaptchaQueryData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaMiniDataSumRequest(AbstractModel):
    """DescribeCaptchaMiniDataSum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _Start: 查询开始时间
        :type Start: int
        :param _End: 查询结束时间
        :type End: int
        """
        self._CaptchaAppId = None
        self._Start = None
        self._End = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniDataSumResponse(AbstractModel):
    """DescribeCaptchaMiniDataSum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GetSum: 请求总量
注意：此字段可能返回 null，表示取不到有效值。
        :type GetSum: int
        :param _VfySuccSum: 请求验证成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type VfySuccSum: int
        :param _VfySum: 请求验证量
注意：此字段可能返回 null，表示取不到有效值。
        :type VfySum: int
        :param _AttackSum: 拦截攻击量
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackSum: int
        :param _CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _CaptchaCode: 成功返回0  其它失败
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaCode: int
        :param _CheckTicketSum: 票据校验总量
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckTicketSum: int
        :param _TicketThroughputSum: 票据验证通过量
注意：此字段可能返回 null，表示取不到有效值。
        :type TicketThroughputSum: int
        :param _TicketInterceptSum: 票据验证拦截量
注意：此字段可能返回 null，表示取不到有效值。
        :type TicketInterceptSum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GetSum = None
        self._VfySuccSum = None
        self._VfySum = None
        self._AttackSum = None
        self._CaptchaMsg = None
        self._CaptchaCode = None
        self._CheckTicketSum = None
        self._TicketThroughputSum = None
        self._TicketInterceptSum = None
        self._RequestId = None

    @property
    def GetSum(self):
        return self._GetSum

    @GetSum.setter
    def GetSum(self, GetSum):
        self._GetSum = GetSum

    @property
    def VfySuccSum(self):
        return self._VfySuccSum

    @VfySuccSum.setter
    def VfySuccSum(self, VfySuccSum):
        self._VfySuccSum = VfySuccSum

    @property
    def VfySum(self):
        return self._VfySum

    @VfySum.setter
    def VfySum(self, VfySum):
        self._VfySum = VfySum

    @property
    def AttackSum(self):
        return self._AttackSum

    @AttackSum.setter
    def AttackSum(self, AttackSum):
        self._AttackSum = AttackSum

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CheckTicketSum(self):
        return self._CheckTicketSum

    @CheckTicketSum.setter
    def CheckTicketSum(self, CheckTicketSum):
        self._CheckTicketSum = CheckTicketSum

    @property
    def TicketThroughputSum(self):
        return self._TicketThroughputSum

    @TicketThroughputSum.setter
    def TicketThroughputSum(self, TicketThroughputSum):
        self._TicketThroughputSum = TicketThroughputSum

    @property
    def TicketInterceptSum(self):
        return self._TicketInterceptSum

    @TicketInterceptSum.setter
    def TicketInterceptSum(self, TicketInterceptSum):
        self._TicketInterceptSum = TicketInterceptSum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GetSum = params.get("GetSum")
        self._VfySuccSum = params.get("VfySuccSum")
        self._VfySum = params.get("VfySum")
        self._AttackSum = params.get("AttackSum")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CheckTicketSum = params.get("CheckTicketSum")
        self._TicketThroughputSum = params.get("TicketThroughputSum")
        self._TicketInterceptSum = params.get("TicketInterceptSum")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaMiniOperDataRequest(AbstractModel):
    """DescribeCaptchaMiniOperData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _Start: 查询开始时间
        :type Start: int
        :param _Type: 查询类型
        :type Type: int
        :param _End: 查询结束时间
        :type End: int
        """
        self._CaptchaAppId = None
        self._Start = None
        self._Type = None
        self._End = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._Start = params.get("Start")
        self._Type = params.get("Type")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniOperDataResponse(AbstractModel):
    """DescribeCaptchaMiniOperData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 成功返回 0 其它失败
        :type CaptchaCode: int
        :param _CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _Data: 用户操作数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaOperDataRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._Data = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        if params.get("Data") is not None:
            self._Data = CaptchaOperDataRes()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCaptchaMiniResultRequest(AbstractModel):
    """DescribeCaptchaMiniResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaType: 固定填值：9
        :type CaptchaType: int
        :param _Ticket: 验证码返回给用户的票据
        :type Ticket: str
        :param _UserIp: 业务侧获取到的验证码使用者的外网IP
        :type UserIp: str
        :param _CaptchaAppId: 验证码应用ID。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到CaptchaAppId。
        :type CaptchaAppId: int
        :param _AppSecretKey: 验证码应用密钥。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到AppSecretKey。AppSecretKey属于服务器端校验验证码票据的密钥，请妥善保密，请勿泄露给第三方。
        :type AppSecretKey: str
        :param _BusinessId: 业务 ID，网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据
        :type BusinessId: int
        :param _SceneId: 场景 ID，网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据
        :type SceneId: int
        :param _MacAddress: mac 地址或设备唯一标识
        :type MacAddress: str
        :param _Imei: 手机设备号
        :type Imei: str
        """
        self._CaptchaType = None
        self._Ticket = None
        self._UserIp = None
        self._CaptchaAppId = None
        self._AppSecretKey = None
        self._BusinessId = None
        self._SceneId = None
        self._MacAddress = None
        self._Imei = None

    @property
    def CaptchaType(self):
        return self._CaptchaType

    @CaptchaType.setter
    def CaptchaType(self, CaptchaType):
        self._CaptchaType = CaptchaType

    @property
    def Ticket(self):
        return self._Ticket

    @Ticket.setter
    def Ticket(self, Ticket):
        self._Ticket = Ticket

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppSecretKey(self):
        return self._AppSecretKey

    @AppSecretKey.setter
    def AppSecretKey(self, AppSecretKey):
        self._AppSecretKey = AppSecretKey

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def MacAddress(self):
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei


    def _deserialize(self, params):
        self._CaptchaType = params.get("CaptchaType")
        self._Ticket = params.get("Ticket")
        self._UserIp = params.get("UserIp")
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppSecretKey = params.get("AppSecretKey")
        self._BusinessId = params.get("BusinessId")
        self._SceneId = params.get("SceneId")
        self._MacAddress = params.get("MacAddress")
        self._Imei = params.get("Imei")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniResultResponse(AbstractModel):
    """DescribeCaptchaMiniResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 1     ticket verification succeeded     票据验证成功
7     CaptchaAppId does not match     票据与验证码应用APPID不匹配
8     ticket expired     票据超时
10    ticket format error     票据格式不正确
15    ticket decryption failed     票据解密失败
16    CaptchaAppId wrong format     检查验证码应用APPID错误
21    (1)ticket error     票据验证错误 (2)diff 一般是由于用户网络较差，导致前端自动容灾，而生成了容灾票据，业务侧可根据需要进行跳过或二次处理
25    invalid ticket     无效票据
26    system internal error     系统内部错误
31    UnauthorizedOperation.Unauthorized   无有效套餐包/账户已欠费
100   param err     参数校验错误
        :type CaptchaCode: int
        :param _CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaMiniRiskResultRequest(AbstractModel):
    """DescribeCaptchaMiniRiskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaType: 固定填值：9（滑块验证码）
        :type CaptchaType: int
        :param _Ticket: 验证码返回给用户的票据
        :type Ticket: str
        :param _UserIp: 业务侧获取到的验证码使用者的外网IP
        :type UserIp: str
        :param _CaptchaAppId: 验证码应用APPID
        :type CaptchaAppId: int
        :param _AppSecretKey: 用于服务器端校验验证码票据的验证密钥，请妥善保密，请勿泄露给第三方
        :type AppSecretKey: str
        :param _BusinessId: 业务 ID，网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据
        :type BusinessId: int
        :param _SceneId: 场景 ID，网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据
        :type SceneId: int
        :param _MacAddress: mac 地址或设备唯一标识
        :type MacAddress: str
        :param _Imei: 手机设备号
        :type Imei: str
        :param _SceneCode: 验证场景：1 活动防刷场景，2 登录保护场景，3 注册保护场景。根据需求选择场景参数。
        :type SceneCode: int
        :param _WeChatOpenId: 用户操作来源的微信开放账号
        :type WeChatOpenId: str
        """
        self._CaptchaType = None
        self._Ticket = None
        self._UserIp = None
        self._CaptchaAppId = None
        self._AppSecretKey = None
        self._BusinessId = None
        self._SceneId = None
        self._MacAddress = None
        self._Imei = None
        self._SceneCode = None
        self._WeChatOpenId = None

    @property
    def CaptchaType(self):
        return self._CaptchaType

    @CaptchaType.setter
    def CaptchaType(self, CaptchaType):
        self._CaptchaType = CaptchaType

    @property
    def Ticket(self):
        return self._Ticket

    @Ticket.setter
    def Ticket(self, Ticket):
        self._Ticket = Ticket

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppSecretKey(self):
        return self._AppSecretKey

    @AppSecretKey.setter
    def AppSecretKey(self, AppSecretKey):
        self._AppSecretKey = AppSecretKey

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def MacAddress(self):
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def SceneCode(self):
        return self._SceneCode

    @SceneCode.setter
    def SceneCode(self, SceneCode):
        self._SceneCode = SceneCode

    @property
    def WeChatOpenId(self):
        return self._WeChatOpenId

    @WeChatOpenId.setter
    def WeChatOpenId(self, WeChatOpenId):
        self._WeChatOpenId = WeChatOpenId


    def _deserialize(self, params):
        self._CaptchaType = params.get("CaptchaType")
        self._Ticket = params.get("Ticket")
        self._UserIp = params.get("UserIp")
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppSecretKey = params.get("AppSecretKey")
        self._BusinessId = params.get("BusinessId")
        self._SceneId = params.get("SceneId")
        self._MacAddress = params.get("MacAddress")
        self._Imei = params.get("Imei")
        self._SceneCode = params.get("SceneCode")
        self._WeChatOpenId = params.get("WeChatOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaMiniRiskResultResponse(AbstractModel):
    """DescribeCaptchaMiniRiskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 1 ticket verification succeeded 票据验证成功
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
        :param _CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _ManageMarketingRiskValue: 拦截策略返回信息
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ManageMarketingRiskValue: :class:`tencentcloud.captcha.v20190722.models.OutputManageMarketingRiskValue`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._ManageMarketingRiskValue = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def ManageMarketingRiskValue(self):
        return self._ManageMarketingRiskValue

    @ManageMarketingRiskValue.setter
    def ManageMarketingRiskValue(self, ManageMarketingRiskValue):
        self._ManageMarketingRiskValue = ManageMarketingRiskValue

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        if params.get("ManageMarketingRiskValue") is not None:
            self._ManageMarketingRiskValue = OutputManageMarketingRiskValue()
            self._ManageMarketingRiskValue._deserialize(params.get("ManageMarketingRiskValue"))
        self._RequestId = params.get("RequestId")


class DescribeCaptchaOperDataRequest(AbstractModel):
    """DescribeCaptchaOperData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _Start: 查询开始时间
        :type Start: int
        :param _Type: 查询类型
        :type Type: int
        :param _End: 查询结束时间
        :type End: int
        """
        self._CaptchaAppId = None
        self._Start = None
        self._Type = None
        self._End = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._Start = params.get("Start")
        self._Type = params.get("Type")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaOperDataResponse(AbstractModel):
    """DescribeCaptchaOperData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 成功返回 0 其它失败
        :type CaptchaCode: int
        :param _CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _Data: 用户操作数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaOperDataRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._Data = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        if params.get("Data") is not None:
            self._Data = CaptchaOperDataRes()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCaptchaRceResultRequest(AbstractModel):
    """DescribeCaptchaRceResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaType: 固定填值：9。
        :type CaptchaType: int
        :param _Ticket: 前端回调函数返回的用户验证票据
        :type Ticket: str
        :param _UserIp: 业务侧获取到的验证码使用者的外网IP
        :type UserIp: str
        :param _Randstr: 前端回调函数返回的随机字符串
        :type Randstr: str
        :param _CaptchaAppId: 验证码应用ID。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到CaptchaAppId。
        :type CaptchaAppId: int
        :param _AppSecretKey: 验证码应用密钥。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到AppSecretKey。AppSecretKey属于服务器端校验验证码票据的密钥，请妥善保密，请勿泄露给第三方。
        :type AppSecretKey: str
        :param _BusinessId: 预留字段
        :type BusinessId: int
        :param _SceneId: 预留字段
        :type SceneId: int
        :param _MacAddress: mac 地址或设备唯一标识
        :type MacAddress: str
        :param _Imei: 手机设备号
        :type Imei: str
        :param _NeedGetCaptchaTime: 是否返回前端获取验证码时间，取值1：需要返回
        :type NeedGetCaptchaTime: int
        """
        self._CaptchaType = None
        self._Ticket = None
        self._UserIp = None
        self._Randstr = None
        self._CaptchaAppId = None
        self._AppSecretKey = None
        self._BusinessId = None
        self._SceneId = None
        self._MacAddress = None
        self._Imei = None
        self._NeedGetCaptchaTime = None

    @property
    def CaptchaType(self):
        return self._CaptchaType

    @CaptchaType.setter
    def CaptchaType(self, CaptchaType):
        self._CaptchaType = CaptchaType

    @property
    def Ticket(self):
        return self._Ticket

    @Ticket.setter
    def Ticket(self, Ticket):
        self._Ticket = Ticket

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Randstr(self):
        return self._Randstr

    @Randstr.setter
    def Randstr(self, Randstr):
        self._Randstr = Randstr

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppSecretKey(self):
        return self._AppSecretKey

    @AppSecretKey.setter
    def AppSecretKey(self, AppSecretKey):
        self._AppSecretKey = AppSecretKey

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def MacAddress(self):
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def NeedGetCaptchaTime(self):
        return self._NeedGetCaptchaTime

    @NeedGetCaptchaTime.setter
    def NeedGetCaptchaTime(self, NeedGetCaptchaTime):
        self._NeedGetCaptchaTime = NeedGetCaptchaTime


    def _deserialize(self, params):
        self._CaptchaType = params.get("CaptchaType")
        self._Ticket = params.get("Ticket")
        self._UserIp = params.get("UserIp")
        self._Randstr = params.get("Randstr")
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppSecretKey = params.get("AppSecretKey")
        self._BusinessId = params.get("BusinessId")
        self._SceneId = params.get("SceneId")
        self._MacAddress = params.get("MacAddress")
        self._Imei = params.get("Imei")
        self._NeedGetCaptchaTime = params.get("NeedGetCaptchaTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaRceResultResponse(AbstractModel):
    """DescribeCaptchaRceResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 1 OK 验证通过
7 captcha no match 传入的Randstr不合法，请检查Randstr是否与前端返回的Randstr一致
8 ticket expired 传入的Ticket已过期（Ticket有效期5分钟），请重新生成Ticket、Randstr进行校验
9 ticket reused 传入的Ticket被重复使用，请重新生成Ticket、Randstr进行校验
15 decrypt fail 传入的Ticket不合法，请检查Ticket是否与前端返回的Ticket一致
16 appid-ticket mismatch 传入的CaptchaAppId错误，请检查CaptchaAppId是否与前端传入的CaptchaAppId一致，并且保障CaptchaAppId是从验证码控制台【验证管理】->【基础配置】中获取
21 diff 票据校验异常，可能的原因是（1）若Ticket包含trerror前缀，一般是由于用户网络较差，导致前端自动容灾，而生成了容灾票据，业务侧可根据需要进行跳过或二次处理。（2）若Ticket不包含trerror前缀，则是由于验证码风控系统发现请求有安全风险，业务侧可根据需要进行拦截。
100 appid-secretkey-ticket mismatch 参数校验错误，（1）请检查CaptchaAppId与AppSecretKey是否正确，CaptchaAppId、AppSecretKey需要在验证码控制台【验证管理】>【基础配置】中获取（2）请检查传入的Ticket是否由传入的CaptchaAppId生成
        :type CaptchaCode: int
        :param _CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _EvilLevel: 无感验证模式下，该参数返回验证结果：
EvilLevel=0 请求无恶意
EvilLevel=100 请求有恶意
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilLevel: int
        :param _GetCaptchaTime: 前端获取验证码时间，时间戳格式
注意：此字段可能返回 null，表示取不到有效值。
        :type GetCaptchaTime: int
        :param _EvilBitmap: 拦截类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilBitmap: int
        :param _SubmitCaptchaTime: 提交验证码时间
        :type SubmitCaptchaTime: int
        :param _RceResult: rce检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type RceResult: :class:`tencentcloud.captcha.v20190722.models.RceResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._EvilLevel = None
        self._GetCaptchaTime = None
        self._EvilBitmap = None
        self._SubmitCaptchaTime = None
        self._RceResult = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def EvilLevel(self):
        return self._EvilLevel

    @EvilLevel.setter
    def EvilLevel(self, EvilLevel):
        self._EvilLevel = EvilLevel

    @property
    def GetCaptchaTime(self):
        return self._GetCaptchaTime

    @GetCaptchaTime.setter
    def GetCaptchaTime(self, GetCaptchaTime):
        self._GetCaptchaTime = GetCaptchaTime

    @property
    def EvilBitmap(self):
        return self._EvilBitmap

    @EvilBitmap.setter
    def EvilBitmap(self, EvilBitmap):
        self._EvilBitmap = EvilBitmap

    @property
    def SubmitCaptchaTime(self):
        return self._SubmitCaptchaTime

    @SubmitCaptchaTime.setter
    def SubmitCaptchaTime(self, SubmitCaptchaTime):
        self._SubmitCaptchaTime = SubmitCaptchaTime

    @property
    def RceResult(self):
        return self._RceResult

    @RceResult.setter
    def RceResult(self, RceResult):
        self._RceResult = RceResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._EvilLevel = params.get("EvilLevel")
        self._GetCaptchaTime = params.get("GetCaptchaTime")
        self._EvilBitmap = params.get("EvilBitmap")
        self._SubmitCaptchaTime = params.get("SubmitCaptchaTime")
        if params.get("RceResult") is not None:
            self._RceResult = RceResult()
            self._RceResult._deserialize(params.get("RceResult"))
        self._RequestId = params.get("RequestId")


class DescribeCaptchaResultRequest(AbstractModel):
    """DescribeCaptchaResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaType: 固定填值：9。
        :type CaptchaType: int
        :param _Ticket: 前端回调函数返回的用户验证票据
        :type Ticket: str
        :param _UserIp: 业务侧获取到的验证码使用者的外网IP
        :type UserIp: str
        :param _Randstr: 前端回调函数返回的随机字符串
        :type Randstr: str
        :param _CaptchaAppId: 验证码应用ID。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到CaptchaAppId。
        :type CaptchaAppId: int
        :param _AppSecretKey: 验证码应用密钥。登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical)，在验证列表的【密钥】列，即可查看到AppSecretKey。AppSecretKey属于服务器端校验验证码票据的密钥，请妥善保密，请勿泄露给第三方。
        :type AppSecretKey: str
        :param _BusinessId: 预留字段
        :type BusinessId: int
        :param _SceneId: 预留字段
        :type SceneId: int
        :param _MacAddress: mac 地址或设备唯一标识
        :type MacAddress: str
        :param _Imei: 手机设备号
        :type Imei: str
        :param _NeedGetCaptchaTime: 是否返回前端获取验证码时间，取值1：需要返回
        :type NeedGetCaptchaTime: int
        """
        self._CaptchaType = None
        self._Ticket = None
        self._UserIp = None
        self._Randstr = None
        self._CaptchaAppId = None
        self._AppSecretKey = None
        self._BusinessId = None
        self._SceneId = None
        self._MacAddress = None
        self._Imei = None
        self._NeedGetCaptchaTime = None

    @property
    def CaptchaType(self):
        return self._CaptchaType

    @CaptchaType.setter
    def CaptchaType(self, CaptchaType):
        self._CaptchaType = CaptchaType

    @property
    def Ticket(self):
        return self._Ticket

    @Ticket.setter
    def Ticket(self, Ticket):
        self._Ticket = Ticket

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Randstr(self):
        return self._Randstr

    @Randstr.setter
    def Randstr(self, Randstr):
        self._Randstr = Randstr

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppSecretKey(self):
        return self._AppSecretKey

    @AppSecretKey.setter
    def AppSecretKey(self, AppSecretKey):
        self._AppSecretKey = AppSecretKey

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def MacAddress(self):
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def NeedGetCaptchaTime(self):
        return self._NeedGetCaptchaTime

    @NeedGetCaptchaTime.setter
    def NeedGetCaptchaTime(self, NeedGetCaptchaTime):
        self._NeedGetCaptchaTime = NeedGetCaptchaTime


    def _deserialize(self, params):
        self._CaptchaType = params.get("CaptchaType")
        self._Ticket = params.get("Ticket")
        self._UserIp = params.get("UserIp")
        self._Randstr = params.get("Randstr")
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppSecretKey = params.get("AppSecretKey")
        self._BusinessId = params.get("BusinessId")
        self._SceneId = params.get("SceneId")
        self._MacAddress = params.get("MacAddress")
        self._Imei = params.get("Imei")
        self._NeedGetCaptchaTime = params.get("NeedGetCaptchaTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaResultResponse(AbstractModel):
    """DescribeCaptchaResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 1 OK 验证通过
7 captcha no match 传入的Randstr不合法，请检查Randstr是否与前端返回的Randstr一致
8 ticket expired 传入的Ticket已过期（Ticket有效期5分钟），请重新生成Ticket、Randstr进行校验
9 ticket reused 传入的Ticket被重复使用，请重新生成Ticket、Randstr进行校验
15 decrypt fail 传入的Ticket不合法，请检查Ticket是否与前端返回的Ticket一致
16 appid-ticket mismatch 传入的CaptchaAppId错误，请检查CaptchaAppId是否与前端传入的CaptchaAppId一致，并且保障CaptchaAppId是从验证码控制台【验证管理】->【基础配置】中获取
21 diff 票据校验异常，可能的原因是（1）若Ticket包含trerror前缀，一般是由于用户网络较差，导致前端自动容灾，而生成了容灾票据，业务侧可根据需要进行跳过或二次处理。（2）若Ticket不包含trerror前缀，则是由于验证码风控系统发现请求有安全风险，业务侧可根据需要进行拦截。
100 appid-secretkey-ticket mismatch 参数校验错误，（1）请检查CaptchaAppId与AppSecretKey是否正确，CaptchaAppId、AppSecretKey需要在验证码控制台【验证管理】>【基础配置】中获取（2）请检查传入的Ticket是否由传入的CaptchaAppId生成
        :type CaptchaCode: int
        :param _CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _EvilLevel: 无感验证模式下，该参数返回验证结果：
EvilLevel=0 请求无恶意
EvilLevel=100 请求有恶意
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilLevel: int
        :param _GetCaptchaTime: 前端获取验证码时间，时间戳格式
注意：此字段可能返回 null，表示取不到有效值。
        :type GetCaptchaTime: int
        :param _EvilBitmap: 拦截类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilBitmap: int
        :param _SubmitCaptchaTime: 提交验证码时间
        :type SubmitCaptchaTime: int
        :param _DeviceRiskCategory: 设备风险大类
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceRiskCategory: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._EvilLevel = None
        self._GetCaptchaTime = None
        self._EvilBitmap = None
        self._SubmitCaptchaTime = None
        self._DeviceRiskCategory = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def EvilLevel(self):
        return self._EvilLevel

    @EvilLevel.setter
    def EvilLevel(self, EvilLevel):
        self._EvilLevel = EvilLevel

    @property
    def GetCaptchaTime(self):
        return self._GetCaptchaTime

    @GetCaptchaTime.setter
    def GetCaptchaTime(self, GetCaptchaTime):
        self._GetCaptchaTime = GetCaptchaTime

    @property
    def EvilBitmap(self):
        return self._EvilBitmap

    @EvilBitmap.setter
    def EvilBitmap(self, EvilBitmap):
        self._EvilBitmap = EvilBitmap

    @property
    def SubmitCaptchaTime(self):
        return self._SubmitCaptchaTime

    @SubmitCaptchaTime.setter
    def SubmitCaptchaTime(self, SubmitCaptchaTime):
        self._SubmitCaptchaTime = SubmitCaptchaTime

    @property
    def DeviceRiskCategory(self):
        return self._DeviceRiskCategory

    @DeviceRiskCategory.setter
    def DeviceRiskCategory(self, DeviceRiskCategory):
        self._DeviceRiskCategory = DeviceRiskCategory

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._EvilLevel = params.get("EvilLevel")
        self._GetCaptchaTime = params.get("GetCaptchaTime")
        self._EvilBitmap = params.get("EvilBitmap")
        self._SubmitCaptchaTime = params.get("SubmitCaptchaTime")
        self._DeviceRiskCategory = params.get("DeviceRiskCategory")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaTicketDataRequest(AbstractModel):
    """DescribeCaptchaTicketData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _Start: 查询开始时间 例如：20200909
        :type Start: int
        :param _End: 查询结束时间 例如：20220314
        :type End: int
        """
        self._CaptchaAppId = None
        self._Start = None
        self._End = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaTicketDataResponse(AbstractModel):
    """DescribeCaptchaTicketData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 成功返回 0 其它失败
        :type CaptchaCode: int
        :param _CaptchaMsg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _Data: 验证码票据信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaTicketDataRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._Data = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        if params.get("Data") is not None:
            self._Data = CaptchaTicketDataRes()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCaptchaUserAllAppIdRequest(AbstractModel):
    """DescribeCaptchaUserAllAppId请求参数结构体

    """


class DescribeCaptchaUserAllAppIdResponse(AbstractModel):
    """DescribeCaptchaUserAllAppId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 用户注册的所有Appid和应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CaptchaUserAllAppId
        :param _CaptchaCode: 成功返回 0  其它失败
        :type CaptchaCode: int
        :param _CaptchaMsg: 返回操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
                obj = CaptchaUserAllAppId()
                obj._deserialize(item)
                self._Data.append(obj)
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class GetRequestStatisticsRequest(AbstractModel):
    """GetRequestStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码AppId
        :type CaptchaAppId: str
        :param _StartTimeStr: 开始时间字符串
        :type StartTimeStr: str
        :param _EndTimeStr: 结束时间字符串
        :type EndTimeStr: str
        :param _Dimension: 查询粒度
        :type Dimension: str
        """
        self._CaptchaAppId = None
        self._StartTimeStr = None
        self._EndTimeStr = None
        self._Dimension = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def StartTimeStr(self):
        return self._StartTimeStr

    @StartTimeStr.setter
    def StartTimeStr(self, StartTimeStr):
        self._StartTimeStr = StartTimeStr

    @property
    def EndTimeStr(self):
        return self._EndTimeStr

    @EndTimeStr.setter
    def EndTimeStr(self, EndTimeStr):
        self._EndTimeStr = EndTimeStr

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._StartTimeStr = params.get("StartTimeStr")
        self._EndTimeStr = params.get("EndTimeStr")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestStatisticsResponse(AbstractModel):
    """GetRequestStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询后数据块
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaStatisticObj`
        :param _CaptchaCode: 验证码返回码
        :type CaptchaCode: int
        :param _CaptchaMsg: 验证码返回信息
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CaptchaStatisticObj()
            self._Data._deserialize(params.get("Data"))
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class GetTicketStatisticsRequest(AbstractModel):
    """GetTicketStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码AppId
        :type CaptchaAppId: str
        :param _StartTimeStr: 开始时间字符串
        :type StartTimeStr: str
        :param _EndTimeStr: 结束时间字符串
        :type EndTimeStr: str
        :param _Dimension: 查询粒度
        :type Dimension: str
        """
        self._CaptchaAppId = None
        self._StartTimeStr = None
        self._EndTimeStr = None
        self._Dimension = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def StartTimeStr(self):
        return self._StartTimeStr

    @StartTimeStr.setter
    def StartTimeStr(self, StartTimeStr):
        self._StartTimeStr = StartTimeStr

    @property
    def EndTimeStr(self):
        return self._EndTimeStr

    @EndTimeStr.setter
    def EndTimeStr(self, EndTimeStr):
        self._EndTimeStr = EndTimeStr

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._StartTimeStr = params.get("StartTimeStr")
        self._EndTimeStr = params.get("EndTimeStr")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTicketStatisticsResponse(AbstractModel):
    """GetTicketStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询后数据块
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaStatisticObj`
        :param _CaptchaCode: 验证码返回码
        :type CaptchaCode: int
        :param _CaptchaMsg: 验证码返回信息
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CaptchaStatisticObj()
            self._Data._deserialize(params.get("Data"))
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class GetTotalRequestStatisticsRequest(AbstractModel):
    """GetTotalRequestStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeStr: 开始时间字符串
        :type StartTimeStr: str
        :param _EndTimeStr: 结束时间字符串
        :type EndTimeStr: str
        :param _Dimension: 查询粒度
        :type Dimension: str
        """
        self._StartTimeStr = None
        self._EndTimeStr = None
        self._Dimension = None

    @property
    def StartTimeStr(self):
        return self._StartTimeStr

    @StartTimeStr.setter
    def StartTimeStr(self, StartTimeStr):
        self._StartTimeStr = StartTimeStr

    @property
    def EndTimeStr(self):
        return self._EndTimeStr

    @EndTimeStr.setter
    def EndTimeStr(self, EndTimeStr):
        self._EndTimeStr = EndTimeStr

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._StartTimeStr = params.get("StartTimeStr")
        self._EndTimeStr = params.get("EndTimeStr")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTotalRequestStatisticsResponse(AbstractModel):
    """GetTotalRequestStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询后数据块
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaStatisticObj`
        :param _CaptchaCode: 验证码返回码
        :type CaptchaCode: int
        :param _CaptchaMsg: 验证码返回信息
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CaptchaStatisticObj()
            self._Data._deserialize(params.get("Data"))
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class GetTotalTicketStatisticsRequest(AbstractModel):
    """GetTotalTicketStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeStr: 开始时间
        :type StartTimeStr: str
        :param _EndTimeStr: 结束时间
        :type EndTimeStr: str
        :param _Dimension: 查询粒度
分钟：“1”
小时：“2”
天：“3”
        :type Dimension: str
        """
        self._StartTimeStr = None
        self._EndTimeStr = None
        self._Dimension = None

    @property
    def StartTimeStr(self):
        return self._StartTimeStr

    @StartTimeStr.setter
    def StartTimeStr(self, StartTimeStr):
        self._StartTimeStr = StartTimeStr

    @property
    def EndTimeStr(self):
        return self._EndTimeStr

    @EndTimeStr.setter
    def EndTimeStr(self, EndTimeStr):
        self._EndTimeStr = EndTimeStr

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._StartTimeStr = params.get("StartTimeStr")
        self._EndTimeStr = params.get("EndTimeStr")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTotalTicketStatisticsResponse(AbstractModel):
    """GetTotalTicketStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.captcha.v20190722.models.CaptchaStatisticObj`
        :param _CaptchaCode: 返回码
        :type CaptchaCode: int
        :param _CaptchaMsg: 返回信息
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CaptchaStatisticObj()
            self._Data._deserialize(params.get("Data"))
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class InterceptPerTrendObj(AbstractModel):
    """拦截率趋势obj

    """

    def __init__(self):
        r"""
        :param _Ftime: 时间参数
        :type Ftime: str
        :param _RequestInterceptPer: 拦截率
        :type RequestInterceptPer: float
        :param _AnswerInterceptPer: 答案拦截率
        :type AnswerInterceptPer: float
        :param _PolicyInterceptPer: 策略拦截率
        :type PolicyInterceptPer: float
        """
        self._Ftime = None
        self._RequestInterceptPer = None
        self._AnswerInterceptPer = None
        self._PolicyInterceptPer = None

    @property
    def Ftime(self):
        return self._Ftime

    @Ftime.setter
    def Ftime(self, Ftime):
        self._Ftime = Ftime

    @property
    def RequestInterceptPer(self):
        return self._RequestInterceptPer

    @RequestInterceptPer.setter
    def RequestInterceptPer(self, RequestInterceptPer):
        self._RequestInterceptPer = RequestInterceptPer

    @property
    def AnswerInterceptPer(self):
        return self._AnswerInterceptPer

    @AnswerInterceptPer.setter
    def AnswerInterceptPer(self, AnswerInterceptPer):
        self._AnswerInterceptPer = AnswerInterceptPer

    @property
    def PolicyInterceptPer(self):
        return self._PolicyInterceptPer

    @PolicyInterceptPer.setter
    def PolicyInterceptPer(self, PolicyInterceptPer):
        self._PolicyInterceptPer = PolicyInterceptPer


    def _deserialize(self, params):
        self._Ftime = params.get("Ftime")
        self._RequestInterceptPer = params.get("RequestInterceptPer")
        self._AnswerInterceptPer = params.get("AnswerInterceptPer")
        self._PolicyInterceptPer = params.get("PolicyInterceptPer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputManageMarketingRiskValue(AbstractModel):
    """拦截策略返回信息

    """

    def __init__(self):
        r"""
        :param _UserId: 账号 ID。对应输入参数： AccountType 是 1 时，对应 QQ 的 OpenID。
AccountType 是 2 时，对应微信的 OpenID/UnionID。
AccountType 是 4 时，对应手机号。
AccountType 是 8 时，对应 imei、idfa、imeiMD5 或者 idfaMD5。
AccountType 是 0 时，对应账号信息。
AccountType 是 10004 时，对应手机号的 MD5。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _PostTime: 操作时间戳，单位秒（对应输入参数）。 
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: int
        :param _AssociateAccount: 对应输入参数，AccountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录 后关联业务自身的账号 ID。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param _UserIp: 业务详情。 注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param _RiskLevel: 风险值 pass : 无恶意
review：需要人工审核
reject：拒绝，高风险恶意
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param _RiskType: 风险类型，请查看下面详细说明 注意：此字段可能返回 null，表示取不到有效值。
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
        self._UserId = None
        self._PostTime = None
        self._AssociateAccount = None
        self._UserIp = None
        self._RiskLevel = None
        self._RiskType = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PostTime(self):
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def AssociateAccount(self):
        return self._AssociateAccount

    @AssociateAccount.setter
    def AssociateAccount(self, AssociateAccount):
        self._AssociateAccount = AssociateAccount

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def RiskLevel(self):
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskType(self):
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PostTime = params.get("PostTime")
        self._AssociateAccount = params.get("AssociateAccount")
        self._UserIp = params.get("UserIp")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskType = params.get("RiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RceResult(AbstractModel):
    """验证码拼装Rce结果，Rce结果部分

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _PostTime: 操作时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: int
        :param _AssociateAccount: 业务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param _UserIp: 用户Ip
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param _RiskLevel: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param _RiskType: 风险类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskType: list of int
        :param _ConstId: 设备唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConstId: str
        :param _RiskInformation: 风险扩展参数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInformation: str
        """
        self._UserId = None
        self._PostTime = None
        self._AssociateAccount = None
        self._UserIp = None
        self._RiskLevel = None
        self._RiskType = None
        self._ConstId = None
        self._RiskInformation = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PostTime(self):
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def AssociateAccount(self):
        return self._AssociateAccount

    @AssociateAccount.setter
    def AssociateAccount(self, AssociateAccount):
        self._AssociateAccount = AssociateAccount

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def RiskLevel(self):
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskType(self):
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def ConstId(self):
        return self._ConstId

    @ConstId.setter
    def ConstId(self, ConstId):
        self._ConstId = ConstId

    @property
    def RiskInformation(self):
        return self._RiskInformation

    @RiskInformation.setter
    def RiskInformation(self, RiskInformation):
        self._RiskInformation = RiskInformation


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PostTime = params.get("PostTime")
        self._AssociateAccount = params.get("AssociateAccount")
        self._UserIp = params.get("UserIp")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskType = params.get("RiskType")
        self._ConstId = params.get("ConstId")
        self._RiskInformation = params.get("RiskInformation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestTrendObj(AbstractModel):
    """验证码请求趋势图obj

    """

    def __init__(self):
        r"""
        :param _Ftime: 时间参数
        :type Ftime: str
        :param _RequestAction: 请求量
        :type RequestAction: int
        :param _RequestVerify: 验证量
        :type RequestVerify: int
        :param _RequestThroughput: 通过量
        :type RequestThroughput: int
        :param _RequestIntercept: 拦截量
        :type RequestIntercept: int
        """
        self._Ftime = None
        self._RequestAction = None
        self._RequestVerify = None
        self._RequestThroughput = None
        self._RequestIntercept = None

    @property
    def Ftime(self):
        return self._Ftime

    @Ftime.setter
    def Ftime(self, Ftime):
        self._Ftime = Ftime

    @property
    def RequestAction(self):
        return self._RequestAction

    @RequestAction.setter
    def RequestAction(self, RequestAction):
        self._RequestAction = RequestAction

    @property
    def RequestVerify(self):
        return self._RequestVerify

    @RequestVerify.setter
    def RequestVerify(self, RequestVerify):
        self._RequestVerify = RequestVerify

    @property
    def RequestThroughput(self):
        return self._RequestThroughput

    @RequestThroughput.setter
    def RequestThroughput(self, RequestThroughput):
        self._RequestThroughput = RequestThroughput

    @property
    def RequestIntercept(self):
        return self._RequestIntercept

    @RequestIntercept.setter
    def RequestIntercept(self, RequestIntercept):
        self._RequestIntercept = RequestIntercept


    def _deserialize(self, params):
        self._Ftime = params.get("Ftime")
        self._RequestAction = params.get("RequestAction")
        self._RequestVerify = params.get("RequestVerify")
        self._RequestThroughput = params.get("RequestThroughput")
        self._RequestIntercept = params.get("RequestIntercept")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketAmountUnit(AbstractModel):
    """DescribeCaptchaTicketData 返回的数据结构

    """

    def __init__(self):
        r"""
        :param _DateKey: 时间
        :type DateKey: str
        :param _Amount: 票据验证总量
        :type Amount: int
        """
        self._DateKey = None
        self._Amount = None

    @property
    def DateKey(self):
        return self._DateKey

    @DateKey.setter
    def DateKey(self, DateKey):
        self._DateKey = DateKey

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount


    def _deserialize(self, params):
        self._DateKey = params.get("DateKey")
        self._Amount = params.get("Amount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketCheckTrendObj(AbstractModel):
    """验证码票据校验趋势obj

    """

    def __init__(self):
        r"""
        :param _Ftime: 时间参数
        :type Ftime: str
        :param _TicketCount: 票据校验量
        :type TicketCount: int
        :param _TicketThroughput: 票据通过量
        :type TicketThroughput: int
        :param _TicketIntercept: 票据拦截量
        :type TicketIntercept: int
        """
        self._Ftime = None
        self._TicketCount = None
        self._TicketThroughput = None
        self._TicketIntercept = None

    @property
    def Ftime(self):
        return self._Ftime

    @Ftime.setter
    def Ftime(self, Ftime):
        self._Ftime = Ftime

    @property
    def TicketCount(self):
        return self._TicketCount

    @TicketCount.setter
    def TicketCount(self, TicketCount):
        self._TicketCount = TicketCount

    @property
    def TicketThroughput(self):
        return self._TicketThroughput

    @TicketThroughput.setter
    def TicketThroughput(self, TicketThroughput):
        self._TicketThroughput = TicketThroughput

    @property
    def TicketIntercept(self):
        return self._TicketIntercept

    @TicketIntercept.setter
    def TicketIntercept(self, TicketIntercept):
        self._TicketIntercept = TicketIntercept


    def _deserialize(self, params):
        self._Ftime = params.get("Ftime")
        self._TicketCount = params.get("TicketCount")
        self._TicketThroughput = params.get("TicketThroughput")
        self._TicketIntercept = params.get("TicketIntercept")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketInterceptUnit(AbstractModel):
    """DescribeCaptchaTicketData 返回的数据结构

    """

    def __init__(self):
        r"""
        :param _DateKey: 时间
        :type DateKey: str
        :param _Intercept: 票据验证拦截量
        :type Intercept: int
        """
        self._DateKey = None
        self._Intercept = None

    @property
    def DateKey(self):
        return self._DateKey

    @DateKey.setter
    def DateKey(self, DateKey):
        self._DateKey = DateKey

    @property
    def Intercept(self):
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept


    def _deserialize(self, params):
        self._DateKey = params.get("DateKey")
        self._Intercept = params.get("Intercept")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketThroughUnit(AbstractModel):
    """DescribeCaptchaTicketData 返回的数据结构

    """

    def __init__(self):
        r"""
        :param _DateKey: 时间
        :type DateKey: str
        :param _Through: 票据验证的通过量
        :type Through: int
        """
        self._DateKey = None
        self._Through = None

    @property
    def DateKey(self):
        return self._DateKey

    @DateKey.setter
    def DateKey(self, DateKey):
        self._DateKey = DateKey

    @property
    def Through(self):
        return self._Through

    @Through.setter
    def Through(self, Through):
        self._Through = Through


    def _deserialize(self, params):
        self._DateKey = params.get("DateKey")
        self._Through = params.get("Through")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCaptchaAppIdInfoRequest(AbstractModel):
    """UpdateCaptchaAppIdInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param _AppName: 应用名
        :type AppName: str
        :param _DomainLimit: 域名限制
        :type DomainLimit: str
        :param _SceneType: 场景类型
        :type SceneType: int
        :param _CapType: 验证码类型
        :type CapType: int
        :param _EvilInterceptGrade: 风险级别
        :type EvilInterceptGrade: int
        :param _SmartVerify: 智能检测
        :type SmartVerify: int
        :param _SmartEngine: 开启智能引擎
        :type SmartEngine: int
        :param _SchemeColor: web风格
        :type SchemeColor: str
        :param _CaptchaLanguage: 语言
        :type CaptchaLanguage: int
        :param _MailAlarm: 告警邮箱
        :type MailAlarm: str
        :param _TopFullScreen: 是否全屏
        :type TopFullScreen: int
        :param _TrafficThreshold: 流量限制
        :type TrafficThreshold: int
        """
        self._CaptchaAppId = None
        self._AppName = None
        self._DomainLimit = None
        self._SceneType = None
        self._CapType = None
        self._EvilInterceptGrade = None
        self._SmartVerify = None
        self._SmartEngine = None
        self._SchemeColor = None
        self._CaptchaLanguage = None
        self._MailAlarm = None
        self._TopFullScreen = None
        self._TrafficThreshold = None

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainLimit(self):
        return self._DomainLimit

    @DomainLimit.setter
    def DomainLimit(self, DomainLimit):
        self._DomainLimit = DomainLimit

    @property
    def SceneType(self):
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def CapType(self):
        return self._CapType

    @CapType.setter
    def CapType(self, CapType):
        self._CapType = CapType

    @property
    def EvilInterceptGrade(self):
        return self._EvilInterceptGrade

    @EvilInterceptGrade.setter
    def EvilInterceptGrade(self, EvilInterceptGrade):
        self._EvilInterceptGrade = EvilInterceptGrade

    @property
    def SmartVerify(self):
        return self._SmartVerify

    @SmartVerify.setter
    def SmartVerify(self, SmartVerify):
        self._SmartVerify = SmartVerify

    @property
    def SmartEngine(self):
        return self._SmartEngine

    @SmartEngine.setter
    def SmartEngine(self, SmartEngine):
        self._SmartEngine = SmartEngine

    @property
    def SchemeColor(self):
        return self._SchemeColor

    @SchemeColor.setter
    def SchemeColor(self, SchemeColor):
        self._SchemeColor = SchemeColor

    @property
    def CaptchaLanguage(self):
        return self._CaptchaLanguage

    @CaptchaLanguage.setter
    def CaptchaLanguage(self, CaptchaLanguage):
        self._CaptchaLanguage = CaptchaLanguage

    @property
    def MailAlarm(self):
        return self._MailAlarm

    @MailAlarm.setter
    def MailAlarm(self, MailAlarm):
        self._MailAlarm = MailAlarm

    @property
    def TopFullScreen(self):
        return self._TopFullScreen

    @TopFullScreen.setter
    def TopFullScreen(self, TopFullScreen):
        self._TopFullScreen = TopFullScreen

    @property
    def TrafficThreshold(self):
        return self._TrafficThreshold

    @TrafficThreshold.setter
    def TrafficThreshold(self, TrafficThreshold):
        self._TrafficThreshold = TrafficThreshold


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppName = params.get("AppName")
        self._DomainLimit = params.get("DomainLimit")
        self._SceneType = params.get("SceneType")
        self._CapType = params.get("CapType")
        self._EvilInterceptGrade = params.get("EvilInterceptGrade")
        self._SmartVerify = params.get("SmartVerify")
        self._SmartEngine = params.get("SmartEngine")
        self._SchemeColor = params.get("SchemeColor")
        self._CaptchaLanguage = params.get("CaptchaLanguage")
        self._MailAlarm = params.get("MailAlarm")
        self._TopFullScreen = params.get("TopFullScreen")
        self._TrafficThreshold = params.get("TrafficThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCaptchaAppIdInfoResponse(AbstractModel):
    """UpdateCaptchaAppIdInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: 返回码 0 成功，其它失败
        :type CaptchaCode: int
        :param _CaptchaMsg: 返回操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")