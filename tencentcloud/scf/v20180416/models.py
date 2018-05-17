# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class InvokeRequest(AbstractModel):
    """Invoke请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 函数名称。
        :type FunctionName: str
        :param InvocationType: RequestResponse(同步) 和 Event(异步)，默认为同步。
        :type InvocationType: str
        :param Qualifier: 触发函数的版本号。
        :type Qualifier: str
        :param ClientContext: 运行函数时的参数，以json格式传入，最大支持的参数长度是 1M。
        :type ClientContext: str
        :param LogType: 同步调用时指定该字段，返回值会包含4K的日志，可选值为None和Tail，默认值为None。当该值为Tail时，返回参数中的logMsg字段会包含对应的函数执行日志。
        :type LogType: str
        """
        self.FunctionName = None
        self.InvocationType = None
        self.Qualifier = None
        self.ClientContext = None
        self.LogType = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.InvocationType = params.get("InvocationType")
        self.Qualifier = params.get("Qualifier")
        self.ClientContext = params.get("ClientContext")
        self.LogType = params.get("LogType")


class InvokeResponse(AbstractModel):
    """Invoke返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 函数执行结果
        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Result()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class Result(AbstractModel):
    """运行函数的返回

    """

    def __init__(self):
        """
        :param Log: 表示执行过程中的日志输出，异步调用返回为空
        :type Log: str
        :param RetMsg: 表示执行函数的返回，异步调用返回为空
        :type RetMsg: str
        :param ErrMsg: 表示执行函数的错误返回信息，异步调用返回为空
        :type ErrMsg: str
        :param MemUsage: 执行函数时的内存大小，单位为Byte，异步调用返回为空
        :type MemUsage: int
        :param Duration: 表示执行函数的耗时，单位是毫秒，异步调用返回为空
        :type Duration: float
        :param BillDuration: 表示函数的计费耗时，单位是毫秒，异步调用返回为空
        :type BillDuration: int
        :param FunctionRequestId: 此次函数执行的Id
        :type FunctionRequestId: str
        :param InvokeResult: 0为正确，异步调用返回为空
        :type InvokeResult: int
        """
        self.Log = None
        self.RetMsg = None
        self.ErrMsg = None
        self.MemUsage = None
        self.Duration = None
        self.BillDuration = None
        self.FunctionRequestId = None
        self.InvokeResult = None


    def _deserialize(self, params):
        self.Log = params.get("Log")
        self.RetMsg = params.get("RetMsg")
        self.ErrMsg = params.get("ErrMsg")
        self.MemUsage = params.get("MemUsage")
        self.Duration = params.get("Duration")
        self.BillDuration = params.get("BillDuration")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.InvokeResult = params.get("InvokeResult")