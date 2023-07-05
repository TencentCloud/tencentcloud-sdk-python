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
        r"""
        :param _Data: 设备端SDK填入测试TID参数后生成的加密数据串
        :type Data: str
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthTestTidResponse(AbstractModel):
    """AuthTestTid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Pass: 认证结果
        :type Pass: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Pass = None
        self._RequestId = None

    @property
    def Pass(self):
        return self._Pass

    @Pass.setter
    def Pass(self, Pass):
        self._Pass = Pass

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Pass = params.get("Pass")
        self._RequestId = params.get("RequestId")


class BurnTidNotifyRequest(AbstractModel):
    """BurnTidNotify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单编号
        :type OrderId: str
        :param _Tid: TID编号
        :type Tid: str
        """
        self._OrderId = None
        self._Tid = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Tid(self):
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Tid = params.get("Tid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BurnTidNotifyResponse(AbstractModel):
    """BurnTidNotify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 接收回执成功的TID
        :type Tid: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tid = None
        self._RequestId = None

    @property
    def Tid(self):
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._RequestId = params.get("RequestId")


class DeliverTidNotifyRequest(AbstractModel):
    """DeliverTidNotify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单编号
        :type OrderId: str
        :param _Tid: TID编号
        :type Tid: str
        """
        self._OrderId = None
        self._Tid = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Tid(self):
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Tid = params.get("Tid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeliverTidNotifyResponse(AbstractModel):
    """DeliverTidNotify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RemaindCount: 剩余空发数量
        :type RemaindCount: int
        :param _Tid: 已回执的TID编码
        :type Tid: str
        :param _ProductKey: 产品公钥
        :type ProductKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RemaindCount = None
        self._Tid = None
        self._ProductKey = None
        self._RequestId = None

    @property
    def RemaindCount(self):
        return self._RemaindCount

    @RemaindCount.setter
    def RemaindCount(self, RemaindCount):
        self._RemaindCount = RemaindCount

    @property
    def Tid(self):
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def ProductKey(self):
        return self._ProductKey

    @ProductKey.setter
    def ProductKey(self, ProductKey):
        self._ProductKey = ProductKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RemaindCount = params.get("RemaindCount")
        self._Tid = params.get("Tid")
        self._ProductKey = params.get("ProductKey")
        self._RequestId = params.get("RequestId")


class DeliverTidsRequest(AbstractModel):
    """DeliverTids请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单ID
        :type OrderId: str
        :param _Quantity: 数量，1~100
        :type Quantity: int
        """
        self._OrderId = None
        self._Quantity = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Quantity = params.get("Quantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeliverTidsResponse(AbstractModel):
    """DeliverTids返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TidSet: 空发的TID信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TidSet: list of TidKeysInfo
        :param _ProductKey: 产品公钥
        :type ProductKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TidSet = None
        self._ProductKey = None
        self._RequestId = None

    @property
    def TidSet(self):
        return self._TidSet

    @TidSet.setter
    def TidSet(self, TidSet):
        self._TidSet = TidSet

    @property
    def ProductKey(self):
        return self._ProductKey

    @ProductKey.setter
    def ProductKey(self, ProductKey):
        self._ProductKey = ProductKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TidSet") is not None:
            self._TidSet = []
            for item in params.get("TidSet"):
                obj = TidKeysInfo()
                obj._deserialize(item)
                self._TidSet.append(obj)
        self._ProductKey = params.get("ProductKey")
        self._RequestId = params.get("RequestId")


class DescribeAvailableLibCountRequest(AbstractModel):
    """DescribeAvailableLibCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单编号
        :type OrderId: str
        """
        self._OrderId = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableLibCountResponse(AbstractModel):
    """DescribeAvailableLibCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Quantity: 可空发的白盒密钥数量
        :type Quantity: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Quantity = None
        self._RequestId = None

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Quantity = params.get("Quantity")
        self._RequestId = params.get("RequestId")


class DescribePermissionRequest(AbstractModel):
    """DescribePermission请求参数结构体

    """


class DescribePermissionResponse(AbstractModel):
    """DescribePermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnterpriseUser: 企业用户
        :type EnterpriseUser: bool
        :param _DownloadPermission: 下载控制台权限
        :type DownloadPermission: str
        :param _UsePermission: 使用控制台权限
        :type UsePermission: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnterpriseUser = None
        self._DownloadPermission = None
        self._UsePermission = None
        self._RequestId = None

    @property
    def EnterpriseUser(self):
        return self._EnterpriseUser

    @EnterpriseUser.setter
    def EnterpriseUser(self, EnterpriseUser):
        self._EnterpriseUser = EnterpriseUser

    @property
    def DownloadPermission(self):
        return self._DownloadPermission

    @DownloadPermission.setter
    def DownloadPermission(self, DownloadPermission):
        self._DownloadPermission = DownloadPermission

    @property
    def UsePermission(self):
        return self._UsePermission

    @UsePermission.setter
    def UsePermission(self, UsePermission):
        self._UsePermission = UsePermission

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnterpriseUser = params.get("EnterpriseUser")
        self._DownloadPermission = params.get("DownloadPermission")
        self._UsePermission = params.get("UsePermission")
        self._RequestId = params.get("RequestId")


class DownloadTidsRequest(AbstractModel):
    """DownloadTids请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单编号
        :type OrderId: str
        :param _Quantity: 下载数量：1~10
        :type Quantity: int
        """
        self._OrderId = None
        self._Quantity = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Quantity = params.get("Quantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadTidsResponse(AbstractModel):
    """DownloadTids返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TidSet: 下载的TID信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TidSet: list of TidKeysInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TidSet = None
        self._RequestId = None

    @property
    def TidSet(self):
        return self._TidSet

    @TidSet.setter
    def TidSet(self, TidSet):
        self._TidSet = TidSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TidSet") is not None:
            self._TidSet = []
            for item in params.get("TidSet"):
                obj = TidKeysInfo()
                obj._deserialize(item)
                self._TidSet.append(obj)
        self._RequestId = params.get("RequestId")


class TidKeysInfo(AbstractModel):
    """系统生成的TID和密钥信息

    """

    def __init__(self):
        r"""
        :param _Tid: TID号码
        :type Tid: str
        :param _PublicKey: 公钥
        :type PublicKey: str
        :param _PrivateKey: 私钥
        :type PrivateKey: str
        :param _Psk: 共享密钥
        :type Psk: str
        :param _DownloadUrl: 软加固白盒密钥下载地址
        :type DownloadUrl: str
        :param _DeviceCode: 软加固设备标识码
        :type DeviceCode: str
        """
        self._Tid = None
        self._PublicKey = None
        self._PrivateKey = None
        self._Psk = None
        self._DownloadUrl = None
        self._DeviceCode = None

    @property
    def Tid(self):
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def Psk(self):
        return self._Psk

    @Psk.setter
    def Psk(self, Psk):
        self._Psk = Psk

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def DeviceCode(self):
        return self._DeviceCode

    @DeviceCode.setter
    def DeviceCode(self, DeviceCode):
        self._DeviceCode = DeviceCode


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._PublicKey = params.get("PublicKey")
        self._PrivateKey = params.get("PrivateKey")
        self._Psk = params.get("Psk")
        self._DownloadUrl = params.get("DownloadUrl")
        self._DeviceCode = params.get("DeviceCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDeviceUniqueCodeRequest(AbstractModel):
    """UploadDeviceUniqueCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeSet: 硬件唯一标识码
        :type CodeSet: list of str
        :param _OrderId: 硬件标识码绑定的申请编号
        :type OrderId: str
        """
        self._CodeSet = None
        self._OrderId = None

    @property
    def CodeSet(self):
        return self._CodeSet

    @CodeSet.setter
    def CodeSet(self, CodeSet):
        self._CodeSet = CodeSet

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._CodeSet = params.get("CodeSet")
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDeviceUniqueCodeResponse(AbstractModel):
    """UploadDeviceUniqueCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 本次已上传数量
        :type Count: int
        :param _ExistedCodeSet: 重复的硬件唯一标识码
注意：此字段可能返回 null，表示取不到有效值。
        :type ExistedCodeSet: list of str
        :param _LeftQuantity: 剩余可上传数量
        :type LeftQuantity: int
        :param _IllegalCodeSet: 错误的硬件唯一标识码
注意：此字段可能返回 null，表示取不到有效值。
        :type IllegalCodeSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._ExistedCodeSet = None
        self._LeftQuantity = None
        self._IllegalCodeSet = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ExistedCodeSet(self):
        return self._ExistedCodeSet

    @ExistedCodeSet.setter
    def ExistedCodeSet(self, ExistedCodeSet):
        self._ExistedCodeSet = ExistedCodeSet

    @property
    def LeftQuantity(self):
        return self._LeftQuantity

    @LeftQuantity.setter
    def LeftQuantity(self, LeftQuantity):
        self._LeftQuantity = LeftQuantity

    @property
    def IllegalCodeSet(self):
        return self._IllegalCodeSet

    @IllegalCodeSet.setter
    def IllegalCodeSet(self, IllegalCodeSet):
        self._IllegalCodeSet = IllegalCodeSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._ExistedCodeSet = params.get("ExistedCodeSet")
        self._LeftQuantity = params.get("LeftQuantity")
        self._IllegalCodeSet = params.get("IllegalCodeSet")
        self._RequestId = params.get("RequestId")


class VerifyChipBurnInfoRequest(AbstractModel):
    """VerifyChipBurnInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 验证数据
        :type Data: str
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyChipBurnInfoResponse(AbstractModel):
    """VerifyChipBurnInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Pass: 验证结果
        :type Pass: bool
        :param _VerifiedTimes: 已验证次数
        :type VerifiedTimes: int
        :param _LeftTimes: 剩余验证次数
        :type LeftTimes: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Pass = None
        self._VerifiedTimes = None
        self._LeftTimes = None
        self._RequestId = None

    @property
    def Pass(self):
        return self._Pass

    @Pass.setter
    def Pass(self, Pass):
        self._Pass = Pass

    @property
    def VerifiedTimes(self):
        return self._VerifiedTimes

    @VerifiedTimes.setter
    def VerifiedTimes(self, VerifiedTimes):
        self._VerifiedTimes = VerifiedTimes

    @property
    def LeftTimes(self):
        return self._LeftTimes

    @LeftTimes.setter
    def LeftTimes(self, LeftTimes):
        self._LeftTimes = LeftTimes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Pass = params.get("Pass")
        self._VerifiedTimes = params.get("VerifiedTimes")
        self._LeftTimes = params.get("LeftTimes")
        self._RequestId = params.get("RequestId")