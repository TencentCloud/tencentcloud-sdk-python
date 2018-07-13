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


class CreateJobRequest(AbstractModel):
    """CreateJob请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务名称
        :type Name: str
        :param Cluster: 运行任务的集群
        :type Cluster: str
        :param RuntimeVersion: 运行任务的环境
        :type RuntimeVersion: str
        :param PackageDir: 挂载的路径，支持nfs,cos(cos只在tia运行环境中支持)
        :type PackageDir: list of str
        :param Command: 任务启动命令
        :type Command: list of str
        :param Args: 任务启动参数
        :type Args: list of str
        :param ScaleTier: 运行任务的配置信息
        :type ScaleTier: str
        :param MasterType: （ScaleTier为Custom时）master机器类型
        :type MasterType: str
        :param WorkerType: （ScaleTier为Custom时）worker机器类型
        :type WorkerType: str
        :param ParameterServerType: （ScaleTier为Custom时）parameter server机器类型
        :type ParameterServerType: str
        :param WorkerCount: （ScaleTier为Custom时）worker机器数量
        :type WorkerCount: int
        :param ParameterServerCount: （ScaleTier为Custom时）parameter server机器数量
        :type ParameterServerCount: int
        :param Debug: 启动debug mode，默认为false
        :type Debug: bool
        """
        self.Name = None
        self.Cluster = None
        self.RuntimeVersion = None
        self.PackageDir = None
        self.Command = None
        self.Args = None
        self.ScaleTier = None
        self.MasterType = None
        self.WorkerType = None
        self.ParameterServerType = None
        self.WorkerCount = None
        self.ParameterServerCount = None
        self.Debug = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.PackageDir = params.get("PackageDir")
        self.Command = params.get("Command")
        self.Args = params.get("Args")
        self.ScaleTier = params.get("ScaleTier")
        self.MasterType = params.get("MasterType")
        self.WorkerType = params.get("WorkerType")
        self.ParameterServerType = params.get("ParameterServerType")
        self.WorkerCount = params.get("WorkerCount")
        self.ParameterServerCount = params.get("ParameterServerCount")
        self.Debug = params.get("Debug")


class CreateJobResponse(AbstractModel):
    """CreateJob返回参数结构体

    """

    def __init__(self):
        """
        :param Job: 训练任务信息
        :type Job: :class:`tencentcloud.tia.v20180226.models.Job`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Job = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.RequestId = params.get("RequestId")


class CreateModelRequest(AbstractModel):
    """CreateModel请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 模型名称
        :type Name: str
        :param Cluster: 指定集群的名称
        :type Cluster: str
        :param Model: 要部署模型的路径名
        :type Model: str
        :param Description: 关于模型的描述
        :type Description: str
        :param RuntimeVersion: 运行环境镜像的标签
        :type RuntimeVersion: str
        :param Replicas: 要部署的模型副本数目
        :type Replicas: int
        :param Expose: 暴露外网或内网，默认暴露外网
        :type Expose: str
        :param ServType: 要部署模型的机器配置
        :type ServType: str
        """
        self.Name = None
        self.Cluster = None
        self.Model = None
        self.Description = None
        self.RuntimeVersion = None
        self.Replicas = None
        self.Expose = None
        self.ServType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")
        self.Model = params.get("Model")
        self.Description = params.get("Description")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.Replicas = params.get("Replicas")
        self.Expose = params.get("Expose")
        self.ServType = params.get("ServType")


class CreateModelResponse(AbstractModel):
    """CreateModel返回参数结构体

    """

    def __init__(self):
        """
        :param Model: 模型的详细信息
        :type Model: :class:`tencentcloud.tia.v20180226.models.Model`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = Model()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务名称
        :type Name: str
        :param Cluster: 运行任务的集群
        :type Cluster: str
        """
        self.Name = None
        self.Cluster = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")


class DeleteJobResponse(AbstractModel):
    """DeleteJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteModelRequest(AbstractModel):
    """DeleteModel请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 要删除的模型名称
        :type Name: str
        :param Cluster: 要删除的模型所在的集群名称
        :type Cluster: str
        """
        self.Name = None
        self.Cluster = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")


class DeleteModelResponse(AbstractModel):
    """DeleteModel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeJobRequest(AbstractModel):
    """DescribeJob请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务名称
        :type Name: str
        :param Cluster: 运行任务的集群
        :type Cluster: str
        """
        self.Name = None
        self.Cluster = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")


class DescribeJobResponse(AbstractModel):
    """DescribeJob返回参数结构体

    """

    def __init__(self):
        """
        :param Job: 训练任务信息
        :type Job: :class:`tencentcloud.tia.v20180226.models.Job`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Job = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.RequestId = params.get("RequestId")


class DescribeModelRequest(AbstractModel):
    """DescribeModel请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 模型名称
        :type Name: str
        :param Cluster: 模型所在集群名称
        :type Cluster: str
        """
        self.Name = None
        self.Cluster = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")


