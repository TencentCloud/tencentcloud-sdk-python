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


class DetectFraudKOLRequest(AbstractModel):
    """DetectFraudKOL请求参数结构体

    """

    def __init__(self):
        """
        :param BspData: 业务数据
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputKolBspData`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputKolBspData()
            self.BspData._deserialize(params.get("BspData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectFraudKOLResponse(AbstractModel):
    """DetectFraudKOL返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 回包数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputKolData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputKolData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class EnhanceTaDegreeRequest(AbstractModel):
    """EnhanceTaDegree请求参数结构体

    """

    def __init__(self):
        """
        :param BspData: 业务数据
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputTaBspData`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputTaBspData()
            self.BspData._deserialize(params.get("BspData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnhanceTaDegreeResponse(AbstractModel):
    """EnhanceTaDegree返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 回包数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputTaData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputTaData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class InputKolBspData(AbstractModel):
    """CheckKol

    """

    def __init__(self):
        """
        :param DataList: BspData
        :type DataList: list of InputKolDataList
        """
        self.DataList = None


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = InputKolDataList()
                obj._deserialize(item)
                self.DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputKolDataList(AbstractModel):
    """CheckKol

    """

    def __init__(self):
        """
        :param Type: 账号类型[1：微信；2：qq；3：微博]
        :type Type: int
        :param Id: KOL账号ID[比如微信公众号ID]
        :type Id: str
        :param Name: KOL名称
        :type Name: str
        :param Phone: 手机号
        :type Phone: str
        :param AgentInfo: 代理商名称
        :type AgentInfo: str
        """
        self.Type = None
        self.Id = None
        self.Name = None
        self.Phone = None
        self.AgentInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")
        self.AgentInfo = params.get("AgentInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputRecognizeEffectiveFlow(AbstractModel):
    """接口入参

    """


class InputRecognizeTargetAudience(AbstractModel):
    """流量反欺诈-验准入参

    """

    def __init__(self):
        """
        :param Uid: 设备ID，AccountType指定的类型
        :type Uid: str
        :param AccountType: 设备号类型，1.imei 2.imeiMd5（小写后转MD5转小写）3.idfa， 4.idfaMd5（大写后转MD5转小写），5.手机号,256.其它
        :type AccountType: int
        :param ModelIdList: 模型ID列表
        :type ModelIdList: list of int
        :param Ip: 用户IP
        :type Ip: str
        :param Os: 操作系统类型(unknown，android，ios，windows)
        :type Os: str
        :param Osv: 操作系统版本
        :type Osv: str
        :param Lat: 纬度
        :type Lat: str
        :param Lon: 经度
        :type Lon: str
        :param DeviceModel: 设备型号(MI 6)
        :type DeviceModel: str
        :param BidFloor: 竞价底价
        :type BidFloor: int
        :param Age: 年龄
        :type Age: int
        :param Gender: 性别(1.MALE 2.FEMALE)
        :type Gender: int
        :param Location: 用户地址
        :type Location: str
        :param DeliveryMode: 投放模式（0=PDB，1=PD，2=RTB，10=其他）
        :type DeliveryMode: int
        :param AdvertisingType: 广告位类型<br />（0=前贴片，1=开屏广告，2=网页头部广告、3=网页中部广告、4=网页底部广告、5=悬浮广告、10=其它）
        :type AdvertisingType: int
        :param Mac: mac地址，建议提供
        :type Mac: str
        :param Phone: 电话号码
        :type Phone: str
        :param Ua: 浏览器类型
        :type Ua: str
        :param App: 客户端应用
        :type App: str
        :param Package: 应用包名
        :type Package: str
        :param Maker: 设备制造商
        :type Maker: str
        :param DeviceType: 设备类型（PHONE,TABLET）
        :type DeviceType: str
        :param AccessMode: 入网方式(wifi,4g,3g,2g)
        :type AccessMode: str
        :param Sp: 运营商(1.移动 2.联通 3.电信等)
        :type Sp: int
        :param DeviceW: 设备屏幕分辨率宽度像素数
        :type DeviceW: int
        :param DeviceH: 设备屏幕分辨率高度像素数
        :type DeviceH: int
        :param FullScreen: 是否全屏插广告(0-否，1-是)
        :type FullScreen: int
        :param ImpBannerW: 广告位宽度
        :type ImpBannerW: int
        :param ImpBannerH: 广告位高度
        :type ImpBannerH: int
        :param Url: 网址
        :type Url: str
        :param Context: 上下文信息
        :type Context: str
        :param Channel: 渠道
        :type Channel: str
        :param ReqId: 请求ID
        :type ReqId: str
        :param ReqMd5: 请求ID的md5值
        :type ReqMd5: str
        :param AdType: ad_type
        :type AdType: int
        :param AppName: app name
        :type AppName: str
        :param AppVer: appVer
        :type AppVer: str
        :param ReqType: 竞价模式1：rtb 2:pd
        :type ReqType: int
        """
        self.Uid = None
        self.AccountType = None
        self.ModelIdList = None
        self.Ip = None
        self.Os = None
        self.Osv = None
        self.Lat = None
        self.Lon = None
        self.DeviceModel = None
        self.BidFloor = None
        self.Age = None
        self.Gender = None
        self.Location = None
        self.DeliveryMode = None
        self.AdvertisingType = None
        self.Mac = None
        self.Phone = None
        self.Ua = None
        self.App = None
        self.Package = None
        self.Maker = None
        self.DeviceType = None
        self.AccessMode = None
        self.Sp = None
        self.DeviceW = None
        self.DeviceH = None
        self.FullScreen = None
        self.ImpBannerW = None
        self.ImpBannerH = None
        self.Url = None
        self.Context = None
        self.Channel = None
        self.ReqId = None
        self.ReqMd5 = None
        self.AdType = None
        self.AppName = None
        self.AppVer = None
        self.ReqType = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.AccountType = params.get("AccountType")
        self.ModelIdList = params.get("ModelIdList")
        self.Ip = params.get("Ip")
        self.Os = params.get("Os")
        self.Osv = params.get("Osv")
        self.Lat = params.get("Lat")
        self.Lon = params.get("Lon")
        self.DeviceModel = params.get("DeviceModel")
        self.BidFloor = params.get("BidFloor")
        self.Age = params.get("Age")
        self.Gender = params.get("Gender")
        self.Location = params.get("Location")
        self.DeliveryMode = params.get("DeliveryMode")
        self.AdvertisingType = params.get("AdvertisingType")
        self.Mac = params.get("Mac")
        self.Phone = params.get("Phone")
        self.Ua = params.get("Ua")
        self.App = params.get("App")
        self.Package = params.get("Package")
        self.Maker = params.get("Maker")
        self.DeviceType = params.get("DeviceType")
        self.AccessMode = params.get("AccessMode")
        self.Sp = params.get("Sp")
        self.DeviceW = params.get("DeviceW")
        self.DeviceH = params.get("DeviceH")
        self.FullScreen = params.get("FullScreen")
        self.ImpBannerW = params.get("ImpBannerW")
        self.ImpBannerH = params.get("ImpBannerH")
        self.Url = params.get("Url")
        self.Context = params.get("Context")
        self.Channel = params.get("Channel")
        self.ReqId = params.get("ReqId")
        self.ReqMd5 = params.get("ReqMd5")
        self.AdType = params.get("AdType")
        self.AppName = params.get("AppName")
        self.AppVer = params.get("AppVer")
        self.ReqType = params.get("ReqType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputSendTrafficSecuritySmsMsg(AbstractModel):
    """业务入参

    """

    def __init__(self):
        """
        :param TaskId: 投放任务ID
        :type TaskId: str
        :param Mobiles: 手机号码列表（号码量<=200）
        :type Mobiles: list of str
        """
        self.TaskId = None
        self.Mobiles = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Mobiles = params.get("Mobiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputTaBspData(AbstractModel):
    """流量反欺诈-虚假TA识别

    """

    def __init__(self):
        """
        :param Seq: 请求序列号
        :type Seq: int
        :param OsType: 操作系统类型[0：未知；1：android；2：ios；3：windows]
        :type OsType: str
        :param AgeFloor: 年龄下限
        :type AgeFloor: int
        :param AgeCeil: 年龄上限
        :type AgeCeil: int
        :param Gender: 性别[1：男；2：女]
        :type Gender: int
        :param UserTime: 用户操作时间
        :type UserTime: int
        :param Imei: Imei [在(Imei|ImeiMd5|Idfa|IdfaMd5)里面4选1]
        :type Imei: str
        :param ImeiMd5: Imei小写后加密Md5 [在(Imei|ImeiMd5|Idfa|IdfaMd5)里面4选1]
        :type ImeiMd5: str
        :param Idfa: Idfa [在(Imei|ImeiMd5|Idfa|IdfaMd5)里面4选1]
        :type Idfa: str
        :param IdfaMd5: Idfa大写后加密Md5 [在(Imei|ImeiMd5|Idfa|IdfaMd5)里面4选1]
        :type IdfaMd5: str
        :param UserIp: 用户IP
        :type UserIp: str
        :param Mac: MAC地址[建议提供]
        :type Mac: str
        :param PhoneNum: 手机号码[中国大陆]
        :type PhoneNum: str
        :param UserAgent: 浏览器
        :type UserAgent: str
        :param App: APP名称
        :type App: str
        :param Package: 应用安装包名称
        :type Package: str
        :param DeviceMaker: 设备制造商
        :type DeviceMaker: str
        :param DeviceModule: 设备型号
        :type DeviceModule: str
        :param AccessMode: 入网方式[1：WIFI；2：4G；3：3G；4：2G；5：其它]
        :type AccessMode: str
        :param Sp: 运营商[1：移动；2：联通；3：电信；4：其它]
        :type Sp: str
        :param Url: 网址
        :type Url: str
        :param Location: 用户地址
        :type Location: str
        :param Latitude: 纬度
        :type Latitude: str
        :param Longitude: 精度
        :type Longitude: str
        :param Context: 辅助区分信息
        :type Context: str
        """
        self.Seq = None
        self.OsType = None
        self.AgeFloor = None
        self.AgeCeil = None
        self.Gender = None
        self.UserTime = None
        self.Imei = None
        self.ImeiMd5 = None
        self.Idfa = None
        self.IdfaMd5 = None
        self.UserIp = None
        self.Mac = None
        self.PhoneNum = None
        self.UserAgent = None
        self.App = None
        self.Package = None
        self.DeviceMaker = None
        self.DeviceModule = None
        self.AccessMode = None
        self.Sp = None
        self.Url = None
        self.Location = None
        self.Latitude = None
        self.Longitude = None
        self.Context = None


    def _deserialize(self, params):
        self.Seq = params.get("Seq")
        self.OsType = params.get("OsType")
        self.AgeFloor = params.get("AgeFloor")
        self.AgeCeil = params.get("AgeCeil")
        self.Gender = params.get("Gender")
        self.UserTime = params.get("UserTime")
        self.Imei = params.get("Imei")
        self.ImeiMd5 = params.get("ImeiMd5")
        self.Idfa = params.get("Idfa")
        self.IdfaMd5 = params.get("IdfaMd5")
        self.UserIp = params.get("UserIp")
        self.Mac = params.get("Mac")
        self.PhoneNum = params.get("PhoneNum")
        self.UserAgent = params.get("UserAgent")
        self.App = params.get("App")
        self.Package = params.get("Package")
        self.DeviceMaker = params.get("DeviceMaker")
        self.DeviceModule = params.get("DeviceModule")
        self.AccessMode = params.get("AccessMode")
        self.Sp = params.get("Sp")
        self.Url = params.get("Url")
        self.Location = params.get("Location")
        self.Latitude = params.get("Latitude")
        self.Longitude = params.get("Longitude")
        self.Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputKolData(AbstractModel):
    """CheckKol

    """

    def __init__(self):
        """
        :param Code: 错误码[0:成功；非0：失败的错误码]
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param Message: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 业务返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of OutputKolValue
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = OutputKolValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputKolValue(AbstractModel):
    """CheckKol

    """

    def __init__(self):
        """
        :param Id: KOL账号ID[比如微信公众号ID]
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param IsCheck: 是否查得[0：未查得；1：查得]
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCheck: int
        :param FraudPScore: 作弊的可能性[0～100]
注意：此字段可能返回 null，表示取不到有效值。
        :type FraudPScore: int
        :param EvilPScore: 作弊的严重性[0～100]
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilPScore: int
        """
        self.Id = None
        self.IsCheck = None
        self.FraudPScore = None
        self.EvilPScore = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.IsCheck = params.get("IsCheck")
        self.FraudPScore = params.get("FraudPScore")
        self.EvilPScore = params.get("EvilPScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputRecognizeEffectiveFlow(AbstractModel):
    """业务出参

    """

    def __init__(self):
        """
        :param Code: 返回码。0表示成功，非0标识失败错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param Message: UTF-8编码，出错消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 业务入参
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeEffectiveFlowValue`
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = OutputRecognizeEffectiveFlowValue()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputRecognizeEffectiveFlowValue(AbstractModel):
    """业务出参

    """

    def __init__(self):
        """
        :param Lable: 返回标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Lable: str
        :param Score: 返回分值
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self.Lable = None
        self.Score = None


    def _deserialize(self, params):
        self.Lable = params.get("Lable")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputRecognizeTargetAudience(AbstractModel):
    """流量反欺诈-验准返回值

    """

    def __init__(self):
        """
        :param Code: 返回码（0，成功，其他失败）
        :type Code: int
        :param Message: 返回码对应的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 返回模型结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of OutputRecognizeTargetAudienceValue
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = OutputRecognizeTargetAudienceValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputRecognizeTargetAudienceValue(AbstractModel):
    """流量反欺诈-验准返回的查询分值

    """

    def __init__(self):
        """
        :param ModelId: 模型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: int
        :param IsFound: 是否正常返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFound: int
        :param Score: 返回分值
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self.ModelId = None
        self.IsFound = None
        self.Score = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.IsFound = params.get("IsFound")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputSendTrafficSecuritySmsMsg(AbstractModel):
    """返回结果

    """

    def __init__(self):
        """
        :param Code: 返回码（0：接口调用成功 非0：接口调用失败）
        :type Code: int
        :param Message: 返回码对应的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 发送失败的号码列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputTaData(AbstractModel):
    """流量反欺诈-虚假TA识别

    """

    def __init__(self):
        """
        :param Code: 错误码[0:成功；非0：失败的错误码]
        :type Code: int
        :param Message: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 结果数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.taf.v20200210.models.OutputTaValue`
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = OutputTaValue()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputTaValue(AbstractModel):
    """流量反欺诈-虚假TA识别

    """

    def __init__(self):
        """
        :param IsCheck: 是否查得[0：未查得；1：查得]
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCheck: int
        :param IsMatch: 是否符合[0：不符合；1：符合]
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMatch: int
        """
        self.IsCheck = None
        self.IsMatch = None


    def _deserialize(self, params):
        self.IsCheck = params.get("IsCheck")
        self.IsMatch = params.get("IsMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeCustomizedAudienceRequest(AbstractModel):
    """RecognizeCustomizedAudience请求参数结构体

    """

    def __init__(self):
        """
        :param BspData: 业务入参
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputRecognizeTargetAudience()
            self.BspData._deserialize(params.get("BspData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeCustomizedAudienceResponse(AbstractModel):
    """RecognizeCustomizedAudience返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 业务出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputRecognizeTargetAudience()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class RecognizeEffectiveFlowRequest(AbstractModel):
    """RecognizeEffectiveFlow请求参数结构体

    """

    def __init__(self):
        """
        :param BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeEffectiveFlow`
        """
        self.BusinessSecurityData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = InputRecognizeEffectiveFlow()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeEffectiveFlowResponse(AbstractModel):
    """RecognizeEffectiveFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 业务出参
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeEffectiveFlow`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputRecognizeEffectiveFlow()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class RecognizePreciseTargetAudienceRequest(AbstractModel):
    """RecognizePreciseTargetAudience请求参数结构体

    """

    def __init__(self):
        """
        :param BspData: 业务数据
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputRecognizeTargetAudience()
            self.BspData._deserialize(params.get("BspData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePreciseTargetAudienceResponse(AbstractModel):
    """RecognizePreciseTargetAudience返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 回包数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputRecognizeTargetAudience()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class RecognizeTargetAudienceRequest(AbstractModel):
    """RecognizeTargetAudience请求参数结构体

    """

    def __init__(self):
        """
        :param BspData: 业务数据
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputRecognizeTargetAudience()
            self.BspData._deserialize(params.get("BspData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTargetAudienceResponse(AbstractModel):
    """RecognizeTargetAudience返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 回包数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputRecognizeTargetAudience()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SendTrafficSecuritySmsMessageRequest(AbstractModel):
    """SendTrafficSecuritySmsMessage请求参数结构体

    """

    def __init__(self):
        """
        :param BspData: 业务入参
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputSendTrafficSecuritySmsMsg`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputSendTrafficSecuritySmsMsg()
            self.BspData._deserialize(params.get("BspData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendTrafficSecuritySmsMessageResponse(AbstractModel):
    """SendTrafficSecuritySmsMessage返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputSendTrafficSecuritySmsMsg`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputSendTrafficSecuritySmsMsg()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")