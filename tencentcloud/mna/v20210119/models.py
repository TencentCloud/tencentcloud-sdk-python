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
        r"""
        :param CTCCToken: 电信鉴权的Token。要加速的电信手机终端访问 http://qos.189.cn/qos-api/getToken?appid=TencentCloud 页面，获取返回结果中result的值
        :type CTCCToken: str
        :param Province: 终端所处在的省份，建议不填写由服务端自动获取，若需填写请填写带有省、市、自治区、特别行政区等后缀的省份中文全称
        :type Province: str
        """
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
        


class Context(AbstractModel):
    """加速策略关键数据

    """

    def __init__(self):
        r"""
        :param NetworkData: 测速数据
        :type NetworkData: :class:`tencentcloud.mna.v20210119.models.NetworkData`
        :param ExpectedLowThreshold: 用户期望最低门限
        :type ExpectedLowThreshold: :class:`tencentcloud.mna.v20210119.models.ExpectedThreshold`
        :param ExpectedHighThreshold: 用户期望最高门限
        :type ExpectedHighThreshold: :class:`tencentcloud.mna.v20210119.models.ExpectedThreshold`
        """
        self.NetworkData = None
        self.ExpectedLowThreshold = None
        self.ExpectedHighThreshold = None


    def _deserialize(self, params):
        if params.get("NetworkData") is not None:
            self.NetworkData = NetworkData()
            self.NetworkData._deserialize(params.get("NetworkData"))
        if params.get("ExpectedLowThreshold") is not None:
            self.ExpectedLowThreshold = ExpectedThreshold()
            self.ExpectedLowThreshold._deserialize(params.get("ExpectedLowThreshold"))
        if params.get("ExpectedHighThreshold") is not None:
            self.ExpectedHighThreshold = ExpectedThreshold()
            self.ExpectedHighThreshold._deserialize(params.get("ExpectedHighThreshold"))
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
        r"""
        :param SrcAddressInfo: 加速业务源地址信息，SrcIpv6和（SrcIpv4+SrcPublicIpv4）二选一，目前Ipv6不可用，全部填写以Ipv4参数为准。
        :type SrcAddressInfo: :class:`tencentcloud.mna.v20210119.models.SrcAddressInfo`
        :param DestAddressInfo: 加速业务目标地址信息
        :type DestAddressInfo: :class:`tencentcloud.mna.v20210119.models.DestAddressInfo`
        :param QosMenu: 加速套餐
T100K：时延性保障 + 带宽保障上下行保障 100kbps
T200K：时延性保障 + 带宽保障上下行保障 200kbps
T400K：时延性保障 + 带宽保障上下行保障  400kbps
BD1M：带宽型保障 + 下行带宽保障1Mbps
BD2M：带宽型保障 + 下行带宽保障2Mbps
BD4M：带宽型保障 + 下行带宽保障4Mbps
BU1M：带宽型保障 + 上行带宽保障1Mbps
BU2M：带宽型保障 + 上行带宽保障2Mbps
BU4M：带宽型保障 + 上行带宽保障4Mbps
        :type QosMenu: str
        :param DeviceInfo: 申请加速的设备信息，包括运营商，操作系统，设备唯一标识等。
        :type DeviceInfo: :class:`tencentcloud.mna.v20210119.models.DeviceInfo`
        :param Duration: 期望加速时长（单位分钟），默认值30分钟
        :type Duration: int
        :param Capacity: 接口能力扩展，如果是电信用户，必须填充CTCC Token字段
        :type Capacity: :class:`tencentcloud.mna.v20210119.models.Capacity`
        :param TemplateId: 应用模板ID
        :type TemplateId: str
        :param Protocol: 针对特殊协议进行加速
1. IP （默认值）
2. UDP
3. TCP
        :type Protocol: int
        :param Context: 加速策略关键数据
        :type Context: :class:`tencentcloud.mna.v20210119.models.Context`
        :param Extern: 签名
        :type Extern: str
        """
        self.SrcAddressInfo = None
        self.DestAddressInfo = None
        self.QosMenu = None
        self.DeviceInfo = None
        self.Duration = None
        self.Capacity = None
        self.TemplateId = None
        self.Protocol = None
        self.Context = None
        self.Extern = None


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
        self.Protocol = params.get("Protocol")
        if params.get("Context") is not None:
            self.Context = Context()
            self.Context._deserialize(params.get("Context"))
        self.Extern = params.get("Extern")
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
        r"""
        :param SessionId: 单次加速唯一 Id
        :type SessionId: str
        :param Duration: 当前加速剩余时长（单位秒）
        :type Duration: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param SessionId: 单次加速唯一 Id
        :type SessionId: str
        """
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
        r"""
        :param SessionId: 单次加速唯一 Id
        :type SessionId: str
        :param Duration: 本次加速会话持续时间（单位秒）
        :type Duration: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionId = None
        self.Duration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Duration = params.get("Duration")
        self.RequestId = params.get("RequestId")


class DescribeQosRequest(AbstractModel):
    """DescribeQos请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: 单次加速唯一 Id
        :type SessionId: str
        """
        self.SessionId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQosResponse(AbstractModel):
    """DescribeQos返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 0：无匹配的加速中会话
