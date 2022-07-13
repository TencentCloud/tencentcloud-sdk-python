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


class CallDeviceActionAsyncRequest(AbstractModel):
    """CallDeviceActionAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ActionId: 产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义
        :type ActionId: str
        :param InputParams: 输入参数
        :type InputParams: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.ActionId = None
        self.InputParams = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ActionId = params.get("ActionId")
        self.InputParams = params.get("InputParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDeviceActionAsyncResponse(AbstractModel):
    """CallDeviceActionAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClientToken: 调用Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param Status: 异步调用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClientToken = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CallDeviceActionSyncRequest(AbstractModel):
    """CallDeviceActionSync请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ActionId: 产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义
        :type ActionId: str
        :param InputParams: 输入参数
        :type InputParams: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.ActionId = None
        self.InputParams = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ActionId = params.get("ActionId")
        self.InputParams = params.get("InputParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDeviceActionSyncResponse(AbstractModel):
    """CallDeviceActionSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClientToken: 调用Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param OutputParams: 输出参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputParams: str
        :param Status: 返回状态，当设备不在线等部分情况，会通过该 Status 返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClientToken = None
        self.OutputParams = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.OutputParams = params.get("OutputParams")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductName: 产品名称
        :type ProductName: str
        :param DeviceType: 产品设备类型 1.普通设备 2.NVR设备
        :type DeviceType: int
        :param ProductVaildYears: 产品有效期
        :type ProductVaildYears: int
        :param Features: 设备功能码 ypsxth音频双向通话 spdxth视频单向通话 sxysp双向音视频
        :type Features: list of str
        :param ChipOs: 设备操作系统，通用设备填default
        :type ChipOs: str
        :param ChipManufactureId: 芯片厂商id，通用设备填default
        :type ChipManufactureId: str
        :param ChipId: 芯片id，通用设备填default
        :type ChipId: str
        :param ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param EncryptionType: 认证方式 只支持取值为2 psk认证
        :type EncryptionType: int
        :param NetType: 连接类型，wifi表示WIFI连接，cellular表示4G连接
        :type NetType: str
        """
        self.ProductName = None
        self.DeviceType = None
        self.ProductVaildYears = None
        self.Features = None
        self.ChipOs = None
        self.ChipManufactureId = None
        self.ChipId = None
        self.ProductDescription = None
        self.EncryptionType = None
        self.NetType = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.DeviceType = params.get("DeviceType")
        self.ProductVaildYears = params.get("ProductVaildYears")
        self.Features = params.get("Features")
        self.ChipOs = params.get("ChipOs")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")
        self.ProductDescription = params.get("ProductDescription")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 产品详情
        :type Data: :class:`tencentcloud.iotvideo.v20211125.models.VideoProduct`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoProduct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataStatsRequest(AbstractModel):
    """DescribeDeviceDataStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartDate: 开始日期
        :type StartDate: str
        :param EndDate: 结束日期
        :type EndDate: str
        :param ProductId: 产品id
        :type ProductId: str
        """
        self.StartDate = None
        self.EndDate = None
        self.ProductId = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataStatsResponse(AbstractModel):
    """DescribeDeviceDataStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegisterCnt: 累计注册设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisterCnt: int
        :param Data: 设备数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DeviceCntStats
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegisterCnt = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegisterCnt = params.get("RegisterCnt")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DeviceCntStats()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeMessageDataStatsRequest(AbstractModel):
    """DescribeMessageDataStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartDate: 统计开始日期
        :type StartDate: str
        :param EndDate: 统计结束日期
        :type EndDate: str
        :param ProductId: 产品id
        :type ProductId: str
        """
        self.StartDate = None
        self.EndDate = None
        self.ProductId = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageDataStatsResponse(AbstractModel):
    """DescribeMessageDataStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 消息数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of MessageCntStats
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = MessageCntStats()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DeviceCntStats(AbstractModel):
    """设备数量统计

    """

    def __init__(self):
        r"""
        :param Date: 统计日期
        :type Date: str
        :param NewRegisterCnt: 新增注册设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type NewRegisterCnt: int
        :param NewActivateCnt: 新增激活设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type NewActivateCnt: int
        :param ActiveCnt: 活跃设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveCnt: int
        """
        self.Date = None
        self.NewRegisterCnt = None
        self.NewActivateCnt = None
        self.ActiveCnt = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.NewRegisterCnt = params.get("NewRegisterCnt")
        self.NewActivateCnt = params.get("NewActivateCnt")
        self.ActiveCnt = params.get("ActiveCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceSignatureInfo(AbstractModel):
    """设备签名信息

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceSignature: 设备签名
        :type DeviceSignature: str
        """
        self.DeviceName = None
        self.DeviceSignature = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DeviceSignature = params.get("DeviceSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenSingleDeviceSignatureOfPublicRequest(AbstractModel):
    """GenSingleDeviceSignatureOfPublic请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 设备所属的产品ID
        :type ProductId: str
        :param DeviceName: 需要绑定的设备
        :type DeviceName: str
        :param Expire: 设备绑定签名的有效时间,以秒为单位。取值范围：0 < Expire <= 86400，Expire == -1（十年）
        :type Expire: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.Expire = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenSingleDeviceSignatureOfPublicResponse(AbstractModel):
    """GenSingleDeviceSignatureOfPublic返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceSignature: 设备签名信息
        :type DeviceSignature: :class:`tencentcloud.iotvideo.v20211125.models.DeviceSignatureInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceSignature = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceSignature") is not None:
            self.DeviceSignature = DeviceSignatureInfo()
            self.DeviceSignature._deserialize(params.get("DeviceSignature"))
        self.RequestId = params.get("RequestId")


class MessageCntStats(AbstractModel):
    """消息数量统计

    """

    def __init__(self):
        r"""
        :param Date: 统计日期
        :type Date: str
        :param UpMsgCnt: 物模型上行消息数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpMsgCnt: int
        :param DownMsgCnt: 物模型下行消息数
