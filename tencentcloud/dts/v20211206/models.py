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


class AdvancedObjectsItem(AbstractModel):
    """数据库不一致的详情，mongodb业务用到

    """

    def __init__(self):
        r"""
        :param _ObjectType: 对象类型,可能得值有：account,index,shardkey,schema
        :type ObjectType: str
        :param _SrcChunk: 源端分块
        :type SrcChunk: str
        :param _DstChunk: 目标端分块
        :type DstChunk: str
        :param _SrcItem: 源端值
        :type SrcItem: str
        :param _DstItem: 目标端值
        :type DstItem: str
        """
        self._ObjectType = None
        self._SrcChunk = None
        self._DstChunk = None
        self._SrcItem = None
        self._DstItem = None

    @property
    def ObjectType(self):
        """对象类型,可能得值有：account,index,shardkey,schema
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def SrcChunk(self):
        """源端分块
        :rtype: str
        """
        return self._SrcChunk

    @SrcChunk.setter
    def SrcChunk(self, SrcChunk):
        self._SrcChunk = SrcChunk

    @property
    def DstChunk(self):
        """目标端分块
        :rtype: str
        """
        return self._DstChunk

    @DstChunk.setter
    def DstChunk(self, DstChunk):
        self._DstChunk = DstChunk

    @property
    def SrcItem(self):
        """源端值
        :rtype: str
        """
        return self._SrcItem

    @SrcItem.setter
    def SrcItem(self, SrcItem):
        self._SrcItem = SrcItem

    @property
    def DstItem(self):
        """目标端值
        :rtype: str
        """
        return self._DstItem

    @DstItem.setter
    def DstItem(self, DstItem):
        self._DstItem = DstItem


    def _deserialize(self, params):
        self._ObjectType = params.get("ObjectType")
        self._SrcChunk = params.get("SrcChunk")
        self._DstChunk = params.get("DstChunk")
        self._SrcItem = params.get("SrcItem")
        self._DstItem = params.get("DstItem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStep(AbstractModel):
    """检查步骤

    """

    def __init__(self):
        r"""
        :param _StepNo: 步骤编号
        :type StepNo: int
        :param _StepId: 步骤Id， 如：ConnectDBCheck、VersionCheck、SrcPrivilegeCheck等，具体校验项和源目标实例相关
        :type StepId: str
        :param _StepName: 步骤名称
        :type StepName: str
        :param _StepStatus: 此检查步骤的结果，pass(校验通过)、failed(校验失败)、notStarted(校验还未开始进行)、blocked(检验阻塞)、warning(校验有告警，但仍通过)
        :type StepStatus: str
        :param _StepMessage: 此检查步骤的错误消息
        :type StepMessage: str
        :param _DetailCheckItems: 每个检查步骤里的具体检查项
        :type DetailCheckItems: list of DetailCheckItem
        :param _HasSkipped: 是否已跳过
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
        """步骤编号
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepId(self):
        """步骤Id， 如：ConnectDBCheck、VersionCheck、SrcPrivilegeCheck等，具体校验项和源目标实例相关
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def StepName(self):
        """步骤名称
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepStatus(self):
        """此检查步骤的结果，pass(校验通过)、failed(校验失败)、notStarted(校验还未开始进行)、blocked(检验阻塞)、warning(校验有告警，但仍通过)
        :rtype: str
        """
        return self._StepStatus

    @StepStatus.setter
    def StepStatus(self, StepStatus):
        self._StepStatus = StepStatus

    @property
    def StepMessage(self):
        """此检查步骤的错误消息
        :rtype: str
        """
        return self._StepMessage

    @StepMessage.setter
    def StepMessage(self, StepMessage):
        self._StepMessage = StepMessage

    @property
    def DetailCheckItems(self):
        """每个检查步骤里的具体检查项
        :rtype: list of DetailCheckItem
        """
        return self._DetailCheckItems

    @DetailCheckItems.setter
    def DetailCheckItems(self, DetailCheckItems):
        self._DetailCheckItems = DetailCheckItems

    @property
    def HasSkipped(self):
        """是否已跳过
        :rtype: bool
        """
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
        :type StartAt: str
        :param _EndAt: 任务结束时间
        :type EndAt: str
        :param _Progress: 任务步骤信息
        :type Progress: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        self._StartAt = None
        self._EndAt = None
        self._Progress = None

    @property
    def StartAt(self):
        """任务开始时间
        :rtype: str
        """
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        """任务结束时间
        :rtype: str
        """
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

    @property
    def Progress(self):
        """任务步骤信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
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
        


class Column(AbstractModel):
    """数据同步中的列信息

    """

    def __init__(self):
        r"""
        :param _ColumnName: 列名
        :type ColumnName: str
        :param _NewColumnName: 新列名
        :type NewColumnName: str
        """
        self._ColumnName = None
        self._NewColumnName = None

    @property
    def ColumnName(self):
        """列名
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def NewColumnName(self):
        """新列名
        :rtype: str
        """
        return self._NewColumnName

    @NewColumnName.setter
    def NewColumnName(self, NewColumnName):
        self._NewColumnName = NewColumnName


    def _deserialize(self, params):
        self._ColumnName = params.get("ColumnName")
        self._NewColumnName = params.get("NewColumnName")
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
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        :param _Objects: 一致性校验对比对象
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _Conclusion: 对比结论: same,different
        :type Conclusion: str
        :param _Status: 任务状态: success,failed
        :type Status: str
        :param _TotalTables: 总的表数量
        :type TotalTables: int
        :param _CheckedTables: 已校验的表数量
        :type CheckedTables: int
        :param _DifferentTables: 不一致的表数量
        :type DifferentTables: int
        :param _SkippedTables: 跳过校验的表数量
        :type SkippedTables: int
        :param _NearlyTableCount: 预估表总数
        :type NearlyTableCount: int
        :param _DifferentRows: 不一致的数据行数量
        :type DifferentRows: int
        :param _SrcSampleRows: 源库行数，当对比类型为**行数对比**时此项有意义
        :type SrcSampleRows: int
        :param _DstSampleRows: 目标库行数，当对比类型为**行数对比**时此项有意义
        :type DstSampleRows: int
        :param _StartedAt: 开始时间
        :type StartedAt: str
        :param _FinishedAt: 结束时间
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
        """校验配置参数
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Objects(self):
        """一致性校验对比对象
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Conclusion(self):
        """对比结论: same,different
        :rtype: str
        """
        return self._Conclusion

    @Conclusion.setter
    def Conclusion(self, Conclusion):
        self._Conclusion = Conclusion

    @property
    def Status(self):
        """任务状态: success,failed
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalTables(self):
        """总的表数量
        :rtype: int
        """
        return self._TotalTables

    @TotalTables.setter
    def TotalTables(self, TotalTables):
        self._TotalTables = TotalTables

    @property
    def CheckedTables(self):
        """已校验的表数量
        :rtype: int
        """
        return self._CheckedTables

    @CheckedTables.setter
    def CheckedTables(self, CheckedTables):
        self._CheckedTables = CheckedTables

    @property
    def DifferentTables(self):
        """不一致的表数量
        :rtype: int
        """
        return self._DifferentTables

    @DifferentTables.setter
    def DifferentTables(self, DifferentTables):
        self._DifferentTables = DifferentTables

    @property
    def SkippedTables(self):
        """跳过校验的表数量
        :rtype: int
        """
        return self._SkippedTables

    @SkippedTables.setter
    def SkippedTables(self, SkippedTables):
        self._SkippedTables = SkippedTables

    @property
    def NearlyTableCount(self):
        """预估表总数
        :rtype: int
        """
        return self._NearlyTableCount

    @NearlyTableCount.setter
    def NearlyTableCount(self, NearlyTableCount):
        self._NearlyTableCount = NearlyTableCount

    @property
    def DifferentRows(self):
        """不一致的数据行数量
        :rtype: int
        """
        return self._DifferentRows

    @DifferentRows.setter
    def DifferentRows(self, DifferentRows):
        self._DifferentRows = DifferentRows

    @property
    def SrcSampleRows(self):
        """源库行数，当对比类型为**行数对比**时此项有意义
        :rtype: int
        """
        return self._SrcSampleRows

    @SrcSampleRows.setter
    def SrcSampleRows(self, SrcSampleRows):
        self._SrcSampleRows = SrcSampleRows

    @property
    def DstSampleRows(self):
        """目标库行数，当对比类型为**行数对比**时此项有意义
        :rtype: int
        """
        return self._DstSampleRows

    @DstSampleRows.setter
    def DstSampleRows(self, DstSampleRows):
        self._DstSampleRows = DstSampleRows

    @property
    def StartedAt(self):
        """开始时间
        :rtype: str
        """
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def FinishedAt(self):
        """结束时间
        :rtype: str
        """
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
        


class CompareColumnItem(AbstractModel):
    """列选项

    """

    def __init__(self):
        r"""
        :param _ColumnName: 列名
        :type ColumnName: str
        """
        self._ColumnName = None

    @property
    def ColumnName(self):
        """列名
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName


    def _deserialize(self, params):
        self._ColumnName = params.get("ColumnName")
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
        :type Difference: :class:`tencentcloud.dts.v20211206.models.DifferenceDetail`
        :param _Skipped: 跳过校验的表详情
        :type Skipped: :class:`tencentcloud.dts.v20211206.models.SkippedDetail`
        :param _DifferenceAdvancedObjects: 数据库不一致的详情，mongodb业务用到
        :type DifferenceAdvancedObjects: :class:`tencentcloud.dts.v20211206.models.DifferenceAdvancedObjectsDetail`
        :param _DifferenceData: 数据不一致的详情，mongodb业务用到
        :type DifferenceData: :class:`tencentcloud.dts.v20211206.models.DifferenceDataDetail`
        :param _DifferenceRow: 数据行不一致的详情，mongodb业务用到
        :type DifferenceRow: :class:`tencentcloud.dts.v20211206.models.DifferenceRowDetail`
        """
        self._Difference = None
        self._Skipped = None
        self._DifferenceAdvancedObjects = None
        self._DifferenceData = None
        self._DifferenceRow = None

    @property
    def Difference(self):
        """数据不一致的表详情
        :rtype: :class:`tencentcloud.dts.v20211206.models.DifferenceDetail`
        """
        return self._Difference

    @Difference.setter
    def Difference(self, Difference):
        self._Difference = Difference

    @property
    def Skipped(self):
        """跳过校验的表详情
        :rtype: :class:`tencentcloud.dts.v20211206.models.SkippedDetail`
        """
        return self._Skipped

    @Skipped.setter
    def Skipped(self, Skipped):
        self._Skipped = Skipped

    @property
    def DifferenceAdvancedObjects(self):
        """数据库不一致的详情，mongodb业务用到
        :rtype: :class:`tencentcloud.dts.v20211206.models.DifferenceAdvancedObjectsDetail`
        """
        return self._DifferenceAdvancedObjects

    @DifferenceAdvancedObjects.setter
    def DifferenceAdvancedObjects(self, DifferenceAdvancedObjects):
        self._DifferenceAdvancedObjects = DifferenceAdvancedObjects

    @property
    def DifferenceData(self):
        """数据不一致的详情，mongodb业务用到
        :rtype: :class:`tencentcloud.dts.v20211206.models.DifferenceDataDetail`
        """
        return self._DifferenceData

    @DifferenceData.setter
    def DifferenceData(self, DifferenceData):
        self._DifferenceData = DifferenceData

    @property
    def DifferenceRow(self):
        """数据行不一致的详情，mongodb业务用到
        :rtype: :class:`tencentcloud.dts.v20211206.models.DifferenceRowDetail`
        """
        return self._DifferenceRow

    @DifferenceRow.setter
    def DifferenceRow(self, DifferenceRow):
        self._DifferenceRow = DifferenceRow


    def _deserialize(self, params):
        if params.get("Difference") is not None:
            self._Difference = DifferenceDetail()
            self._Difference._deserialize(params.get("Difference"))
        if params.get("Skipped") is not None:
            self._Skipped = SkippedDetail()
            self._Skipped._deserialize(params.get("Skipped"))
        if params.get("DifferenceAdvancedObjects") is not None:
            self._DifferenceAdvancedObjects = DifferenceAdvancedObjectsDetail()
            self._DifferenceAdvancedObjects._deserialize(params.get("DifferenceAdvancedObjects"))
        if params.get("DifferenceData") is not None:
            self._DifferenceData = DifferenceDataDetail()
            self._DifferenceData._deserialize(params.get("DifferenceData"))
        if params.get("DifferenceRow") is not None:
            self._DifferenceRow = DifferenceRowDetail()
            self._DifferenceRow._deserialize(params.get("DifferenceRow"))
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
        :type ObjectMode: str
        :param _ObjectItems: 对象列表
        :type ObjectItems: list of CompareObjectItem
        :param _AdvancedObjects: 高级对象类型，目前只支持mongodb链路。如index(索引),shardkey(片键),schema(库表)
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedObjects: list of str
        """
        self._ObjectMode = None
        self._ObjectItems = None
        self._AdvancedObjects = None

    @property
    def ObjectMode(self):
        """对象模式 整实例-all,部分对象-partial
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def ObjectItems(self):
        """对象列表
        :rtype: list of CompareObjectItem
        """
        return self._ObjectItems

    @ObjectItems.setter
    def ObjectItems(self, ObjectItems):
        self._ObjectItems = ObjectItems

    @property
    def AdvancedObjects(self):
        """高级对象类型，目前只支持mongodb链路。如index(索引),shardkey(片键),schema(库表)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
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
        :type DbName: str
        :param _DbMode: 数据库选择模式: all 为当前对象下的所有对象,partial 为部分对象
        :type DbMode: str
        :param _SchemaName: schema名称
        :type SchemaName: str
        :param _TableMode: 表选择模式: all 为当前对象下的所有表对象,partial 为部分表对象
        :type TableMode: str
        :param _Tables: 用于一致性校验的表配置，当 TableMode 为 partial 时，需要填写
        :type Tables: list of CompareTableItem
        :param _ViewMode: 视图选择模式: all 为当前对象下的所有视图对象,partial 为部分视图对象(一致性校验不校验视图，当前参数未启作用)
        :type ViewMode: str
        :param _Views: 用于一致性校验的视图配置，当 ViewMode 为 partial 时， 需要填写(一致性校验不校验视图，当前参数未启作用)
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
        """数据库名
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def DbMode(self):
        """数据库选择模式: all 为当前对象下的所有对象,partial 为部分对象
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def SchemaName(self):
        """schema名称
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableMode(self):
        """表选择模式: all 为当前对象下的所有表对象,partial 为部分表对象
        :rtype: str
        """
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        """用于一致性校验的表配置，当 TableMode 为 partial 时，需要填写
        :rtype: list of CompareTableItem
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        """视图选择模式: all 为当前对象下的所有视图对象,partial 为部分视图对象(一致性校验不校验视图，当前参数未启作用)
        :rtype: str
        """
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        """用于一致性校验的视图配置，当 ViewMode 为 partial 时， 需要填写(一致性校验不校验视图，当前参数未启作用)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CompareViewItem
        """
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
        :param _Method: 对比方式：dataCheck(完整数据对比)、sampleDataCheck(抽样数据对比)、rowsCount(行数对比), 默认为dataCheck
        :type Method: str
        :param _SampleRate: 抽样比例;范围0,100。默认为100
        :type SampleRate: int
        :param _ThreadCount: 线程数，取值1-8，默认为1
        :type ThreadCount: int
        """
        self._Method = None
        self._SampleRate = None
        self._ThreadCount = None

    @property
    def Method(self):
        """对比方式：dataCheck(完整数据对比)、sampleDataCheck(抽样数据对比)、rowsCount(行数对比), 默认为dataCheck
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def SampleRate(self):
        """抽样比例;范围0,100。默认为100
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ThreadCount(self):
        """线程数，取值1-8，默认为1
        :rtype: int
        """
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
        :type TableName: str
        :param _ColumnMode: column 模式，all 为全部，partial 表示部分(该参数仅对数据同步任务有效)
        :type ColumnMode: str
        :param _Columns: 当 ColumnMode 为 partial 时必填(该参数仅对数据同步任务有效)
        :type Columns: list of CompareColumnItem
        """
        self._TableName = None
        self._ColumnMode = None
        self._Columns = None

    @property
    def TableName(self):
        """表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def ColumnMode(self):
        """column 模式，all 为全部，partial 表示部分(该参数仅对数据同步任务有效)
        :rtype: str
        """
        return self._ColumnMode

    @ColumnMode.setter
    def ColumnMode(self, ColumnMode):
        self._ColumnMode = ColumnMode

    @property
    def Columns(self):
        """当 ColumnMode 为 partial 时必填(该参数仅对数据同步任务有效)
        :rtype: list of CompareColumnItem
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._ColumnMode = params.get("ColumnMode")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = CompareColumnItem()
                obj._deserialize(item)
                self._Columns.append(obj)
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
        :type CompareTaskId: str
        :param _Status: 一致性校验结果，包括：unstart(未启动)、running(校验中)、canceled(已终止)、failed(校验任务失败)、inconsistent(不一致)、consistent(一致)、notexist(不存在校验任务)
        :type Status: str
        """
        self._CompareTaskId = None
        self._Status = None

    @property
    def CompareTaskId(self):
        """一致性校验任务Id
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def Status(self):
        """一致性校验结果，包括：unstart(未启动)、running(校验中)、canceled(已终止)、failed(校验任务失败)、inconsistent(不一致)、consistent(一致)、notexist(不存在校验任务)
        :rtype: str
        """
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
        :type JobId: str
        :param _CompareTaskId: 对比任务 Id
        :type CompareTaskId: str
        :param _TaskName: 对比任务名称
        :type TaskName: str
        :param _Status: 对比任务状态, 可能的值：created - 创建完成；readyRun - 等待运行；running - 运行中；success - 成功；stopping - 结束中；failed - 失败；canceled - 已终止
        :type Status: str
        :param _Config: 对比任务配置
        :type Config: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _CheckProcess: 对比任务校验详情
        :type CheckProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param _CompareProcess: 对比任务运行详情
        :type CompareProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param _Conclusion: 对比结果, 可能的值：same - 一致；different - 不一致；skipAll - 跳过
        :type Conclusion: str
        :param _CreatedAt: 任务创建时间
        :type CreatedAt: str
        :param _StartedAt: 任务启动时间
        :type StartedAt: str
        :param _FinishedAt: 对比结束时间
        :type FinishedAt: str
        :param _Method: 对比类型，dataCheck(完整数据对比)、sampleDataCheck(抽样数据对比)、rowsCount(行数对比)
        :type Method: str
        :param _Options: 对比配置信息
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        :param _Message: 一致性校验提示信息
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
        """任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """对比任务 Id
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        """对比任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Status(self):
        """对比任务状态, 可能的值：created - 创建完成；readyRun - 等待运行；running - 运行中；success - 成功；stopping - 结束中；failed - 失败；canceled - 已终止
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Config(self):
        """对比任务配置
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CheckProcess(self):
        """对比任务校验详情
        :rtype: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        return self._CheckProcess

    @CheckProcess.setter
    def CheckProcess(self, CheckProcess):
        self._CheckProcess = CheckProcess

    @property
    def CompareProcess(self):
        """对比任务运行详情
        :rtype: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        return self._CompareProcess

    @CompareProcess.setter
    def CompareProcess(self, CompareProcess):
        self._CompareProcess = CompareProcess

    @property
    def Conclusion(self):
        """对比结果, 可能的值：same - 一致；different - 不一致；skipAll - 跳过
        :rtype: str
        """
        return self._Conclusion

    @Conclusion.setter
    def Conclusion(self, Conclusion):
        self._Conclusion = Conclusion

    @property
    def CreatedAt(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def StartedAt(self):
        """任务启动时间
        :rtype: str
        """
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def FinishedAt(self):
        """对比结束时间
        :rtype: str
        """
        return self._FinishedAt

    @FinishedAt.setter
    def FinishedAt(self, FinishedAt):
        self._FinishedAt = FinishedAt

    @property
    def Method(self):
        """对比类型，dataCheck(完整数据对比)、sampleDataCheck(抽样数据对比)、rowsCount(行数对比)
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Options(self):
        """对比配置信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Message(self):
        """一致性校验提示信息
        :rtype: str
        """
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
        :type ViewName: str
        """
        self._ViewName = None

    @property
    def ViewName(self):
        """视图名
        :rtype: str
        """
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
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompleteMode(self):
        """完成任务的方式,仅支持旧版MySQL迁移任务。waitForSync-等待主从差距为0才停止,immediately-立即完成，不会等待主从差距一致。默认为waitForSync
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ConfigureSubscribeJobRequest(AbstractModel):
    """ConfigureSubscribeJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        :param _SubscribeMode: 数据订阅的类型，当 DatabaseType 不为 mongodb 时，枚举值为：all-全实例更新；dml-数据更新；ddl-结构更新；dmlAndDdl-数据更新+结构更新。当 DatabaseType 为 mongodb 时，枚举值为 all-全实例更新；database-订阅单库；collection-订阅单集合
        :type SubscribeMode: str
        :param _AccessType: 源数据库接入类型，如：extranet(公网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、cdb(云数据库)、cvm(云服务器自建)、intranet(自研上云)、vpc(私有网络vpc)。注意具体可选值依赖当前链路支持能力
        :type AccessType: str
        :param _Endpoints: 数据库节点信息
        :type Endpoints: list of EndpointItem
        :param _KafkaConfig: Kafka配置
        :type KafkaConfig: :class:`tencentcloud.dts.v20211206.models.SubscribeKafkaConfig`
        :param _SubscribeObjects: 订阅的数据库表信息，当 SubscribeMode 不为 all和ddl 时，SubscribeObjects 为必选参数
        :type SubscribeObjects: list of SubscribeObject
        :param _Protocol: 订阅数据格式，如：protobuf、json、avro。注意具体可选值依赖当前链路支持能力，数据格式详情参考官网的消费demo文档
        :type Protocol: str
        :param _PipelineInfo: mongo选填参数：输出聚合设置。
        :type PipelineInfo: list of PipelineInfo
        :param _ExtraAttr: 为业务添加的额外信息。参数名作key，参数值作value。
mysql选填参数：ProcessXA-是否处理XA事务，填true处理，不填或填其他值不处理。
mongo选填参数：SubscribeType-订阅类型，目前只支持changeStream，不填也是默认changeStream。
其他业务暂没有可选参数。
        :type ExtraAttr: list of KeyValuePairOption
        """
        self._SubscribeId = None
        self._SubscribeMode = None
        self._AccessType = None
        self._Endpoints = None
        self._KafkaConfig = None
        self._SubscribeObjects = None
        self._Protocol = None
        self._PipelineInfo = None
        self._ExtraAttr = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeMode(self):
        """数据订阅的类型，当 DatabaseType 不为 mongodb 时，枚举值为：all-全实例更新；dml-数据更新；ddl-结构更新；dmlAndDdl-数据更新+结构更新。当 DatabaseType 为 mongodb 时，枚举值为 all-全实例更新；database-订阅单库；collection-订阅单集合
        :rtype: str
        """
        return self._SubscribeMode

    @SubscribeMode.setter
    def SubscribeMode(self, SubscribeMode):
        self._SubscribeMode = SubscribeMode

    @property
    def AccessType(self):
        """源数据库接入类型，如：extranet(公网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、cdb(云数据库)、cvm(云服务器自建)、intranet(自研上云)、vpc(私有网络vpc)。注意具体可选值依赖当前链路支持能力
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Endpoints(self):
        """数据库节点信息
        :rtype: list of EndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def KafkaConfig(self):
        """Kafka配置
        :rtype: :class:`tencentcloud.dts.v20211206.models.SubscribeKafkaConfig`
        """
        return self._KafkaConfig

    @KafkaConfig.setter
    def KafkaConfig(self, KafkaConfig):
        self._KafkaConfig = KafkaConfig

    @property
    def SubscribeObjects(self):
        """订阅的数据库表信息，当 SubscribeMode 不为 all和ddl 时，SubscribeObjects 为必选参数
        :rtype: list of SubscribeObject
        """
        return self._SubscribeObjects

    @SubscribeObjects.setter
    def SubscribeObjects(self, SubscribeObjects):
        self._SubscribeObjects = SubscribeObjects

    @property
    def Protocol(self):
        """订阅数据格式，如：protobuf、json、avro。注意具体可选值依赖当前链路支持能力，数据格式详情参考官网的消费demo文档
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PipelineInfo(self):
        """mongo选填参数：输出聚合设置。
        :rtype: list of PipelineInfo
        """
        return self._PipelineInfo

    @PipelineInfo.setter
    def PipelineInfo(self, PipelineInfo):
        self._PipelineInfo = PipelineInfo

    @property
    def ExtraAttr(self):
        """为业务添加的额外信息。参数名作key，参数值作value。
mysql选填参数：ProcessXA-是否处理XA事务，填true处理，不填或填其他值不处理。
mongo选填参数：SubscribeType-订阅类型，目前只支持changeStream，不填也是默认changeStream。
其他业务暂没有可选参数。
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeMode = params.get("SubscribeMode")
        self._AccessType = params.get("AccessType")
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = EndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        if params.get("KafkaConfig") is not None:
            self._KafkaConfig = SubscribeKafkaConfig()
            self._KafkaConfig._deserialize(params.get("KafkaConfig"))
        if params.get("SubscribeObjects") is not None:
            self._SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self._SubscribeObjects.append(obj)
        self._Protocol = params.get("Protocol")
        if params.get("PipelineInfo") is not None:
            self._PipelineInfo = []
            for item in params.get("PipelineInfo"):
                obj = PipelineInfo()
                obj._deserialize(item)
                self._PipelineInfo.append(obj)
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
        


class ConfigureSubscribeJobResponse(AbstractModel):
    """ConfigureSubscribeJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _SrcConnectType: 源端tdsql连接方式：proxy-通过tdsql proxy主机访问各个set节点，注意只有在自研上云的网络环境下才能通过这种方式连接，SrcInfos中只需要提供proxy主机信息。set-直连set节点，如选择直连set方式，需要正确填写proxy主机信息及所有set节点信息。源端是tdsqlmysql类型必填。
        :type SrcConnectType: str
        :param _SrcInfo: 源端信息，单机版类型数据库配置使用，且SrcNodeType传single。例如mysql、percona、mariadb等。
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _SrcInfos: 源端信息，分布式类型数据库配置使用，且SrcNodeType传cluster。例如分布式数据库tdsqlmysql等。
        :type SrcInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _SrcNodeType: 枚举值：cluster、single。源库为单节点数据库使用single，多节点使用cluster
        :type SrcNodeType: str
        :param _DstInfo: 目标端信息，单机版类型数据库配置使用，且SrcNodeType传single。例如mysql、percona、mariadb等。
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _DstInfos: 目标端信息，分布式类型数据库配置使用，且SrcNodeType传cluster。例如分布式数据库tdsqlmysql等。
        :type DstInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _DstNodeType: 枚举值：cluster、single。目标库为单节点数据库使用single，多节点使用cluster
        :type DstNodeType: str
        :param _Options: 同步任务选项；该字段下的RateLimitOption暂时无法生效、如果需要修改限速、可通过ModifySyncRateLimit接口完成限速
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
        self._SrcConnectType = None
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
        """同步实例id（即标识一个同步作业），形如sync-werwfs23
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def SrcAccessType(self):
        """源端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云),注意具体可选值依赖当前链路
        :rtype: str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def DstAccessType(self):
        """目标端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)、ckafka(CKafka实例),注意具体可选值依赖当前链路
        :rtype: str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def Objects(self):
        """同步库表对象信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.Objects`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def JobName(self):
        """同步任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobMode(self):
        """枚举值是 liteMode 和 fullMode ，分别对应精简模式或正常模式
        :rtype: str
        """
        return self._JobMode

    @JobMode.setter
    def JobMode(self, JobMode):
        self._JobMode = JobMode

    @property
    def RunMode(self):
        """运行模式，取值如：Immediate(表示立即运行，默认为此项值)、Timed(表示定时运行)
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        """期待启动时间，当RunMode取值为Timed时，此值必填，形如："2006-01-02 15:04:05"
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def SrcConnectType(self):
        """源端tdsql连接方式：proxy-通过tdsql proxy主机访问各个set节点，注意只有在自研上云的网络环境下才能通过这种方式连接，SrcInfos中只需要提供proxy主机信息。set-直连set节点，如选择直连set方式，需要正确填写proxy主机信息及所有set节点信息。源端是tdsqlmysql类型必填。
        :rtype: str
        """
        return self._SrcConnectType

    @SrcConnectType.setter
    def SrcConnectType(self, SrcConnectType):
        self._SrcConnectType = SrcConnectType

    @property
    def SrcInfo(self):
        """源端信息，单机版类型数据库配置使用，且SrcNodeType传single。例如mysql、percona、mariadb等。
        :rtype: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def SrcInfos(self):
        """源端信息，分布式类型数据库配置使用，且SrcNodeType传cluster。例如分布式数据库tdsqlmysql等。
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        """
        return self._SrcInfos

    @SrcInfos.setter
    def SrcInfos(self, SrcInfos):
        self._SrcInfos = SrcInfos

    @property
    def SrcNodeType(self):
        """枚举值：cluster、single。源库为单节点数据库使用single，多节点使用cluster
        :rtype: str
        """
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def DstInfo(self):
        """目标端信息，单机版类型数据库配置使用，且SrcNodeType传single。例如mysql、percona、mariadb等。
        :rtype: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DstInfos(self):
        """目标端信息，分布式类型数据库配置使用，且SrcNodeType传cluster。例如分布式数据库tdsqlmysql等。
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        """
        return self._DstInfos

    @DstInfos.setter
    def DstInfos(self, DstInfos):
        self._DstInfos = DstInfos

    @property
    def DstNodeType(self):
        """枚举值：cluster、single。目标库为单节点数据库使用single，多节点使用cluster
        :rtype: str
        """
        return self._DstNodeType

    @DstNodeType.setter
    def DstNodeType(self, DstNodeType):
        self._DstNodeType = DstNodeType

    @property
    def Options(self):
        """同步任务选项；该字段下的RateLimitOption暂时无法生效、如果需要修改限速、可通过ModifySyncRateLimit接口完成限速
        :rtype: :class:`tencentcloud.dts.v20211206.models.Options`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def AutoRetryTimeRangeMinutes(self):
        """自动重试的时间段、可设置5至720分钟、0表示不重试
        :rtype: int
        """
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
        self._SrcConnectType = params.get("SrcConnectType")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type ConditionColumn: str
        :param _ConditionOperator: 条件覆盖操作
        :type ConditionOperator: str
        :param _ConditionOrderInSrcAndDst: 条件覆盖优先级处理
        :type ConditionOrderInSrcAndDst: str
        """
        self._ConditionColumn = None
        self._ConditionOperator = None
        self._ConditionOrderInSrcAndDst = None

    @property
    def ConditionColumn(self):
        """条件覆盖的列
        :rtype: str
        """
        return self._ConditionColumn

    @ConditionColumn.setter
    def ConditionColumn(self, ConditionColumn):
        self._ConditionColumn = ConditionColumn

    @property
    def ConditionOperator(self):
        """条件覆盖操作
        :rtype: str
        """
        return self._ConditionOperator

    @ConditionOperator.setter
    def ConditionOperator(self, ConditionOperator):
        self._ConditionOperator = ConditionOperator

    @property
    def ConditionOrderInSrcAndDst(self):
        """条件覆盖优先级处理
        :rtype: str
        """
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
        :type Mode: str
        """
        self._Mode = None

    @property
    def Mode(self):
        """一致性检测类型: full(全量检测迁移对象)、noCheck(不检测)、notConfigured(未配置)
        :rtype: str
        """
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
        """数据迁移任务ID
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _Objects: 数据对比对象，当ObjectMode为custom时，此项需要填写。
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
        """任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        """数据对比任务名称，若为空则默认给CompareTaskId相同值
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ObjectMode(self):
        """数据对比对象模式，sameAsMigrate(全部迁移对象， 默认为此项配置)，custom(自定义模式)
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Objects(self):
        """数据对比对象，当ObjectMode为custom时，此项需要填写。
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Options(self):
        """一致性校验选项
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
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
        :type CompareTaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompareTaskId = None
        self._RequestId = None

    @property
    def CompareTaskId(self):
        """数据对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompareTaskId = params.get("CompareTaskId")
        self._RequestId = params.get("RequestId")


