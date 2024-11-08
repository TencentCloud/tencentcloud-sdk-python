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


class CreateJobRequest(AbstractModel):
    """CreateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _Cluster: 运行任务的集群，详见 [使用集群](https://cloud.tencent.com/document/product/851/17317)
        :type Cluster: str
        :param _RuntimeVersion: 运行任务的环境，详见 [运行环境](https://cloud.tencent.com/document/product/851/17320)
        :type RuntimeVersion: str
        :param _PackageDir: 挂载的路径，支持 NFS，[CFS](https://cloud.tencent.com/product/cfs) 和 [COS](https://cloud.tencent.com/product/cos)，其中 COS 只在 [TI-A 定制环境](https://cloud.tencent.com/document/product/851/17320#ti-a-.E5.AE.9A.E5.88.B6.E7.8E.AF.E5.A2.83) 中支持
        :type PackageDir: list of str
        :param _Command: 任务启动命令
        :type Command: list of str
        :param _Args: 任务启动参数
        :type Args: list of str
        :param _ScaleTier: 运行任务的配置信息，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :type ScaleTier: str
        :param _MasterType: Master 机器类型，ScaleTier 取值为 `CUSTOM` 时必填，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :type MasterType: str
        :param _WorkerType: Worker 机器类型，ScaleTier 取值为 `CUSTOM` 时必填，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :type WorkerType: str
        :param _ParameterServerType: Parameter server 机器类型，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :type ParameterServerType: str
        :param _WorkerCount: Worker 机器数量，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :type WorkerCount: int
        :param _ParameterServerCount: Parameter server 机器数量，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :type ParameterServerCount: int
        :param _Debug: 启动 debug 模式，默认为 false
        :type Debug: bool
        :param _RuntimeConf: 运行任务的其他配置信息
        :type RuntimeConf: list of str
        """
        self._Name = None
        self._Cluster = None
        self._RuntimeVersion = None
        self._PackageDir = None
        self._Command = None
        self._Args = None
        self._ScaleTier = None
        self._MasterType = None
        self._WorkerType = None
        self._ParameterServerType = None
        self._WorkerCount = None
        self._ParameterServerCount = None
        self._Debug = None
        self._RuntimeConf = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cluster(self):
        """运行任务的集群，详见 [使用集群](https://cloud.tencent.com/document/product/851/17317)
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def RuntimeVersion(self):
        """运行任务的环境，详见 [运行环境](https://cloud.tencent.com/document/product/851/17320)
        :rtype: str
        """
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def PackageDir(self):
        """挂载的路径，支持 NFS，[CFS](https://cloud.tencent.com/product/cfs) 和 [COS](https://cloud.tencent.com/product/cos)，其中 COS 只在 [TI-A 定制环境](https://cloud.tencent.com/document/product/851/17320#ti-a-.E5.AE.9A.E5.88.B6.E7.8E.AF.E5.A2.83) 中支持
        :rtype: list of str
        """
        return self._PackageDir

    @PackageDir.setter
    def PackageDir(self, PackageDir):
        self._PackageDir = PackageDir

    @property
    def Command(self):
        """任务启动命令
        :rtype: list of str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Args(self):
        """任务启动参数
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def ScaleTier(self):
        """运行任务的配置信息，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :rtype: str
        """
        return self._ScaleTier

    @ScaleTier.setter
    def ScaleTier(self, ScaleTier):
        self._ScaleTier = ScaleTier

    @property
    def MasterType(self):
        """Master 机器类型，ScaleTier 取值为 `CUSTOM` 时必填，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :rtype: str
        """
        return self._MasterType

    @MasterType.setter
    def MasterType(self, MasterType):
        self._MasterType = MasterType

    @property
    def WorkerType(self):
        """Worker 机器类型，ScaleTier 取值为 `CUSTOM` 时必填，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :rtype: str
        """
        return self._WorkerType

    @WorkerType.setter
    def WorkerType(self, WorkerType):
        self._WorkerType = WorkerType

    @property
    def ParameterServerType(self):
        """Parameter server 机器类型，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :rtype: str
        """
        return self._ParameterServerType

    @ParameterServerType.setter
    def ParameterServerType(self, ParameterServerType):
        self._ParameterServerType = ParameterServerType

    @property
    def WorkerCount(self):
        """Worker 机器数量，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :rtype: int
        """
        return self._WorkerCount

    @WorkerCount.setter
    def WorkerCount(self, WorkerCount):
        self._WorkerCount = WorkerCount

    @property
    def ParameterServerCount(self):
        """Parameter server 机器数量，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)
        :rtype: int
        """
        return self._ParameterServerCount

    @ParameterServerCount.setter
    def ParameterServerCount(self, ParameterServerCount):
        self._ParameterServerCount = ParameterServerCount

    @property
    def Debug(self):
        """启动 debug 模式，默认为 false
        :rtype: bool
        """
        return self._Debug

    @Debug.setter
    def Debug(self, Debug):
        self._Debug = Debug

    @property
    def RuntimeConf(self):
        """运行任务的其他配置信息
        :rtype: list of str
        """
        return self._RuntimeConf

    @RuntimeConf.setter
    def RuntimeConf(self, RuntimeConf):
        self._RuntimeConf = RuntimeConf


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Cluster = params.get("Cluster")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._PackageDir = params.get("PackageDir")
        self._Command = params.get("Command")
        self._Args = params.get("Args")
        self._ScaleTier = params.get("ScaleTier")
        self._MasterType = params.get("MasterType")
        self._WorkerType = params.get("WorkerType")
        self._ParameterServerType = params.get("ParameterServerType")
        self._WorkerCount = params.get("WorkerCount")
        self._ParameterServerCount = params.get("ParameterServerCount")
        self._Debug = params.get("Debug")
        self._RuntimeConf = params.get("RuntimeConf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJobResponse(AbstractModel):
    """CreateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Job: 训练任务信息
        :type Job: :class:`tencentcloud.tia.v20180226.models.Job`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        """训练任务信息
        :rtype: :class:`tencentcloud.tia.v20180226.models.Job`
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class CreateModelRequest(AbstractModel):
    """CreateModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 模型名称
        :type Name: str
        :param _Model: 要部署的模型文件路径名
        :type Model: str
        :param _Description: 关于模型的描述
        :type Description: str
        :param _Cluster: 部署目标集群的名称，`集群模式` 必填
        :type Cluster: str
        :param _RuntimeVersion: 运行环境镜像的标签，详见 [Serving 环境](https://cloud.tencent.com/document/product/851/17320#serving-.E7.8E.AF.E5.A2.83)
        :type RuntimeVersion: str
        :param _Replicas: 要部署的模型副本数目，`集群模式` 选填
        :type Replicas: int
        :param _Expose: 暴露外网或内网，默认暴露外网，`集群模式` 选填
        :type Expose: str
        :param _ServType: 部署模式，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式` 下服务的运行规模，形如 `2U4G1P`，详见 [自定义的训练规模](https://cloud.tencent.com/document/product/851/17319#.E8.87.AA.E5.AE.9A.E4.B9.89.E7.9A.84.E8.AE.AD.E7.BB.83.E8.A7.84.E6.A8.A1)
        :type ServType: str
        :param _RuntimeConf: `无服务器模式` 可选的其他配置信息，详见 [利用无服务器函数部署](https://cloud.tencent.com/document/product/851/17049#.E5.88.A9.E7.94.A8.E6.97.A0.E6.9C.8D.E5.8A.A1.E5.99.A8.E5.87.BD.E6.95.B0.E9.83.A8.E7.BD.B2)
        :type RuntimeConf: list of str
        """
        self._Name = None
        self._Model = None
        self._Description = None
        self._Cluster = None
        self._RuntimeVersion = None
        self._Replicas = None
        self._Expose = None
        self._ServType = None
        self._RuntimeConf = None

    @property
    def Name(self):
        """模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Model(self):
        """要部署的模型文件路径名
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Description(self):
        """关于模型的描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Cluster(self):
        """部署目标集群的名称，`集群模式` 必填
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def RuntimeVersion(self):
        """运行环境镜像的标签，详见 [Serving 环境](https://cloud.tencent.com/document/product/851/17320#serving-.E7.8E.AF.E5.A2.83)
        :rtype: str
        """
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def Replicas(self):
        """要部署的模型副本数目，`集群模式` 选填
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Expose(self):
        """暴露外网或内网，默认暴露外网，`集群模式` 选填
        :rtype: str
        """
        return self._Expose

    @Expose.setter
    def Expose(self, Expose):
        self._Expose = Expose

    @property
    def ServType(self):
        """部署模式，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式` 下服务的运行规模，形如 `2U4G1P`，详见 [自定义的训练规模](https://cloud.tencent.com/document/product/851/17319#.E8.87.AA.E5.AE.9A.E4.B9.89.E7.9A.84.E8.AE.AD.E7.BB.83.E8.A7.84.E6.A8.A1)
        :rtype: str
        """
        return self._ServType

    @ServType.setter
    def ServType(self, ServType):
        self._ServType = ServType

    @property
    def RuntimeConf(self):
        """`无服务器模式` 可选的其他配置信息，详见 [利用无服务器函数部署](https://cloud.tencent.com/document/product/851/17049#.E5.88.A9.E7.94.A8.E6.97.A0.E6.9C.8D.E5.8A.A1.E5.99.A8.E5.87.BD.E6.95.B0.E9.83.A8.E7.BD.B2)
        :rtype: list of str
        """
        return self._RuntimeConf

    @RuntimeConf.setter
    def RuntimeConf(self, RuntimeConf):
        self._RuntimeConf = RuntimeConf


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Model = params.get("Model")
        self._Description = params.get("Description")
        self._Cluster = params.get("Cluster")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._Replicas = params.get("Replicas")
        self._Expose = params.get("Expose")
        self._ServType = params.get("ServType")
        self._RuntimeConf = params.get("RuntimeConf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModelResponse(AbstractModel):
    """CreateModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型的详细信息
        :type Model: :class:`tencentcloud.tia.v20180226.models.Model`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Model = None
        self._RequestId = None

    @property
    def Model(self):
        """模型的详细信息
        :rtype: :class:`tencentcloud.tia.v20180226.models.Model`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = Model()
            self._Model._deserialize(params.get("Model"))
        self._RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _Cluster: 运行任务的集群
        :type Cluster: str
        """
        self._Name = None
        self._Cluster = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cluster(self):
        """运行任务的集群
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Cluster = params.get("Cluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobResponse(AbstractModel):
    """DeleteJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteModelRequest(AbstractModel):
    """DeleteModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 要删除的模型名称
        :type Name: str
        :param _Cluster: 要删除的模型所在的集群名称，`集群模式` 必填
        :type Cluster: str
        :param _ServType: 模型类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`
        :type ServType: str
        """
        self._Name = None
        self._Cluster = None
        self._ServType = None

    @property
    def Name(self):
        """要删除的模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cluster(self):
        """要删除的模型所在的集群名称，`集群模式` 必填
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def ServType(self):
        """模型类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`
        :rtype: str
        """
        return self._ServType

    @ServType.setter
    def ServType(self, ServType):
        self._ServType = ServType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Cluster = params.get("Cluster")
        self._ServType = params.get("ServType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelResponse(AbstractModel):
    """DeleteModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeJobRequest(AbstractModel):
    """DescribeJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _Cluster: 运行任务的集群
        :type Cluster: str
        """
        self._Name = None
        self._Cluster = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cluster(self):
        """运行任务的集群
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Cluster = params.get("Cluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobResponse(AbstractModel):
    """DescribeJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Job: 训练任务信息
        :type Job: :class:`tencentcloud.tia.v20180226.models.Job`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        """训练任务信息
        :rtype: :class:`tencentcloud.tia.v20180226.models.Job`
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class DescribeModelRequest(AbstractModel):
    """DescribeModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 模型名称
        :type Name: str
        :param _Cluster: 模型所在集群名称，`集群模式` 必填
        :type Cluster: str
        :param _ServType: 模型类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`
        :type ServType: str
        """
        self._Name = None
        self._Cluster = None
        self._ServType = None

    @property
    def Name(self):
        """模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cluster(self):
        """模型所在集群名称，`集群模式` 必填
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def ServType(self):
        """模型类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`
        :rtype: str
        """
        return self._ServType

    @ServType.setter
    def ServType(self, ServType):
        self._ServType = ServType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Cluster = params.get("Cluster")
        self._ServType = params.get("ServType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelResponse(AbstractModel):
    """DescribeModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型信息
        :type Model: :class:`tencentcloud.tia.v20180226.models.Model`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Model = None
        self._RequestId = None

    @property
    def Model(self):
        """模型信息
        :rtype: :class:`tencentcloud.tia.v20180226.models.Model`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = Model()
            self._Model._deserialize(params.get("Model"))
        self._RequestId = params.get("RequestId")


class InstallAgentRequest(AbstractModel):
    """InstallAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cluster: 集群名称
        :type Cluster: str
        :param _TiaVersion: Agent版本, 用于私有集群的agent安装，默认为“private-training”
        :type TiaVersion: str
        :param _Update: 是否允许更新Agent
        :type Update: bool
        """
        self._Cluster = None
        self._TiaVersion = None
        self._Update = None

    @property
    def Cluster(self):
        """集群名称
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def TiaVersion(self):
        """Agent版本, 用于私有集群的agent安装，默认为“private-training”
        :rtype: str
        """
        return self._TiaVersion

    @TiaVersion.setter
    def TiaVersion(self, TiaVersion):
        self._TiaVersion = TiaVersion

    @property
    def Update(self):
        """是否允许更新Agent
        :rtype: bool
        """
        return self._Update

    @Update.setter
    def Update(self, Update):
        self._Update = Update


    def _deserialize(self, params):
        self._Cluster = params.get("Cluster")
        self._TiaVersion = params.get("TiaVersion")
        self._Update = params.get("Update")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallAgentResponse(AbstractModel):
    """InstallAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TiaVersion: Agent版本, 用于私有集群的agent安装
        :type TiaVersion: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TiaVersion = None
        self._RequestId = None

    @property
    def TiaVersion(self):
        """Agent版本, 用于私有集群的agent安装
        :rtype: str
        """
        return self._TiaVersion

    @TiaVersion.setter
    def TiaVersion(self, TiaVersion):
        self._TiaVersion = TiaVersion

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TiaVersion = params.get("TiaVersion")
        self._RequestId = params.get("RequestId")


class Job(AbstractModel):
    """训练任务信息

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _CreateTime: 任务创建时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type CreateTime: str
        :param _StartTime: 任务开始时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type StartTime: str
        :param _EndTime: 任务结束时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type EndTime: str
        :param _State: 任务状态，可能的状态为Created（已创建），Running（运行中），Succeeded（运行完成：成功），Failed（运行完成：失败）
        :type State: str
        :param _Message: 任务状态信息
        :type Message: str
        :param _ScaleTier: 运行任务的配置信息
        :type ScaleTier: str
        :param _MasterType: （ScaleTier为Custom时）master机器类型
        :type MasterType: str
        :param _WorkerType: （ScaleTier为Custom时）worker机器类型
        :type WorkerType: str
        :param _ParameterServerType: （ScaleTier为Custom时）parameter server机器类型
        :type ParameterServerType: str
        :param _WorkerCount: （ScaleTier为Custom时）worker机器数量
        :type WorkerCount: int
        :param _ParameterServerCount: （ScaleTier为Custom时）parameter server机器数量
        :type ParameterServerCount: int
        :param _PackageDir: 挂载的路径
        :type PackageDir: list of str
        :param _Command: 任务启动命令
        :type Command: list of str
        :param _Args: 任务启动参数
        :type Args: list of str
        :param _Cluster: 运行任务的集群
        :type Cluster: str
        :param _RuntimeVersion: 运行任务的环境
        :type RuntimeVersion: str
        :param _DelTime: 任务删除时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type DelTime: str
        :param _AppId: 创建任务的AppId
        :type AppId: int
        :param _Uin: 创建任务的Uin
        :type Uin: str
        :param _Debug: 创建任务的Debug模式
        :type Debug: bool
        :param _RuntimeConf: Runtime的额外配置信息
        :type RuntimeConf: list of str
        :param _Id: 任务Id
        :type Id: str
        """
        self._Name = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._State = None
        self._Message = None
        self._ScaleTier = None
        self._MasterType = None
        self._WorkerType = None
        self._ParameterServerType = None
        self._WorkerCount = None
        self._ParameterServerCount = None
        self._PackageDir = None
        self._Command = None
        self._Args = None
        self._Cluster = None
        self._RuntimeVersion = None
        self._DelTime = None
        self._AppId = None
        self._Uin = None
        self._Debug = None
        self._RuntimeConf = None
        self._Id = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        """任务创建时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """任务开始时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def State(self):
        """任务状态，可能的状态为Created（已创建），Running（运行中），Succeeded（运行完成：成功），Failed（运行完成：失败）
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Message(self):
        """任务状态信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ScaleTier(self):
        """运行任务的配置信息
        :rtype: str
        """
        return self._ScaleTier

    @ScaleTier.setter
    def ScaleTier(self, ScaleTier):
        self._ScaleTier = ScaleTier

    @property
    def MasterType(self):
        """（ScaleTier为Custom时）master机器类型
        :rtype: str
        """
        return self._MasterType

    @MasterType.setter
    def MasterType(self, MasterType):
        self._MasterType = MasterType

    @property
    def WorkerType(self):
        """（ScaleTier为Custom时）worker机器类型
        :rtype: str
        """
        return self._WorkerType

    @WorkerType.setter
    def WorkerType(self, WorkerType):
        self._WorkerType = WorkerType

    @property
    def ParameterServerType(self):
        """（ScaleTier为Custom时）parameter server机器类型
        :rtype: str
        """
        return self._ParameterServerType

    @ParameterServerType.setter
    def ParameterServerType(self, ParameterServerType):
        self._ParameterServerType = ParameterServerType

    @property
    def WorkerCount(self):
        """（ScaleTier为Custom时）worker机器数量
        :rtype: int
        """
        return self._WorkerCount

    @WorkerCount.setter
    def WorkerCount(self, WorkerCount):
        self._WorkerCount = WorkerCount

    @property
    def ParameterServerCount(self):
        """（ScaleTier为Custom时）parameter server机器数量
        :rtype: int
        """
        return self._ParameterServerCount

    @ParameterServerCount.setter
    def ParameterServerCount(self, ParameterServerCount):
        self._ParameterServerCount = ParameterServerCount

    @property
    def PackageDir(self):
        """挂载的路径
        :rtype: list of str
        """
        return self._PackageDir

    @PackageDir.setter
    def PackageDir(self, PackageDir):
        self._PackageDir = PackageDir

    @property
    def Command(self):
        """任务启动命令
        :rtype: list of str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Args(self):
        """任务启动参数
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def Cluster(self):
        """运行任务的集群
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def RuntimeVersion(self):
        """运行任务的环境
        :rtype: str
        """
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def DelTime(self):
        """任务删除时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :rtype: str
        """
        return self._DelTime

    @DelTime.setter
    def DelTime(self, DelTime):
        self._DelTime = DelTime

    @property
    def AppId(self):
        """创建任务的AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """创建任务的Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Debug(self):
        """创建任务的Debug模式
        :rtype: bool
        """
        return self._Debug

    @Debug.setter
    def Debug(self, Debug):
        self._Debug = Debug

    @property
    def RuntimeConf(self):
        """Runtime的额外配置信息
        :rtype: list of str
        """
        return self._RuntimeConf

    @RuntimeConf.setter
    def RuntimeConf(self, RuntimeConf):
        self._RuntimeConf = RuntimeConf

    @property
    def Id(self):
        """任务Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        self._Message = params.get("Message")
        self._ScaleTier = params.get("ScaleTier")
        self._MasterType = params.get("MasterType")
        self._WorkerType = params.get("WorkerType")
        self._ParameterServerType = params.get("ParameterServerType")
        self._WorkerCount = params.get("WorkerCount")
        self._ParameterServerCount = params.get("ParameterServerCount")
        self._PackageDir = params.get("PackageDir")
        self._Command = params.get("Command")
        self._Args = params.get("Args")
        self._Cluster = params.get("Cluster")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._DelTime = params.get("DelTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Debug = params.get("Debug")
        self._RuntimeConf = params.get("RuntimeConf")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListJobsRequest(AbstractModel):
    """ListJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cluster: 运行任务的集群
        :type Cluster: str
        :param _Limit: 分页参数，返回数量
        :type Limit: int
        :param _Offset: 分页参数，起始位置
        :type Offset: int
        """
        self._Cluster = None
        self._Limit = None
        self._Offset = None

    @property
    def Cluster(self):
        """运行任务的集群
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Limit(self):
        """分页参数，返回数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页参数，起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Cluster = params.get("Cluster")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListJobsResponse(AbstractModel):
    """ListJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Jobs: 训练任务列表
        :type Jobs: list of Job
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Jobs = None
        self._RequestId = None

    @property
    def Jobs(self):
        """训练任务列表
        :rtype: list of Job
        """
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = Job()
                obj._deserialize(item)
                self._Jobs.append(obj)
        self._RequestId = params.get("RequestId")


class ListModelsRequest(AbstractModel):
    """ListModels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cluster: 部署模型的集群， `集群模式` 必填
        :type Cluster: str
        :param _Limit: 分页参数，返回数量上限
        :type Limit: int
        :param _Offset: 分页参数，分页起始位置
        :type Offset: int
        :param _ServType: 部署类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`。
        :type ServType: str
        """
        self._Cluster = None
        self._Limit = None
        self._Offset = None
        self._ServType = None

    @property
    def Cluster(self):
        """部署模型的集群， `集群模式` 必填
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Limit(self):
        """分页参数，返回数量上限
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页参数，分页起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ServType(self):
        """部署类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`。
        :rtype: str
        """
        return self._ServType

    @ServType.setter
    def ServType(self, ServType):
        self._ServType = ServType


    def _deserialize(self, params):
        self._Cluster = params.get("Cluster")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ServType = params.get("ServType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListModelsResponse(AbstractModel):
    """ListModels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Models: Model 数组，用以显示所有模型的信息
        :type Models: list of Model
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Models = None
        self._RequestId = None

    @property
    def Models(self):
        """Model 数组，用以显示所有模型的信息
        :rtype: list of Model
        """
        return self._Models

    @Models.setter
    def Models(self, Models):
        self._Models = Models

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Models") is not None:
            self._Models = []
            for item in params.get("Models"):
                obj = Model()
                obj._deserialize(item)
                self._Models.append(obj)
        self._RequestId = params.get("RequestId")


class Log(AbstractModel):
    """日志

    """

    def __init__(self):
        r"""
        :param _ContainerName: 容器名
        :type ContainerName: str
        :param _Log: 日志内容
        :type Log: str
        :param _Namespace: 空间名
        :type Namespace: str
        :param _PodId: Pod Id
        :type PodId: str
        :param _PodName: Pod名
        :type PodName: str
        :param _Time: 日志日期，格式为“2018-07-02T09:10:04.916553368Z”
        :type Time: str
        """
        self._ContainerName = None
        self._Log = None
        self._Namespace = None
        self._PodId = None
        self._PodName = None
        self._Time = None

    @property
    def ContainerName(self):
        """容器名
        :rtype: str
        """
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def Log(self):
        """日志内容
        :rtype: str
        """
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def Namespace(self):
        """空间名
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def PodId(self):
        """Pod Id
        :rtype: str
        """
        return self._PodId

    @PodId.setter
    def PodId(self, PodId):
        self._PodId = PodId

    @property
    def PodName(self):
        """Pod名
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Time(self):
        """日志日期，格式为“2018-07-02T09:10:04.916553368Z”
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._ContainerName = params.get("ContainerName")
        self._Log = params.get("Log")
        self._Namespace = params.get("Namespace")
        self._PodId = params.get("PodId")
        self._PodName = params.get("PodName")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        r"""
        :param _Name: 模型名称
        :type Name: str
        :param _Description: 模型描述
        :type Description: str
        :param _Cluster: 集群名称
        :type Cluster: str
        :param _Model: 模型地址
        :type Model: str
        :param _RuntimeVersion: 运行环境编号
        :type RuntimeVersion: str
        :param _CreateTime: 模型创建时间
        :type CreateTime: str
        :param _State: 模型运行状态
        :type State: str
        :param _ServingUrl: 提供服务的url
        :type ServingUrl: str
        :param _Message: 相关消息
        :type Message: str
        :param _AppId: 编号
        :type AppId: int
        :param _ServType: 机型
        :type ServType: str
        :param _Expose: 模型暴露方式
        :type Expose: str
        :param _Replicas: 部署副本数量
        :type Replicas: int
        :param _Id: 模型Id
        :type Id: str
        :param _Uin: 创建任务的Uin
        :type Uin: str
        :param _DelTime: 模型删除时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :type DelTime: str
        """
        self._Name = None
        self._Description = None
        self._Cluster = None
        self._Model = None
        self._RuntimeVersion = None
        self._CreateTime = None
        self._State = None
        self._ServingUrl = None
        self._Message = None
        self._AppId = None
        self._ServType = None
        self._Expose = None
        self._Replicas = None
        self._Id = None
        self._Uin = None
        self._DelTime = None

    @property
    def Name(self):
        """模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """模型描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Cluster(self):
        """集群名称
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Model(self):
        """模型地址
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def RuntimeVersion(self):
        """运行环境编号
        :rtype: str
        """
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def CreateTime(self):
        """模型创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        """模型运行状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ServingUrl(self):
        """提供服务的url
        :rtype: str
        """
        return self._ServingUrl

    @ServingUrl.setter
    def ServingUrl(self, ServingUrl):
        self._ServingUrl = ServingUrl

    @property
    def Message(self):
        """相关消息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def AppId(self):
        """编号
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ServType(self):
        """机型
        :rtype: str
        """
        return self._ServType

    @ServType.setter
    def ServType(self, ServType):
        self._ServType = ServType

    @property
    def Expose(self):
        """模型暴露方式
        :rtype: str
        """
        return self._Expose

    @Expose.setter
    def Expose(self, Expose):
        self._Expose = Expose

    @property
    def Replicas(self):
        """部署副本数量
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Id(self):
        """模型Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uin(self):
        """创建任务的Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def DelTime(self):
        """模型删除时间，格式为：2006-01-02 15:04:05.999999999 -0700 MST
        :rtype: str
        """
        return self._DelTime

    @DelTime.setter
    def DelTime(self, DelTime):
        self._DelTime = DelTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Cluster = params.get("Cluster")
        self._Model = params.get("Model")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._CreateTime = params.get("CreateTime")
        self._State = params.get("State")
        self._ServingUrl = params.get("ServingUrl")
        self._Message = params.get("Message")
        self._AppId = params.get("AppId")
        self._ServType = params.get("ServType")
        self._Expose = params.get("Expose")
        self._Replicas = params.get("Replicas")
        self._Id = params.get("Id")
        self._Uin = params.get("Uin")
        self._DelTime = params.get("DelTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryLogsRequest(AbstractModel):
    """QueryLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobName: 任务的名称
        :type JobName: str
        :param _Cluster: 任务所在集群的名称
        :type Cluster: str
        :param _StartTime: 查询日志的开始时间，格式：2019-01-01 00:00:00
        :type StartTime: str
        :param _EndTime: 查询日志的结束时间，格式：2019-01-01 00:00:00
        :type EndTime: str
        :param _Limit: 单次要返回的日志条数上限
        :type Limit: int
        :param _Context: 加载更多日志时使用，透传上次返回的 Context 值，获取后续的日志内容；使用 Context 翻页最多能获取 10000 条日志
        :type Context: str
        """
        self._JobName = None
        self._Cluster = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Context = None

    @property
    def JobName(self):
        """任务的名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Cluster(self):
        """任务所在集群的名称
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def StartTime(self):
        """查询日志的开始时间，格式：2019-01-01 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询日志的结束时间，格式：2019-01-01 00:00:00
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """单次要返回的日志条数上限
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        """加载更多日志时使用，透传上次返回的 Context 值，获取后续的日志内容；使用 Context 翻页最多能获取 10000 条日志
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._JobName = params.get("JobName")
        self._Cluster = params.get("Cluster")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryLogsResponse(AbstractModel):
    """QueryLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 日志查询上下文，用于加载更多日志
        :type Context: str
        :param _Logs: 日志内容列表
        :type Logs: list of Log
        :param _Listover: 是否已经返回所有符合条件的日志
        :type Listover: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Logs = None
        self._Listover = None
        self._RequestId = None

    @property
    def Context(self):
        """日志查询上下文，用于加载更多日志
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Logs(self):
        """日志内容列表
        :rtype: list of Log
        """
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

    @property
    def Listover(self):
        """是否已经返回所有符合条件的日志
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        if params.get("Logs") is not None:
            self._Logs = []
            for item in params.get("Logs"):
                obj = Log()
                obj._deserialize(item)
                self._Logs.append(obj)
        self._Listover = params.get("Listover")
        self._RequestId = params.get("RequestId")