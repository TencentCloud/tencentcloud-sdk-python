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


class AddDelayLiveStreamRequest(AbstractModel):
    """AddDelayLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。
        :type AppName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _DelayTime: 延播时间，单位：秒，上限：600秒。
        :type DelayTime: int
        :param _ExpireTime: 延播设置的过期时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：
1. 默认7天后过期，且最长支持7天内生效。
2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ExpireTime: str
        """
        self._AppName = None
        self._DomainName = None
        self._StreamName = None
        self._DelayTime = None
        self._ExpireTime = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def DelayTime(self):
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamName = params.get("StreamName")
        self._DelayTime = params.get("DelayTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDelayLiveStreamResponse(AbstractModel):
    """AddDelayLiveStream返回参数结构体

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


class AddLiveDomainRequest(AbstractModel):
    """AddLiveDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名名称。
        :type DomainName: str
        :param _DomainType: 域名类型，
0：推流域名，
1：播放域名。
        :type DomainType: int
        :param _PlayType: 拉流域名类型：
1：国内，
2：全球，
3：境外。
默认值：1。
        :type PlayType: int
        :param _IsDelayLive: 是否是慢直播：
0： 普通直播，
1 ：慢直播 。
默认值： 0。
        :type IsDelayLive: int
        :param _IsMiniProgramLive: 是否是小程序直播：
0： 标准直播，
1 ：小程序直播 。
默认值： 0。
        :type IsMiniProgramLive: int
        :param _VerifyOwnerType: 域名归属校验类型。
可取值（与 AuthenticateDomainOwner 接口的 VerifyType 参数一致。）：
dnsCheck ：立即验证配置 dns 的解析记录是否与待验证内容一致，成功则保存记录。
fileCheck ：立即验证 web 文件是否与待验证内容一致，成功则保存记录。
dbCheck :  检查是否已经验证成功过。
若不传默认为 dbCheck 。
        :type VerifyOwnerType: str
        """
        self._DomainName = None
        self._DomainType = None
        self._PlayType = None
        self._IsDelayLive = None
        self._IsMiniProgramLive = None
        self._VerifyOwnerType = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DomainType(self):
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType

    @property
    def PlayType(self):
        return self._PlayType

    @PlayType.setter
    def PlayType(self, PlayType):
        self._PlayType = PlayType

    @property
    def IsDelayLive(self):
        return self._IsDelayLive

    @IsDelayLive.setter
    def IsDelayLive(self, IsDelayLive):
        self._IsDelayLive = IsDelayLive

    @property
    def IsMiniProgramLive(self):
        return self._IsMiniProgramLive

    @IsMiniProgramLive.setter
    def IsMiniProgramLive(self, IsMiniProgramLive):
        self._IsMiniProgramLive = IsMiniProgramLive

    @property
    def VerifyOwnerType(self):
        return self._VerifyOwnerType

    @VerifyOwnerType.setter
    def VerifyOwnerType(self, VerifyOwnerType):
        self._VerifyOwnerType = VerifyOwnerType


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._DomainType = params.get("DomainType")
        self._PlayType = params.get("PlayType")
        self._IsDelayLive = params.get("IsDelayLive")
        self._IsMiniProgramLive = params.get("IsMiniProgramLive")
        self._VerifyOwnerType = params.get("VerifyOwnerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLiveDomainResponse(AbstractModel):
    """AddLiveDomain返回参数结构体

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


class AddLiveWatermarkRequest(AbstractModel):
    """AddLiveWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PictureUrl: 水印图片 URL。
URL中禁止包含的字符：
 ;(){}$>`#"\'|
        :type PictureUrl: str
        :param _WatermarkName: 水印名称。
最长16字节。
        :type WatermarkName: str
        :param _XPosition: 显示位置，X轴偏移，单位是百分比，默认 0。
        :type XPosition: int
        :param _YPosition: 显示位置，Y轴偏移，单位是百分比，默认 0。
        :type YPosition: int
        :param _Width: 水印宽度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始宽度。
        :type Width: int
        :param _Height: 水印高度，占直播原始画面高度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始高度。
        :type Height: int
        :param _BackgroundWidth: 背景水印宽度。默认宽度1920。
        :type BackgroundWidth: int
        :param _BackgroundHeight: 背景水印高度。默认高度1080。
        :type BackgroundHeight: int
        """
        self._PictureUrl = None
        self._WatermarkName = None
        self._XPosition = None
        self._YPosition = None
        self._Width = None
        self._Height = None
        self._BackgroundWidth = None
        self._BackgroundHeight = None

    @property
    def PictureUrl(self):
        return self._PictureUrl

    @PictureUrl.setter
    def PictureUrl(self, PictureUrl):
        self._PictureUrl = PictureUrl

    @property
    def WatermarkName(self):
        return self._WatermarkName

    @WatermarkName.setter
    def WatermarkName(self, WatermarkName):
        self._WatermarkName = WatermarkName

    @property
    def XPosition(self):
        return self._XPosition

    @XPosition.setter
    def XPosition(self, XPosition):
        self._XPosition = XPosition

    @property
    def YPosition(self):
        return self._YPosition

    @YPosition.setter
    def YPosition(self, YPosition):
        self._YPosition = YPosition

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def BackgroundWidth(self):
        return self._BackgroundWidth

    @BackgroundWidth.setter
    def BackgroundWidth(self, BackgroundWidth):
        self._BackgroundWidth = BackgroundWidth

    @property
    def BackgroundHeight(self):
        return self._BackgroundHeight

    @BackgroundHeight.setter
    def BackgroundHeight(self, BackgroundHeight):
        self._BackgroundHeight = BackgroundHeight


    def _deserialize(self, params):
        self._PictureUrl = params.get("PictureUrl")
        self._WatermarkName = params.get("WatermarkName")
        self._XPosition = params.get("XPosition")
        self._YPosition = params.get("YPosition")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._BackgroundWidth = params.get("BackgroundWidth")
        self._BackgroundHeight = params.get("BackgroundHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLiveWatermarkResponse(AbstractModel):
    """AddLiveWatermark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WatermarkId: 水印ID。
        :type WatermarkId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WatermarkId = None
        self._RequestId = None

    @property
    def WatermarkId(self):
        return self._WatermarkId

    @WatermarkId.setter
    def WatermarkId(self, WatermarkId):
        self._WatermarkId = WatermarkId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WatermarkId = params.get("WatermarkId")
        self._RequestId = params.get("RequestId")


class AuthenticateDomainOwnerRequest(AbstractModel):
    """AuthenticateDomainOwner请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 要验证的域名。
        :type DomainName: str
        :param _VerifyType: 验证类型。可取值：
dnsCheck ：立即验证配置 dns 的解析记录是否与待验证内容一致，成功则保存记录。
fileCheck ：立即验证 web 文件是否与待验证内容一致，成功则保存记录。
dbCheck :  检查是否已经验证成功过。
        :type VerifyType: str
        """
        self._DomainName = None
        self._VerifyType = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticateDomainOwnerResponse(AbstractModel):
    """AuthenticateDomainOwner返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 验证内容。
VerifyType 传 dnsCheck 时，为要配的 TXT 记录值。
VerifyType 传 fileCheck 时，为文件内容。
        :type Content: str
        :param _Status: 域名验证状态。
>=0 为已验证归属。
<0 未验证归属权。
        :type Status: int
        :param _MainDomain: DomainName 对应的主域名。
同一主域名下的所有域名只需成功验证一次，后续均无需再验证。
        :type MainDomain: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._Status = None
        self._MainDomain = None
        self._RequestId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MainDomain(self):
        return self._MainDomain

    @MainDomain.setter
    def MainDomain(self, MainDomain):
        self._MainDomain = MainDomain

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Status = params.get("Status")
        self._MainDomain = params.get("MainDomain")
        self._RequestId = params.get("RequestId")


class BandwidthInfo(AbstractModel):
    """带宽信息

    """

    def __init__(self):
        r"""
        :param _Time: 返回格式：
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
根据粒度会有不同程度的缩减。
        :type Time: str
        :param _Bandwidth: 带宽。
        :type Bandwidth: float
        """
        self._Time = None
        self._Bandwidth = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDomainOperateErrors(AbstractModel):
    """批量操作域名相关接口，若其中个别域名操作失败将会跳过，相应的域名错误信息将统一汇总在此类型中

    """

    def __init__(self):
        r"""
        :param _DomainName: 操作失败的域名。
        :type DomainName: str
        :param _Code: API3.0错误码。
        :type Code: str
        :param _Message: API3.0错误信息。
        :type Message: str
        """
        self._DomainName = None
        self._Code = None
        self._Message = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillAreaInfo(AbstractModel):
    """海外分区直播带宽出参，分区信息

    """

    def __init__(self):
        r"""
        :param _Name: 大区名称。
        :type Name: str
        :param _Countrys: 国家或地区明细数据。
        :type Countrys: list of BillCountryInfo
        """
        self._Name = None
        self._Countrys = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Countrys(self):
        return self._Countrys

    @Countrys.setter
    def Countrys(self, Countrys):
        self._Countrys = Countrys


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Countrys") is not None:
            self._Countrys = []
            for item in params.get("Countrys"):
                obj = BillCountryInfo()
                obj._deserialize(item)
                self._Countrys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillCountryInfo(AbstractModel):
    """海外分区直播带宽出参国家带宽信息

    """

    def __init__(self):
        r"""
        :param _Name: 国家名称
        :type Name: str
        :param _BandInfoList: 带宽明细数据信息。
        :type BandInfoList: list of BillDataInfo
        """
        self._Name = None
        self._BandInfoList = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BandInfoList(self):
        return self._BandInfoList

    @BandInfoList.setter
    def BandInfoList(self, BandInfoList):
        self._BandInfoList = BandInfoList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("BandInfoList") is not None:
            self._BandInfoList = []
            for item in params.get("BandInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self._BandInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDataInfo(AbstractModel):
    """带宽和流量信息。

    """

    def __init__(self):
        r"""
        :param _Time: 时间点，
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type Time: str
        :param _Bandwidth: 带宽，单位是 Mbps。
        :type Bandwidth: float
        :param _Flux: 流量，单位是 MB。
        :type Flux: float
        :param _PeakTime: 峰值时间点，
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
原始数据为5分钟粒度，如果查询小时和天粒度数据，则返回对应粒度内的带宽峰值时间点。
        :type PeakTime: str
        """
        self._Time = None
        self._Bandwidth = None
        self._Flux = None
        self._PeakTime = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Flux(self):
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux

    @property
    def PeakTime(self):
        return self._PeakTime

    @PeakTime.setter
    def PeakTime(self, PeakTime):
        self._PeakTime = PeakTime


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Bandwidth = params.get("Bandwidth")
        self._Flux = params.get("Flux")
        self._PeakTime = params.get("PeakTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallBackRuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 规则创建时间。
注：此字段为北京时间（UTC+8时区）。
        :type CreateTime: str
        :param _UpdateTime: 规则更新时间。
注：此字段为北京时间（UTC+8时区）。
        :type UpdateTime: str
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。
        :type AppName: str
        """
        self._CreateTime = None
        self._UpdateTime = None
        self._TemplateId = None
        self._DomainName = None
        self._AppName = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TemplateId = params.get("TemplateId")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallBackTemplateInfo(AbstractModel):
    """回调模板信息。

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _Description: 描述信息。
        :type Description: str
        :param _StreamBeginNotifyUrl: 开播回调 URL。
        :type StreamBeginNotifyUrl: str
        :param _StreamMixNotifyUrl: 混流回调 URL。(参数已弃用)。
        :type StreamMixNotifyUrl: str
        :param _StreamEndNotifyUrl: 断流回调 URL。
        :type StreamEndNotifyUrl: str
        :param _RecordNotifyUrl: 录制回调 URL。
        :type RecordNotifyUrl: str
        :param _SnapshotNotifyUrl: 截图回调 URL。
        :type SnapshotNotifyUrl: str
        :param _PornCensorshipNotifyUrl: 鉴黄回调 URL。
        :type PornCensorshipNotifyUrl: str
        :param _CallbackKey: 回调的鉴权 key。
        :type CallbackKey: str
        :param _PushExceptionNotifyUrl: 推流异常回调 URL。
注意：此字段可能返回 null，表示取不到有效值。
        :type PushExceptionNotifyUrl: str
        :param _AudioAuditNotifyUrl: 音频审核回调 URL。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioAuditNotifyUrl: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._StreamBeginNotifyUrl = None
        self._StreamMixNotifyUrl = None
        self._StreamEndNotifyUrl = None
        self._RecordNotifyUrl = None
        self._SnapshotNotifyUrl = None
        self._PornCensorshipNotifyUrl = None
        self._CallbackKey = None
        self._PushExceptionNotifyUrl = None
        self._AudioAuditNotifyUrl = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StreamBeginNotifyUrl(self):
        return self._StreamBeginNotifyUrl

    @StreamBeginNotifyUrl.setter
    def StreamBeginNotifyUrl(self, StreamBeginNotifyUrl):
        self._StreamBeginNotifyUrl = StreamBeginNotifyUrl

    @property
    def StreamMixNotifyUrl(self):
        return self._StreamMixNotifyUrl

    @StreamMixNotifyUrl.setter
    def StreamMixNotifyUrl(self, StreamMixNotifyUrl):
        self._StreamMixNotifyUrl = StreamMixNotifyUrl

    @property
    def StreamEndNotifyUrl(self):
        return self._StreamEndNotifyUrl

    @StreamEndNotifyUrl.setter
    def StreamEndNotifyUrl(self, StreamEndNotifyUrl):
        self._StreamEndNotifyUrl = StreamEndNotifyUrl

    @property
    def RecordNotifyUrl(self):
        return self._RecordNotifyUrl

    @RecordNotifyUrl.setter
    def RecordNotifyUrl(self, RecordNotifyUrl):
        self._RecordNotifyUrl = RecordNotifyUrl

    @property
    def SnapshotNotifyUrl(self):
        return self._SnapshotNotifyUrl

    @SnapshotNotifyUrl.setter
    def SnapshotNotifyUrl(self, SnapshotNotifyUrl):
        self._SnapshotNotifyUrl = SnapshotNotifyUrl

    @property
    def PornCensorshipNotifyUrl(self):
        return self._PornCensorshipNotifyUrl

    @PornCensorshipNotifyUrl.setter
    def PornCensorshipNotifyUrl(self, PornCensorshipNotifyUrl):
        self._PornCensorshipNotifyUrl = PornCensorshipNotifyUrl

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def PushExceptionNotifyUrl(self):
        return self._PushExceptionNotifyUrl

    @PushExceptionNotifyUrl.setter
    def PushExceptionNotifyUrl(self, PushExceptionNotifyUrl):
        self._PushExceptionNotifyUrl = PushExceptionNotifyUrl

    @property
    def AudioAuditNotifyUrl(self):
        return self._AudioAuditNotifyUrl

    @AudioAuditNotifyUrl.setter
    def AudioAuditNotifyUrl(self, AudioAuditNotifyUrl):
        self._AudioAuditNotifyUrl = AudioAuditNotifyUrl


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self._StreamMixNotifyUrl = params.get("StreamMixNotifyUrl")
        self._StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self._RecordNotifyUrl = params.get("RecordNotifyUrl")
        self._SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self._PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self._CallbackKey = params.get("CallbackKey")
        self._PushExceptionNotifyUrl = params.get("PushExceptionNotifyUrl")
        self._AudioAuditNotifyUrl = params.get("AudioAuditNotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackEventInfo(AbstractModel):
    """回调事件信息

    """

    def __init__(self):
        r"""
        :param _EventTime: 事件时间
        :type EventTime: str
        :param _EventType: 事件类型
        :type EventType: int
        :param _Request: 回调请求
        :type Request: str
        :param _Response: 回调响应
        :type Response: str
        :param _ResponseTime: 客户接口响应时间
        :type ResponseTime: str
        :param _ResultCode: 回调结果
        :type ResultCode: int
        :param _StreamId: 流名称
        :type StreamId: str
        """
        self._EventTime = None
        self._EventType = None
        self._Request = None
        self._Response = None
        self._ResponseTime = None
        self._ResultCode = None
        self._StreamId = None

    @property
    def EventTime(self):
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Request(self):
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def Response(self):
        return self._Response

    @Response.setter
    def Response(self, Response):
        self._Response = Response

    @property
    def ResponseTime(self):
        return self._ResponseTime

    @ResponseTime.setter
    def ResponseTime(self, ResponseTime):
        self._ResponseTime = ResponseTime

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def StreamId(self):
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId


    def _deserialize(self, params):
        self._EventTime = params.get("EventTime")
        self._EventType = params.get("EventType")
        self._Request = params.get("Request")
        self._Response = params.get("Response")
        self._ResponseTime = params.get("ResponseTime")
        self._ResultCode = params.get("ResultCode")
        self._StreamId = params.get("StreamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCommonMixStreamRequest(AbstractModel):
    """CancelCommonMixStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MixStreamSessionId: 混流会话（申请混流开始到取消混流结束）标识 ID。
该值与CreateCommonMixStream中的MixStreamSessionId保持一致。
        :type MixStreamSessionId: str
        """
        self._MixStreamSessionId = None

    @property
    def MixStreamSessionId(self):
        return self._MixStreamSessionId

    @MixStreamSessionId.setter
    def MixStreamSessionId(self, MixStreamSessionId):
        self._MixStreamSessionId = MixStreamSessionId


    def _deserialize(self, params):
        self._MixStreamSessionId = params.get("MixStreamSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCommonMixStreamResponse(AbstractModel):
    """CancelCommonMixStream返回参数结构体

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


class CdnPlayStatData(AbstractModel):
    """下行播放统计指标

    """

    def __init__(self):
        r"""
        :param _Time: 时间点，
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type Time: str
        :param _Bandwidth: 带宽，单位: Mbps。
        :type Bandwidth: float
        :param _Flux: 流量，单位: MB。
        :type Flux: float
        :param _Request: 新增请求数。
        :type Request: int
        :param _Online: 并发连接数。
        :type Online: int
        """
        self._Time = None
        self._Bandwidth = None
        self._Flux = None
        self._Request = None
        self._Online = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Flux(self):
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux

    @property
    def Request(self):
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Bandwidth = params.get("Bandwidth")
        self._Flux = params.get("Flux")
        self._Request = params.get("Request")
        self._Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertInfo(AbstractModel):
    """证书信息。

    """

    def __init__(self):
        r"""
        :param _CertId: 证书 ID。
        :type CertId: int
        :param _CertName: 证书名称。
        :type CertName: str
        :param _Description: 描述信息。
        :type Description: str
        :param _CreateTime: 创建时间，UTC 格式。
注：此字段为北京时间（UTC+8时区）。
        :type CreateTime: str
        :param _HttpsCrt: 证书内容。
        :type HttpsCrt: str
        :param _CertType: 证书类型。
0：用户添加证书，
1：腾讯云托管证书。
        :type CertType: int
        :param _CertExpireTime: 证书过期时间，UTC 格式。
注：此字段为北京时间（UTC+8时区）。
        :type CertExpireTime: str
        :param _DomainList: 使用此证书的域名列表。
        :type DomainList: list of str
        """
        self._CertId = None
        self._CertName = None
        self._Description = None
        self._CreateTime = None
        self._HttpsCrt = None
        self._CertType = None
        self._CertExpireTime = None
        self._DomainList = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def HttpsCrt(self):
        return self._HttpsCrt

    @HttpsCrt.setter
    def HttpsCrt(self, HttpsCrt):
        self._HttpsCrt = HttpsCrt

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def CertExpireTime(self):
        return self._CertExpireTime

    @CertExpireTime.setter
    def CertExpireTime(self, CertExpireTime):
        self._CertExpireTime = CertExpireTime

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._HttpsCrt = params.get("HttpsCrt")
        self._CertType = params.get("CertType")
        self._CertExpireTime = params.get("CertExpireTime")
        self._DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientIpPlaySumInfo(AbstractModel):
    """客户端ip播放汇总信息。

    """

    def __init__(self):
        r"""
        :param _ClientIp: 客户端 IP，点分型。
        :type ClientIp: str
        :param _Province: 客户端所在省份。
        :type Province: str
        :param _TotalFlux: 总流量。
        :type TotalFlux: float
        :param _TotalRequest: 总请求数。
        :type TotalRequest: int
        :param _TotalFailedRequest: 总失败请求数。
        :type TotalFailedRequest: int
        :param _CountryArea: 客户端所在国家。
        :type CountryArea: str
        """
        self._ClientIp = None
        self._Province = None
        self._TotalFlux = None
        self._TotalRequest = None
        self._TotalFailedRequest = None
        self._CountryArea = None

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def TotalFlux(self):
        return self._TotalFlux

    @TotalFlux.setter
    def TotalFlux(self, TotalFlux):
        self._TotalFlux = TotalFlux

    @property
    def TotalRequest(self):
        return self._TotalRequest

    @TotalRequest.setter
    def TotalRequest(self, TotalRequest):
        self._TotalRequest = TotalRequest

    @property
    def TotalFailedRequest(self):
        return self._TotalFailedRequest

    @TotalFailedRequest.setter
    def TotalFailedRequest(self, TotalFailedRequest):
        self._TotalFailedRequest = TotalFailedRequest

    @property
    def CountryArea(self):
        return self._CountryArea

    @CountryArea.setter
    def CountryArea(self, CountryArea):
        self._CountryArea = CountryArea


    def _deserialize(self, params):
        self._ClientIp = params.get("ClientIp")
        self._Province = params.get("Province")
        self._TotalFlux = params.get("TotalFlux")
        self._TotalRequest = params.get("TotalRequest")
        self._TotalFailedRequest = params.get("TotalFailedRequest")
        self._CountryArea = params.get("CountryArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixControlParams(AbstractModel):
    """通用混流控制参数

    """

    def __init__(self):
        r"""
        :param _UseMixCropCenter: 取值范围[0,1]。
填1时，当参数中图层分辨率参数与视频实际分辨率不一致时，自动从视频中按图层设置的分辨率比例进行裁剪。
        :type UseMixCropCenter: int
        :param _AllowCopy: 取值范围[0,1]
填1时，当InputStreamList中个数为1时，且OutputParams.OutputStreamType为1时，不执行取消操作，执行拷贝流操作
        :type AllowCopy: int
        :param _PassInputSei: 取值范围[0,1]
填1时，透传原始流的sei
        :type PassInputSei: int
        """
        self._UseMixCropCenter = None
        self._AllowCopy = None
        self._PassInputSei = None

    @property
    def UseMixCropCenter(self):
        return self._UseMixCropCenter

    @UseMixCropCenter.setter
    def UseMixCropCenter(self, UseMixCropCenter):
        self._UseMixCropCenter = UseMixCropCenter

    @property
    def AllowCopy(self):
        return self._AllowCopy

    @AllowCopy.setter
    def AllowCopy(self, AllowCopy):
        self._AllowCopy = AllowCopy

    @property
    def PassInputSei(self):
        return self._PassInputSei

    @PassInputSei.setter
    def PassInputSei(self, PassInputSei):
        self._PassInputSei = PassInputSei


    def _deserialize(self, params):
        self._UseMixCropCenter = params.get("UseMixCropCenter")
        self._AllowCopy = params.get("AllowCopy")
        self._PassInputSei = params.get("PassInputSei")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixCropParams(AbstractModel):
    """通用混流输入裁剪参数。

    """

    def __init__(self):
        r"""
        :param _CropWidth: 裁剪的宽度。取值范围[0，2000]。
        :type CropWidth: float
        :param _CropHeight: 裁剪的高度。取值范围[0，2000]。
        :type CropHeight: float
        :param _CropStartLocationX: 裁剪的起始X坐标。取值范围[0，2000]。
        :type CropStartLocationX: float
        :param _CropStartLocationY: 裁剪的起始Y坐标。取值范围[0，2000]。
        :type CropStartLocationY: float
        """
        self._CropWidth = None
        self._CropHeight = None
        self._CropStartLocationX = None
        self._CropStartLocationY = None

    @property
    def CropWidth(self):
        return self._CropWidth

    @CropWidth.setter
    def CropWidth(self, CropWidth):
        self._CropWidth = CropWidth

    @property
    def CropHeight(self):
        return self._CropHeight

    @CropHeight.setter
    def CropHeight(self, CropHeight):
        self._CropHeight = CropHeight

    @property
    def CropStartLocationX(self):
        return self._CropStartLocationX

    @CropStartLocationX.setter
    def CropStartLocationX(self, CropStartLocationX):
        self._CropStartLocationX = CropStartLocationX

    @property
    def CropStartLocationY(self):
        return self._CropStartLocationY

    @CropStartLocationY.setter
    def CropStartLocationY(self, CropStartLocationY):
        self._CropStartLocationY = CropStartLocationY


    def _deserialize(self, params):
        self._CropWidth = params.get("CropWidth")
        self._CropHeight = params.get("CropHeight")
        self._CropStartLocationX = params.get("CropStartLocationX")
        self._CropStartLocationY = params.get("CropStartLocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixInputParam(AbstractModel):
    """通用混流输入参数。

    """

    def __init__(self):
        r"""
        :param _InputStreamName: 输入流名称。80字节以内，仅含字母、数字以及下划线的字符串。
当LayoutParams.InputType=0(音视频)/4(纯音频)/5(纯视频)时，该值为需要混流的流名称。
当LayoutParams.InputType=2(图片)/3(画布)时，该值仅用作标识输入，可用类似Canvas1、Pictrue1的名称。
        :type InputStreamName: str
        :param _LayoutParams: 输入流布局参数。
        :type LayoutParams: :class:`tencentcloud.live.v20180801.models.CommonMixLayoutParams`
        :param _CropParams: 输入流裁剪参数。
        :type CropParams: :class:`tencentcloud.live.v20180801.models.CommonMixCropParams`
        """
        self._InputStreamName = None
        self._LayoutParams = None
        self._CropParams = None

    @property
    def InputStreamName(self):
        return self._InputStreamName

    @InputStreamName.setter
    def InputStreamName(self, InputStreamName):
        self._InputStreamName = InputStreamName

    @property
    def LayoutParams(self):
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def CropParams(self):
        return self._CropParams

    @CropParams.setter
    def CropParams(self, CropParams):
        self._CropParams = CropParams


    def _deserialize(self, params):
        self._InputStreamName = params.get("InputStreamName")
        if params.get("LayoutParams") is not None:
            self._LayoutParams = CommonMixLayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("CropParams") is not None:
            self._CropParams = CommonMixCropParams()
            self._CropParams._deserialize(params.get("CropParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixLayoutParams(AbstractModel):
    """通用混流布局参数。

    """

    def __init__(self):
        r"""
        :param _ImageLayer: 输入图层。取值范围[1，16]。
1)背景流（即大主播画面或画布）的 image_layer 填1。
2)纯音频混流，该参数也需填。
注意：不同输入，该值不可重复
        :type ImageLayer: int
        :param _InputType: 输入类型。取值范围[0，5]。
不填默认为0。
0表示输入流为音视频。
2表示输入流为图片。
3表示输入流为画布。 
4表示输入流为音频。
5表示输入流为纯视频。
        :type InputType: int
        :param _ImageHeight: 输入画面在输出时的高度。取值范围：
像素：[0，2000]
百分比：[0.01，0.99]
不填默认为输入流的高度。
使用百分比时，期望输出为（百分比 * 背景高）。
        :type ImageHeight: float
        :param _ImageWidth: 输入画面在输出时的宽度。取值范围：
像素：[0，2000]
百分比：[0.01，0.99]
不填默认为输入流的宽度。
使用百分比时，期望输出为（百分比 * 背景宽）。
        :type ImageWidth: float
        :param _LocationX: 输入在输出画面的X偏移。取值范围：
像素：[0，2000]
百分比：[0.01，0.99]
不填默认为0。
相对于大主播背景画面左上角的横向偏移。 
使用百分比时，期望输出为（百分比 * 背景宽）。
        :type LocationX: float
        :param _LocationY: 输入在输出画面的Y偏移。取值范围：
像素：[0，2000]
百分比：[0.01，0.99]
不填默认为0。
相对于大主播背景画面左上角的纵向偏移。 
使用百分比时，期望输出为（百分比 * 背景宽）
        :type LocationY: float
        :param _Color: 当InputType为3(画布)时，该值表示画布的颜色。
常用的颜色有：
红色：0xcc0033。
黄色：0xcc9900。
绿色：0xcccc33。
蓝色：0x99CCFF。
黑色：0x000000。
白色：0xFFFFFF。
灰色：0x999999。
        :type Color: str
        :param _WatermarkId: 当InputType为2(图片)时，该值是水印ID。
        :type WatermarkId: int
        """
        self._ImageLayer = None
        self._InputType = None
        self._ImageHeight = None
        self._ImageWidth = None
        self._LocationX = None
        self._LocationY = None
        self._Color = None
        self._WatermarkId = None

    @property
    def ImageLayer(self):
        return self._ImageLayer

    @ImageLayer.setter
    def ImageLayer(self, ImageLayer):
        self._ImageLayer = ImageLayer

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def LocationX(self):
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def WatermarkId(self):
        return self._WatermarkId

    @WatermarkId.setter
    def WatermarkId(self, WatermarkId):
        self._WatermarkId = WatermarkId


    def _deserialize(self, params):
        self._ImageLayer = params.get("ImageLayer")
        self._InputType = params.get("InputType")
        self._ImageHeight = params.get("ImageHeight")
        self._ImageWidth = params.get("ImageWidth")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._Color = params.get("Color")
        self._WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixOutputParams(AbstractModel):
    """通用混流输出参数。

    """

    def __init__(self):
        r"""
        :param _OutputStreamName: 输出流名称。
        :type OutputStreamName: str
        :param _OutputStreamType: 输出流类型，取值范围[0,1]。
不填默认为0。
当输出流为输入流 list 中的一条时，填写0。
当期望生成的混流结果成为一条新流时，该值填为1。
该值为1时，output_stream_id 不能出现在 input_stram_list 中，且直播后台中，不能存在相同 ID 的流。
        :type OutputStreamType: int
        :param _OutputStreamBitRate: 输出流比特率。取值范围[1，10000]。
不填的情况下，系统会自动判断。
        :type OutputStreamBitRate: int
        :param _OutputStreamGop: 输出流GOP大小。取值范围[1,10]。
不填的情况下，系统会自动判断。
        :type OutputStreamGop: int
        :param _OutputStreamFrameRate: 输出流帧率大小。取值范围[1,60]。
不填的情况下，系统会自动判断。
        :type OutputStreamFrameRate: int
        :param _OutputAudioBitRate: 输出流音频比特率。取值范围[1,500]
不填的情况下，系统会自动判断。
        :type OutputAudioBitRate: int
        :param _OutputAudioSampleRate: 输出流音频采样率。取值范围[96000, 88200, 64000, 48000, 44100, 32000,24000, 22050, 16000, 12000, 11025, 8000]。
不填的情况下，系统会自动判断。
        :type OutputAudioSampleRate: int
        :param _OutputAudioChannels: 输出流音频声道数。取值范围[1,2]。
不填的情况下，系统会自动判断。
        :type OutputAudioChannels: int
        :param _MixSei: 输出流中的sei信息。如果无特殊需要，不填。
        :type MixSei: str
        """
        self._OutputStreamName = None
        self._OutputStreamType = None
        self._OutputStreamBitRate = None
        self._OutputStreamGop = None
        self._OutputStreamFrameRate = None
        self._OutputAudioBitRate = None
        self._OutputAudioSampleRate = None
        self._OutputAudioChannels = None
        self._MixSei = None

    @property
    def OutputStreamName(self):
        return self._OutputStreamName

    @OutputStreamName.setter
    def OutputStreamName(self, OutputStreamName):
        self._OutputStreamName = OutputStreamName

    @property
    def OutputStreamType(self):
        return self._OutputStreamType

    @OutputStreamType.setter
    def OutputStreamType(self, OutputStreamType):
        self._OutputStreamType = OutputStreamType

    @property
    def OutputStreamBitRate(self):
        return self._OutputStreamBitRate

    @OutputStreamBitRate.setter
    def OutputStreamBitRate(self, OutputStreamBitRate):
        self._OutputStreamBitRate = OutputStreamBitRate

    @property
    def OutputStreamGop(self):
        return self._OutputStreamGop

    @OutputStreamGop.setter
    def OutputStreamGop(self, OutputStreamGop):
        self._OutputStreamGop = OutputStreamGop

    @property
    def OutputStreamFrameRate(self):
        return self._OutputStreamFrameRate

    @OutputStreamFrameRate.setter
    def OutputStreamFrameRate(self, OutputStreamFrameRate):
        self._OutputStreamFrameRate = OutputStreamFrameRate

    @property
    def OutputAudioBitRate(self):
        return self._OutputAudioBitRate

    @OutputAudioBitRate.setter
    def OutputAudioBitRate(self, OutputAudioBitRate):
        self._OutputAudioBitRate = OutputAudioBitRate

    @property
    def OutputAudioSampleRate(self):
        return self._OutputAudioSampleRate

    @OutputAudioSampleRate.setter
    def OutputAudioSampleRate(self, OutputAudioSampleRate):
        self._OutputAudioSampleRate = OutputAudioSampleRate

    @property
    def OutputAudioChannels(self):
        return self._OutputAudioChannels

    @OutputAudioChannels.setter
    def OutputAudioChannels(self, OutputAudioChannels):
        self._OutputAudioChannels = OutputAudioChannels

    @property
    def MixSei(self):
        return self._MixSei

    @MixSei.setter
    def MixSei(self, MixSei):
        self._MixSei = MixSei


    def _deserialize(self, params):
        self._OutputStreamName = params.get("OutputStreamName")
        self._OutputStreamType = params.get("OutputStreamType")
        self._OutputStreamBitRate = params.get("OutputStreamBitRate")
        self._OutputStreamGop = params.get("OutputStreamGop")
        self._OutputStreamFrameRate = params.get("OutputStreamFrameRate")
        self._OutputAudioBitRate = params.get("OutputAudioBitRate")
        self._OutputAudioSampleRate = params.get("OutputAudioSampleRate")
        self._OutputAudioChannels = params.get("OutputAudioChannels")
        self._MixSei = params.get("MixSei")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConcurrentRecordStreamNum(AbstractModel):
    """并发录制路数

    """

    def __init__(self):
        r"""
        :param _Time: 时间点。
        :type Time: str
        :param _Num: 路数。
        :type Num: int
        """
        self._Time = None
        self._Num = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommonMixStreamRequest(AbstractModel):
    """CreateCommonMixStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MixStreamSessionId: 混流会话（申请混流开始到取消混流结束）标识 ID。80字节以内，仅含字母、数字以及下划线的字符串。
        :type MixStreamSessionId: str
        :param _InputStreamList: 混流输入流列表。
        :type InputStreamList: list of CommonMixInputParam
        :param _OutputParams: 混流输出流参数。
        :type OutputParams: :class:`tencentcloud.live.v20180801.models.CommonMixOutputParams`
        :param _MixStreamTemplateId: 输入模板 ID，若设置该参数，将按默认模板布局输出，无需填入自定义位置参数。
不填默认为0。
两输入源支持10，20，30，40，50。
三输入源支持310，390，391。
四输入源支持410。
五输入源支持510，590。
六输入源支持610。
        :type MixStreamTemplateId: int
        :param _ControlParams: 混流的特殊控制参数。如无特殊需求，无需填写。
        :type ControlParams: :class:`tencentcloud.live.v20180801.models.CommonMixControlParams`
        """
        self._MixStreamSessionId = None
        self._InputStreamList = None
        self._OutputParams = None
        self._MixStreamTemplateId = None
        self._ControlParams = None

    @property
    def MixStreamSessionId(self):
        return self._MixStreamSessionId

    @MixStreamSessionId.setter
    def MixStreamSessionId(self, MixStreamSessionId):
        self._MixStreamSessionId = MixStreamSessionId

    @property
    def InputStreamList(self):
        return self._InputStreamList

    @InputStreamList.setter
    def InputStreamList(self, InputStreamList):
        self._InputStreamList = InputStreamList

    @property
    def OutputParams(self):
        return self._OutputParams

    @OutputParams.setter
    def OutputParams(self, OutputParams):
        self._OutputParams = OutputParams

    @property
    def MixStreamTemplateId(self):
        return self._MixStreamTemplateId

    @MixStreamTemplateId.setter
    def MixStreamTemplateId(self, MixStreamTemplateId):
        self._MixStreamTemplateId = MixStreamTemplateId

    @property
    def ControlParams(self):
        return self._ControlParams

    @ControlParams.setter
    def ControlParams(self, ControlParams):
        self._ControlParams = ControlParams


    def _deserialize(self, params):
        self._MixStreamSessionId = params.get("MixStreamSessionId")
        if params.get("InputStreamList") is not None:
            self._InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = CommonMixInputParam()
                obj._deserialize(item)
                self._InputStreamList.append(obj)
        if params.get("OutputParams") is not None:
            self._OutputParams = CommonMixOutputParams()
            self._OutputParams._deserialize(params.get("OutputParams"))
        self._MixStreamTemplateId = params.get("MixStreamTemplateId")
        if params.get("ControlParams") is not None:
            self._ControlParams = CommonMixControlParams()
            self._ControlParams._deserialize(params.get("ControlParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommonMixStreamResponse(AbstractModel):
    """CreateCommonMixStream返回参数结构体

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


class CreateLiveCallbackRuleRequest(AbstractModel):
    """CreateLiveCallbackRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为live。
        :type AppName: str
        :param _TemplateId: 模板ID。
        :type TemplateId: int
        """
        self._DomainName = None
        self._AppName = None
        self._TemplateId = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveCallbackRuleResponse(AbstractModel):
    """CreateLiveCallbackRule返回参数结构体

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


class CreateLiveCallbackTemplateRequest(AbstractModel):
    """CreateLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称。
长度上限：255字节。
仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param _Description: 描述信息。
长度上限：1024字节。
仅支持中文、英文、数字、_、-。
        :type Description: str
        :param _StreamBeginNotifyUrl: 开播回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type StreamBeginNotifyUrl: str
        :param _StreamEndNotifyUrl: 断流回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type StreamEndNotifyUrl: str
        :param _RecordNotifyUrl: 录制回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type RecordNotifyUrl: str
        :param _SnapshotNotifyUrl: 截图回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type SnapshotNotifyUrl: str
        :param _PornCensorshipNotifyUrl: 鉴黄回调 URL ，
相关协议文档：[事件消息通知](/document/product/267/32741)。
        :type PornCensorshipNotifyUrl: str
        :param _CallbackKey: 回调 Key，回调 URL 公用，回调签名详见事件消息通知文档。
[事件消息通知](/document/product/267/32744)。
        :type CallbackKey: str
        :param _StreamMixNotifyUrl: 参数已弃用。
        :type StreamMixNotifyUrl: str
        :param _PushExceptionNotifyUrl: 推流异常回调 URL。
        :type PushExceptionNotifyUrl: str
        :param _AudioAuditNotifyUrl: 音频审核回调 URL。
        :type AudioAuditNotifyUrl: str
        """
        self._TemplateName = None
        self._Description = None
        self._StreamBeginNotifyUrl = None
        self._StreamEndNotifyUrl = None
        self._RecordNotifyUrl = None
        self._SnapshotNotifyUrl = None
        self._PornCensorshipNotifyUrl = None
        self._CallbackKey = None
        self._StreamMixNotifyUrl = None
        self._PushExceptionNotifyUrl = None
        self._AudioAuditNotifyUrl = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StreamBeginNotifyUrl(self):
        return self._StreamBeginNotifyUrl

    @StreamBeginNotifyUrl.setter
    def StreamBeginNotifyUrl(self, StreamBeginNotifyUrl):
        self._StreamBeginNotifyUrl = StreamBeginNotifyUrl

    @property
    def StreamEndNotifyUrl(self):
        return self._StreamEndNotifyUrl

    @StreamEndNotifyUrl.setter
    def StreamEndNotifyUrl(self, StreamEndNotifyUrl):
        self._StreamEndNotifyUrl = StreamEndNotifyUrl

    @property
    def RecordNotifyUrl(self):
        return self._RecordNotifyUrl

    @RecordNotifyUrl.setter
    def RecordNotifyUrl(self, RecordNotifyUrl):
        self._RecordNotifyUrl = RecordNotifyUrl

    @property
    def SnapshotNotifyUrl(self):
        return self._SnapshotNotifyUrl

    @SnapshotNotifyUrl.setter
    def SnapshotNotifyUrl(self, SnapshotNotifyUrl):
        self._SnapshotNotifyUrl = SnapshotNotifyUrl

    @property
    def PornCensorshipNotifyUrl(self):
        return self._PornCensorshipNotifyUrl

    @PornCensorshipNotifyUrl.setter
    def PornCensorshipNotifyUrl(self, PornCensorshipNotifyUrl):
        self._PornCensorshipNotifyUrl = PornCensorshipNotifyUrl

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def StreamMixNotifyUrl(self):
        return self._StreamMixNotifyUrl

    @StreamMixNotifyUrl.setter
    def StreamMixNotifyUrl(self, StreamMixNotifyUrl):
        self._StreamMixNotifyUrl = StreamMixNotifyUrl

    @property
    def PushExceptionNotifyUrl(self):
        return self._PushExceptionNotifyUrl

    @PushExceptionNotifyUrl.setter
    def PushExceptionNotifyUrl(self, PushExceptionNotifyUrl):
        self._PushExceptionNotifyUrl = PushExceptionNotifyUrl

    @property
    def AudioAuditNotifyUrl(self):
        return self._AudioAuditNotifyUrl

    @AudioAuditNotifyUrl.setter
    def AudioAuditNotifyUrl(self, AudioAuditNotifyUrl):
        self._AudioAuditNotifyUrl = AudioAuditNotifyUrl


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self._StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self._RecordNotifyUrl = params.get("RecordNotifyUrl")
        self._SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self._PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self._CallbackKey = params.get("CallbackKey")
        self._StreamMixNotifyUrl = params.get("StreamMixNotifyUrl")
        self._PushExceptionNotifyUrl = params.get("PushExceptionNotifyUrl")
        self._AudioAuditNotifyUrl = params.get("AudioAuditNotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveCallbackTemplateResponse(AbstractModel):
    """CreateLiveCallbackTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID。
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateLivePadRuleRequest(AbstractModel):
    """CreateLivePadRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param _StreamName: 流名称。
注：如果本参数设置为非空字符串，规则将只对此推流起作用。
        :type StreamName: str
        """
        self._DomainName = None
        self._TemplateId = None
        self._AppName = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._TemplateId = params.get("TemplateId")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLivePadRuleResponse(AbstractModel):
    """CreateLivePadRule返回参数结构体

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


class CreateLivePadTemplateRequest(AbstractModel):
    """CreateLivePadTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称。
长度上限：255字节。
仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param _Url: 垫片内容。
        :type Url: str
        :param _Description: 描述信息。
长度上限：1024字节。
仅支持中文、英文、数字、_、-。
        :type Description: str
        :param _WaitDuration: 断流等待时间。
取值范围：0-30000。
单位：ms。
        :type WaitDuration: int
        :param _MaxDuration: 最大垫片时长。
取值范围：0 - 正无穷。
单位：ms。
        :type MaxDuration: int
        :param _Type: 垫片内容类型：
1：图片，2：视频。
默认值：1。
        :type Type: int
        """
        self._TemplateName = None
        self._Url = None
        self._Description = None
        self._WaitDuration = None
        self._MaxDuration = None
        self._Type = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WaitDuration(self):
        return self._WaitDuration

    @WaitDuration.setter
    def WaitDuration(self, WaitDuration):
        self._WaitDuration = WaitDuration

    @property
    def MaxDuration(self):
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._Url = params.get("Url")
        self._Description = params.get("Description")
        self._WaitDuration = params.get("WaitDuration")
        self._MaxDuration = params.get("MaxDuration")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLivePadTemplateResponse(AbstractModel):
    """CreateLivePadTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板Id。
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateLivePullStreamTaskRequest(AbstractModel):
    """CreateLivePullStreamTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceType: 拉流源的类型：
PullLivePushLive -直播，
PullVodPushLive -点播，
PullPicPushLive -图片。
        :type SourceType: str
        :param _SourceUrls: 拉流源 url 列表。
SourceType 为直播（PullLivePushLive）只可以填1个，
SourceType 为点播（PullVodPushLive）可以填多个，上限30个。
当前支持的文件格式：flv，mp4，hls。
当前支持的拉流协议：http，https，rtmp，rtmps，rtsp，srt。
注意：
1. 建议优先使用 flv 文件，对于 mp4 未交织好的文件轮播推流易产生卡顿，可通过点播转码进行重新交织后再轮播。
2. 拒绝内网域名等攻击性拉流地址，如有使用，则做账号封禁处理。
3. 源文件请保持时间戳正常交织递增，避免因源文件异常影响推流及播放。
4. 视频编码格式仅支持: H264, H265。
5. 音频编码格式仅支持: AAC。
6. 点播源请使用小文件，尽量时长保持在1小时内，较大文件打开和续播耗时较久，耗时超过15秒会有无法正常转推风险。
        :type SourceUrls: list of str
        :param _DomainName: 推流域名。
将拉取过来的流推到该域名。
注意：如果目标地址为非云直播，且样式不同于云直播，请使用 ToUrl 传入完整推流地址，详细用法请参考 ToUrl 参数说明。
        :type DomainName: str
        :param _AppName: 推流路径。
将拉取过来的流推到该路径。
        :type AppName: str
        :param _StreamName: 推流名称。
将拉取过来的流推到该流名称。
        :type StreamName: str
        :param _StartTime: 开始时间。
使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时。
        :type StartTime: str
        :param _EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时。
        :type EndTime: str
        :param _Operator: 任务操作人备注。
        :type Operator: str
        :param _PushArgs: 推流参数。
推流时携带自定义参数。
示例：
bak=1&test=2 。
        :type PushArgs: str
        :param _CallbackEvents: 选择需要回调的事件（不填则回调全部）：
TaskStart：任务启动回调，
TaskExit：任务停止回调，
VodSourceFileStart：从点播源文件开始拉流回调，
VodSourceFileFinish：从点播源文件拉流结束回调，
ResetTaskConfig：任务更新回调。

TaskAlarm: 用于告警事件通知，AlarmType 示例:
PullFileUnstable - 文件拉取不稳定，
PushStreamUnstable - 推流不稳定，
PullFileFailed - 文件拉取出错，
PushStreamFailed - 推流出现失败，
FileEndEarly - 文件提前结束。
        :type CallbackEvents: list of str
        :param _VodLoopTimes: 点播拉流转推循环次数。默认：-1。
-1：无限循环，直到任务结束。
0：不循环。
>0：具体循环次数。次数和时间以先结束的为准。
注意：该配置仅对拉流源为点播时生效。
        :type VodLoopTimes: str
        :param _VodRefreshType: 点播更新SourceUrls后的播放方式：
ImmediateNewSource：立即播放新的拉流源内容；
ContinueBreakPoint：播放完当前正在播放的点播 url 后再使用新的拉流源播放。（旧拉流源未播放的点播 url 不会再播放）

注意：该配置生效仅对变更前拉流源为点播时生效。
        :type VodRefreshType: str
        :param _CallbackUrl: 自定义回调地址。
拉流转推任务相关事件会回调到该地址。
        :type CallbackUrl: str
        :param _ExtraCmd: 其他参数。
示例: ignore_region  用于忽略传入地域, 内部按负载分配。
        :type ExtraCmd: str
        :param _Comment: 任务描述，限制 512 字节。
        :type Comment: str
        :param _ToUrl: 完整目标 URL 地址。
用法注意：如果使用该参数来传完整目标地址，则 DomainName, AppName, StreamName 需要传入空字符串，任务将会使用该 ToUrl 参数指定的目标地址。

使用该方式传入目标地址支持的协议有：
rtmp、rtmps、rtsp、rtp、srt。

注意：签名时间需要超过任务结束时间，避免因签名过期造成任务失败。
        :type ToUrl: str
        :param _BackupSourceType: 备源的类型：
PullLivePushLive -直播，
PullVodPushLive -点播。
注意：
1. 仅当主源类型为直播源时，备源才会生效。
2. 主直播源拉流中断时，自动使用备源进行拉流。
3. 如果备源为点播文件时，则每次轮播完点播文件就检查主源是否恢复，如果主源恢复则自动切回到主源，否则继续拉备源。
        :type BackupSourceType: str
        :param _BackupSourceUrl: 备源 URL。
只允许填一个备源 URL
        :type BackupSourceUrl: str
        :param _WatermarkList: 水印信息列表。
注意：
1. 最多支持4个不同位置的水印。
2. 水印图片 URL 请使用合法外网可访问地址。
3. 支持的水印图片格式：png，jpg，gif 等。
        :type WatermarkList: list of PullPushWatermarkInfo
        :param _VodLocalMode: 点播源是否启用本地推流模式，默认0，不启用。
0 - 不启用。
1 - 启用。
注意：启用本地模式后，会将源列表中的 MP4 文件进行本地下载，优先使用本地已下载文件进行推流，提高点播源推流稳定性。使用本地下载文件推流时，会产生增值费用。
        :type VodLocalMode: int
        :param _RecordTemplateId: 录制模板 ID。
        :type RecordTemplateId: str
        """
        self._SourceType = None
        self._SourceUrls = None
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._StartTime = None
        self._EndTime = None
        self._Operator = None
        self._PushArgs = None
        self._CallbackEvents = None
        self._VodLoopTimes = None
        self._VodRefreshType = None
        self._CallbackUrl = None
        self._ExtraCmd = None
        self._Comment = None
        self._ToUrl = None
        self._BackupSourceType = None
        self._BackupSourceUrl = None
        self._WatermarkList = None
        self._VodLocalMode = None
        self._RecordTemplateId = None

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceUrls(self):
        return self._SourceUrls

    @SourceUrls.setter
    def SourceUrls(self, SourceUrls):
        self._SourceUrls = SourceUrls

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def PushArgs(self):
        return self._PushArgs

    @PushArgs.setter
    def PushArgs(self, PushArgs):
        self._PushArgs = PushArgs

    @property
    def CallbackEvents(self):
        return self._CallbackEvents

    @CallbackEvents.setter
    def CallbackEvents(self, CallbackEvents):
        self._CallbackEvents = CallbackEvents

    @property
    def VodLoopTimes(self):
        return self._VodLoopTimes

    @VodLoopTimes.setter
    def VodLoopTimes(self, VodLoopTimes):
        self._VodLoopTimes = VodLoopTimes

    @property
    def VodRefreshType(self):
        return self._VodRefreshType

    @VodRefreshType.setter
    def VodRefreshType(self, VodRefreshType):
        self._VodRefreshType = VodRefreshType

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def ExtraCmd(self):
        return self._ExtraCmd

    @ExtraCmd.setter
    def ExtraCmd(self, ExtraCmd):
        self._ExtraCmd = ExtraCmd

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def ToUrl(self):
        return self._ToUrl

    @ToUrl.setter
    def ToUrl(self, ToUrl):
        self._ToUrl = ToUrl

    @property
    def BackupSourceType(self):
        return self._BackupSourceType

    @BackupSourceType.setter
    def BackupSourceType(self, BackupSourceType):
        self._BackupSourceType = BackupSourceType

    @property
    def BackupSourceUrl(self):
        return self._BackupSourceUrl

    @BackupSourceUrl.setter
    def BackupSourceUrl(self, BackupSourceUrl):
        self._BackupSourceUrl = BackupSourceUrl

    @property
    def WatermarkList(self):
        return self._WatermarkList

    @WatermarkList.setter
    def WatermarkList(self, WatermarkList):
        self._WatermarkList = WatermarkList

    @property
    def VodLocalMode(self):
        return self._VodLocalMode

    @VodLocalMode.setter
    def VodLocalMode(self, VodLocalMode):
        self._VodLocalMode = VodLocalMode

    @property
    def RecordTemplateId(self):
        return self._RecordTemplateId

    @RecordTemplateId.setter
    def RecordTemplateId(self, RecordTemplateId):
        self._RecordTemplateId = RecordTemplateId


    def _deserialize(self, params):
        self._SourceType = params.get("SourceType")
        self._SourceUrls = params.get("SourceUrls")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Operator = params.get("Operator")
        self._PushArgs = params.get("PushArgs")
        self._CallbackEvents = params.get("CallbackEvents")
        self._VodLoopTimes = params.get("VodLoopTimes")
        self._VodRefreshType = params.get("VodRefreshType")
        self._CallbackUrl = params.get("CallbackUrl")
        self._ExtraCmd = params.get("ExtraCmd")
        self._Comment = params.get("Comment")
        self._ToUrl = params.get("ToUrl")
        self._BackupSourceType = params.get("BackupSourceType")
        self._BackupSourceUrl = params.get("BackupSourceUrl")
        if params.get("WatermarkList") is not None:
            self._WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = PullPushWatermarkInfo()
                obj._deserialize(item)
                self._WatermarkList.append(obj)
        self._VodLocalMode = params.get("VodLocalMode")
        self._RecordTemplateId = params.get("RecordTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLivePullStreamTaskResponse(AbstractModel):
    """CreateLivePullStreamTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id 。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateLiveRecordRequest(AbstractModel):
    """CreateLiveRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _AppName: 推流路径，与推流和播放地址中的 AppName保持一致，默认为 live。
        :type AppName: str
        :param _DomainName: 推流域名。多域名推流必须设置。
        :type DomainName: str
        :param _StartTime: 录制开始时间。中国标准时间，需要 URLEncode(rfc3986)。如 2017-01-01 10:10:01，编码为：2017-01-01+10%3a10%3a01。
定时录制模式，必须设置该字段；实时视频录制模式，忽略该字段。
        :type StartTime: str
        :param _EndTime: 录制结束时间。中国标准时间，需要 URLEncode(rfc3986)。如 2017-01-01 10:30:01，编码为：2017-01-01+10%3a30%3a01。
定时录制模式，必须设置该字段；实时录制模式，为可选字段。如果通过Highlight参数，设置录制为实时视频录制模式，其设置的结束时间不应超过当前时间+30分钟，如果设置的结束时间超过当前时间+30分钟或者小于当前时间或者不设置该参数，则实际结束时间为当前时间+30分钟。
        :type EndTime: str
        :param _RecordType: 录制类型。
“video” : 音视频录制【默认】。
“audio” : 纯音频录制。
在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。
        :type RecordType: str
        :param _FileFormat: 录制文件格式。其值为：
“flv”【默认】,“hls”,”mp4”,“aac”,”mp3”。
在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。
        :type FileFormat: str
        :param _Highlight: 开启实时视频录制模式标志。
0：不开启实时视频录制模式，即定时录制模式【默认】。见[示例一](#.E7.A4.BA.E4.BE.8B1-.E5.88.9B.E5.BB.BA.E5.AE.9A.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)。
1：开启实时视频录制模式。见[示例二](#.E7.A4.BA.E4.BE.8B2-.E5.88.9B.E5.BB.BA.E5.AE.9E.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)。
        :type Highlight: int
        :param _MixStream: 开启 A+B=C混流C流录制标志。
0：不开启 A+B=C混流C流录制【默认】。
1：开启 A+B=C混流C流录制。
在定时录制模式或实时视频录制模式下，该参数均有效。
        :type MixStream: int
        :param _StreamParam: 录制流参数。当前支持以下参数：
record_interval - 录制分片时长，单位 秒，1800 - 7200。
storage_time - 录制文件存储时长，单位 秒。
eg. record_interval=3600&storage_time=2592000。
注：参数需要url encode。
在定时录制模式或实时视频录制模式下，该参数均有效。
        :type StreamParam: str
        """
        self._StreamName = None
        self._AppName = None
        self._DomainName = None
        self._StartTime = None
        self._EndTime = None
        self._RecordType = None
        self._FileFormat = None
        self._Highlight = None
        self._MixStream = None
        self._StreamParam = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def FileFormat(self):
        return self._FileFormat

    @FileFormat.setter
    def FileFormat(self, FileFormat):
        self._FileFormat = FileFormat

    @property
    def Highlight(self):
        return self._Highlight

    @Highlight.setter
    def Highlight(self, Highlight):
        self._Highlight = Highlight

    @property
    def MixStream(self):
        return self._MixStream

    @MixStream.setter
    def MixStream(self, MixStream):
        self._MixStream = MixStream

    @property
    def StreamParam(self):
        return self._StreamParam

    @StreamParam.setter
    def StreamParam(self, StreamParam):
        self._StreamParam = StreamParam


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RecordType = params.get("RecordType")
        self._FileFormat = params.get("FileFormat")
        self._Highlight = params.get("Highlight")
        self._MixStream = params.get("MixStream")
        self._StreamParam = params.get("StreamParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveRecordResponse(AbstractModel):
    """CreateLiveRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID，全局唯一标识录制任务。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateLiveRecordRuleRequest(AbstractModel):
    """CreateLiveRecordRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param _StreamName: 流名称。
注：如果本参数设置为非空字符串，规则将只对此推流起作用。
        :type StreamName: str
        """
        self._DomainName = None
        self._TemplateId = None
        self._AppName = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._TemplateId = params.get("TemplateId")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveRecordRuleResponse(AbstractModel):
    """CreateLiveRecordRule返回参数结构体

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


class CreateLiveRecordTemplateRequest(AbstractModel):
    """CreateLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名。仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param _Description: 描述信息。
        :type Description: str
        :param _FlvParam: Flv录制参数，开启Flv录制时设置。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _HlsParam: Hls录制参数，开启hls录制时设置。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _Mp4Param: Mp4录制参数，开启Mp4录制时设置。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _AacParam: Aac录制参数，开启Aac录制时设置。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _IsDelayLive: 直播类型，默认 0。
0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param _HlsSpecialParam: HLS专属录制参数。
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param _Mp3Param: Mp3录制参数，开启Mp3录制时设置。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _RemoveWatermark: 是否去除水印，类型为慢直播时此参数无效。
        :type RemoveWatermark: bool
        :param _FlvSpecialParam: FLV 录制特殊参数。
        :type FlvSpecialParam: :class:`tencentcloud.live.v20180801.models.FlvSpecialParam`
        """
        self._TemplateName = None
        self._Description = None
        self._FlvParam = None
        self._HlsParam = None
        self._Mp4Param = None
        self._AacParam = None
        self._IsDelayLive = None
        self._HlsSpecialParam = None
        self._Mp3Param = None
        self._RemoveWatermark = None
        self._FlvSpecialParam = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def FlvParam(self):
        return self._FlvParam

    @FlvParam.setter
    def FlvParam(self, FlvParam):
        self._FlvParam = FlvParam

    @property
    def HlsParam(self):
        return self._HlsParam

    @HlsParam.setter
    def HlsParam(self, HlsParam):
        self._HlsParam = HlsParam

    @property
    def Mp4Param(self):
        return self._Mp4Param

    @Mp4Param.setter
    def Mp4Param(self, Mp4Param):
        self._Mp4Param = Mp4Param

    @property
    def AacParam(self):
        return self._AacParam

    @AacParam.setter
    def AacParam(self, AacParam):
        self._AacParam = AacParam

    @property
    def IsDelayLive(self):
        return self._IsDelayLive

    @IsDelayLive.setter
    def IsDelayLive(self, IsDelayLive):
        self._IsDelayLive = IsDelayLive

    @property
    def HlsSpecialParam(self):
        return self._HlsSpecialParam

    @HlsSpecialParam.setter
    def HlsSpecialParam(self, HlsSpecialParam):
        self._HlsSpecialParam = HlsSpecialParam

    @property
    def Mp3Param(self):
        return self._Mp3Param

    @Mp3Param.setter
    def Mp3Param(self, Mp3Param):
        self._Mp3Param = Mp3Param

    @property
    def RemoveWatermark(self):
        return self._RemoveWatermark

    @RemoveWatermark.setter
    def RemoveWatermark(self, RemoveWatermark):
        self._RemoveWatermark = RemoveWatermark

    @property
    def FlvSpecialParam(self):
        return self._FlvSpecialParam

    @FlvSpecialParam.setter
    def FlvSpecialParam(self, FlvSpecialParam):
        self._FlvSpecialParam = FlvSpecialParam


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self._FlvParam = RecordParam()
            self._FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self._HlsParam = RecordParam()
            self._HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self._Mp4Param = RecordParam()
            self._Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self._AacParam = RecordParam()
            self._AacParam._deserialize(params.get("AacParam"))
        self._IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self._HlsSpecialParam = HlsSpecialParam()
            self._HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self._Mp3Param = RecordParam()
            self._Mp3Param._deserialize(params.get("Mp3Param"))
        self._RemoveWatermark = params.get("RemoveWatermark")
        if params.get("FlvSpecialParam") is not None:
            self._FlvSpecialParam = FlvSpecialParam()
            self._FlvSpecialParam._deserialize(params.get("FlvSpecialParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveRecordTemplateResponse(AbstractModel):
    """CreateLiveRecordTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板Id。
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateLiveSnapshotRuleRequest(AbstractModel):
    """CreateLiveSnapshotRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。
        :type AppName: str
        :param _StreamName: 流名称。
注：如果本参数设置为非空字符串，规则将只对此推流起作用。
        :type StreamName: str
        """
        self._DomainName = None
        self._TemplateId = None
        self._AppName = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._TemplateId = params.get("TemplateId")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveSnapshotRuleResponse(AbstractModel):
    """CreateLiveSnapshotRule返回参数结构体

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


class CreateLiveSnapshotTemplateRequest(AbstractModel):
    """CreateLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称。
长度上限：255字节。
仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param _CosAppId: Cos 应用 ID。
        :type CosAppId: int
        :param _CosBucket: Cos Bucket名称。
注：CosBucket参数值不能包含-[appid] 部分。
        :type CosBucket: str
        :param _CosRegion: Cos地区。
        :type CosRegion: str
        :param _Description: 描述信息。
长度上限：1024字节。
仅支持中文、英文、数字、_、-。
        :type Description: str
        :param _SnapshotInterval: 截图间隔，单位s，默认10s。
范围： 2s ~ 300s。
        :type SnapshotInterval: int
        :param _Width: 截图宽度。默认：0（原始宽）。
范围：0-3000 。
        :type Width: int
        :param _Height: 截图高度。默认：0（原始高）。
范围：0-2000 。
        :type Height: int
        :param _PornFlag: 是否开启鉴黄，0：不开启，1：开启。默认：0。
        :type PornFlag: int
        :param _CosPrefix: Cos Bucket文件夹前缀。
如不传，实际按默认值
/{Year}-{Month}-{Day}
生效
        :type CosPrefix: str
        :param _CosFileName: Cos 文件名称。
如不传，实际按默认值
{StreamID}-screenshot-{Hour}-{Minute}-{Second}-{Width}x{Height}{Ext}
生效
        :type CosFileName: str
        """
        self._TemplateName = None
        self._CosAppId = None
        self._CosBucket = None
        self._CosRegion = None
        self._Description = None
        self._SnapshotInterval = None
        self._Width = None
        self._Height = None
        self._PornFlag = None
        self._CosPrefix = None
        self._CosFileName = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def CosAppId(self):
        return self._CosAppId

    @CosAppId.setter
    def CosAppId(self, CosAppId):
        self._CosAppId = CosAppId

    @property
    def CosBucket(self):
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SnapshotInterval(self):
        return self._SnapshotInterval

    @SnapshotInterval.setter
    def SnapshotInterval(self, SnapshotInterval):
        self._SnapshotInterval = SnapshotInterval

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def PornFlag(self):
        return self._PornFlag

    @PornFlag.setter
    def PornFlag(self, PornFlag):
        self._PornFlag = PornFlag

    @property
    def CosPrefix(self):
        return self._CosPrefix

    @CosPrefix.setter
    def CosPrefix(self, CosPrefix):
        self._CosPrefix = CosPrefix

    @property
    def CosFileName(self):
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._CosAppId = params.get("CosAppId")
        self._CosBucket = params.get("CosBucket")
        self._CosRegion = params.get("CosRegion")
        self._Description = params.get("Description")
        self._SnapshotInterval = params.get("SnapshotInterval")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._PornFlag = params.get("PornFlag")
        self._CosPrefix = params.get("CosPrefix")
        self._CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveSnapshotTemplateResponse(AbstractModel):
    """CreateLiveSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板Id。
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateLiveStreamMonitorRequest(AbstractModel):
    """CreateLiveStreamMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OutputInfo: 监播任务的输出信息。
        :type OutputInfo: :class:`tencentcloud.live.v20180801.models.LiveStreamMonitorOutputInfo`
        :param _InputList: 待监播的输入流信息列表。
        :type InputList: list of LiveStreamMonitorInputInfo
        :param _MonitorName: 监播任务名称。字段长度小于128字节（一个汉字两个字节）。
        :type MonitorName: str
        :param _NotifyPolicy: 监播事件通知策略。
不填默认为没有任何通知。
        :type NotifyPolicy: :class:`tencentcloud.live.v20180801.models.LiveStreamMonitorNotifyPolicy`
        :param _AsrLanguage: 智能语音识别语种设置：
0 关闭 1 中文 2 英文 3 日文 4 韩文。
        :type AsrLanguage: int
        :param _OcrLanguage: 智能文字识别语种设置：
0 关闭 1 中、英文。
        :type OcrLanguage: int
        :param _AiAsrInputIndexList: 智能语音识别的输入列表，若开启语音识别则必填。
（第1条输入流index为1）
        :type AiAsrInputIndexList: list of int non-negative
        :param _AiOcrInputIndexList: 智能文字识别的输入列表，若开启文字识别则必填。
（第1条输入流index为1）
        :type AiOcrInputIndexList: list of int non-negative
        :param _CheckStreamBroken: 是否开启断流检测。
        :type CheckStreamBroken: int
        :param _CheckStreamLowFrameRate: 是否开启低帧率检测。
        :type CheckStreamLowFrameRate: int
        :param _AllowMonitorReport: 是否存储监播事件到监播报告，以及是否允许查询监播报告。
        :type AllowMonitorReport: int
        :param _AiFormatDiagnose: 是否开启格式诊断。
        :type AiFormatDiagnose: int
        """
        self._OutputInfo = None
        self._InputList = None
        self._MonitorName = None
        self._NotifyPolicy = None
        self._AsrLanguage = None
        self._OcrLanguage = None
        self._AiAsrInputIndexList = None
        self._AiOcrInputIndexList = None
        self._CheckStreamBroken = None
        self._CheckStreamLowFrameRate = None
        self._AllowMonitorReport = None
        self._AiFormatDiagnose = None

    @property
    def OutputInfo(self):
        return self._OutputInfo

    @OutputInfo.setter
    def OutputInfo(self, OutputInfo):
        self._OutputInfo = OutputInfo

    @property
    def InputList(self):
        return self._InputList

    @InputList.setter
    def InputList(self, InputList):
        self._InputList = InputList

    @property
    def MonitorName(self):
        return self._MonitorName

    @MonitorName.setter
    def MonitorName(self, MonitorName):
        self._MonitorName = MonitorName

    @property
    def NotifyPolicy(self):
        return self._NotifyPolicy

    @NotifyPolicy.setter
    def NotifyPolicy(self, NotifyPolicy):
        self._NotifyPolicy = NotifyPolicy

    @property
    def AsrLanguage(self):
        return self._AsrLanguage

    @AsrLanguage.setter
    def AsrLanguage(self, AsrLanguage):
        self._AsrLanguage = AsrLanguage

    @property
    def OcrLanguage(self):
        return self._OcrLanguage

    @OcrLanguage.setter
    def OcrLanguage(self, OcrLanguage):
        self._OcrLanguage = OcrLanguage

    @property
    def AiAsrInputIndexList(self):
        return self._AiAsrInputIndexList

    @AiAsrInputIndexList.setter
    def AiAsrInputIndexList(self, AiAsrInputIndexList):
        self._AiAsrInputIndexList = AiAsrInputIndexList

    @property
    def AiOcrInputIndexList(self):
        return self._AiOcrInputIndexList

    @AiOcrInputIndexList.setter
    def AiOcrInputIndexList(self, AiOcrInputIndexList):
        self._AiOcrInputIndexList = AiOcrInputIndexList

    @property
    def CheckStreamBroken(self):
        return self._CheckStreamBroken

    @CheckStreamBroken.setter
    def CheckStreamBroken(self, CheckStreamBroken):
        self._CheckStreamBroken = CheckStreamBroken

    @property
    def CheckStreamLowFrameRate(self):
        return self._CheckStreamLowFrameRate

    @CheckStreamLowFrameRate.setter
    def CheckStreamLowFrameRate(self, CheckStreamLowFrameRate):
        self._CheckStreamLowFrameRate = CheckStreamLowFrameRate

    @property
    def AllowMonitorReport(self):
        return self._AllowMonitorReport

    @AllowMonitorReport.setter
    def AllowMonitorReport(self, AllowMonitorReport):
        self._AllowMonitorReport = AllowMonitorReport

    @property
    def AiFormatDiagnose(self):
        return self._AiFormatDiagnose

    @AiFormatDiagnose.setter
    def AiFormatDiagnose(self, AiFormatDiagnose):
        self._AiFormatDiagnose = AiFormatDiagnose


    def _deserialize(self, params):
        if params.get("OutputInfo") is not None:
            self._OutputInfo = LiveStreamMonitorOutputInfo()
            self._OutputInfo._deserialize(params.get("OutputInfo"))
        if params.get("InputList") is not None:
            self._InputList = []
            for item in params.get("InputList"):
                obj = LiveStreamMonitorInputInfo()
                obj._deserialize(item)
                self._InputList.append(obj)
        self._MonitorName = params.get("MonitorName")
        if params.get("NotifyPolicy") is not None:
            self._NotifyPolicy = LiveStreamMonitorNotifyPolicy()
            self._NotifyPolicy._deserialize(params.get("NotifyPolicy"))
        self._AsrLanguage = params.get("AsrLanguage")
        self._OcrLanguage = params.get("OcrLanguage")
        self._AiAsrInputIndexList = params.get("AiAsrInputIndexList")
        self._AiOcrInputIndexList = params.get("AiOcrInputIndexList")
        self._CheckStreamBroken = params.get("CheckStreamBroken")
        self._CheckStreamLowFrameRate = params.get("CheckStreamLowFrameRate")
        self._AllowMonitorReport = params.get("AllowMonitorReport")
        self._AiFormatDiagnose = params.get("AiFormatDiagnose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveStreamMonitorResponse(AbstractModel):
    """CreateLiveStreamMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监播任务ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorId = None
        self._RequestId = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._RequestId = params.get("RequestId")


class CreateLiveTimeShiftRuleRequest(AbstractModel):
    """CreateLiveTimeShiftRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param _StreamName: 流名称。
注：如果本参数设置为非空字符串，规则将只对此推流起作用。
        :type StreamName: str
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._TemplateId = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveTimeShiftRuleResponse(AbstractModel):
    """CreateLiveTimeShiftRule返回参数结构体

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


class CreateLiveTimeShiftTemplateRequest(AbstractModel):
    """CreateLiveTimeShiftTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称。
长度上限：255字节。
仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param _Duration: 时移时长。
单位：s。
        :type Duration: int
        :param _Description: 描述信息。
仅支持中文、英文、数字、_、-。
        :type Description: str
        :param _Area: 地域。
Mainland：中国大陆。
Overseas：海外及港澳台地区。
默认值：Mainland。
        :type Area: str
        :param _ItemDuration: 分片时长。
可取3-10。
单位：s。
默认值：5。
        :type ItemDuration: int
        :param _RemoveWatermark: 是否去除水印。
传true则将录制原始流。
默认值：false。
        :type RemoveWatermark: bool
        :param _TranscodeTemplateIds: 转码流id列表。
此参数仅在 RemoveWatermark为false时生效。
        :type TranscodeTemplateIds: list of int
        """
        self._TemplateName = None
        self._Duration = None
        self._Description = None
        self._Area = None
        self._ItemDuration = None
        self._RemoveWatermark = None
        self._TranscodeTemplateIds = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ItemDuration(self):
        return self._ItemDuration

    @ItemDuration.setter
    def ItemDuration(self, ItemDuration):
        self._ItemDuration = ItemDuration

    @property
    def RemoveWatermark(self):
        return self._RemoveWatermark

    @RemoveWatermark.setter
    def RemoveWatermark(self, RemoveWatermark):
        self._RemoveWatermark = RemoveWatermark

    @property
    def TranscodeTemplateIds(self):
        return self._TranscodeTemplateIds

    @TranscodeTemplateIds.setter
    def TranscodeTemplateIds(self, TranscodeTemplateIds):
        self._TranscodeTemplateIds = TranscodeTemplateIds


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._Duration = params.get("Duration")
        self._Description = params.get("Description")
        self._Area = params.get("Area")
        self._ItemDuration = params.get("ItemDuration")
        self._RemoveWatermark = params.get("RemoveWatermark")
        self._TranscodeTemplateIds = params.get("TranscodeTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveTimeShiftTemplateResponse(AbstractModel):
    """CreateLiveTimeShiftTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板Id。
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateLiveTranscodeRuleRequest(AbstractModel):
    """CreateLiveTranscodeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 播放域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致。如果只绑定域名，则此处填""。
        :type AppName: str
        :param _StreamName: 流名称。如果只绑定域名或路径，则此处填空。
        :type StreamName: str
        :param _TemplateId: 指定已有的模板Id。
        :type TemplateId: int
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._TemplateId = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveTranscodeRuleResponse(AbstractModel):
    """CreateLiveTranscodeRule返回参数结构体

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


class CreateLiveTranscodeTemplateRequest(AbstractModel):
    """CreateLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称，例： 900p 仅支持字母和数字的组合。
长度限制：
  标准转码：1-10个字符
  极速高清转码：3-10个字符
        :type TemplateName: str
        :param _VideoBitrate: 视频码率。范围：0kbps - 8000kbps。
0为保持原始码率。
注: 转码模板有码率唯一要求，最终保存的码率可能与输入码率有所差别。
        :type VideoBitrate: int
        :param _Acodec: 音频编码：aac，默认aac。
注意：当前该参数未生效，待后续支持！
        :type Acodec: str
        :param _AudioBitrate: 音频码率，默认0。
范围：0-500。
        :type AudioBitrate: int
        :param _Vcodec: 视频编码：h264/h265/origin，默认origin。

origin: 保持原始编码格式
        :type Vcodec: str
        :param _Description: 模板描述。
        :type Description: str
        :param _NeedVideo: 是否保留视频，0：否，1：是。默认1。
        :type NeedVideo: int
        :param _Width: 宽，默认0。
范围[0-3000]
数值必须是2的倍数，0是原始宽度
        :type Width: int
        :param _NeedAudio: 是否保留音频，0：否，1：是。默认1。
        :type NeedAudio: int
        :param _Height: 高，默认0。
范围[0-3000]
数值必须是2的倍数，0是原始高度。
极速高清模板（AiTransCode = 1 的时候）必须传。
        :type Height: int
        :param _Fps: 帧率，默认0。
范围0-60fps
        :type Fps: int
        :param _Gop: 关键帧间隔，单位：秒。
默认原始的间隔
范围2-6
        :type Gop: int
        :param _Rotate: 旋转角度，默认0。
可取值：0，90，180，270
        :type Rotate: int
        :param _Profile: 编码质量：
baseline/main/high。默认baseline
        :type Profile: str
        :param _BitrateToOrig: 当设置的码率>原始码率时，是否以原始码率为准。
0：否， 1：是
默认 0。
        :type BitrateToOrig: int
        :param _HeightToOrig: 当设置的高度>原始高度时，是否以原始高度为准。
0：否， 1：是
默认 0。
        :type HeightToOrig: int
        :param _FpsToOrig: 当设置的帧率>原始帧率时，是否以原始帧率为准。
0：否， 1：是
默认 0。
        :type FpsToOrig: int
        :param _AiTransCode: 是否是极速高清模板，0：否，1：是。默认0。
        :type AiTransCode: int
        :param _AdaptBitratePercent: 极速高清视频码率压缩比。
极速高清目标码率=VideoBitrate * (1-AdaptBitratePercent)

取值范围：0.0到0.5
        :type AdaptBitratePercent: float
        :param _ShortEdgeAsHeight: 是否以短边作为高度，0：否，1：是。默认0。
        :type ShortEdgeAsHeight: int
        :param _DRMType: DRM 加密类型，可选值：fairplay、normalaes、widevine。
不传递或者为空字符串，清空之前的DRM配置。
        :type DRMType: str
        :param _DRMTracks: DRM 加密项，可选值：AUDIO、SD、HD、UHD1、UHD2，后四个为一组，同组中的内容只能选一个。
不传递或者为空字符串，清空之前的DRM配置。
        :type DRMTracks: str
        """
        self._TemplateName = None
        self._VideoBitrate = None
        self._Acodec = None
        self._AudioBitrate = None
        self._Vcodec = None
        self._Description = None
        self._NeedVideo = None
        self._Width = None
        self._NeedAudio = None
        self._Height = None
        self._Fps = None
        self._Gop = None
        self._Rotate = None
        self._Profile = None
        self._BitrateToOrig = None
        self._HeightToOrig = None
        self._FpsToOrig = None
        self._AiTransCode = None
        self._AdaptBitratePercent = None
        self._ShortEdgeAsHeight = None
        self._DRMType = None
        self._DRMTracks = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def VideoBitrate(self):
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def Acodec(self):
        return self._Acodec

    @Acodec.setter
    def Acodec(self, Acodec):
        self._Acodec = Acodec

    @property
    def AudioBitrate(self):
        return self._AudioBitrate

    @AudioBitrate.setter
    def AudioBitrate(self, AudioBitrate):
        self._AudioBitrate = AudioBitrate

    @property
    def Vcodec(self):
        return self._Vcodec

    @Vcodec.setter
    def Vcodec(self, Vcodec):
        self._Vcodec = Vcodec

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NeedVideo(self):
        return self._NeedVideo

    @NeedVideo.setter
    def NeedVideo(self, NeedVideo):
        self._NeedVideo = NeedVideo

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def NeedAudio(self):
        return self._NeedAudio

    @NeedAudio.setter
    def NeedAudio(self, NeedAudio):
        self._NeedAudio = NeedAudio

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Gop(self):
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop

    @property
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate

    @property
    def Profile(self):
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def BitrateToOrig(self):
        return self._BitrateToOrig

    @BitrateToOrig.setter
    def BitrateToOrig(self, BitrateToOrig):
        self._BitrateToOrig = BitrateToOrig

    @property
    def HeightToOrig(self):
        return self._HeightToOrig

    @HeightToOrig.setter
    def HeightToOrig(self, HeightToOrig):
        self._HeightToOrig = HeightToOrig

    @property
    def FpsToOrig(self):
        return self._FpsToOrig

    @FpsToOrig.setter
    def FpsToOrig(self, FpsToOrig):
        self._FpsToOrig = FpsToOrig

    @property
    def AiTransCode(self):
        return self._AiTransCode

    @AiTransCode.setter
    def AiTransCode(self, AiTransCode):
        self._AiTransCode = AiTransCode

    @property
    def AdaptBitratePercent(self):
        return self._AdaptBitratePercent

    @AdaptBitratePercent.setter
    def AdaptBitratePercent(self, AdaptBitratePercent):
        self._AdaptBitratePercent = AdaptBitratePercent

    @property
    def ShortEdgeAsHeight(self):
        return self._ShortEdgeAsHeight

    @ShortEdgeAsHeight.setter
    def ShortEdgeAsHeight(self, ShortEdgeAsHeight):
        self._ShortEdgeAsHeight = ShortEdgeAsHeight

    @property
    def DRMType(self):
        return self._DRMType

    @DRMType.setter
    def DRMType(self, DRMType):
        self._DRMType = DRMType

    @property
    def DRMTracks(self):
        return self._DRMTracks

    @DRMTracks.setter
    def DRMTracks(self, DRMTracks):
        self._DRMTracks = DRMTracks


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._VideoBitrate = params.get("VideoBitrate")
        self._Acodec = params.get("Acodec")
        self._AudioBitrate = params.get("AudioBitrate")
        self._Vcodec = params.get("Vcodec")
        self._Description = params.get("Description")
        self._NeedVideo = params.get("NeedVideo")
        self._Width = params.get("Width")
        self._NeedAudio = params.get("NeedAudio")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._Gop = params.get("Gop")
        self._Rotate = params.get("Rotate")
        self._Profile = params.get("Profile")
        self._BitrateToOrig = params.get("BitrateToOrig")
        self._HeightToOrig = params.get("HeightToOrig")
        self._FpsToOrig = params.get("FpsToOrig")
        self._AiTransCode = params.get("AiTransCode")
        self._AdaptBitratePercent = params.get("AdaptBitratePercent")
        self._ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        self._DRMType = params.get("DRMType")
        self._DRMTracks = params.get("DRMTracks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveTranscodeTemplateResponse(AbstractModel):
    """CreateLiveTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板Id。
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateLiveWatermarkRuleRequest(AbstractModel):
    """CreateLiveWatermarkRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为live。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _TemplateId: 水印Id，即调用[AddLiveWatermark](/document/product/267/30154)接口返回的WatermarkId。
        :type TemplateId: int
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._TemplateId = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveWatermarkRuleResponse(AbstractModel):
    """CreateLiveWatermarkRule返回参数结构体

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


class CreatePullStreamConfigRequest(AbstractModel):
    """CreatePullStreamConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromUrl: 源 Url ，用于拉流的地址。目前可支持直播流及点播文件。
注意：
1. 多个点播url之间使用空格拼接。
2. 目前上限支持10个url。
3. 目前不支持https协议。
4. 支持拉流文件格式：flv，rtmp，hls，mp4。
        :type FromUrl: str
        :param _ToUrl: 目的 Url ，用于推流的地址，目前限制该目标地址为腾讯域名。
仅支持：rtmp 协议。
        :type ToUrl: str
        :param _AreaId: 选择完成转拉推的服务所在区域:
1-深圳，
2-上海，
3-天津，
4-中国香港。
        :type AreaId: int
        :param _IspId: 选择完成转拉推服务使用的运营商网络：
1-电信，
2-移动，
3-联通，
4-其他。
注：AreaId 为4的时候，IspId 只能为其他。
        :type IspId: int
        :param _StartTime: 开始时间。
使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param _EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        """
        self._FromUrl = None
        self._ToUrl = None
        self._AreaId = None
        self._IspId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FromUrl(self):
        return self._FromUrl

    @FromUrl.setter
    def FromUrl(self, FromUrl):
        self._FromUrl = FromUrl

    @property
    def ToUrl(self):
        return self._ToUrl

    @ToUrl.setter
    def ToUrl(self, ToUrl):
        self._ToUrl = ToUrl

    @property
    def AreaId(self):
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def IspId(self):
        return self._IspId

    @IspId.setter
    def IspId(self, IspId):
        self._IspId = IspId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._FromUrl = params.get("FromUrl")
        self._ToUrl = params.get("ToUrl")
        self._AreaId = params.get("AreaId")
        self._IspId = params.get("IspId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePullStreamConfigResponse(AbstractModel):
    """CreatePullStreamConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 配置成功后的 ID。
        :type ConfigId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigId = None
        self._RequestId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._RequestId = params.get("RequestId")


class CreateRecordTaskRequest(AbstractModel):
    """CreateRecordTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _EndTime: 录制任务结束时间，Unix时间戳。设置时间必须大于StartTime及当前时间，且EndTime - StartTime不能超过24小时。
        :type EndTime: int
        :param _StartTime: 录制任务开始时间，Unix时间戳。如果不填表示立即启动录制。StartTime不能超过当前时间+6天。
        :type StartTime: int
        :param _StreamType: 推流类型，默认0。取值：
0-直播推流。
1-合成流，即 A+B=C 类型混流。
        :type StreamType: int
        :param _TemplateId: 录制模板ID，CreateLiveRecordTemplate 返回值。如果不填或者传入错误ID，则默认录制HLS格式、永久存储。
        :type TemplateId: int
        :param _Extension: 扩展字段，暂无定义。默认为空。
        :type Extension: str
        """
        self._StreamName = None
        self._DomainName = None
        self._AppName = None
        self._EndTime = None
        self._StartTime = None
        self._StreamType = None
        self._TemplateId = None
        self._Extension = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Extension(self):
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._StreamType = params.get("StreamType")
        self._TemplateId = params.get("TemplateId")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordTaskResponse(AbstractModel):
    """CreateRecordTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，全局唯一标识录制任务。返回TaskId字段说明录制任务创建成功。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateScreenshotTaskRequest(AbstractModel):
    """CreateScreenshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _EndTime: 截图任务结束时间，Unix时间戳。设置时间必须大于StartTime及当前时间，且EndTime - StartTime不能超过24小时。
        :type EndTime: int
        :param _TemplateId: 截图模板ID，CreateLiveSnapshotTemplate 返回值。如果传入错误ID，则不拉起截图。
        :type TemplateId: int
        :param _StartTime: 截图任务开始时间，Unix时间戳。如果不填表示立即启动截图。StartTime不能超过当前时间+6天。
        :type StartTime: int
        :param _StreamType: 推流类型，默认0。取值：
0-直播推流。
1-合成流，即 A+B=C 类型混流。
        :type StreamType: int
        :param _Extension: 扩展字段，暂无定义。默认为空。
        :type Extension: str
        """
        self._StreamName = None
        self._DomainName = None
        self._AppName = None
        self._EndTime = None
        self._TemplateId = None
        self._StartTime = None
        self._StreamType = None
        self._Extension = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def Extension(self):
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._EndTime = params.get("EndTime")
        self._TemplateId = params.get("TemplateId")
        self._StartTime = params.get("StartTime")
        self._StreamType = params.get("StreamType")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScreenshotTaskResponse(AbstractModel):
    """CreateScreenshotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，全局唯一标识截图任务。返回TaskId字段说明截图任务创建成功。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DayStreamPlayInfo(AbstractModel):
    """流播放信息

    """

    def __init__(self):
        r"""
        :param _Time: 数据时间点，接口返回支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）yyyy-MM-dd HH:mm:ss：使用此格式时，默认代表北京时间。
接口返回的时间格式和查询请求传入的时间格式一致。
        :type Time: str
        :param _Bandwidth: 带宽（单位Mbps）。
        :type Bandwidth: float
        :param _Flux: 流量 （单位MB）。
        :type Flux: float
        :param _Request: 请求数。
        :type Request: int
        :param _Online: 在线人数。
        :type Online: int
        """
        self._Time = None
        self._Bandwidth = None
        self._Flux = None
        self._Request = None
        self._Online = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Flux(self):
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux

    @property
    def Request(self):
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Bandwidth = params.get("Bandwidth")
        self._Flux = params.get("Flux")
        self._Request = params.get("Request")
        self._Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DelayInfo(AbstractModel):
    """延播信息。

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的 
 AppName 保持一致，默认为 live。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _DelayInterval: 延播时间，单位：秒。
        :type DelayInterval: int
        :param _CreateTime: 创建时间，UTC 时间。
注意：UTC时间和北京时间相差8小时。
例如：2019-06-18T12:00:00Z（为北京时间 2019 年 6 月 18 日 20 点 0 分 0 秒）。
        :type CreateTime: str
        :param _ExpireTime: 过期时间，UTC 时间。
注意：UTC时间和北京时间相差8小时。
例如：2019-06-18T12:00:00Z（为北京时间 2019 年 6 月 18 日 20 点 0 分 0 秒）。
        :type ExpireTime: str
        :param _Status: 当前状态:
-1：已过期。
1： 生效中。
        :type Status: int
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._DelayInterval = None
        self._CreateTime = None
        self._ExpireTime = None
        self._Status = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def DelayInterval(self):
        return self._DelayInterval

    @DelayInterval.setter
    def DelayInterval(self, DelayInterval):
        self._DelayInterval = DelayInterval

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._DelayInterval = params.get("DelayInterval")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveCallbackRuleRequest(AbstractModel):
    """DeleteLiveCallbackRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。
        :type AppName: str
        """
        self._DomainName = None
        self._AppName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveCallbackRuleResponse(AbstractModel):
    """DeleteLiveCallbackRule返回参数结构体

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


class DeleteLiveCallbackTemplateRequest(AbstractModel):
    """DeleteLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
1. 在创建回调模板接口 [CreateLiveCallbackTemplate](/document/product/267/32637) 调用的返回值中获取模板 ID。
2. 可以从接口 [DescribeLiveCallbackTemplates](/document/product/267/32632) 查询已经创建的过的模板列表。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveCallbackTemplateResponse(AbstractModel):
    """DeleteLiveCallbackTemplate返回参数结构体

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


class DeleteLiveDomainRequest(AbstractModel):
    """DeleteLiveDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 要删除的域名
        :type DomainName: str
        :param _DomainType: 类型。0-推流，1-播放
        :type DomainType: int
        """
        self._DomainName = None
        self._DomainType = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DomainType(self):
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._DomainType = params.get("DomainType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveDomainResponse(AbstractModel):
    """DeleteLiveDomain返回参数结构体

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


class DeleteLivePadRuleRequest(AbstractModel):
    """DeleteLivePadRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type AppName: str
        :param _StreamName: 流名称。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type StreamName: str
        :param _TemplateId: 直播垫片模板id。
        :type TemplateId: int
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._TemplateId = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLivePadRuleResponse(AbstractModel):
    """DeleteLivePadRule返回参数结构体

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


class DeleteLivePadTemplateRequest(AbstractModel):
    """DeleteLivePadTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLivePadTemplateResponse(AbstractModel):
    """DeleteLivePadTemplate返回参数结构体

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


class DeleteLivePullStreamTaskRequest(AbstractModel):
    """DeleteLivePullStreamTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id。
        :type TaskId: str
        :param _Operator: 操作人姓名。
        :type Operator: str
        """
        self._TaskId = None
        self._Operator = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLivePullStreamTaskResponse(AbstractModel):
    """DeleteLivePullStreamTask返回参数结构体

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


class DeleteLiveRecordRequest(AbstractModel):
    """DeleteLiveRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _TaskId: 任务ID，由CreateLiveRecord接口返回。
        :type TaskId: int
        """
        self._StreamName = None
        self._TaskId = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveRecordResponse(AbstractModel):
    """DeleteLiveRecord返回参数结构体

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


class DeleteLiveRecordRuleRequest(AbstractModel):
    """DeleteLiveRecordRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type AppName: str
        :param _StreamName: 流名称。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type StreamName: str
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveRecordRuleResponse(AbstractModel):
    """DeleteLiveRecordRule返回参数结构体

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


class DeleteLiveRecordTemplateRequest(AbstractModel):
    """DeleteLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: DescribeRecordTemplates接口获取到的模板 ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveRecordTemplateResponse(AbstractModel):
    """DeleteLiveRecordTemplate返回参数结构体

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


class DeleteLiveSnapshotRuleRequest(AbstractModel):
    """DeleteLiveSnapshotRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveSnapshotRuleResponse(AbstractModel):
    """DeleteLiveSnapshotRule返回参数结构体

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


class DeleteLiveSnapshotTemplateRequest(AbstractModel):
    """DeleteLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
1. 在创建截图模板接口 [CreateLiveSnapshotTemplate](/document/product/267/32624) 调用的返回值中获取。
2. 可以从接口 [DescribeLiveSnapshotTemplates](/document/product/267/32619) 中查询已创建的截图模板列表。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveSnapshotTemplateResponse(AbstractModel):
    """DeleteLiveSnapshotTemplate返回参数结构体

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


class DeleteLiveStreamMonitorRequest(AbstractModel):
    """DeleteLiveStreamMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监播任务ID
        :type MonitorId: str
        """
        self._MonitorId = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveStreamMonitorResponse(AbstractModel):
    """DeleteLiveStreamMonitor返回参数结构体

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


class DeleteLiveTimeShiftRuleRequest(AbstractModel):
    """DeleteLiveTimeShiftRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
域名+AppName+StreamName唯一标识单个时移规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
域名+AppName+StreamName唯一标识单个时移规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type AppName: str
        :param _StreamName: 流名称。
域名+AppName+StreamName唯一标识单个时移规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type StreamName: str
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveTimeShiftRuleResponse(AbstractModel):
    """DeleteLiveTimeShiftRule返回参数结构体

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


class DeleteLiveTimeShiftTemplateRequest(AbstractModel):
    """DeleteLiveTimeShiftTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveTimeShiftTemplateResponse(AbstractModel):
    """DeleteLiveTimeShiftTemplate返回参数结构体

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


class DeleteLiveTranscodeRuleRequest(AbstractModel):
    """DeleteLiveTranscodeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 播放域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _TemplateId: 模板ID。
        :type TemplateId: int
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._TemplateId = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveTranscodeRuleResponse(AbstractModel):
    """DeleteLiveTranscodeRule返回参数结构体

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


class DeleteLiveTranscodeTemplateRequest(AbstractModel):
    """DeleteLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
1. 在创建转码模板接口 [CreateLiveTranscodeTemplate](/document/product/267/32646) 调用的返回值中获取模板 ID。
2. 可以从接口 [DescribeLiveTranscodeTemplates](/document/product/267/32641) 查询已经创建过的模板列表。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveTranscodeTemplateResponse(AbstractModel):
    """DeleteLiveTranscodeTemplate返回参数结构体

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


class DeleteLiveWatermarkRequest(AbstractModel):
    """DeleteLiveWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WatermarkId: 水印 ID。
在添加水印接口 [AddLiveWatermark](/document/product/267/30154) 调用返回值中获取水印 ID。
或DescribeLiveWatermarks接口返回的水印ID。
        :type WatermarkId: int
        """
        self._WatermarkId = None

    @property
    def WatermarkId(self):
        return self._WatermarkId

    @WatermarkId.setter
    def WatermarkId(self, WatermarkId):
        self._WatermarkId = WatermarkId


    def _deserialize(self, params):
        self._WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveWatermarkResponse(AbstractModel):
    """DeleteLiveWatermark返回参数结构体

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


class DeleteLiveWatermarkRuleRequest(AbstractModel):
    """DeleteLiveWatermarkRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。与推流和播放地址中的 AppName 保持一致，默认为live。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        """
        self._DomainName = None
        self._AppName = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveWatermarkRuleResponse(AbstractModel):
    """DeleteLiveWatermarkRule返回参数结构体

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


class DeletePullStreamConfigRequest(AbstractModel):
    """DeletePullStreamConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 配置 ID。
1. 在添加拉流配置接口 [CreatePullStreamConfig](/document/api/267/30159) 调用返回值中获取配置 ID。
2. 可以从接口 [DescribePullStreamConfigs](/document/api/267/30158) 中查询已创建过的拉流配置列表。
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePullStreamConfigResponse(AbstractModel):
    """DeletePullStreamConfig返回参数结构体

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


class DeleteRecordTaskRequest(AbstractModel):
    """DeleteRecordTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，CreateRecordTask返回。删除TaskId指定的录制任务。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class DeleteRecordTaskResponse(AbstractModel):
    """DeleteRecordTask返回参数结构体

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


class DeleteScreenshotTaskRequest(AbstractModel):
    """DeleteScreenshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，CreateScreenshotTask返回。删除TaskId指定的截图任务。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class DeleteScreenshotTaskResponse(AbstractModel):
    """DeleteScreenshotTask返回参数结构体

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


class DescribeAllStreamPlayInfoListRequest(AbstractModel):
    """DescribeAllStreamPlayInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueryTime: 查询时间点，精确到分钟粒度，支持最近1个月的数据查询，数据延迟为5分钟左右，如果要查询实时的数据，建议传递5分钟前的时间点，格式为yyyy-mm-dd HH:MM:00。（只精确至分钟，秒数填00）。
        :type QueryTime: str
        :param _PlayDomains: 播放域名列表，若不填，表示总体数据。
        :type PlayDomains: list of str
        """
        self._QueryTime = None
        self._PlayDomains = None

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains


    def _deserialize(self, params):
        self._QueryTime = params.get("QueryTime")
        self._PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllStreamPlayInfoListResponse(AbstractModel):
    """DescribeAllStreamPlayInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueryTime: 查询时间点，回传的输入参数中的查询时间。
        :type QueryTime: str
        :param _DataInfoList: 数据信息列表。
        :type DataInfoList: list of MonitorStreamPlayInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueryTime = None
        self._DataInfoList = None
        self._RequestId = None

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QueryTime = params.get("QueryTime")
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = MonitorStreamPlayInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAreaBillBandwidthAndFluxListRequest(AbstractModel):
    """DescribeAreaBillBandwidthAndFluxList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS，起始和结束时间跨度不支持超过1天。
        :type EndTime: str
        :param _PlayDomains: 直播播放域名，若不填，表示总体数据。
        :type PlayDomains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PlayDomains = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAreaBillBandwidthAndFluxListResponse(AbstractModel):
    """DescribeAreaBillBandwidthAndFluxList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 明细数据信息。
        :type DataInfoList: list of BillAreaInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillAreaInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillBandwidthAndFluxListRequest(AbstractModel):
    """DescribeBillBandwidthAndFluxList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
        :type StartTime: str
        :param _EndTime: 结束时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
起始和结束时间跨度不支持超过31天。支持最近3年的数据查询
        :type EndTime: str
        :param _PlayDomains: 直播播放域名，若不填，表示总体数据。
        :type PlayDomains: list of str
        :param _MainlandOrOversea: 可选值：
Mainland：查询国内数据，
Oversea：则查询国外数据，
默认：查询国内+国外的数据。
注：LEB（快直播）只支持国内+国外数据查询。
        :type MainlandOrOversea: str
        :param _Granularity: 数据粒度，支持如下粒度：
5：5分钟粒度，（跨度不支持超过1天），
60：1小时粒度（跨度不支持超过一个月），
1440：天粒度（跨度不支持超过一个月）。
默认值：5。
        :type Granularity: int
        :param _ServiceName: 服务名称，可选值包括LVB(标准直播)，LEB(快直播)，不填则查LVB+LEB总值。
        :type ServiceName: str
        :param _RegionNames: 大区，映射表如下：
China Mainland 中国大陆
Asia Pacific I 亚太一区
Asia Pacific II 亚太二区
Asia Pacific III 亚太三区
Europe 欧洲
North America 北美
South America 南美
Middle East 中东
Africa 非洲。
        :type RegionNames: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PlayDomains = None
        self._MainlandOrOversea = None
        self._Granularity = None
        self._ServiceName = None
        self._RegionNames = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def RegionNames(self):
        return self._RegionNames

    @RegionNames.setter
    def RegionNames(self, RegionNames):
        self._RegionNames = RegionNames


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayDomains = params.get("PlayDomains")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._Granularity = params.get("Granularity")
        self._ServiceName = params.get("ServiceName")
        self._RegionNames = params.get("RegionNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillBandwidthAndFluxListResponse(AbstractModel):
    """DescribeBillBandwidthAndFluxList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PeakBandwidthTime: 峰值带宽所在时间点，接口返回支持两种时间格式(与接口请求传递的时间格式一致)：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
        :type PeakBandwidthTime: str
        :param _PeakBandwidth: 峰值带宽，单位是Mbps。
        :type PeakBandwidth: float
        :param _P95PeakBandwidthTime: 95峰值带宽所在时间点，接口返回支持两种时间格式(与接口请求传递的时间格式一致)：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
        :type P95PeakBandwidthTime: str
        :param _P95PeakBandwidth: 95峰值带宽，单位是Mbps。
        :type P95PeakBandwidth: float
        :param _SumFlux: 总流量，单位是MB。
        :type SumFlux: float
        :param _DataInfoList: 明细数据信息。
        :type DataInfoList: list of BillDataInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PeakBandwidthTime = None
        self._PeakBandwidth = None
        self._P95PeakBandwidthTime = None
        self._P95PeakBandwidth = None
        self._SumFlux = None
        self._DataInfoList = None
        self._RequestId = None

    @property
    def PeakBandwidthTime(self):
        return self._PeakBandwidthTime

    @PeakBandwidthTime.setter
    def PeakBandwidthTime(self, PeakBandwidthTime):
        self._PeakBandwidthTime = PeakBandwidthTime

    @property
    def PeakBandwidth(self):
        return self._PeakBandwidth

    @PeakBandwidth.setter
    def PeakBandwidth(self, PeakBandwidth):
        self._PeakBandwidth = PeakBandwidth

    @property
    def P95PeakBandwidthTime(self):
        return self._P95PeakBandwidthTime

    @P95PeakBandwidthTime.setter
    def P95PeakBandwidthTime(self, P95PeakBandwidthTime):
        self._P95PeakBandwidthTime = P95PeakBandwidthTime

    @property
    def P95PeakBandwidth(self):
        return self._P95PeakBandwidth

    @P95PeakBandwidth.setter
    def P95PeakBandwidth(self, P95PeakBandwidth):
        self._P95PeakBandwidth = P95PeakBandwidth

    @property
    def SumFlux(self):
        return self._SumFlux

    @SumFlux.setter
    def SumFlux(self, SumFlux):
        self._SumFlux = SumFlux

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PeakBandwidthTime = params.get("PeakBandwidthTime")
        self._PeakBandwidth = params.get("PeakBandwidth")
        self._P95PeakBandwidthTime = params.get("P95PeakBandwidthTime")
        self._P95PeakBandwidth = params.get("P95PeakBandwidth")
        self._SumFlux = params.get("SumFlux")
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCallbackRecordsListRequest(AbstractModel):
    """DescribeCallbackRecordsList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
        :type StartTime: str
        :param _EndTime: 结束时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。

查询的起始和结束时间跨度不支持超过1天。仅支持查询最近14天的数据。
        :type EndTime: str
        :param _StreamName: 流名称，精确匹配。
        :type StreamName: str
        :param _PageNum: 页码。
        :type PageNum: int
        :param _PageSize: 每页条数。
        :type PageSize: int
        :param _EventType: 事件类型。
0: "断流",
1: "推流",
100: "录制"
200: "截图回调"。
        :type EventType: int
        :param _ResultCode: 回调结果。
0为成功，其他为失败。
        :type ResultCode: int
        """
        self._StartTime = None
        self._EndTime = None
        self._StreamName = None
        self._PageNum = None
        self._PageSize = None
        self._EventType = None
        self._ResultCode = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._StreamName = params.get("StreamName")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._EventType = params.get("EventType")
        self._ResultCode = params.get("ResultCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallbackRecordsListResponse(AbstractModel):
    """DescribeCallbackRecordsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 回调事件列表。
        :type DataInfoList: list of CallbackEventInfo
        :param _PageNum: 页码。
        :type PageNum: int
        :param _PageSize: 每页条数。
        :type PageSize: int
        :param _TotalNum: 总条数。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = CallbackEventInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeConcurrentRecordStreamNumRequest(AbstractModel):
    """DescribeConcurrentRecordStreamNum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveType: 直播类型，SlowLive：慢直播。
NormalLive：普通直播。
        :type LiveType: str
        :param _StartTime: 起始时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
可以查询最近180天的数据。
        :type StartTime: str
        :param _EndTime: 结束时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
时间跨度最大支持31天。
        :type EndTime: str
        :param _MainlandOrOversea: 如果为空，查询所有地区数据；如果为“Mainland”，查询国内数据；如果为“Oversea”，则查询国外数据。
        :type MainlandOrOversea: str
        :param _PushDomains: 推流域名列表，不填表示总体数据。
        :type PushDomains: list of str
        """
        self._LiveType = None
        self._StartTime = None
        self._EndTime = None
        self._MainlandOrOversea = None
        self._PushDomains = None

    @property
    def LiveType(self):
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def PushDomains(self):
        return self._PushDomains

    @PushDomains.setter
    def PushDomains(self, PushDomains):
        self._PushDomains = PushDomains


    def _deserialize(self, params):
        self._LiveType = params.get("LiveType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._PushDomains = params.get("PushDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConcurrentRecordStreamNumResponse(AbstractModel):
    """DescribeConcurrentRecordStreamNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 统计信息列表。
        :type DataInfoList: list of ConcurrentRecordStreamNum
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ConcurrentRecordStreamNum()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeliverBandwidthListRequest(AbstractModel):
    """DescribeDeliverBandwidthList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
        :type StartTime: str
        :param _EndTime: 结束时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
支持最近三个月的数据查询，时间跨度最大是1个月。
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
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
        


class DescribeDeliverBandwidthListResponse(AbstractModel):
    """DescribeDeliverBandwidthList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 转推计费带宽数据
        :type DataInfoList: list of BandwidthInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BandwidthInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupProIspPlayInfoListRequest(AbstractModel):
    """DescribeGroupProIspPlayInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS
时间跨度在（0,3小时]，支持最近1个月数据查询。
        :type EndTime: str
        :param _PlayDomains: 播放域名，默认为不填，表示求总体数据。
        :type PlayDomains: list of str
        :param _ProvinceNames: 省份列表，默认不填，则返回各省份的数据。
        :type ProvinceNames: list of str
        :param _IspNames: 运营商列表，默认不填，则返回整个运营商的数据。
        :type IspNames: list of str
        :param _MainlandOrOversea: 国内还是国外，如果为空，查询所有地区数据；如果为“Mainland”，查询国内数据；如果为“Oversea”，则查询国外数据。
        :type MainlandOrOversea: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PlayDomains = None
        self._ProvinceNames = None
        self._IspNames = None
        self._MainlandOrOversea = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def ProvinceNames(self):
        return self._ProvinceNames

    @ProvinceNames.setter
    def ProvinceNames(self, ProvinceNames):
        self._ProvinceNames = ProvinceNames

    @property
    def IspNames(self):
        return self._IspNames

    @IspNames.setter
    def IspNames(self, IspNames):
        self._IspNames = IspNames

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayDomains = params.get("PlayDomains")
        self._ProvinceNames = params.get("ProvinceNames")
        self._IspNames = params.get("IspNames")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupProIspPlayInfoListResponse(AbstractModel):
    """DescribeGroupProIspPlayInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 数据内容。
        :type DataInfoList: list of GroupProIspDataInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = GroupProIspDataInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHttpStatusInfoListRequest(AbstractModel):
    """DescribeHttpStatusInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
注：最大时间跨度支持1天，支持最近3个月的数据查询。
        :type EndTime: str
        :param _PlayDomains: 播放域名列表。
        :type PlayDomains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PlayDomains = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHttpStatusInfoListResponse(AbstractModel):
    """DescribeHttpStatusInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 播放状态码列表。
        :type DataInfoList: list of HttpStatusData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = HttpStatusData()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveCallbackRulesRequest(AbstractModel):
    """DescribeLiveCallbackRules请求参数结构体

    """


class DescribeLiveCallbackRulesResponse(AbstractModel):
    """DescribeLiveCallbackRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则信息列表。
        :type Rules: list of CallBackRuleInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = CallBackRuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveCallbackTemplateRequest(AbstractModel):
    """DescribeLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
1. 在创建回调模板接口 [CreateLiveCallbackTemplate](/document/product/267/32637) 调用的返回值中获取模板 ID。
2. 可以从接口 [DescribeLiveCallbackTemplates](/document/product/267/32632) 查询已经创建的过的模板列表。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveCallbackTemplateResponse(AbstractModel):
    """DescribeLiveCallbackTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 回调模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.CallBackTemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = CallBackTemplateInfo()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class DescribeLiveCallbackTemplatesRequest(AbstractModel):
    """DescribeLiveCallbackTemplates请求参数结构体

    """


class DescribeLiveCallbackTemplatesResponse(AbstractModel):
    """DescribeLiveCallbackTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 模板信息列表。
        :type Templates: list of CallBackTemplateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = CallBackTemplateInfo()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveCertRequest(AbstractModel):
    """DescribeLiveCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: DescribeLiveCerts接口获取到的证书Id。
        :type CertId: int
        """
        self._CertId = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveCertResponse(AbstractModel):
    """DescribeLiveCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertInfo: 证书信息。
        :type CertInfo: :class:`tencentcloud.live.v20180801.models.CertInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertInfo = None
        self._RequestId = None

    @property
    def CertInfo(self):
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertInfo") is not None:
            self._CertInfo = CertInfo()
            self._CertInfo._deserialize(params.get("CertInfo"))
        self._RequestId = params.get("RequestId")


class DescribeLiveCertsRequest(AbstractModel):
    """DescribeLiveCerts请求参数结构体

    """


class DescribeLiveCertsResponse(AbstractModel):
    """DescribeLiveCerts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertInfoSet: 证书信息列表。
        :type CertInfoSet: list of CertInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertInfoSet = None
        self._RequestId = None

    @property
    def CertInfoSet(self):
        return self._CertInfoSet

    @CertInfoSet.setter
    def CertInfoSet(self, CertInfoSet):
        self._CertInfoSet = CertInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertInfoSet") is not None:
            self._CertInfoSet = []
            for item in params.get("CertInfoSet"):
                obj = CertInfo()
                obj._deserialize(item)
                self._CertInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveDelayInfoListRequest(AbstractModel):
    """DescribeLiveDelayInfoList请求参数结构体

    """


class DescribeLiveDelayInfoListResponse(AbstractModel):
    """DescribeLiveDelayInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DelayInfoList: 延播信息列表。
        :type DelayInfoList: list of DelayInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DelayInfoList = None
        self._RequestId = None

    @property
    def DelayInfoList(self):
        return self._DelayInfoList

    @DelayInfoList.setter
    def DelayInfoList(self, DelayInfoList):
        self._DelayInfoList = DelayInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DelayInfoList") is not None:
            self._DelayInfoList = []
            for item in params.get("DelayInfoList"):
                obj = DelayInfo()
                obj._deserialize(item)
                self._DelayInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveDomainCertBindingsRequest(AbstractModel):
    """DescribeLiveDomainCertBindings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainSearch: 要搜索的域名字符串。
        :type DomainSearch: str
        :param _Offset: 记录行的位置，从0开始。默认0。
        :type Offset: int
        :param _Length: 记录行的最大数目。默认50。
若不传，则最多返回50条数据。
        :type Length: int
        :param _DomainName: 要查询的单个域名。
        :type DomainName: str
        :param _OrderBy: 可取值：
ExpireTimeAsc：证书过期时间升序。
ExpireTimeDesc：证书过期时间降序。
        :type OrderBy: str
        """
        self._DomainSearch = None
        self._Offset = None
        self._Length = None
        self._DomainName = None
        self._OrderBy = None

    @property
    def DomainSearch(self):
        return self._DomainSearch

    @DomainSearch.setter
    def DomainSearch(self, DomainSearch):
        self._DomainSearch = DomainSearch

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._DomainSearch = params.get("DomainSearch")
        self._Offset = params.get("Offset")
        self._Length = params.get("Length")
        self._DomainName = params.get("DomainName")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainCertBindingsResponse(AbstractModel):
    """DescribeLiveDomainCertBindings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveDomainCertBindings: 有绑定证书的域名信息数组。
        :type LiveDomainCertBindings: list of LiveDomainCertBindings
        :param _TotalNum: 总的记录行数，便于分页。
        :type TotalNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LiveDomainCertBindings = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def LiveDomainCertBindings(self):
        return self._LiveDomainCertBindings

    @LiveDomainCertBindings.setter
    def LiveDomainCertBindings(self, LiveDomainCertBindings):
        self._LiveDomainCertBindings = LiveDomainCertBindings

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LiveDomainCertBindings") is not None:
            self._LiveDomainCertBindings = []
            for item in params.get("LiveDomainCertBindings"):
                obj = LiveDomainCertBindings()
                obj._deserialize(item)
                self._LiveDomainCertBindings.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class DescribeLiveDomainCertRequest(AbstractModel):
    """DescribeLiveDomainCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 播放域名。
        :type DomainName: str
        """
        self._DomainName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainCertResponse(AbstractModel):
    """DescribeLiveDomainCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainCertInfo: 证书信息。
        :type DomainCertInfo: :class:`tencentcloud.live.v20180801.models.DomainCertInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainCertInfo = None
        self._RequestId = None

    @property
    def DomainCertInfo(self):
        return self._DomainCertInfo

    @DomainCertInfo.setter
    def DomainCertInfo(self, DomainCertInfo):
        self._DomainCertInfo = DomainCertInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainCertInfo") is not None:
            self._DomainCertInfo = DomainCertInfo()
            self._DomainCertInfo._deserialize(params.get("DomainCertInfo"))
        self._RequestId = params.get("RequestId")


class DescribeLiveDomainPlayInfoListRequest(AbstractModel):
    """DescribeLiveDomainPlayInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlayDomains: 播放域名列表。
        :type PlayDomains: list of str
        """
        self._PlayDomains = None

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains


    def _deserialize(self, params):
        self._PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainPlayInfoListResponse(AbstractModel):
    """DescribeLiveDomainPlayInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Time: 数据时间，格式为yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param _TotalBandwidth: 实时总带宽。
        :type TotalBandwidth: float
        :param _TotalFlux: 实时总流量。
        :type TotalFlux: float
        :param _TotalRequest: 总请求数。
        :type TotalRequest: int
        :param _TotalOnline: 实时总连接数。
        :type TotalOnline: int
        :param _DomainInfoList: 分域名的数据情况。
        :type DomainInfoList: list of DomainInfoList
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Time = None
        self._TotalBandwidth = None
        self._TotalFlux = None
        self._TotalRequest = None
        self._TotalOnline = None
        self._DomainInfoList = None
        self._RequestId = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TotalBandwidth(self):
        return self._TotalBandwidth

    @TotalBandwidth.setter
    def TotalBandwidth(self, TotalBandwidth):
        self._TotalBandwidth = TotalBandwidth

    @property
    def TotalFlux(self):
        return self._TotalFlux

    @TotalFlux.setter
    def TotalFlux(self, TotalFlux):
        self._TotalFlux = TotalFlux

    @property
    def TotalRequest(self):
        return self._TotalRequest

    @TotalRequest.setter
    def TotalRequest(self, TotalRequest):
        self._TotalRequest = TotalRequest

    @property
    def TotalOnline(self):
        return self._TotalOnline

    @TotalOnline.setter
    def TotalOnline(self, TotalOnline):
        self._TotalOnline = TotalOnline

    @property
    def DomainInfoList(self):
        return self._DomainInfoList

    @DomainInfoList.setter
    def DomainInfoList(self, DomainInfoList):
        self._DomainInfoList = DomainInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._TotalBandwidth = params.get("TotalBandwidth")
        self._TotalFlux = params.get("TotalFlux")
        self._TotalRequest = params.get("TotalRequest")
        self._TotalOnline = params.get("TotalOnline")
        if params.get("DomainInfoList") is not None:
            self._DomainInfoList = []
            for item in params.get("DomainInfoList"):
                obj = DomainInfoList()
                obj._deserialize(item)
                self._DomainInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveDomainRefererRequest(AbstractModel):
    """DescribeLiveDomainReferer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 播放域名。
        :type DomainName: str
        """
        self._DomainName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainRefererResponse(AbstractModel):
    """DescribeLiveDomainReferer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RefererAuthConfig: 域名 Referer 黑白名单配置。
        :type RefererAuthConfig: :class:`tencentcloud.live.v20180801.models.RefererAuthConfig`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RefererAuthConfig = None
        self._RequestId = None

    @property
    def RefererAuthConfig(self):
        return self._RefererAuthConfig

    @RefererAuthConfig.setter
    def RefererAuthConfig(self, RefererAuthConfig):
        self._RefererAuthConfig = RefererAuthConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RefererAuthConfig") is not None:
            self._RefererAuthConfig = RefererAuthConfig()
            self._RefererAuthConfig._deserialize(params.get("RefererAuthConfig"))
        self._RequestId = params.get("RequestId")


class DescribeLiveDomainRequest(AbstractModel):
    """DescribeLiveDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名。
        :type DomainName: str
        """
        self._DomainName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainResponse(AbstractModel):
    """DescribeLiveDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInfo: 域名信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainInfo: :class:`tencentcloud.live.v20180801.models.DomainInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainInfo = None
        self._RequestId = None

    @property
    def DomainInfo(self):
        return self._DomainInfo

    @DomainInfo.setter
    def DomainInfo(self, DomainInfo):
        self._DomainInfo = DomainInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self._DomainInfo = DomainInfo()
            self._DomainInfo._deserialize(params.get("DomainInfo"))
        self._RequestId = params.get("RequestId")


class DescribeLiveDomainsRequest(AbstractModel):
    """DescribeLiveDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainStatus: 域名状态过滤。0-停用，1-启用。
        :type DomainStatus: int
        :param _DomainType: 域名类型过滤。0-推流，1-播放。
        :type DomainType: int
        :param _PageSize: 分页大小，范围：10~100。默认10。
        :type PageSize: int
        :param _PageNum: 取第几页，范围：1~100000。默认1。
        :type PageNum: int
        :param _IsDelayLive: 0 普通直播 1慢直播 默认0。
        :type IsDelayLive: int
        :param _DomainPrefix: 域名前缀。
        :type DomainPrefix: str
        :param _PlayType: 播放区域，只在 DomainType=1 时该参数有意义。
1: 国内。
2: 全球。
3: 海外。
        :type PlayType: int
        """
        self._DomainStatus = None
        self._DomainType = None
        self._PageSize = None
        self._PageNum = None
        self._IsDelayLive = None
        self._DomainPrefix = None
        self._PlayType = None

    @property
    def DomainStatus(self):
        return self._DomainStatus

    @DomainStatus.setter
    def DomainStatus(self, DomainStatus):
        self._DomainStatus = DomainStatus

    @property
    def DomainType(self):
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def IsDelayLive(self):
        return self._IsDelayLive

    @IsDelayLive.setter
    def IsDelayLive(self, IsDelayLive):
        self._IsDelayLive = IsDelayLive

    @property
    def DomainPrefix(self):
        return self._DomainPrefix

    @DomainPrefix.setter
    def DomainPrefix(self, DomainPrefix):
        self._DomainPrefix = DomainPrefix

    @property
    def PlayType(self):
        return self._PlayType

    @PlayType.setter
    def PlayType(self, PlayType):
        self._PlayType = PlayType


    def _deserialize(self, params):
        self._DomainStatus = params.get("DomainStatus")
        self._DomainType = params.get("DomainType")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._IsDelayLive = params.get("IsDelayLive")
        self._DomainPrefix = params.get("DomainPrefix")
        self._PlayType = params.get("PlayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainsResponse(AbstractModel):
    """DescribeLiveDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllCount: 总记录数。
        :type AllCount: int
        :param _DomainList: 域名详细信息列表。
        :type DomainList: list of DomainInfo
        :param _CreateLimitCount: 可继续添加域名数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateLimitCount: int
        :param _PlayTypeCount: 启用的播放域名加速区域统计，数组元素分别为：中国大陆（境内），全球地区，国际/港澳台（境外）域名数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayTypeCount: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllCount = None
        self._DomainList = None
        self._CreateLimitCount = None
        self._PlayTypeCount = None
        self._RequestId = None

    @property
    def AllCount(self):
        return self._AllCount

    @AllCount.setter
    def AllCount(self, AllCount):
        self._AllCount = AllCount

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def CreateLimitCount(self):
        return self._CreateLimitCount

    @CreateLimitCount.setter
    def CreateLimitCount(self, CreateLimitCount):
        self._CreateLimitCount = CreateLimitCount

    @property
    def PlayTypeCount(self):
        return self._PlayTypeCount

    @PlayTypeCount.setter
    def PlayTypeCount(self, PlayTypeCount):
        self._PlayTypeCount = PlayTypeCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllCount = params.get("AllCount")
        if params.get("DomainList") is not None:
            self._DomainList = []
            for item in params.get("DomainList"):
                obj = DomainInfo()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._CreateLimitCount = params.get("CreateLimitCount")
        self._PlayTypeCount = params.get("PlayTypeCount")
        self._RequestId = params.get("RequestId")


class DescribeLiveForbidStreamListRequest(AbstractModel):
    """DescribeLiveForbidStreamList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 取得第几页，默认1。
        :type PageNum: int
        :param _PageSize: 每页大小，最大100。 
取值：1~100之前的任意整数。
默认值：10。
        :type PageSize: int
        :param _StreamName: 按流名称查询。
        :type StreamName: str
        """
        self._PageNum = None
        self._PageSize = None
        self._StreamName = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveForbidStreamListResponse(AbstractModel):
    """DescribeLiveForbidStreamList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _PageNum: 分页的页码。
        :type PageNum: int
        :param _PageSize: 每页显示的条数。
        :type PageSize: int
        :param _ForbidStreamList: 禁推流列表。
        :type ForbidStreamList: list of ForbidStreamInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._TotalPage = None
        self._PageNum = None
        self._PageSize = None
        self._ForbidStreamList = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ForbidStreamList(self):
        return self._ForbidStreamList

    @ForbidStreamList.setter
    def ForbidStreamList(self, ForbidStreamList):
        self._ForbidStreamList = ForbidStreamList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        if params.get("ForbidStreamList") is not None:
            self._ForbidStreamList = []
            for item in params.get("ForbidStreamList"):
                obj = ForbidStreamInfo()
                obj._deserialize(item)
                self._ForbidStreamList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLivePackageInfoRequest(AbstractModel):
    """DescribeLivePackageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageType: 包类型，可选值：
0：流量包
1：转码包
2: 连麦包。
        :type PackageType: int
        :param _OrderBy: 排序规则:
1. BuyTimeDesc： 最新购买的排在最前面
2. BuyTimeAsc： 最老购买的排在最前面
3. ExpireTimeDesc： 最后过期的排在最前面
4. ExpireTimeAsc：最先过期的排在最前面。

注意：
1. PackageType 为 2（连麦包） 的时候，不支持 3、4 排序。
        :type OrderBy: str
        :param _PageNum: 取得第几页的数据，和 PageSize 同时传递才会生效。
        :type PageNum: int
        :param _PageSize: 分页大小，和 PageNum 同时传递才会生效。
取值：10 ～ 100 之间的任意整数。
        :type PageSize: int
        """
        self._PackageType = None
        self._OrderBy = None
        self._PageNum = None
        self._PageSize = None

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PackageType = params.get("PackageType")
        self._OrderBy = params.get("OrderBy")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLivePackageInfoResponse(AbstractModel):
    """DescribeLivePackageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LivePackageInfoList: 套餐包信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePackageInfoList: list of LivePackageInfo
        :param _PackageBillMode: 套餐包当前计费方式:
-1: 无计费方式或获取失败
0: 无计费方式
201: 月结带宽
202: 月结流量
203: 日结带宽
204: 日结流量
205: 日结时长
206: 月结时长
304: 日结流量。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageBillMode: int
        :param _TotalPage: 总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPage: int
        :param _TotalNum: 数据总条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: int
        :param _PageNum: 当前页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNum: int
        :param _PageSize: 当前每页数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _FluxPackageBillMode: 当请求参数 PackageType = 0 时生效，逗号分隔，从第一个到最后一个分别表示：
标准直播，中国大陆（境内全地区）计费方式。
标准直播，国际/港澳台（境外多地区）计费方式。
快直播，中国大陆（境内全地区）计费方式。
快直播，国际/港澳台（境外多地区）计费方式。
注意：此字段可能返回 null，表示取不到有效值。
        :type FluxPackageBillMode: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LivePackageInfoList = None
        self._PackageBillMode = None
        self._TotalPage = None
        self._TotalNum = None
        self._PageNum = None
        self._PageSize = None
        self._FluxPackageBillMode = None
        self._RequestId = None

    @property
    def LivePackageInfoList(self):
        return self._LivePackageInfoList

    @LivePackageInfoList.setter
    def LivePackageInfoList(self, LivePackageInfoList):
        self._LivePackageInfoList = LivePackageInfoList

    @property
    def PackageBillMode(self):
        return self._PackageBillMode

    @PackageBillMode.setter
    def PackageBillMode(self, PackageBillMode):
        self._PackageBillMode = PackageBillMode

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def FluxPackageBillMode(self):
        return self._FluxPackageBillMode

    @FluxPackageBillMode.setter
    def FluxPackageBillMode(self, FluxPackageBillMode):
        self._FluxPackageBillMode = FluxPackageBillMode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LivePackageInfoList") is not None:
            self._LivePackageInfoList = []
            for item in params.get("LivePackageInfoList"):
                obj = LivePackageInfo()
                obj._deserialize(item)
                self._LivePackageInfoList.append(obj)
        self._PackageBillMode = params.get("PackageBillMode")
        self._TotalPage = params.get("TotalPage")
        self._TotalNum = params.get("TotalNum")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._FluxPackageBillMode = params.get("FluxPackageBillMode")
        self._RequestId = params.get("RequestId")


class DescribeLivePadRulesRequest(AbstractModel):
    """DescribeLivePadRules请求参数结构体

    """


class DescribeLivePadRulesResponse(AbstractModel):
    """DescribeLivePadRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则信息列表。
        :type Rules: list of RuleInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLivePadTemplateRequest(AbstractModel):
    """DescribeLivePadTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLivePadTemplateResponse(AbstractModel):
    """DescribeLivePadTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 直播垫片模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.PadTemplate`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = PadTemplate()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class DescribeLivePadTemplatesRequest(AbstractModel):
    """DescribeLivePadTemplates请求参数结构体

    """


class DescribeLivePadTemplatesResponse(AbstractModel):
    """DescribeLivePadTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 直播垫片模板信息。
        :type Templates: list of PadTemplate
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = PadTemplate()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLivePlayAuthKeyRequest(AbstractModel):
    """DescribeLivePlayAuthKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名。
        :type DomainName: str
        """
        self._DomainName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLivePlayAuthKeyResponse(AbstractModel):
    """DescribeLivePlayAuthKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlayAuthKeyInfo: 播放鉴权key信息。
        :type PlayAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PlayAuthKeyInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlayAuthKeyInfo = None
        self._RequestId = None

    @property
    def PlayAuthKeyInfo(self):
        return self._PlayAuthKeyInfo

    @PlayAuthKeyInfo.setter
    def PlayAuthKeyInfo(self, PlayAuthKeyInfo):
        self._PlayAuthKeyInfo = PlayAuthKeyInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlayAuthKeyInfo") is not None:
            self._PlayAuthKeyInfo = PlayAuthKeyInfo()
            self._PlayAuthKeyInfo._deserialize(params.get("PlayAuthKeyInfo"))
        self._RequestId = params.get("RequestId")


class DescribeLivePullStreamTaskStatusRequest(AbstractModel):
    """DescribeLivePullStreamTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class DescribeLivePullStreamTaskStatusResponse(AbstractModel):
    """DescribeLivePullStreamTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatusInfo: 任务状态信息。
        :type TaskStatusInfo: :class:`tencentcloud.live.v20180801.models.TaskStatusInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatusInfo = None
        self._RequestId = None

    @property
    def TaskStatusInfo(self):
        return self._TaskStatusInfo

    @TaskStatusInfo.setter
    def TaskStatusInfo(self, TaskStatusInfo):
        self._TaskStatusInfo = TaskStatusInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskStatusInfo") is not None:
            self._TaskStatusInfo = TaskStatusInfo()
            self._TaskStatusInfo._deserialize(params.get("TaskStatusInfo"))
        self._RequestId = params.get("RequestId")


class DescribeLivePullStreamTasksRequest(AbstractModel):
    """DescribeLivePullStreamTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。 
来源：调用 CreateLivePullStreamTask 接口时返回。
不填默认查询所有任务，按更新时间倒序排序。
        :type TaskId: str
        :param _PageNum: 取得第几页，默认值：1。
        :type PageNum: int
        :param _PageSize: 分页大小，默认值：10。
取值范围：1~20 之前的任意整数。
        :type PageSize: int
        """
        self._TaskId = None
        self._PageNum = None
        self._PageSize = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLivePullStreamTasksResponse(AbstractModel):
    """DescribeLivePullStreamTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfos: 直播拉流任务信息列表。
        :type TaskInfos: list of PullStreamTaskInfo
        :param _PageNum: 分页的页码。
        :type PageNum: int
        :param _PageSize: 每页大小。
        :type PageSize: int
        :param _TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _LimitTaskNum: 限制可创建的最大任务数。
        :type LimitTaskNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfos = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._LimitTaskNum = None
        self._RequestId = None

    @property
    def TaskInfos(self):
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def LimitTaskNum(self):
        return self._LimitTaskNum

    @LimitTaskNum.setter
    def LimitTaskNum(self, LimitTaskNum):
        self._LimitTaskNum = LimitTaskNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = PullStreamTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._LimitTaskNum = params.get("LimitTaskNum")
        self._RequestId = params.get("RequestId")


class DescribeLivePushAuthKeyRequest(AbstractModel):
    """DescribeLivePushAuthKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        """
        self._DomainName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLivePushAuthKeyResponse(AbstractModel):
    """DescribeLivePushAuthKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PushAuthKeyInfo: 推流鉴权key信息。
        :type PushAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PushAuthKeyInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PushAuthKeyInfo = None
        self._RequestId = None

    @property
    def PushAuthKeyInfo(self):
        return self._PushAuthKeyInfo

    @PushAuthKeyInfo.setter
    def PushAuthKeyInfo(self, PushAuthKeyInfo):
        self._PushAuthKeyInfo = PushAuthKeyInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PushAuthKeyInfo") is not None:
            self._PushAuthKeyInfo = PushAuthKeyInfo()
            self._PushAuthKeyInfo._deserialize(params.get("PushAuthKeyInfo"))
        self._RequestId = params.get("RequestId")


class DescribeLiveRecordRulesRequest(AbstractModel):
    """DescribeLiveRecordRules请求参数结构体

    """


class DescribeLiveRecordRulesResponse(AbstractModel):
    """DescribeLiveRecordRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表。
        :type Rules: list of RuleInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveRecordTemplateRequest(AbstractModel):
    """DescribeLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: [DescribeLiveRecordTemplates](/document/product/267/32609)接口获取到的模板 ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveRecordTemplateResponse(AbstractModel):
    """DescribeLiveRecordTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 录制模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.RecordTemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = RecordTemplateInfo()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class DescribeLiveRecordTemplatesRequest(AbstractModel):
    """DescribeLiveRecordTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsDelayLive: 是否属于慢直播模板，默认：0。
0： 标准直播。
1：慢直播。
        :type IsDelayLive: int
        """
        self._IsDelayLive = None

    @property
    def IsDelayLive(self):
        return self._IsDelayLive

    @IsDelayLive.setter
    def IsDelayLive(self, IsDelayLive):
        self._IsDelayLive = IsDelayLive


    def _deserialize(self, params):
        self._IsDelayLive = params.get("IsDelayLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveRecordTemplatesResponse(AbstractModel):
    """DescribeLiveRecordTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 录制模板信息列表。
        :type Templates: list of RecordTemplateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = RecordTemplateInfo()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveSnapshotRulesRequest(AbstractModel):
    """DescribeLiveSnapshotRules请求参数结构体

    """


class DescribeLiveSnapshotRulesResponse(AbstractModel):
    """DescribeLiveSnapshotRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表。
        :type Rules: list of RuleInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveSnapshotTemplateRequest(AbstractModel):
    """DescribeLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
调用 [CreateLiveSnapshotTemplate](/document/product/267/32624) 时返回的模板 ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveSnapshotTemplateResponse(AbstractModel):
    """DescribeLiveSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 截图模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.SnapshotTemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = SnapshotTemplateInfo()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class DescribeLiveSnapshotTemplatesRequest(AbstractModel):
    """DescribeLiveSnapshotTemplates请求参数结构体

    """


class DescribeLiveSnapshotTemplatesResponse(AbstractModel):
    """DescribeLiveSnapshotTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 截图模板列表。
        :type Templates: list of SnapshotTemplateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = SnapshotTemplateInfo()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveStreamEventListRequest(AbstractModel):
    """DescribeLiveStreamEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间。 
UTC 格式，例如：2018-12-29T19:00:00Z。
支持查询60天内的历史记录。
        :type StartTime: str
        :param _EndTime: 结束时间。
UTC 格式，例如：2018-12-29T20:00:00Z。
不超过当前时间，且和起始时间相差不得超过30天。
        :type EndTime: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _StreamName: 流名称，不支持通配符（*）查询，默认模糊匹配。
可使用IsStrict字段改为精确查询。
        :type StreamName: str
        :param _PageNum: 取得第几页。
默认值：1。
注： 目前只支持10000条内的查询。
        :type PageNum: int
        :param _PageSize: 分页大小。
最大值：100。
取值范围：1~100 之间的任意整数。
默认值：10。
注： 目前只支持10000条内的查询。
        :type PageSize: int
        :param _IsFilter: 是否过滤，默认不过滤。
0：不进行任何过滤。
1：过滤掉开播失败的，只返回开播成功的。
        :type IsFilter: int
        :param _IsStrict: 是否精确查询，默认模糊匹配。
0：模糊匹配。
1：精确查询。
注：使用StreamName时该参数生效。
        :type IsStrict: int
        :param _IsAsc: 是否按结束时间正序显示，默认逆序。
0：逆序。
1：正序。
        :type IsAsc: int
        """
        self._StartTime = None
        self._EndTime = None
        self._AppName = None
        self._DomainName = None
        self._StreamName = None
        self._PageNum = None
        self._PageSize = None
        self._IsFilter = None
        self._IsStrict = None
        self._IsAsc = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def IsFilter(self):
        return self._IsFilter

    @IsFilter.setter
    def IsFilter(self, IsFilter):
        self._IsFilter = IsFilter

    @property
    def IsStrict(self):
        return self._IsStrict

    @IsStrict.setter
    def IsStrict(self, IsStrict):
        self._IsStrict = IsStrict

    @property
    def IsAsc(self):
        return self._IsAsc

    @IsAsc.setter
    def IsAsc(self, IsAsc):
        self._IsAsc = IsAsc


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamName = params.get("StreamName")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._IsFilter = params.get("IsFilter")
        self._IsStrict = params.get("IsStrict")
        self._IsAsc = params.get("IsAsc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamEventListResponse(AbstractModel):
    """DescribeLiveStreamEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventList: 推断流事件列表。
        :type EventList: list of StreamEventInfo
        :param _PageNum: 分页的页码。
        :type PageNum: int
        :param _PageSize: 每页大小。
        :type PageSize: int
        :param _TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventList = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def EventList(self):
        return self._EventList

    @EventList.setter
    def EventList(self, EventList):
        self._EventList = EventList

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self._EventList = []
            for item in params.get("EventList"):
                obj = StreamEventInfo()
                obj._deserialize(item)
                self._EventList.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeLiveStreamMonitorListRequest(AbstractModel):
    """DescribeLiveStreamMonitorList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Index: 查询列表时的起始偏移。
        :type Index: int
        :param _Count: 本次查询的记录个数。最小值为1。
        :type Count: int
        """
        self._Index = None
        self._Count = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamMonitorListResponse(AbstractModel):
    """DescribeLiveStreamMonitorList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 账号下的直播流监播任务个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: int
        :param _LiveStreamMonitors: 直播流监播任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveStreamMonitors: list of LiveStreamMonitorInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._LiveStreamMonitors = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def LiveStreamMonitors(self):
        return self._LiveStreamMonitors

    @LiveStreamMonitors.setter
    def LiveStreamMonitors(self, LiveStreamMonitors):
        self._LiveStreamMonitors = LiveStreamMonitors

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("LiveStreamMonitors") is not None:
            self._LiveStreamMonitors = []
            for item in params.get("LiveStreamMonitors"):
                obj = LiveStreamMonitorInfo()
                obj._deserialize(item)
                self._LiveStreamMonitors.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveStreamMonitorRequest(AbstractModel):
    """DescribeLiveStreamMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监播任务ID。
        :type MonitorId: str
        """
        self._MonitorId = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamMonitorResponse(AbstractModel):
    """DescribeLiveStreamMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveStreamMonitor: 直播监播任务相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveStreamMonitor: :class:`tencentcloud.live.v20180801.models.LiveStreamMonitorInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LiveStreamMonitor = None
        self._RequestId = None

    @property
    def LiveStreamMonitor(self):
        return self._LiveStreamMonitor

    @LiveStreamMonitor.setter
    def LiveStreamMonitor(self, LiveStreamMonitor):
        self._LiveStreamMonitor = LiveStreamMonitor

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LiveStreamMonitor") is not None:
            self._LiveStreamMonitor = LiveStreamMonitorInfo()
            self._LiveStreamMonitor._deserialize(params.get("LiveStreamMonitor"))
        self._RequestId = params.get("RequestId")


class DescribeLiveStreamOnlineListRequest(AbstractModel):
    """DescribeLiveStreamOnlineList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。多域名用户需要填写 DomainName。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。多路径用户需要填写 AppName。
        :type AppName: str
        :param _PageNum: 取得第几页，默认1。
        :type PageNum: int
        :param _PageSize: 每页大小，最大100。 
取值：10~100之间的任意整数。
默认值：10。
        :type PageSize: int
        :param _StreamName: 流名称，用于精确查询。
        :type StreamName: str
        """
        self._DomainName = None
        self._AppName = None
        self._PageNum = None
        self._PageSize = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamOnlineListResponse(AbstractModel):
    """DescribeLiveStreamOnlineList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _PageNum: 分页的页码。
        :type PageNum: int
        :param _PageSize: 每页显示的条数。
        :type PageSize: int
        :param _OnlineInfo: 正在推送流的信息列表。
        :type OnlineInfo: list of StreamOnlineInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._TotalPage = None
        self._PageNum = None
        self._PageSize = None
        self._OnlineInfo = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def OnlineInfo(self):
        return self._OnlineInfo

    @OnlineInfo.setter
    def OnlineInfo(self, OnlineInfo):
        self._OnlineInfo = OnlineInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        if params.get("OnlineInfo") is not None:
            self._OnlineInfo = []
            for item in params.get("OnlineInfo"):
                obj = StreamOnlineInfo()
                obj._deserialize(item)
                self._OnlineInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveStreamPublishedListRequest(AbstractModel):
    """DescribeLiveStreamPublishedList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 您的推流域名。
        :type DomainName: str
        :param _EndTime: 结束时间。
UTC 格式，例如：2016-06-30T19:00:00Z。
不超过当前时间。
注意：EndTime和StartTime相差不可超过30天。
        :type EndTime: str
        :param _StartTime: 起始时间。 
UTC 格式，例如：2016-06-29T19:00:00Z。
最长支持查询60天内数据。
        :type StartTime: str
        :param _AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。不支持模糊匹配。
        :type AppName: str
        :param _PageNum: 取得第几页。
默认值：1。
        :type PageNum: int
        :param _PageSize: 分页大小。
最大值：100。
取值范围：10~100 之前的任意整数。
默认值：10。
        :type PageSize: int
        :param _StreamName: 流名称，支持模糊匹配。
        :type StreamName: str
        """
        self._DomainName = None
        self._EndTime = None
        self._StartTime = None
        self._AppName = None
        self._PageNum = None
        self._PageSize = None
        self._StreamName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._AppName = params.get("AppName")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamPublishedListResponse(AbstractModel):
    """DescribeLiveStreamPublishedList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PublishInfo: 推流记录信息。
        :type PublishInfo: list of StreamName
        :param _PageNum: 分页的页码。
        :type PageNum: int
        :param _PageSize: 每页大小
        :type PageSize: int
        :param _TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PublishInfo = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def PublishInfo(self):
        return self._PublishInfo

    @PublishInfo.setter
    def PublishInfo(self, PublishInfo):
        self._PublishInfo = PublishInfo

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PublishInfo") is not None:
            self._PublishInfo = []
            for item in params.get("PublishInfo"):
                obj = StreamName()
                obj._deserialize(item)
                self._PublishInfo.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeLiveStreamPushInfoListRequest(AbstractModel):
    """DescribeLiveStreamPushInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PushDomain: 推流域名。
        :type PushDomain: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为live。
        :type AppName: str
        :param _PageNum: 页数，
范围[1,10000]，
默认值：1。
        :type PageNum: int
        :param _PageSize: 每页个数，
范围：[1,1000]，
默认值： 200。
        :type PageSize: int
        """
        self._PushDomain = None
        self._AppName = None
        self._PageNum = None
        self._PageSize = None

    @property
    def PushDomain(self):
        return self._PushDomain

    @PushDomain.setter
    def PushDomain(self, PushDomain):
        self._PushDomain = PushDomain

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PushDomain = params.get("PushDomain")
        self._AppName = params.get("AppName")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamPushInfoListResponse(AbstractModel):
    """DescribeLiveStreamPushInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 直播流的统计信息列表。
        :type DataInfoList: list of PushDataInfo
        :param _TotalNum: 所有在线流的总数量。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _PageNum: 当前数据所在页码。
        :type PageNum: int
        :param _PageSize: 每页的在线流的个数。
        :type PageSize: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._TotalNum = None
        self._TotalPage = None
        self._PageNum = None
        self._PageSize = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushDataInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._RequestId = params.get("RequestId")


class DescribeLiveStreamStateRequest(AbstractModel):
    """DescribeLiveStreamState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param _DomainName: 您的推流域名。
        :type DomainName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        """
        self._AppName = None
        self._DomainName = None
        self._StreamName = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamStateResponse(AbstractModel):
    """DescribeLiveStreamState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamState: 流状态，
active：活跃，
inactive：非活跃，
forbid：禁播。
        :type StreamState: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StreamState = None
        self._RequestId = None

    @property
    def StreamState(self):
        return self._StreamState

    @StreamState.setter
    def StreamState(self, StreamState):
        self._StreamState = StreamState

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StreamState = params.get("StreamState")
        self._RequestId = params.get("RequestId")


class DescribeLiveTimeShiftBillInfoListRequest(AbstractModel):
    """DescribeLiveTimeShiftBillInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: UTC开始时间，支持最近三个月的查询，查询时间最长跨度为一个月。

使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param _EndTime: UTC结束时间，支持最近三个月的查询，查询时间最长跨度为一个月。

使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param _PushDomains: 推流域名列表，若不传递此参数，则表示查询总体数据。
        :type PushDomains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PushDomains = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PushDomains(self):
        return self._PushDomains

    @PushDomains.setter
    def PushDomains(self, PushDomains):
        self._PushDomains = PushDomains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PushDomains = params.get("PushDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTimeShiftBillInfoListResponse(AbstractModel):
    """DescribeLiveTimeShiftBillInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 时移计费明细数据。
        :type DataInfoList: list of TimeShiftBillData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TimeShiftBillData()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveTimeShiftRulesRequest(AbstractModel):
    """DescribeLiveTimeShiftRules请求参数结构体

    """


class DescribeLiveTimeShiftRulesResponse(AbstractModel):
    """DescribeLiveTimeShiftRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则信息列表。
        :type Rules: list of RuleInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveTimeShiftTemplatesRequest(AbstractModel):
    """DescribeLiveTimeShiftTemplates请求参数结构体

    """


class DescribeLiveTimeShiftTemplatesResponse(AbstractModel):
    """DescribeLiveTimeShiftTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 直播时移模板信息。
        :type Templates: list of TimeShiftTemplate
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = TimeShiftTemplate()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveTranscodeDetailInfoRequest(AbstractModel):
    """DescribeLiveTranscodeDetailInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PushDomain: 推流域名。
        :type PushDomain: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _DayTime: 查询时间，北京时间，
格式：yyyymmdd。
注意：支持查询近1个月内某天的详细数据，截止到昨天。
        :type DayTime: str
        :param _PageNum: 页数，默认1，
不超过100页。
        :type PageNum: int
        :param _PageSize: 每页个数，默认20，
范围：[10,1000]。
        :type PageSize: int
        :param _StartDayTime: 起始天时间，北京时间，
格式：yyyymmdd。
注意：支持查询近1个月内的详细数据。
        :type StartDayTime: str
        :param _EndDayTime: 结束天时间，北京时间，
格式：yyyymmdd。
注意：支持查询近1个月内的详细数据，截止到昨天，注意DayTime 与（StartDayTime，EndDayTime）必须要传一个，如果都传，会以DayTime为准 。
        :type EndDayTime: str
        """
        self._PushDomain = None
        self._StreamName = None
        self._DayTime = None
        self._PageNum = None
        self._PageSize = None
        self._StartDayTime = None
        self._EndDayTime = None

    @property
    def PushDomain(self):
        return self._PushDomain

    @PushDomain.setter
    def PushDomain(self, PushDomain):
        self._PushDomain = PushDomain

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def DayTime(self):
        return self._DayTime

    @DayTime.setter
    def DayTime(self, DayTime):
        self._DayTime = DayTime

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StartDayTime(self):
        return self._StartDayTime

    @StartDayTime.setter
    def StartDayTime(self, StartDayTime):
        self._StartDayTime = StartDayTime

    @property
    def EndDayTime(self):
        return self._EndDayTime

    @EndDayTime.setter
    def EndDayTime(self, EndDayTime):
        self._EndDayTime = EndDayTime


    def _deserialize(self, params):
        self._PushDomain = params.get("PushDomain")
        self._StreamName = params.get("StreamName")
        self._DayTime = params.get("DayTime")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._StartDayTime = params.get("StartDayTime")
        self._EndDayTime = params.get("EndDayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTranscodeDetailInfoResponse(AbstractModel):
    """DescribeLiveTranscodeDetailInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 统计数据列表。
        :type DataInfoList: list of TranscodeDetailInfo
        :param _PageNum: 页码。
        :type PageNum: int
        :param _PageSize: 每页个数。
        :type PageSize: int
        :param _TotalNum: 总个数。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TranscodeDetailInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeLiveTranscodeRulesRequest(AbstractModel):
    """DescribeLiveTranscodeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateIds: 要筛选的模板ID数组。
        :type TemplateIds: list of int
        :param _DomainNames: 要筛选的域名数组。
        :type DomainNames: list of str
        """
        self._TemplateIds = None
        self._DomainNames = None

    @property
    def TemplateIds(self):
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds

    @property
    def DomainNames(self):
        return self._DomainNames

    @DomainNames.setter
    def DomainNames(self, DomainNames):
        self._DomainNames = DomainNames


    def _deserialize(self, params):
        self._TemplateIds = params.get("TemplateIds")
        self._DomainNames = params.get("DomainNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTranscodeRulesResponse(AbstractModel):
    """DescribeLiveTranscodeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 转码规则列表。
        :type Rules: list of RuleInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveTranscodeTemplateRequest(AbstractModel):
    """DescribeLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
注意：在创建转码模板接口 [CreateLiveTranscodeTemplate](/document/product/267/32646) 调用的返回值中获取模板 ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTranscodeTemplateResponse(AbstractModel):
    """DescribeLiveTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.TemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = TemplateInfo()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class DescribeLiveTranscodeTemplatesRequest(AbstractModel):
    """DescribeLiveTranscodeTemplates请求参数结构体

    """


class DescribeLiveTranscodeTemplatesResponse(AbstractModel):
    """DescribeLiveTranscodeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 转码模板列表。
        :type Templates: list of TemplateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveTranscodeTotalInfoRequest(AbstractModel):
    """DescribeLiveTranscodeTotalInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 结束时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
        :type StartTime: str
        :param _EndTime: 结束时间，
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param _PushDomains: 推流域名列表，若不填，表示查询所有域名总体数据。
指定域名时返回1小时粒度数据。
        :type PushDomains: list of str
        :param _MainlandOrOversea: 可选值：
Mainland：查询中国大陆（境内）数据，
Oversea：则查询国际/港澳台（境外）数据，
默认：查询全球地区（境内+境外）的数据。
        :type MainlandOrOversea: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PushDomains = None
        self._MainlandOrOversea = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PushDomains(self):
        return self._PushDomains

    @PushDomains.setter
    def PushDomains(self, PushDomains):
        self._PushDomains = PushDomains

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PushDomains = params.get("PushDomains")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTranscodeTotalInfoResponse(AbstractModel):
    """DescribeLiveTranscodeTotalInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 统计数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataInfoList: list of TranscodeTotalInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TranscodeTotalInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveWatermarkRequest(AbstractModel):
    """DescribeLiveWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WatermarkId: DescribeLiveWatermarks接口返回的水印 ID。
        :type WatermarkId: int
        """
        self._WatermarkId = None

    @property
    def WatermarkId(self):
        return self._WatermarkId

    @WatermarkId.setter
    def WatermarkId(self, WatermarkId):
        self._WatermarkId = WatermarkId


    def _deserialize(self, params):
        self._WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveWatermarkResponse(AbstractModel):
    """DescribeLiveWatermark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Watermark: 水印信息。
        :type Watermark: :class:`tencentcloud.live.v20180801.models.WatermarkInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Watermark = None
        self._RequestId = None

    @property
    def Watermark(self):
        return self._Watermark

    @Watermark.setter
    def Watermark(self, Watermark):
        self._Watermark = Watermark

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Watermark") is not None:
            self._Watermark = WatermarkInfo()
            self._Watermark._deserialize(params.get("Watermark"))
        self._RequestId = params.get("RequestId")


class DescribeLiveWatermarkRulesRequest(AbstractModel):
    """DescribeLiveWatermarkRules请求参数结构体

    """


class DescribeLiveWatermarkRulesResponse(AbstractModel):
    """DescribeLiveWatermarkRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 水印规则列表。
        :type Rules: list of RuleInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveWatermarksRequest(AbstractModel):
    """DescribeLiveWatermarks请求参数结构体

    """


class DescribeLiveWatermarksResponse(AbstractModel):
    """DescribeLiveWatermarks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 水印总个数。
        :type TotalNum: int
        :param _WatermarkList: 水印信息列表。
        :type WatermarkList: list of WatermarkInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._WatermarkList = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def WatermarkList(self):
        return self._WatermarkList

    @WatermarkList.setter
    def WatermarkList(self, WatermarkList):
        self._WatermarkList = WatermarkList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("WatermarkList") is not None:
            self._WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = WatermarkInfo()
                obj._deserialize(item)
                self._WatermarkList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveXP2PDetailInfoListRequest(AbstractModel):
    """DescribeLiveXP2PDetailInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueryTime: utc分钟粒度查询时间，查询某一分钟的用量数据，格式为：yyyy-mm-ddTHH:MM:00Z，参考https://cloud.tencent.com/document/product/266/11732#I，
例如：北京时间2019-01-08 10:00:00，对应utc时间为：2019-01-08T10:00:00+08:00。

支持最近六个月的查询。
        :type QueryTime: str
        :param _Type: 类型数组，分直播live和点播vod，不传默认查全部。
        :type Type: list of str
        :param _StreamNames: 查询流数组，不传默认查所有流。
        :type StreamNames: list of str
        :param _Dimension: 查询维度，不传该参数则默认查询流维度的数据，传递该参数则只查对应维度的数据，和返回值的字段相关，目前支持AppId维度查询。
        :type Dimension: list of str
        """
        self._QueryTime = None
        self._Type = None
        self._StreamNames = None
        self._Dimension = None

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StreamNames(self):
        return self._StreamNames

    @StreamNames.setter
    def StreamNames(self, StreamNames):
        self._StreamNames = StreamNames

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._QueryTime = params.get("QueryTime")
        self._Type = params.get("Type")
        self._StreamNames = params.get("StreamNames")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveXP2PDetailInfoListResponse(AbstractModel):
    """DescribeLiveXP2PDetailInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: P2P流统计信息。
        :type DataInfoList: list of XP2PDetailInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = XP2PDetailInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogDownloadListRequest(AbstractModel):
    """DescribeLogDownloadList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，北京时间。
格式：yyyy-mm-dd HH:MM:SS。
注：此字段为北京时间（UTC+8时区）。
        :type StartTime: str
        :param _EndTime: 结束时间，北京时间。
格式：yyyy-mm-dd HH:MM:SS。
注意：结束时间 - 开始时间 <=7天。
注：此字段为北京时间（UTC+8时区）。
        :type EndTime: str
        :param _PlayDomains: 域名列表。
        :type PlayDomains: list of str
        :param _IsFastLive: 快直播还是标准直播，0：标准直播，1：快直播。默认为0。
        :type IsFastLive: int
        """
        self._StartTime = None
        self._EndTime = None
        self._PlayDomains = None
        self._IsFastLive = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def IsFastLive(self):
        return self._IsFastLive

    @IsFastLive.setter
    def IsFastLive(self, IsFastLive):
        self._IsFastLive = IsFastLive


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayDomains = params.get("PlayDomains")
        self._IsFastLive = params.get("IsFastLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogDownloadListResponse(AbstractModel):
    """DescribeLogDownloadList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogInfoList: 日志信息列表。
        :type LogInfoList: list of LogInfo
        :param _TotalNum: 总条数。
        :type TotalNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogInfoList = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def LogInfoList(self):
        return self._LogInfoList

    @LogInfoList.setter
    def LogInfoList(self, LogInfoList):
        self._LogInfoList = LogInfoList

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LogInfoList") is not None:
            self._LogInfoList = []
            for item in params.get("LogInfoList"):
                obj = LogInfo()
                obj._deserialize(item)
                self._LogInfoList.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class DescribeMonitorReportRequest(AbstractModel):
    """DescribeMonitorReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监播任务ID。
        :type MonitorId: str
        """
        self._MonitorId = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorReportResponse(AbstractModel):
    """DescribeMonitorReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MPSResult: 媒体处理结果信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MPSResult: :class:`tencentcloud.live.v20180801.models.MPSResult`
        :param _DiagnoseResult: 媒体诊断结果信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseResult: :class:`tencentcloud.live.v20180801.models.DiagnoseResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MPSResult = None
        self._DiagnoseResult = None
        self._RequestId = None

    @property
    def MPSResult(self):
        return self._MPSResult

    @MPSResult.setter
    def MPSResult(self, MPSResult):
        self._MPSResult = MPSResult

    @property
    def DiagnoseResult(self):
        return self._DiagnoseResult

    @DiagnoseResult.setter
    def DiagnoseResult(self, DiagnoseResult):
        self._DiagnoseResult = DiagnoseResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MPSResult") is not None:
            self._MPSResult = MPSResult()
            self._MPSResult._deserialize(params.get("MPSResult"))
        if params.get("DiagnoseResult") is not None:
            self._DiagnoseResult = DiagnoseResult()
            self._DiagnoseResult._deserialize(params.get("DiagnoseResult"))
        self._RequestId = params.get("RequestId")


class DescribePlayErrorCodeDetailInfoListRequest(AbstractModel):
    """DescribePlayErrorCodeDetailInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支持最近1天的数据查询。
        :type EndTime: str
        :param _Granularity: 查询粒度：
1-1分钟粒度。
        :type Granularity: int
        :param _StatType: 是，可选值包括”4xx”,”5xx”，支持”4xx,5xx”等这种混合模式。
        :type StatType: str
        :param _PlayDomains: 播放域名列表。
        :type PlayDomains: list of str
        :param _MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Granularity = None
        self._StatType = None
        self._PlayDomains = None
        self._MainlandOrOversea = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Granularity = params.get("Granularity")
        self._StatType = params.get("StatType")
        self._PlayDomains = params.get("PlayDomains")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayErrorCodeDetailInfoListResponse(AbstractModel):
    """DescribePlayErrorCodeDetailInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HttpCodeList: 统计信息列表。
        :type HttpCodeList: list of HttpCodeInfo
        :param _StatType: 统计类型。
        :type StatType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HttpCodeList = None
        self._StatType = None
        self._RequestId = None

    @property
    def HttpCodeList(self):
        return self._HttpCodeList

    @HttpCodeList.setter
    def HttpCodeList(self, HttpCodeList):
        self._HttpCodeList = HttpCodeList

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HttpCodeList") is not None:
            self._HttpCodeList = []
            for item in params.get("HttpCodeList"):
                obj = HttpCodeInfo()
                obj._deserialize(item)
                self._HttpCodeList.append(obj)
        self._StatType = params.get("StatType")
        self._RequestId = params.get("RequestId")


class DescribePlayErrorCodeSumInfoListRequest(AbstractModel):
    """DescribePlayErrorCodeSumInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，北京时间。
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间点，北京时间。
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支持最近1天的数据查询。
        :type EndTime: str
        :param _PlayDomains: 播放域名列表，不填表示总体数据。
        :type PlayDomains: list of str
        :param _PageNum: 页数，范围[1,1000]，默认值是1。
        :type PageNum: int
        :param _PageSize: 每页个数，范围：[1,1000]，默认值是20。
        :type PageSize: int
        :param _MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        :param _GroupType: 分组参数，可选值：CountryProIsp（默认值），Country（国家），默认是按照国家+省份+运营商来进行分组；目前国外的省份和运营商暂时无法识别。
        :type GroupType: str
        :param _OutLanguage: 输出字段使用的语言，可选值：Chinese（默认值），English，目前国家，省份和运营商支持多语言。
        :type OutLanguage: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PlayDomains = None
        self._PageNum = None
        self._PageSize = None
        self._MainlandOrOversea = None
        self._GroupType = None
        self._OutLanguage = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def OutLanguage(self):
        return self._OutLanguage

    @OutLanguage.setter
    def OutLanguage(self, OutLanguage):
        self._OutLanguage = OutLanguage


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayDomains = params.get("PlayDomains")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._GroupType = params.get("GroupType")
        self._OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayErrorCodeSumInfoListResponse(AbstractModel):
    """DescribePlayErrorCodeSumInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProIspInfoList: 分省份分运营商错误码为2或3或4或5开头的状态码数据信息。
        :type ProIspInfoList: list of ProIspPlayCodeDataInfo
        :param _TotalCodeAll: 所有状态码的加和的次数。
        :type TotalCodeAll: int
        :param _TotalCode4xx: 状态码为4开头的总次数。
        :type TotalCode4xx: int
        :param _TotalCode5xx: 状态码为5开头的总次数。
        :type TotalCode5xx: int
        :param _TotalCodeList: 各状态码的总次数。
        :type TotalCodeList: list of PlayCodeTotalInfo
        :param _PageNum: 页号。
        :type PageNum: int
        :param _PageSize: 每页大小。
        :type PageSize: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _TotalNum: 总记录数。
        :type TotalNum: int
        :param _TotalCode2xx: 状态码为2开头的总次数。
        :type TotalCode2xx: int
        :param _TotalCode3xx: 状态码为3开头的总次数。
        :type TotalCode3xx: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProIspInfoList = None
        self._TotalCodeAll = None
        self._TotalCode4xx = None
        self._TotalCode5xx = None
        self._TotalCodeList = None
        self._PageNum = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalNum = None
        self._TotalCode2xx = None
        self._TotalCode3xx = None
        self._RequestId = None

    @property
    def ProIspInfoList(self):
        return self._ProIspInfoList

    @ProIspInfoList.setter
    def ProIspInfoList(self, ProIspInfoList):
        self._ProIspInfoList = ProIspInfoList

    @property
    def TotalCodeAll(self):
        return self._TotalCodeAll

    @TotalCodeAll.setter
    def TotalCodeAll(self, TotalCodeAll):
        self._TotalCodeAll = TotalCodeAll

    @property
    def TotalCode4xx(self):
        return self._TotalCode4xx

    @TotalCode4xx.setter
    def TotalCode4xx(self, TotalCode4xx):
        self._TotalCode4xx = TotalCode4xx

    @property
    def TotalCode5xx(self):
        return self._TotalCode5xx

    @TotalCode5xx.setter
    def TotalCode5xx(self, TotalCode5xx):
        self._TotalCode5xx = TotalCode5xx

    @property
    def TotalCodeList(self):
        return self._TotalCodeList

    @TotalCodeList.setter
    def TotalCodeList(self, TotalCodeList):
        self._TotalCodeList = TotalCodeList

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalCode2xx(self):
        return self._TotalCode2xx

    @TotalCode2xx.setter
    def TotalCode2xx(self, TotalCode2xx):
        self._TotalCode2xx = TotalCode2xx

    @property
    def TotalCode3xx(self):
        return self._TotalCode3xx

    @TotalCode3xx.setter
    def TotalCode3xx(self, TotalCode3xx):
        self._TotalCode3xx = TotalCode3xx

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProIspInfoList") is not None:
            self._ProIspInfoList = []
            for item in params.get("ProIspInfoList"):
                obj = ProIspPlayCodeDataInfo()
                obj._deserialize(item)
                self._ProIspInfoList.append(obj)
        self._TotalCodeAll = params.get("TotalCodeAll")
        self._TotalCode4xx = params.get("TotalCode4xx")
        self._TotalCode5xx = params.get("TotalCode5xx")
        if params.get("TotalCodeList") is not None:
            self._TotalCodeList = []
            for item in params.get("TotalCodeList"):
                obj = PlayCodeTotalInfo()
                obj._deserialize(item)
                self._TotalCodeList.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalNum = params.get("TotalNum")
        self._TotalCode2xx = params.get("TotalCode2xx")
        self._TotalCode3xx = params.get("TotalCode3xx")
        self._RequestId = params.get("RequestId")


class DescribeProIspPlaySumInfoListRequest(AbstractModel):
    """DescribeProIspPlaySumInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支持最近1天的数据查询。
        :type EndTime: str
        :param _StatType: 统计的类型，可选值：”Province”(省份)，”Isp”(运营商)，“CountryOrArea”(国家或地区)。
        :type StatType: str
        :param _PlayDomains: 播放域名列表，不填则为全部。
        :type PlayDomains: list of str
        :param _PageNum: 页号，范围是[1,1000]，默认值是1。
        :type PageNum: int
        :param _PageSize: 每页个数，范围是[1,1000]，默认值是20。
        :type PageSize: int
        :param _MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        :param _OutLanguage: 输出字段使用的语言，可选值：Chinese（默认值），English；目前国家，省份和运营商支持多语言。
        :type OutLanguage: str
        """
        self._StartTime = None
        self._EndTime = None
        self._StatType = None
        self._PlayDomains = None
        self._PageNum = None
        self._PageSize = None
        self._MainlandOrOversea = None
        self._OutLanguage = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def OutLanguage(self):
        return self._OutLanguage

    @OutLanguage.setter
    def OutLanguage(self, OutLanguage):
        self._OutLanguage = OutLanguage


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._StatType = params.get("StatType")
        self._PlayDomains = params.get("PlayDomains")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProIspPlaySumInfoListResponse(AbstractModel):
    """DescribeProIspPlaySumInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalFlux: 总流量。
        :type TotalFlux: float
        :param _TotalRequest: 总请求数。
        :type TotalRequest: int
        :param _StatType: 统计的类型。
        :type StatType: str
        :param _PageSize: 每页的记录数。
        :type PageSize: int
        :param _PageNum: 页号。
        :type PageNum: int
        :param _TotalNum: 总记录数。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _DataInfoList: 省份，运营商，国家或地区汇总数据列表。
        :type DataInfoList: list of ProIspPlaySumInfo
        :param _AvgFluxPerSecond: 下载速度，单位：MB/s，计算方式：总流量/总时长。
        :type AvgFluxPerSecond: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalFlux = None
        self._TotalRequest = None
        self._StatType = None
        self._PageSize = None
        self._PageNum = None
        self._TotalNum = None
        self._TotalPage = None
        self._DataInfoList = None
        self._AvgFluxPerSecond = None
        self._RequestId = None

    @property
    def TotalFlux(self):
        return self._TotalFlux

    @TotalFlux.setter
    def TotalFlux(self, TotalFlux):
        self._TotalFlux = TotalFlux

    @property
    def TotalRequest(self):
        return self._TotalRequest

    @TotalRequest.setter
    def TotalRequest(self, TotalRequest):
        self._TotalRequest = TotalRequest

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def AvgFluxPerSecond(self):
        return self._AvgFluxPerSecond

    @AvgFluxPerSecond.setter
    def AvgFluxPerSecond(self, AvgFluxPerSecond):
        self._AvgFluxPerSecond = AvgFluxPerSecond

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalFlux = params.get("TotalFlux")
        self._TotalRequest = params.get("TotalRequest")
        self._StatType = params.get("StatType")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ProIspPlaySumInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self._RequestId = params.get("RequestId")


class DescribeProvinceIspPlayInfoListRequest(AbstractModel):
    """DescribeProvinceIspPlayInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，当前使用北京时间，
例：2019-02-21 10:00:00。
        :type StartTime: str
        :param _EndTime: 结束时间点，当前使用北京时间，
例：2019-02-21 12:00:00。
注：EndTime 和 StartTime 只支持最近1天的数据查询。
        :type EndTime: str
        :param _Granularity: 支持如下粒度：
1：1分钟粒度（跨度不支持超过1天）
        :type Granularity: int
        :param _StatType: 统计指标类型：
“Bandwidth”：带宽
“FluxPerSecond”：平均流量
“Flux”：流量
“Request”：请求数
“Online”：并发连接数
        :type StatType: str
        :param _PlayDomains: 播放域名列表。
        :type PlayDomains: list of str
        :param _ProvinceNames: 要查询的省份（地区）英文名称列表，如 Beijing。
        :type ProvinceNames: list of str
        :param _IspNames: 要查询的运营商英文名称列表，如 China Mobile ，如果为空，查询所有运营商的数据。
        :type IspNames: list of str
        :param _MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        :param _IpType: ip类型：
“Ipv6”：Ipv6数据
如果为空，查询总的数据；
        :type IpType: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Granularity = None
        self._StatType = None
        self._PlayDomains = None
        self._ProvinceNames = None
        self._IspNames = None
        self._MainlandOrOversea = None
        self._IpType = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def ProvinceNames(self):
        return self._ProvinceNames

    @ProvinceNames.setter
    def ProvinceNames(self, ProvinceNames):
        self._ProvinceNames = ProvinceNames

    @property
    def IspNames(self):
        return self._IspNames

    @IspNames.setter
    def IspNames(self, IspNames):
        self._IspNames = IspNames

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def IpType(self):
        return self._IpType

    @IpType.setter
    def IpType(self, IpType):
        self._IpType = IpType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Granularity = params.get("Granularity")
        self._StatType = params.get("StatType")
        self._PlayDomains = params.get("PlayDomains")
        self._ProvinceNames = params.get("ProvinceNames")
        self._IspNames = params.get("IspNames")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._IpType = params.get("IpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProvinceIspPlayInfoListResponse(AbstractModel):
    """DescribeProvinceIspPlayInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 播放信息列表。
        :type DataInfoList: list of PlayStatInfo
        :param _StatType: 统计的类型，和输入参数保持一致。
        :type StatType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._StatType = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayStatInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._StatType = params.get("StatType")
        self._RequestId = params.get("RequestId")


class DescribePullStreamConfigsRequest(AbstractModel):
    """DescribePullStreamConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 配置 ID。
获取途径：从 CreatePullStreamConfig 接口返回值获取。
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePullStreamConfigsResponse(AbstractModel):
    """DescribePullStreamConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PullStreamConfigs: 拉流配置。
        :type PullStreamConfigs: list of PullStreamConfig
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullStreamConfigs = None
        self._RequestId = None

    @property
    def PullStreamConfigs(self):
        return self._PullStreamConfigs

    @PullStreamConfigs.setter
    def PullStreamConfigs(self, PullStreamConfigs):
        self._PullStreamConfigs = PullStreamConfigs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullStreamConfigs") is not None:
            self._PullStreamConfigs = []
            for item in params.get("PullStreamConfigs"):
                obj = PullStreamConfig()
                obj._deserialize(item)
                self._PullStreamConfigs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePushBandwidthAndFluxListRequest(AbstractModel):
    """DescribePushBandwidthAndFluxList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，格式为 yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间点，格式为 yyyy-mm-dd HH:MM:SS，起始和结束时间跨度不支持超过31天。
        :type EndTime: str
        :param _PushDomains: 域名，可以填多个，若不填，表示总体数据。
        :type PushDomains: list of str
        :param _MainlandOrOversea: 可选值：
Mainland：查询中国大陆（境内）数据，
Oversea：则查询国际/港澳台（境外）数据，
不填则默认查询全球地区（境内+境外）的数据。
        :type MainlandOrOversea: str
        :param _Granularity: 数据粒度，支持如下粒度：
5：5分钟粒度，（跨度不支持超过1天），
60：1小时粒度（跨度不支持超过一个月），
1440：天粒度（跨度不支持超过一个月）。
默认值：5。
        :type Granularity: int
        :param _RegionNames: 大区，映射表如下：
China Mainland 中国大陆
Asia Pacific I 亚太一区
Asia Pacific II 亚太二区
Asia Pacific III 亚太三区
Europe 欧洲
North America 北美
South America 南美
Middle East 中东
Africa 非洲。
        :type RegionNames: list of str
        :param _CountryNames: 国家，映射表参照如下文档：
https://cloud.tencent.com/document/product/267/34019。
        :type CountryNames: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PushDomains = None
        self._MainlandOrOversea = None
        self._Granularity = None
        self._RegionNames = None
        self._CountryNames = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PushDomains(self):
        return self._PushDomains

    @PushDomains.setter
    def PushDomains(self, PushDomains):
        self._PushDomains = PushDomains

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity

    @property
    def RegionNames(self):
        return self._RegionNames

    @RegionNames.setter
    def RegionNames(self, RegionNames):
        self._RegionNames = RegionNames

    @property
    def CountryNames(self):
        return self._CountryNames

    @CountryNames.setter
    def CountryNames(self, CountryNames):
        self._CountryNames = CountryNames


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PushDomains = params.get("PushDomains")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._Granularity = params.get("Granularity")
        self._RegionNames = params.get("RegionNames")
        self._CountryNames = params.get("CountryNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePushBandwidthAndFluxListResponse(AbstractModel):
    """DescribePushBandwidthAndFluxList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PeakBandwidthTime: 峰值带宽所在时间点，格式为 yyyy-mm-dd HH:MM:SS。
        :type PeakBandwidthTime: str
        :param _PeakBandwidth: 峰值带宽，单位是 Mbps。
        :type PeakBandwidth: float
        :param _P95PeakBandwidthTime: 95峰值带宽所在时间点，格式为 yyyy-mm-dd HH:MM:SS。
        :type P95PeakBandwidthTime: str
        :param _P95PeakBandwidth: 95峰值带宽，单位是 Mbps。
        :type P95PeakBandwidth: float
        :param _SumFlux: 总流量，单位是 MB。
        :type SumFlux: float
        :param _DataInfoList: 明细数据信息。
        :type DataInfoList: list of BillDataInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PeakBandwidthTime = None
        self._PeakBandwidth = None
        self._P95PeakBandwidthTime = None
        self._P95PeakBandwidth = None
        self._SumFlux = None
        self._DataInfoList = None
        self._RequestId = None

    @property
    def PeakBandwidthTime(self):
        return self._PeakBandwidthTime

    @PeakBandwidthTime.setter
    def PeakBandwidthTime(self, PeakBandwidthTime):
        self._PeakBandwidthTime = PeakBandwidthTime

    @property
    def PeakBandwidth(self):
        return self._PeakBandwidth

    @PeakBandwidth.setter
    def PeakBandwidth(self, PeakBandwidth):
        self._PeakBandwidth = PeakBandwidth

    @property
    def P95PeakBandwidthTime(self):
        return self._P95PeakBandwidthTime

    @P95PeakBandwidthTime.setter
    def P95PeakBandwidthTime(self, P95PeakBandwidthTime):
        self._P95PeakBandwidthTime = P95PeakBandwidthTime

    @property
    def P95PeakBandwidth(self):
        return self._P95PeakBandwidth

    @P95PeakBandwidth.setter
    def P95PeakBandwidth(self, P95PeakBandwidth):
        self._P95PeakBandwidth = P95PeakBandwidth

    @property
    def SumFlux(self):
        return self._SumFlux

    @SumFlux.setter
    def SumFlux(self, SumFlux):
        self._SumFlux = SumFlux

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PeakBandwidthTime = params.get("PeakBandwidthTime")
        self._PeakBandwidth = params.get("PeakBandwidth")
        self._P95PeakBandwidthTime = params.get("P95PeakBandwidthTime")
        self._P95PeakBandwidth = params.get("P95PeakBandwidth")
        self._SumFlux = params.get("SumFlux")
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordTaskRequest(AbstractModel):
    """DescribeRecordTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询任务开始时间，Unix 时间戳。设置时间不早于当前时间之前90天的时间，且查询时间跨度不超过一周。
        :type StartTime: int
        :param _EndTime: 查询任务结束时间，Unix 时间戳。EndTime 必须大于 StartTime，设置时间不早于当前时间之前90天的时间，且查询时间跨度不超过一周。（注意：任务开始结束时间必须在查询时间范围内）。
        :type EndTime: int
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _ScrollToken: 翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。
        :type ScrollToken: str
        """
        self._StartTime = None
        self._EndTime = None
        self._StreamName = None
        self._DomainName = None
        self._AppName = None
        self._ScrollToken = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._StreamName = params.get("StreamName")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._ScrollToken = params.get("ScrollToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordTaskResponse(AbstractModel):
    """DescribeRecordTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScrollToken: 翻页标识，当请求未返回所有数据，该字段表示下一条记录的 Token。当该字段为空，说明已无更多数据。
        :type ScrollToken: str
        :param _TaskList: 录制任务列表。当该字段为空，说明已返回所有数据。
        :type TaskList: list of RecordTask
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScrollToken = None
        self._TaskList = None
        self._RequestId = None

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken

    @property
    def TaskList(self):
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScrollToken = params.get("ScrollToken")
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = RecordTask()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScreenShotSheetNumListRequest(AbstractModel):
    """DescribeScreenShotSheetNumList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
        :type StartTime: str
        :param _EndTime: 结束时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
支持查询最近1年的数据。
        :type EndTime: str
        :param _Zone: 地域信息，可选值包括Mainland，Oversea，前者是查询中国大陆范围内的数据，后者是除中国大陆范围之外的数据，若不传该参数，则查询所有地区的数据。
        :type Zone: str
        :param _PushDomains: 推流域名（支持查询2019年11 月1日之后的域名维度数据）。
        :type PushDomains: list of str
        :param _Granularity: 数据维度，数据延迟1个半小时，可选值包括：1、Minute（5分钟粒度，最大支持查询时间范围是31天），2、Day（天粒度，默认值，按照北京时间做跨天处理，最大支持查询时间范围是186天当天）。
        :type Granularity: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Zone = None
        self._PushDomains = None
        self._Granularity = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def PushDomains(self):
        return self._PushDomains

    @PushDomains.setter
    def PushDomains(self, PushDomains):
        self._PushDomains = PushDomains

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Zone = params.get("Zone")
        self._PushDomains = params.get("PushDomains")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScreenShotSheetNumListResponse(AbstractModel):
    """DescribeScreenShotSheetNumList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 数据信息列表。
        :type DataInfoList: list of TimeValue
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TimeValue()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScreenshotTaskRequest(AbstractModel):
    """DescribeScreenshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询任务开始时间，Unix 时间戳。设置时间不早于当前时间之前90天的时间，且查询时间跨度不超过一周。
        :type StartTime: int
        :param _EndTime: 查询任务结束时间，Unix 时间戳。EndTime 必须大于 StartTime，设置时间不早于当前时间之前90天的时间，且查询时间跨度不超过一周。（注意：任务开始结束时间必须在查询时间范围内）。
        :type EndTime: int
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _ScrollToken: 翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。
        :type ScrollToken: str
        """
        self._StartTime = None
        self._EndTime = None
        self._StreamName = None
        self._DomainName = None
        self._AppName = None
        self._ScrollToken = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._StreamName = params.get("StreamName")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._ScrollToken = params.get("ScrollToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScreenshotTaskResponse(AbstractModel):
    """DescribeScreenshotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScrollToken: 翻页标识，当请求未返回所有数据，该字段表示下一条记录的 Token。当该字段为空，说明已无更多数据。
        :type ScrollToken: str
        :param _TaskList: 截图任务列表。当该字段为空，说明已返回所有数据。
        :type TaskList: list of ScreenshotTask
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScrollToken = None
        self._TaskList = None
        self._RequestId = None

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken

    @property
    def TaskList(self):
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScrollToken = params.get("ScrollToken")
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = ScreenshotTask()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamDayPlayInfoListRequest(AbstractModel):
    """DescribeStreamDayPlayInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DayTime: 日期，格式：YYYY-mm-dd。
第二天凌晨3点出昨天的数据，建议在这个时间点之后查询最新数据。支持最近3个月的数据查询。
        :type DayTime: str
        :param _PlayDomain: 播放域名。
        :type PlayDomain: str
        :param _PageNum: 页号，范围[1,1000]，默认值是1。
        :type PageNum: int
        :param _PageSize: 每页个数，范围[100,1000]，默认值是1000。
        :type PageSize: int
        :param _MainlandOrOversea: 可选值：
Mainland：查询国内数据，
Oversea：则查询国外数据，
默认：查询国内+国外的数据。
        :type MainlandOrOversea: str
        :param _ServiceName: 服务名称，可选值包括LVB(标准直播)，LEB(快直播)，不填则查LVB+LEB总值。
        :type ServiceName: str
        """
        self._DayTime = None
        self._PlayDomain = None
        self._PageNum = None
        self._PageSize = None
        self._MainlandOrOversea = None
        self._ServiceName = None

    @property
    def DayTime(self):
        return self._DayTime

    @DayTime.setter
    def DayTime(self, DayTime):
        self._DayTime = DayTime

    @property
    def PlayDomain(self):
        return self._PlayDomain

    @PlayDomain.setter
    def PlayDomain(self, PlayDomain):
        self._PlayDomain = PlayDomain

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._DayTime = params.get("DayTime")
        self._PlayDomain = params.get("PlayDomain")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamDayPlayInfoListResponse(AbstractModel):
    """DescribeStreamDayPlayInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 播放数据信息列表。
        :type DataInfoList: list of PlayDataInfoByStream
        :param _TotalNum: 总数量。
        :type TotalNum: int
        :param _TotalPage: 总页数。
        :type TotalPage: int
        :param _PageNum: 当前数据所处页码。
        :type PageNum: int
        :param _PageSize: 每页个数。
        :type PageSize: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._TotalNum = None
        self._TotalPage = None
        self._PageNum = None
        self._PageSize = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayDataInfoByStream()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._RequestId = params.get("RequestId")


class DescribeStreamPlayInfoListRequest(AbstractModel):
    """DescribeStreamPlayInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）yyyy-MM-dd HH:mm:ss：使用此格式时，默认代表北京时间。
开始时间和结束时间的格式需要保持一致。
        :type StartTime: str
        :param _EndTime: 结束时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）yyyy-MM-dd HH:mm:ss：使用此格式时，默认代表北京时间。
开始时间和结束时间的格式需要保持一致。结束时间和开始时间跨度不支持超过24小时，支持距当前时间一个月内的数据查询。
        :type EndTime: str
        :param _PlayDomain: 播放域名，
若不填，则为查询所有播放域名的在线流数据。
        :type PlayDomain: str
        :param _StreamName: 流名称，精确匹配。
若不填，则为查询总体播放数据。
        :type StreamName: str
        :param _AppName: 推流路径，与播放地址中的AppName保持一致，会精确匹配，在同时传递了StreamName时生效。
若不填，则为查询总体播放数据。
        :type AppName: str
        :param _ServiceName: 服务名称，可选值包括LVB(标准直播)，LEB(快直播)，不填则查LVB+LEB总值。
        :type ServiceName: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PlayDomain = None
        self._StreamName = None
        self._AppName = None
        self._ServiceName = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomain(self):
        return self._PlayDomain

    @PlayDomain.setter
    def PlayDomain(self, PlayDomain):
        self._PlayDomain = PlayDomain

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayDomain = params.get("PlayDomain")
        self._StreamName = params.get("StreamName")
        self._AppName = params.get("AppName")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPlayInfoListResponse(AbstractModel):
    """DescribeStreamPlayInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 统计信息列表，时间粒度是1分钟。
        :type DataInfoList: list of DayStreamPlayInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = DayStreamPlayInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamPushInfoListRequest(AbstractModel):
    """DescribeStreamPushInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _StartTime: 起始时间点，北京时间，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间点，北京时间，格式为yyyy-mm-dd HH:MM:SS，支持查询最近7天数据，建议查询时间跨度在3小时之内。
        :type EndTime: str
        :param _PushDomain: 推流域名。
        :type PushDomain: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        """
        self._StreamName = None
        self._StartTime = None
        self._EndTime = None
        self._PushDomain = None
        self._AppName = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PushDomain(self):
        return self._PushDomain

    @PushDomain.setter
    def PushDomain(self, PushDomain):
        self._PushDomain = PushDomain

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PushDomain = params.get("PushDomain")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPushInfoListResponse(AbstractModel):
    """DescribeStreamPushInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 返回的数据列表。
        :type DataInfoList: list of PushQualityData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushQualityData()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimeShiftRecordDetailRequest(AbstractModel):
    """DescribeTimeShiftRecordDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 推流域名。
        :type Domain: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _StartTime: 查询范围起始时间，Unix 时间戳。
        :type StartTime: int
        :param _EndTime: 查询范围终止时间，Unix 时间戳。 
        :type EndTime: int
        :param _DomainGroup: 推流域名所属组，没有域名组或者域名组为空字符串可不填。
        :type DomainGroup: str
        :param _TransCodeId: 转码模板ID，转码模板ID为0可不填。
        :type TransCodeId: int
        """
        self._Domain = None
        self._AppName = None
        self._StreamName = None
        self._StartTime = None
        self._EndTime = None
        self._DomainGroup = None
        self._TransCodeId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DomainGroup(self):
        return self._DomainGroup

    @DomainGroup.setter
    def DomainGroup(self, DomainGroup):
        self._DomainGroup = DomainGroup

    @property
    def TransCodeId(self):
        return self._TransCodeId

    @TransCodeId.setter
    def TransCodeId(self, TransCodeId):
        self._TransCodeId = TransCodeId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DomainGroup = params.get("DomainGroup")
        self._TransCodeId = params.get("TransCodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimeShiftRecordDetailResponse(AbstractModel):
    """DescribeTimeShiftRecordDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordList: 时移录制会话数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of TimeShiftRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordList = None
        self._RequestId = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = TimeShiftRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimeShiftStreamListRequest(AbstractModel):
    """DescribeTimeShiftStreamList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询范围起始时间，Unix 时间戳。
        :type StartTime: int
        :param _EndTime: 查询范围结束时间，Unix 时间戳。
        :type EndTime: int
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _Domain: 推流域名。
        :type Domain: str
        :param _DomainGroup: 推流域名所属域名组。
        :type DomainGroup: str
        :param _PageSize: 用户指定要返回的最大结果数，取值范围[0,100]，不指定或者指定为0时，API 
默认值为100。指定超过100时，API 强制使用100。指定值为负数时，接口返回错误。
        :type PageSize: int
        :param _PageNum: 指定拉取的页码，不传时默认为1。
        :type PageNum: int
        """
        self._StartTime = None
        self._EndTime = None
        self._StreamName = None
        self._Domain = None
        self._DomainGroup = None
        self._PageSize = None
        self._PageNum = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGroup(self):
        return self._DomainGroup

    @DomainGroup.setter
    def DomainGroup(self, DomainGroup):
        self._DomainGroup = DomainGroup

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._StreamName = params.get("StreamName")
        self._Domain = params.get("Domain")
        self._DomainGroup = params.get("DomainGroup")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimeShiftStreamListResponse(AbstractModel):
    """DescribeTimeShiftStreamList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalSize: 时间段内所有的数据量。
        :type TotalSize: int
        :param _StreamList: 流列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamList: list of TimeShiftStreamInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalSize = None
        self._StreamList = None
        self._RequestId = None

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def StreamList(self):
        return self._StreamList

    @StreamList.setter
    def StreamList(self, StreamList):
        self._StreamList = StreamList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalSize = params.get("TotalSize")
        if params.get("StreamList") is not None:
            self._StreamList = []
            for item in params.get("StreamList"):
                obj = TimeShiftStreamInfo()
                obj._deserialize(item)
                self._StreamList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopClientIpSumInfoListRequest(AbstractModel):
    """DescribeTopClientIpSumInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS
时间跨度在[0,4小时]，支持最近1天数据查询。
        :type EndTime: str
        :param _PlayDomains: 播放域名，默认为不填，表示求总体数据。
        :type PlayDomains: list of str
        :param _PageNum: 页号，范围是[1,1000]，默认值是1。
        :type PageNum: int
        :param _PageSize: 每页个数，范围是[1,1000]，默认值是20。
        :type PageSize: int
        :param _OrderParam: 排序指标，可选值包括TotalRequest（默认值），FailedRequest,TotalFlux。
        :type OrderParam: str
        :param _MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        :param _OutLanguage: 输出字段使用的语言，可选值：Chinese（默认值），English；目前国家，省份和运营商支持多语言。
        :type OutLanguage: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PlayDomains = None
        self._PageNum = None
        self._PageSize = None
        self._OrderParam = None
        self._MainlandOrOversea = None
        self._OutLanguage = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def OrderParam(self):
        return self._OrderParam

    @OrderParam.setter
    def OrderParam(self, OrderParam):
        self._OrderParam = OrderParam

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def OutLanguage(self):
        return self._OutLanguage

    @OutLanguage.setter
    def OutLanguage(self, OutLanguage):
        self._OutLanguage = OutLanguage


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayDomains = params.get("PlayDomains")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._OrderParam = params.get("OrderParam")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopClientIpSumInfoListResponse(AbstractModel):
    """DescribeTopClientIpSumInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 页号，范围是[1,1000]，默认值是1。
        :type PageNum: int
        :param _PageSize: 每页个数，范围是[1,1000]，默认值是20。
        :type PageSize: int
        :param _OrderParam: 排序指标，可选值包括”TotalRequest”，”FailedRequest”,“TotalFlux”。
        :type OrderParam: str
        :param _TotalNum: 记录总数。
        :type TotalNum: int
        :param _TotalPage: 记录总页数。
        :type TotalPage: int
        :param _DataInfoList: 数据内容。
        :type DataInfoList: list of ClientIpPlaySumInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PageNum = None
        self._PageSize = None
        self._OrderParam = None
        self._TotalNum = None
        self._TotalPage = None
        self._DataInfoList = None
        self._RequestId = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def OrderParam(self):
        return self._OrderParam

    @OrderParam.setter
    def OrderParam(self, OrderParam):
        self._OrderParam = OrderParam

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._OrderParam = params.get("OrderParam")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ClientIpPlaySumInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTranscodeTaskNumRequest(AbstractModel):
    """DescribeTranscodeTaskNum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间，格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间，格式：yyyy-mm-dd HH:MM:SS。
        :type EndTime: str
        :param _PushDomains: 推流域名列表，不填表示总体数据。
        :type PushDomains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PushDomains = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PushDomains(self):
        return self._PushDomains

    @PushDomains.setter
    def PushDomains(self, PushDomains):
        self._PushDomains = PushDomains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PushDomains = params.get("PushDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeTaskNumResponse(AbstractModel):
    """DescribeTranscodeTaskNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 任务数列表。
        :type DataInfoList: list of TranscodeTaskNum
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TranscodeTaskNum()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUploadStreamNumsRequest(AbstractModel):
    """DescribeUploadStreamNums请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
        :type StartTime: str
        :param _EndTime: 结束时间点，接口查询支持两种时间格式：
1）YYYY-MM-DDThh:mm:ssZ：UTC时间格式，详见IOS日期格式说明文档: https://cloud.tencent.com/document/product/266/11732#I
2）YYYY-MM-DD hh:mm:ss：使用此格式时，默认代表北京时间。
起始和结束时间跨度不支持超过31天。支持最近31天的数据查询
        :type EndTime: str
        :param _Domains: 直播域名，若不填，表示总体数据。
        :type Domains: list of str
        :param _Granularity: 数据粒度，支持如下粒度：
5：5分钟粒度，（跨度不支持超过1天），
1440：天粒度（跨度不支持超过一个月）。
默认值：5。
        :type Granularity: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Domains = None
        self._Granularity = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domains = params.get("Domains")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadStreamNumsResponse(AbstractModel):
    """DescribeUploadStreamNums返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 明细数据信息
        :type DataInfoList: list of ConcurrentRecordStreamNum
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ConcurrentRecordStreamNum()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVisitTopSumInfoListRequest(AbstractModel):
    """DescribeVisitTopSumInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param _EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS
时间跨度在(0,4小时]，支持最近1天数据查询。
        :type EndTime: str
        :param _TopIndex: 峰值指标，可选值包括”Domain”，”StreamId”。
        :type TopIndex: str
        :param _PlayDomains: 播放域名，默认为不填，表示求总体数据。
        :type PlayDomains: list of str
        :param _PageNum: 页号，
范围是[1,1000]，
默认值是1。
        :type PageNum: int
        :param _PageSize: 每页个数，范围是[1,1000]，
默认值是20。
        :type PageSize: int
        :param _OrderParam: 排序指标，可选值包括” AvgFluxPerSecond”，”TotalRequest”（默认）,“TotalFlux”。
        :type OrderParam: str
        """
        self._StartTime = None
        self._EndTime = None
        self._TopIndex = None
        self._PlayDomains = None
        self._PageNum = None
        self._PageSize = None
        self._OrderParam = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TopIndex(self):
        return self._TopIndex

    @TopIndex.setter
    def TopIndex(self, TopIndex):
        self._TopIndex = TopIndex

    @property
    def PlayDomains(self):
        return self._PlayDomains

    @PlayDomains.setter
    def PlayDomains(self, PlayDomains):
        self._PlayDomains = PlayDomains

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def OrderParam(self):
        return self._OrderParam

    @OrderParam.setter
    def OrderParam(self, OrderParam):
        self._OrderParam = OrderParam


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TopIndex = params.get("TopIndex")
        self._PlayDomains = params.get("PlayDomains")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._OrderParam = params.get("OrderParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVisitTopSumInfoListResponse(AbstractModel):
    """DescribeVisitTopSumInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 页号，
范围是[1,1000]，
默认值是1。
        :type PageNum: int
        :param _PageSize: 每页个数，范围是[1,1000]，
默认值是20。
        :type PageSize: int
        :param _TopIndex: 峰值指标，可选值包括”Domain”，”StreamId”。
        :type TopIndex: str
        :param _OrderParam: 排序指标，可选值包括” AvgFluxPerSecond”(按每秒平均流量排序)，”TotalRequest”（默认，按总请求数排序）,“TotalFlux”（按总流量排序）。
        :type OrderParam: str
        :param _TotalNum: 记录总数。
        :type TotalNum: int
        :param _TotalPage: 记录总页数。
        :type TotalPage: int
        :param _DataInfoList: 数据内容。
        :type DataInfoList: list of PlaySumStatInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PageNum = None
        self._PageSize = None
        self._TopIndex = None
        self._OrderParam = None
        self._TotalNum = None
        self._TotalPage = None
        self._DataInfoList = None
        self._RequestId = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TopIndex(self):
        return self._TopIndex

    @TopIndex.setter
    def TopIndex(self, TopIndex):
        self._TopIndex = TopIndex

    @property
    def OrderParam(self):
        return self._OrderParam

    @OrderParam.setter
    def OrderParam(self, OrderParam):
        self._OrderParam = OrderParam

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def DataInfoList(self):
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TopIndex = params.get("TopIndex")
        self._OrderParam = params.get("OrderParam")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlaySumStatInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DiagnoseResult(AbstractModel):
    """媒体诊断结果，包含断流信息、低帧率信息等

    """

    def __init__(self):
        r"""
        :param _StreamBrokenResults: 断流信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamBrokenResults: list of str
        :param _LowFrameRateResults: 低帧率信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LowFrameRateResults: list of str
        :param _StreamFormatResults: 流格式诊断信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamFormatResults: list of str
        """
        self._StreamBrokenResults = None
        self._LowFrameRateResults = None
        self._StreamFormatResults = None

    @property
    def StreamBrokenResults(self):
        return self._StreamBrokenResults

    @StreamBrokenResults.setter
    def StreamBrokenResults(self, StreamBrokenResults):
        self._StreamBrokenResults = StreamBrokenResults

    @property
    def LowFrameRateResults(self):
        return self._LowFrameRateResults

    @LowFrameRateResults.setter
    def LowFrameRateResults(self, LowFrameRateResults):
        self._LowFrameRateResults = LowFrameRateResults

    @property
    def StreamFormatResults(self):
        return self._StreamFormatResults

    @StreamFormatResults.setter
    def StreamFormatResults(self, StreamFormatResults):
        self._StreamFormatResults = StreamFormatResults


    def _deserialize(self, params):
        self._StreamBrokenResults = params.get("StreamBrokenResults")
        self._LowFrameRateResults = params.get("LowFrameRateResults")
        self._StreamFormatResults = params.get("StreamFormatResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainCertInfo(AbstractModel):
    """域名证书信息

    """

    def __init__(self):
        r"""
        :param _CertId: 证书Id。
        :type CertId: int
        :param _CertName: 证书名称。
        :type CertName: str
        :param _Description: 描述信息。
        :type Description: str
        :param _CreateTime: 创建时间，UTC格式。
注：此字段为北京时间（UTC+8时区）。
        :type CreateTime: str
        :param _HttpsCrt: 证书内容。
        :type HttpsCrt: str
        :param _CertType: 证书类型。
0：用户添加证书，
1：腾讯云托管证书。
        :type CertType: int
        :param _CertExpireTime: 证书过期时间，UTC格式。
注：此字段为北京时间（UTC+8时区）。
        :type CertExpireTime: str
        :param _DomainName: 使用此证书的域名名称。
        :type DomainName: str
        :param _Status: 证书状态。
        :type Status: int
        :param _CertDomains: 证书本身标识的域名列表。
比如: ["*.x.com"]
注意：此字段可能返回 null，表示取不到有效值。
        :type CertDomains: list of str
        :param _CloudCertId: 腾讯云ssl的证书Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudCertId: str
        """
        self._CertId = None
        self._CertName = None
        self._Description = None
        self._CreateTime = None
        self._HttpsCrt = None
        self._CertType = None
        self._CertExpireTime = None
        self._DomainName = None
        self._Status = None
        self._CertDomains = None
        self._CloudCertId = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def HttpsCrt(self):
        return self._HttpsCrt

    @HttpsCrt.setter
    def HttpsCrt(self, HttpsCrt):
        self._HttpsCrt = HttpsCrt

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def CertExpireTime(self):
        return self._CertExpireTime

    @CertExpireTime.setter
    def CertExpireTime(self, CertExpireTime):
        self._CertExpireTime = CertExpireTime

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertDomains(self):
        return self._CertDomains

    @CertDomains.setter
    def CertDomains(self, CertDomains):
        self._CertDomains = CertDomains

    @property
    def CloudCertId(self):
        return self._CloudCertId

    @CloudCertId.setter
    def CloudCertId(self, CloudCertId):
        self._CloudCertId = CloudCertId


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._HttpsCrt = params.get("HttpsCrt")
        self._CertType = params.get("CertType")
        self._CertExpireTime = params.get("CertExpireTime")
        self._DomainName = params.get("DomainName")
        self._Status = params.get("Status")
        self._CertDomains = params.get("CertDomains")
        self._CloudCertId = params.get("CloudCertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainDetailInfo(AbstractModel):
    """每个域名的统计信息。

    """

    def __init__(self):
        r"""
        :param _MainlandOrOversea: 国内还是国外:
Mainland: 表示国内数据。
Oversea: 表示国外数据。
        :type MainlandOrOversea: str
        :param _Bandwidth: 带宽，单位: Mbps。
        :type Bandwidth: float
        :param _Flux: 流量，单位: MB。
        :type Flux: float
        :param _Online: 人数。
        :type Online: int
        :param _Request: 请求数。
        :type Request: int
        """
        self._MainlandOrOversea = None
        self._Bandwidth = None
        self._Flux = None
        self._Online = None
        self._Request = None

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Flux(self):
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def Request(self):
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request


    def _deserialize(self, params):
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        self._Bandwidth = params.get("Bandwidth")
        self._Flux = params.get("Flux")
        self._Online = params.get("Online")
        self._Request = params.get("Request")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainInfo(AbstractModel):
    """直播域名信息

    """

    def __init__(self):
        r"""
        :param _Name: 直播域名。
        :type Name: str
        :param _Type: 域名类型:
0: 推流。
1: 播放。
        :type Type: int
        :param _Status: 域名状态:
0: 停用。
1: 启用。
        :type Status: int
        :param _CreateTime: 添加时间。
注：此字段为北京时间（UTC+8时区）。
        :type CreateTime: str
        :param _BCName: 是否有 CName 到固定规则域名:
0: 否。
1: 是。
        :type BCName: int
        :param _TargetDomain: cname 对应的域名。
        :type TargetDomain: str
        :param _PlayType: 播放区域，只在 Type=1 时该参数有意义。
1: 国内。
2: 全球。
3: 海外。
        :type PlayType: int
        :param _IsDelayLive: 是否慢直播:
0: 普通直播。
1: 慢直播。
        :type IsDelayLive: int
        :param _CurrentCName: 当前客户使用的 cname 信息。
        :type CurrentCName: str
        :param _RentTag: 失效参数，可忽略。
        :type RentTag: int
        :param _RentExpireTime: 失效参数，可忽略。
注：此字段为北京时间（UTC+8时区）。
        :type RentExpireTime: str
        :param _IsMiniProgramLive: 0: 标准直播。
1: 小程序直播。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMiniProgramLive: int
        """
        self._Name = None
        self._Type = None
        self._Status = None
        self._CreateTime = None
        self._BCName = None
        self._TargetDomain = None
        self._PlayType = None
        self._IsDelayLive = None
        self._CurrentCName = None
        self._RentTag = None
        self._RentExpireTime = None
        self._IsMiniProgramLive = None

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BCName(self):
        return self._BCName

    @BCName.setter
    def BCName(self, BCName):
        self._BCName = BCName

    @property
    def TargetDomain(self):
        return self._TargetDomain

    @TargetDomain.setter
    def TargetDomain(self, TargetDomain):
        self._TargetDomain = TargetDomain

    @property
    def PlayType(self):
        return self._PlayType

    @PlayType.setter
    def PlayType(self, PlayType):
        self._PlayType = PlayType

    @property
    def IsDelayLive(self):
        return self._IsDelayLive

    @IsDelayLive.setter
    def IsDelayLive(self, IsDelayLive):
        self._IsDelayLive = IsDelayLive

    @property
    def CurrentCName(self):
        return self._CurrentCName

    @CurrentCName.setter
    def CurrentCName(self, CurrentCName):
        self._CurrentCName = CurrentCName

    @property
    def RentTag(self):
        return self._RentTag

    @RentTag.setter
    def RentTag(self, RentTag):
        self._RentTag = RentTag

    @property
    def RentExpireTime(self):
        return self._RentExpireTime

    @RentExpireTime.setter
    def RentExpireTime(self, RentExpireTime):
        self._RentExpireTime = RentExpireTime

    @property
    def IsMiniProgramLive(self):
        return self._IsMiniProgramLive

    @IsMiniProgramLive.setter
    def IsMiniProgramLive(self, IsMiniProgramLive):
        self._IsMiniProgramLive = IsMiniProgramLive


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._BCName = params.get("BCName")
        self._TargetDomain = params.get("TargetDomain")
        self._PlayType = params.get("PlayType")
        self._IsDelayLive = params.get("IsDelayLive")
        self._CurrentCName = params.get("CurrentCName")
        self._RentTag = params.get("RentTag")
        self._RentExpireTime = params.get("RentExpireTime")
        self._IsMiniProgramLive = params.get("IsMiniProgramLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainInfoList(AbstractModel):
    """多个域名信息列表

    """

    def __init__(self):
        r"""
        :param _Domain: 域名。
        :type Domain: str
        :param _DetailInfoList: 明细信息。
        :type DetailInfoList: list of DomainDetailInfo
        """
        self._Domain = None
        self._DetailInfoList = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DetailInfoList(self):
        return self._DetailInfoList

    @DetailInfoList.setter
    def DetailInfoList(self, DetailInfoList):
        self._DetailInfoList = DetailInfoList


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("DetailInfoList") is not None:
            self._DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self._DetailInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropLiveStreamRequest(AbstractModel):
    """DropLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _DomainName: 您的推流域名。
        :type DomainName: str
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        """
        self._StreamName = None
        self._DomainName = None
        self._AppName = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropLiveStreamResponse(AbstractModel):
    """DropLiveStream返回参数结构体

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


class EnableLiveDomainRequest(AbstractModel):
    """EnableLiveDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 待启用的直播域名。
        :type DomainName: str
        """
        self._DomainName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableLiveDomainResponse(AbstractModel):
    """EnableLiveDomain返回参数结构体

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


class FlvSpecialParam(AbstractModel):
    """flv格式特殊配置

    """

    def __init__(self):
        r"""
        :param _UploadInRecording: 是否开启边录边传，仅flv格式有效。
        :type UploadInRecording: bool
        """
        self._UploadInRecording = None

    @property
    def UploadInRecording(self):
        return self._UploadInRecording

    @UploadInRecording.setter
    def UploadInRecording(self, UploadInRecording):
        self._UploadInRecording = UploadInRecording


    def _deserialize(self, params):
        self._UploadInRecording = params.get("UploadInRecording")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidLiveDomainRequest(AbstractModel):
    """ForbidLiveDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 待停用的直播域名。
        :type DomainName: str
        """
        self._DomainName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidLiveDomainResponse(AbstractModel):
    """ForbidLiveDomain返回参数结构体

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


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param _DomainName: 您的推流域名。
        :type DomainName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _ResumeTime: 恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：
1. 默认禁推7天，且最长支持禁推90天。
2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ResumeTime: str
        :param _Reason: 禁推原因。
注明：请务必填写禁推原因，防止误操作。
长度限制：2048字节。
        :type Reason: str
        """
        self._AppName = None
        self._DomainName = None
        self._StreamName = None
        self._ResumeTime = None
        self._Reason = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def ResumeTime(self):
        return self._ResumeTime

    @ResumeTime.setter
    def ResumeTime(self, ResumeTime):
        self._ResumeTime = ResumeTime

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamName = params.get("StreamName")
        self._ResumeTime = params.get("ResumeTime")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidLiveStreamResponse(AbstractModel):
    """ForbidLiveStream返回参数结构体

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


class ForbidStreamInfo(AbstractModel):
    """禁推流列表

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _CreateTime: 创建时间。
注：此字段为北京时间（UTC+8时区）。
        :type CreateTime: str
        :param _ExpireTime: 禁推过期时间。
注：此字段为北京时间（UTC+8时区）。
        :type ExpireTime: str
        :param _AppName: 推流路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param _DomainName: 推流域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainName: str
        """
        self._StreamName = None
        self._CreateTime = None
        self._ExpireTime = None
        self._AppName = None
        self._DomainName = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupProIspDataInfo(AbstractModel):
    """某省份某运营商在某段时间内的带宽，流量，请求数和并发数

    """

    def __init__(self):
        r"""
        :param _ProvinceName: 省份。
        :type ProvinceName: str
        :param _IspName: 运营商。
        :type IspName: str
        :param _DetailInfoList: 分钟维度的明细数据。
        :type DetailInfoList: list of CdnPlayStatData
        """
        self._ProvinceName = None
        self._IspName = None
        self._DetailInfoList = None

    @property
    def ProvinceName(self):
        return self._ProvinceName

    @ProvinceName.setter
    def ProvinceName(self, ProvinceName):
        self._ProvinceName = ProvinceName

    @property
    def IspName(self):
        return self._IspName

    @IspName.setter
    def IspName(self, IspName):
        self._IspName = IspName

    @property
    def DetailInfoList(self):
        return self._DetailInfoList

    @DetailInfoList.setter
    def DetailInfoList(self, DetailInfoList):
        self._DetailInfoList = DetailInfoList


    def _deserialize(self, params):
        self._ProvinceName = params.get("ProvinceName")
        self._IspName = params.get("IspName")
        if params.get("DetailInfoList") is not None:
            self._DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = CdnPlayStatData()
                obj._deserialize(item)
                self._DetailInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HlsSpecialParam(AbstractModel):
    """HLS专属录制参数

    """

    def __init__(self):
        r"""
        :param _FlowContinueDuration: HLS续流超时时间。
取值范围[0，1800]。
        :type FlowContinueDuration: int
        """
        self._FlowContinueDuration = None

    @property
    def FlowContinueDuration(self):
        return self._FlowContinueDuration

    @FlowContinueDuration.setter
    def FlowContinueDuration(self, FlowContinueDuration):
        self._FlowContinueDuration = FlowContinueDuration


    def _deserialize(self, params):
        self._FlowContinueDuration = params.get("FlowContinueDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpCodeInfo(AbstractModel):
    """HTTP返回码和统计数据

    """

    def __init__(self):
        r"""
        :param _HttpCode: HTTP协议返回码。
例："2xx", "3xx", "4xx", "5xx"。
        :type HttpCode: str
        :param _ValueList: 统计信息，对于无数据的时间点，会补0。
        :type ValueList: list of HttpCodeValue
        """
        self._HttpCode = None
        self._ValueList = None

    @property
    def HttpCode(self):
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def ValueList(self):
        return self._ValueList

    @ValueList.setter
    def ValueList(self, ValueList):
        self._ValueList = ValueList


    def _deserialize(self, params):
        self._HttpCode = params.get("HttpCode")
        if params.get("ValueList") is not None:
            self._ValueList = []
            for item in params.get("ValueList"):
                obj = HttpCodeValue()
                obj._deserialize(item)
                self._ValueList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpCodeValue(AbstractModel):
    """HTTP返回码数据信息

    """

    def __init__(self):
        r"""
        :param _Time: 时间，格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param _Numbers: 次数。
        :type Numbers: int
        :param _Percentage: 占比。
        :type Percentage: float
        """
        self._Time = None
        self._Numbers = None
        self._Percentage = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Numbers(self):
        return self._Numbers

    @Numbers.setter
    def Numbers(self, Numbers):
        self._Numbers = Numbers

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Numbers = params.get("Numbers")
        self._Percentage = params.get("Percentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpStatusData(AbstractModel):
    """播放错误码信息

    """

    def __init__(self):
        r"""
        :param _Time: 数据时间点，
格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param _HttpStatusInfoList: 播放状态码详细信息。
        :type HttpStatusInfoList: list of HttpStatusInfo
        """
        self._Time = None
        self._HttpStatusInfoList = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def HttpStatusInfoList(self):
        return self._HttpStatusInfoList

    @HttpStatusInfoList.setter
    def HttpStatusInfoList(self, HttpStatusInfoList):
        self._HttpStatusInfoList = HttpStatusInfoList


    def _deserialize(self, params):
        self._Time = params.get("Time")
        if params.get("HttpStatusInfoList") is not None:
            self._HttpStatusInfoList = []
            for item in params.get("HttpStatusInfoList"):
                obj = HttpStatusInfo()
                obj._deserialize(item)
                self._HttpStatusInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpStatusInfo(AbstractModel):
    """播放错误码信息

    """

    def __init__(self):
        r"""
        :param _HttpStatus: 播放HTTP状态码。
        :type HttpStatus: str
        :param _Num: 个数。
        :type Num: int
        """
        self._HttpStatus = None
        self._Num = None

    @property
    def HttpStatus(self):
        return self._HttpStatus

    @HttpStatus.setter
    def HttpStatus(self, HttpStatus):
        self._HttpStatus = HttpStatus

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._HttpStatus = params.get("HttpStatus")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveCertDomainInfo(AbstractModel):
    """用作批量绑定域名和证书。

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名。
        :type DomainName: str
        :param _Status: 是否启用域名的https规则。
1：启用
0：禁用
-1：保持不变
        :type Status: int
        """
        self._DomainName = None
        self._Status = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveDomainCertBindings(AbstractModel):
    """DescribeLiveDomainCertBindings, DescribeLiveDomainCertBindingsGray接口返回的域名证书信息

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名。
        :type DomainName: str
        :param _CertificateAlias: 证书备注。与CertName同义。
        :type CertificateAlias: str
        :param _CertType: 证书类型。
0：自有证书
1：腾讯云ssl托管证书
        :type CertType: int
        :param _Status: https状态。
1：已开启。
0：已关闭。
        :type Status: int
        :param _CertExpireTime: 证书过期时间。
注：此字段为北京时间（UTC+8时区）。
        :type CertExpireTime: str
        :param _CertId: 证书Id。
        :type CertId: int
        :param _CloudCertId: 腾讯云ssl的证书Id。
        :type CloudCertId: str
        :param _UpdateTime: 规则最后更新时间。
注：此字段为北京时间（UTC+8时区）。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._DomainName = None
        self._CertificateAlias = None
        self._CertType = None
        self._Status = None
        self._CertExpireTime = None
        self._CertId = None
        self._CloudCertId = None
        self._UpdateTime = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertExpireTime(self):
        return self._CertExpireTime

    @CertExpireTime.setter
    def CertExpireTime(self, CertExpireTime):
        self._CertExpireTime = CertExpireTime

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CloudCertId(self):
        return self._CloudCertId

    @CloudCertId.setter
    def CloudCertId(self, CloudCertId):
        self._CloudCertId = CloudCertId

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._CertificateAlias = params.get("CertificateAlias")
        self._CertType = params.get("CertType")
        self._Status = params.get("Status")
        self._CertExpireTime = params.get("CertExpireTime")
        self._CertId = params.get("CertId")
        self._CloudCertId = params.get("CloudCertId")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivePackageInfo(AbstractModel):
    """直播包信息。

    """

    def __init__(self):
        r"""
        :param _Id: 包 ID。
        :type Id: str
        :param _Total: 总量。
注意：当为流量包时单位为字节。
当为转码包时单位为分钟。
        :type Total: int
        :param _Used: 使用量。
注意：当为流量包时单位为字节。
当为转码包时单位为分钟。
当为连麦包时单位为小时。
        :type Used: int
        :param _Left: 剩余量。
注意：当为流量包时单位为字节。
当为转码包时单位为分钟。
当为连麦包时单位为小时。
        :type Left: int
        :param _BuyTime: 购买时间。
注：此字段为北京时间（UTC+8时区）。
        :type BuyTime: str
        :param _ExpireTime: 过期时间。
注：此字段为北京时间（UTC+8时区）。
        :type ExpireTime: str
        :param _Type: 包类型，可选值:
0: 流量包。
1: 普通转码包。
2: 极速高清包。
3: 连麦包。
        :type Type: int
        :param _Status: 包状态，可选值:
0: 未使用。
1: 使用中。
2: 已过期。
3: 已冻结。
4: 已耗尽。
5: 已退款
        :type Status: int
        :param _WillRenew: 是否自动续购。
注意：此字段可能返回 null，表示取不到有效值。
        :type WillRenew: int
        :param _RenewalResult: 续购状态。
1 ：续购成功。
0 ：尚未续购。
<0  : 续购失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewalResult: int
        """
        self._Id = None
        self._Total = None
        self._Used = None
        self._Left = None
        self._BuyTime = None
        self._ExpireTime = None
        self._Type = None
        self._Status = None
        self._WillRenew = None
        self._RenewalResult = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Left(self):
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def BuyTime(self):
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WillRenew(self):
        return self._WillRenew

    @WillRenew.setter
    def WillRenew(self, WillRenew):
        self._WillRenew = WillRenew

    @property
    def RenewalResult(self):
        return self._RenewalResult

    @RenewalResult.setter
    def RenewalResult(self, RenewalResult):
        self._RenewalResult = RenewalResult


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._Left = params.get("Left")
        self._BuyTime = params.get("BuyTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._WillRenew = params.get("WillRenew")
        self._RenewalResult = params.get("RenewalResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamMonitorInfo(AbstractModel):
    """直播监播任务信息。

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监播任务ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorId: str
        :param _MonitorName: 监播任务名称。128字节以内。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorName: str
        :param _OutputInfo: 监播任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputInfo: :class:`tencentcloud.live.v20180801.models.LiveStreamMonitorOutputInfo`
        :param _InputList: 待监播的输入流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputList: list of LiveStreamMonitorInputInfo
        :param _Status: 监播任务状态。
0： 代表空闲
1： 代表监播中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StartTime: 上一次的启动时间，unix时间戳。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _StopTime: 上一次的停止时间，unix时间戳。
注意：此字段可能返回 null，表示取不到有效值。
        :type StopTime: int
        :param _CreateTime: 监播任务创建时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _UpdateTime: 监播任务更新时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _NotifyPolicy: 监播事件通知策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyPolicy: :class:`tencentcloud.live.v20180801.models.LiveStreamMonitorNotifyPolicy`
        :param _AudibleInputIndexList: 输出音频的输入Index列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudibleInputIndexList: list of int non-negative
        :param _AiAsrInputIndexList: 开启智能语音识别的输入Index列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AiAsrInputIndexList: list of int non-negative
        :param _CheckStreamBroken: 是否开启断流检测
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckStreamBroken: int
        :param _CheckStreamLowFrameRate: 是否开启低帧率检测
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckStreamLowFrameRate: int
        :param _AsrLanguage: 智能语音识别语种：
0 关闭 1 中文 2 英文 3日文 4 韩文
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrLanguage: int
        :param _OcrLanguage: 智能文字识别语种：
0 关闭 1 中、英文
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrLanguage: int
        :param _AiOcrInputIndexList: 开启智能文字识别的输入Index列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AiOcrInputIndexList: list of int non-negative
        :param _AllowMonitorReport: 是否存储监播事件到监播报告，以及是否允许查询监播报告
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowMonitorReport: int
        :param _AiFormatDiagnose: 是否开启格式诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AiFormatDiagnose: int
        """
        self._MonitorId = None
        self._MonitorName = None
        self._OutputInfo = None
        self._InputList = None
        self._Status = None
        self._StartTime = None
        self._StopTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._NotifyPolicy = None
        self._AudibleInputIndexList = None
        self._AiAsrInputIndexList = None
        self._CheckStreamBroken = None
        self._CheckStreamLowFrameRate = None
        self._AsrLanguage = None
        self._OcrLanguage = None
        self._AiOcrInputIndexList = None
        self._AllowMonitorReport = None
        self._AiFormatDiagnose = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def MonitorName(self):
        return self._MonitorName

    @MonitorName.setter
    def MonitorName(self, MonitorName):
        self._MonitorName = MonitorName

    @property
    def OutputInfo(self):
        return self._OutputInfo

    @OutputInfo.setter
    def OutputInfo(self, OutputInfo):
        self._OutputInfo = OutputInfo

    @property
    def InputList(self):
        return self._InputList

    @InputList.setter
    def InputList(self, InputList):
        self._InputList = InputList

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StopTime(self):
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def NotifyPolicy(self):
        return self._NotifyPolicy

    @NotifyPolicy.setter
    def NotifyPolicy(self, NotifyPolicy):
        self._NotifyPolicy = NotifyPolicy

    @property
    def AudibleInputIndexList(self):
        return self._AudibleInputIndexList

    @AudibleInputIndexList.setter
    def AudibleInputIndexList(self, AudibleInputIndexList):
        self._AudibleInputIndexList = AudibleInputIndexList

    @property
    def AiAsrInputIndexList(self):
        return self._AiAsrInputIndexList

    @AiAsrInputIndexList.setter
    def AiAsrInputIndexList(self, AiAsrInputIndexList):
        self._AiAsrInputIndexList = AiAsrInputIndexList

    @property
    def CheckStreamBroken(self):
        return self._CheckStreamBroken

    @CheckStreamBroken.setter
    def CheckStreamBroken(self, CheckStreamBroken):
        self._CheckStreamBroken = CheckStreamBroken

    @property
    def CheckStreamLowFrameRate(self):
        return self._CheckStreamLowFrameRate

    @CheckStreamLowFrameRate.setter
    def CheckStreamLowFrameRate(self, CheckStreamLowFrameRate):
        self._CheckStreamLowFrameRate = CheckStreamLowFrameRate

    @property
    def AsrLanguage(self):
        return self._AsrLanguage

    @AsrLanguage.setter
    def AsrLanguage(self, AsrLanguage):
        self._AsrLanguage = AsrLanguage

    @property
    def OcrLanguage(self):
        return self._OcrLanguage

    @OcrLanguage.setter
    def OcrLanguage(self, OcrLanguage):
        self._OcrLanguage = OcrLanguage

    @property
    def AiOcrInputIndexList(self):
        return self._AiOcrInputIndexList

    @AiOcrInputIndexList.setter
    def AiOcrInputIndexList(self, AiOcrInputIndexList):
        self._AiOcrInputIndexList = AiOcrInputIndexList

    @property
    def AllowMonitorReport(self):
        return self._AllowMonitorReport

    @AllowMonitorReport.setter
    def AllowMonitorReport(self, AllowMonitorReport):
        self._AllowMonitorReport = AllowMonitorReport

    @property
    def AiFormatDiagnose(self):
        return self._AiFormatDiagnose

    @AiFormatDiagnose.setter
    def AiFormatDiagnose(self, AiFormatDiagnose):
        self._AiFormatDiagnose = AiFormatDiagnose


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._MonitorName = params.get("MonitorName")
        if params.get("OutputInfo") is not None:
            self._OutputInfo = LiveStreamMonitorOutputInfo()
            self._OutputInfo._deserialize(params.get("OutputInfo"))
        if params.get("InputList") is not None:
            self._InputList = []
            for item in params.get("InputList"):
                obj = LiveStreamMonitorInputInfo()
                obj._deserialize(item)
                self._InputList.append(obj)
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._StopTime = params.get("StopTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("NotifyPolicy") is not None:
            self._NotifyPolicy = LiveStreamMonitorNotifyPolicy()
            self._NotifyPolicy._deserialize(params.get("NotifyPolicy"))
        self._AudibleInputIndexList = params.get("AudibleInputIndexList")
        self._AiAsrInputIndexList = params.get("AiAsrInputIndexList")
        self._CheckStreamBroken = params.get("CheckStreamBroken")
        self._CheckStreamLowFrameRate = params.get("CheckStreamLowFrameRate")
        self._AsrLanguage = params.get("AsrLanguage")
        self._OcrLanguage = params.get("OcrLanguage")
        self._AiOcrInputIndexList = params.get("AiOcrInputIndexList")
        self._AllowMonitorReport = params.get("AllowMonitorReport")
        self._AiFormatDiagnose = params.get("AiFormatDiagnose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamMonitorInputInfo(AbstractModel):
    """直播监播功能输入流信息

    """

    def __init__(self):
        r"""
        :param _InputStreamName: 待监播的输入流名称。256字节以内，只允许包含字母、数字、‘-’，‘_’，'.'字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputStreamName: str
        :param _InputDomain: 待监播的输入流推流域名。128字节以内，只允许填处于启用状态的推流域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputDomain: str
        :param _InputApp: 待监播的输入流推流路径。32字节以内，只允许包含字母、数字、‘-’，‘_’，'.'字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputApp: str
        :param _InputUrl: 待监播的输入流推流url。一般场景下，无需该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputUrl: str
        :param _Description: 描述。256字节以内。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._InputStreamName = None
        self._InputDomain = None
        self._InputApp = None
        self._InputUrl = None
        self._Description = None

    @property
    def InputStreamName(self):
        return self._InputStreamName

    @InputStreamName.setter
    def InputStreamName(self, InputStreamName):
        self._InputStreamName = InputStreamName

    @property
    def InputDomain(self):
        return self._InputDomain

    @InputDomain.setter
    def InputDomain(self, InputDomain):
        self._InputDomain = InputDomain

    @property
    def InputApp(self):
        return self._InputApp

    @InputApp.setter
    def InputApp(self, InputApp):
        self._InputApp = InputApp

    @property
    def InputUrl(self):
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InputStreamName = params.get("InputStreamName")
        self._InputDomain = params.get("InputDomain")
        self._InputApp = params.get("InputApp")
        self._InputUrl = params.get("InputUrl")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamMonitorNotifyPolicy(AbstractModel):
    """直播流监播通知策略

    """

    def __init__(self):
        r"""
        :param _NotifyPolicyType: 通知策略类型：范围[0,1]
0:代表不使用任何通知策略
1:代表使用全局回调策略，所有事件通知到CallbackUrl。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyPolicyType: int
        :param _CallbackUrl: 回调URL：长度[0,512]
只支持http和https类型的url。
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        """
        self._NotifyPolicyType = None
        self._CallbackUrl = None

    @property
    def NotifyPolicyType(self):
        return self._NotifyPolicyType

    @NotifyPolicyType.setter
    def NotifyPolicyType(self, NotifyPolicyType):
        self._NotifyPolicyType = NotifyPolicyType

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._NotifyPolicyType = params.get("NotifyPolicyType")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamMonitorOutputInfo(AbstractModel):
    """直播流监播输出流信息

    """

    def __init__(self):
        r"""
        :param _OutputStreamWidth: 监播任务输出流宽度像素。范围[1,1920]。建议至少大于100像素。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStreamWidth: int
        :param _OutputStreamHeight: 监播任务输出流长度像素。范围[1,1080]，建议至少大于100像素。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStreamHeight: int
        :param _OutputStreamName: 监播任务输出流名称。
不填时，系统会自动生成。
256字节以内，只允许包含字母、数字、‘-’，‘_’，'.'字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStreamName: str
        :param _OutputDomain: 监播任务播放域名。128字节以内，只允许填处于启用状态的播放域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputDomain: str
        :param _OutputApp: 监播任务播放路径。32字节以内，只允许包含字母、数字、‘-’，‘_’，'.'字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputApp: str
        """
        self._OutputStreamWidth = None
        self._OutputStreamHeight = None
        self._OutputStreamName = None
        self._OutputDomain = None
        self._OutputApp = None

    @property
    def OutputStreamWidth(self):
        return self._OutputStreamWidth

    @OutputStreamWidth.setter
    def OutputStreamWidth(self, OutputStreamWidth):
        self._OutputStreamWidth = OutputStreamWidth

    @property
    def OutputStreamHeight(self):
        return self._OutputStreamHeight

    @OutputStreamHeight.setter
    def OutputStreamHeight(self, OutputStreamHeight):
        self._OutputStreamHeight = OutputStreamHeight

    @property
    def OutputStreamName(self):
        return self._OutputStreamName

    @OutputStreamName.setter
    def OutputStreamName(self, OutputStreamName):
        self._OutputStreamName = OutputStreamName

    @property
    def OutputDomain(self):
        return self._OutputDomain

    @OutputDomain.setter
    def OutputDomain(self, OutputDomain):
        self._OutputDomain = OutputDomain

    @property
    def OutputApp(self):
        return self._OutputApp

    @OutputApp.setter
    def OutputApp(self, OutputApp):
        self._OutputApp = OutputApp


    def _deserialize(self, params):
        self._OutputStreamWidth = params.get("OutputStreamWidth")
        self._OutputStreamHeight = params.get("OutputStreamHeight")
        self._OutputStreamName = params.get("OutputStreamName")
        self._OutputDomain = params.get("OutputDomain")
        self._OutputApp = params.get("OutputApp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """日志url信息。

    """

    def __init__(self):
        r"""
        :param _LogName: 日志名称。
        :type LogName: str
        :param _LogUrl: 日志 URL。
        :type LogUrl: str
        :param _LogTime: 日志生成时间。
注：此字段为北京时间（UTC+8时区）。
        :type LogTime: str
        :param _FileSize: 文件大小。
        :type FileSize: int
        """
        self._LogName = None
        self._LogUrl = None
        self._LogTime = None
        self._FileSize = None

    @property
    def LogName(self):
        return self._LogName

    @LogName.setter
    def LogName(self, LogName):
        self._LogName = LogName

    @property
    def LogUrl(self):
        return self._LogUrl

    @LogUrl.setter
    def LogUrl(self, LogUrl):
        self._LogUrl = LogUrl

    @property
    def LogTime(self):
        return self._LogTime

    @LogTime.setter
    def LogTime(self, LogTime):
        self._LogTime = LogTime

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._LogName = params.get("LogName")
        self._LogUrl = params.get("LogUrl")
        self._LogTime = params.get("LogTime")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MPSResult(AbstractModel):
    """媒体处理结果，包含智能语音识别、智能文字识别结果

    """

    def __init__(self):
        r"""
        :param _AiAsrResults: 智能语音识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AiAsrResults: list of str
        :param _AiOcrResults: 智能文字识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AiOcrResults: list of str
        """
        self._AiAsrResults = None
        self._AiOcrResults = None

    @property
    def AiAsrResults(self):
        return self._AiAsrResults

    @AiAsrResults.setter
    def AiAsrResults(self, AiAsrResults):
        self._AiAsrResults = AiAsrResults

    @property
    def AiOcrResults(self):
        return self._AiOcrResults

    @AiOcrResults.setter
    def AiOcrResults(self, AiOcrResults):
        self._AiOcrResults = AiOcrResults


    def _deserialize(self, params):
        self._AiAsrResults = params.get("AiAsrResults")
        self._AiOcrResults = params.get("AiOcrResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveCallbackTemplateRequest(AbstractModel):
    """ModifyLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: DescribeLiveCallbackTemplates接口返回的模板 ID。
        :type TemplateId: int
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _Description: 描述信息。
        :type Description: str
        :param _StreamBeginNotifyUrl: 开播回调 URL。
        :type StreamBeginNotifyUrl: str
        :param _StreamEndNotifyUrl: 断流回调 URL。
        :type StreamEndNotifyUrl: str
        :param _RecordNotifyUrl: 录制回调 URL。
        :type RecordNotifyUrl: str
        :param _SnapshotNotifyUrl: 截图回调 URL。
        :type SnapshotNotifyUrl: str
        :param _PornCensorshipNotifyUrl: 鉴黄回调 URL。
        :type PornCensorshipNotifyUrl: str
        :param _CallbackKey: 回调 Key，回调 URL 公用，回调签名详见事件消息通知文档。
[事件消息通知](/document/product/267/32744)。
        :type CallbackKey: str
        :param _PushExceptionNotifyUrl: 推流异常回调 URL。
        :type PushExceptionNotifyUrl: str
        :param _AudioAuditNotifyUrl: 音频审核回调 URL。
        :type AudioAuditNotifyUrl: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._StreamBeginNotifyUrl = None
        self._StreamEndNotifyUrl = None
        self._RecordNotifyUrl = None
        self._SnapshotNotifyUrl = None
        self._PornCensorshipNotifyUrl = None
        self._CallbackKey = None
        self._PushExceptionNotifyUrl = None
        self._AudioAuditNotifyUrl = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StreamBeginNotifyUrl(self):
        return self._StreamBeginNotifyUrl

    @StreamBeginNotifyUrl.setter
    def StreamBeginNotifyUrl(self, StreamBeginNotifyUrl):
        self._StreamBeginNotifyUrl = StreamBeginNotifyUrl

    @property
    def StreamEndNotifyUrl(self):
        return self._StreamEndNotifyUrl

    @StreamEndNotifyUrl.setter
    def StreamEndNotifyUrl(self, StreamEndNotifyUrl):
        self._StreamEndNotifyUrl = StreamEndNotifyUrl

    @property
    def RecordNotifyUrl(self):
        return self._RecordNotifyUrl

    @RecordNotifyUrl.setter
    def RecordNotifyUrl(self, RecordNotifyUrl):
        self._RecordNotifyUrl = RecordNotifyUrl

    @property
    def SnapshotNotifyUrl(self):
        return self._SnapshotNotifyUrl

    @SnapshotNotifyUrl.setter
    def SnapshotNotifyUrl(self, SnapshotNotifyUrl):
        self._SnapshotNotifyUrl = SnapshotNotifyUrl

    @property
    def PornCensorshipNotifyUrl(self):
        return self._PornCensorshipNotifyUrl

    @PornCensorshipNotifyUrl.setter
    def PornCensorshipNotifyUrl(self, PornCensorshipNotifyUrl):
        self._PornCensorshipNotifyUrl = PornCensorshipNotifyUrl

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def PushExceptionNotifyUrl(self):
        return self._PushExceptionNotifyUrl

    @PushExceptionNotifyUrl.setter
    def PushExceptionNotifyUrl(self, PushExceptionNotifyUrl):
        self._PushExceptionNotifyUrl = PushExceptionNotifyUrl

    @property
    def AudioAuditNotifyUrl(self):
        return self._AudioAuditNotifyUrl

    @AudioAuditNotifyUrl.setter
    def AudioAuditNotifyUrl(self, AudioAuditNotifyUrl):
        self._AudioAuditNotifyUrl = AudioAuditNotifyUrl


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self._StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self._RecordNotifyUrl = params.get("RecordNotifyUrl")
        self._SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self._PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self._CallbackKey = params.get("CallbackKey")
        self._PushExceptionNotifyUrl = params.get("PushExceptionNotifyUrl")
        self._AudioAuditNotifyUrl = params.get("AudioAuditNotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveCallbackTemplateResponse(AbstractModel):
    """ModifyLiveCallbackTemplate返回参数结构体

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


class ModifyLiveDomainCertBindingsRequest(AbstractModel):
    """ModifyLiveDomainCertBindings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInfos: 要绑定证书的播放域名/状态 信息列表。
如果CloudCertId和证书公钥私钥对均不传，且域名列表已有绑定规则，只批量更新域名https规则的启用状态，并把未上传至腾讯云ssl的已有自有证书上传。
        :type DomainInfos: list of LiveCertDomainInfo
        :param _CloudCertId: 腾讯云ssl的证书Id。
见 https://cloud.tencent.com/document/api/400/41665
        :type CloudCertId: str
        :param _CertificatePublicKey: 证书公钥。
CloudCertId和公钥私钥对二选一，若CloudCertId将会舍弃公钥和私钥参数，否则将自动先把公钥私钥对上传至ssl新建证书，并使用上传成功后返回的CloudCertId。
        :type CertificatePublicKey: str
        :param _CertificatePrivateKey: 证书私钥。
CloudCertId和公钥私钥对二选一，若传CloudCertId将会舍弃公钥和私钥参数，否则将自动先把公钥私钥对上传至ssl新建证书，并使用上传成功后返回的CloudCertId。
        :type CertificatePrivateKey: str
        :param _CertificateAlias: 上传至ssl证书中心的备注信息，只有新建证书时有效。传CloudCertId时会忽略。
        :type CertificateAlias: str
        """
        self._DomainInfos = None
        self._CloudCertId = None
        self._CertificatePublicKey = None
        self._CertificatePrivateKey = None
        self._CertificateAlias = None

    @property
    def DomainInfos(self):
        return self._DomainInfos

    @DomainInfos.setter
    def DomainInfos(self, DomainInfos):
        self._DomainInfos = DomainInfos

    @property
    def CloudCertId(self):
        return self._CloudCertId

    @CloudCertId.setter
    def CloudCertId(self, CloudCertId):
        self._CloudCertId = CloudCertId

    @property
    def CertificatePublicKey(self):
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def CertificatePrivateKey(self):
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias


    def _deserialize(self, params):
        if params.get("DomainInfos") is not None:
            self._DomainInfos = []
            for item in params.get("DomainInfos"):
                obj = LiveCertDomainInfo()
                obj._deserialize(item)
                self._DomainInfos.append(obj)
        self._CloudCertId = params.get("CloudCertId")
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._CertificateAlias = params.get("CertificateAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveDomainCertBindingsResponse(AbstractModel):
    """ModifyLiveDomainCertBindings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MismatchedDomainNames: DomainNames 入参中，与证书不匹配的域名列表，将会跳过处理。
        :type MismatchedDomainNames: list of str
        :param _Errors: 操作失败的域名及错误码，错误信息，包括MismatchedDomainNames中的域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of BatchDomainOperateErrors
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MismatchedDomainNames = None
        self._Errors = None
        self._RequestId = None

    @property
    def MismatchedDomainNames(self):
        return self._MismatchedDomainNames

    @MismatchedDomainNames.setter
    def MismatchedDomainNames(self, MismatchedDomainNames):
        self._MismatchedDomainNames = MismatchedDomainNames

    @property
    def Errors(self):
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MismatchedDomainNames = params.get("MismatchedDomainNames")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = BatchDomainOperateErrors()
                obj._deserialize(item)
                self._Errors.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyLiveDomainRefererRequest(AbstractModel):
    """ModifyLiveDomainReferer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 播放域名。
        :type DomainName: str
        :param _Enable: 是否开启当前域名的 Referer 黑白名单鉴权。
        :type Enable: int
        :param _Type: 名单类型，0：黑名单，1：白名单。
        :type Type: int
        :param _AllowEmpty: 是否允许空 Referer，0：不允许，1：允许。
        :type AllowEmpty: int
        :param _Rules: Referer 名单列表，以;分隔。
        :type Rules: str
        """
        self._DomainName = None
        self._Enable = None
        self._Type = None
        self._AllowEmpty = None
        self._Rules = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AllowEmpty(self):
        return self._AllowEmpty

    @AllowEmpty.setter
    def AllowEmpty(self, AllowEmpty):
        self._AllowEmpty = AllowEmpty

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Enable = params.get("Enable")
        self._Type = params.get("Type")
        self._AllowEmpty = params.get("AllowEmpty")
        self._Rules = params.get("Rules")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveDomainRefererResponse(AbstractModel):
    """ModifyLiveDomainReferer返回参数结构体

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


class ModifyLivePadTemplateRequest(AbstractModel):
    """ModifyLivePadTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id。
        :type TemplateId: int
        :param _Url: 垫片内容。
        :type Url: str
        :param _WaitDuration: 断流等待时间。
取值范围：0-30000。
单位：ms。
        :type WaitDuration: int
        :param _MaxDuration: 最大垫片时长。
取值范围：0 - 正无穷。
单位：ms。
        :type MaxDuration: int
        :param _TemplateName: 模板名称。
长度上限：255字节。
仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param _Description: 描述信息。
长度上限：1024字节。
仅支持中文、英文、数字、_、-。
        :type Description: str
        :param _Type: 垫片内容类型： 1：图片，2：视频。 默认值：1。
        :type Type: int
        """
        self._TemplateId = None
        self._Url = None
        self._WaitDuration = None
        self._MaxDuration = None
        self._TemplateName = None
        self._Description = None
        self._Type = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def WaitDuration(self):
        return self._WaitDuration

    @WaitDuration.setter
    def WaitDuration(self, WaitDuration):
        self._WaitDuration = WaitDuration

    @property
    def MaxDuration(self):
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Url = params.get("Url")
        self._WaitDuration = params.get("WaitDuration")
        self._MaxDuration = params.get("MaxDuration")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePadTemplateResponse(AbstractModel):
    """ModifyLivePadTemplate返回参数结构体

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


class ModifyLivePlayAuthKeyRequest(AbstractModel):
    """ModifyLivePlayAuthKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 播放域名。
        :type DomainName: str
        :param _Enable: 是否启用，0：关闭，1：启用。
不传表示不修改当前值。
        :type Enable: int
        :param _AuthKey: 鉴权key。
不传表示不修改当前值。
        :type AuthKey: str
        :param _AuthDelta: 有效时间，单位：秒。
不传表示不修改当前值。
        :type AuthDelta: int
        :param _AuthBackKey: 鉴权备用key。
不传表示不修改当前值。
        :type AuthBackKey: str
        """
        self._DomainName = None
        self._Enable = None
        self._AuthKey = None
        self._AuthDelta = None
        self._AuthBackKey = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def AuthKey(self):
        return self._AuthKey

    @AuthKey.setter
    def AuthKey(self, AuthKey):
        self._AuthKey = AuthKey

    @property
    def AuthDelta(self):
        return self._AuthDelta

    @AuthDelta.setter
    def AuthDelta(self, AuthDelta):
        self._AuthDelta = AuthDelta

    @property
    def AuthBackKey(self):
        return self._AuthBackKey

    @AuthBackKey.setter
    def AuthBackKey(self, AuthBackKey):
        self._AuthBackKey = AuthBackKey


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Enable = params.get("Enable")
        self._AuthKey = params.get("AuthKey")
        self._AuthDelta = params.get("AuthDelta")
        self._AuthBackKey = params.get("AuthBackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePlayAuthKeyResponse(AbstractModel):
    """ModifyLivePlayAuthKey返回参数结构体

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


class ModifyLivePlayDomainRequest(AbstractModel):
    """ModifyLivePlayDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 播放域名。
        :type DomainName: str
        :param _PlayType: 拉流域名类型。1-国内；2-全球；3-境外
        :type PlayType: int
        """
        self._DomainName = None
        self._PlayType = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def PlayType(self):
        return self._PlayType

    @PlayType.setter
    def PlayType(self, PlayType):
        self._PlayType = PlayType


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._PlayType = params.get("PlayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePlayDomainResponse(AbstractModel):
    """ModifyLivePlayDomain返回参数结构体

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


class ModifyLivePullStreamTaskRequest(AbstractModel):
    """ModifyLivePullStreamTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id。
        :type TaskId: str
        :param _Operator: 操作人姓名。
        :type Operator: str
        :param _SourceUrls: 拉流源url列表。
SourceType为直播（PullLivePushLive）只可以填1个，
SourceType为点播（PullVodPushLive）可以填多个，上限30个。
        :type SourceUrls: list of str
        :param _StartTime: 开始时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param _EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param _VodLoopTimes: 点播拉流转推循环次数。
-1：无限循环，直到任务结束。
0：不循环。
>0：具体循环次数。次数和时间以先结束的为准。
注意：拉流源为点播，该配置生效。
        :type VodLoopTimes: int
        :param _VodRefreshType: 点播更新SourceUrls后的播放方式：
ImmediateNewSource：立即从更新的拉流源开始播放；
ContinueBreakPoint：从上次断流url源的断点处继续，结束后再使用新的拉流源。
注意：拉流源为点播，该配置生效。
        :type VodRefreshType: str
        :param _Status: 任务状态：
enable - 启用，
pause - 暂停。
        :type Status: str
        :param _CallbackEvents: 选择需要回调的事件（不填则回调全部）：
TaskStart：任务启动回调，
TaskExit：任务停止回调，
VodSourceFileStart：从点播源文件开始拉流回调，
VodSourceFileFinish：从点播源文件拉流结束回调，
ResetTaskConfig：任务更新回调。
        :type CallbackEvents: list of str
        :param _CallbackUrl: 自定义回调地址。
相关事件会回调到该地址。
        :type CallbackUrl: str
        :param _FileIndex: 指定播放文件索引。
注意： 从1开始，不大于SourceUrls中文件个数。
        :type FileIndex: int
        :param _OffsetTime: 指定播放文件偏移。
注意：
1. 单位：秒，配合FileIndex使用。
        :type OffsetTime: int
        :param _Comment: 任务备注。
        :type Comment: str
        :param _BackupSourceType: 备源的类型：
PullLivePushLive -直播，
PullVodPushLive -点播。
注意：
1. 仅当主源类型为直播源时，备源才会生效。
2. 将该参数置为空，则可将任务去除备源信息。
3. 主直播源拉流中断时，自动使用备源进行拉流。
4. 如果备源为点播文件时，则每次轮播完点播文件就检查主源是否恢复，如果主源恢复则自动切回到主源，否则继续拉备源。
        :type BackupSourceType: str
        :param _BackupSourceUrl: 备源 URL。
只允许填一个备源 URL
        :type BackupSourceUrl: str
        :param _WatermarkList: 水印信息列表。
注意：
1. 最多支持4个不同位置的水印。
2. 水印图片 URL 请使用合法外网可访问地址。
3. 支持的水印图片格式：png，jpg等。
4. 轮播任务修改水印后，轮播到下一个文件时新水印生效。
5. 直播源任务修改水印后，水印立即生效。
6. 清除水印时，需携带该水印列表参数，内容为空数组。
7. 暂不支持动图水印。
        :type WatermarkList: list of PullPushWatermarkInfo
        :param _VodLocalMode: 点播源是否启用本地推流模式，默认0，不启用。
0 - 不启用。
1 - 启用。
注意：启用本地模式后，会将源列表中的 MP4 文件进行本地下载，优先使用本地已下载文件进行推流，提高点播源推流稳定性。使用本地下载文件推流时，会产生增值费用。
        :type VodLocalMode: int
        """
        self._TaskId = None
        self._Operator = None
        self._SourceUrls = None
        self._StartTime = None
        self._EndTime = None
        self._VodLoopTimes = None
        self._VodRefreshType = None
        self._Status = None
        self._CallbackEvents = None
        self._CallbackUrl = None
        self._FileIndex = None
        self._OffsetTime = None
        self._Comment = None
        self._BackupSourceType = None
        self._BackupSourceUrl = None
        self._WatermarkList = None
        self._VodLocalMode = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def SourceUrls(self):
        return self._SourceUrls

    @SourceUrls.setter
    def SourceUrls(self, SourceUrls):
        self._SourceUrls = SourceUrls

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def VodLoopTimes(self):
        return self._VodLoopTimes

    @VodLoopTimes.setter
    def VodLoopTimes(self, VodLoopTimes):
        self._VodLoopTimes = VodLoopTimes

    @property
    def VodRefreshType(self):
        return self._VodRefreshType

    @VodRefreshType.setter
    def VodRefreshType(self, VodRefreshType):
        self._VodRefreshType = VodRefreshType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CallbackEvents(self):
        return self._CallbackEvents

    @CallbackEvents.setter
    def CallbackEvents(self, CallbackEvents):
        self._CallbackEvents = CallbackEvents

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def FileIndex(self):
        return self._FileIndex

    @FileIndex.setter
    def FileIndex(self, FileIndex):
        self._FileIndex = FileIndex

    @property
    def OffsetTime(self):
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def BackupSourceType(self):
        return self._BackupSourceType

    @BackupSourceType.setter
    def BackupSourceType(self, BackupSourceType):
        self._BackupSourceType = BackupSourceType

    @property
    def BackupSourceUrl(self):
        return self._BackupSourceUrl

    @BackupSourceUrl.setter
    def BackupSourceUrl(self, BackupSourceUrl):
        self._BackupSourceUrl = BackupSourceUrl

    @property
    def WatermarkList(self):
        return self._WatermarkList

    @WatermarkList.setter
    def WatermarkList(self, WatermarkList):
        self._WatermarkList = WatermarkList

    @property
    def VodLocalMode(self):
        return self._VodLocalMode

    @VodLocalMode.setter
    def VodLocalMode(self, VodLocalMode):
        self._VodLocalMode = VodLocalMode


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Operator = params.get("Operator")
        self._SourceUrls = params.get("SourceUrls")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._VodLoopTimes = params.get("VodLoopTimes")
        self._VodRefreshType = params.get("VodRefreshType")
        self._Status = params.get("Status")
        self._CallbackEvents = params.get("CallbackEvents")
        self._CallbackUrl = params.get("CallbackUrl")
        self._FileIndex = params.get("FileIndex")
        self._OffsetTime = params.get("OffsetTime")
        self._Comment = params.get("Comment")
        self._BackupSourceType = params.get("BackupSourceType")
        self._BackupSourceUrl = params.get("BackupSourceUrl")
        if params.get("WatermarkList") is not None:
            self._WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = PullPushWatermarkInfo()
                obj._deserialize(item)
                self._WatermarkList.append(obj)
        self._VodLocalMode = params.get("VodLocalMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePullStreamTaskResponse(AbstractModel):
    """ModifyLivePullStreamTask返回参数结构体

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


class ModifyLivePushAuthKeyRequest(AbstractModel):
    """ModifyLivePushAuthKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _Enable: 是否启用，0：关闭，1：启用。
不传表示不修改当前值。
        :type Enable: int
        :param _MasterAuthKey: 主鉴权key。
不传表示不修改当前值。
        :type MasterAuthKey: str
        :param _BackupAuthKey: 备鉴权key。
不传表示不修改当前值。
        :type BackupAuthKey: str
        :param _AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        """
        self._DomainName = None
        self._Enable = None
        self._MasterAuthKey = None
        self._BackupAuthKey = None
        self._AuthDelta = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def MasterAuthKey(self):
        return self._MasterAuthKey

    @MasterAuthKey.setter
    def MasterAuthKey(self, MasterAuthKey):
        self._MasterAuthKey = MasterAuthKey

    @property
    def BackupAuthKey(self):
        return self._BackupAuthKey

    @BackupAuthKey.setter
    def BackupAuthKey(self, BackupAuthKey):
        self._BackupAuthKey = BackupAuthKey

    @property
    def AuthDelta(self):
        return self._AuthDelta

    @AuthDelta.setter
    def AuthDelta(self, AuthDelta):
        self._AuthDelta = AuthDelta


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Enable = params.get("Enable")
        self._MasterAuthKey = params.get("MasterAuthKey")
        self._BackupAuthKey = params.get("BackupAuthKey")
        self._AuthDelta = params.get("AuthDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePushAuthKeyResponse(AbstractModel):
    """ModifyLivePushAuthKey返回参数结构体

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


class ModifyLiveRecordTemplateRequest(AbstractModel):
    """ModifyLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: DescribeRecordTemplates接口获取到的模板 ID。
        :type TemplateId: int
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _Description: 描述信息。
        :type Description: str
        :param _FlvParam: FLV 录制参数，开启 FLV 录制时设置。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _HlsParam: HLS 录制参数，开启 HLS 录制时设置。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _Mp4Param: MP4 录制参数，开启 MP4 录制时设置。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _AacParam: AAC 录制参数，开启 AAC 录制时设置。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _HlsSpecialParam: HLS 录制定制参数。
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param _Mp3Param: MP3 录制参数，开启 MP3 录制时设置。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _RemoveWatermark: 是否去除水印，类型为慢直播时此参数无效。
        :type RemoveWatermark: bool
        :param _FlvSpecialParam: FLV 录制定制参数。
        :type FlvSpecialParam: :class:`tencentcloud.live.v20180801.models.FlvSpecialParam`
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._FlvParam = None
        self._HlsParam = None
        self._Mp4Param = None
        self._AacParam = None
        self._HlsSpecialParam = None
        self._Mp3Param = None
        self._RemoveWatermark = None
        self._FlvSpecialParam = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def FlvParam(self):
        return self._FlvParam

    @FlvParam.setter
    def FlvParam(self, FlvParam):
        self._FlvParam = FlvParam

    @property
    def HlsParam(self):
        return self._HlsParam

    @HlsParam.setter
    def HlsParam(self, HlsParam):
        self._HlsParam = HlsParam

    @property
    def Mp4Param(self):
        return self._Mp4Param

    @Mp4Param.setter
    def Mp4Param(self, Mp4Param):
        self._Mp4Param = Mp4Param

    @property
    def AacParam(self):
        return self._AacParam

    @AacParam.setter
    def AacParam(self, AacParam):
        self._AacParam = AacParam

    @property
    def HlsSpecialParam(self):
        return self._HlsSpecialParam

    @HlsSpecialParam.setter
    def HlsSpecialParam(self, HlsSpecialParam):
        self._HlsSpecialParam = HlsSpecialParam

    @property
    def Mp3Param(self):
        return self._Mp3Param

    @Mp3Param.setter
    def Mp3Param(self, Mp3Param):
        self._Mp3Param = Mp3Param

    @property
    def RemoveWatermark(self):
        return self._RemoveWatermark

    @RemoveWatermark.setter
    def RemoveWatermark(self, RemoveWatermark):
        self._RemoveWatermark = RemoveWatermark

    @property
    def FlvSpecialParam(self):
        return self._FlvSpecialParam

    @FlvSpecialParam.setter
    def FlvSpecialParam(self, FlvSpecialParam):
        self._FlvSpecialParam = FlvSpecialParam


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self._FlvParam = RecordParam()
            self._FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self._HlsParam = RecordParam()
            self._HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self._Mp4Param = RecordParam()
            self._Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self._AacParam = RecordParam()
            self._AacParam._deserialize(params.get("AacParam"))
        if params.get("HlsSpecialParam") is not None:
            self._HlsSpecialParam = HlsSpecialParam()
            self._HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self._Mp3Param = RecordParam()
            self._Mp3Param._deserialize(params.get("Mp3Param"))
        self._RemoveWatermark = params.get("RemoveWatermark")
        if params.get("FlvSpecialParam") is not None:
            self._FlvSpecialParam = FlvSpecialParam()
            self._FlvSpecialParam._deserialize(params.get("FlvSpecialParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveRecordTemplateResponse(AbstractModel):
    """ModifyLiveRecordTemplate返回参数结构体

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


class ModifyLiveSnapshotTemplateRequest(AbstractModel):
    """ModifyLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _CosAppId: Cos 应用 ID。
**注：此参数现在须必选。**
        :type CosAppId: int
        :param _CosBucket: Cos Bucket名称。
注：CosBucket参数值不能包含-[appid] 部分。
**注：此参数现在须必选。**
        :type CosBucket: str
        :param _CosRegion: Cos 地域。
**注：此参数现在须必选。**
        :type CosRegion: str
        :param _TemplateName: 模板名称。
长度上限：255字节。
        :type TemplateName: str
        :param _Description: 描述信息。
长度上限：1024字节。
        :type Description: str
        :param _SnapshotInterval: 截图间隔，单位s，默认10s。
范围： 5s ~ 300s。
        :type SnapshotInterval: int
        :param _Width: 截图宽度。默认：0（原始宽）。
        :type Width: int
        :param _Height: 截图高度。默认：0（原始高）。
        :type Height: int
        :param _PornFlag: 是否开启鉴黄，默认 0 。
0：不开启。
1：开启。
        :type PornFlag: int
        :param _CosPrefix: Cos Bucket文件夹前缀。
        :type CosPrefix: str
        :param _CosFileName: Cos 文件名称。
        :type CosFileName: str
        """
        self._TemplateId = None
        self._CosAppId = None
        self._CosBucket = None
        self._CosRegion = None
        self._TemplateName = None
        self._Description = None
        self._SnapshotInterval = None
        self._Width = None
        self._Height = None
        self._PornFlag = None
        self._CosPrefix = None
        self._CosFileName = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def CosAppId(self):
        return self._CosAppId

    @CosAppId.setter
    def CosAppId(self, CosAppId):
        self._CosAppId = CosAppId

    @property
    def CosBucket(self):
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SnapshotInterval(self):
        return self._SnapshotInterval

    @SnapshotInterval.setter
    def SnapshotInterval(self, SnapshotInterval):
        self._SnapshotInterval = SnapshotInterval

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def PornFlag(self):
        return self._PornFlag

    @PornFlag.setter
    def PornFlag(self, PornFlag):
        self._PornFlag = PornFlag

    @property
    def CosPrefix(self):
        return self._CosPrefix

    @CosPrefix.setter
    def CosPrefix(self, CosPrefix):
        self._CosPrefix = CosPrefix

    @property
    def CosFileName(self):
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._CosAppId = params.get("CosAppId")
        self._CosBucket = params.get("CosBucket")
        self._CosRegion = params.get("CosRegion")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._SnapshotInterval = params.get("SnapshotInterval")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._PornFlag = params.get("PornFlag")
        self._CosPrefix = params.get("CosPrefix")
        self._CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveSnapshotTemplateResponse(AbstractModel):
    """ModifyLiveSnapshotTemplate返回参数结构体

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


class ModifyLiveStreamMonitorRequest(AbstractModel):
    """ModifyLiveStreamMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监播任务ID。
        :type MonitorId: str
        :param _MonitorName: 监播任务的名称。长度128字节以内（一个汉字两个字节）。
        :type MonitorName: str
        :param _OutputInfo: 监播任务输出信息。
        :type OutputInfo: :class:`tencentcloud.live.v20180801.models.LiveStreamMonitorOutputInfo`
        :param _InputList: 待监播的输入流信息。
        :type InputList: list of LiveStreamMonitorInputInfo
        :param _NotifyPolicy: 监播事件通知策略。
        :type NotifyPolicy: :class:`tencentcloud.live.v20180801.models.LiveStreamMonitorNotifyPolicy`
        :param _AsrLanguage: 智能语音识别语种：
0 关闭 1 中文 2 英文 3 日文 4 韩文。
        :type AsrLanguage: int
        :param _OcrLanguage: 智能文字识别语种：
0 关闭 1 中、英文。
        :type OcrLanguage: int
        :param _AiAsrInputIndexList: 语音识别输入流列表，1代表第一条输入流。
        :type AiAsrInputIndexList: list of int non-negative
        :param _AiOcrInputIndexList: 文字识别输入流列表，1代表第一条输入流。
        :type AiOcrInputIndexList: list of int non-negative
        :param _CheckStreamBroken: 是否开启断流检测。
        :type CheckStreamBroken: int
        :param _CheckStreamLowFrameRate: 是否开启低帧率检测。
        :type CheckStreamLowFrameRate: int
        :param _AllowMonitorReport: 是否存储监播事件到监播报告，以及是否允许查询监播报告。
        :type AllowMonitorReport: int
        :param _AiFormatDiagnose: 是否开启格式诊断。
        :type AiFormatDiagnose: int
        """
        self._MonitorId = None
        self._MonitorName = None
        self._OutputInfo = None
        self._InputList = None
        self._NotifyPolicy = None
        self._AsrLanguage = None
        self._OcrLanguage = None
        self._AiAsrInputIndexList = None
        self._AiOcrInputIndexList = None
        self._CheckStreamBroken = None
        self._CheckStreamLowFrameRate = None
        self._AllowMonitorReport = None
        self._AiFormatDiagnose = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def MonitorName(self):
        return self._MonitorName

    @MonitorName.setter
    def MonitorName(self, MonitorName):
        self._MonitorName = MonitorName

    @property
    def OutputInfo(self):
        return self._OutputInfo

    @OutputInfo.setter
    def OutputInfo(self, OutputInfo):
        self._OutputInfo = OutputInfo

    @property
    def InputList(self):
        return self._InputList

    @InputList.setter
    def InputList(self, InputList):
        self._InputList = InputList

    @property
    def NotifyPolicy(self):
        return self._NotifyPolicy

    @NotifyPolicy.setter
    def NotifyPolicy(self, NotifyPolicy):
        self._NotifyPolicy = NotifyPolicy

    @property
    def AsrLanguage(self):
        return self._AsrLanguage

    @AsrLanguage.setter
    def AsrLanguage(self, AsrLanguage):
        self._AsrLanguage = AsrLanguage

    @property
    def OcrLanguage(self):
        return self._OcrLanguage

    @OcrLanguage.setter
    def OcrLanguage(self, OcrLanguage):
        self._OcrLanguage = OcrLanguage

    @property
    def AiAsrInputIndexList(self):
        return self._AiAsrInputIndexList

    @AiAsrInputIndexList.setter
    def AiAsrInputIndexList(self, AiAsrInputIndexList):
        self._AiAsrInputIndexList = AiAsrInputIndexList

    @property
    def AiOcrInputIndexList(self):
        return self._AiOcrInputIndexList

    @AiOcrInputIndexList.setter
    def AiOcrInputIndexList(self, AiOcrInputIndexList):
        self._AiOcrInputIndexList = AiOcrInputIndexList

    @property
    def CheckStreamBroken(self):
        return self._CheckStreamBroken

    @CheckStreamBroken.setter
    def CheckStreamBroken(self, CheckStreamBroken):
        self._CheckStreamBroken = CheckStreamBroken

    @property
    def CheckStreamLowFrameRate(self):
        return self._CheckStreamLowFrameRate

    @CheckStreamLowFrameRate.setter
    def CheckStreamLowFrameRate(self, CheckStreamLowFrameRate):
        self._CheckStreamLowFrameRate = CheckStreamLowFrameRate

    @property
    def AllowMonitorReport(self):
        return self._AllowMonitorReport

    @AllowMonitorReport.setter
    def AllowMonitorReport(self, AllowMonitorReport):
        self._AllowMonitorReport = AllowMonitorReport

    @property
    def AiFormatDiagnose(self):
        return self._AiFormatDiagnose

    @AiFormatDiagnose.setter
    def AiFormatDiagnose(self, AiFormatDiagnose):
        self._AiFormatDiagnose = AiFormatDiagnose


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._MonitorName = params.get("MonitorName")
        if params.get("OutputInfo") is not None:
            self._OutputInfo = LiveStreamMonitorOutputInfo()
            self._OutputInfo._deserialize(params.get("OutputInfo"))
        if params.get("InputList") is not None:
            self._InputList = []
            for item in params.get("InputList"):
                obj = LiveStreamMonitorInputInfo()
                obj._deserialize(item)
                self._InputList.append(obj)
        if params.get("NotifyPolicy") is not None:
            self._NotifyPolicy = LiveStreamMonitorNotifyPolicy()
            self._NotifyPolicy._deserialize(params.get("NotifyPolicy"))
        self._AsrLanguage = params.get("AsrLanguage")
        self._OcrLanguage = params.get("OcrLanguage")
        self._AiAsrInputIndexList = params.get("AiAsrInputIndexList")
        self._AiOcrInputIndexList = params.get("AiOcrInputIndexList")
        self._CheckStreamBroken = params.get("CheckStreamBroken")
        self._CheckStreamLowFrameRate = params.get("CheckStreamLowFrameRate")
        self._AllowMonitorReport = params.get("AllowMonitorReport")
        self._AiFormatDiagnose = params.get("AiFormatDiagnose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveStreamMonitorResponse(AbstractModel):
    """ModifyLiveStreamMonitor返回参数结构体

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


class ModifyLiveTimeShiftTemplateRequest(AbstractModel):
    """ModifyLiveTimeShiftTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 时移模板id。
        :type TemplateId: int
        :param _TemplateName: 模板名称。
仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param _Description: 描述信息。
长度上限：1024字节。
仅支持中文、英文、数字、_、-。
        :type Description: str
        :param _Duration: 时移时长。
单位：s。
        :type Duration: int
        :param _ItemDuration: 分片时长。
可取3-10。
单位：s。
默认值：5。
        :type ItemDuration: int
        :param _RemoveWatermark: 是否去除水印。
传true则将录制原始流。
默认值：false。
        :type RemoveWatermark: bool
        :param _TranscodeTemplateIds: 转码流id列表。
此参数仅在 RemoveWatermark为false时生效。
        :type TranscodeTemplateIds: list of int
        :param _Area: 地域。
Mainland：中国大陆。
Overseas：海外及港澳台地区。
默认值：Mainland。
        :type Area: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._Duration = None
        self._ItemDuration = None
        self._RemoveWatermark = None
        self._TranscodeTemplateIds = None
        self._Area = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ItemDuration(self):
        return self._ItemDuration

    @ItemDuration.setter
    def ItemDuration(self, ItemDuration):
        self._ItemDuration = ItemDuration

    @property
    def RemoveWatermark(self):
        return self._RemoveWatermark

    @RemoveWatermark.setter
    def RemoveWatermark(self, RemoveWatermark):
        self._RemoveWatermark = RemoveWatermark

    @property
    def TranscodeTemplateIds(self):
        return self._TranscodeTemplateIds

    @TranscodeTemplateIds.setter
    def TranscodeTemplateIds(self, TranscodeTemplateIds):
        self._TranscodeTemplateIds = TranscodeTemplateIds

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._Duration = params.get("Duration")
        self._ItemDuration = params.get("ItemDuration")
        self._RemoveWatermark = params.get("RemoveWatermark")
        self._TranscodeTemplateIds = params.get("TranscodeTemplateIds")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveTimeShiftTemplateResponse(AbstractModel):
    """ModifyLiveTimeShiftTemplate返回参数结构体

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


class ModifyLiveTranscodeTemplateRequest(AbstractModel):
    """ModifyLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 Id。
        :type TemplateId: int
        :param _Vcodec: 视频编码：h264/h265/origin，默认origin。

origin: 保持原始编码格式
        :type Vcodec: str
        :param _Acodec: 音频编码：aac，默认aac。
注意：当前该参数未生效，待后续支持！
        :type Acodec: str
        :param _AudioBitrate: 音频码率，默认0。
范围：0-500。
        :type AudioBitrate: int
        :param _Description: 模板描述。
        :type Description: str
        :param _VideoBitrate: 视频码率。范围：0kbps - 8000kbps。
0为保持原始码率。
注: 转码模板有码率唯一要求，最终保存的码率可能与输入码率有所差别。
        :type VideoBitrate: int
        :param _Width: 宽。0-3000。
数值必须是2的倍数，0是原始宽度
        :type Width: int
        :param _NeedVideo: 是否保留视频，0：否，1：是。默认1。
        :type NeedVideo: int
        :param _NeedAudio: 是否保留音频，0：否，1：是。默认1。
        :type NeedAudio: int
        :param _Height: 高。0-3000。
数值必须是2的倍数，0是原始宽度
        :type Height: int
        :param _Fps: 帧率，默认0。
范围0-60
        :type Fps: int
        :param _Gop: 关键帧间隔，单位：秒。
范围2-6
        :type Gop: int
        :param _Rotate: 旋转角度，默认0。
可取值：0，90，180，270
        :type Rotate: int
        :param _Profile: 编码质量：
baseline/main/high。
        :type Profile: str
        :param _BitrateToOrig: 当设置的码率>原始码率时，是否以原始码率为准。
0：否， 1：是
默认 0。
        :type BitrateToOrig: int
        :param _HeightToOrig: 当设置的高度>原始高度时，是否以原始高度为准。
0：否， 1：是
默认 0。
        :type HeightToOrig: int
        :param _FpsToOrig: 当设置的帧率>原始帧率时，是否以原始帧率为准。
0：否， 1：是
默认 0。
        :type FpsToOrig: int
        :param _AdaptBitratePercent: 极速高清视频码率压缩比。
极速高清目标码率=VideoBitrate * (1-AdaptBitratePercent)

取值范围：0.0到0.5
        :type AdaptBitratePercent: float
        :param _ShortEdgeAsHeight: 是否以短边作为高度，0：否，1：是。默认0。
        :type ShortEdgeAsHeight: int
        :param _DRMType: DRM 加密类型，可选值：fairplay、normalaes、widevine。
不传递或者为空字符串，清空之前的DRM配置。
        :type DRMType: str
        :param _DRMTracks: DRM 加密项，可选值：AUDIO、SD、HD、UHD1、UHD2，后四个为一组，同组中的内容只能选一个。
不传递或者为空字符串，清空之前的DRM配置。
        :type DRMTracks: str
        """
        self._TemplateId = None
        self._Vcodec = None
        self._Acodec = None
        self._AudioBitrate = None
        self._Description = None
        self._VideoBitrate = None
        self._Width = None
        self._NeedVideo = None
        self._NeedAudio = None
        self._Height = None
        self._Fps = None
        self._Gop = None
        self._Rotate = None
        self._Profile = None
        self._BitrateToOrig = None
        self._HeightToOrig = None
        self._FpsToOrig = None
        self._AdaptBitratePercent = None
        self._ShortEdgeAsHeight = None
        self._DRMType = None
        self._DRMTracks = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Vcodec(self):
        return self._Vcodec

    @Vcodec.setter
    def Vcodec(self, Vcodec):
        self._Vcodec = Vcodec

    @property
    def Acodec(self):
        return self._Acodec

    @Acodec.setter
    def Acodec(self, Acodec):
        self._Acodec = Acodec

    @property
    def AudioBitrate(self):
        return self._AudioBitrate

    @AudioBitrate.setter
    def AudioBitrate(self, AudioBitrate):
        self._AudioBitrate = AudioBitrate

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VideoBitrate(self):
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def NeedVideo(self):
        return self._NeedVideo

    @NeedVideo.setter
    def NeedVideo(self, NeedVideo):
        self._NeedVideo = NeedVideo

    @property
    def NeedAudio(self):
        return self._NeedAudio

    @NeedAudio.setter
    def NeedAudio(self, NeedAudio):
        self._NeedAudio = NeedAudio

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Gop(self):
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop

    @property
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate

    @property
    def Profile(self):
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def BitrateToOrig(self):
        return self._BitrateToOrig

    @BitrateToOrig.setter
    def BitrateToOrig(self, BitrateToOrig):
        self._BitrateToOrig = BitrateToOrig

    @property
    def HeightToOrig(self):
        return self._HeightToOrig

    @HeightToOrig.setter
    def HeightToOrig(self, HeightToOrig):
        self._HeightToOrig = HeightToOrig

    @property
    def FpsToOrig(self):
        return self._FpsToOrig

    @FpsToOrig.setter
    def FpsToOrig(self, FpsToOrig):
        self._FpsToOrig = FpsToOrig

    @property
    def AdaptBitratePercent(self):
        return self._AdaptBitratePercent

    @AdaptBitratePercent.setter
    def AdaptBitratePercent(self, AdaptBitratePercent):
        self._AdaptBitratePercent = AdaptBitratePercent

    @property
    def ShortEdgeAsHeight(self):
        return self._ShortEdgeAsHeight

    @ShortEdgeAsHeight.setter
    def ShortEdgeAsHeight(self, ShortEdgeAsHeight):
        self._ShortEdgeAsHeight = ShortEdgeAsHeight

    @property
    def DRMType(self):
        return self._DRMType

    @DRMType.setter
    def DRMType(self, DRMType):
        self._DRMType = DRMType

    @property
    def DRMTracks(self):
        return self._DRMTracks

    @DRMTracks.setter
    def DRMTracks(self, DRMTracks):
        self._DRMTracks = DRMTracks


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Vcodec = params.get("Vcodec")
        self._Acodec = params.get("Acodec")
        self._AudioBitrate = params.get("AudioBitrate")
        self._Description = params.get("Description")
        self._VideoBitrate = params.get("VideoBitrate")
        self._Width = params.get("Width")
        self._NeedVideo = params.get("NeedVideo")
        self._NeedAudio = params.get("NeedAudio")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._Gop = params.get("Gop")
        self._Rotate = params.get("Rotate")
        self._Profile = params.get("Profile")
        self._BitrateToOrig = params.get("BitrateToOrig")
        self._HeightToOrig = params.get("HeightToOrig")
        self._FpsToOrig = params.get("FpsToOrig")
        self._AdaptBitratePercent = params.get("AdaptBitratePercent")
        self._ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        self._DRMType = params.get("DRMType")
        self._DRMTracks = params.get("DRMTracks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveTranscodeTemplateResponse(AbstractModel):
    """ModifyLiveTranscodeTemplate返回参数结构体

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


class ModifyPullStreamConfigRequest(AbstractModel):
    """ModifyPullStreamConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 配置 ID。
获取来源：
1. 创建拉流配置接口CreatePullStreamConfig返回的配置 ID。
2. 通过查询接口DescribePullStreamConfigs获取配置 ID。
        :type ConfigId: str
        :param _FromUrl: 源 URL，用于拉流的地址。目前可支持直播流及点播文件。
注意：
1. 多个点播 URL 之间使用空格拼接。
2. 目前上限支持10个 URL。
3. 支持拉流文件格式：FLV，RTMP，HLS，MP4。
4. 使用标准三层样式，如：http://test.com/live/stream.flv。
        :type FromUrl: str
        :param _ToUrl: 目的 URL，用于推流的地址，目前限制该目标地址为腾讯域名。
1. 仅支持 RTMP 协议。
2. 使用标准三层样式，如：http://test.com/live/stream.flv。
        :type ToUrl: str
        :param _AreaId: 区域 ID：
1-深圳。
2-上海。
3-天津。
4-中国香港。
如有改动，需同时传入IspId。
        :type AreaId: int
        :param _IspId: 运营商 ID，
1：电信。
2：移动。
3：联通。
4：其他。
AreaId为4的时候，IspId只能为其他。如有改动，需同时传入AreaId。
        :type IspId: int
        :param _StartTime: 开始时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param _EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。

使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        """
        self._ConfigId = None
        self._FromUrl = None
        self._ToUrl = None
        self._AreaId = None
        self._IspId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def FromUrl(self):
        return self._FromUrl

    @FromUrl.setter
    def FromUrl(self, FromUrl):
        self._FromUrl = FromUrl

    @property
    def ToUrl(self):
        return self._ToUrl

    @ToUrl.setter
    def ToUrl(self, ToUrl):
        self._ToUrl = ToUrl

    @property
    def AreaId(self):
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def IspId(self):
        return self._IspId

    @IspId.setter
    def IspId(self, IspId):
        self._IspId = IspId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._FromUrl = params.get("FromUrl")
        self._ToUrl = params.get("ToUrl")
        self._AreaId = params.get("AreaId")
        self._IspId = params.get("IspId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPullStreamConfigResponse(AbstractModel):
    """ModifyPullStreamConfig返回参数结构体

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


class ModifyPullStreamStatusRequest(AbstractModel):
    """ModifyPullStreamStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigIds: 配置 ID 列表。
        :type ConfigIds: list of str
        :param _Status: 目标状态。0无效，2正在运行，4暂停。
        :type Status: str
        """
        self._ConfigIds = None
        self._Status = None

    @property
    def ConfigIds(self):
        return self._ConfigIds

    @ConfigIds.setter
    def ConfigIds(self, ConfigIds):
        self._ConfigIds = ConfigIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ConfigIds = params.get("ConfigIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPullStreamStatusResponse(AbstractModel):
    """ModifyPullStreamStatus返回参数结构体

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


class MonitorStreamPlayInfo(AbstractModel):
    """监控播放数据

    """

    def __init__(self):
        r"""
        :param _PlayDomain: 播放域名。
        :type PlayDomain: str
        :param _StreamName: 流id。
        :type StreamName: str
        :param _Rate: 播放码率，0表示原始码率。
        :type Rate: int
        :param _Protocol: 播放协议，可选值包括 Unknown，Flv，Hls，Rtmp，Huyap2p。
        :type Protocol: str
        :param _Bandwidth: 带宽，单位是Mbps。
        :type Bandwidth: float
        :param _Online: 在线人数，1分钟采样一个点，统计采样点的tcp链接数目。
        :type Online: int
        :param _Request: 请求数。
        :type Request: int
        """
        self._PlayDomain = None
        self._StreamName = None
        self._Rate = None
        self._Protocol = None
        self._Bandwidth = None
        self._Online = None
        self._Request = None

    @property
    def PlayDomain(self):
        return self._PlayDomain

    @PlayDomain.setter
    def PlayDomain(self, PlayDomain):
        self._PlayDomain = PlayDomain

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def Request(self):
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request


    def _deserialize(self, params):
        self._PlayDomain = params.get("PlayDomain")
        self._StreamName = params.get("StreamName")
        self._Rate = params.get("Rate")
        self._Protocol = params.get("Protocol")
        self._Bandwidth = params.get("Bandwidth")
        self._Online = params.get("Online")
        self._Request = params.get("Request")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PadTemplate(AbstractModel):
    """直播垫片模板。

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id。
        :type TemplateId: int
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _Url: 垫片内容。
        :type Url: str
        :param _CreateTime: 模板创建时间。
        :type CreateTime: str
        :param _UpdateTime: 模板修改时间。
        :type UpdateTime: str
        :param _Description: 模板描述。
        :type Description: str
        :param _WaitDuration: 断流等待时间。
取值范围：0-30000。
单位：ms。
        :type WaitDuration: int
        :param _MaxDuration: 最大垫片时长。
取值范围：0 - 正无穷。
单位：ms。
        :type MaxDuration: int
        :param _Type: 垫片内容类型： 1：图片，2：视频。 默认值：1。
        :type Type: int
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Url = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Description = None
        self._WaitDuration = None
        self._MaxDuration = None
        self._Type = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WaitDuration(self):
        return self._WaitDuration

    @WaitDuration.setter
    def WaitDuration(self, WaitDuration):
        self._WaitDuration = WaitDuration

    @property
    def MaxDuration(self):
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Url = params.get("Url")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Description = params.get("Description")
        self._WaitDuration = params.get("WaitDuration")
        self._MaxDuration = params.get("MaxDuration")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayAuthKeyInfo(AbstractModel):
    """播放鉴权key信息。

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名。
        :type DomainName: str
        :param _Enable: 是否启用:
0: 关闭。
1: 启用。
        :type Enable: int
        :param _AuthKey: 鉴权 Key。
        :type AuthKey: str
        :param _AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        :param _AuthBackKey: 鉴权 BackKey。
        :type AuthBackKey: str
        """
        self._DomainName = None
        self._Enable = None
        self._AuthKey = None
        self._AuthDelta = None
        self._AuthBackKey = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def AuthKey(self):
        return self._AuthKey

    @AuthKey.setter
    def AuthKey(self, AuthKey):
        self._AuthKey = AuthKey

    @property
    def AuthDelta(self):
        return self._AuthDelta

    @AuthDelta.setter
    def AuthDelta(self, AuthDelta):
        self._AuthDelta = AuthDelta

    @property
    def AuthBackKey(self):
        return self._AuthBackKey

    @AuthBackKey.setter
    def AuthBackKey(self, AuthBackKey):
        self._AuthBackKey = AuthBackKey


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Enable = params.get("Enable")
        self._AuthKey = params.get("AuthKey")
        self._AuthDelta = params.get("AuthDelta")
        self._AuthBackKey = params.get("AuthBackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayCodeTotalInfo(AbstractModel):
    """各状态码的总次数，支持大多数的 HTTP 协议返回码。

    """

    def __init__(self):
        r"""
        :param _Code: HTTP code，可选值包括:
400，403，404，500，502，503，504。
        :type Code: str
        :param _Num: 总次数。
        :type Num: int
        """
        self._Code = None
        self._Num = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayDataInfoByStream(AbstractModel):
    """流维度的播放信息。

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _TotalFlux: 总流量，单位: MB。
        :type TotalFlux: float
        """
        self._StreamName = None
        self._TotalFlux = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def TotalFlux(self):
        return self._TotalFlux

    @TotalFlux.setter
    def TotalFlux(self, TotalFlux):
        self._TotalFlux = TotalFlux


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._TotalFlux = params.get("TotalFlux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayStatInfo(AbstractModel):
    """按省份运营商查询的播放信息。

    """

    def __init__(self):
        r"""
        :param _Time: 数据时间点。
        :type Time: str
        :param _Value: 带宽/流量/请求数/并发连接数/下载速度的值，若没数据返回时该值为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlaySumStatInfo(AbstractModel):
    """播放汇总统计信息。

    """

    def __init__(self):
        r"""
        :param _Name: 域名或流 ID。
        :type Name: str
        :param _AvgFluxPerSecond: 平均下载速度，
单位: MB/s。
计算公式: 每分钟的下载速度求平均值。
        :type AvgFluxPerSecond: float
        :param _TotalFlux: 总流量，单位: MB。
        :type TotalFlux: float
        :param _TotalRequest: 总请求数。
        :type TotalRequest: int
        """
        self._Name = None
        self._AvgFluxPerSecond = None
        self._TotalFlux = None
        self._TotalRequest = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AvgFluxPerSecond(self):
        return self._AvgFluxPerSecond

    @AvgFluxPerSecond.setter
    def AvgFluxPerSecond(self, AvgFluxPerSecond):
        self._AvgFluxPerSecond = AvgFluxPerSecond

    @property
    def TotalFlux(self):
        return self._TotalFlux

    @TotalFlux.setter
    def TotalFlux(self, TotalFlux):
        self._TotalFlux = TotalFlux

    @property
    def TotalRequest(self):
        return self._TotalRequest

    @TotalRequest.setter
    def TotalRequest(self, TotalRequest):
        self._TotalRequest = TotalRequest


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self._TotalFlux = params.get("TotalFlux")
        self._TotalRequest = params.get("TotalRequest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProIspPlayCodeDataInfo(AbstractModel):
    """播放错误码信息

    """

    def __init__(self):
        r"""
        :param _CountryAreaName: 国家或地区。
        :type CountryAreaName: str
        :param _ProvinceName: 省份。
        :type ProvinceName: str
        :param _IspName: 运营商。
        :type IspName: str
        :param _Code2xx: 错误码为2开头的次数。
        :type Code2xx: int
        :param _Code3xx: 错误码为3开头的次数。
        :type Code3xx: int
        :param _Code4xx: 错误码为4开头的次数。
        :type Code4xx: int
        :param _Code5xx: 错误码为5开头的次数。
        :type Code5xx: int
        """
        self._CountryAreaName = None
        self._ProvinceName = None
        self._IspName = None
        self._Code2xx = None
        self._Code3xx = None
        self._Code4xx = None
        self._Code5xx = None

    @property
    def CountryAreaName(self):
        return self._CountryAreaName

    @CountryAreaName.setter
    def CountryAreaName(self, CountryAreaName):
        self._CountryAreaName = CountryAreaName

    @property
    def ProvinceName(self):
        return self._ProvinceName

    @ProvinceName.setter
    def ProvinceName(self, ProvinceName):
        self._ProvinceName = ProvinceName

    @property
    def IspName(self):
        return self._IspName

    @IspName.setter
    def IspName(self, IspName):
        self._IspName = IspName

    @property
    def Code2xx(self):
        return self._Code2xx

    @Code2xx.setter
    def Code2xx(self, Code2xx):
        self._Code2xx = Code2xx

    @property
    def Code3xx(self):
        return self._Code3xx

    @Code3xx.setter
    def Code3xx(self, Code3xx):
        self._Code3xx = Code3xx

    @property
    def Code4xx(self):
        return self._Code4xx

    @Code4xx.setter
    def Code4xx(self, Code4xx):
        self._Code4xx = Code4xx

    @property
    def Code5xx(self):
        return self._Code5xx

    @Code5xx.setter
    def Code5xx(self, Code5xx):
        self._Code5xx = Code5xx


    def _deserialize(self, params):
        self._CountryAreaName = params.get("CountryAreaName")
        self._ProvinceName = params.get("ProvinceName")
        self._IspName = params.get("IspName")
        self._Code2xx = params.get("Code2xx")
        self._Code3xx = params.get("Code3xx")
        self._Code4xx = params.get("Code4xx")
        self._Code5xx = params.get("Code5xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProIspPlaySumInfo(AbstractModel):
    """获取省份/运营商的播放信息。

    """

    def __init__(self):
        r"""
        :param _Name: 省份/运营商/国家或地区。
        :type Name: str
        :param _TotalFlux: 总流量，单位: MB。
        :type TotalFlux: float
        :param _TotalRequest: 总请求数。
        :type TotalRequest: int
        :param _AvgFluxPerSecond: 平均下载流量，单位: MB/s。
        :type AvgFluxPerSecond: float
        """
        self._Name = None
        self._TotalFlux = None
        self._TotalRequest = None
        self._AvgFluxPerSecond = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TotalFlux(self):
        return self._TotalFlux

    @TotalFlux.setter
    def TotalFlux(self, TotalFlux):
        self._TotalFlux = TotalFlux

    @property
    def TotalRequest(self):
        return self._TotalRequest

    @TotalRequest.setter
    def TotalRequest(self, TotalRequest):
        self._TotalRequest = TotalRequest

    @property
    def AvgFluxPerSecond(self):
        return self._AvgFluxPerSecond

    @AvgFluxPerSecond.setter
    def AvgFluxPerSecond(self, AvgFluxPerSecond):
        self._AvgFluxPerSecond = AvgFluxPerSecond


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TotalFlux = params.get("TotalFlux")
        self._TotalRequest = params.get("TotalRequest")
        self._AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishTime(AbstractModel):
    """推流时间。

    """

    def __init__(self):
        r"""
        :param _PublishTime: 推流时间。
UTC 格式，例如：2018-06-29T19:00:00Z。
        :type PublishTime: str
        """
        self._PublishTime = None

    @property
    def PublishTime(self):
        return self._PublishTime

    @PublishTime.setter
    def PublishTime(self, PublishTime):
        self._PublishTime = PublishTime


    def _deserialize(self, params):
        self._PublishTime = params.get("PublishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullPushWatermarkInfo(AbstractModel):
    """云转推水印信息。

    """

    def __init__(self):
        r"""
        :param _PictureUrl: 水印图片 URL。
URL中禁止包含的字符：
;(){}$>`#"'|
        :type PictureUrl: str
        :param _XPosition: 显示位置，X轴偏移，单位是百分比，默认 0。
        :type XPosition: int
        :param _YPosition: 显示位置，Y轴偏移，单位是百分比，默认 0。
        :type YPosition: int
        :param _Width: 水印宽度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始宽度。
        :type Width: int
        :param _Height: 水印高度，占直播原始画面高度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始高度。
        :type Height: int
        :param _Location: 水印位置，默认 0。
0：左上角。
1：右上角。
2：右下角。
3：左下角。
        :type Location: int
        """
        self._PictureUrl = None
        self._XPosition = None
        self._YPosition = None
        self._Width = None
        self._Height = None
        self._Location = None

    @property
    def PictureUrl(self):
        return self._PictureUrl

    @PictureUrl.setter
    def PictureUrl(self, PictureUrl):
        self._PictureUrl = PictureUrl

    @property
    def XPosition(self):
        return self._XPosition

    @XPosition.setter
    def XPosition(self, XPosition):
        self._XPosition = XPosition

    @property
    def YPosition(self):
        return self._YPosition

    @YPosition.setter
    def YPosition(self, YPosition):
        self._YPosition = YPosition

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._PictureUrl = params.get("PictureUrl")
        self._XPosition = params.get("XPosition")
        self._YPosition = params.get("YPosition")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullStreamConfig(AbstractModel):
    """拉流配置。

    """

    def __init__(self):
        r"""
        :param _ConfigId: 拉流配置 ID。
        :type ConfigId: str
        :param _FromUrl: 源 URL。
        :type FromUrl: str
        :param _ToUrl: 目的 URL。
        :type ToUrl: str
        :param _AreaName: 区域名。
        :type AreaName: str
        :param _IspName: 运营商名。
        :type IspName: str
        :param _StartTime: 开始时间。
UTC格式时间，例如: 2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param _EndTime: 结束时间。

UTC格式时间，例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param _Status: 状态:
0: 无效。
1: 初始状态。
2: 正在运行。
3: 拉起失败。
4: 暂停。
        :type Status: str
        """
        self._ConfigId = None
        self._FromUrl = None
        self._ToUrl = None
        self._AreaName = None
        self._IspName = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def FromUrl(self):
        return self._FromUrl

    @FromUrl.setter
    def FromUrl(self, FromUrl):
        self._FromUrl = FromUrl

    @property
    def ToUrl(self):
        return self._ToUrl

    @ToUrl.setter
    def ToUrl(self, ToUrl):
        self._ToUrl = ToUrl

    @property
    def AreaName(self):
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def IspName(self):
        return self._IspName

    @IspName.setter
    def IspName(self, IspName):
        self._IspName = IspName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._FromUrl = params.get("FromUrl")
        self._ToUrl = params.get("ToUrl")
        self._AreaName = params.get("AreaName")
        self._IspName = params.get("IspName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullStreamTaskInfo(AbstractModel):
    """直播拉流任务信息。

    """

    def __init__(self):
        r"""
        :param _TaskId: 拉流任务Id。
        :type TaskId: str
        :param _SourceType: 拉流源的类型：
PullLivePushLive -直播，
PullVodPushLive -点播，
PullPicPushLive -图片。
        :type SourceType: str
        :param _SourceUrls: 拉流源url列表。
SourceType为直播（PullLiveToLive）只可以填1个，
SourceType为点播（PullVodToLive）可以填多个，上限10个。
        :type SourceUrls: list of str
        :param _DomainName: 推流域名。
将拉到的源推到该域名。
        :type DomainName: str
        :param _AppName: 推流路径。
将拉到的源推到该路径。
        :type AppName: str
        :param _StreamName: 流名称。
将拉到的源推到该流名称。
        :type StreamName: str
        :param _PushArgs: 推流参数。
推流携带的自定义参数。
        :type PushArgs: str
        :param _StartTime: 开始时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param _EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param _Region: 任务创建所在地域：
ap-beijing - 华北地区(北京)，
ap-shanghai -华东地区(上海)，
ap-guangzhou -华南地区(广州)，
ap-mumbai - 印度，
ap-hongkong - 香港，
eu-frankfurt - 德国，
ap-seoul - 韩国，
ap-bangkok - 泰国，
ap-singapore - 新加坡，
na-siliconvalley - 美西，
na-ashburn - 美东，
ap-tokyo - 日本。
        :type Region: str
        :param _VodLoopTimes: 点播拉流转推循环次数。
-1：无限循环，直到任务结束。
0：不循环。
>0：具体循环次数。次数和时间以先结束的为准。
注意：拉流源为点播，该配置生效。
        :type VodLoopTimes: int
        :param _VodRefreshType: 点播更新SourceUrls后的播放方式：
ImmediateNewSource：立即从更新的拉流源开始播放；
ContinueBreakPoint：从上次断流url源的断点处继续，结束后再使用新的拉流源。

注意：拉流源为点播，该配置生效。
        :type VodRefreshType: str
        :param _CreateTime: 任务创建时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param _UpdateTime: 任务更新时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        :param _CreateBy: 创建任务的操作者。
        :type CreateBy: str
        :param _UpdateBy: 最后更新任务的操作者。
        :type UpdateBy: str
        :param _CallbackUrl: 回调地址。
        :type CallbackUrl: str
        :param _CallbackEvents: 选择需要回调的事件：
TaskStart：任务启动回调，
TaskExit：任务停止回调，
VodSourceFileStart：从点播源文件开始拉流回调，
VodSourceFileFinish：从点播源文件拉流结束回调，
ResetTaskConfig：任务更新回调。
        :type CallbackEvents: list of str
        :param _CallbackInfo: 注意：该信息暂不返回。
最后一次回调信息。
        :type CallbackInfo: str
        :param _ErrorInfo: 注意：该信息暂不返回。
错误信息。
        :type ErrorInfo: str
        :param _Status: 状态。
enable：生效中。
pause：暂停中。
        :type Status: str
        :param _RecentPullInfo: 注意：该信息仅在查询单个任务时返回。
任务最新拉流信息。
包含：源 url，偏移时间，上报时间。
        :type RecentPullInfo: :class:`tencentcloud.live.v20180801.models.RecentPullInfo`
        :param _Comment: 任务备注信息。
        :type Comment: str
        :param _BackupSourceType: 备源类型：
PullLivePushLive -直播，
PullVodPushLive -点播。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSourceType: str
        :param _BackupSourceUrl: 备源URL。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSourceUrl: str
        :param _WatermarkList: 水印信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkList: list of PullPushWatermarkInfo
        :param _VodLocalMode: 点播源是否启用本地推流模式，默认0，不启用。
0 - 不启用。
1 - 启用。
注意：此字段可能返回 null，表示取不到有效值。
        :type VodLocalMode: int
        :param _RecordTemplateId: 录制模板 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordTemplateId: str
        """
        self._TaskId = None
        self._SourceType = None
        self._SourceUrls = None
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._PushArgs = None
        self._StartTime = None
        self._EndTime = None
        self._Region = None
        self._VodLoopTimes = None
        self._VodRefreshType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CreateBy = None
        self._UpdateBy = None
        self._CallbackUrl = None
        self._CallbackEvents = None
        self._CallbackInfo = None
        self._ErrorInfo = None
        self._Status = None
        self._RecentPullInfo = None
        self._Comment = None
        self._BackupSourceType = None
        self._BackupSourceUrl = None
        self._WatermarkList = None
        self._VodLocalMode = None
        self._RecordTemplateId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceUrls(self):
        return self._SourceUrls

    @SourceUrls.setter
    def SourceUrls(self, SourceUrls):
        self._SourceUrls = SourceUrls

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def PushArgs(self):
        return self._PushArgs

    @PushArgs.setter
    def PushArgs(self, PushArgs):
        self._PushArgs = PushArgs

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VodLoopTimes(self):
        return self._VodLoopTimes

    @VodLoopTimes.setter
    def VodLoopTimes(self, VodLoopTimes):
        self._VodLoopTimes = VodLoopTimes

    @property
    def VodRefreshType(self):
        return self._VodRefreshType

    @VodRefreshType.setter
    def VodRefreshType(self, VodRefreshType):
        self._VodRefreshType = VodRefreshType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateBy(self):
        return self._CreateBy

    @CreateBy.setter
    def CreateBy(self, CreateBy):
        self._CreateBy = CreateBy

    @property
    def UpdateBy(self):
        return self._UpdateBy

    @UpdateBy.setter
    def UpdateBy(self, UpdateBy):
        self._UpdateBy = UpdateBy

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def CallbackEvents(self):
        return self._CallbackEvents

    @CallbackEvents.setter
    def CallbackEvents(self, CallbackEvents):
        self._CallbackEvents = CallbackEvents

    @property
    def CallbackInfo(self):
        return self._CallbackInfo

    @CallbackInfo.setter
    def CallbackInfo(self, CallbackInfo):
        self._CallbackInfo = CallbackInfo

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RecentPullInfo(self):
        return self._RecentPullInfo

    @RecentPullInfo.setter
    def RecentPullInfo(self, RecentPullInfo):
        self._RecentPullInfo = RecentPullInfo

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def BackupSourceType(self):
        return self._BackupSourceType

    @BackupSourceType.setter
    def BackupSourceType(self, BackupSourceType):
        self._BackupSourceType = BackupSourceType

    @property
    def BackupSourceUrl(self):
        return self._BackupSourceUrl

    @BackupSourceUrl.setter
    def BackupSourceUrl(self, BackupSourceUrl):
        self._BackupSourceUrl = BackupSourceUrl

    @property
    def WatermarkList(self):
        return self._WatermarkList

    @WatermarkList.setter
    def WatermarkList(self, WatermarkList):
        self._WatermarkList = WatermarkList

    @property
    def VodLocalMode(self):
        return self._VodLocalMode

    @VodLocalMode.setter
    def VodLocalMode(self, VodLocalMode):
        self._VodLocalMode = VodLocalMode

    @property
    def RecordTemplateId(self):
        return self._RecordTemplateId

    @RecordTemplateId.setter
    def RecordTemplateId(self, RecordTemplateId):
        self._RecordTemplateId = RecordTemplateId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SourceType = params.get("SourceType")
        self._SourceUrls = params.get("SourceUrls")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._PushArgs = params.get("PushArgs")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Region = params.get("Region")
        self._VodLoopTimes = params.get("VodLoopTimes")
        self._VodRefreshType = params.get("VodRefreshType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateBy = params.get("CreateBy")
        self._UpdateBy = params.get("UpdateBy")
        self._CallbackUrl = params.get("CallbackUrl")
        self._CallbackEvents = params.get("CallbackEvents")
        self._CallbackInfo = params.get("CallbackInfo")
        self._ErrorInfo = params.get("ErrorInfo")
        self._Status = params.get("Status")
        if params.get("RecentPullInfo") is not None:
            self._RecentPullInfo = RecentPullInfo()
            self._RecentPullInfo._deserialize(params.get("RecentPullInfo"))
        self._Comment = params.get("Comment")
        self._BackupSourceType = params.get("BackupSourceType")
        self._BackupSourceUrl = params.get("BackupSourceUrl")
        if params.get("WatermarkList") is not None:
            self._WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = PullPushWatermarkInfo()
                obj._deserialize(item)
                self._WatermarkList.append(obj)
        self._VodLocalMode = params.get("VodLocalMode")
        self._RecordTemplateId = params.get("RecordTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushAuthKeyInfo(AbstractModel):
    """推流鉴权key信息。

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名。
        :type DomainName: str
        :param _Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param _MasterAuthKey: 主鉴权 Key。
        :type MasterAuthKey: str
        :param _BackupAuthKey: 备鉴权 Key。
        :type BackupAuthKey: str
        :param _AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        """
        self._DomainName = None
        self._Enable = None
        self._MasterAuthKey = None
        self._BackupAuthKey = None
        self._AuthDelta = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def MasterAuthKey(self):
        return self._MasterAuthKey

    @MasterAuthKey.setter
    def MasterAuthKey(self, MasterAuthKey):
        self._MasterAuthKey = MasterAuthKey

    @property
    def BackupAuthKey(self):
        return self._BackupAuthKey

    @BackupAuthKey.setter
    def BackupAuthKey(self, BackupAuthKey):
        self._BackupAuthKey = BackupAuthKey

    @property
    def AuthDelta(self):
        return self._AuthDelta

    @AuthDelta.setter
    def AuthDelta(self, AuthDelta):
        self._AuthDelta = AuthDelta


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Enable = params.get("Enable")
        self._MasterAuthKey = params.get("MasterAuthKey")
        self._BackupAuthKey = params.get("BackupAuthKey")
        self._AuthDelta = params.get("AuthDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushDataInfo(AbstractModel):
    """推流数据信息

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _ClientIp: 推流客户端 IP。
        :type ClientIp: str
        :param _ServerIp: 接流服务器 IP。
        :type ServerIp: str
        :param _VideoFps: 推流视频帧率，单位: Hz。
        :type VideoFps: int
        :param _VideoSpeed: 推流视频码率，单位: bps。
        :type VideoSpeed: int
        :param _AudioFps: 推流音频帧率，单位: Hz。
        :type AudioFps: int
        :param _AudioSpeed: 推流音频码率，单位: bps。
        :type AudioSpeed: int
        :param _PushDomain: 推流域名。
        :type PushDomain: str
        :param _BeginPushTime: 推流开始时间。
        :type BeginPushTime: str
        :param _Acodec: 音频编码格式，
例："AAC"。
        :type Acodec: str
        :param _Vcodec: 视频编码格式，
例："H264"。
        :type Vcodec: str
        :param _Resolution: 分辨率。
        :type Resolution: str
        :param _AsampleRate: 采样率。
        :type AsampleRate: int
        :param _MetaAudioSpeed: metadata 中的音频码率，单位: bps。
        :type MetaAudioSpeed: int
        :param _MetaVideoSpeed: metadata 中的视频码率，单位: bps。
        :type MetaVideoSpeed: int
        :param _MetaFps: metadata 中的帧率。
        :type MetaFps: int
        """
        self._StreamName = None
        self._AppName = None
        self._ClientIp = None
        self._ServerIp = None
        self._VideoFps = None
        self._VideoSpeed = None
        self._AudioFps = None
        self._AudioSpeed = None
        self._PushDomain = None
        self._BeginPushTime = None
        self._Acodec = None
        self._Vcodec = None
        self._Resolution = None
        self._AsampleRate = None
        self._MetaAudioSpeed = None
        self._MetaVideoSpeed = None
        self._MetaFps = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def ServerIp(self):
        return self._ServerIp

    @ServerIp.setter
    def ServerIp(self, ServerIp):
        self._ServerIp = ServerIp

    @property
    def VideoFps(self):
        return self._VideoFps

    @VideoFps.setter
    def VideoFps(self, VideoFps):
        self._VideoFps = VideoFps

    @property
    def VideoSpeed(self):
        return self._VideoSpeed

    @VideoSpeed.setter
    def VideoSpeed(self, VideoSpeed):
        self._VideoSpeed = VideoSpeed

    @property
    def AudioFps(self):
        return self._AudioFps

    @AudioFps.setter
    def AudioFps(self, AudioFps):
        self._AudioFps = AudioFps

    @property
    def AudioSpeed(self):
        return self._AudioSpeed

    @AudioSpeed.setter
    def AudioSpeed(self, AudioSpeed):
        self._AudioSpeed = AudioSpeed

    @property
    def PushDomain(self):
        return self._PushDomain

    @PushDomain.setter
    def PushDomain(self, PushDomain):
        self._PushDomain = PushDomain

    @property
    def BeginPushTime(self):
        return self._BeginPushTime

    @BeginPushTime.setter
    def BeginPushTime(self, BeginPushTime):
        self._BeginPushTime = BeginPushTime

    @property
    def Acodec(self):
        return self._Acodec

    @Acodec.setter
    def Acodec(self, Acodec):
        self._Acodec = Acodec

    @property
    def Vcodec(self):
        return self._Vcodec

    @Vcodec.setter
    def Vcodec(self, Vcodec):
        self._Vcodec = Vcodec

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def AsampleRate(self):
        return self._AsampleRate

    @AsampleRate.setter
    def AsampleRate(self, AsampleRate):
        self._AsampleRate = AsampleRate

    @property
    def MetaAudioSpeed(self):
        return self._MetaAudioSpeed

    @MetaAudioSpeed.setter
    def MetaAudioSpeed(self, MetaAudioSpeed):
        self._MetaAudioSpeed = MetaAudioSpeed

    @property
    def MetaVideoSpeed(self):
        return self._MetaVideoSpeed

    @MetaVideoSpeed.setter
    def MetaVideoSpeed(self, MetaVideoSpeed):
        self._MetaVideoSpeed = MetaVideoSpeed

    @property
    def MetaFps(self):
        return self._MetaFps

    @MetaFps.setter
    def MetaFps(self, MetaFps):
        self._MetaFps = MetaFps


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._AppName = params.get("AppName")
        self._ClientIp = params.get("ClientIp")
        self._ServerIp = params.get("ServerIp")
        self._VideoFps = params.get("VideoFps")
        self._VideoSpeed = params.get("VideoSpeed")
        self._AudioFps = params.get("AudioFps")
        self._AudioSpeed = params.get("AudioSpeed")
        self._PushDomain = params.get("PushDomain")
        self._BeginPushTime = params.get("BeginPushTime")
        self._Acodec = params.get("Acodec")
        self._Vcodec = params.get("Vcodec")
        self._Resolution = params.get("Resolution")
        self._AsampleRate = params.get("AsampleRate")
        self._MetaAudioSpeed = params.get("MetaAudioSpeed")
        self._MetaVideoSpeed = params.get("MetaVideoSpeed")
        self._MetaFps = params.get("MetaFps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushQualityData(AbstractModel):
    """某条流的推流质量详情数据。

    """

    def __init__(self):
        r"""
        :param _Time: 数据时间，格式: %Y-%m-%d %H:%M:%S.%ms，精确到毫秒级。
        :type Time: str
        :param _PushDomain: 推流域名。
        :type PushDomain: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _ClientIp: 推流客户端 IP。
        :type ClientIp: str
        :param _BeginPushTime: 开始推流时间，格式: %Y-%m-%d %H:%M:%S.%ms，精确到毫秒级。
        :type BeginPushTime: str
        :param _Resolution: 分辨率信息。
        :type Resolution: str
        :param _VCodec: 视频编码格式。
        :type VCodec: str
        :param _ACodec: 音频编码格式。
        :type ACodec: str
        :param _Sequence: 推流序列号，用来唯一的标志一次推流。
        :type Sequence: str
        :param _VideoFps: 视频帧率。
        :type VideoFps: int
        :param _VideoRate: 视频码率，单位: bps。
        :type VideoRate: int
        :param _AudioFps: 音频帧率。
        :type AudioFps: int
        :param _AudioRate: 音频码率，单位: bps。
        :type AudioRate: int
        :param _LocalTs: 本地流逝时间，单位: ms，音视频流逝时间与本地流逝时间的差距越大表示推流质量越差，上行卡顿越严重。
        :type LocalTs: int
        :param _VideoTs: 视频流逝时间，单位: ms。
        :type VideoTs: int
        :param _AudioTs: 音频流逝时间，单位: ms。
        :type AudioTs: int
        :param _MetaVideoRate: metadata 中的视频码率，单位: kbps。
        :type MetaVideoRate: int
        :param _MetaAudioRate: metadata 中的音频码率，单位: kbps。
        :type MetaAudioRate: int
        :param _MateFps: metadata 中的帧率。
        :type MateFps: int
        :param _StreamParam: 推流参数
        :type StreamParam: str
        :param _Bandwidth: 带宽，单位Mbps。
        :type Bandwidth: float
        :param _Flux: 流量，单位MB。
        :type Flux: float
        :param _ServerIp: 推流服务端 IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerIp: str
        """
        self._Time = None
        self._PushDomain = None
        self._AppName = None
        self._ClientIp = None
        self._BeginPushTime = None
        self._Resolution = None
        self._VCodec = None
        self._ACodec = None
        self._Sequence = None
        self._VideoFps = None
        self._VideoRate = None
        self._AudioFps = None
        self._AudioRate = None
        self._LocalTs = None
        self._VideoTs = None
        self._AudioTs = None
        self._MetaVideoRate = None
        self._MetaAudioRate = None
        self._MateFps = None
        self._StreamParam = None
        self._Bandwidth = None
        self._Flux = None
        self._ServerIp = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def PushDomain(self):
        return self._PushDomain

    @PushDomain.setter
    def PushDomain(self, PushDomain):
        self._PushDomain = PushDomain

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def BeginPushTime(self):
        return self._BeginPushTime

    @BeginPushTime.setter
    def BeginPushTime(self, BeginPushTime):
        self._BeginPushTime = BeginPushTime

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def VCodec(self):
        return self._VCodec

    @VCodec.setter
    def VCodec(self, VCodec):
        self._VCodec = VCodec

    @property
    def ACodec(self):
        return self._ACodec

    @ACodec.setter
    def ACodec(self, ACodec):
        self._ACodec = ACodec

    @property
    def Sequence(self):
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def VideoFps(self):
        return self._VideoFps

    @VideoFps.setter
    def VideoFps(self, VideoFps):
        self._VideoFps = VideoFps

    @property
    def VideoRate(self):
        return self._VideoRate

    @VideoRate.setter
    def VideoRate(self, VideoRate):
        self._VideoRate = VideoRate

    @property
    def AudioFps(self):
        return self._AudioFps

    @AudioFps.setter
    def AudioFps(self, AudioFps):
        self._AudioFps = AudioFps

    @property
    def AudioRate(self):
        return self._AudioRate

    @AudioRate.setter
    def AudioRate(self, AudioRate):
        self._AudioRate = AudioRate

    @property
    def LocalTs(self):
        return self._LocalTs

    @LocalTs.setter
    def LocalTs(self, LocalTs):
        self._LocalTs = LocalTs

    @property
    def VideoTs(self):
        return self._VideoTs

    @VideoTs.setter
    def VideoTs(self, VideoTs):
        self._VideoTs = VideoTs

    @property
    def AudioTs(self):
        return self._AudioTs

    @AudioTs.setter
    def AudioTs(self, AudioTs):
        self._AudioTs = AudioTs

    @property
    def MetaVideoRate(self):
        return self._MetaVideoRate

    @MetaVideoRate.setter
    def MetaVideoRate(self, MetaVideoRate):
        self._MetaVideoRate = MetaVideoRate

    @property
    def MetaAudioRate(self):
        return self._MetaAudioRate

    @MetaAudioRate.setter
    def MetaAudioRate(self, MetaAudioRate):
        self._MetaAudioRate = MetaAudioRate

    @property
    def MateFps(self):
        return self._MateFps

    @MateFps.setter
    def MateFps(self, MateFps):
        self._MateFps = MateFps

    @property
    def StreamParam(self):
        return self._StreamParam

    @StreamParam.setter
    def StreamParam(self, StreamParam):
        self._StreamParam = StreamParam

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Flux(self):
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux

    @property
    def ServerIp(self):
        return self._ServerIp

    @ServerIp.setter
    def ServerIp(self, ServerIp):
        self._ServerIp = ServerIp


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._PushDomain = params.get("PushDomain")
        self._AppName = params.get("AppName")
        self._ClientIp = params.get("ClientIp")
        self._BeginPushTime = params.get("BeginPushTime")
        self._Resolution = params.get("Resolution")
        self._VCodec = params.get("VCodec")
        self._ACodec = params.get("ACodec")
        self._Sequence = params.get("Sequence")
        self._VideoFps = params.get("VideoFps")
        self._VideoRate = params.get("VideoRate")
        self._AudioFps = params.get("AudioFps")
        self._AudioRate = params.get("AudioRate")
        self._LocalTs = params.get("LocalTs")
        self._VideoTs = params.get("VideoTs")
        self._AudioTs = params.get("AudioTs")
        self._MetaVideoRate = params.get("MetaVideoRate")
        self._MetaAudioRate = params.get("MetaAudioRate")
        self._MateFps = params.get("MateFps")
        self._StreamParam = params.get("StreamParam")
        self._Bandwidth = params.get("Bandwidth")
        self._Flux = params.get("Flux")
        self._ServerIp = params.get("ServerIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecentPullInfo(AbstractModel):
    """直播拉流当前正在拉的文件信息。

    """

    def __init__(self):
        r"""
        :param _FileUrl: 当前正在拉的文件地址。
        :type FileUrl: str
        :param _OffsetTime: 当前正在拉的文件偏移，单位：秒。
        :type OffsetTime: int
        :param _ReportTime: 最新上报偏移信息时间。UTC格式。
如：2020-07-23T03:20:39Z。
注意：与北京时间相差八小时。
        :type ReportTime: str
        :param _LoopedTimes: 已经轮播的次数。
        :type LoopedTimes: int
        """
        self._FileUrl = None
        self._OffsetTime = None
        self._ReportTime = None
        self._LoopedTimes = None

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def OffsetTime(self):
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def ReportTime(self):
        return self._ReportTime

    @ReportTime.setter
    def ReportTime(self, ReportTime):
        self._ReportTime = ReportTime

    @property
    def LoopedTimes(self):
        return self._LoopedTimes

    @LoopedTimes.setter
    def LoopedTimes(self, LoopedTimes):
        self._LoopedTimes = LoopedTimes


    def _deserialize(self, params):
        self._FileUrl = params.get("FileUrl")
        self._OffsetTime = params.get("OffsetTime")
        self._ReportTime = params.get("ReportTime")
        self._LoopedTimes = params.get("LoopedTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordParam(AbstractModel):
    """录制模板参数。

    """

    def __init__(self):
        r"""
        :param _RecordInterval: 录制间隔。
单位秒，默认：1800。
取值范围：30-7200。
此参数对 HLS 无效，当录制 HLS 时从推流到断流生成一个文件。
        :type RecordInterval: int
        :param _StorageTime: 录制存储时长。
单位秒，取值范围： 0 - 1500天。
0：表示永久存储。
        :type StorageTime: int
        :param _Enable: 是否开启当前格式录制，默认值为0，0：否， 1：是。
        :type Enable: int
        :param _VodSubAppId: 点播子应用 ID。
        :type VodSubAppId: int
        :param _VodFileName: 录制文件名。
支持的特殊占位符有：
{StreamID}: 流ID
{StartYear}: 开始时间-年
{StartMonth}: 开始时间-月
{StartDay}: 开始时间-日
{StartHour}: 开始时间-小时
{StartMinute}: 开始时间-分钟
{StartSecond}: 开始时间-秒
{StartMillisecond}: 开始时间-毫秒
{EndYear}: 结束时间-年
{EndMonth}: 结束时间-月
{EndDay}: 结束时间-日
{EndHour}: 结束时间-小时
{EndMinute}: 结束时间-分钟
{EndSecond}: 结束时间-秒
{EndMillisecond}: 结束时间-毫秒

若未设置默认录制文件名为{StreamID}_{StartYear}-{StartMonth}-{StartDay}-{StartHour}-{StartMinute}-{StartSecond}_{EndYear}-{EndMonth}-{EndDay}-{EndHour}-{EndMinute}-{EndSecond}
        :type VodFileName: str
        :param _Procedure: 任务流
注意：此字段可能返回 null，表示取不到有效值。
        :type Procedure: str
        :param _StorageMode: 视频存储策略。
normal：标准存储。
cold：低频存储。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageMode: str
        :param _ClassId: 点播应用分类
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassId: int
        """
        self._RecordInterval = None
        self._StorageTime = None
        self._Enable = None
        self._VodSubAppId = None
        self._VodFileName = None
        self._Procedure = None
        self._StorageMode = None
        self._ClassId = None

    @property
    def RecordInterval(self):
        return self._RecordInterval

    @RecordInterval.setter
    def RecordInterval(self, RecordInterval):
        self._RecordInterval = RecordInterval

    @property
    def StorageTime(self):
        return self._StorageTime

    @StorageTime.setter
    def StorageTime(self, StorageTime):
        self._StorageTime = StorageTime

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def VodSubAppId(self):
        return self._VodSubAppId

    @VodSubAppId.setter
    def VodSubAppId(self, VodSubAppId):
        self._VodSubAppId = VodSubAppId

    @property
    def VodFileName(self):
        return self._VodFileName

    @VodFileName.setter
    def VodFileName(self, VodFileName):
        self._VodFileName = VodFileName

    @property
    def Procedure(self):
        return self._Procedure

    @Procedure.setter
    def Procedure(self, Procedure):
        self._Procedure = Procedure

    @property
    def StorageMode(self):
        return self._StorageMode

    @StorageMode.setter
    def StorageMode(self, StorageMode):
        self._StorageMode = StorageMode

    @property
    def ClassId(self):
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId


    def _deserialize(self, params):
        self._RecordInterval = params.get("RecordInterval")
        self._StorageTime = params.get("StorageTime")
        self._Enable = params.get("Enable")
        self._VodSubAppId = params.get("VodSubAppId")
        self._VodFileName = params.get("VodFileName")
        self._Procedure = params.get("Procedure")
        self._StorageMode = params.get("StorageMode")
        self._ClassId = params.get("ClassId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTask(AbstractModel):
    """录制任务

    """

    def __init__(self):
        r"""
        :param _TaskId: 录制任务ID。
        :type TaskId: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _StartTime: 任务开始时间，Unix时间戳。
        :type StartTime: int
        :param _EndTime: 任务结束时间，Unix时间戳。
        :type EndTime: int
        :param _TemplateId: 录制模板ID。
        :type TemplateId: int
        :param _Stopped: 调用 StopRecordTask 停止任务时间，Unix时间戳。值为0表示未曾调用接口停止任务。
        :type Stopped: int
        """
        self._TaskId = None
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._StartTime = None
        self._EndTime = None
        self._TemplateId = None
        self._Stopped = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Stopped(self):
        return self._Stopped

    @Stopped.setter
    def Stopped(self, Stopped):
        self._Stopped = Stopped


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TemplateId = params.get("TemplateId")
        self._Stopped = params.get("Stopped")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTemplateInfo(AbstractModel):
    """录制模板信息

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _Description: 描述信息。
        :type Description: str
        :param _FlvParam: FLV 录制参数。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _HlsParam: HLS 录制参数。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _Mp4Param: MP4 录制参数。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _AacParam: AAC 录制参数。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param _HlsSpecialParam: HLS 录制定制参数。
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param _Mp3Param: MP3 录制参数。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param _RemoveWatermark: 是否去除水印。
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoveWatermark: bool
        :param _FlvSpecialParam: FLV 录制定制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlvSpecialParam: :class:`tencentcloud.live.v20180801.models.FlvSpecialParam`
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._FlvParam = None
        self._HlsParam = None
        self._Mp4Param = None
        self._AacParam = None
        self._IsDelayLive = None
        self._HlsSpecialParam = None
        self._Mp3Param = None
        self._RemoveWatermark = None
        self._FlvSpecialParam = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def FlvParam(self):
        return self._FlvParam

    @FlvParam.setter
    def FlvParam(self, FlvParam):
        self._FlvParam = FlvParam

    @property
    def HlsParam(self):
        return self._HlsParam

    @HlsParam.setter
    def HlsParam(self, HlsParam):
        self._HlsParam = HlsParam

    @property
    def Mp4Param(self):
        return self._Mp4Param

    @Mp4Param.setter
    def Mp4Param(self, Mp4Param):
        self._Mp4Param = Mp4Param

    @property
    def AacParam(self):
        return self._AacParam

    @AacParam.setter
    def AacParam(self, AacParam):
        self._AacParam = AacParam

    @property
    def IsDelayLive(self):
        return self._IsDelayLive

    @IsDelayLive.setter
    def IsDelayLive(self, IsDelayLive):
        self._IsDelayLive = IsDelayLive

    @property
    def HlsSpecialParam(self):
        return self._HlsSpecialParam

    @HlsSpecialParam.setter
    def HlsSpecialParam(self, HlsSpecialParam):
        self._HlsSpecialParam = HlsSpecialParam

    @property
    def Mp3Param(self):
        return self._Mp3Param

    @Mp3Param.setter
    def Mp3Param(self, Mp3Param):
        self._Mp3Param = Mp3Param

    @property
    def RemoveWatermark(self):
        return self._RemoveWatermark

    @RemoveWatermark.setter
    def RemoveWatermark(self, RemoveWatermark):
        self._RemoveWatermark = RemoveWatermark

    @property
    def FlvSpecialParam(self):
        return self._FlvSpecialParam

    @FlvSpecialParam.setter
    def FlvSpecialParam(self, FlvSpecialParam):
        self._FlvSpecialParam = FlvSpecialParam


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self._FlvParam = RecordParam()
            self._FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self._HlsParam = RecordParam()
            self._HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self._Mp4Param = RecordParam()
            self._Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self._AacParam = RecordParam()
            self._AacParam._deserialize(params.get("AacParam"))
        self._IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self._HlsSpecialParam = HlsSpecialParam()
            self._HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self._Mp3Param = RecordParam()
            self._Mp3Param._deserialize(params.get("Mp3Param"))
        self._RemoveWatermark = params.get("RemoveWatermark")
        if params.get("FlvSpecialParam") is not None:
            self._FlvSpecialParam = FlvSpecialParam()
            self._FlvSpecialParam._deserialize(params.get("FlvSpecialParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefererAuthConfig(AbstractModel):
    """直播域名Referer黑白名单配置

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名。
        :type DomainName: str
        :param _Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param _Type: 名单类型，0：黑名单，1：白名单。
        :type Type: int
        :param _AllowEmpty: 是否允许空Referer，0：不允许，1：允许。
        :type AllowEmpty: int
        :param _Rules: 名单列表，以分号(;)分隔。
        :type Rules: str
        """
        self._DomainName = None
        self._Enable = None
        self._Type = None
        self._AllowEmpty = None
        self._Rules = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AllowEmpty(self):
        return self._AllowEmpty

    @AllowEmpty.setter
    def AllowEmpty(self, AllowEmpty):
        self._AllowEmpty = AllowEmpty

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Enable = params.get("Enable")
        self._Type = params.get("Type")
        self._AllowEmpty = params.get("AllowEmpty")
        self._Rules = params.get("Rules")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartLivePullStreamTaskRequest(AbstractModel):
    """RestartLivePullStreamTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id。
        :type TaskId: str
        :param _Operator: 操作人备注名称。
        :type Operator: str
        """
        self._TaskId = None
        self._Operator = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartLivePullStreamTaskResponse(AbstractModel):
    """RestartLivePullStreamTask返回参数结构体

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


class ResumeDelayLiveStreamRequest(AbstractModel):
    """ResumeDelayLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为live。
        :type AppName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        """
        self._AppName = None
        self._DomainName = None
        self._StreamName = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeDelayLiveStreamResponse(AbstractModel):
    """ResumeDelayLiveStream返回参数结构体

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


class ResumeLiveStreamRequest(AbstractModel):
    """ResumeLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param _DomainName: 您的推流域名。
        :type DomainName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        """
        self._AppName = None
        self._DomainName = None
        self._StreamName = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeLiveStreamResponse(AbstractModel):
    """ResumeLiveStream返回参数结构体

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


class RuleInfo(AbstractModel):
    """规则信息。

    """

    def __init__(self):
        r"""
        :param _CreateTime: 规则创建时间。
注：此字段为北京时间（UTC+8时区）。
        :type CreateTime: str
        :param _UpdateTime: 规则更新时间。
注：此字段为北京时间（UTC+8时区）。
        :type UpdateTime: str
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        """
        self._CreateTime = None
        self._UpdateTime = None
        self._TemplateId = None
        self._DomainName = None
        self._AppName = None
        self._StreamName = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TemplateId = params.get("TemplateId")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScreenshotTask(AbstractModel):
    """截图任务

    """

    def __init__(self):
        r"""
        :param _TaskId: 截图任务ID。
        :type TaskId: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _StartTime: 任务开始时间，Unix时间戳。
        :type StartTime: int
        :param _EndTime: 任务结束时间，Unix时间戳。
        :type EndTime: int
        :param _TemplateId: 截图模板ID。
        :type TemplateId: int
        :param _Stopped: 调用 StopScreenshotTask 停止任务时间，Unix时间戳。值为0表示未曾调用接口停止任务。
        :type Stopped: int
        """
        self._TaskId = None
        self._DomainName = None
        self._AppName = None
        self._StreamName = None
        self._StartTime = None
        self._EndTime = None
        self._TemplateId = None
        self._Stopped = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Stopped(self):
        return self._Stopped

    @Stopped.setter
    def Stopped(self, Stopped):
        self._Stopped = Stopped


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DomainName = params.get("DomainName")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TemplateId = params.get("TemplateId")
        self._Stopped = params.get("Stopped")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotTemplateInfo(AbstractModel):
    """截图模板信息。

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _SnapshotInterval: 截图时间间隔，5-300秒。
        :type SnapshotInterval: int
        :param _Width: 截图宽度，范围：0-3000。 
0：原始宽度并适配原始比例。
        :type Width: int
        :param _Height: 截图高度，范围：0-2000。
0：原始高度并适配原始比例。
        :type Height: int
        :param _PornFlag: 是否开启鉴黄，0：不开启，1：开启。
        :type PornFlag: int
        :param _CosAppId: Cos 应用 ID。
        :type CosAppId: int
        :param _CosBucket: Cos Bucket名称。
        :type CosBucket: str
        :param _CosRegion: Cos 地域。
        :type CosRegion: str
        :param _Description: 模板描述。
        :type Description: str
        :param _CosPrefix: Cos Bucket文件夹前缀。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPrefix: str
        :param _CosFileName: Cos 文件名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosFileName: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._SnapshotInterval = None
        self._Width = None
        self._Height = None
        self._PornFlag = None
        self._CosAppId = None
        self._CosBucket = None
        self._CosRegion = None
        self._Description = None
        self._CosPrefix = None
        self._CosFileName = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def SnapshotInterval(self):
        return self._SnapshotInterval

    @SnapshotInterval.setter
    def SnapshotInterval(self, SnapshotInterval):
        self._SnapshotInterval = SnapshotInterval

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def PornFlag(self):
        return self._PornFlag

    @PornFlag.setter
    def PornFlag(self, PornFlag):
        self._PornFlag = PornFlag

    @property
    def CosAppId(self):
        return self._CosAppId

    @CosAppId.setter
    def CosAppId(self, CosAppId):
        self._CosAppId = CosAppId

    @property
    def CosBucket(self):
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CosPrefix(self):
        return self._CosPrefix

    @CosPrefix.setter
    def CosPrefix(self, CosPrefix):
        self._CosPrefix = CosPrefix

    @property
    def CosFileName(self):
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._SnapshotInterval = params.get("SnapshotInterval")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._PornFlag = params.get("PornFlag")
        self._CosAppId = params.get("CosAppId")
        self._CosBucket = params.get("CosBucket")
        self._CosRegion = params.get("CosRegion")
        self._Description = params.get("Description")
        self._CosPrefix = params.get("CosPrefix")
        self._CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLiveStreamMonitorRequest(AbstractModel):
    """StartLiveStreamMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监播ID。
        :type MonitorId: str
        :param _AudibleInputIndexList: 监播画面声音InputIndex,支持多个输入声音。
取值范围 InputIndex必须已经存在。
不填默认无声音输出。
        :type AudibleInputIndexList: list of int non-negative
        """
        self._MonitorId = None
        self._AudibleInputIndexList = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def AudibleInputIndexList(self):
        return self._AudibleInputIndexList

    @AudibleInputIndexList.setter
    def AudibleInputIndexList(self, AudibleInputIndexList):
        self._AudibleInputIndexList = AudibleInputIndexList


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._AudibleInputIndexList = params.get("AudibleInputIndexList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLiveStreamMonitorResponse(AbstractModel):
    """StartLiveStreamMonitor返回参数结构体

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


class StopLiveRecordRequest(AbstractModel):
    """StopLiveRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _TaskId: 任务ID，由CreateLiveRecord接口返回。
        :type TaskId: int
        """
        self._StreamName = None
        self._TaskId = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLiveRecordResponse(AbstractModel):
    """StopLiveRecord返回参数结构体

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


class StopLiveStreamMonitorRequest(AbstractModel):
    """StopLiveStreamMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监播ID
        :type MonitorId: str
        """
        self._MonitorId = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLiveStreamMonitorResponse(AbstractModel):
    """StopLiveStreamMonitor返回参数结构体

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


class StopRecordTaskRequest(AbstractModel):
    """StopRecordTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 录制任务ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class StopRecordTaskResponse(AbstractModel):
    """StopRecordTask返回参数结构体

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


class StopScreenshotTaskRequest(AbstractModel):
    """StopScreenshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 截图任务ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class StopScreenshotTaskResponse(AbstractModel):
    """StopScreenshotTask返回参数结构体

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


class StreamEventInfo(AbstractModel):
    """推断流事件信息。

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _StreamStartTime: 推流开始时间。
UTC 格式时间，例如：2019-01-07T12:00:00Z。
        :type StreamStartTime: str
        :param _StreamEndTime: 推流结束时间。
UTC 格式时间，例如：2019-01-07T15:00:00Z。
        :type StreamEndTime: str
        :param _StopReason: 停止原因。
        :type StopReason: str
        :param _Duration: 推流持续时长，单位：秒。
        :type Duration: int
        :param _ClientIp: 主播 IP。
当客户端为内网推流时，展示为: - 。
        :type ClientIp: str
        :param _Resolution: 分辨率。
        :type Resolution: str
        """
        self._AppName = None
        self._DomainName = None
        self._StreamName = None
        self._StreamStartTime = None
        self._StreamEndTime = None
        self._StopReason = None
        self._Duration = None
        self._ClientIp = None
        self._Resolution = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def StreamStartTime(self):
        return self._StreamStartTime

    @StreamStartTime.setter
    def StreamStartTime(self, StreamStartTime):
        self._StreamStartTime = StreamStartTime

    @property
    def StreamEndTime(self):
        return self._StreamEndTime

    @StreamEndTime.setter
    def StreamEndTime(self, StreamEndTime):
        self._StreamEndTime = StreamEndTime

    @property
    def StopReason(self):
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamName = params.get("StreamName")
        self._StreamStartTime = params.get("StreamStartTime")
        self._StreamEndTime = params.get("StreamEndTime")
        self._StopReason = params.get("StopReason")
        self._Duration = params.get("Duration")
        self._ClientIp = params.get("ClientIp")
        self._Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamName(AbstractModel):
    """流名称列表。

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _AppName: 应用名称。
        :type AppName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _StreamStartTime: 推流开始时间。
UTC格式时间，例如：2019-01-07T12:00:00Z。
        :type StreamStartTime: str
        :param _StreamEndTime: 推流结束时间。
UTC格式时间，例如：2019-01-07T15:00:00Z。
        :type StreamEndTime: str
        :param _StopReason: 停止原因。
        :type StopReason: str
        :param _Duration: 推流持续时长，单位：秒。
        :type Duration: int
        :param _ClientIp: 主播 IP。
        :type ClientIp: str
        :param _Resolution: 分辨率。
        :type Resolution: str
        """
        self._StreamName = None
        self._AppName = None
        self._DomainName = None
        self._StreamStartTime = None
        self._StreamEndTime = None
        self._StopReason = None
        self._Duration = None
        self._ClientIp = None
        self._Resolution = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamStartTime(self):
        return self._StreamStartTime

    @StreamStartTime.setter
    def StreamStartTime(self, StreamStartTime):
        self._StreamStartTime = StreamStartTime

    @property
    def StreamEndTime(self):
        return self._StreamEndTime

    @StreamEndTime.setter
    def StreamEndTime(self, StreamEndTime):
        self._StreamEndTime = StreamEndTime

    @property
    def StopReason(self):
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamStartTime = params.get("StreamStartTime")
        self._StreamEndTime = params.get("StreamEndTime")
        self._StopReason = params.get("StopReason")
        self._Duration = params.get("Duration")
        self._ClientIp = params.get("ClientIp")
        self._Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamOnlineInfo(AbstractModel):
    """查询当前正在推流的信息

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _PublishTimeList: 推流时间列表
        :type PublishTimeList: list of PublishTime
        :param _AppName: 应用名称。
        :type AppName: str
        :param _DomainName: 推流域名。
        :type DomainName: str
        :param _PushToDelay: 流是否推送到延播。
0 - 无延播，
1 - 有延播。
注意：此字段可能返回 null，表示取不到有效值。
        :type PushToDelay: int
        """
        self._StreamName = None
        self._PublishTimeList = None
        self._AppName = None
        self._DomainName = None
        self._PushToDelay = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def PublishTimeList(self):
        return self._PublishTimeList

    @PublishTimeList.setter
    def PublishTimeList(self, PublishTimeList):
        self._PublishTimeList = PublishTimeList

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def PushToDelay(self):
        return self._PushToDelay

    @PushToDelay.setter
    def PushToDelay(self, PushToDelay):
        self._PushToDelay = PushToDelay


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        if params.get("PublishTimeList") is not None:
            self._PublishTimeList = []
            for item in params.get("PublishTimeList"):
                obj = PublishTime()
                obj._deserialize(item)
                self._PublishTimeList.append(obj)
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._PushToDelay = params.get("PushToDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatusInfo(AbstractModel):
    """直播拉流任务状态信息。

    """

    def __init__(self):
        r"""
        :param _FileUrl: 当前使用的源 URL。
        :type FileUrl: str
        :param _LoopedTimes: 点播源任务的轮播次数。
        :type LoopedTimes: int
        :param _OffsetTime: 点播源的播放偏移，单位：秒。
        :type OffsetTime: int
        :param _ReportTime: 最新心跳上报时间。UTC时间，例如：
2022-02-11T10:00:00Z。
注意：UTC时间与北京时间相差八小时。
        :type ReportTime: str
        :param _RunStatus: 实际运行状态：
active - 活跃，
inactive - 不活跃。
        :type RunStatus: str
        :param _FileDuration: 点播源的文件时长，单位：秒。
        :type FileDuration: int
        :param _NextFileUrl: 下一进度点播文件 URL。
        :type NextFileUrl: str
        """
        self._FileUrl = None
        self._LoopedTimes = None
        self._OffsetTime = None
        self._ReportTime = None
        self._RunStatus = None
        self._FileDuration = None
        self._NextFileUrl = None

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def LoopedTimes(self):
        return self._LoopedTimes

    @LoopedTimes.setter
    def LoopedTimes(self, LoopedTimes):
        self._LoopedTimes = LoopedTimes

    @property
    def OffsetTime(self):
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def ReportTime(self):
        return self._ReportTime

    @ReportTime.setter
    def ReportTime(self, ReportTime):
        self._ReportTime = ReportTime

    @property
    def RunStatus(self):
        return self._RunStatus

    @RunStatus.setter
    def RunStatus(self, RunStatus):
        self._RunStatus = RunStatus

    @property
    def FileDuration(self):
        return self._FileDuration

    @FileDuration.setter
    def FileDuration(self, FileDuration):
        self._FileDuration = FileDuration

    @property
    def NextFileUrl(self):
        return self._NextFileUrl

    @NextFileUrl.setter
    def NextFileUrl(self, NextFileUrl):
        self._NextFileUrl = NextFileUrl


    def _deserialize(self, params):
        self._FileUrl = params.get("FileUrl")
        self._LoopedTimes = params.get("LoopedTimes")
        self._OffsetTime = params.get("OffsetTime")
        self._ReportTime = params.get("ReportTime")
        self._RunStatus = params.get("RunStatus")
        self._FileDuration = params.get("FileDuration")
        self._NextFileUrl = params.get("NextFileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateInfo(AbstractModel):
    """转码模板信息。

    """

    def __init__(self):
        r"""
        :param _Vcodec: 视频编码：h264/h265/origin，默认h264。

origin: 保持原始编码格式
        :type Vcodec: str
        :param _VideoBitrate: 视频码率。范围：0kbps - 8000kbps。
0为保持原始码率。
注: 转码模板有码率唯一要求，最终保存的码率可能与输入码率有所差别。
        :type VideoBitrate: int
        :param _Acodec: 音频编码：aac，默认aac。
注意：当前该参数未生效，待后续支持！
        :type Acodec: str
        :param _AudioBitrate: 音频码率。取值范围：0kbps - 500kbps。
默认0。
        :type AudioBitrate: int
        :param _Width: 宽，默认0。
范围[0-3000]
数值必须是2的倍数，0是原始宽度
        :type Width: int
        :param _Height: 高，默认0。
范围[0-3000]
数值必须是2的倍数，0是原始宽度
        :type Height: int
        :param _Fps: 帧率，默认0。
范围0-60fps
        :type Fps: int
        :param _Gop: 关键帧间隔，单位：秒。
默认原始的间隔
范围2-6
        :type Gop: int
        :param _Rotate: 旋转角度，默认0。
可取值：0，90，180，270
        :type Rotate: int
        :param _Profile: 编码质量：
baseline/main/high。默认baseline
        :type Profile: str
        :param _BitrateToOrig: 当设置的码率>原始码率时，是否以原始码率为准。
0：否， 1：是
默认 0。
        :type BitrateToOrig: int
        :param _HeightToOrig: 当设置的高度>原始高度时，是否以原始高度为准。
0：否， 1：是
默认 0。
        :type HeightToOrig: int
        :param _FpsToOrig: 当设置的帧率>原始帧率时，是否以原始帧率为准。
0：否， 1：是
默认 0。
        :type FpsToOrig: int
        :param _NeedVideo: 是否保留视频。0：否，1：是。
        :type NeedVideo: int
        :param _NeedAudio: 是否保留音频。0：否，1：是。
        :type NeedAudio: int
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _Description: 模板描述。
        :type Description: str
        :param _AiTransCode: 是否是极速高清模板，0：否，1：是。默认0。
        :type AiTransCode: int
        :param _AdaptBitratePercent: 极速高清视频码率压缩比。
极速高清目标码率=VideoBitrate * (1-AdaptBitratePercent)

取值范围：0.0到0.5
        :type AdaptBitratePercent: float
        :param _ShortEdgeAsHeight: 是否以短边作为高度，0：否，1：是。默认0。
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortEdgeAsHeight: int
        :param _DRMType: DRM 加密类型，可选值：fairplay、normalaes、widevine。
注意：此字段可能返回 null，表示取不到有效值。
        :type DRMType: str
        :param _DRMTracks: DRM 加密项，多个用|分割，可选值：AUDIO、SD、HD、UHD1、UHD2，后四个为一组，同组中的内容只能选一个。
注意：此字段可能返回 null，表示取不到有效值。
        :type DRMTracks: str
        """
        self._Vcodec = None
        self._VideoBitrate = None
        self._Acodec = None
        self._AudioBitrate = None
        self._Width = None
        self._Height = None
        self._Fps = None
        self._Gop = None
        self._Rotate = None
        self._Profile = None
        self._BitrateToOrig = None
        self._HeightToOrig = None
        self._FpsToOrig = None
        self._NeedVideo = None
        self._NeedAudio = None
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._AiTransCode = None
        self._AdaptBitratePercent = None
        self._ShortEdgeAsHeight = None
        self._DRMType = None
        self._DRMTracks = None

    @property
    def Vcodec(self):
        return self._Vcodec

    @Vcodec.setter
    def Vcodec(self, Vcodec):
        self._Vcodec = Vcodec

    @property
    def VideoBitrate(self):
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def Acodec(self):
        return self._Acodec

    @Acodec.setter
    def Acodec(self, Acodec):
        self._Acodec = Acodec

    @property
    def AudioBitrate(self):
        return self._AudioBitrate

    @AudioBitrate.setter
    def AudioBitrate(self, AudioBitrate):
        self._AudioBitrate = AudioBitrate

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Gop(self):
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop

    @property
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate

    @property
    def Profile(self):
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def BitrateToOrig(self):
        return self._BitrateToOrig

    @BitrateToOrig.setter
    def BitrateToOrig(self, BitrateToOrig):
        self._BitrateToOrig = BitrateToOrig

    @property
    def HeightToOrig(self):
        return self._HeightToOrig

    @HeightToOrig.setter
    def HeightToOrig(self, HeightToOrig):
        self._HeightToOrig = HeightToOrig

    @property
    def FpsToOrig(self):
        return self._FpsToOrig

    @FpsToOrig.setter
    def FpsToOrig(self, FpsToOrig):
        self._FpsToOrig = FpsToOrig

    @property
    def NeedVideo(self):
        return self._NeedVideo

    @NeedVideo.setter
    def NeedVideo(self, NeedVideo):
        self._NeedVideo = NeedVideo

    @property
    def NeedAudio(self):
        return self._NeedAudio

    @NeedAudio.setter
    def NeedAudio(self, NeedAudio):
        self._NeedAudio = NeedAudio

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AiTransCode(self):
        return self._AiTransCode

    @AiTransCode.setter
    def AiTransCode(self, AiTransCode):
        self._AiTransCode = AiTransCode

    @property
    def AdaptBitratePercent(self):
        return self._AdaptBitratePercent

    @AdaptBitratePercent.setter
    def AdaptBitratePercent(self, AdaptBitratePercent):
        self._AdaptBitratePercent = AdaptBitratePercent

    @property
    def ShortEdgeAsHeight(self):
        return self._ShortEdgeAsHeight

    @ShortEdgeAsHeight.setter
    def ShortEdgeAsHeight(self, ShortEdgeAsHeight):
        self._ShortEdgeAsHeight = ShortEdgeAsHeight

    @property
    def DRMType(self):
        return self._DRMType

    @DRMType.setter
    def DRMType(self, DRMType):
        self._DRMType = DRMType

    @property
    def DRMTracks(self):
        return self._DRMTracks

    @DRMTracks.setter
    def DRMTracks(self, DRMTracks):
        self._DRMTracks = DRMTracks


    def _deserialize(self, params):
        self._Vcodec = params.get("Vcodec")
        self._VideoBitrate = params.get("VideoBitrate")
        self._Acodec = params.get("Acodec")
        self._AudioBitrate = params.get("AudioBitrate")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._Gop = params.get("Gop")
        self._Rotate = params.get("Rotate")
        self._Profile = params.get("Profile")
        self._BitrateToOrig = params.get("BitrateToOrig")
        self._HeightToOrig = params.get("HeightToOrig")
        self._FpsToOrig = params.get("FpsToOrig")
        self._NeedVideo = params.get("NeedVideo")
        self._NeedAudio = params.get("NeedAudio")
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._AiTransCode = params.get("AiTransCode")
        self._AdaptBitratePercent = params.get("AdaptBitratePercent")
        self._ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        self._DRMType = params.get("DRMType")
        self._DRMTracks = params.get("DRMTracks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeShiftBillData(AbstractModel):
    """时移计费明细数据。

    """

    def __init__(self):
        r"""
        :param _Domain: 推流域名。
        :type Domain: str
        :param _Duration: 时移文件时长，单位分钟。
        :type Duration: float
        :param _StoragePeriod: 时移配置天数，单位天。
        :type StoragePeriod: float
        :param _Time: 时间点，格式: yyyy-mm-ddTHH:MM:SSZ。
        :type Time: str
        :param _TotalDuration: 时移总时长，单位分钟。
        :type TotalDuration: float
        """
        self._Domain = None
        self._Duration = None
        self._StoragePeriod = None
        self._Time = None
        self._TotalDuration = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def StoragePeriod(self):
        return self._StoragePeriod

    @StoragePeriod.setter
    def StoragePeriod(self, StoragePeriod):
        self._StoragePeriod = StoragePeriod

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TotalDuration(self):
        return self._TotalDuration

    @TotalDuration.setter
    def TotalDuration(self, TotalDuration):
        self._TotalDuration = TotalDuration


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Duration = params.get("Duration")
        self._StoragePeriod = params.get("StoragePeriod")
        self._Time = params.get("Time")
        self._TotalDuration = params.get("TotalDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeShiftRecord(AbstractModel):
    """时移录制段。

    """

    def __init__(self):
        r"""
        :param _Sid: 时移录制会话标识。
        :type Sid: str
        :param _StartTime: 录制会话开始时间，Unix 时间戳。
        :type StartTime: int
        :param _EndTime: 录制会话结束时间，Unix 时间戳。
        :type EndTime: int
        """
        self._Sid = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Sid(self):
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeShiftStreamInfo(AbstractModel):
    """时移流。

    """

    def __init__(self):
        r"""
        :param _DomainGroup: 推流域名所属组。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGroup: str
        :param _Domain: 推流域名。
        :type Domain: str
        :param _AppName: 推流路径。
        :type AppName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _StartTime: 流起始时间，Unix 时间戳。
        :type StartTime: int
        :param _EndTime: 截止查询时流结束时间，Unix 时间戳。
        :type EndTime: int
        :param _TransCodeId: 转码模板ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransCodeId: int
        :param _StreamType: 流类型，取值0为原始流，1为水印流，2为转码流。
        :type StreamType: int
        :param _Duration: 时移数据存储时长，单位秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        """
        self._DomainGroup = None
        self._Domain = None
        self._AppName = None
        self._StreamName = None
        self._StartTime = None
        self._EndTime = None
        self._TransCodeId = None
        self._StreamType = None
        self._Duration = None

    @property
    def DomainGroup(self):
        return self._DomainGroup

    @DomainGroup.setter
    def DomainGroup(self, DomainGroup):
        self._DomainGroup = DomainGroup

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TransCodeId(self):
        return self._TransCodeId

    @TransCodeId.setter
    def TransCodeId(self, TransCodeId):
        self._TransCodeId = TransCodeId

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._DomainGroup = params.get("DomainGroup")
        self._Domain = params.get("Domain")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TransCodeId = params.get("TransCodeId")
        self._StreamType = params.get("StreamType")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeShiftTemplate(AbstractModel):
    """直播时移模板配置

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _Duration: 时移时长。
单位：秒。
        :type Duration: int
        :param _ItemDuration: 分片时长。
可取3-10。
单位：s。
默认值：5。
        :type ItemDuration: int
        :param _TemplateId: 模板id。
        :type TemplateId: int
        :param _Description: 模板描述。
        :type Description: str
        :param _Area: 地域：
Mainland：中国大陆；
Overseas：海外及港澳台地区；
默认值：Mainland。
        :type Area: str
        :param _RemoveWatermark: 是否去除水印。
为true则将录制原始流。
默认值：false。
        :type RemoveWatermark: bool
        :param _TranscodeTemplateIds: 转码流id列表。
此参数仅在 RemoveWatermark为false时生效。
        :type TranscodeTemplateIds: list of int non-negative
        """
        self._TemplateName = None
        self._Duration = None
        self._ItemDuration = None
        self._TemplateId = None
        self._Description = None
        self._Area = None
        self._RemoveWatermark = None
        self._TranscodeTemplateIds = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ItemDuration(self):
        return self._ItemDuration

    @ItemDuration.setter
    def ItemDuration(self, ItemDuration):
        self._ItemDuration = ItemDuration

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def RemoveWatermark(self):
        return self._RemoveWatermark

    @RemoveWatermark.setter
    def RemoveWatermark(self, RemoveWatermark):
        self._RemoveWatermark = RemoveWatermark

    @property
    def TranscodeTemplateIds(self):
        return self._TranscodeTemplateIds

    @TranscodeTemplateIds.setter
    def TranscodeTemplateIds(self, TranscodeTemplateIds):
        self._TranscodeTemplateIds = TranscodeTemplateIds


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._Duration = params.get("Duration")
        self._ItemDuration = params.get("ItemDuration")
        self._TemplateId = params.get("TemplateId")
        self._Description = params.get("Description")
        self._Area = params.get("Area")
        self._RemoveWatermark = params.get("RemoveWatermark")
        self._TranscodeTemplateIds = params.get("TranscodeTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeValue(AbstractModel):
    """某个时间点的指标的数值是多少。

    """

    def __init__(self):
        r"""
        :param _Time: UTC 时间，时间格式：yyyy-mm-ddTHH:MM:SSZ。
        :type Time: str
        :param _Num: 数值。
        :type Num: int
        """
        self._Time = None
        self._Num = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeDetailInfo(AbstractModel):
    """转码详细信息。

    """

    def __init__(self):
        r"""
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _StartTime: 开始时间（北京时间），格式：yyyy-mm-dd HH:MM。
        :type StartTime: str
        :param _EndTime: 结束时间（北京时间），格式：yyyy-mm-dd HH:MM。
        :type EndTime: str
        :param _Duration: 转码时长，单位：分钟。
注意：因推流过程中可能有中断重推情况，此处时长为真实转码时长累加值，并非结束时间和开始时间的间隔。
        :type Duration: int
        :param _ModuleCodec: 编码方式，带模块，
示例：
liveprocessor_H264：直播转码-H264，
liveprocessor_H265： 直播转码-H265，
topspeed_H264：极速高清-H264，
topspeed_H265：极速高清-H265。
        :type ModuleCodec: str
        :param _Bitrate: 码率。
        :type Bitrate: int
        :param _Type: 类型，包含：转码（Transcode），混流（MixStream），水印（WaterMark），快直播（Webrtc）。
        :type Type: str
        :param _PushDomain: 推流域名。
        :type PushDomain: str
        :param _Resolution: 分辨率。
        :type Resolution: str
        :param _MainlandOrOversea: 地域：
Mainland：国内。
Overseas：海外。
        :type MainlandOrOversea: str
        """
        self._StreamName = None
        self._StartTime = None
        self._EndTime = None
        self._Duration = None
        self._ModuleCodec = None
        self._Bitrate = None
        self._Type = None
        self._PushDomain = None
        self._Resolution = None
        self._MainlandOrOversea = None

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ModuleCodec(self):
        return self._ModuleCodec

    @ModuleCodec.setter
    def ModuleCodec(self, ModuleCodec):
        self._ModuleCodec = ModuleCodec

    @property
    def Bitrate(self):
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PushDomain(self):
        return self._PushDomain

    @PushDomain.setter
    def PushDomain(self, PushDomain):
        self._PushDomain = PushDomain

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MainlandOrOversea(self):
        return self._MainlandOrOversea

    @MainlandOrOversea.setter
    def MainlandOrOversea(self, MainlandOrOversea):
        self._MainlandOrOversea = MainlandOrOversea


    def _deserialize(self, params):
        self._StreamName = params.get("StreamName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Duration = params.get("Duration")
        self._ModuleCodec = params.get("ModuleCodec")
        self._Bitrate = params.get("Bitrate")
        self._Type = params.get("Type")
        self._PushDomain = params.get("PushDomain")
        self._Resolution = params.get("Resolution")
        self._MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskNum(AbstractModel):
    """转码任务数。

    """

    def __init__(self):
        r"""
        :param _Time: 时间点。
        :type Time: str
        :param _CodeRate: 码率。
        :type CodeRate: int
        :param _Num: 任务数。
        :type Num: int
        """
        self._Time = None
        self._CodeRate = None
        self._Num = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def CodeRate(self):
        return self._CodeRate

    @CodeRate.setter
    def CodeRate(self, CodeRate):
        self._CodeRate = CodeRate

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._CodeRate = params.get("CodeRate")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTotalInfo(AbstractModel):
    """转码总量数据

    """

    def __init__(self):
        r"""
        :param _Time: 时间点，
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type Time: str
        :param _Duration: 转码时长，单位：分钟。
        :type Duration: int
        :param _ModuleCodec: 编码方式，带模块，
示例：
liveprocessor_H264 =》直播转码-H264，
liveprocessor_H265 =》 直播转码-H265，
topspeed_H264 =》极速高清-H264，
topspeed_H265 =》极速高清-H265。
        :type ModuleCodec: str
        :param _Resolution: 分辨率，
示例：540*480。
        :type Resolution: str
        """
        self._Time = None
        self._Duration = None
        self._ModuleCodec = None
        self._Resolution = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ModuleCodec(self):
        return self._ModuleCodec

    @ModuleCodec.setter
    def ModuleCodec(self, ModuleCodec):
        self._ModuleCodec = ModuleCodec

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Duration = params.get("Duration")
        self._ModuleCodec = params.get("ModuleCodec")
        self._Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindLiveDomainCertRequest(AbstractModel):
    """UnBindLiveDomainCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 播放域名。
        :type DomainName: str
        :param _Type: 枚举值：
gray: 解绑灰度规则
formal(默认): 解绑正式规则

不传则为formal
        :type Type: str
        """
        self._DomainName = None
        self._Type = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindLiveDomainCertResponse(AbstractModel):
    """UnBindLiveDomainCert返回参数结构体

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


class UpdateLiveWatermarkRequest(AbstractModel):
    """UpdateLiveWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WatermarkId: 水印 ID。
在添加水印接口 [AddLiveWatermark](/document/product/267/30154) 调用返回值中获取水印 ID。
        :type WatermarkId: int
        :param _PictureUrl: 水印图片 URL。
URL中禁止包含的字符：
 ;(){}$>`#"\'|
        :type PictureUrl: str
        :param _XPosition: 显示位置，X轴偏移，单位是百分比，默认 0。
        :type XPosition: int
        :param _YPosition: 显示位置，Y轴偏移，单位是百分比，默认 0。
        :type YPosition: int
        :param _WatermarkName: 水印名称。
最长16字节。
        :type WatermarkName: str
        :param _Width: 水印宽度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始宽度。
        :type Width: int
        :param _Height: 水印高度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始高度。
        :type Height: int
        :param _BackgroundWidth: 背景水印宽度。默认宽度1920。
        :type BackgroundWidth: int
        :param _BackgroundHeight: 背景水印高度。默认高度1080。
        :type BackgroundHeight: int
        """
        self._WatermarkId = None
        self._PictureUrl = None
        self._XPosition = None
        self._YPosition = None
        self._WatermarkName = None
        self._Width = None
        self._Height = None
        self._BackgroundWidth = None
        self._BackgroundHeight = None

    @property
    def WatermarkId(self):
        return self._WatermarkId

    @WatermarkId.setter
    def WatermarkId(self, WatermarkId):
        self._WatermarkId = WatermarkId

    @property
    def PictureUrl(self):
        return self._PictureUrl

    @PictureUrl.setter
    def PictureUrl(self, PictureUrl):
        self._PictureUrl = PictureUrl

    @property
    def XPosition(self):
        return self._XPosition

    @XPosition.setter
    def XPosition(self, XPosition):
        self._XPosition = XPosition

    @property
    def YPosition(self):
        return self._YPosition

    @YPosition.setter
    def YPosition(self, YPosition):
        self._YPosition = YPosition

    @property
    def WatermarkName(self):
        return self._WatermarkName

    @WatermarkName.setter
    def WatermarkName(self, WatermarkName):
        self._WatermarkName = WatermarkName

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def BackgroundWidth(self):
        return self._BackgroundWidth

    @BackgroundWidth.setter
    def BackgroundWidth(self, BackgroundWidth):
        self._BackgroundWidth = BackgroundWidth

    @property
    def BackgroundHeight(self):
        return self._BackgroundHeight

    @BackgroundHeight.setter
    def BackgroundHeight(self, BackgroundHeight):
        self._BackgroundHeight = BackgroundHeight


    def _deserialize(self, params):
        self._WatermarkId = params.get("WatermarkId")
        self._PictureUrl = params.get("PictureUrl")
        self._XPosition = params.get("XPosition")
        self._YPosition = params.get("YPosition")
        self._WatermarkName = params.get("WatermarkName")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._BackgroundWidth = params.get("BackgroundWidth")
        self._BackgroundHeight = params.get("BackgroundHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateLiveWatermarkResponse(AbstractModel):
    """UpdateLiveWatermark返回参数结构体

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


class WatermarkInfo(AbstractModel):
    """水印信息。

    """

    def __init__(self):
        r"""
        :param _WatermarkId: 水印 ID。
        :type WatermarkId: int
        :param _PictureUrl: 水印图片 URL。
        :type PictureUrl: str
        :param _XPosition: 显示位置，X 轴偏移。
        :type XPosition: int
        :param _YPosition: 显示位置，Y 轴偏移。
        :type YPosition: int
        :param _WatermarkName: 水印名称。
        :type WatermarkName: str
        :param _Status: 当前状态。0：未使用，1:使用中。
        :type Status: int
        :param _CreateTime: 添加时间。
注：此字段为北京时间（UTC+8时区）。
        :type CreateTime: str
        :param _Width: 水印宽。
        :type Width: int
        :param _Height: 水印高。
        :type Height: int
        :param _BackgroundWidth: 背景水印宽。
        :type BackgroundWidth: int
        :param _BackgroundHeight: 背景水印高。
        :type BackgroundHeight: int
        """
        self._WatermarkId = None
        self._PictureUrl = None
        self._XPosition = None
        self._YPosition = None
        self._WatermarkName = None
        self._Status = None
        self._CreateTime = None
        self._Width = None
        self._Height = None
        self._BackgroundWidth = None
        self._BackgroundHeight = None

    @property
    def WatermarkId(self):
        return self._WatermarkId

    @WatermarkId.setter
    def WatermarkId(self, WatermarkId):
        self._WatermarkId = WatermarkId

    @property
    def PictureUrl(self):
        return self._PictureUrl

    @PictureUrl.setter
    def PictureUrl(self, PictureUrl):
        self._PictureUrl = PictureUrl

    @property
    def XPosition(self):
        return self._XPosition

    @XPosition.setter
    def XPosition(self, XPosition):
        self._XPosition = XPosition

    @property
    def YPosition(self):
        return self._YPosition

    @YPosition.setter
    def YPosition(self, YPosition):
        self._YPosition = YPosition

    @property
    def WatermarkName(self):
        return self._WatermarkName

    @WatermarkName.setter
    def WatermarkName(self, WatermarkName):
        self._WatermarkName = WatermarkName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def BackgroundWidth(self):
        return self._BackgroundWidth

    @BackgroundWidth.setter
    def BackgroundWidth(self, BackgroundWidth):
        self._BackgroundWidth = BackgroundWidth

    @property
    def BackgroundHeight(self):
        return self._BackgroundHeight

    @BackgroundHeight.setter
    def BackgroundHeight(self, BackgroundHeight):
        self._BackgroundHeight = BackgroundHeight


    def _deserialize(self, params):
        self._WatermarkId = params.get("WatermarkId")
        self._PictureUrl = params.get("PictureUrl")
        self._XPosition = params.get("XPosition")
        self._YPosition = params.get("YPosition")
        self._WatermarkName = params.get("WatermarkName")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._BackgroundWidth = params.get("BackgroundWidth")
        self._BackgroundHeight = params.get("BackgroundHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XP2PDetailInfo(AbstractModel):
    """P2P流信息。

    """

    def __init__(self):
        r"""
        :param _CdnBytes: CDN流量。
        :type CdnBytes: int
        :param _P2pBytes: P2P流量。
        :type P2pBytes: int
        :param _StuckPeople: 卡播人数。
        :type StuckPeople: int
        :param _StuckTimes: 卡播次数。
        :type StuckTimes: int
        :param _OnlinePeople: 在线人数。
        :type OnlinePeople: int
        :param _Request: 起播请求次数
        :type Request: int
        :param _RequestSuccess: 起播成功次数
        :type RequestSuccess: int
        :param _Time: 时间，一分钟粒度，utc格式：yyyy-mm-ddTHH:MM:SSZ，参考https://cloud.tencent.com/document/product/266/11732#I。。
        :type Time: str
        :param _Type: 类型，分live和vod两种。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _StreamName: 流ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamName: str
        :param _AppId: AppId。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        """
        self._CdnBytes = None
        self._P2pBytes = None
        self._StuckPeople = None
        self._StuckTimes = None
        self._OnlinePeople = None
        self._Request = None
        self._RequestSuccess = None
        self._Time = None
        self._Type = None
        self._StreamName = None
        self._AppId = None

    @property
    def CdnBytes(self):
        return self._CdnBytes

    @CdnBytes.setter
    def CdnBytes(self, CdnBytes):
        self._CdnBytes = CdnBytes

    @property
    def P2pBytes(self):
        return self._P2pBytes

    @P2pBytes.setter
    def P2pBytes(self, P2pBytes):
        self._P2pBytes = P2pBytes

    @property
    def StuckPeople(self):
        return self._StuckPeople

    @StuckPeople.setter
    def StuckPeople(self, StuckPeople):
        self._StuckPeople = StuckPeople

    @property
    def StuckTimes(self):
        return self._StuckTimes

    @StuckTimes.setter
    def StuckTimes(self, StuckTimes):
        self._StuckTimes = StuckTimes

    @property
    def OnlinePeople(self):
        return self._OnlinePeople

    @OnlinePeople.setter
    def OnlinePeople(self, OnlinePeople):
        self._OnlinePeople = OnlinePeople

    @property
    def Request(self):
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def RequestSuccess(self):
        return self._RequestSuccess

    @RequestSuccess.setter
    def RequestSuccess(self, RequestSuccess):
        self._RequestSuccess = RequestSuccess

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._CdnBytes = params.get("CdnBytes")
        self._P2pBytes = params.get("P2pBytes")
        self._StuckPeople = params.get("StuckPeople")
        self._StuckTimes = params.get("StuckTimes")
        self._OnlinePeople = params.get("OnlinePeople")
        self._Request = params.get("Request")
        self._RequestSuccess = params.get("RequestSuccess")
        self._Time = params.get("Time")
        self._Type = params.get("Type")
        self._StreamName = params.get("StreamName")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        