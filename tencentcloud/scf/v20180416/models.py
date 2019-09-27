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


class AccessInfo(AbstractModel):
    """HTTP域名相关信息

    """

    def __init__(self):
        """
        :param Host: 域名
        :type Host: str
        :param Vip: VIP
        :type Vip: str
        """
        self.Host = None
        self.Vip = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Vip = params.get("Vip")


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
        :param DemoId: 如果是通过Demo创建的话，需要传入DemoId
        :type DemoId: str
        :param TempCosObjectName: 如果是从TempCos创建的话，需要传入TempCosObjectName
        :type TempCosObjectName: str
        :param GitUrl: Git地址
        :type GitUrl: str
        :param GitUserName: Git用户名
        :type GitUserName: str
        :param GitPassword: Git密码
        :type GitPassword: str
        :param GitPasswordSecret: 加密后的Git密码，一般无需指定
        :type GitPasswordSecret: str
        :param GitBranch: Git分支
        :type GitBranch: str
        :param GitDirectory: 代码在Git仓库中的路径
        :type GitDirectory: str
        :param GitCommitId: 指定要拉取的版本
        :type GitCommitId: str
        :param GitUserNameSecret: 加密后的Git用户名，一般无需指定
        :type GitUserNameSecret: str
        """
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.CosBucketRegion = None
        self.DemoId = None
        self.TempCosObjectName = None
        self.GitUrl = None
        self.GitUserName = None
        self.GitPassword = None
        self.GitPasswordSecret = None
        self.GitBranch = None
        self.GitDirectory = None
        self.GitCommitId = None
        self.GitUserNameSecret = None


    def _deserialize(self, params):
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.CosBucketRegion = params.get("CosBucketRegion")
        self.DemoId = params.get("DemoId")
        self.TempCosObjectName = params.get("TempCosObjectName")
        self.GitUrl = params.get("GitUrl")
        self.GitUserName = params.get("GitUserName")
        self.GitPassword = params.get("GitPassword")
        self.GitPasswordSecret = params.get("GitPasswordSecret")
        self.GitBranch = params.get("GitBranch")
        self.GitDirectory = params.get("GitDirectory")
        self.GitCommitId = params.get("GitCommitId")
        self.GitUserNameSecret = params.get("GitUserNameSecret")


class CopyFunctionRequest(AbstractModel):
    """CopyFunction请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 要复制的函数的名称
        :type FunctionName: str
        :param NewFunctionName: 新函数的名称
        :type NewFunctionName: str
        :param Namespace: 要复制的函数所在的命名空间，默认为default
        :type Namespace: str
        :param TargetNamespace: 将函数复制到的命名空间，默认为default
        :type TargetNamespace: str
        :param Description: 新函数的描述
        :type Description: str
        :param TargetRegion: 要将函数复制到的地域，不填则默认为当前地域
        :type TargetRegion: str
        :param Override: 如果目标Namespace下已有同名函数，是否覆盖，默认为否
（注意：如果选择覆盖，会导致同名函数被删除，请慎重操作）
TRUE：覆盖同名函数
FALSE：不覆盖同名函数
        :type Override: bool
        :param CopyConfiguration: 是否复制函数的属性，包括环境变量、内存、超时、函数描述、标签、VPC等，默认为是。
TRUE：复制函数配置
FALSE：不复制函数配置
        :type CopyConfiguration: bool
        """
        self.FunctionName = None
        self.NewFunctionName = None
        self.Namespace = None
        self.TargetNamespace = None
        self.Description = None
        self.TargetRegion = None
        self.Override = None
        self.CopyConfiguration = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.NewFunctionName = params.get("NewFunctionName")
        self.Namespace = params.get("Namespace")
        self.TargetNamespace = params.get("TargetNamespace")
        self.Description = params.get("Description")
        self.TargetRegion = params.get("TargetRegion")
        self.Override = params.get("Override")
        self.CopyConfiguration = params.get("CopyConfiguration")


class CopyFunctionResponse(AbstractModel):
    """CopyFunction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param Role: 函数绑定的角色
        :type Role: str
        :param ClsLogsetId: 函数日志投递到的CLS LogsetID
        :type ClsLogsetId: str
        :param ClsTopicId: 函数日志投递到的CLS TopicID
        :type ClsTopicId: str
        :param Type: 函数类型，默认值为Event，创建触发器函数请填写Event，创建HTTP函数级服务请填写HTTP
        :type Type: str
        :param CodeSource: CodeSource 代码来源，支持以下'ZipFile', 'Cos', 'Demo', 'TempCos', 'Git'之一，使用Git来源必须指定此字段
        :type CodeSource: str
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
        self.Namespace = None
        self.Role = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.Type = None
        self.CodeSource = None


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
        self.Namespace = params.get("Namespace")
        self.Role = params.get("Role")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.Type = params.get("Type")
        self.CodeSource = params.get("CodeSource")


