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


class AbortCronJobsRequest(AbstractModel):
    """AbortCronJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param CronJobIds: 定时任务ID数组
        :type CronJobIds: list of str
        """
        self.ProjectId = None
        self.CronJobIds = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CronJobIds = params.get("CronJobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortCronJobsResponse(AbstractModel):
    """AbortCronJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AbortJobRequest(AbstractModel):
    """AbortJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param AbortReason: 中断原因
        :type AbortReason: int
        """
        self.JobId = None
        self.ProjectId = None
        self.ScenarioId = None
        self.AbortReason = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        self.AbortReason = params.get("AbortReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortJobResponse(AbstractModel):
    """AbortJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AdjustJobSpeedRequest(AbstractModel):
    """AdjustJobSpeed请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param TargetRequestsPerSecond: 目标RPS
        :type TargetRequestsPerSecond: int
        """
        self.JobId = None
        self.TargetRequestsPerSecond = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TargetRequestsPerSecond = params.get("TargetRequestsPerSecond")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdjustJobSpeedResponse(AbstractModel):
    """AdjustJobSpeed返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AggregationLegend(AbstractModel):
    """聚合函数

    """

    def __init__(self):
        r"""
        :param Aggregation: 指标支持的聚合函数
        :type Aggregation: str
        :param Legend: 聚合函数作用于指标后对应的描述
        :type Legend: str
        :param Unit: 聚合之后的指标单位
        :type Unit: str
        """
        self.Aggregation = None
        self.Legend = None
        self.Unit = None


    def _deserialize(self, params):
        self.Aggregation = params.get("Aggregation")
        self.Legend = params.get("Legend")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertChannel(AbstractModel):
    """告警通知渠道

    """

    def __init__(self):
        r"""
        :param NoticeId: 通知模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeId: str
        :param AMPConsumerId: AMP consumer ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AMPConsumerId: str
        """
        self.NoticeId = None
        self.AMPConsumerId = None


    def _deserialize(self, params):
        self.NoticeId = params.get("NoticeId")
        self.AMPConsumerId = params.get("AMPConsumerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertChannelRecord(AbstractModel):
    """告警通知接收组

    """

    def __init__(self):
        r"""
        :param NoticeId: Notice ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeId: str
        :param AMPConsumerId: Consumer ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AMPConsumerId: str
        :param ProjectId: 项目 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self.NoticeId = None
        self.AMPConsumerId = None
        self.ProjectId = None
        self.Status = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.NoticeId = params.get("NoticeId")
        self.AMPConsumerId = params.get("AMPConsumerId")
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertRecord(AbstractModel):
    """告警历史记录项

    """

    def __init__(self):
        r"""
        :param AlertRecordId: 告警历史记录项 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRecordId: str
        :param ProjectId: 项目 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param ScenarioId: 场景 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioId: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.pts.v20210728.models.AlertRecordStatus`
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param JobId: 任务 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        """
        self.AlertRecordId = None
        self.ProjectId = None
        self.ScenarioId = None
        self.Status = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.JobId = None


    def _deserialize(self, params):
        self.AlertRecordId = params.get("AlertRecordId")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        if params.get("Status") is not None:
            self.Status = AlertRecordStatus()
            self.Status._deserialize(params.get("Status"))
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertRecordStatus(AbstractModel):
    """告警历史项的状态

    """

    def __init__(self):
        r"""
        :param AbortJob: 停止压测任务成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :type AbortJob: int
        :param SendNotice: 发送告警通知成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :type SendNotice: int
        """
        self.AbortJob = None
        self.SendNotice = None


    def _deserialize(self, params):
        self.AbortJob = params.get("AbortJob")
        self.SendNotice = params.get("SendNotice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Attributes(AbstractModel):
    """采样日志附带属性

    """

    def __init__(self):
        r"""
        :param Status: 采用请求返回码
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Result: 采样请求结果码
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param Service: 采样请求API
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param Method: 采样请求调用方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param Duration: 采样请求延时时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        """
        self.Status = None
        self.Result = None
        self.Service = None
        self.Method = None
        self.Duration = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Result = params.get("Result")
        self.Service = params.get("Service")
        self.Method = params.get("Method")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckSummary(AbstractModel):
    """检查点汇总结果

    """

    def __init__(self):
        r"""
        :param Name: 检查点名字
        :type Name: str
        :param Step: 检查点所在步骤名字
        :type Step: str
        :param SuccessCount: 检查点成功次数
        :type SuccessCount: int
        :param FailCount: 检查失败次数
        :type FailCount: int
        :param ErrorRate: 错误比例
        :type ErrorRate: float
        """
        self.Name = None
        self.Step = None
        self.SuccessCount = None
        self.FailCount = None
        self.ErrorRate = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Step = params.get("Step")
        self.SuccessCount = params.get("SuccessCount")
        self.FailCount = params.get("FailCount")
        self.ErrorRate = params.get("ErrorRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Concurrency(AbstractModel):
    """并发模式的施压配置

    """

    def __init__(self):
        r"""
        :param Stages: 多阶段配置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Stages: list of Stage
        :param IterationCount: 运行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type IterationCount: int
        :param MaxRequestsPerSecond: 最大RPS
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestsPerSecond: int
        """
        self.Stages = None
        self.IterationCount = None
        self.MaxRequestsPerSecond = None


    def _deserialize(self, params):
        if params.get("Stages") is not None:
            self.Stages = []
            for item in params.get("Stages"):
                obj = Stage()
                obj._deserialize(item)
                self.Stages.append(obj)
        self.IterationCount = params.get("IterationCount")
        self.MaxRequestsPerSecond = params.get("MaxRequestsPerSecond")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyScenarioRequest(AbstractModel):
    """CopyScenario请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目 ID
        :type ProjectId: str
        :param ScenarioId: 场景 ID
        :type ScenarioId: str
        """
        self.ProjectId = None
        self.ScenarioId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyScenarioResponse(AbstractModel):
    """CopyScenario返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioId: 复制出的新场景 ID
        :type ScenarioId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScenarioId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScenarioId = params.get("ScenarioId")
        self.RequestId = params.get("RequestId")


class CreateAlertChannelRequest(AbstractModel):
    """CreateAlertChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param NoticeId: Notice ID
        :type NoticeId: str
        :param ProjectId: 项目 ID
        :type ProjectId: str
        :param AMPConsumerId: AMP Consumer ID
        :type AMPConsumerId: str
        """
        self.NoticeId = None
        self.ProjectId = None
        self.AMPConsumerId = None


    def _deserialize(self, params):
        self.NoticeId = params.get("NoticeId")
        self.ProjectId = params.get("ProjectId")
        self.AMPConsumerId = params.get("AMPConsumerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlertChannelResponse(AbstractModel):
    """CreateAlertChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCronJobRequest(AbstractModel):
    """CreateCronJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 定时任务名字
        :type Name: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param ScenarioName: 场景名称
        :type ScenarioName: str
        :param FrequencyType: 执行频率类型，1:只执行一次; 2:日粒度; 3:周粒度; 4:高级
        :type FrequencyType: int
        :param CronExpression: cron表达式
        :type CronExpression: str
        :param JobOwner: 任务发起人
        :type JobOwner: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param NoticeId: Notice ID
        :type NoticeId: str
        :param Note: 备注
        :type Note: str
        """
        self.Name = None
        self.ProjectId = None
        self.ScenarioId = None
        self.ScenarioName = None
        self.FrequencyType = None
        self.CronExpression = None
        self.JobOwner = None
        self.EndTime = None
        self.NoticeId = None
        self.Note = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        self.ScenarioName = params.get("ScenarioName")
        self.FrequencyType = params.get("FrequencyType")
        self.CronExpression = params.get("CronExpression")
        self.JobOwner = params.get("JobOwner")
        self.EndTime = params.get("EndTime")
        self.NoticeId = params.get("NoticeId")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCronJobResponse(AbstractModel):
    """CreateCronJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param CronJobId: 定时任务ID
        :type CronJobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CronJobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CronJobId = params.get("CronJobId")
        self.RequestId = params.get("RequestId")


class CreateFileRequest(AbstractModel):
    """CreateFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileId: 文件 ID
        :type FileId: str
        :param ProjectId: 项目 ID
        :type ProjectId: str
        :param Kind: 文件种类，参数文件-1，协议文件-2，请求文件-3
        :type Kind: int
        :param Name: 文件名
        :type Name: str
        :param Size: 文件大小
        :type Size: int
        :param Type: 文件类型，文件夹-folder
        :type Type: str
        :param LineCount: 行数
        :type LineCount: int
        :param HeadLines: 前几行数据
        :type HeadLines: list of str
        :param TailLines: 后几行数据
        :type TailLines: list of str
        :param HeaderInFile: 表头是否在文件内
        :type HeaderInFile: bool
        :param HeaderColumns: 表头
        :type HeaderColumns: list of str
        :param FileInfos: 文件夹中的文件
        :type FileInfos: list of FileInfo
        """
        self.FileId = None
        self.ProjectId = None
        self.Kind = None
        self.Name = None
        self.Size = None
        self.Type = None
        self.LineCount = None
        self.HeadLines = None
        self.TailLines = None
        self.HeaderInFile = None
        self.HeaderColumns = None
        self.FileInfos = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.ProjectId = params.get("ProjectId")
        self.Kind = params.get("Kind")
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Type = params.get("Type")
        self.LineCount = params.get("LineCount")
        self.HeadLines = params.get("HeadLines")
        self.TailLines = params.get("TailLines")
        self.HeaderInFile = params.get("HeaderInFile")
        self.HeaderColumns = params.get("HeaderColumns")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileResponse(AbstractModel):
    """CreateFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 项目名
        :type Name: str
        :param Description: 项目描述
        :type Description: str
        :param Tags: 标签数组
        :type Tags: list of TagSpec
        """
        self.Name = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagSpec()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RequestId = params.get("RequestId")


class CreateScenarioRequest(AbstractModel):
    """CreateScenario请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 场景名
        :type Name: str
        :param Type: 压测引擎类型
        :type Type: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Description: 场景描述
        :type Description: str
        :param Load: 施压配置
        :type Load: :class:`tencentcloud.pts.v20210728.models.Load`
        :param Configs: deprecated
        :type Configs: list of str
        :param Datasets: 测试数据集
        :type Datasets: list of TestData
        :param Extensions: deprecated
        :type Extensions: list of str
        :param SLAId: deprecated
        :type SLAId: str
        :param CronId: cron job ID
        :type CronId: str
        :param Scripts: deprecated
        :type Scripts: list of str
        :param TestScripts: 测试脚本文件信息
        :type TestScripts: list of ScriptInfo
        :param Protocols: 协议文件路径
        :type Protocols: list of ProtocolInfo
        :param RequestFiles: 请求文件路径
        :type RequestFiles: list of FileInfo
        :param SLAPolicy: SLA 策略
        :type SLAPolicy: :class:`tencentcloud.pts.v20210728.models.SLAPolicy`
        :param Plugins: 拓展包文件路径
        :type Plugins: list of FileInfo
        :param DomainNameConfig: 域名解析配置
        :type DomainNameConfig: :class:`tencentcloud.pts.v20210728.models.DomainNameConfig`
        """
        self.Name = None
        self.Type = None
        self.ProjectId = None
        self.Description = None
        self.Load = None
        self.Configs = None
        self.Datasets = None
        self.Extensions = None
        self.SLAId = None
        self.CronId = None
        self.Scripts = None
        self.TestScripts = None
        self.Protocols = None
        self.RequestFiles = None
        self.SLAPolicy = None
        self.Plugins = None
        self.DomainNameConfig = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.ProjectId = params.get("ProjectId")
        self.Description = params.get("Description")
        if params.get("Load") is not None:
            self.Load = Load()
            self.Load._deserialize(params.get("Load"))
        self.Configs = params.get("Configs")
        if params.get("Datasets") is not None:
            self.Datasets = []
            for item in params.get("Datasets"):
                obj = TestData()
                obj._deserialize(item)
                self.Datasets.append(obj)
        self.Extensions = params.get("Extensions")
        self.SLAId = params.get("SLAId")
        self.CronId = params.get("CronId")
        self.Scripts = params.get("Scripts")
        if params.get("TestScripts") is not None:
            self.TestScripts = []
            for item in params.get("TestScripts"):
                obj = ScriptInfo()
                obj._deserialize(item)
                self.TestScripts.append(obj)
        if params.get("Protocols") is not None:
            self.Protocols = []
            for item in params.get("Protocols"):
                obj = ProtocolInfo()
                obj._deserialize(item)
                self.Protocols.append(obj)
        if params.get("RequestFiles") is not None:
            self.RequestFiles = []
            for item in params.get("RequestFiles"):
                obj = FileInfo()
                obj._deserialize(item)
                self.RequestFiles.append(obj)
        if params.get("SLAPolicy") is not None:
            self.SLAPolicy = SLAPolicy()
            self.SLAPolicy._deserialize(params.get("SLAPolicy"))
        if params.get("Plugins") is not None:
            self.Plugins = []
            for item in params.get("Plugins"):
                obj = FileInfo()
                obj._deserialize(item)
                self.Plugins.append(obj)
        if params.get("DomainNameConfig") is not None:
            self.DomainNameConfig = DomainNameConfig()
            self.DomainNameConfig._deserialize(params.get("DomainNameConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScenarioResponse(AbstractModel):
    """CreateScenario返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScenarioId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScenarioId = params.get("ScenarioId")
        self.RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """COS临时凭证

    """

    def __init__(self):
        r"""
        :param TmpSecretId: 临时secret ID
        :type TmpSecretId: str
        :param TmpSecretKey: 临时secret key
        :type TmpSecretKey: str
        :param Token: 临时token
        :type Token: str
        """
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.Token = None


    def _deserialize(self, params):
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CronJob(AbstractModel):
    """定时任务

    """

    def __init__(self):
        r"""
        :param CronJobId: 定时任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CronJobId: str
        :param Name: 定时任务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param ScenarioId: 场景ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioId: str
        :param ScenarioName: 场景名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioName: str
        :param CronExpression: cron 表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type CronExpression: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param AbortReason: 中止原因
注意：此字段可能返回 null，表示取不到有效值。
        :type AbortReason: int
        :param Status: 定时任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param NoticeId: Notice ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeId: str
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param FrequencyType: 执行频率类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FrequencyType: int
        :param Note: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param JobOwner: tom
注意：此字段可能返回 null，表示取不到有效值。
        :type JobOwner: str
        """
        self.CronJobId = None
        self.Name = None
        self.ProjectId = None
        self.ScenarioId = None
        self.ScenarioName = None
        self.CronExpression = None
        self.EndTime = None
        self.AbortReason = None
        self.Status = None
        self.NoticeId = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.FrequencyType = None
        self.Note = None
        self.JobOwner = None


    def _deserialize(self, params):
        self.CronJobId = params.get("CronJobId")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        self.ScenarioName = params.get("ScenarioName")
        self.CronExpression = params.get("CronExpression")
        self.EndTime = params.get("EndTime")
        self.AbortReason = params.get("AbortReason")
        self.Status = params.get("Status")
        self.NoticeId = params.get("NoticeId")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.FrequencyType = params.get("FrequencyType")
        self.Note = params.get("Note")
        self.JobOwner = params.get("JobOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomSample(AbstractModel):
    """sample附带原始查询语句中的metric, aggregation

    """

    def __init__(self):
        r"""
        :param Metric: 指标名
        :type Metric: str
        :param Aggregation: 聚合条件
        :type Aggregation: str
        :param Labels: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        :param Value: 查询值
        :type Value: float
        :param Timestamp: Time is the number of milliseconds since the epoch
// (1970-01-01 00:00 UTC) excluding leap seconds.
        :type Timestamp: int
        :param Unit: 指标对应的单位，当前单位有：s,bytes,bytes/s,reqs,reqs/s,checks,checks/s,iters,iters/s,VUs, %
        :type Unit: str
        """
        self.Metric = None
        self.Aggregation = None
        self.Labels = None
        self.Value = None
        self.Timestamp = None
        self.Unit = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Aggregation = params.get("Aggregation")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.Value = params.get("Value")
        self.Timestamp = params.get("Timestamp")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomSampleMatrix(AbstractModel):
    """指标矩阵，可包含多条指标序列

    """

    def __init__(self):
        r"""
        :param Metric: 指标名字
        :type Metric: str
        :param Aggregation: 聚合函数
        :type Aggregation: str
        :param Unit: 指标单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Streams: 指标序列数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Streams: list of SampleStream
        """
        self.Metric = None
        self.Aggregation = None
        self.Unit = None
        self.Streams = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Aggregation = params.get("Aggregation")
        self.Unit = params.get("Unit")
        if params.get("Streams") is not None:
            self.Streams = []
            for item in params.get("Streams"):
                obj = SampleStream()
                obj._deserialize(item)
                self.Streams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DNSConfig(AbstractModel):
    """施压机 DNS 配置

    """

    def __init__(self):
        r"""
        :param Nameservers: DNS IP 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Nameservers: list of str
        """
        self.Nameservers = None


    def _deserialize(self, params):
        self.Nameservers = params.get("Nameservers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlertChannelRequest(AbstractModel):
    """DeleteAlertChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目 ID
        :type ProjectId: str
        :param NoticeId: Notice ID
        :type NoticeId: str
        """
        self.ProjectId = None
        self.NoticeId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.NoticeId = params.get("NoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlertChannelResponse(AbstractModel):
    """DeleteAlertChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCronJobsRequest(AbstractModel):
    """DeleteCronJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param CronJobIds: 定时任务ID数组
        :type CronJobIds: list of str
        """
        self.ProjectId = None
        self.CronJobIds = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CronJobIds = params.get("CronJobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCronJobsResponse(AbstractModel):
    """DeleteCronJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFilesRequest(AbstractModel):
    """DeleteFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目 ID
        :type ProjectId: str
        :param FileIds: 文件 ID 数组
        :type FileIds: list of str
        """
        self.ProjectId = None
        self.FileIds = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.FileIds = params.get("FileIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFilesResponse(AbstractModel):
    """DeleteFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteJobsRequest(AbstractModel):
    """DeleteJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobIds: 任务ID数组
        :type JobIds: list of str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        """
        self.JobIds = None
        self.ProjectId = None
        self.ScenarioIds = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioIds = params.get("ScenarioIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobsResponse(AbstractModel):
    """DeleteJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProjectsRequest(AbstractModel):
    """DeleteProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param DeleteScenarios: 是否删除项目相关的场景。默认为否。
        :type DeleteScenarios: bool
        :param DeleteJobs: 是否删除项目相关的任务。默认为否。
        :type DeleteJobs: bool
        """
        self.ProjectIds = None
        self.DeleteScenarios = None
        self.DeleteJobs = None


    def _deserialize(self, params):
        self.ProjectIds = params.get("ProjectIds")
        self.DeleteScenarios = params.get("DeleteScenarios")
        self.DeleteJobs = params.get("DeleteJobs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectsResponse(AbstractModel):
    """DeleteProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScenariosRequest(AbstractModel):
    """DeleteScenarios请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param DeleteJobs: 是否删除场景相关的任务。默认为否。
        :type DeleteJobs: bool
        """
        self.ScenarioIds = None
        self.ProjectId = None
        self.DeleteJobs = None


    def _deserialize(self, params):
        self.ScenarioIds = params.get("ScenarioIds")
        self.ProjectId = params.get("ProjectId")
        self.DeleteJobs = params.get("DeleteJobs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScenariosResponse(AbstractModel):
    """DeleteScenarios返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAlertChannelsRequest(AbstractModel):
    """DescribeAlertChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectIds: 项目 ID 列表
        :type ProjectIds: list of str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大为100
        :type Limit: int
        :param NoticeIds: Notice ID 列表
        :type NoticeIds: list of str
        :param OrderBy: 排序项
        :type OrderBy: str
        :param Ascend: 是否正序
        :type Ascend: bool
        """
        self.ProjectIds = None
        self.Offset = None
        self.Limit = None
        self.NoticeIds = None
        self.OrderBy = None
        self.Ascend = None


    def _deserialize(self, params):
        self.ProjectIds = params.get("ProjectIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NoticeIds = params.get("NoticeIds")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertChannelsResponse(AbstractModel):
    """DescribeAlertChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param AlertChannelSet: 告警通知接收组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertChannelSet: list of AlertChannelRecord
        :param Total: 告警通知接收组数目
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlertChannelSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlertChannelSet") is not None:
            self.AlertChannelSet = []
            for item in params.get("AlertChannelSet"):
                obj = AlertChannelRecord()
                obj._deserialize(item)
                self.AlertChannelSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAlertRecordsRequest(AbstractModel):
    """DescribeAlertRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectIds: 项目 ID 列表
        :type ProjectIds: list of str
        :param ScenarioIds: 场景 ID 列表
        :type ScenarioIds: list of str
        :param JobIds: 任务 ID 列表
        :type JobIds: list of str
        :param Ascend: 是否正序
        :type Ascend: bool
        :param OrderBy: 排序项
        :type OrderBy: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大为100
        :type Limit: int
        :param ScenarioNames: 按场景名筛选
        :type ScenarioNames: list of str
        """
        self.ProjectIds = None
        self.ScenarioIds = None
        self.JobIds = None
        self.Ascend = None
        self.OrderBy = None
        self.Offset = None
        self.Limit = None
        self.ScenarioNames = None


    def _deserialize(self, params):
        self.ProjectIds = params.get("ProjectIds")
        self.ScenarioIds = params.get("ScenarioIds")
        self.JobIds = params.get("JobIds")
        self.Ascend = params.get("Ascend")
        self.OrderBy = params.get("OrderBy")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ScenarioNames = params.get("ScenarioNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertRecordsResponse(AbstractModel):
    """DescribeAlertRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param AlertRecordSet: 告警历史
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRecordSet: list of AlertRecord
        :param Total: 告警历史记录的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlertRecordSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlertRecordSet") is not None:
            self.AlertRecordSet = []
            for item in params.get("AlertRecordSet"):
                obj = AlertRecord()
                obj._deserialize(item)
                self.AlertRecordSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAvailableMetricsRequest(AbstractModel):
    """DescribeAvailableMetrics请求参数结构体

    """


class DescribeAvailableMetricsResponse(AbstractModel):
    """DescribeAvailableMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricSet: 系统支持的所有指标
        :type MetricSet: list of MetricInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self.MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricInfo()
                obj._deserialize(item)
                self.MetricSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCheckSummaryRequest(AbstractModel):
    """DescribeCheckSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.JobId = None
        self.ScenarioId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ScenarioId = params.get("ScenarioId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckSummaryResponse(AbstractModel):
    """DescribeCheckSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckSummarySet: 检查点汇总信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckSummarySet: list of CheckSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckSummarySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CheckSummarySet") is not None:
            self.CheckSummarySet = []
            for item in params.get("CheckSummarySet"):
                obj = CheckSummary()
                obj._deserialize(item)
                self.CheckSummarySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCronJobsRequest(AbstractModel):
    """DescribeCronJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        :param CronJobIds: 定时任务ID数组
        :type CronJobIds: list of str
        :param CronJobName: 定时任务名字，模糊查询
        :type CronJobName: str
        :param CronJobStatus: 定时任务状态数组
        :type CronJobStatus: list of int
        :param OrderBy: 排序的列
        :type OrderBy: str
        :param Ascend: 是否正序
        :type Ascend: bool
        """
        self.ProjectIds = None
        self.Offset = None
        self.Limit = None
        self.CronJobIds = None
        self.CronJobName = None
        self.CronJobStatus = None
        self.OrderBy = None
        self.Ascend = None


    def _deserialize(self, params):
        self.ProjectIds = params.get("ProjectIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CronJobIds = params.get("CronJobIds")
        self.CronJobName = params.get("CronJobName")
        self.CronJobStatus = params.get("CronJobStatus")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCronJobsResponse(AbstractModel):
    """DescribeCronJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 定时任务总数
        :type Total: int
        :param CronJobSet: 定时任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CronJobSet: list of CronJob
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.CronJobSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("CronJobSet") is not None:
            self.CronJobSet = []
            for item in params.get("CronJobSet"):
                obj = CronJob()
                obj._deserialize(item)
                self.CronJobSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFilesRequest(AbstractModel):
    """DescribeFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectIds: 项目 ID 数组
        :type ProjectIds: list of str
        :param FileIds: 文件 ID 数组
        :type FileIds: list of str
        :param FileName: 文件名
        :type FileName: str
        :param Offset: 偏移量，默认为 0
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大为 100
        :type Limit: int
        :param Kind: 文件种类，参数文件-1，协议文件-2，请求文件-3
        :type Kind: int
        """
        self.ProjectIds = None
        self.FileIds = None
        self.FileName = None
        self.Offset = None
        self.Limit = None
        self.Kind = None


    def _deserialize(self, params):
        self.ProjectIds = params.get("ProjectIds")
        self.FileIds = params.get("FileIds")
        self.FileName = params.get("FileName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFilesResponse(AbstractModel):
    """DescribeFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileSet: 文件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSet: list of File
        :param Total: 文件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSet") is not None:
            self.FileSet = []
            for item in params.get("FileSet"):
                obj = File()
                obj._deserialize(item)
                self.FileSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        :param ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param Offset: 分页起始位置
        :type Offset: int
        :param Limit: 每页最大数目
        :type Limit: int
        :param JobIds: 任务ID数组
        :type JobIds: list of str
        :param OrderBy: 按字段排序
        :type OrderBy: str
        :param Ascend: 升序/降序
        :type Ascend: bool
        :param StartTime: 任务开始时间
        :type StartTime: str
        :param EndTime: 任务结束时间
        :type EndTime: str
        :param Debug: 调试任务标记
        :type Debug: bool
        :param Status: 任务的状态
        :type Status: list of int
        """
        self.ScenarioIds = None
        self.ProjectIds = None
        self.Offset = None
        self.Limit = None
        self.JobIds = None
        self.OrderBy = None
        self.Ascend = None
        self.StartTime = None
        self.EndTime = None
        self.Debug = None
        self.Status = None


    def _deserialize(self, params):
        self.ScenarioIds = params.get("ScenarioIds")
        self.ProjectIds = params.get("ProjectIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.JobIds = params.get("JobIds")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Debug = params.get("Debug")
        self.Status = params.get("Status")
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
        :param JobSet: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobSet: list of Job
        :param Total: 任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobSet") is not None:
            self.JobSet = []
            for item in params.get("JobSet"):
                obj = Job()
                obj._deserialize(item)
                self.JobSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeLabelValuesRequest(AbstractModel):
    """DescribeLabelValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param Metric: 指标名称
        :type Metric: str
        :param LabelName: 查询标签名称
        :type LabelName: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.JobId = None
        self.ScenarioId = None
        self.Metric = None
        self.LabelName = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ScenarioId = params.get("ScenarioId")
        self.Metric = params.get("Metric")
        self.LabelName = params.get("LabelName")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLabelValuesResponse(AbstractModel):
    """DescribeLabelValues返回参数结构体

    """

    def __init__(self):
        r"""
        :param LabelValueSet: 标签值数组
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValueSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LabelValueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LabelValueSet = params.get("LabelValueSet")
        self.RequestId = params.get("RequestId")


class DescribeMetricLabelWithValuesRequest(AbstractModel):
    """DescribeMetricLabelWithValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: job id
        :type JobId: str
        :param ProjectId: project id
        :type ProjectId: str
        :param ScenarioId: scenario id
        :type ScenarioId: str
        """
        self.JobId = None
        self.ProjectId = None
        self.ScenarioId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMetricLabelWithValuesResponse(AbstractModel):
    """DescribeMetricLabelWithValues返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricLabelWithValuesSet: 指标所有的label和values数组
        :type MetricLabelWithValuesSet: list of MetricLabelWithValues
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricLabelWithValuesSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricLabelWithValuesSet") is not None:
            self.MetricLabelWithValuesSet = []
            for item in params.get("MetricLabelWithValuesSet"):
                obj = MetricLabelWithValues()
                obj._deserialize(item)
                self.MetricLabelWithValuesSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNormalLogsRequest(AbstractModel):
    """DescribeNormalLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 压测项目ID
        :type ProjectId: str
        :param ScenarioId: 测试场景ID
        :type ScenarioId: str
        :param JobId: 压测任务ID
        :type JobId: str
        :param Context: 日志上下文，加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。过期时间1小时
        :type Context: str
        :param From: 日志开始时间
        :type From: str
        :param To: 日志结束时间
        :type To: str
        :param SeverityText: 日志级别，可取debug/info/error
        :type SeverityText: str
        :param Instance: 施压节点IP
        :type Instance: str
        :param InstanceRegion: 施压节点所在地域
        :type InstanceRegion: str
        :param LogType: 日志类型， console代表用户输出，engine代表引擎输出
        :type LogType: str
        :param Limit: 返回日志条数限制，最大100
        :type Limit: int
        """
        self.ProjectId = None
        self.ScenarioId = None
        self.JobId = None
        self.Context = None
        self.From = None
        self.To = None
        self.SeverityText = None
        self.Instance = None
        self.InstanceRegion = None
        self.LogType = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        self.JobId = params.get("JobId")
        self.Context = params.get("Context")
        self.From = params.get("From")
        self.To = params.get("To")
        self.SeverityText = params.get("SeverityText")
        self.Instance = params.get("Instance")
        self.InstanceRegion = params.get("InstanceRegion")
        self.LogType = params.get("LogType")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNormalLogsResponse(AbstractModel):
    """DescribeNormalLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 日志上下文，加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。过期时间1小时
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param NormalLogs: 日志数组
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalLogs: list of NormalLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.NormalLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        if params.get("NormalLogs") is not None:
            self.NormalLogs = []
            for item in params.get("NormalLogs"):
                obj = NormalLog()
                obj._deserialize(item)
                self.NormalLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页offset
        :type Offset: int
        :param Limit: 每页limit
        :type Limit: int
        :param ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param ProjectName: 项目名
        :type ProjectName: str
        :param OrderBy: 按字段排序
        :type OrderBy: str
        :param Ascend: 升序/降序
        :type Ascend: bool
        :param TagFilters: 标签数组
        :type TagFilters: list of TagSpec
        """
        self.Offset = None
        self.Limit = None
        self.ProjectIds = None
        self.ProjectName = None
        self.OrderBy = None
        self.Ascend = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectIds = params.get("ProjectIds")
        self.ProjectName = params.get("ProjectName")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagSpec()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectSet: 项目数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectSet: list of Project
        :param Total: 项目数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectSet") is not None:
            self.ProjectSet = []
            for item in params.get("ProjectSet"):
                obj = Project()
                obj._deserialize(item)
                self.ProjectSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionSet: 地域数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionSet: list of RegionDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRequestSummaryRequest(AbstractModel):
    """DescribeRequestSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 压测任务ID
        :type JobId: str
        :param ScenarioId: 压测场景ID
        :type ScenarioId: str
        :param ProjectId: 压测项目ID
        :type ProjectId: str
        """
        self.JobId = None
        self.ScenarioId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ScenarioId = params.get("ScenarioId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRequestSummaryResponse(AbstractModel):
    """DescribeRequestSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestSummarySet: 请求汇总信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestSummarySet: list of RequestSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestSummarySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RequestSummarySet") is not None:
            self.RequestSummarySet = []
            for item in params.get("RequestSummarySet"):
                obj = RequestSummary()
                obj._deserialize(item)
                self.RequestSummarySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleBatchQueryRequest(AbstractModel):
    """DescribeSampleBatchQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: job id
        :type JobId: str
        :param ScenarioId: 场景id
        :type ScenarioId: str
        :param Queries: 查询指标数组
        :type Queries: list of InternalMetricQuery
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.JobId = None
        self.ScenarioId = None
        self.Queries = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ScenarioId = params.get("ScenarioId")
        if params.get("Queries") is not None:
            self.Queries = []
            for item in params.get("Queries"):
                obj = InternalMetricQuery()
                obj._deserialize(item)
                self.Queries.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleBatchQueryResponse(AbstractModel):
    """DescribeSampleBatchQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricSampleSet: 返回指标内容
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricSampleSet: list of CustomSample
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSampleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSampleSet") is not None:
            self.MetricSampleSet = []
            for item in params.get("MetricSampleSet"):
                obj = CustomSample()
                obj._deserialize(item)
                self.MetricSampleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleLogsRequest(AbstractModel):
    """DescribeSampleLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 测试项目ID
        :type ProjectId: str
        :param ScenarioId: 测试场景ID
        :type ScenarioId: str
        :param JobId: 测试任务ID
        :type JobId: str
        :param Context: 加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。过期时间1小时
        :type Context: str
        :param From: 日志开始时间
        :type From: str
        :param To: 日志结束时间
        :type To: str
        :param SeverityText: 日志级别debug,info,error
        :type SeverityText: str
        :param InstanceRegion: ap-shanghai, ap-guangzhou
        :type InstanceRegion: str
        :param Instance: 施压引擎节点IP
        :type Instance: str
        :param LogType: request 代表采样日志,可为不填
        :type LogType: str
        :param Limit: 返回日志条数，最大100
        :type Limit: int
        :param ReactionTimeRange: 采样日志响应时间范围
        :type ReactionTimeRange: :class:`tencentcloud.pts.v20210728.models.ReactionTimeRange`
        :param Status: 采样请求状态码
        :type Status: str
        :param Result: 采样请求结果码
        :type Result: str
        :param Method: 采样请求方法
        :type Method: str
        :param Service: 采样服务API
        :type Service: str
        """
        self.ProjectId = None
        self.ScenarioId = None
        self.JobId = None
        self.Context = None
        self.From = None
        self.To = None
        self.SeverityText = None
        self.InstanceRegion = None
        self.Instance = None
        self.LogType = None
        self.Limit = None
        self.ReactionTimeRange = None
        self.Status = None
        self.Result = None
        self.Method = None
        self.Service = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        self.JobId = params.get("JobId")
        self.Context = params.get("Context")
        self.From = params.get("From")
        self.To = params.get("To")
        self.SeverityText = params.get("SeverityText")
        self.InstanceRegion = params.get("InstanceRegion")
        self.Instance = params.get("Instance")
        self.LogType = params.get("LogType")
        self.Limit = params.get("Limit")
        if params.get("ReactionTimeRange") is not None:
            self.ReactionTimeRange = ReactionTimeRange()
            self.ReactionTimeRange._deserialize(params.get("ReactionTimeRange"))
        self.Status = params.get("Status")
        self.Result = params.get("Result")
        self.Method = params.get("Method")
        self.Service = params.get("Service")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleLogsResponse(AbstractModel):
    """DescribeSampleLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 日志总数
        :type Total: int
        :param Context: 日志上下文，加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。过期时间1小时
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param SampleLogs: 采样日志数组
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleLogs: list of SampleLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Context = None
        self.SampleLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Context = params.get("Context")
        if params.get("SampleLogs") is not None:
            self.SampleLogs = []
            for item in params.get("SampleLogs"):
                obj = SampleLog()
                obj._deserialize(item)
                self.SampleLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleMatrixBatchQueryRequest(AbstractModel):
    """DescribeSampleMatrixBatchQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param Queries: 查询语句
        :type Queries: list of InternalMetricQuery
        """
        self.JobId = None
        self.ProjectId = None
        self.ScenarioId = None
        self.Queries = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        if params.get("Queries") is not None:
            self.Queries = []
            for item in params.get("Queries"):
                obj = InternalMetricQuery()
                obj._deserialize(item)
                self.Queries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleMatrixBatchQueryResponse(AbstractModel):
    """DescribeSampleMatrixBatchQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricSampleMatrixSet: 批量指标矩阵
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricSampleMatrixSet: list of CustomSampleMatrix
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSampleMatrixSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSampleMatrixSet") is not None:
            self.MetricSampleMatrixSet = []
            for item in params.get("MetricSampleMatrixSet"):
                obj = CustomSampleMatrix()
                obj._deserialize(item)
                self.MetricSampleMatrixSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleMatrixQueryRequest(AbstractModel):
    """DescribeSampleMatrixQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param Metric: 指标名字
        :type Metric: str
        :param Aggregation: 聚合函数
        :type Aggregation: str
        :param Filters: 指标过滤
        :type Filters: list of Filter
        :param GroupBy: 分组
        :type GroupBy: list of str
        """
        self.JobId = None
        self.ProjectId = None
        self.ScenarioId = None
        self.Metric = None
        self.Aggregation = None
        self.Filters = None
        self.GroupBy = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        self.Metric = params.get("Metric")
        self.Aggregation = params.get("Aggregation")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.GroupBy = params.get("GroupBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleMatrixQueryResponse(AbstractModel):
    """DescribeSampleMatrixQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricSampleMatrix: 指标矩阵
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricSampleMatrix: :class:`tencentcloud.pts.v20210728.models.CustomSampleMatrix`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSampleMatrix = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSampleMatrix") is not None:
            self.MetricSampleMatrix = CustomSampleMatrix()
            self.MetricSampleMatrix._deserialize(params.get("MetricSampleMatrix"))
        self.RequestId = params.get("RequestId")


class DescribeSampleQueryRequest(AbstractModel):
    """DescribeSampleQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: job id
        :type JobId: str
        :param ScenarioId: 场景Id
        :type ScenarioId: str
        :param Metric: 指标名
        :type Metric: str
        :param Aggregation: 聚合条件
        :type Aggregation: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Labels: 过滤条件
        :type Labels: list of Label
        """
        self.JobId = None
        self.ScenarioId = None
        self.Metric = None
        self.Aggregation = None
        self.ProjectId = None
        self.Labels = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ScenarioId = params.get("ScenarioId")
        self.Metric = params.get("Metric")
        self.Aggregation = params.get("Aggregation")
        self.ProjectId = params.get("ProjectId")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleQueryResponse(AbstractModel):
    """DescribeSampleQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricSample: 返回指标内容
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricSample: :class:`tencentcloud.pts.v20210728.models.CustomSample`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSample = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSample") is not None:
            self.MetricSample = CustomSample()
            self.MetricSample._deserialize(params.get("MetricSample"))
        self.RequestId = params.get("RequestId")


class DescribeScenarioWithJobsRequest(AbstractModel):
    """DescribeScenarioWithJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大为100
        :type Limit: int
        :param ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        :param ScenarioName: 场景名
        :type ScenarioName: str
        :param ScenarioStatus: 场景状态数组
        :type ScenarioStatus: int
        :param OrderBy: 排序的列
        :type OrderBy: str
        :param Ascend: 是否正序
        :type Ascend: bool
        :param ScenarioRelatedJobsParams: job相关参数
        :type ScenarioRelatedJobsParams: :class:`tencentcloud.pts.v20210728.models.ScenarioRelatedJobsParams`
        :param IgnoreScript: 是否需要返回场景的脚本内容
        :type IgnoreScript: bool
        """
        self.Offset = None
        self.Limit = None
        self.ProjectIds = None
        self.ScenarioIds = None
        self.ScenarioName = None
        self.ScenarioStatus = None
        self.OrderBy = None
        self.Ascend = None
        self.ScenarioRelatedJobsParams = None
        self.IgnoreScript = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectIds = params.get("ProjectIds")
        self.ScenarioIds = params.get("ScenarioIds")
        self.ScenarioName = params.get("ScenarioName")
        self.ScenarioStatus = params.get("ScenarioStatus")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        if params.get("ScenarioRelatedJobsParams") is not None:
            self.ScenarioRelatedJobsParams = ScenarioRelatedJobsParams()
            self.ScenarioRelatedJobsParams._deserialize(params.get("ScenarioRelatedJobsParams"))
        self.IgnoreScript = params.get("IgnoreScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenarioWithJobsResponse(AbstractModel):
    """DescribeScenarioWithJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioWithJobsSet: 场景配置以及附带的job内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioWithJobsSet: list of ScenarioWithJobs
        :param Total: 场景总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScenarioWithJobsSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScenarioWithJobsSet") is not None:
            self.ScenarioWithJobsSet = []
            for item in params.get("ScenarioWithJobsSet"):
                obj = ScenarioWithJobs()
                obj._deserialize(item)
                self.ScenarioWithJobsSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeScenariosRequest(AbstractModel):
    """DescribeScenarios请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        :param ScenarioName: 场景名
        :type ScenarioName: str
        :param ScenarioStatus: 场景状态数组
        :type ScenarioStatus: list of int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大为100
        :type Limit: int
        :param OrderBy: 排序的列
        :type OrderBy: str
        :param Ascend: 是否正序
        :type Ascend: bool
        :param ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param ScenarioType: 场景类型
        :type ScenarioType: str
        """
        self.ScenarioIds = None
        self.ScenarioName = None
        self.ScenarioStatus = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.Ascend = None
        self.ProjectIds = None
        self.ScenarioType = None


    def _deserialize(self, params):
        self.ScenarioIds = params.get("ScenarioIds")
        self.ScenarioName = params.get("ScenarioName")
        self.ScenarioStatus = params.get("ScenarioStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        self.ProjectIds = params.get("ProjectIds")
        self.ScenarioType = params.get("ScenarioType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenariosResponse(AbstractModel):
    """DescribeScenarios返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioSet: 场景列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioSet: list of Scenario
        :param Total: 场景总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScenarioSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScenarioSet") is not None:
            self.ScenarioSet = []
            for item in params.get("ScenarioSet"):
                obj = Scenario()
                obj._deserialize(item)
                self.ScenarioSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DomainNameConfig(AbstractModel):
    """施压机的域名解析相关配置

    """

    def __init__(self):
        r"""
        :param HostAliases: 域名绑定配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HostAliases: list of HostAlias
        :param DNSConfig: DNS 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DNSConfig: :class:`tencentcloud.pts.v20210728.models.DNSConfig`
        """
        self.HostAliases = None
        self.DNSConfig = None


    def _deserialize(self, params):
        if params.get("HostAliases") is not None:
            self.HostAliases = []
            for item in params.get("HostAliases"):
                obj = HostAlias()
                obj._deserialize(item)
                self.HostAliases.append(obj)
        if params.get("DNSConfig") is not None:
            self.DNSConfig = DNSConfig()
            self.DNSConfig._deserialize(params.get("DNSConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class File(AbstractModel):
    """文件列表

    """

    def __init__(self):
        r"""
        :param FileId: 文件 ID
        :type FileId: str
        :param Kind: 文件种类，参数文件-1，协议文件-2，请求文件-3
        :type Kind: int
        :param Name: 文件名
        :type Name: str
        :param Size: 文件字节数
        :type Size: int
        :param Type: 文件类型
        :type Type: str
        :param UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param LineCount: 文件行数
注意：此字段可能返回 null，表示取不到有效值。
        :type LineCount: int
        :param HeadLines: 头部数据行
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadLines: list of str
        :param TailLines: 尾部数据行
注意：此字段可能返回 null，表示取不到有效值。
        :type TailLines: list of str
        :param HeaderInFile: 首行是否为参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderInFile: bool
        :param HeaderColumns: 参数名数组
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderColumns: list of str
        :param FileInfos: 文件夹中的文件
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfos: list of FileInfo
        :param ScenarioSet: 关联场景
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioSet: list of Scenario
        :param Status: 文件状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.FileId = None
        self.Kind = None
        self.Name = None
        self.Size = None
        self.Type = None
        self.UpdatedAt = None
        self.LineCount = None
        self.HeadLines = None
        self.TailLines = None
        self.HeaderInFile = None
        self.HeaderColumns = None
        self.FileInfos = None
        self.ScenarioSet = None
        self.Status = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Kind = params.get("Kind")
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Type = params.get("Type")
        self.UpdatedAt = params.get("UpdatedAt")
        self.LineCount = params.get("LineCount")
        self.HeadLines = params.get("HeadLines")
        self.TailLines = params.get("TailLines")
        self.HeaderInFile = params.get("HeaderInFile")
        self.HeaderColumns = params.get("HeaderColumns")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("ScenarioSet") is not None:
            self.ScenarioSet = []
            for item in params.get("ScenarioSet"):
                obj = Scenario()
                obj._deserialize(item)
                self.ScenarioSet.append(obj)
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """文件基本信息

    """

    def __init__(self):
        r"""
        :param Name: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Size: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Type: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param FileId: 文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        """
        self.Name = None
        self.Size = None
        self.Type = None
        self.UpdatedAt = None
        self.FileId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Type = params.get("Type")
        self.UpdatedAt = params.get("UpdatedAt")
        self.FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """指标查询过滤

    """

    def __init__(self):
        r"""
        :param Operator: 等于：0，不等于：1
        :type Operator: int
        :param LabelName: 指标名
        :type LabelName: str
        :param LabelValue: 指标值
        :type LabelValue: str
        """
        self.Operator = None
        self.LabelName = None
        self.LabelValue = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.LabelName = params.get("LabelName")
        self.LabelValue = params.get("LabelValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateTmpKeyRequest(AbstractModel):
    """GenerateTmpKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        """
        self.ProjectId = None
        self.ScenarioId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateTmpKeyResponse(AbstractModel):
    """GenerateTmpKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 临时访问凭证获取时刻的时间戳（单位秒）
        :type StartTime: int
        :param ExpiredTime: 临时访问凭证超时 时刻的时间戳（单位秒）
        :type ExpiredTime: int
        :param Credentials: 临时访问凭证
        :type Credentials: :class:`tencentcloud.pts.v20210728.models.Credentials`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StartTime = None
        self.ExpiredTime = None
        self.Credentials = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.RequestId = params.get("RequestId")


class GeoRegionsLoadItem(AbstractModel):
    """压力分布配置

    """

    def __init__(self):
        r"""
        :param RegionId: 地域ID
        :type RegionId: int
        :param Region: 地域
        :type Region: str
        :param Percentage: 百分比
        :type Percentage: int
        """
        self.RegionId = None
        self.Region = None
        self.Percentage = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Region = params.get("Region")
        self.Percentage = params.get("Percentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostAlias(AbstractModel):
    """施压机域名绑定配置

    """

    def __init__(self):
        r"""
        :param HostNames: 需绑定的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type HostNames: list of str
        :param IP: 需绑定的 IP 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        """
        self.HostNames = None
        self.IP = None


    def _deserialize(self, params):
        self.HostNames = params.get("HostNames")
        self.IP = params.get("IP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternalMetricQuery(AbstractModel):
    """查询结构封装

    """

    def __init__(self):
        r"""
        :param Metric: 指标名
        :type Metric: str
        :param Aggregation: 聚合函数
        :type Aggregation: str
        :param Labels: deprecated, 请使用Filters
        :type Labels: list of Label
        :param Filters: 指标过滤
        :type Filters: list of Filter
        :param GroupBy: 指标分组
        :type GroupBy: list of str
        """
        self.Metric = None
        self.Aggregation = None
        self.Labels = None
        self.Filters = None
        self.GroupBy = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Aggregation = params.get("Aggregation")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.GroupBy = params.get("GroupBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """任务

    """

    def __init__(self):
        r"""
        :param JobId: 任务的JobID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param ScenarioId: 任务的场景ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioId: str
        :param Load: 任务的施压配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Load: :class:`tencentcloud.pts.v20210728.models.Load`
        :param Configs: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of str
        :param Datasets: 任务的数据集文件
注意：此字段可能返回 null，表示取不到有效值。
        :type Datasets: list of TestData
        :param Extensions: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type Extensions: list of str
        :param Status: 任务的运行状态, JobUnknown: 0,JobCreated:1,JobPending:2, JobPreparing:3,JobSelectClustering:4,JobCreateTasking:5,JobSyncTasking:6
JobRunning:11,JobFinished:12,JobPrepareException:13,JobFinishException:14,JobAborting:15,JobAborted:16,JobAbortException:17,JobDeleted:18,
JobSelectClusterException:19,JobCreateTaskException:20,JobSyncTaskException:21
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param StartTime: 任务的开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 任务的结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param MaxVirtualUserCount: 任务的最大VU数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxVirtualUserCount: int
        :param Note: 任务的备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param ErrorRate: 错误率百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorRate: float
        :param JobOwner: 任务发起人
注意：此字段可能返回 null，表示取不到有效值。
        :type JobOwner: str
        :param LoadSources: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadSources: :class:`tencentcloud.pts.v20210728.models.LoadSource`
        :param Duration: 任务时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param MaxRequestsPerSecond: 最大每秒请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestsPerSecond: int
        :param RequestTotal: 总请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestTotal: float
        :param RequestsPerSecond: 平均每秒请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestsPerSecond: float
        :param ResponseTimeAverage: 平均响应时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeAverage: float
        :param ResponseTimeP99: 响应时间第99百分位
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeP99: float
        :param ResponseTimeP95: 响应时间第95百分位
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeP95: float
        :param ResponseTimeP90: 响应时间第90百分位
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeP90: float
        :param Scripts: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type Scripts: list of str
        :param ResponseTimeMax: 最大响应时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeMax: float
        :param ResponseTimeMin: 最小响应时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeMin: float
        :param LoadSourceInfos: 发压host信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadSourceInfos: list of LoadSource
        :param TestScripts: 测试脚本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TestScripts: list of ScriptInfo
        :param Protocols: 协议脚本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocols: list of ProtocolInfo
        :param RequestFiles: 请求文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestFiles: list of FileInfo
        :param Plugins: 拓展包文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Plugins: list of FileInfo
        :param CronId: 定时任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CronId: str
        """
        self.JobId = None
        self.ScenarioId = None
        self.Load = None
        self.Configs = None
        self.Datasets = None
        self.Extensions = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.MaxVirtualUserCount = None
        self.Note = None
        self.ErrorRate = None
        self.JobOwner = None
        self.LoadSources = None
        self.Duration = None
        self.MaxRequestsPerSecond = None
        self.RequestTotal = None
        self.RequestsPerSecond = None
        self.ResponseTimeAverage = None
        self.ResponseTimeP99 = None
        self.ResponseTimeP95 = None
        self.ResponseTimeP90 = None
        self.Scripts = None
        self.ResponseTimeMax = None
        self.ResponseTimeMin = None
        self.LoadSourceInfos = None
        self.TestScripts = None
        self.Protocols = None
        self.RequestFiles = None
        self.Plugins = None
        self.CronId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ScenarioId = params.get("ScenarioId")
        if params.get("Load") is not None:
            self.Load = Load()
            self.Load._deserialize(params.get("Load"))
        self.Configs = params.get("Configs")
        if params.get("Datasets") is not None:
            self.Datasets = []
            for item in params.get("Datasets"):
                obj = TestData()
                obj._deserialize(item)
                self.Datasets.append(obj)
        self.Extensions = params.get("Extensions")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MaxVirtualUserCount = params.get("MaxVirtualUserCount")
        self.Note = params.get("Note")
        self.ErrorRate = params.get("ErrorRate")
        self.JobOwner = params.get("JobOwner")
        if params.get("LoadSources") is not None:
            self.LoadSources = LoadSource()
            self.LoadSources._deserialize(params.get("LoadSources"))
        self.Duration = params.get("Duration")
        self.MaxRequestsPerSecond = params.get("MaxRequestsPerSecond")
        self.RequestTotal = params.get("RequestTotal")
        self.RequestsPerSecond = params.get("RequestsPerSecond")
        self.ResponseTimeAverage = params.get("ResponseTimeAverage")
        self.ResponseTimeP99 = params.get("ResponseTimeP99")
        self.ResponseTimeP95 = params.get("ResponseTimeP95")
        self.ResponseTimeP90 = params.get("ResponseTimeP90")
        self.Scripts = params.get("Scripts")
        self.ResponseTimeMax = params.get("ResponseTimeMax")
        self.ResponseTimeMin = params.get("ResponseTimeMin")
        if params.get("LoadSourceInfos") is not None:
            self.LoadSourceInfos = []
            for item in params.get("LoadSourceInfos"):
                obj = LoadSource()
                obj._deserialize(item)
                self.LoadSourceInfos.append(obj)
        if params.get("TestScripts") is not None:
            self.TestScripts = []
            for item in params.get("TestScripts"):
                obj = ScriptInfo()
                obj._deserialize(item)
                self.TestScripts.append(obj)
        if params.get("Protocols") is not None:
            self.Protocols = []
            for item in params.get("Protocols"):
                obj = ProtocolInfo()
                obj._deserialize(item)
                self.Protocols.append(obj)
        if params.get("RequestFiles") is not None:
            self.RequestFiles = []
            for item in params.get("RequestFiles"):
                obj = FileInfo()
                obj._deserialize(item)
                self.RequestFiles.append(obj)
        if params.get("Plugins") is not None:
            self.Plugins = []
            for item in params.get("Plugins"):
                obj = FileInfo()
                obj._deserialize(item)
                self.Plugins.append(obj)
        self.CronId = params.get("CronId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """包含labelName 和labelValue

    """

    def __init__(self):
        r"""
        :param LabelName: label名字
        :type LabelName: str
        :param LabelValue: label值
        :type LabelValue: str
        """
        self.LabelName = None
        self.LabelValue = None


    def _deserialize(self, params):
        self.LabelName = params.get("LabelName")
        self.LabelValue = params.get("LabelValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LabelWithValues(AbstractModel):
    """标签及对应的值

    """

    def __init__(self):
        r"""
        :param LabelName: 标签名称
        :type LabelName: str
        :param LabelValues: 标签值
        :type LabelValues: list of str
        """
        self.LabelName = None
        self.LabelValues = None


    def _deserialize(self, params):
        self.LabelName = params.get("LabelName")
        self.LabelValues = params.get("LabelValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Load(AbstractModel):
    """施压配置

    """

    def __init__(self):
        r"""
        :param LoadSpec: 施压配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadSpec: :class:`tencentcloud.pts.v20210728.models.LoadSpec`
        :param VpcLoadDistribution: 压力来源
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcLoadDistribution: :class:`tencentcloud.pts.v20210728.models.VpcLoadDistribution`
        :param GeoRegionsLoadDistribution: 压力分布
注意：此字段可能返回 null，表示取不到有效值。
        :type GeoRegionsLoadDistribution: list of GeoRegionsLoadItem
        """
        self.LoadSpec = None
        self.VpcLoadDistribution = None
        self.GeoRegionsLoadDistribution = None


    def _deserialize(self, params):
        if params.get("LoadSpec") is not None:
            self.LoadSpec = LoadSpec()
            self.LoadSpec._deserialize(params.get("LoadSpec"))
        if params.get("VpcLoadDistribution") is not None:
            self.VpcLoadDistribution = VpcLoadDistribution()
            self.VpcLoadDistribution._deserialize(params.get("VpcLoadDistribution"))
        if params.get("GeoRegionsLoadDistribution") is not None:
            self.GeoRegionsLoadDistribution = []
            for item in params.get("GeoRegionsLoadDistribution"):
                obj = GeoRegionsLoadItem()
                obj._deserialize(item)
                self.GeoRegionsLoadDistribution.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadSource(AbstractModel):
    """发压host来源

    """

    def __init__(self):
        r"""
        :param IP: 发压host的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param PodName: 发压host所在的pod
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param Region: 所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self.IP = None
        self.PodName = None
        self.Region = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.PodName = params.get("PodName")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadSpec(AbstractModel):
    """施压配置

    """

    def __init__(self):
        r"""
        :param Concurrency: 并发施压模式的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Concurrency: :class:`tencentcloud.pts.v20210728.models.Concurrency`
        :param RequestsPerSecond: RPS施压模式的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestsPerSecond: :class:`tencentcloud.pts.v20210728.models.RequestsPerSecond`
        :param ScriptOrigin: 脚本内置压力模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptOrigin: :class:`tencentcloud.pts.v20210728.models.ScriptOrigin`
        """
        self.Concurrency = None
        self.RequestsPerSecond = None
        self.ScriptOrigin = None


    def _deserialize(self, params):
        if params.get("Concurrency") is not None:
            self.Concurrency = Concurrency()
            self.Concurrency._deserialize(params.get("Concurrency"))
        if params.get("RequestsPerSecond") is not None:
            self.RequestsPerSecond = RequestsPerSecond()
            self.RequestsPerSecond._deserialize(params.get("RequestsPerSecond"))
        if params.get("ScriptOrigin") is not None:
            self.ScriptOrigin = ScriptOrigin()
            self.ScriptOrigin._deserialize(params.get("ScriptOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricInfo(AbstractModel):
    """指标结构

    """

    def __init__(self):
        r"""
        :param Metric: 后台指标
        :type Metric: str
        :param Alias: 前台展示指标名称
        :type Alias: str
        :param Description: 指标描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param MetricType: 指标类型
        :type MetricType: str
        :param Unit: 默认指标单位
        :type Unit: str
        :param Aggregations: 指标支持的聚合函数
        :type Aggregations: list of AggregationLegend
        :param InnerMetric: 是否内部指标，内部指标不可在前台提供用户自由选择
        :type InnerMetric: bool
        """
        self.Metric = None
        self.Alias = None
        self.Description = None
        self.MetricType = None
        self.Unit = None
        self.Aggregations = None
        self.InnerMetric = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Alias = params.get("Alias")
        self.Description = params.get("Description")
        self.MetricType = params.get("MetricType")
        self.Unit = params.get("Unit")
        if params.get("Aggregations") is not None:
            self.Aggregations = []
            for item in params.get("Aggregations"):
                obj = AggregationLegend()
                obj._deserialize(item)
                self.Aggregations.append(obj)
        self.InnerMetric = params.get("InnerMetric")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricLabelWithValues(AbstractModel):
    """PTS提供的指标名，指标对应的labels及values

    """

    def __init__(self):
        r"""
        :param MetricName: metric 名字
        :type MetricName: str
        :param LabelValuesSet: label及values 数组
        :type LabelValuesSet: list of LabelWithValues
        """
        self.MetricName = None
        self.LabelValuesSet = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("LabelValuesSet") is not None:
            self.LabelValuesSet = []
            for item in params.get("LabelValuesSet"):
                obj = LabelWithValues()
                obj._deserialize(item)
                self.LabelValuesSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalLog(AbstractModel):
    """通用日志

    """

    def __init__(self):
        r"""
        :param Timestamp: 毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param SeverityText: 日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type SeverityText: str
        :param Body: 日志输出内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        """
        self.Timestamp = None
        self.SeverityText = None
        self.Body = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.SeverityText = params.get("SeverityText")
        self.Body = params.get("Body")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Project(AbstractModel):
    """项目

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Name: 项目名
        :type Name: str
        :param Description: 项目描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Tags: 标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagSpec
        :param Status: 项目状态
        :type Status: int
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param UpdatedAt: 修改时间
        :type UpdatedAt: str
        :param AppId: App ID
        :type AppId: int
        :param Uin: 用户ID
        :type Uin: str
        :param SubAccountUin: 子用户ID
        :type SubAccountUin: str
        """
        self.ProjectId = None
        self.Name = None
        self.Description = None
        self.Tags = None
        self.Status = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.AppId = None
        self.Uin = None
        self.SubAccountUin = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagSpec()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.SubAccountUin = params.get("SubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolInfo(AbstractModel):
    """协议文件详情

    """

    def __init__(self):
        r"""
        :param Name: 协议详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Size: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Type: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param FileId: 文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        """
        self.Name = None
        self.Size = None
        self.Type = None
        self.UpdatedAt = None
        self.FileId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Type = params.get("Type")
        self.UpdatedAt = params.get("UpdatedAt")
        self.FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReactionTimeRange(AbstractModel):
    """采用日志响应时间RT范围

    """

    def __init__(self):
        r"""
        :param Min: 最小响应时间，单位ms
        :type Min: str
        :param Max: 最大响应时间，单位ms
        :type Max: str
        """
        self.Min = None
        self.Max = None


    def _deserialize(self, params):
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionDetail(AbstractModel):
    """地域

    """

    def __init__(self):
        r"""
        :param Region: 地域代码
        :type Region: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param Area: 地域所在的地区
        :type Area: str
        :param RegionName: 地域名称
        :type RegionName: str
        :param RegionState: 地域状态
        :type RegionState: int
        :param RegionShortName: 地域简称
        :type RegionShortName: str
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
        :type UpdatedAt: str
        """
        self.Region = None
        self.RegionId = None
        self.Area = None
        self.RegionName = None
        self.RegionState = None
        self.RegionShortName = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.Area = params.get("Area")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")
        self.RegionShortName = params.get("RegionShortName")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestSummary(AbstractModel):
    """压测请求明细

    """

    def __init__(self):
        r"""
        :param Service: 请求URL
        :type Service: str
        :param Method: 请求方法
        :type Method: str
        :param Count: 请求次数
        :type Count: int
        :param Average: 请求响应平均耗时，单位秒
        :type Average: float
        :param P90: 请求p90耗时，单位秒
        :type P90: float
        :param P95: 请求p95耗时，单位秒
        :type P95: float
        :param Min: 请求最小耗时，单位秒
        :type Min: float
        :param Max: 请求最大耗时，单位秒
        :type Max: float
        :param ErrorPercentage: 请求错误率
        :type ErrorPercentage: float
        """
        self.Service = None
        self.Method = None
        self.Count = None
        self.Average = None
        self.P90 = None
        self.P95 = None
        self.Min = None
        self.Max = None
        self.ErrorPercentage = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.Method = params.get("Method")
        self.Count = params.get("Count")
        self.Average = params.get("Average")
        self.P90 = params.get("P90")
        self.P95 = params.get("P95")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.ErrorPercentage = params.get("ErrorPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestsPerSecond(AbstractModel):
    """RPS模式的施压配置

    """

    def __init__(self):
        r"""
        :param MaxRequestsPerSecond: 最大RPS
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestsPerSecond: int
        :param DurationSeconds: 施压时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationSeconds: int
        :param TargetVirtualUsers: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetVirtualUsers: int
        :param Resources: 资源数
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: int
        :param StartRequestsPerSecond: 起始RPS
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRequestsPerSecond: int
        :param TargetRequestsPerSecond: 目标RPS，入参无效
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetRequestsPerSecond: int
        """
        self.MaxRequestsPerSecond = None
        self.DurationSeconds = None
        self.TargetVirtualUsers = None
        self.Resources = None
        self.StartRequestsPerSecond = None
        self.TargetRequestsPerSecond = None


    def _deserialize(self, params):
        self.MaxRequestsPerSecond = params.get("MaxRequestsPerSecond")
        self.DurationSeconds = params.get("DurationSeconds")
        self.TargetVirtualUsers = params.get("TargetVirtualUsers")
        self.Resources = params.get("Resources")
        self.StartRequestsPerSecond = params.get("StartRequestsPerSecond")
        self.TargetRequestsPerSecond = params.get("TargetRequestsPerSecond")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartCronJobsRequest(AbstractModel):
    """RestartCronJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param CronJobIds: 定时任务ID数组
        :type CronJobIds: list of str
        """
        self.ProjectId = None
        self.CronJobIds = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CronJobIds = params.get("CronJobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartCronJobsResponse(AbstractModel):
    """RestartCronJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SLALabel(AbstractModel):
    """SLA 标签

    """

    def __init__(self):
        r"""
        :param LabelName: 标签名
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelName: str
        :param LabelValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        """
        self.LabelName = None
        self.LabelValue = None


    def _deserialize(self, params):
        self.LabelName = params.get("LabelName")
        self.LabelValue = params.get("LabelValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SLAPolicy(AbstractModel):
    """SLA 策略

    """

    def __init__(self):
        r"""
        :param SLARules: SLA 规则
注意：此字段可能返回 null，表示取不到有效值。
        :type SLARules: list of SLARule
        :param AlertChannel: 告警通知渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertChannel: :class:`tencentcloud.pts.v20210728.models.AlertChannel`
        """
        self.SLARules = None
        self.AlertChannel = None


    def _deserialize(self, params):
        if params.get("SLARules") is not None:
            self.SLARules = []
            for item in params.get("SLARules"):
                obj = SLARule()
                obj._deserialize(item)
                self.SLARules.append(obj)
        if params.get("AlertChannel") is not None:
            self.AlertChannel = AlertChannel()
            self.AlertChannel._deserialize(params.get("AlertChannel"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SLARule(AbstractModel):
    """SLA 规则

    """

    def __init__(self):
        r"""
        :param Metric: 压测指标
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param Aggregation: 压测指标聚合方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Aggregation: str
        :param Condition: 压测指标条件判断符号
注意：此字段可能返回 null，表示取不到有效值。
        :type Condition: str
        :param Value: 阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        :param LabelFilter: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelFilter: list of SLALabel
        :param AbortFlag: 是否停止压测任务
注意：此字段可能返回 null，表示取不到有效值。
        :type AbortFlag: bool
        :param For: 持续时长
注意：此字段可能返回 null，表示取不到有效值。
        :type For: str
        """
        self.Metric = None
        self.Aggregation = None
        self.Condition = None
        self.Value = None
        self.LabelFilter = None
        self.AbortFlag = None
        self.For = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Aggregation = params.get("Aggregation")
        self.Condition = params.get("Condition")
        self.Value = params.get("Value")
        if params.get("LabelFilter") is not None:
            self.LabelFilter = []
            for item in params.get("LabelFilter"):
                obj = SLALabel()
                obj._deserialize(item)
                self.LabelFilter.append(obj)
        self.AbortFlag = params.get("AbortFlag")
        self.For = params.get("For")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleLog(AbstractModel):
    """采样日志

    """

    def __init__(self):
        r"""
        :param Timestamp: 日志毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Attributes: 采样日志属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Attributes: :class:`tencentcloud.pts.v20210728.models.Attributes`
        :param Body: har格式的采样请求
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        """
        self.Timestamp = None
        self.Attributes = None
        self.Body = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        if params.get("Attributes") is not None:
            self.Attributes = Attributes()
            self.Attributes._deserialize(params.get("Attributes"))
        self.Body = params.get("Body")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SamplePair(AbstractModel):
    """sample采样值

    """

    def __init__(self):
        r"""
        :param Timestamp: is the number of milliseconds since the epoch (1970-01-01 00:00 UTC) excluding leap seconds.
        :type Timestamp: int
        :param Value: is a representation of a value for a given sample at a given time.
        :type Value: float
        """
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleStream(AbstractModel):
    """连续指标采样内容

    """

    def __init__(self):
        r"""
        :param Labels: labels描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        :param Values: 指标采样数组
        :type Values: list of SamplePair
        :param Name: 指标序列名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Labels = None
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = SamplePair()
                obj._deserialize(item)
                self.Values.append(obj)
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Scenario(AbstractModel):
    """场景列表

    """

    def __init__(self):
        r"""
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param Name: 场景名
        :type Name: str
        :param Description: 场景描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Type: 场景类型，如pts-http, pts-js, pts-trpc, pts-jmeter
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Status: 场景状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Load: 施压配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Load: :class:`tencentcloud.pts.v20210728.models.Load`
        :param EncodedScripts: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type EncodedScripts: str
        :param Configs: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of str
        :param Extensions: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type Extensions: list of str
        :param Datasets: 测试数据集
注意：此字段可能返回 null，表示取不到有效值。
        :type Datasets: list of TestData
        :param SLAId: SLA规则的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SLAId: str
        :param CronId: Cron Job规则的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CronId: str
        :param CreatedAt: 场景创建时间
        :type CreatedAt: str
        :param UpdatedAt: 场景修改时间
        :type UpdatedAt: str
        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param AppId: App ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param Uin: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param SubAccountUin: 子用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param TestScripts: 测试脚本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TestScripts: list of ScriptInfo
        :param Protocols: 协议文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocols: list of ProtocolInfo
        :param RequestFiles: 请求文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestFiles: list of FileInfo
        :param SLAPolicy: SLA 策略
注意：此字段可能返回 null，表示取不到有效值。
        :type SLAPolicy: :class:`tencentcloud.pts.v20210728.models.SLAPolicy`
        :param Plugins: 扩展包信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Plugins: list of FileInfo
        :param DomainNameConfig: 域名解析配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainNameConfig: :class:`tencentcloud.pts.v20210728.models.DomainNameConfig`
        """
        self.ScenarioId = None
        self.Name = None
        self.Description = None
        self.Type = None
        self.Status = None
        self.Load = None
        self.EncodedScripts = None
        self.Configs = None
        self.Extensions = None
        self.Datasets = None
        self.SLAId = None
        self.CronId = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.ProjectId = None
        self.AppId = None
        self.Uin = None
        self.SubAccountUin = None
        self.TestScripts = None
        self.Protocols = None
        self.RequestFiles = None
        self.SLAPolicy = None
        self.Plugins = None
        self.DomainNameConfig = None


    def _deserialize(self, params):
        self.ScenarioId = params.get("ScenarioId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        if params.get("Load") is not None:
            self.Load = Load()
            self.Load._deserialize(params.get("Load"))
        self.EncodedScripts = params.get("EncodedScripts")
        self.Configs = params.get("Configs")
        self.Extensions = params.get("Extensions")
        if params.get("Datasets") is not None:
            self.Datasets = []
            for item in params.get("Datasets"):
                obj = TestData()
                obj._deserialize(item)
                self.Datasets.append(obj)
        self.SLAId = params.get("SLAId")
        self.CronId = params.get("CronId")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.ProjectId = params.get("ProjectId")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.SubAccountUin = params.get("SubAccountUin")
        if params.get("TestScripts") is not None:
            self.TestScripts = []
            for item in params.get("TestScripts"):
                obj = ScriptInfo()
                obj._deserialize(item)
                self.TestScripts.append(obj)
        if params.get("Protocols") is not None:
            self.Protocols = []
            for item in params.get("Protocols"):
                obj = ProtocolInfo()
                obj._deserialize(item)
                self.Protocols.append(obj)
        if params.get("RequestFiles") is not None:
            self.RequestFiles = []
            for item in params.get("RequestFiles"):
                obj = FileInfo()
                obj._deserialize(item)
                self.RequestFiles.append(obj)
        if params.get("SLAPolicy") is not None:
            self.SLAPolicy = SLAPolicy()
            self.SLAPolicy._deserialize(params.get("SLAPolicy"))
        if params.get("Plugins") is not None:
            self.Plugins = []
            for item in params.get("Plugins"):
                obj = FileInfo()
                obj._deserialize(item)
                self.Plugins.append(obj)
        if params.get("DomainNameConfig") is not None:
            self.DomainNameConfig = DomainNameConfig()
            self.DomainNameConfig._deserialize(params.get("DomainNameConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScenarioRelatedJobsParams(AbstractModel):
    """查询与特定scenario关联的job的参数

    """

    def __init__(self):
        r"""
        :param Offset: job偏移量
        :type Offset: int
        :param Limit: 限制最多查询的job数
        :type Limit: int
        :param OrderBy: 排序字段
        :type OrderBy: str
        :param Ascend: 是否升序
        :type Ascend: bool
        """
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.Ascend = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScenarioWithJobs(AbstractModel):
    """带已执行任务的scenario

    """

    def __init__(self):
        r"""
        :param Scenario: scecario结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Scenario: :class:`tencentcloud.pts.v20210728.models.Scenario`
        :param Jobs: job结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Jobs: list of Job
        """
        self.Scenario = None
        self.Jobs = None


    def _deserialize(self, params):
        if params.get("Scenario") is not None:
            self.Scenario = Scenario()
            self.Scenario._deserialize(params.get("Scenario"))
        if params.get("Jobs") is not None:
            self.Jobs = []
            for item in params.get("Jobs"):
                obj = Job()
                obj._deserialize(item)
                self.Jobs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScriptInfo(AbstractModel):
    """脚本信息

    """

    def __init__(self):
        r"""
        :param Name: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Size: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Type: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param EncodedContent: base64编码后的文件内容
注意：此字段可能返回 null，表示取不到有效值。
        :type EncodedContent: str
        :param EncodedHttpArchive: base64编码后的har结构体
注意：此字段可能返回 null，表示取不到有效值。
        :type EncodedHttpArchive: str
        :param LoadWeight: 脚本权重，范围 1-100
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadWeight: int
        """
        self.Name = None
        self.Size = None
        self.Type = None
        self.UpdatedAt = None
        self.EncodedContent = None
        self.EncodedHttpArchive = None
        self.LoadWeight = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Type = params.get("Type")
        self.UpdatedAt = params.get("UpdatedAt")
        self.EncodedContent = params.get("EncodedContent")
        self.EncodedHttpArchive = params.get("EncodedHttpArchive")
        self.LoadWeight = params.get("LoadWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScriptOrigin(AbstractModel):
    """脚本内置压力模型

    """

    def __init__(self):
        r"""
        :param MachineNumber: 机器数量
        :type MachineNumber: int
        :param MachineSpecification: 机器规格
        :type MachineSpecification: str
        :param DurationSeconds: 压测时长
        :type DurationSeconds: int
        """
        self.MachineNumber = None
        self.MachineSpecification = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.MachineNumber = params.get("MachineNumber")
        self.MachineSpecification = params.get("MachineSpecification")
        self.DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Stage(AbstractModel):
    """分阶段施压时，对单个阶段的配置

    """

    def __init__(self):
        r"""
        :param DurationSeconds: 施压时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationSeconds: int
        :param TargetVirtualUsers: 虚拟用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetVirtualUsers: int
        """
        self.DurationSeconds = None
        self.TargetVirtualUsers = None


    def _deserialize(self, params):
        self.DurationSeconds = params.get("DurationSeconds")
        self.TargetVirtualUsers = params.get("TargetVirtualUsers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartJobRequest(AbstractModel):
    """StartJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param JobOwner: 任务发起人
        :type JobOwner: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Debug: 是否调试
        :type Debug: bool
        :param Note: 备注
        :type Note: str
        """
        self.ScenarioId = None
        self.JobOwner = None
        self.ProjectId = None
        self.Debug = None
        self.Note = None


    def _deserialize(self, params):
        self.ScenarioId = params.get("ScenarioId")
        self.JobOwner = params.get("JobOwner")
        self.ProjectId = params.get("ProjectId")
        self.Debug = params.get("Debug")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartJobResponse(AbstractModel):
    """StartJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class TagSpec(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TestData(AbstractModel):
    """测试数据集

    """

    def __init__(self):
        r"""
        :param Name: 测试数据集所在的文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Split: 测试数据集是否分片
注意：此字段可能返回 null，表示取不到有效值。
        :type Split: bool
        :param HeaderInFile: 首行是否为参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderInFile: bool
        :param HeaderColumns: 参数名数组
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderColumns: list of str
        :param LineCount: 文件行数
注意：此字段可能返回 null，表示取不到有效值。
        :type LineCount: int
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param Size: 文件字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param HeadLines: 头部数据行
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadLines: list of str
        :param TailLines: 尾部数据行
注意：此字段可能返回 null，表示取不到有效值。
        :type TailLines: list of str
        :param Type: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param FileId: 文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        """
        self.Name = None
        self.Split = None
        self.HeaderInFile = None
        self.HeaderColumns = None
        self.LineCount = None
        self.UpdatedAt = None
        self.Size = None
        self.HeadLines = None
        self.TailLines = None
        self.Type = None
        self.FileId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Split = params.get("Split")
        self.HeaderInFile = params.get("HeaderInFile")
        self.HeaderColumns = params.get("HeaderColumns")
        self.LineCount = params.get("LineCount")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Size = params.get("Size")
        self.HeadLines = params.get("HeadLines")
        self.TailLines = params.get("TailLines")
        self.Type = params.get("Type")
        self.FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCronJobRequest(AbstractModel):
    """UpdateCronJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param CronJobId: 定时任务ID
        :type CronJobId: str
        :param Note: 备注
        :type Note: str
        :param CronExpression: cron表达式
        :type CronExpression: str
        :param FrequencyType: 执行频率类型，1:只执行一次; 2:日粒度; 3:周粒度; 4:高级
        :type FrequencyType: int
        :param Name: 定时任务名字
        :type Name: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param ScenarioName: 场景名称
        :type ScenarioName: str
        :param JobOwner: 任务发起人
        :type JobOwner: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param NoticeId: Notice ID
        :type NoticeId: str
        """
        self.ProjectId = None
        self.CronJobId = None
        self.Note = None
        self.CronExpression = None
        self.FrequencyType = None
        self.Name = None
        self.ScenarioId = None
        self.ScenarioName = None
        self.JobOwner = None
        self.EndTime = None
        self.NoticeId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CronJobId = params.get("CronJobId")
        self.Note = params.get("Note")
        self.CronExpression = params.get("CronExpression")
        self.FrequencyType = params.get("FrequencyType")
        self.Name = params.get("Name")
        self.ScenarioId = params.get("ScenarioId")
        self.ScenarioName = params.get("ScenarioName")
        self.JobOwner = params.get("JobOwner")
        self.EndTime = params.get("EndTime")
        self.NoticeId = params.get("NoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCronJobResponse(AbstractModel):
    """UpdateCronJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFileScenarioRelationRequest(AbstractModel):
    """UpdateFileScenarioRelation请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileId: 文件 ID
        :type FileId: str
        :param ProjectId: 项目 ID
        :type ProjectId: str
        :param ScenarioIds: 场景 ID 数组
        :type ScenarioIds: list of str
        """
        self.FileId = None
        self.ProjectId = None
        self.ScenarioIds = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioIds = params.get("ScenarioIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFileScenarioRelationResponse(AbstractModel):
    """UpdateFileScenarioRelation返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateJobRequest(AbstractModel):
    """UpdateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param Note: 任务备注信息
        :type Note: str
        """
        self.JobId = None
        self.ProjectId = None
        self.ScenarioId = None
        self.Note = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ProjectId = params.get("ProjectId")
        self.ScenarioId = params.get("ScenarioId")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateJobResponse(AbstractModel):
    """UpdateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateProjectRequest(AbstractModel):
    """UpdateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Name: 项目名
        :type Name: str
        :param Description: 项目描述
        :type Description: str
        :param Status: 项目状态，默认传递1
        :type Status: int
        :param Tags: 标签数组
        :type Tags: list of TagSpec
        """
        self.ProjectId = None
        self.Name = None
        self.Description = None
        self.Status = None
        self.Tags = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagSpec()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProjectResponse(AbstractModel):
    """UpdateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateScenarioRequest(AbstractModel):
    """UpdateScenario请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScenarioId: 场景ID
        :type ScenarioId: str
        :param Name: 场景名
        :type Name: str
        :param Description: 场景描述
        :type Description: str
        :param Type: 压测引擎类型
        :type Type: str
        :param Load: 施压配置
        :type Load: :class:`tencentcloud.pts.v20210728.models.Load`
        :param EncodedScripts: deprecated
        :type EncodedScripts: str
        :param Configs: deprecated
        :type Configs: list of str
        :param Datasets: 测试数据集
        :type Datasets: list of TestData
        :param Extensions: deprecated
        :type Extensions: list of str
        :param SLAId: SLA规则ID
        :type SLAId: str
        :param CronId: cron job ID
        :type CronId: str
        :param Status: 场景状态（注：现已无需传递该参数）
        :type Status: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param TestScripts: 测试脚本路径
        :type TestScripts: list of ScriptInfo
        :param Protocols: 协议文件路径
        :type Protocols: list of ProtocolInfo
        :param RequestFiles: 请求文件路径
        :type RequestFiles: list of FileInfo
        :param SLAPolicy: SLA 策略
        :type SLAPolicy: :class:`tencentcloud.pts.v20210728.models.SLAPolicy`
        :param Plugins: 拓展包文件路径
        :type Plugins: list of FileInfo
        :param DomainNameConfig: 域名解析配置
        :type DomainNameConfig: :class:`tencentcloud.pts.v20210728.models.DomainNameConfig`
        """
        self.ScenarioId = None
        self.Name = None
        self.Description = None
        self.Type = None
        self.Load = None
        self.EncodedScripts = None
        self.Configs = None
        self.Datasets = None
        self.Extensions = None
        self.SLAId = None
        self.CronId = None
        self.Status = None
        self.ProjectId = None
        self.TestScripts = None
        self.Protocols = None
        self.RequestFiles = None
        self.SLAPolicy = None
        self.Plugins = None
        self.DomainNameConfig = None


    def _deserialize(self, params):
        self.ScenarioId = params.get("ScenarioId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        if params.get("Load") is not None:
            self.Load = Load()
            self.Load._deserialize(params.get("Load"))
        self.EncodedScripts = params.get("EncodedScripts")
        self.Configs = params.get("Configs")
        if params.get("Datasets") is not None:
            self.Datasets = []
            for item in params.get("Datasets"):
                obj = TestData()
                obj._deserialize(item)
                self.Datasets.append(obj)
        self.Extensions = params.get("Extensions")
        self.SLAId = params.get("SLAId")
        self.CronId = params.get("CronId")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        if params.get("TestScripts") is not None:
            self.TestScripts = []
            for item in params.get("TestScripts"):
                obj = ScriptInfo()
                obj._deserialize(item)
                self.TestScripts.append(obj)
        if params.get("Protocols") is not None:
            self.Protocols = []
            for item in params.get("Protocols"):
                obj = ProtocolInfo()
                obj._deserialize(item)
                self.Protocols.append(obj)
        if params.get("RequestFiles") is not None:
            self.RequestFiles = []
            for item in params.get("RequestFiles"):
                obj = FileInfo()
                obj._deserialize(item)
                self.RequestFiles.append(obj)
        if params.get("SLAPolicy") is not None:
            self.SLAPolicy = SLAPolicy()
            self.SLAPolicy._deserialize(params.get("SLAPolicy"))
        if params.get("Plugins") is not None:
            self.Plugins = []
            for item in params.get("Plugins"):
                obj = FileInfo()
                obj._deserialize(item)
                self.Plugins.append(obj)
        if params.get("DomainNameConfig") is not None:
            self.DomainNameConfig = DomainNameConfig()
            self.DomainNameConfig._deserialize(params.get("DomainNameConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScenarioResponse(AbstractModel):
    """UpdateScenario返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VpcLoadDistribution(AbstractModel):
    """压力来源配置

    """

    def __init__(self):
        r"""
        :param RegionId: 地域ID
        :type RegionId: int
        :param Region: 地域
        :type Region: str
        :param VpcId: VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetIds: 子网ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        """
        self.RegionId = None
        self.Region = None
        self.VpcId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        