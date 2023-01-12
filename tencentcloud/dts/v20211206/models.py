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


class CheckStep(AbstractModel):
    """检查步骤

    """

    def __init__(self):
        r"""
        :param StepNo: 步骤编号
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNo: int
        :param StepId: 步骤Id， 如：ConnectDBCheck、VersionCheck、SrcPrivilegeCheck等，具体校验项和源目标实例相关
注意：此字段可能返回 null，表示取不到有效值。
        :type StepId: str
        :param StepName: 步骤名称
注意：此字段可能返回 null，表示取不到有效值。
        :type StepName: str
        :param StepStatus: 此检查步骤的结果，pass(校验通过)、failed(校验失败)、notStarted(校验还未开始进行)、blocked(检验阻塞)、warning(校验有告警，但仍通过)
注意：此字段可能返回 null，表示取不到有效值。
        :type StepStatus: str
        :param StepMessage: 此检查步骤的错误消息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepMessage: str
        :param DetailCheckItems: 每个检查步骤里的具体检查项
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailCheckItems: list of DetailCheckItem
        :param HasSkipped: 是否已跳过
注意：此字段可能返回 null，表示取不到有效值。
        :type HasSkipped: bool
        """
        self.StepNo = None
        self.StepId = None
        self.StepName = None
        self.StepStatus = None
        self.StepMessage = None
        self.DetailCheckItems = None
        self.HasSkipped = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepId = params.get("StepId")
        self.StepName = params.get("StepName")
        self.StepStatus = params.get("StepStatus")
        self.StepMessage = params.get("StepMessage")
        if params.get("DetailCheckItems") is not None:
            self.DetailCheckItems = []
            for item in params.get("DetailCheckItems"):
                obj = DetailCheckItem()
                obj._deserialize(item)
                self.DetailCheckItems.append(obj)
        self.HasSkipped = params.get("HasSkipped")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStepInfo(AbstractModel):
    """校验任务运行详情

    """

    def __init__(self):
        r"""
        :param StartAt: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartAt: str
        :param EndAt: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndAt: str
        :param Progress: 任务步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        self.StartAt = None
        self.EndAt = None
        self.Progress = None


    def _deserialize(self, params):
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        if params.get("Progress") is not None:
            self.Progress = ProcessProgress()
            self.Progress._deserialize(params.get("Progress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareAbstractInfo(AbstractModel):
    """一致性校验摘要信息

    """

    def __init__(self):
        r"""
        :param Options: 校验配置参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        :param Objects: 一致性校验对比对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param Conclusion: 对比结论: same,different
注意：此字段可能返回 null，表示取不到有效值。
        :type Conclusion: str
        :param Status: 任务状态: success,failed
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param TotalTables: 总的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTables: int
        :param CheckedTables: 已校验的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckedTables: int
        :param DifferentTables: 不一致的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DifferentTables: int
        :param SkippedTables: 跳过校验的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SkippedTables: int
        :param NearlyTableCount: 预估表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type NearlyTableCount: int
        :param DifferentRows: 不一致的数据行数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DifferentRows: int
        :param SrcSampleRows: 源库行数，当对比类型为**行数对比**时此项有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcSampleRows: int
        :param DstSampleRows: 目标库行数，当对比类型为**行数对比**时此项有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type DstSampleRows: int
        :param StartedAt: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedAt: str
        :param FinishedAt: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedAt: str
        """
        self.Options = None
        self.Objects = None
        self.Conclusion = None
        self.Status = None
        self.TotalTables = None
        self.CheckedTables = None
        self.DifferentTables = None
        self.SkippedTables = None
        self.NearlyTableCount = None
        self.DifferentRows = None
        self.SrcSampleRows = None
        self.DstSampleRows = None
        self.StartedAt = None
        self.FinishedAt = None


    def _deserialize(self, params):
        if params.get("Options") is not None:
            self.Options = CompareOptions()
            self.Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self.Objects = CompareObject()
            self.Objects._deserialize(params.get("Objects"))
        self.Conclusion = params.get("Conclusion")
        self.Status = params.get("Status")
        self.TotalTables = params.get("TotalTables")
        self.CheckedTables = params.get("CheckedTables")
        self.DifferentTables = params.get("DifferentTables")
        self.SkippedTables = params.get("SkippedTables")
        self.NearlyTableCount = params.get("NearlyTableCount")
        self.DifferentRows = params.get("DifferentRows")
        self.SrcSampleRows = params.get("SrcSampleRows")
        self.DstSampleRows = params.get("DstSampleRows")
        self.StartedAt = params.get("StartedAt")
        self.FinishedAt = params.get("FinishedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareDetailInfo(AbstractModel):
    """一致性校验详细信息

    """

    def __init__(self):
        r"""
        :param Difference: 数据不一致的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Difference: :class:`tencentcloud.dts.v20211206.models.DifferenceDetail`
        :param Skipped: 跳过校验的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Skipped: :class:`tencentcloud.dts.v20211206.models.SkippedDetail`
        """
        self.Difference = None
        self.Skipped = None


    def _deserialize(self, params):
        if params.get("Difference") is not None:
            self.Difference = DifferenceDetail()
            self.Difference._deserialize(params.get("Difference"))
        if params.get("Skipped") is not None:
            self.Skipped = SkippedDetail()
            self.Skipped._deserialize(params.get("Skipped"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareObject(AbstractModel):
    """一致性对比对象配置

    """

    def __init__(self):
        r"""
        :param ObjectMode: 对象模式 整实例-all,部分对象-partial
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectMode: str
        :param ObjectItems: 对象列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectItems: list of CompareObjectItem
        :param AdvancedObjects: 高级对象类型，如account(账号),index(索引),shardkey(片建，后面可能会调整),schema(库表结构)
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedObjects: list of str
        """
        self.ObjectMode = None
        self.ObjectItems = None
        self.AdvancedObjects = None


    def _deserialize(self, params):
        self.ObjectMode = params.get("ObjectMode")
        if params.get("ObjectItems") is not None:
            self.ObjectItems = []
            for item in params.get("ObjectItems"):
                obj = CompareObjectItem()
                obj._deserialize(item)
                self.ObjectItems.append(obj)
        self.AdvancedObjects = params.get("AdvancedObjects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareObjectItem(AbstractModel):
    """一致性校验库表对象

    """

    def __init__(self):
        r"""
        :param DbName: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param DbMode: 数据库选择模式: all 为当前对象下的所有对象,partial 为部分对象
注意：此字段可能返回 null，表示取不到有效值。
        :type DbMode: str
        :param SchemaName: schema名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param TableMode: 表选择模式: all 为当前对象下的所有表对象,partial 为部分表对象
