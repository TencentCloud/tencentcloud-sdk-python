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


class Device(AbstractModel):
    """业务入参

    """

    def __init__(self):
        r"""
        :param DeviceId: 业务入参id
        :type DeviceId: str
        :param DeviceType: 业务入参类型
        :type DeviceType: int
        """
        self.DeviceId = None
        self.DeviceType = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputBusinessEncryptData(AbstractModel):
    """业务入参

    """


class InputRecognizeTargetAudience(AbstractModel):
    """流量反欺诈-验准入参

    """

    def __init__(self):
        r"""
        :param ModelIdList: 模型ID列表
        :type ModelIdList: list of int
        :param Uid: 设备ID，AccountType指定的类型
        :type Uid: str
        :param AccountType: 设备号类型，1.imei 2.imeiMd5（小写后转MD5转小写）3.idfa， 4.idfaMd5（大写后转MD5转小写），5.手机号,256.其它
        :type AccountType: int
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
        :param AppName: app名称
        :type AppName: str
        :param AppVer: app版本描述
        :type AppVer: str
        :param ReqType: 竞价模式1：rtb 2:pd
        :type ReqType: int
        :param IsAuthorized: 用户是否授权,1为授权，0为未授权
        :type IsAuthorized: int
        :param DeviceList: 设备信息
        :type DeviceList: list of Device
        """
        self.ModelIdList = None
        self.Uid = None
        self.AccountType = None
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
        self.IsAuthorized = None
        self.DeviceList = None


    def _deserialize(self, params):
        self.ModelIdList = params.get("ModelIdList")
        self.Uid = params.get("Uid")
        self.AccountType = params.get("AccountType")
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
        self.IsAuthorized = params.get("IsAuthorized")
        if params.get("DeviceList") is not None:
            self.DeviceList = []
            for item in params.get("DeviceList"):
                obj = Device()
                obj._deserialize(item)
                self.DeviceList.append(obj)
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
        r"""
        :param TaskId: 投放任务ID
        :type TaskId: str
        :param Mobiles: 手机号码列表（号码量<=200）
        :type Mobiles: list of str
        :param IsAuthorized: 是否授权，1：已授权
        :type IsAuthorized: int
        :param EncryptMethod: 加密方式，0：AES加密；1：DES加密
        :type EncryptMethod: int
        :param EncryptMode: 加密算法中的块处理模式，0：ECB模式；1：CBC模式；2：CTR模式；3：CFB模式；4：OFB模式；
        :type EncryptMode: int
        :param PaddingType: 填充模式，0：ZeroPadding；1：PKCS5Padding；2：PKCS7Padding；
        :type PaddingType: int
        :param EncryptData: 加密数据
        :type EncryptData: str
        """
        self.TaskId = None
        self.Mobiles = None
        self.IsAuthorized = None
        self.EncryptMethod = None
        self.EncryptMode = None
        self.PaddingType = None
        self.EncryptData = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Mobiles = params.get("Mobiles")
        self.IsAuthorized = params.get("IsAuthorized")
        self.EncryptMethod = params.get("EncryptMethod")
        self.EncryptMode = params.get("EncryptMode")
        self.PaddingType = params.get("PaddingType")
        self.EncryptData = params.get("EncryptData")
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
        r"""
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
        r"""
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
        r"""
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
        


class RecognizeCustomizedAudienceRequest(AbstractModel):
    """RecognizeCustomizedAudience请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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


class RecognizePreciseTargetAudienceRequest(AbstractModel):
    """RecognizePreciseTargetAudience请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param BspData: 业务数据
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        :param BusinessEncryptData: 业务加密数据
        :type BusinessEncryptData: :class:`tencentcloud.taf.v20200210.models.InputBusinessEncryptData`
        """
        self.BspData = None
        self.BusinessEncryptData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputRecognizeTargetAudience()
            self.BspData._deserialize(params.get("BspData"))
        if params.get("BusinessEncryptData") is not None:
            self.BusinessEncryptData = InputBusinessEncryptData()
            self.BusinessEncryptData._deserialize(params.get("BusinessEncryptData"))
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
        r"""
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
        r"""
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
        r"""
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