class DescribeModelResponse(AbstractModel):
    """DescribeModel返回参数结构体

    """

    def __init__(self):
        """
        :param Model: 模型信息
        :type Model: :class:`tencentcloud.tia.v20180226.models.Model`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = Model()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class InstallAgentRequest(AbstractModel):
    """InstallAgent请求参数结构体

    """

    def __init__(self):
        """
        :param Cluster: 集群名称
        :type Cluster: str
        :param TiaVersion: Agent版本, 用于私有集群的agent安装，默认为“private-training”
        :type TiaVersion: str
        :param Update: 是否允许更新Agent
        :type Update: bool
        """
        self.Cluster = None
        self.TiaVersion = None
        self.Update = None


    def _deserialize(self, params):
        self.Cluster = params.get("Cluster")
        self.TiaVersion = params.get("TiaVersion")
        self.Update = params.get("Update")


class InstallAgentResponse(AbstractModel):
    """InstallAgent返回参数结构体

    """

    def __init__(self):
        """
        :param TiaVersion: Agent版本, 用于私有集群的agent安装
        :type TiaVersion: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TiaVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TiaVersion = params.get("TiaVersion")
        self.RequestId = params.get("RequestId")


class Job(AbstractModel):
    """训练任务信息

    """

    def __init__(self):
        """
        :param Name: 任务名称
        :type Name: str
        :param CreateTime: 任务创建时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type CreateTime: str
        :param StartTime: 任务开始时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type StartTime: str
        :param EndTime: 任务结束时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type EndTime: str
        :param State: 任务状态，可能的状态为Created（已创建），Running（运行中），Succeeded（运行完成：成功），Failed（运行完成：失败）
        :type State: str
        :param Message: 任务状态信息
        :type Message: str
        :param ScaleTier: 运行任务的配置信息
        :type ScaleTier: str
        :param MasterType: （ScaleTier为Custom时）master机器类型
        :type MasterType: str
        :param WorkerType: （ScaleTier为Custom时）worker机器类型
        :type WorkerType: str
        :param ParameterServerType: （ScaleTier为Custom时）parameter server机器类型
        :type ParameterServerType: str
        :param WorkerCount: （ScaleTier为Custom时）worker机器数量
        :type WorkerCount: int
        :param ParameterServerCount: （ScaleTier为Custom时）parameter server机器数量
        :type ParameterServerCount: int
        :param PackageDir: 挂载的路径
        :type PackageDir: list of str
        :param Command: 任务启动命令
        :type Command: list of str
        :param Args: 任务启动参数
        :type Args: list of str
        :param Cluster: 运行任务的集群
        :type Cluster: str
        :param RuntimeVersion: 运行任务的环境
        :type RuntimeVersion: str
        :param DelTime: 任务删除时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type DelTime: str
        :param AppId: 创建任务的AppId
        :type AppId: int
        :param Uin: 创建任务的Uin
        :type Uin: str
        :param Debug: 创建任务的Debug模式
        :type Debug: bool
        """
        self.Name = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.State = None
        self.Message = None
        self.ScaleTier = None
        self.MasterType = None
        self.WorkerType = None
        self.ParameterServerType = None
        self.WorkerCount = None
        self.ParameterServerCount = None
        self.PackageDir = None
        self.Command = None
        self.Args = None
        self.Cluster = None
        self.RuntimeVersion = None
        self.DelTime = None
        self.AppId = None
        self.Uin = None
        self.Debug = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.State = params.get("State")
        self.Message = params.get("Message")
        self.ScaleTier = params.get("ScaleTier")
        self.MasterType = params.get("MasterType")
        self.WorkerType = params.get("WorkerType")
        self.ParameterServerType = params.get("ParameterServerType")
        self.WorkerCount = params.get("WorkerCount")
        self.ParameterServerCount = params.get("ParameterServerCount")
        self.PackageDir = params.get("PackageDir")
        self.Command = params.get("Command")
        self.Args = params.get("Args")
        self.Cluster = params.get("Cluster")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.DelTime = params.get("DelTime")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.Debug = params.get("Debug")


class ListJobsRequest(AbstractModel):
    """ListJobs请求参数结构体

    """

    def __init__(self):
        """
        :param Cluster: 运行任务的集群
        :type Cluster: str
        :param Limit: 分页参数，返回数量
        :type Limit: int
        :param Offset: 分页参数，起始位置
        :type Offset: int
        """
        self.Cluster = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Cluster = params.get("Cluster")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class ListJobsResponse(AbstractModel):
    """ListJobs返回参数结构体

    """

    def __init__(self):
        """
        :param Jobs: 训练任务列表
        :type Jobs: list of Job
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Jobs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self.Jobs = []
            for item in params.get("Jobs"):
                obj = Job()
                obj._deserialize(item)
                self.Jobs.append(obj)
        self.RequestId = params.get("RequestId")


class ListModelsRequest(AbstractModel):
    """ListModels请求参数结构体

    """

    def __init__(self):
        """
        :param Cluster: 部署模型的集群
        :type Cluster: str
        :param Limit: 分页参数，返回数量
        :type Limit: int
        :param Offset: 分页参数，起始位置
        :type Offset: int
        """
        self.Cluster = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Cluster = params.get("Cluster")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class ListModelsResponse(AbstractModel):
    """ListModels返回参数结构体

    """

    def __init__(self):
        """
        :param Models: Model数组，用以显示所有模型的信息
        :type Models: list of Model
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Models = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Models") is not None:
            self.Models = []
            for item in params.get("Models"):
                obj = Model()
                obj._deserialize(item)
                self.Models.append(obj)
        self.RequestId = params.get("RequestId")


