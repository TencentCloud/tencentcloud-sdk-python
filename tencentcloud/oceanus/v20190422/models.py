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


class CreateJobConfigRequest(AbstractModel):
    """CreateJobConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 作业Id
        :type JobId: str
        :param EntrypointClass: 主类
        :type EntrypointClass: str
        :param ProgramArgs: 主类入参
        :type ProgramArgs: str
        :param Remark: 备注
        :type Remark: str
        :param ResourceRefs: 资源引用数组
        :type ResourceRefs: list of ResourceRef
        :param DefaultParallelism: 作业默认并行度
        :type DefaultParallelism: int
        :param Properties: 系统参数
        :type Properties: list of Property
        :param AutoDelete: 1: 作业配置达到上限之后，自动删除可删除的最早版本
        :type AutoDelete: int
        :param COSBucket: 作业使用的 COS 存储桶名
        :type COSBucket: str
        :param LogCollect: 是否采集作业日志
        :type LogCollect: bool
        :param JobManagerSpec: JobManager规格
        :type JobManagerSpec: float
        :param TaskManagerSpec: TaskManager规格
        :type TaskManagerSpec: float
        :param ClsLogsetId: CLS日志集ID
        :type ClsLogsetId: str
        :param ClsTopicId: CLS日志主题ID
        :type ClsTopicId: str
        """
        self.JobId = None
        self.EntrypointClass = None
        self.ProgramArgs = None
        self.Remark = None
        self.ResourceRefs = None
        self.DefaultParallelism = None
        self.Properties = None
        self.AutoDelete = None
        self.COSBucket = None
        self.LogCollect = None
        self.JobManagerSpec = None
        self.TaskManagerSpec = None
        self.ClsLogsetId = None
        self.ClsTopicId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.EntrypointClass = params.get("EntrypointClass")
        self.ProgramArgs = params.get("ProgramArgs")
        self.Remark = params.get("Remark")
        if params.get("ResourceRefs") is not None:
            self.ResourceRefs = []
            for item in params.get("ResourceRefs"):
                obj = ResourceRef()
                obj._deserialize(item)
                self.ResourceRefs.append(obj)
        self.DefaultParallelism = params.get("DefaultParallelism")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        self.AutoDelete = params.get("AutoDelete")
        self.COSBucket = params.get("COSBucket")
        self.LogCollect = params.get("LogCollect")
        self.JobManagerSpec = params.get("JobManagerSpec")
        self.TaskManagerSpec = params.get("TaskManagerSpec")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJobConfigResponse(AbstractModel):
    """CreateJobConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Version: 作业配置版本号
        :type Version: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Version = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.RequestId = params.get("RequestId")


class CreateJobRequest(AbstractModel):
    """CreateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 作业名称，允许输入长度小于等于50个字符的中文、英文、数字、-（横线）、_（下划线）、.（点），且符号必须半角字符。注意作业名不能和现有作业同名
        :type Name: str
        :param JobType: 作业的类型，1 表示 SQL 作业，2 表示 JAR 作业
        :type JobType: int
        :param ClusterType: 集群的类型，1 表示共享集群，2 表示独享集群
        :type ClusterType: int
        :param ClusterId: 当 ClusterType=2 时，必选，用来指定该作业提交的独享集群 ID
        :type ClusterId: str
        :param CuMem: 设置每 CU 的内存规格，单位为 GB，支持 2、4、8、16（需申请开通白名单后使用）。默认为 4，即 1 CU 对应 4 GB 的运行内存
        :type CuMem: int
        :param Remark: 作业的备注信息，可以随意设置
        :type Remark: str
        :param FolderId: 作业名所属文件夹ID，根目录为"root"
        :type FolderId: str
        :param FlinkVersion: 作业运行的Flink版本
        :type FlinkVersion: str
        """
        self.Name = None
        self.JobType = None
        self.ClusterType = None
        self.ClusterId = None
        self.CuMem = None
        self.Remark = None
        self.FolderId = None
        self.FlinkVersion = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.JobType = params.get("JobType")
        self.ClusterType = params.get("ClusterType")
        self.ClusterId = params.get("ClusterId")
        self.CuMem = params.get("CuMem")
        self.Remark = params.get("Remark")
        self.FolderId = params.get("FolderId")
        self.FlinkVersion = params.get("FlinkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJobResponse(AbstractModel):
    """CreateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 作业Id
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateResourceConfigRequest(AbstractModel):
    """CreateResourceConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param ResourceLoc: 位置信息
        :type ResourceLoc: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        :param Remark: 资源描述信息
        :type Remark: str
        :param AutoDelete: 1： 资源版本达到上限，自动删除最早可删除的版本
        :type AutoDelete: int
        """
        self.ResourceId = None
        self.ResourceLoc = None
        self.Remark = None
        self.AutoDelete = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        if params.get("ResourceLoc") is not None:
            self.ResourceLoc = ResourceLoc()
            self.ResourceLoc._deserialize(params.get("ResourceLoc"))
        self.Remark = params.get("Remark")
        self.AutoDelete = params.get("AutoDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceConfigResponse(AbstractModel):
    """CreateResourceConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Version: 资源版本ID
        :type Version: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Version = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    """CreateResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceLoc: 资源位置
        :type ResourceLoc: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        :param ResourceType: 资源类型。目前只支持 JAR，取值为 1
        :type ResourceType: int
        :param Remark: 资源描述
        :type Remark: str
        :param Name: 资源名称
        :type Name: str
        :param ResourceConfigRemark: 资源版本描述
        :type ResourceConfigRemark: str
        :param FolderId: 目录ID
        :type FolderId: str
        """
        self.ResourceLoc = None
        self.ResourceType = None
        self.Remark = None
        self.Name = None
        self.ResourceConfigRemark = None
        self.FolderId = None


    def _deserialize(self, params):
        if params.get("ResourceLoc") is not None:
            self.ResourceLoc = ResourceLoc()
            self.ResourceLoc._deserialize(params.get("ResourceLoc"))
        self.ResourceType = params.get("ResourceType")
        self.Remark = params.get("Remark")
        self.Name = params.get("Name")
        self.ResourceConfigRemark = params.get("ResourceConfigRemark")
        self.FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    """CreateResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param Version: 资源版本
        :type Version: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceId = None
        self.Version = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Version = params.get("Version")
        self.RequestId = params.get("RequestId")


class DeleteResourceConfigsRequest(AbstractModel):
    """DeleteResourceConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param ResourceConfigVersions: 资源版本数组
        :type ResourceConfigVersions: list of int
        """
        self.ResourceId = None
        self.ResourceConfigVersions = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceConfigVersions = params.get("ResourceConfigVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceConfigsResponse(AbstractModel):
    """DeleteResourceConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteResourcesRequest(AbstractModel):
    """DeleteResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceIds: 待删除资源ID列表
        :type ResourceIds: list of str
        """
        self.ResourceIds = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourcesResponse(AbstractModel):
    """DeleteResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTableConfigRequest(AbstractModel):
    """DeleteTableConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 作业ID
        :type JobId: str
        :param DebugId: 调试作业ID
        :type DebugId: int
        :param TableName: 表名
        :type TableName: str
        """
        self.JobId = None
        self.DebugId = None
        self.TableName = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.DebugId = params.get("DebugId")
        self.TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableConfigResponse(AbstractModel):
    """DeleteTableConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeJobConfigsRequest(AbstractModel):
    """DescribeJobConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 作业Id
        :type JobId: str
        :param JobConfigVersions: 作业配置版本
        :type JobConfigVersions: list of int non-negative
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 分页大小，默认20，最大100
        :type Limit: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param OnlyDraft: true 表示只展示草稿
        :type OnlyDraft: bool
        """
        self.JobId = None
        self.JobConfigVersions = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.OnlyDraft = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobConfigVersions = params.get("JobConfigVersions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OnlyDraft = params.get("OnlyDraft")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobConfigsResponse(AbstractModel):
    """DescribeJobConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总的配置版本数量
        :type TotalCount: int
        :param JobConfigSet: 作业配置列表
        :type JobConfigSet: list of JobConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobConfigSet") is not None:
            self.JobConfigSet = []
            for item in params.get("JobConfigSet"):
                obj = JobConfig()
                obj._deserialize(item)
                self.JobConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobIds: 按照一个或者多个作业ID查询。作业ID形如：cql-11112222，每次请求的作业上限为100。参数不支持同时指定JobIds和Filters。
        :type JobIds: list of str
        :param Filters: 过滤条件，支持的 Filter.Name 为：作业名 Name、作业状态 Status、所属集群 ClusterId。每次请求的 Filters 个数的上限为 3，Filter.Values 的个数上限为 5。参数不支持同时指定 JobIds 和 Filters。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 分页大小，默认为20，最大值为100
        :type Limit: int
        """
        self.JobIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobsResponse(AbstractModel):
    """DescribeJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 作业总数
        :type TotalCount: int
        :param JobSet: 作业列表
        :type JobSet: list of JobV1
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobSet") is not None:
            self.JobSet = []
            for item in params.get("JobSet"):
                obj = JobV1()
                obj._deserialize(item)
                self.JobSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceConfigsRequest(AbstractModel):
    """DescribeResourceConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param Offset: 偏移量，仅当设置 Limit 时该参数有效
        :type Offset: int
        :param Limit: 返回值大小，不填则返回全量数据
        :type Limit: int
        :param ResourceConfigVersions: 资源配置Versions集合
        :type ResourceConfigVersions: list of int
        :param JobConfigVersion: 作业配置版本
        :type JobConfigVersion: int
        :param JobId: 作业ID
        :type JobId: str
        """
        self.ResourceId = None
        self.Offset = None
        self.Limit = None
        self.ResourceConfigVersions = None
        self.JobConfigVersion = None
        self.JobId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ResourceConfigVersions = params.get("ResourceConfigVersions")
        self.JobConfigVersion = params.get("JobConfigVersion")
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceConfigsResponse(AbstractModel):
    """DescribeResourceConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceConfigSet: 资源配置描述数组
        :type ResourceConfigSet: list of ResourceConfigItem
        :param TotalCount: 资源配置数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceConfigSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceConfigSet") is not None:
            self.ResourceConfigSet = []
            for item in params.get("ResourceConfigSet"):
                obj = ResourceConfigItem()
                obj._deserialize(item)
                self.ResourceConfigSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeResourceRelatedJobsRequest(AbstractModel):
    """DescribeResourceRelatedJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param DESCByJobConfigCreateTime: 默认0;   1： 按照作业版本创建时间降序
        :type DESCByJobConfigCreateTime: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 分页大小，默认为20，最大值为100
        :type Limit: int
        :param ResourceConfigVersion: 资源版本号
        :type ResourceConfigVersion: int
        """
        self.ResourceId = None
        self.DESCByJobConfigCreateTime = None
        self.Offset = None
        self.Limit = None
        self.ResourceConfigVersion = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.DESCByJobConfigCreateTime = params.get("DESCByJobConfigCreateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ResourceConfigVersion = params.get("ResourceConfigVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceRelatedJobsResponse(AbstractModel):
    """DescribeResourceRelatedJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param RefJobInfos: 关联作业信息
        :type RefJobInfos: list of ResourceRefJobInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RefJobInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RefJobInfos") is not None:
            self.RefJobInfos = []
            for item in params.get("RefJobInfos"):
                obj = ResourceRefJobInfo()
                obj._deserialize(item)
                self.RefJobInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourcesRequest(AbstractModel):
    """DescribeResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceIds: 需要查询的资源ID数组，数量不超过100个。如果填写了该参数则忽略Filters参数。
        :type ResourceIds: list of str
        :param Offset: 偏移量，仅当设置 Limit 参数时有效
        :type Offset: int
        :param Limit: 条数限制。如果不填，默认返回 20 条
        :type Limit: int
        :param Filters: <li><strong>ResourceName</strong></li>
<p style="padding-left: 30px;">按照资源名字过滤，支持模糊过滤。传入的过滤名字不超过5个</p><p style="padding-left: 30px;">类型: String</p><p style="padding-left: 30px;">必选: 否</p>
        :type Filters: list of Filter
        """
        self.ResourceIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesResponse(AbstractModel):
    """DescribeResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceSet: 资源详细信息集合
        :type ResourceSet: list of ResourceItem
        :param TotalCount: 总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = ResourceItem()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSystemResourcesRequest(AbstractModel):
    """DescribeSystemResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceIds: 需要查询的资源ID数组
        :type ResourceIds: list of str
        :param Offset: 偏移量，仅当设置 Limit 参数时有效
        :type Offset: int
        :param Limit: 条数限制，默认返回 20 条
        :type Limit: int
        :param Filters: 查询资源配置列表， 如果不填写，返回该 ResourceIds.N 下所有作业配置列表
        :type Filters: list of Filter
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param FlinkVersion: 查询对应Flink版本的内置connector
        :type FlinkVersion: str
        """
        self.ResourceIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.ClusterId = None
        self.FlinkVersion = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.FlinkVersion = params.get("FlinkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSystemResourcesResponse(AbstractModel):
    """DescribeSystemResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceSet: 资源详细信息集合
        :type ResourceSet: list of SystemResourceItem
        :param TotalCount: 总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = SystemResourceItem()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询作业列表时的过滤器

    """

    def __init__(self):
        r"""
        :param Name: 要过滤的字段
        :type Name: str
        :param Values: 字段的过滤值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobConfig(AbstractModel):
    """作业配置详情

    """

    def __init__(self):
        r"""
        :param JobId: 作业Id
        :type JobId: str
        :param EntrypointClass: 主类
注意：此字段可能返回 null，表示取不到有效值。
        :type EntrypointClass: str
        :param ProgramArgs: 主类入参
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramArgs: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 作业配置创建时间
        :type CreateTime: str
        :param Version: 作业配置的版本号
        :type Version: int
        :param DefaultParallelism: 作业默认并行度
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultParallelism: int
        :param Properties: 系统参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param ResourceRefDetails: 引用资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRefDetails: list of ResourceRefDetail
        :param CreatorUin: 创建者uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param UpdateTime: 作业配置上次启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param COSBucket: 作业绑定的存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :type COSBucket: str
        :param LogCollect: 是否启用日志收集，0-未启用，1-已启用，2-历史集群未设置日志集，3-历史集群已开启
注意：此字段可能返回 null，表示取不到有效值。
        :type LogCollect: int
        :param MaxParallelism: 作业的最大并行度
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxParallelism: int
        :param JobManagerSpec: JobManager规格
注意：此字段可能返回 null，表示取不到有效值。
        :type JobManagerSpec: float
        :param TaskManagerSpec: TaskManager规格
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskManagerSpec: float
        :param ClsLogsetId: CLS日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsLogsetId: str
        :param ClsTopicId: CLS日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsTopicId: str
        """
        self.JobId = None
        self.EntrypointClass = None
        self.ProgramArgs = None
        self.Remark = None
        self.CreateTime = None
        self.Version = None
        self.DefaultParallelism = None
        self.Properties = None
        self.ResourceRefDetails = None
        self.CreatorUin = None
        self.UpdateTime = None
        self.COSBucket = None
        self.LogCollect = None
        self.MaxParallelism = None
        self.JobManagerSpec = None
        self.TaskManagerSpec = None
        self.ClsLogsetId = None
        self.ClsTopicId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.EntrypointClass = params.get("EntrypointClass")
        self.ProgramArgs = params.get("ProgramArgs")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.Version = params.get("Version")
        self.DefaultParallelism = params.get("DefaultParallelism")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        if params.get("ResourceRefDetails") is not None:
            self.ResourceRefDetails = []
            for item in params.get("ResourceRefDetails"):
                obj = ResourceRefDetail()
                obj._deserialize(item)
                self.ResourceRefDetails.append(obj)
        self.CreatorUin = params.get("CreatorUin")
        self.UpdateTime = params.get("UpdateTime")
        self.COSBucket = params.get("COSBucket")
        self.LogCollect = params.get("LogCollect")
        self.MaxParallelism = params.get("MaxParallelism")
        self.JobManagerSpec = params.get("JobManagerSpec")
        self.TaskManagerSpec = params.get("TaskManagerSpec")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobV1(AbstractModel):
    """Job详细信息

    """

    def __init__(self):
        r"""
        :param JobId: 作业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param OwnerUin: 用户UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param CreatorUin: 创建者UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param Name: 作业名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param JobType: 作业类型，1：sql作业，2：Jar作业
注意：此字段可能返回 null，表示取不到有效值。
        :type JobType: int
        :param Status: 作业状态，1：未初始化，2：未发布，3：操作中，4：运行中，5：停止，6：暂停，-1：故障
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CreateTime: 作业创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param StartTime: 作业启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param StopTime: 作业停止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StopTime: str
        :param UpdateTime: 作业更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param TotalRunMillis: 作业累计运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalRunMillis: int
        :param Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param LastOpResult: 操作错误提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOpResult: str
        :param ClusterName: 集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param LatestJobConfigVersion: 最新配置版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestJobConfigVersion: int
        :param PublishedJobConfigVersion: 已发布的配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishedJobConfigVersion: int
        :param RunningCuNum: 运行的CU数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCuNum: int
        :param CuMem: 作业内存规格
注意：此字段可能返回 null，表示取不到有效值。
        :type CuMem: int
        :param StatusDesc: 作业状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param CurrentRunMillis: 运行状态时表示单次运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentRunMillis: int
        :param ClusterId: 作业所在的集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param WebUIUrl: 作业管理WEB UI 入口
注意：此字段可能返回 null，表示取不到有效值。
        :type WebUIUrl: str
        :param SchedulerType: 作业所在集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerType: int
        :param ClusterStatus: 作业所在集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: int
        :param RunningCu: 细粒度下的运行的CU数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCu: float
        :param FlinkVersion: 作业运行的 Flink 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FlinkVersion: str
        """
        self.JobId = None
        self.Region = None
        self.Zone = None
        self.AppId = None
        self.OwnerUin = None
        self.CreatorUin = None
        self.Name = None
        self.JobType = None
        self.Status = None
        self.CreateTime = None
        self.StartTime = None
        self.StopTime = None
        self.UpdateTime = None
        self.TotalRunMillis = None
        self.Remark = None
        self.LastOpResult = None
        self.ClusterName = None
        self.LatestJobConfigVersion = None
        self.PublishedJobConfigVersion = None
        self.RunningCuNum = None
        self.CuMem = None
        self.StatusDesc = None
        self.CurrentRunMillis = None
        self.ClusterId = None
        self.WebUIUrl = None
        self.SchedulerType = None
        self.ClusterStatus = None
        self.RunningCu = None
        self.FlinkVersion = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.AppId = params.get("AppId")
        self.OwnerUin = params.get("OwnerUin")
        self.CreatorUin = params.get("CreatorUin")
        self.Name = params.get("Name")
        self.JobType = params.get("JobType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.StopTime = params.get("StopTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TotalRunMillis = params.get("TotalRunMillis")
        self.Remark = params.get("Remark")
        self.LastOpResult = params.get("LastOpResult")
        self.ClusterName = params.get("ClusterName")
        self.LatestJobConfigVersion = params.get("LatestJobConfigVersion")
        self.PublishedJobConfigVersion = params.get("PublishedJobConfigVersion")
        self.RunningCuNum = params.get("RunningCuNum")
        self.CuMem = params.get("CuMem")
        self.StatusDesc = params.get("StatusDesc")
        self.CurrentRunMillis = params.get("CurrentRunMillis")
        self.ClusterId = params.get("ClusterId")
        self.WebUIUrl = params.get("WebUIUrl")
        self.SchedulerType = params.get("SchedulerType")
        self.ClusterStatus = params.get("ClusterStatus")
        self.RunningCu = params.get("RunningCu")
        self.FlinkVersion = params.get("FlinkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Property(AbstractModel):
    """系统配置属性

    """

    def __init__(self):
        r"""
        :param Key: 系统配置的Key
        :type Key: str
        :param Value: 系统配置的Value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceConfigItem(AbstractModel):
    """描述资源配置的返回参数

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param ResourceType: 资源类型
        :type ResourceType: int
        :param Region: 资源所属地域
        :type Region: str
        :param AppId: 资源所属AppId
        :type AppId: int
        :param OwnerUin: 主账号Uin
        :type OwnerUin: str
        :param CreatorUin: 子账号Uin
        :type CreatorUin: str
        :param ResourceLoc: 资源位置描述
        :type ResourceLoc: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        :param CreateTime: 资源创建时间
        :type CreateTime: str
        :param Version: 资源版本
        :type Version: int
        :param Remark: 资源描述
        :type Remark: str
        :param Status: 资源状态：0: 资源同步中，1:资源已就绪
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param RefJobCount: 关联作业个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RefJobCount: int
        """
        self.ResourceId = None
        self.ResourceType = None
        self.Region = None
        self.AppId = None
        self.OwnerUin = None
        self.CreatorUin = None
        self.ResourceLoc = None
        self.CreateTime = None
        self.Version = None
        self.Remark = None
        self.Status = None
        self.RefJobCount = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceType = params.get("ResourceType")
        self.Region = params.get("Region")
        self.AppId = params.get("AppId")
        self.OwnerUin = params.get("OwnerUin")
        self.CreatorUin = params.get("CreatorUin")
        if params.get("ResourceLoc") is not None:
            self.ResourceLoc = ResourceLoc()
            self.ResourceLoc._deserialize(params.get("ResourceLoc"))
        self.CreateTime = params.get("CreateTime")
        self.Version = params.get("Version")
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        self.RefJobCount = params.get("RefJobCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceItem(AbstractModel):
    """资源详细描述

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param Name: 资源名称
        :type Name: str
        :param ResourceType: 资源类型
        :type ResourceType: int
        :param ResourceLoc: 资源位置
        :type ResourceLoc: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        :param Region: 资源地域
        :type Region: str
        :param AppId: 应用ID
        :type AppId: int
        :param OwnerUin: 主账号Uin
        :type OwnerUin: str
        :param CreatorUin: 子账号Uin
        :type CreatorUin: str
        :param CreateTime: 资源创建时间
        :type CreateTime: str
        :param UpdateTime: 资源最后更新时间
        :type UpdateTime: str
        :param LatestResourceConfigVersion: 资源的资源版本ID
        :type LatestResourceConfigVersion: int
        :param Remark: 资源备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param VersionCount: 版本个数
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionCount: int
        :param RefJobCount: 关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :type RefJobCount: int
        """
        self.ResourceId = None
        self.Name = None
        self.ResourceType = None
        self.ResourceLoc = None
        self.Region = None
        self.AppId = None
        self.OwnerUin = None
        self.CreatorUin = None
        self.CreateTime = None
        self.UpdateTime = None
        self.LatestResourceConfigVersion = None
        self.Remark = None
        self.VersionCount = None
        self.RefJobCount = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Name = params.get("Name")
        self.ResourceType = params.get("ResourceType")
        if params.get("ResourceLoc") is not None:
            self.ResourceLoc = ResourceLoc()
            self.ResourceLoc._deserialize(params.get("ResourceLoc"))
        self.Region = params.get("Region")
        self.AppId = params.get("AppId")
        self.OwnerUin = params.get("OwnerUin")
        self.CreatorUin = params.get("CreatorUin")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.LatestResourceConfigVersion = params.get("LatestResourceConfigVersion")
        self.Remark = params.get("Remark")
        self.VersionCount = params.get("VersionCount")
        self.RefJobCount = params.get("RefJobCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceLoc(AbstractModel):
    """资源位置描述

    """

    def __init__(self):
        r"""
        :param StorageType: 资源位置的存储类型，目前只支持1:COS
        :type StorageType: int
        :param Param: 描述资源位置的json
        :type Param: :class:`tencentcloud.oceanus.v20190422.models.ResourceLocParam`
        """
        self.StorageType = None
        self.Param = None


    def _deserialize(self, params):
        self.StorageType = params.get("StorageType")
        if params.get("Param") is not None:
            self.Param = ResourceLocParam()
            self.Param._deserialize(params.get("Param"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceLocParam(AbstractModel):
    """资源参数描述

    """

    def __init__(self):
        r"""
        :param Bucket: 资源bucket
        :type Bucket: str
        :param Path: 资源路径
        :type Path: str
        :param Region: 资源所在地域，如果不填，则使用Resource的Region
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self.Bucket = None
        self.Path = None
        self.Region = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Path = params.get("Path")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRef(AbstractModel):
    """资源引用参数

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param Version: 资源版本ID，-1表示使用最新版本
        :type Version: int
        :param Type: 引用资源类型，例如主资源设置为1，代表main class所在的jar包
        :type Type: int
        """
        self.ResourceId = None
        self.Version = None
        self.Type = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Version = params.get("Version")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRefDetail(AbstractModel):
    """JobConfig引用资源信息

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源id
        :type ResourceId: str
        :param Version: 资源版本，-1表示使用最新版本
        :type Version: int
        :param Name: 资源名称
        :type Name: str
        :param Type: 1: 主资源
        :type Type: int
        :param SystemProvide: 1: 系统内置资源
        :type SystemProvide: int
        """
        self.ResourceId = None
        self.Version = None
        self.Name = None
        self.Type = None
        self.SystemProvide = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Version = params.get("Version")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.SystemProvide = params.get("SystemProvide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRefJobInfo(AbstractModel):
    """资源被Job 引用信息

    """

    def __init__(self):
        r"""
        :param JobId: Job id
        :type JobId: str
        :param JobConfigVersion: Job配置版本
        :type JobConfigVersion: int
        :param ResourceVersion: 资源版本
        :type ResourceVersion: int
        """
        self.JobId = None
        self.JobConfigVersion = None
        self.ResourceVersion = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobConfigVersion = params.get("JobConfigVersion")
        self.ResourceVersion = params.get("ResourceVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobDescription(AbstractModel):
    """作业启动详情

    """

    def __init__(self):
        r"""
        :param JobId: 作业Id
        :type JobId: str
        :param RunType: 运行类型，1：启动，2：恢复
        :type RunType: int
        :param StartMode: 已废弃。旧版 SQL 类型作业启动参数：指定数据源消费起始时间点
        :type StartMode: str
        :param JobConfigVersion: 当前作业的某个版本
        :type JobConfigVersion: int
        :param SavepointPath: Savepoint路径
        :type SavepointPath: str
        :param SavepointId: Savepoint的Id
        :type SavepointId: str
        """
        self.JobId = None
        self.RunType = None
        self.StartMode = None
        self.JobConfigVersion = None
        self.SavepointPath = None
        self.SavepointId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RunType = params.get("RunType")
        self.StartMode = params.get("StartMode")
        self.JobConfigVersion = params.get("JobConfigVersion")
        self.SavepointPath = params.get("SavepointPath")
        self.SavepointId = params.get("SavepointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobsRequest(AbstractModel):
    """RunJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param RunJobDescriptions: 批量启动作业的描述信息
        :type RunJobDescriptions: list of RunJobDescription
        """
        self.RunJobDescriptions = None


    def _deserialize(self, params):
        if params.get("RunJobDescriptions") is not None:
            self.RunJobDescriptions = []
            for item in params.get("RunJobDescriptions"):
                obj = RunJobDescription()
                obj._deserialize(item)
                self.RunJobDescriptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobsResponse(AbstractModel):
    """RunJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopJobDescription(AbstractModel):
    """停止作业的描述信息

    """

    def __init__(self):
        r"""
        :param JobId: 作业Id
        :type JobId: str
        :param StopType: 停止类型，1 停止 2 暂停
        :type StopType: int
        """
        self.JobId = None
        self.StopType = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopJobsRequest(AbstractModel):
    """StopJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param StopJobDescriptions: 批量停止作业的描述信息
        :type StopJobDescriptions: list of StopJobDescription
        """
        self.StopJobDescriptions = None


    def _deserialize(self, params):
        if params.get("StopJobDescriptions") is not None:
            self.StopJobDescriptions = []
            for item in params.get("StopJobDescriptions"):
                obj = StopJobDescription()
                obj._deserialize(item)
                self.StopJobDescriptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopJobsResponse(AbstractModel):
    """StopJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SystemResourceItem(AbstractModel):
    """系统资源返回值

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param Name: 资源名称
        :type Name: str
        :param ResourceType: 资源类型。1 表示 JAR 包，目前只支持该值。
        :type ResourceType: int
        :param Remark: 资源备注
        :type Remark: str
        :param Region: 资源所属地域
        :type Region: str
        :param LatestResourceConfigVersion: 资源的最新版本
        :type LatestResourceConfigVersion: int
        """
        self.ResourceId = None
        self.Name = None
        self.ResourceType = None
        self.Remark = None
        self.Region = None
        self.LatestResourceConfigVersion = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Name = params.get("Name")
        self.ResourceType = params.get("ResourceType")
        self.Remark = params.get("Remark")
        self.Region = params.get("Region")
        self.LatestResourceConfigVersion = params.get("LatestResourceConfigVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        