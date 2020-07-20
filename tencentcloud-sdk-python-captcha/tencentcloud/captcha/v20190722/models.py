# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class CaptchaOperDataInterceptUnit(AbstractModel):
    """DescribeCaptchaOperData方法 拦截情况type = 2 返回的数据结构

    """

    def __init__(self):
        """
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


class CaptchaOperDataLoadTimeUnit(AbstractModel):
    """操作数据查询方法DescribeCaptchaOperData 的返回结果，安全验证码加载耗时type = 1

    """

    def __init__(self):
        """
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


class CaptchaOperDataRes(AbstractModel):
    """DescribeCaptchaOperData 接口 返回数据类型集合

    """

    def __init__(self):
        """
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


class CaptchaOperDataTryTimesDistributeUnit(AbstractModel):
    """DescribeCaptchaOperData方法 尝试次数分布 type = 4

    """

    def __init__(self):
        """
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


class CaptchaOperDataTryTimesUnit(AbstractModel):
    """DescribeCaptchaOperData操作数据查询尝试次数 type = 3

    """

    def __init__(self):
        """
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


class CaptchaQueryData(AbstractModel):
    """该类型为DescribeCaptchaData 方法返回数据类型

    """

    def __init__(self):
        """
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


class CaptchaUserAllAppId(AbstractModel):
    """用户注册的APPID和应用名称对象

    """

    def __init__(self):
        """
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param AppName: 注册应用名称
        :type AppName: str
        :param TcAppId: 腾讯云APPID
        :type TcAppId: int
        """
        self.CaptchaAppId = None
        self.AppName = None
        self.TcAppId = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppName = params.get("AppName")
        self.TcAppId = params.get("TcAppId")


class DescribeCaptchaAppIdInfoRequest(AbstractModel):
    """DescribeCaptchaAppIdInfo请求参数结构体

    """

    def __init__(self):
        """
        :param CaptchaAppId: 验证码应用注册APPID
        :type CaptchaAppId: int
        """
        self.CaptchaAppId = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")


class DescribeCaptchaAppIdInfoResponse(AbstractModel):
    """DescribeCaptchaAppIdInfo返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeCaptchaDataResponse(AbstractModel):
    """DescribeCaptchaData返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeCaptchaDataSumResponse(AbstractModel):
    """DescribeCaptchaDataSum返回参数结构体

    """

    def __init__(self):
        """
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
        :param CheckTicketSum: 票据校验量
        :type CheckTicketSum: int
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
        self.RequestId = None


    def _deserialize(self, params):
        self.GetSum = params.get("GetSum")
        self.VfySuccSum = params.get("VfySuccSum")
        self.VfySum = params.get("VfySum")
        self.AttackSum = params.get("AttackSum")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.CaptchaCode = params.get("CaptchaCode")
        self.CheckTicketSum = params.get("CheckTicketSum")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaOperDataRequest(AbstractModel):
    """DescribeCaptchaOperData请求参数结构体

    """

    def __init__(self):
        """
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param Start: 查询开始时间
        :type Start: int
        :param Type: 查询类型
        :type Type: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.Type = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.Type = params.get("Type")


class DescribeCaptchaOperDataResponse(AbstractModel):
    """DescribeCaptchaOperData返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param CaptchaType: 固定填值：9。可在控制台配置不同验证码类型。
        :type CaptchaType: int
        :param Ticket: 前端回调函数返回的用户验证票据
        :type Ticket: str
        :param UserIp: 用户操作来源的外网 IP
        :type UserIp: str
        :param Randstr: 前端回调函数返回的随机字符串
        :type Randstr: str
        :param CaptchaAppId: 验证码应用ID
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


class DescribeCaptchaResultResponse(AbstractModel):
    """DescribeCaptchaResult返回参数结构体

    """

    def __init__(self):
        """
        :param CaptchaCode: 1	OK	验证通过
6	user code len error	验证码长度不匹配
7	captcha no match	验证码答案不匹配/Randstr参数不匹配
8	verify timeout	验证码签名超时
9	Sequnce repeat	验证码签名重放
10	Sequnce invalid	验证码签名序列
11	Cookie invalid	验证码cooking信息不合法
12	sig len error	签名长度错误
13	verify ip no match	ip不匹配
15	decrypt fail	验证码签名解密失败
16	appid no match	验证码强校验appid错误
17	cmd no much	验证码系统命令不匹配
18	uin no match	号码不匹配
19	seq redirect	重定向验证
20	opt no vcode	操作使用pt免验证码校验错误
21	diff	差别，验证错误
22	captcha type not match	验证码类型与拉取时不一致
23	verify type error	验证类型错误
24	invalid pkg	非法请求包
25	bad visitor	策略拦截
26	system busy	系统内部错误
100	param err	appsecretkey 参数校验错误
        :type CaptchaCode: int
        :param CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param EvilLevel: [0,100]，恶意等级
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


class DescribeCaptchaUserAllAppIdRequest(AbstractModel):
    """DescribeCaptchaUserAllAppId请求参数结构体

    """


class DescribeCaptchaUserAllAppIdResponse(AbstractModel):
    """DescribeCaptchaUserAllAppId返回参数结构体

    """

    def __init__(self):
        """
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


class UpdateCaptchaAppIdInfoRequest(AbstractModel):
    """UpdateCaptchaAppIdInfo请求参数结构体

    """

    def __init__(self):
        """
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


class UpdateCaptchaAppIdInfoResponse(AbstractModel):
    """UpdateCaptchaAppIdInfo返回参数结构体

    """

    def __init__(self):
        """
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