class Log(AbstractModel):
    """日志

    """

    def __init__(self):
        """
        :param ContainerName: 容器名
        :type ContainerName: str
        :param Log: 日志内容
        :type Log: str
        :param Namespace: 空间名
        :type Namespace: str
        :param PodId: Pod Id
        :type PodId: str
        :param PodName: Pod名
        :type PodName: str
        :param Time: 日志日期，格式为“2018-07-02T09:10:04.916553368Z”
        :type Time: str
        """
        self.ContainerName = None
        self.Log = None
        self.Namespace = None
        self.PodId = None
        self.PodName = None
        self.Time = None


    def _deserialize(self, params):
        self.ContainerName = params.get("ContainerName")
        self.Log = params.get("Log")
        self.Namespace = params.get("Namespace")
        self.PodId = params.get("PodId")
        self.PodName = params.get("PodName")
        self.Time = params.get("Time")


class Model(AbstractModel):
    """用于描述模型的详细情况
            "Model": {
                "Name": "test-model",
                "Description": "test-model",
                "Cluster": "ap-beijing",
                "Model": "cos://test-1255502019.cos.ap-shanghai.myqcloud.com/example:/data/mnist",
                "RuntimeVersion": "tiaserv-1.6.0-cpu",
                "CreateTime": "2018-04-26 15:59:25 +0800 CST",
                "State": "Running",
                "ServingUrl": "140.143.51.230",
                "Message": "Deployment does not have minimum availability.",
                "AppId": 1255502019,
                "ServType": "1U2G0P"
            },

    """

    def __init__(self):
        """
        :param Name: 模型名称
        :type Name: str
        :param Description: 模型描述
        :type Description: str
        :param Cluster: 集群名称
        :type Cluster: str
        :param Model: 模型地址
        :type Model: str
        :param RuntimeVersion: 运行环境编号
        :type RuntimeVersion: str
        :param CreateTime: 模型创建时间
        :type CreateTime: str
        :param State: 模型运行状态
        :type State: str
        :param ServingUrl: 提供服务的url
        :type ServingUrl: str
        :param Message: 相关消息
        :type Message: str
        :param AppId: 编号
        :type AppId: int
        :param ServType: 机型
        :type ServType: str
        :param Expose: 模型暴露方式
        :type Expose: str
        :param Replicas: 部署副本数量
        :type Replicas: int
        """
        self.Name = None
        self.Description = None
        self.Cluster = None
        self.Model = None
        self.RuntimeVersion = None
        self.CreateTime = None
        self.State = None
        self.ServingUrl = None
        self.Message = None
        self.AppId = None
        self.ServType = None
        self.Expose = None
        self.Replicas = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Cluster = params.get("Cluster")
        self.Model = params.get("Model")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.CreateTime = params.get("CreateTime")
        self.State = params.get("State")
        self.ServingUrl = params.get("ServingUrl")
        self.Message = params.get("Message")
        self.AppId = params.get("AppId")
        self.ServType = params.get("ServType")
        self.Expose = params.get("Expose")
        self.Replicas = params.get("Replicas")


class QueryLogsRequest(AbstractModel):
    """QueryLogs请求参数结构体

    """

    def __init__(self):
        """
        :param JobName: 任务名称
        :type JobName: str
        :param Cluster: 集群名称
        :type Cluster: str
        :param StartTime: 查询日志的开始时间
        :type StartTime: str
        :param EndTime: 查询日志的结束时间
        :type EndTime: str
        :param Limit: 单次要返回的日志条数
        :type Limit: int
        :param Context: 加载更多使用，透传上次返回的context值，获取后续的日志内容
        :type Context: str
        """
        self.JobName = None
        self.Cluster = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        self.Cluster = params.get("Cluster")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")


class QueryLogsResponse(AbstractModel):
    """QueryLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Context: 日志查询上下文，用于加载更多日志
        :type Context: str
        :param Logs: 日志内容列表
        :type Logs: list of Log
        :param Listover: 是否已经返回所有符合条件的日志
        :type Listover: bool
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Logs = None
        self.Listover = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        if params.get("Logs") is not None:
            self.Logs = []
            for item in params.get("Logs"):
                obj = Log()
                obj._deserialize(item)
                self.Logs.append(obj)
        self.Listover = params.get("Listover")
        self.RequestId = params.get("RequestId")