class CreateConsumerGroupRequest(AbstractModel):
    """CreateConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例id
        :type SubscribeId: str
        :param _ConsumerGroupName: 消费组名称，以数字、字母(大小写)或者_ - .开头，以数字、字母(大小写)结尾。实际生成的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}
        :type ConsumerGroupName: str
        :param _AccountName: 账号名称。以数字、字母(大小写)或者_ - .开头，以数字、字母(大小写)结尾。实际生成的账户全称形如：account-#{SubscribeId}-#{AccountName}
        :type AccountName: str
        :param _Password: 消费组密码，长度必须大于3
        :type Password: str
        :param _Description: 消费组备注
        :type Description: str
        """
        self._SubscribeId = None
        self._ConsumerGroupName = None
        self._AccountName = None
        self._Password = None
        self._Description = None

    @property
    def SubscribeId(self):
        """订阅实例id
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def ConsumerGroupName(self):
        """消费组名称，以数字、字母(大小写)或者_ - .开头，以数字、字母(大小写)结尾。实际生成的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def AccountName(self):
        """账号名称。以数字、字母(大小写)或者_ - .开头，以数字、字母(大小写)结尾。实际生成的账户全称形如：account-#{SubscribeId}-#{AccountName}
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Password(self):
        """消费组密码，长度必须大于3
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        """消费组备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._AccountName = params.get("AccountName")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerGroupResponse(AbstractModel):
    """CreateConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
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
        """数据迁移任务ID
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """源实例数据库类型，如mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb,cynosdbmysql
        :rtype: str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def DstDatabaseType(self):
        """目标实例数据库类型，如mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb,cynosdbmysql
        :rtype: str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def SrcRegion(self):
        """源实例地域，如：ap-guangzhou
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def DstRegion(self):
        """目标实例地域，如：ap-guangzhou。注意，目标地域必须和API请求地域保持一致。
        :rtype: str
        """
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def InstanceClass(self):
        """实例规格，包括：small、medium、large、xlarge、2xlarge
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def Count(self):
        """购买数量，范围为[1,15]，默认为1
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def JobName(self):
        """迁移服务名称，最大长度128
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Tags(self):
        """标签信息
        :rtype: list of TagItem
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobIds = None
        self._RequestId = None

    @property
    def JobIds(self):
        """下单成功随机生成的迁移任务id列表，形如：dts-c1f6rs21
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSubscribeCheckJobRequest(AbstractModel):
    """CreateSubscribeCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeCheckJobResponse(AbstractModel):
    """CreateSubscribeCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 订阅的数据库类型，目前支持 cynosdbmysql(tdsql-c mysql版),mariadb,mongodb,mysql,percona,tdpg(tdsql postgresql版),tdsqlpercona(tdsql mysql版)
        :type Product: str
        :param _PayType: 付费方式，枚举值：0-包年包月，1-按量计费
        :type PayType: int
        :param _Duration: 购买时长。当 payType 为包年包月时，该项需要填，单位为月，最小值为 1，最大值为 120。不填默认1
        :type Duration: int
        :param _AutoRenew: 是否自动续费。当 payType 为包年包月时，该项需要填。枚举值：0-不自动续费，1-自动续费。默认不自动续费。按量计费设置该标识无效。
        :type AutoRenew: int
        :param _Count: 购买数量,默认为1，最大为10
        :type Count: int
        :param _Tags: 实例资源标签
        :type Tags: list of TagItem
        :param _Name: 任务名，自定义
        :type Name: str
        """
        self._Product = None
        self._PayType = None
        self._Duration = None
        self._AutoRenew = None
        self._Count = None
        self._Tags = None
        self._Name = None

    @property
    def Product(self):
        """订阅的数据库类型，目前支持 cynosdbmysql(tdsql-c mysql版),mariadb,mongodb,mysql,percona,tdpg(tdsql postgresql版),tdsqlpercona(tdsql mysql版)
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def PayType(self):
        """付费方式，枚举值：0-包年包月，1-按量计费
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Duration(self):
        """购买时长。当 payType 为包年包月时，该项需要填，单位为月，最小值为 1，最大值为 120。不填默认1
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def AutoRenew(self):
        """是否自动续费。当 payType 为包年包月时，该项需要填。枚举值：0-不自动续费，1-自动续费。默认不自动续费。按量计费设置该标识无效。
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Count(self):
        """购买数量,默认为1，最大为10
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Tags(self):
        """实例资源标签
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Name(self):
        """任务名，自定义
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._PayType = params.get("PayType")
        self._Duration = params.get("Duration")
        self._AutoRenew = params.get("AutoRenew")
        self._Count = params.get("Count")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeIds: 数据订阅实例的ID数组
        :type SubscribeIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscribeIds = None
        self._RequestId = None

    @property
    def SubscribeIds(self):
        """数据订阅实例的ID数组
        :rtype: list of str
        """
        return self._SubscribeIds

    @SubscribeIds.setter
    def SubscribeIds(self, SubscribeIds):
        self._SubscribeIds = SubscribeIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscribeIds = params.get("SubscribeIds")
        self._RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PayMode: 付款类型, 如：PrePay(表示包年包月)、PostPay(表示按时按量)
        :type PayMode: str
        :param _SrcDatabaseType: 源端数据库类型,如mysql,mariadb,percona,postgresql,cynosdbmysql(表示TDSQL-C MySQL),tdpg(TDSQL PostgreSQL版),tdsqlmysql,tdstore(表示TDSQL TDStore版)等。
        :type SrcDatabaseType: str
        :param _SrcRegion: 源端数据库所在地域,如ap-guangzhou
        :type SrcRegion: str
        :param _DstDatabaseType: 目标端数据库类型,如mysql,mariadb,percona,cynosdbmysql(表示TDSQL-C MySQL),tdpg(TDSQL PostgreSQL版),tdsqlmysql,kafka,tdstore(表示TDSQL TDStore版)等。
        :type DstDatabaseType: str
        :param _DstRegion: 目标端数据库所在地域,如ap-guangzhou
        :type DstRegion: str
        :param _Specification: 同步任务规格，Standard:标准版
        :type Specification: str
        :param _TimeSpan: 购买时长（单位：月），当PayMode值为PrePay则此项配置有意义，默认为1月，取值范围为[1,100]
        :type TimeSpan: int
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
        self._TimeSpan = None
        self._Tags = None
        self._Count = None
        self._AutoRenew = None
        self._InstanceClass = None
        self._JobName = None
        self._ExistedJobId = None

    @property
    def PayMode(self):
        """付款类型, 如：PrePay(表示包年包月)、PostPay(表示按时按量)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SrcDatabaseType(self):
        """源端数据库类型,如mysql,mariadb,percona,postgresql,cynosdbmysql(表示TDSQL-C MySQL),tdpg(TDSQL PostgreSQL版),tdsqlmysql,tdstore(表示TDSQL TDStore版)等。
        :rtype: str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcRegion(self):
        """源端数据库所在地域,如ap-guangzhou
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def DstDatabaseType(self):
        """目标端数据库类型,如mysql,mariadb,percona,cynosdbmysql(表示TDSQL-C MySQL),tdpg(TDSQL PostgreSQL版),tdsqlmysql,kafka,tdstore(表示TDSQL TDStore版)等。
        :rtype: str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstRegion(self):
        """目标端数据库所在地域,如ap-guangzhou
        :rtype: str
        """
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def Specification(self):
        """同步任务规格，Standard:标准版
        :rtype: str
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def TimeSpan(self):
        """购买时长（单位：月），当PayMode值为PrePay则此项配置有意义，默认为1月，取值范围为[1,100]
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def Tags(self):
        """标签信息
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Count(self):
        """一次购买的同步任务数量，取值范围为[1, 10]，默认为1
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AutoRenew(self):
        """自动续费标识，当PayMode值为PrePay则此项配置有意义，取值为：1（表示自动续费）、0（不自动续费，默认为此值）
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def InstanceClass(self):
        """同步链路规格，如micro,small,medium,large，默认为medium
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def JobName(self):
        """同步任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def ExistedJobId(self):
        """创建类似任务的现有任务Id
        :rtype: str
        """
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
        self._TimeSpan = params.get("TimeSpan")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobIds = None
        self._RequestId = None

    @property
    def JobIds(self):
        """同步任务ids
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type Region: str
        :param _AccessType: 实例网络接入类型，如：extranet(外网)、ipv6(公网ipv6)、cvm(云主机自建)、dcg(专线接入)、vpncloud(vpn接入的实例)、cdb(云数据库)、ccn(云联网)、intranet(自研上云)、vpc(私有网络)等，注意具体可选值依赖当前链路
        :type AccessType: str
        :param _DatabaseType: 实例数据库类型，如：mysql,redis,mongodb,postgresql,mariadb,percona 等
        :type DatabaseType: str
        :param _NodeType: 节点类型，simple表示普通节点、cluster表示集群节点；
对于mongo业务，取值为replicaset(mongodb副本集)、standalone(mongodb单节点)、cluster(mongodb集群)；
对于redis实例，simple(单节点)、cluster-cache(直连集群)、cluster-proxy(代理集群)；
        :type NodeType: str
        :param _Info: 实例具体的连接信息，如ip、port、接入方式等
        :type Info: list of DBInfo
        :param _Supplier: 实例服务提供商，如:"aliyun","others"
        :type Supplier: str
        :param _ExtraAttr: 此参数为数组类型，可以传多个键值对结构对象。
MongoDB可定义如下的参数：
'AuthDatabase':'admin',
'AuthFlag': "1",
'AuthMechanism':"SCRAM-SHA-1",
"fetchMethod":"oplog",
"connectMode":"srv",
"EncryptedConnProtocol":"mongo_atlas_ssl"；
其中fetchMethod表示迁移方式，还可支持change_stream；EncryptedConnProtocol值为mongo_atlas_ssl表示使用atlas ssl连接方式。
        :type ExtraAttr: list of KeyValuePairOption
        :param _DatabaseNetEnv: 数据库所属网络环境，AccessType为云联网(ccn)时必填， UserIDC表示用户IDC、TencentVPC表示腾讯云VPC；
        :type DatabaseNetEnv: str
        :param _ConnectType: tdsql连接方式：proxy-通过tdsql proxy主机访问各个set节点，注意只有在自研上云的网络环境下才能通过这种方式连接，Info中只需要提供proxy主机信息。set-直连set节点，如选择直连set方式，Info中需要正确填写proxy主机信息及所有set节点信息。源端是tdsqlmysql类型必填。
        :type ConnectType: str
        """
        self._Region = None
        self._AccessType = None
        self._DatabaseType = None
        self._NodeType = None
        self._Info = None
        self._Supplier = None
        self._ExtraAttr = None
        self._DatabaseNetEnv = None
        self._ConnectType = None

    @property
    def Region(self):
        """实例所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccessType(self):
        """实例网络接入类型，如：extranet(外网)、ipv6(公网ipv6)、cvm(云主机自建)、dcg(专线接入)、vpncloud(vpn接入的实例)、cdb(云数据库)、ccn(云联网)、intranet(自研上云)、vpc(私有网络)等，注意具体可选值依赖当前链路
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def DatabaseType(self):
        """实例数据库类型，如：mysql,redis,mongodb,postgresql,mariadb,percona 等
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def NodeType(self):
        """节点类型，simple表示普通节点、cluster表示集群节点；
对于mongo业务，取值为replicaset(mongodb副本集)、standalone(mongodb单节点)、cluster(mongodb集群)；
对于redis实例，simple(单节点)、cluster-cache(直连集群)、cluster-proxy(代理集群)；
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Info(self):
        """实例具体的连接信息，如ip、port、接入方式等
        :rtype: list of DBInfo
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Supplier(self):
        """实例服务提供商，如:"aliyun","others"
        :rtype: str
        """
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def ExtraAttr(self):
        """此参数为数组类型，可以传多个键值对结构对象。
MongoDB可定义如下的参数：
'AuthDatabase':'admin',
'AuthFlag': "1",
'AuthMechanism':"SCRAM-SHA-1",
"fetchMethod":"oplog",
"connectMode":"srv",
"EncryptedConnProtocol":"mongo_atlas_ssl"；
其中fetchMethod表示迁移方式，还可支持change_stream；EncryptedConnProtocol值为mongo_atlas_ssl表示使用atlas ssl连接方式。
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def DatabaseNetEnv(self):
        """数据库所属网络环境，AccessType为云联网(ccn)时必填， UserIDC表示用户IDC、TencentVPC表示腾讯云VPC；
        :rtype: str
        """
        return self._DatabaseNetEnv

    @DatabaseNetEnv.setter
    def DatabaseNetEnv(self, DatabaseNetEnv):
        self._DatabaseNetEnv = DatabaseNetEnv

    @property
    def ConnectType(self):
        """tdsql连接方式：proxy-通过tdsql proxy主机访问各个set节点，注意只有在自研上云的网络环境下才能通过这种方式连接，Info中只需要提供proxy主机信息。set-直连set节点，如选择直连set方式，Info中需要正确填写proxy主机信息及所有set节点信息。源端是tdsqlmysql类型必填。
        :rtype: str
        """
        return self._ConnectType

    @ConnectType.setter
    def ConnectType(self, ConnectType):
        self._ConnectType = ConnectType


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
        self._ConnectType = params.get("ConnectType")
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
        :param _Role: 表示节点角色，针对分布式数据库，如mongodb中的mongos节点。tdsqlmysql的可选项：proxy表示节点类型为主机，set表示节点类型为节点。proxy类型必须填在数组第一项。tdsqlmysql类型的源/目标配置必填。
        :type Role: str
        :param _DbKernel: 内核版本，针对mariadb的不同内核版本等
        :type DbKernel: str
        :param _Host: 实例的IP地址，对于公网、专线、VPN、云联网、自研上云、VPC等接入方式此项必填
        :type Host: str
        :param _Port: 实例的端口，对于公网、云主机自建、专线、VPN、云联网、自研上云、VPC等接入方式此项必填
        :type Port: int
        :param _User: 实例的用户名
        :type User: str
        :param _Password: 实例的密码
        :type Password: str
        :param _CvmInstanceId: CVM实例短ID，格式如：ins-olgl39y8；与云服务器控制台页面显示的实例ID相同；如果接入类型为云主机自建的方式，此项必填
        :type CvmInstanceId: str
        :param _UniqVpnGwId: VPN网关ID，格式如：vpngw-9ghexg7q；如果接入类型为vpncloud的方式，此项必填
        :type UniqVpnGwId: str
        :param _UniqDcgId: 专线网关ID，格式如：dcg-0rxtqqxb；如果接入类型为专线接入的方式，此项必填
        :type UniqDcgId: str
        :param _InstanceId: 数据库实例ID，格式如：cdb-powiqx8q；如果接入类型为云数据库的方式，此项必填
        :type InstanceId: str
        :param _CcnGwId: 云联网ID，如：ccn-afp6kltc 注意：此字段可能返回 null，表示取不到有效值。
        :type CcnGwId: str
        :param _VpcId: 私有网络ID，格式如：vpc-92jblxto；如果接入类型为vpc、vpncloud、ccn、dcg的方式，此项必填
        :type VpcId: str
        :param _SubnetId: 私有网络下的子网ID，格式如：subnet-3paxmkdz；如果接入类型为vpc、vpncloud、ccn、dcg的方式，此项必填
        :type SubnetId: str
        :param _EngineVersion: 数据库版本，当实例为RDS实例时才有效，格式如：5.6或者5.7，默认为5.6
        :type EngineVersion: str
        :param _Account: 实例所属账号
        :type Account: str
        :param _AccountRole: 跨账号迁移时的角色,只允许[a-zA-Z0-9\-\_]+
        :type AccountRole: str
        :param _AccountMode: 资源所属账号 为空或self(表示本账号内资源)、other(表示其他账户资源)
        :type AccountMode: str
        :param _TmpSecretId: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :type TmpSecretKey: str
        :param _TmpToken: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :type TmpToken: str
        :param _EncryptConn: 是否走加密传输、UnEncrypted表示不走加密传输，Encrypted表示走加密传输，默认UnEncrypted
        :type EncryptConn: str
        :param _SetId: tdsql的分片id。如节点类型为set必填。
        :type SetId: str
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
        self._EncryptConn = None
        self._SetId = None

    @property
    def Role(self):
        """表示节点角色，针对分布式数据库，如mongodb中的mongos节点。tdsqlmysql的可选项：proxy表示节点类型为主机，set表示节点类型为节点。proxy类型必须填在数组第一项。tdsqlmysql类型的源/目标配置必填。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def DbKernel(self):
        """内核版本，针对mariadb的不同内核版本等
        :rtype: str
        """
        return self._DbKernel

    @DbKernel.setter
    def DbKernel(self, DbKernel):
        self._DbKernel = DbKernel

    @property
    def Host(self):
        """实例的IP地址，对于公网、专线、VPN、云联网、自研上云、VPC等接入方式此项必填
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        """实例的端口，对于公网、云主机自建、专线、VPN、云联网、自研上云、VPC等接入方式此项必填
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        """实例的用户名
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """实例的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CvmInstanceId(self):
        """CVM实例短ID，格式如：ins-olgl39y8；与云服务器控制台页面显示的实例ID相同；如果接入类型为云主机自建的方式，此项必填
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqVpnGwId(self):
        """VPN网关ID，格式如：vpngw-9ghexg7q；如果接入类型为vpncloud的方式，此项必填
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def UniqDcgId(self):
        """专线网关ID，格式如：dcg-0rxtqqxb；如果接入类型为专线接入的方式，此项必填
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def InstanceId(self):
        """数据库实例ID，格式如：cdb-powiqx8q；如果接入类型为云数据库的方式，此项必填
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CcnGwId(self):
        """云联网ID，如：ccn-afp6kltc 注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CcnGwId

    @CcnGwId.setter
    def CcnGwId(self, CcnGwId):
        self._CcnGwId = CcnGwId

    @property
    def VpcId(self):
        """私有网络ID，格式如：vpc-92jblxto；如果接入类型为vpc、vpncloud、ccn、dcg的方式，此项必填
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络下的子网ID，格式如：subnet-3paxmkdz；如果接入类型为vpc、vpncloud、ccn、dcg的方式，此项必填
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EngineVersion(self):
        """数据库版本，当实例为RDS实例时才有效，格式如：5.6或者5.7，默认为5.6
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Account(self):
        """实例所属账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def AccountRole(self):
        """跨账号迁移时的角色,只允许[a-zA-Z0-9\-\_]+
        :rtype: str
        """
        return self._AccountRole

    @AccountRole.setter
    def AccountRole(self, AccountRole):
        self._AccountRole = AccountRole

    @property
    def AccountMode(self):
        """资源所属账号 为空或self(表示本账号内资源)、other(表示其他账户资源)
        :rtype: str
        """
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def TmpSecretId(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :rtype: str
        """
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken

    @property
    def EncryptConn(self):
        """是否走加密传输、UnEncrypted表示不走加密传输，Encrypted表示走加密传输，默认UnEncrypted
        :rtype: str
        """
        return self._EncryptConn

    @EncryptConn.setter
    def EncryptConn(self, EncryptConn):
        self._EncryptConn = EncryptConn

    @property
    def SetId(self):
        """tdsql的分片id。如节点类型为set必填。
        :rtype: str
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId


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
        self._EncryptConn = params.get("EncryptConn")
        self._SetId = params.get("SetId")
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
        :type DbName: str
        :param _NewDbName: 迁移或同步后的库名，默认与源库相同
        :type NewDbName: str
        :param _SchemaName: 迁移或同步的 schema
        :type SchemaName: str
        :param _NewSchemaName: 迁移或同步后的 schema name
        :type NewSchemaName: str
        :param _DBMode: DB选择模式: all(为当前对象下的所有对象)，partial(部分对象)，当ObjectMode为partial时，此项必填
        :type DBMode: str
        :param _SchemaMode: schema选择模式: all(为当前对象下的所有对象)，partial(部分对象)
        :type SchemaMode: str
        :param _TableMode: 表选择模式: all(为当前对象下的所有对象)，partial(部分对象)，当DBMode为partial时此项必填
        :type TableMode: str
        :param _Tables: 表图对象集合，当 TableMode 为 partial 时，此项需要填写
        :type Tables: list of TableItem
        :param _ViewMode: 视图选择模式: all 为当前对象下的所有视图对象,partial 为部分视图对象
        :type ViewMode: str
        :param _Views: 视图对象集合，当 ViewMode 为 partial 时， 此项需要填写
        :type Views: list of ViewItem
        :param _RoleMode: postgresql独有参数，角色选择模式: all 为当前对象下的所有角色对象,partial 为部分角色对象
        :type RoleMode: str
        :param _Roles: postgresql独有参数，当 RoleMode 为 partial 时， 此项需要填写
        :type Roles: list of RoleItem
        :param _FunctionMode: 选择要同步的模式，partial为部分，all为整选
        :type FunctionMode: str
        :param _TriggerMode: 选择要同步的模式，partial为部分，all为整选
        :type TriggerMode: str
        :param _EventMode: 选择要同步的模式，partial为部分，all为整选
        :type EventMode: str
        :param _ProcedureMode: 选择要同步的模式，partial为部分，all为整选
        :type ProcedureMode: str
        :param _Functions: FunctionMode取值为partial时需要填写
        :type Functions: list of str
        :param _Procedures: ProcedureMode取值为partial时需要填写
        :type Procedures: list of str
        :param _Events: EventMode取值为partial时需要填写
        :type Events: list of str
        :param _Triggers: TriggerMode取值为partial时需要填写
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
        """需要迁移或同步的库名，当ObjectMode为partial时，此项必填
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewDbName(self):
        """迁移或同步后的库名，默认与源库相同
        :rtype: str
        """
        return self._NewDbName

    @NewDbName.setter
    def NewDbName(self, NewDbName):
        self._NewDbName = NewDbName

    @property
    def SchemaName(self):
        """迁移或同步的 schema
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def NewSchemaName(self):
        """迁移或同步后的 schema name
        :rtype: str
        """
        return self._NewSchemaName

    @NewSchemaName.setter
    def NewSchemaName(self, NewSchemaName):
        self._NewSchemaName = NewSchemaName

    @property
    def DBMode(self):
        """DB选择模式: all(为当前对象下的所有对象)，partial(部分对象)，当ObjectMode为partial时，此项必填
        :rtype: str
        """
        return self._DBMode

    @DBMode.setter
    def DBMode(self, DBMode):
        self._DBMode = DBMode

    @property
    def SchemaMode(self):
        """schema选择模式: all(为当前对象下的所有对象)，partial(部分对象)
        :rtype: str
        """
        return self._SchemaMode

    @SchemaMode.setter
    def SchemaMode(self, SchemaMode):
        self._SchemaMode = SchemaMode

    @property
    def TableMode(self):
        """表选择模式: all(为当前对象下的所有对象)，partial(部分对象)，当DBMode为partial时此项必填
        :rtype: str
        """
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        """表图对象集合，当 TableMode 为 partial 时，此项需要填写
        :rtype: list of TableItem
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        """视图选择模式: all 为当前对象下的所有视图对象,partial 为部分视图对象
        :rtype: str
        """
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        """视图对象集合，当 ViewMode 为 partial 时， 此项需要填写
        :rtype: list of ViewItem
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def RoleMode(self):
        """postgresql独有参数，角色选择模式: all 为当前对象下的所有角色对象,partial 为部分角色对象
        :rtype: str
        """
        return self._RoleMode

    @RoleMode.setter
    def RoleMode(self, RoleMode):
        self._RoleMode = RoleMode

    @property
    def Roles(self):
        """postgresql独有参数，当 RoleMode 为 partial 时， 此项需要填写
        :rtype: list of RoleItem
        """
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def FunctionMode(self):
        """选择要同步的模式，partial为部分，all为整选
        :rtype: str
        """
        return self._FunctionMode

    @FunctionMode.setter
    def FunctionMode(self, FunctionMode):
        self._FunctionMode = FunctionMode

    @property
    def TriggerMode(self):
        """选择要同步的模式，partial为部分，all为整选
        :rtype: str
        """
        return self._TriggerMode

    @TriggerMode.setter
    def TriggerMode(self, TriggerMode):
        self._TriggerMode = TriggerMode

    @property
    def EventMode(self):
        """选择要同步的模式，partial为部分，all为整选
        :rtype: str
        """
        return self._EventMode

    @EventMode.setter
    def EventMode(self, EventMode):
        self._EventMode = EventMode

    @property
    def ProcedureMode(self):
        """选择要同步的模式，partial为部分，all为整选
        :rtype: str
        """
        return self._ProcedureMode

    @ProcedureMode.setter
    def ProcedureMode(self, ProcedureMode):
        self._ProcedureMode = ProcedureMode

    @property
    def Functions(self):
        """FunctionMode取值为partial时需要填写
        :rtype: list of str
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def Procedures(self):
        """ProcedureMode取值为partial时需要填写
        :rtype: list of str
        """
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def Events(self):
        """EventMode取值为partial时需要填写
        :rtype: list of str
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def Triggers(self):
        """TriggerMode取值为partial时需要填写
        :rtype: list of str
        """
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
        :type DbName: str
        :param _NewDbName: 迁移或同步后的库名，默认与源库相同
        :type NewDbName: str
        :param _DbMode: DB选择模式: All(为当前对象下的所有对象)，Partial(部分对象)，当Mode为Partial时，此项必填。注意，高级对象的同步不依赖此值，如果整库同步此处应该为All。
        :type DbMode: str
        :param _SchemaName: 迁移或同步的 schema
        :type SchemaName: str
        :param _NewSchemaName: 迁移或同步后的 schema name
        :type NewSchemaName: str
        :param _TableMode: 表选择模式: All(为当前对象下的所有对象)，Partial(部分对象)，当DBMode为Partial时此项必填，如果整库同步此处应该为All。
        :type TableMode: str
        :param _Tables: 表图对象集合，当 TableMode 为 Partial 时，此项需要填写
        :type Tables: list of Table
        :param _ViewMode: 视图选择模式: All 为当前对象下的所有视图对象,Partial 为部分视图对象，如果整库同步此处应该为All。
        :type ViewMode: str
        :param _Views: 视图对象集合，当 ViewMode 为 Partial 时， 此项需要填写
        :type Views: list of View
        :param _FunctionMode: 选择要同步的模式，Partial为部分，All为整选，如果整库同步此处应该为All。
        :type FunctionMode: str
        :param _Functions: FunctionMode取值为Partial时需要填写
        :type Functions: list of str
        :param _ProcedureMode: 选择要同步的模式，Partial为部分，All为整选，如果整库同步此处应该为All。
        :type ProcedureMode: str
        :param _Procedures: ProcedureMode取值为Partial时需要填写
        :type Procedures: list of str
        :param _TriggerMode: 触发器迁移模式，All(为当前对象下的所有对象)，Partial(部分对象)，如果整库同步此处应该为All。数据同步暂不支持此高级对象。
        :type TriggerMode: str
        :param _Triggers: 当TriggerMode为partial，指定要迁移的触发器名称
        :type Triggers: list of str
        :param _EventMode: 事件迁移模式，All(为当前对象下的所有对象)，Partial(部分对象)，如果整库同步此处应该为All。数据同步暂不支持此高级对象。
        :type EventMode: str
        :param _Events: 当EventMode为partial，指定要迁移的事件名称
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
        """需要迁移或同步的库名，当ObjectMode为Partial时，此项必填
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewDbName(self):
        """迁移或同步后的库名，默认与源库相同
        :rtype: str
        """
        return self._NewDbName

    @NewDbName.setter
    def NewDbName(self, NewDbName):
        self._NewDbName = NewDbName

    @property
    def DbMode(self):
        """DB选择模式: All(为当前对象下的所有对象)，Partial(部分对象)，当Mode为Partial时，此项必填。注意，高级对象的同步不依赖此值，如果整库同步此处应该为All。
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def SchemaName(self):
        """迁移或同步的 schema
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def NewSchemaName(self):
        """迁移或同步后的 schema name
        :rtype: str
        """
        return self._NewSchemaName

    @NewSchemaName.setter
    def NewSchemaName(self, NewSchemaName):
        self._NewSchemaName = NewSchemaName

    @property
    def TableMode(self):
        """表选择模式: All(为当前对象下的所有对象)，Partial(部分对象)，当DBMode为Partial时此项必填，如果整库同步此处应该为All。
        :rtype: str
        """
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        """表图对象集合，当 TableMode 为 Partial 时，此项需要填写
        :rtype: list of Table
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        """视图选择模式: All 为当前对象下的所有视图对象,Partial 为部分视图对象，如果整库同步此处应该为All。
        :rtype: str
        """
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        """视图对象集合，当 ViewMode 为 Partial 时， 此项需要填写
        :rtype: list of View
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def FunctionMode(self):
        """选择要同步的模式，Partial为部分，All为整选，如果整库同步此处应该为All。
        :rtype: str
        """
        return self._FunctionMode

    @FunctionMode.setter
    def FunctionMode(self, FunctionMode):
        self._FunctionMode = FunctionMode

    @property
    def Functions(self):
        """FunctionMode取值为Partial时需要填写
        :rtype: list of str
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def ProcedureMode(self):
        """选择要同步的模式，Partial为部分，All为整选，如果整库同步此处应该为All。
        :rtype: str
        """
        return self._ProcedureMode

    @ProcedureMode.setter
    def ProcedureMode(self, ProcedureMode):
        self._ProcedureMode = ProcedureMode

    @property
    def Procedures(self):
        """ProcedureMode取值为Partial时需要填写
        :rtype: list of str
        """
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def TriggerMode(self):
        """触发器迁移模式，All(为当前对象下的所有对象)，Partial(部分对象)，如果整库同步此处应该为All。数据同步暂不支持此高级对象。
        :rtype: str
        """
        return self._TriggerMode

    @TriggerMode.setter
    def TriggerMode(self, TriggerMode):
        self._TriggerMode = TriggerMode

    @property
    def Triggers(self):
        """当TriggerMode为partial，指定要迁移的触发器名称
        :rtype: list of str
        """
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers

    @property
    def EventMode(self):
        """事件迁移模式，All(为当前对象下的所有对象)，Partial(部分对象)，如果整库同步此处应该为All。数据同步暂不支持此高级对象。
        :rtype: str
        """
        return self._EventMode

    @EventMode.setter
    def EventMode(self, EventMode):
        self._EventMode = EventMode

    @property
    def Events(self):
        """当EventMode为partial，指定要迁移的事件名称
        :rtype: list of str
        """
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
        :type ObjectMode: str
        :param _Databases: 迁移对象，当 ObjectMode 为 partial 时，不为空
        :type Databases: list of DBItem
        :param _AdvancedObjects: 高级对象类型，如trigger、function、procedure、event。注意：如果要迁移同步高级对象，此配置中应该包含对应的高级对象类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedObjects: list of str
        """
        self._ObjectMode = None
        self._Databases = None
        self._AdvancedObjects = None

    @property
    def ObjectMode(self):
        """迁移对象类型 all(全实例)，partial(部分对象)
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Databases(self):
        """迁移对象，当 ObjectMode 为 partial 时，不为空
        :rtype: list of DBItem
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def AdvancedObjects(self):
        """高级对象类型，如trigger、function、procedure、event。注意：如果要迁移同步高级对象，此配置中应该包含对应的高级对象类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
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
        :type DdlObject: str
        :param _DdlValue: ddl具体值，对于Database可取值[Create,Drop,Alter]<br>对于Table可取值[Create,Drop,Alter,Truncate,Rename]<br/>对于View可取值[Create,Drop]<br/>对于Index可取值[Create,Drop]
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlValue: list of str
        """
        self._DdlObject = None
        self._DdlValue = None

    @property
    def DdlObject(self):
        """ddl类型，如Database,Table,View,Index等
        :rtype: str
        """
        return self._DdlObject

    @DdlObject.setter
    def DdlObject(self, DdlObject):
        self._DdlObject = DdlObject

    @property
    def DdlValue(self):
        """ddl具体值，对于Database可取值[Create,Drop,Alter]<br>对于Table可取值[Create,Drop,Alter,Truncate,Rename]<br/>对于View可取值[Create,Drop]<br/>对于Index可取值[Create,Drop]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
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
        """迁移任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteConsumerGroupRequest(AbstractModel):
    """DeleteConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        :param _ConsumerGroupName: 消费组名称。实际的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}。
请务必保证消费组名称正确。
        :type ConsumerGroupName: str
        :param _AccountName: 账号名称。实际的账户全称形如：account-#{SubscribeId}-#{AccountName}。
请务必保证账户名称正确。
        :type AccountName: str
        """
        self._SubscribeId = None
        self._ConsumerGroupName = None
        self._AccountName = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def ConsumerGroupName(self):
        """消费组名称。实际的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}。
请务必保证消费组名称正确。
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def AccountName(self):
        """账号名称。实际的账户全称形如：account-#{SubscribeId}-#{AccountName}。
