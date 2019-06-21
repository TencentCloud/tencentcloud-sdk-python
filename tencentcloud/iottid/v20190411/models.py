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


class BurnTidNotifyRequest(AbstractModel):
    """BurnTidNotify请求参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单编号
        :type OrderId: str
        :param Tid: TID编号
        :type Tid: str
        """
        self.OrderId = None
        self.Tid = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Tid = params.get("Tid")


class BurnTidNotifyResponse(AbstractModel):
    """BurnTidNotify返回参数结构体

    """

    def __init__(self):
        """
        :param Tid: 接收回执成功的TID
        :type Tid: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param OrderId: 订单编号
        :type OrderId: str
        :param Tid: TID编号
        :type Tid: str
        """
        self.OrderId = None
        self.Tid = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Tid = params.get("Tid")


class DeliverTidNotifyResponse(AbstractModel):
    """DeliverTidNotify返回参数结构体

    """

    def __init__(self):
        """
        :param RemaindCount: 剩余空发数量
        :type RemaindCount: int
        :param Tid: 已回执的TID编码
        :type Tid: str
        :param ProductKey: 产品公钥
        :type ProductKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param OrderId: 订单ID
        :type OrderId: str
        :param Quantity: 数量，1~10
        :type Quantity: int
        """
        self.OrderId = None
        self.Quantity = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Quantity = params.get("Quantity")


class DeliverTidsResponse(AbstractModel):
    """DeliverTids返回参数结构体

    """

    def __init__(self):
        """
        :param TidSet: 空发的TID信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TidSet: list of TidKeysInfo
        :param ProductKey: 产品公钥
        :type ProductKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribePermissionRequest(AbstractModel):
    """DescribePermission请求参数结构体

    """


class DescribePermissionResponse(AbstractModel):
    """DescribePermission返回参数结构体

    """

    def __init__(self):
        """
        :param EnterpriseUser: 企业用户
        :type EnterpriseUser: bool
        :param DownloadPermission: 下载控制台权限
        :type DownloadPermission: str
        :param UsePermission: 使用控制台权限
        :type UsePermission: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param OrderId: 订单编号
        :type OrderId: str
        :param Quantity: 下载数量：1~10
        :type Quantity: int
        """
        self.OrderId = None
        self.Quantity = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Quantity = params.get("Quantity")


class DownloadTidsResponse(AbstractModel):
    """DownloadTids返回参数结构体

    """

    def __init__(self):
        """
        :param TidSet: 下载的TID信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TidSet: list of TidKeysInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Tid: TID号码
        :type Tid: str
        :param PublicKey: 公钥
        :type PublicKey: str
        :param PrivateKey: 私钥
        :type PrivateKey: str
        :param Psk: 共享密钥
        :type Psk: str
        """
        self.Tid = None
        self.PublicKey = None
        self.PrivateKey = None
        self.Psk = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.Psk = params.get("Psk")