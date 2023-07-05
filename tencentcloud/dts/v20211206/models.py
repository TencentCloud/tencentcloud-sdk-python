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
        :param _StepNo: 步骤编号
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNo: int
        :param _StepId: 步骤Id， 如：ConnectDBCheck、VersionCheck、SrcPrivilegeCheck等，具体校验项和源目标实例相关
注意：此字段可能返回 null，表示取不到有效值。
        :type StepId: str
        :param _StepName: 步骤名称
注意：此字段可能返回 null，表示取不到有效值。
        :type StepName: str
        :param _StepStatus: 此检查步骤的结果，pass(校验通过)、failed(校验失败)、notStarted(校验还未开始进行)、blocked(检验阻塞)、warning(校验有告警，但仍通过)
注意：此字段可能返回 null，表示取不到有效值。
        :type StepStatus: str
        :param _StepMessage: 此检查步骤的错误消息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepMessage: str
        :param _DetailCheckItems: 每个检查步骤里的具体检查项
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailCheckItems: list of DetailCheckItem
        :param _HasSkipped: 是否已跳过
注意：此字段可能返回 null，表示取不到有效值。
        :type HasSkipped: bool
        """
        self._StepNo = None
        self._StepId = None
        self._StepName = None
        self._StepStatus = None
        self._StepMessage = None
        self._DetailCheckItems = None
        self._HasSkipped = None

    @property
    def StepNo(self):
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepId(self):
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def StepName(self):
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepStatus(self):
        return self._StepStatus

    @StepStatus.setter
    def StepStatus(self, StepStatus):
        self._StepStatus = StepStatus

    @property
    def StepMessage(self):
        return self._StepMessage

    @StepMessage.setter
    def StepMessage(self, StepMessage):
        self._StepMessage = StepMessage

    @property
    def DetailCheckItems(self):
        return self._DetailCheckItems

    @DetailCheckItems.setter
    def DetailCheckItems(self, DetailCheckItems):
        self._DetailCheckItems = DetailCheckItems

    @property
    def HasSkipped(self):
        return self._HasSkipped

    @HasSkipped.setter
    def HasSkipped(self, HasSkipped):
        self._HasSkipped = HasSkipped


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepId = params.get("StepId")
        self._StepName = params.get("StepName")
        self._StepStatus = params.get("StepStatus")
        self._StepMessage = params.get("StepMessage")
        if params.get("DetailCheckItems") is not None:
            self._DetailCheckItems = []
            for item in params.get("DetailCheckItems"):
                obj = DetailCheckItem()
                obj._deserialize(item)
                self._DetailCheckItems.append(obj)
        self._HasSkipped = params.get("HasSkipped")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStepInfo(AbstractModel):
    """校验任务运行详情

    """

    def __init__(self):
        r"""
        :param _StartAt: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartAt: str
        :param _EndAt: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndAt: str
        :param _Progress: 任务步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        self._StartAt = None
        self._EndAt = None
        self._Progress = None

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress


    def _deserialize(self, params):
        self._StartAt = params.get("StartAt")
        self._EndAt = params.get("EndAt")
        if params.get("Progress") is not None:
            self._Progress = ProcessProgress()
            self._Progress._deserialize(params.get("Progress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareAbstractInfo(AbstractModel):
    """一致性校验摘要信息

    """

    def __init__(self):
        r"""
        :param _Options: 校验配置参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        :param _Objects: 一致性校验对比对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _Conclusion: 对比结论: same,different
注意：此字段可能返回 null，表示取不到有效值。
        :type Conclusion: str
        :param _Status: 任务状态: success,failed
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _TotalTables: 总的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTables: int
        :param _CheckedTables: 已校验的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckedTables: int
        :param _DifferentTables: 不一致的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DifferentTables: int
        :param _SkippedTables: 跳过校验的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SkippedTables: int
        :param _NearlyTableCount: 预估表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type NearlyTableCount: int
        :param _DifferentRows: 不一致的数据行数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DifferentRows: int
        :param _SrcSampleRows: 源库行数，当对比类型为**行数对比**时此项有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcSampleRows: int
        :param _DstSampleRows: 目标库行数，当对比类型为**行数对比**时此项有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type DstSampleRows: int
        :param _StartedAt: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedAt: str
        :param _FinishedAt: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedAt: str
        """
        self._Options = None
        self._Objects = None
        self._Conclusion = None
        self._Status = None
        self._TotalTables = None
        self._CheckedTables = None
        self._DifferentTables = None
        self._SkippedTables = None
        self._NearlyTableCount = None
        self._DifferentRows = None
        self._SrcSampleRows = None
        self._DstSampleRows = None
        self._StartedAt = None
        self._FinishedAt = None

    @property
    def Options(self):
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Objects(self):
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Conclusion(self):
        return self._Conclusion

    @Conclusion.setter
    def Conclusion(self, Conclusion):
        self._Conclusion = Conclusion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalTables(self):
        return self._TotalTables

    @TotalTables.setter
    def TotalTables(self, TotalTables):
        self._TotalTables = TotalTables

    @property
    def CheckedTables(self):
        return self._CheckedTables

    @CheckedTables.setter
    def CheckedTables(self, CheckedTables):
        self._CheckedTables = CheckedTables

    @property
    def DifferentTables(self):
        return self._DifferentTables

    @DifferentTables.setter
    def DifferentTables(self, DifferentTables):
        self._DifferentTables = DifferentTables

    @property
    def SkippedTables(self):
        return self._SkippedTables

    @SkippedTables.setter
    def SkippedTables(self, SkippedTables):
        self._SkippedTables = SkippedTables

    @property
    def NearlyTableCount(self):
        return self._NearlyTableCount

    @NearlyTableCount.setter
    def NearlyTableCount(self, NearlyTableCount):
        self._NearlyTableCount = NearlyTableCount

    @property
    def DifferentRows(self):
        return self._DifferentRows

    @DifferentRows.setter
    def DifferentRows(self, DifferentRows):
        self._DifferentRows = DifferentRows

    @property
    def SrcSampleRows(self):
        return self._SrcSampleRows

    @SrcSampleRows.setter
    def SrcSampleRows(self, SrcSampleRows):
        self._SrcSampleRows = SrcSampleRows

    @property
    def DstSampleRows(self):
        return self._DstSampleRows

    @DstSampleRows.setter
    def DstSampleRows(self, DstSampleRows):
        self._DstSampleRows = DstSampleRows

    @property
    def StartedAt(self):
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def FinishedAt(self):
        return self._FinishedAt

    @FinishedAt.setter
    def FinishedAt(self, FinishedAt):
        self._FinishedAt = FinishedAt


    def _deserialize(self, params):
        if params.get("Options") is not None:
            self._Options = CompareOptions()
            self._Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self._Objects = CompareObject()
            self._Objects._deserialize(params.get("Objects"))
        self._Conclusion = params.get("Conclusion")
        self._Status = params.get("Status")
        self._TotalTables = params.get("TotalTables")
        self._CheckedTables = params.get("CheckedTables")
        self._DifferentTables = params.get("DifferentTables")
        self._SkippedTables = params.get("SkippedTables")
        self._NearlyTableCount = params.get("NearlyTableCount")
        self._DifferentRows = params.get("DifferentRows")
        self._SrcSampleRows = params.get("SrcSampleRows")
        self._DstSampleRows = params.get("DstSampleRows")
        self._StartedAt = params.get("StartedAt")
        self._FinishedAt = params.get("FinishedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareDetailInfo(AbstractModel):
    """一致性校验详细信息

    """

    def __init__(self):
        r"""
        :param _Difference: 数据不一致的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Difference: :class:`tencentcloud.dts.v20211206.models.DifferenceDetail`
        :param _Skipped: 跳过校验的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Skipped: :class:`tencentcloud.dts.v20211206.models.SkippedDetail`
        """
        self._Difference = None
        self._Skipped = None

    @property
    def Difference(self):
        return self._Difference

    @Difference.setter
    def Difference(self, Difference):
        self._Difference = Difference

    @property
    def Skipped(self):
        return self._Skipped

    @Skipped.setter
    def Skipped(self, Skipped):
        self._Skipped = Skipped


    def _deserialize(self, params):
        if params.get("Difference") is not None:
            self._Difference = DifferenceDetail()
            self._Difference._deserialize(params.get("Difference"))
        if params.get("Skipped") is not None:
            self._Skipped = SkippedDetail()
            self._Skipped._deserialize(params.get("Skipped"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareObject(AbstractModel):
    """一致性对比对象配置

    """

    def __init__(self):
        r"""
        :param _ObjectMode: 对象模式 整实例-all,部分对象-partial
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectMode: str
        :param _ObjectItems: 对象列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectItems: list of CompareObjectItem
        :param _AdvancedObjects: 高级对象类型，如account(账号),index(索引),shardkey(片建，后面可能会调整),schema(库表结构)
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedObjects: list of str
        """
        self._ObjectMode = None
        self._ObjectItems = None
        self._AdvancedObjects = None

    @property
    def ObjectMode(self):
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def ObjectItems(self):
        return self._ObjectItems

    @ObjectItems.setter
    def ObjectItems(self, ObjectItems):
        self._ObjectItems = ObjectItems

    @property
    def AdvancedObjects(self):
        return self._AdvancedObjects

    @AdvancedObjects.setter
    def AdvancedObjects(self, AdvancedObjects):
        self._AdvancedObjects = AdvancedObjects


    def _deserialize(self, params):
        self._ObjectMode = params.get("ObjectMode")
        if params.get("ObjectItems") is not None:
            self._ObjectItems = []
            for item in params.get("ObjectItems"):
                obj = CompareObjectItem()
                obj._deserialize(item)
                self._ObjectItems.append(obj)
        self._AdvancedObjects = params.get("AdvancedObjects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareObjectItem(AbstractModel):
    """一致性校验库表对象

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param _DbMode: 数据库选择模式: all 为当前对象下的所有对象,partial 为部分对象
注意：此字段可能返回 null，表示取不到有效值。
        :type DbMode: str
        :param _SchemaName: schema名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param _TableMode: 表选择模式: all 为当前对象下的所有表对象,partial 为部分表对象
注意：此字段可能返回 null，表示取不到有效值。
        :type TableMode: str
        :param _Tables: 用于一致性校验的表配置，当 TableMode 为 partial 时，需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of CompareTableItem
        :param _ViewMode: 视图选择模式: all 为当前对象下的所有视图对象,partial 为部分视图对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewMode: str
        :param _Views: 用于一致性校验的视图配置，当 ViewMode 为 partial 时， 需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Views: list of CompareViewItem
        """
        self._DbName = None
        self._DbMode = None
        self._SchemaName = None
        self._TableMode = None
        self._Tables = None
        self._ViewMode = None
        self._Views = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableMode(self):
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._DbMode = params.get("DbMode")
        self._SchemaName = params.get("SchemaName")
        self._TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = CompareTableItem()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = CompareViewItem()
                obj._deserialize(item)
                self._Views.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareOptions(AbstractModel):
    """一致性校验选项

    """

    def __init__(self):
        r"""
        :param _Method: 对比类型：dataCheck(完整数据对比)、sampleDataCheck(抽样数据对比)、rowsCount(行数对比)
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _SampleRate: 抽样比例;范围0,100
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleRate: int
        :param _ThreadCount: 线程数，取值1-5，默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type ThreadCount: int
        """
        self._Method = None
        self._SampleRate = None
        self._ThreadCount = None

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ThreadCount(self):
        return self._ThreadCount

    @ThreadCount.setter
    def ThreadCount(self, ThreadCount):
        self._ThreadCount = ThreadCount


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._SampleRate = params.get("SampleRate")
        self._ThreadCount = params.get("ThreadCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTableItem(AbstractModel):
    """用于一致性校验的表配置

    """

    def __init__(self):
        r"""
        :param _TableName: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        """
        self._TableName = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTaskInfo(AbstractModel):
    """数据一致性校验结果

    """

    def __init__(self):
        r"""
        :param _CompareTaskId: 一致性校验任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTaskId: str
        :param _Status: 一致性校验结果，包括：unstart(未启动)、running(校验中)、canceled(已终止)、failed(校验任务失败)、inconsistent(不一致)、consistent(一致)、notexist(不存在校验任务)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._CompareTaskId = None
        self._Status = None

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CompareTaskId = params.get("CompareTaskId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTaskItem(AbstractModel):
    """一致性校验对象信息

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _CompareTaskId: 对比任务 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTaskId: str
        :param _TaskName: 对比任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _Status: 对比任务状态, 可能的值：created - 创建完成；readyRun - 等待运行；running - 运行中；success - 成功；stopping - 结束中；failed - 失败；canceled - 已终止
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Config: 对比任务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _CheckProcess: 对比任务校验详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param _CompareProcess: 对比任务运行详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param _Conclusion: 对比结果, 可能的值：same - 一致；different - 不一致；skipAll - 跳过
注意：此字段可能返回 null，表示取不到有效值。
        :type Conclusion: str
        :param _CreatedAt: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _StartedAt: 任务启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedAt: str
        :param _FinishedAt: 对比结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedAt: str
        :param _Method: 对比类型，dataCheck(完整数据对比)、sampleDataCheck(抽样数据对比)、rowsCount(行数对比)
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _Options: 对比配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        :param _Message: 一致性校验提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._JobId = None
        self._CompareTaskId = None
        self._TaskName = None
        self._Status = None
        self._Config = None
        self._CheckProcess = None
        self._CompareProcess = None
        self._Conclusion = None
        self._CreatedAt = None
        self._StartedAt = None
        self._FinishedAt = None
        self._Method = None
        self._Options = None
        self._Message = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CheckProcess(self):
        return self._CheckProcess

    @CheckProcess.setter
    def CheckProcess(self, CheckProcess):
        self._CheckProcess = CheckProcess

    @property
    def CompareProcess(self):
        return self._CompareProcess

    @CompareProcess.setter
    def CompareProcess(self, CompareProcess):
        self._CompareProcess = CompareProcess

    @property
    def Conclusion(self):
        return self._Conclusion

    @Conclusion.setter
    def Conclusion(self, Conclusion):
        self._Conclusion = Conclusion

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def StartedAt(self):
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def FinishedAt(self):
        return self._FinishedAt

    @FinishedAt.setter
    def FinishedAt(self, FinishedAt):
        self._FinishedAt = FinishedAt

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Options(self):
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._TaskName = params.get("TaskName")
        self._Status = params.get("Status")
        if params.get("Config") is not None:
            self._Config = CompareObject()
            self._Config._deserialize(params.get("Config"))
        if params.get("CheckProcess") is not None:
            self._CheckProcess = ProcessProgress()
            self._CheckProcess._deserialize(params.get("CheckProcess"))
        if params.get("CompareProcess") is not None:
            self._CompareProcess = ProcessProgress()
            self._CompareProcess._deserialize(params.get("CompareProcess"))
        self._Conclusion = params.get("Conclusion")
        self._CreatedAt = params.get("CreatedAt")
        self._StartedAt = params.get("StartedAt")
        self._FinishedAt = params.get("FinishedAt")
        self._Method = params.get("Method")
        if params.get("Options") is not None:
            self._Options = CompareOptions()
            self._Options._deserialize(params.get("Options"))
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareViewItem(AbstractModel):
    """用于一致性校验的视图配置

    """

    def __init__(self):
        r"""
        :param _ViewName: 视图名
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        """
        self._ViewName = None

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName


    def _deserialize(self, params):
        self._ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        :param _CompleteMode: 完成任务的方式,仅支持旧版MySQL迁移任务。waitForSync-等待主从差距为0才停止,immediately-立即完成，不会等待主从差距一致。默认为waitForSync
        :type CompleteMode: str
        """
        self._JobId = None
        self._CompleteMode = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompleteMode(self):
        return self._CompleteMode

    @CompleteMode.setter
    def CompleteMode(self, CompleteMode):
        self._CompleteMode = CompleteMode


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompleteMode = params.get("CompleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ConfigureSyncJobRequest(AbstractModel):
    """ConfigureSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步实例id（即标识一个同步作业），形如sync-werwfs23
        :type JobId: str
        :param _SrcAccessType: 源端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云),注意具体可选值依赖当前链路
        :type SrcAccessType: str
        :param _DstAccessType: 目标端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)、ckafka(CKafka实例),注意具体可选值依赖当前链路
        :type DstAccessType: str
        :param _Objects: 同步库表对象信息
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param _JobName: 同步任务名称
        :type JobName: str
        :param _JobMode: 枚举值是 liteMode 和 fullMode ，分别对应精简模式或正常模式
        :type JobMode: str
        :param _RunMode: 运行模式，取值如：Immediate(表示立即运行，默认为此项值)、Timed(表示定时运行)
        :type RunMode: str
        :param _ExpectRunTime: 期待启动时间，当RunMode取值为Timed时，此值必填，形如："2006-01-02 15:04:05"
        :type ExpectRunTime: str
        :param _SrcInfo: 源端信息，单节点数据库使用，且SrcNodeType传single
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _SrcInfos: 源端信息，多节点数据库使用，且SrcNodeType传cluster
        :type SrcInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _SrcNodeType: 枚举值：cluster、single。源库为单节点数据库使用single，多节点使用cluster
        :type SrcNodeType: str
        :param _DstInfo: 目标端信息，单节点数据库使用
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _DstInfos: 目标端信息，多节点数据库使用，且DstNodeType传cluster
        :type DstInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _DstNodeType: 枚举值：cluster、single。目标库为单节点数据库使用single，多节点使用cluster
        :type DstNodeType: str
        :param _Options: 同步任务选项
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param _AutoRetryTimeRangeMinutes: 自动重试的时间段、可设置5至720分钟、0表示不重试
        :type AutoRetryTimeRangeMinutes: int
        """
        self._JobId = None
        self._SrcAccessType = None
        self._DstAccessType = None
        self._Objects = None
        self._JobName = None
        self._JobMode = None
        self._RunMode = None
        self._ExpectRunTime = None
        self._SrcInfo = None
        self._SrcInfos = None
        self._SrcNodeType = None
        self._DstInfo = None
        self._DstInfos = None
        self._DstNodeType = None
        self._Options = None
        self._AutoRetryTimeRangeMinutes = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def SrcAccessType(self):
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def DstAccessType(self):
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def Objects(self):
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobMode(self):
        return self._JobMode

    @JobMode.setter
    def JobMode(self, JobMode):
        self._JobMode = JobMode

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def SrcInfos(self):
        return self._SrcInfos

    @SrcInfos.setter
    def SrcInfos(self, SrcInfos):
        self._SrcInfos = SrcInfos

    @property
    def SrcNodeType(self):
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DstInfos(self):
        return self._DstInfos

    @DstInfos.setter
    def DstInfos(self, DstInfos):
        self._DstInfos = DstInfos

    @property
    def DstNodeType(self):
        return self._DstNodeType

    @DstNodeType.setter
    def DstNodeType(self, DstNodeType):
        self._DstNodeType = DstNodeType

    @property
    def Options(self):
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def AutoRetryTimeRangeMinutes(self):
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._SrcAccessType = params.get("SrcAccessType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("Objects") is not None:
            self._Objects = Objects()
            self._Objects._deserialize(params.get("Objects"))
        self._JobName = params.get("JobName")
        self._JobMode = params.get("JobMode")
        self._RunMode = params.get("RunMode")
        self._ExpectRunTime = params.get("ExpectRunTime")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = Endpoint()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("SrcInfos") is not None:
            self._SrcInfos = SyncDBEndpointInfos()
            self._SrcInfos._deserialize(params.get("SrcInfos"))
        self._SrcNodeType = params.get("SrcNodeType")
        if params.get("DstInfo") is not None:
            self._DstInfo = Endpoint()
            self._DstInfo._deserialize(params.get("DstInfo"))
        if params.get("DstInfos") is not None:
            self._DstInfos = SyncDBEndpointInfos()
            self._DstInfos._deserialize(params.get("DstInfos"))
        self._DstNodeType = params.get("DstNodeType")
        if params.get("Options") is not None:
            self._Options = Options()
            self._Options._deserialize(params.get("Options"))
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureSyncJobResponse(AbstractModel):
    """ConfigureSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ConflictHandleOption(AbstractModel):
    """冲突处理里的详细描述

    """

    def __init__(self):
        r"""
        :param _ConditionColumn: 条件覆盖的列
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionColumn: str
        :param _ConditionOperator: 条件覆盖操作
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionOperator: str
        :param _ConditionOrderInSrcAndDst: 条件覆盖优先级处理
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionOrderInSrcAndDst: str
        """
        self._ConditionColumn = None
        self._ConditionOperator = None
        self._ConditionOrderInSrcAndDst = None

    @property
    def ConditionColumn(self):
        return self._ConditionColumn

    @ConditionColumn.setter
    def ConditionColumn(self, ConditionColumn):
        self._ConditionColumn = ConditionColumn

    @property
    def ConditionOperator(self):
        return self._ConditionOperator

    @ConditionOperator.setter
    def ConditionOperator(self, ConditionOperator):
        self._ConditionOperator = ConditionOperator

    @property
    def ConditionOrderInSrcAndDst(self):
        return self._ConditionOrderInSrcAndDst

    @ConditionOrderInSrcAndDst.setter
    def ConditionOrderInSrcAndDst(self, ConditionOrderInSrcAndDst):
        self._ConditionOrderInSrcAndDst = ConditionOrderInSrcAndDst


    def _deserialize(self, params):
        self._ConditionColumn = params.get("ConditionColumn")
        self._ConditionOperator = params.get("ConditionOperator")
        self._ConditionOrderInSrcAndDst = params.get("ConditionOrderInSrcAndDst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsistencyOption(AbstractModel):
    """数据一致性校验选项， 默认为不开启一致性校验

    """

    def __init__(self):
        r"""
        :param _Mode: 一致性检测类型: full(全量检测迁移对象)、noCheck(不检测)、notConfigured(未配置)
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        """
        self._Mode = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueMigrateJobRequest(AbstractModel):
    """ContinueMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueMigrateJobResponse(AbstractModel):
    """ContinueMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ContinueSyncJobRequest(AbstractModel):
    """ContinueSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueSyncJobResponse(AbstractModel):
    """ContinueSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCheckSyncJobRequest(AbstractModel):
    """CreateCheckSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCheckSyncJobResponse(AbstractModel):
    """CreateCheckSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCompareTaskRequest(AbstractModel):
    """CreateCompareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 Id
        :type JobId: str
        :param _TaskName: 数据对比任务名称，若为空则默认给CompareTaskId相同值
        :type TaskName: str
        :param _ObjectMode: 数据对比对象模式，sameAsMigrate(全部迁移对象， 默认为此项配置)，custom(自定义模式)
        :type ObjectMode: str
        :param _Objects: 一致性对比对象配置
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _Options: 一致性校验选项
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        self._JobId = None
        self._TaskName = None
        self._ObjectMode = None
        self._Objects = None
        self._Options = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ObjectMode(self):
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Objects(self):
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Options(self):
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
        self._ObjectMode = params.get("ObjectMode")
        if params.get("Objects") is not None:
            self._Objects = CompareObject()
            self._Objects._deserialize(params.get("Objects"))
        if params.get("Options") is not None:
            self._Options = CompareOptions()
            self._Options._deserialize(params.get("Options"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCompareTaskResponse(AbstractModel):
    """CreateCompareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompareTaskId: 数据对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompareTaskId = None
        self._RequestId = None

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompareTaskId = params.get("CompareTaskId")
        self._RequestId = params.get("RequestId")


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateMigrationServiceRequest(AbstractModel):
    """CreateMigrationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcDatabaseType: 源实例数据库类型，如mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb,cynosdbmysql
        :type SrcDatabaseType: str
        :param _DstDatabaseType: 目标实例数据库类型，如mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb,cynosdbmysql
        :type DstDatabaseType: str
        :param _SrcRegion: 源实例地域，如：ap-guangzhou
        :type SrcRegion: str
        :param _DstRegion: 目标实例地域，如：ap-guangzhou。注意，目标地域必须和API请求地域保持一致。
        :type DstRegion: str
        :param _InstanceClass: 实例规格，包括：small、medium、large、xlarge、2xlarge
        :type InstanceClass: str
        :param _Count: 购买数量，范围为[1,15]，默认为1
        :type Count: int
        :param _JobName: 迁移服务名称，最大长度128
        :type JobName: str
        :param _Tags: 标签信息
        :type Tags: list of TagItem
        """
        self._SrcDatabaseType = None
        self._DstDatabaseType = None
        self._SrcRegion = None
        self._DstRegion = None
        self._InstanceClass = None
        self._Count = None
        self._JobName = None
        self._Tags = None

    @property
    def SrcDatabaseType(self):
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def DstDatabaseType(self):
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def SrcRegion(self):
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def DstRegion(self):
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def InstanceClass(self):
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._SrcRegion = params.get("SrcRegion")
        self._DstRegion = params.get("DstRegion")
        self._InstanceClass = params.get("InstanceClass")
        self._Count = params.get("Count")
        self._JobName = params.get("JobName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationServiceResponse(AbstractModel):
    """CreateMigrationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobIds: 下单成功随机生成的迁移任务id列表，形如：dts-c1f6rs21
注意：此字段可能返回 null，表示取不到有效值。
        :type JobIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobIds = None
        self._RequestId = None

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        self._RequestId = params.get("RequestId")


class CreateModifyCheckSyncJobRequest(AbstractModel):
    """CreateModifyCheckSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModifyCheckSyncJobResponse(AbstractModel):
    """CreateModifyCheckSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PayMode: 付款类型, 如：PrePay(表示包年包月)、PostPay(表示按时按量)
        :type PayMode: str
        :param _SrcDatabaseType: 源端数据库类型,如mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
        :type SrcDatabaseType: str
        :param _SrcRegion: 源端数据库所在地域,如ap-guangzhou
        :type SrcRegion: str
        :param _DstDatabaseType: 目标端数据库类型,如mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql,kafka等
        :type DstDatabaseType: str
        :param _DstRegion: 目标端数据库所在地域,如ap-guangzhou
        :type DstRegion: str
        :param _Specification: 同步任务规格，Standard:标准版
        :type Specification: str
        :param _Tags: 标签信息
        :type Tags: list of TagItem
        :param _Count: 一次购买的同步任务数量，取值范围为[1, 10]，默认为1
        :type Count: int
        :param _AutoRenew: 自动续费标识，当PayMode值为PrePay则此项配置有意义，取值为：1（表示自动续费）、0（不自动续费，默认为此值）
        :type AutoRenew: int
        :param _InstanceClass: 同步链路规格，如micro,small,medium,large，默认为medium
        :type InstanceClass: str
        :param _JobName: 同步任务名称
        :type JobName: str
        :param _ExistedJobId: 创建类似任务的现有任务Id
        :type ExistedJobId: str
        """
        self._PayMode = None
        self._SrcDatabaseType = None
        self._SrcRegion = None
        self._DstDatabaseType = None
        self._DstRegion = None
        self._Specification = None
        self._Tags = None
        self._Count = None
        self._AutoRenew = None
        self._InstanceClass = None
        self._JobName = None
        self._ExistedJobId = None

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SrcDatabaseType(self):
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcRegion(self):
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def DstDatabaseType(self):
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstRegion(self):
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def InstanceClass(self):
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def ExistedJobId(self):
        return self._ExistedJobId

    @ExistedJobId.setter
    def ExistedJobId(self, ExistedJobId):
        self._ExistedJobId = ExistedJobId


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcRegion = params.get("SrcRegion")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstRegion = params.get("DstRegion")
        self._Specification = params.get("Specification")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Count = params.get("Count")
        self._AutoRenew = params.get("AutoRenew")
        self._InstanceClass = params.get("InstanceClass")
        self._JobName = params.get("JobName")
        self._ExistedJobId = params.get("ExistedJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobIds: 同步任务ids
        :type JobIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobIds = None
        self._RequestId = None

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        self._RequestId = params.get("RequestId")


class DBEndpointInfo(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param _Region: 实例所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _AccessType: 实例网络接入类型，如：extranet(外网)、ipv6(公网ipv6)、cvm(云主机自建)、dcg(专线接入)、vpncloud(vpn接入的实例)、cdb(云数据库)、ccn(云联网)、intranet(自研上云)、vpc(私有网络)等，注意具体可选值依赖当前链路
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: str
        :param _DatabaseType: 实例数据库类型，如：mysql,redis,mongodb,postgresql,mariadb,percona 等
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseType: str
        :param _NodeType: 节点类型，为空或者"simple":表示普通节点，"cluster": 集群节点
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param _Info: 数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: list of DBInfo
        :param _Supplier: 实例服务提供商，如:"aliyun","others"
注意：此字段可能返回 null，表示取不到有效值。
        :type Supplier: str
        :param _ExtraAttr: MongoDB可定义如下的参数: 	['AuthDatabase':'admin', 
'AuthFlag': "1",	'AuthMechanism':"SCRAM-SHA-1"]
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraAttr: list of KeyValuePairOption
        :param _DatabaseNetEnv: 数据库所属网络环境，AccessType为云联网(ccn)时必填， UserIDC表示用户IDC、TencentVPC表示腾讯云VPC；
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseNetEnv: str
        """
        self._Region = None
        self._AccessType = None
        self._DatabaseType = None
        self._NodeType = None
        self._Info = None
        self._Supplier = None
        self._ExtraAttr = None
        self._DatabaseNetEnv = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccessType(self):
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def DatabaseType(self):
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Supplier(self):
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def ExtraAttr(self):
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def DatabaseNetEnv(self):
        return self._DatabaseNetEnv

    @DatabaseNetEnv.setter
    def DatabaseNetEnv(self, DatabaseNetEnv):
        self._DatabaseNetEnv = DatabaseNetEnv


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._AccessType = params.get("AccessType")
        self._DatabaseType = params.get("DatabaseType")
        self._NodeType = params.get("NodeType")
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = DBInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        self._Supplier = params.get("Supplier")
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        self._DatabaseNetEnv = params.get("DatabaseNetEnv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInfo(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        r"""
        :param _Role: 表示节点角色，针对分布式数据库，如mongodb中的mongos节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _DbKernel: 内核版本，针对mariadb的不同内核版本等
注意：此字段可能返回 null，表示取不到有效值。
        :type DbKernel: str
        :param _Host: 实例的IP地址，对于公网、专线、VPN、云联网、自研上云、VPC等接入方式此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Port: 实例的端口，对于公网、云主机自建、专线、VPN、云联网、自研上云、VPC等接入方式此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _User: 实例的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _Password: 实例的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _CvmInstanceId: CVM实例短ID，格式如：ins-olgl39y8；与云服务器控制台页面显示的实例ID相同；如果接入类型为云主机自建的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstanceId: str
        :param _UniqVpnGwId: VPN网关ID，格式如：vpngw-9ghexg7q；如果接入类型为vpncloud的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpnGwId: str
        :param _UniqDcgId: 专线网关ID，格式如：dcg-0rxtqqxb；如果接入类型为专线接入的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqDcgId: str
        :param _InstanceId: 数据库实例ID，格式如：cdb-powiqx8q；如果接入类型为云数据库的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _CcnGwId: 云联网ID，如：ccn-afp6kltc 注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnGwId: str
        :param _VpcId: 私有网络ID，格式如：vpc-92jblxto；如果接入类型为vpc、vpncloud、ccn、dcg的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 私有网络下的子网ID，格式如：subnet-3paxmkdz；如果接入类型为vpc、vpncloud、ccn、dcg的方式，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _EngineVersion: 数据库版本，当实例为RDS实例时才有效，格式如：5.6或者5.7，默认为5.6
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineVersion: str
        :param _Account: 实例所属账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param _AccountRole: 跨账号迁移时的角色,只允许[a-zA-Z0-9\-\_]+
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountRole: str
        :param _AccountMode: 资源所属账号 为空或self(表示本账号内资源)、other(表示其他账户资源)
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountMode: str
        :param _TmpSecretId: 临时密钥Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥Key
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        :param _TmpToken: 临时Token
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpToken: str
        """
        self._Role = None
        self._DbKernel = None
        self._Host = None
        self._Port = None
        self._User = None
        self._Password = None
        self._CvmInstanceId = None
        self._UniqVpnGwId = None
        self._UniqDcgId = None
        self._InstanceId = None
        self._CcnGwId = None
        self._VpcId = None
        self._SubnetId = None
        self._EngineVersion = None
        self._Account = None
        self._AccountRole = None
        self._AccountMode = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._TmpToken = None

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def DbKernel(self):
        return self._DbKernel

    @DbKernel.setter
    def DbKernel(self, DbKernel):
        self._DbKernel = DbKernel

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CvmInstanceId(self):
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqVpnGwId(self):
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def UniqDcgId(self):
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CcnGwId(self):
        return self._CcnGwId

    @CcnGwId.setter
    def CcnGwId(self, CcnGwId):
        self._CcnGwId = CcnGwId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def AccountRole(self):
        return self._AccountRole

    @AccountRole.setter
    def AccountRole(self, AccountRole):
        self._AccountRole = AccountRole

    @property
    def AccountMode(self):
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._DbKernel = params.get("DbKernel")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._InstanceId = params.get("InstanceId")
        self._CcnGwId = params.get("CcnGwId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._EngineVersion = params.get("EngineVersion")
        self._Account = params.get("Account")
        self._AccountRole = params.get("AccountRole")
        self._AccountMode = params.get("AccountMode")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._TmpToken = params.get("TmpToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBItem(AbstractModel):
    """迁移对象信息，在配置库表视图等对象信息时大小写敏感

    """

    def __init__(self):
        r"""
        :param _DbName: 需要迁移或同步的库名，当ObjectMode为partial时，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param _NewDbName: 迁移或同步后的库名，默认与源库相同
注意：此字段可能返回 null，表示取不到有效值。
        :type NewDbName: str
        :param _SchemaName: 迁移或同步的 schema
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param _NewSchemaName: 迁移或同步后的 schema name
注意：此字段可能返回 null，表示取不到有效值。
        :type NewSchemaName: str
        :param _DBMode: DB选择模式: all(为当前对象下的所有对象)，partial(部分对象)，当ObjectMode为partial时，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type DBMode: str
        :param _SchemaMode: schema选择模式: all(为当前对象下的所有对象)，partial(部分对象)
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaMode: str
        :param _TableMode: 表选择模式: all(为当前对象下的所有对象)，partial(部分对象)，当DBMode为partial时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TableMode: str
        :param _Tables: 表图对象集合，当 TableMode 为 partial 时，此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of TableItem
        :param _ViewMode: 视图选择模式: all 为当前对象下的所有视图对象,partial 为部分视图对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewMode: str
        :param _Views: 视图对象集合，当 ViewMode 为 partial 时， 此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Views: list of ViewItem
        :param _RoleMode: postgresql独有参数，角色选择模式: all 为当前对象下的所有角色对象,partial 为部分角色对象
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleMode: str
        :param _Roles: postgresql独有参数，当 RoleMode 为 partial 时， 此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of RoleItem
        :param _FunctionMode: 选择要同步的模式，partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionMode: str
        :param _TriggerMode: 选择要同步的模式，partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerMode: str
        :param _EventMode: 选择要同步的模式，partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type EventMode: str
        :param _ProcedureMode: 选择要同步的模式，partial为部分，all为整选
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureMode: str
        :param _Functions: FunctionMode取值为partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Functions: list of str
        :param _Procedures: ProcedureMode取值为partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Procedures: list of str
        :param _Events: EventMode取值为partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of str
        :param _Triggers: TriggerMode取值为partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Triggers: list of str
        """
        self._DbName = None
        self._NewDbName = None
        self._SchemaName = None
        self._NewSchemaName = None
        self._DBMode = None
        self._SchemaMode = None
        self._TableMode = None
        self._Tables = None
        self._ViewMode = None
        self._Views = None
        self._RoleMode = None
        self._Roles = None
        self._FunctionMode = None
        self._TriggerMode = None
        self._EventMode = None
        self._ProcedureMode = None
        self._Functions = None
        self._Procedures = None
        self._Events = None
        self._Triggers = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewDbName(self):
        return self._NewDbName

    @NewDbName.setter
    def NewDbName(self, NewDbName):
        self._NewDbName = NewDbName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def NewSchemaName(self):
        return self._NewSchemaName

    @NewSchemaName.setter
    def NewSchemaName(self, NewSchemaName):
        self._NewSchemaName = NewSchemaName

    @property
    def DBMode(self):
        return self._DBMode

    @DBMode.setter
    def DBMode(self, DBMode):
        self._DBMode = DBMode

    @property
    def SchemaMode(self):
        return self._SchemaMode

    @SchemaMode.setter
    def SchemaMode(self, SchemaMode):
        self._SchemaMode = SchemaMode

    @property
    def TableMode(self):
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def RoleMode(self):
        return self._RoleMode

    @RoleMode.setter
    def RoleMode(self, RoleMode):
        self._RoleMode = RoleMode

    @property
    def Roles(self):
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def FunctionMode(self):
        return self._FunctionMode

    @FunctionMode.setter
    def FunctionMode(self, FunctionMode):
        self._FunctionMode = FunctionMode

    @property
    def TriggerMode(self):
        return self._TriggerMode

    @TriggerMode.setter
    def TriggerMode(self, TriggerMode):
        self._TriggerMode = TriggerMode

    @property
    def EventMode(self):
        return self._EventMode

    @EventMode.setter
    def EventMode(self, EventMode):
        self._EventMode = EventMode

    @property
    def ProcedureMode(self):
        return self._ProcedureMode

    @ProcedureMode.setter
    def ProcedureMode(self, ProcedureMode):
        self._ProcedureMode = ProcedureMode

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def Procedures(self):
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def Triggers(self):
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._NewDbName = params.get("NewDbName")
        self._SchemaName = params.get("SchemaName")
        self._NewSchemaName = params.get("NewSchemaName")
        self._DBMode = params.get("DBMode")
        self._SchemaMode = params.get("SchemaMode")
        self._TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = TableItem()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = ViewItem()
                obj._deserialize(item)
                self._Views.append(obj)
        self._RoleMode = params.get("RoleMode")
        if params.get("Roles") is not None:
            self._Roles = []
            for item in params.get("Roles"):
                obj = RoleItem()
                obj._deserialize(item)
                self._Roles.append(obj)
        self._FunctionMode = params.get("FunctionMode")
        self._TriggerMode = params.get("TriggerMode")
        self._EventMode = params.get("EventMode")
        self._ProcedureMode = params.get("ProcedureMode")
        self._Functions = params.get("Functions")
        self._Procedures = params.get("Procedures")
        self._Events = params.get("Events")
        self._Triggers = params.get("Triggers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """需要同步的库表对象

    """

    def __init__(self):
        r"""
        :param _DbName: 需要迁移或同步的库名，当ObjectMode为Partial时，此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param _NewDbName: 迁移或同步后的库名，默认与源库相同
注意：此字段可能返回 null，表示取不到有效值。
        :type NewDbName: str
        :param _DbMode: DB选择模式: All(为当前对象下的所有对象)，Partial(部分对象)，当Mode为Partial时，此项必填。注意，高级对象的同步不依赖此值，如果整库同步此处应该为All。
注意：此字段可能返回 null，表示取不到有效值。
        :type DbMode: str
        :param _SchemaName: 迁移或同步的 schema
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param _NewSchemaName: 迁移或同步后的 schema name
注意：此字段可能返回 null，表示取不到有效值。
        :type NewSchemaName: str
        :param _TableMode: 表选择模式: All(为当前对象下的所有对象)，Partial(部分对象)，当DBMode为Partial时此项必填，如果整库同步此处应该为All。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableMode: str
        :param _Tables: 表图对象集合，当 TableMode 为 Partial 时，此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of Table
        :param _ViewMode: 视图选择模式: All 为当前对象下的所有视图对象,Partial 为部分视图对象，如果整库同步此处应该为All。
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewMode: str
        :param _Views: 视图对象集合，当 ViewMode 为 Partial 时， 此项需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Views: list of View
        :param _FunctionMode: 选择要同步的模式，Partial为部分，All为整选，如果整库同步此处应该为All。
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionMode: str
        :param _Functions: FunctionMode取值为Partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Functions: list of str
        :param _ProcedureMode: 选择要同步的模式，Partial为部分，All为整选，如果整库同步此处应该为All。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureMode: str
        :param _Procedures: ProcedureMode取值为Partial时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Procedures: list of str
        :param _TriggerMode: 触发器迁移模式，All(为当前对象下的所有对象)，Partial(部分对象)，如果整库同步此处应该为All。数据同步暂不支持此高级对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerMode: str
        :param _Triggers: 当TriggerMode为partial，指定要迁移的触发器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Triggers: list of str
        :param _EventMode: 事件迁移模式，All(为当前对象下的所有对象)，Partial(部分对象)，如果整库同步此处应该为All。数据同步暂不支持此高级对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type EventMode: str
        :param _Events: 当EventMode为partial，指定要迁移的事件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of str
        """
        self._DbName = None
        self._NewDbName = None
        self._DbMode = None
        self._SchemaName = None
        self._NewSchemaName = None
        self._TableMode = None
        self._Tables = None
        self._ViewMode = None
        self._Views = None
        self._FunctionMode = None
        self._Functions = None
        self._ProcedureMode = None
        self._Procedures = None
        self._TriggerMode = None
        self._Triggers = None
        self._EventMode = None
        self._Events = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewDbName(self):
        return self._NewDbName

    @NewDbName.setter
    def NewDbName(self, NewDbName):
        self._NewDbName = NewDbName

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def NewSchemaName(self):
        return self._NewSchemaName

    @NewSchemaName.setter
    def NewSchemaName(self, NewSchemaName):
        self._NewSchemaName = NewSchemaName

    @property
    def TableMode(self):
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def FunctionMode(self):
        return self._FunctionMode

    @FunctionMode.setter
    def FunctionMode(self, FunctionMode):
        self._FunctionMode = FunctionMode

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def ProcedureMode(self):
        return self._ProcedureMode

    @ProcedureMode.setter
    def ProcedureMode(self, ProcedureMode):
        self._ProcedureMode = ProcedureMode

    @property
    def Procedures(self):
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def TriggerMode(self):
        return self._TriggerMode

    @TriggerMode.setter
    def TriggerMode(self, TriggerMode):
        self._TriggerMode = TriggerMode

    @property
    def Triggers(self):
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers

    @property
    def EventMode(self):
        return self._EventMode

    @EventMode.setter
    def EventMode(self, EventMode):
        self._EventMode = EventMode

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._NewDbName = params.get("NewDbName")
        self._DbMode = params.get("DbMode")
        self._SchemaName = params.get("SchemaName")
        self._NewSchemaName = params.get("NewSchemaName")
        self._TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = Table()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = View()
                obj._deserialize(item)
                self._Views.append(obj)
        self._FunctionMode = params.get("FunctionMode")
        self._Functions = params.get("Functions")
        self._ProcedureMode = params.get("ProcedureMode")
        self._Procedures = params.get("Procedures")
        self._TriggerMode = params.get("TriggerMode")
        self._Triggers = params.get("Triggers")
        self._EventMode = params.get("EventMode")
        self._Events = params.get("Events")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTableObject(AbstractModel):
    """迁移对象选项，需要告知迁移服务迁移哪些库表对象

    """

    def __init__(self):
        r"""
        :param _ObjectMode: 迁移对象类型 all(全实例)，partial(部分对象)
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectMode: str
        :param _Databases: 迁移对象，当 ObjectMode 为 partial 时，不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of DBItem
        :param _AdvancedObjects: 高级对象类型，如trigger、function、procedure、event
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedObjects: list of str
        """
        self._ObjectMode = None
        self._Databases = None
        self._AdvancedObjects = None

    @property
    def ObjectMode(self):
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def AdvancedObjects(self):
        return self._AdvancedObjects

    @AdvancedObjects.setter
    def AdvancedObjects(self, AdvancedObjects):
        self._AdvancedObjects = AdvancedObjects


    def _deserialize(self, params):
        self._ObjectMode = params.get("ObjectMode")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = DBItem()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._AdvancedObjects = params.get("AdvancedObjects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdlOption(AbstractModel):
    """数据同步中的ddl同步处理

    """

    def __init__(self):
        r"""
        :param _DdlObject: ddl类型，如Database,Table,View,Index等
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlObject: str
        :param _DdlValue: ddl具体值，对于Database可取值[Create,Drop,Alter]<br>对于Table可取值[Create,Drop,Alter,Truncate,Rename]<br/>对于View可取值[Create,Drop]<br/>对于Index可取值[Create,Drop]
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlValue: list of str
        """
        self._DdlObject = None
        self._DdlValue = None

    @property
    def DdlObject(self):
        return self._DdlObject

    @DdlObject.setter
    def DdlObject(self, DdlObject):
        self._DdlObject = DdlObject

    @property
    def DdlValue(self):
        return self._DdlValue

    @DdlValue.setter
    def DdlValue(self, DdlValue):
        self._DdlValue = DdlValue


    def _deserialize(self, params):
        self._DdlObject = params.get("DdlObject")
        self._DdlValue = params.get("DdlValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompareTaskRequest(AbstractModel):
    """DeleteCompareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务 Id
        :type JobId: str
        :param _CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        """
        self._JobId = None
        self._CompareTaskId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompareTaskResponse(AbstractModel):
    """DeleteCompareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeCheckSyncJobResultRequest(AbstractModel):
    """DescribeCheckSyncJobResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步实例id（即标识一个同步作业），形如sync-werwfs23，此值必填
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckSyncJobResultResponse(AbstractModel):
    """DescribeCheckSyncJobResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 校验任务执行状态，如：notStarted(未开始)、running(校验中)、failed(校验任务失败)、success(任务成功)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StepCount: 步骤总数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepCount: int
        :param _StepCur: 当前所在步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepCur: int
        :param _Progress: 总体进度，范围为[0,100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _StepInfos: 步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfos: list of StepInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._StepCount = None
        self._StepCur = None
        self._Progress = None
        self._StepInfos = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StepCount(self):
        return self._StepCount

    @StepCount.setter
    def StepCount(self, StepCount):
        self._StepCount = StepCount

    @property
    def StepCur(self):
        return self._StepCur

    @StepCur.setter
    def StepCur(self, StepCur):
        self._StepCur = StepCur

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfos(self):
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StepCount = params.get("StepCount")
        self._StepCur = params.get("StepCur")
        self._Progress = params.get("Progress")
        if params.get("StepInfos") is not None:
            self._StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self._StepInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCompareReportRequest(AbstractModel):
    """DescribeCompareReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务 Id
        :type JobId: str
        :param _CompareTaskId: 校验任务 Id
        :type CompareTaskId: str
        :param _DifferenceLimit: 校验不一致结果的 limit
        :type DifferenceLimit: int
        :param _DifferenceOffset: 不一致的 Offset
        :type DifferenceOffset: int
        :param _DifferenceDB: 搜索条件，不一致的库名
        :type DifferenceDB: str
        :param _DifferenceTable: 搜索条件，不一致的表名
        :type DifferenceTable: str
        :param _SkippedLimit: 未校验的 Limit
        :type SkippedLimit: int
        :param _SkippedOffset: 未校验的 Offset
        :type SkippedOffset: int
        :param _SkippedDB: 搜索条件，未校验的库名
        :type SkippedDB: str
        :param _SkippedTable: 搜索条件，未校验的表名
        :type SkippedTable: str
        """
        self._JobId = None
        self._CompareTaskId = None
        self._DifferenceLimit = None
        self._DifferenceOffset = None
        self._DifferenceDB = None
        self._DifferenceTable = None
        self._SkippedLimit = None
        self._SkippedOffset = None
        self._SkippedDB = None
        self._SkippedTable = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def DifferenceLimit(self):
        return self._DifferenceLimit

    @DifferenceLimit.setter
    def DifferenceLimit(self, DifferenceLimit):
        self._DifferenceLimit = DifferenceLimit

    @property
    def DifferenceOffset(self):
        return self._DifferenceOffset

    @DifferenceOffset.setter
    def DifferenceOffset(self, DifferenceOffset):
        self._DifferenceOffset = DifferenceOffset

    @property
    def DifferenceDB(self):
        return self._DifferenceDB

    @DifferenceDB.setter
    def DifferenceDB(self, DifferenceDB):
        self._DifferenceDB = DifferenceDB

    @property
    def DifferenceTable(self):
        return self._DifferenceTable

    @DifferenceTable.setter
    def DifferenceTable(self, DifferenceTable):
        self._DifferenceTable = DifferenceTable

    @property
    def SkippedLimit(self):
        return self._SkippedLimit

    @SkippedLimit.setter
    def SkippedLimit(self, SkippedLimit):
        self._SkippedLimit = SkippedLimit

    @property
    def SkippedOffset(self):
        return self._SkippedOffset

    @SkippedOffset.setter
    def SkippedOffset(self, SkippedOffset):
        self._SkippedOffset = SkippedOffset

    @property
    def SkippedDB(self):
        return self._SkippedDB

    @SkippedDB.setter
    def SkippedDB(self, SkippedDB):
        self._SkippedDB = SkippedDB

    @property
    def SkippedTable(self):
        return self._SkippedTable

    @SkippedTable.setter
    def SkippedTable(self, SkippedTable):
        self._SkippedTable = SkippedTable


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._DifferenceLimit = params.get("DifferenceLimit")
        self._DifferenceOffset = params.get("DifferenceOffset")
        self._DifferenceDB = params.get("DifferenceDB")
        self._DifferenceTable = params.get("DifferenceTable")
        self._SkippedLimit = params.get("SkippedLimit")
        self._SkippedOffset = params.get("SkippedOffset")
        self._SkippedDB = params.get("SkippedDB")
        self._SkippedTable = params.get("SkippedTable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompareReportResponse(AbstractModel):
    """DescribeCompareReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Abstract: 一致性校验摘要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Abstract: :class:`tencentcloud.dts.v20211206.models.CompareAbstractInfo`
        :param _Detail: 一致性校验详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: :class:`tencentcloud.dts.v20211206.models.CompareDetailInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Abstract = None
        self._Detail = None
        self._RequestId = None

    @property
    def Abstract(self):
        return self._Abstract

    @Abstract.setter
    def Abstract(self, Abstract):
        self._Abstract = Abstract

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Abstract") is not None:
            self._Abstract = CompareAbstractInfo()
            self._Abstract._deserialize(params.get("Abstract"))
        if params.get("Detail") is not None:
            self._Detail = CompareDetailInfo()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeCompareTasksRequest(AbstractModel):
    """DescribeCompareTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务 Id
        :type JobId: str
        :param _Limit: 分页设置，表示每页显示多少条任务，默认为 20
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _CompareTaskId: 校验任务 ID
        :type CompareTaskId: str
        :param _Status: 任务状态过滤，可能的值：created - 创建完成；readyRun - 等待运行；running - 运行中；success - 成功；stopping - 结束中；failed - 失败；canceled - 已终止
        :type Status: list of str
        """
        self._JobId = None
        self._Limit = None
        self._Offset = None
        self._CompareTaskId = None
        self._Status = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CompareTaskId = params.get("CompareTaskId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompareTasksResponse(AbstractModel):
    """DescribeCompareTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Items: 一致性校验列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of CompareTaskItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = CompareTaskItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrateDBInstancesRequest(AbstractModel):
    """DescribeMigrateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseType: 数据库类型，如mysql
        :type DatabaseType: str
        :param _MigrateRole: 实例作为迁移的源还是目标,src(表示源)，dst(表示目标)
        :type MigrateRole: str
        :param _InstanceId: 云数据库实例ID
        :type InstanceId: str
        :param _InstanceName: 云数据库名称
        :type InstanceName: str
        :param _Limit: 返回数量限制
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _AccountMode: 资源所属账号 为空值或self(表示本账号内资源)、other(表示其他账户资源)
        :type AccountMode: str
        :param _TmpSecretId: 临时密钥Id，若为跨账号资源此项必填
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥Key，若为跨账号资源此项必填
        :type TmpSecretKey: str
        :param _TmpToken: 临时密钥Token，若为跨账号资源此项必填
        :type TmpToken: str
        """
        self._DatabaseType = None
        self._MigrateRole = None
        self._InstanceId = None
        self._InstanceName = None
        self._Limit = None
        self._Offset = None
        self._AccountMode = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._TmpToken = None

    @property
    def DatabaseType(self):
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def MigrateRole(self):
        return self._MigrateRole

    @MigrateRole.setter
    def MigrateRole(self, MigrateRole):
        self._MigrateRole = MigrateRole

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AccountMode(self):
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken


    def _deserialize(self, params):
        self._DatabaseType = params.get("DatabaseType")
        self._MigrateRole = params.get("MigrateRole")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AccountMode = params.get("AccountMode")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._TmpToken = params.get("TmpToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateDBInstancesResponse(AbstractModel):
    """DescribeMigrateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合筛选条件的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Instances: 实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of MigrateDBItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = MigrateDBItem()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrationCheckJobRequest(AbstractModel):
    """DescribeMigrationCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationCheckJobResponse(AbstractModel):
    """DescribeMigrationCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 校验任务执行状态，如：notStarted(未开始)、running(校验中)、failed(校验任务失败)、success(任务成功)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _BriefMsg: 校验任务结果输出简要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefMsg: str
        :param _StepInfo: 检查步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: list of CheckStep
        :param _CheckFlag: 校验结果，如：checkPass(校验通过)、checkNotPass(校验未通过)
        :type CheckFlag: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._BriefMsg = None
        self._StepInfo = None
        self._CheckFlag = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BriefMsg(self):
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def StepInfo(self):
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def CheckFlag(self):
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._BriefMsg = params.get("BriefMsg")
        if params.get("StepInfo") is not None:
            self._StepInfo = []
            for item in params.get("StepInfo"):
                obj = CheckStep()
                obj._deserialize(item)
                self._StepInfo.append(obj)
        self._CheckFlag = params.get("CheckFlag")
        self._RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _JobName: 数据迁移任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param _CreateTime: 任务创建(提交)时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 任务更新时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _StartTime: 任务开始执行时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务执行结束时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _BriefMsg: 迁移任务简要错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefMsg: str
        :param _Status: 任务状态，取值为：created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行中)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)、
pausing(暂停中)、
manualPaused(已暂停)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Action: 任务操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param _StepInfo: 迁移执行过程信息，在校验阶段显示校验过程步骤信息，在迁移阶段会显示迁移步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param _SrcInfo: 源实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _DstInfo: 目标端信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _CompareTask: 数据一致性校验结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param _Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param _RunMode: 运行模式，取值如：immediate(表示立即运行)、timed(表示定时运行)
注意：此字段可能返回 null，表示取不到有效值。
        :type RunMode: str
        :param _ExpectRunTime: 期待启动时间，当RunMode取值为timed时，此值必填，形如："2006-01-02 15:04:05"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectRunTime: str
        :param _MigrateOption: 迁移选项，描述任务如何执行迁移等一系列配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param _CheckStepInfo: 校验任务运行详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckStepInfo: :class:`tencentcloud.dts.v20211206.models.CheckStepInfo`
        :param _TradeInfo: 描述计费相关的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param _ErrorInfo: 任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: list of ErrorInfoItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._JobName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._StartTime = None
        self._EndTime = None
        self._BriefMsg = None
        self._Status = None
        self._Action = None
        self._StepInfo = None
        self._SrcInfo = None
        self._DstInfo = None
        self._CompareTask = None
        self._Tags = None
        self._RunMode = None
        self._ExpectRunTime = None
        self._MigrateOption = None
        self._CheckStepInfo = None
        self._TradeInfo = None
        self._ErrorInfo = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BriefMsg(self):
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StepInfo(self):
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def CompareTask(self):
        return self._CompareTask

    @CompareTask.setter
    def CompareTask(self, CompareTask):
        self._CompareTask = CompareTask

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def MigrateOption(self):
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def CheckStepInfo(self):
        return self._CheckStepInfo

    @CheckStepInfo.setter
    def CheckStepInfo(self, CheckStepInfo):
        self._CheckStepInfo = CheckStepInfo

    @property
    def TradeInfo(self):
        return self._TradeInfo

    @TradeInfo.setter
    def TradeInfo(self, TradeInfo):
        self._TradeInfo = TradeInfo

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._BriefMsg = params.get("BriefMsg")
        self._Status = params.get("Status")
        if params.get("Action") is not None:
            self._Action = MigrateAction()
            self._Action._deserialize(params.get("Action"))
        if params.get("StepInfo") is not None:
            self._StepInfo = MigrateDetailInfo()
            self._StepInfo._deserialize(params.get("StepInfo"))
        if params.get("SrcInfo") is not None:
            self._SrcInfo = DBEndpointInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DBEndpointInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        if params.get("CompareTask") is not None:
            self._CompareTask = CompareTaskInfo()
            self._CompareTask._deserialize(params.get("CompareTask"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RunMode = params.get("RunMode")
        self._ExpectRunTime = params.get("ExpectRunTime")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        if params.get("CheckStepInfo") is not None:
            self._CheckStepInfo = CheckStepInfo()
            self._CheckStepInfo._deserialize(params.get("CheckStepInfo"))
        if params.get("TradeInfo") is not None:
            self._TradeInfo = TradeInfo()
            self._TradeInfo._deserialize(params.get("TradeInfo"))
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfoItem()
                obj._deserialize(item)
                self._ErrorInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrationJobsRequest(AbstractModel):
    """DescribeMigrationJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID，如：dts-amm1jw5q
        :type JobId: str
        :param _JobName: 数据迁移任务名称
        :type JobName: str
        :param _Status: 数据迁移任务状态，可取值包括：created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行中)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)
        :type Status: list of str
        :param _SrcInstanceId: 源实例ID，格式如：cdb-c1nl9rpv
        :type SrcInstanceId: str
        :param _SrcRegion: 源实例地域，如：ap-guangzhou
        :type SrcRegion: str
        :param _SrcDatabaseType: 源实例数据库类型，如：sqlserver,mysql,mongodb,redis,tendis,keewidb,clickhouse,cynosdbmysql,percona,tdsqlpercona,mariadb,tdsqlmysql,postgresql
        :type SrcDatabaseType: list of str
        :param _SrcAccessType: 源实例接入类型，值包括：extranet(外网)、vpncloud(云vpn接入的实例)、dcg(专线接入的实例)、ccn(云联网接入的实例)、cdb(云上cdb实例)、cvm(cvm自建实例)
        :type SrcAccessType: list of str
        :param _DstInstanceId: 目标实例ID，格式如：cdb-c1nl9rpv
        :type DstInstanceId: str
        :param _DstRegion: 目标实例地域，如：ap-guangzhou
        :type DstRegion: str
        :param _DstDatabaseType: 目标源实例数据库类型，如：sqlserver,mysql,mongodb,redis,tendis,keewidb,clickhouse,cynosdbmysql,percona,tdsqlpercona,mariadb,tdsqlmysql,postgresql
        :type DstDatabaseType: list of str
        :param _DstAccessType: 目标实例接入类型，值包括：extranet(外网)、vpncloud(云vpn接入的实例)、dcg(专线接入的实例)、ccn(云联网接入的实例)、cdb(云上cdb实例)、cvm(cvm自建实例)
        :type DstAccessType: list of str
        :param _RunMode: 任务运行模式，值包括：immediate(立即运行)，timed(定时运行)
        :type RunMode: str
        :param _OrderSeq: 排序方式，可能取值为asc、desc，默认按照创建时间倒序
        :type OrderSeq: str
        :param _Limit: 返回实例数量，默认20，有效区间[1,100]
        :type Limit: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _TagFilters: 标签过滤
        :type TagFilters: list of TagFilter
        """
        self._JobId = None
        self._JobName = None
        self._Status = None
        self._SrcInstanceId = None
        self._SrcRegion = None
        self._SrcDatabaseType = None
        self._SrcAccessType = None
        self._DstInstanceId = None
        self._DstRegion = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._RunMode = None
        self._OrderSeq = None
        self._Limit = None
        self._Offset = None
        self._TagFilters = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SrcInstanceId(self):
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def SrcRegion(self):
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def SrcDatabaseType(self):
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def DstInstanceId(self):
        return self._DstInstanceId

    @DstInstanceId.setter
    def DstInstanceId(self, DstInstanceId):
        self._DstInstanceId = DstInstanceId

    @property
    def DstRegion(self):
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def DstDatabaseType(self):
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def OrderSeq(self):
        return self._OrderSeq

    @OrderSeq.setter
    def OrderSeq(self, OrderSeq):
        self._OrderSeq = OrderSeq

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Status = params.get("Status")
        self._SrcInstanceId = params.get("SrcInstanceId")
        self._SrcRegion = params.get("SrcRegion")
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcAccessType = params.get("SrcAccessType")
        self._DstInstanceId = params.get("DstInstanceId")
        self._DstRegion = params.get("DstRegion")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        self._RunMode = params.get("RunMode")
        self._OrderSeq = params.get("OrderSeq")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationJobsResponse(AbstractModel):
    """DescribeMigrationJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 迁移任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _JobList: 迁移任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobList: list of JobItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobList(self):
        return self._JobList

    @JobList.setter
    def JobList(self, JobList):
        self._JobList = JobList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self._JobList = []
            for item in params.get("JobList"):
                obj = JobItem()
                obj._deserialize(item)
                self._JobList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModifyCheckSyncJobResultRequest(AbstractModel):
    """DescribeModifyCheckSyncJobResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModifyCheckSyncJobResultResponse(AbstractModel):
    """DescribeModifyCheckSyncJobResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 校验任务执行状态，如：notStarted(未开始)、running(校验中)、failed(校验任务失败)、success(任务成功)
        :type Status: str
        :param _StepCount: 校验的步骤总数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepCount: int
        :param _StepCur: 当前所在步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepCur: int
        :param _Progress: 总体进度，范围为[0,100]	
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _StepInfos: 步骤详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfos: list of StepInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._StepCount = None
        self._StepCur = None
        self._Progress = None
        self._StepInfos = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StepCount(self):
        return self._StepCount

    @StepCount.setter
    def StepCount(self, StepCount):
        self._StepCount = StepCount

    @property
    def StepCur(self):
        return self._StepCur

    @StepCur.setter
    def StepCur(self, StepCur):
        self._StepCur = StepCur

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfos(self):
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StepCount = params.get("StepCount")
        self._StepCur = params.get("StepCur")
        self._Progress = params.get("Progress")
        if params.get("StepInfos") is not None:
            self._StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self._StepInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSyncJobsRequest(AbstractModel):
    """DescribeSyncJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id，如sync-werwfs23
        :type JobId: str
        :param _JobName: 同步任务名
        :type JobName: str
        :param _Order: 排序字段，可以取值为CreateTime
        :type Order: str
        :param _OrderSeq: 排序方式，升序为ASC，降序为DESC，默认为CreateTime降序
        :type OrderSeq: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回同步任务实例数量，默认20，有效区间[1,100]
        :type Limit: int
        :param _Status: 状态集合，如Initialized,CheckPass,Running,ResumableErr,Stopped
        :type Status: list of str
        :param _RunMode: 运行模式，如Immediate:立即运行，Timed:定时运行
        :type RunMode: str
        :param _JobType: 任务类型，如mysql2mysql：msyql同步到mysql
        :type JobType: str
        :param _PayMode: 付费类型，PrePay：预付费，PostPay：后付费
        :type PayMode: str
        :param _TagFilters: tag
        :type TagFilters: list of TagFilter
        """
        self._JobId = None
        self._JobName = None
        self._Order = None
        self._OrderSeq = None
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._RunMode = None
        self._JobType = None
        self._PayMode = None
        self._TagFilters = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderSeq(self):
        return self._OrderSeq

    @OrderSeq.setter
    def OrderSeq(self, OrderSeq):
        self._OrderSeq = OrderSeq

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def JobType(self):
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Order = params.get("Order")
        self._OrderSeq = params.get("OrderSeq")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._RunMode = params.get("RunMode")
        self._JobType = params.get("JobType")
        self._PayMode = params.get("PayMode")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _JobList: 任务详情数组
注意：此字段可能返回 null，表示取不到有效值。
        :type JobList: list of SyncJobInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobList(self):
        return self._JobList

    @JobList.setter
    def JobList(self, JobList):
        self._JobList = JobList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self._JobList = []
            for item in params.get("JobList"):
                obj = SyncJobInfo()
                obj._deserialize(item)
                self._JobList.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyMigrateJobRequest(AbstractModel):
    """DestroyMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyMigrateJobResponse(AbstractModel):
    """DestroyMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DestroySyncJobRequest(AbstractModel):
    """DestroySyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroySyncJobResponse(AbstractModel):
    """DestroySyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DetailCheckItem(AbstractModel):
    """每个检查步骤里的具体检查项

    """

    def __init__(self):
        r"""
        :param _CheckItemName: 检查项的名称，如：源实例权限检查
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckItemName: str
        :param _Description: 检查项详细内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CheckResult: pass(通过)，failed(失败), warning(校验有警告，但仍通过)
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckResult: str
        :param _FailureReason: 检查项失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param _Solution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param _ErrorLog: 运行报错日志
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorLog: list of str
        :param _HelpDoc: 详细帮助的文档链接
注意：此字段可能返回 null，表示取不到有效值。
        :type HelpDoc: list of str
        :param _SkipInfo: 跳过风险文案
注意：此字段可能返回 null，表示取不到有效值。
        :type SkipInfo: str
        """
        self._CheckItemName = None
        self._Description = None
        self._CheckResult = None
        self._FailureReason = None
        self._Solution = None
        self._ErrorLog = None
        self._HelpDoc = None
        self._SkipInfo = None

    @property
    def CheckItemName(self):
        return self._CheckItemName

    @CheckItemName.setter
    def CheckItemName(self, CheckItemName):
        self._CheckItemName = CheckItemName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CheckResult(self):
        return self._CheckResult

    @CheckResult.setter
    def CheckResult(self, CheckResult):
        self._CheckResult = CheckResult

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def Solution(self):
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def ErrorLog(self):
        return self._ErrorLog

    @ErrorLog.setter
    def ErrorLog(self, ErrorLog):
        self._ErrorLog = ErrorLog

    @property
    def HelpDoc(self):
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc

    @property
    def SkipInfo(self):
        return self._SkipInfo

    @SkipInfo.setter
    def SkipInfo(self, SkipInfo):
        self._SkipInfo = SkipInfo


    def _deserialize(self, params):
        self._CheckItemName = params.get("CheckItemName")
        self._Description = params.get("Description")
        self._CheckResult = params.get("CheckResult")
        self._FailureReason = params.get("FailureReason")
        self._Solution = params.get("Solution")
        self._ErrorLog = params.get("ErrorLog")
        self._HelpDoc = params.get("HelpDoc")
        self._SkipInfo = params.get("SkipInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceDetail(AbstractModel):
    """数据不一致的表详情

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据不一致的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Items: 校验不一致的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DifferenceItem
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DifferenceItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceItem(AbstractModel):
    """校验不一致的表详情

    """

    def __init__(self):
        r"""
        :param _Db: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Db: str
        :param _Table: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _Chunk: 分块号
注意：此字段可能返回 null，表示取不到有效值。
        :type Chunk: int
        :param _SrcItem: 源库数值
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcItem: str
        :param _DstItem: 目标库数值
注意：此字段可能返回 null，表示取不到有效值。
        :type DstItem: str
        :param _IndexName: 索引名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param _LowerBoundary: 索引下边界
注意：此字段可能返回 null，表示取不到有效值。
        :type LowerBoundary: str
        :param _UpperBoundary: 索引上边界
注意：此字段可能返回 null，表示取不到有效值。
        :type UpperBoundary: str
        :param _CostTime: 对比消耗时间,单位为 ms
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: float
        :param _FinishedAt: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedAt: str
        """
        self._Db = None
        self._Table = None
        self._Chunk = None
        self._SrcItem = None
        self._DstItem = None
        self._IndexName = None
        self._LowerBoundary = None
        self._UpperBoundary = None
        self._CostTime = None
        self._FinishedAt = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Chunk(self):
        return self._Chunk

    @Chunk.setter
    def Chunk(self, Chunk):
        self._Chunk = Chunk

    @property
    def SrcItem(self):
        return self._SrcItem

    @SrcItem.setter
    def SrcItem(self, SrcItem):
        self._SrcItem = SrcItem

    @property
    def DstItem(self):
        return self._DstItem

    @DstItem.setter
    def DstItem(self, DstItem):
        self._DstItem = DstItem

    @property
    def IndexName(self):
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def LowerBoundary(self):
        return self._LowerBoundary

    @LowerBoundary.setter
    def LowerBoundary(self, LowerBoundary):
        self._LowerBoundary = LowerBoundary

    @property
    def UpperBoundary(self):
        return self._UpperBoundary

    @UpperBoundary.setter
    def UpperBoundary(self, UpperBoundary):
        self._UpperBoundary = UpperBoundary

    @property
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def FinishedAt(self):
        return self._FinishedAt

    @FinishedAt.setter
    def FinishedAt(self, FinishedAt):
        self._FinishedAt = FinishedAt


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Table = params.get("Table")
        self._Chunk = params.get("Chunk")
        self._SrcItem = params.get("SrcItem")
        self._DstItem = params.get("DstItem")
        self._IndexName = params.get("IndexName")
        self._LowerBoundary = params.get("LowerBoundary")
        self._UpperBoundary = params.get("UpperBoundary")
        self._CostTime = params.get("CostTime")
        self._FinishedAt = params.get("FinishedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicOptions(AbstractModel):
    """数据同步中的选项

    """

    def __init__(self):
        r"""
        :param _OpTypes: 所要同步的DML和DDL的选项，Insert(插入操作)、Update(更新操作)、Delete(删除操作)、DDL(结构同步)，PartialDDL(自定义,和DdlOptions一起起作用 )；必填、dts会用该值覆盖原有的值
注意：此字段可能返回 null，表示取不到有效值。
        :type OpTypes: list of str
        :param _DdlOptions: DDL同步选项，具体描述要同步那些DDL; 当OpTypes取值PartialDDL时、字段不能为空；必填、dts会用该值覆盖原有的值
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlOptions: list of DdlOption
        :param _ConflictHandleType: 冲突处理选项，ReportError(报错)、Ignore(忽略)、Cover(覆盖)、ConditionCover(条件覆盖); 目前目标端为kafka的链路不支持修改该配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ConflictHandleType: str
        :param _ConflictHandleOption: 冲突处理的详细选项，如条件覆盖中的条件行和条件操作；不能部分更新该选项的内部字段；有更新时、需要全量更新该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ConflictHandleOption: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        """
        self._OpTypes = None
        self._DdlOptions = None
        self._ConflictHandleType = None
        self._ConflictHandleOption = None

    @property
    def OpTypes(self):
        return self._OpTypes

    @OpTypes.setter
    def OpTypes(self, OpTypes):
        self._OpTypes = OpTypes

    @property
    def DdlOptions(self):
        return self._DdlOptions

    @DdlOptions.setter
    def DdlOptions(self, DdlOptions):
        self._DdlOptions = DdlOptions

    @property
    def ConflictHandleType(self):
        return self._ConflictHandleType

    @ConflictHandleType.setter
    def ConflictHandleType(self, ConflictHandleType):
        self._ConflictHandleType = ConflictHandleType

    @property
    def ConflictHandleOption(self):
        return self._ConflictHandleOption

    @ConflictHandleOption.setter
    def ConflictHandleOption(self, ConflictHandleOption):
        self._ConflictHandleOption = ConflictHandleOption


    def _deserialize(self, params):
        self._OpTypes = params.get("OpTypes")
        if params.get("DdlOptions") is not None:
            self._DdlOptions = []
            for item in params.get("DdlOptions"):
                obj = DdlOption()
                obj._deserialize(item)
                self._DdlOptions.append(obj)
        self._ConflictHandleType = params.get("ConflictHandleType")
        if params.get("ConflictHandleOption") is not None:
            self._ConflictHandleOption = ConflictHandleOption()
            self._ConflictHandleOption._deserialize(params.get("ConflictHandleOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Endpoint(AbstractModel):
    """数据同步中的描述源端和目的端的信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域英文名，如：ap-guangzhou
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Role: tdsql mysql版的节点类型，枚举值为proxy、set
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _DbKernel: 数据库内核类型，tdsql中用于区分不同内核：percona,mariadb,mysql
注意：此字段可能返回 null，表示取不到有效值。
        :type DbKernel: str
        :param _InstanceId: 数据库实例ID，格式如：cdb-powiqx8q
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Ip: 实例的IP地址，接入类型为非cdb时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 实例端口，接入类型为非cdb时此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _User: 用户名，对于访问需要用户名密码认证的实例必填
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _Password: 密码，对于访问需要用户名密码认证的实例必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _DbName: 数据库名，数据库为cdwpg时，需要提供
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param _VpcId: 私有网络ID，对于私有网络、专线、VPN的接入方式此项必填，格式如：vpc-92jblxto
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 私有网络下的子网ID，对于私有网络、专线、VPN的接入方式此项必填，格式如：subnet-3paxmkdz
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _CvmInstanceId: CVM实例短ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要传递此字段
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstanceId: str
        :param _UniqDcgId: 专线网关ID，对于专线接入类型此项必填，格式如：dcg-0rxtqqxb
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqDcgId: str
        :param _UniqVpnGwId: VPN网关ID，对于vpn接入类型此项必填，格式如：vpngw-9ghexg7q
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpnGwId: str
        :param _CcnId: 云联网ID，对于云联网接入类型此项必填，如：ccn-afp6kltc
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnId: str
        :param _Supplier: 云厂商类型，当实例为RDS实例时，填写为aliyun, 其他情况均填写others，默认为others
注意：此字段可能返回 null，表示取不到有效值。
        :type Supplier: str
        :param _EngineVersion: 数据库版本，当实例为RDS实例时才有效，其他实例忽略，格式如：5.6或者5.7，默认为5.6
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineVersion: str
        :param _Account: 实例所属账号，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param _AccountMode: 资源所属账号 为空或self(表示本账号内资源)、other(表示跨账号资源)
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountMode: str
        :param _AccountRole: 跨账号同步时的角色，只允许[a-zA-Z0-9\-\_]+，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountRole: str
        :param _RoleExternalId: 外部角色id
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleExternalId: str
        :param _TmpSecretId: 临时密钥Id，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥Key，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        :param _TmpToken: 临时Token，如果为跨账号实例此项必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpToken: str
        :param _EncryptConn: 是否走加密传输、UnEncrypted表示不走加密传输，Encrypted表示走加密传输，默认UnEncrypted
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptConn: str
        :param _DatabaseNetEnv: 数据库所属网络环境，AccessType为云联网(ccn)时必填， UserIDC表示用户IDC、TencentVPC表示腾讯云VPC；
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseNetEnv: str
        """
        self._Region = None
        self._Role = None
        self._DbKernel = None
        self._InstanceId = None
        self._Ip = None
        self._Port = None
        self._User = None
        self._Password = None
        self._DbName = None
        self._VpcId = None
        self._SubnetId = None
        self._CvmInstanceId = None
        self._UniqDcgId = None
        self._UniqVpnGwId = None
        self._CcnId = None
        self._Supplier = None
        self._EngineVersion = None
        self._Account = None
        self._AccountMode = None
        self._AccountRole = None
        self._RoleExternalId = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._TmpToken = None
        self._EncryptConn = None
        self._DatabaseNetEnv = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def DbKernel(self):
        return self._DbKernel

    @DbKernel.setter
    def DbKernel(self, DbKernel):
        self._DbKernel = DbKernel

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CvmInstanceId(self):
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def UniqVpnGwId(self):
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def Supplier(self):
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def AccountMode(self):
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def AccountRole(self):
        return self._AccountRole

    @AccountRole.setter
    def AccountRole(self, AccountRole):
        self._AccountRole = AccountRole

    @property
    def RoleExternalId(self):
        return self._RoleExternalId

    @RoleExternalId.setter
    def RoleExternalId(self, RoleExternalId):
        self._RoleExternalId = RoleExternalId

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken

    @property
    def EncryptConn(self):
        return self._EncryptConn

    @EncryptConn.setter
    def EncryptConn(self, EncryptConn):
        self._EncryptConn = EncryptConn

    @property
    def DatabaseNetEnv(self):
        return self._DatabaseNetEnv

    @DatabaseNetEnv.setter
    def DatabaseNetEnv(self, DatabaseNetEnv):
        self._DatabaseNetEnv = DatabaseNetEnv


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Role = params.get("Role")
        self._DbKernel = params.get("DbKernel")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._DbName = params.get("DbName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._CcnId = params.get("CcnId")
        self._Supplier = params.get("Supplier")
        self._EngineVersion = params.get("EngineVersion")
        self._Account = params.get("Account")
        self._AccountMode = params.get("AccountMode")
        self._AccountRole = params.get("AccountRole")
        self._RoleExternalId = params.get("RoleExternalId")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._TmpToken = params.get("TmpToken")
        self._EncryptConn = params.get("EncryptConn")
        self._DatabaseNetEnv = params.get("DatabaseNetEnv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfoItem(AbstractModel):
    """任务错误信息

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Solution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param _ErrorLog: 错误日志信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorLog: str
        :param _HelpDoc: 文档提示
注意：此字段可能返回 null，表示取不到有效值。
        :type HelpDoc: str
        """
        self._Code = None
        self._Solution = None
        self._ErrorLog = None
        self._HelpDoc = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Solution(self):
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def ErrorLog(self):
        return self._ErrorLog

    @ErrorLog.setter
    def ErrorLog(self, ErrorLog):
        self._ErrorLog = ErrorLog

    @property
    def HelpDoc(self):
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Solution = params.get("Solution")
        self._ErrorLog = params.get("ErrorLog")
        self._HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMigrateJobRequest(AbstractModel):
    """IsolateMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMigrateJobResponse(AbstractModel):
    """IsolateMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class IsolateSyncJobRequest(AbstractModel):
    """IsolateSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSyncJobResponse(AbstractModel):
    """IsolateSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class JobItem(AbstractModel):
    """迁移任务列表

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _JobName: 数据迁移任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param _CreateTime: 任务创建(提交)时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 任务更新时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _StartTime: 任务开始执行时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务执行结束时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _BriefMsg: 迁移任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefMsg: str
        :param _Status: 任务状态，取值为：creating(创建中)、created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)、
pausing(暂停中)、
manualPaused(已暂停)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _RunMode: 任务运行模式，值包括：immediate(立即运行)，timed(定时运行)
注意：此字段可能返回 null，表示取不到有效值。
        :type RunMode: str
        :param _ExpectRunTime: 期待启动时间，当RunMode取值为timed时，此值必填，形如：2022-07-11 16:20:49
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectRunTime: str
        :param _Action: 任务操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param _StepInfo: 迁移执行过程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param _SrcInfo: 源实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _DstInfo: 目标端信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _CompareTask: 数据一致性校验结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param _TradeInfo: 计费状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param _Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param _AutoRetryTimeRangeMinutes: 自动重试时间段信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRetryTimeRangeMinutes: int
        """
        self._JobId = None
        self._JobName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._StartTime = None
        self._EndTime = None
        self._BriefMsg = None
        self._Status = None
        self._RunMode = None
        self._ExpectRunTime = None
        self._Action = None
        self._StepInfo = None
        self._SrcInfo = None
        self._DstInfo = None
        self._CompareTask = None
        self._TradeInfo = None
        self._Tags = None
        self._AutoRetryTimeRangeMinutes = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BriefMsg(self):
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StepInfo(self):
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def CompareTask(self):
        return self._CompareTask

    @CompareTask.setter
    def CompareTask(self, CompareTask):
        self._CompareTask = CompareTask

    @property
    def TradeInfo(self):
        return self._TradeInfo

    @TradeInfo.setter
    def TradeInfo(self, TradeInfo):
        self._TradeInfo = TradeInfo

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRetryTimeRangeMinutes(self):
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._BriefMsg = params.get("BriefMsg")
        self._Status = params.get("Status")
        self._RunMode = params.get("RunMode")
        self._ExpectRunTime = params.get("ExpectRunTime")
        if params.get("Action") is not None:
            self._Action = MigrateAction()
            self._Action._deserialize(params.get("Action"))
        if params.get("StepInfo") is not None:
            self._StepInfo = MigrateDetailInfo()
            self._StepInfo._deserialize(params.get("StepInfo"))
        if params.get("SrcInfo") is not None:
            self._SrcInfo = DBEndpointInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DBEndpointInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        if params.get("CompareTask") is not None:
            self._CompareTask = CompareTaskInfo()
            self._CompareTask._deserialize(params.get("CompareTask"))
        if params.get("TradeInfo") is not None:
            self._TradeInfo = TradeInfo()
            self._TradeInfo._deserialize(params.get("TradeInfo"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaOption(AbstractModel):
    """目标端为kakfa时添加的同步选项字段

    """

    def __init__(self):
        r"""
        :param _DataType: 投递到kafka的数据类型，如Avro,Json
        :type DataType: str
        :param _TopicType: 同步topic策略，如Single（集中投递到单topic）,Multi (自定义topic名称)
        :type TopicType: str
        :param _DDLTopicName: 用于存储ddl的topic
        :type DDLTopicName: str
        :param _TopicRules: 单topic和自定义topic的描述
        :type TopicRules: list of TopicRule
        """
        self._DataType = None
        self._TopicType = None
        self._DDLTopicName = None
        self._TopicRules = None

    @property
    def DataType(self):
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def DDLTopicName(self):
        return self._DDLTopicName

    @DDLTopicName.setter
    def DDLTopicName(self, DDLTopicName):
        self._DDLTopicName = DDLTopicName

    @property
    def TopicRules(self):
        return self._TopicRules

    @TopicRules.setter
    def TopicRules(self, TopicRules):
        self._TopicRules = TopicRules


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._TopicType = params.get("TopicType")
        self._DDLTopicName = params.get("DDLTopicName")
        if params.get("TopicRules") is not None:
            self._TopicRules = []
            for item in params.get("TopicRules"):
                obj = TopicRule()
                obj._deserialize(item)
                self._TopicRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValuePairOption(AbstractModel):
    """存放配置时的额外信息

    """

    def __init__(self):
        r"""
        :param _Key: 选项key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 选项value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateAction(AbstractModel):
    """任务操作信息，包含迁移任务的所有操作列表，及迁移任务在当前状态下允许的操作列表

    """

    def __init__(self):
        r"""
        :param _AllAction: 任务的所有操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AllAction: list of str
        :param _AllowedAction: 任务在当前状态下允许的操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowedAction: list of str
        """
        self._AllAction = None
        self._AllowedAction = None

    @property
    def AllAction(self):
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        return self._AllowedAction

    @AllowedAction.setter
    def AllowedAction(self, AllowedAction):
        self._AllowedAction = AllowedAction


    def _deserialize(self, params):
        self._AllAction = params.get("AllAction")
        self._AllowedAction = params.get("AllowedAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDBItem(AbstractModel):
    """查询迁移实例列表的实例对象

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Vip: 实例Vip
        :type Vip: str
        :param _Vport: 实例Vport
        :type Vport: int
        :param _Usable: 是否可以作为迁移对象，1-可以，0-不可以
        :type Usable: int
        :param _Hint: 不可以作为迁移对象的原因
        :type Hint: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Vip = None
        self._Vport = None
        self._Usable = None
        self._Hint = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Usable(self):
        return self._Usable

    @Usable.setter
    def Usable(self, Usable):
        self._Usable = Usable

    @property
    def Hint(self):
        return self._Hint

    @Hint.setter
    def Hint(self, Hint):
        self._Hint = Hint


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Usable = params.get("Usable")
        self._Hint = params.get("Hint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDetailInfo(AbstractModel):
    """迁移执行过程信息

    """

    def __init__(self):
        r"""
        :param _StepAll: 总步骤数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepAll: int
        :param _StepNow: 当前步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNow: int
        :param _MasterSlaveDistance: 主从差距，MB；只在任务正常，迁移或者同步的最后一步（追Binlog的阶段才有校），如果是非法值，返回-1
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterSlaveDistance: int
        :param _SecondsBehindMaster: 主从差距，秒；只在任务正常，迁移或者同步的最后一步（追Binlog的阶段才有校），如果是非法值，返回-1
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondsBehindMaster: int
        :param _StepInfo: 步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: list of StepDetailInfo
        """
        self._StepAll = None
        self._StepNow = None
        self._MasterSlaveDistance = None
        self._SecondsBehindMaster = None
        self._StepInfo = None

    @property
    def StepAll(self):
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def MasterSlaveDistance(self):
        return self._MasterSlaveDistance

    @MasterSlaveDistance.setter
    def MasterSlaveDistance(self, MasterSlaveDistance):
        self._MasterSlaveDistance = MasterSlaveDistance

    @property
    def SecondsBehindMaster(self):
        return self._SecondsBehindMaster

    @SecondsBehindMaster.setter
    def SecondsBehindMaster(self, SecondsBehindMaster):
        self._SecondsBehindMaster = SecondsBehindMaster

    @property
    def StepInfo(self):
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo


    def _deserialize(self, params):
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._MasterSlaveDistance = params.get("MasterSlaveDistance")
        self._SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self._StepInfo = []
            for item in params.get("StepInfo"):
                obj = StepDetailInfo()
                obj._deserialize(item)
                self._StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOption(AbstractModel):
    """迁移选项，描述任务如何执行迁移等一系列配置信息

    """

    def __init__(self):
        r"""
        :param _DatabaseTable: 迁移对象选项，需要告知迁移服务迁移哪些库表对象
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseTable: :class:`tencentcloud.dts.v20211206.models.DatabaseTableObject`
        :param _MigrateType: 迁移类型，full(全量迁移)，structure(结构迁移)，fullAndIncrement(全量加增量迁移)， 默认为fullAndIncrement
注意：此字段可能返回 null，表示取不到有效值。
        :type MigrateType: str
        :param _Consistency: 数据一致性校验选项， 默认为不开启一致性校验
注意：此字段可能返回 null，表示取不到有效值。
        :type Consistency: :class:`tencentcloud.dts.v20211206.models.ConsistencyOption`
        :param _IsMigrateAccount: 是否迁移账号，yes(迁移账号)，no(不迁移账号)
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMigrateAccount: bool
        :param _IsOverrideRoot: 是否用源库Root账户覆盖目标库，值包括：false-不覆盖，true-覆盖，选择库表或者结构迁移时应该为false，注意只对旧版迁移有效
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOverrideRoot: bool
        :param _IsDstReadOnly: 是否在迁移时设置目标库只读(仅对mysql有效)，true(设置只读)、false(不设置只读，默认此值)
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDstReadOnly: bool
        :param _ExtraAttr: 其他附加信息，对于特定库可设置额外参数，Redis可定义如下的参数: 
["ClientOutputBufferHardLimit":512, 	从机缓冲区的硬性容量限制(MB) 	"ClientOutputBufferSoftLimit":512, 	从机缓冲区的软性容量限制(MB) 	"ClientOutputBufferPersistTime":60, 从机缓冲区的软性限制持续时间(秒) 	"ReplBacklogSize":512, 	环形缓冲区容量限制(MB) 	"ReplTimeout":120，		复制超时时间(秒) ]
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraAttr: list of KeyValuePairOption
        """
        self._DatabaseTable = None
        self._MigrateType = None
        self._Consistency = None
        self._IsMigrateAccount = None
        self._IsOverrideRoot = None
        self._IsDstReadOnly = None
        self._ExtraAttr = None

    @property
    def DatabaseTable(self):
        return self._DatabaseTable

    @DatabaseTable.setter
    def DatabaseTable(self, DatabaseTable):
        self._DatabaseTable = DatabaseTable

    @property
    def MigrateType(self):
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def Consistency(self):
        return self._Consistency

    @Consistency.setter
    def Consistency(self, Consistency):
        self._Consistency = Consistency

    @property
    def IsMigrateAccount(self):
        return self._IsMigrateAccount

    @IsMigrateAccount.setter
    def IsMigrateAccount(self, IsMigrateAccount):
        self._IsMigrateAccount = IsMigrateAccount

    @property
    def IsOverrideRoot(self):
        return self._IsOverrideRoot

    @IsOverrideRoot.setter
    def IsOverrideRoot(self, IsOverrideRoot):
        self._IsOverrideRoot = IsOverrideRoot

    @property
    def IsDstReadOnly(self):
        return self._IsDstReadOnly

    @IsDstReadOnly.setter
    def IsDstReadOnly(self, IsDstReadOnly):
        self._IsDstReadOnly = IsDstReadOnly

    @property
    def ExtraAttr(self):
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr


    def _deserialize(self, params):
        if params.get("DatabaseTable") is not None:
            self._DatabaseTable = DatabaseTableObject()
            self._DatabaseTable._deserialize(params.get("DatabaseTable"))
        self._MigrateType = params.get("MigrateType")
        if params.get("Consistency") is not None:
            self._Consistency = ConsistencyOption()
            self._Consistency._deserialize(params.get("Consistency"))
        self._IsMigrateAccount = params.get("IsMigrateAccount")
        self._IsOverrideRoot = params.get("IsOverrideRoot")
        self._IsDstReadOnly = params.get("IsDstReadOnly")
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskNameRequest(AbstractModel):
    """ModifyCompareTaskName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务 Id
        :type JobId: str
        :param _CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        :param _TaskName: 一致性校验任务名称
        :type TaskName: str
        """
        self._JobId = None
        self._CompareTaskId = None
        self._TaskName = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskNameResponse(AbstractModel):
    """ModifyCompareTaskName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCompareTaskRequest(AbstractModel):
    """ModifyCompareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 Id
        :type JobId: str
        :param _CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ObjectMode: 数据对比对象模式，sameAsMigrate(全部迁移对象， 默认为此项配置)、custom(自定义)，注意自定义对比对象必须是迁移对象的子集
        :type ObjectMode: str
        :param _Objects: 对比对象，若CompareObjectMode取值为custom，则此项必填
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _Options: 一致性校验选项
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        self._JobId = None
        self._CompareTaskId = None
        self._TaskName = None
        self._ObjectMode = None
        self._Objects = None
        self._Options = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ObjectMode(self):
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Objects(self):
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Options(self):
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._TaskName = params.get("TaskName")
        self._ObjectMode = params.get("ObjectMode")
        if params.get("Objects") is not None:
            self._Objects = CompareObject()
            self._Objects._deserialize(params.get("Objects"))
        if params.get("Options") is not None:
            self._Options = CompareOptions()
            self._Options._deserialize(params.get("Options"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskResponse(AbstractModel):
    """ModifyCompareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrateJobSpecRequest(AbstractModel):
    """ModifyMigrateJobSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id
        :type JobId: str
        :param _NewInstanceClass: 新实例规格大小，包括：micro、small、medium、large、xlarge、2xlarge
        :type NewInstanceClass: str
        """
        self._JobId = None
        self._NewInstanceClass = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NewInstanceClass(self):
        return self._NewInstanceClass

    @NewInstanceClass.setter
    def NewInstanceClass(self, NewInstanceClass):
        self._NewInstanceClass = NewInstanceClass


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._NewInstanceClass = params.get("NewInstanceClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobSpecResponse(AbstractModel):
    """ModifyMigrateJobSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrateNameRequest(AbstractModel):
    """ModifyMigrateName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务id
        :type JobId: str
        :param _JobName: 修改后的迁移任务名
        :type JobName: str
        """
        self._JobId = None
        self._JobName = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateNameResponse(AbstractModel):
    """ModifyMigrateName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrationJobRequest(AbstractModel):
    """ModifyMigrationJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id
        :type JobId: str
        :param _RunMode: 运行模式，取值如：immediate(表示立即运行)、timed(表示定时运行)
        :type RunMode: str
        :param _MigrateOption: 迁移任务配置选项，描述任务如何执行迁移等一系列配置信息
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param _SrcInfo: 源实例信息
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _JobName: 迁移任务名称，最大长度128
        :type JobName: str
        :param _ExpectRunTime: 期待启动时间，当RunMode取值为timed时，此值必填，形如："2006-01-02 15:04:05"
        :type ExpectRunTime: str
        :param _Tags: 标签信息
        :type Tags: list of TagItem
        :param _AutoRetryTimeRangeMinutes: 自动重试的时间段、可设置5至720分钟、0表示不重试
        :type AutoRetryTimeRangeMinutes: int
        """
        self._JobId = None
        self._RunMode = None
        self._MigrateOption = None
        self._SrcInfo = None
        self._DstInfo = None
        self._JobName = None
        self._ExpectRunTime = None
        self._Tags = None
        self._AutoRetryTimeRangeMinutes = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def MigrateOption(self):
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def ExpectRunTime(self):
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRetryTimeRangeMinutes(self):
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RunMode = params.get("RunMode")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        if params.get("SrcInfo") is not None:
            self._SrcInfo = DBEndpointInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DBEndpointInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._JobName = params.get("JobName")
        self._ExpectRunTime = params.get("ExpectRunTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationJobResponse(AbstractModel):
    """ModifyMigrationJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySyncJobConfigRequest(AbstractModel):
    """ModifySyncJobConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        :param _DynamicObjects: 修改后的同步对象
        :type DynamicObjects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param _DynamicOptions: 修改后的同步任务选项
        :type DynamicOptions: :class:`tencentcloud.dts.v20211206.models.DynamicOptions`
        """
        self._JobId = None
        self._DynamicObjects = None
        self._DynamicOptions = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DynamicObjects(self):
        return self._DynamicObjects

    @DynamicObjects.setter
    def DynamicObjects(self, DynamicObjects):
        self._DynamicObjects = DynamicObjects

    @property
    def DynamicOptions(self):
        return self._DynamicOptions

    @DynamicOptions.setter
    def DynamicOptions(self, DynamicOptions):
        self._DynamicOptions = DynamicOptions


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("DynamicObjects") is not None:
            self._DynamicObjects = Objects()
            self._DynamicObjects._deserialize(params.get("DynamicObjects"))
        if params.get("DynamicOptions") is not None:
            self._DynamicOptions = DynamicOptions()
            self._DynamicOptions._deserialize(params.get("DynamicOptions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySyncJobConfigResponse(AbstractModel):
    """ModifySyncJobConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Objects(AbstractModel):
    """同步的数据库对对象描述

    """

    def __init__(self):
        r"""
        :param _Mode: 同步对象类型 Partial(部分对象)
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param _Databases: 同步对象，当 Mode 为 Partial 时，不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of Database
        :param _AdvancedObjects: 高级对象类型，如function、procedure，当需要同步高级对象时，初始化类型必须包含结构初始化类型，即任务的Options.InitType字段值为Structure或Full
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedObjects: list of str
        :param _OnlineDDL: OnlineDDL类型，冗余字段不做配置用途
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineDDL: :class:`tencentcloud.dts.v20211206.models.OnlineDDL`
        """
        self._Mode = None
        self._Databases = None
        self._AdvancedObjects = None
        self._OnlineDDL = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def AdvancedObjects(self):
        return self._AdvancedObjects

    @AdvancedObjects.setter
    def AdvancedObjects(self, AdvancedObjects):
        self._AdvancedObjects = AdvancedObjects

    @property
    def OnlineDDL(self):
        return self._OnlineDDL

    @OnlineDDL.setter
    def OnlineDDL(self, OnlineDDL):
        self._OnlineDDL = OnlineDDL


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._AdvancedObjects = params.get("AdvancedObjects")
        if params.get("OnlineDDL") is not None:
            self._OnlineDDL = OnlineDDL()
            self._OnlineDDL._deserialize(params.get("OnlineDDL"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OnlineDDL(AbstractModel):
    """OnlineDDL类型

    """

    def __init__(self):
        r"""
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Options(AbstractModel):
    """数据同步中的选项

    """

    def __init__(self):
        r"""
        :param _InitType: 同步初始化选项，Data(全量数据初始化)、Structure(结构初始化)、Full(全量数据且结构初始化，默认)、None(仅增量)
注意：此字段可能返回 null，表示取不到有效值。
        :type InitType: str
        :param _DealOfExistSameTable: 同名表的处理，ReportErrorAfterCheck(前置校验并报错，默认)、InitializeAfterDelete(删除并重新初始化)、ExecuteAfterIgnore(忽略并继续执行)
注意：此字段可能返回 null，表示取不到有效值。
        :type DealOfExistSameTable: str
        :param _ConflictHandleType: 冲突处理选项，ReportError(报错，默认为该值)、Ignore(忽略)、Cover(覆盖)、ConditionCover(条件覆盖)
注意：此字段可能返回 null，表示取不到有效值。
        :type ConflictHandleType: str
        :param _AddAdditionalColumn: 是否添加附加列
注意：此字段可能返回 null，表示取不到有效值。
        :type AddAdditionalColumn: bool
        :param _OpTypes: 所要同步的DML和DDL的选项，Insert(插入操作)、Update(更新操作)、Delete(删除操作)、DDL(结构同步)， 不填（不选），PartialDDL(自定义,和DdlOptions一起起作用 )
注意：此字段可能返回 null，表示取不到有效值。
        :type OpTypes: list of str
        :param _ConflictHandleOption: 冲突处理的详细选项，如条件覆盖中的条件行和条件操作
注意：此字段可能返回 null，表示取不到有效值。
        :type ConflictHandleOption: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        :param _DdlOptions: DDL同步选项，具体描述要同步那些DDL
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlOptions: list of DdlOption
        :param _KafkaOption: kafka同步选项
注意：此字段可能返回 null，表示取不到有效值。
        :type KafkaOption: :class:`tencentcloud.dts.v20211206.models.KafkaOption`
        """
        self._InitType = None
        self._DealOfExistSameTable = None
        self._ConflictHandleType = None
        self._AddAdditionalColumn = None
        self._OpTypes = None
        self._ConflictHandleOption = None
        self._DdlOptions = None
        self._KafkaOption = None

    @property
    def InitType(self):
        return self._InitType

    @InitType.setter
    def InitType(self, InitType):
        self._InitType = InitType

    @property
    def DealOfExistSameTable(self):
        return self._DealOfExistSameTable

    @DealOfExistSameTable.setter
    def DealOfExistSameTable(self, DealOfExistSameTable):
        self._DealOfExistSameTable = DealOfExistSameTable

    @property
    def ConflictHandleType(self):
        return self._ConflictHandleType

    @ConflictHandleType.setter
    def ConflictHandleType(self, ConflictHandleType):
        self._ConflictHandleType = ConflictHandleType

    @property
    def AddAdditionalColumn(self):
        return self._AddAdditionalColumn

    @AddAdditionalColumn.setter
    def AddAdditionalColumn(self, AddAdditionalColumn):
        self._AddAdditionalColumn = AddAdditionalColumn

    @property
    def OpTypes(self):
        return self._OpTypes

    @OpTypes.setter
    def OpTypes(self, OpTypes):
        self._OpTypes = OpTypes

    @property
    def ConflictHandleOption(self):
        return self._ConflictHandleOption

    @ConflictHandleOption.setter
    def ConflictHandleOption(self, ConflictHandleOption):
        self._ConflictHandleOption = ConflictHandleOption

    @property
    def DdlOptions(self):
        return self._DdlOptions

    @DdlOptions.setter
    def DdlOptions(self, DdlOptions):
        self._DdlOptions = DdlOptions

    @property
    def KafkaOption(self):
        return self._KafkaOption

    @KafkaOption.setter
    def KafkaOption(self, KafkaOption):
        self._KafkaOption = KafkaOption


    def _deserialize(self, params):
        self._InitType = params.get("InitType")
        self._DealOfExistSameTable = params.get("DealOfExistSameTable")
        self._ConflictHandleType = params.get("ConflictHandleType")
        self._AddAdditionalColumn = params.get("AddAdditionalColumn")
        self._OpTypes = params.get("OpTypes")
        if params.get("ConflictHandleOption") is not None:
            self._ConflictHandleOption = ConflictHandleOption()
            self._ConflictHandleOption._deserialize(params.get("ConflictHandleOption"))
        if params.get("DdlOptions") is not None:
            self._DdlOptions = []
            for item in params.get("DdlOptions"):
                obj = DdlOption()
                obj._deserialize(item)
                self._DdlOptions.append(obj)
        if params.get("KafkaOption") is not None:
            self._KafkaOption = KafkaOption()
            self._KafkaOption._deserialize(params.get("KafkaOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseMigrateJobRequest(AbstractModel):
    """PauseMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseMigrateJobResponse(AbstractModel):
    """PauseMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PauseSyncJobRequest(AbstractModel):
    """PauseSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseSyncJobResponse(AbstractModel):
    """PauseSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ProcessProgress(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        r"""
        :param _Status: 步骤的状态， 包括：notStarted(未开始)、running(运行中)、success(成功)、failed(失败)等
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Percent: 进度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _StepAll: 总的步骤数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepAll: int
        :param _StepNow: 当前进行的步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNow: int
        :param _Message: 当前步骤输出提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Steps: 步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Steps: list of StepDetailInfo
        """
        self._Status = None
        self._Percent = None
        self._StepAll = None
        self._StepNow = None
        self._Message = None
        self._Steps = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def StepAll(self):
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Steps(self):
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._Message = params.get("Message")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = StepDetailInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStepTip(AbstractModel):
    """错误信息及告警信息对象

    """

    def __init__(self):
        r"""
        :param _Message: 提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Solution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param _HelpDoc: 文档提示
注意：此字段可能返回 null，表示取不到有效值。
        :type HelpDoc: str
        """
        self._Message = None
        self._Solution = None
        self._HelpDoc = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Solution(self):
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def HelpDoc(self):
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Solution = params.get("Solution")
        self._HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMigrateJobRequest(AbstractModel):
    """RecoverMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMigrateJobResponse(AbstractModel):
    """RecoverMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RecoverSyncJobRequest(AbstractModel):
    """RecoverSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步实例id（即标识一个同步作业），形如sync-werwfs23
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverSyncJobResponse(AbstractModel):
    """RecoverSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResizeSyncJobRequest(AbstractModel):
    """ResizeSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        :param _NewInstanceClass: 任务规格
        :type NewInstanceClass: str
        """
        self._JobId = None
        self._NewInstanceClass = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NewInstanceClass(self):
        return self._NewInstanceClass

    @NewInstanceClass.setter
    def NewInstanceClass(self, NewInstanceClass):
        self._NewInstanceClass = NewInstanceClass


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._NewInstanceClass = params.get("NewInstanceClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeSyncJobResponse(AbstractModel):
    """ResizeSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResumeMigrateJobRequest(AbstractModel):
    """ResumeMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        :param _ResumeOption: 恢复任务的模式，目前的取值有：clearData 清空目标实例数据，overwrite 以覆盖写的方式执行任务，normal 跟正常流程一样，不做额外动作；注意，clearData、overwrite仅对redis生效，normal仅针对非redis链路生效
        :type ResumeOption: str
        """
        self._JobId = None
        self._ResumeOption = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ResumeOption(self):
        return self._ResumeOption

    @ResumeOption.setter
    def ResumeOption(self, ResumeOption):
        self._ResumeOption = ResumeOption


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ResumeOption = params.get("ResumeOption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeMigrateJobResponse(AbstractModel):
    """ResumeMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResumeSyncJobRequest(AbstractModel):
    """ResumeSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeSyncJobResponse(AbstractModel):
    """ResumeSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RoleItem(AbstractModel):
    """角色对象，postgresql独有参数

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param _NewRoleName: 迁移后的角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NewRoleName: str
        """
        self._RoleName = None
        self._NewRoleName = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def NewRoleName(self):
        return self._NewRoleName

    @NewRoleName.setter
    def NewRoleName(self, NewRoleName):
        self._NewRoleName = NewRoleName


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._NewRoleName = params.get("NewRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCheckItemRequest(AbstractModel):
    """SkipCheckItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        :param _StepIds: 需要跳过校验项的步骤id，需要通过DescribeMigrationCheckJob接口返回StepInfo[i].StepId字段获取，例如：["OptimizeCheck"]
        :type StepIds: list of str
        :param _ForeignKeyFlag: 当出现外键依赖检查导致校验不通过时、可以通过该字段选择是否迁移外键依赖，当StepIds包含ConstraintCheck且该字段值为shield时表示不迁移外键依赖、当StepIds包含ConstraintCheck且值为migrate时表示迁移外键依赖
        :type ForeignKeyFlag: str
        """
        self._JobId = None
        self._StepIds = None
        self._ForeignKeyFlag = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StepIds(self):
        return self._StepIds

    @StepIds.setter
    def StepIds(self, StepIds):
        self._StepIds = StepIds

    @property
    def ForeignKeyFlag(self):
        return self._ForeignKeyFlag

    @ForeignKeyFlag.setter
    def ForeignKeyFlag(self, ForeignKeyFlag):
        self._ForeignKeyFlag = ForeignKeyFlag


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StepIds = params.get("StepIds")
        self._ForeignKeyFlag = params.get("ForeignKeyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCheckItemResponse(AbstractModel):
    """SkipCheckItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Message: 跳过的提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class SkipSyncCheckItemRequest(AbstractModel):
    """SkipSyncCheckItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id，如：sync-4ddgid2
        :type JobId: str
        :param _StepIds: 需要跳过校验项的步骤id，需要通过`DescribeCheckSyncJobResult`接口返回StepInfos[i].StepId字段获取，例如：["OptimizeCheck"]
        :type StepIds: list of str
        """
        self._JobId = None
        self._StepIds = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StepIds(self):
        return self._StepIds

    @StepIds.setter
    def StepIds(self, StepIds):
        self._StepIds = StepIds


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StepIds = params.get("StepIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipSyncCheckItemResponse(AbstractModel):
    """SkipSyncCheckItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SkippedDetail(AbstractModel):
    """跳过校验的表详情

    """

    def __init__(self):
        r"""
        :param _TotalCount: 跳过的表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Items: 跳过校验的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SkippedItem
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SkippedItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkippedItem(AbstractModel):
    """跳过校验的表详情

    """

    def __init__(self):
        r"""
        :param _Db: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Db: str
        :param _Table: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _Reason: 未发起检查的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self._Db = None
        self._Table = None
        self._Reason = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Table = params.get("Table")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCompareRequest(AbstractModel):
    """StartCompare请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务 Id
        :type JobId: str
        :param _CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        """
        self._JobId = None
        self._CompareTaskId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCompareResponse(AbstractModel):
    """StartCompare返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartModifySyncJobRequest(AbstractModel):
    """StartModifySyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartModifySyncJobResponse(AbstractModel):
    """StartModifySyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartSyncJobRequest(AbstractModel):
    """StartSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StepDetailInfo(AbstractModel):
    """步骤信息

    """

    def __init__(self):
        r"""
        :param _StepNo: 步骤序列
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNo: int
        :param _StepName: 步骤展现名称
注意：此字段可能返回 null，表示取不到有效值。
        :type StepName: str
        :param _StepId: 步骤英文标识
注意：此字段可能返回 null，表示取不到有效值。
        :type StepId: str
        :param _Status: 步骤状态:success(成功)、failed(失败)、running(执行中)、notStarted(未执行)、默认为notStarted
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StartTime: 当前步骤开始的时间，格式为"yyyy-mm-dd hh:mm:ss"，该字段不存在或者为空是无意义 注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _StepMessage: 步骤错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepMessage: str
        :param _Percent: 执行进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _Errors: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of ProcessStepTip
        :param _Warnings: 告警提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Warnings: list of ProcessStepTip
        """
        self._StepNo = None
        self._StepName = None
        self._StepId = None
        self._Status = None
        self._StartTime = None
        self._StepMessage = None
        self._Percent = None
        self._Errors = None
        self._Warnings = None

    @property
    def StepNo(self):
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StepMessage(self):
        return self._StepMessage

    @StepMessage.setter
    def StepMessage(self, StepMessage):
        self._StepMessage = StepMessage

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Errors(self):
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Warnings(self):
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._StepMessage = params.get("StepMessage")
        self._Percent = params.get("Percent")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = ProcessStepTip()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("Warnings") is not None:
            self._Warnings = []
            for item in params.get("Warnings"):
                obj = ProcessStepTip()
                obj._deserialize(item)
                self._Warnings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepInfo(AbstractModel):
    """单个步骤的详细信息

    """

    def __init__(self):
        r"""
        :param _StepNo: 步骤编号
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNo: int
        :param _StepName: 步骤名
注意：此字段可能返回 null，表示取不到有效值。
        :type StepName: str
        :param _StepId: 步骤标号
注意：此字段可能返回 null，表示取不到有效值。
        :type StepId: str
        :param _Status: 当前步骤状态,可能返回有 notStarted(未开始)、running(校验中)、failed(校验任务失败)、finished(完成)、skipped(跳过)、paused(暂停)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StartTime: 步骤开始时间，可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _Errors: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of StepTip
        :param _Warnings: 警告信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Warnings: list of StepTip
        :param _Progress: 当前步骤进度，范围为[0-100]，若为-1表示当前步骤不支持查看进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        """
        self._StepNo = None
        self._StepName = None
        self._StepId = None
        self._Status = None
        self._StartTime = None
        self._Errors = None
        self._Warnings = None
        self._Progress = None

    @property
    def StepNo(self):
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Errors(self):
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Warnings(self):
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = StepTip()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("Warnings") is not None:
            self._Warnings = []
            for item in params.get("Warnings"):
                obj = StepTip()
                obj._deserialize(item)
                self._Warnings.append(obj)
        self._Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepTip(AbstractModel):
    """当前步骤错误信息或者警告信息

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Message: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Solution: 解决方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param _HelpDoc: 帮助文档
注意：此字段可能返回 null，表示取不到有效值。
        :type HelpDoc: str
        :param _SkipInfo: 当前步骤跳过信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SkipInfo: str
        """
        self._Code = None
        self._Message = None
        self._Solution = None
        self._HelpDoc = None
        self._SkipInfo = None

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
    def Solution(self):
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def HelpDoc(self):
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc

    @property
    def SkipInfo(self):
        return self._SkipInfo

    @SkipInfo.setter
    def SkipInfo(self, SkipInfo):
        self._SkipInfo = SkipInfo


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._Solution = params.get("Solution")
        self._HelpDoc = params.get("HelpDoc")
        self._SkipInfo = params.get("SkipInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCompareRequest(AbstractModel):
    """StopCompare请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务 Id
        :type JobId: str
        :param _CompareTaskId: 对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :type CompareTaskId: str
        """
        self._JobId = None
        self._CompareTaskId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCompareResponse(AbstractModel):
    """StopCompare返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopSyncJobRequest(AbstractModel):
    """StopSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSyncJobResponse(AbstractModel):
    """StopSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SyncDBEndpointInfos(AbstractModel):
    """数据同步配置多节点数据库的节点信息。多节点数据库，如tdsqlmysql使用该结构；单节点数据库，如mysql使用Endpoint。

    """

    def __init__(self):
        r"""
        :param _Region: 数据库所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _AccessType: 实例网络接入类型，如：extranet(外网)、ipv6(公网ipv6)、cvm(云主机自建)、dcg(专线接入)、vpncloud(vpn接入的实例)、cdb(云数据库)、ccn(云联网)、intranet(自研上云)、vpc(私有网络)等，注意具体可选值依赖当前链路
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: str
        :param _DatabaseType: 实例数据库类型，如：mysql,redis,mongodb,postgresql,mariadb,percona 等
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseType: str
        :param _Info: 数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: list of Endpoint
        """
        self._Region = None
        self._AccessType = None
        self._DatabaseType = None
        self._Info = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccessType(self):
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def DatabaseType(self):
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._AccessType = params.get("AccessType")
        self._DatabaseType = params.get("DatabaseType")
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = Endpoint()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDetailInfo(AbstractModel):
    """同步任务的步骤信息

    """

    def __init__(self):
        r"""
        :param _StepAll: 总步骤数
注意：此字段可能返回 null，表示取不到有效值。
        :type StepAll: int
        :param _StepNow: 当前步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type StepNow: int
        :param _Progress: 总体进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _CurrentStepProgress: 当前步骤进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentStepProgress: int
        :param _MasterSlaveDistance: 同步两端数据量差距
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterSlaveDistance: int
        :param _SecondsBehindMaster: 同步两端时间差距
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondsBehindMaster: int
        :param _Message: 总体描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _StepInfos: 详细步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfos: list of StepInfo
        :param _CauseOfCompareDisable: 不能发起一致性校验的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type CauseOfCompareDisable: str
        """
        self._StepAll = None
        self._StepNow = None
        self._Progress = None
        self._CurrentStepProgress = None
        self._MasterSlaveDistance = None
        self._SecondsBehindMaster = None
        self._Message = None
        self._StepInfos = None
        self._CauseOfCompareDisable = None

    @property
    def StepAll(self):
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CurrentStepProgress(self):
        return self._CurrentStepProgress

    @CurrentStepProgress.setter
    def CurrentStepProgress(self, CurrentStepProgress):
        self._CurrentStepProgress = CurrentStepProgress

    @property
    def MasterSlaveDistance(self):
        return self._MasterSlaveDistance

    @MasterSlaveDistance.setter
    def MasterSlaveDistance(self, MasterSlaveDistance):
        self._MasterSlaveDistance = MasterSlaveDistance

    @property
    def SecondsBehindMaster(self):
        return self._SecondsBehindMaster

    @SecondsBehindMaster.setter
    def SecondsBehindMaster(self, SecondsBehindMaster):
        self._SecondsBehindMaster = SecondsBehindMaster

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def StepInfos(self):
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def CauseOfCompareDisable(self):
        return self._CauseOfCompareDisable

    @CauseOfCompareDisable.setter
    def CauseOfCompareDisable(self, CauseOfCompareDisable):
        self._CauseOfCompareDisable = CauseOfCompareDisable


    def _deserialize(self, params):
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._Progress = params.get("Progress")
        self._CurrentStepProgress = params.get("CurrentStepProgress")
        self._MasterSlaveDistance = params.get("MasterSlaveDistance")
        self._SecondsBehindMaster = params.get("SecondsBehindMaster")
        self._Message = params.get("Message")
        if params.get("StepInfos") is not None:
            self._StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self._StepInfos.append(obj)
        self._CauseOfCompareDisable = params.get("CauseOfCompareDisable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncJobInfo(AbstractModel):
    """同步任务信息

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id，如：sync-btso140
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _JobName: 同步任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param _PayMode: 付款方式，PostPay(按量付费)、PrePay(包年包月)
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _RunMode: 运行模式，Immediate(表示立即运行，默认为此项值)、Timed(表示定时运行)
注意：此字段可能返回 null，表示取不到有效值。
        :type RunMode: str
        :param _ExpectRunTime: 期待运行时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectRunTime: str
        :param _AllActions: 支持的所有操作
注意：此字段可能返回 null，表示取不到有效值。
        :type AllActions: list of str
        :param _Actions: 当前状态能进行的操作
注意：此字段可能返回 null，表示取不到有效值。
        :type Actions: list of str
        :param _Options: 同步选项
注意：此字段可能返回 null，表示取不到有效值。
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param _Objects: 同步库表对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param _Specification: 任务规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param _ExpireTime: 过期时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _SrcRegion: 源端地域，如：ap-guangzhou等
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcRegion: str
        :param _SrcDatabaseType: 源端数据库类型，mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcDatabaseType: str
        :param _SrcAccessType: 源端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcAccessType: str
        :param _SrcInfo: 源端信息，单节点数据库使用
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _DstRegion: 目标端地域，如：ap-guangzhou等
注意：此字段可能返回 null，表示取不到有效值。
        :type DstRegion: str
        :param _DstDatabaseType: 目标端数据库类型，mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
注意：此字段可能返回 null，表示取不到有效值。
        :type DstDatabaseType: str
        :param _DstAccessType: 目标端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)
注意：此字段可能返回 null，表示取不到有效值。
        :type DstAccessType: str
        :param _DstInfo: 目标端信息，单节点数据库使用
注意：此字段可能返回 null，表示取不到有效值。
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _CreateTime: 创建时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _StartTime: 开始时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _Status: 任务状态，UnInitialized(未初始化)、Initialized(已初始化)、Checking(校验中)、CheckPass(校验通过)、CheckNotPass(校验不通过)、ReadyRunning(准备运行)、Running(运行中)、Pausing(暂停中)、Paused(已暂停)、Stopping(停止中)、Stopped(已结束)、ResumableErr(任务错误)、Resuming(恢复中)、Failed(失败)、Released(已释放)、Resetting(重置中)、Unknown(未知)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _EndTime: 结束时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Tags: 标签相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param _Detail: 同步任务运行步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: :class:`tencentcloud.dts.v20211206.models.SyncDetailInfo`
        :param _TradeStatus: 用于计费的状态，可能取值有：Normal(正常状态)、Resizing(变配中)、Renewing(续费中)、Isolating(隔离中)、Isolated(已隔离)、Offlining(下线中)、Offlined(已下线)、NotBilled(未计费)、Recovering(解隔离)、PostPay2Prepaying(按量计费转包年包月中)、PrePay2Postpaying(包年包月转按量计费中)
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeStatus: str
        :param _InstanceClass: 同步链路规格，如micro,small,medium,large
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceClass: str
        :param _AutoRenew: 自动续费标识，当PayMode值为PrePay则此项配置有意义，取值为：1（表示自动续费）、0（不自动续费）
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenew: int
        :param _OfflineTime: 下线时间，格式为 yyyy-mm-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTime: str
        :param _AutoRetryTimeRangeMinutes: 自动重试时间段设置
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRetryTimeRangeMinutes: int
        """
        self._JobId = None
        self._JobName = None
        self._PayMode = None
        self._RunMode = None
        self._ExpectRunTime = None
        self._AllActions = None
        self._Actions = None
        self._Options = None
        self._Objects = None
        self._Specification = None
        self._ExpireTime = None
        self._SrcRegion = None
        self._SrcDatabaseType = None
        self._SrcAccessType = None
        self._SrcInfo = None
        self._DstRegion = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._DstInfo = None
        self._CreateTime = None
        self._StartTime = None
        self._Status = None
        self._EndTime = None
        self._Tags = None
        self._Detail = None
        self._TradeStatus = None
        self._InstanceClass = None
        self._AutoRenew = None
        self._OfflineTime = None
        self._AutoRetryTimeRangeMinutes = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def AllActions(self):
        return self._AllActions

    @AllActions.setter
    def AllActions(self, AllActions):
        self._AllActions = AllActions

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Options(self):
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Objects(self):
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SrcRegion(self):
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def SrcDatabaseType(self):
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstRegion(self):
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def DstDatabaseType(self):
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def TradeStatus(self):
        return self._TradeStatus

    @TradeStatus.setter
    def TradeStatus(self, TradeStatus):
        self._TradeStatus = TradeStatus

    @property
    def InstanceClass(self):
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def AutoRetryTimeRangeMinutes(self):
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._PayMode = params.get("PayMode")
        self._RunMode = params.get("RunMode")
        self._ExpectRunTime = params.get("ExpectRunTime")
        self._AllActions = params.get("AllActions")
        self._Actions = params.get("Actions")
        if params.get("Options") is not None:
            self._Options = Options()
            self._Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self._Objects = Objects()
            self._Objects._deserialize(params.get("Objects"))
        self._Specification = params.get("Specification")
        self._ExpireTime = params.get("ExpireTime")
        self._SrcRegion = params.get("SrcRegion")
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = Endpoint()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        self._DstRegion = params.get("DstRegion")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = Endpoint()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._EndTime = params.get("EndTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Detail") is not None:
            self._Detail = SyncDetailInfo()
            self._Detail._deserialize(params.get("Detail"))
        self._TradeStatus = params.get("TradeStatus")
        self._InstanceClass = params.get("InstanceClass")
        self._AutoRenew = params.get("AutoRenew")
        self._OfflineTime = params.get("OfflineTime")
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """数据同步库表信息描述

    """

    def __init__(self):
        r"""
        :param _TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param _NewTableName: 新表名
注意：此字段可能返回 null，表示取不到有效值。
        :type NewTableName: str
        :param _FilterCondition: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterCondition: str
        :param _TmpTables: 同步临时表，注意此配置与NewTableName互斥，只能使用其中一种。当配置的同步对象为表级别且TableEditMode为pt时此项有意义，针对pt-osc等工具在同步过程中产生的临时表进行同步，需要提前将可能的临时表配置在这里，否则不会同步任何临时表。示例，如要对t1进行pt-osc操作，此项配置应该为["\_t1\_new","\_t1\_old"]；如要对t1进行gh-ost操作，此项配置应该为["\_t1\_ghc","\_t1\_gho","\_t1\_del"]，pt-osc与gh-ost产生的临时表可同时配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpTables: list of str
        :param _TableEditMode: 编辑表类型，rename(表映射)，pt(同步附加表)
注意：此字段可能返回 null，表示取不到有效值。
        :type TableEditMode: str
        """
        self._TableName = None
        self._NewTableName = None
        self._FilterCondition = None
        self._TmpTables = None
        self._TableEditMode = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName

    @property
    def FilterCondition(self):
        return self._FilterCondition

    @FilterCondition.setter
    def FilterCondition(self, FilterCondition):
        self._FilterCondition = FilterCondition

    @property
    def TmpTables(self):
        return self._TmpTables

    @TmpTables.setter
    def TmpTables(self, TmpTables):
        self._TmpTables = TmpTables

    @property
    def TableEditMode(self):
        return self._TableEditMode

    @TableEditMode.setter
    def TableEditMode(self, TableEditMode):
        self._TableEditMode = TableEditMode


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._NewTableName = params.get("NewTableName")
        self._FilterCondition = params.get("FilterCondition")
        self._TmpTables = params.get("TmpTables")
        self._TableEditMode = params.get("TableEditMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableItem(AbstractModel):
    """表对象集合，当 TableMode 为 partial 时，此项需要填写

    """

    def __init__(self):
        r"""
        :param _TableName: 迁移的表名，大小写敏感
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param _NewTableName: 迁移后的表名，当TableEditMode为rename时此项必填，注意此配置与TmpTables互斥，只能使用其中一种
注意：此字段可能返回 null，表示取不到有效值。
        :type NewTableName: str
        :param _TmpTables: 迁移临时表，注意此配置与NewTableName互斥，只能使用其中一种。当配置的同步对象为表级别且TableEditMode为pt时此项有意义，针对pt-osc等工具在迁移过程中产生的临时表进行同步，需要提前将可能的临时表配置在这里，否则不会同步任何临时表。示例，如要对t1进行pt-osc操作，此项配置应该为["\_t1\_new","\_t1\_old"]；如要对t1进行gh-ost操作，此项配置应该为["\_t1\_ghc","\_t1\_gho","\_t1\_del"]，pt-osc与gh-ost产生的临时表可同时配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpTables: list of str
        :param _TableEditMode: 编辑表类型，rename(表映射)，pt(同步附加表)
注意：此字段可能返回 null，表示取不到有效值。
        :type TableEditMode: str
        """
        self._TableName = None
        self._NewTableName = None
        self._TmpTables = None
        self._TableEditMode = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName

    @property
    def TmpTables(self):
        return self._TmpTables

    @TmpTables.setter
    def TmpTables(self, TmpTables):
        self._TmpTables = TmpTables

    @property
    def TableEditMode(self):
        return self._TableEditMode

    @TableEditMode.setter
    def TableEditMode(self, TableEditMode):
        self._TableEditMode = TableEditMode


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._NewTableName = params.get("NewTableName")
        self._TmpTables = params.get("TmpTables")
        self._TableEditMode = params.get("TableEditMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """标签过滤

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键值
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagItem(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRule(AbstractModel):
    """单topic和自定义topic的描述

    """

    def __init__(self):
        r"""
        :param _TopicName: topic名
        :type TopicName: str
        :param _PartitionType: topic分区策略，如 自定义topic：Random（随机投递），集中投递到单Topic：AllInPartitionZero（全部投递至partition0）、PartitionByTable(按表名分区)、PartitionByTableAndKey(按表名加主键分区)
        :type PartitionType: str
        :param _DbMatchMode: 库名匹配规则，仅“自定义topic”生效，如Regular（正则匹配）, Default(不符合匹配规则的剩余库)，数组中必须有一项为‘Default’
        :type DbMatchMode: str
        :param _DbName: 库名，仅“自定义topic”时，DbMatchMode=Regular生效
        :type DbName: str
        :param _TableMatchMode: 表名匹配规则，仅“自定义topic”生效，如Regular（正则匹配）, Default(不符合匹配规则的剩余表)，数组中必须有一项为‘Default’
        :type TableMatchMode: str
        :param _TableName: 表名，仅“自定义topic”时，TableMatchMode=Regular生效
        :type TableName: str
        """
        self._TopicName = None
        self._PartitionType = None
        self._DbMatchMode = None
        self._DbName = None
        self._TableMatchMode = None
        self._TableName = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionType(self):
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def DbMatchMode(self):
        return self._DbMatchMode

    @DbMatchMode.setter
    def DbMatchMode(self, DbMatchMode):
        self._DbMatchMode = DbMatchMode

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableMatchMode(self):
        return self._TableMatchMode

    @TableMatchMode.setter
    def TableMatchMode(self, TableMatchMode):
        self._TableMatchMode = TableMatchMode

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._PartitionType = params.get("PartitionType")
        self._DbMatchMode = params.get("DbMatchMode")
        self._DbName = params.get("DbName")
        self._TableMatchMode = params.get("TableMatchMode")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeInfo(AbstractModel):
    """计费状态信息

    """

    def __init__(self):
        r"""
        :param _DealName: 交易订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _LastDealName: 上一次交易订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type LastDealName: str
        :param _InstanceClass: 实例规格，包括：micro、small、medium、large、xlarge、2xlarge等
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceClass: str
        :param _TradeStatus: 计费任务状态， normal(计费或待计费)、resizing(变配中)、reversing(冲正中，比较短暂的状态)、isolating(隔离中，比较短暂的状态)、isolated(已隔离)、offlining(下线中)、offlined(已下线)、notBilled(未计费)
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeStatus: str
        :param _ExpireTime: 到期时间，格式为"yyyy-mm-dd hh:mm:ss"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _OfflineTime: 下线时间，格式为"yyyy-mm-dd hh:mm:ss"
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTime: str
        :param _IsolateTime: 隔离时间，格式为"yyyy-mm-dd hh:mm:ss"
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param _OfflineReason: 下线原因
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineReason: str
        :param _IsolateReason: 隔离原因
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateReason: str
        :param _PayType: 付费类型，包括：postpay(后付费)、prepay(预付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type PayType: str
        :param _BillingType: 任务计费类型，包括：billing(计费)、notBilling(不计费)、 promotions(促销活动中)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingType: str
        """
        self._DealName = None
        self._LastDealName = None
        self._InstanceClass = None
        self._TradeStatus = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._IsolateTime = None
        self._OfflineReason = None
        self._IsolateReason = None
        self._PayType = None
        self._BillingType = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def LastDealName(self):
        return self._LastDealName

    @LastDealName.setter
    def LastDealName(self, LastDealName):
        self._LastDealName = LastDealName

    @property
    def InstanceClass(self):
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def TradeStatus(self):
        return self._TradeStatus

    @TradeStatus.setter
    def TradeStatus(self, TradeStatus):
        self._TradeStatus = TradeStatus

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def OfflineReason(self):
        return self._OfflineReason

    @OfflineReason.setter
    def OfflineReason(self, OfflineReason):
        self._OfflineReason = OfflineReason

    @property
    def IsolateReason(self):
        return self._IsolateReason

    @IsolateReason.setter
    def IsolateReason(self, IsolateReason):
        self._IsolateReason = IsolateReason

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def BillingType(self):
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._LastDealName = params.get("LastDealName")
        self._InstanceClass = params.get("InstanceClass")
        self._TradeStatus = params.get("TradeStatus")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._IsolateTime = params.get("IsolateTime")
        self._OfflineReason = params.get("OfflineReason")
        self._IsolateReason = params.get("IsolateReason")
        self._PayType = params.get("PayType")
        self._BillingType = params.get("BillingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class View(AbstractModel):
    """数据同步view的描述

    """

    def __init__(self):
        r"""
        :param _ViewName: view名
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        :param _NewViewName: 预留字段、目前暂时不支持view的重命名
注意：此字段可能返回 null，表示取不到有效值。
        :type NewViewName: str
        """
        self._ViewName = None
        self._NewViewName = None

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def NewViewName(self):
        return self._NewViewName

    @NewViewName.setter
    def NewViewName(self, NewViewName):
        self._NewViewName = NewViewName


    def _deserialize(self, params):
        self._ViewName = params.get("ViewName")
        self._NewViewName = params.get("NewViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewItem(AbstractModel):
    """视图对象

    """

    def __init__(self):
        r"""
        :param _ViewName: 视图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        :param _NewViewName: 迁移后的视图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NewViewName: str
        """
        self._ViewName = None
        self._NewViewName = None

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def NewViewName(self):
        return self._NewViewName

    @NewViewName.setter
    def NewViewName(self, NewViewName):
        self._NewViewName = NewViewName


    def _deserialize(self, params):
        self._ViewName = params.get("ViewName")
        self._NewViewName = params.get("NewViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        