class CreateFunctionResponse(AbstractModel):
    """CreateFunction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param Description: 命名空间描述
        :type Description: str
        """
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param TriggerName: 新建触发器名称。如果是定时触发器，名称支持英文字母、数字、连接符和下划线，最长100个字符；如果是cos触发器，需要是对应cos存储桶适用于XML API的访问域名(例如:5401-5ff414-12345.cos.ap-shanghai.myqcloud.com);如果是其他触发器，见具体触发器绑定参数的说明
        :type TriggerName: str
        :param Type: 触发器类型，目前支持 cos 、cmq、 timer、 ckafka类型
        :type Type: str
        :param TriggerDesc: 触发器对应的参数，如果是 timer 类型的触发器其内容是 Linux cron 表达式。如果是cos类型的触发器，其内容是json字符串 {"event":"cos:ObjectCreated:*","filter":{"Prefix":"","Suffix":""}},其中event是触发的cos事件，fitler中Prefix是对应的文件前缀过滤条件，Suffix是后缀过滤条件，如果不需要filter条件可不传。如果是其他触发器，见具体触发器说明
        :type TriggerDesc: str
        :param Namespace: 函数的命名空间
        :type Namespace: str
        :param Qualifier: 函数的版本
        :type Qualifier: str
        :param Enable: 触发器的初始是能状态 OPEN表示开启 CLOSE表示关闭
        :type Enable: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.Namespace = None
        self.Qualifier = None
        self.Enable = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.Enable = params.get("Enable")


class CreateTriggerResponse(AbstractModel):
    """CreateTrigger返回参数结构体

    """

    def __init__(self):
        """
        :param TriggerInfo: 触发器信息
        :type TriggerInfo: :class:`tencentcloud.scf.v20180416.models.Trigger`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TriggerInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TriggerInfo") is not None:
            self.TriggerInfo = Trigger()
            self.TriggerInfo._deserialize(params.get("TriggerInfo"))
        self.RequestId = params.get("RequestId")


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 要删除的函数名称
        :type FunctionName: str
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间名称
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param TriggerDesc: 如果删除的触发器类型为 COS 触发器，该字段为必填值，存放 JSON 格式的数据 {"event":"cos:ObjectCreated:*"}，数据内容和 SetTrigger 接口中该字段的格式相同；如果删除的触发器类型为定时触发器或 CMQ 触发器，可以不指定该字段
        :type TriggerDesc: str
        :param Qualifier: 函数的版本信息
        :type Qualifier: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.Namespace = None
        self.TriggerDesc = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.Namespace = params.get("Namespace")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Qualifier = params.get("Qualifier")


class DeleteTriggerResponse(AbstractModel):
    """DeleteTrigger返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EipOutConfig(AbstractModel):
    """EipOutConfig

    """

    def __init__(self):
        """
        :param EipFixed: 是否是固定IP，["TRUE","FALSE"]
        :type EipFixed: str
        :param Eips: IP列表
        :type Eips: list of str
        """
        self.EipFixed = None
        self.Eips = None


    def _deserialize(self, params):
        self.EipFixed = params.get("EipFixed")
        self.Eips = params.get("Eips")


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
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


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
        :param Status: 函数状态
        :type Status: str
        :param StatusDesc: 函数状态详情
        :type StatusDesc: str
        :param Description: 函数描述
        :type Description: str
        :param Tags: 函数标签
        :type Tags: list of Tag
        :param Type: 函数类型，取值为 HTTP 或者 Event
        :type Type: str
        """
        self.ModTime = None
        self.AddTime = None
        self.Runtime = None
        self.FunctionName = None
        self.FunctionId = None
        self.Namespace = None
        self.Status = None
        self.StatusDesc = None
        self.Description = None
        self.Tags = None
        self.Type = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.AddTime = params.get("AddTime")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        self.FunctionId = params.get("FunctionId")
        self.Namespace = params.get("Namespace")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Type = params.get("Type")


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
        :param Level: 日志等级
        :type Level: str
        :param Source: 日志来源
        :type Source: str
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
        self.Level = None
        self.Source = None


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
        self.Level = params.get("Level")
        self.Source = params.get("Source")


class FunctionVersion(AbstractModel):
    """函数版本信息

    """

    def __init__(self):
        """
        :param Version: 函数版本名称
        :type Version: str
        :param Description: 版本描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.Version = None
        self.Description = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Description = params.get("Description")


