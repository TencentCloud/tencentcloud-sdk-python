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


class Code(AbstractModel):
    """函数代码

    """

    def __init__(self):
        """
        :param CosBucketName: 对象存储桶名称
        :type CosBucketName: str
        :param CosObjectName: 对象存储对象路径
        :type CosObjectName: str
        :param ZipFile: 包含函数代码文件及其依赖项的 zip 格式文件，使用该接口时要求将 zip 文件的内容转成 base64 编码，最大支持20M
        :type ZipFile: str
        :param CosBucketRegion: 对象存储的地域，地域为北京时需要传入ap-beijing,北京一区时需要传递ap-beijing-1，其他的地域不需要传递。
        :type CosBucketRegion: str
        """
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.CosBucketRegion = None


    def _deserialize(self, params):
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.CosBucketRegion = params.get("CosBucketRegion")


class CreateFunctionRequest(AbstractModel):
    """CreateFunction请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 创建的函数名称，函数名称支持26个英文字母大小写、数字、连接符和下划线，第一个字符只能以字母开头，最后一个字符不能为连接符或者下划线，名称长度2-60
        :type FunctionName: str
        :param Code: 函数的代码. 注意：不能同时指定Cos与ZipFile
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param Handler: 函数处理方法名称，名称格式支持 "文件名称.方法名称" 形式，文件名称和函数名称之间以"."隔开，文件名称和函数名称要求以字母开始和结尾，中间允许插入字母、数字、下划线和连接符，文件名称和函数名字的长度要求是 2-60 个字符
        :type Handler: str
        :param Description: 函数描述,最大支持 1000 个英文字母、数字、空格、逗号、换行符和英文句号，支持中文
        :type Description: str
        :param MemorySize: 函数运行时内存大小，默认为 128M，可选范围 128MB-1536MB，并且以 128MB 为阶梯
        :type MemorySize: int
        :param Timeout: 函数最长执行时间，单位为秒，可选值范围 1-300 秒，默认为 3 秒
        :type Timeout: int
        :param Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param Runtime: 函数运行环境，目前仅支持 Python2.7，Python3.6，Nodejs6.10， PHP5， PHP7，Golang1 和 Java8，默认Python2.7
        :type Runtime: str
        :param VpcConfig: 函数的私有网络配置
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        """
        self.FunctionName = None
        self.Code = None
        self.Handler = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Environment = None
        self.Runtime = None
        self.VpcConfig = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        if params.get("Code") is not None:
            self.Code = Code()
            self.Code._deserialize(params.get("Code"))
        self.Handler = params.get("Handler")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.Runtime = params.get("Runtime")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))


class CreateFunctionResponse(AbstractModel):
    """CreateFunction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTriggerRequest(AbstractModel):
    """CreateTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 新建触发器绑定的函数名称
        :type FunctionName: str
        :param TriggerName: 新建触发器名称。如果是定时触发器，名称支持英文字母、数字、连接符和下划线，最长100个字符；如果是其他触发器，见具体触发器绑定参数的说明
        :type TriggerName: str
        :param Type: 触发器类型，目前支持 cos 、cmq、 timers、 ckafka类型
        :type Type: str
        :param TriggerDesc: 触发器对应的参数，如果是 timer 类型的触发器其内容是 Linux cron 表达式，如果是其他触发器，见具体触发器说明
        :type TriggerDesc: str
        :param Qualifier: 函数的版本
        :type Qualifier: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Qualifier = params.get("Qualifier")


class CreateTriggerResponse(AbstractModel):
    """CreateTrigger返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 要删除的函数名称
        :type FunctionName: str
        """
        self.FunctionName = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTriggerRequest(AbstractModel):
    """DeleteTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param TriggerName: 要删除的触发器名称
        :type TriggerName: str
        :param Type: 要删除的触发器类型，目前支持 cos 、cmq、 timer、ckafka 类型
        :type Type: str
        :param TriggerDesc: 如果删除的触发器类型为 COS 触发器，该字段为必填值，存放 JSON 格式的数据 {"event":"cos:ObjectCreated:*"}，数据内容和 SetTrigger 接口中该字段的格式相同；如果删除的触发器类型为定时触发器或 CMQ 触发器，可以不指定该字段
        :type TriggerDesc: str
        :param Qualifier: 函数的版本信息
        :type Qualifier: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Qualifier = params.get("Qualifier")


class DeleteTriggerResponse(AbstractModel):
    """DeleteTrigger返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """函数的环境变量参数

    """

    def __init__(self):
        """
        :param Variables: 环境变量数组
        :type Variables: list of Variable
        """
        self.Variables = None


    def _deserialize(self, params):
        if params.get("Variables") is not None:
            self.Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self.Variables.append(obj)


