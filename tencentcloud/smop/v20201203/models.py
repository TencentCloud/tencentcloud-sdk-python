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


class SubmitTaskEventRequest(AbstractModel):
    """SubmitTaskEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccountId: 用户ID
        :type AccountId: str
        :param DeviceId: 设备ID
        :type DeviceId: str
        :param OrderId: 订单ID
        :type OrderId: str
        :param Code: 任务事件Code
        :type Code: str
        :param Async: 同步异步方式：0为同步、1位异步
        :type Async: int
        :param ProductId: 产品ID
        :type ProductId: int
        :param NotifyURL: 回调地址
        :type NotifyURL: str
        """
        self.AccountId = None
        self.DeviceId = None
        self.OrderId = None
        self.Code = None
        self.Async = None
        self.ProductId = None
        self.NotifyURL = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.DeviceId = params.get("DeviceId")
        self.OrderId = params.get("OrderId")
        self.Code = params.get("Code")
        self.Async = params.get("Async")
        self.ProductId = params.get("ProductId")
        self.NotifyURL = params.get("NotifyURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTaskEventResponse(AbstractModel):
    """SubmitTaskEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param OrderId: 订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param Code: 信息码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param Message: success
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Data: 任务处理结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TaskEventData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrderId = None
        self.Code = None
        self.Message = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TaskEventData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class TaskEventData(AbstractModel):
    """后端提交任务事件返回Data复杂类型

    """

    def __init__(self):
        r"""
        :param Code: 状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param Message: 提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param TaskOrderId: 当前完成或正在完成的任务订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskOrderId: str
        :param TaskCode: 当前任务订单状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCode: int
        :param TaskCoinNumber: 获得积分数/成长值
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCoinNumber: int
        :param TaskType: 任务类型后台代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: int
        :param TotalCoin: 当前积分
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCoin: int
        :param Attach: 用户透传的代码块
注意：此字段可能返回 null，表示取不到有效值。
        :type Attach: str
        :param DoneTimes: 计次任务当前完成次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DoneTimes: int
        :param TotalTimes: 计次任务当前所需完成次数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTimes: int
        :param TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param GrowScore: 当前成长值
注意：此字段可能返回 null，表示取不到有效值。
        :type GrowScore: int
        """
        self.Code = None
        self.Message = None
        self.TaskId = None
        self.TaskOrderId = None
        self.TaskCode = None
        self.TaskCoinNumber = None
        self.TaskType = None
        self.TotalCoin = None
        self.Attach = None
        self.DoneTimes = None
        self.TotalTimes = None
        self.TaskName = None
        self.GrowScore = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.TaskId = params.get("TaskId")
        self.TaskOrderId = params.get("TaskOrderId")
        self.TaskCode = params.get("TaskCode")
        self.TaskCoinNumber = params.get("TaskCoinNumber")
        self.TaskType = params.get("TaskType")
        self.TotalCoin = params.get("TotalCoin")
        self.Attach = params.get("Attach")
        self.DoneTimes = params.get("DoneTimes")
        self.TotalTimes = params.get("TotalTimes")
        self.TaskName = params.get("TaskName")
        self.GrowScore = params.get("GrowScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        