注意：此字段可能返回 null，表示取不到有效值。
        :type TableMode: str
        :param Tables: 用于一致性校验的表配置，当 TableMode 为 partial 时，需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of CompareTableItem
        :param ViewMode: 视图选择模式: all 为当前对象下的所有视图对象,partial 为部分视图对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewMode: str
        :param Views: 用于一致性校验的视图配置，当 ViewMode 为 partial 时， 需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Views: list of CompareViewItem
        """
        self.DbName = None
        self.DbMode = None
        self.SchemaName = None
        self.TableMode = None
        self.Tables = None
        self.ViewMode = None
        self.Views = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.DbMode = params.get("DbMode")
        self.SchemaName = params.get("SchemaName")
        self.TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = CompareTableItem()
                obj._deserialize(item)
                self.Tables.append(obj)
        self.ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = CompareViewItem()
                obj._deserialize(item)
                self.Views.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareOptions(AbstractModel):
    """一致性校验选项

    """

    def __init__(self):
        r"""
        :param Method: 对比类型：dataCheck(完整数据对比)、sampleDataCheck(抽样数据对比)、rowsCount(行数对比)
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param SampleRate: 抽样比例;范围0,100
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleRate: int
        :param ThreadCount: 线程数，取值1-5，默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type ThreadCount: int
        """
        self.Method = None
        self.SampleRate = None
        self.ThreadCount = None


    def _deserialize(self, params):
        self.Method = params.get("Method")
        self.SampleRate = params.get("SampleRate")
        self.ThreadCount = params.get("ThreadCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTableItem(AbstractModel):
    """用于一致性校验的表配置

    """

    def __init__(self):
        r"""
        :param TableName: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        """
        self.TableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTaskInfo(AbstractModel):
    """数据一致性校验结果

    """

    def __init__(self):
        r"""
        :param CompareTaskId: 一致性校验任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTaskId: str
        :param Status: 一致性校验结果，包括：unstart(未启动)、running(校验中)、canceled(已终止)、failed(校验任务失败)、inconsistent(不一致)、consistent(一致)、notexist(不存在校验任务)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.CompareTaskId = None
        self.Status = None


    def _deserialize(self, params):
        self.CompareTaskId = params.get("CompareTaskId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTaskItem(AbstractModel):
    """一致性校验对象信息

    """

    def __init__(self):
        r"""
        :param JobId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param CompareTaskId: 对比任务 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTaskId: str
        :param TaskName: 对比任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param Status: 对比任务状态, 可能的值：created - 创建完成；readyRun - 等待运行；running - 运行中；success - 成功；stopping - 结束中；failed - 失败；canceled - 已终止
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Config: 对比任务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param CheckProcess: 对比任务校验详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param CompareProcess: 对比任务运行详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param Conclusion: 对比结果, 可能的值：same - 一致；different - 不一致；skipAll - 跳过
注意：此字段可能返回 null，表示取不到有效值。
        :type Conclusion: str
        :param CreatedAt: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param StartedAt: 任务启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedAt: str
        :param FinishedAt: 对比结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedAt: str
        :param Method: 对比类型，dataCheck(完整数据对比)、sampleDataCheck(抽样数据对比)、rowsCount(行数对比)
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param Options: 对比配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        :param Message: 一致性校验提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.JobId = None
        self.CompareTaskId = None
        self.TaskName = None
        self.Status = None
        self.Config = None
        self.CheckProcess = None
        self.CompareProcess = None
        self.Conclusion = None
        self.CreatedAt = None
        self.StartedAt = None
        self.FinishedAt = None
        self.Method = None
        self.Options = None
        self.Message = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        self.TaskName = params.get("TaskName")
        self.Status = params.get("Status")
        if params.get("Config") is not None:
            self.Config = CompareObject()
            self.Config._deserialize(params.get("Config"))
        if params.get("CheckProcess") is not None:
            self.CheckProcess = ProcessProgress()
            self.CheckProcess._deserialize(params.get("CheckProcess"))
        if params.get("CompareProcess") is not None:
            self.CompareProcess = ProcessProgress()
            self.CompareProcess._deserialize(params.get("CompareProcess"))
        self.Conclusion = params.get("Conclusion")
        self.CreatedAt = params.get("CreatedAt")
        self.StartedAt = params.get("StartedAt")
        self.FinishedAt = params.get("FinishedAt")
        self.Method = params.get("Method")
        if params.get("Options") is not None:
            self.Options = CompareOptions()
            self.Options._deserialize(params.get("Options"))
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareViewItem(AbstractModel):
    """用于一致性校验的视图配置

    """

    def __init__(self):
        r"""
        :param ViewName: 视图名
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        """
        self.ViewName = None


    def _deserialize(self, params):
        self.ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        :param CompleteMode: 完成任务的方式,仅支持旧版MySQL迁移任务。waitForSync-等待主从差距为0才停止,immediately-立即完成，不会等待主从差距一致。默认为waitForSync
        :type CompleteMode: str
        """
        self.JobId = None
        self.CompleteMode = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompleteMode = params.get("CompleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConfigureSyncJobRequest(AbstractModel):
    """ConfigureSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步实例id（即标识一个同步作业），形如sync-werwfs23
        :type JobId: str
        :param SrcAccessType: 源端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)、noProxy,注意具体可选值依赖当前链路
        :type SrcAccessType: str
        :param DstAccessType: 目标端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)、noProxy,注意具体可选值依赖当前链路
        :type DstAccessType: str
        :param Options: 同步任务选项
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param Objects: 同步库表对象信息
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param JobName: 同步任务名称
        :type JobName: str
        :param JobMode: 枚举值是 liteMode 和 fullMode ，分别对应精简模式或正常模式
        :type JobMode: str
        :param RunMode: 运行模式，取值如：Immediate(表示立即运行，默认为此项值)、Timed(表示定时运行)
        :type RunMode: str
        :param ExpectRunTime: 期待启动时间，当RunMode取值为Timed时，此值必填，形如："2006-01-02 15:04:05"
        :type ExpectRunTime: str
        :param SrcInfo: 源端信息，单节点数据库使用
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param DstInfo: 目标端信息，单节点数据库使用
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param AutoRetryTimeRangeMinutes: 自动重试的时间段、可设置5至720分钟、0表示不重试
        :type AutoRetryTimeRangeMinutes: int
        """
        self.JobId = None
        self.SrcAccessType = None
        self.DstAccessType = None
        self.Options = None
        self.Objects = None
        self.JobName = None
        self.JobMode = None
        self.RunMode = None
        self.ExpectRunTime = None
        self.SrcInfo = None
        self.DstInfo = None
        self.AutoRetryTimeRangeMinutes = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.SrcAccessType = params.get("SrcAccessType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("Options") is not None:
            self.Options = Options()
            self.Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self.Objects = Objects()
            self.Objects._deserialize(params.get("Objects"))
        self.JobName = params.get("JobName")
        self.JobMode = params.get("JobMode")
        self.RunMode = params.get("RunMode")
        self.ExpectRunTime = params.get("ExpectRunTime")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = Endpoint()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = Endpoint()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureSyncJobResponse(AbstractModel):
    """ConfigureSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConflictHandleOption(AbstractModel):
    """冲突处理里的详细描述

    """

    def __init__(self):
        r"""
        :param ConditionColumn: 条件覆盖的列
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionColumn: str
        :param ConditionOperator: 条件覆盖操作
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionOperator: str
        :param ConditionOrderInSrcAndDst: 条件覆盖优先级处理
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionOrderInSrcAndDst: str
        """
        self.ConditionColumn = None
        self.ConditionOperator = None
        self.ConditionOrderInSrcAndDst = None


    def _deserialize(self, params):
        self.ConditionColumn = params.get("ConditionColumn")
        self.ConditionOperator = params.get("ConditionOperator")
        self.ConditionOrderInSrcAndDst = params.get("ConditionOrderInSrcAndDst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsistencyOption(AbstractModel):
    """数据一致性校验选项， 默认为不开启一致性校验

    """

    def __init__(self):
        r"""
        :param Mode: 一致性检测类型: full(全量检测迁移对象)、noCheck(不检测)、notConfigured(未配置)
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        """
        self.Mode = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueMigrateJobRequest(AbstractModel):
    """ContinueMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueMigrateJobResponse(AbstractModel):
    """ContinueMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ContinueSyncJobRequest(AbstractModel):
    """ContinueSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueSyncJobResponse(AbstractModel):
    """ContinueSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCheckSyncJobRequest(AbstractModel):
    """CreateCheckSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCheckSyncJobResponse(AbstractModel):
    """CreateCheckSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCompareTaskRequest(AbstractModel):
    """CreateCompareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务 Id
        :type JobId: str
        :param TaskName: 数据对比任务名称，若为空则默认给CompareTaskId相同值
        :type TaskName: str
        :param ObjectMode: 数据对比对象模式，sameAsMigrate(全部迁移对象， 默认为此项配置)，custom(自定义模式)
        :type ObjectMode: str
        :param Objects: 一致性对比对象配置
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param Options: 一致性校验选项
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        self.JobId = None
        self.TaskName = None
        self.ObjectMode = None
        self.Objects = None
        self.Options = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.ObjectMode = params.get("ObjectMode")
        if params.get("Objects") is not None:
            self.Objects = CompareObject()
            self.Objects._deserialize(params.get("Objects"))
        if params.get("Options") is not None:
            self.Options = CompareOptions()
            self.Options._deserialize(params.get("Options"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCompareTaskResponse(AbstractModel):
    """CreateCompareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompareTaskId: 数据对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompareTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompareTaskId = params.get("CompareTaskId")
        self.RequestId = params.get("RequestId")


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMigrationServiceRequest(AbstractModel):
    """CreateMigrationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param SrcDatabaseType: 源实例数据库类型，mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb
        :type SrcDatabaseType: str
        :param DstDatabaseType: 目标实例数据库类型，mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb
        :type DstDatabaseType: str
        :param SrcRegion: 源实例地域，如：ap-guangzhou
        :type SrcRegion: str
        :param DstRegion: 目标实例地域，如：ap-guangzhou。注意，目标地域必须和API请求地域保持一致。
        :type DstRegion: str
        :param InstanceClass: 实例规格，包括：small、medium、large、xlarge、2xlarge
        :type InstanceClass: str
        :param Count: 购买数量，范围为[1,15]，默认为1
        :type Count: int
        :param JobName: 迁移服务名称，最大长度128
        :type JobName: str
        :param Tags: 标签信息
        :type Tags: list of TagItem
        """
        self.SrcDatabaseType = None
        self.DstDatabaseType = None
        self.SrcRegion = None
        self.DstRegion = None
        self.InstanceClass = None
        self.Count = None
        self.JobName = None
        self.Tags = None


    def _deserialize(self, params):
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.SrcRegion = params.get("SrcRegion")
        self.DstRegion = params.get("DstRegion")
        self.InstanceClass = params.get("InstanceClass")
        self.Count = params.get("Count")
        self.JobName = params.get("JobName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationServiceResponse(AbstractModel):
    """CreateMigrationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobIds: 下单成功随机生成的迁移任务id列表，形如：dts-c1f6rs21
注意：此字段可能返回 null，表示取不到有效值。
        :type JobIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        self.RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayMode: 付款类型, 如：PrePay(表示包年包月)、PostPay(表示按时按量)
        :type PayMode: str
        :param SrcDatabaseType: 源端数据库类型,如mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
        :type SrcDatabaseType: str
        :param SrcRegion: 源端数据库所在地域,如ap-guangzhou
        :type SrcRegion: str
        :param DstDatabaseType: 目标端数据库类型,如mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
        :type DstDatabaseType: str
        :param DstRegion: 目标端数据库所在地域,如ap-guangzhou
        :type DstRegion: str
        :param Specification: 同步任务规格，Standard:标准版
        :type Specification: str
        :param Tags: 标签信息
        :type Tags: list of TagItem
        :param Count: 一次购买的同步任务数量，取值范围为[1, 10]，默认为1
        :type Count: int
        :param AutoRenew: 自动续费标识，当PayMode值为PrePay则此项配置有意义，取值为：1（表示自动续费）、0（不自动续费，默认为此值）
        :type AutoRenew: int
        :param InstanceClass: 同步链路规格，如micro,small,medium,large，默认为medium
        :type InstanceClass: str
        :param JobName: 同步任务名称
        :type JobName: str
        :param ExistedJobId: 创建类似任务的现有任务Id
        :type ExistedJobId: str
        """
        self.PayMode = None
        self.SrcDatabaseType = None
        self.SrcRegion = None
        self.DstDatabaseType = None
        self.DstRegion = None
        self.Specification = None
        self.Tags = None
        self.Count = None
        self.AutoRenew = None
        self.InstanceClass = None
        self.JobName = None
        self.ExistedJobId = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcRegion = params.get("SrcRegion")
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstRegion = params.get("DstRegion")
        self.Specification = params.get("Specification")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Count = params.get("Count")
        self.AutoRenew = params.get("AutoRenew")
        self.InstanceClass = params.get("InstanceClass")
        self.JobName = params.get("JobName")
        self.ExistedJobId = params.get("ExistedJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobIds: 同步任务ids
        :type JobIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        self.RequestId = params.get("RequestId")


class DBEndpointInfo(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param Region: 实例所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param AccessType: 实例网络接入类型，如：extranet(外网)、ipv6(公网ipv6)、cvm(云主机自建)、dcg(专线接入)、vpncloud(vpn接入的实例)、cdb(云数据库)、ccn(云联网)、intranet(自研上云)、vpc(私有网络)等，注意具体可选值依赖当前链路
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: str
        :param DatabaseType: 实例数据库类型，如：mysql,redis,mongodb,postgresql,mariadb,percona 等
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseType: str
        :param NodeType: 节点类型，为空或者"simple":表示普通节点，"cluster": 集群节点
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param Info: 数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: list of DBInfo
        :param Supplier: 实例服务提供商，如:"aliyun","others"
注意：此字段可能返回 null，表示取不到有效值。
        :type Supplier: str
        :param ExtraAttr: MongoDB可定义如下的参数: 	['AuthDatabase':'admin', 
'AuthFlag': "1",	'AuthMechanism':"SCRAM-SHA-1"]
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraAttr: list of KeyValuePairOption
        """
        self.Region = None
        self.AccessType = None
        self.DatabaseType = None
        self.NodeType = None
        self.Info = None
        self.Supplier = None
        self.ExtraAttr = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.AccessType = params.get("AccessType")
        self.DatabaseType = params.get("DatabaseType")
        self.NodeType = params.get("NodeType")
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = DBInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        self.Supplier = params.get("Supplier")
        if params.get("ExtraAttr") is not None:
            self.ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self.ExtraAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInfo(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        r"""
        :param Role: 表示节点角色，针对分布式数据库，如mongodb中的mongos节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param DbKernel: 内核版本，针对mariadb的不同内核版本等
注意：此字段可能返回 null，表示取不到有效值。
        :type DbKernel: str
        :param Host: 实例的IP地址，对于公网、专线、VPN、云联网、自研上云、VPC等接入方式此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param Port: 实例的端口，对于公网、云主机自建、专线、VPN、云联网、自研上云、VPC等接入方式此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param User: 实例的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param Password: 实例的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param CvmInstanceId: CVM实例短ID，格式如：ins-olgl39y8；与云服务器控制台页面显示的实例ID相同；如果接入类型为云主机自建的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstanceId: str
        :param UniqVpnGwId: VPN网关ID，格式如：vpngw-9ghexg7q；如果接入类型为vpncloud的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpnGwId: str
        :param UniqDcgId: 专线网关ID，格式如：dcg-0rxtqqxb；如果接入类型为专线接入的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqDcgId: str
        :param InstanceId: 数据库实例ID，格式如：cdb-powiqx8q；如果接入类型为云数据库的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param CcnGwId: 云联网ID，如：ccn-afp6kltc 注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnGwId: str
        :param VpcId: 私有网络ID，格式如：vpc-92jblxto；如果接入类型为vpc、vpncloud、ccn、dcg的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 私有网络下的子网ID，格式如：subnet-3paxmkdz；如果接入类型为vpc、vpncloud、ccn、dcg的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param EngineVersion: 数据库版本，当实例为RDS实例时才有效，格式如：5.6或者5.7，默认为5.6
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineVersion: str
        :param Account: 实例所属账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param AccountRole: 跨账号迁移时的角色,只允许[a-zA-Z0-9\-\_]+
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountRole: str
        :param AccountMode: 资源所属账号 为空或self(表示本账号内资源)、other(表示其他账户资源)
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountMode: str
        :param TmpSecretId: 临时密钥Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param TmpSecretKey: 临时密钥Key
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        :param TmpToken: 临时Token
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpToken: str
        """
        self.Role = None
        self.DbKernel = None
        self.Host = None
        self.Port = None
        self.User = None
        self.Password = None
        self.CvmInstanceId = None
        self.UniqVpnGwId = None
        self.UniqDcgId = None
        self.InstanceId = None
        self.CcnGwId = None
        self.VpcId = None
        self.SubnetId = None
        self.EngineVersion = None
        self.Account = None
        self.AccountRole = None
        self.AccountMode = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.TmpToken = None


    def _deserialize(self, params):
        self.Role = params.get("Role")
        self.DbKernel = params.get("DbKernel")
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.UniqVpnGwId = params.get("UniqVpnGwId")
        self.UniqDcgId = params.get("UniqDcgId")
        self.InstanceId = params.get("InstanceId")
        self.CcnGwId = params.get("CcnGwId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.EngineVersion = params.get("EngineVersion")
        self.Account = params.get("Account")
        self.AccountRole = params.get("AccountRole")
        self.AccountMode = params.get("AccountMode")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.TmpToken = params.get("TmpToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBItem(AbstractModel):
    """迁移对象信息，在配置库表视图等对象信息时大小写敏感

    """

    def __init__(self):
        r"""
        :param DbName: 需要迁移或同步的库名，当ObjectMode为partial时，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param NewDbName: 迁移或同步后的库名，默认与源库相同
注意：此字段可能返回 null，表示取不到有效值。
        :type NewDbName: str
        :param SchemaName: 迁移或同步的 schema
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param NewSchemaName: 迁移或同步后的 schema name
注意：此字段可能返回 null，表示取不到有效值。
        :type NewSchemaName: str
        :param DBMode: DB选择模式: all(为当前对象下的所有对象)，partial(部分对象)，当ObjectMode为partial时，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type DBMode: str
        :param SchemaMode: schema选择模式: all(为当前对象下的所有对象)，partial(部分对象)
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaMode: str
        :param TableMode: 表选择模式: all(为当前对象下的所有对象)，partial(部分对象)，当DBMode为partial时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TableMode: str
        :param Tables: 表图对象集合，当 TableMode 为 partial 时，此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of TableItem
        :param ViewMode: 视图选择模式: all 为当前对象下的所有视图对象,partial 为部分视图对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewMode: str
        :param Views: 视图对象集合，当 ViewMode 为 partial 时， 此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Views: list of ViewItem
        :param RoleMode: postgresql独有参数，角色选择模式: all 为当前对象下的所有角色对象,partial 为部分角色对象
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleMode: str
        :param Roles: postgresql独有参数，当 RoleMode 为 partial 时， 此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of RoleItem
        :param FunctionMode: 选择要同步的模式，partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionMode: str
        :param TriggerMode: 选择要同步的模式，partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerMode: str
        :param EventMode: 选择要同步的模式，partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type EventMode: str
        :param ProcedureMode: 选择要同步的模式，partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureMode: str
        :param Functions: FunctionMode取值为partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Functions: list of str
        :param Procedures: ProcedureMode取值为partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Procedures: list of str
        :param Events: EventMode取值为partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of str
        :param Triggers: TriggerMode取值为partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Triggers: list of str
        """
        self.DbName = None
        self.NewDbName = None
        self.SchemaName = None
        self.NewSchemaName = None
        self.DBMode = None
        self.SchemaMode = None
        self.TableMode = None
        self.Tables = None
        self.ViewMode = None
        self.Views = None
        self.RoleMode = None
        self.Roles = None
        self.FunctionMode = None
        self.TriggerMode = None
        self.EventMode = None
        self.ProcedureMode = None
        self.Functions = None
        self.Procedures = None
        self.Events = None
        self.Triggers = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.NewDbName = params.get("NewDbName")
        self.SchemaName = params.get("SchemaName")
        self.NewSchemaName = params.get("NewSchemaName")
        self.DBMode = params.get("DBMode")
        self.SchemaMode = params.get("SchemaMode")
        self.TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = TableItem()
                obj._deserialize(item)
                self.Tables.append(obj)
        self.ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = ViewItem()
                obj._deserialize(item)
                self.Views.append(obj)
        self.RoleMode = params.get("RoleMode")
        if params.get("Roles") is not None:
            self.Roles = []
            for item in params.get("Roles"):
                obj = RoleItem()
                obj._deserialize(item)
                self.Roles.append(obj)
        self.FunctionMode = params.get("FunctionMode")
        self.TriggerMode = params.get("TriggerMode")
        self.EventMode = params.get("EventMode")
        self.ProcedureMode = params.get("ProcedureMode")
        self.Functions = params.get("Functions")
        self.Procedures = params.get("Procedures")
        self.Events = params.get("Events")
        self.Triggers = params.get("Triggers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """需要同步的库表对象

    """

    def __init__(self):
        r"""
        :param DbName: 需要迁移或同步的库名，当ObjectMode为Partial时，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param NewDbName: 迁移或同步后的库名，默认与源库相同
注意：此字段可能返回 null，表示取不到有效值。
        :type NewDbName: str
        :param DbMode: DB选择模式: All(为当前对象下的所有对象)，Partial(部分对象)，当Mode为Partial时，此项必填。注意，高级对象的同步不依赖此值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DbMode: str
        :param SchemaName: 迁移或同步的 schema
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param NewSchemaName: 迁移或同步后的 schema name
注意：此字段可能返回 null，表示取不到有效值。
        :type NewSchemaName: str
        :param TableMode: 表选择模式: All(为当前对象下的所有对象)，Partial(部分对象)，当DBMode为Partial时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TableMode: str
        :param Tables: 表图对象集合，当 TableMode 为 Partial 时，此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of Table
        :param ViewMode: 视图选择模式: All 为当前对象下的所有视图对象,Partial 为部分视图对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewMode: str
        :param Views: 视图对象集合，当 ViewMode 为 Partial 时， 此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Views: list of View
        :param FunctionMode: 选择要同步的模式，Partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionMode: str
        :param Functions: FunctionMode取值为Partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Functions: list of str
        :param ProcedureMode: 选择要同步的模式，Partial为部分，All为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureMode: str
        :param Procedures: ProcedureMode取值为Partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Procedures: list of str
        :param TriggerMode: 触发器迁移模式，all(为当前对象下的所有对象)，partial(部分对象)
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerMode: str
        :param Triggers: 当TriggerMode为partial，指定要迁移的触发器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Triggers: list of str
        :param EventMode: 事件迁移模式，all(为当前对象下的所有对象)，partial(部分对象)
注意：此字段可能返回 null，表示取不到有效值。
        :type EventMode: str
        :param Events: 当EventMode为partial，指定要迁移的事件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of str
        """
        self.DbName = None
        self.NewDbName = None
        self.DbMode = None
        self.SchemaName = None
        self.NewSchemaName = None
        self.TableMode = None
        self.Tables = None
        self.ViewMode = None
        self.Views = None
        self.FunctionMode = None
        self.Functions = None
        self.ProcedureMode = None
        self.Procedures = None
        self.TriggerMode = None
        self.Triggers = None
        self.EventMode = None
        self.Events = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.NewDbName = params.get("NewDbName")
        self.DbMode = params.get("DbMode")
        self.SchemaName = params.get("SchemaName")
        self.NewSchemaName = params.get("NewSchemaName")
        self.TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = Table()
                obj._deserialize(item)
                self.Tables.append(obj)
        self.ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = View()
                obj._deserialize(item)
                self.Views.append(obj)
        self.FunctionMode = params.get("FunctionMode")
        self.Functions = params.get("Functions")
        self.ProcedureMode = params.get("ProcedureMode")
        self.Procedures = params.get("Procedures")
        self.TriggerMode = params.get("TriggerMode")
        self.Triggers = params.get("Triggers")
        self.EventMode = params.get("EventMode")
        self.Events = params.get("Events")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTableObject(AbstractModel):
    """迁移对象选项，需要告知迁移服务迁移哪些库表对象

    """

    def __init__(self):
        r"""
        :param ObjectMode: 迁移对象类型 all(全实例)，partial(部分对象)
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectMode: str
        :param Databases: 迁移对象，当 ObjectMode 为 partial 时，不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of DBItem
        :param AdvancedObjects: 高级对象类型，如trigger、function、procedure、event
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedObjects: list of str
        """
        self.ObjectMode = None
        self.Databases = None
        self.AdvancedObjects = None


    def _deserialize(self, params):
        self.ObjectMode = params.get("ObjectMode")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = DBItem()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.AdvancedObjects = params.get("AdvancedObjects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdlOption(AbstractModel):
    """数据同步中的ddl同步处理

    """

    def __init__(self):
        r"""
        :param DdlObject: ddl类型，如Database,Table,View,Index等
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlObject: str
        :param DdlValue: ddl具体值，对于Database可取值[Create,Drop,Alter]<br>对于Table可取值[Create,Drop,Alter,Truncate,Rename]<br/>对于View可取值[Create,Drop]<br/>对于Index可取值[Create,Drop]
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlValue: list of str
        """
        self.DdlObject = None
        self.DdlValue = None


    def _deserialize(self, params):
        self.DdlObject = params.get("DdlObject")
        self.DdlValue = params.get("DdlValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompareTaskRequest(AbstractModel):
    """DeleteCompareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 迁移任务 Id
        :type JobId: str
        :param CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        """
        self.JobId = None
        self.CompareTaskId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompareTaskResponse(AbstractModel):
    """DeleteCompareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCheckSyncJobResultRequest(AbstractModel):
    """DescribeCheckSyncJobResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckSyncJobResultResponse(AbstractModel):
    """DescribeCheckSyncJobResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 校验结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param StepCount: 步骤总数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepCount: int
        :param StepCur: 当前所在步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepCur: int
        :param Progress: 总体进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param StepInfos: 步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfos: list of StepInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.StepCount = None
        self.StepCur = None
        self.Progress = None
        self.StepInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StepCount = params.get("StepCount")
        self.StepCur = params.get("StepCur")
        self.Progress = params.get("Progress")
        if params.get("StepInfos") is not None:
            self.StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self.StepInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCompareReportRequest(AbstractModel):
    """DescribeCompareReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 迁移任务 Id
        :type JobId: str
        :param CompareTaskId: 校验任务 Id
        :type CompareTaskId: str
        :param DifferenceLimit: 校验不一致结果的 limit
        :type DifferenceLimit: int
        :param DifferenceOffset: 不一致的 Offset
        :type DifferenceOffset: int
        :param DifferenceDB: 搜索条件，不一致的库名
        :type DifferenceDB: str
        :param DifferenceTable: 搜索条件，不一致的表名
        :type DifferenceTable: str
        :param SkippedLimit: 未校验的 Limit
        :type SkippedLimit: int
        :param SkippedOffset: 未校验的 Offset
        :type SkippedOffset: int
        :param SkippedDB: 搜索条件，未校验的库名
        :type SkippedDB: str
        :param SkippedTable: 搜索条件，未校验的表名
        :type SkippedTable: str
        """
        self.JobId = None
        self.CompareTaskId = None
        self.DifferenceLimit = None
        self.DifferenceOffset = None
        self.DifferenceDB = None
        self.DifferenceTable = None
        self.SkippedLimit = None
        self.SkippedOffset = None
        self.SkippedDB = None
        self.SkippedTable = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        self.DifferenceLimit = params.get("DifferenceLimit")
        self.DifferenceOffset = params.get("DifferenceOffset")
        self.DifferenceDB = params.get("DifferenceDB")
        self.DifferenceTable = params.get("DifferenceTable")
        self.SkippedLimit = params.get("SkippedLimit")
        self.SkippedOffset = params.get("SkippedOffset")
        self.SkippedDB = params.get("SkippedDB")
        self.SkippedTable = params.get("SkippedTable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompareReportResponse(AbstractModel):
    """DescribeCompareReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param Abstract: 一致性校验摘要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Abstract: :class:`tencentcloud.dts.v20211206.models.CompareAbstractInfo`
        :param Detail: 一致性校验详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: :class:`tencentcloud.dts.v20211206.models.CompareDetailInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Abstract = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Abstract") is not None:
            self.Abstract = CompareAbstractInfo()
            self.Abstract._deserialize(params.get("Abstract"))
        if params.get("Detail") is not None:
            self.Detail = CompareDetailInfo()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeCompareTasksRequest(AbstractModel):
    """DescribeCompareTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 迁移任务 Id
        :type JobId: str
        :param Limit: 分页设置，表示每页显示多少条任务，默认为 20
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        :param CompareTaskId: 校验任务 ID
        :type CompareTaskId: str
        :param Status: 任务状态过滤，可能的值：created - 创建完成；readyRun - 等待运行；running - 运行中；success - 成功；stopping - 结束中；failed - 失败；canceled - 已终止
        :type Status: list of str
        """
        self.JobId = None
        self.Limit = None
        self.Offset = None
        self.CompareTaskId = None
        self.Status = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.CompareTaskId = params.get("CompareTaskId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompareTasksResponse(AbstractModel):
    """DescribeCompareTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 一致性校验列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of CompareTaskItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CompareTaskItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMigrateDBInstancesRequest(AbstractModel):
    """DescribeMigrateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatabaseType: 数据库类型，如mysql
        :type DatabaseType: str
        :param MigrateRole: 实例作为迁移的源还是目标,src(表示源)，dst(表示目标)
        :type MigrateRole: str
        :param InstanceId: 云数据库实例ID
        :type InstanceId: str
        :param InstanceName: 云数据库名称
        :type InstanceName: str
        :param Limit: 返回数量限制
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param AccountMode: 资源所属账号 为空值或self(表示本账号内资源)、other(表示其他账户资源)
        :type AccountMode: str
        :param TmpSecretId: 临时密钥Id，若为跨账号资源此项必填
        :type TmpSecretId: str
        :param TmpSecretKey: 临时密钥Key，若为跨账号资源此项必填
        :type TmpSecretKey: str
        :param TmpToken: 临时密钥Token，若为跨账号资源此项必填
        :type TmpToken: str
        """
        self.DatabaseType = None
        self.MigrateRole = None
        self.InstanceId = None
        self.InstanceName = None
        self.Limit = None
        self.Offset = None
        self.AccountMode = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.TmpToken = None


    def _deserialize(self, params):
        self.DatabaseType = params.get("DatabaseType")
        self.MigrateRole = params.get("MigrateRole")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.AccountMode = params.get("AccountMode")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.TmpToken = params.get("TmpToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateDBInstancesResponse(AbstractModel):
    """DescribeMigrateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合筛选条件的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Instances: 实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of MigrateDBItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = MigrateDBItem()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMigrationCheckJobRequest(AbstractModel):
    """DescribeMigrationCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationCheckJobResponse(AbstractModel):
    """DescribeMigrationCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 校验任务执行状态，如：notStarted(未开始)、running(校验中)、failed(校验任务失败)、success(任务成功)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param BriefMsg: 校验任务结果输出简要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefMsg: str
        :param StepInfo: 检查步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: list of CheckStep
        :param CheckFlag: 校验结果，如：checkPass(校验通过)、checkNotPass(校验未通过)
        :type CheckFlag: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.BriefMsg = None
        self.StepInfo = None
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.BriefMsg = params.get("BriefMsg")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = CheckStep()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param JobName: 数据迁移任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param CreateTime: 任务创建(提交)时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 任务更新时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param StartTime: 任务开始执行时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 任务执行结束时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param BriefMsg: 迁移任务简要错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefMsg: str
        :param Status: 任务状态，取值为：created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行中)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Action: 任务操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param StepInfo: 迁移执行过程信息，在校验阶段显示校验过程步骤信息，在迁移阶段会显示迁移步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param SrcInfo: 源实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param DstInfo: 目标端信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param CompareTask: 数据一致性校验结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param RunMode: 运行模式，取值如：immediate(表示立即运行)、timed(表示定时运行)
注意：此字段可能返回 null，表示取不到有效值。
        :type RunMode: str
        :param ExpectRunTime: 期待启动时间，当RunMode取值为timed时，此值必填，形如："2006-01-02 15:04:05"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectRunTime: str
        :param MigrateOption: 迁移选项，描述任务如何执行迁移等一系列配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param CheckStepInfo: 校验任务运行详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckStepInfo: :class:`tencentcloud.dts.v20211206.models.CheckStepInfo`
        :param TradeInfo: 描述计费相关的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param ErrorInfo: 任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: list of ErrorInfoItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.JobName = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.EndTime = None
        self.BriefMsg = None
        self.Status = None
        self.Action = None
        self.StepInfo = None
        self.SrcInfo = None
        self.DstInfo = None
        self.CompareTask = None
        self.Tags = None
        self.RunMode = None
        self.ExpectRunTime = None
        self.MigrateOption = None
        self.CheckStepInfo = None
        self.TradeInfo = None
        self.ErrorInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.BriefMsg = params.get("BriefMsg")
        self.Status = params.get("Status")
        if params.get("Action") is not None:
            self.Action = MigrateAction()
            self.Action._deserialize(params.get("Action"))
        if params.get("StepInfo") is not None:
            self.StepInfo = MigrateDetailInfo()
            self.StepInfo._deserialize(params.get("StepInfo"))
        if params.get("SrcInfo") is not None:
            self.SrcInfo = DBEndpointInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DBEndpointInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        if params.get("CompareTask") is not None:
            self.CompareTask = CompareTaskInfo()
            self.CompareTask._deserialize(params.get("CompareTask"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RunMode = params.get("RunMode")
        self.ExpectRunTime = params.get("ExpectRunTime")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        if params.get("CheckStepInfo") is not None:
            self.CheckStepInfo = CheckStepInfo()
            self.CheckStepInfo._deserialize(params.get("CheckStepInfo"))
        if params.get("TradeInfo") is not None:
            self.TradeInfo = TradeInfo()
            self.TradeInfo._deserialize(params.get("TradeInfo"))
        if params.get("ErrorInfo") is not None:
            self.ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfoItem()
                obj._deserialize(item)
                self.ErrorInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMigrationJobsRequest(AbstractModel):
    """DescribeMigrationJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID，如：dts-amm1jw5q
        :type JobId: str
        :param JobName: 数据迁移任务名称
        :type JobName: str
        :param Status: 数据迁移任务状态，可取值包括：created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行中)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)
        :type Status: list of str
        :param SrcInstanceId: 源实例ID，格式如：cdb-c1nl9rpv
        :type SrcInstanceId: str
        :param SrcRegion: 源实例地域，如：ap-guangzhou
        :type SrcRegion: str
        :param SrcDatabaseType: 源实例数据库类型，如：sqlserver,mysql,mongodb,redis,tendis,keewidb,clickhouse,cynosdbmysql,percona,tdsqlpercona,mariadb,tdsqlmysql,postgresql
        :type SrcDatabaseType: list of str
        :param SrcAccessType: 源实例接入类型，值包括：extranet(外网)、vpncloud(云vpn接入的实例)、dcg(专线接入的实例)、ccn(云联网接入的实例)、cdb(云上cdb实例)、cvm(cvm自建实例)
        :type SrcAccessType: list of str
        :param DstInstanceId: 目标实例ID，格式如：cdb-c1nl9rpv
        :type DstInstanceId: str
        :param DstRegion: 目标实例地域，如：ap-guangzhou
        :type DstRegion: str
        :param DstDatabaseType: 目标源实例数据库类型，如：sqlserver,mysql,mongodb,redis,tendis,keewidb,clickhouse,cynosdbmysql,percona,tdsqlpercona,mariadb,tdsqlmysql,postgresql
        :type DstDatabaseType: list of str
        :param DstAccessType: 目标实例接入类型，值包括：extranet(外网)、vpncloud(云vpn接入的实例)、dcg(专线接入的实例)、ccn(云联网接入的实例)、cdb(云上cdb实例)、cvm(cvm自建实例)
        :type DstAccessType: list of str
        :param RunMode: 任务运行模式，值包括：immediate(立即运行)，timed(定时运行)
        :type RunMode: str
        :param OrderSeq: 排序方式，可能取值为asc、desc，默认按照创建时间倒序
        :type OrderSeq: str
        :param Limit: 返回实例数量，默认20，有效区间[1,100]
        :type Limit: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param TagFilters: 标签过滤
        :type TagFilters: list of TagFilter
        """
        self.JobId = None
        self.JobName = None
        self.Status = None
        self.SrcInstanceId = None
        self.SrcRegion = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.DstInstanceId = None
        self.DstRegion = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.RunMode = None
        self.OrderSeq = None
        self.Limit = None
        self.Offset = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Status = params.get("Status")
        self.SrcInstanceId = params.get("SrcInstanceId")
        self.SrcRegion = params.get("SrcRegion")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        self.DstInstanceId = params.get("DstInstanceId")
        self.DstRegion = params.get("DstRegion")
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        self.RunMode = params.get("RunMode")
        self.OrderSeq = params.get("OrderSeq")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationJobsResponse(AbstractModel):
    """DescribeMigrationJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 迁移任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param JobList: 迁移任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobList: list of JobItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = JobItem()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSyncJobsRequest(AbstractModel):
    """DescribeSyncJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id，如sync-werwfs23
        :type JobId: str
        :param JobName: 同步任务名
        :type JobName: str
        :param Order: 排序字段，可以取值为CreateTime
        :type Order: str
        :param OrderSeq: 排序方式，升序为ASC，降序为DESC，默认为CreateTime降序
        :type OrderSeq: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回同步任务实例数量，默认20，有效区间[1,100]
        :type Limit: int
        :param Status: 状态集合，如Initialized,CheckPass,Running,ResumableErr,Stopped
        :type Status: list of str
        :param RunMode: 运行模式，如Immediate:立即运行，Timed:定时运行
        :type RunMode: str
        :param JobType: 任务类型，如mysql2mysql：msyql同步到mysql
        :type JobType: str
        :param PayMode: 付费类型，PrePay：预付费，PostPay：后付费
        :type PayMode: str
        :param TagFilters: tag
        :type TagFilters: list of TagFilter
        """
        self.JobId = None
        self.JobName = None
        self.Order = None
        self.OrderSeq = None
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.RunMode = None
        self.JobType = None
        self.PayMode = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Order = params.get("Order")
        self.OrderSeq = params.get("OrderSeq")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.RunMode = params.get("RunMode")
        self.JobType = params.get("JobType")
        self.PayMode = params.get("PayMode")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 任务数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param JobList: 任务详情数组
注意：此字段可能返回 null，表示取不到有效值。
        :type JobList: list of SyncJobInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = SyncJobInfo()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyMigrateJobRequest(AbstractModel):
    """DestroyMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyMigrateJobResponse(AbstractModel):
    """DestroyMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DestroySyncJobRequest(AbstractModel):
    """DestroySyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroySyncJobResponse(AbstractModel):
    """DestroySyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetailCheckItem(AbstractModel):
    """每个检查步骤里的具体检查项

    """

    def __init__(self):
        r"""
        :param CheckItemName: 检查项的名称，如：源实例权限检查
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckItemName: str
        :param Description: 检查项详细内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CheckResult: pass(通过)，failed(失败), warning(校验有警告，但仍通过)
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckResult: str
        :param FailureReason: 检查项失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param Solution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param ErrorLog: 运行报错日志
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorLog: list of str
        :param HelpDoc: 详细帮助的文档链接
注意：此字段可能返回 null，表示取不到有效值。
        :type HelpDoc: list of str
        :param SkipInfo: 跳过风险文案
注意：此字段可能返回 null，表示取不到有效值。
        :type SkipInfo: str
        """
        self.CheckItemName = None
        self.Description = None
        self.CheckResult = None
        self.FailureReason = None
        self.Solution = None
        self.ErrorLog = None
        self.HelpDoc = None
        self.SkipInfo = None


    def _deserialize(self, params):
        self.CheckItemName = params.get("CheckItemName")
        self.Description = params.get("Description")
        self.CheckResult = params.get("CheckResult")
        self.FailureReason = params.get("FailureReason")
        self.Solution = params.get("Solution")
        self.ErrorLog = params.get("ErrorLog")
        self.HelpDoc = params.get("HelpDoc")
        self.SkipInfo = params.get("SkipInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceDetail(AbstractModel):
    """数据不一致的表详情

    """

    def __init__(self):
        r"""
        :param TotalCount: 数据不一致的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 校验不一致的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DifferenceItem
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DifferenceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceItem(AbstractModel):
    """校验不一致的表详情

    """

    def __init__(self):
        r"""
        :param Db: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Db: str
        :param Table: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param Chunk: 分块号
注意：此字段可能返回 null，表示取不到有效值。
        :type Chunk: int
        :param SrcItem: 源库数值
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcItem: str
        :param DstItem: 目标库数值
注意：此字段可能返回 null，表示取不到有效值。
        :type DstItem: str
        :param IndexName: 索引名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param LowerBoundary: 索引下边界
注意：此字段可能返回 null，表示取不到有效值。
        :type LowerBoundary: str
        :param UpperBoundary: 索引上边界
注意：此字段可能返回 null，表示取不到有效值。
        :type UpperBoundary: str
        :param CostTime: 对比消耗时间,单位为 ms
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: float
        :param FinishedAt: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedAt: str
        """
        self.Db = None
        self.Table = None
        self.Chunk = None
        self.SrcItem = None
        self.DstItem = None
        self.IndexName = None
        self.LowerBoundary = None
        self.UpperBoundary = None
        self.CostTime = None
        self.FinishedAt = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.Table = params.get("Table")
        self.Chunk = params.get("Chunk")
        self.SrcItem = params.get("SrcItem")
        self.DstItem = params.get("DstItem")
        self.IndexName = params.get("IndexName")
        self.LowerBoundary = params.get("LowerBoundary")
        self.UpperBoundary = params.get("UpperBoundary")
        self.CostTime = params.get("CostTime")
        self.FinishedAt = params.get("FinishedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Endpoint(AbstractModel):
    """数据同步中的描述源端和目的端的信息

    """

    def __init__(self):
        r"""
        :param Region: 地域英文名，如：ap-guangzhou
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Role: tdsql mysql版的节点类型，枚举值为proxy、set
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param DbKernel: 数据库内核类型，tdsql中用于区分不同内核：percona,mariadb,mysql
注意：此字段可能返回 null，表示取不到有效值。
        :type DbKernel: str
        :param InstanceId: 数据库实例ID，格式如：cdb-powiqx8q
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Ip: 实例的IP地址，接入类型为非cdb时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Port: 实例端口，接入类型为非cdb时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param User: 用户名，对于访问需要用户名密码认证的实例必填
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param Password: 密码，对于访问需要用户名密码认证的实例必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param DbName: 数据库名，数据库为cdwpg时，需要提供
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param VpcId: 私有网络ID，对于私有网络、专线、VPN的接入方式此项必填，格式如：vpc-92jblxto
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 私有网络下的子网ID，对于私有网络、专线、VPN的接入方式此项必填，格式如：subnet-3paxmkdz
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param CvmInstanceId: CVM实例短ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要传递此字段
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstanceId: str
        :param UniqDcgId: 专线网关ID，对于专线接入类型此项必填，格式如：dcg-0rxtqqxb
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqDcgId: str
        :param UniqVpnGwId: VPN网关ID，对于vpn接入类型此项必填，格式如：vpngw-9ghexg7q
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpnGwId: str
        :param CcnId: 云联网ID，对于云联网接入类型此项必填，如：ccn-afp6kltc
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnId: str
        :param Supplier: 云厂商类型，当实例为RDS实例时，填写为aliyun, 其他情况均填写others，默认为others
注意：此字段可能返回 null，表示取不到有效值。
        :type Supplier: str
        :param EngineVersion: 数据库版本，当实例为RDS实例时才有效，其他实例忽略，格式如：5.6或者5.7，默认为5.6
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineVersion: str
        :param Account: 实例所属账号，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param AccountMode: 资源所属账号 为空或self(表示本账号内资源)、other(表示跨账号资源)
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountMode: str
        :param AccountRole: 跨账号同步时的角色，只允许[a-zA-Z0-9\-\_]+，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountRole: str
        :param RoleExternalId: 外部角色id
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleExternalId: str
        :param TmpSecretId: 临时密钥Id，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param TmpSecretKey: 临时密钥Key，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        :param TmpToken: 临时Token，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpToken: str
        :param EncryptConn: 是否走加密传输、UnEncrypted表示不走加密传输，Encrypted表示走加密传输，默认UnEncrypted
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptConn: str
        """
        self.Region = None
        self.Role = None
        self.DbKernel = None
        self.InstanceId = None
        self.Ip = None
        self.Port = None
        self.User = None
        self.Password = None
        self.DbName = None
        self.VpcId = None
        self.SubnetId = None
        self.CvmInstanceId = None
        self.UniqDcgId = None
        self.UniqVpnGwId = None
        self.CcnId = None
        self.Supplier = None
        self.EngineVersion = None
        self.Account = None
        self.AccountMode = None
        self.AccountRole = None
        self.RoleExternalId = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.TmpToken = None
        self.EncryptConn = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Role = params.get("Role")
        self.DbKernel = params.get("DbKernel")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.DbName = params.get("DbName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.UniqDcgId = params.get("UniqDcgId")
        self.UniqVpnGwId = params.get("UniqVpnGwId")
        self.CcnId = params.get("CcnId")
        self.Supplier = params.get("Supplier")
        self.EngineVersion = params.get("EngineVersion")
        self.Account = params.get("Account")
        self.AccountMode = params.get("AccountMode")
        self.AccountRole = params.get("AccountRole")
        self.RoleExternalId = params.get("RoleExternalId")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.TmpToken = params.get("TmpToken")
        self.EncryptConn = params.get("EncryptConn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfoItem(AbstractModel):
    """任务错误信息

    """

    def __init__(self):
        r"""
        :param Code: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Solution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param ErrorLog: 错误日志信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorLog: str
        :param HelpDoc: 文档提示
注意：此字段可能返回 null，表示取不到有效值。
        :type HelpDoc: str
        """
        self.Code = None
        self.Solution = None
        self.ErrorLog = None
        self.HelpDoc = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Solution = params.get("Solution")
        self.ErrorLog = params.get("ErrorLog")
        self.HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMigrateJobRequest(AbstractModel):
    """IsolateMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMigrateJobResponse(AbstractModel):
    """IsolateMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IsolateSyncJobRequest(AbstractModel):
    """IsolateSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSyncJobResponse(AbstractModel):
    """IsolateSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class JobItem(AbstractModel):
    """迁移任务列表

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param JobName: 数据迁移任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param CreateTime: 任务创建(提交)时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 任务更新时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param StartTime: 任务开始执行时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 任务执行结束时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param BriefMsg: 迁移任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefMsg: str
        :param Status: 任务状态，取值为：creating(创建中)、created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RunMode: 任务运行模式，值包括：immediate(立即运行)，timed(定时运行)
注意：此字段可能返回 null，表示取不到有效值。
        :type RunMode: str
        :param ExpectRunTime: 期待启动时间，当RunMode取值为timed时，此值必填，形如：2022-07-11 16:20:49
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectRunTime: str
        :param Action: 任务操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param StepInfo: 迁移执行过程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param SrcInfo: 源实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param DstInfo: 目标端信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param CompareTask: 数据一致性校验结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param TradeInfo: 计费状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param AutoRetryTimeRangeMinutes: 自动重试时间段信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRetryTimeRangeMinutes: int
        """
        self.JobId = None
        self.JobName = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.EndTime = None
        self.BriefMsg = None
        self.Status = None
        self.RunMode = None
        self.ExpectRunTime = None
        self.Action = None
        self.StepInfo = None
        self.SrcInfo = None
        self.DstInfo = None
        self.CompareTask = None
        self.TradeInfo = None
        self.Tags = None
        self.AutoRetryTimeRangeMinutes = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.BriefMsg = params.get("BriefMsg")
        self.Status = params.get("Status")
        self.RunMode = params.get("RunMode")
        self.ExpectRunTime = params.get("ExpectRunTime")
        if params.get("Action") is not None:
            self.Action = MigrateAction()
            self.Action._deserialize(params.get("Action"))
        if params.get("StepInfo") is not None:
            self.StepInfo = MigrateDetailInfo()
            self.StepInfo._deserialize(params.get("StepInfo"))
        if params.get("SrcInfo") is not None:
            self.SrcInfo = DBEndpointInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DBEndpointInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        if params.get("CompareTask") is not None:
            self.CompareTask = CompareTaskInfo()
            self.CompareTask._deserialize(params.get("CompareTask"))
        if params.get("TradeInfo") is not None:
            self.TradeInfo = TradeInfo()
            self.TradeInfo._deserialize(params.get("TradeInfo"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValuePairOption(AbstractModel):
    """存放配置时的额外信息

    """

    def __init__(self):
        r"""
        :param Key: 选项key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 选项value
注意：此字段可能返回 null，表示取不到有效值。
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
        


class MigrateAction(AbstractModel):
    """任务操作信息，包含迁移任务的所有操作列表，及迁移任务在当前状态下允许的操作列表

    """

    def __init__(self):
        r"""
        :param AllAction: 任务的所有操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AllAction: list of str
        :param AllowedAction: 任务在当前状态下允许的操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowedAction: list of str
        """
        self.AllAction = None
        self.AllowedAction = None


    def _deserialize(self, params):
        self.AllAction = params.get("AllAction")
        self.AllowedAction = params.get("AllowedAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDBItem(AbstractModel):
    """查询迁移实例列表的实例对象

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Vip: 实例Vip
        :type Vip: str
        :param Vport: 实例Vport
        :type Vport: int
        :param Usable: 是否可以作为迁移对象，1-可以，0-不可以
        :type Usable: int
        :param Hint: 不可以作为迁移对象的原因
        :type Hint: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.Vport = None
        self.Usable = None
        self.Hint = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Usable = params.get("Usable")
        self.Hint = params.get("Hint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDetailInfo(AbstractModel):
    """迁移执行过程信息

    """

    def __init__(self):
        r"""
        :param StepAll: 总步骤数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepAll: int
        :param StepNow: 当前步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNow: int
        :param MasterSlaveDistance: 主从差距，MB；只在任务正常，迁移或者同步的最后一步（追Binlog的阶段才有校），如果是非法值，返回-1
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: 主从差距，秒；只在任务正常，迁移或者同步的最后一步（追Binlog的阶段才有校），如果是非法值，返回-1
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondsBehindMaster: int
        :param StepInfo: 步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: list of StepDetailInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = StepDetailInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOption(AbstractModel):
    """迁移选项，描述任务如何执行迁移等一系列配置信息

    """

    def __init__(self):
        r"""
        :param DatabaseTable: 迁移对象选项，需要告知迁移服务迁移哪些库表对象
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseTable: :class:`tencentcloud.dts.v20211206.models.DatabaseTableObject`
        :param MigrateType: 迁移类型，full(全量迁移)，structure(结构迁移)，fullAndIncrement(全量加增量迁移)， 默认为fullAndIncrement
注意：此字段可能返回 null，表示取不到有效值。
        :type MigrateType: str
        :param Consistency: 数据一致性校验选项， 默认为不开启一致性校验
注意：此字段可能返回 null，表示取不到有效值。
        :type Consistency: :class:`tencentcloud.dts.v20211206.models.ConsistencyOption`
        :param IsMigrateAccount: 是否迁移账号，yes(迁移账号)，no(不迁移账号)
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMigrateAccount: bool
        :param IsOverrideRoot: 是否用源库Root账户覆盖目标库，值包括：false-不覆盖，true-覆盖，选择库表或者结构迁移时应该为false，注意只对旧版迁移有效
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOverrideRoot: bool
        :param IsDstReadOnly: 是否在迁移时设置目标库只读(仅对mysql有效)，true(设置只读)、false(不设置只读，默认此值)
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDstReadOnly: bool
        :param ExtraAttr: 其他附加信息，对于特定库可设置额外参数，Redis可定义如下的参数: 
["ClientOutputBufferHardLimit":512, 	从机缓冲区的硬性容量限制(MB) 	"ClientOutputBufferSoftLimit":512, 	从机缓冲区的软性容量限制(MB) 	"ClientOutputBufferPersistTime":60, 从机缓冲区的软性限制持续时间(秒) 	"ReplBacklogSize":512, 	环形缓冲区容量限制(MB) 	"ReplTimeout":120，		复制超时时间(秒) ]
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraAttr: list of KeyValuePairOption
        """
        self.DatabaseTable = None
        self.MigrateType = None
        self.Consistency = None
        self.IsMigrateAccount = None
        self.IsOverrideRoot = None
        self.IsDstReadOnly = None
        self.ExtraAttr = None


    def _deserialize(self, params):
        if params.get("DatabaseTable") is not None:
            self.DatabaseTable = DatabaseTableObject()
            self.DatabaseTable._deserialize(params.get("DatabaseTable"))
        self.MigrateType = params.get("MigrateType")
        if params.get("Consistency") is not None:
            self.Consistency = ConsistencyOption()
            self.Consistency._deserialize(params.get("Consistency"))
        self.IsMigrateAccount = params.get("IsMigrateAccount")
        self.IsOverrideRoot = params.get("IsOverrideRoot")
        self.IsDstReadOnly = params.get("IsDstReadOnly")
        if params.get("ExtraAttr") is not None:
            self.ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self.ExtraAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskNameRequest(AbstractModel):
    """ModifyCompareTaskName请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 迁移任务 Id
        :type JobId: str
        :param CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        :param TaskName: 一致性校验任务名称
        :type TaskName: str
        """
        self.JobId = None
        self.CompareTaskId = None
        self.TaskName = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        self.TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskNameResponse(AbstractModel):
    """ModifyCompareTaskName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCompareTaskRequest(AbstractModel):
    """ModifyCompareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务 Id
        :type JobId: str
        :param CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        :param TaskName: 任务名称
        :type TaskName: str
        :param ObjectMode: 数据对比对象模式，sameAsMigrate(全部迁移对象， 默认为此项配置)、custom(自定义)，注意自定义对比对象必须是迁移对象的子集
        :type ObjectMode: str
        :param Objects: 对比对象，若CompareObjectMode取值为custom，则此项必填
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param Options: 一致性校验选项
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        self.JobId = None
        self.CompareTaskId = None
        self.TaskName = None
        self.ObjectMode = None
        self.Objects = None
        self.Options = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        self.TaskName = params.get("TaskName")
        self.ObjectMode = params.get("ObjectMode")
        if params.get("Objects") is not None:
            self.Objects = CompareObject()
            self.Objects._deserialize(params.get("Objects"))
        if params.get("Options") is not None:
            self.Options = CompareOptions()
            self.Options._deserialize(params.get("Options"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskResponse(AbstractModel):
    """ModifyCompareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrateJobSpecRequest(AbstractModel):
    """ModifyMigrateJobSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务id
        :type JobId: str
        :param NewInstanceClass: 新实例规格大小，包括：micro、small、medium、large、xlarge、2xlarge
        :type NewInstanceClass: str
        """
        self.JobId = None
        self.NewInstanceClass = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NewInstanceClass = params.get("NewInstanceClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobSpecResponse(AbstractModel):
    """ModifyMigrateJobSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrateNameRequest(AbstractModel):
    """ModifyMigrateName请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 迁移任务id
        :type JobId: str
        :param JobName: 修改后的迁移任务名
        :type JobName: str
        """
        self.JobId = None
        self.JobName = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateNameResponse(AbstractModel):
    """ModifyMigrateName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationJobRequest(AbstractModel):
    """ModifyMigrationJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务id
        :type JobId: str
        :param RunMode: 运行模式，取值如：immediate(表示立即运行)、timed(表示定时运行)
        :type RunMode: str
        :param MigrateOption: 迁移任务配置选项，描述任务如何执行迁移等一系列配置信息
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param SrcInfo: 源实例信息
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param JobName: 迁移任务名称，最大长度128
        :type JobName: str
        :param ExpectRunTime: 期待启动时间，当RunMode取值为timed时，此值必填，形如："2006-01-02 15:04:05"
        :type ExpectRunTime: str
        :param Tags: 标签信息
        :type Tags: list of TagItem
        :param AutoRetryTimeRangeMinutes: 自动重试的时间段、可设置5至720分钟、0表示不重试
        :type AutoRetryTimeRangeMinutes: int
        """
        self.JobId = None
        self.RunMode = None
        self.MigrateOption = None
        self.SrcInfo = None
        self.DstInfo = None
        self.JobName = None
        self.ExpectRunTime = None
        self.Tags = None
        self.AutoRetryTimeRangeMinutes = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RunMode = params.get("RunMode")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        if params.get("SrcInfo") is not None:
            self.SrcInfo = DBEndpointInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DBEndpointInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.JobName = params.get("JobName")
        self.ExpectRunTime = params.get("ExpectRunTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationJobResponse(AbstractModel):
    """ModifyMigrationJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Objects(AbstractModel):
    """同步的数据库对对象描述

    """

    def __init__(self):
        r"""
        :param Mode: 迁移对象类型 Partial(部分对象)
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param Databases: 同步对象，当 Mode 为 Partial 时，不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of Database
        :param AdvancedObjects: 高级对象类型，如function、procedure，当需要同步高级对象时，初始化类型必须包含结构初始化类型，即Options.InitType字段值为Structure或Full
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedObjects: list of str
        :param OnlineDDL: OnlineDDL类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineDDL: :class:`tencentcloud.dts.v20211206.models.OnlineDDL`
        """
        self.Mode = None
        self.Databases = None
        self.AdvancedObjects = None
        self.OnlineDDL = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.AdvancedObjects = params.get("AdvancedObjects")
        if params.get("OnlineDDL") is not None:
            self.OnlineDDL = OnlineDDL()
            self.OnlineDDL._deserialize(params.get("OnlineDDL"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OnlineDDL(AbstractModel):
    """OnlineDDL类型

    """


class Options(AbstractModel):
    """数据同步中的选项

    """

    def __init__(self):
        r"""
        :param InitType: 同步初始化选项，Data(全量数据初始化)、Structure(结构初始化)、Full(全量数据且结构初始化，默认)、None(仅增量)
注意：此字段可能返回 null，表示取不到有效值。
        :type InitType: str
        :param DealOfExistSameTable: 同名表的处理，ReportErrorAfterCheck(前置校验并报错，默认)、InitializeAfterDelete(删除并重新初始化)、ExecuteAfterIgnore(忽略并继续执行)
注意：此字段可能返回 null，表示取不到有效值。
        :type DealOfExistSameTable: str
        :param ConflictHandleType: 冲突处理选项，ReportError(报错，默认为该值)、Ignore(忽略)、Cover(覆盖)、ConditionCover(条件覆盖)
注意：此字段可能返回 null，表示取不到有效值。
        :type ConflictHandleType: str
        :param AddAdditionalColumn: 是否添加附加列
注意：此字段可能返回 null，表示取不到有效值。
        :type AddAdditionalColumn: bool
        :param OpTypes: 所要同步的DML和DDL的选项，Insert(插入操作)、Update(更新操作)、Delete(删除操作)、DDL(结构同步)， 不填（不选），PartialDDL(自定义,和DdlOptions一起起作用 )
注意：此字段可能返回 null，表示取不到有效值。
        :type OpTypes: list of str
        :param ConflictHandleOption: 冲突处理的详细选项，如条件覆盖中的条件行和条件操作
注意：此字段可能返回 null，表示取不到有效值。
        :type ConflictHandleOption: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        :param DdlOptions: DDL同步选项，具体描述要同步那些DDL
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlOptions: list of DdlOption
        """
        self.InitType = None
        self.DealOfExistSameTable = None
        self.ConflictHandleType = None
        self.AddAdditionalColumn = None
        self.OpTypes = None
        self.ConflictHandleOption = None
        self.DdlOptions = None


    def _deserialize(self, params):
        self.InitType = params.get("InitType")
        self.DealOfExistSameTable = params.get("DealOfExistSameTable")
        self.ConflictHandleType = params.get("ConflictHandleType")
        self.AddAdditionalColumn = params.get("AddAdditionalColumn")
        self.OpTypes = params.get("OpTypes")
        if params.get("ConflictHandleOption") is not None:
            self.ConflictHandleOption = ConflictHandleOption()
            self.ConflictHandleOption._deserialize(params.get("ConflictHandleOption"))
        if params.get("DdlOptions") is not None:
            self.DdlOptions = []
            for item in params.get("DdlOptions"):
                obj = DdlOption()
                obj._deserialize(item)
                self.DdlOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseMigrateJobRequest(AbstractModel):
    """PauseMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseMigrateJobResponse(AbstractModel):
    """PauseMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PauseSyncJobRequest(AbstractModel):
    """PauseSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseSyncJobResponse(AbstractModel):
    """PauseSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProcessProgress(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        r"""
        :param Status: 步骤的状态， 包括：notStarted(未开始)、running(运行中)、success(成功)、failed(失败)等
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Percent: 进度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param StepAll: 总的步骤数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepAll: int
        :param StepNow: 当前进行的步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNow: int
        :param Message: 当前步骤输出提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Steps: 步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Steps: list of StepDetailInfo
        """
        self.Status = None
        self.Percent = None
        self.StepAll = None
        self.StepNow = None
        self.Message = None
        self.Steps = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Message = params.get("Message")
        if params.get("Steps") is not None:
            self.Steps = []
            for item in params.get("Steps"):
                obj = StepDetailInfo()
                obj._deserialize(item)
                self.Steps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStepTip(AbstractModel):
    """错误信息及告警信息对象

    """

    def __init__(self):
        r"""
        :param Message: 提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Solution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param HelpDoc: 文档提示
注意：此字段可能返回 null，表示取不到有效值。
        :type HelpDoc: str
        """
        self.Message = None
        self.Solution = None
        self.HelpDoc = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Solution = params.get("Solution")
        self.HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMigrateJobRequest(AbstractModel):
    """RecoverMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMigrateJobResponse(AbstractModel):
    """RecoverMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RecoverSyncJobRequest(AbstractModel):
    """RecoverSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步实例id（即标识一个同步作业），形如sync-werwfs23
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverSyncJobResponse(AbstractModel):
    """RecoverSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResizeSyncJobRequest(AbstractModel):
    """ResizeSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        :param NewInstanceClass: 任务规格
        :type NewInstanceClass: str
        """
        self.JobId = None
        self.NewInstanceClass = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NewInstanceClass = params.get("NewInstanceClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeSyncJobResponse(AbstractModel):
    """ResizeSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeMigrateJobRequest(AbstractModel):
    """ResumeMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        :param ResumeOption: 恢复任务的模式，目前的取值有：clearData 清空目标实例数据，overwrite 以覆盖写的方式执行任务，normal 跟正常流程一样，不做额外动作
        :type ResumeOption: str
        """
        self.JobId = None
        self.ResumeOption = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ResumeOption = params.get("ResumeOption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeMigrateJobResponse(AbstractModel):
    """ResumeMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeSyncJobRequest(AbstractModel):
    """ResumeSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeSyncJobResponse(AbstractModel):
    """ResumeSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoleItem(AbstractModel):
    """角色对象，postgresql独有参数

    """

    def __init__(self):
        r"""
        :param RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param NewRoleName: 迁移后的角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NewRoleName: str
        """
        self.RoleName = None
        self.NewRoleName = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.NewRoleName = params.get("NewRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCheckItemRequest(AbstractModel):
    """SkipCheckItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        :param StepIds: 需要跳过校验项的步骤id，需要通过DescribeMigrationCheckJob接口返回StepInfo[i].StepId字段获取，例如：["OptimizeCheck"]
        :type StepIds: list of str
        :param ForeignKeyFlag: 当出现外键依赖检查导致校验不通过时、可以通过该字段选择是否迁移外键依赖，当StepIds包含ConstraintCheck且该字段值为shield时表示不迁移外键依赖、当StepIds包含ConstraintCheck且值为migrate时表示迁移外键依赖
        :type ForeignKeyFlag: str
        """
        self.JobId = None
        self.StepIds = None
        self.ForeignKeyFlag = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StepIds = params.get("StepIds")
        self.ForeignKeyFlag = params.get("ForeignKeyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCheckItemResponse(AbstractModel):
    """SkipCheckItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param Message: 跳过的提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Message = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.RequestId = params.get("RequestId")


class SkipSyncCheckItemRequest(AbstractModel):
    """SkipSyncCheckItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务id，如：sync-4ddgid2
        :type JobId: str
        :param StepIds: 需要跳过校验项的步骤id，需要通过`DescribeCheckSyncJobResult`接口返回StepInfos[i].StepId字段获取，例如：["OptimizeCheck"]
        :type StepIds: list of str
        """
        self.JobId = None
        self.StepIds = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StepIds = params.get("StepIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipSyncCheckItemResponse(AbstractModel):
    """SkipSyncCheckItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SkippedDetail(AbstractModel):
    """跳过校验的表详情

    """

    def __init__(self):
        r"""
        :param TotalCount: 跳过的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 跳过校验的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SkippedItem
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SkippedItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkippedItem(AbstractModel):
    """跳过校验的表详情

    """

    def __init__(self):
        r"""
        :param Db: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Db: str
        :param Table: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param Reason: 未发起检查的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self.Db = None
        self.Table = None
        self.Reason = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.Table = params.get("Table")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCompareRequest(AbstractModel):
    """StartCompare请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 迁移任务 Id
        :type JobId: str
        :param CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        """
        self.JobId = None
        self.CompareTaskId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCompareResponse(AbstractModel):
    """StartCompare返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartSyncJobRequest(AbstractModel):
    """StartSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StepDetailInfo(AbstractModel):
    """步骤信息

    """

    def __init__(self):
        r"""
        :param StepNo: 步骤序列
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNo: int
        :param StepName: 步骤展现名称
注意：此字段可能返回 null，表示取不到有效值。
        :type StepName: str
        :param StepId: 步骤英文标识
注意：此字段可能返回 null，表示取不到有效值。
        :type StepId: str
        :param Status: 步骤状态:success(成功)、failed(失败)、running(执行中)、notStarted(未执行)、默认为notStarted
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param StartTime: 当前步骤开始的时间，格式为"yyyy-mm-dd hh:mm:ss"，该字段不存在或者为空是无意义 注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param StepMessage: 步骤错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepMessage: str
        :param Percent: 执行进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param Errors: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of ProcessStepTip
        :param Warnings: 告警提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Warnings: list of ProcessStepTip
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None
        self.StartTime = None
        self.StepMessage = None
        self.Percent = None
        self.Errors = None
        self.Warnings = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.StepMessage = params.get("StepMessage")
        self.Percent = params.get("Percent")
        if params.get("Errors") is not None:
            self.Errors = []
            for item in params.get("Errors"):
                obj = ProcessStepTip()
                obj._deserialize(item)
                self.Errors.append(obj)
        if params.get("Warnings") is not None:
            self.Warnings = []
            for item in params.get("Warnings"):
                obj = ProcessStepTip()
                obj._deserialize(item)
                self.Warnings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepInfo(AbstractModel):
    """单个步骤的详细信息

    """

    def __init__(self):
        r"""
        :param StepNo: 步骤编号
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNo: int
        :param StepName: 步骤名
注意：此字段可能返回 null，表示取不到有效值。
        :type StepName: str
        :param StepId: 步骤标号
注意：此字段可能返回 null，表示取不到有效值。
        :type StepId: str
        :param Status: 当前状态，是否完成
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param StartTime: 步骤开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param Errors: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of StepTip
        :param Warnings: 警告信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Warnings: list of StepTip
        :param Progress: 当前步骤进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None
        self.StartTime = None
        self.Errors = None
        self.Warnings = None
        self.Progress = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        if params.get("Errors") is not None:
            self.Errors = []
            for item in params.get("Errors"):
                obj = StepTip()
                obj._deserialize(item)
                self.Errors.append(obj)
        if params.get("Warnings") is not None:
            self.Warnings = []
            for item in params.get("Warnings"):
                obj = StepTip()
                obj._deserialize(item)
                self.Warnings.append(obj)
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepTip(AbstractModel):
    """当前步骤错误信息或者警告信息

    """

    def __init__(self):
        r"""
        :param Code: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Message: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Solution: 解决方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param HelpDoc: 帮助文档
注意：此字段可能返回 null，表示取不到有效值。
        :type HelpDoc: str
        :param SkipInfo: 当前步骤跳过信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SkipInfo: str
        """
        self.Code = None
        self.Message = None
        self.Solution = None
        self.HelpDoc = None
        self.SkipInfo = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.Solution = params.get("Solution")
        self.HelpDoc = params.get("HelpDoc")
        self.SkipInfo = params.get("SkipInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCompareRequest(AbstractModel):
    """StopCompare请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 迁移任务 Id
        :type JobId: str
        :param CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        """
        self.JobId = None
        self.CompareTaskId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCompareResponse(AbstractModel):
    """StopCompare返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopSyncJobRequest(AbstractModel):
    """StopSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSyncJobResponse(AbstractModel):
    """StopSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SyncDetailInfo(AbstractModel):
    """同步任务的步骤信息

    """

    def __init__(self):
        r"""
        :param StepAll: 总步骤数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepAll: int
        :param StepNow: 当前步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNow: int
        :param Progress: 总体进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param CurrentStepProgress: 当前步骤进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentStepProgress: int
        :param MasterSlaveDistance: 同步两端数据量差距
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: 同步两端时间差距
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondsBehindMaster: int
        :param Message: 总体描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param StepInfos: 详细步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfos: list of StepInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.CurrentStepProgress = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.Message = None
        self.StepInfos = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        self.CurrentStepProgress = params.get("CurrentStepProgress")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        self.Message = params.get("Message")
        if params.get("StepInfos") is not None:
            self.StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self.StepInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncJobInfo(AbstractModel):
    """同步任务信息

    """

    def __init__(self):
        r"""
        :param JobId: 同步任务id，如：sync-btso140
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param JobName: 同步任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param PayMode: 付款方式，PostPay(按量付费)、PrePay(包年包月)
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param RunMode: 运行模式，Immediate(表示立即运行，默认为此项值)、Timed(表示定时运行)
注意：此字段可能返回 null，表示取不到有效值。
        :type RunMode: str
        :param ExpectRunTime: 期待运行时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectRunTime: str
        :param AllActions: 支持的所有操作
注意：此字段可能返回 null，表示取不到有效值。
        :type AllActions: list of str
        :param Actions: 当前状态能进行的操作
注意：此字段可能返回 null，表示取不到有效值。
        :type Actions: list of str
        :param Options: 同步选项
注意：此字段可能返回 null，表示取不到有效值。
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param Objects: 同步库表对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param Specification: 任务规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param ExpireTime: 过期时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param SrcRegion: 源端地域，如：ap-guangzhou等
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcRegion: str
        :param SrcDatabaseType: 源端数据库类型，mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcDatabaseType: str
        :param SrcAccessType: 源端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcAccessType: str
        :param SrcInfo: 源端信息，单节点数据库使用
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param DstRegion: 目标端地域，如：ap-guangzhou等
注意：此字段可能返回 null，表示取不到有效值。
        :type DstRegion: str
        :param DstDatabaseType: 目标端数据库类型，mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
注意：此字段可能返回 null，表示取不到有效值。
        :type DstDatabaseType: str
        :param DstAccessType: 目标端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)
注意：此字段可能返回 null，表示取不到有效值。
        :type DstAccessType: str
        :param DstInfo: 目标端信息，单节点数据库使用
注意：此字段可能返回 null，表示取不到有效值。
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param CreateTime: 创建时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param StartTime: 开始时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param Status: 任务状态，UnInitialized(未初始化)、Initialized(已初始化)、Checking(校验中)、CheckPass(校验通过)、CheckNotPass(校验不通过)、ReadyRunning(准备运行)、Running(运行中)、Pausing(暂停中)、Paused(已暂停)、Stopping(停止中)、Stopped(已结束)、ResumableErr(任务错误)、Resuming(恢复中)、Failed(失败)、Released(已释放)、Resetting(重置中)、Unknown(未知)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param EndTime: 结束时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Tags: 标签相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param Detail: 同步任务运行步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: :class:`tencentcloud.dts.v20211206.models.SyncDetailInfo`
        :param TradeStatus: 用于计费的状态，可能取值有：Normal(正常状态)、Resizing(变配中)、Renewing(续费中)、Isolating(隔离中)、Isolated(已隔离)、Offlining(下线中)、Offlined(已下线)、NotBilled(未计费)、Recovering(解隔离)、PostPay2Prepaying(按量计费转包年包月中)、PrePay2Postpaying(包年包月转按量计费中)
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeStatus: str
        :param InstanceClass: 同步链路规格，如micro,small,medium,large
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceClass: str
        :param AutoRenew: 自动续费标识，当PayMode值为PrePay则此项配置有意义，取值为：1（表示自动续费）、0（不自动续费）
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenew: int
        :param OfflineTime: 下线时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTime: str
        :param AutoRetryTimeRangeMinutes: 自动重试时间段设置
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRetryTimeRangeMinutes: int
        """
        self.JobId = None
        self.JobName = None
        self.PayMode = None
        self.RunMode = None
        self.ExpectRunTime = None
        self.AllActions = None
        self.Actions = None
        self.Options = None
        self.Objects = None
        self.Specification = None
        self.ExpireTime = None
        self.SrcRegion = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstRegion = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.CreateTime = None
        self.StartTime = None
        self.Status = None
        self.EndTime = None
        self.Tags = None
        self.Detail = None
        self.TradeStatus = None
        self.InstanceClass = None
        self.AutoRenew = None
        self.OfflineTime = None
        self.AutoRetryTimeRangeMinutes = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.PayMode = params.get("PayMode")
        self.RunMode = params.get("RunMode")
        self.ExpectRunTime = params.get("ExpectRunTime")
        self.AllActions = params.get("AllActions")
        self.Actions = params.get("Actions")
        if params.get("Options") is not None:
            self.Options = Options()
            self.Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self.Objects = Objects()
            self.Objects._deserialize(params.get("Objects"))
        self.Specification = params.get("Specification")
        self.ExpireTime = params.get("ExpireTime")
        self.SrcRegion = params.get("SrcRegion")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = Endpoint()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstRegion = params.get("DstRegion")
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = Endpoint()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.Status = params.get("Status")
        self.EndTime = params.get("EndTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Detail") is not None:
            self.Detail = SyncDetailInfo()
            self.Detail._deserialize(params.get("Detail"))
        self.TradeStatus = params.get("TradeStatus")
        self.InstanceClass = params.get("InstanceClass")
        self.AutoRenew = params.get("AutoRenew")
        self.OfflineTime = params.get("OfflineTime")
        self.AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """数据同步库表信息描述

    """

    def __init__(self):
        r"""
        :param TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param NewTableName: 新表名
注意：此字段可能返回 null，表示取不到有效值。
        :type NewTableName: str
        :param FilterCondition: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterCondition: str
        """
        self.TableName = None
        self.NewTableName = None
        self.FilterCondition = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.NewTableName = params.get("NewTableName")
        self.FilterCondition = params.get("FilterCondition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableItem(AbstractModel):
    """表对象集合，当 TableMode 为 partial 时，此项需要填写

    """

    def __init__(self):
        r"""
        :param TableName: 迁移的表名，大小写敏感
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param NewTableName: 迁移后的表名，当TableEditMode为rename时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type NewTableName: str
        :param TmpTables: 迁移临时表，针对pt-osc等工具在迁移过程中产生的临时表同步，需要提前将可能的临时表配置在这里，当TableEditMode为pt时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpTables: list of str
        :param TableEditMode: 编辑表类型，rename(表映射)，pt(同步附加表)
注意：此字段可能返回 null，表示取不到有效值。
        :type TableEditMode: str
        """
        self.TableName = None
        self.NewTableName = None
        self.TmpTables = None
        self.TableEditMode = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.NewTableName = params.get("NewTableName")
        self.TmpTables = params.get("TmpTables")
        self.TableEditMode = params.get("TableEditMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """标签过滤

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键值
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: list of str
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
        


class TagItem(AbstractModel):
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
        


class TradeInfo(AbstractModel):
    """计费状态信息

    """

    def __init__(self):
        r"""
        :param DealName: 交易订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param LastDealName: 上一次交易订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type LastDealName: str
        :param InstanceClass: 实例规格，包括：micro、small、medium、large、xlarge、2xlarge等
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceClass: str
        :param TradeStatus: 计费任务状态， normal(计费或待计费)、resizing(变配中)、reversing(冲正中，比较短暂的状态)、isolating(隔离中，比较短暂的状态)、isolated(已隔离)、offlining(下线中)、offlined(已下线)、notBilled(未计费)
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeStatus: str
        :param ExpireTime: 到期时间，格式为"yyyy-mm-dd hh:mm:ss"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param OfflineTime: 下线时间，格式为"yyyy-mm-dd hh:mm:ss"
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTime: str
        :param IsolateTime: 隔离时间，格式为"yyyy-mm-dd hh:mm:ss"
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param OfflineReason: 下线原因
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineReason: str
        :param IsolateReason: 隔离原因
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateReason: str
        :param PayType: 付费类型，包括：postpay(后付费)、prepay(预付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type PayType: str
        :param BillingType: 任务计费类型，包括：billing(计费)、notBilling(不计费)、 promotions(促销活动中)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingType: str
        """
        self.DealName = None
        self.LastDealName = None
        self.InstanceClass = None
        self.TradeStatus = None
        self.ExpireTime = None
        self.OfflineTime = None
        self.IsolateTime = None
        self.OfflineReason = None
        self.IsolateReason = None
        self.PayType = None
        self.BillingType = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.LastDealName = params.get("LastDealName")
        self.InstanceClass = params.get("InstanceClass")
        self.TradeStatus = params.get("TradeStatus")
        self.ExpireTime = params.get("ExpireTime")
        self.OfflineTime = params.get("OfflineTime")
        self.IsolateTime = params.get("IsolateTime")
        self.OfflineReason = params.get("OfflineReason")
        self.IsolateReason = params.get("IsolateReason")
        self.PayType = params.get("PayType")
        self.BillingType = params.get("BillingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class View(AbstractModel):
    """数据同步view的描述

    """

    def __init__(self):
        r"""
        :param ViewName: view名
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        :param NewViewName: 新view名
注意：此字段可能返回 null，表示取不到有效值。
        :type NewViewName: str
        """
        self.ViewName = None
        self.NewViewName = None


    def _deserialize(self, params):
        self.ViewName = params.get("ViewName")
        self.NewViewName = params.get("NewViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewItem(AbstractModel):
    """视图对象

    """

    def __init__(self):
        r"""
        :param ViewName: 视图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        :param NewViewName: 迁移后的视图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NewViewName: str
        """
        self.ViewName = None
        self.NewViewName = None


    def _deserialize(self, params):
        self.ViewName = params.get("ViewName")
        self.NewViewName = params.get("NewViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        