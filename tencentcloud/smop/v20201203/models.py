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
        :param _AccountId: 用户ID
        :type AccountId: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _OrderId: 订单ID
        :type OrderId: str
        :param _Code: 任务事件Code
        :type Code: str
        :param _Async: 同步异步方式：0为同步、1位异步
        :type Async: int
        :param _ProductId: 产品ID
        :type ProductId: int
        :param _NotifyURL: 回调地址
        :type NotifyURL: str
        """
        self._AccountId = None
        self._DeviceId = None
        self._OrderId = None
        self._Code = None
        self._Async = None
        self._ProductId = None
        self._NotifyURL = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Async(self):
        return self._Async

    @Async.setter
    def Async(self, Async):
        self._Async = Async

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def NotifyURL(self):
        return self._NotifyURL

    @NotifyURL.setter
    def NotifyURL(self, NotifyURL):
        self._NotifyURL = NotifyURL


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._DeviceId = params.get("DeviceId")
        self._OrderId = params.get("OrderId")
        self._Code = params.get("Code")
        self._Async = params.get("Async")
        self._ProductId = params.get("ProductId")
        self._NotifyURL = params.get("NotifyURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTaskEventResponse(AbstractModel):
    """SubmitTaskEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param _Code: 信息码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Message: success
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Data: 任务处理结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TaskEventData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskEventData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class TaskEventData(AbstractModel):
    """后端提交任务事件返回Data复杂类型

    """

    def __init__(self):
        r"""
        :param _Code: 状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Message: 提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _TaskOrderId: 当前完成或正在完成的任务订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskOrderId: str
        :param _TaskCode: 当前任务订单状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCode: int
        :param _TaskCoinNumber: 获得积分数/成长值
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCoinNumber: int
        :param _TaskType: 任务类型后台代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: int
        :param _TotalCoin: 当前积分
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCoin: int
        :param _Attach: 用户透传的代码块
注意：此字段可能返回 null，表示取不到有效值。
        :type Attach: str
        :param _DoneTimes: 计次任务当前完成次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DoneTimes: int
        :param _TotalTimes: 计次任务当前所需完成次数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTimes: int
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _GrowScore: 当前成长值
注意：此字段可能返回 null，表示取不到有效值。
        :type GrowScore: int
        """
        self._Code = None
        self._Message = None
        self._TaskId = None
        self._TaskOrderId = None
        self._TaskCode = None
        self._TaskCoinNumber = None
        self._TaskType = None
        self._TotalCoin = None
        self._Attach = None
        self._DoneTimes = None
        self._TotalTimes = None
        self._TaskName = None
        self._GrowScore = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskOrderId(self):
        return self._TaskOrderId

    @TaskOrderId.setter
    def TaskOrderId(self, TaskOrderId):
        self._TaskOrderId = TaskOrderId

    @property
    def TaskCode(self):
        return self._TaskCode

    @TaskCode.setter
    def TaskCode(self, TaskCode):
        self._TaskCode = TaskCode

    @property
    def TaskCoinNumber(self):
        return self._TaskCoinNumber

    @TaskCoinNumber.setter
    def TaskCoinNumber(self, TaskCoinNumber):
        self._TaskCoinNumber = TaskCoinNumber

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TotalCoin(self):
        return self._TotalCoin

    @TotalCoin.setter
    def TotalCoin(self, TotalCoin):
        self._TotalCoin = TotalCoin

    @property
    def Attach(self):
        return self._Attach

    @Attach.setter
    def Attach(self, Attach):
        self._Attach = Attach

    @property
    def DoneTimes(self):
        return self._DoneTimes

    @DoneTimes.setter
    def DoneTimes(self, DoneTimes):
        self._DoneTimes = DoneTimes

    @property
    def TotalTimes(self):
        return self._TotalTimes

    @TotalTimes.setter
    def TotalTimes(self, TotalTimes):
        self._TotalTimes = TotalTimes

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def GrowScore(self):
        return self._GrowScore

    @GrowScore.setter
    def GrowScore(self, GrowScore):
        self._GrowScore = GrowScore


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._TaskId = params.get("TaskId")
        self._TaskOrderId = params.get("TaskOrderId")
        self._TaskCode = params.get("TaskCode")
        self._TaskCoinNumber = params.get("TaskCoinNumber")
        self._TaskType = params.get("TaskType")
        self._TotalCoin = params.get("TotalCoin")
        self._Attach = params.get("Attach")
        self._DoneTimes = params.get("DoneTimes")
        self._TotalTimes = params.get("TotalTimes")
        self._TaskName = params.get("TaskName")
        self._GrowScore = params.get("GrowScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        