class Filter(AbstractModel):
    """日志过滤条件，用于区分正确与错误日志

    """

    def __init__(self):
        """
        :param RetCode: filter.RetCode=not0 表示只返回错误日志，filter.RetCode=is0 表示只返回正确日志，无输入则返回所有日志。
        :type RetCode: str
        """
        self.RetCode = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")


class Function(AbstractModel):
    """函数列表

    """

    def __init__(self):
        """
        :param ModTime: 修改时间
        :type ModTime: str
        :param AddTime: 创建时间
        :type AddTime: str
        :param Runtime: 运行时
        :type Runtime: str
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param FunctionId: 函数ID
        :type FunctionId: str
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.ModTime = None
        self.AddTime = None
        self.Runtime = None
        self.FunctionName = None
        self.FunctionId = None
        self.Namespace = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.AddTime = params.get("AddTime")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        self.FunctionId = params.get("FunctionId")
        self.Namespace = params.get("Namespace")


class FunctionLog(AbstractModel):
    """日志信息

    """

    def __init__(self):
        """
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param RetMsg: 函数执行完成后的返回值
        :type RetMsg: str
        :param RequestId: 执行该函数对应的requestId
        :type RequestId: str
        :param StartTime: 函数开始执行时的时间点
        :type StartTime: str
        :param RetCode: 函数执行结果，如果是 0 表示执行成功，其他值表示失败
        :type RetCode: int
        :param InvokeFinished: 函数调用是否结束，如果是 1 表示执行结束，其他值表示调用异常
        :type InvokeFinished: int
        :param Duration: 函数执行耗时，单位为 ms
        :type Duration: float
        :param BillDuration: 函数计费时间，根据 duration 向上取最近的 100ms，单位为ms
        :type BillDuration: int
        :param MemUsage: 函数执行时消耗实际内存大小，单位为 Byte
        :type MemUsage: int
        :param Log: 函数执行过程中的日志输出
        :type Log: str
        """
        self.FunctionName = None
        self.RetMsg = None
        self.RequestId = None
        self.StartTime = None
        self.RetCode = None
        self.InvokeFinished = None
        self.Duration = None
        self.BillDuration = None
        self.MemUsage = None
        self.Log = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")
        self.StartTime = params.get("StartTime")
        self.RetCode = params.get("RetCode")
        self.InvokeFinished = params.get("InvokeFinished")
        self.Duration = params.get("Duration")
        self.BillDuration = params.get("BillDuration")
        self.MemUsage = params.get("MemUsage")
        self.Log = params.get("Log")


class GetFunctionLogsRequest(AbstractModel):
    """GetFunctionLogs请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param Offset: 数据的偏移量，Offset+Limit不能大于10000
        :type Offset: int
        :param Limit: 返回数据的长度，Offset+Limit不能大于10000
        :type Limit: int
        :param Order: 以升序还是降序的方式对日志进行排序，可选值 desc和 acs
        :type Order: str
        :param OrderBy: 根据某个字段排序日志,支持以下字段：startTime、functionName、requestId、duration和 memUsage
        :type OrderBy: str
        :param Filter: 日志过滤条件。可用来区分正确和错误日志，filter.retCode=not0 表示只返回错误日志，filter.retCode=is0 表示只返回正确日志，不传，则返回所有日志
        :type Filter: :class:`tencentcloud.scf.v20180416.models.Filter`
        :param Qualifier: 函数的版本
        :type Qualifier: str
        :param FunctionRequestId: 执行该函数对应的requestId
        :type FunctionRequestId: str
        :param StartTime: 查询的具体日期，例如：2017-05-16 20:00:00，只能与endtime相差一天之内
        :type StartTime: str
        :param EndTime: 查询的具体日期，例如：2017-05-16 20:59:59，只能与startTime相差一天之内
        :type EndTime: str
        """
        self.FunctionName = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None
        self.Filter = None
        self.Qualifier = None
        self.FunctionRequestId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self.Filter = Filter()
            self.Filter._deserialize(params.get("Filter"))
        self.Qualifier = params.get("Qualifier")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GetFunctionLogsResponse(AbstractModel):
    """GetFunctionLogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 函数日志的总数
        :type TotalCount: int
        :param Data: 函数日志信息
        :type Data: list of FunctionLog
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = FunctionLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class GetFunctionRequest(AbstractModel):
    """GetFunction请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 需要获取详情的函数名称
        :type FunctionName: str
        :param Qualifier: 函数的版本号
        :type Qualifier: str
        :param ShowCode: 是否显示代码, TRUE表示显示代码，FALSE表示不显示代码,大于1M的入口文件不会显示
        :type ShowCode: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.ShowCode = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.ShowCode = params.get("ShowCode")


class GetFunctionResponse(AbstractModel):
    """GetFunction返回参数结构体

    """

    def __init__(self):
        """
        :param ModTime: 函数的最后修改时间
        :type ModTime: str
        :param CodeInfo: 函数的代码
        :type CodeInfo: str
        :param Description: 函数的描述信息
        :type Description: str
        :param Triggers: 函数的触发器列表
        :type Triggers: list of Trigger
        :param Handler: 函数的入口
        :type Handler: str
        :param CodeSize: 函数代码大小
        :type CodeSize: int
        :param Timeout: 函数的超时时间
        :type Timeout: int
        :param FunctionVersion: 函数的版本
        :type FunctionVersion: str
        :param MemorySize: 函数的最大可用内存
        :type MemorySize: int
        :param Runtime: 函数的运行环境
        :type Runtime: str
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param VpcConfig: 函数的私有网络
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param UseGpu: 是否使用GPU
        :type UseGpu: str
        :param Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param CodeResult: 代码是否正确
        :type CodeResult: str
        :param CodeError: 代码错误信息
        :type CodeError: str
        :param ErrNo: 代码错误码
        :type ErrNo: int
        :param Namespace: 函数的命名空间
        :type Namespace: str
        :param Role: 函数绑定的角色
        :type Role: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ModTime = None
        self.CodeInfo = None
        self.Description = None
        self.Triggers = None
        self.Handler = None
        self.CodeSize = None
        self.Timeout = None
        self.FunctionVersion = None
        self.MemorySize = None
        self.Runtime = None
        self.FunctionName = None
        self.VpcConfig = None
        self.UseGpu = None
        self.Environment = None
        self.CodeResult = None
        self.CodeError = None
        self.ErrNo = None
        self.Namespace = None
        self.Role = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.CodeInfo = params.get("CodeInfo")
        self.Description = params.get("Description")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = Trigger()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.Handler = params.get("Handler")
        self.CodeSize = params.get("CodeSize")
        self.Timeout = params.get("Timeout")
        self.FunctionVersion = params.get("FunctionVersion")
        self.MemorySize = params.get("MemorySize")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.UseGpu = params.get("UseGpu")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.CodeResult = params.get("CodeResult")
        self.CodeError = params.get("CodeError")
        self.ErrNo = params.get("ErrNo")
        self.Namespace = params.get("Namespace")
        self.Role = params.get("Role")
        self.RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param InvocationType: RequestResponse(同步) 和 Event(异步)，默认为同步
        :type InvocationType: str
        :param Qualifier: 触发函数的版本号
        :type Qualifier: str
        :param ClientContext: 运行函数时的参数，以json格式传入，最大支持的参数长度是 1M
        :type ClientContext: str
        :param LogType: 同步调用时指定该字段，返回值会包含4K的日志，可选值为None和Tail，默认值为None。当该值为Tail时，返回参数中的logMsg字段会包含对应的函数执行日志
        :type LogType: str
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.InvocationType = None
        self.Qualifier = None
        self.ClientContext = None
        self.LogType = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.InvocationType = params.get("InvocationType")
        self.Qualifier = params.get("Qualifier")
        self.ClientContext = params.get("ClientContext")
        self.LogType = params.get("LogType")
        self.Namespace = params.get("Namespace")


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


