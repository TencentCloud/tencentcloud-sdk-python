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


class AddPromotionEvent(AbstractModel):
    r"""参加营销活动事件详情

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>营销活动ID</p>
        :type PromotionId: str
        :param _PromotionName: <p>营销活动名称</p>
        :type PromotionName: str
        :param _Description: <p>营销活动描述</p>
        :type Description: str
        :param _InviterUserId: <p>邀请人ID</p>
        :type InviterUserId: str
        :param _Coupon: <p>营销活动关联的优惠券</p>
        :type Coupon: :class:`tencentcloud.rce.v20260130.models.Coupon`
        :param _Point: <p>营销活动关联的积分活动</p>
        :type Point: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        :param _Result: <p>参加营销活动结果</p>
        :type Result: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._Coupon = None
        self._Point = None
        self._Result = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>营销活动ID</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>营销活动名称</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>营销活动描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>邀请人ID</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def Coupon(self):
        r"""<p>营销活动关联的优惠券</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Coupon`
        """
        return self._Coupon

    @Coupon.setter
    def Coupon(self, Coupon):
        self._Coupon = Coupon

    @property
    def Point(self):
        r"""<p>营销活动关联的积分活动</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        """
        return self._Point

    @Point.setter
    def Point(self, Point):
        self._Point = Point

    @property
    def Result(self):
        r"""<p>参加营销活动结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        if params.get("Coupon") is not None:
            self._Coupon = Coupon()
            self._Coupon._deserialize(params.get("Coupon"))
        if params.get("Point") is not None:
            self._Point = CreditPoint()
            self._Point._deserialize(params.get("Point"))
        if params.get("Result") is not None:
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Address(AbstractModel):
    r"""地址

    """

    def __init__(self):
        r"""
        :param _Country: <p>国家</p><p>参数格式：符合ISO 3166标准</p>
        :type Country: str
        :param _Region: <p>省份</p>
        :type Region: str
        :param _City: <p>城市</p>
        :type City: str
        :param _District: <p>地区</p>
        :type District: str
        :param _Detail: <p>详细地址</p>
        :type Detail: str
        :param _ZipCode: <p>邮政编码</p>
        :type ZipCode: str
        """
        self._Country = None
        self._Region = None
        self._City = None
        self._District = None
        self._Detail = None
        self._ZipCode = None

    @property
    def Country(self):
        r"""<p>国家</p><p>参数格式：符合ISO 3166标准</p>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Region(self):
        r"""<p>省份</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def City(self):
        r"""<p>城市</p>
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        r"""<p>地区</p>
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Detail(self):
        r"""<p>详细地址</p>
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def ZipCode(self):
        r"""<p>邮政编码</p>
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._Region = params.get("Region")
        self._City = params.get("City")
        self._District = params.get("District")
        self._Detail = params.get("Detail")
        self._ZipCode = params.get("ZipCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Amount(AbstractModel):
    r"""金额

    """

    def __init__(self):
        r"""
        :param _Currency: <p>原始货币类型</p><p>参数格式：符合ISO 4217标准</p>
        :type Currency: str
        :param _OriginalAmount: <p>原始金额</p>
        :type OriginalAmount: float
        :param _ExchangeRateUSD: <p>当前币种对美金的汇率</p>
        :type ExchangeRateUSD: float
        :param _ExchangeRateCNY: <p>当前币种对人民币的汇率</p>
        :type ExchangeRateCNY: float
        """
        self._Currency = None
        self._OriginalAmount = None
        self._ExchangeRateUSD = None
        self._ExchangeRateCNY = None

    @property
    def Currency(self):
        r"""<p>原始货币类型</p><p>参数格式：符合ISO 4217标准</p>
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def OriginalAmount(self):
        r"""<p>原始金额</p>
        :rtype: float
        """
        return self._OriginalAmount

    @OriginalAmount.setter
    def OriginalAmount(self, OriginalAmount):
        self._OriginalAmount = OriginalAmount

    @property
    def ExchangeRateUSD(self):
        r"""<p>当前币种对美金的汇率</p>
        :rtype: float
        """
        return self._ExchangeRateUSD

    @ExchangeRateUSD.setter
    def ExchangeRateUSD(self, ExchangeRateUSD):
        self._ExchangeRateUSD = ExchangeRateUSD

    @property
    def ExchangeRateCNY(self):
        r"""<p>当前币种对人民币的汇率</p>
        :rtype: float
        """
        return self._ExchangeRateCNY

    @ExchangeRateCNY.setter
    def ExchangeRateCNY(self, ExchangeRateCNY):
        self._ExchangeRateCNY = ExchangeRateCNY


    def _deserialize(self, params):
        self._Currency = params.get("Currency")
        self._OriginalAmount = params.get("OriginalAmount")
        self._ExchangeRateUSD = params.get("ExchangeRateUSD")
        self._ExchangeRateCNY = params.get("ExchangeRateCNY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class App(AbstractModel):
    r"""应用程序信息

    """

    def __init__(self):
        r"""
        :param _OS: <p>应用程序运行的移动设备的操作系统类型</p>
        :type OS: str
        :param _OSVersion: <p>应用程序运行的移动设备的操作系统版本</p>
        :type OSVersion: str
        :param _DeviceManufacturer: <p>应用程序运行的移动设备的生产厂商</p>
        :type DeviceManufacturer: str
        :param _DeviceModel: <p>应用程序运行的移动设备的型号</p>
        :type DeviceModel: str
        :param _DeviceId: <p>应用程序运行的移动设备的唯一ID，对于iOS为IFV标识，对于Android为Android ID</p>
        :type DeviceId: str
        :param _AppName: <p>应用程序名称</p>
        :type AppName: str
        :param _AppVersion: <p>应用程序版本</p>
        :type AppVersion: str
        :param _ClientLanguage: <p>应用程序提供的语言</p>
        :type ClientLanguage: str
        """
        self._OS = None
        self._OSVersion = None
        self._DeviceManufacturer = None
        self._DeviceModel = None
        self._DeviceId = None
        self._AppName = None
        self._AppVersion = None
        self._ClientLanguage = None

    @property
    def OS(self):
        r"""<p>应用程序运行的移动设备的操作系统类型</p>
        :rtype: str
        """
        return self._OS

    @OS.setter
    def OS(self, OS):
        self._OS = OS

    @property
    def OSVersion(self):
        r"""<p>应用程序运行的移动设备的操作系统版本</p>
        :rtype: str
        """
        return self._OSVersion

    @OSVersion.setter
    def OSVersion(self, OSVersion):
        self._OSVersion = OSVersion

    @property
    def DeviceManufacturer(self):
        r"""<p>应用程序运行的移动设备的生产厂商</p>
        :rtype: str
        """
        return self._DeviceManufacturer

    @DeviceManufacturer.setter
    def DeviceManufacturer(self, DeviceManufacturer):
        self._DeviceManufacturer = DeviceManufacturer

    @property
    def DeviceModel(self):
        r"""<p>应用程序运行的移动设备的型号</p>
        :rtype: str
        """
        return self._DeviceModel

    @DeviceModel.setter
    def DeviceModel(self, DeviceModel):
        self._DeviceModel = DeviceModel

    @property
    def DeviceId(self):
        r"""<p>应用程序运行的移动设备的唯一ID，对于iOS为IFV标识，对于Android为Android ID</p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def AppName(self):
        r"""<p>应用程序名称</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        r"""<p>应用程序版本</p>
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def ClientLanguage(self):
        r"""<p>应用程序提供的语言</p>
        :rtype: str
        """
        return self._ClientLanguage

    @ClientLanguage.setter
    def ClientLanguage(self, ClientLanguage):
        self._ClientLanguage = ClientLanguage


    def _deserialize(self, params):
        self._OS = params.get("OS")
        self._OSVersion = params.get("OSVersion")
        self._DeviceManufacturer = params.get("DeviceManufacturer")
        self._DeviceModel = params.get("DeviceModel")
        self._DeviceId = params.get("DeviceId")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._ClientLanguage = params.get("ClientLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessDeviceRiskPremiumProRequest(AbstractModel):
    r"""AssessDeviceRiskPremiumPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceToken: <p>用户设备指纹token标识，在您的网站或者应用程序中集成设备指纹的SDK后获取</p>
        :type DeviceToken: str
        :param _UserIp: <p>客户端 IP 地址（IPv4或IPv6）</p>
        :type UserIp: str
        """
        self._DeviceToken = None
        self._UserIp = None

    @property
    def DeviceToken(self):
        r"""<p>用户设备指纹token标识，在您的网站或者应用程序中集成设备指纹的SDK后获取</p>
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def UserIp(self):
        r"""<p>客户端 IP 地址（IPv4或IPv6）</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessDeviceRiskPremiumProResponse(AbstractModel):
    r"""AssessDeviceRiskPremiumPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>设备风险评估高级版返回结果</p>
        :type Data: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskPremiumRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>设备风险评估高级版返回结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskPremiumRsp`
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
            self._Data = AssessDeviceRiskPremiumRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AssessDeviceRiskPremiumRsp(AbstractModel):
    r"""设备风险评估高级版返回结果

    """

    def __init__(self):
        r"""
        :param _Decision: <p>决策信息</p>
        :type Decision: :class:`tencentcloud.rce.v20260130.models.Decision`
        :param _Score: <p>设备风险分信息</p>
        :type Score: :class:`tencentcloud.rce.v20260130.models.DataScore`
        :param _Device: <p>设备基础信息</p>
        :type Device: :class:`tencentcloud.rce.v20260130.models.Device`
        :param _Environment: <p>IP环境基础信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Environment: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        self._Decision = None
        self._Score = None
        self._Device = None
        self._Environment = None

    @property
    def Decision(self):
        r"""<p>决策信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Decision`
        """
        return self._Decision

    @Decision.setter
    def Decision(self, Decision):
        self._Decision = Decision

    @property
    def Score(self):
        r"""<p>设备风险分信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataScore`
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Device(self):
        r"""<p>设备基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Environment(self):
        r"""<p>IP环境基础信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        if params.get("Decision") is not None:
            self._Decision = Decision()
            self._Decision._deserialize(params.get("Decision"))
        if params.get("Score") is not None:
            self._Score = DataScore()
            self._Score._deserialize(params.get("Score"))
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessDeviceRiskProRequest(AbstractModel):
    r"""AssessDeviceRiskPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceToken: <p>用户设备指纹token标识，在您的网站或者应用程序中集成设备指纹的SDK后获取</p>
        :type DeviceToken: str
        :param _UserIp: <p>客户端 IP 地址（IPv4或IPv6）</p>
        :type UserIp: str
        """
        self._DeviceToken = None
        self._UserIp = None

    @property
    def DeviceToken(self):
        r"""<p>用户设备指纹token标识，在您的网站或者应用程序中集成设备指纹的SDK后获取</p>
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def UserIp(self):
        r"""<p>客户端 IP 地址（IPv4或IPv6）</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessDeviceRiskProResponse(AbstractModel):
    r"""AssessDeviceRiskPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>设备风险评估基础版返回结果</p>
        :type Data: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>设备风险评估基础版返回结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskRsp`
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
            self._Data = AssessDeviceRiskRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AssessDeviceRiskRsp(AbstractModel):
    r"""设备风险评估基础版返回结果

    """

    def __init__(self):
        r"""
        :param _Score: <p>设备风险分信息</p>
        :type Score: :class:`tencentcloud.rce.v20260130.models.DataScore`
        :param _Device: <p>设备基础信息</p>
        :type Device: :class:`tencentcloud.rce.v20260130.models.Device`
        :param _Environment: <p>IP环境基础信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Environment: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        self._Score = None
        self._Device = None
        self._Environment = None

    @property
    def Score(self):
        r"""<p>设备风险分信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataScore`
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Device(self):
        r"""<p>设备基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Environment(self):
        r"""<p>IP环境基础信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        if params.get("Score") is not None:
            self._Score = DataScore()
            self._Score._deserialize(params.get("Score"))
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessEnvironmentRiskRequest(AbstractModel):
    r"""AssessEnvironmentRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIp: <p>客户端 IP 地址（IPv4或IPv6）</p>
        :type UserIp: str
        """
        self._UserIp = None

    @property
    def UserIp(self):
        r"""<p>客户端 IP 地址（IPv4或IPv6）</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessEnvironmentRiskResponse(AbstractModel):
    r"""AssessEnvironmentRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>环境风险评估返回结果</p>
        :type Data: :class:`tencentcloud.rce.v20260130.models.AssessEnvironmentRiskRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>环境风险评估返回结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessEnvironmentRiskRsp`
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
            self._Data = AssessEnvironmentRiskRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AssessEnvironmentRiskRsp(AbstractModel):
    r"""环境风险评估返回结果

    """

    def __init__(self):
        r"""
        :param _Score: <p>IP环境风险分信息</p>
        :type Score: :class:`tencentcloud.rce.v20260130.models.DataScore`
        :param _Environment: <p>IP环境基础信息</p>
        :type Environment: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        self._Score = None
        self._Environment = None

    @property
    def Score(self):
        r"""<p>IP环境风险分信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataScore`
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Environment(self):
        r"""<p>IP环境基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        if params.get("Score") is not None:
            self._Score = DataScore()
            self._Score._deserialize(params.get("Score"))
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessRiskRequest(AbstractModel):
    r"""AssessRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventCode: <p>事件码，标准事件包含：</p><p>枚举值：</p><ul><li>login： 登录</li><li>register： 注册</li><li>create_order： 创建订单</li><li>transaction： 交易支付</li><li>charge_back： 拒付</li><li>sms： 短信</li><li>logout： 登出</li><li>modify_account： 修改账号</li><li>modify_password： 修改密码</li><li>security_verification： 安全验证</li><li>add_promotion： 参加营销活动</li><li>redeem： 兑奖</li><li>withdraw： 提现</li><li>cust_event： 自定义事件，cust_xxx</li><li>scan_code： 扫码</li><li>lucky_draw： 抽奖</li><li>task： 做任务</li><li>invitation： 邀请</li><li>claim_red_packet： 领红包</li><li>browse： 浏览</li></ul><p>自定义事件可与RCE约定后进行风险评估</p>
        :type EventCode: str
        :param _EventTime: <p>事件的发生时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :type EventTime: str
        :param _SessionId: <p>用户当前会话 ID， 用于关联用户登录前后的动作，如果没有传UserId，则SessionId必传，如缺失则可填充空字符串</p>
        :type SessionId: str
        :param _DeviceToken: <p>用户设备指纹token标识，在您的网站或者应用程序中集成设备指纹的SDK后获取</p>
        :type DeviceToken: str
        :param _UserIp: <p>客户端 IP 地址（IPv4或IPv6）</p>
        :type UserIp: str
        :param _EventDetail: <p>事件详情，根据您输入的事件码传入对应的事件信息</p>
        :type EventDetail: :class:`tencentcloud.rce.v20260130.models.EventDetail`
        :param _UserId: <p>用户在您系统中的唯一ID</p>
        :type UserId: str
        :param _UserEmail: <p>用户邮箱</p>
        :type UserEmail: str
        :param _UserPhone: <p>用户提供的联系方式</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :type UserPhone: str
        :param _Browser: <p>web浏览器相关信息，若您已集成我们的设备指纹SDK，则无需传入此字段</p>
        :type Browser: :class:`tencentcloud.rce.v20260130.models.Browser`
        :param _App: <p>应用程序、操作系统和移动设备详细信息，若您已集成我们的设备指纹SDK，则无需传入此字段</p>
        :type App: :class:`tencentcloud.rce.v20260130.models.App`
        :param _DataAuthorization: <p>数据授权信息，国内地域必填</p>
        :type DataAuthorization: :class:`tencentcloud.rce.v20260130.models.DataAuthorization`
        :param _UserPhoneEncrypt: <p>手机号码加密方式，国内地域必填</p><p>枚举值：</p><ul><li>md5： md5加密</li><li>plain： 明文</li></ul>
        :type UserPhoneEncrypt: str
        :param _WeChatOpenId: <p>微信开放账号</p>
        :type WeChatOpenId: str
        :param _QQOpenId: <p>QQ开放账号</p>
        :type QQOpenId: str
        :param _QQAppId: <p>QQ应用ID，当传入QQ开放账号时，该字段必填，QQ分配给网站或应用的AppId，用来唯一标识网站或应用</p>
        :type QQAppId: str
        """
        self._EventCode = None
        self._EventTime = None
        self._SessionId = None
        self._DeviceToken = None
        self._UserIp = None
        self._EventDetail = None
        self._UserId = None
        self._UserEmail = None
        self._UserPhone = None
        self._Browser = None
        self._App = None
        self._DataAuthorization = None
        self._UserPhoneEncrypt = None
        self._WeChatOpenId = None
        self._QQOpenId = None
        self._QQAppId = None

    @property
    def EventCode(self):
        r"""<p>事件码，标准事件包含：</p><p>枚举值：</p><ul><li>login： 登录</li><li>register： 注册</li><li>create_order： 创建订单</li><li>transaction： 交易支付</li><li>charge_back： 拒付</li><li>sms： 短信</li><li>logout： 登出</li><li>modify_account： 修改账号</li><li>modify_password： 修改密码</li><li>security_verification： 安全验证</li><li>add_promotion： 参加营销活动</li><li>redeem： 兑奖</li><li>withdraw： 提现</li><li>cust_event： 自定义事件，cust_xxx</li><li>scan_code： 扫码</li><li>lucky_draw： 抽奖</li><li>task： 做任务</li><li>invitation： 邀请</li><li>claim_red_packet： 领红包</li><li>browse： 浏览</li></ul><p>自定义事件可与RCE约定后进行风险评估</p>
        :rtype: str
        """
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventTime(self):
        r"""<p>事件的发生时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def SessionId(self):
        r"""<p>用户当前会话 ID， 用于关联用户登录前后的动作，如果没有传UserId，则SessionId必传，如缺失则可填充空字符串</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def DeviceToken(self):
        r"""<p>用户设备指纹token标识，在您的网站或者应用程序中集成设备指纹的SDK后获取</p>
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def UserIp(self):
        r"""<p>客户端 IP 地址（IPv4或IPv6）</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def EventDetail(self):
        r"""<p>事件详情，根据您输入的事件码传入对应的事件信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.EventDetail`
        """
        return self._EventDetail

    @EventDetail.setter
    def EventDetail(self, EventDetail):
        self._EventDetail = EventDetail

    @property
    def UserId(self):
        r"""<p>用户在您系统中的唯一ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserEmail(self):
        r"""<p>用户邮箱</p>
        :rtype: str
        """
        return self._UserEmail

    @UserEmail.setter
    def UserEmail(self, UserEmail):
        self._UserEmail = UserEmail

    @property
    def UserPhone(self):
        r"""<p>用户提供的联系方式</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :rtype: str
        """
        return self._UserPhone

    @UserPhone.setter
    def UserPhone(self, UserPhone):
        self._UserPhone = UserPhone

    @property
    def Browser(self):
        r"""<p>web浏览器相关信息，若您已集成我们的设备指纹SDK，则无需传入此字段</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Browser`
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def App(self):
        r"""<p>应用程序、操作系统和移动设备详细信息，若您已集成我们的设备指纹SDK，则无需传入此字段</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.App`
        """
        return self._App

    @App.setter
    def App(self, App):
        self._App = App

    @property
    def DataAuthorization(self):
        r"""<p>数据授权信息，国内地域必填</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataAuthorization`
        """
        return self._DataAuthorization

    @DataAuthorization.setter
    def DataAuthorization(self, DataAuthorization):
        self._DataAuthorization = DataAuthorization

    @property
    def UserPhoneEncrypt(self):
        r"""<p>手机号码加密方式，国内地域必填</p><p>枚举值：</p><ul><li>md5： md5加密</li><li>plain： 明文</li></ul>
        :rtype: str
        """
        return self._UserPhoneEncrypt

    @UserPhoneEncrypt.setter
    def UserPhoneEncrypt(self, UserPhoneEncrypt):
        self._UserPhoneEncrypt = UserPhoneEncrypt

    @property
    def WeChatOpenId(self):
        r"""<p>微信开放账号</p>
        :rtype: str
        """
        return self._WeChatOpenId

    @WeChatOpenId.setter
    def WeChatOpenId(self, WeChatOpenId):
        self._WeChatOpenId = WeChatOpenId

    @property
    def QQOpenId(self):
        r"""<p>QQ开放账号</p>
        :rtype: str
        """
        return self._QQOpenId

    @QQOpenId.setter
    def QQOpenId(self, QQOpenId):
        self._QQOpenId = QQOpenId

    @property
    def QQAppId(self):
        r"""<p>QQ应用ID，当传入QQ开放账号时，该字段必填，QQ分配给网站或应用的AppId，用来唯一标识网站或应用</p>
        :rtype: str
        """
        return self._QQAppId

    @QQAppId.setter
    def QQAppId(self, QQAppId):
        self._QQAppId = QQAppId


    def _deserialize(self, params):
        self._EventCode = params.get("EventCode")
        self._EventTime = params.get("EventTime")
        self._SessionId = params.get("SessionId")
        self._DeviceToken = params.get("DeviceToken")
        self._UserIp = params.get("UserIp")
        if params.get("EventDetail") is not None:
            self._EventDetail = EventDetail()
            self._EventDetail._deserialize(params.get("EventDetail"))
        self._UserId = params.get("UserId")
        self._UserEmail = params.get("UserEmail")
        self._UserPhone = params.get("UserPhone")
        if params.get("Browser") is not None:
            self._Browser = Browser()
            self._Browser._deserialize(params.get("Browser"))
        if params.get("App") is not None:
            self._App = App()
            self._App._deserialize(params.get("App"))
        if params.get("DataAuthorization") is not None:
            self._DataAuthorization = DataAuthorization()
            self._DataAuthorization._deserialize(params.get("DataAuthorization"))
        self._UserPhoneEncrypt = params.get("UserPhoneEncrypt")
        self._WeChatOpenId = params.get("WeChatOpenId")
        self._QQOpenId = params.get("QQOpenId")
        self._QQAppId = params.get("QQAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessRiskResponse(AbstractModel):
    r"""AssessRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>事件风险评估结果</p>
        :type Data: :class:`tencentcloud.rce.v20260130.models.AssessRiskRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>事件风险评估结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessRiskRsp`
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
            self._Data = AssessRiskRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AssessRiskRsp(AbstractModel):
    r"""事件风险评估返回结果

    """

    def __init__(self):
        r"""
        :param _Decision: <p>决策信息</p>
        :type Decision: :class:`tencentcloud.rce.v20260130.models.Decision`
        :param _Score: <p>风险分，根据您开启的产品服务计算的评分结果</p>
        :type Score: :class:`tencentcloud.rce.v20260130.models.Score`
        :param _ExtraInfo: <p>扩展信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: list of Cust
        """
        self._Decision = None
        self._Score = None
        self._ExtraInfo = None

    @property
    def Decision(self):
        r"""<p>决策信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Decision`
        """
        return self._Decision

    @Decision.setter
    def Decision(self, Decision):
        self._Decision = Decision

    @property
    def Score(self):
        r"""<p>风险分，根据您开启的产品服务计算的评分结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Score`
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def ExtraInfo(self):
        r"""<p>扩展信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Cust
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo


    def _deserialize(self, params):
        if params.get("Decision") is not None:
            self._Decision = Decision()
            self._Decision._deserialize(params.get("Decision"))
        if params.get("Score") is not None:
            self._Score = Score()
            self._Score._deserialize(params.get("Score"))
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = []
            for item in params.get("ExtraInfo"):
                obj = Cust()
                obj._deserialize(item)
                self._ExtraInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Billing(AbstractModel):
    r"""账单信息

    """

    def __init__(self):
        r"""
        :param _Address: <p>账单地址</p>
        :type Address: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Phone: <p>账单联系电话</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :type Phone: str
        :param _Email: <p>账单邮箱</p>
        :type Email: str
        :param _Recipient: <p>账单接收人姓名</p>
        :type Recipient: str
        """
        self._Address = None
        self._Phone = None
        self._Email = None
        self._Recipient = None

    @property
    def Address(self):
        r"""<p>账单地址</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Phone(self):
        r"""<p>账单联系电话</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""<p>账单邮箱</p>
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Recipient(self):
        r"""<p>账单接收人姓名</p>
        :rtype: str
        """
        return self._Recipient

    @Recipient.setter
    def Recipient(self, Recipient):
        self._Recipient = Recipient


    def _deserialize(self, params):
        if params.get("Address") is not None:
            self._Address = Address()
            self._Address._deserialize(params.get("Address"))
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._Recipient = params.get("Recipient")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrowseEvent(AbstractModel):
    r"""浏览事件详情

    """

    def __init__(self):
        r"""
        :param _PageType: <p>当前浏览网页的类型，例如主页、搜索页等</p>
        :type PageType: str
        :param _PageUrl: <p>当前浏览的网页URL</p>
        :type PageUrl: str
        :param _Duration: <p>浏览耗时</p><p>单位：毫秒</p>
        :type Duration: int
        :param _ContentType: <p>网页内容类型，例如广告、视频、文章等</p>
        :type ContentType: str
        :param _ContentId: <p>网页内容ID</p>
        :type ContentId: str
        :param _ReferPageType: <p>上一个网页的类型，例如主页、搜索页等</p>
        :type ReferPageType: str
        :param _ReferPageUrl: <p>上一个网页URL</p>
        :type ReferPageUrl: str
        :param _GuestId: <p>游客账号ID</p>
        :type GuestId: str
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._PageType = None
        self._PageUrl = None
        self._Duration = None
        self._ContentType = None
        self._ContentId = None
        self._ReferPageType = None
        self._ReferPageUrl = None
        self._GuestId = None
        self._Cust = None

    @property
    def PageType(self):
        r"""<p>当前浏览网页的类型，例如主页、搜索页等</p>
        :rtype: str
        """
        return self._PageType

    @PageType.setter
    def PageType(self, PageType):
        self._PageType = PageType

    @property
    def PageUrl(self):
        r"""<p>当前浏览的网页URL</p>
        :rtype: str
        """
        return self._PageUrl

    @PageUrl.setter
    def PageUrl(self, PageUrl):
        self._PageUrl = PageUrl

    @property
    def Duration(self):
        r"""<p>浏览耗时</p><p>单位：毫秒</p>
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ContentType(self):
        r"""<p>网页内容类型，例如广告、视频、文章等</p>
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def ContentId(self):
        r"""<p>网页内容ID</p>
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def ReferPageType(self):
        r"""<p>上一个网页的类型，例如主页、搜索页等</p>
        :rtype: str
        """
        return self._ReferPageType

    @ReferPageType.setter
    def ReferPageType(self, ReferPageType):
        self._ReferPageType = ReferPageType

    @property
    def ReferPageUrl(self):
        r"""<p>上一个网页URL</p>
        :rtype: str
        """
        return self._ReferPageUrl

    @ReferPageUrl.setter
    def ReferPageUrl(self, ReferPageUrl):
        self._ReferPageUrl = ReferPageUrl

    @property
    def GuestId(self):
        r"""<p>游客账号ID</p>
        :rtype: str
        """
        return self._GuestId

    @GuestId.setter
    def GuestId(self, GuestId):
        self._GuestId = GuestId

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PageType = params.get("PageType")
        self._PageUrl = params.get("PageUrl")
        self._Duration = params.get("Duration")
        self._ContentType = params.get("ContentType")
        self._ContentId = params.get("ContentId")
        self._ReferPageType = params.get("ReferPageType")
        self._ReferPageUrl = params.get("ReferPageUrl")
        self._GuestId = params.get("GuestId")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Browser(AbstractModel):
    r"""浏览器信息

    """

    def __init__(self):
        r"""
        :param _UserAgent: <p>与网站交互的浏览器的用户代理</p>
        :type UserAgent: str
        :param _AcceptLanguage: <p>浏览器支持的用户请求语言</p><p>参数格式：符合ISO 3166标准</p>
        :type AcceptLanguage: str
        :param _ContentLanguage: <p>浏览器当前网站内容的语言</p><p>参数格式：符合ISO 3166标准</p>
        :type ContentLanguage: str
        """
        self._UserAgent = None
        self._AcceptLanguage = None
        self._ContentLanguage = None

    @property
    def UserAgent(self):
        r"""<p>与网站交互的浏览器的用户代理</p>
        :rtype: str
        """
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def AcceptLanguage(self):
        r"""<p>浏览器支持的用户请求语言</p><p>参数格式：符合ISO 3166标准</p>
        :rtype: str
        """
        return self._AcceptLanguage

    @AcceptLanguage.setter
    def AcceptLanguage(self, AcceptLanguage):
        self._AcceptLanguage = AcceptLanguage

    @property
    def ContentLanguage(self):
        r"""<p>浏览器当前网站内容的语言</p><p>参数格式：符合ISO 3166标准</p>
        :rtype: str
        """
        return self._ContentLanguage

    @ContentLanguage.setter
    def ContentLanguage(self, ContentLanguage):
        self._ContentLanguage = ContentLanguage


    def _deserialize(self, params):
        self._UserAgent = params.get("UserAgent")
        self._AcceptLanguage = params.get("AcceptLanguage")
        self._ContentLanguage = params.get("ContentLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Card(AbstractModel):
    r"""银行卡

    """

    def __init__(self):
        r"""
        :param _CardBin: <p>发卡行识别码卡号前6位</p><p>参数格式：符合ISO 13616-1标准</p>
        :type CardBin: str
        :param _LastFourDigits: <p>发卡行识别码卡号后4位</p><p>参数格式：符合ISO 13616-1标准</p>
        :type LastFourDigits: str
        :param _Country: <p>发行国家</p>
        :type Country: str
        :param _Bank: <p>发行银行</p>
        :type Bank: str
        :param _Type: <p>支付卡类型</p><p>枚举值：</p><ul><li>credit： 信用卡</li><li>debit： 借记卡</li><li>charge： 签账卡</li></ul>
        :type Type: str
        :param _Brand: <p>支付卡品牌</p>
        :type Brand: str
        :param _Level: <p>支付卡等级</p>
        :type Level: str
        :param _HolderName: <p>持有者姓名</p>
        :type HolderName: str
        :param _ExpireTime: <p>过期日期</p><p>参数格式：YYYY-MM-DD</p>
        :type ExpireTime: str
        """
        self._CardBin = None
        self._LastFourDigits = None
        self._Country = None
        self._Bank = None
        self._Type = None
        self._Brand = None
        self._Level = None
        self._HolderName = None
        self._ExpireTime = None

    @property
    def CardBin(self):
        r"""<p>发卡行识别码卡号前6位</p><p>参数格式：符合ISO 13616-1标准</p>
        :rtype: str
        """
        return self._CardBin

    @CardBin.setter
    def CardBin(self, CardBin):
        self._CardBin = CardBin

    @property
    def LastFourDigits(self):
        r"""<p>发卡行识别码卡号后4位</p><p>参数格式：符合ISO 13616-1标准</p>
        :rtype: str
        """
        return self._LastFourDigits

    @LastFourDigits.setter
    def LastFourDigits(self, LastFourDigits):
        self._LastFourDigits = LastFourDigits

    @property
    def Country(self):
        r"""<p>发行国家</p>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Bank(self):
        r"""<p>发行银行</p>
        :rtype: str
        """
        return self._Bank

    @Bank.setter
    def Bank(self, Bank):
        self._Bank = Bank

    @property
    def Type(self):
        r"""<p>支付卡类型</p><p>枚举值：</p><ul><li>credit： 信用卡</li><li>debit： 借记卡</li><li>charge： 签账卡</li></ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Brand(self):
        r"""<p>支付卡品牌</p>
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Level(self):
        r"""<p>支付卡等级</p>
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def HolderName(self):
        r"""<p>持有者姓名</p>
        :rtype: str
        """
        return self._HolderName

    @HolderName.setter
    def HolderName(self, HolderName):
        self._HolderName = HolderName

    @property
    def ExpireTime(self):
        r"""<p>过期日期</p><p>参数格式：YYYY-MM-DD</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._CardBin = params.get("CardBin")
        self._LastFourDigits = params.get("LastFourDigits")
        self._Country = params.get("Country")
        self._Bank = params.get("Bank")
        self._Type = params.get("Type")
        self._Brand = params.get("Brand")
        self._Level = params.get("Level")
        self._HolderName = params.get("HolderName")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargeBackEvent(AbstractModel):
    r"""拒付事件详情

    """

    def __init__(self):
        r"""
        :param _TransactionId: <p>交易ID</p>
        :type TransactionId: str
        :param _OrderId: <p>订单 ID，当一笔交易关联多个订单（合并支付）时请输入所有订单ID</p>
        :type OrderId: list of str
        :param _ChargeBackCode: <p>拒付理由码，参考各卡组织定义的拒付码，例如：10.1、13.1、 4870、4871等</p>
        :type ChargeBackCode: str
        :param _ChargeBackReason: <p>拒付原因，参考各卡组织定义的拒付原因，例如：未收到商品、欺诈等</p>
        :type ChargeBackReason: str
        :param _ChargeBackProcess: <p>拒付申诉阶段</p><p>枚举值：</p><ul><li>need_response： 需要商家回应</li><li>information_supplied： 商家已提供信息</li><li>chargeback_reversed： 拒付已撤销</li><li>chargeback_sustained： 拒付已成立</li></ul>
        :type ChargeBackProcess: str
        :param _ChargeBackAmount: <p>拒付金额</p>
        :type ChargeBackAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._TransactionId = None
        self._OrderId = None
        self._ChargeBackCode = None
        self._ChargeBackReason = None
        self._ChargeBackProcess = None
        self._ChargeBackAmount = None
        self._Cust = None

    @property
    def TransactionId(self):
        r"""<p>交易ID</p>
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def OrderId(self):
        r"""<p>订单 ID，当一笔交易关联多个订单（合并支付）时请输入所有订单ID</p>
        :rtype: list of str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ChargeBackCode(self):
        r"""<p>拒付理由码，参考各卡组织定义的拒付码，例如：10.1、13.1、 4870、4871等</p>
        :rtype: str
        """
        return self._ChargeBackCode

    @ChargeBackCode.setter
    def ChargeBackCode(self, ChargeBackCode):
        self._ChargeBackCode = ChargeBackCode

    @property
    def ChargeBackReason(self):
        r"""<p>拒付原因，参考各卡组织定义的拒付原因，例如：未收到商品、欺诈等</p>
        :rtype: str
        """
        return self._ChargeBackReason

    @ChargeBackReason.setter
    def ChargeBackReason(self, ChargeBackReason):
        self._ChargeBackReason = ChargeBackReason

    @property
    def ChargeBackProcess(self):
        r"""<p>拒付申诉阶段</p><p>枚举值：</p><ul><li>need_response： 需要商家回应</li><li>information_supplied： 商家已提供信息</li><li>chargeback_reversed： 拒付已撤销</li><li>chargeback_sustained： 拒付已成立</li></ul>
        :rtype: str
        """
        return self._ChargeBackProcess

    @ChargeBackProcess.setter
    def ChargeBackProcess(self, ChargeBackProcess):
        self._ChargeBackProcess = ChargeBackProcess

    @property
    def ChargeBackAmount(self):
        r"""<p>拒付金额</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._ChargeBackAmount

    @ChargeBackAmount.setter
    def ChargeBackAmount(self, ChargeBackAmount):
        self._ChargeBackAmount = ChargeBackAmount

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._TransactionId = params.get("TransactionId")
        self._OrderId = params.get("OrderId")
        self._ChargeBackCode = params.get("ChargeBackCode")
        self._ChargeBackReason = params.get("ChargeBackReason")
        self._ChargeBackProcess = params.get("ChargeBackProcess")
        if params.get("ChargeBackAmount") is not None:
            self._ChargeBackAmount = Amount()
            self._ChargeBackAmount._deserialize(params.get("ChargeBackAmount"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClaimRedPacketEvent(AbstractModel):
    r"""领红包事件详情

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>营销活动ID</p>
        :type PromotionId: str
        :param _PromotionName: <p>营销活动名称</p>
        :type PromotionName: str
        :param _Description: <p>营销活动描述</p>
        :type Description: str
        :param _InviterUserId: <p>邀请人ID</p>
        :type InviterUserId: str
        :param _RedPacketId: <p>红包ID</p>
        :type RedPacketId: str
        :param _RedPacketType: <p>红包类型，如手气红包、口令红包、均分红包等</p>
        :type RedPacketType: str
        :param _RedPacketAmount: <p>红包金额</p>
        :type RedPacketAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._RedPacketId = None
        self._RedPacketType = None
        self._RedPacketAmount = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>营销活动ID</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>营销活动名称</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>营销活动描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>邀请人ID</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def RedPacketId(self):
        r"""<p>红包ID</p>
        :rtype: str
        """
        return self._RedPacketId

    @RedPacketId.setter
    def RedPacketId(self, RedPacketId):
        self._RedPacketId = RedPacketId

    @property
    def RedPacketType(self):
        r"""<p>红包类型，如手气红包、口令红包、均分红包等</p>
        :rtype: str
        """
        return self._RedPacketType

    @RedPacketType.setter
    def RedPacketType(self, RedPacketType):
        self._RedPacketType = RedPacketType

    @property
    def RedPacketAmount(self):
        r"""<p>红包金额</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._RedPacketAmount

    @RedPacketAmount.setter
    def RedPacketAmount(self, RedPacketAmount):
        self._RedPacketAmount = RedPacketAmount

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        self._RedPacketId = params.get("RedPacketId")
        self._RedPacketType = params.get("RedPacketType")
        if params.get("RedPacketAmount") is not None:
            self._RedPacketAmount = Amount()
            self._RedPacketAmount._deserialize(params.get("RedPacketAmount"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coupon(AbstractModel):
    r"""优惠券

    """

    def __init__(self):
        r"""
        :param _CouponId: <p>优惠券ID</p>
        :type CouponId: str
        :param _CouponName: <p>优惠券名称</p>
        :type CouponName: str
        :param _StartTime: <p>优惠券开始时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :type StartTime: str
        :param _ExpireTime: <p>优惠券过期时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :type ExpireTime: str
        :param _PercentageRate: <p>折扣百分比，如果折扣为 10%，则发送“0.1”</p>
        :type PercentageRate: float
        :param _DiscountAmount: <p>折扣金额</p>
        :type DiscountAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Threshold: <p>优惠券门槛</p>
        :type Threshold: float
        """
        self._CouponId = None
        self._CouponName = None
        self._StartTime = None
        self._ExpireTime = None
        self._PercentageRate = None
        self._DiscountAmount = None
        self._Threshold = None

    @property
    def CouponId(self):
        r"""<p>优惠券ID</p>
        :rtype: str
        """
        return self._CouponId

    @CouponId.setter
    def CouponId(self, CouponId):
        self._CouponId = CouponId

    @property
    def CouponName(self):
        r"""<p>优惠券名称</p>
        :rtype: str
        """
        return self._CouponName

    @CouponName.setter
    def CouponName(self, CouponName):
        self._CouponName = CouponName

    @property
    def StartTime(self):
        r"""<p>优惠券开始时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        r"""<p>优惠券过期时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PercentageRate(self):
        r"""<p>折扣百分比，如果折扣为 10%，则发送“0.1”</p>
        :rtype: float
        """
        return self._PercentageRate

    @PercentageRate.setter
    def PercentageRate(self, PercentageRate):
        self._PercentageRate = PercentageRate

    @property
    def DiscountAmount(self):
        r"""<p>折扣金额</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._DiscountAmount

    @DiscountAmount.setter
    def DiscountAmount(self, DiscountAmount):
        self._DiscountAmount = DiscountAmount

    @property
    def Threshold(self):
        r"""<p>优惠券门槛</p>
        :rtype: float
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._CouponId = params.get("CouponId")
        self._CouponName = params.get("CouponName")
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        self._PercentageRate = params.get("PercentageRate")
        if params.get("DiscountAmount") is not None:
            self._DiscountAmount = Amount()
            self._DiscountAmount._deserialize(params.get("DiscountAmount"))
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderEvent(AbstractModel):
    r"""创建订单事件详情

    """

    def __init__(self):
        r"""
        :param _OrderId: <p>订单ID</p>
        :type OrderId: str
        :param _Amount: <p>订单金额</p>
        :type Amount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Merchant: <p>商家信息</p>
        :type Merchant: :class:`tencentcloud.rce.v20260130.models.Merchant`
        :param _Billing: <p>账单信息</p>
        :type Billing: :class:`tencentcloud.rce.v20260130.models.Billing`
        :param _Items: <p>商品信息</p>
        :type Items: list of Item
        :param _Delivery: <p>物流信息</p>
        :type Delivery: :class:`tencentcloud.rce.v20260130.models.Delivery`
        :param _Promotions: <p>营销活动信息</p>
        :type Promotions: list of Promotion
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._OrderId = None
        self._Amount = None
        self._Merchant = None
        self._Billing = None
        self._Items = None
        self._Delivery = None
        self._Promotions = None
        self._Cust = None

    @property
    def OrderId(self):
        r"""<p>订单ID</p>
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Amount(self):
        r"""<p>订单金额</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Merchant(self):
        r"""<p>商家信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Merchant`
        """
        return self._Merchant

    @Merchant.setter
    def Merchant(self, Merchant):
        self._Merchant = Merchant

    @property
    def Billing(self):
        r"""<p>账单信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Billing`
        """
        return self._Billing

    @Billing.setter
    def Billing(self, Billing):
        self._Billing = Billing

    @property
    def Items(self):
        r"""<p>商品信息</p>
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Delivery(self):
        r"""<p>物流信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Delivery`
        """
        return self._Delivery

    @Delivery.setter
    def Delivery(self, Delivery):
        self._Delivery = Delivery

    @property
    def Promotions(self):
        r"""<p>营销活动信息</p>
        :rtype: list of Promotion
        """
        return self._Promotions

    @Promotions.setter
    def Promotions(self, Promotions):
        self._Promotions = Promotions

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        if params.get("Amount") is not None:
            self._Amount = Amount()
            self._Amount._deserialize(params.get("Amount"))
        if params.get("Merchant") is not None:
            self._Merchant = Merchant()
            self._Merchant._deserialize(params.get("Merchant"))
        if params.get("Billing") is not None:
            self._Billing = Billing()
            self._Billing._deserialize(params.get("Billing"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Delivery") is not None:
            self._Delivery = Delivery()
            self._Delivery._deserialize(params.get("Delivery"))
        if params.get("Promotions") is not None:
            self._Promotions = []
            for item in params.get("Promotions"):
                obj = Promotion()
                obj._deserialize(item)
                self._Promotions.append(obj)
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreditPoint(AbstractModel):
    r"""账号积分

    """

    def __init__(self):
        r"""
        :param _Point: <p>积分分值</p>
        :type Point: float
        :param _PointType: <p>积分类型</p>
        :type PointType: str
        """
        self._Point = None
        self._PointType = None

    @property
    def Point(self):
        r"""<p>积分分值</p>
        :rtype: float
        """
        return self._Point

    @Point.setter
    def Point(self, Point):
        self._Point = Point

    @property
    def PointType(self):
        r"""<p>积分类型</p>
        :rtype: str
        """
        return self._PointType

    @PointType.setter
    def PointType(self, PointType):
        self._PointType = PointType


    def _deserialize(self, params):
        self._Point = params.get("Point")
        self._PointType = params.get("PointType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cust(AbstractModel):
    r"""与RCE约定的定制化参数，K:V 格式的对象数组

    """

    def __init__(self):
        r"""
        :param _Key: <p>标识符</p>
        :type Key: str
        :param _Value: <p>数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>标识符</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>数据</p>