注意：此字段可能返回 null，表示取不到有效值。
        :type DownMsgCnt: int
        :param NtpMsgCnt: ntp消息数
注意：此字段可能返回 null，表示取不到有效值。
        :type NtpMsgCnt: int
        """
        self.Date = None
        self.UpMsgCnt = None
        self.DownMsgCnt = None
        self.NtpMsgCnt = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.UpMsgCnt = params.get("UpMsgCnt")
        self.DownMsgCnt = params.get("DownMsgCnt")
        self.NtpMsgCnt = params.get("NtpMsgCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoProduct(AbstractModel):
    """video产品元数据

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param DeviceType: 产品设备类型（普通设备)	1.普通设备
        :type DeviceType: int
        :param EncryptionType: 认证方式：2：PSK
        :type EncryptionType: int
        :param Features: 设备功能码
        :type Features: list of str
        :param ChipOs: 操作系统
        :type ChipOs: str
        :param ChipManufactureId: 芯片厂商id
        :type ChipManufactureId: str
        :param ChipId: 芯片id
        :type ChipId: str
        :param ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param CreateTime: 创建时间unix时间戳
        :type CreateTime: int
        :param UpdateTime: 修改时间unix时间戳
        :type UpdateTime: int
        :param NetType: 连接类型，wifi表示WIFI连接，cellular表示4G连接
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: str
        """
        self.ProductId = None
        self.ProductName = None
        self.DeviceType = None
        self.EncryptionType = None
        self.Features = None
        self.ChipOs = None
        self.ChipManufactureId = None
        self.ChipId = None
        self.ProductDescription = None
        self.CreateTime = None
        self.UpdateTime = None
        self.NetType = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.DeviceType = params.get("DeviceType")
        self.EncryptionType = params.get("EncryptionType")
        self.Features = params.get("Features")
        self.ChipOs = params.get("ChipOs")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")
        self.ProductDescription = params.get("ProductDescription")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        