class ListFunctionsRequest(AbstractModel):
    """ListFunctions请求参数结构体

    """

    def __init__(self):
        """
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param Orderby: 根据哪个字段进行返回结果排序,支持以下字段：AddTime, ModTime, FunctionName
        :type Orderby: str
        :param Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param SearchKey: 支持FunctionName模糊匹配
        :type SearchKey: str
        """
        self.Order = None
        self.Orderby = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.Order = params.get("Order")
        self.Orderby = params.get("Orderby")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")


class ListFunctionsResponse(AbstractModel):
    """ListFunctions返回参数结构体

    """

    def __init__(self):
        """
        :param Functions: 函数列表
        :type Functions: list of Function
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Functions = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self.Functions = []
            for item in params.get("Functions"):
                obj = Function()
                obj._deserialize(item)
                self.Functions.append(obj)
        self.TotalCount = params.get("TotalCount")
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


class Trigger(AbstractModel):
    """触发器类型

    """

    def __init__(self):
        """
        :param ModTime: 触发器最后修改时间
        :type ModTime: str
        :param Type: 触发器类型
        :type Type: str
        :param TriggerDesc: 触发器详细配置
        :type TriggerDesc: str
        :param TriggerName: 触发器名称
        :type TriggerName: str
        :param AddTime: 触发器创建时间
        :type AddTime: str
        """
        self.ModTime = None
        self.Type = None
        self.TriggerDesc = None
        self.TriggerName = None
        self.AddTime = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.TriggerName = params.get("TriggerName")
        self.AddTime = params.get("AddTime")


class UpdateFunctionCodeRequest(AbstractModel):
    """UpdateFunctionCode请求参数结构体

    """

    def __init__(self):
        """
        :param Handler: 函数处理方法名称。名称格式支持“文件名称.函数名称”形式，文件名称和函数名称之间以"."隔开，文件名称和函数名称要求以字母开始和结尾，中间允许插入字母、数字、下划线和连接符，文件名称和函数名字的长度要求 2-60 个字符
        :type Handler: str
        :param FunctionName: 要修改的函数名称
        :type FunctionName: str
        :param CosBucketName: 对象存储桶名称
        :type CosBucketName: str
        :param CosObjectName: 对象存储对象路径
        :type CosObjectName: str
        :param ZipFile: 包含函数代码文件及其依赖项的 zip 格式文件，使用该接口时要求将 zip 文件的内容转成 base64 编码，最大支持20M
        :type ZipFile: str
        :param CosBucketRegion: 对象存储的地域，地域为北京时需要传入ap-beijing,北京一区时需要传递ap-beijing-1，其他的地域不需要传递。
        :type CosBucketRegion: str
        """
        self.Handler = None
        self.FunctionName = None
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.CosBucketRegion = None


    def _deserialize(self, params):
        self.Handler = params.get("Handler")
        self.FunctionName = params.get("FunctionName")
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.CosBucketRegion = params.get("CosBucketRegion")


class UpdateFunctionCodeResponse(AbstractModel):
    """UpdateFunctionCode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionConfigurationRequest(AbstractModel):
    """UpdateFunctionConfiguration请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 要修改的函数名称
        :type FunctionName: str
        :param Description: 函数描述。最大支持 1000 个英文字母、数字、空格、逗号和英文句号，支持中文
        :type Description: str
        :param MemorySize: 函数运行时内存大小，默认为 128 M，可选范 128 M-1536 M
        :type MemorySize: int
        :param Timeout: 函数最长执行时间，单位为秒，可选值范 1-300 秒，默认为 3 秒
        :type Timeout: int
        :param Runtime: 函数运行环境，目前仅支持 Python2.7，Python3.6，Nodejs6.10，PHP5， PHP7，Golang1 和 Java8
        :type Runtime: str
        :param Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param VpcConfig: 函数的私有网络配置
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        """
        self.FunctionName = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Runtime = None
        self.Environment = None
        self.VpcConfig = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        self.Runtime = params.get("Runtime")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))


class UpdateFunctionConfigurationResponse(AbstractModel):
    """UpdateFunctionConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Variable(AbstractModel):
    """变量参数

    """

    def __init__(self):
        """
        :param Key: 变量的名称
        :type Key: str
        :param Value: 变量的值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class VpcConfig(AbstractModel):
    """私有网络参数配置

    """

    def __init__(self):
        """
        :param VpcId: 私有网络 的 id
        :type VpcId: str
        :param SubnetId: 子网的 id
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")