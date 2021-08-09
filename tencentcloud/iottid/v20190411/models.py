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


class AuthTestTidRequest(AbstractModel):
    """AuthTestTid请求参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备端SDK填入测试TID参数后生成的加密数据串\n        :type Data: str\n        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthTestTidResponse(AbstractModel):
    """AuthTestTid返回参数结构体

    """

    def __init__(self):
        """
        :param Pass: 认证结果\n        :type Pass: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Pass = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Pass = params.get("Pass")
        self.RequestId = params.get("RequestId")


class BurnTidNotifyRequest(AbstractModel):
    """BurnTidNotify请求参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单编号\n        :type OrderId: str\n        :param Tid: TID编号\n        :type Tid: str\n        """
        self.OrderId = None
        self.Tid = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Tid = params.get("Tid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BurnTidNotifyResponse(AbstractModel):
    """BurnTidNotify返回参数结构体

    """

    def __init__(self):
        """
        :param Tid: 接收回执成功的TID\n        :type Tid: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Tid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.RequestId = params.get("RequestId")


class DeliverTidNotifyRequest(AbstractModel):
    """DeliverTidNotify请求参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单编号\n        :type OrderId: str\n        :param Tid: TID编号\n        :type Tid: str\n        """
        self.OrderId = None
        self.Tid = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Tid = params.get("Tid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeliverTidNotifyResponse(AbstractModel):
    """DeliverTidNotify返回参数结构体

    """

    def __init__(self):
        """
        :param RemaindCount: 剩余空发数量\n        :type RemaindCount: int\n        :param Tid: 已回执的TID编码\n        :type Tid: str\n        :param ProductKey: 产品公钥\n        :type ProductKey: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RemaindCount = None
        self.Tid = None
        self.ProductKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RemaindCount = params.get("RemaindCount")
        self.Tid = params.get("Tid")
        self.ProductKey = params.get("ProductKey")
        self.RequestId = params.get("RequestId")


class DeliverTidsRequest(AbstractModel):
    """DeliverTids请求参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单ID\n        :type OrderId: str\n        :param Quantity: 数量，1~100\n        :type Quantity: int\n        """
        self.OrderId = None
        self.Quantity = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Quantity = params.get("Quantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeliverTidsResponse(AbstractModel):
    """DeliverTids返回参数结构体

    """

    def __init__(self):
        """
        :param TidSet: 空发的TID信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type TidSet: list of TidKeysInfo\n        :param ProductKey: 产品公钥\n        :type ProductKey: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TidSet = None
        self.ProductKey = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TidSet") is not None:
            self.TidSet = []
            for item in params.get("TidSet"):
                obj = TidKeysInfo()
                obj._deserialize(item)
                self.TidSet.append(obj)
        self.ProductKey = params.get("ProductKey")
        self.RequestId = params.get("RequestId")


class DescribeAvailableLibCountRequest(AbstractModel):
    """DescribeAvailableLibCount请求参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单编号\n        :type OrderId: str\n        """
        self.OrderId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableLibCountResponse(AbstractModel):
    """DescribeAvailableLibCount返回参数结构体

    """

    def __init__(self):
        """
        :param Quantity: 可空发的白盒密钥数量\n        :type Quantity: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Quantity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Quantity = params.get("Quantity")
        self.RequestId = params.get("RequestId")


class DescribePermissionRequest(AbstractModel):
    """DescribePermission请求参数结构体

    """


class DescribePermissionResponse(AbstractModel):
    """DescribePermission返回参数结构体

    """

    def __init__(self):
        """
        :param EnterpriseUser: 企业用户\n        :type EnterpriseUser: bool\n        :param DownloadPermission: 下载控制台权限\n        :type DownloadPermission: str\n        :param UsePermission: 使用控制台权限\n        :type UsePermission: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EnterpriseUser = None
        self.DownloadPermission = None
        self.UsePermission = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnterpriseUser = params.get("EnterpriseUser")
        self.DownloadPermission = params.get("DownloadPermission")
        self.UsePermission = params.get("UsePermission")
        self.RequestId = params.get("RequestId")


class DownloadTidsRequest(AbstractModel):
    """DownloadTids请求参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单编号\n        :type OrderId: str\n        :param Quantity: 下载数量：1~10\n        :type Quantity: int\n        """
        self.OrderId = None
        self.Quantity = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Quantity = params.get("Quantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadTidsResponse(AbstractModel):
    """DownloadTids返回参数结构体

    """

    def __init__(self):
        """
        :param TidSet: 下载的TID信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TidSet: list of TidKeysInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TidSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TidSet") is not None:
            self.TidSet = []
            for item in params.get("TidSet"):
                obj = TidKeysInfo()
                obj._deserialize(item)
                self.TidSet.append(obj)
        self.RequestId = params.get("RequestId")


class TidKeysInfo(AbstractModel):
    """系统生成的TID和密钥信息

    """

    def __init__(self):
        """
        :param Tid: TID号码\n        :type Tid: str\n        :param PublicKey: 公钥\n        :type PublicKey: str\n        :param PrivateKey: 私钥\n        :type PrivateKey: str\n        :param Psk: 共享密钥\n        :type Psk: str\n        :param DownloadUrl: 软加固白盒密钥下载地址\n        :type DownloadUrl: str\n        :param DeviceCode: 软加固设备标识码\n        :type DeviceCode: str\n        """
        self.Tid = None
        self.PublicKey = None
        self.PrivateKey = None
        self.Psk = None
        self.DownloadUrl = None
        self.DeviceCode = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.Psk = params.get("Psk")
        self.DownloadUrl = params.get("DownloadUrl")
        self.DeviceCode = params.get("DeviceCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDeviceUniqueCodeRequest(AbstractModel):
    """UploadDeviceUniqueCode请求参数结构体

    """

    def __init__(self):
        """
        :param CodeSet: 硬件唯一标识码\n        :type CodeSet: list of str\n        :param OrderId: 硬件标识码绑定的申请编号\n        :type OrderId: str\n        """
        self.CodeSet = None
        self.OrderId = None


    def _deserialize(self, params):
        self.CodeSet = params.get("CodeSet")
        self.OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDeviceUniqueCodeResponse(AbstractModel):
    """UploadDeviceUniqueCode返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 本次已上传数量\n        :type Count: int\n        :param ExistedCodeSet: 重复的硬件唯一标识码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExistedCodeSet: list of str\n        :param LeftQuantity: 剩余可上传数量\n        :type LeftQuantity: int\n        :param IllegalCodeSet: 错误的硬件唯一标识码
注意：此字段可能返回 null，表示取不到有效值。\n        :type IllegalCodeSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Count = None
        self.ExistedCodeSet = None
        self.LeftQuantity = None
        self.IllegalCodeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.ExistedCodeSet = params.get("ExistedCodeSet")
        self.LeftQuantity = params.get("LeftQuantity")
        self.IllegalCodeSet = params.get("IllegalCodeSet")
        self.RequestId = params.get("RequestId")


class VerifyChipBurnInfoRequest(AbstractModel):
    """VerifyChipBurnInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Data: 验证数据\n        :type Data: str\n        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyChipBurnInfoResponse(AbstractModel):
    """VerifyChipBurnInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Pass: 验证结果\n        :type Pass: bool\n        :param VerifiedTimes: 已验证次数\n        :type VerifiedTimes: int\n        :param LeftTimes: 剩余验证次数\n        :type LeftTimes: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Pass = None
        self.VerifiedTimes = None
        self.LeftTimes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Pass = params.get("Pass")
        self.VerifiedTimes = params.get("VerifiedTimes")
        self.LeftTimes = params.get("LeftTimes")
        self.RequestId = params.get("RequestId")