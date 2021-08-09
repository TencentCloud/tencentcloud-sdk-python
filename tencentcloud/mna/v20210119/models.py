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


class Capacity(AbstractModel):
    """接口能力扩展，用于填充电信的加速Token，并为未来参数提供兼容空间

    """

    def __init__(self):
        """
        :param CTCCToken: 电信鉴权的Token。要加速的电信手机终端访问 http://qos.189.cn/qos-api/getToken?appid=TencentCloud 页面，获取返回结果中result的值\n        :type CTCCToken: str\n        :param Province: 终端所处在的省份，建议不填写由服务端自动获取，若需填写请填写带有省、市、自治区、特别行政区等后缀的省份中文全称\n        :type Province: str\n        """
        self.CTCCToken = None
        self.Province = None


    def _deserialize(self, params):
        self.CTCCToken = params.get("CTCCToken")
        self.Province = params.get("Province")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQosRequest(AbstractModel):
    """CreateQos请求参数结构体

    """

    def __init__(self):
        """
        :param SrcAddressInfo: 加速业务源地址信息，SrcIpv6和（SrcIpv4+SrcPublicIpv4）二选一，目前Ipv6不可用，全部填写以Ipv4参数为准。\n        :type SrcAddressInfo: :class:`tencentcloud.mna.v20210119.models.SrcAddressInfo`\n        :param DestAddressInfo: 加速业务目标地址信息\n        :type DestAddressInfo: :class:`tencentcloud.mna.v20210119.models.DestAddressInfo`\n        :param QosMenu: 加速套餐
T100K：上/下行保障 100kbps
T200K：上/下行保障 200kbps
T400K：上/下行保障 400kbps
BD1M：下行带宽保障1Mbps
BD2M：下行带宽保障2Mbps
BD4M：下行带宽保障4Mbps
BU1M：上行带宽保障1Mbps
BU2M：上行带宽保障2Mbps
BU4M：上行带宽保障4Mbps\n        :type QosMenu: str\n        :param DeviceInfo: 申请加速的设备信息，包括运营商，操作系统，设备唯一标识等。\n        :type DeviceInfo: :class:`tencentcloud.mna.v20210119.models.DeviceInfo`\n        :param Duration: 期望加速时长（单位分钟），默认值30分钟\n        :type Duration: int\n        :param Capacity: 接口能力扩展，如果是电信用户，必须填充CTCC Token字段\n        :type Capacity: :class:`tencentcloud.mna.v20210119.models.Capacity`\n        :param TemplateId: 应用模板ID\n        :type TemplateId: str\n        """
        self.SrcAddressInfo = None
        self.DestAddressInfo = None
        self.QosMenu = None
        self.DeviceInfo = None
        self.Duration = None
        self.Capacity = None
        self.TemplateId = None


    def _deserialize(self, params):
        if params.get("SrcAddressInfo") is not None:
            self.SrcAddressInfo = SrcAddressInfo()
            self.SrcAddressInfo._deserialize(params.get("SrcAddressInfo"))
        if params.get("DestAddressInfo") is not None:
            self.DestAddressInfo = DestAddressInfo()
            self.DestAddressInfo._deserialize(params.get("DestAddressInfo"))
        self.QosMenu = params.get("QosMenu")
        if params.get("DeviceInfo") is not None:
            self.DeviceInfo = DeviceInfo()
            self.DeviceInfo._deserialize(params.get("DeviceInfo"))
        self.Duration = params.get("Duration")
        if params.get("Capacity") is not None:
            self.Capacity = Capacity()
            self.Capacity._deserialize(params.get("Capacity"))
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQosResponse(AbstractModel):
    """CreateQos返回参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 单次加速唯一 Id\n        :type SessionId: str\n        :param Duration: 当前加速剩余时长（单位秒）\n        :type Duration: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SessionId = None
        self.Duration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Duration = params.get("Duration")
        self.RequestId = params.get("RequestId")


class DeleteQosRequest(AbstractModel):
    """DeleteQos请求参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 单次加速唯一 Id\n        :type SessionId: str\n        """
        self.SessionId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQosResponse(AbstractModel):
    """DeleteQos返回参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 单次加速唯一 Id\n        :type SessionId: str\n        :param Duration: 本次加速会话持续时间（单位秒）\n        :type Duration: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SessionId = None
        self.Duration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Duration = params.get("Duration")
        self.RequestId = params.get("RequestId")


class DestAddressInfo(AbstractModel):
    """移动网络加速目标地址结构体

    """

    def __init__(self):
        """
        :param DestIp: 加速业务目标 ip 地址数组\n        :type DestIp: list of str\n        """
        self.DestIp = None


    def _deserialize(self, params):
        self.DestIp = params.get("DestIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """设备信息结构体

    """

    def __init__(self):
        """
        :param Vendor: 运营商
1：移动 
2：电信
3：联通
4：广电
99：其他\n        :type Vendor: int\n        :param OS: 设备操作系统：
1：Android
2： IOS
99：其他\n        :type OS: int\n        :param DeviceId: 设备唯一标识
IOS 填写 IDFV
Android 填写 IMEI\n        :type DeviceId: str\n        :param PhoneNum: 用户手机号码\n        :type PhoneNum: str\n        :param Wireless: 无线信息
1：4G
2：5G
3：WIFI
99：其他\n        :type Wireless: int\n        """
        self.Vendor = None
        self.OS = None
        self.DeviceId = None
        self.PhoneNum = None
        self.Wireless = None


    def _deserialize(self, params):
        self.Vendor = params.get("Vendor")
        self.OS = params.get("OS")
        self.DeviceId = params.get("DeviceId")
        self.PhoneNum = params.get("PhoneNum")
        self.Wireless = params.get("Wireless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SrcAddressInfo(AbstractModel):
    """移动网络加速源地址结构体

    """

    def __init__(self):
        """
        :param SrcIpv4: 用户私网 ipv4 地址\n        :type SrcIpv4: str\n        :param SrcPublicIpv4: 用户公网 ipv4 地址\n        :type SrcPublicIpv4: str\n        :param SrcIpv6: 用户 ipv6 地址\n        :type SrcIpv6: str\n        """
        self.SrcIpv4 = None
        self.SrcPublicIpv4 = None
        self.SrcIpv6 = None


    def _deserialize(self, params):
        self.SrcIpv4 = params.get("SrcIpv4")
        self.SrcPublicIpv4 = params.get("SrcPublicIpv4")
        self.SrcIpv6 = params.get("SrcIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        