1：存在匹配的加速中会话
        :type Status: int
        :param SrcPublicIpv4: 手机公网出口IP，仅匹配时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcPublicIpv4: str
        :param DestIpv4: 业务访问目的IP，仅匹配时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type DestIpv4: list of str
        :param Duration: 当前加速剩余时长（单位秒）有，仅匹配时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param QosMenu: 加速套餐类型，仅匹配时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type QosMenu: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.SrcPublicIpv4 = None
        self.DestIpv4 = None
        self.Duration = None
        self.QosMenu = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.SrcPublicIpv4 = params.get("SrcPublicIpv4")
        self.DestIpv4 = params.get("DestIpv4")
        self.Duration = params.get("Duration")
        self.QosMenu = params.get("QosMenu")
        self.RequestId = params.get("RequestId")


class DestAddressInfo(AbstractModel):
    """移动网络加速目标地址结构体

    """

    def __init__(self):
        r"""
        :param DestIp: 加速业务目标 ip 地址数组
        :type DestIp: list of str
        """
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
        r"""
        :param Vendor: 运营商
1：移动 
2：电信
3：联通
4：广电
99：其他
        :type Vendor: int
        :param OS: 设备操作系统：
1：Android
2： IOS
99：其他
        :type OS: int
        :param DeviceId: 设备唯一标识
IOS 填写 IDFV
Android 填写 IMEI
        :type DeviceId: str
        :param PhoneNum: 用户手机号码
        :type PhoneNum: str
        :param Wireless: 无线信息
1：4G
2：5G
3：WIFI
99：其他
        :type Wireless: int
        """
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
        


class ExpectedThreshold(AbstractModel):
    """用户期望门限

    """

    def __init__(self):
        r"""
        :param RTT: 期望发起加速的时延阈值
        :type RTT: float
        :param Loss: 期望发起加速的丢包率阈值
        :type Loss: float
        :param Jitter: 期望发起加速的抖动阈值
        :type Jitter: float
        """
        self.RTT = None
        self.Loss = None
        self.Jitter = None


    def _deserialize(self, params):
        self.RTT = params.get("RTT")
        self.Loss = params.get("Loss")
        self.Jitter = params.get("Jitter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkData(AbstractModel):
    """测速数据

    """

    def __init__(self):
        r"""
        :param RTT: 时延数组，最大长度30
        :type RTT: list of float
        :param Loss: 丢包率
        :type Loss: float
        :param Jitter: 抖动
        :type Jitter: float
        :param Timestamp: 10位秒级时间戳
        :type Timestamp: int
        """
        self.RTT = None
        self.Loss = None
        self.Jitter = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.RTT = params.get("RTT")
        self.Loss = params.get("Loss")
        self.Jitter = params.get("Jitter")
        self.Timestamp = params.get("Timestamp")
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
        r"""
        :param SrcIpv4: 用户私网 ipv4 地址
        :type SrcIpv4: str
        :param SrcPublicIpv4: 用户公网 ipv4 地址
        :type SrcPublicIpv4: str
        :param SrcIpv6: 用户 ipv6 地址
        :type SrcIpv6: str
        """
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
        