请务必保证账户名称正确。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsumerGroupResponse(AbstractModel):
    """DeleteConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步实例id（即标识一个同步作业），形如sync-werwfs23，此值必填
        :rtype: str
        """
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
        :type Status: str
        :param _StepCount: 步骤总数
        :type StepCount: int
        :param _StepCur: 当前所在步骤
        :type StepCur: int
        :param _Progress: 总体进度，范围为[0,100]
        :type Progress: int
        :param _StepInfos: 步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfos: list of StepInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        """校验任务执行状态，如：notStarted(未开始)、running(校验中)、failed(校验任务失败)、success(任务成功)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StepCount(self):
        """步骤总数
        :rtype: int
        """
        return self._StepCount

    @StepCount.setter
    def StepCount(self, StepCount):
        self._StepCount = StepCount

    @property
    def StepCur(self):
        """当前所在步骤
        :rtype: int
        """
        return self._StepCur

    @StepCur.setter
    def StepCur(self, StepCur):
        self._StepCur = StepCur

    @property
    def Progress(self):
        """总体进度，范围为[0,100]
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfos(self):
        """步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StepInfo
        """
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """迁移任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """校验任务 Id
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def DifferenceLimit(self):
        """校验不一致结果的 limit
        :rtype: int
        """
        return self._DifferenceLimit

    @DifferenceLimit.setter
    def DifferenceLimit(self, DifferenceLimit):
        self._DifferenceLimit = DifferenceLimit

    @property
    def DifferenceOffset(self):
        """不一致的 Offset
        :rtype: int
        """
        return self._DifferenceOffset

    @DifferenceOffset.setter
    def DifferenceOffset(self, DifferenceOffset):
        self._DifferenceOffset = DifferenceOffset

    @property
    def DifferenceDB(self):
        """搜索条件，不一致的库名
        :rtype: str
        """
        return self._DifferenceDB

    @DifferenceDB.setter
    def DifferenceDB(self, DifferenceDB):
        self._DifferenceDB = DifferenceDB

    @property
    def DifferenceTable(self):
        """搜索条件，不一致的表名
        :rtype: str
        """
        return self._DifferenceTable

    @DifferenceTable.setter
    def DifferenceTable(self, DifferenceTable):
        self._DifferenceTable = DifferenceTable

    @property
    def SkippedLimit(self):
        """未校验的 Limit
        :rtype: int
        """
        return self._SkippedLimit

    @SkippedLimit.setter
    def SkippedLimit(self, SkippedLimit):
        self._SkippedLimit = SkippedLimit

    @property
    def SkippedOffset(self):
        """未校验的 Offset
        :rtype: int
        """
        return self._SkippedOffset

    @SkippedOffset.setter
    def SkippedOffset(self, SkippedOffset):
        self._SkippedOffset = SkippedOffset

    @property
    def SkippedDB(self):
        """搜索条件，未校验的库名
        :rtype: str
        """
        return self._SkippedDB

    @SkippedDB.setter
    def SkippedDB(self, SkippedDB):
        self._SkippedDB = SkippedDB

    @property
    def SkippedTable(self):
        """搜索条件，未校验的表名
        :rtype: str
        """
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
        :type Abstract: :class:`tencentcloud.dts.v20211206.models.CompareAbstractInfo`
        :param _Detail: 一致性校验详细信息
        :type Detail: :class:`tencentcloud.dts.v20211206.models.CompareDetailInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Abstract = None
        self._Detail = None
        self._RequestId = None

    @property
    def Abstract(self):
        """一致性校验摘要信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareAbstractInfo`
        """
        return self._Abstract

    @Abstract.setter
    def Abstract(self, Abstract):
        self._Abstract = Abstract

    @property
    def Detail(self):
        """一致性校验详细信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareDetailInfo`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """迁移任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Limit(self):
        """分页设置，表示每页显示多少条任务，默认为 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CompareTaskId(self):
        """校验任务 ID
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def Status(self):
        """任务状态过滤，可能的值：created - 创建完成；readyRun - 等待运行；running - 运行中；success - 成功；stopping - 结束中；failed - 失败；canceled - 已终止
        :rtype: list of str
        """
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
        :type TotalCount: int
        :param _Items: 一致性校验列表
        :type Items: list of CompareTaskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """一致性校验列表
        :rtype: list of CompareTaskItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeConsumerGroupsRequest(AbstractModel):
    """DescribeConsumerGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例id
        :type SubscribeId: str
        :param _Offset: 返回记录的起始偏移量。默认0
        :type Offset: int
        :param _Limit: 单次返回的记录数量。默认10
        :type Limit: int
        """
        self._SubscribeId = None
        self._Offset = None
        self._Limit = None

    @property
    def SubscribeId(self):
        """订阅实例id
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def Offset(self):
        """返回记录的起始偏移量。默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """单次返回的记录数量。默认10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupsResponse(AbstractModel):
    """DescribeConsumerGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 指定实例下的消费者组总数
        :type TotalCount: int
        :param _Items: 消费者组列表
        :type Items: list of GroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """指定实例下的消费者组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """消费者组列表
        :rtype: list of GroupInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrateDBInstancesRequest(AbstractModel):
    """DescribeMigrateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseType: 数据库类型，如mysql,redis等
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
        :param _TmpSecretId: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :type TmpSecretKey: str
        :param _TmpToken: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
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
        """数据库类型，如mysql,redis等
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def MigrateRole(self):
        """实例作为迁移的源还是目标,src(表示源)，dst(表示目标)
        :rtype: str
        """
        return self._MigrateRole

    @MigrateRole.setter
    def MigrateRole(self, MigrateRole):
        self._MigrateRole = MigrateRole

    @property
    def InstanceId(self):
        """云数据库实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """云数据库名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Limit(self):
        """返回数量限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AccountMode(self):
        """资源所属账号 为空值或self(表示本账号内资源)、other(表示其他账户资源)
        :rtype: str
        """
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def TmpSecretId(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号迁移文档(https://cloud.tencent.com/document/product/571/54117)第4节中关于角色的定义。
        :rtype: str
        """
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
        :type TotalCount: int
        :param _Instances: 实例列表
        :type Instances: list of MigrateDBItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合筛选条件的数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        """实例列表
        :rtype: list of MigrateDBItem
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """任务id
        :rtype: str
        """
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
        :type Status: str
        :param _BriefMsg: 校验任务结果输出简要信息
        :type BriefMsg: str
        :param _StepInfo: 检查步骤
        :type StepInfo: list of CheckStep
        :param _CheckFlag: 校验结果，如：checkPass(校验通过)、checkNotPass(校验未通过)
        :type CheckFlag: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._BriefMsg = None
        self._StepInfo = None
        self._CheckFlag = None
        self._RequestId = None

    @property
    def Status(self):
        """校验任务执行状态，如：notStarted(未开始)、running(校验中)、failed(校验任务失败)、success(任务成功)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BriefMsg(self):
        """校验任务结果输出简要信息
        :rtype: str
        """
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def StepInfo(self):
        """检查步骤
        :rtype: list of CheckStep
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def CheckFlag(self):
        """校验结果，如：checkPass(校验通过)、checkNotPass(校验未通过)
        :rtype: str
        """
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """数据迁移任务ID
        :rtype: str
        """
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
        :type JobId: str
        :param _JobName: 数据迁移任务名称
        :type JobName: str
        :param _CreateTime: 任务创建(提交)时间，格式为 yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _UpdateTime: 任务更新时间，格式为 yyyy-mm-dd hh:mm:ss
        :type UpdateTime: str
        :param _StartTime: 任务开始执行时间，格式为 yyyy-mm-dd hh:mm:ss
        :type StartTime: str
        :param _EndTime: 任务执行结束时间，格式为 yyyy-mm-dd hh:mm:ss
        :type EndTime: str
        :param _BriefMsg: 迁移任务简要错误信息
        :type BriefMsg: str
        :param _Status: 任务状态，取值为：created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行中)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)、
pausing(暂停中)、
manualPaused(已暂停)
        :type Status: str
        :param _Action: 任务操作信息
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param _StepInfo: 迁移执行过程信息，在校验阶段显示校验过程步骤信息，在迁移阶段会显示迁移步骤信息
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param _SrcInfo: 源实例信息
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _DstInfo: 目标端信息
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _CompareTask: 数据一致性校验结果
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param _Tags: 标签信息
        :type Tags: list of TagItem
        :param _RunMode: 运行模式，取值如：immediate(表示立即运行)、timed(表示定时运行)
        :type RunMode: str
        :param _ExpectRunTime: 期待启动时间，当RunMode取值为timed时，此值必填，形如："2006-01-02 15:04:05"
        :type ExpectRunTime: str
        :param _MigrateOption: 迁移选项，描述任务如何执行迁移等一系列配置信息
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param _CheckStepInfo: 校验任务运行详情
        :type CheckStepInfo: :class:`tencentcloud.dts.v20211206.models.CheckStepInfo`
        :param _TradeInfo: 描述计费相关的信息
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param _ErrorInfo: 任务错误信息
        :type ErrorInfo: list of ErrorInfoItem
        :param _DumperResumeCtrl: 全量导出可重入标识：enum::"yes"/"no"。yes表示当前任务可重入、no表示当前任务处于全量导出且不可重入阶段；如果在该值为no时重启任务导出流程不支持断点续传
        :type DumperResumeCtrl: str
        :param _RateLimitOption: 任务的限速信息
        :type RateLimitOption: :class:`tencentcloud.dts.v20211206.models.RateLimitOption`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._DumperResumeCtrl = None
        self._RateLimitOption = None
        self._RequestId = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """数据迁移任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def CreateTime(self):
        """任务创建(提交)时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """任务更新时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        """任务开始执行时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务执行结束时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BriefMsg(self):
        """迁移任务简要错误信息
        :rtype: str
        """
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def Status(self):
        """任务状态，取值为：created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行中)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)、
pausing(暂停中)、
manualPaused(已暂停)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Action(self):
        """任务操作信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StepInfo(self):
        """迁移执行过程信息，在校验阶段显示校验过程步骤信息，在迁移阶段会显示迁移步骤信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def SrcInfo(self):
        """源实例信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        """目标端信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def CompareTask(self):
        """数据一致性校验结果
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        """
        return self._CompareTask

    @CompareTask.setter
    def CompareTask(self, CompareTask):
        self._CompareTask = CompareTask

    @property
    def Tags(self):
        """标签信息
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RunMode(self):
        """运行模式，取值如：immediate(表示立即运行)、timed(表示定时运行)
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        """期待启动时间，当RunMode取值为timed时，此值必填，形如："2006-01-02 15:04:05"
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def MigrateOption(self):
        """迁移选项，描述任务如何执行迁移等一系列配置信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        """
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def CheckStepInfo(self):
        """校验任务运行详情
        :rtype: :class:`tencentcloud.dts.v20211206.models.CheckStepInfo`
        """
        return self._CheckStepInfo

    @CheckStepInfo.setter
    def CheckStepInfo(self, CheckStepInfo):
        self._CheckStepInfo = CheckStepInfo

    @property
    def TradeInfo(self):
        """描述计费相关的信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        """
        return self._TradeInfo

    @TradeInfo.setter
    def TradeInfo(self, TradeInfo):
        self._TradeInfo = TradeInfo

    @property
    def ErrorInfo(self):
        """任务错误信息
        :rtype: list of ErrorInfoItem
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def DumperResumeCtrl(self):
        """全量导出可重入标识：enum::"yes"/"no"。yes表示当前任务可重入、no表示当前任务处于全量导出且不可重入阶段；如果在该值为no时重启任务导出流程不支持断点续传
        :rtype: str
        """
        return self._DumperResumeCtrl

    @DumperResumeCtrl.setter
    def DumperResumeCtrl(self, DumperResumeCtrl):
        self._DumperResumeCtrl = DumperResumeCtrl

    @property
    def RateLimitOption(self):
        """任务的限速信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.RateLimitOption`
        """
        return self._RateLimitOption

    @RateLimitOption.setter
    def RateLimitOption(self, RateLimitOption):
        self._RateLimitOption = RateLimitOption

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        self._DumperResumeCtrl = params.get("DumperResumeCtrl")
        if params.get("RateLimitOption") is not None:
            self._RateLimitOption = RateLimitOption()
            self._RateLimitOption._deserialize(params.get("RateLimitOption"))
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
        """数据迁移任务ID，如：dts-amm1jw5q
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """数据迁移任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Status(self):
        """数据迁移任务状态，可取值包括：created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行中)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SrcInstanceId(self):
        """源实例ID，格式如：cdb-c1nl9rpv
        :rtype: str
        """
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def SrcRegion(self):
        """源实例地域，如：ap-guangzhou
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def SrcDatabaseType(self):
        """源实例数据库类型，如：sqlserver,mysql,mongodb,redis,tendis,keewidb,clickhouse,cynosdbmysql,percona,tdsqlpercona,mariadb,tdsqlmysql,postgresql
        :rtype: list of str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        """源实例接入类型，值包括：extranet(外网)、vpncloud(云vpn接入的实例)、dcg(专线接入的实例)、ccn(云联网接入的实例)、cdb(云上cdb实例)、cvm(cvm自建实例)
        :rtype: list of str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def DstInstanceId(self):
        """目标实例ID，格式如：cdb-c1nl9rpv
        :rtype: str
        """
        return self._DstInstanceId

    @DstInstanceId.setter
    def DstInstanceId(self, DstInstanceId):
        self._DstInstanceId = DstInstanceId

    @property
    def DstRegion(self):
        """目标实例地域，如：ap-guangzhou
        :rtype: str
        """
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def DstDatabaseType(self):
        """目标源实例数据库类型，如：sqlserver,mysql,mongodb,redis,tendis,keewidb,clickhouse,cynosdbmysql,percona,tdsqlpercona,mariadb,tdsqlmysql,postgresql
        :rtype: list of str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        """目标实例接入类型，值包括：extranet(外网)、vpncloud(云vpn接入的实例)、dcg(专线接入的实例)、ccn(云联网接入的实例)、cdb(云上cdb实例)、cvm(cvm自建实例)
        :rtype: list of str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def RunMode(self):
        """任务运行模式，值包括：immediate(立即运行)，timed(定时运行)
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def OrderSeq(self):
        """排序方式，可能取值为asc、desc，默认按照创建时间倒序
        :rtype: str
        """
        return self._OrderSeq

    @OrderSeq.setter
    def OrderSeq(self, OrderSeq):
        self._OrderSeq = OrderSeq

    @property
    def Limit(self):
        """返回实例数量，默认20，有效区间[1,100]
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TagFilters(self):
        """标签过滤
        :rtype: list of TagFilter
        """
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
        :type TotalCount: int
        :param _JobList: 迁移任务列表
        :type JobList: list of JobItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """迁移任务数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobList(self):
        """迁移任务列表
        :rtype: list of JobItem
        """
        return self._JobList

    @JobList.setter
    def JobList(self, JobList):
        self._JobList = JobList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :type StepCount: int
        :param _StepCur: 当前所在步骤
        :type StepCur: int
        :param _Progress: 总体进度，范围为[0,100]	
        :type Progress: int
        :param _StepInfos: 步骤详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfos: list of StepInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        """校验任务执行状态，如：notStarted(未开始)、running(校验中)、failed(校验任务失败)、success(任务成功)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StepCount(self):
        """校验的步骤总数
        :rtype: int
        """
        return self._StepCount

    @StepCount.setter
    def StepCount(self, StepCount):
        self._StepCount = StepCount

    @property
    def StepCur(self):
        """当前所在步骤
        :rtype: int
        """
        return self._StepCur

    @StepCur.setter
    def StepCur(self, StepCur):
        self._StepCur = StepCur

    @property
    def Progress(self):
        """总体进度，范围为[0,100]	
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfos(self):
        """步骤详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StepInfo
        """
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeOffsetByTimeRequest(AbstractModel):
    """DescribeOffsetByTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        :param _Time: 时间点，格式为：Y-m-d h:m:s。如果输入时间比当前时间晚的多，相当于查询最新offset；如果输入时间比当前时间早的多，相当于查询最老offset；如果输入空，默认0时间，等价于查询最老offset。
        :type Time: str
        """
        self._SubscribeId = None
        self._Time = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def Time(self):
        """时间点，格式为：Y-m-d h:m:s。如果输入时间比当前时间晚的多，相当于查询最新offset；如果输入时间比当前时间早的多，相当于查询最老offset；如果输入空，默认0时间，等价于查询最老offset。
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOffsetByTimeResponse(AbstractModel):
    """DescribeOffsetByTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 时间与Offset的对应
        :type Items: list of OffsetTimeMap
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """时间与Offset的对应
        :rtype: list of OffsetTimeMap
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OffsetTimeMap()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeCheckJobRequest(AbstractModel):
    """DescribeSubscribeCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeCheckJobResponse(AbstractModel):
    """DescribeSubscribeCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID
        :type SubscribeId: str
        :param _Message: 失败或者报错提示，成功则提示success。
        :type Message: str
        :param _Status: 任务运行状态，可能值为 running,failed,success
        :type Status: str
        :param _Progress: 当前总体进度，范围 0~100
        :type Progress: int
        :param _StepAll: 校验总步骤数
        :type StepAll: int
        :param _StepNow: 当前执行步骤
        :type StepNow: int
        :param _Steps: 各个步骤运行状态
        :type Steps: list of SubscribeCheckStepInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscribeId = None
        self._Message = None
        self._Status = None
        self._Progress = None
        self._StepAll = None
        self._StepNow = None
        self._Steps = None
        self._RequestId = None

    @property
    def SubscribeId(self):
        """订阅实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def Message(self):
        """失败或者报错提示，成功则提示success。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Status(self):
        """任务运行状态，可能值为 running,failed,success
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        """当前总体进度，范围 0~100
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepAll(self):
        """校验总步骤数
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """当前执行步骤
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Steps(self):
        """各个步骤运行状态
        :rtype: list of SubscribeCheckStepInfo
        """
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._Message = params.get("Message")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = SubscribeCheckStepInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeDetailRequest(AbstractModel):
    """DescribeSubscribeDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """订阅实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeDetailResponse(AbstractModel):
    """DescribeSubscribeDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅的ID，形如subs-b6x64o31tm
        :type SubscribeId: str
        :param _SubscribeName: 数据订阅实例的名称
        :type SubscribeName: str
        :param _Product: 订阅的数据库类型，目前支持 cynosdbmysql(tdsql-c mysql版),mariadb,mongodb,mysql,percona,tdpg(tdsql postgresql版),tdsqlpercona(tdsql mysql版)
        :type Product: str
        :param _InstanceId: 订阅的云数据库实例ID，只有订阅云数据库该值才有意义
        :type InstanceId: str
        :param _InstanceStatus: 订阅的云数据库实例状态，只有订阅云数据库该值才有意义。可能值为：running, isolated, offline
        :type InstanceStatus: str
        :param _Status: 订阅任务计费状态，可能值为：正常normal, 隔离中isolating, 已隔离isolated, 下线中offlining, 按量转包年包月中 post2PrePayIng
        :type Status: str
        :param _SubsStatus: 订阅任务状态，可能值为：未启动notStarted, 校验中checking, 校验不通过checkNotPass, 校验通过checkPass, 启动中starting, 运行中running, 异常出错error
        :type SubsStatus: str
        :param _ModifyTime: 修改时间，时间格式如：Y-m-d h:m:s
        :type ModifyTime: str
        :param _CreateTime: 创建时间，时间格式如：Y-m-d h:m:s
        :type CreateTime: str
        :param _IsolateTime: 隔离时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :type IsolateTime: str
        :param _ExpireTime: 包年包月任务的到期时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :type ExpireTime: str
        :param _OfflineTime: 下线时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :type OfflineTime: str
        :param _PayType: 付费方式，可能值为：0-包年包月，1-按量计费
        :type PayType: int
        :param _AutoRenewFlag: 自动续费标识。只有当 PayType=0，该值才有意义。枚举值：0-不自动续费，1-自动续费
        :type AutoRenewFlag: int
        :param _Region: 任务所在地域
        :type Region: str
        :param _Topic: Kafka topic
        :type Topic: str
        :param _Broker: Kafka服务Broker地址
        :type Broker: str
        :param _SubscribeMode: 数据订阅的类型，当 Product 不为 mongodb 时，可能值为：all-全实例更新；dml-数据更新；ddl-结构更新；dmlAndDdl-数据更新+结构更新。当 Product 为 mongodb 时，可能值为 all-全实例更新；database-订阅单库；collection-订阅单集合
        :type SubscribeMode: str
        :param _Protocol: 订阅数据格式。如果为空则用的默认格式: mysql\cynosdbmysql\mariadb\percona\tdsqlpercona\tdpg是protobuf，mongo是json。当 DatabaseType 为 mysql和cynosdbmysql 时有三种可选协议：protobuf\avro\json。数据格式详情参考官网的消费demo文档
        :type Protocol: str
        :param _SubscribeObjects: 订阅的数据库表信息
        :type SubscribeObjects: list of SubscribeObject
        :param _KafkaConfig: kafka配置信息
        :type KafkaConfig: :class:`tencentcloud.dts.v20211206.models.SubscribeKafkaConfig`
        :param _KafkaVersion: 订阅内置kafka的版本信息
        :type KafkaVersion: str
        :param _AccessType: 源数据库接入类型，如：extranet(公网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、cdb(云数据库)、cvm(云服务器自建)、intranet(自研上云)、vpc(私有网络vpc)。注意具体可选值依赖当前链路支持能力
        :type AccessType: str
        :param _Endpoints: 接入类型信息
        :type Endpoints: list of EndpointItem
        :param _PipelineInfo: mongo输出聚合设置
        :type PipelineInfo: list of PipelineInfo
        :param _Tags: 标签
        :type Tags: list of TagItem
        :param _Errors: 订阅任务报错信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of SubsErr
        :param _ExtraAttr: 为业务添加的额外信息。参数名作key，参数值作value。
mysql选填参数：ProcessXA-是否处理XA事务，为true处理，其他不处理。
mongo选填参数：SubscribeType-订阅类型，目前只支持changeStream。
        :type ExtraAttr: list of KeyValuePairOption
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._Product = None
        self._InstanceId = None
        self._InstanceStatus = None
        self._Status = None
        self._SubsStatus = None
        self._ModifyTime = None
        self._CreateTime = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._PayType = None
        self._AutoRenewFlag = None
        self._Region = None
        self._Topic = None
        self._Broker = None
        self._SubscribeMode = None
        self._Protocol = None
        self._SubscribeObjects = None
        self._KafkaConfig = None
        self._KafkaVersion = None
        self._AccessType = None
        self._Endpoints = None
        self._PipelineInfo = None
        self._Tags = None
        self._Errors = None
        self._ExtraAttr = None
        self._RequestId = None

    @property
    def SubscribeId(self):
        """数据订阅的ID，形如subs-b6x64o31tm
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """数据订阅实例的名称
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def Product(self):
        """订阅的数据库类型，目前支持 cynosdbmysql(tdsql-c mysql版),mariadb,mongodb,mysql,percona,tdpg(tdsql postgresql版),tdsqlpercona(tdsql mysql版)
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """订阅的云数据库实例ID，只有订阅云数据库该值才有意义
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """订阅的云数据库实例状态，只有订阅云数据库该值才有意义。可能值为：running, isolated, offline
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def Status(self):
        """订阅任务计费状态，可能值为：正常normal, 隔离中isolating, 已隔离isolated, 下线中offlining, 按量转包年包月中 post2PrePayIng
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubsStatus(self):
        """订阅任务状态，可能值为：未启动notStarted, 校验中checking, 校验不通过checkNotPass, 校验通过checkPass, 启动中starting, 运行中running, 异常出错error
        :rtype: str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def ModifyTime(self):
        """修改时间，时间格式如：Y-m-d h:m:s
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        """创建时间，时间格式如：Y-m-d h:m:s
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsolateTime(self):
        """隔离时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        """包年包月任务的到期时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        """下线时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def PayType(self):
        """付费方式，可能值为：0-包年包月，1-按量计费
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def AutoRenewFlag(self):
        """自动续费标识。只有当 PayType=0，该值才有意义。枚举值：0-不自动续费，1-自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Region(self):
        """任务所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Topic(self):
        """Kafka topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Broker(self):
        """Kafka服务Broker地址
        :rtype: str
        """
        return self._Broker

    @Broker.setter
    def Broker(self, Broker):
        self._Broker = Broker

    @property
    def SubscribeMode(self):
        """数据订阅的类型，当 Product 不为 mongodb 时，可能值为：all-全实例更新；dml-数据更新；ddl-结构更新；dmlAndDdl-数据更新+结构更新。当 Product 为 mongodb 时，可能值为 all-全实例更新；database-订阅单库；collection-订阅单集合
        :rtype: str
        """
        return self._SubscribeMode

    @SubscribeMode.setter
    def SubscribeMode(self, SubscribeMode):
        self._SubscribeMode = SubscribeMode

    @property
    def Protocol(self):
        """订阅数据格式。如果为空则用的默认格式: mysql\cynosdbmysql\mariadb\percona\tdsqlpercona\tdpg是protobuf，mongo是json。当 DatabaseType 为 mysql和cynosdbmysql 时有三种可选协议：protobuf\avro\json。数据格式详情参考官网的消费demo文档
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SubscribeObjects(self):
        """订阅的数据库表信息
        :rtype: list of SubscribeObject
        """
        return self._SubscribeObjects

    @SubscribeObjects.setter
    def SubscribeObjects(self, SubscribeObjects):
        self._SubscribeObjects = SubscribeObjects

    @property
    def KafkaConfig(self):
        """kafka配置信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.SubscribeKafkaConfig`
        """
        return self._KafkaConfig

    @KafkaConfig.setter
    def KafkaConfig(self, KafkaConfig):
        self._KafkaConfig = KafkaConfig

    @property
    def KafkaVersion(self):
        """订阅内置kafka的版本信息
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def AccessType(self):
        """源数据库接入类型，如：extranet(公网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、cdb(云数据库)、cvm(云服务器自建)、intranet(自研上云)、vpc(私有网络vpc)。注意具体可选值依赖当前链路支持能力
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Endpoints(self):
        """接入类型信息
        :rtype: list of EndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def PipelineInfo(self):
        """mongo输出聚合设置
        :rtype: list of PipelineInfo
        """
        return self._PipelineInfo

    @PipelineInfo.setter
    def PipelineInfo(self, PipelineInfo):
        self._PipelineInfo = PipelineInfo

    @property
    def Tags(self):
        """标签
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Errors(self):
        """订阅任务报错信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SubsErr
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def ExtraAttr(self):
        """为业务添加的额外信息。参数名作key，参数值作value。
mysql选填参数：ProcessXA-是否处理XA事务，为true处理，其他不处理。
mongo选填参数：SubscribeType-订阅类型，目前只支持changeStream。
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._Status = params.get("Status")
        self._SubsStatus = params.get("SubsStatus")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._PayType = params.get("PayType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Region = params.get("Region")
        self._Topic = params.get("Topic")
        self._Broker = params.get("Broker")
        self._SubscribeMode = params.get("SubscribeMode")
        self._Protocol = params.get("Protocol")
        if params.get("SubscribeObjects") is not None:
            self._SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self._SubscribeObjects.append(obj)
        if params.get("KafkaConfig") is not None:
            self._KafkaConfig = SubscribeKafkaConfig()
            self._KafkaConfig._deserialize(params.get("KafkaConfig"))
        self._KafkaVersion = params.get("KafkaVersion")
        self._AccessType = params.get("AccessType")
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = EndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        if params.get("PipelineInfo") is not None:
            self._PipelineInfo = []
            for item in params.get("PipelineInfo"):
                obj = PipelineInfo()
                obj._deserialize(item)
                self._PipelineInfo.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SubsErr()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeJobsRequest(AbstractModel):
    """DescribeSubscribeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅 ID 筛选，精确匹配
        :type SubscribeId: str
        :param _SubscribeIds: 订阅 ID 筛选，精确匹配
        :type SubscribeIds: list of str
        :param _SubscribeName: 订阅名称，前缀模糊匹配
        :type SubscribeName: str
        :param _InstanceId: 订阅的云上数据库实例的 ID，精确匹配
        :type InstanceId: str
        :param _Topic: 订阅的topicName
        :type Topic: str
        :param _PayType: 计费模式筛选，可能的值：0-包年包月，1-按量计费
        :type PayType: int
        :param _Product: 订阅的数据库产品，目前支持 cynosdbmysql,mariadb,mongodb,mysql,percona,tdpg,tdsqlpercona(tdsqlmysql)
        :type Product: str
        :param _Status: 数据订阅生命周期状态，可能的值为：正常 normal, 隔离中 isolating, 已隔离 isolated, 下线中 offlining，按量转包年包月中 post2PrePayIng
        :type Status: list of str
        :param _SubsStatus: 数据订阅状态，可能的值为：未启动 notStarted, 校验中 checking, 校验不通过 checkNotPass, 校验通过 checkPass, 启动中 starting, 运行中 running, 异常出错 error
        :type SubsStatus: list of str
        :param _Offset: 返回记录的起始偏移量。默认0
        :type Offset: int
        :param _Limit: 单次返回的记录数量。默认20，最大100
        :type Limit: int
        :param _OrderDirection: 排序方向，可选的值为"DESC"和"ASC"，默认为"DESC"，按创建时间逆序排序
        :type OrderDirection: str
        :param _TagFilters: tag 过滤条件，多个 TagFilter 之间关系为且
        :type TagFilters: list of TagFilter
        """
        self._SubscribeId = None
        self._SubscribeIds = None
        self._SubscribeName = None
        self._InstanceId = None
        self._Topic = None
        self._PayType = None
        self._Product = None
        self._Status = None
        self._SubsStatus = None
        self._Offset = None
        self._Limit = None
        self._OrderDirection = None
        self._TagFilters = None

    @property
    def SubscribeId(self):
        """订阅 ID 筛选，精确匹配
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeIds(self):
        """订阅 ID 筛选，精确匹配
        :rtype: list of str
        """
        return self._SubscribeIds

    @SubscribeIds.setter
    def SubscribeIds(self, SubscribeIds):
        self._SubscribeIds = SubscribeIds

    @property
    def SubscribeName(self):
        """订阅名称，前缀模糊匹配
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def InstanceId(self):
        """订阅的云上数据库实例的 ID，精确匹配
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """订阅的topicName
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def PayType(self):
        """计费模式筛选，可能的值：0-包年包月，1-按量计费
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Product(self):
        """订阅的数据库产品，目前支持 cynosdbmysql,mariadb,mongodb,mysql,percona,tdpg,tdsqlpercona(tdsqlmysql)
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Status(self):
        """数据订阅生命周期状态，可能的值为：正常 normal, 隔离中 isolating, 已隔离 isolated, 下线中 offlining，按量转包年包月中 post2PrePayIng
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubsStatus(self):
        """数据订阅状态，可能的值为：未启动 notStarted, 校验中 checking, 校验不通过 checkNotPass, 校验通过 checkPass, 启动中 starting, 运行中 running, 异常出错 error
        :rtype: list of str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def Offset(self):
        """返回记录的起始偏移量。默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """单次返回的记录数量。默认20，最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderDirection(self):
        """排序方向，可选的值为"DESC"和"ASC"，默认为"DESC"，按创建时间逆序排序
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def TagFilters(self):
        """tag 过滤条件，多个 TagFilter 之间关系为且
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeIds = params.get("SubscribeIds")
        self._SubscribeName = params.get("SubscribeName")
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._PayType = params.get("PayType")
        self._Product = params.get("Product")
        self._Status = params.get("Status")
        self._SubsStatus = params.get("SubsStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderDirection = params.get("OrderDirection")
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
        


class DescribeSubscribeJobsResponse(AbstractModel):
    """DescribeSubscribeJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param _Items: 数据订阅实例的信息列表
        :type Items: list of SubscribeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合查询条件的实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """数据订阅实例的信息列表
        :rtype: list of SubscribeInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SubscribeInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeReturnableRequest(AbstractModel):
    """DescribeSubscribeReturnable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeReturnableResponse(AbstractModel):
    """DescribeSubscribeReturnable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsReturnable: 实例是否支持退还/退货
        :type IsReturnable: bool
        :param _ReturnFailMessage: 不支持退还的原因
        :type ReturnFailMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsReturnable = None
        self._ReturnFailMessage = None
        self._RequestId = None

    @property
    def IsReturnable(self):
        """实例是否支持退还/退货
        :rtype: bool
        """
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def ReturnFailMessage(self):
        """不支持退还的原因
        :rtype: str
        """
        return self._ReturnFailMessage

    @ReturnFailMessage.setter
    def ReturnFailMessage(self, ReturnFailMessage):
        self._ReturnFailMessage = ReturnFailMessage

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsReturnable = params.get("IsReturnable")
        self._ReturnFailMessage = params.get("ReturnFailMessage")
        self._RequestId = params.get("RequestId")


class DescribeSyncJobsRequest(AbstractModel):
    """DescribeSyncJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 同步任务id，如sync-werwfs23
        :type JobId: str
        :param _JobIds: 同步任务id列表，如sync-werwfs23
        :type JobIds: list of str
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
        :param _SrcInfoPattern: 源端数据库连接信息，可以输入实例ID或者IP等
        :type SrcInfoPattern: str
        :param _DstInfoPattern: 目标端数据库连接信息，可以输入实例ID或者IP等
        :type DstInfoPattern: str
        """
        self._JobId = None
        self._JobIds = None
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
        self._SrcInfoPattern = None
        self._DstInfoPattern = None

    @property
    def JobId(self):
        """同步任务id，如sync-werwfs23
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobIds(self):
        """同步任务id列表，如sync-werwfs23
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def JobName(self):
        """同步任务名
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Order(self):
        """排序字段，可以取值为CreateTime
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderSeq(self):
        """排序方式，升序为ASC，降序为DESC，默认为CreateTime降序
        :rtype: str
        """
        return self._OrderSeq

    @OrderSeq.setter
    def OrderSeq(self, OrderSeq):
        self._OrderSeq = OrderSeq

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回同步任务实例数量，默认20，有效区间[1,100]
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """状态集合，如Initialized,CheckPass,Running,ResumableErr,Stopped
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RunMode(self):
        """运行模式，如Immediate:立即运行，Timed:定时运行
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def JobType(self):
        """任务类型，如mysql2mysql：msyql同步到mysql
        :rtype: str
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def PayMode(self):
        """付费类型，PrePay：预付费，PostPay：后付费
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TagFilters(self):
        """tag
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def SrcInfoPattern(self):
        """源端数据库连接信息，可以输入实例ID或者IP等
        :rtype: str
        """
        return self._SrcInfoPattern

    @SrcInfoPattern.setter
    def SrcInfoPattern(self, SrcInfoPattern):
        self._SrcInfoPattern = SrcInfoPattern

    @property
    def DstInfoPattern(self):
        """目标端数据库连接信息，可以输入实例ID或者IP等
        :rtype: str
        """
        return self._DstInfoPattern

    @DstInfoPattern.setter
    def DstInfoPattern(self, DstInfoPattern):
        self._DstInfoPattern = DstInfoPattern


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobIds = params.get("JobIds")
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
        self._SrcInfoPattern = params.get("SrcInfoPattern")
        self._DstInfoPattern = params.get("DstInfoPattern")
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
        :type TotalCount: int
        :param _JobList: 任务详情数组
        :type JobList: list of SyncJobInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """任务数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobList(self):
        """任务详情数组
        :rtype: list of SyncJobInfo
        """
        return self._JobList

    @JobList.setter
    def JobList(self, JobList):
        self._JobList = JobList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DestroyIsolatedSubscribeRequest(AbstractModel):
    """DestroyIsolatedSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyIsolatedSubscribeResponse(AbstractModel):
    """DestroyIsolatedSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
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
        """任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type CheckItemName: str
        :param _Description: 检查项详细内容
        :type Description: str
        :param _CheckResult: pass(通过)，failed(失败), warning(校验有警告，但仍通过)
        :type CheckResult: str
        :param _FailureReason: 检查项失败原因
        :type FailureReason: str
        :param _Solution: 解决方案
        :type Solution: str
        :param _ErrorLog: 运行报错日志
        :type ErrorLog: list of str
        :param _HelpDoc: 详细帮助的文档链接
        :type HelpDoc: list of str
        :param _SkipInfo: 跳过风险文案
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
        """检查项的名称，如：源实例权限检查
        :rtype: str
        """
        return self._CheckItemName

    @CheckItemName.setter
    def CheckItemName(self, CheckItemName):
        self._CheckItemName = CheckItemName

    @property
    def Description(self):
        """检查项详细内容
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CheckResult(self):
        """pass(通过)，failed(失败), warning(校验有警告，但仍通过)
        :rtype: str
        """
        return self._CheckResult

    @CheckResult.setter
    def CheckResult(self, CheckResult):
        self._CheckResult = CheckResult

    @property
    def FailureReason(self):
        """检查项失败原因
        :rtype: str
        """
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def Solution(self):
        """解决方案
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def ErrorLog(self):
        """运行报错日志
        :rtype: list of str
        """
        return self._ErrorLog

    @ErrorLog.setter
    def ErrorLog(self, ErrorLog):
        self._ErrorLog = ErrorLog

    @property
    def HelpDoc(self):
        """详细帮助的文档链接
        :rtype: list of str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc

    @property
    def SkipInfo(self):
        """跳过风险文案
        :rtype: str
        """
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
        


class DifferenceAdvancedObjectsDetail(AbstractModel):
    """数据库不一致的详情，mongodb业务用到

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Items: 不一致详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AdvancedObjectsItem
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """不一致详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AdvancedObjectsItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AdvancedObjectsItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceData(AbstractModel):
    """数据不一致详情

    """

    def __init__(self):
        r"""
        :param _Db: 数据库名
        :type Db: str
        :param _Table: 集合
        :type Table: str
        :param _SrcChunk: 源端ID
        :type SrcChunk: str
        :param _DstChunk: 目标端ID
        :type DstChunk: str
        :param _SrcItem: 源端值
        :type SrcItem: str
        :param _DstItem: 目标端值
        :type DstItem: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        """
        self._Db = None
        self._Table = None
        self._SrcChunk = None
        self._DstChunk = None
        self._SrcItem = None
        self._DstItem = None
        self._UpdatedAt = None

    @property
    def Db(self):
        """数据库名
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        """集合
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def SrcChunk(self):
        """源端ID
        :rtype: str
        """
        return self._SrcChunk

    @SrcChunk.setter
    def SrcChunk(self, SrcChunk):
        self._SrcChunk = SrcChunk

    @property
    def DstChunk(self):
        """目标端ID
        :rtype: str
        """
        return self._DstChunk

    @DstChunk.setter
    def DstChunk(self, DstChunk):
        self._DstChunk = DstChunk

    @property
    def SrcItem(self):
        """源端值
        :rtype: str
        """
        return self._SrcItem

    @SrcItem.setter
    def SrcItem(self, SrcItem):
        self._SrcItem = SrcItem

    @property
    def DstItem(self):
        """目标端值
        :rtype: str
        """
        return self._DstItem

    @DstItem.setter
    def DstItem(self, DstItem):
        self._DstItem = DstItem

    @property
    def UpdatedAt(self):
        """更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Table = params.get("Table")
        self._SrcChunk = params.get("SrcChunk")
        self._DstChunk = params.get("DstChunk")
        self._SrcItem = params.get("SrcItem")
        self._DstItem = params.get("DstItem")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceDataDetail(AbstractModel):
    """mongodb数据不一致性详情

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Items: mongo数据不一致详细列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DifferenceData
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """mongo数据不一致详细列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DifferenceData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DifferenceData()
                obj._deserialize(item)
                self._Items.append(obj)
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
        :type TotalCount: int
        :param _Items: 校验不一致的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DifferenceItem
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        """数据不一致的表数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """校验不一致的表详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DifferenceItem
        """
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
        :type Db: str
        :param _Table: 表名
        :type Table: str
        :param _Chunk: 分块号
        :type Chunk: int
        :param _SrcItem: 源库数值
        :type SrcItem: str
        :param _DstItem: 目标库数值
        :type DstItem: str
        :param _IndexName: 索引名称
        :type IndexName: str
        :param _LowerBoundary: 索引下边界
        :type LowerBoundary: str
        :param _UpperBoundary: 索引上边界
        :type UpperBoundary: str
        :param _CostTime: 对比消耗时间,单位为 ms
        :type CostTime: float
        :param _FinishedAt: 完成时间
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
        """数据库名
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        """表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Chunk(self):
        """分块号
        :rtype: int
        """
        return self._Chunk

    @Chunk.setter
    def Chunk(self, Chunk):
        self._Chunk = Chunk

    @property
    def SrcItem(self):
        """源库数值
        :rtype: str
        """
        return self._SrcItem

    @SrcItem.setter
    def SrcItem(self, SrcItem):
        self._SrcItem = SrcItem

    @property
    def DstItem(self):
        """目标库数值
        :rtype: str
        """
        return self._DstItem

    @DstItem.setter
    def DstItem(self, DstItem):
        self._DstItem = DstItem

    @property
    def IndexName(self):
        """索引名称
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def LowerBoundary(self):
        """索引下边界
        :rtype: str
        """
        return self._LowerBoundary

    @LowerBoundary.setter
    def LowerBoundary(self, LowerBoundary):
        self._LowerBoundary = LowerBoundary

    @property
    def UpperBoundary(self):
        """索引上边界
        :rtype: str
        """
        return self._UpperBoundary

    @UpperBoundary.setter
    def UpperBoundary(self, UpperBoundary):
        self._UpperBoundary = UpperBoundary

    @property
    def CostTime(self):
        """对比消耗时间,单位为 ms
        :rtype: float
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def FinishedAt(self):
        """完成时间
        :rtype: str
        """
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
        


class DifferenceRowDetail(AbstractModel):
    """mongodb行数校验不一致性详情结果

    """

    def __init__(self):
        r"""
        :param _TotalCount: 不一致总数
        :type TotalCount: int
        :param _Items: 不一致列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of RowsCountDifference
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        """不一致总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """不一致列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RowsCountDifference
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RowsCountDifference()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeRule(AbstractModel):
    """订阅任务的kafka分区规则。符合库名和表名正则表达式的数据将按照RuleType计算该条数据将被投递的kafka分区。如果配置了多个规则，将按照配置的顺序，第一条命中的规则生效。

    """

    def __init__(self):
        r"""
        :param _RuleType: 规则类型。非mongo产品的枚举值为: table-按表名分区，pk-按表名+主键分区，cols-按列名分区。mongo的枚举值为：collection-按集合名分区、collectionAndObjectId-按集合+主键分区。
        :type RuleType: str
        :param _DbPattern: 库名匹配规则，请填写正则表达式
        :type DbPattern: str
        :param _TablePattern: 表名匹配规则，如果 DatabaseType 为 mongodb，则匹配集合名
        :type TablePattern: str
        :param _Columns: 列名。如果 RuleType 为 cols，此项必填。订阅任务会用该列的值计算分区。mongo没有按列分区，因此也不用传这个字段。
        :type Columns: list of str
        """
        self._RuleType = None
        self._DbPattern = None
        self._TablePattern = None
        self._Columns = None

    @property
    def RuleType(self):
        """规则类型。非mongo产品的枚举值为: table-按表名分区，pk-按表名+主键分区，cols-按列名分区。mongo的枚举值为：collection-按集合名分区、collectionAndObjectId-按集合+主键分区。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def DbPattern(self):
        """库名匹配规则，请填写正则表达式
        :rtype: str
        """
        return self._DbPattern

    @DbPattern.setter
    def DbPattern(self, DbPattern):
        self._DbPattern = DbPattern

    @property
    def TablePattern(self):
        """表名匹配规则，如果 DatabaseType 为 mongodb，则匹配集合名
        :rtype: str
        """
        return self._TablePattern

    @TablePattern.setter
    def TablePattern(self, TablePattern):
        self._TablePattern = TablePattern

    @property
    def Columns(self):
        """列名。如果 RuleType 为 cols，此项必填。订阅任务会用该列的值计算分区。mongo没有按列分区，因此也不用传这个字段。
        :rtype: list of str
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._DbPattern = params.get("DbPattern")
        self._TablePattern = params.get("TablePattern")
        self._Columns = params.get("Columns")
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
        :type OpTypes: list of str
        :param _DdlOptions: DDL同步选项，具体描述要同步哪些DDL; 当OpTypes取值PartialDDL时、字段不能为空；必填、dts会用该值覆盖原有的值
        :type DdlOptions: list of DdlOption
        :param _ConflictHandleType: 冲突处理选项，ReportError(报错)、Ignore(忽略)、Cover(覆盖)、ConditionCover(条件覆盖); 目前目标端为kafka的链路不支持修改该配置
        :type ConflictHandleType: str
        :param _ConflictHandleOption: 冲突处理的详细选项，如条件覆盖中的条件行和条件操作；不能部分更新该选项的内部字段；有更新时、需要全量更新该字段
        :type ConflictHandleOption: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        :param _KafkaOption: 同步到kafka链路的kafka配置
        :type KafkaOption: :class:`tencentcloud.dts.v20211206.models.KafkaOption`
        :param _FilterBeginCommit: 同步到kafka链路是否过滤掉begin和commit消息。目前仅mysql2kafka链路支持
        :type FilterBeginCommit: bool
        :param _FilterCheckpoint: 同步到kafka链路是否过滤掉checkpoint消息。目前仅mysql2kafka链路支持
        :type FilterCheckpoint: bool
        :param _DealOfExistSameTable: 同名表的处理，ReportErrorAfterCheck(前置校验并报错，默认)、ExecuteAfterIgnore(忽略并继续执行)
        :type DealOfExistSameTable: str
        :param _StartPosition: 仅增量任务重新设置指定位点
        :type StartPosition: str
        """
        self._OpTypes = None
        self._DdlOptions = None
        self._ConflictHandleType = None
        self._ConflictHandleOption = None
        self._KafkaOption = None
        self._FilterBeginCommit = None
        self._FilterCheckpoint = None
        self._DealOfExistSameTable = None
        self._StartPosition = None

    @property
    def OpTypes(self):
        """所要同步的DML和DDL的选项，Insert(插入操作)、Update(更新操作)、Delete(删除操作)、DDL(结构同步)，PartialDDL(自定义,和DdlOptions一起起作用 )；必填、dts会用该值覆盖原有的值
        :rtype: list of str
        """
        return self._OpTypes

    @OpTypes.setter
    def OpTypes(self, OpTypes):
        self._OpTypes = OpTypes

    @property
    def DdlOptions(self):
        """DDL同步选项，具体描述要同步哪些DDL; 当OpTypes取值PartialDDL时、字段不能为空；必填、dts会用该值覆盖原有的值
        :rtype: list of DdlOption
        """
        return self._DdlOptions

    @DdlOptions.setter
    def DdlOptions(self, DdlOptions):
        self._DdlOptions = DdlOptions

    @property
    def ConflictHandleType(self):
        """冲突处理选项，ReportError(报错)、Ignore(忽略)、Cover(覆盖)、ConditionCover(条件覆盖); 目前目标端为kafka的链路不支持修改该配置
        :rtype: str
        """
        return self._ConflictHandleType

    @ConflictHandleType.setter
    def ConflictHandleType(self, ConflictHandleType):
        self._ConflictHandleType = ConflictHandleType

    @property
    def ConflictHandleOption(self):
        """冲突处理的详细选项，如条件覆盖中的条件行和条件操作；不能部分更新该选项的内部字段；有更新时、需要全量更新该字段
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        """
        return self._ConflictHandleOption

    @ConflictHandleOption.setter
    def ConflictHandleOption(self, ConflictHandleOption):
        self._ConflictHandleOption = ConflictHandleOption

    @property
    def KafkaOption(self):
        """同步到kafka链路的kafka配置
        :rtype: :class:`tencentcloud.dts.v20211206.models.KafkaOption`
        """
        return self._KafkaOption

    @KafkaOption.setter
    def KafkaOption(self, KafkaOption):
        self._KafkaOption = KafkaOption

    @property
    def FilterBeginCommit(self):
        """同步到kafka链路是否过滤掉begin和commit消息。目前仅mysql2kafka链路支持
        :rtype: bool
        """
        return self._FilterBeginCommit

    @FilterBeginCommit.setter
    def FilterBeginCommit(self, FilterBeginCommit):
        self._FilterBeginCommit = FilterBeginCommit

    @property
    def FilterCheckpoint(self):
        """同步到kafka链路是否过滤掉checkpoint消息。目前仅mysql2kafka链路支持
        :rtype: bool
        """
        return self._FilterCheckpoint

    @FilterCheckpoint.setter
    def FilterCheckpoint(self, FilterCheckpoint):
        self._FilterCheckpoint = FilterCheckpoint

    @property
    def DealOfExistSameTable(self):
        """同名表的处理，ReportErrorAfterCheck(前置校验并报错，默认)、ExecuteAfterIgnore(忽略并继续执行)
        :rtype: str
        """
        return self._DealOfExistSameTable

    @DealOfExistSameTable.setter
    def DealOfExistSameTable(self, DealOfExistSameTable):
        self._DealOfExistSameTable = DealOfExistSameTable

    @property
    def StartPosition(self):
        """仅增量任务重新设置指定位点
        :rtype: str
        """
        return self._StartPosition

    @StartPosition.setter
    def StartPosition(self, StartPosition):
        self._StartPosition = StartPosition


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
        if params.get("KafkaOption") is not None:
            self._KafkaOption = KafkaOption()
            self._KafkaOption._deserialize(params.get("KafkaOption"))
        self._FilterBeginCommit = params.get("FilterBeginCommit")
        self._FilterCheckpoint = params.get("FilterCheckpoint")
        self._DealOfExistSameTable = params.get("DealOfExistSameTable")
        self._StartPosition = params.get("StartPosition")
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
        :type Region: str
        :param _Role: 节点类型，proxy表示节点类型为主机，set表示节点类型为节点。proxy类型必须填在数组第一项。tdsqlmysql类型的源/目标配置必填
        :type Role: str
        :param _DbKernel: 数据库内核类型，tdsql中用于区分不同内核：percona,mariadb,mysql。注意TDSQL-C MySQL、TDSQL PostgreSQL无需填写此项值。
        :type DbKernel: str
        :param _InstanceId: 数据库实例ID，格式如：cdb-powiqx8q
        :type InstanceId: str
        :param _Ip: 实例的IP地址，接入类型为非cdb时此项必填
        :type Ip: str
        :param _Port: 实例端口，接入类型为非cdb时此项必填
        :type Port: int
        :param _User: 用户名，对于访问需要用户名密码认证的实例必填
        :type User: str
        :param _Password: 密码，对于访问需要用户名密码认证的实例必填
        :type Password: str
        :param _DbName: 数据库名，数据库为cdwpg时，需要提供
        :type DbName: str
        :param _VpcId: 私有网络ID，对于私有网络、专线、VPN的接入方式此项必填，格式如：vpc-92jblxto
        :type VpcId: str
        :param _SubnetId: 私有网络下的子网ID，对于私有网络、专线、VPN的接入方式此项必填，格式如：subnet-3paxmkdz
        :type SubnetId: str
        :param _CvmInstanceId: CVM实例短ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要传递此字段
        :type CvmInstanceId: str
        :param _UniqDcgId: 专线网关ID，对于专线接入类型此项必填，格式如：dcg-0rxtqqxb
        :type UniqDcgId: str
        :param _UniqVpnGwId: VPN网关ID，对于vpn接入类型此项必填，格式如：vpngw-9ghexg7q
        :type UniqVpnGwId: str
        :param _CcnId: 云联网ID，对于云联网接入类型此项必填，如：ccn-afp6kltc
        :type CcnId: str
        :param _Supplier: 云厂商类型，当实例为RDS实例时，填写为aliyun, 其他情况均填写others，默认为others
        :type Supplier: str
        :param _EngineVersion: 数据库版本，当实例为RDS实例时才有效，其他实例忽略，格式如：5.6或者5.7，默认为5.6
        :type EngineVersion: str
        :param _Account: 实例所属账号，如果为跨账号实例此项必填
        :type Account: str
        :param _AccountMode: 资源所属账号 为空或self(表示本账号内资源)、other(表示跨账号资源)
        :type AccountMode: str
        :param _AccountRole: 跨账号同步时的角色，只允许[a-zA-Z0-9\-\_]+，如果为跨账号实例此项必填
        :type AccountRole: str
        :param _RoleExternalId: 外部角色id
        :type RoleExternalId: str
        :param _TmpSecretId: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号同步文档(https://cloud.tencent.com/document/product/571/68729)第4节中关于角色的定义。
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号同步文档(https://cloud.tencent.com/document/product/571/68729)第4节中关于角色的定义。
        :type TmpSecretKey: str
        :param _TmpToken: 临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号同步文档(https://cloud.tencent.com/document/product/571/68729)第4节中关于角色的定义。
        :type TmpToken: str
        :param _EncryptConn: 是否走加密传输、UnEncrypted表示不走加密传输，Encrypted表示走加密传输，默认UnEncrypted
        :type EncryptConn: str
        :param _DatabaseNetEnv: 数据库所属网络环境，AccessType为云联网(ccn)时必填， UserIDC表示用户IDC、TencentVPC表示腾讯云VPC；
        :type DatabaseNetEnv: str
        :param _CcnOwnerUin: 数据库为跨账号云联网下的实例时、表示云联网所属主账号
        :type CcnOwnerUin: str
        :param _ChildInstanceId: 数据库为cynos、且是cynos集群内的一个子数据库实例时、该参数为该子实例的ID
        :type ChildInstanceId: str
        :param _ChildInstanceType: 数据库为cynos、且是cynos集群内的一个子数据库实例时、该参数为该子实例的类型、例如：只读实例传ro、读写实例传rw
        :type ChildInstanceType: str
        :param _SetId: tdsql的分片id。如节点类型为set必填。
        :type SetId: str
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
        self._CcnOwnerUin = None
        self._ChildInstanceId = None
        self._ChildInstanceType = None
        self._SetId = None

    @property
    def Region(self):
        """地域英文名，如：ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Role(self):
        """节点类型，proxy表示节点类型为主机，set表示节点类型为节点。proxy类型必须填在数组第一项。tdsqlmysql类型的源/目标配置必填
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def DbKernel(self):
        """数据库内核类型，tdsql中用于区分不同内核：percona,mariadb,mysql。注意TDSQL-C MySQL、TDSQL PostgreSQL无需填写此项值。
        :rtype: str
        """
        return self._DbKernel

    @DbKernel.setter
    def DbKernel(self, DbKernel):
        self._DbKernel = DbKernel

    @property
    def InstanceId(self):
        """数据库实例ID，格式如：cdb-powiqx8q
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """实例的IP地址，接入类型为非cdb时此项必填
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """实例端口，接入类型为非cdb时此项必填
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        """用户名，对于访问需要用户名密码认证的实例必填
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """密码，对于访问需要用户名密码认证的实例必填
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DbName(self):
        """数据库名，数据库为cdwpg时，需要提供
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def VpcId(self):
        """私有网络ID，对于私有网络、专线、VPN的接入方式此项必填，格式如：vpc-92jblxto
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络下的子网ID，对于私有网络、专线、VPN的接入方式此项必填，格式如：subnet-3paxmkdz
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CvmInstanceId(self):
        """CVM实例短ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要传递此字段
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        """专线网关ID，对于专线接入类型此项必填，格式如：dcg-0rxtqqxb
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def UniqVpnGwId(self):
        """VPN网关ID，对于vpn接入类型此项必填，格式如：vpngw-9ghexg7q
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def CcnId(self):
        """云联网ID，对于云联网接入类型此项必填，如：ccn-afp6kltc
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def Supplier(self):
        """云厂商类型，当实例为RDS实例时，填写为aliyun, 其他情况均填写others，默认为others
        :rtype: str
        """
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def EngineVersion(self):
        """数据库版本，当实例为RDS实例时才有效，其他实例忽略，格式如：5.6或者5.7，默认为5.6
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Account(self):
        """实例所属账号，如果为跨账号实例此项必填
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def AccountMode(self):
        """资源所属账号 为空或self(表示本账号内资源)、other(表示跨账号资源)
        :rtype: str
        """
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def AccountRole(self):
        """跨账号同步时的角色，只允许[a-zA-Z0-9\-\_]+，如果为跨账号实例此项必填
        :rtype: str
        """
        return self._AccountRole

    @AccountRole.setter
    def AccountRole(self, AccountRole):
        self._AccountRole = AccountRole

    @property
    def RoleExternalId(self):
        """外部角色id
        :rtype: str
        """
        return self._RoleExternalId

    @RoleExternalId.setter
    def RoleExternalId(self, RoleExternalId):
        self._RoleExternalId = RoleExternalId

    @property
    def TmpSecretId(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号同步文档(https://cloud.tencent.com/document/product/571/68729)第4节中关于角色的定义。
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号同步文档(https://cloud.tencent.com/document/product/571/68729)第4节中关于角色的定义。
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        """临时密钥Id，可通过申请扮演角色临时访问凭证获取临时密钥https://cloud.tencent.com/document/product/1312/48197，其中角色资源RoleArn的定义可参考DTS跨账号同步文档(https://cloud.tencent.com/document/product/571/68729)第4节中关于角色的定义。
        :rtype: str
        """
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken

    @property
    def EncryptConn(self):
        """是否走加密传输、UnEncrypted表示不走加密传输，Encrypted表示走加密传输，默认UnEncrypted
        :rtype: str
        """
        return self._EncryptConn

    @EncryptConn.setter
    def EncryptConn(self, EncryptConn):
        self._EncryptConn = EncryptConn

    @property
    def DatabaseNetEnv(self):
        """数据库所属网络环境，AccessType为云联网(ccn)时必填， UserIDC表示用户IDC、TencentVPC表示腾讯云VPC；
        :rtype: str
        """
        return self._DatabaseNetEnv

    @DatabaseNetEnv.setter
    def DatabaseNetEnv(self, DatabaseNetEnv):
        self._DatabaseNetEnv = DatabaseNetEnv

    @property
    def CcnOwnerUin(self):
        """数据库为跨账号云联网下的实例时、表示云联网所属主账号
        :rtype: str
        """
        return self._CcnOwnerUin

    @CcnOwnerUin.setter
    def CcnOwnerUin(self, CcnOwnerUin):
        self._CcnOwnerUin = CcnOwnerUin

    @property
    def ChildInstanceId(self):
        """数据库为cynos、且是cynos集群内的一个子数据库实例时、该参数为该子实例的ID
        :rtype: str
        """
        return self._ChildInstanceId

    @ChildInstanceId.setter
    def ChildInstanceId(self, ChildInstanceId):
        self._ChildInstanceId = ChildInstanceId

    @property
    def ChildInstanceType(self):
        """数据库为cynos、且是cynos集群内的一个子数据库实例时、该参数为该子实例的类型、例如：只读实例传ro、读写实例传rw
        :rtype: str
        """
        return self._ChildInstanceType

    @ChildInstanceType.setter
    def ChildInstanceType(self, ChildInstanceType):
        self._ChildInstanceType = ChildInstanceType

    @property
    def SetId(self):
        """tdsql的分片id。如节点类型为set必填。
        :rtype: str
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId


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
        self._CcnOwnerUin = params.get("CcnOwnerUin")
        self._ChildInstanceId = params.get("ChildInstanceId")
        self._ChildInstanceType = params.get("ChildInstanceType")
        self._SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointItem(AbstractModel):
    """数据订阅的实例节点信息

    """

    def __init__(self):
        r"""
        :param _DatabaseRegion: 源库所在地域。如果 AccessType 为 ccn，请填vpc所在地域，因为此时不知道源库在哪个地域。其他接入方式，请填订阅任务所在地域，因为确保订阅任务与源库在同一地域是最优的网络方案。
        :type DatabaseRegion: str
        :param _User: 用户名
        :type User: str
        :param _Password: 密码。作为入参时必填，作为出参时为空。
        :type Password: str
        :param _InstanceId: 目标实例ID。如果 AccessType 为 cdb，此项必填。配置InstanceId时会查询并校验实例信息。mysql的查询接口经过了鉴权，请确保子用户有 cdb:DescribeDBInstances 的接口权限。
        :type InstanceId: str
        :param _CvmInstanceId: 云主机ID。如果 AccessType 为 cvm，此项必填。
        :type CvmInstanceId: str
        :param _UniqDcgId: 专线网关ID。如果 AccessType 为 dcg，此项必填。
        :type UniqDcgId: str
        :param _CcnId: 云联网ID。如果 AccessType 为 ccn，此项必填。 
        :type CcnId: str
        :param _UniqVpnGwId: vpn网关ID。如果 AccessType 为 vpncloud，此项必填。
        :type UniqVpnGwId: str
        :param _VpcId: VpcID。如果 AccessType 为 dcg\ccn\vpncloud\vpc，此项必填。
        :type VpcId: str
        :param _SubnetId: 子网ID。如果 AccessType 为 dcg\ccn\vpncloud\vpc，此项必填。
        :type SubnetId: str
        :param _HostName: 数据库地址，支持域名与IP。如果 AccessType 为 dcg\ccn\vpncloud\vpc\extranet\intranet，此项必填。
        :type HostName: str
        :param _Port: 数据库端口。如果 AccessType 为 dcg\ccn\vpncloud\vpc\extranet\intranet\cvm，此项必填。
        :type Port: int
        :param _EncryptConn: 是否走加密传输，枚举值：UnEncrypted-不加密，Encrypted-加密。只有mysql支持，不填默认不加密，其他产品不填。
        :type EncryptConn: str
        :param _DatabaseNetEnv: 数据库网络环境。如果 AccessType 为 ccn 此项必填。枚举值：UserIDC-自建idc，TencentVPC-腾讯云，Aws-aws，AliYun-阿里云，Others-其他。
        :type DatabaseNetEnv: str
        :param _CcnOwnerUin: 云联网网关所属的主账号uin、跨账号云联网需要。
        :type CcnOwnerUin: str
        :param _ExtraAttr: 为业务添加的额外信息。参数名作key，参数值作value。 
tdpg必填参数：PgDatabase-订阅的库名；
mongo选填参数：InstanceType-实例类型：replicaset-副本集，cluster-分片集，主要用于控制台跳转到mongo实例页面，如不填不影响任务运行；
全业务选填参数：EngineVersion-内核版本。
        :type ExtraAttr: list of KeyValuePairOption
        :param _ChildInstanceId: 数据库为cynos、且是cynos集群内的一个子数据库实例时、该参数为该子实例的ID
        :type ChildInstanceId: str
        :param _ChildInstanceType: 数据库为cynos、且是cynos集群内的一个子数据库实例时、该参数为该子实例的类型、例如：只读实例传ro、读写实例传rw
        :type ChildInstanceType: str
        """
        self._DatabaseRegion = None
        self._User = None
        self._Password = None
        self._InstanceId = None
        self._CvmInstanceId = None
        self._UniqDcgId = None
        self._CcnId = None
        self._UniqVpnGwId = None
        self._VpcId = None
        self._SubnetId = None
        self._HostName = None
        self._Port = None
        self._EncryptConn = None
        self._DatabaseNetEnv = None
        self._CcnOwnerUin = None
        self._ExtraAttr = None
        self._ChildInstanceId = None
        self._ChildInstanceType = None

    @property
    def DatabaseRegion(self):
        """源库所在地域。如果 AccessType 为 ccn，请填vpc所在地域，因为此时不知道源库在哪个地域。其他接入方式，请填订阅任务所在地域，因为确保订阅任务与源库在同一地域是最优的网络方案。
        :rtype: str
        """
        return self._DatabaseRegion

    @DatabaseRegion.setter
    def DatabaseRegion(self, DatabaseRegion):
        self._DatabaseRegion = DatabaseRegion

    @property
    def User(self):
        """用户名
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """密码。作为入参时必填，作为出参时为空。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InstanceId(self):
        """目标实例ID。如果 AccessType 为 cdb，此项必填。配置InstanceId时会查询并校验实例信息。mysql的查询接口经过了鉴权，请确保子用户有 cdb:DescribeDBInstances 的接口权限。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmInstanceId(self):
        """云主机ID。如果 AccessType 为 cvm，此项必填。
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        """专线网关ID。如果 AccessType 为 dcg，此项必填。
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def CcnId(self):
        """云联网ID。如果 AccessType 为 ccn，此项必填。 
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def UniqVpnGwId(self):
        """vpn网关ID。如果 AccessType 为 vpncloud，此项必填。
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def VpcId(self):
        """VpcID。如果 AccessType 为 dcg\ccn\vpncloud\vpc，此项必填。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID。如果 AccessType 为 dcg\ccn\vpncloud\vpc，此项必填。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def HostName(self):
        """数据库地址，支持域名与IP。如果 AccessType 为 dcg\ccn\vpncloud\vpc\extranet\intranet，此项必填。
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def Port(self):
        """数据库端口。如果 AccessType 为 dcg\ccn\vpncloud\vpc\extranet\intranet\cvm，此项必填。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def EncryptConn(self):
        """是否走加密传输，枚举值：UnEncrypted-不加密，Encrypted-加密。只有mysql支持，不填默认不加密，其他产品不填。
        :rtype: str
        """
        return self._EncryptConn

    @EncryptConn.setter
    def EncryptConn(self, EncryptConn):
        self._EncryptConn = EncryptConn

    @property
    def DatabaseNetEnv(self):
        """数据库网络环境。如果 AccessType 为 ccn 此项必填。枚举值：UserIDC-自建idc，TencentVPC-腾讯云，Aws-aws，AliYun-阿里云，Others-其他。
        :rtype: str
        """
        return self._DatabaseNetEnv

    @DatabaseNetEnv.setter
    def DatabaseNetEnv(self, DatabaseNetEnv):
        self._DatabaseNetEnv = DatabaseNetEnv

    @property
    def CcnOwnerUin(self):
        """云联网网关所属的主账号uin、跨账号云联网需要。
        :rtype: str
        """
        return self._CcnOwnerUin

    @CcnOwnerUin.setter
    def CcnOwnerUin(self, CcnOwnerUin):
        self._CcnOwnerUin = CcnOwnerUin

    @property
    def ExtraAttr(self):
        """为业务添加的额外信息。参数名作key，参数值作value。 
tdpg必填参数：PgDatabase-订阅的库名；
mongo选填参数：InstanceType-实例类型：replicaset-副本集，cluster-分片集，主要用于控制台跳转到mongo实例页面，如不填不影响任务运行；
全业务选填参数：EngineVersion-内核版本。
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def ChildInstanceId(self):
        """数据库为cynos、且是cynos集群内的一个子数据库实例时、该参数为该子实例的ID
        :rtype: str
        """
        return self._ChildInstanceId

    @ChildInstanceId.setter
    def ChildInstanceId(self, ChildInstanceId):
        self._ChildInstanceId = ChildInstanceId

    @property
    def ChildInstanceType(self):
        """数据库为cynos、且是cynos集群内的一个子数据库实例时、该参数为该子实例的类型、例如：只读实例传ro、读写实例传rw
        :rtype: str
        """
        return self._ChildInstanceType

    @ChildInstanceType.setter
    def ChildInstanceType(self, ChildInstanceType):
        self._ChildInstanceType = ChildInstanceType


    def _deserialize(self, params):
        self._DatabaseRegion = params.get("DatabaseRegion")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._InstanceId = params.get("InstanceId")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._CcnId = params.get("CcnId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._HostName = params.get("HostName")
        self._Port = params.get("Port")
        self._EncryptConn = params.get("EncryptConn")
        self._DatabaseNetEnv = params.get("DatabaseNetEnv")
        self._CcnOwnerUin = params.get("CcnOwnerUin")
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        self._ChildInstanceId = params.get("ChildInstanceId")
        self._ChildInstanceType = params.get("ChildInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrInfo(AbstractModel):
    """错误信息及其解决方案

    """

    def __init__(self):
        r"""
        :param _Reason: 错误原因
        :type Reason: str
        :param _Message: 错误信息
        :type Message: str
        :param _Solution: 解决方案
        :type Solution: str
        """
        self._Reason = None
        self._Message = None
        self._Solution = None

    @property
    def Reason(self):
        """错误原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Message(self):
        """错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Solution(self):
        """解决方案
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        self._Message = params.get("Message")
        self._Solution = params.get("Solution")
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
        :type Code: str
        :param _Solution: 解决方案
        :type Solution: str
        :param _ErrorLog: 错误日志信息
        :type ErrorLog: str
        :param _HelpDoc: 文档提示
        :type HelpDoc: str
        """
        self._Code = None
        self._Solution = None
        self._ErrorLog = None
        self._HelpDoc = None

    @property
    def Code(self):
        """错误码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Solution(self):
        """解决方案
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def ErrorLog(self):
        """错误日志信息
        :rtype: str
        """
        return self._ErrorLog

    @ErrorLog.setter
    def ErrorLog(self, ErrorLog):
        self._ErrorLog = ErrorLog

    @property
    def HelpDoc(self):
        """文档提示
        :rtype: str
        """
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
        


class GroupInfo(AbstractModel):
    """kafka消费者组详情

    """

    def __init__(self):
        r"""
        :param _Account: 消费者组账号
        :type Account: str
        :param _ConsumerGroupName: 消费者组名称
        :type ConsumerGroupName: str
        :param _Description: 消费者组备注
        :type Description: str
        :param _ConsumerGroupOffset: 消费组偏移量。该字段是为了兼容以前单Partition的情况，取值为最后一个分区的偏移量。各分区的偏移量详见StateOfPartition字段
        :type ConsumerGroupOffset: int
        :param _ConsumerGroupLag: 消费组未消费的数据量。该字段是为了兼容以前单Partition的情况，取值为最后一个分区未消费的数据量。各分区未消费数据量详见StateOfPartition字段
        :type ConsumerGroupLag: int
        :param _Latency: 消费延迟(单位为秒)
        :type Latency: int
        :param _StateOfPartition: 各分区的消费状态
        :type StateOfPartition: list of MonitorInfo
        :param _CreatedAt: 消费者组创建时间，格式为YYYY-MM-DD hh:mm:ss
        :type CreatedAt: str
        :param _UpdatedAt: 消费者组修改时间，格式为YYYY-MM-DD hh:mm:ss
        :type UpdatedAt: str
        :param _ConsumerGroupState: 消费者组状态，包括Dead、Empty、Stable等，只有Dead和Empty两种状态可以执行reset操作
        :type ConsumerGroupState: str
        :param _PartitionAssignment: 每个消费者正在消费的分区
        :type PartitionAssignment: list of PartitionAssignment
        """
        self._Account = None
        self._ConsumerGroupName = None
        self._Description = None
        self._ConsumerGroupOffset = None
        self._ConsumerGroupLag = None
        self._Latency = None
        self._StateOfPartition = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._ConsumerGroupState = None
        self._PartitionAssignment = None

    @property
    def Account(self):
        """消费者组账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def ConsumerGroupName(self):
        """消费者组名称
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def Description(self):
        """消费者组备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConsumerGroupOffset(self):
        """消费组偏移量。该字段是为了兼容以前单Partition的情况，取值为最后一个分区的偏移量。各分区的偏移量详见StateOfPartition字段
        :rtype: int
        """
        return self._ConsumerGroupOffset

    @ConsumerGroupOffset.setter
    def ConsumerGroupOffset(self, ConsumerGroupOffset):
        self._ConsumerGroupOffset = ConsumerGroupOffset

    @property
    def ConsumerGroupLag(self):
        """消费组未消费的数据量。该字段是为了兼容以前单Partition的情况，取值为最后一个分区未消费的数据量。各分区未消费数据量详见StateOfPartition字段
        :rtype: int
        """
        return self._ConsumerGroupLag

    @ConsumerGroupLag.setter
    def ConsumerGroupLag(self, ConsumerGroupLag):
        self._ConsumerGroupLag = ConsumerGroupLag

    @property
    def Latency(self):
        """消费延迟(单位为秒)
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def StateOfPartition(self):
        """各分区的消费状态
        :rtype: list of MonitorInfo
        """
        return self._StateOfPartition

    @StateOfPartition.setter
    def StateOfPartition(self, StateOfPartition):
        self._StateOfPartition = StateOfPartition

    @property
    def CreatedAt(self):
        """消费者组创建时间，格式为YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        """消费者组修改时间，格式为YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def ConsumerGroupState(self):
        """消费者组状态，包括Dead、Empty、Stable等，只有Dead和Empty两种状态可以执行reset操作
        :rtype: str
        """
        return self._ConsumerGroupState

    @ConsumerGroupState.setter
    def ConsumerGroupState(self, ConsumerGroupState):
        self._ConsumerGroupState = ConsumerGroupState

    @property
    def PartitionAssignment(self):
        """每个消费者正在消费的分区
        :rtype: list of PartitionAssignment
        """
        return self._PartitionAssignment

    @PartitionAssignment.setter
    def PartitionAssignment(self, PartitionAssignment):
        self._PartitionAssignment = PartitionAssignment


    def _deserialize(self, params):
        self._Account = params.get("Account")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._Description = params.get("Description")
        self._ConsumerGroupOffset = params.get("ConsumerGroupOffset")
        self._ConsumerGroupLag = params.get("ConsumerGroupLag")
        self._Latency = params.get("Latency")
        if params.get("StateOfPartition") is not None:
            self._StateOfPartition = []
            for item in params.get("StateOfPartition"):
                obj = MonitorInfo()
                obj._deserialize(item)
                self._StateOfPartition.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._ConsumerGroupState = params.get("ConsumerGroupState")
        if params.get("PartitionAssignment") is not None:
            self._PartitionAssignment = []
            for item in params.get("PartitionAssignment"):
                obj = PartitionAssignment()
                obj._deserialize(item)
                self._PartitionAssignment.append(obj)
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
        """任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class IsolateSubscribeRequest(AbstractModel):
    """IsolateSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """订阅实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSubscribeResponse(AbstractModel):
    """IsolateSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type JobId: str
        :param _JobName: 数据迁移任务名称
        :type JobName: str
        :param _CreateTime: 任务创建(提交)时间，格式为 yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _UpdateTime: 任务更新时间，格式为 yyyy-mm-dd hh:mm:ss
        :type UpdateTime: str
        :param _StartTime: 任务开始执行时间，格式为 yyyy-mm-dd hh:mm:ss
        :type StartTime: str
        :param _EndTime: 任务执行结束时间，格式为 yyyy-mm-dd hh:mm:ss
        :type EndTime: str
        :param _BriefMsg: 迁移任务错误信息
        :type BriefMsg: str
        :param _Status: 任务状态，取值为：creating(创建中)、created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)、
pausing(暂停中)、
manualPaused(已暂停)
        :type Status: str
        :param _RunMode: 任务运行模式，值包括：immediate(立即运行)，timed(定时运行)
        :type RunMode: str
        :param _ExpectRunTime: 期待启动时间，当RunMode取值为timed时，此值必填，形如：2022-07-11 16:20:49
        :type ExpectRunTime: str
        :param _Action: 任务操作信息
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param _StepInfo: 迁移执行过程信息
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param _SrcInfo: 源实例信息
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _DstInfo: 目标端信息
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _CompareTask: 数据一致性校验结果
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param _TradeInfo: 计费状态信息
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param _Tags: 标签信息
        :type Tags: list of TagItem
        :param _AutoRetryTimeRangeMinutes: 自动重试时间段信息
        :type AutoRetryTimeRangeMinutes: int
        :param _DumperResumeCtrl: 全量导出可重入标识：enum::"yes"/"no"。yes表示当前任务可重入、no表示当前任务处于全量导出且不可重入阶段；如果在该值为no时重启任务导出流程不支持断点续传
        :type DumperResumeCtrl: str
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
        self._DumperResumeCtrl = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """数据迁移任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def CreateTime(self):
        """任务创建(提交)时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """任务更新时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        """任务开始执行时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务执行结束时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BriefMsg(self):
        """迁移任务错误信息
        :rtype: str
        """
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def Status(self):
        """任务状态，取值为：creating(创建中)、created(创建完成)、checking(校验中)、checkPass(校验通过)、checkNotPass(校验不通过)、readyRun(准备运行)、running(任务运行)、readyComplete(准备完成)、success(任务成功)、failed(任务失败)、stopping(中止中)、completing(完成中)、
pausing(暂停中)、
manualPaused(已暂停)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RunMode(self):
        """任务运行模式，值包括：immediate(立即运行)，timed(定时运行)
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        """期待启动时间，当RunMode取值为timed时，此值必填，形如：2022-07-11 16:20:49
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def Action(self):
        """任务操作信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StepInfo(self):
        """迁移执行过程信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def SrcInfo(self):
        """源实例信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        """目标端信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def CompareTask(self):
        """数据一致性校验结果
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        """
        return self._CompareTask

    @CompareTask.setter
    def CompareTask(self, CompareTask):
        self._CompareTask = CompareTask

    @property
    def TradeInfo(self):
        """计费状态信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        """
        return self._TradeInfo

    @TradeInfo.setter
    def TradeInfo(self, TradeInfo):
        self._TradeInfo = TradeInfo

    @property
    def Tags(self):
        """标签信息
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRetryTimeRangeMinutes(self):
        """自动重试时间段信息
        :rtype: int
        """
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes

    @property
    def DumperResumeCtrl(self):
        """全量导出可重入标识：enum::"yes"/"no"。yes表示当前任务可重入、no表示当前任务处于全量导出且不可重入阶段；如果在该值为no时重启任务导出流程不支持断点续传
        :rtype: str
        """
        return self._DumperResumeCtrl

    @DumperResumeCtrl.setter
    def DumperResumeCtrl(self, DumperResumeCtrl):
        self._DumperResumeCtrl = DumperResumeCtrl


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
        self._DumperResumeCtrl = params.get("DumperResumeCtrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaOption(AbstractModel):
    """目标端为kafka时添加的同步选项字段

    """

    def __init__(self):
        r"""
        :param _DataType: 投递到kafka的数据类型，如Avro,Json,canal-pb,canal-json
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
        """投递到kafka的数据类型，如Avro,Json,canal-pb,canal-json
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TopicType(self):
        """同步topic策略，如Single（集中投递到单topic）,Multi (自定义topic名称)
        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def DDLTopicName(self):
        """用于存储ddl的topic
        :rtype: str
        """
        return self._DDLTopicName

    @DDLTopicName.setter
    def DDLTopicName(self, DDLTopicName):
        self._DDLTopicName = DDLTopicName

    @property
    def TopicRules(self):
        """单topic和自定义topic的描述
        :rtype: list of TopicRule
        """
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
        :type Key: str
        :param _Value: 选项value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """选项key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """选项value
        :rtype: str
        """
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
        :type AllAction: list of str
        :param _AllowedAction: 任务在当前状态下允许的操作列表
        :type AllowedAction: list of str
        """
        self._AllAction = None
        self._AllowedAction = None

    @property
    def AllAction(self):
        """任务的所有操作列表
        :rtype: list of str
        """
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        """任务在当前状态下允许的操作列表
        :rtype: list of str
        """
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
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        """实例Vip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """实例Vport
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Usable(self):
        """是否可以作为迁移对象，1-可以，0-不可以
        :rtype: int
        """
        return self._Usable

    @Usable.setter
    def Usable(self, Usable):
        self._Usable = Usable

    @property
    def Hint(self):
        """不可以作为迁移对象的原因
        :rtype: str
        """
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
        :type StepAll: int
        :param _StepNow: 当前步骤
        :type StepNow: int
        :param _MasterSlaveDistance: 主从差距，MB；只在任务正常，迁移或者同步的最后一步（追Binlog的阶段才有校），如果是非法值，返回-1
        :type MasterSlaveDistance: int
        :param _SecondsBehindMaster: 主从差距，秒；只在任务正常，迁移或者同步的最后一步（追Binlog的阶段才有校），如果是非法值，返回-1
        :type SecondsBehindMaster: int
        :param _StepInfo: 步骤信息
        :type StepInfo: list of StepDetailInfo
        """
        self._StepAll = None
        self._StepNow = None
        self._MasterSlaveDistance = None
        self._SecondsBehindMaster = None
        self._StepInfo = None

    @property
    def StepAll(self):
        """总步骤数
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """当前步骤
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def MasterSlaveDistance(self):
        """主从差距，MB；只在任务正常，迁移或者同步的最后一步（追Binlog的阶段才有校），如果是非法值，返回-1
        :rtype: int
        """
        return self._MasterSlaveDistance

    @MasterSlaveDistance.setter
    def MasterSlaveDistance(self, MasterSlaveDistance):
        self._MasterSlaveDistance = MasterSlaveDistance

    @property
    def SecondsBehindMaster(self):
        """主从差距，秒；只在任务正常，迁移或者同步的最后一步（追Binlog的阶段才有校），如果是非法值，返回-1
        :rtype: int
        """
        return self._SecondsBehindMaster

    @SecondsBehindMaster.setter
    def SecondsBehindMaster(self, SecondsBehindMaster):
        self._SecondsBehindMaster = SecondsBehindMaster

    @property
    def StepInfo(self):
        """步骤信息
        :rtype: list of StepDetailInfo
        """
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
        :type DatabaseTable: :class:`tencentcloud.dts.v20211206.models.DatabaseTableObject`
        :param _MigrateType: 迁移类型，full(全量迁移)，structure(结构迁移)，fullAndIncrement(全量加增量迁移)， 默认为fullAndIncrement;注意redis,keewidb产品只支持fullAndIncrement类型。
        :type MigrateType: str
        :param _Consistency: 数据一致性校验选项， 默认为不开启一致性校验
        :type Consistency: :class:`tencentcloud.dts.v20211206.models.ConsistencyOption`
        :param _IsMigrateAccount: 是否迁移账号，true(迁移账号)，false(不迁移账号)
        :type IsMigrateAccount: bool
        :param _IsOverrideRoot: 是否用源库Root账户覆盖目标库，值包括：false-不覆盖，true-覆盖，选择库表或者结构迁移时应该为false，注意只对旧版迁移有效
        :type IsOverrideRoot: bool
        :param _IsDstReadOnly: 是否在迁移时设置目标库只读(仅对mysql有效)，true(设置只读)、false(不设置只读，默认此值)
        :type IsDstReadOnly: bool
        :param _ExtraAttr: 其他附加信息，对于特定库可设置额外参数，Redis可定义如下的参数: 
["DstWriteMode":normal, 	目标库写入模式,可取值clearData(清空目标实例数据)、overwrite(以覆盖写的方式执行任务)、normal(跟正常流程一样，不做额外动作) 	"IsDstReadOnly":true, 	是否在迁移时设置目标库只读,true(设置只读)、false(不设置只读) 	"ClientOutputBufferHardLimit":512, 	从机缓冲区的硬性容量限制(MB) 	"ClientOutputBufferSoftLimit":512, 	从机缓冲区的软性容量限制(MB) 	"ClientOutputBufferPersistTime":60, 从机缓冲区的软性限制持续时间(秒) 	"ReplBacklogSize":512, 	环形缓冲区容量限制(MB) 	"ReplTimeout":120，		复制超时时间(秒) 	"IsExpireKey":"true",过期key自动淘汰]
        :type ExtraAttr: list of KeyValuePairOption
        :param _MigrateWay: pgsql迁移分类：logical(逻辑迁移)、physical(物理迁移)
        :type MigrateWay: str
        """
        self._DatabaseTable = None
        self._MigrateType = None
        self._Consistency = None
        self._IsMigrateAccount = None
        self._IsOverrideRoot = None
        self._IsDstReadOnly = None
        self._ExtraAttr = None
        self._MigrateWay = None

    @property
    def DatabaseTable(self):
        """迁移对象选项，需要告知迁移服务迁移哪些库表对象
        :rtype: :class:`tencentcloud.dts.v20211206.models.DatabaseTableObject`
        """
        return self._DatabaseTable

    @DatabaseTable.setter
    def DatabaseTable(self, DatabaseTable):
        self._DatabaseTable = DatabaseTable

    @property
    def MigrateType(self):
        """迁移类型，full(全量迁移)，structure(结构迁移)，fullAndIncrement(全量加增量迁移)， 默认为fullAndIncrement;注意redis,keewidb产品只支持fullAndIncrement类型。
        :rtype: str
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def Consistency(self):
        """数据一致性校验选项， 默认为不开启一致性校验
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConsistencyOption`
        """
        return self._Consistency

    @Consistency.setter
    def Consistency(self, Consistency):
        self._Consistency = Consistency

    @property
    def IsMigrateAccount(self):
        """是否迁移账号，true(迁移账号)，false(不迁移账号)
        :rtype: bool
        """
        return self._IsMigrateAccount

    @IsMigrateAccount.setter
    def IsMigrateAccount(self, IsMigrateAccount):
        self._IsMigrateAccount = IsMigrateAccount

    @property
    def IsOverrideRoot(self):
        """是否用源库Root账户覆盖目标库，值包括：false-不覆盖，true-覆盖，选择库表或者结构迁移时应该为false，注意只对旧版迁移有效
        :rtype: bool
        """
        return self._IsOverrideRoot

    @IsOverrideRoot.setter
    def IsOverrideRoot(self, IsOverrideRoot):
        self._IsOverrideRoot = IsOverrideRoot

    @property
    def IsDstReadOnly(self):
        """是否在迁移时设置目标库只读(仅对mysql有效)，true(设置只读)、false(不设置只读，默认此值)
        :rtype: bool
        """
        return self._IsDstReadOnly

    @IsDstReadOnly.setter
    def IsDstReadOnly(self, IsDstReadOnly):
        self._IsDstReadOnly = IsDstReadOnly

    @property
    def ExtraAttr(self):
        """其他附加信息，对于特定库可设置额外参数，Redis可定义如下的参数: 
["DstWriteMode":normal, 	目标库写入模式,可取值clearData(清空目标实例数据)、overwrite(以覆盖写的方式执行任务)、normal(跟正常流程一样，不做额外动作) 	"IsDstReadOnly":true, 	是否在迁移时设置目标库只读,true(设置只读)、false(不设置只读) 	"ClientOutputBufferHardLimit":512, 	从机缓冲区的硬性容量限制(MB) 	"ClientOutputBufferSoftLimit":512, 	从机缓冲区的软性容量限制(MB) 	"ClientOutputBufferPersistTime":60, 从机缓冲区的软性限制持续时间(秒) 	"ReplBacklogSize":512, 	环形缓冲区容量限制(MB) 	"ReplTimeout":120，		复制超时时间(秒) 	"IsExpireKey":"true",过期key自动淘汰]
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def MigrateWay(self):
        """pgsql迁移分类：logical(逻辑迁移)、physical(物理迁移)
        :rtype: str
        """
        return self._MigrateWay

    @MigrateWay.setter
    def MigrateWay(self, MigrateWay):
        self._MigrateWay = MigrateWay


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
        self._MigrateWay = params.get("MigrateWay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifiedSubscribeObject(AbstractModel):
    """数据数据订阅的对象，用于修改订阅对象接口。与SubscribeObject结构类似，只是类型和参数名不同。

    """

    def __init__(self):
        r"""
        :param _ObjectsType: 订阅对象的类型，枚举值为：0-库，1-表(该值对于mongo任务来说，是集合) 。
注意：mongo只支持全实例、单库或者单集合订阅，因此该字段不要与SubscribeObjectType冲突。如：SubscribeObjectType=4，表示mongo单库订阅，那么该字段应该传0。
        :type ObjectsType: int
        :param _DatabaseName: 订阅数据库的名称
        :type DatabaseName: str
        :param _TableNames: 订阅数据库中表(或集合)的名称。如果 ObjectsType 为 1，那么此字段为必填，且不为空；
        :type TableNames: list of str
        """
        self._ObjectsType = None
        self._DatabaseName = None
        self._TableNames = None

    @property
    def ObjectsType(self):
        """订阅对象的类型，枚举值为：0-库，1-表(该值对于mongo任务来说，是集合) 。
注意：mongo只支持全实例、单库或者单集合订阅，因此该字段不要与SubscribeObjectType冲突。如：SubscribeObjectType=4，表示mongo单库订阅，那么该字段应该传0。
        :rtype: int
        """
        return self._ObjectsType

    @ObjectsType.setter
    def ObjectsType(self, ObjectsType):
        self._ObjectsType = ObjectsType

    @property
    def DatabaseName(self):
        """订阅数据库的名称
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableNames(self):
        """订阅数据库中表(或集合)的名称。如果 ObjectsType 为 1，那么此字段为必填，且不为空；
        :rtype: list of str
        """
        return self._TableNames

    @TableNames.setter
    def TableNames(self, TableNames):
        self._TableNames = TableNames


    def _deserialize(self, params):
        self._ObjectsType = params.get("ObjectsType")
        self._DatabaseName = params.get("DatabaseName")
        self._TableNames = params.get("TableNames")
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
        """迁移任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        """一致性校验任务名称
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ObjectMode(self):
        """数据对比对象模式，sameAsMigrate(全部迁移对象， 默认为此项配置)、custom(自定义)，注意自定义对比对象必须是迁移对象的子集
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Objects(self):
        """对比对象，若CompareObjectMode取值为custom，则此项必填
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Options(self):
        """一致性校验选项
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyConsumerGroupDescriptionRequest(AbstractModel):
    """ModifyConsumerGroupDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        :param _ConsumerGroupName: 消费组名称。实际的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}。
请务必保证消费组名称正确。
        :type ConsumerGroupName: str
        :param _AccountName: 账户名称。实际的账户全称形如：account-#{SubscribeId}-#{AccountName}。
请务必保证账户名称正确。
        :type AccountName: str
        :param _Description: 修改之后的消费组描述
        :type Description: str
        """
        self._SubscribeId = None
        self._ConsumerGroupName = None
        self._AccountName = None
        self._Description = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def ConsumerGroupName(self):
        """消费组名称。实际的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}。
请务必保证消费组名称正确。
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def AccountName(self):
        """账户名称。实际的账户全称形如：account-#{SubscribeId}-#{AccountName}。
请务必保证账户名称正确。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Description(self):
        """修改之后的消费组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._AccountName = params.get("AccountName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerGroupDescriptionResponse(AbstractModel):
    """ModifyConsumerGroupDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyConsumerGroupPasswordRequest(AbstractModel):
    """ModifyConsumerGroupPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        :param _AccountName: 账号名称。实际的账户全称形如：account-#{SubscribeId}-#{AccountName}
        :type AccountName: str
        :param _ConsumerGroupName: 消费组名称。实际的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}
        :type ConsumerGroupName: str
        :param _NewPassword: 新密码。字符长度不小于3，不大于32
        :type NewPassword: str
        """
        self._SubscribeId = None
        self._AccountName = None
        self._ConsumerGroupName = None
        self._NewPassword = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def AccountName(self):
        """账号名称。实际的账户全称形如：account-#{SubscribeId}-#{AccountName}
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def ConsumerGroupName(self):
        """消费组名称。实际的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def NewPassword(self):
        """新密码。字符长度不小于3，不大于32
        :rtype: str
        """
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._AccountName = params.get("AccountName")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._NewPassword = params.get("NewPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerGroupPasswordResponse(AbstractModel):
    """ModifyConsumerGroupPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NewInstanceClass(self):
        """新实例规格大小，包括：micro、small、medium、large、xlarge、2xlarge
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """迁移任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """修改后的迁移任务名
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrateRateLimitRequest(AbstractModel):
    """ModifyMigrateRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务ID
        :type JobId: str
        :param _DumpThread: 迁移任务全量导出线程数、有效值为 1-16
        :type DumpThread: int
        :param _DumpRps: 迁移全量导出的 Rps 限制、需要大于 0
        :type DumpRps: int
        :param _LoadThread: 迁移任务全量导入线程数、有效值为 1-16
        :type LoadThread: int
        :param _SinkerThread: 迁移任务增量导入线程数、有效值为 1-128
        :type SinkerThread: int
        :param _LoadRps: 全量导入Rps限制
        :type LoadRps: int
        """
        self._JobId = None
        self._DumpThread = None
        self._DumpRps = None
        self._LoadThread = None
        self._SinkerThread = None
        self._LoadRps = None

    @property
    def JobId(self):
        """迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DumpThread(self):
        """迁移任务全量导出线程数、有效值为 1-16
        :rtype: int
        """
        return self._DumpThread

    @DumpThread.setter
    def DumpThread(self, DumpThread):
        self._DumpThread = DumpThread

    @property
    def DumpRps(self):
        """迁移全量导出的 Rps 限制、需要大于 0
        :rtype: int
        """
        return self._DumpRps

    @DumpRps.setter
    def DumpRps(self, DumpRps):
        self._DumpRps = DumpRps

    @property
    def LoadThread(self):
        """迁移任务全量导入线程数、有效值为 1-16
        :rtype: int
        """
        return self._LoadThread

    @LoadThread.setter
    def LoadThread(self, LoadThread):
        self._LoadThread = LoadThread

    @property
    def SinkerThread(self):
        """迁移任务增量导入线程数、有效值为 1-128
        :rtype: int
        """
        return self._SinkerThread

    @SinkerThread.setter
    def SinkerThread(self, SinkerThread):
        self._SinkerThread = SinkerThread

    @property
    def LoadRps(self):
        """全量导入Rps限制
        :rtype: int
        """
        return self._LoadRps

    @LoadRps.setter
    def LoadRps(self, LoadRps):
        self._LoadRps = LoadRps


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._DumpThread = params.get("DumpThread")
        self._DumpRps = params.get("DumpRps")
        self._LoadThread = params.get("LoadThread")
        self._SinkerThread = params.get("SinkerThread")
        self._LoadRps = params.get("LoadRps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateRateLimitResponse(AbstractModel):
    """ModifyMigrateRateLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrateRuntimeAttributeRequest(AbstractModel):
    """ModifyMigrateRuntimeAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务id，如：dts-2rgv0f09
        :type JobId: str
        :param _OtherOptions: 需要修改的属性，此结构设计为通用结构，用于屏蔽多个业务的定制属性。<br>例如对于Redis:<br>{<br>	 "Key": "DstWriteMode",	//目标库写入模式<br> 	"Value": "normal"	          //clearData(清空目标实例数据)、overwrite(以覆盖写的方式执行任务)、normal(跟正常流程一样，不做额外动作，默认为此值) <br>},<br>{<br/>	 "Key": "IsDstReadOnly",	//是否在迁移时设置目标库只读<br/> 	"Value": "true"	          //true(设置只读)、false(不设置只读) <br/>} 
        :type OtherOptions: list of KeyValuePairOption
        """
        self._JobId = None
        self._OtherOptions = None

    @property
    def JobId(self):
        """迁移任务id，如：dts-2rgv0f09
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def OtherOptions(self):
        """需要修改的属性，此结构设计为通用结构，用于屏蔽多个业务的定制属性。<br>例如对于Redis:<br>{<br>	 "Key": "DstWriteMode",	//目标库写入模式<br> 	"Value": "normal"	          //clearData(清空目标实例数据)、overwrite(以覆盖写的方式执行任务)、normal(跟正常流程一样，不做额外动作，默认为此值) <br>},<br>{<br/>	 "Key": "IsDstReadOnly",	//是否在迁移时设置目标库只读<br/> 	"Value": "true"	          //true(设置只读)、false(不设置只读) <br/>} 
        :rtype: list of KeyValuePairOption
        """
        return self._OtherOptions

    @OtherOptions.setter
    def OtherOptions(self, OtherOptions):
        self._OtherOptions = OtherOptions


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("OtherOptions") is not None:
            self._OtherOptions = []
            for item in params.get("OtherOptions"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._OtherOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateRuntimeAttributeResponse(AbstractModel):
    """ModifyMigrateRuntimeAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _MigrateOption: 迁移任务配置选项，描述任务如何执行迁移等一系列配置信息；字段下的RateLimitOption不可配置、如果需要修改任务的限速信息、请在任务运行后通过ModifyMigrateRateLimit接口修改
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
        """任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RunMode(self):
        """运行模式，取值如：immediate(表示立即运行)、timed(表示定时运行)
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def MigrateOption(self):
        """迁移任务配置选项，描述任务如何执行迁移等一系列配置信息；字段下的RateLimitOption不可配置、如果需要修改任务的限速信息、请在任务运行后通过ModifyMigrateRateLimit接口修改
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        """
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcInfo(self):
        """源实例信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        """目标实例信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def JobName(self):
        """迁移任务名称，最大长度128
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def ExpectRunTime(self):
        """期待启动时间，当RunMode取值为timed时，此值必填，形如："2006-01-02 15:04:05"
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def Tags(self):
        """标签信息
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRetryTimeRangeMinutes(self):
        """自动重试的时间段、可设置5至720分钟、0表示不重试
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubscribeAutoRenewFlagRequest(AbstractModel):
    """ModifySubscribeAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID
        :type SubscribeId: str
        :param _AutoRenewFlag: 自动续费标识。1-自动续费，0-不自动续费
        :type AutoRenewFlag: int
        """
        self._SubscribeId = None
        self._AutoRenewFlag = None

    @property
    def SubscribeId(self):
        """订阅实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def AutoRenewFlag(self):
        """自动续费标识。1-自动续费，0-不自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeAutoRenewFlagResponse(AbstractModel):
    """ModifySubscribeAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubscribeNameRequest(AbstractModel):
    """ModifySubscribeName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param _SubscribeName: 修改后的数据订阅实例的名称，长度限制为[1,60]
        :type SubscribeName: str
        """
        self._SubscribeId = None
        self._SubscribeName = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """修改后的数据订阅实例的名称，长度限制为[1,60]
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeNameResponse(AbstractModel):
    """ModifySubscribeName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubscribeObjectsRequest(AbstractModel):
    """ModifySubscribeObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param _SubscribeObjectType: 数据订阅的类型，非mongo任务的枚举值：0-全实例更新；1-数据更新；2-结构更新；3-数据更新+结构更新。mongo任务的枚举值：0-全实例更新；4-订阅单库；5-订阅单集合
        :type SubscribeObjectType: int
        :param _Objects: 修改后的订阅数据库表信息。会覆盖原来的订阅对象，所以除非 SubscribeObjectType = 0或2，否则改字段必填。
        :type Objects: list of ModifiedSubscribeObject
        :param _DistributeRules: kafka分区策略。如果不填，默认不修改。如果填了，会覆盖原来的策略。
        :type DistributeRules: list of DistributeRule
        :param _DefaultRuleType: 默认分区策略。不满足DistributeRules中正则表达式的数据，将按照默认分区策略计算分区。
非mongo产品支持的默认策略: table-按表名分区，pk-按表名+主键分区。mongo的默认策略仅支持：collection-按集合名分区。
该字段与DistributeRules搭配使用。如果配置了DistributeRules，该字段也必填。如果配置了该字段，视为配置了一条DistributeRules，原来的分区策略也会被覆盖。
        :type DefaultRuleType: str
        :param _PipelineInfo: mongo输出聚合设置，mongo任务可选。如果不填，默认不修改。
        :type PipelineInfo: list of PipelineInfo
        """
        self._SubscribeId = None
        self._SubscribeObjectType = None
        self._Objects = None
        self._DistributeRules = None
        self._DefaultRuleType = None
        self._PipelineInfo = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeObjectType(self):
        """数据订阅的类型，非mongo任务的枚举值：0-全实例更新；1-数据更新；2-结构更新；3-数据更新+结构更新。mongo任务的枚举值：0-全实例更新；4-订阅单库；5-订阅单集合
        :rtype: int
        """
        return self._SubscribeObjectType

    @SubscribeObjectType.setter
    def SubscribeObjectType(self, SubscribeObjectType):
        self._SubscribeObjectType = SubscribeObjectType

    @property
    def Objects(self):
        """修改后的订阅数据库表信息。会覆盖原来的订阅对象，所以除非 SubscribeObjectType = 0或2，否则改字段必填。
        :rtype: list of ModifiedSubscribeObject
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def DistributeRules(self):
        """kafka分区策略。如果不填，默认不修改。如果填了，会覆盖原来的策略。
        :rtype: list of DistributeRule
        """
        return self._DistributeRules

    @DistributeRules.setter
    def DistributeRules(self, DistributeRules):
        self._DistributeRules = DistributeRules

    @property
    def DefaultRuleType(self):
        """默认分区策略。不满足DistributeRules中正则表达式的数据，将按照默认分区策略计算分区。
非mongo产品支持的默认策略: table-按表名分区，pk-按表名+主键分区。mongo的默认策略仅支持：collection-按集合名分区。
该字段与DistributeRules搭配使用。如果配置了DistributeRules，该字段也必填。如果配置了该字段，视为配置了一条DistributeRules，原来的分区策略也会被覆盖。
        :rtype: str
        """
        return self._DefaultRuleType

    @DefaultRuleType.setter
    def DefaultRuleType(self, DefaultRuleType):
        self._DefaultRuleType = DefaultRuleType

    @property
    def PipelineInfo(self):
        """mongo输出聚合设置，mongo任务可选。如果不填，默认不修改。
        :rtype: list of PipelineInfo
        """
        return self._PipelineInfo

    @PipelineInfo.setter
    def PipelineInfo(self, PipelineInfo):
        self._PipelineInfo = PipelineInfo


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self._Objects = []
            for item in params.get("Objects"):
                obj = ModifiedSubscribeObject()
                obj._deserialize(item)
                self._Objects.append(obj)
        if params.get("DistributeRules") is not None:
            self._DistributeRules = []
            for item in params.get("DistributeRules"):
                obj = DistributeRule()
                obj._deserialize(item)
                self._DistributeRules.append(obj)
        self._DefaultRuleType = params.get("DefaultRuleType")
        if params.get("PipelineInfo") is not None:
            self._PipelineInfo = []
            for item in params.get("PipelineInfo"):
                obj = PipelineInfo()
                obj._deserialize(item)
                self._PipelineInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeObjectsResponse(AbstractModel):
    """ModifySubscribeObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DynamicObjects(self):
        """修改后的同步对象
        :rtype: :class:`tencentcloud.dts.v20211206.models.Objects`
        """
        return self._DynamicObjects

    @DynamicObjects.setter
    def DynamicObjects(self, DynamicObjects):
        self._DynamicObjects = DynamicObjects

    @property
    def DynamicOptions(self):
        """修改后的同步任务选项
        :rtype: :class:`tencentcloud.dts.v20211206.models.DynamicOptions`
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySyncRateLimitRequest(AbstractModel):
    """ModifySyncRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 迁移任务ID
        :type JobId: str
        :param _DumpThread: 同步任务全量导出线程数、有效值为 1-16
        :type DumpThread: int
        :param _DumpRps: 同步任务全量导出的 Rps 限制、需要大于 0
        :type DumpRps: int
        :param _LoadThread: 同步任务全量导入线程数、有效值为 1-16
        :type LoadThread: int
        :param _SinkerThread: 同步任务增量导入线程数、有效值为 1-128
        :type SinkerThread: int
        :param _LoadRps: 同步任务全量导入的Rps
        :type LoadRps: int
        """
        self._JobId = None
        self._DumpThread = None
        self._DumpRps = None
        self._LoadThread = None
        self._SinkerThread = None
        self._LoadRps = None

    @property
    def JobId(self):
        """迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DumpThread(self):
        """同步任务全量导出线程数、有效值为 1-16
        :rtype: int
        """
        return self._DumpThread

    @DumpThread.setter
    def DumpThread(self, DumpThread):
        self._DumpThread = DumpThread

    @property
    def DumpRps(self):
        """同步任务全量导出的 Rps 限制、需要大于 0
        :rtype: int
        """
        return self._DumpRps

    @DumpRps.setter
    def DumpRps(self, DumpRps):
        self._DumpRps = DumpRps

    @property
    def LoadThread(self):
        """同步任务全量导入线程数、有效值为 1-16
        :rtype: int
        """
        return self._LoadThread

    @LoadThread.setter
    def LoadThread(self, LoadThread):
        self._LoadThread = LoadThread

    @property
    def SinkerThread(self):
        """同步任务增量导入线程数、有效值为 1-128
        :rtype: int
        """
        return self._SinkerThread

    @SinkerThread.setter
    def SinkerThread(self, SinkerThread):
        self._SinkerThread = SinkerThread

    @property
    def LoadRps(self):
        """同步任务全量导入的Rps
        :rtype: int
        """
        return self._LoadRps

    @LoadRps.setter
    def LoadRps(self, LoadRps):
        self._LoadRps = LoadRps


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._DumpThread = params.get("DumpThread")
        self._DumpRps = params.get("DumpRps")
        self._LoadThread = params.get("LoadThread")
        self._SinkerThread = params.get("SinkerThread")
        self._LoadRps = params.get("LoadRps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySyncRateLimitResponse(AbstractModel):
    """ModifySyncRateLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MonitorInfo(AbstractModel):
    """kafka消费者组的分区详情

    """

    def __init__(self):
        r"""
        :param _PartitionNo: 当前分区的编号，从0开始
        :type PartitionNo: int
        :param _ConsumerGroupOffset: 当前分区的偏移量
        :type ConsumerGroupOffset: int
        :param _ConsumerGroupLag: 当前分区未消费的数据量
        :type ConsumerGroupLag: int
        :param _Latency: 当前分区的消费延迟(单位为秒)
        :type Latency: int
        """
        self._PartitionNo = None
        self._ConsumerGroupOffset = None
        self._ConsumerGroupLag = None
        self._Latency = None

    @property
    def PartitionNo(self):
        """当前分区的编号，从0开始
        :rtype: int
        """
        return self._PartitionNo

    @PartitionNo.setter
    def PartitionNo(self, PartitionNo):
        self._PartitionNo = PartitionNo

    @property
    def ConsumerGroupOffset(self):
        """当前分区的偏移量
        :rtype: int
        """
        return self._ConsumerGroupOffset

    @ConsumerGroupOffset.setter
    def ConsumerGroupOffset(self, ConsumerGroupOffset):
        self._ConsumerGroupOffset = ConsumerGroupOffset

    @property
    def ConsumerGroupLag(self):
        """当前分区未消费的数据量
        :rtype: int
        """
        return self._ConsumerGroupLag

    @ConsumerGroupLag.setter
    def ConsumerGroupLag(self, ConsumerGroupLag):
        self._ConsumerGroupLag = ConsumerGroupLag

    @property
    def Latency(self):
        """当前分区的消费延迟(单位为秒)
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency


    def _deserialize(self, params):
        self._PartitionNo = params.get("PartitionNo")
        self._ConsumerGroupOffset = params.get("ConsumerGroupOffset")
        self._ConsumerGroupLag = params.get("ConsumerGroupLag")
        self._Latency = params.get("Latency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Objects(AbstractModel):
    """同步的数据库对对象描述

    """

    def __init__(self):
        r"""
        :param _Mode: 同步对象类型 Partial(部分对象)
        :type Mode: str
        :param _Databases: 同步对象，当 Mode 为 Partial 时，不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of Database
        :param _AdvancedObjects: 高级对象类型，如function、procedure。注意：如果要迁移同步高级对象，此配置中应该包含对应的高级对象类型。当需要同步高级对象时，初始化类型必须包含结构初始化类型，即任务的Options.InitType字段值为Structure或Full
        :type AdvancedObjects: list of str
        :param _OnlineDDL: OnlineDDL类型，冗余字段不做配置用途
        :type OnlineDDL: :class:`tencentcloud.dts.v20211206.models.OnlineDDL`
        """
        self._Mode = None
        self._Databases = None
        self._AdvancedObjects = None
        self._OnlineDDL = None

    @property
    def Mode(self):
        """同步对象类型 Partial(部分对象)
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Databases(self):
        """同步对象，当 Mode 为 Partial 时，不为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def AdvancedObjects(self):
        """高级对象类型，如function、procedure。注意：如果要迁移同步高级对象，此配置中应该包含对应的高级对象类型。当需要同步高级对象时，初始化类型必须包含结构初始化类型，即任务的Options.InitType字段值为Structure或Full
        :rtype: list of str
        """
        return self._AdvancedObjects

    @AdvancedObjects.setter
    def AdvancedObjects(self, AdvancedObjects):
        self._AdvancedObjects = AdvancedObjects

    @property
    def OnlineDDL(self):
        """OnlineDDL类型，冗余字段不做配置用途
        :rtype: :class:`tencentcloud.dts.v20211206.models.OnlineDDL`
        """
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
        


class OffsetTimeMap(AbstractModel):
    """数据订阅kafka分区中checkpoint信息

    """

    def __init__(self):
        r"""
        :param _PartitionNo: kafka分区编号
        :type PartitionNo: int
        :param _Offset: kafka offset
        :type Offset: int
        """
        self._PartitionNo = None
        self._Offset = None

    @property
    def PartitionNo(self):
        """kafka分区编号
        :rtype: int
        """
        return self._PartitionNo

    @PartitionNo.setter
    def PartitionNo(self, PartitionNo):
        self._PartitionNo = PartitionNo

    @property
    def Offset(self):
        """kafka offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._PartitionNo = params.get("PartitionNo")
        self._Offset = params.get("Offset")
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
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        """状态
        :rtype: str
        """
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
        :type InitType: str
        :param _DealOfExistSameTable: 同名表的处理，ReportErrorAfterCheck(前置校验并报错，默认)、ExecuteAfterIgnore(忽略并继续执行)
        :type DealOfExistSameTable: str
        :param _ConflictHandleType: 冲突处理选项，ReportError(报错，默认为该值)、Ignore(忽略)、Cover(覆盖)、ConditionCover(条件覆盖)
        :type ConflictHandleType: str
        :param _AddAdditionalColumn: 是否添加附加列
        :type AddAdditionalColumn: bool
        :param _OpTypes: 所要同步的DML和DDL的选项，Insert(插入操作)、Update(更新操作)、Delete(删除操作)、DDL(结构同步)， PartialDDL(自定义,和DdlOptions一起配合使用)。注意，这里至少需要包含DML中的一种。
注意：此字段可能返回 null，表示取不到有效值。
        :type OpTypes: list of str
        :param _ConflictHandleOption: 冲突处理的详细选项，如条件覆盖中的条件行和条件操作
        :type ConflictHandleOption: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        :param _DdlOptions: DDL同步选项，具体描述要同步哪些DDL
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlOptions: list of DdlOption
        :param _KafkaOption: kafka同步选项
        :type KafkaOption: :class:`tencentcloud.dts.v20211206.models.KafkaOption`
        :param _RateLimitOption: 任务限速信息
        :type RateLimitOption: :class:`tencentcloud.dts.v20211206.models.RateLimitOption`
        :param _AutoRetryTimeRangeMinutes: 自动重试的时间窗口设置
        :type AutoRetryTimeRangeMinutes: int
        :param _StartPosition: 同步到kafka链路指定位点。目前只支持时间格式：2023-12-20T19:24:23+08:00。如果没有指定位点，为空。
        :type StartPosition: str
        :param _FilterBeginCommit: 同步到kafka链路是否过滤掉begin和commit消息。目前仅mysql2kafka链路支持
        :type FilterBeginCommit: bool
        :param _FilterCheckpoint: 同步到kafka链路是否过滤掉checkpoint消息。目前仅mysql2kafka链路支持
        :type FilterCheckpoint: bool
        """
        self._InitType = None
        self._DealOfExistSameTable = None
        self._ConflictHandleType = None
        self._AddAdditionalColumn = None
        self._OpTypes = None
        self._ConflictHandleOption = None
        self._DdlOptions = None
        self._KafkaOption = None
        self._RateLimitOption = None
        self._AutoRetryTimeRangeMinutes = None
        self._StartPosition = None
        self._FilterBeginCommit = None
        self._FilterCheckpoint = None

    @property
    def InitType(self):
        """同步初始化选项，Data(全量数据初始化)、Structure(结构初始化)、Full(全量数据且结构初始化，默认)、None(仅增量)
        :rtype: str
        """
        return self._InitType

    @InitType.setter
    def InitType(self, InitType):
        self._InitType = InitType

    @property
    def DealOfExistSameTable(self):
        """同名表的处理，ReportErrorAfterCheck(前置校验并报错，默认)、ExecuteAfterIgnore(忽略并继续执行)
        :rtype: str
        """
        return self._DealOfExistSameTable

    @DealOfExistSameTable.setter
    def DealOfExistSameTable(self, DealOfExistSameTable):
        self._DealOfExistSameTable = DealOfExistSameTable

    @property
    def ConflictHandleType(self):
        """冲突处理选项，ReportError(报错，默认为该值)、Ignore(忽略)、Cover(覆盖)、ConditionCover(条件覆盖)
        :rtype: str
        """
        return self._ConflictHandleType

    @ConflictHandleType.setter
    def ConflictHandleType(self, ConflictHandleType):
        self._ConflictHandleType = ConflictHandleType

    @property
    def AddAdditionalColumn(self):
        """是否添加附加列
        :rtype: bool
        """
        return self._AddAdditionalColumn

    @AddAdditionalColumn.setter
    def AddAdditionalColumn(self, AddAdditionalColumn):
        self._AddAdditionalColumn = AddAdditionalColumn

    @property
    def OpTypes(self):
        """所要同步的DML和DDL的选项，Insert(插入操作)、Update(更新操作)、Delete(删除操作)、DDL(结构同步)， PartialDDL(自定义,和DdlOptions一起配合使用)。注意，这里至少需要包含DML中的一种。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OpTypes

    @OpTypes.setter
    def OpTypes(self, OpTypes):
        self._OpTypes = OpTypes

    @property
    def ConflictHandleOption(self):
        """冲突处理的详细选项，如条件覆盖中的条件行和条件操作
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        """
        return self._ConflictHandleOption

    @ConflictHandleOption.setter
    def ConflictHandleOption(self, ConflictHandleOption):
        self._ConflictHandleOption = ConflictHandleOption

    @property
    def DdlOptions(self):
        """DDL同步选项，具体描述要同步哪些DDL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DdlOption
        """
        return self._DdlOptions

    @DdlOptions.setter
    def DdlOptions(self, DdlOptions):
        self._DdlOptions = DdlOptions

    @property
    def KafkaOption(self):
        """kafka同步选项
        :rtype: :class:`tencentcloud.dts.v20211206.models.KafkaOption`
        """
        return self._KafkaOption

    @KafkaOption.setter
    def KafkaOption(self, KafkaOption):
        self._KafkaOption = KafkaOption

    @property
    def RateLimitOption(self):
        """任务限速信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.RateLimitOption`
        """
        return self._RateLimitOption

    @RateLimitOption.setter
    def RateLimitOption(self, RateLimitOption):
        self._RateLimitOption = RateLimitOption

    @property
    def AutoRetryTimeRangeMinutes(self):
        """自动重试的时间窗口设置
        :rtype: int
        """
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes

    @property
    def StartPosition(self):
        """同步到kafka链路指定位点。目前只支持时间格式：2023-12-20T19:24:23+08:00。如果没有指定位点，为空。
        :rtype: str
        """
        return self._StartPosition

    @StartPosition.setter
    def StartPosition(self, StartPosition):
        self._StartPosition = StartPosition

    @property
    def FilterBeginCommit(self):
        """同步到kafka链路是否过滤掉begin和commit消息。目前仅mysql2kafka链路支持
        :rtype: bool
        """
        return self._FilterBeginCommit

    @FilterBeginCommit.setter
    def FilterBeginCommit(self, FilterBeginCommit):
        self._FilterBeginCommit = FilterBeginCommit

    @property
    def FilterCheckpoint(self):
        """同步到kafka链路是否过滤掉checkpoint消息。目前仅mysql2kafka链路支持
        :rtype: bool
        """
        return self._FilterCheckpoint

    @FilterCheckpoint.setter
    def FilterCheckpoint(self, FilterCheckpoint):
        self._FilterCheckpoint = FilterCheckpoint


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
        if params.get("RateLimitOption") is not None:
            self._RateLimitOption = RateLimitOption()
            self._RateLimitOption._deserialize(params.get("RateLimitOption"))
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        self._StartPosition = params.get("StartPosition")
        self._FilterBeginCommit = params.get("FilterBeginCommit")
        self._FilterCheckpoint = params.get("FilterCheckpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionAssignment(AbstractModel):
    """数据订阅中kafka消费者组的分区分配情况。该数据是实时查询的，如果需要最新数据，需重新掉接口查询。

    """

    def __init__(self):
        r"""
        :param _ClientId: 消费者的clientId
        :type ClientId: str
        :param _PartitionNo: 该消费者正在消费的分区
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionNo: list of int non-negative
        """
        self._ClientId = None
        self._PartitionNo = None

    @property
    def ClientId(self):
        """消费者的clientId
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def PartitionNo(self):
        """该消费者正在消费的分区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int non-negative
        """
        return self._PartitionNo

    @PartitionNo.setter
    def PartitionNo(self, PartitionNo):
        self._PartitionNo = PartitionNo


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._PartitionNo = params.get("PartitionNo")
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
        """数据迁移任务ID
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PipelineInfo(AbstractModel):
    """mongo输出聚合设置。输出默认 Change Event

    """

    def __init__(self):
        r"""
        :param _AggOp: 聚合运算符：$addFields、$match、$project、$replaceRoot、$redact、$replaceWith、$set、$unset。其中 $replaceWith、$set、$unset 只有当订阅实例是4.2及以上版本可选。
        :type AggOp: str
        :param _AggCmd: 聚合表达式。必须是json格式
        :type AggCmd: str
        """
        self._AggOp = None
        self._AggCmd = None

    @property
    def AggOp(self):
        """聚合运算符：$addFields、$match、$project、$replaceRoot、$redact、$replaceWith、$set、$unset。其中 $replaceWith、$set、$unset 只有当订阅实例是4.2及以上版本可选。
        :rtype: str
        """
        return self._AggOp

    @AggOp.setter
    def AggOp(self, AggOp):
        self._AggOp = AggOp

    @property
    def AggCmd(self):
        """聚合表达式。必须是json格式
        :rtype: str
        """
        return self._AggCmd

    @AggCmd.setter
    def AggCmd(self, AggCmd):
        self._AggCmd = AggCmd


    def _deserialize(self, params):
        self._AggOp = params.get("AggOp")
        self._AggCmd = params.get("AggCmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessProgress(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        r"""
        :param _Status: 步骤的状态， 包括：notStarted(未开始)、running(运行中)、success(成功)、failed(失败)等
        :type Status: str
        :param _Percent: 进度信息
        :type Percent: int
        :param _StepAll: 总的步骤数
        :type StepAll: int
        :param _StepNow: 当前进行的步骤
        :type StepNow: int
        :param _Message: 当前步骤输出提示信息
        :type Message: str
        :param _Steps: 步骤信息
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
        """步骤的状态， 包括：notStarted(未开始)、running(运行中)、success(成功)、failed(失败)等
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        """进度信息
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def StepAll(self):
        """总的步骤数
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """当前进行的步骤
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Message(self):
        """当前步骤输出提示信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Steps(self):
        """步骤信息
        :rtype: list of StepDetailInfo
        """
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
        :type Message: str
        :param _Solution: 解决方案
        :type Solution: str
        :param _HelpDoc: 文档提示
        :type HelpDoc: str
        """
        self._Message = None
        self._Solution = None
        self._HelpDoc = None

    @property
    def Message(self):
        """提示信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Solution(self):
        """解决方案
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def HelpDoc(self):
        """文档提示
        :rtype: str
        """
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
        


class RateLimitOption(AbstractModel):
    """迁移和同步任务限速的详细信息

    """

    def __init__(self):
        r"""
        :param _CurrentDumpThread: 当前生效的全量导出线程数，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为16
        :type CurrentDumpThread: int
        :param _DefaultDumpThread: 默认的全量导出线程数，该字段仅在出参有意义
        :type DefaultDumpThread: int
        :param _CurrentDumpRps: 当前生效的全量导出Rps，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为50000000
        :type CurrentDumpRps: int
        :param _DefaultDumpRps: 默认的全量导出Rps，该字段仅在出参有意义
        :type DefaultDumpRps: int
        :param _CurrentLoadThread: 当前生效的全量导入线程数，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为16
        :type CurrentLoadThread: int
        :param _DefaultLoadThread: 默认的全量导入线程数，该字段仅在出参有意义
        :type DefaultLoadThread: int
        :param _CurrentLoadRps: 当前生效的全量导入Rps，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为50000000	
        :type CurrentLoadRps: int
        :param _DefaultLoadRps: 默认的全量导入Rps，该字段仅在出参有意义	
        :type DefaultLoadRps: int
        :param _CurrentSinkerThread: 当前生效的增量导入线程数，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为128
        :type CurrentSinkerThread: int
        :param _DefaultSinkerThread: 默认的增量导入线程数，该字段仅在出参有意义
        :type DefaultSinkerThread: int
        :param _HasUserSetRateLimit: enum:"no"/"yes"、no表示用户未设置过限速、yes表示设置过限速，该字段仅在出参有意义
        :type HasUserSetRateLimit: str
        """
        self._CurrentDumpThread = None
        self._DefaultDumpThread = None
        self._CurrentDumpRps = None
        self._DefaultDumpRps = None
        self._CurrentLoadThread = None
        self._DefaultLoadThread = None
        self._CurrentLoadRps = None
        self._DefaultLoadRps = None
        self._CurrentSinkerThread = None
        self._DefaultSinkerThread = None
        self._HasUserSetRateLimit = None

    @property
    def CurrentDumpThread(self):
        """当前生效的全量导出线程数，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为16
        :rtype: int
        """
        return self._CurrentDumpThread

    @CurrentDumpThread.setter
    def CurrentDumpThread(self, CurrentDumpThread):
        self._CurrentDumpThread = CurrentDumpThread

    @property
    def DefaultDumpThread(self):
        """默认的全量导出线程数，该字段仅在出参有意义
        :rtype: int
        """
        return self._DefaultDumpThread

    @DefaultDumpThread.setter
    def DefaultDumpThread(self, DefaultDumpThread):
        self._DefaultDumpThread = DefaultDumpThread

    @property
    def CurrentDumpRps(self):
        """当前生效的全量导出Rps，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为50000000
        :rtype: int
        """
        return self._CurrentDumpRps

    @CurrentDumpRps.setter
    def CurrentDumpRps(self, CurrentDumpRps):
        self._CurrentDumpRps = CurrentDumpRps

    @property
    def DefaultDumpRps(self):
        """默认的全量导出Rps，该字段仅在出参有意义
        :rtype: int
        """
        return self._DefaultDumpRps

    @DefaultDumpRps.setter
    def DefaultDumpRps(self, DefaultDumpRps):
        self._DefaultDumpRps = DefaultDumpRps

    @property
    def CurrentLoadThread(self):
        """当前生效的全量导入线程数，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为16
        :rtype: int
        """
        return self._CurrentLoadThread

    @CurrentLoadThread.setter
    def CurrentLoadThread(self, CurrentLoadThread):
        self._CurrentLoadThread = CurrentLoadThread

    @property
    def DefaultLoadThread(self):
        """默认的全量导入线程数，该字段仅在出参有意义
        :rtype: int
        """
        return self._DefaultLoadThread

    @DefaultLoadThread.setter
    def DefaultLoadThread(self, DefaultLoadThread):
        self._DefaultLoadThread = DefaultLoadThread

    @property
    def CurrentLoadRps(self):
        """当前生效的全量导入Rps，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为50000000	
        :rtype: int
        """
        return self._CurrentLoadRps

    @CurrentLoadRps.setter
    def CurrentLoadRps(self, CurrentLoadRps):
        self._CurrentLoadRps = CurrentLoadRps

    @property
    def DefaultLoadRps(self):
        """默认的全量导入Rps，该字段仅在出参有意义	
        :rtype: int
        """
        return self._DefaultLoadRps

    @DefaultLoadRps.setter
    def DefaultLoadRps(self, DefaultLoadRps):
        self._DefaultLoadRps = DefaultLoadRps

    @property
    def CurrentSinkerThread(self):
        """当前生效的增量导入线程数，配置任务时可调整该字段值，注意：如果不设置或设置为0则表示保持当前值，最大值为128
        :rtype: int
        """
        return self._CurrentSinkerThread

    @CurrentSinkerThread.setter
    def CurrentSinkerThread(self, CurrentSinkerThread):
        self._CurrentSinkerThread = CurrentSinkerThread

    @property
    def DefaultSinkerThread(self):
        """默认的增量导入线程数，该字段仅在出参有意义
        :rtype: int
        """
        return self._DefaultSinkerThread

    @DefaultSinkerThread.setter
    def DefaultSinkerThread(self, DefaultSinkerThread):
        self._DefaultSinkerThread = DefaultSinkerThread

    @property
    def HasUserSetRateLimit(self):
        """enum:"no"/"yes"、no表示用户未设置过限速、yes表示设置过限速，该字段仅在出参有意义
        :rtype: str
        """
        return self._HasUserSetRateLimit

    @HasUserSetRateLimit.setter
    def HasUserSetRateLimit(self, HasUserSetRateLimit):
        self._HasUserSetRateLimit = HasUserSetRateLimit


    def _deserialize(self, params):
        self._CurrentDumpThread = params.get("CurrentDumpThread")
        self._DefaultDumpThread = params.get("DefaultDumpThread")
        self._CurrentDumpRps = params.get("CurrentDumpRps")
        self._DefaultDumpRps = params.get("DefaultDumpRps")
        self._CurrentLoadThread = params.get("CurrentLoadThread")
        self._DefaultLoadThread = params.get("DefaultLoadThread")
        self._CurrentLoadRps = params.get("CurrentLoadRps")
        self._DefaultLoadRps = params.get("DefaultLoadRps")
        self._CurrentSinkerThread = params.get("CurrentSinkerThread")
        self._DefaultSinkerThread = params.get("DefaultSinkerThread")
        self._HasUserSetRateLimit = params.get("HasUserSetRateLimit")
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
        """任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步实例id（即标识一个同步作业），形如sync-werwfs23
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetConsumerGroupOffsetRequest(AbstractModel):
    """ResetConsumerGroupOffset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例id
        :type SubscribeId: str
        :param _TopicName: 订阅的kafka topic
        :type TopicName: str
        :param _ConsumerGroupName: 消费组名称。实际的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}
        :type ConsumerGroupName: str
        :param _PartitionNos: 需要修改offset的分区编号
        :type PartitionNos: list of int
        :param _ResetMode: 重置方式。枚举值为 earliest-从最开始位置开始消费；latest-从最新位置开始消费；datetime-从指定时间前最近的checkpoint开始消费
        :type ResetMode: str
        :param _ResetDatetime: 当 ResetMode 为 datetime 时，该项需要填，格式为：Y-m-d h:m:s。如果不填，默认用0时间，效果与earliest相同。
        :type ResetDatetime: str
        """
        self._SubscribeId = None
        self._TopicName = None
        self._ConsumerGroupName = None
        self._PartitionNos = None
        self._ResetMode = None
        self._ResetDatetime = None

    @property
    def SubscribeId(self):
        """订阅实例id
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def TopicName(self):
        """订阅的kafka topic
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ConsumerGroupName(self):
        """消费组名称。实际的消费组全称形如：consumer-grp-#{SubscribeId}-#{ConsumerGroupName}
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def PartitionNos(self):
        """需要修改offset的分区编号
        :rtype: list of int
        """
        return self._PartitionNos

    @PartitionNos.setter
    def PartitionNos(self, PartitionNos):
        self._PartitionNos = PartitionNos

    @property
    def ResetMode(self):
        """重置方式。枚举值为 earliest-从最开始位置开始消费；latest-从最新位置开始消费；datetime-从指定时间前最近的checkpoint开始消费
        :rtype: str
        """
        return self._ResetMode

    @ResetMode.setter
    def ResetMode(self, ResetMode):
        self._ResetMode = ResetMode

    @property
    def ResetDatetime(self):
        """当 ResetMode 为 datetime 时，该项需要填，格式为：Y-m-d h:m:s。如果不填，默认用0时间，效果与earliest相同。
        :rtype: str
        """
        return self._ResetDatetime

    @ResetDatetime.setter
    def ResetDatetime(self, ResetDatetime):
        self._ResetDatetime = ResetDatetime


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._TopicName = params.get("TopicName")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._PartitionNos = params.get("PartitionNos")
        self._ResetMode = params.get("ResetMode")
        self._ResetDatetime = params.get("ResetDatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetConsumerGroupOffsetResponse(AbstractModel):
    """ResetConsumerGroupOffset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetSubscribeRequest(AbstractModel):
    """ResetSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetSubscribeResponse(AbstractModel):
    """ResetSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NewInstanceClass(self):
        """任务规格
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ResumeOption(self):
        """恢复任务的模式，目前的取值有：clearData 清空目标实例数据，overwrite 以覆盖写的方式执行任务，normal 跟正常流程一样，不做额外动作；注意，clearData、overwrite仅对redis生效，normal仅针对非redis链路生效
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResumeSubscribeRequest(AbstractModel):
    """ResumeSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeSubscribeResponse(AbstractModel):
    """ResumeSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type RoleName: str
        :param _NewRoleName: 迁移后的角色名称
        :type NewRoleName: str
        """
        self._RoleName = None
        self._NewRoleName = None

    @property
    def RoleName(self):
        """角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def NewRoleName(self):
        """迁移后的角色名称
        :rtype: str
        """
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
        


class RowsCountDifference(AbstractModel):
    """mongodb行校验不一致详细信息

    """

    def __init__(self):
        r"""
        :param _Db: 数据库名
        :type Db: str
        :param _Table: 集合
        :type Table: str
        :param _SrcCount: 源端行数
        :type SrcCount: int
        :param _DstCount: 目标端行数
        :type DstCount: int
        """
        self._Db = None
        self._Table = None
        self._SrcCount = None
        self._DstCount = None

    @property
    def Db(self):
        """数据库名
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        """集合
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def SrcCount(self):
        """源端行数
        :rtype: int
        """
        return self._SrcCount

    @SrcCount.setter
    def SrcCount(self, SrcCount):
        self._SrcCount = SrcCount

    @property
    def DstCount(self):
        """目标端行数
        :rtype: int
        """
        return self._DstCount

    @DstCount.setter
    def DstCount(self, DstCount):
        self._DstCount = DstCount


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Table = params.get("Table")
        self._SrcCount = params.get("SrcCount")
        self._DstCount = params.get("DstCount")
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
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StepIds(self):
        """需要跳过校验项的步骤id，需要通过DescribeMigrationCheckJob接口返回StepInfo[i].StepId字段获取，例如：["OptimizeCheck"]
        :rtype: list of str
        """
        return self._StepIds

    @StepIds.setter
    def StepIds(self, StepIds):
        self._StepIds = StepIds

    @property
    def ForeignKeyFlag(self):
        """当出现外键依赖检查导致校验不通过时、可以通过该字段选择是否迁移外键依赖，当StepIds包含ConstraintCheck且该字段值为shield时表示不迁移外键依赖、当StepIds包含ConstraintCheck且值为migrate时表示迁移外键依赖
        :rtype: str
        """
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
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        """跳过的提示信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """任务id，如：sync-4ddgid2
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StepIds(self):
        """需要跳过校验项的步骤id，需要通过`DescribeCheckSyncJobResult`接口返回StepInfos[i].StepId字段获取，例如：["OptimizeCheck"]
        :rtype: list of str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type TotalCount: int
        :param _Items: 跳过校验的表详情
        :type Items: list of SkippedItem
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        """跳过的表数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """跳过校验的表详情
        :rtype: list of SkippedItem
        """
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
        :type Db: str
        :param _Table: 表名
        :type Table: str
        :param _Reason: 未发起检查的原因
        :type Reason: str
        """
        self._Db = None
        self._Table = None
        self._Reason = None

    @property
    def Db(self):
        """数据库名
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        """表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Reason(self):
        """未发起检查的原因
        :rtype: str
        """
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
        """迁移任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """数据迁移任务ID
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartSubscribeRequest(AbstractModel):
    """StartSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的 ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的 ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSubscribeResponse(AbstractModel):
    """StartSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type StepNo: int
        :param _StepName: 步骤展现名称
        :type StepName: str
        :param _StepId: 步骤英文标识
        :type StepId: str
        :param _Status: 步骤状态:success(成功)、failed(失败)、running(执行中)、notStarted(未执行)、默认为notStarted
        :type Status: str
        :param _StartTime: 当前步骤开始的时间，格式为"yyyy-mm-dd hh:mm:ss"，该字段不存在或者为空是无意义 注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _StepMessage: 步骤错误信息
        :type StepMessage: str
        :param _Percent: 执行进度
        :type Percent: int
        :param _Errors: 错误信息
        :type Errors: list of ProcessStepTip
        :param _Warnings: 告警提示
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
        """步骤序列
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        """步骤展现名称
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        """步骤英文标识
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        """步骤状态:success(成功)、failed(失败)、running(执行中)、notStarted(未执行)、默认为notStarted
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        """当前步骤开始的时间，格式为"yyyy-mm-dd hh:mm:ss"，该字段不存在或者为空是无意义 注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StepMessage(self):
        """步骤错误信息
        :rtype: str
        """
        return self._StepMessage

    @StepMessage.setter
    def StepMessage(self, StepMessage):
        self._StepMessage = StepMessage

    @property
    def Percent(self):
        """执行进度
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Errors(self):
        """错误信息
        :rtype: list of ProcessStepTip
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Warnings(self):
        """告警提示
        :rtype: list of ProcessStepTip
        """
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
        :type StepNo: int
        :param _StepName: 步骤名
        :type StepName: str
        :param _StepId: 步骤标号
        :type StepId: str
        :param _Status: 当前步骤状态,可能返回有 notStarted(未开始)、running(校验中)、failed(校验任务失败)、finished(完成)、skipped(跳过)、paused(暂停)
        :type Status: str
        :param _StartTime: 步骤开始时间，可能为空
        :type StartTime: str
        :param _Errors: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of StepTip
        :param _Warnings: 警告信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Warnings: list of StepTip
        :param _Progress: 当前步骤进度，范围为[0-100]，若为-1表示当前步骤不支持查看进度
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
        """步骤编号
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        """步骤名
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        """步骤标号
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        """当前步骤状态,可能返回有 notStarted(未开始)、running(校验中)、failed(校验任务失败)、finished(完成)、skipped(跳过)、paused(暂停)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        """步骤开始时间，可能为空
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Errors(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StepTip
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Warnings(self):
        """警告信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StepTip
        """
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings

    @property
    def Progress(self):
        """当前步骤进度，范围为[0-100]，若为-1表示当前步骤不支持查看进度
        :rtype: int
        """
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
        :type Code: str
        :param _Message: 错误信息
        :type Message: str
        :param _Solution: 解决方式
        :type Solution: str
        :param _HelpDoc: 帮助文档
        :type HelpDoc: str
        :param _SkipInfo: 当前步骤跳过信息
        :type SkipInfo: str
        """
        self._Code = None
        self._Message = None
        self._Solution = None
        self._HelpDoc = None
        self._SkipInfo = None

    @property
    def Code(self):
        """错误码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Solution(self):
        """解决方式
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def HelpDoc(self):
        """帮助文档
        :rtype: str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc

    @property
    def SkipInfo(self):
        """当前步骤跳过信息
        :rtype: str
        """
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
        :param _ForceStop: 是否强制停止。如果填true，同步任务增量阶段会跳过一致性校验产生的binlog，达到快速恢复任务的效果
        :type ForceStop: bool
        """
        self._JobId = None
        self._CompareTaskId = None
        self._ForceStop = None

    @property
    def JobId(self):
        """迁移任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def ForceStop(self):
        """是否强制停止。如果填true，同步任务增量阶段会跳过一致性校验产生的binlog，达到快速恢复任务的效果
        :rtype: bool
        """
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._ForceStop = params.get("ForceStop")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """数据迁移任务ID
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """同步任务id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SubsErr(AbstractModel):
    """订阅报错信息

    """

    def __init__(self):
        r"""
        :param _Message: 报错信息
        :type Message: str
        :param _Reason: 报错原因
        :type Reason: str
        :param _Solution: 建议的修复方案
        :type Solution: str
        """
        self._Message = None
        self._Reason = None
        self._Solution = None

    @property
    def Message(self):
        """报错信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Reason(self):
        """报错原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Solution(self):
        """建议的修复方案
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Reason = params.get("Reason")
        self._Solution = params.get("Solution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeCheckStepInfo(AbstractModel):
    """订阅校验任务的各步骤信息。

    """

    def __init__(self):
        r"""
        :param _StepName: 步骤名称
        :type StepName: str
        :param _StepId: 步骤Id
        :type StepId: str
        :param _StepNo: 步骤编号，从 1 开始
        :type StepNo: int
        :param _Status: 当前步骤状态，可能值为 notStarted,running,finished,failed
        :type Status: str
        :param _Percent: 当前步骤进度
        :type Percent: int
        :param _Errors: 错误提示
        :type Errors: list of SubscribeCheckStepTip
        :param _Warnings: 告警提示
        :type Warnings: list of SubscribeCheckStepTip
        """
        self._StepName = None
        self._StepId = None
        self._StepNo = None
        self._Status = None
        self._Percent = None
        self._Errors = None
        self._Warnings = None

    @property
    def StepName(self):
        """步骤名称
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        """步骤Id
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def StepNo(self):
        """步骤编号，从 1 开始
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def Status(self):
        """当前步骤状态，可能值为 notStarted,running,finished,failed
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        """当前步骤进度
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Errors(self):
        """错误提示
        :rtype: list of SubscribeCheckStepTip
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Warnings(self):
        """告警提示
        :rtype: list of SubscribeCheckStepTip
        """
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings


    def _deserialize(self, params):
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._StepNo = params.get("StepNo")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SubscribeCheckStepTip()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("Warnings") is not None:
            self._Warnings = []
            for item in params.get("Warnings"):
                obj = SubscribeCheckStepTip()
                obj._deserialize(item)
                self._Warnings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeCheckStepTip(AbstractModel):
    """订阅校验任务的提示信息

    """

    def __init__(self):
        r"""
        :param _Message: 错误或告警的详细信息
        :type Message: str
        :param _HelpDoc: 帮助文档
        :type HelpDoc: str
        """
        self._Message = None
        self._HelpDoc = None

    @property
    def Message(self):
        """错误或告警的详细信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def HelpDoc(self):
        """帮助文档
        :rtype: str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeInfo(AbstractModel):
    """订阅实例信息

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅的实例ID
        :type SubscribeId: str
        :param _SubscribeName: 数据订阅实例的名称
        :type SubscribeName: str
        :param _Topic: 订阅实例发送数据的kafka topic
        :type Topic: str
        :param _Product: 订阅实例的类型，目前支持 cynosdbmysql,mariadb,mongodb,mysql,percona,tdpg,tdsqlpercona(tdsqlmysql)
        :type Product: str
        :param _InstanceId: 订阅的数据库实例ID（如果订阅的是云数据库）如果实例不是腾讯云上的，此值为空。
        :type InstanceId: str
        :param _InstanceStatus: 云数据库状态：running 运行中，isolated 已隔离，offline 已下线。如果不是云上，此值为空
        :type InstanceStatus: str
        :param _Status: 数据订阅生命周期状态，可能的值为：正常 normal, 隔离中 isolating, 已隔离 isolated, 下线中 offlining, 按量转包年包月中 post2PrePayIng
        :type Status: str
        :param _SubsStatus: 数据订阅状态，可能的值为：未启动 notStarted, 校验中 checking, 校验不通过 checkNotPass, 校验通过 checkPass, 启动中 starting, 运行中 running, 异常出错 error
        :type SubsStatus: str
        :param _ModifyTime: 上次修改时间，时间格式如：Y-m-d h:m:s
        :type ModifyTime: str
        :param _CreateTime: 创建时间，时间格式如：Y-m-d h:m:s
        :type CreateTime: str
        :param _IsolateTime: 隔离时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :type IsolateTime: str
        :param _ExpireTime: 包年包月任务的到期时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :type ExpireTime: str
        :param _OfflineTime: 下线时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :type OfflineTime: str
        :param _PayType: 计费方式，0 - 包年包月，1 - 按量计费
        :type PayType: int
        :param _AutoRenewFlag: 自动续费标识。只有当 PayType=0，该值才有意义。枚举值：0-不自动续费，1-自动续费
        :type AutoRenewFlag: int
        :param _Region: 数据订阅实例所属地域
        :type Region: str
        :param _AccessType: 接入方式。枚举值：extranet(公网) vpncloud(vpn接入) dcg(专线接入) ccn(云联网) cdb(云数据库) cvm(云主机自建) intranet(自研上云) vpc(私有网络vpc)
        :type AccessType: str
        :param _Endpoints: 数据库节点信息
        :type Endpoints: list of EndpointItem
        :param _SubscribeVersion: 数据订阅版本, 当前只支持 kafka 版本。
        :type SubscribeVersion: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param _Errors: 任务报错信息，如果有的话。
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of SubsErr
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._Topic = None
        self._Product = None
        self._InstanceId = None
        self._InstanceStatus = None
        self._Status = None
        self._SubsStatus = None
        self._ModifyTime = None
        self._CreateTime = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._PayType = None
        self._AutoRenewFlag = None
        self._Region = None
        self._AccessType = None
        self._Endpoints = None
        self._SubscribeVersion = None
        self._Tags = None
        self._Errors = None

    @property
    def SubscribeId(self):
        """数据订阅的实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """数据订阅实例的名称
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def Topic(self):
        """订阅实例发送数据的kafka topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Product(self):
        """订阅实例的类型，目前支持 cynosdbmysql,mariadb,mongodb,mysql,percona,tdpg,tdsqlpercona(tdsqlmysql)
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """订阅的数据库实例ID（如果订阅的是云数据库）如果实例不是腾讯云上的，此值为空。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """云数据库状态：running 运行中，isolated 已隔离，offline 已下线。如果不是云上，此值为空
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def Status(self):
        """数据订阅生命周期状态，可能的值为：正常 normal, 隔离中 isolating, 已隔离 isolated, 下线中 offlining, 按量转包年包月中 post2PrePayIng
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubsStatus(self):
        """数据订阅状态，可能的值为：未启动 notStarted, 校验中 checking, 校验不通过 checkNotPass, 校验通过 checkPass, 启动中 starting, 运行中 running, 异常出错 error
        :rtype: str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def ModifyTime(self):
        """上次修改时间，时间格式如：Y-m-d h:m:s
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        """创建时间，时间格式如：Y-m-d h:m:s
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsolateTime(self):
        """隔离时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        """包年包月任务的到期时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        """下线时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def PayType(self):
        """计费方式，0 - 包年包月，1 - 按量计费
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def AutoRenewFlag(self):
        """自动续费标识。只有当 PayType=0，该值才有意义。枚举值：0-不自动续费，1-自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Region(self):
        """数据订阅实例所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccessType(self):
        """接入方式。枚举值：extranet(公网) vpncloud(vpn接入) dcg(专线接入) ccn(云联网) cdb(云数据库) cvm(云主机自建) intranet(自研上云) vpc(私有网络vpc)
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Endpoints(self):
        """数据库节点信息
        :rtype: list of EndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def SubscribeVersion(self):
        """数据订阅版本, 当前只支持 kafka 版本。
        :rtype: str
        """
        return self._SubscribeVersion

    @SubscribeVersion.setter
    def SubscribeVersion(self, SubscribeVersion):
        self._SubscribeVersion = SubscribeVersion

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Errors(self):
        """任务报错信息，如果有的话。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SubsErr
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._Topic = params.get("Topic")
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._Status = params.get("Status")
        self._SubsStatus = params.get("SubsStatus")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._PayType = params.get("PayType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Region = params.get("Region")
        self._AccessType = params.get("AccessType")
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = EndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        self._SubscribeVersion = params.get("SubscribeVersion")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SubsErr()
                obj._deserialize(item)
                self._Errors.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeKafkaConfig(AbstractModel):
    """订阅的kafka分区数和分区规则。mariadb，percona，tdsqlmysql，tdpg不支持自定义分区，所以DistributeRules和DefaultRuleType可以不填，但是NumberOfPartitions是必填。

    """

    def __init__(self):
        r"""
        :param _NumberOfPartitions: kafka分区数量，枚举值为1，4，8
        :type NumberOfPartitions: int
        :param _DistributeRules: 分区规则。当NumberOfPartitions > 1时，该项必填。
        :type DistributeRules: list of DistributeRule
        :param _DefaultRuleType: 默认分区策略。当NumberOfPartitions > 1时，该项必填。不满足DistributeRules中正则表达式的数据，将按照默认分区策略计算分区。
非mongo产品的枚举值为: table-按表名分区，pk-按表名+主键分区。mongo的枚举值为：collection-按集合名分区。
该字段与DistributeRules搭配使用，如果配置了该字段，视为配置了一条DistributeRules。
        :type DefaultRuleType: str
        """
        self._NumberOfPartitions = None
        self._DistributeRules = None
        self._DefaultRuleType = None

    @property
    def NumberOfPartitions(self):
        """kafka分区数量，枚举值为1，4，8
        :rtype: int
        """
        return self._NumberOfPartitions

    @NumberOfPartitions.setter
    def NumberOfPartitions(self, NumberOfPartitions):
        self._NumberOfPartitions = NumberOfPartitions

    @property
    def DistributeRules(self):
        """分区规则。当NumberOfPartitions > 1时，该项必填。
        :rtype: list of DistributeRule
        """
        return self._DistributeRules

    @DistributeRules.setter
    def DistributeRules(self, DistributeRules):
        self._DistributeRules = DistributeRules

    @property
    def DefaultRuleType(self):
        """默认分区策略。当NumberOfPartitions > 1时，该项必填。不满足DistributeRules中正则表达式的数据，将按照默认分区策略计算分区。
非mongo产品的枚举值为: table-按表名分区，pk-按表名+主键分区。mongo的枚举值为：collection-按集合名分区。
该字段与DistributeRules搭配使用，如果配置了该字段，视为配置了一条DistributeRules。
        :rtype: str
        """
        return self._DefaultRuleType

    @DefaultRuleType.setter
    def DefaultRuleType(self, DefaultRuleType):
        self._DefaultRuleType = DefaultRuleType


    def _deserialize(self, params):
        self._NumberOfPartitions = params.get("NumberOfPartitions")
        if params.get("DistributeRules") is not None:
            self._DistributeRules = []
            for item in params.get("DistributeRules"):
                obj = DistributeRule()
                obj._deserialize(item)
                self._DistributeRules.append(obj)
        self._DefaultRuleType = params.get("DefaultRuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeObject(AbstractModel):
    """订阅的数据库表信息，用于配置和查询订阅任务接口。

    """

    def __init__(self):
        r"""
        :param _ObjectType: 订阅数据的类型，枚举值：database-数据库，table-数据库的表(如果 DatabaseType 为 mongodb，则表示集合)
        :type ObjectType: str
        :param _Database: 订阅的数据库名称
        :type Database: str
        :param _Tables: 订阅数据库中表的名称。如果 DatabaseType 为 mongodb，填集合名。mongodb只支持订阅单库或者单集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of str
        """
        self._ObjectType = None
        self._Database = None
        self._Tables = None

    @property
    def ObjectType(self):
        """订阅数据的类型，枚举值：database-数据库，table-数据库的表(如果 DatabaseType 为 mongodb，则表示集合)
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def Database(self):
        """订阅的数据库名称
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Tables(self):
        """订阅数据库中表的名称。如果 DatabaseType 为 mongodb，填集合名。mongodb只支持订阅单库或者单集合。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables


    def _deserialize(self, params):
        self._ObjectType = params.get("ObjectType")
        self._Database = params.get("Database")
        self._Tables = params.get("Tables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDBEndpointInfos(AbstractModel):
    """数据同步配置多节点数据库的节点信息。多节点数据库，如tdsqlmysql使用该结构；单节点数据库，如mysql使用Endpoint。

    """

    def __init__(self):
        r"""
        :param _Region: 数据库所在地域
        :type Region: str
        :param _AccessType: 实例网络接入类型，如：extranet(外网)、ipv6(公网ipv6)、cvm(云主机自建)、dcg(专线接入)、vpncloud(vpn接入的实例)、cdb(云数据库)、ccn(云联网)、intranet(自研上云)、vpc(私有网络)等，注意具体可选值依赖当前链路
        :type AccessType: str
        :param _DatabaseType: 实例数据库类型，如：mysql,redis,mongodb,postgresql,mariadb,percona 等
        :type DatabaseType: str
        :param _Info: 数据库信息。注意：如果数据库类型为tdsqlmysql，此处Endpoint数组的顺序应满足规则：proxy节点放在set节点之前。如果SrcConnectType选择proxy接入则只需要填写proxy节点即可。如果选择set接入，数组中第一个set节点必须是shardkey范围起始为0的分片
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: list of Endpoint
        """
        self._Region = None
        self._AccessType = None
        self._DatabaseType = None
        self._Info = None

    @property
    def Region(self):
        """数据库所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccessType(self):
        """实例网络接入类型，如：extranet(外网)、ipv6(公网ipv6)、cvm(云主机自建)、dcg(专线接入)、vpncloud(vpn接入的实例)、cdb(云数据库)、ccn(云联网)、intranet(自研上云)、vpc(私有网络)等，注意具体可选值依赖当前链路
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def DatabaseType(self):
        """实例数据库类型，如：mysql,redis,mongodb,postgresql,mariadb,percona 等
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def Info(self):
        """数据库信息。注意：如果数据库类型为tdsqlmysql，此处Endpoint数组的顺序应满足规则：proxy节点放在set节点之前。如果SrcConnectType选择proxy接入则只需要填写proxy节点即可。如果选择set接入，数组中第一个set节点必须是shardkey范围起始为0的分片
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Endpoint
        """
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
        :type StepAll: int
        :param _StepNow: 当前步骤
        :type StepNow: int
        :param _Progress: 总体进度
        :type Progress: int
        :param _CurrentStepProgress: 当前步骤进度，范围为[0-100]，若为-1表示当前步骤不支持查看进度
        :type CurrentStepProgress: int
        :param _MasterSlaveDistance: 同步两端数据量差距
        :type MasterSlaveDistance: int
        :param _SecondsBehindMaster: 同步两端时间差距
        :type SecondsBehindMaster: int
        :param _Message: 总体描述信息
        :type Message: str
        :param _StepInfos: 详细步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfos: list of StepInfo
        :param _CauseOfCompareDisable: 不能发起一致性校验的原因
        :type CauseOfCompareDisable: str
        :param _ErrInfo: 任务的错误和解决方案信息
        :type ErrInfo: :class:`tencentcloud.dts.v20211206.models.ErrInfo`
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
        self._ErrInfo = None

    @property
    def StepAll(self):
        """总步骤数
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """当前步骤
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Progress(self):
        """总体进度
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CurrentStepProgress(self):
        """当前步骤进度，范围为[0-100]，若为-1表示当前步骤不支持查看进度
        :rtype: int
        """
        return self._CurrentStepProgress

    @CurrentStepProgress.setter
    def CurrentStepProgress(self, CurrentStepProgress):
        self._CurrentStepProgress = CurrentStepProgress

    @property
    def MasterSlaveDistance(self):
        """同步两端数据量差距
        :rtype: int
        """
        return self._MasterSlaveDistance

    @MasterSlaveDistance.setter
    def MasterSlaveDistance(self, MasterSlaveDistance):
        self._MasterSlaveDistance = MasterSlaveDistance

    @property
    def SecondsBehindMaster(self):
        """同步两端时间差距
        :rtype: int
        """
        return self._SecondsBehindMaster

    @SecondsBehindMaster.setter
    def SecondsBehindMaster(self, SecondsBehindMaster):
        self._SecondsBehindMaster = SecondsBehindMaster

    @property
    def Message(self):
        """总体描述信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def StepInfos(self):
        """详细步骤信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StepInfo
        """
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def CauseOfCompareDisable(self):
        """不能发起一致性校验的原因
        :rtype: str
        """
        return self._CauseOfCompareDisable

    @CauseOfCompareDisable.setter
    def CauseOfCompareDisable(self, CauseOfCompareDisable):
        self._CauseOfCompareDisable = CauseOfCompareDisable

    @property
    def ErrInfo(self):
        """任务的错误和解决方案信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.ErrInfo`
        """
        return self._ErrInfo

    @ErrInfo.setter
    def ErrInfo(self, ErrInfo):
        self._ErrInfo = ErrInfo


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
        if params.get("ErrInfo") is not None:
            self._ErrInfo = ErrInfo()
            self._ErrInfo._deserialize(params.get("ErrInfo"))
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
        :type JobId: str
        :param _JobName: 同步任务名
        :type JobName: str
        :param _PayMode: 付款方式，PostPay(按量付费)、PrePay(包年包月)
        :type PayMode: str
        :param _RunMode: 运行模式，Immediate(表示立即运行，默认为此项值)、Timed(表示定时运行)
        :type RunMode: str
        :param _ExpectRunTime: 期待运行时间，格式为 yyyy-mm-dd hh:mm:ss
        :type ExpectRunTime: str
        :param _AllActions: 支持的所有操作
        :type AllActions: list of str
        :param _Actions: 当前状态能进行的操作
注意：此字段可能返回 null，表示取不到有效值。
        :type Actions: list of str
        :param _Options: 同步选项
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param _Objects: 同步库表对象
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param _Specification: 任务规格
        :type Specification: str
        :param _ExpireTime: 过期时间，格式为 yyyy-mm-dd hh:mm:ss
        :type ExpireTime: str
        :param _SrcRegion: 源端地域，如：ap-guangzhou等
        :type SrcRegion: str
        :param _SrcDatabaseType: 源端数据库类型，mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
        :type SrcDatabaseType: str
        :param _SrcAccessType: 源端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)
        :type SrcAccessType: str
        :param _SrcInfo: 源端信息，单节点数据库使用
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _SrcNodeType: 枚举值：cluster、single。源库为单节点数据库使用single，多节点使用cluster
        :type SrcNodeType: str
        :param _SrcInfos: 源端信息，多节点数据库使用
        :type SrcInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _DstRegion: 目标端地域，如：ap-guangzhou等
        :type DstRegion: str
        :param _DstDatabaseType: 目标端数据库类型，mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
        :type DstDatabaseType: str
        :param _DstAccessType: 目标端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)
        :type DstAccessType: str
        :param _DstInfo: 目标端信息，单节点数据库使用
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _DstNodeType: 枚举值：cluster、single。目标库为单节点数据库使用single，多节点使用cluster
        :type DstNodeType: str
        :param _DstInfos: 目标端信息，多节点数据库使用
        :type DstInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _CreateTime: 创建时间，格式为 yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _StartTime: 开始时间，格式为 yyyy-mm-dd hh:mm:ss
        :type StartTime: str
        :param _Status: 任务状态，UnInitialized(未初始化)、Initialized(已初始化)、Checking(校验中)、CheckPass(校验通过)、CheckNotPass(校验不通过)、ReadyRunning(准备运行)、Running(运行中)、Pausing(暂停中)、Paused(已暂停)、Stopping(停止中)、Stopped(已结束)、ResumableErr(任务错误)、Resuming(恢复中)、Failed(失败)、Released(已释放)、Resetting(重置中)、Unknown(未知)
        :type Status: str
        :param _EndTime: 结束时间，格式为 yyyy-mm-dd hh:mm:ss
        :type EndTime: str
        :param _Tags: 标签相关信息
        :type Tags: list of TagItem
        :param _Detail: 同步任务运行步骤信息
        :type Detail: :class:`tencentcloud.dts.v20211206.models.SyncDetailInfo`
        :param _TradeStatus: 用于计费的状态，可能取值有：Normal(正常状态)、Resizing(变配中)、Renewing(续费中)、Isolating(隔离中)、Isolated(已隔离)、Offlining(下线中)、Offlined(已下线)、NotBilled(未计费)、Recovering(解隔离)、PostPay2Prepaying(按量计费转包年包月中)、PrePay2Postpaying(包年包月转按量计费中)
        :type TradeStatus: str
        :param _InstanceClass: 同步链路规格，如micro,small,medium,large
        :type InstanceClass: str
        :param _AutoRenew: 自动续费标识，当PayMode值为PrePay则此项配置有意义，取值为：1（表示自动续费）、0（不自动续费）
        :type AutoRenew: int
        :param _OfflineTime: 下线时间，格式为 yyyy-mm-dd hh:mm:ss
        :type OfflineTime: str
        :param _OptObjStatus: 动态修改对象，修改任务的状态等
        :type OptObjStatus: str
        :param _AutoRetryTimeRangeMinutes: 自动重试时间段设置
        :type AutoRetryTimeRangeMinutes: int
        :param _DumperResumeCtrl: 全量导出可重入标识：enum::"yes"/"no"。yes表示当前任务可重入、no表示当前任务处于全量导出且不可重入阶段；如果在该值为no时重启任务导出流程不支持断点续传
        :type DumperResumeCtrl: str
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
        self._SrcNodeType = None
        self._SrcInfos = None
        self._DstRegion = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._DstInfo = None
        self._DstNodeType = None
        self._DstInfos = None
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
        self._OptObjStatus = None
        self._AutoRetryTimeRangeMinutes = None
        self._DumperResumeCtrl = None

    @property
    def JobId(self):
        """同步任务id，如：sync-btso140
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """同步任务名
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def PayMode(self):
        """付款方式，PostPay(按量付费)、PrePay(包年包月)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RunMode(self):
        """运行模式，Immediate(表示立即运行，默认为此项值)、Timed(表示定时运行)
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        """期待运行时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def AllActions(self):
        """支持的所有操作
        :rtype: list of str
        """
        return self._AllActions

    @AllActions.setter
    def AllActions(self, AllActions):
        self._AllActions = AllActions

    @property
    def Actions(self):
        """当前状态能进行的操作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Options(self):
        """同步选项
        :rtype: :class:`tencentcloud.dts.v20211206.models.Options`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Objects(self):
        """同步库表对象
        :rtype: :class:`tencentcloud.dts.v20211206.models.Objects`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Specification(self):
        """任务规格
        :rtype: str
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def ExpireTime(self):
        """过期时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SrcRegion(self):
        """源端地域，如：ap-guangzhou等
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def SrcDatabaseType(self):
        """源端数据库类型，mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
        :rtype: str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        """源端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)
        :rtype: str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        """源端信息，单节点数据库使用
        :rtype: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def SrcNodeType(self):
        """枚举值：cluster、single。源库为单节点数据库使用single，多节点使用cluster
        :rtype: str
        """
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def SrcInfos(self):
        """源端信息，多节点数据库使用
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        """
        return self._SrcInfos

    @SrcInfos.setter
    def SrcInfos(self, SrcInfos):
        self._SrcInfos = SrcInfos

    @property
    def DstRegion(self):
        """目标端地域，如：ap-guangzhou等
        :rtype: str
        """
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def DstDatabaseType(self):
        """目标端数据库类型，mysql,cynosdbmysql,tdapg,tdpg,tdsqlmysql等
        :rtype: str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        """目标端接入类型，cdb(云数据库)、cvm(云主机自建)、vpc(私有网络)、extranet(外网)、vpncloud(vpn接入)、dcg(专线接入)、ccn(云联网)、intranet(自研上云)
        :rtype: str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        """目标端信息，单节点数据库使用
        :rtype: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DstNodeType(self):
        """枚举值：cluster、single。目标库为单节点数据库使用single，多节点使用cluster
        :rtype: str
        """
        return self._DstNodeType

    @DstNodeType.setter
    def DstNodeType(self, DstNodeType):
        self._DstNodeType = DstNodeType

    @property
    def DstInfos(self):
        """目标端信息，多节点数据库使用
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        """
        return self._DstInfos

    @DstInfos.setter
    def DstInfos(self, DstInfos):
        self._DstInfos = DstInfos

    @property
    def CreateTime(self):
        """创建时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """开始时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        """任务状态，UnInitialized(未初始化)、Initialized(已初始化)、Checking(校验中)、CheckPass(校验通过)、CheckNotPass(校验不通过)、ReadyRunning(准备运行)、Running(运行中)、Pausing(暂停中)、Paused(已暂停)、Stopping(停止中)、Stopped(已结束)、ResumableErr(任务错误)、Resuming(恢复中)、Failed(失败)、Released(已释放)、Resetting(重置中)、Unknown(未知)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EndTime(self):
        """结束时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Tags(self):
        """标签相关信息
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Detail(self):
        """同步任务运行步骤信息
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDetailInfo`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def TradeStatus(self):
        """用于计费的状态，可能取值有：Normal(正常状态)、Resizing(变配中)、Renewing(续费中)、Isolating(隔离中)、Isolated(已隔离)、Offlining(下线中)、Offlined(已下线)、NotBilled(未计费)、Recovering(解隔离)、PostPay2Prepaying(按量计费转包年包月中)、PrePay2Postpaying(包年包月转按量计费中)
        :rtype: str
        """
        return self._TradeStatus

    @TradeStatus.setter
    def TradeStatus(self, TradeStatus):
        self._TradeStatus = TradeStatus

    @property
    def InstanceClass(self):
        """同步链路规格，如micro,small,medium,large
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def AutoRenew(self):
        """自动续费标识，当PayMode值为PrePay则此项配置有意义，取值为：1（表示自动续费）、0（不自动续费）
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def OfflineTime(self):
        """下线时间，格式为 yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def OptObjStatus(self):
        """动态修改对象，修改任务的状态等
        :rtype: str
        """
        return self._OptObjStatus

    @OptObjStatus.setter
    def OptObjStatus(self, OptObjStatus):
        self._OptObjStatus = OptObjStatus

    @property
    def AutoRetryTimeRangeMinutes(self):
        """自动重试时间段设置
        :rtype: int
        """
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes

    @property
    def DumperResumeCtrl(self):
        """全量导出可重入标识：enum::"yes"/"no"。yes表示当前任务可重入、no表示当前任务处于全量导出且不可重入阶段；如果在该值为no时重启任务导出流程不支持断点续传
        :rtype: str
        """
        return self._DumperResumeCtrl

    @DumperResumeCtrl.setter
    def DumperResumeCtrl(self, DumperResumeCtrl):
        self._DumperResumeCtrl = DumperResumeCtrl


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
        self._SrcNodeType = params.get("SrcNodeType")
        if params.get("SrcInfos") is not None:
            self._SrcInfos = SyncDBEndpointInfos()
            self._SrcInfos._deserialize(params.get("SrcInfos"))
        self._DstRegion = params.get("DstRegion")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = Endpoint()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._DstNodeType = params.get("DstNodeType")
        if params.get("DstInfos") is not None:
            self._DstInfos = SyncDBEndpointInfos()
            self._DstInfos._deserialize(params.get("DstInfos"))
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
        self._OptObjStatus = params.get("OptObjStatus")
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        self._DumperResumeCtrl = params.get("DumperResumeCtrl")
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
        :type TableName: str
        :param _NewTableName: 新表名
        :type NewTableName: str
        :param _FilterCondition: 过滤条件
        :type FilterCondition: str
        :param _ColumnMode: 是否同步表中所有列，All：当前表下的所有列,Partial(ModifySyncJobConfig接口里的对应字段ColumnMode暂不支持Partial)：当前表下的部分列，通过填充Columns字段详细表信息
        :type ColumnMode: str
        :param _Columns: 同步的列信息，当ColumnMode为Partial时，必填
        :type Columns: list of Column
        :param _TmpTables: 同步临时表，注意此配置与NewTableName互斥，只能使用其中一种。当配置的同步对象为表级别且TableEditMode为pt时此项有意义，针对pt-osc等工具在同步过程中产生的临时表进行同步，需要提前将可能的临时表配置在这里，否则不会同步任何临时表。示例，如要对t1进行pt-osc操作，此项配置应该为["\_t1\_new","\_t1\_old"]；如要对t1进行gh-ost操作，此项配置应该为["\_t1\_ghc","\_t1\_gho","\_t1\_del"]，pt-osc与gh-ost产生的临时表可同时配置。
        :type TmpTables: list of str
        :param _TableEditMode: 编辑表类型，rename(表映射)，pt(同步附加表)
        :type TableEditMode: str
        """
        self._TableName = None
        self._NewTableName = None
        self._FilterCondition = None
        self._ColumnMode = None
        self._Columns = None
        self._TmpTables = None
        self._TableEditMode = None

    @property
    def TableName(self):
        """表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        """新表名
        :rtype: str
        """
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName

    @property
    def FilterCondition(self):
        """过滤条件
        :rtype: str
        """
        return self._FilterCondition

    @FilterCondition.setter
    def FilterCondition(self, FilterCondition):
        self._FilterCondition = FilterCondition

    @property
    def ColumnMode(self):
        """是否同步表中所有列，All：当前表下的所有列,Partial(ModifySyncJobConfig接口里的对应字段ColumnMode暂不支持Partial)：当前表下的部分列，通过填充Columns字段详细表信息
        :rtype: str
        """
        return self._ColumnMode

    @ColumnMode.setter
    def ColumnMode(self, ColumnMode):
        self._ColumnMode = ColumnMode

    @property
    def Columns(self):
        """同步的列信息，当ColumnMode为Partial时，必填
        :rtype: list of Column
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def TmpTables(self):
        """同步临时表，注意此配置与NewTableName互斥，只能使用其中一种。当配置的同步对象为表级别且TableEditMode为pt时此项有意义，针对pt-osc等工具在同步过程中产生的临时表进行同步，需要提前将可能的临时表配置在这里，否则不会同步任何临时表。示例，如要对t1进行pt-osc操作，此项配置应该为["\_t1\_new","\_t1\_old"]；如要对t1进行gh-ost操作，此项配置应该为["\_t1\_ghc","\_t1\_gho","\_t1\_del"]，pt-osc与gh-ost产生的临时表可同时配置。
        :rtype: list of str
        """
        return self._TmpTables

    @TmpTables.setter
    def TmpTables(self, TmpTables):
        self._TmpTables = TmpTables

    @property
    def TableEditMode(self):
        """编辑表类型，rename(表映射)，pt(同步附加表)
        :rtype: str
        """
        return self._TableEditMode

    @TableEditMode.setter
    def TableEditMode(self, TableEditMode):
        self._TableEditMode = TableEditMode


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._NewTableName = params.get("NewTableName")
        self._FilterCondition = params.get("FilterCondition")
        self._ColumnMode = params.get("ColumnMode")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
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
        :type TableName: str
        :param _NewTableName: 迁移后的表名，当TableEditMode为rename时此项必填，注意此配置与TmpTables互斥，只能使用其中一种
        :type NewTableName: str
        :param _TmpTables: 迁移临时表，注意此配置与NewTableName互斥，只能使用其中一种。当配置的同步对象为表级别且TableEditMode为pt时此项有意义，针对pt-osc等工具在迁移过程中产生的临时表进行同步，需要提前将可能的临时表配置在这里，否则不会同步任何临时表。示例，如要对t1进行pt-osc操作，此项配置应该为["\_t1\_new","\_t1\_old"]；如要对t1进行gh-ost操作，此项配置应该为["\_t1\_ghc","\_t1\_gho","\_t1\_del"]，pt-osc与gh-ost产生的临时表可同时配置。
        :type TmpTables: list of str
        :param _TableEditMode: 编辑表类型，rename(表映射)，pt(同步附加表)
        :type TableEditMode: str
        """
        self._TableName = None
        self._NewTableName = None
        self._TmpTables = None
        self._TableEditMode = None

    @property
    def TableName(self):
        """迁移的表名，大小写敏感
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        """迁移后的表名，当TableEditMode为rename时此项必填，注意此配置与TmpTables互斥，只能使用其中一种
        :rtype: str
        """
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName

    @property
    def TmpTables(self):
        """迁移临时表，注意此配置与NewTableName互斥，只能使用其中一种。当配置的同步对象为表级别且TableEditMode为pt时此项有意义，针对pt-osc等工具在迁移过程中产生的临时表进行同步，需要提前将可能的临时表配置在这里，否则不会同步任何临时表。示例，如要对t1进行pt-osc操作，此项配置应该为["\_t1\_new","\_t1\_old"]；如要对t1进行gh-ost操作，此项配置应该为["\_t1\_ghc","\_t1\_gho","\_t1\_del"]，pt-osc与gh-ost产生的临时表可同时配置。
        :rtype: list of str
        """
        return self._TmpTables

    @TmpTables.setter
    def TmpTables(self, TmpTables):
        self._TmpTables = TmpTables

    @property
    def TableEditMode(self):
        """编辑表类型，rename(表映射)，pt(同步附加表)
        :rtype: str
        """
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
        """标签键值
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: list of str
        """
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
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
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
    """单topic和自定义topic的描述。投递到单topic时，该数组的最后一项会被视为默认分区策略，所有未匹配到的数据都会按该策略投递，默认策略只支持 投递至partition0、按表名、表名+主键三种。

    """

    def __init__(self):
        r"""
        :param _TopicName: topic名。单topic时，所有的TopicName必须相同
        :type TopicName: str
        :param _PartitionType: topic分区策略，自定义topic时支持：Random（随机投递），集中投递到单Topic时支持：AllInPartitionZero（全部投递至partition0）、PartitionByTable(按表名分区)、PartitionByTableAndKey(按表名加主键分区)、PartitionByCols(按列分区)
        :type PartitionType: str
        :param _DbMatchMode: 库名匹配规则，如Regular（正则匹配）, Default(不符合匹配规则的剩余库)，数组中最后一项必须为‘Default’
        :type DbMatchMode: str
        :param _DbName: 库名，DbMatchMode=Regular时生效
        :type DbName: str
        :param _TableMatchMode: 表名匹配规则，如Regular（正则匹配）, Default(不符合匹配规则的剩余表)，数组中最后一项必须为‘Default’
        :type TableMatchMode: str
        :param _TableName: 表名，仅TableMatchMode=Regular时生效
        :type TableName: str
        :param _Columns: 按列分区时需要选择配置列名，可以选择多列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of str
        """
        self._TopicName = None
        self._PartitionType = None
        self._DbMatchMode = None
        self._DbName = None
        self._TableMatchMode = None
        self._TableName = None
        self._Columns = None

    @property
    def TopicName(self):
        """topic名。单topic时，所有的TopicName必须相同
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionType(self):
        """topic分区策略，自定义topic时支持：Random（随机投递），集中投递到单Topic时支持：AllInPartitionZero（全部投递至partition0）、PartitionByTable(按表名分区)、PartitionByTableAndKey(按表名加主键分区)、PartitionByCols(按列分区)
        :rtype: str
        """
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def DbMatchMode(self):
        """库名匹配规则，如Regular（正则匹配）, Default(不符合匹配规则的剩余库)，数组中最后一项必须为‘Default’
        :rtype: str
        """
        return self._DbMatchMode

    @DbMatchMode.setter
    def DbMatchMode(self, DbMatchMode):
        self._DbMatchMode = DbMatchMode

    @property
    def DbName(self):
        """库名，DbMatchMode=Regular时生效
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableMatchMode(self):
        """表名匹配规则，如Regular（正则匹配）, Default(不符合匹配规则的剩余表)，数组中最后一项必须为‘Default’
        :rtype: str
        """
        return self._TableMatchMode

    @TableMatchMode.setter
    def TableMatchMode(self, TableMatchMode):
        self._TableMatchMode = TableMatchMode

    @property
    def TableName(self):
        """表名，仅TableMatchMode=Regular时生效
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Columns(self):
        """按列分区时需要选择配置列名，可以选择多列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._PartitionType = params.get("PartitionType")
        self._DbMatchMode = params.get("DbMatchMode")
        self._DbName = params.get("DbName")
        self._TableMatchMode = params.get("TableMatchMode")
        self._TableName = params.get("TableName")
        self._Columns = params.get("Columns")
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
        :type DealName: str
        :param _LastDealName: 上一次交易订单号
        :type LastDealName: str
        :param _InstanceClass: 实例规格，包括：micro、small、medium、large、xlarge、2xlarge等
        :type InstanceClass: str
        :param _TradeStatus: 计费任务状态， normal(计费或待计费)、resizing(变配中)、reversing(冲正中，比较短暂的状态)、isolating(隔离中，比较短暂的状态)、isolated(已隔离)、offlining(下线中)、offlined(已下线)、notBilled(未计费)
        :type TradeStatus: str
        :param _ExpireTime: 到期时间，格式为"yyyy-mm-dd hh:mm:ss"
        :type ExpireTime: str
        :param _OfflineTime: 下线时间，格式为"yyyy-mm-dd hh:mm:ss"
        :type OfflineTime: str
        :param _IsolateTime: 隔离时间，格式为"yyyy-mm-dd hh:mm:ss"
        :type IsolateTime: str
        :param _OfflineReason: 下线原因
        :type OfflineReason: str
        :param _IsolateReason: 隔离原因
        :type IsolateReason: str
        :param _PayType: 付费类型，包括：postpay(后付费)、prepay(预付费)
        :type PayType: str
        :param _BillingType: 任务计费类型，包括：billing(计费)、notBilling(不计费)、 promotions(促销活动中)
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
        """交易订单号
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def LastDealName(self):
        """上一次交易订单号
        :rtype: str
        """
        return self._LastDealName

    @LastDealName.setter
    def LastDealName(self, LastDealName):
        self._LastDealName = LastDealName

    @property
    def InstanceClass(self):
        """实例规格，包括：micro、small、medium、large、xlarge、2xlarge等
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def TradeStatus(self):
        """计费任务状态， normal(计费或待计费)、resizing(变配中)、reversing(冲正中，比较短暂的状态)、isolating(隔离中，比较短暂的状态)、isolated(已隔离)、offlining(下线中)、offlined(已下线)、notBilled(未计费)
        :rtype: str
        """
        return self._TradeStatus

    @TradeStatus.setter
    def TradeStatus(self, TradeStatus):
        self._TradeStatus = TradeStatus

    @property
    def ExpireTime(self):
        """到期时间，格式为"yyyy-mm-dd hh:mm:ss"
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        """下线时间，格式为"yyyy-mm-dd hh:mm:ss"
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def IsolateTime(self):
        """隔离时间，格式为"yyyy-mm-dd hh:mm:ss"
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def OfflineReason(self):
        """下线原因
        :rtype: str
        """
        return self._OfflineReason

    @OfflineReason.setter
    def OfflineReason(self, OfflineReason):
        self._OfflineReason = OfflineReason

    @property
    def IsolateReason(self):
        """隔离原因
        :rtype: str
        """
        return self._IsolateReason

    @IsolateReason.setter
    def IsolateReason(self, IsolateReason):
        self._IsolateReason = IsolateReason

    @property
    def PayType(self):
        """付费类型，包括：postpay(后付费)、prepay(预付费)
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def BillingType(self):
        """任务计费类型，包括：billing(计费)、notBilling(不计费)、 promotions(促销活动中)
        :rtype: str
        """
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
        :type ViewName: str
        :param _NewViewName: 预留字段、目前暂时不支持view的重命名
        :type NewViewName: str
        """
        self._ViewName = None
        self._NewViewName = None

    @property
    def ViewName(self):
        """view名
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def NewViewName(self):
        """预留字段、目前暂时不支持view的重命名
        :rtype: str
        """
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
        :type ViewName: str
        :param _NewViewName: 迁移后的视图名称
        :type NewViewName: str
        """
        self._ViewName = None
        self._NewViewName = None

    @property
    def ViewName(self):
        """视图名称
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def NewViewName(self):
        """迁移后的视图名称
        :rtype: str
        """
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
        