注意：此字段可能返回 null，表示取不到有效值。
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
        


class CustEvent(AbstractModel):
    r"""自定义事件

    """

    def __init__(self):
        r"""
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._Cust = None

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataAuthorization(AbstractModel):
    r"""数据授权信息

    """

    def __init__(self):
        r"""
        :param _DataProviderName: <p>数据委托方，客户主体名称</p>
        :type DataProviderName: str
        :param _DataRecipientName: <p>数据受托方，腾讯云主体名称，固定填：腾讯云计算（北京）有限责任公司</p>
        :type DataRecipientName: str
        :param _UserDataType: <p>客户请求RCE所提供的用户数据类型，支持多选</p><p>枚举值：</p><ul><li>1： 手机号</li><li>2： 微信开放账号</li><li>3： QQ开放账号</li><li>4： IP地址</li><li>5： URL网址</li><li>999： 其他</li></ul>
        :type UserDataType: list of int
        :param _IsAuthorized: <p>客户是否已按合规指南要求获取用户授权，同意客户委托腾讯云处理入参信息</p><p>枚举值：</p><ul><li>true： 已授权</li><li>false： 未授权</li></ul>
        :type IsAuthorized: bool
        :param _IsOrderHanding: <p>客户是否已按合规指南要求获取用户授权，同意腾讯云结合客户提供的信息，对已合法收集的用户数据进行必要处理得出服务结果，并返回给客户</p><p>枚举值：</p><ul><li>true： 已授权</li><li>false： 未授权</li></ul>
        :type IsOrderHanding: bool
        :param _AuthorizationDeadline: <p>客户获得的用户授权期限Unix时间戳（单位秒），不填默认无固定期限</p>
        :type AuthorizationDeadline: int
        :param _PrivacyPolicyLink: <p>客户获得用户授权所依赖的协议地址</p>
        :type PrivacyPolicyLink: str
        """
        self._DataProviderName = None
        self._DataRecipientName = None
        self._UserDataType = None
        self._IsAuthorized = None
        self._IsOrderHanding = None
        self._AuthorizationDeadline = None
        self._PrivacyPolicyLink = None

    @property
    def DataProviderName(self):
        r"""<p>数据委托方，客户主体名称</p>
        :rtype: str
        """
        return self._DataProviderName

    @DataProviderName.setter
    def DataProviderName(self, DataProviderName):
        self._DataProviderName = DataProviderName

    @property
    def DataRecipientName(self):
        r"""<p>数据受托方，腾讯云主体名称，固定填：腾讯云计算（北京）有限责任公司</p>
        :rtype: str
        """
        return self._DataRecipientName

    @DataRecipientName.setter
    def DataRecipientName(self, DataRecipientName):
        self._DataRecipientName = DataRecipientName

    @property
    def UserDataType(self):
        r"""<p>客户请求RCE所提供的用户数据类型，支持多选</p><p>枚举值：</p><ul><li>1： 手机号</li><li>2： 微信开放账号</li><li>3： QQ开放账号</li><li>4： IP地址</li><li>5： URL网址</li><li>999： 其他</li></ul>
        :rtype: list of int
        """
        return self._UserDataType

    @UserDataType.setter
    def UserDataType(self, UserDataType):
        self._UserDataType = UserDataType

    @property
    def IsAuthorized(self):
        r"""<p>客户是否已按合规指南要求获取用户授权，同意客户委托腾讯云处理入参信息</p><p>枚举值：</p><ul><li>true： 已授权</li><li>false： 未授权</li></ul>
        :rtype: bool
        """
        return self._IsAuthorized

    @IsAuthorized.setter
    def IsAuthorized(self, IsAuthorized):
        self._IsAuthorized = IsAuthorized

    @property
    def IsOrderHanding(self):
        r"""<p>客户是否已按合规指南要求获取用户授权，同意腾讯云结合客户提供的信息，对已合法收集的用户数据进行必要处理得出服务结果，并返回给客户</p><p>枚举值：</p><ul><li>true： 已授权</li><li>false： 未授权</li></ul>
        :rtype: bool
        """
        return self._IsOrderHanding

    @IsOrderHanding.setter
    def IsOrderHanding(self, IsOrderHanding):
        self._IsOrderHanding = IsOrderHanding

    @property
    def AuthorizationDeadline(self):
        r"""<p>客户获得的用户授权期限Unix时间戳（单位秒），不填默认无固定期限</p>
        :rtype: int
        """
        return self._AuthorizationDeadline

    @AuthorizationDeadline.setter
    def AuthorizationDeadline(self, AuthorizationDeadline):
        self._AuthorizationDeadline = AuthorizationDeadline

    @property
    def PrivacyPolicyLink(self):
        r"""<p>客户获得用户授权所依赖的协议地址</p>
        :rtype: str
        """
        return self._PrivacyPolicyLink

    @PrivacyPolicyLink.setter
    def PrivacyPolicyLink(self, PrivacyPolicyLink):
        self._PrivacyPolicyLink = PrivacyPolicyLink


    def _deserialize(self, params):
        self._DataProviderName = params.get("DataProviderName")
        self._DataRecipientName = params.get("DataRecipientName")
        self._UserDataType = params.get("UserDataType")
        self._IsAuthorized = params.get("IsAuthorized")
        self._IsOrderHanding = params.get("IsOrderHanding")
        self._AuthorizationDeadline = params.get("AuthorizationDeadline")
        self._PrivacyPolicyLink = params.get("PrivacyPolicyLink")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataScore(AbstractModel):
    r"""风险分信息

    """

    def __init__(self):
        r"""
        :param _RiskLevel: <p>风险等级</p>
        :type RiskLevel: int
        :param _RiskLabels: <p>风险标签</p>
        :type RiskLabels: list of RiskLabel
        :param _RiskScore: <p>综合风险分数。</p><p>取值范围：[1, 1000]</p><p>数值越大，风险越大。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskScore: int
        """
        self._RiskLevel = None
        self._RiskLabels = None
        self._RiskScore = None

    @property
    def RiskLevel(self):
        r"""<p>风险等级</p>
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskLabels(self):
        r"""<p>风险标签</p>
        :rtype: list of RiskLabel
        """
        return self._RiskLabels

    @RiskLabels.setter
    def RiskLabels(self, RiskLabels):
        self._RiskLabels = RiskLabels

    @property
    def RiskScore(self):
        r"""<p>综合风险分数。</p><p>取值范围：[1, 1000]</p><p>数值越大，风险越大。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore


    def _deserialize(self, params):
        self._RiskLevel = params.get("RiskLevel")
        if params.get("RiskLabels") is not None:
            self._RiskLabels = []
            for item in params.get("RiskLabels"):
                obj = RiskLabel()
                obj._deserialize(item)
                self._RiskLabels.append(obj)
        self._RiskScore = params.get("RiskScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Decision(AbstractModel):
    r"""决策信息

    """

    def __init__(self):
        r"""
        :param _DecisionResult: <p>决策结果</p><ul><li>pass：通过</li><li>review：复审</li><li>reject：拒绝</li></ul>
        :type DecisionResult: str
        :param _Disposition: <p>命中策略后的决策动作，可在控制台配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Disposition: str
        """
        self._DecisionResult = None
        self._Disposition = None

    @property
    def DecisionResult(self):
        r"""<p>决策结果</p><ul><li>pass：通过</li><li>review：复审</li><li>reject：拒绝</li></ul>
        :rtype: str
        """
        return self._DecisionResult

    @DecisionResult.setter
    def DecisionResult(self, DecisionResult):
        self._DecisionResult = DecisionResult

    @property
    def Disposition(self):
        r"""<p>命中策略后的决策动作，可在控制台配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Disposition

    @Disposition.setter
    def Disposition(self, Disposition):
        self._Disposition = Disposition


    def _deserialize(self, params):
        self._DecisionResult = params.get("DecisionResult")
        self._Disposition = params.get("Disposition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Delivery(AbstractModel):
    r"""物流信息

    """

    def __init__(self):
        r"""
        :param _DeliveryMethod: <p>物流方式</p><ul><li>physical：物理投送</li><li>electonic：电子投送</li></ul>
        :type DeliveryMethod: str
        :param _DeliveryAmount: <p>物流费用</p>
        :type DeliveryAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _DeliveryAddress: <p>收货地址</p>
        :type DeliveryAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _ConsigneePhone: <p>收货人电话</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :type ConsigneePhone: str
        :param _ConsigneeEmail: <p>收货人邮箱</p>
        :type ConsigneeEmail: str
        :param _ConsigneeName: <p>收货人姓名</p>
        :type ConsigneeName: str
        :param _Expedited: <p>是否加急</p>
        :type Expedited: bool
        :param _DeliveryCarrier: <p>物流厂商，一般是物流的公司</p>
        :type DeliveryCarrier: str
        :param _DeliveryTracking: <p>物流追踪单号</p>
        :type DeliveryTracking: str
        """
        self._DeliveryMethod = None
        self._DeliveryAmount = None
        self._DeliveryAddress = None
        self._ConsigneePhone = None
        self._ConsigneeEmail = None
        self._ConsigneeName = None
        self._Expedited = None
        self._DeliveryCarrier = None
        self._DeliveryTracking = None

    @property
    def DeliveryMethod(self):
        r"""<p>物流方式</p><ul><li>physical：物理投送</li><li>electonic：电子投送</li></ul>
        :rtype: str
        """
        return self._DeliveryMethod

    @DeliveryMethod.setter
    def DeliveryMethod(self, DeliveryMethod):
        self._DeliveryMethod = DeliveryMethod

    @property
    def DeliveryAmount(self):
        r"""<p>物流费用</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._DeliveryAmount

    @DeliveryAmount.setter
    def DeliveryAmount(self, DeliveryAmount):
        self._DeliveryAmount = DeliveryAmount

    @property
    def DeliveryAddress(self):
        r"""<p>收货地址</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._DeliveryAddress

    @DeliveryAddress.setter
    def DeliveryAddress(self, DeliveryAddress):
        self._DeliveryAddress = DeliveryAddress

    @property
    def ConsigneePhone(self):
        r"""<p>收货人电话</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :rtype: str
        """
        return self._ConsigneePhone

    @ConsigneePhone.setter
    def ConsigneePhone(self, ConsigneePhone):
        self._ConsigneePhone = ConsigneePhone

    @property
    def ConsigneeEmail(self):
        r"""<p>收货人邮箱</p>
        :rtype: str
        """
        return self._ConsigneeEmail

    @ConsigneeEmail.setter
    def ConsigneeEmail(self, ConsigneeEmail):
        self._ConsigneeEmail = ConsigneeEmail

    @property
    def ConsigneeName(self):
        r"""<p>收货人姓名</p>
        :rtype: str
        """
        return self._ConsigneeName

    @ConsigneeName.setter
    def ConsigneeName(self, ConsigneeName):
        self._ConsigneeName = ConsigneeName

    @property
    def Expedited(self):
        r"""<p>是否加急</p>
        :rtype: bool
        """
        return self._Expedited

    @Expedited.setter
    def Expedited(self, Expedited):
        self._Expedited = Expedited

    @property
    def DeliveryCarrier(self):
        r"""<p>物流厂商，一般是物流的公司</p>
        :rtype: str
        """
        return self._DeliveryCarrier

    @DeliveryCarrier.setter
    def DeliveryCarrier(self, DeliveryCarrier):
        self._DeliveryCarrier = DeliveryCarrier

    @property
    def DeliveryTracking(self):
        r"""<p>物流追踪单号</p>
        :rtype: str
        """
        return self._DeliveryTracking

    @DeliveryTracking.setter
    def DeliveryTracking(self, DeliveryTracking):
        self._DeliveryTracking = DeliveryTracking


    def _deserialize(self, params):
        self._DeliveryMethod = params.get("DeliveryMethod")
        if params.get("DeliveryAmount") is not None:
            self._DeliveryAmount = Amount()
            self._DeliveryAmount._deserialize(params.get("DeliveryAmount"))
        if params.get("DeliveryAddress") is not None:
            self._DeliveryAddress = Address()
            self._DeliveryAddress._deserialize(params.get("DeliveryAddress"))
        self._ConsigneePhone = params.get("ConsigneePhone")
        self._ConsigneeEmail = params.get("ConsigneeEmail")
        self._ConsigneeName = params.get("ConsigneeName")
        self._Expedited = params.get("Expedited")
        self._DeliveryCarrier = params.get("DeliveryCarrier")
        self._DeliveryTracking = params.get("DeliveryTracking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    r"""设备基础信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: <p>设备ID</p>
        :type DeviceId: str
        :param _AppVersion: <p>App版本信息</p>
        :type AppVersion: str
        :param _Brand: <p>品牌</p>
        :type Brand: str
        :param _ClientIp: <p>客户端IP</p>
        :type ClientIp: str
        :param _Model: <p>机型</p>
        :type Model: str
        :param _NetworkType: <p>网络类型</p>
        :type NetworkType: str
        :param _PackageName: <p>应用包名</p>
        :type PackageName: str
        :param _Platform: <p>平台</p><p>枚举值：</p><ul><li>2： Android</li><li>3： IOS</li><li>4： H5</li><li>5： 微信小程序</li></ul>
        :type Platform: str
        :param _SystemVersion: <p>系统版本</p>
        :type SystemVersion: str
        :param _SdkBuildVersion: <p>SDK版本</p>
        :type SdkBuildVersion: str
        :param _SignToken: <p>验签token，验签功能启用请联系我们。</p>
        :type SignToken: str
        :param _TokenTime: <p>token生成时间戳，毫秒级。</p>
        :type TokenTime: str
        :param _PrivacyBrowser: <p>隐私浏览器类型，当检测到隐私浏览器时返回，仅H5。</p>
        :type PrivacyBrowser: str
        """
        self._DeviceId = None
        self._AppVersion = None
        self._Brand = None
        self._ClientIp = None
        self._Model = None
        self._NetworkType = None
        self._PackageName = None
        self._Platform = None
        self._SystemVersion = None
        self._SdkBuildVersion = None
        self._SignToken = None
        self._TokenTime = None
        self._PrivacyBrowser = None

    @property
    def DeviceId(self):
        r"""<p>设备ID</p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def AppVersion(self):
        r"""<p>App版本信息</p>
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Brand(self):
        r"""<p>品牌</p>
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def ClientIp(self):
        r"""<p>客户端IP</p>
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Model(self):
        r"""<p>机型</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def NetworkType(self):
        r"""<p>网络类型</p>
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageName(self):
        r"""<p>应用包名</p>
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        r"""<p>平台</p><p>枚举值：</p><ul><li>2： Android</li><li>3： IOS</li><li>4： H5</li><li>5： 微信小程序</li></ul>
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SystemVersion(self):
        r"""<p>系统版本</p>
        :rtype: str
        """
        return self._SystemVersion

    @SystemVersion.setter
    def SystemVersion(self, SystemVersion):
        self._SystemVersion = SystemVersion

    @property
    def SdkBuildVersion(self):
        r"""<p>SDK版本</p>
        :rtype: str
        """
        return self._SdkBuildVersion

    @SdkBuildVersion.setter
    def SdkBuildVersion(self, SdkBuildVersion):
        self._SdkBuildVersion = SdkBuildVersion

    @property
    def SignToken(self):
        r"""<p>验签token，验签功能启用请联系我们。</p>
        :rtype: str
        """
        return self._SignToken

    @SignToken.setter
    def SignToken(self, SignToken):
        self._SignToken = SignToken

    @property
    def TokenTime(self):
        r"""<p>token生成时间戳，毫秒级。</p>
        :rtype: str
        """
        return self._TokenTime

    @TokenTime.setter
    def TokenTime(self, TokenTime):
        self._TokenTime = TokenTime

    @property
    def PrivacyBrowser(self):
        r"""<p>隐私浏览器类型，当检测到隐私浏览器时返回，仅H5。</p>
        :rtype: str
        """
        return self._PrivacyBrowser

    @PrivacyBrowser.setter
    def PrivacyBrowser(self, PrivacyBrowser):
        self._PrivacyBrowser = PrivacyBrowser


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._AppVersion = params.get("AppVersion")
        self._Brand = params.get("Brand")
        self._ClientIp = params.get("ClientIp")
        self._Model = params.get("Model")
        self._NetworkType = params.get("NetworkType")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._SystemVersion = params.get("SystemVersion")
        self._SdkBuildVersion = params.get("SdkBuildVersion")
        self._SignToken = params.get("SignToken")
        self._TokenTime = params.get("TokenTime")
        self._PrivacyBrowser = params.get("PrivacyBrowser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DigitalOrder(AbstractModel):
    r"""数字订单

    """

    def __init__(self):
        r"""
        :param _DigitalAsset: <p>数字资产</p>
        :type DigitalAsset: str
        :param _AssetType: <p>数字资产类型</p><p>枚举值：</p><ul><li>coin： 代币</li><li>commodity： 大宗商品</li><li>crypto： 加密货币</li><li>fiat： 法币</li><li>token： 通证</li><li>stock： 股票</li><li>bond： 债券</li></ul>
        :type AssetType: str
        :param _OrderType: <p>订单类型</p><p>枚举值：</p><ul><li>limit： 限价单</li><li>market： 市价单</li><li>stop_limit： 止损限价单</li><li>stop_loss： 止损单</li><li>take_profit： 止盈单</li><li>take_profit_limit： 止盈限价单</li></ul>
        :type OrderType: str
        :param _Volume: <p>数字资产的数量</p>
        :type Volume: float
        """
        self._DigitalAsset = None
        self._AssetType = None
        self._OrderType = None
        self._Volume = None

    @property
    def DigitalAsset(self):
        r"""<p>数字资产</p>
        :rtype: str
        """
        return self._DigitalAsset

    @DigitalAsset.setter
    def DigitalAsset(self, DigitalAsset):
        self._DigitalAsset = DigitalAsset

    @property
    def AssetType(self):
        r"""<p>数字资产类型</p><p>枚举值：</p><ul><li>coin： 代币</li><li>commodity： 大宗商品</li><li>crypto： 加密货币</li><li>fiat： 法币</li><li>token： 通证</li><li>stock： 股票</li><li>bond： 债券</li></ul>
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def OrderType(self):
        r"""<p>订单类型</p><p>枚举值：</p><ul><li>limit： 限价单</li><li>market： 市价单</li><li>stop_limit： 止损限价单</li><li>stop_loss： 止损单</li><li>take_profit： 止盈单</li><li>take_profit_limit： 止盈限价单</li></ul>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Volume(self):
        r"""<p>数字资产的数量</p>
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._DigitalAsset = params.get("DigitalAsset")
        self._AssetType = params.get("AssetType")
        self._OrderType = params.get("OrderType")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    r"""环境基础信息

    """

    def __init__(self):
        r"""
        :param _Location: <p>IP地理位置信息</p>
        :type Location: :class:`tencentcloud.rce.v20260130.models.IPLocation`
        :param _Network: <p>IP基础网络信息</p>
        :type Network: :class:`tencentcloud.rce.v20260130.models.IPNetwork`
        """
        self._Location = None
        self._Network = None

    @property
    def Location(self):
        r"""<p>IP地理位置信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.IPLocation`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Network(self):
        r"""<p>IP基础网络信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.IPNetwork`
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network


    def _deserialize(self, params):
        if params.get("Location") is not None:
            self._Location = IPLocation()
            self._Location._deserialize(params.get("Location"))
        if params.get("Network") is not None:
            self._Network = IPNetwork()
            self._Network._deserialize(params.get("Network"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventDetail(AbstractModel):
    r"""事件详情

    """

    def __init__(self):
        r"""
        :param _Login: <p>登录</p>
        :type Login: :class:`tencentcloud.rce.v20260130.models.LoginEvent`
        :param _Register: <p>注册（变更用户信息）</p>
        :type Register: :class:`tencentcloud.rce.v20260130.models.RegisterEvent`
        :param _CreateOrder: <p>创建订单</p>
        :type CreateOrder: :class:`tencentcloud.rce.v20260130.models.CreateOrderEvent`
        :param _Transaction: <p>交易支付</p>
        :type Transaction: :class:`tencentcloud.rce.v20260130.models.TransactionEvent`
        :param _Sms: <p>短信</p>
        :type Sms: :class:`tencentcloud.rce.v20260130.models.SMSEvent`
        :param _ChargeBack: <p>拒付</p>
        :type ChargeBack: :class:`tencentcloud.rce.v20260130.models.ChargeBackEvent`
        :param _Logout: <p>登出</p>
        :type Logout: :class:`tencentcloud.rce.v20260130.models.LogoutEvent`
        :param _ModifyAccount: <p>修改账号</p>
        :type ModifyAccount: :class:`tencentcloud.rce.v20260130.models.ModifyAccountEvent`
        :param _ModifyPassword: <p>修改密码</p>
        :type ModifyPassword: :class:`tencentcloud.rce.v20260130.models.ModifyPasswordEvent`
        :param _SecurityVerification: <p>安全验证</p>
        :type SecurityVerification: :class:`tencentcloud.rce.v20260130.models.SecurityVerificationEvent`
        :param _AddPromotion: <p>参加营销活动</p>
        :type AddPromotion: :class:`tencentcloud.rce.v20260130.models.AddPromotionEvent`
        :param _Redeem: <p>兑奖</p>
        :type Redeem: :class:`tencentcloud.rce.v20260130.models.RedeemEvent`
        :param _Withdraw: <p>提现</p>
        :type Withdraw: :class:`tencentcloud.rce.v20260130.models.WithdrawEvent`
        :param _CustEvent: <p>自定义事件</p>
        :type CustEvent: :class:`tencentcloud.rce.v20260130.models.CustEvent`
        :param _ScanCode: <p>扫码</p>
        :type ScanCode: :class:`tencentcloud.rce.v20260130.models.ScanCodeEvent`
        :param _LuckyDraw: <p>抽奖</p>
        :type LuckyDraw: :class:`tencentcloud.rce.v20260130.models.LuckyDrawEvent`
        :param _Task: <p>做任务</p>
        :type Task: :class:`tencentcloud.rce.v20260130.models.TaskEvent`
        :param _Invitation: <p>邀请</p>
        :type Invitation: :class:`tencentcloud.rce.v20260130.models.InvitationEvent`
        :param _ClaimRedPacket: <p>领红包</p>
        :type ClaimRedPacket: :class:`tencentcloud.rce.v20260130.models.ClaimRedPacketEvent`
        :param _Browse: <p>浏览</p>
        :type Browse: :class:`tencentcloud.rce.v20260130.models.BrowseEvent`
        """
        self._Login = None
        self._Register = None
        self._CreateOrder = None
        self._Transaction = None
        self._Sms = None
        self._ChargeBack = None
        self._Logout = None
        self._ModifyAccount = None
        self._ModifyPassword = None
        self._SecurityVerification = None
        self._AddPromotion = None
        self._Redeem = None
        self._Withdraw = None
        self._CustEvent = None
        self._ScanCode = None
        self._LuckyDraw = None
        self._Task = None
        self._Invitation = None
        self._ClaimRedPacket = None
        self._Browse = None

    @property
    def Login(self):
        r"""<p>登录</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.LoginEvent`
        """
        return self._Login

    @Login.setter
    def Login(self, Login):
        self._Login = Login

    @property
    def Register(self):
        r"""<p>注册（变更用户信息）</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.RegisterEvent`
        """
        return self._Register

    @Register.setter
    def Register(self, Register):
        self._Register = Register

    @property
    def CreateOrder(self):
        r"""<p>创建订单</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CreateOrderEvent`
        """
        return self._CreateOrder

    @CreateOrder.setter
    def CreateOrder(self, CreateOrder):
        self._CreateOrder = CreateOrder

    @property
    def Transaction(self):
        r"""<p>交易支付</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.TransactionEvent`
        """
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def Sms(self):
        r"""<p>短信</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.SMSEvent`
        """
        return self._Sms

    @Sms.setter
    def Sms(self, Sms):
        self._Sms = Sms

    @property
    def ChargeBack(self):
        r"""<p>拒付</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ChargeBackEvent`
        """
        return self._ChargeBack

    @ChargeBack.setter
    def ChargeBack(self, ChargeBack):
        self._ChargeBack = ChargeBack

    @property
    def Logout(self):
        r"""<p>登出</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.LogoutEvent`
        """
        return self._Logout

    @Logout.setter
    def Logout(self, Logout):
        self._Logout = Logout

    @property
    def ModifyAccount(self):
        r"""<p>修改账号</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ModifyAccountEvent`
        """
        return self._ModifyAccount

    @ModifyAccount.setter
    def ModifyAccount(self, ModifyAccount):
        self._ModifyAccount = ModifyAccount

    @property
    def ModifyPassword(self):
        r"""<p>修改密码</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ModifyPasswordEvent`
        """
        return self._ModifyPassword

    @ModifyPassword.setter
    def ModifyPassword(self, ModifyPassword):
        self._ModifyPassword = ModifyPassword

    @property
    def SecurityVerification(self):
        r"""<p>安全验证</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.SecurityVerificationEvent`
        """
        return self._SecurityVerification

    @SecurityVerification.setter
    def SecurityVerification(self, SecurityVerification):
        self._SecurityVerification = SecurityVerification

    @property
    def AddPromotion(self):
        r"""<p>参加营销活动</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AddPromotionEvent`
        """
        return self._AddPromotion

    @AddPromotion.setter
    def AddPromotion(self, AddPromotion):
        self._AddPromotion = AddPromotion

    @property
    def Redeem(self):
        r"""<p>兑奖</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.RedeemEvent`
        """
        return self._Redeem

    @Redeem.setter
    def Redeem(self, Redeem):
        self._Redeem = Redeem

    @property
    def Withdraw(self):
        r"""<p>提现</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.WithdrawEvent`
        """
        return self._Withdraw

    @Withdraw.setter
    def Withdraw(self, Withdraw):
        self._Withdraw = Withdraw

    @property
    def CustEvent(self):
        r"""<p>自定义事件</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CustEvent`
        """
        return self._CustEvent

    @CustEvent.setter
    def CustEvent(self, CustEvent):
        self._CustEvent = CustEvent

    @property
    def ScanCode(self):
        r"""<p>扫码</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ScanCodeEvent`
        """
        return self._ScanCode

    @ScanCode.setter
    def ScanCode(self, ScanCode):
        self._ScanCode = ScanCode

    @property
    def LuckyDraw(self):
        r"""<p>抽奖</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.LuckyDrawEvent`
        """
        return self._LuckyDraw

    @LuckyDraw.setter
    def LuckyDraw(self, LuckyDraw):
        self._LuckyDraw = LuckyDraw

    @property
    def Task(self):
        r"""<p>做任务</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.TaskEvent`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def Invitation(self):
        r"""<p>邀请</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.InvitationEvent`
        """
        return self._Invitation

    @Invitation.setter
    def Invitation(self, Invitation):
        self._Invitation = Invitation

    @property
    def ClaimRedPacket(self):
        r"""<p>领红包</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ClaimRedPacketEvent`
        """
        return self._ClaimRedPacket

    @ClaimRedPacket.setter
    def ClaimRedPacket(self, ClaimRedPacket):
        self._ClaimRedPacket = ClaimRedPacket

    @property
    def Browse(self):
        r"""<p>浏览</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.BrowseEvent`
        """
        return self._Browse

    @Browse.setter
    def Browse(self, Browse):
        self._Browse = Browse


    def _deserialize(self, params):
        if params.get("Login") is not None:
            self._Login = LoginEvent()
            self._Login._deserialize(params.get("Login"))
        if params.get("Register") is not None:
            self._Register = RegisterEvent()
            self._Register._deserialize(params.get("Register"))
        if params.get("CreateOrder") is not None:
            self._CreateOrder = CreateOrderEvent()
            self._CreateOrder._deserialize(params.get("CreateOrder"))
        if params.get("Transaction") is not None:
            self._Transaction = TransactionEvent()
            self._Transaction._deserialize(params.get("Transaction"))
        if params.get("Sms") is not None:
            self._Sms = SMSEvent()
            self._Sms._deserialize(params.get("Sms"))
        if params.get("ChargeBack") is not None:
            self._ChargeBack = ChargeBackEvent()
            self._ChargeBack._deserialize(params.get("ChargeBack"))
        if params.get("Logout") is not None:
            self._Logout = LogoutEvent()
            self._Logout._deserialize(params.get("Logout"))
        if params.get("ModifyAccount") is not None:
            self._ModifyAccount = ModifyAccountEvent()
            self._ModifyAccount._deserialize(params.get("ModifyAccount"))
        if params.get("ModifyPassword") is not None:
            self._ModifyPassword = ModifyPasswordEvent()
            self._ModifyPassword._deserialize(params.get("ModifyPassword"))
        if params.get("SecurityVerification") is not None:
            self._SecurityVerification = SecurityVerificationEvent()
            self._SecurityVerification._deserialize(params.get("SecurityVerification"))
        if params.get("AddPromotion") is not None:
            self._AddPromotion = AddPromotionEvent()
            self._AddPromotion._deserialize(params.get("AddPromotion"))
        if params.get("Redeem") is not None:
            self._Redeem = RedeemEvent()
            self._Redeem._deserialize(params.get("Redeem"))
        if params.get("Withdraw") is not None:
            self._Withdraw = WithdrawEvent()
            self._Withdraw._deserialize(params.get("Withdraw"))
        if params.get("CustEvent") is not None:
            self._CustEvent = CustEvent()
            self._CustEvent._deserialize(params.get("CustEvent"))
        if params.get("ScanCode") is not None:
            self._ScanCode = ScanCodeEvent()
            self._ScanCode._deserialize(params.get("ScanCode"))
        if params.get("LuckyDraw") is not None:
            self._LuckyDraw = LuckyDrawEvent()
            self._LuckyDraw._deserialize(params.get("LuckyDraw"))
        if params.get("Task") is not None:
            self._Task = TaskEvent()
            self._Task._deserialize(params.get("Task"))
        if params.get("Invitation") is not None:
            self._Invitation = InvitationEvent()
            self._Invitation._deserialize(params.get("Invitation"))
        if params.get("ClaimRedPacket") is not None:
            self._ClaimRedPacket = ClaimRedPacketEvent()
            self._ClaimRedPacket._deserialize(params.get("ClaimRedPacket"))
        if params.get("Browse") is not None:
            self._Browse = BrowseEvent()
            self._Browse._deserialize(params.get("Browse"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPLocation(AbstractModel):
    r"""IP地理位置信息

    """

    def __init__(self):
        r"""
        :param _Country: <p>IP地址所属国家</p>
        :type Country: str
        :param _Region: <p>IP地址所属省份</p>
        :type Region: str
        :param _City: <p>IP地址所属城市</p>
        :type City: str
        :param _District: <p>IP地址所属地区</p>
        :type District: str
        :param _Longitude: <p>IP地址的经度</p>
        :type Longitude: str
        :param _Latitude: <p>IP地址的纬度</p>
        :type Latitude: str
        :param _Timezone: <p>IP地址所属时区</p>
        :type Timezone: str
        :param _ZipCode: <p>IP地址的邮政编码</p>
        :type ZipCode: str
        """
        self._Country = None
        self._Region = None
        self._City = None
        self._District = None
        self._Longitude = None
        self._Latitude = None
        self._Timezone = None
        self._ZipCode = None

    @property
    def Country(self):
        r"""<p>IP地址所属国家</p>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Region(self):
        r"""<p>IP地址所属省份</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def City(self):
        r"""<p>IP地址所属城市</p>
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        r"""<p>IP地址所属地区</p>
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Longitude(self):
        r"""<p>IP地址的经度</p>
        :rtype: str
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        r"""<p>IP地址的纬度</p>
        :rtype: str
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Timezone(self):
        r"""<p>IP地址所属时区</p>
        :rtype: str
        """
        return self._Timezone

    @Timezone.setter
    def Timezone(self, Timezone):
        self._Timezone = Timezone

    @property
    def ZipCode(self):
        r"""<p>IP地址的邮政编码</p>
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._Region = params.get("Region")
        self._City = params.get("City")
        self._District = params.get("District")
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._Timezone = params.get("Timezone")
        self._ZipCode = params.get("ZipCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPNetwork(AbstractModel):
    r"""IP基础网络信息

    """

    def __init__(self):
        r"""
        :param _ISP: <p>互联网服务提供商</p>
        :type ISP: str
        :param _ASN: <p>自治系统号</p>
        :type ASN: str
        :param _Organization: <p>IP注册组织名称</p>
        :type Organization: str
        :param _IsReserved: <p>是否保留IP</p>
        :type IsReserved: bool
        :param _IsGateway: <p>是否网关IP</p>
        :type IsGateway: bool
        :param _IsAnycast: <p>是否任播网络</p>
        :type IsAnycast: bool
        :param _IsMobile: <p>是否移动网络</p>
        :type IsMobile: bool
        :param _IsDynamic: <p>是否动态IP</p>
        :type IsDynamic: bool
        :param _IsEgress: <p>是否网络出口</p>
        :type IsEgress: bool
        :param _IsDNS: <p>是否域名解析</p>
        :type IsDNS: bool
        :param _IsEducation: <p>是否教育机构</p>
        :type IsEducation: bool
        :param _IsInstitution: <p>是否组织机构</p>
        :type IsInstitution: bool
        :param _IsCompany: <p>是否企业专线</p>
        :type IsCompany: bool
        :param _IsResidence: <p>是否家用宽带</p>
        :type IsResidence: bool
        :param _IsCloudService: <p>是否云服务</p>
        :type IsCloudService: bool
        :param _IsInfrastructure: <p>是否基础设施</p>
        :type IsInfrastructure: bool
        :param _IsMXServer: <p>是否邮箱服务</p>
        :type IsMXServer: bool
        """
        self._ISP = None
        self._ASN = None
        self._Organization = None
        self._IsReserved = None
        self._IsGateway = None
        self._IsAnycast = None
        self._IsMobile = None
        self._IsDynamic = None
        self._IsEgress = None
        self._IsDNS = None
        self._IsEducation = None
        self._IsInstitution = None
        self._IsCompany = None
        self._IsResidence = None
        self._IsCloudService = None
        self._IsInfrastructure = None
        self._IsMXServer = None

    @property
    def ISP(self):
        r"""<p>互联网服务提供商</p>
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def ASN(self):
        r"""<p>自治系统号</p>
        :rtype: str
        """
        return self._ASN

    @ASN.setter
    def ASN(self, ASN):
        self._ASN = ASN

    @property
    def Organization(self):
        r"""<p>IP注册组织名称</p>
        :rtype: str
        """
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def IsReserved(self):
        r"""<p>是否保留IP</p>
        :rtype: bool
        """
        return self._IsReserved

    @IsReserved.setter
    def IsReserved(self, IsReserved):
        self._IsReserved = IsReserved

    @property
    def IsGateway(self):
        r"""<p>是否网关IP</p>
        :rtype: bool
        """
        return self._IsGateway

    @IsGateway.setter
    def IsGateway(self, IsGateway):
        self._IsGateway = IsGateway

    @property
    def IsAnycast(self):
        r"""<p>是否任播网络</p>
        :rtype: bool
        """
        return self._IsAnycast

    @IsAnycast.setter
    def IsAnycast(self, IsAnycast):
        self._IsAnycast = IsAnycast

    @property
    def IsMobile(self):
        r"""<p>是否移动网络</p>
        :rtype: bool
        """
        return self._IsMobile

    @IsMobile.setter
    def IsMobile(self, IsMobile):
        self._IsMobile = IsMobile

    @property
    def IsDynamic(self):
        r"""<p>是否动态IP</p>
        :rtype: bool
        """
        return self._IsDynamic

    @IsDynamic.setter
    def IsDynamic(self, IsDynamic):
        self._IsDynamic = IsDynamic

    @property
    def IsEgress(self):
        r"""<p>是否网络出口</p>
        :rtype: bool
        """
        return self._IsEgress

    @IsEgress.setter
    def IsEgress(self, IsEgress):
        self._IsEgress = IsEgress

    @property
    def IsDNS(self):
        r"""<p>是否域名解析</p>
        :rtype: bool
        """
        return self._IsDNS

    @IsDNS.setter
    def IsDNS(self, IsDNS):
        self._IsDNS = IsDNS

    @property
    def IsEducation(self):
        r"""<p>是否教育机构</p>
        :rtype: bool
        """
        return self._IsEducation

    @IsEducation.setter
    def IsEducation(self, IsEducation):
        self._IsEducation = IsEducation

    @property
    def IsInstitution(self):
        r"""<p>是否组织机构</p>
        :rtype: bool
        """
        return self._IsInstitution

    @IsInstitution.setter
    def IsInstitution(self, IsInstitution):
        self._IsInstitution = IsInstitution

    @property
    def IsCompany(self):
        r"""<p>是否企业专线</p>
        :rtype: bool
        """
        return self._IsCompany

    @IsCompany.setter
    def IsCompany(self, IsCompany):
        self._IsCompany = IsCompany

    @property
    def IsResidence(self):
        r"""<p>是否家用宽带</p>
        :rtype: bool
        """
        return self._IsResidence

    @IsResidence.setter
    def IsResidence(self, IsResidence):
        self._IsResidence = IsResidence

    @property
    def IsCloudService(self):
        r"""<p>是否云服务</p>
        :rtype: bool
        """
        return self._IsCloudService

    @IsCloudService.setter
    def IsCloudService(self, IsCloudService):
        self._IsCloudService = IsCloudService

    @property
    def IsInfrastructure(self):
        r"""<p>是否基础设施</p>
        :rtype: bool
        """
        return self._IsInfrastructure

    @IsInfrastructure.setter
    def IsInfrastructure(self, IsInfrastructure):
        self._IsInfrastructure = IsInfrastructure

    @property
    def IsMXServer(self):
        r"""<p>是否邮箱服务</p>
        :rtype: bool
        """
        return self._IsMXServer

    @IsMXServer.setter
    def IsMXServer(self, IsMXServer):
        self._IsMXServer = IsMXServer


    def _deserialize(self, params):
        self._ISP = params.get("ISP")
        self._ASN = params.get("ASN")
        self._Organization = params.get("Organization")
        self._IsReserved = params.get("IsReserved")
        self._IsGateway = params.get("IsGateway")
        self._IsAnycast = params.get("IsAnycast")
        self._IsMobile = params.get("IsMobile")
        self._IsDynamic = params.get("IsDynamic")
        self._IsEgress = params.get("IsEgress")
        self._IsDNS = params.get("IsDNS")
        self._IsEducation = params.get("IsEducation")
        self._IsInstitution = params.get("IsInstitution")
        self._IsCompany = params.get("IsCompany")
        self._IsResidence = params.get("IsResidence")
        self._IsCloudService = params.get("IsCloudService")
        self._IsInfrastructure = params.get("IsInfrastructure")
        self._IsMXServer = params.get("IsMXServer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvitationEvent(AbstractModel):
    r"""邀请事件详情

    """

    def __init__(self):
        r"""
        :param _InviteeUserId: <p>受邀请人ID</p>
        :type InviteeUserId: str
        :param _PromotionId: <p>营销活动ID</p>
        :type PromotionId: str
        :param _PromotionName: <p>营销活动名称</p>
        :type PromotionName: str
        :param _Description: <p>营销活动描述</p>
        :type Description: str
        :param _InviteePhone: <p>受邀请人电话号码</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :type InviteePhone: str
        :param _InvitationCode: <p>邀请码</p>
        :type InvitationCode: str
        :param _InvitationUrl: <p>邀请链接</p>
        :type InvitationUrl: str
        :param _InvitationChannel: <p>邀请渠道，如微信、抖音、小红书等</p>
        :type InvitationChannel: str
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._InviteeUserId = None
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviteePhone = None
        self._InvitationCode = None
        self._InvitationUrl = None
        self._InvitationChannel = None
        self._Cust = None

    @property
    def InviteeUserId(self):
        r"""<p>受邀请人ID</p>
        :rtype: str
        """
        return self._InviteeUserId

    @InviteeUserId.setter
    def InviteeUserId(self, InviteeUserId):
        self._InviteeUserId = InviteeUserId

    @property
    def PromotionId(self):
        r"""<p>营销活动ID</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>营销活动名称</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>营销活动描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviteePhone(self):
        r"""<p>受邀请人电话号码</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :rtype: str
        """
        return self._InviteePhone

    @InviteePhone.setter
    def InviteePhone(self, InviteePhone):
        self._InviteePhone = InviteePhone

    @property
    def InvitationCode(self):
        r"""<p>邀请码</p>
        :rtype: str
        """
        return self._InvitationCode

    @InvitationCode.setter
    def InvitationCode(self, InvitationCode):
        self._InvitationCode = InvitationCode

    @property
    def InvitationUrl(self):
        r"""<p>邀请链接</p>
        :rtype: str
        """
        return self._InvitationUrl

    @InvitationUrl.setter
    def InvitationUrl(self, InvitationUrl):
        self._InvitationUrl = InvitationUrl

    @property
    def InvitationChannel(self):
        r"""<p>邀请渠道，如微信、抖音、小红书等</p>
        :rtype: str
        """
        return self._InvitationChannel

    @InvitationChannel.setter
    def InvitationChannel(self, InvitationChannel):
        self._InvitationChannel = InvitationChannel

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._InviteeUserId = params.get("InviteeUserId")
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviteePhone = params.get("InviteePhone")
        self._InvitationCode = params.get("InvitationCode")
        self._InvitationUrl = params.get("InvitationUrl")
        self._InvitationChannel = params.get("InvitationChannel")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inviter(AbstractModel):
    r"""邀请人信息

    """

    def __init__(self):
        r"""
        :param _InviterUserId: <p>邀请人ID</p>
        :type InviterUserId: str
        :param _InviterPhone: <p>邀请人电话号码</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :type InviterPhone: str
        :param _InviteCode: <p>邀请码</p>
        :type InviteCode: str
        :param _InviteChannel: <p>邀请渠道</p>
        :type InviteChannel: str
        """
        self._InviterUserId = None
        self._InviterPhone = None
        self._InviteCode = None
        self._InviteChannel = None

    @property
    def InviterUserId(self):
        r"""<p>邀请人ID</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def InviterPhone(self):
        r"""<p>邀请人电话号码</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :rtype: str
        """
        return self._InviterPhone

    @InviterPhone.setter
    def InviterPhone(self, InviterPhone):
        self._InviterPhone = InviterPhone

    @property
    def InviteCode(self):
        r"""<p>邀请码</p>
        :rtype: str
        """
        return self._InviteCode

    @InviteCode.setter
    def InviteCode(self, InviteCode):
        self._InviteCode = InviteCode

    @property
    def InviteChannel(self):
        r"""<p>邀请渠道</p>
        :rtype: str
        """
        return self._InviteChannel

    @InviteChannel.setter
    def InviteChannel(self, InviteChannel):
        self._InviteChannel = InviteChannel


    def _deserialize(self, params):
        self._InviterUserId = params.get("InviterUserId")
        self._InviterPhone = params.get("InviterPhone")
        self._InviteCode = params.get("InviteCode")
        self._InviteChannel = params.get("InviteChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Item(AbstractModel):
    r"""商品信息

    """

    def __init__(self):
        r"""
        :param _ItemId: <p>商品ID</p>
        :type ItemId: str
        :param _ItemName: <p>商品名称</p>
        :type ItemName: str
        :param _Category: <p>商品类别</p>
        :type Category: str
        :param _Price: <p>商品单价</p>
        :type Price: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _UPC: <p>如果商品有UPC码（Universal Product Code），请提供</p>
        :type UPC: str
        :param _EAN: <p>如果商品有EAN码（European Article Number），请提供</p>
        :type EAN: str
        :param _SKU: <p>如果商品有SKU码（Stock Keeping Unit），请提供</p>
        :type SKU: str
        :param _ISBN: <p>如果商品有ISBN码（International Standard Book Number ），请提供</p>
        :type ISBN: str
        :param _Brand: <p>商品品牌</p>
        :type Brand: str
        :param _Quantity: <p>商品数量</p>
        :type Quantity: int
        :param _Manufacturer: <p>生产厂商</p>
        :type Manufacturer: str
        :param _Tags: <p>商品标签</p>
        :type Tags: str
        """
        self._ItemId = None
        self._ItemName = None
        self._Category = None
        self._Price = None
        self._UPC = None
        self._EAN = None
        self._SKU = None
        self._ISBN = None
        self._Brand = None
        self._Quantity = None
        self._Manufacturer = None
        self._Tags = None

    @property
    def ItemId(self):
        r"""<p>商品ID</p>
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def ItemName(self):
        r"""<p>商品名称</p>
        :rtype: str
        """
        return self._ItemName

    @ItemName.setter
    def ItemName(self, ItemName):
        self._ItemName = ItemName

    @property
    def Category(self):
        r"""<p>商品类别</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Price(self):
        r"""<p>商品单价</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def UPC(self):
        r"""<p>如果商品有UPC码（Universal Product Code），请提供</p>
        :rtype: str
        """
        return self._UPC

    @UPC.setter
    def UPC(self, UPC):
        self._UPC = UPC

    @property
    def EAN(self):
        r"""<p>如果商品有EAN码（European Article Number），请提供</p>
        :rtype: str
        """
        return self._EAN

    @EAN.setter
    def EAN(self, EAN):
        self._EAN = EAN

    @property
    def SKU(self):
        r"""<p>如果商品有SKU码（Stock Keeping Unit），请提供</p>
        :rtype: str
        """
        return self._SKU

    @SKU.setter
    def SKU(self, SKU):
        self._SKU = SKU

    @property
    def ISBN(self):
        r"""<p>如果商品有ISBN码（International Standard Book Number ），请提供</p>
        :rtype: str
        """
        return self._ISBN

    @ISBN.setter
    def ISBN(self, ISBN):
        self._ISBN = ISBN

    @property
    def Brand(self):
        r"""<p>商品品牌</p>
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Quantity(self):
        r"""<p>商品数量</p>
        :rtype: int
        """
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Manufacturer(self):
        r"""<p>生产厂商</p>
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def Tags(self):
        r"""<p>商品标签</p>
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._ItemName = params.get("ItemName")
        self._Category = params.get("Category")
        if params.get("Price") is not None:
            self._Price = Amount()
            self._Price._deserialize(params.get("Price"))
        self._UPC = params.get("UPC")
        self._EAN = params.get("EAN")
        self._SKU = params.get("SKU")
        self._ISBN = params.get("ISBN")
        self._Brand = params.get("Brand")
        self._Quantity = params.get("Quantity")
        self._Manufacturer = params.get("Manufacturer")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginEvent(AbstractModel):
    r"""登录事件详情

    """

    def __init__(self):
        r"""
        :param _UserInfo: <p>用户基础信息</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _UserLoginName: <p>用户登录时输入的用户名</p>
        :type UserLoginName: str
        :param _LoginResult: <p>登录结果</p>
        :type LoginResult: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._UserInfo = None
        self._UserLoginName = None
        self._LoginResult = None
        self._Cust = None

    @property
    def UserInfo(self):
        r"""<p>用户基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def UserLoginName(self):
        r"""<p>用户登录时输入的用户名</p>
        :rtype: str
        """
        return self._UserLoginName

    @UserLoginName.setter
    def UserLoginName(self, UserLoginName):
        self._UserLoginName = UserLoginName

    @property
    def LoginResult(self):
        r"""<p>登录结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._LoginResult

    @LoginResult.setter
    def LoginResult(self, LoginResult):
        self._LoginResult = LoginResult

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._UserLoginName = params.get("UserLoginName")
        if params.get("LoginResult") is not None:
            self._LoginResult = Result()
            self._LoginResult._deserialize(params.get("LoginResult"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoutEvent(AbstractModel):
    r"""登出事件详情

    """

    def __init__(self):
        r"""
        :param _UserInfo: <p>用户基础信息</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _UserLoginName: <p>用户登录时输入的用户名</p>
        :type UserLoginName: str
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._UserInfo = None
        self._UserLoginName = None
        self._Cust = None

    @property
    def UserInfo(self):
        r"""<p>用户基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def UserLoginName(self):
        r"""<p>用户登录时输入的用户名</p>
        :rtype: str
        """
        return self._UserLoginName

    @UserLoginName.setter
    def UserLoginName(self, UserLoginName):
        self._UserLoginName = UserLoginName

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._UserLoginName = params.get("UserLoginName")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LuckyDrawEvent(AbstractModel):
    r"""抽奖事件详情

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>营销活动ID</p>
        :type PromotionId: str
        :param _PromotionName: <p>营销活动名称</p>
        :type PromotionName: str
        :param _Description: <p>营销活动描述</p>
        :type Description: str
        :param _InviterUserId: <p>邀请人ID</p>
        :type InviterUserId: str
        :param _LuckyDrawCount: <p>抽奖次数</p><p>单位：次数</p>
        :type LuckyDrawCount: int
        :param _LuckyDrawType: <p>抽奖类型</p>
        :type LuckyDrawType: str
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._LuckyDrawCount = None
        self._LuckyDrawType = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>营销活动ID</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>营销活动名称</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>营销活动描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>邀请人ID</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def LuckyDrawCount(self):
        r"""<p>抽奖次数</p><p>单位：次数</p>
        :rtype: int
        """
        return self._LuckyDrawCount

    @LuckyDrawCount.setter
    def LuckyDrawCount(self, LuckyDrawCount):
        self._LuckyDrawCount = LuckyDrawCount

    @property
    def LuckyDrawType(self):
        r"""<p>抽奖类型</p>
        :rtype: str
        """
        return self._LuckyDrawType

    @LuckyDrawType.setter
    def LuckyDrawType(self, LuckyDrawType):
        self._LuckyDrawType = LuckyDrawType

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        self._LuckyDrawCount = params.get("LuckyDrawCount")
        self._LuckyDrawType = params.get("LuckyDrawType")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Merchant(AbstractModel):
    r"""商家信息

    """

    def __init__(self):
        r"""
        :param _MerchantId: <p>商家ID</p>
        :type MerchantId: str
        :param _Name: <p>商家名称</p>
        :type Name: str
        :param _RegisterTime: <p>商家的注册时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :type RegisterTime: str
        :param _Category: <p>商家类别代码</p><p>参数格式：符合ISO 18245标准的4位编号</p>
        :type Category: str
        :param _Phone: <p>商家电话</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :type Phone: str
        :param _Email: <p>商家邮件</p>
        :type Email: str
        :param _URL: <p>商家店铺网址</p>
        :type URL: str
        :param _Address: <p>商家地址</p>
        :type Address: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Level: <p>商家等级</p>
        :type Level: str
        :param _BusinessType: <p>经营类型</p><p>枚举值：</p><ul><li>person： 个人</li><li>company： 企业</li></ul>
        :type BusinessType: str
        :param _GoodsQuantity: <p>商家在售商品数量</p>
        :type GoodsQuantity: int
        :param _HistoricSalesQuantity: <p>商家历史销售数量</p>
        :type HistoricSalesQuantity: int
        :param _HistoricSalesAmount: <p>商家历史销售总额</p>
        :type HistoricSalesAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        self._MerchantId = None
        self._Name = None
        self._RegisterTime = None
        self._Category = None
        self._Phone = None
        self._Email = None
        self._URL = None
        self._Address = None
        self._Level = None
        self._BusinessType = None
        self._GoodsQuantity = None
        self._HistoricSalesQuantity = None
        self._HistoricSalesAmount = None

    @property
    def MerchantId(self):
        r"""<p>商家ID</p>
        :rtype: str
        """
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def Name(self):
        r"""<p>商家名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RegisterTime(self):
        r"""<p>商家的注册时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :rtype: str
        """
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def Category(self):
        r"""<p>商家类别代码</p><p>参数格式：符合ISO 18245标准的4位编号</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Phone(self):
        r"""<p>商家电话</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""<p>商家邮件</p>
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def URL(self):
        r"""<p>商家店铺网址</p>
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Address(self):
        r"""<p>商家地址</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Level(self):
        r"""<p>商家等级</p>
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def BusinessType(self):
        r"""<p>经营类型</p><p>枚举值：</p><ul><li>person： 个人</li><li>company： 企业</li></ul>
        :rtype: str
        """
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def GoodsQuantity(self):
        r"""<p>商家在售商品数量</p>
        :rtype: int
        """
        return self._GoodsQuantity

    @GoodsQuantity.setter
    def GoodsQuantity(self, GoodsQuantity):
        self._GoodsQuantity = GoodsQuantity

    @property
    def HistoricSalesQuantity(self):
        r"""<p>商家历史销售数量</p>
        :rtype: int
        """
        return self._HistoricSalesQuantity

    @HistoricSalesQuantity.setter
    def HistoricSalesQuantity(self, HistoricSalesQuantity):
        self._HistoricSalesQuantity = HistoricSalesQuantity

    @property
    def HistoricSalesAmount(self):
        r"""<p>商家历史销售总额</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._HistoricSalesAmount

    @HistoricSalesAmount.setter
    def HistoricSalesAmount(self, HistoricSalesAmount):
        self._HistoricSalesAmount = HistoricSalesAmount


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._Name = params.get("Name")
        self._RegisterTime = params.get("RegisterTime")
        self._Category = params.get("Category")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._URL = params.get("URL")
        if params.get("Address") is not None:
            self._Address = Address()
            self._Address._deserialize(params.get("Address"))
        self._Level = params.get("Level")
        self._BusinessType = params.get("BusinessType")
        self._GoodsQuantity = params.get("GoodsQuantity")
        self._HistoricSalesQuantity = params.get("HistoricSalesQuantity")
        if params.get("HistoricSalesAmount") is not None:
            self._HistoricSalesAmount = Amount()
            self._HistoricSalesAmount._deserialize(params.get("HistoricSalesAmount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountEvent(AbstractModel):
    r"""修改账号事件详情

    """

    def __init__(self):
        r"""
        :param _UserInfo: <p>用户基础信息</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _Person: <p>用户填写的个人信息</p>
        :type Person: :class:`tencentcloud.rce.v20260130.models.Person`
        :param _BillingAddress: <p>用户填写的账单地址</p>
        :type BillingAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _DeliveryAddress: <p>用户填写的收货地址</p>
        :type DeliveryAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._UserInfo = None
        self._Person = None
        self._BillingAddress = None
        self._DeliveryAddress = None
        self._Cust = None

    @property
    def UserInfo(self):
        r"""<p>用户基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def Person(self):
        r"""<p>用户填写的个人信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Person`
        """
        return self._Person

    @Person.setter
    def Person(self, Person):
        self._Person = Person

    @property
    def BillingAddress(self):
        r"""<p>用户填写的账单地址</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._BillingAddress

    @BillingAddress.setter
    def BillingAddress(self, BillingAddress):
        self._BillingAddress = BillingAddress

    @property
    def DeliveryAddress(self):
        r"""<p>用户填写的收货地址</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._DeliveryAddress

    @DeliveryAddress.setter
    def DeliveryAddress(self, DeliveryAddress):
        self._DeliveryAddress = DeliveryAddress

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("Person") is not None:
            self._Person = Person()
            self._Person._deserialize(params.get("Person"))
        if params.get("BillingAddress") is not None:
            self._BillingAddress = Address()
            self._BillingAddress._deserialize(params.get("BillingAddress"))
        if params.get("DeliveryAddress") is not None:
            self._DeliveryAddress = Address()
            self._DeliveryAddress._deserialize(params.get("DeliveryAddress"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPasswordEvent(AbstractModel):
    r"""修改密码事件详情

    """

    def __init__(self):
        r"""
        :param _Reason: <p>修改原因</p><p>枚举值：</p><ul><li>user_modify： 用户主动修改</li><li>forgot_password： 忘记密码</li><li>forced_reset： 系统强制重置</li></ul>
        :type Reason: str
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._Reason = None
        self._Cust = None

    @property
    def Reason(self):
        r"""<p>修改原因</p><p>枚举值：</p><ul><li>user_modify： 用户主动修改</li><li>forgot_password： 忘记密码</li><li>forced_reset： 系统强制重置</li></ul>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Order(AbstractModel):
    r"""订单信息

    """

    def __init__(self):
        r"""
        :param _OrderId: <p>订单ID</p>
        :type OrderId: str
        :param _Amount: <p>订单金额</p>
        :type Amount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Items: <p>商品信息</p>
        :type Items: list of Item
        :param _Delivery: <p>物流信息</p>
        :type Delivery: :class:`tencentcloud.rce.v20260130.models.Delivery`
        """
        self._OrderId = None
        self._Amount = None
        self._Items = None
        self._Delivery = None

    @property
    def OrderId(self):
        r"""<p>订单ID</p>
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Amount(self):
        r"""<p>订单金额</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Items(self):
        r"""<p>商品信息</p>
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Delivery(self):
        r"""<p>物流信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Delivery`
        """
        return self._Delivery

    @Delivery.setter
    def Delivery(self, Delivery):
        self._Delivery = Delivery


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        if params.get("Amount") is not None:
            self._Amount = Amount()
            self._Amount._deserialize(params.get("Amount"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Delivery") is not None:
            self._Delivery = Delivery()
            self._Delivery._deserialize(params.get("Delivery"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentMethod(AbstractModel):
    r"""支付方式，支持多种支付方式

    """

    def __init__(self):
        r"""
        :param _PaymentType: <p>支付方式</p><p>枚举值：</p><ul><li>cash： 现金</li><li>check： 支票</li><li>credit_card： 信用卡</li><li>debit_card： 借记卡</li><li>crypto_currency： 加密货币</li><li>digital_wallet： 数字钱包</li><li>gift_card： 礼品卡</li><li>points： 积分</li><li>in_app_purchase： APP内购买</li><li>electronic_fund_transfer： 电子资金转账</li><li>financing： 融资</li><li>invoice： 发票</li><li>prepaid_card： 预付卡</li><li>sepa_credit： SEPA信用转账</li></ul>
        :type PaymentType: str
        :param _PaymentChannel: <p>支付渠道</p>
        :type PaymentChannel: str
        :param _Card: <p>银行卡信息，当用支付方式是credit_card、debit_card时必填</p>
        :type Card: :class:`tencentcloud.rce.v20260130.models.Card`
        :param _SEPADirectDebitMandate: <p>SEPA直接借记授权</p><p>枚举值：</p><ul><li>true： 是</li><li>false： 否</li></ul>
        :type SEPADirectDebitMandate: bool
        :param _DigitalWallet: <p>数字钱包</p>
        :type DigitalWallet: :class:`tencentcloud.rce.v20260130.models.Wallet`
        """
        self._PaymentType = None
        self._PaymentChannel = None
        self._Card = None
        self._SEPADirectDebitMandate = None
        self._DigitalWallet = None

    @property
    def PaymentType(self):
        r"""<p>支付方式</p><p>枚举值：</p><ul><li>cash： 现金</li><li>check： 支票</li><li>credit_card： 信用卡</li><li>debit_card： 借记卡</li><li>crypto_currency： 加密货币</li><li>digital_wallet： 数字钱包</li><li>gift_card： 礼品卡</li><li>points： 积分</li><li>in_app_purchase： APP内购买</li><li>electronic_fund_transfer： 电子资金转账</li><li>financing： 融资</li><li>invoice： 发票</li><li>prepaid_card： 预付卡</li><li>sepa_credit： SEPA信用转账</li></ul>
        :rtype: str
        """
        return self._PaymentType

    @PaymentType.setter
    def PaymentType(self, PaymentType):
        self._PaymentType = PaymentType

    @property
    def PaymentChannel(self):
        r"""<p>支付渠道</p>
        :rtype: str
        """
        return self._PaymentChannel

    @PaymentChannel.setter
    def PaymentChannel(self, PaymentChannel):
        self._PaymentChannel = PaymentChannel

    @property
    def Card(self):
        r"""<p>银行卡信息，当用支付方式是credit_card、debit_card时必填</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Card`
        """
        return self._Card

    @Card.setter
    def Card(self, Card):
        self._Card = Card

    @property
    def SEPADirectDebitMandate(self):
        r"""<p>SEPA直接借记授权</p><p>枚举值：</p><ul><li>true： 是</li><li>false： 否</li></ul>
        :rtype: bool
        """
        return self._SEPADirectDebitMandate

    @SEPADirectDebitMandate.setter
    def SEPADirectDebitMandate(self, SEPADirectDebitMandate):
        self._SEPADirectDebitMandate = SEPADirectDebitMandate

    @property
    def DigitalWallet(self):
        r"""<p>数字钱包</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Wallet`
        """
        return self._DigitalWallet

    @DigitalWallet.setter
    def DigitalWallet(self, DigitalWallet):
        self._DigitalWallet = DigitalWallet


    def _deserialize(self, params):
        self._PaymentType = params.get("PaymentType")
        self._PaymentChannel = params.get("PaymentChannel")
        if params.get("Card") is not None:
            self._Card = Card()
            self._Card._deserialize(params.get("Card"))
        self._SEPADirectDebitMandate = params.get("SEPADirectDebitMandate")
        if params.get("DigitalWallet") is not None:
            self._DigitalWallet = Wallet()
            self._DigitalWallet._deserialize(params.get("DigitalWallet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentResult(AbstractModel):
    r"""支付结果

    """

    def __init__(self):
        r"""
        :param _Status: <p>支付状态</p><p>枚举值：</p><ul><li>success： 成功</li><li>failure： 失败</li></ul>
        :type Status: str
        :param _FailureReason: <p>支付失败原因</p>
        :type FailureReason: str
        :param _ThreeDomainSecure: <p>是否使用3DS，枚举值：</p><ul><li>是：true</li><li>否：false</li></ul>
        :type ThreeDomainSecure: bool
        :param _ECICode: <p>ECI返回码</p>
        :type ECICode: str
        :param _AVSCode: <p>AVS响应结果（地址验证）</p>
        :type AVSCode: str
        :param _CVCCode: <p>CVC验证结果（交易真实性验证）</p>
        :type CVCCode: str
        """
        self._Status = None
        self._FailureReason = None
        self._ThreeDomainSecure = None
        self._ECICode = None
        self._AVSCode = None
        self._CVCCode = None

    @property
    def Status(self):
        r"""<p>支付状态</p><p>枚举值：</p><ul><li>success： 成功</li><li>failure： 失败</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailureReason(self):
        r"""<p>支付失败原因</p>
        :rtype: str
        """
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def ThreeDomainSecure(self):
        r"""<p>是否使用3DS，枚举值：</p><ul><li>是：true</li><li>否：false</li></ul>
        :rtype: bool
        """
        return self._ThreeDomainSecure

    @ThreeDomainSecure.setter
    def ThreeDomainSecure(self, ThreeDomainSecure):
        self._ThreeDomainSecure = ThreeDomainSecure

    @property
    def ECICode(self):
        r"""<p>ECI返回码</p>
        :rtype: str
        """
        return self._ECICode

    @ECICode.setter
    def ECICode(self, ECICode):
        self._ECICode = ECICode

    @property
    def AVSCode(self):
        r"""<p>AVS响应结果（地址验证）</p>
        :rtype: str
        """
        return self._AVSCode

    @AVSCode.setter
    def AVSCode(self, AVSCode):
        self._AVSCode = AVSCode

    @property
    def CVCCode(self):
        r"""<p>CVC验证结果（交易真实性验证）</p>
        :rtype: str
        """
        return self._CVCCode

    @CVCCode.setter
    def CVCCode(self, CVCCode):
        self._CVCCode = CVCCode


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FailureReason = params.get("FailureReason")
        self._ThreeDomainSecure = params.get("ThreeDomainSecure")
        self._ECICode = params.get("ECICode")
        self._AVSCode = params.get("AVSCode")
        self._CVCCode = params.get("CVCCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Person(AbstractModel):
    r"""个人信息

    """

    def __init__(self):
        r"""
        :param _Name: <p>姓名全称</p>
        :type Name: str
        :param _Gender: <p>性别</p>
        :type Gender: str
        :param _Birthday: <p>出生日期</p><p>参数格式：YYYY-MM-DD</p>
        :type Birthday: str
        :param _Degree: <p>学历</p>
        :type Degree: str
        :param _Occupation: <p>职业</p>
        :type Occupation: str
        """
        self._Name = None
        self._Gender = None
        self._Birthday = None
        self._Degree = None
        self._Occupation = None

    @property
    def Name(self):
        r"""<p>姓名全称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Gender(self):
        r"""<p>性别</p>
        :rtype: str
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Birthday(self):
        r"""<p>出生日期</p><p>参数格式：YYYY-MM-DD</p>
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Degree(self):
        r"""<p>学历</p>
        :rtype: str
        """
        return self._Degree

    @Degree.setter
    def Degree(self, Degree):
        self._Degree = Degree

    @property
    def Occupation(self):
        r"""<p>职业</p>
        :rtype: str
        """
        return self._Occupation

    @Occupation.setter
    def Occupation(self, Occupation):
        self._Occupation = Occupation


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Gender = params.get("Gender")
        self._Birthday = params.get("Birthday")
        self._Degree = params.get("Degree")
        self._Occupation = params.get("Occupation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Promotion(AbstractModel):
    r"""营销活动

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>营销活动ID</p>
        :type PromotionId: str
        :param _PromotionName: <p>营销活动名称</p>
        :type PromotionName: str
        :param _Description: <p>营销活动描述</p>
        :type Description: str
        :param _InviterUserId: <p>邀请人ID</p>
        :type InviterUserId: str
        :param _Coupon: <p>优惠券</p>
        :type Coupon: :class:`tencentcloud.rce.v20260130.models.Coupon`
        :param _CreditPoint: <p>积分</p>
        :type CreditPoint: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._Coupon = None
        self._CreditPoint = None

    @property
    def PromotionId(self):
        r"""<p>营销活动ID</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>营销活动名称</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>营销活动描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>邀请人ID</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def Coupon(self):
        r"""<p>优惠券</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Coupon`
        """
        return self._Coupon

    @Coupon.setter
    def Coupon(self, Coupon):
        self._Coupon = Coupon

    @property
    def CreditPoint(self):
        r"""<p>积分</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        """
        return self._CreditPoint

    @CreditPoint.setter
    def CreditPoint(self, CreditPoint):
        self._CreditPoint = CreditPoint


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        if params.get("Coupon") is not None:
            self._Coupon = Coupon()
            self._Coupon._deserialize(params.get("Coupon"))
        if params.get("CreditPoint") is not None:
            self._CreditPoint = CreditPoint()
            self._CreditPoint._deserialize(params.get("CreditPoint"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PromotionCode(AbstractModel):
    r"""营销活动码

    """

    def __init__(self):
        r"""
        :param _Id: <p>活动码ID</p>
        :type Id: str
        :param _Type: <p>活动码类型，例如：qrcode-二维码、barcode-条形码、miniprogram_code-小程序码</p>
        :type Type: str
        :param _ImageLink: <p>活动码图片URL或链接</p>
        :type ImageLink: str
        :param _Address: <p>营销活动码使用地址</p>
        :type Address: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Items: <p>营销活动码关联的商品</p>
        :type Items: list of Item
        """
        self._Id = None
        self._Type = None
        self._ImageLink = None
        self._Address = None
        self._Items = None

    @property
    def Id(self):
        r"""<p>活动码ID</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        r"""<p>活动码类型，例如：qrcode-二维码、barcode-条形码、miniprogram_code-小程序码</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ImageLink(self):
        r"""<p>活动码图片URL或链接</p>
        :rtype: str
        """
        return self._ImageLink

    @ImageLink.setter
    def ImageLink(self, ImageLink):
        self._ImageLink = ImageLink

    @property
    def Address(self):
        r"""<p>营销活动码使用地址</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Items(self):
        r"""<p>营销活动码关联的商品</p>
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._ImageLink = params.get("ImageLink")
        if params.get("Address") is not None:
            self._Address = Address()
            self._Address._deserialize(params.get("Address"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedeemEvent(AbstractModel):
    r"""兑奖事件详情

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>营销活动ID</p>
        :type PromotionId: str
        :param _PromotionName: <p>营销活动名称</p>
        :type PromotionName: str
        :param _Description: <p>营销活动描述</p>
        :type Description: str
        :param _InviterUserId: <p>邀请人ID</p>
        :type InviterUserId: str
        :param _Order: <p>兑奖关联的订单信息</p>
        :type Order: :class:`tencentcloud.rce.v20260130.models.Order`
        :param _Result: <p>兑奖结果</p>
        :type Result: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._Order = None
        self._Result = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>营销活动ID</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>营销活动名称</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>营销活动描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>邀请人ID</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def Order(self):
        r"""<p>兑奖关联的订单信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Order`
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Result(self):
        r"""<p>兑奖结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        if params.get("Order") is not None:
            self._Order = Order()
            self._Order._deserialize(params.get("Order"))
        if params.get("Result") is not None:
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterEvent(AbstractModel):
    r"""注册事件详情

    """

    def __init__(self):
        r"""
        :param _RegisterResult: <p>注册结果</p>
        :type RegisterResult: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _UserInfo: <p>用户基础信息</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _Person: <p>用户注册时填写的个人信息</p>
        :type Person: :class:`tencentcloud.rce.v20260130.models.Person`
        :param _BillingAddress: <p>用户注册时填写的账单地址</p>
        :type BillingAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _DeliveryAddress: <p>用户注册时填写的收货地址</p>
        :type DeliveryAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Inviter: <p>邀请人信息</p>
        :type Inviter: :class:`tencentcloud.rce.v20260130.models.Inviter`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._RegisterResult = None
        self._UserInfo = None
        self._Person = None
        self._BillingAddress = None
        self._DeliveryAddress = None
        self._Inviter = None
        self._Cust = None

    @property
    def RegisterResult(self):
        r"""<p>注册结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._RegisterResult

    @RegisterResult.setter
    def RegisterResult(self, RegisterResult):
        self._RegisterResult = RegisterResult

    @property
    def UserInfo(self):
        r"""<p>用户基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def Person(self):
        r"""<p>用户注册时填写的个人信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Person`
        """
        return self._Person

    @Person.setter
    def Person(self, Person):
        self._Person = Person

    @property
    def BillingAddress(self):
        r"""<p>用户注册时填写的账单地址</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._BillingAddress

    @BillingAddress.setter
    def BillingAddress(self, BillingAddress):
        self._BillingAddress = BillingAddress

    @property
    def DeliveryAddress(self):
        r"""<p>用户注册时填写的收货地址</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._DeliveryAddress

    @DeliveryAddress.setter
    def DeliveryAddress(self, DeliveryAddress):
        self._DeliveryAddress = DeliveryAddress

    @property
    def Inviter(self):
        r"""<p>邀请人信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Inviter`
        """
        return self._Inviter

    @Inviter.setter
    def Inviter(self, Inviter):
        self._Inviter = Inviter

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("RegisterResult") is not None:
            self._RegisterResult = Result()
            self._RegisterResult._deserialize(params.get("RegisterResult"))
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("Person") is not None:
            self._Person = Person()
            self._Person._deserialize(params.get("Person"))
        if params.get("BillingAddress") is not None:
            self._BillingAddress = Address()
            self._BillingAddress._deserialize(params.get("BillingAddress"))
        if params.get("DeliveryAddress") is not None:
            self._DeliveryAddress = Address()
            self._DeliveryAddress._deserialize(params.get("DeliveryAddress"))
        if params.get("Inviter") is not None:
            self._Inviter = Inviter()
            self._Inviter._deserialize(params.get("Inviter"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportEventRequest(AbstractModel):
    r"""ReportEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventCode: <p>事件码，标准事件包含：</p><p>枚举值：</p><ul><li>login： 登录</li><li>register： 注册</li><li>create_order： 创建订单</li><li>transaction： 交易支付</li><li>charge_back： 拒付</li><li>sms： 短信</li><li>logout： 登出</li><li>modify_account： 修改账号</li><li>modify_password： 修改密码</li><li>security_verification： 安全验证</li><li>add_promotion： 参加营销活动</li><li>redeem： 兑奖</li><li>withdraw： 提现</li><li>cust_event： 自定义事件，cust_xxx</li><li>scan_code： 扫码</li><li>lucky_draw： 抽奖</li><li>task： 做任务</li><li>invitation： 邀请</li><li>claim_red_packet： 领红包</li><li>browse： 浏览</li></ul><p>自定义事件可与RCE约定后进行风险评估</p>
        :type EventCode: str
        :param _EventTime: <p>事件的发生时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :type EventTime: str
        :param _SessionId: <p>用户当前会话 ID， 用于关联用户登录前后的动作，如果没有传UserId，则SessionId必传，如缺失则可填充空字符串</p>
        :type SessionId: str
        :param _DeviceToken: <p>用户设备指纹token标识，在您的网站或者应用程序中集成设备指纹的SDK后获取</p>
        :type DeviceToken: str
        :param _UserIp: <p>客户端 IP 地址（IPv4或IPv6）</p>
        :type UserIp: str
        :param _EventDetail: <p>事件详情，根据您输入的事件码传入对应的事件信息</p>
        :type EventDetail: :class:`tencentcloud.rce.v20260130.models.EventDetail`
        :param _UserId: <p>用户在您系统中的唯一ID</p>
        :type UserId: str
        :param _UserEmail: <p>用户邮箱</p>
        :type UserEmail: str
        :param _UserPhone: <p>用户提供的联系方式</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :type UserPhone: str
        :param _Browser: <p>web浏览器相关信息，若您已集成我们的设备指纹SDK，则无需传入此字段</p>
        :type Browser: :class:`tencentcloud.rce.v20260130.models.Browser`
        :param _App: <p>应用程序、操作系统和移动设备详细信息，若您已集成我们的设备指纹SDK，则无需传入此字段</p>
        :type App: :class:`tencentcloud.rce.v20260130.models.App`
        :param _DataAuthorization: <p>数据授权信息，国内地域必填</p>
        :type DataAuthorization: :class:`tencentcloud.rce.v20260130.models.DataAuthorization`
        :param _UserPhoneEncrypt: <p>手机号码加密方式，国内地域必填</p><p>枚举值：</p><ul><li>md5： md5加密</li><li>plain： 明文</li></ul>
        :type UserPhoneEncrypt: str
        :param _WeChatOpenId: <p>微信开放账号</p>
        :type WeChatOpenId: str
        :param _QQOpenId: <p>QQ开放账号</p>
        :type QQOpenId: str
        :param _QQAppId: <p>QQ应用ID，当传入QQ开放账号时，该字段必填，QQ分配给网站或应用的AppId，用来唯一标识网站或应用</p>
        :type QQAppId: str
        """
        self._EventCode = None
        self._EventTime = None
        self._SessionId = None
        self._DeviceToken = None
        self._UserIp = None
        self._EventDetail = None
        self._UserId = None
        self._UserEmail = None
        self._UserPhone = None
        self._Browser = None
        self._App = None
        self._DataAuthorization = None
        self._UserPhoneEncrypt = None
        self._WeChatOpenId = None
        self._QQOpenId = None
        self._QQAppId = None

    @property
    def EventCode(self):
        r"""<p>事件码，标准事件包含：</p><p>枚举值：</p><ul><li>login： 登录</li><li>register： 注册</li><li>create_order： 创建订单</li><li>transaction： 交易支付</li><li>charge_back： 拒付</li><li>sms： 短信</li><li>logout： 登出</li><li>modify_account： 修改账号</li><li>modify_password： 修改密码</li><li>security_verification： 安全验证</li><li>add_promotion： 参加营销活动</li><li>redeem： 兑奖</li><li>withdraw： 提现</li><li>cust_event： 自定义事件，cust_xxx</li><li>scan_code： 扫码</li><li>lucky_draw： 抽奖</li><li>task： 做任务</li><li>invitation： 邀请</li><li>claim_red_packet： 领红包</li><li>browse： 浏览</li></ul><p>自定义事件可与RCE约定后进行风险评估</p>
        :rtype: str
        """
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventTime(self):
        r"""<p>事件的发生时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def SessionId(self):
        r"""<p>用户当前会话 ID， 用于关联用户登录前后的动作，如果没有传UserId，则SessionId必传，如缺失则可填充空字符串</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def DeviceToken(self):
        r"""<p>用户设备指纹token标识，在您的网站或者应用程序中集成设备指纹的SDK后获取</p>
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def UserIp(self):
        r"""<p>客户端 IP 地址（IPv4或IPv6）</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def EventDetail(self):
        r"""<p>事件详情，根据您输入的事件码传入对应的事件信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.EventDetail`
        """
        return self._EventDetail

    @EventDetail.setter
    def EventDetail(self, EventDetail):
        self._EventDetail = EventDetail

    @property
    def UserId(self):
        r"""<p>用户在您系统中的唯一ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserEmail(self):
        r"""<p>用户邮箱</p>
        :rtype: str
        """
        return self._UserEmail

    @UserEmail.setter
    def UserEmail(self, UserEmail):
        self._UserEmail = UserEmail

    @property
    def UserPhone(self):
        r"""<p>用户提供的联系方式</p><p>参数格式：符合E.164标准的带“+”、地区编码和号码的格式</p>
        :rtype: str
        """
        return self._UserPhone

    @UserPhone.setter
    def UserPhone(self, UserPhone):
        self._UserPhone = UserPhone

    @property
    def Browser(self):
        r"""<p>web浏览器相关信息，若您已集成我们的设备指纹SDK，则无需传入此字段</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Browser`
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def App(self):
        r"""<p>应用程序、操作系统和移动设备详细信息，若您已集成我们的设备指纹SDK，则无需传入此字段</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.App`
        """
        return self._App

    @App.setter
    def App(self, App):
        self._App = App

    @property
    def DataAuthorization(self):
        r"""<p>数据授权信息，国内地域必填</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataAuthorization`
        """
        return self._DataAuthorization

    @DataAuthorization.setter
    def DataAuthorization(self, DataAuthorization):
        self._DataAuthorization = DataAuthorization

    @property
    def UserPhoneEncrypt(self):
        r"""<p>手机号码加密方式，国内地域必填</p><p>枚举值：</p><ul><li>md5： md5加密</li><li>plain： 明文</li></ul>
        :rtype: str
        """
        return self._UserPhoneEncrypt

    @UserPhoneEncrypt.setter
    def UserPhoneEncrypt(self, UserPhoneEncrypt):
        self._UserPhoneEncrypt = UserPhoneEncrypt

    @property
    def WeChatOpenId(self):
        r"""<p>微信开放账号</p>
        :rtype: str
        """
        return self._WeChatOpenId

    @WeChatOpenId.setter
    def WeChatOpenId(self, WeChatOpenId):
        self._WeChatOpenId = WeChatOpenId

    @property
    def QQOpenId(self):
        r"""<p>QQ开放账号</p>
        :rtype: str
        """
        return self._QQOpenId

    @QQOpenId.setter
    def QQOpenId(self, QQOpenId):
        self._QQOpenId = QQOpenId

    @property
    def QQAppId(self):
        r"""<p>QQ应用ID，当传入QQ开放账号时，该字段必填，QQ分配给网站或应用的AppId，用来唯一标识网站或应用</p>
        :rtype: str
        """
        return self._QQAppId

    @QQAppId.setter
    def QQAppId(self, QQAppId):
        self._QQAppId = QQAppId


    def _deserialize(self, params):
        self._EventCode = params.get("EventCode")
        self._EventTime = params.get("EventTime")
        self._SessionId = params.get("SessionId")
        self._DeviceToken = params.get("DeviceToken")
        self._UserIp = params.get("UserIp")
        if params.get("EventDetail") is not None:
            self._EventDetail = EventDetail()
            self._EventDetail._deserialize(params.get("EventDetail"))
        self._UserId = params.get("UserId")
        self._UserEmail = params.get("UserEmail")
        self._UserPhone = params.get("UserPhone")
        if params.get("Browser") is not None:
            self._Browser = Browser()
            self._Browser._deserialize(params.get("Browser"))
        if params.get("App") is not None:
            self._App = App()
            self._App._deserialize(params.get("App"))
        if params.get("DataAuthorization") is not None:
            self._DataAuthorization = DataAuthorization()
            self._DataAuthorization._deserialize(params.get("DataAuthorization"))
        self._UserPhoneEncrypt = params.get("UserPhoneEncrypt")
        self._WeChatOpenId = params.get("WeChatOpenId")
        self._QQOpenId = params.get("QQOpenId")
        self._QQAppId = params.get("QQAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportEventResponse(AbstractModel):
    r"""ReportEvent返回参数结构体

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


class Result(AbstractModel):
    r"""事件结果

    """

    def __init__(self):
        r"""
        :param _Status: <p>实际是否完成状态</p><p>枚举值：</p><ul><li>success： 成功</li><li>failure： 失败</li></ul>
        :type Status: str
        :param _FailureReason: <p>失败原因</p>
        :type FailureReason: str
        """
        self._Status = None
        self._FailureReason = None

    @property
    def Status(self):
        r"""<p>实际是否完成状态</p><p>枚举值：</p><ul><li>success： 成功</li><li>failure： 失败</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailureReason(self):
        r"""<p>失败原因</p>
        :rtype: str
        """
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FailureReason = params.get("FailureReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskLabel(AbstractModel):
    r"""风险标签

    """

    def __init__(self):
        r"""
        :param _Id: <p>风险ID</p>
        :type Id: str
        :param _Reason: <p>风险描述</p>
        :type Reason: str
        """
        self._Id = None
        self._Reason = None

    @property
    def Id(self):
        r"""<p>风险ID</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Reason(self):
        r"""<p>风险描述</p>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SMSEvent(AbstractModel):
    r"""短信事件详情

    """

    def __init__(self):
        r"""
        :param _UserInfo: <p>用户基础信息</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _SMSId: <p>本次短信发送标识 ID</p>
        :type SMSId: str
        :param _ReceivedTime: <p>用户实际完成验证码时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :type ReceivedTime: str
        :param _Action: <p>记录用户收到短信的动作</p><ul><li>no_action：用户无动作</li><li>safe：用户确认本人操作</li><li>compromised：用户反馈为第三方操作</li></ul>
        :type Action: str
        :param _SMSResult: <p>短信回执结果</p>
        :type SMSResult: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._UserInfo = None
        self._SMSId = None
        self._ReceivedTime = None
        self._Action = None
        self._SMSResult = None
        self._Cust = None

    @property
    def UserInfo(self):
        r"""<p>用户基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def SMSId(self):
        r"""<p>本次短信发送标识 ID</p>
        :rtype: str
        """
        return self._SMSId

    @SMSId.setter
    def SMSId(self, SMSId):
        self._SMSId = SMSId

    @property
    def ReceivedTime(self):
        r"""<p>用户实际完成验证码时间</p><p>参数格式：符合ISO 8601标准的带UTC时区的毫秒级时间</p>
        :rtype: str
        """
        return self._ReceivedTime

    @ReceivedTime.setter
    def ReceivedTime(self, ReceivedTime):
        self._ReceivedTime = ReceivedTime

    @property
    def Action(self):
        r"""<p>记录用户收到短信的动作</p><ul><li>no_action：用户无动作</li><li>safe：用户确认本人操作</li><li>compromised：用户反馈为第三方操作</li></ul>
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def SMSResult(self):
        r"""<p>短信回执结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._SMSResult

    @SMSResult.setter
    def SMSResult(self, SMSResult):
        self._SMSResult = SMSResult

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._SMSId = params.get("SMSId")
        self._ReceivedTime = params.get("ReceivedTime")
        self._Action = params.get("Action")
        if params.get("SMSResult") is not None:
            self._SMSResult = Result()
            self._SMSResult._deserialize(params.get("SMSResult"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanCodeEvent(AbstractModel):
    r"""扫码事件详情

    """

    def __init__(self):
        r"""
        :param _PromotionCode: <p>营销活动码</p>
        :type PromotionCode: :class:`tencentcloud.rce.v20260130.models.PromotionCode`
        :param _PromotionId: <p>营销活动ID</p>
        :type PromotionId: str
        :param _PromotionName: <p>营销活动名称</p>
        :type PromotionName: str
        :param _Description: <p>营销活动描述</p>
        :type Description: str
        :param _InviterUserId: <p>邀请人ID</p>
        :type InviterUserId: str
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组， 示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._PromotionCode = None
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._Cust = None

    @property
    def PromotionCode(self):
        r"""<p>营销活动码</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.PromotionCode`
        """
        return self._PromotionCode

    @PromotionCode.setter
    def PromotionCode(self, PromotionCode):
        self._PromotionCode = PromotionCode

    @property
    def PromotionId(self):
        r"""<p>营销活动ID</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>营销活动名称</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>营销活动描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>邀请人ID</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组， 示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("PromotionCode") is not None:
            self._PromotionCode = PromotionCode()
            self._PromotionCode._deserialize(params.get("PromotionCode"))
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Score(AbstractModel):
    r"""风险分

    """

    def __init__(self):
        r"""
        :param _RiskScore: <p>风险分值，范围[1, 1000]，分值越大，风险越高</p>
        :type RiskScore: int
        :param _RiskLabels: <p>风险标签</p>
        :type RiskLabels: list of RiskLabel
        """
        self._RiskScore = None
        self._RiskLabels = None

    @property
    def RiskScore(self):
        r"""<p>风险分值，范围[1, 1000]，分值越大，风险越高</p>
        :rtype: int
        """
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore

    @property
    def RiskLabels(self):
        r"""<p>风险标签</p>
        :rtype: list of RiskLabel
        """
        return self._RiskLabels

    @RiskLabels.setter
    def RiskLabels(self, RiskLabels):
        self._RiskLabels = RiskLabels


    def _deserialize(self, params):
        self._RiskScore = params.get("RiskScore")
        if params.get("RiskLabels") is not None:
            self._RiskLabels = []
            for item in params.get("RiskLabels"):
                obj = RiskLabel()
                obj._deserialize(item)
                self._RiskLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityVerificationEvent(AbstractModel):
    r"""安全验证事件详情

    """

    def __init__(self):
        r"""
        :param _VerificationEvent: <p>安全验证所处的事件类型</p><p>枚举值：</p><ul><li>register： 注册</li><li>login： 登录</li><li>modify_account： 修改账号</li><li>modify_password： 修改密码</li><li>create_order： 创建订单</li><li>transaction： 交易支付</li><li>modify_order： 修改订单</li><li>withdraw： 提现</li><li>add_promotion： 参加营销活动</li><li>redeem： 兑奖</li></ul>
        :type VerificationEvent: str
        :param _VerificationType: <p>安全验证类型，sms-短信、phone_call-电话、email-邮件、captcha-验证码、shared_knowledge-共享知识、face-人脸、fingerprint-指纹等</p>
        :type VerificationType: str
        :param _VerificationContent: <p>安全验证的内容，例如：用于验证的电话号码、邮件、验证码或者问题，当安全验证类型是sms、phone_call、email、captcha、shared_knowledge时输入</p>
        :type VerificationContent: str
        :param _VerificationResult: <p>安全验证结果</p>
        :type VerificationResult: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._VerificationEvent = None
        self._VerificationType = None
        self._VerificationContent = None
        self._VerificationResult = None
        self._Cust = None

    @property
    def VerificationEvent(self):
        r"""<p>安全验证所处的事件类型</p><p>枚举值：</p><ul><li>register： 注册</li><li>login： 登录</li><li>modify_account： 修改账号</li><li>modify_password： 修改密码</li><li>create_order： 创建订单</li><li>transaction： 交易支付</li><li>modify_order： 修改订单</li><li>withdraw： 提现</li><li>add_promotion： 参加营销活动</li><li>redeem： 兑奖</li></ul>
        :rtype: str
        """
        return self._VerificationEvent

    @VerificationEvent.setter
    def VerificationEvent(self, VerificationEvent):
        self._VerificationEvent = VerificationEvent

    @property
    def VerificationType(self):
        r"""<p>安全验证类型，sms-短信、phone_call-电话、email-邮件、captcha-验证码、shared_knowledge-共享知识、face-人脸、fingerprint-指纹等</p>
        :rtype: str
        """
        return self._VerificationType

    @VerificationType.setter
    def VerificationType(self, VerificationType):
        self._VerificationType = VerificationType

    @property
    def VerificationContent(self):
        r"""<p>安全验证的内容，例如：用于验证的电话号码、邮件、验证码或者问题，当安全验证类型是sms、phone_call、email、captcha、shared_knowledge时输入</p>
        :rtype: str
        """
        return self._VerificationContent

    @VerificationContent.setter
    def VerificationContent(self, VerificationContent):
        self._VerificationContent = VerificationContent

    @property
    def VerificationResult(self):
        r"""<p>安全验证结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._VerificationResult

    @VerificationResult.setter
    def VerificationResult(self, VerificationResult):
        self._VerificationResult = VerificationResult

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._VerificationEvent = params.get("VerificationEvent")
        self._VerificationType = params.get("VerificationType")
        self._VerificationContent = params.get("VerificationContent")
        if params.get("VerificationResult") is not None:
            self._VerificationResult = Result()
            self._VerificationResult._deserialize(params.get("VerificationResult"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskEvent(AbstractModel):
    r"""做任务事件详情

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>营销活动ID</p>
        :type PromotionId: str
        :param _PromotionName: <p>营销活动名称</p>
        :type PromotionName: str
        :param _Description: <p>营销活动描述</p>
        :type Description: str
        :param _InviterUserId: <p>邀请人ID</p>
        :type InviterUserId: str
        :param _TaskId: <p>任务ID</p>
        :type TaskId: str
        :param _TaskName: <p>任务名称</p>
        :type TaskName: str
        :param _TaskType: <p>任务类型，如签到打卡、观看广告、累计步数等</p>
        :type TaskType: str
        :param _TaskCostTime: <p>任务完成耗时</p><p>单位：毫秒</p>
        :type TaskCostTime: int
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._TaskId = None
        self._TaskName = None
        self._TaskType = None
        self._TaskCostTime = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>营销活动ID</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>营销活动名称</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>营销活动描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>邀请人ID</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def TaskId(self):
        r"""<p>任务ID</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""<p>任务名称</p>
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        r"""<p>任务类型，如签到打卡、观看广告、累计步数等</p>
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskCostTime(self):
        r"""<p>任务完成耗时</p><p>单位：毫秒</p>
        :rtype: int
        """
        return self._TaskCostTime

    @TaskCostTime.setter
    def TaskCostTime(self, TaskCostTime):
        self._TaskCostTime = TaskCostTime

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskType = params.get("TaskType")
        self._TaskCostTime = params.get("TaskCostTime")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionEvent(AbstractModel):
    r"""交易事件详情

    """

    def __init__(self):
        r"""
        :param _TransactionId: <p>交易唯一标识</p>
        :type TransactionId: str
        :param _OrderId: <p>您系统中的订单 ID，当一笔交易关联多个订单（合并支付）时请输入所有订单ID</p>
        :type OrderId: list of str
        :param _PaymentAmount: <p>交易金额</p>
        :type PaymentAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _PaymentMethod: <p>支付方式，支持多种支付方式</p>
        :type PaymentMethod: :class:`tencentcloud.rce.v20260130.models.PaymentMethod`
        :param _TransactionType: <p>交易类型</p><p>枚举值：</p><ul><li>sale： 一次性完成授权与扣款（最常见）</li><li>authorize： 仅授权（冻结金额）</li><li>capture： 执行扣款（在授权后）</li><li>void： 取消待处理的授权或扣款</li><li>refund： 退款（部分或全部）</li><li>deposit： 向账户存款</li><li>withdrawal： 从账户提现</li><li>transfer： 账户间转账</li><li>buy： 购买资产（如加密货币）</li><li>sell： 出售资产</li><li>send： 发送资金/资产（如跨钱包转账）</li><li>receive： 接收资金/资产</li></ul><p>默认值：sale</p>
        :type TransactionType: str
        :param _Billing: <p>账单信息</p>
        :type Billing: :class:`tencentcloud.rce.v20260130.models.Billing`
        :param _Delivery: <p>物流信息</p>
        :type Delivery: :class:`tencentcloud.rce.v20260130.models.Delivery`
        :param _Merchant: <p>商家信息</p>
        :type Merchant: :class:`tencentcloud.rce.v20260130.models.Merchant`
        :param _PaymentResult: <p>支付结果</p>
        :type PaymentResult: :class:`tencentcloud.rce.v20260130.models.PaymentResult`
        :param _TransferRecipientUserId: <p>接收方的用户ID，适用于 transfer 交易类型</p>
        :type TransferRecipientUserId: str
        :param _TransferSentAddress: <p>发送方的物理地址，适用于 transfer 交易类型</p>
        :type TransferSentAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _TransferReceivedAddress: <p>接收方的物理地址，适用于 transfer 交易类型</p>
        :type TransferReceivedAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _DigitalOrders: <p>数字订单列表</p>
        :type DigitalOrders: list of DigitalOrder
        :param _ReceiverWallet: <p>接收加密货币的钱包</p>
        :type ReceiverWallet: :class:`tencentcloud.rce.v20260130.models.Wallet`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._TransactionId = None
        self._OrderId = None
        self._PaymentAmount = None
        self._PaymentMethod = None
        self._TransactionType = None
        self._Billing = None
        self._Delivery = None
        self._Merchant = None
        self._PaymentResult = None
        self._TransferRecipientUserId = None
        self._TransferSentAddress = None
        self._TransferReceivedAddress = None
        self._DigitalOrders = None
        self._ReceiverWallet = None
        self._Cust = None

    @property
    def TransactionId(self):
        r"""<p>交易唯一标识</p>
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def OrderId(self):
        r"""<p>您系统中的订单 ID，当一笔交易关联多个订单（合并支付）时请输入所有订单ID</p>
        :rtype: list of str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PaymentAmount(self):
        r"""<p>交易金额</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._PaymentAmount

    @PaymentAmount.setter
    def PaymentAmount(self, PaymentAmount):
        self._PaymentAmount = PaymentAmount

    @property
    def PaymentMethod(self):
        r"""<p>支付方式，支持多种支付方式</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.PaymentMethod`
        """
        return self._PaymentMethod

    @PaymentMethod.setter
    def PaymentMethod(self, PaymentMethod):
        self._PaymentMethod = PaymentMethod

    @property
    def TransactionType(self):
        r"""<p>交易类型</p><p>枚举值：</p><ul><li>sale： 一次性完成授权与扣款（最常见）</li><li>authorize： 仅授权（冻结金额）</li><li>capture： 执行扣款（在授权后）</li><li>void： 取消待处理的授权或扣款</li><li>refund： 退款（部分或全部）</li><li>deposit： 向账户存款</li><li>withdrawal： 从账户提现</li><li>transfer： 账户间转账</li><li>buy： 购买资产（如加密货币）</li><li>sell： 出售资产</li><li>send： 发送资金/资产（如跨钱包转账）</li><li>receive： 接收资金/资产</li></ul><p>默认值：sale</p>
        :rtype: str
        """
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def Billing(self):
        r"""<p>账单信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Billing`
        """
        return self._Billing

    @Billing.setter
    def Billing(self, Billing):
        self._Billing = Billing

    @property
    def Delivery(self):
        r"""<p>物流信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Delivery`
        """
        return self._Delivery

    @Delivery.setter
    def Delivery(self, Delivery):
        self._Delivery = Delivery

    @property
    def Merchant(self):
        r"""<p>商家信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Merchant`
        """
        return self._Merchant

    @Merchant.setter
    def Merchant(self, Merchant):
        self._Merchant = Merchant

    @property
    def PaymentResult(self):
        r"""<p>支付结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.PaymentResult`
        """
        return self._PaymentResult

    @PaymentResult.setter
    def PaymentResult(self, PaymentResult):
        self._PaymentResult = PaymentResult

    @property
    def TransferRecipientUserId(self):
        r"""<p>接收方的用户ID，适用于 transfer 交易类型</p>
        :rtype: str
        """
        return self._TransferRecipientUserId

    @TransferRecipientUserId.setter
    def TransferRecipientUserId(self, TransferRecipientUserId):
        self._TransferRecipientUserId = TransferRecipientUserId

    @property
    def TransferSentAddress(self):
        r"""<p>发送方的物理地址，适用于 transfer 交易类型</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._TransferSentAddress

    @TransferSentAddress.setter
    def TransferSentAddress(self, TransferSentAddress):
        self._TransferSentAddress = TransferSentAddress

    @property
    def TransferReceivedAddress(self):
        r"""<p>接收方的物理地址，适用于 transfer 交易类型</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._TransferReceivedAddress

    @TransferReceivedAddress.setter
    def TransferReceivedAddress(self, TransferReceivedAddress):
        self._TransferReceivedAddress = TransferReceivedAddress

    @property
    def DigitalOrders(self):
        r"""<p>数字订单列表</p>
        :rtype: list of DigitalOrder
        """
        return self._DigitalOrders

    @DigitalOrders.setter
    def DigitalOrders(self, DigitalOrders):
        self._DigitalOrders = DigitalOrders

    @property
    def ReceiverWallet(self):
        r"""<p>接收加密货币的钱包</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Wallet`
        """
        return self._ReceiverWallet

    @ReceiverWallet.setter
    def ReceiverWallet(self, ReceiverWallet):
        self._ReceiverWallet = ReceiverWallet

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._TransactionId = params.get("TransactionId")
        self._OrderId = params.get("OrderId")
        if params.get("PaymentAmount") is not None:
            self._PaymentAmount = Amount()
            self._PaymentAmount._deserialize(params.get("PaymentAmount"))
        if params.get("PaymentMethod") is not None:
            self._PaymentMethod = PaymentMethod()
            self._PaymentMethod._deserialize(params.get("PaymentMethod"))
        self._TransactionType = params.get("TransactionType")
        if params.get("Billing") is not None:
            self._Billing = Billing()
            self._Billing._deserialize(params.get("Billing"))
        if params.get("Delivery") is not None:
            self._Delivery = Delivery()
            self._Delivery._deserialize(params.get("Delivery"))
        if params.get("Merchant") is not None:
            self._Merchant = Merchant()
            self._Merchant._deserialize(params.get("Merchant"))
        if params.get("PaymentResult") is not None:
            self._PaymentResult = PaymentResult()
            self._PaymentResult._deserialize(params.get("PaymentResult"))
        self._TransferRecipientUserId = params.get("TransferRecipientUserId")
        if params.get("TransferSentAddress") is not None:
            self._TransferSentAddress = Address()
            self._TransferSentAddress._deserialize(params.get("TransferSentAddress"))
        if params.get("TransferReceivedAddress") is not None:
            self._TransferReceivedAddress = Address()
            self._TransferReceivedAddress._deserialize(params.get("TransferReceivedAddress"))
        if params.get("DigitalOrders") is not None:
            self._DigitalOrders = []
            for item in params.get("DigitalOrders"):
                obj = DigitalOrder()
                obj._deserialize(item)
                self._DigitalOrders.append(obj)
        if params.get("ReceiverWallet") is not None:
            self._ReceiverWallet = Wallet()
            self._ReceiverWallet._deserialize(params.get("ReceiverWallet"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    r"""账号信息

    """

    def __init__(self):
        r"""
        :param _UserLevel: <p>用户等级</p>
        :type UserLevel: str
        :param _UserPoint: <p>用户积分</p>
        :type UserPoint: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        :param _UserType: <p>用户类型</p>
        :type UserType: str
        """
        self._UserLevel = None
        self._UserPoint = None
        self._UserType = None

    @property
    def UserLevel(self):
        r"""<p>用户等级</p>
        :rtype: str
        """
        return self._UserLevel

    @UserLevel.setter
    def UserLevel(self, UserLevel):
        self._UserLevel = UserLevel

    @property
    def UserPoint(self):
        r"""<p>用户积分</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        """
        return self._UserPoint

    @UserPoint.setter
    def UserPoint(self, UserPoint):
        self._UserPoint = UserPoint

    @property
    def UserType(self):
        r"""<p>用户类型</p>
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType


    def _deserialize(self, params):
        self._UserLevel = params.get("UserLevel")
        if params.get("UserPoint") is not None:
            self._UserPoint = CreditPoint()
            self._UserPoint._deserialize(params.get("UserPoint"))
        self._UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Wallet(AbstractModel):
    r"""数字钱包

    """

    def __init__(self):
        r"""
        :param _WalletType: <p>钱包类型</p><p>枚举值：</p><ul><li>crypto： 加密货币</li><li>digital： 数字货币</li><li>fiat： 法币</li></ul>
        :type WalletType: str
        :param _WalletAddress: <p>钱包地址，通常为钱包的唯一标识</p>
        :type WalletAddress: str
        :param _WalletHolderName: <p>钱包归属人姓名</p>
        :type WalletHolderName: str
        :param _WalletProvider: <p>钱包供应商，wechat、alipay、paypal等</p>
        :type WalletProvider: str
        """
        self._WalletType = None
        self._WalletAddress = None
        self._WalletHolderName = None
        self._WalletProvider = None

    @property
    def WalletType(self):
        r"""<p>钱包类型</p><p>枚举值：</p><ul><li>crypto： 加密货币</li><li>digital： 数字货币</li><li>fiat： 法币</li></ul>
        :rtype: str
        """
        return self._WalletType

    @WalletType.setter
    def WalletType(self, WalletType):
        self._WalletType = WalletType

    @property
    def WalletAddress(self):
        r"""<p>钱包地址，通常为钱包的唯一标识</p>
        :rtype: str
        """
        return self._WalletAddress

    @WalletAddress.setter
    def WalletAddress(self, WalletAddress):
        self._WalletAddress = WalletAddress

    @property
    def WalletHolderName(self):
        r"""<p>钱包归属人姓名</p>
        :rtype: str
        """
        return self._WalletHolderName

    @WalletHolderName.setter
    def WalletHolderName(self, WalletHolderName):
        self._WalletHolderName = WalletHolderName

    @property
    def WalletProvider(self):
        r"""<p>钱包供应商，wechat、alipay、paypal等</p>
        :rtype: str
        """
        return self._WalletProvider

    @WalletProvider.setter
    def WalletProvider(self, WalletProvider):
        self._WalletProvider = WalletProvider


    def _deserialize(self, params):
        self._WalletType = params.get("WalletType")
        self._WalletAddress = params.get("WalletAddress")
        self._WalletHolderName = params.get("WalletHolderName")
        self._WalletProvider = params.get("WalletProvider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawEvent(AbstractModel):
    r"""提现事件详情

    """

    def __init__(self):
        r"""
        :param _Amount: <p>提现金额</p>
        :type Amount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Method: <p>提现方式</p><p>枚举值：</p><ul><li>card： 银行卡</li><li>wallet： 电子钱包</li></ul>
        :type Method: str
        :param _Card: <p>提现银行卡，当提现方式是card时必填</p>
        :type Card: :class:`tencentcloud.rce.v20260130.models.Card`
        :param _Wallet: <p>提现数字钱包，当提现方式是wallet时必填</p>
        :type Wallet: :class:`tencentcloud.rce.v20260130.models.Wallet`
        :param _Result: <p>提现结果</p>
        :type Result: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :type Cust: list of Cust
        """
        self._Amount = None
        self._Method = None
        self._Card = None
        self._Wallet = None
        self._Result = None
        self._Cust = None

    @property
    def Amount(self):
        r"""<p>提现金额</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Method(self):
        r"""<p>提现方式</p><p>枚举值：</p><ul><li>card： 银行卡</li><li>wallet： 电子钱包</li></ul>
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Card(self):
        r"""<p>提现银行卡，当提现方式是card时必填</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Card`
        """
        return self._Card

    @Card.setter
    def Card(self, Card):
        self._Card = Card

    @property
    def Wallet(self):
        r"""<p>提现数字钱包，当提现方式是wallet时必填</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Wallet`
        """
        return self._Wallet

    @Wallet.setter
    def Wallet(self, Wallet):
        self._Wallet = Wallet

    @property
    def Result(self):
        r"""<p>提现结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Cust(self):
        r"""<p>与RCE约定的定制化信息，为K:V 格式的对象数组，示例：[{&quot;Key&quot;: &quot;ApproverName&quot;, &quot;Value&quot;: &quot;bob&quot;},{&quot;Key&quot;:&quot;ApproverPhone&quot;,&quot;Value&quot;: &quot;+86131****5678&quot;}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("Amount") is not None:
            self._Amount = Amount()
            self._Amount._deserialize(params.get("Amount"))
        self._Method = params.get("Method")
        if params.get("Card") is not None:
            self._Card = Card()
            self._Card._deserialize(params.get("Card"))
        if params.get("Wallet") is not None:
            self._Wallet = Wallet()
            self._Wallet._deserialize(params.get("Wallet"))
        if params.get("Result") is not None:
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        