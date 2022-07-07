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
        