class GetFunctionAddressRequest(AbstractModel):
    """GetFunctionAddress请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param Qualifier: 函数的版本
        :type Qualifier: str
        :param Namespace: 函数的命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")


class GetFunctionAddressResponse(AbstractModel):
    """GetFunctionAddress返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 函数的Cos地址
        :type Url: str
        :param CodeSha256: 函数的SHA256编码
        :type CodeSha256: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.CodeSha256 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.CodeSha256 = params.get("CodeSha256")
        self.RequestId = params.get("RequestId")


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
        :param Order: 以升序还是降序的方式对日志进行排序，可选值 desc和 asc
        :type Order: str
        :param OrderBy: 根据某个字段排序日志,支持以下字段：function_name, duration, mem_usage, start_time
        :type OrderBy: str
        :param Filter: 日志过滤条件。可用来区分正确和错误日志，filter.retCode=not0 表示只返回错误日志，filter.retCode=is0 表示只返回正确日志，不传，则返回所有日志
        :type Filter: :class:`tencentcloud.scf.v20180416.models.LogFilter`
        :param Namespace: 函数的命名空间
        :type Namespace: str
        :param Qualifier: 函数的版本
        :type Qualifier: str
        :param FunctionRequestId: 执行该函数对应的requestId
        :type FunctionRequestId: str
        :param StartTime: 查询的具体日期，例如：2017-05-16 20:00:00，只能与endtime相差一天之内
        :type StartTime: str
        :param EndTime: 查询的具体日期，例如：2017-05-16 20:59:59，只能与startTime相差一天之内
        :type EndTime: str
        :param SearchContext: 服务日志相关参数，第一页日志 Offset 为空字符串，后续分页按响应字段里的SearchContext填写
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        """
        self.FunctionName = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None
        self.Filter = None
        self.Namespace = None
        self.Qualifier = None
        self.FunctionRequestId = None
        self.StartTime = None
        self.EndTime = None
        self.SearchContext = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self.Filter = LogFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("SearchContext") is not None:
            self.SearchContext = LogSearchContext()
            self.SearchContext._deserialize(params.get("SearchContext"))


class GetFunctionLogsResponse(AbstractModel):
    """GetFunctionLogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 函数日志的总数
        :type TotalCount: int
        :param Data: 函数日志信息
        :type Data: list of FunctionLog
        :param SearchContext: 日志服务分页参数
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.SearchContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = FunctionLog()
                obj._deserialize(item)
                self.Data.append(obj)
        if params.get("SearchContext") is not None:
            self.SearchContext = LogSearchContext()
            self.SearchContext._deserialize(params.get("SearchContext"))
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
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param ShowCode: 是否显示代码, TRUE表示显示代码，FALSE表示不显示代码,大于1M的入口文件不会显示
        :type ShowCode: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None
        self.ShowCode = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")
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
        :param InstallDependency: 是否自动安装依赖
        :type InstallDependency: str
        :param Status: 函数状态
        :type Status: str
        :param StatusDesc: 状态描述
        :type StatusDesc: str
        :param ClsLogsetId: 日志投递到的Cls日志集
        :type ClsLogsetId: str
        :param ClsTopicId: 日志投递到的Cls Topic
        :type ClsTopicId: str
        :param FunctionId: 函数ID
        :type FunctionId: str
        :param Tags: 函数的标签列表
        :type Tags: list of Tag
        :param EipConfig: EipConfig配置
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipOutConfig`
        :param AccessInfo: 域名信息
        :type AccessInfo: :class:`tencentcloud.scf.v20180416.models.AccessInfo`
        :param Type: 函数类型，取值为HTTP或者Event
        :type Type: str
        :param L5Enable: 是否启用L5
        :type L5Enable: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        self.InstallDependency = None
        self.Status = None
        self.StatusDesc = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.FunctionId = None
        self.Tags = None
        self.EipConfig = None
        self.AccessInfo = None
        self.Type = None
        self.L5Enable = None
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
        self.InstallDependency = params.get("InstallDependency")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.FunctionId = params.get("FunctionId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("EipConfig") is not None:
            self.EipConfig = EipOutConfig()
            self.EipConfig._deserialize(params.get("EipConfig"))
        if params.get("AccessInfo") is not None:
            self.AccessInfo = AccessInfo()
            self.AccessInfo._deserialize(params.get("AccessInfo"))
        self.Type = params.get("Type")
        self.L5Enable = params.get("L5Enable")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 函数描述，支持模糊搜索
        :type Description: str
        :param Filters: 过滤条件。
- tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        """
        self.Order = None
        self.Orderby = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.Namespace = None
        self.Description = None
        self.Filters = None


    def _deserialize(self, params):
        self.Order = params.get("Order")
        self.Orderby = params.get("Orderby")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class ListFunctionsResponse(AbstractModel):
    """ListFunctions返回参数结构体

    """

    def __init__(self):
        """
        :param Functions: 函数列表
        :type Functions: list of Function
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ListNamespacesRequest(AbstractModel):
    """ListNamespaces请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param Offset: 数据的偏移量，默认值为 0
        :type Offset: int
        :param Orderby: 根据哪个字段进行返回结果排序,支持以下字段：Name,Updatetime
        :type Orderby: str
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Orderby = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Orderby = params.get("Orderby")
        self.Order = params.get("Order")


class ListNamespacesResponse(AbstractModel):
    """ListNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param Namespaces: namespace详情
        :type Namespaces: list of Namespace
        :param TotalCount: 返回的namespace数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Namespaces = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Namespaces") is not None:
            self.Namespaces = []
            for item in params.get("Namespaces"):
                obj = Namespace()
                obj._deserialize(item)
                self.Namespaces.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListVersionByFunctionRequest(AbstractModel):
    """ListVersionByFunction请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 函数ID
        :type FunctionName: str
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")


class ListVersionByFunctionResponse(AbstractModel):
    """ListVersionByFunction返回参数结构体

    """

    def __init__(self):
        """
        :param FunctionVersion: 函数版本。
        :type FunctionVersion: list of str
        :param Versions: 函数版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of FunctionVersion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionVersion = None
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = FunctionVersion()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class LogFilter(AbstractModel):
    """日志过滤条件，用于区分正确与错误日志

    """

    def __init__(self):
        """
        :param RetCode: filter.RetCode的取值有：
not0 表示只返回错误日志，
is0 表示只返回正确日志，
TimeLimitExceeded 返回函数调用发生超时的日志，
ResourceLimitExceeded 返回函数调用发生资源超限的日志，
UserCodeException 返回函数调用发生用户代码错误的日志，
无输入则返回所有日志。
        :type RetCode: str
        """
        self.RetCode = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")


class LogSearchContext(AbstractModel):
    """日志搜索上下文

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: str
        :param Limit: 日志条数
        :type Limit: int
        :param Keyword: 日志关键词
        :type Keyword: str
        :param Type: 日志类型，支持Application和Platform，默认为Application
        :type Type: str
        """
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Type = params.get("Type")


class Namespace(AbstractModel):
    """命名空间

    """

    def __init__(self):
        """
        :param ModTime: 命名空间创建时间
        :type ModTime: str
        :param AddTime: 命名空间修改时间
        :type AddTime: str
        :param Description: 命名空间描述
        :type Description: str
        :param Name: 命名空间名称
        :type Name: str
        :param Type: 默认default，TCB表示是小程序云开发创建的
        :type Type: str
        """
        self.ModTime = None
        self.AddTime = None
        self.Description = None
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.AddTime = params.get("AddTime")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Type = params.get("Type")


class PublishVersionRequest(AbstractModel):
    """PublishVersion请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 发布函数的名称
        :type FunctionName: str
        :param Description: 函数的描述
        :type Description: str
        :param Namespace: 函数的命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.Description = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.Namespace = params.get("Namespace")


class PublishVersionResponse(AbstractModel):
    """PublishVersion返回参数结构体

    """

    def __init__(self):
        """
        :param FunctionVersion: 函数的版本
        :type FunctionVersion: str
        :param CodeSize: 代码大小
        :type CodeSize: int
        :param MemorySize: 最大可用内存
        :type MemorySize: int
        :param Description: 函数的描述
        :type Description: str
        :param Handler: 函数的入口
        :type Handler: str
        :param Timeout: 函数的超时时间
        :type Timeout: int
        :param Runtime: 函数的运行环境
        :type Runtime: str
        :param Namespace: 函数的命名空间
        :type Namespace: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionVersion = None
        self.CodeSize = None
        self.MemorySize = None
        self.Description = None
        self.Handler = None
        self.Timeout = None
        self.Runtime = None
        self.Namespace = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        self.CodeSize = params.get("CodeSize")
        self.MemorySize = params.get("MemorySize")
        self.Description = params.get("Description")
        self.Handler = params.get("Handler")
        self.Timeout = params.get("Timeout")
        self.Runtime = params.get("Runtime")
        self.Namespace = params.get("Namespace")
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


class Tag(AbstractModel):
    """函数标签

    """

    def __init__(self):
        """
        :param Key: 标签的key
        :type Key: str
        :param Value: 标签的value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


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
        :param Enable: 使能开关
        :type Enable: int
        :param CustomArgument: 客户自定义参数
        :type CustomArgument: str
        """
        self.ModTime = None
        self.Type = None
        self.TriggerDesc = None
        self.TriggerName = None
        self.AddTime = None
        self.Enable = None
        self.CustomArgument = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.TriggerName = params.get("TriggerName")
        self.AddTime = params.get("AddTime")
        self.Enable = params.get("Enable")
        self.CustomArgument = params.get("CustomArgument")


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
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param CosBucketRegion: 对象存储的地域，注：北京分为ap-beijing和ap-beijing-1
        :type CosBucketRegion: str
        :param EnvId: 函数所属环境
        :type EnvId: str
        :param Publish: 在更新时是否同步发布新版本，默认为：FALSE，不发布
        :type Publish: str
        :param Code: 函数代码
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param CodeSource: 代码来源方式，支持以下'ZipFile', 'Cos', 'Inline', 'TempCos', 'Git' 之一，使用Git来源必须指定此字段
        :type CodeSource: str
        """
        self.Handler = None
        self.FunctionName = None
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.Namespace = None
        self.CosBucketRegion = None
        self.EnvId = None
        self.Publish = None
        self.Code = None
        self.CodeSource = None


    def _deserialize(self, params):
        self.Handler = params.get("Handler")
        self.FunctionName = params.get("FunctionName")
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.Namespace = params.get("Namespace")
        self.CosBucketRegion = params.get("CosBucketRegion")
        self.EnvId = params.get("EnvId")
        self.Publish = params.get("Publish")
        if params.get("Code") is not None:
            self.Code = Code()
            self.Code._deserialize(params.get("Code"))
        self.CodeSource = params.get("CodeSource")


class UpdateFunctionCodeResponse(AbstractModel):
    """UpdateFunctionCode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param VpcConfig: 函数的私有网络配置
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param Role: 函数绑定的角色
        :type Role: str
        :param ClsLogsetId: 日志投递到的cls日志集ID
        :type ClsLogsetId: str
        :param ClsTopicId: 日志投递到的cls Topic ID
        :type ClsTopicId: str
        :param Publish: 在更新时是否同步发布新版本，默认为：FALSE，不发布
        :type Publish: str
        :param L5Enable: 是否开启L5访问能力，TRUE 为开启，FALSE为关闭
        :type L5Enable: str
        """
        self.FunctionName = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Runtime = None
        self.Environment = None
        self.Namespace = None
        self.VpcConfig = None
        self.Role = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.Publish = None
        self.L5Enable = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        self.Runtime = params.get("Runtime")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.Namespace = params.get("Namespace")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.Role = params.get("Role")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.Publish = params.get("Publish")
        self.L5Enable = params.get("L5Enable")


class UpdateFunctionConfigurationResponse(AbstractModel):
    """UpdateFunctionConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateNamespaceRequest(AbstractModel):
    """UpdateNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param Description: 命名空间描述
        :type Description: str
        """
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")


class UpdateNamespaceResponse(AbstractModel):
    """UpdateNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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