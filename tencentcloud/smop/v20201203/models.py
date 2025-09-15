# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""SubmitTaskEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountId: 用户唯一标识，最大长度为64
        :type AccountId: str
        :param _DeviceId: 用户设备ID，最大长度为64
        :type DeviceId: str
        :param _OrderId: 任务的唯一订单号，只能是数字、大小写字母，且在同一个产品ID下唯一，最大长度为64
        :type OrderId: str
        :param _Code: 任务事件Code，在腾讯安心用户运营平台下的任务事件列表中设置并获取
        :type Code: str
        :param _Async: 任务结果是否异步通知。0表示任务结果在返回信息中同步返回；1表示任务结果通过回调结果异步通知。
        :type Async: int
        :param _ProductId: 产品ID，可在腾讯安心用户运营平台的企业管理中获取
        :type ProductId: int
        :param _NotifyURL: 异步接收任务结果通知的回调地址。在Async为1的时候，会将任务结果通过该回调地址进行通知。
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
        r"""用户唯一标识，最大长度为64
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def DeviceId(self):
        r"""用户设备ID，最大长度为64
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def OrderId(self):
        r"""任务的唯一订单号，只能是数字、大小写字母，且在同一个产品ID下唯一，最大长度为64
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Code(self):
        r"""任务事件Code，在腾讯安心用户运营平台下的任务事件列表中设置并获取
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Async(self):
        r"""任务结果是否异步通知。0表示任务结果在返回信息中同步返回；1表示任务结果通过回调结果异步通知。
        :rtype: int
        """
        return self._Async

    @Async.setter
    def Async(self, Async):
        self._Async = Async

    @property
    def ProductId(self):
        r"""产品ID，可在腾讯安心用户运营平台的企业管理中获取
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def NotifyURL(self):
        r"""异步接收任务结果通知的回调地址。在Async为1的时候，会将任务结果通过该回调地址进行通知。
        :rtype: str
        """
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
    r"""SubmitTaskEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 任务的唯一订单号
        :type OrderId: str
        :param _Code: 信息码。0表示成功，-1标识失败
        :type Code: int
        :param _Message: 提示信息
        :type Message: str
        :param _Data: 任务处理结果列表
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
        r"""任务的唯一订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Code(self):
        r"""信息码。0表示成功，-1标识失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""提示信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""任务处理结果列表
        :rtype: list of TaskEventData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""后端提交任务事件返回Data复杂类型

    """

    def __init__(self):
        r"""
        :param _Code: 状态码，0为成功，-1为失败
        :type Code: int
        :param _Message: 提示信息
        :type Message: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _TaskOrderId: 当前完成或正在完成的安心用户运营平台的任务订单ID
        :type TaskOrderId: str
        :param _TaskCode: 当前任务订单状态码。1代表未完成；2代表已完成但未提交任务；3表示已完成，且已提交获得积分任务；4表示过期任务，提交后不获得积分。
        :type TaskCode: int
        :param _TaskCoinNumber: 获得积分数
        :type TaskCoinNumber: int
        :param _TaskType: 任务类型后台代码
        :type TaskType: int
        :param _TotalCoin: 用户的当前积分
        :type TotalCoin: int
        :param _Attach: 用户透传的附加数据
        :type Attach: str
        :param _DoneTimes: 计次任务当前完成次数
        :type DoneTimes: int
        :param _TotalTimes: 计次任务当前所需完成次数
        :type TotalTimes: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _GrowScore: 用户当前成长值
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
        r"""状态码，0为成功，-1为失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""提示信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskOrderId(self):
        r"""当前完成或正在完成的安心用户运营平台的任务订单ID
        :rtype: str
        """
        return self._TaskOrderId

    @TaskOrderId.setter
    def TaskOrderId(self, TaskOrderId):
        self._TaskOrderId = TaskOrderId

    @property
    def TaskCode(self):
        r"""当前任务订单状态码。1代表未完成；2代表已完成但未提交任务；3表示已完成，且已提交获得积分任务；4表示过期任务，提交后不获得积分。
        :rtype: int
        """
        return self._TaskCode

    @TaskCode.setter
    def TaskCode(self, TaskCode):
        self._TaskCode = TaskCode

    @property
    def TaskCoinNumber(self):
        r"""获得积分数
        :rtype: int
        """
        return self._TaskCoinNumber

    @TaskCoinNumber.setter
    def TaskCoinNumber(self, TaskCoinNumber):
        self._TaskCoinNumber = TaskCoinNumber

    @property
    def TaskType(self):
        r"""任务类型后台代码
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TotalCoin(self):
        r"""用户的当前积分
        :rtype: int
        """
        return self._TotalCoin

    @TotalCoin.setter
    def TotalCoin(self, TotalCoin):
        self._TotalCoin = TotalCoin

    @property
    def Attach(self):
        r"""用户透传的附加数据
        :rtype: str
        """
        return self._Attach

    @Attach.setter
    def Attach(self, Attach):
        self._Attach = Attach

    @property
    def DoneTimes(self):
        r"""计次任务当前完成次数
        :rtype: int
        """
        return self._DoneTimes

    @DoneTimes.setter
    def DoneTimes(self, DoneTimes):
        self._DoneTimes = DoneTimes

    @property
    def TotalTimes(self):
        r"""计次任务当前所需完成次数
        :rtype: int
        """
        return self._TotalTimes

    @TotalTimes.setter
    def TotalTimes(self, TotalTimes):
        self._TotalTimes = TotalTimes

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def GrowScore(self):
        r"""用户当前成长值
        :rtype: int
        """
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
        