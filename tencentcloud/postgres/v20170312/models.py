# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AccountInfo(AbstractModel):
    r"""账户信息

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param _UserName: 账号
        :type UserName: str
        :param _Remark: 账号备注
        :type Remark: str
        :param _Status: 账号状态。 1-创建中，2-正常，3-修改中，4-密码重置中，5-锁定中，-1-删除中
        :type Status: int
        :param _CreateTime: 账号创建时间
        :type CreateTime: str
        :param _UpdateTime: 账号最后一次更新时间
        :type UpdateTime: str
        :param _PasswordUpdateTime: 账号密码最近一次修改时间。

此字段只在2025-10-31后才生效，之前无论是否修改密码，该值统一为默认值：0000-00-00 00:00:00
同时仅通过云API或者管控控制台修改密码，才会更新该字段。
        :type PasswordUpdateTime: str
        :param _UserType: 账号类型。支持normal、tencentDBSuper。normal指代普通用户，tencentDBSuper为拥有pg_tencentdb_superuser角色的账号。
        :type UserType: str
        :param _OpenCam: 用户账号是否启用CAM验证
        :type OpenCam: bool
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Remark = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._PasswordUpdateTime = None
        self._UserType = None
        self._OpenCam = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-lnp6j617
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""账号
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Remark(self):
        r"""账号备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        r"""账号状态。 1-创建中，2-正常，3-修改中，4-密码重置中，5-锁定中，-1-删除中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""账号创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""账号最后一次更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PasswordUpdateTime(self):
        r"""账号密码最近一次修改时间。

此字段只在2025-10-31后才生效，之前无论是否修改密码，该值统一为默认值：0000-00-00 00:00:00
同时仅通过云API或者管控控制台修改密码，才会更新该字段。
        :rtype: str
        """
        return self._PasswordUpdateTime

    @PasswordUpdateTime.setter
    def PasswordUpdateTime(self, PasswordUpdateTime):
        self._PasswordUpdateTime = PasswordUpdateTime

    @property
    def UserType(self):
        r"""账号类型。支持normal、tencentDBSuper。normal指代普通用户，tencentDBSuper为拥有pg_tencentdb_superuser角色的账号。
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def OpenCam(self):
        r"""用户账号是否启用CAM验证
        :rtype: bool
        """
        return self._OpenCam

    @OpenCam.setter
    def OpenCam(self, OpenCam):
        self._OpenCam = OpenCam


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._PasswordUpdateTime = params.get("PasswordUpdateTime")
        self._UserType = params.get("UserType")
        self._OpenCam = params.get("OpenCam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDBInstanceToReadOnlyGroupRequest(AbstractModel):
    r"""AddDBInstanceToReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: 只读组ID。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :type ReadOnlyGroupId: str
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDBInstanceToReadOnlyGroupResponse(AbstractModel):
    r"""AddDBInstanceToReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class AnalysisItems(AbstractModel):
    r"""慢查询分析接口返回的分析详情，按照参数抽象之后进行分类

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 慢SQL查询的数据库名
        :type DatabaseName: str
        :param _UserName: 慢SQL执行的用户名
        :type UserName: str
        :param _NormalQuery: 抽象参数之后的慢SQL
        :type NormalQuery: str
        :param _ClientAddr: 慢SQL执行的客户端地址
        :type ClientAddr: str
        :param _CallNum: 在选定时间范围内慢SQL语句执行的次数
        :type CallNum: int
        :param _CallPercent: 在选定时间范围内，慢SQL语句执行的次数占所有慢SQL的百分比。
        :type CallPercent: float
        :param _CostTime: 在选定时间范围内，慢SQL执行的总时间
        :type CostTime: float
        :param _CostPercent: 在选定时间范围内，慢SQL语句执行的总时间占所有慢SQL的比例（小数返回）
        :type CostPercent: float
        :param _MinCostTime: 在选定时间范围内，慢SQL语句执行的耗时最短的时间（单位：ms）
        :type MinCostTime: float
        :param _MaxCostTime: 在选定时间范围内，慢SQL语句执行的耗时最长的时间（单位：ms）
        :type MaxCostTime: float
        :param _AvgCostTime: 在选定时间范围内，慢SQL语句执行的耗时平均时间（单位：ms）
        :type AvgCostTime: float
        :param _FirstTime: 在选定时间范围内，慢SQL第一条开始执行的时间
        :type FirstTime: str
        :param _LastTime: 在选定时间范围内，慢SQL最后一条开始执行的时间
        :type LastTime: str
        """
        self._DatabaseName = None
        self._UserName = None
        self._NormalQuery = None
        self._ClientAddr = None
        self._CallNum = None
        self._CallPercent = None
        self._CostTime = None
        self._CostPercent = None
        self._MinCostTime = None
        self._MaxCostTime = None
        self._AvgCostTime = None
        self._FirstTime = None
        self._LastTime = None

    @property
    def DatabaseName(self):
        r"""慢SQL查询的数据库名
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def UserName(self):
        r"""慢SQL执行的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def NormalQuery(self):
        r"""抽象参数之后的慢SQL
        :rtype: str
        """
        return self._NormalQuery

    @NormalQuery.setter
    def NormalQuery(self, NormalQuery):
        self._NormalQuery = NormalQuery

    @property
    def ClientAddr(self):
        r"""慢SQL执行的客户端地址
        :rtype: str
        """
        return self._ClientAddr

    @ClientAddr.setter
    def ClientAddr(self, ClientAddr):
        self._ClientAddr = ClientAddr

    @property
    def CallNum(self):
        r"""在选定时间范围内慢SQL语句执行的次数
        :rtype: int
        """
        return self._CallNum

    @CallNum.setter
    def CallNum(self, CallNum):
        self._CallNum = CallNum

    @property
    def CallPercent(self):
        r"""在选定时间范围内，慢SQL语句执行的次数占所有慢SQL的百分比。
        :rtype: float
        """
        return self._CallPercent

    @CallPercent.setter
    def CallPercent(self, CallPercent):
        self._CallPercent = CallPercent

    @property
    def CostTime(self):
        r"""在选定时间范围内，慢SQL执行的总时间
        :rtype: float
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def CostPercent(self):
        r"""在选定时间范围内，慢SQL语句执行的总时间占所有慢SQL的比例（小数返回）
        :rtype: float
        """
        return self._CostPercent

    @CostPercent.setter
    def CostPercent(self, CostPercent):
        self._CostPercent = CostPercent

    @property
    def MinCostTime(self):
        r"""在选定时间范围内，慢SQL语句执行的耗时最短的时间（单位：ms）
        :rtype: float
        """
        return self._MinCostTime

    @MinCostTime.setter
    def MinCostTime(self, MinCostTime):
        self._MinCostTime = MinCostTime

    @property
    def MaxCostTime(self):
        r"""在选定时间范围内，慢SQL语句执行的耗时最长的时间（单位：ms）
        :rtype: float
        """
        return self._MaxCostTime

    @MaxCostTime.setter
    def MaxCostTime(self, MaxCostTime):
        self._MaxCostTime = MaxCostTime

    @property
    def AvgCostTime(self):
        r"""在选定时间范围内，慢SQL语句执行的耗时平均时间（单位：ms）
        :rtype: float
        """
        return self._AvgCostTime

    @AvgCostTime.setter
    def AvgCostTime(self, AvgCostTime):
        self._AvgCostTime = AvgCostTime

    @property
    def FirstTime(self):
        r"""在选定时间范围内，慢SQL第一条开始执行的时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def LastTime(self):
        r"""在选定时间范围内，慢SQL最后一条开始执行的时间
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._UserName = params.get("UserName")
        self._NormalQuery = params.get("NormalQuery")
        self._ClientAddr = params.get("ClientAddr")
        self._CallNum = params.get("CallNum")
        self._CallPercent = params.get("CallPercent")
        self._CostTime = params.get("CostTime")
        self._CostPercent = params.get("CostPercent")
        self._MinCostTime = params.get("MinCostTime")
        self._MaxCostTime = params.get("MaxCostTime")
        self._AvgCostTime = params.get("AvgCostTime")
        self._FirstTime = params.get("FirstTime")
        self._LastTime = params.get("LastTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadRestriction(AbstractModel):
    r"""备份下载限制信息

    """

    def __init__(self):
        r"""
        :param _RestrictionType: 备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。当该参数取值为CUSTOMIZE 时，vpc或ip信息至少填写一项
        :type RestrictionType: str
        :param _VpcRestrictionEffect: vpc限制效力，ALLOW 允许；DENY 拒绝。
        :type VpcRestrictionEffect: str
        :param _VpcIdSet: 允许或拒绝下载备份文件的vpcId列表。
        :type VpcIdSet: list of str
        :param _IpRestrictionEffect: ip限制效力，ALLOW 允许；DENY 拒绝。
        :type IpRestrictionEffect: str
        :param _IpSet: 允许或拒绝下载备份文件的ip列表。
        :type IpSet: list of str
        """
        self._RestrictionType = None
        self._VpcRestrictionEffect = None
        self._VpcIdSet = None
        self._IpRestrictionEffect = None
        self._IpSet = None

    @property
    def RestrictionType(self):
        r"""备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。当该参数取值为CUSTOMIZE 时，vpc或ip信息至少填写一项
        :rtype: str
        """
        return self._RestrictionType

    @RestrictionType.setter
    def RestrictionType(self, RestrictionType):
        self._RestrictionType = RestrictionType

    @property
    def VpcRestrictionEffect(self):
        r"""vpc限制效力，ALLOW 允许；DENY 拒绝。
        :rtype: str
        """
        return self._VpcRestrictionEffect

    @VpcRestrictionEffect.setter
    def VpcRestrictionEffect(self, VpcRestrictionEffect):
        self._VpcRestrictionEffect = VpcRestrictionEffect

    @property
    def VpcIdSet(self):
        r"""允许或拒绝下载备份文件的vpcId列表。
        :rtype: list of str
        """
        return self._VpcIdSet

    @VpcIdSet.setter
    def VpcIdSet(self, VpcIdSet):
        self._VpcIdSet = VpcIdSet

    @property
    def IpRestrictionEffect(self):
        r"""ip限制效力，ALLOW 允许；DENY 拒绝。
        :rtype: str
        """
        return self._IpRestrictionEffect

    @IpRestrictionEffect.setter
    def IpRestrictionEffect(self, IpRestrictionEffect):
        self._IpRestrictionEffect = IpRestrictionEffect

    @property
    def IpSet(self):
        r"""允许或拒绝下载备份文件的ip列表。
        :rtype: list of str
        """
        return self._IpSet

    @IpSet.setter
    def IpSet(self, IpSet):
        self._IpSet = IpSet


    def _deserialize(self, params):
        self._RestrictionType = params.get("RestrictionType")
        self._VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self._VpcIdSet = params.get("VpcIdSet")
        self._IpRestrictionEffect = params.get("IpRestrictionEffect")
        self._IpSet = params.get("IpSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPlan(AbstractModel):
    r"""备份计划

    """

    def __init__(self):
        r"""
        :param _BackupPeriod: 备份周期
        :type BackupPeriod: str
        :param _BaseBackupRetentionPeriod: 数据备份保留时长。单位：天
        :type BaseBackupRetentionPeriod: int
        :param _MinBackupStartTime: 开始备份的最早时间
        :type MinBackupStartTime: str
        :param _MaxBackupStartTime: 开始备份的最晚时间
        :type MaxBackupStartTime: str
        :param _PlanId: 备份计划ID
        :type PlanId: str
        :param _PlanName: 备份计划自定义名称。
        :type PlanName: str
        :param _LogBackupRetentionPeriod: 日志备份保留时长。单位：天
        :type LogBackupRetentionPeriod: int
        :param _CreatedTime: 创建时间。
        :type CreatedTime: str
        :param _UpdatedTime: 最近一次的修改时间。
        :type UpdatedTime: str
        :param _PlanType: 备份计划类型。系统默认创建的为default，自定义的为custom。
        :type PlanType: str
        :param _BackupPeriodType: 备份周期类型。当前支持week、month。
        :type BackupPeriodType: str
        """
        self._BackupPeriod = None
        self._BaseBackupRetentionPeriod = None
        self._MinBackupStartTime = None
        self._MaxBackupStartTime = None
        self._PlanId = None
        self._PlanName = None
        self._LogBackupRetentionPeriod = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._PlanType = None
        self._BackupPeriodType = None

    @property
    def BackupPeriod(self):
        r"""备份周期
        :rtype: str
        """
        return self._BackupPeriod

    @BackupPeriod.setter
    def BackupPeriod(self, BackupPeriod):
        self._BackupPeriod = BackupPeriod

    @property
    def BaseBackupRetentionPeriod(self):
        r"""数据备份保留时长。单位：天
        :rtype: int
        """
        return self._BaseBackupRetentionPeriod

    @BaseBackupRetentionPeriod.setter
    def BaseBackupRetentionPeriod(self, BaseBackupRetentionPeriod):
        self._BaseBackupRetentionPeriod = BaseBackupRetentionPeriod

    @property
    def MinBackupStartTime(self):
        r"""开始备份的最早时间
        :rtype: str
        """
        return self._MinBackupStartTime

    @MinBackupStartTime.setter
    def MinBackupStartTime(self, MinBackupStartTime):
        self._MinBackupStartTime = MinBackupStartTime

    @property
    def MaxBackupStartTime(self):
        r"""开始备份的最晚时间
        :rtype: str
        """
        return self._MaxBackupStartTime

    @MaxBackupStartTime.setter
    def MaxBackupStartTime(self, MaxBackupStartTime):
        self._MaxBackupStartTime = MaxBackupStartTime

    @property
    def PlanId(self):
        r"""备份计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        r"""备份计划自定义名称。
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def LogBackupRetentionPeriod(self):
        r"""日志备份保留时长。单位：天
        :rtype: int
        """
        return self._LogBackupRetentionPeriod

    @LogBackupRetentionPeriod.setter
    def LogBackupRetentionPeriod(self, LogBackupRetentionPeriod):
        self._LogBackupRetentionPeriod = LogBackupRetentionPeriod

    @property
    def CreatedTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""最近一次的修改时间。
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def PlanType(self):
        r"""备份计划类型。系统默认创建的为default，自定义的为custom。
        :rtype: str
        """
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType

    @property
    def BackupPeriodType(self):
        r"""备份周期类型。当前支持week、month。
        :rtype: str
        """
        return self._BackupPeriodType

    @BackupPeriodType.setter
    def BackupPeriodType(self, BackupPeriodType):
        self._BackupPeriodType = BackupPeriodType


    def _deserialize(self, params):
        self._BackupPeriod = params.get("BackupPeriod")
        self._BaseBackupRetentionPeriod = params.get("BaseBackupRetentionPeriod")
        self._MinBackupStartTime = params.get("MinBackupStartTime")
        self._MaxBackupStartTime = params.get("MaxBackupStartTime")
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._LogBackupRetentionPeriod = params.get("LogBackupRetentionPeriod")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._PlanType = params.get("PlanType")
        self._BackupPeriodType = params.get("BackupPeriodType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSummary(AbstractModel):
    r"""实例备份统计项

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param _LogBackupCount: 实例日志备份数量。
        :type LogBackupCount: int
        :param _LogBackupSize: 实例日志备份大小。
        :type LogBackupSize: int
        :param _ManualBaseBackupCount: 手动创建的实例数据备份数量。
        :type ManualBaseBackupCount: int
        :param _ManualBaseBackupSize: 手动创建的实例数据备份大小。
        :type ManualBaseBackupSize: int
        :param _AutoBaseBackupCount: 自动创建的实例数据备份数量。
        :type AutoBaseBackupCount: int
        :param _AutoBaseBackupSize: 自动创建的实例数据备份大小。
        :type AutoBaseBackupSize: int
        :param _TotalBackupCount: 总备份数量
        :type TotalBackupCount: int
        :param _TotalBackupSize: 总备份大小
        :type TotalBackupSize: int
        """
        self._DBInstanceId = None
        self._LogBackupCount = None
        self._LogBackupSize = None
        self._ManualBaseBackupCount = None
        self._ManualBaseBackupSize = None
        self._AutoBaseBackupCount = None
        self._AutoBaseBackupSize = None
        self._TotalBackupCount = None
        self._TotalBackupSize = None

    @property
    def DBInstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def LogBackupCount(self):
        r"""实例日志备份数量。
        :rtype: int
        """
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def LogBackupSize(self):
        r"""实例日志备份大小。
        :rtype: int
        """
        return self._LogBackupSize

    @LogBackupSize.setter
    def LogBackupSize(self, LogBackupSize):
        self._LogBackupSize = LogBackupSize

    @property
    def ManualBaseBackupCount(self):
        r"""手动创建的实例数据备份数量。
        :rtype: int
        """
        return self._ManualBaseBackupCount

    @ManualBaseBackupCount.setter
    def ManualBaseBackupCount(self, ManualBaseBackupCount):
        self._ManualBaseBackupCount = ManualBaseBackupCount

    @property
    def ManualBaseBackupSize(self):
        r"""手动创建的实例数据备份大小。
        :rtype: int
        """
        return self._ManualBaseBackupSize

    @ManualBaseBackupSize.setter
    def ManualBaseBackupSize(self, ManualBaseBackupSize):
        self._ManualBaseBackupSize = ManualBaseBackupSize

    @property
    def AutoBaseBackupCount(self):
        r"""自动创建的实例数据备份数量。
        :rtype: int
        """
        return self._AutoBaseBackupCount

    @AutoBaseBackupCount.setter
    def AutoBaseBackupCount(self, AutoBaseBackupCount):
        self._AutoBaseBackupCount = AutoBaseBackupCount

    @property
    def AutoBaseBackupSize(self):
        r"""自动创建的实例数据备份大小。
        :rtype: int
        """
        return self._AutoBaseBackupSize

    @AutoBaseBackupSize.setter
    def AutoBaseBackupSize(self, AutoBaseBackupSize):
        self._AutoBaseBackupSize = AutoBaseBackupSize

    @property
    def TotalBackupCount(self):
        r"""总备份数量
        :rtype: int
        """
        return self._TotalBackupCount

    @TotalBackupCount.setter
    def TotalBackupCount(self, TotalBackupCount):
        self._TotalBackupCount = TotalBackupCount

    @property
    def TotalBackupSize(self):
        r"""总备份大小
        :rtype: int
        """
        return self._TotalBackupSize

    @TotalBackupSize.setter
    def TotalBackupSize(self, TotalBackupSize):
        self._TotalBackupSize = TotalBackupSize


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._LogBackupCount = params.get("LogBackupCount")
        self._LogBackupSize = params.get("LogBackupSize")
        self._ManualBaseBackupCount = params.get("ManualBaseBackupCount")
        self._ManualBaseBackupSize = params.get("ManualBaseBackupSize")
        self._AutoBaseBackupCount = params.get("AutoBaseBackupCount")
        self._AutoBaseBackupSize = params.get("AutoBaseBackupSize")
        self._TotalBackupCount = params.get("TotalBackupCount")
        self._TotalBackupSize = params.get("TotalBackupSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseBackup(AbstractModel):
    r"""数据库数据备份信息

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param _Id: 备份文件唯一标识。
        :type Id: str
        :param _Name: 备份文件名称。
        :type Name: str
        :param _BackupMethod: 备份方式：physical - 物理备份、logical - 逻辑备份。
        :type BackupMethod: str
        :param _BackupMode: 备份模式：automatic - 自动备份、manual - 手动备份。
        :type BackupMode: str
        :param _State: 备份任务状态。枚举值：init、running、finished、failed、canceled
        :type State: str
        :param _Size: 备份集大小，单位bytes。
        :type Size: int
        :param _StartTime: 备份的开始时间。
        :type StartTime: str
        :param _FinishTime: 备份的结束时间。
        :type FinishTime: str
        :param _ExpireTime: 备份的过期时间。
        :type ExpireTime: str
        """
        self._DBInstanceId = None
        self._Id = None
        self._Name = None
        self._BackupMethod = None
        self._BackupMode = None
        self._State = None
        self._Size = None
        self._StartTime = None
        self._FinishTime = None
        self._ExpireTime = None

    @property
    def DBInstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Id(self):
        r"""备份文件唯一标识。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""备份文件名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BackupMethod(self):
        r"""备份方式：physical - 物理备份、logical - 逻辑备份。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupMode(self):
        r"""备份模式：automatic - 自动备份、manual - 手动备份。
        :rtype: str
        """
        return self._BackupMode

    @BackupMode.setter
    def BackupMode(self, BackupMode):
        self._BackupMode = BackupMode

    @property
    def State(self):
        r"""备份任务状态。枚举值：init、running、finished、failed、canceled
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Size(self):
        r"""备份集大小，单位bytes。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def StartTime(self):
        r"""备份的开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        r"""备份的结束时间。
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def ExpireTime(self):
        r"""备份的过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupMode = params.get("BackupMode")
        self._State = params.get("State")
        self._Size = params.get("Size")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassInfo(AbstractModel):
    r"""数据库实例规格

    """

    def __init__(self):
        r"""
        :param _SpecCode: 规格ID
        :type SpecCode: str
        :param _CPU: CPU核数
        :type CPU: int
        :param _Memory: 内存大小，单位：MB
        :type Memory: int
        :param _MaxStorage: 该规格所支持最大存储容量，单位：GB
        :type MaxStorage: int
        :param _MinStorage: 该规格所支持最小存储容量，单位：GB
        :type MinStorage: int
        :param _QPS: 该规格的预估QPS
        :type QPS: int
        """
        self._SpecCode = None
        self._CPU = None
        self._Memory = None
        self._MaxStorage = None
        self._MinStorage = None
        self._QPS = None

    @property
    def SpecCode(self):
        r"""规格ID
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def CPU(self):
        r"""CPU核数
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        r"""内存大小，单位：MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def MaxStorage(self):
        r"""该规格所支持最大存储容量，单位：GB
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def MinStorage(self):
        r"""该规格所支持最小存储容量，单位：GB
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def QPS(self):
        r"""该规格的预估QPS
        :rtype: int
        """
        return self._QPS

    @QPS.setter
    def QPS(self, QPS):
        self._QPS = QPS


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._MaxStorage = params.get("MaxStorage")
        self._MinStorage = params.get("MinStorage")
        self._QPS = params.get("QPS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBInstanceRequest(AbstractModel):
    r"""CloneDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 克隆的源实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _SpecCode: 售卖规格码。该参数可以通过调用[DescribeClasses](https://cloud.tencent.com/document/api/409/89019)的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param _Storage: 实例磁盘容量大小，设置步长限制为10。单位：GB。
        :type Storage: int
        :param _Period: 购买时长，单位：月。

- 预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36
- 后付费：只支持1

        :type Period: int
        :param _AutoRenewFlag: 续费标记。仅当计费模式为预付费时生效。
枚举值：

- 0：手动续费
- 1：自动续费

默认值：0
        :type AutoRenewFlag: int
        :param _VpcId: 私有网络ID，形如vpc-xxxxxxxx。有效的VpcId可通过登录控制台查询；也可以调用接口 [DescribeVpcEx](https://cloud.tencent.com/document/api/215/1372) ，从接口返回中的unVpcId字段获取。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如subnet-xxxxxxxx。有效的私有网络子网ID可通过登录控制台查询；也可以调用接口 [DescribeSubnets ](https://cloud.tencent.com/document/api/215/15784)，从接口返回中的unSubnetId字段获取。
        :type SubnetId: str
        :param _Name: 新购的实例名称，仅支持长度小于60的中文/英文/数字/"_"/"-"，不指定实例名称则默认显示"源实例名-Copy"。
        :type Name: str
        :param _InstanceChargeType: 实例计费类型，目前支持：

- PREPAID：预付费，即包年包月
- POSTPAID_BY_HOUR：后付费，即按量计费

默认值：PREPAID
        :type InstanceChargeType: str
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用[DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808)的返回值中的SecurityGroupId字段来获取。若不指定该参数，则绑定默认安全组。

        :type SecurityGroupIds: list of str
        :param _ProjectId: 项目ID。默认值为0，表示所属默认项目。
        :type ProjectId: int
        :param _TagList: 实例需要绑定的Tag信息，默认为空；可以通过调用 [DescribeTags](https://cloud.tencent.com/document/api/651/35316) 返回值中的 Tags 字段来获取。
        :type TagList: list of Tag
        :param _DBNodeSet: 实例节点部署信息，必须填写主备节点可用区。支持多可用区部署时需要指定每个节点的部署可用区信息。
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :type DBNodeSet: list of DBNode
        :param _AutoVoucher: 是否自动使用代金券：

- 0：否
- 1：是

默认值：0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表。
        :type VoucherIds: str
        :param _ActivityId: 活动ID。
        :type ActivityId: int
        :param _BackupSetId: 基础备份集ID。参数BackupSetId、RecoveryTargetTime两者必须填写一项，且不能同时填写。
        :type BackupSetId: str
        :param _RecoveryTargetTime: 恢复时间点。参数BackupSetId、RecoveryTargetTime两者必须填写一项，且不能同时填写。
        :type RecoveryTargetTime: str
        :param _SyncMode: 主从同步方式，支持： 
<li>Semi-sync：半同步</li>
<li>Async：异步</li>
主实例默认值：Semi-sync
只读实例默认值：Async
        :type SyncMode: str
        :param _DeletionProtection: 实例是否开启删除保护: true-开启删除保护；false-关闭删除保护。
        :type DeletionProtection: bool
        """
        self._DBInstanceId = None
        self._SpecCode = None
        self._Storage = None
        self._Period = None
        self._AutoRenewFlag = None
        self._VpcId = None
        self._SubnetId = None
        self._Name = None
        self._InstanceChargeType = None
        self._SecurityGroupIds = None
        self._ProjectId = None
        self._TagList = None
        self._DBNodeSet = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ActivityId = None
        self._BackupSetId = None
        self._RecoveryTargetTime = None
        self._SyncMode = None
        self._DeletionProtection = None

    @property
    def DBInstanceId(self):
        r"""克隆的源实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def SpecCode(self):
        r"""售卖规格码。该参数可以通过调用[DescribeClasses](https://cloud.tencent.com/document/api/409/89019)的返回值中的SpecCode字段来获取。
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""实例磁盘容量大小，设置步长限制为10。单位：GB。
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Period(self):
        r"""购买时长，单位：月。

- 预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36
- 后付费：只支持1

        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoRenewFlag(self):
        r"""续费标记。仅当计费模式为预付费时生效。
枚举值：

- 0：手动续费
- 1：自动续费

默认值：0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def VpcId(self):
        r"""私有网络ID，形如vpc-xxxxxxxx。有效的VpcId可通过登录控制台查询；也可以调用接口 [DescribeVpcEx](https://cloud.tencent.com/document/api/215/1372) ，从接口返回中的unVpcId字段获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络子网ID，形如subnet-xxxxxxxx。有效的私有网络子网ID可通过登录控制台查询；也可以调用接口 [DescribeSubnets ](https://cloud.tencent.com/document/api/215/15784)，从接口返回中的unSubnetId字段获取。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Name(self):
        r"""新购的实例名称，仅支持长度小于60的中文/英文/数字/"_"/"-"，不指定实例名称则默认显示"源实例名-Copy"。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InstanceChargeType(self):
        r"""实例计费类型，目前支持：

- PREPAID：预付费，即包年包月
- POSTPAID_BY_HOUR：后付费，即按量计费

默认值：PREPAID
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SecurityGroupIds(self):
        r"""实例所属安全组。该参数可以通过调用[DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808)的返回值中的SecurityGroupId字段来获取。若不指定该参数，则绑定默认安全组。

        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ProjectId(self):
        r"""项目ID。默认值为0，表示所属默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagList(self):
        r"""实例需要绑定的Tag信息，默认为空；可以通过调用 [DescribeTags](https://cloud.tencent.com/document/api/651/35316) 返回值中的 Tags 字段来获取。
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def DBNodeSet(self):
        r"""实例节点部署信息，必须填写主备节点可用区。支持多可用区部署时需要指定每个节点的部署可用区信息。
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :rtype: list of DBNode
        """
        return self._DBNodeSet

    @DBNodeSet.setter
    def DBNodeSet(self, DBNodeSet):
        self._DBNodeSet = DBNodeSet

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券：

- 0：否
- 1：是

默认值：0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""代金券ID列表。
        :rtype: str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ActivityId(self):
        r"""活动ID。
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def BackupSetId(self):
        r"""基础备份集ID。参数BackupSetId、RecoveryTargetTime两者必须填写一项，且不能同时填写。
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def RecoveryTargetTime(self):
        r"""恢复时间点。参数BackupSetId、RecoveryTargetTime两者必须填写一项，且不能同时填写。
        :rtype: str
        """
        return self._RecoveryTargetTime

    @RecoveryTargetTime.setter
    def RecoveryTargetTime(self, RecoveryTargetTime):
        self._RecoveryTargetTime = RecoveryTargetTime

    @property
    def SyncMode(self):
        r"""主从同步方式，支持： 
<li>Semi-sync：半同步</li>
<li>Async：异步</li>
主实例默认值：Semi-sync
只读实例默认值：Async
        :rtype: str
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def DeletionProtection(self):
        r"""实例是否开启删除保护: true-开启删除保护；false-关闭删除保护。
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._Period = params.get("Period")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Name = params.get("Name")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        if params.get("DBNodeSet") is not None:
            self._DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self._DBNodeSet.append(obj)
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._ActivityId = params.get("ActivityId")
        self._BackupSetId = params.get("BackupSetId")
        self._RecoveryTargetTime = params.get("RecoveryTargetTime")
        self._SyncMode = params.get("SyncMode")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBInstanceResponse(AbstractModel):
    r"""CloneDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单号。
        :type DealName: str
        :param _BillId: 订单流水号。
        :type BillId: str
        :param _DBInstanceId: 克隆出的新实例ID，当前只支持后付费返回该值。
        :type DBInstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._BillId = None
        self._DBInstanceId = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""订单号。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def BillId(self):
        r"""订单流水号。
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def DBInstanceId(self):
        r"""克隆出的新实例ID，当前只支持后付费返回该值。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._BillId = params.get("BillId")
        self._DBInstanceId = params.get("DBInstanceId")
        self._RequestId = params.get("RequestId")


class CloseAccountCAMRequest(AbstractModel):
    r"""CloseAccountCAM请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param _UserName: 需要关闭CAM服务的账号名称
        :type UserName: str
        :param _Password: 关闭CAM后，登录该账号所需要的新密码
        :type Password: str
        :param _PasswordEncrypt: 密码是否加密
        :type PasswordEncrypt: bool
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Password = None
        self._PasswordEncrypt = None

    @property
    def DBInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""需要关闭CAM服务的账号名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""关闭CAM后，登录该账号所需要的新密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordEncrypt(self):
        r"""密码是否加密
        :rtype: bool
        """
        return self._PasswordEncrypt

    @PasswordEncrypt.setter
    def PasswordEncrypt(self, PasswordEncrypt):
        self._PasswordEncrypt = PasswordEncrypt


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._PasswordEncrypt = params.get("PasswordEncrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseAccountCAMResponse(AbstractModel):
    r"""CloseAccountCAM返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    r"""CloseDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。形如postgres-6r233v55
        :type DBInstanceId: str
        :param _IsIpv6: 是否关闭Ipv6外网，1：是，0：否。默认值：0。
        :type IsIpv6: int
        """
        self._DBInstanceId = None
        self._IsIpv6 = None

    @property
    def DBInstanceId(self):
        r"""实例ID，可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。形如postgres-6r233v55
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def IsIpv6(self):
        r"""是否关闭Ipv6外网，1：是，0：否。默认值：0。
        :rtype: int
        """
        return self._IsIpv6

    @IsIpv6.setter
    def IsIpv6(self, IsIpv6):
        self._IsIpv6 = IsIpv6


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._IsIpv6 = params.get("IsIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    r"""CloseDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    r"""CreateAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _UserName: 创建的账号名称。由字母（a-z, A-Z）、数字（0-9）、下划线（_）组成，以字母或（_）开头，最多63个字符。不能使用系统保留关键字，不能为postgres，且不能由pg_或tencentdb_开头
        :type UserName: str
        :param _Type: 账号类型。当前支持normal、tencentDBSuper两个输入。normal指代普通用户，tencentDBSuper为拥有pg_tencentdb_superuser角色的账号。
        :type Type: str
        :param _Password: 账号对应的密码。密码规则如下：
<li>长度8 ~ 32位，推荐使用12位以上的密码</li>
<li>不能以" / "开头</li>
<li>必须包含以下四项:</li>

小写字母 a ~ z           
大写字母 A ～ Z
数字 0 ～ 9
特殊字符 ()`~!@#$%^&*-+=_|{}[]:<>,.?/

        :type Password: str
        :param _Remark: 账号备注。只允许英文字母、数字、下划线、中划线，以及全体汉字，限60个字符
        :type Remark: str
        :param _OpenCam: 账号是否开启CAM验证
        :type OpenCam: bool
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Type = None
        self._Password = None
        self._Remark = None
        self._OpenCam = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""创建的账号名称。由字母（a-z, A-Z）、数字（0-9）、下划线（_）组成，以字母或（_）开头，最多63个字符。不能使用系统保留关键字，不能为postgres，且不能由pg_或tencentdb_开头
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Type(self):
        r"""账号类型。当前支持normal、tencentDBSuper两个输入。normal指代普通用户，tencentDBSuper为拥有pg_tencentdb_superuser角色的账号。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Password(self):
        r"""账号对应的密码。密码规则如下：
<li>长度8 ~ 32位，推荐使用12位以上的密码</li>
<li>不能以" / "开头</li>
<li>必须包含以下四项:</li>

小写字母 a ~ z           
大写字母 A ～ Z
数字 0 ～ 9
特殊字符 ()`~!@#$%^&*-+=_|{}[]:<>,.?/

        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Remark(self):
        r"""账号备注。只允许英文字母、数字、下划线、中划线，以及全体汉字，限60个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def OpenCam(self):
        r"""账号是否开启CAM验证
        :rtype: bool
        """
        return self._OpenCam

    @OpenCam.setter
    def OpenCam(self, OpenCam):
        self._OpenCam = OpenCam


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Type = params.get("Type")
        self._Password = params.get("Password")
        self._Remark = params.get("Remark")
        self._OpenCam = params.get("OpenCam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    r"""CreateAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBackupPlanRequest(AbstractModel):
    r"""CreateBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _PlanName: 备份计划名称。
        :type PlanName: str
        :param _BackupPeriodType: 创建的备份计划类型，当前仅支持month创建。
        :type BackupPeriodType: str
        :param _BackupPeriod: 备份的日期，示例是每个月的2号开启备份。
        :type BackupPeriod: list of str
        :param _MinBackupStartTime: 备份开始时间，不传跟随默认备份计划。
        :type MinBackupStartTime: str
        :param _MaxBackupStartTime: 备份结束时间，不传跟随默认计划。
        :type MaxBackupStartTime: str
        :param _BaseBackupRetentionPeriod: 数据备份保留时长，单位：天。取值范围为：[0,30000)
BackupPeriodType为week时默认是7,为month时默认为31。
        :type BaseBackupRetentionPeriod: int
        """
        self._DBInstanceId = None
        self._PlanName = None
        self._BackupPeriodType = None
        self._BackupPeriod = None
        self._MinBackupStartTime = None
        self._MaxBackupStartTime = None
        self._BaseBackupRetentionPeriod = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def PlanName(self):
        r"""备份计划名称。
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def BackupPeriodType(self):
        r"""创建的备份计划类型，当前仅支持month创建。
        :rtype: str
        """
        return self._BackupPeriodType

    @BackupPeriodType.setter
    def BackupPeriodType(self, BackupPeriodType):
        self._BackupPeriodType = BackupPeriodType

    @property
    def BackupPeriod(self):
        r"""备份的日期，示例是每个月的2号开启备份。
        :rtype: list of str
        """
        return self._BackupPeriod

    @BackupPeriod.setter
    def BackupPeriod(self, BackupPeriod):
        self._BackupPeriod = BackupPeriod

    @property
    def MinBackupStartTime(self):
        r"""备份开始时间，不传跟随默认备份计划。
        :rtype: str
        """
        return self._MinBackupStartTime

    @MinBackupStartTime.setter
    def MinBackupStartTime(self, MinBackupStartTime):
        self._MinBackupStartTime = MinBackupStartTime

    @property
    def MaxBackupStartTime(self):
        r"""备份结束时间，不传跟随默认计划。
        :rtype: str
        """
        return self._MaxBackupStartTime

    @MaxBackupStartTime.setter
    def MaxBackupStartTime(self, MaxBackupStartTime):
        self._MaxBackupStartTime = MaxBackupStartTime

    @property
    def BaseBackupRetentionPeriod(self):
        r"""数据备份保留时长，单位：天。取值范围为：[0,30000)
BackupPeriodType为week时默认是7,为month时默认为31。
        :rtype: int
        """
        return self._BaseBackupRetentionPeriod

    @BaseBackupRetentionPeriod.setter
    def BaseBackupRetentionPeriod(self, BaseBackupRetentionPeriod):
        self._BaseBackupRetentionPeriod = BaseBackupRetentionPeriod


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._PlanName = params.get("PlanName")
        self._BackupPeriodType = params.get("BackupPeriodType")
        self._BackupPeriod = params.get("BackupPeriod")
        self._MinBackupStartTime = params.get("MinBackupStartTime")
        self._MaxBackupStartTime = params.get("MaxBackupStartTime")
        self._BaseBackupRetentionPeriod = params.get("BaseBackupRetentionPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupPlanResponse(AbstractModel):
    r"""CreateBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 备份策略的ID.
        :type PlanId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlanId = None
        self._RequestId = None

    @property
    def PlanId(self):
        r"""备份策略的ID.
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._RequestId = params.get("RequestId")


class CreateBaseBackupRequest(AbstractModel):
    r"""CreateBaseBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaseBackupResponse(AbstractModel):
    r"""CreateBaseBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BaseBackupId: 数据备份集ID
        :type BaseBackupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaseBackupId = None
        self._RequestId = None

    @property
    def BaseBackupId(self):
        r"""数据备份集ID
        :rtype: str
        """
        return self._BaseBackupId

    @BaseBackupId.setter
    def BaseBackupId(self, BaseBackupId):
        self._BaseBackupId = BaseBackupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BaseBackupId = params.get("BaseBackupId")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceNetworkAccessRequest(AbstractModel):
    r"""CreateDBInstanceNetworkAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如：postgres-6bwgamo3。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _VpcId: 私有网络统一 ID。
        :type VpcId: str
        :param _SubnetId: 子网ID。
        :type SubnetId: str
        :param _IsAssignVip: 是否指定分配vip true-指定分配  false-自动分配。
        :type IsAssignVip: bool
        :param _Vip: 目标VIP地址。当不指定该参数，且IsAssignVip为true时，默认自动分配Vip。
        :type Vip: str
        """
        self._DBInstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._IsAssignVip = None
        self._Vip = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如：postgres-6bwgamo3。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def VpcId(self):
        r"""私有网络统一 ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def IsAssignVip(self):
        r"""是否指定分配vip true-指定分配  false-自动分配。
        :rtype: bool
        """
        return self._IsAssignVip

    @IsAssignVip.setter
    def IsAssignVip(self, IsAssignVip):
        self._IsAssignVip = IsAssignVip

    @property
    def Vip(self):
        r"""目标VIP地址。当不指定该参数，且IsAssignVip为true时，默认自动分配Vip。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._IsAssignVip = params.get("IsAssignVip")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceNetworkAccessResponse(AbstractModel):
    r"""CreateDBInstanceNetworkAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateDatabaseRequest(AbstractModel):
    r"""CreateDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _DatabaseName: 创建的数据库名。
名称规范：由字母（a-z, A-Z）、数字（0-9）、下划线（_）组成，以字母或（_）开头，最多63个字符。不能使用系统保留关键字，不能为postgres。
        :type DatabaseName: str
        :param _DatabaseOwner: 数据库的所有者。可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :type DatabaseOwner: str
        :param _Encoding: 数据库的字符编码。
支持的常用字符集包括：UTF8、LATIN1、LATIN2、WIN1250、WIN1251、WIN1252、KOI8R、EUC_JP、EUC_KR
默认值：UTF8
        :type Encoding: str
        :param _Collate: 数据库的排序规则
        :type Collate: str
        :param _Ctype: 数据库的字符分类
        :type Ctype: str
        """
        self._DBInstanceId = None
        self._DatabaseName = None
        self._DatabaseOwner = None
        self._Encoding = None
        self._Collate = None
        self._Ctype = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DatabaseName(self):
        r"""创建的数据库名。
名称规范：由字母（a-z, A-Z）、数字（0-9）、下划线（_）组成，以字母或（_）开头，最多63个字符。不能使用系统保留关键字，不能为postgres。
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatabaseOwner(self):
        r"""数据库的所有者。可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :rtype: str
        """
        return self._DatabaseOwner

    @DatabaseOwner.setter
    def DatabaseOwner(self, DatabaseOwner):
        self._DatabaseOwner = DatabaseOwner

    @property
    def Encoding(self):
        r"""数据库的字符编码。
支持的常用字符集包括：UTF8、LATIN1、LATIN2、WIN1250、WIN1251、WIN1252、KOI8R、EUC_JP、EUC_KR
默认值：UTF8
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Collate(self):
        r"""数据库的排序规则
        :rtype: str
        """
        return self._Collate

    @Collate.setter
    def Collate(self, Collate):
        self._Collate = Collate

    @property
    def Ctype(self):
        r"""数据库的字符分类
        :rtype: str
        """
        return self._Ctype

    @Ctype.setter
    def Ctype(self, Ctype):
        self._Ctype = Ctype


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._DatabaseName = params.get("DatabaseName")
        self._DatabaseOwner = params.get("DatabaseOwner")
        self._Encoding = params.get("Encoding")
        self._Collate = params.get("Collate")
        self._Ctype = params.get("Ctype")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatabaseResponse(AbstractModel):
    r"""CreateDatabase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    r"""CreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属主可用区， 如：ap-guangzhou-3；若需要支持多可用区，在DBNodeSet.N字段中进行添加主可用区和备可用区信息；
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param _SpecCode: 售卖规格码。该参数可以通过调用[DescribeClasses](https://cloud.tencent.com/document/api/409/89019)的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param _Storage: 实例磁盘容量大小，单位：GB。该参数的设置步长为10。
        :type Storage: int
        :param _InstanceCount: 购买实例数量，取值范围：[1-10]。一次性购买支持最大数量10个，若超过该数量，可进行多次调用进行购买。
        :type InstanceCount: int
        :param _Period: 购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
<li>后付费：只支持1</li>
        :type Period: int
        :param _Charset: 实例字符集，目前只支持：
<li> UTF8</li>
<li> LATIN1</li>
        :type Charset: str
        :param _AdminName: 实例根账号用户名，具体规范如下：
<li>用户名需要1-16个字符，只能由字母、数字或下划线组成</li>
<li>不能为postgres</li>
<li>不能由数字和pg_开头</li>
<li>所有规则均不区分大小写</li>
        :type AdminName: str
        :param _AdminPassword: 实例根账号用户名对应的密码，长度8 ~ 32位，推荐使用12位以上的密码;不能以" / "开头;
必须包含以下四项，字符种类:
<li>小写字母： [a ~ z]</li>
<li>大写字母：[A ～ Z]</li>
<li>数字：0 - 9</li>
<li>特殊字符：()`~!@#$%^&*-+=_|{}[]:;'<>,.?/</li>
        :type AdminPassword: str
        :param _DBMajorVersion: PostgreSQL大版本号（该参数当前必传），版本信息可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)获取。目前支持10，11，12，13，14，15这几个大版本，详情见[内核版本概述](https://cloud.tencent.com/document/product/409/67018)。
输入该参数时，会基于此大版本号创建对应的最新小版本的最新内核版本号实例。
        :type DBMajorVersion: str
        :param _DBVersion: PostgreSQL社区大版本+小版本号。
一般场景不推荐传入该参数。如需指定，只能传当前大版本号下最新小版本号。
        :type DBVersion: str
        :param _DBKernelVersion: PostgreSQL内核版本号。
一般场景不推荐传入该参数。如需指定，只能传当前大版本号下最新内核版本号。
        :type DBKernelVersion: str
        :param _InstanceChargeType: 实例计费类型，目前支持：
<li>PREPAID：预付费，即包年包月</li>
<li>POSTPAID_BY_HOUR：后付费，即按量计费</li>
默认值：PREPAID
        :type InstanceChargeType: str
        :param _VpcId: 私有网络ID，形如vpc-xxxxxxxx（该参数当前必传）。有效的VpcId可通过登录控制台查询；也可以调用接口 [DescribeVpcEx](https://cloud.tencent.com/document/api/215/1372) ，从接口返回中的unVpcId字段获取。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如subnet-xxxxxxxx（该参数当前必传）。有效的私有网络子网ID可通过登录控制台查询；也可以调用接口 [DescribeSubnets ](https://cloud.tencent.com/document/api/215/15784)，从接口返回中的unSubnetId字段获取。
        :type SubnetId: str
        :param _DBNodeSet: 实例节点部署信息，支持多可用区部署时需要指定每个节点的部署可用区信息。
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :type DBNodeSet: list of DBNode
        :param _AutoRenewFlag: 续费标记：
<li>0：手动续费</li>
<li>1：自动续费</li>
默认值：0
        :type AutoRenewFlag: int
        :param _AutoVoucher: 是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param _ProjectId: 项目ID。默认取之为0，表示归属默认项目。
        :type ProjectId: int
        :param _ActivityId: 活动ID。
        :type ActivityId: int
        :param _Name: 实例名称，仅支持长度小于60的中文/英文/数字/"_"/"-"，不指定实例名称则默认显示"未命名"。

        :type Name: str
        :param _TagList: 实例需要绑定的Tag信息，默认为空；可以通过调用 [DescribeTags](https://cloud.tencent.com/document/api/651/35316) 返回值中的 Tags 字段来获取。
        :type TagList: list of Tag
        :param _SecurityGroupIds: 实例所属安全组，该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。

        :type SecurityGroupIds: list of str
        :param _NeedSupportTDE: 是否需要支持数据透明加密：
<li>0：否</li>
<li>1：是</li>
默认值：0
参考[数据透明加密概述](https://cloud.tencent.com/document/product/409/71748)
        :type NeedSupportTDE: int
        :param _KMSKeyId: 自定义密钥的KeyId，若选择自定义密匙加密，则需要传入自定义密匙的KeyId，KeyId是CMK的唯一标识。
KeyId创建获取相关参考[开启透明数据加密](https://cloud.tencent.com/document/product/409/71749)
        :type KMSKeyId: str
        :param _KMSRegion: 使用KMS服务的地域，KMSRegion为空默认使用本地域的KMS，本地域不支持的情况下需自选其他KMS支持的地域。
KMSRegion相关介绍参考[开启透明数据加密](https://cloud.tencent.com/document/product/409/71749)
        :type KMSRegion: str
        :param _KMSClusterId: 指定KMS服务的集群，KMSClusterId为空使用默认集群的KMS，若选择指定KMS集群，则需要传入KMSClusterId。 KMSClusterId相关介绍参考开启透明数据加密
        :type KMSClusterId: str
        :param _DBEngine: 数据库引擎，支持：
<li>postgresql：云数据库PostgreSQL</li>
<li>mssql_compatible：MSSQL兼容-云数据库PostgreSQL</li>
默认值：postgresql
        :type DBEngine: str
        :param _DBEngineConfig: 数据库引擎的配置信息，配置格式如下：
{"$key1":"$value1", "$key2":"$value2"}
各引擎支持如下：
mssql_compatible引擎：
<li>migrationMode：数据库模式，可选参数，可取值：single-db（单数据库模式），multi-db（多数据库模式）。默认为single-db。</li>
<li>defaultLocale：排序区域规则，可选参数，在初始化后不可修改，默认为en_US，可选值如下：
"af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN"。</li>
<li>serverCollationName：排序规则名称，可选参数，在初始化后不可修改，默认为sql_latin1_general_cp1_ci_as，可选值如下："bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as"。</li>
        :type DBEngineConfig: str
        :param _SyncMode: 主从同步方式，支持： 
<li>Semi-sync：半同步</li>
<li>Async：异步</li>
主实例默认值：Semi-sync
只读实例默认值：Async
        :type SyncMode: str
        :param _NeedSupportIpv6: 是否需要支持Ipv6：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :type NeedSupportIpv6: int
        :param _DeletionProtection: 实例是否开启删除保护: true-开启删除保护；false-关闭删除保护。
        :type DeletionProtection: bool
        """
        self._Zone = None
        self._SpecCode = None
        self._Storage = None
        self._InstanceCount = None
        self._Period = None
        self._Charset = None
        self._AdminName = None
        self._AdminPassword = None
        self._DBMajorVersion = None
        self._DBVersion = None
        self._DBKernelVersion = None
        self._InstanceChargeType = None
        self._VpcId = None
        self._SubnetId = None
        self._DBNodeSet = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ProjectId = None
        self._ActivityId = None
        self._Name = None
        self._TagList = None
        self._SecurityGroupIds = None
        self._NeedSupportTDE = None
        self._KMSKeyId = None
        self._KMSRegion = None
        self._KMSClusterId = None
        self._DBEngine = None
        self._DBEngineConfig = None
        self._SyncMode = None
        self._NeedSupportIpv6 = None
        self._DeletionProtection = None

    @property
    def Zone(self):
        r"""实例所属主可用区， 如：ap-guangzhou-3；若需要支持多可用区，在DBNodeSet.N字段中进行添加主可用区和备可用区信息；
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecCode(self):
        r"""售卖规格码。该参数可以通过调用[DescribeClasses](https://cloud.tencent.com/document/api/409/89019)的返回值中的SpecCode字段来获取。
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""实例磁盘容量大小，单位：GB。该参数的设置步长为10。
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceCount(self):
        r"""购买实例数量，取值范围：[1-10]。一次性购买支持最大数量10个，若超过该数量，可进行多次调用进行购买。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        r"""购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
<li>后付费：只支持1</li>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Charset(self):
        r"""实例字符集，目前只支持：
<li> UTF8</li>
<li> LATIN1</li>
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def AdminName(self):
        r"""实例根账号用户名，具体规范如下：
<li>用户名需要1-16个字符，只能由字母、数字或下划线组成</li>
<li>不能为postgres</li>
<li>不能由数字和pg_开头</li>
<li>所有规则均不区分大小写</li>
        :rtype: str
        """
        return self._AdminName

    @AdminName.setter
    def AdminName(self, AdminName):
        self._AdminName = AdminName

    @property
    def AdminPassword(self):
        r"""实例根账号用户名对应的密码，长度8 ~ 32位，推荐使用12位以上的密码;不能以" / "开头;
必须包含以下四项，字符种类:
<li>小写字母： [a ~ z]</li>
<li>大写字母：[A ～ Z]</li>
<li>数字：0 - 9</li>
<li>特殊字符：()`~!@#$%^&*-+=_|{}[]:;'<>,.?/</li>
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def DBMajorVersion(self):
        r"""PostgreSQL大版本号（该参数当前必传），版本信息可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)获取。目前支持10，11，12，13，14，15这几个大版本，详情见[内核版本概述](https://cloud.tencent.com/document/product/409/67018)。
输入该参数时，会基于此大版本号创建对应的最新小版本的最新内核版本号实例。
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBVersion(self):
        r"""PostgreSQL社区大版本+小版本号。
一般场景不推荐传入该参数。如需指定，只能传当前大版本号下最新小版本号。
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def DBKernelVersion(self):
        r"""PostgreSQL内核版本号。
一般场景不推荐传入该参数。如需指定，只能传当前大版本号下最新内核版本号。
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def InstanceChargeType(self):
        r"""实例计费类型，目前支持：
<li>PREPAID：预付费，即包年包月</li>
<li>POSTPAID_BY_HOUR：后付费，即按量计费</li>
默认值：PREPAID
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def VpcId(self):
        r"""私有网络ID，形如vpc-xxxxxxxx（该参数当前必传）。有效的VpcId可通过登录控制台查询；也可以调用接口 [DescribeVpcEx](https://cloud.tencent.com/document/api/215/1372) ，从接口返回中的unVpcId字段获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络子网ID，形如subnet-xxxxxxxx（该参数当前必传）。有效的私有网络子网ID可通过登录控制台查询；也可以调用接口 [DescribeSubnets ](https://cloud.tencent.com/document/api/215/15784)，从接口返回中的unSubnetId字段获取。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DBNodeSet(self):
        r"""实例节点部署信息，支持多可用区部署时需要指定每个节点的部署可用区信息。
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :rtype: list of DBNode
        """
        return self._DBNodeSet

    @DBNodeSet.setter
    def DBNodeSet(self, DBNodeSet):
        self._DBNodeSet = DBNodeSet

    @property
    def AutoRenewFlag(self):
        r"""续费标记：
<li>0：手动续费</li>
<li>1：自动续费</li>
默认值：0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""代金券ID列表，目前仅支持指定一张代金券。
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ProjectId(self):
        r"""项目ID。默认取之为0，表示归属默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ActivityId(self):
        r"""活动ID。
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def Name(self):
        r"""实例名称，仅支持长度小于60的中文/英文/数字/"_"/"-"，不指定实例名称则默认显示"未命名"。

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TagList(self):
        r"""实例需要绑定的Tag信息，默认为空；可以通过调用 [DescribeTags](https://cloud.tencent.com/document/api/651/35316) 返回值中的 Tags 字段来获取。
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SecurityGroupIds(self):
        r"""实例所属安全组，该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。

        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def NeedSupportTDE(self):
        r"""是否需要支持数据透明加密：
<li>0：否</li>
<li>1：是</li>
默认值：0
参考[数据透明加密概述](https://cloud.tencent.com/document/product/409/71748)
        :rtype: int
        """
        return self._NeedSupportTDE

    @NeedSupportTDE.setter
    def NeedSupportTDE(self, NeedSupportTDE):
        self._NeedSupportTDE = NeedSupportTDE

    @property
    def KMSKeyId(self):
        r"""自定义密钥的KeyId，若选择自定义密匙加密，则需要传入自定义密匙的KeyId，KeyId是CMK的唯一标识。
KeyId创建获取相关参考[开启透明数据加密](https://cloud.tencent.com/document/product/409/71749)
        :rtype: str
        """
        return self._KMSKeyId

    @KMSKeyId.setter
    def KMSKeyId(self, KMSKeyId):
        self._KMSKeyId = KMSKeyId

    @property
    def KMSRegion(self):
        r"""使用KMS服务的地域，KMSRegion为空默认使用本地域的KMS，本地域不支持的情况下需自选其他KMS支持的地域。
KMSRegion相关介绍参考[开启透明数据加密](https://cloud.tencent.com/document/product/409/71749)
        :rtype: str
        """
        return self._KMSRegion

    @KMSRegion.setter
    def KMSRegion(self, KMSRegion):
        self._KMSRegion = KMSRegion

    @property
    def KMSClusterId(self):
        r"""指定KMS服务的集群，KMSClusterId为空使用默认集群的KMS，若选择指定KMS集群，则需要传入KMSClusterId。 KMSClusterId相关介绍参考开启透明数据加密
        :rtype: str
        """
        return self._KMSClusterId

    @KMSClusterId.setter
    def KMSClusterId(self, KMSClusterId):
        self._KMSClusterId = KMSClusterId

    @property
    def DBEngine(self):
        r"""数据库引擎，支持：
<li>postgresql：云数据库PostgreSQL</li>
<li>mssql_compatible：MSSQL兼容-云数据库PostgreSQL</li>
默认值：postgresql
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def DBEngineConfig(self):
        r"""数据库引擎的配置信息，配置格式如下：
{"$key1":"$value1", "$key2":"$value2"}
各引擎支持如下：
mssql_compatible引擎：
<li>migrationMode：数据库模式，可选参数，可取值：single-db（单数据库模式），multi-db（多数据库模式）。默认为single-db。</li>
<li>defaultLocale：排序区域规则，可选参数，在初始化后不可修改，默认为en_US，可选值如下：
"af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN"。</li>
<li>serverCollationName：排序规则名称，可选参数，在初始化后不可修改，默认为sql_latin1_general_cp1_ci_as，可选值如下："bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as"。</li>
        :rtype: str
        """
        return self._DBEngineConfig

    @DBEngineConfig.setter
    def DBEngineConfig(self, DBEngineConfig):
        self._DBEngineConfig = DBEngineConfig

    @property
    def SyncMode(self):
        r"""主从同步方式，支持： 
<li>Semi-sync：半同步</li>
<li>Async：异步</li>
主实例默认值：Semi-sync
只读实例默认值：Async
        :rtype: str
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def NeedSupportIpv6(self):
        r"""是否需要支持Ipv6：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :rtype: int
        """
        return self._NeedSupportIpv6

    @NeedSupportIpv6.setter
    def NeedSupportIpv6(self, NeedSupportIpv6):
        self._NeedSupportIpv6 = NeedSupportIpv6

    @property
    def DeletionProtection(self):
        r"""实例是否开启删除保护: true-开启删除保护；false-关闭删除保护。
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._Charset = params.get("Charset")
        self._AdminName = params.get("AdminName")
        self._AdminPassword = params.get("AdminPassword")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBVersion = params.get("DBVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("DBNodeSet") is not None:
            self._DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self._DBNodeSet.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._ProjectId = params.get("ProjectId")
        self._ActivityId = params.get("ActivityId")
        self._Name = params.get("Name")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._NeedSupportTDE = params.get("NeedSupportTDE")
        self._KMSKeyId = params.get("KMSKeyId")
        self._KMSRegion = params.get("KMSRegion")
        self._KMSClusterId = params.get("KMSClusterId")
        self._DBEngine = params.get("DBEngine")
        self._DBEngineConfig = params.get("DBEngineConfig")
        self._SyncMode = params.get("SyncMode")
        self._NeedSupportIpv6 = params.get("NeedSupportIpv6")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    r"""CreateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单号列表。每个实例对应一个订单号。
        :type DealNames: list of str
        :param _BillId: 冻结流水号。
        :type BillId: str
        :param _DBInstanceIdSet: 创建成功的实例ID集合，只在后付费情景下有返回值。
        :type DBInstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealNames = None
        self._BillId = None
        self._DBInstanceIdSet = None
        self._RequestId = None

    @property
    def DealNames(self):
        r"""订单号列表。每个实例对应一个订单号。
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BillId(self):
        r"""冻结流水号。
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def DBInstanceIdSet(self):
        r"""创建成功的实例ID集合，只在后付费情景下有返回值。
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        self._BillId = params.get("BillId")
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreateParameterTemplateRequest(AbstractModel):
    r"""CreateParameterTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称，长度为1～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@
        :type TemplateName: str
        :param _DBMajorVersion: 数据库大版本号，例如：11，12，13。可通过[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)接口获取
        :type DBMajorVersion: str
        :param _DBEngine: 数据库引擎，例如：postgresql，mssql_compatible
        :type DBEngine: str
        :param _TemplateDescription: 参数模板描述，长度为0～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@
        :type TemplateDescription: str
        """
        self._TemplateName = None
        self._DBMajorVersion = None
        self._DBEngine = None
        self._TemplateDescription = None

    @property
    def TemplateName(self):
        r"""模板名称，长度为1～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def DBMajorVersion(self):
        r"""数据库大版本号，例如：11，12，13。可通过[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)接口获取
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBEngine(self):
        r"""数据库引擎，例如：postgresql，mssql_compatible
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def TemplateDescription(self):
        r"""参数模板描述，长度为0～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBEngine = params.get("DBEngine")
        self._TemplateDescription = params.get("TemplateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParameterTemplateResponse(AbstractModel):
    r"""CreateParameterTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID，用于唯一确认参数模板
        :type TemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        r"""参数模板ID，用于唯一确认参数模板
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateReadOnlyDBInstanceRequest(AbstractModel):
    r"""CreateReadOnlyDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属主可用区， 如：ap-guangzhou-3；
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param _MasterDBInstanceId: 只读实例的主实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type MasterDBInstanceId: str
        :param _SpecCode: 售卖规格码。该参数可以通过调用[DescribeClasses](https://cloud.tencent.com/document/api/409/89019)的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param _Storage: 实例硬盘容量大小，单位：GB。该参数的设置步长为10。
        :type Storage: int
        :param _InstanceCount: 购买实例数量，取值范围：[1-6]。购买支持最大数量6个。
        :type InstanceCount: int
        :param _Period: 购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
<li>后付费：只支持1</li>
        :type Period: int
        :param _VpcId: 私有网络ID，形如vpc-xxxxxxxx（该参数当前必传）。有效的VpcId可通过登录控制台查询；也可以调用接口 [DescribeVpcEx](https://cloud.tencent.com/document/api/215/1372) ，从接口返回中的unVpcId字段获取。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如subnet-xxxxxxxx（该参数当前必传）。有效的私有网络子网ID可通过登录控制台查询；也可以调用接口 [DescribeSubnets ](https://cloud.tencent.com/document/api/215/15784)，从接口返回中的unSubnetId字段获取。
        :type SubnetId: str
        :param _InstanceChargeType: 实例计费类型，目前支持：
<li>PREPAID：预付费，即包年包月。</li>
<li>POSTPAID_BY_HOUR：后付费，即按量计费。</li>
默认值：PREPAID。如果主实例为后付费，只读实例必须也为后付费。
        :type InstanceChargeType: str
        :param _AutoVoucher: 是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param _AutoRenewFlag: 续费标记：
<li>0：手动续费</li>
<li>1：自动续费</li>
默认值：0
        :type AutoRenewFlag: int
        :param _ProjectId: 项目ID。默认值为0，表示归属默认项目。
        :type ProjectId: int
        :param _ActivityId: 优惠活动ID
        :type ActivityId: int
        :param _ReadOnlyGroupId: 只读组ID。
        :type ReadOnlyGroupId: str
        :param _TagList: 实例需要绑定的Tag信息，默认为空；可以通过调用 [DescribeTags](https://cloud.tencent.com/document/api/651/35316) 返回值中的 Tags 字段来获取。
        :type TagList: :class:`tencentcloud.postgres.v20170312.models.Tag`
        :param _SecurityGroupIds: 实例所属安全组，该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。

        :type SecurityGroupIds: list of str
        :param _NeedSupportIpv6: 是否需要支持Ipv6：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :type NeedSupportIpv6: int
        :param _Name: 实例名。仅支持长度小于60的中文/英文/数字/"_"/"-"
        :type Name: str
        :param _DBVersion: 不再需要指定，内核版本号与主实例保持一致
        :type DBVersion: str
        :param _DedicatedClusterId: 专属集群ID
        :type DedicatedClusterId: str
        :param _DeletionProtection: 实例是否开启删除保护: true-开启删除保护；false-关闭删除保护。
        :type DeletionProtection: bool
        """
        self._Zone = None
        self._MasterDBInstanceId = None
        self._SpecCode = None
        self._Storage = None
        self._InstanceCount = None
        self._Period = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceChargeType = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._AutoRenewFlag = None
        self._ProjectId = None
        self._ActivityId = None
        self._ReadOnlyGroupId = None
        self._TagList = None
        self._SecurityGroupIds = None
        self._NeedSupportIpv6 = None
        self._Name = None
        self._DBVersion = None
        self._DedicatedClusterId = None
        self._DeletionProtection = None

    @property
    def Zone(self):
        r"""实例所属主可用区， 如：ap-guangzhou-3；
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def MasterDBInstanceId(self):
        r"""只读实例的主实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._MasterDBInstanceId

    @MasterDBInstanceId.setter
    def MasterDBInstanceId(self, MasterDBInstanceId):
        self._MasterDBInstanceId = MasterDBInstanceId

    @property
    def SpecCode(self):
        r"""售卖规格码。该参数可以通过调用[DescribeClasses](https://cloud.tencent.com/document/api/409/89019)的返回值中的SpecCode字段来获取。
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""实例硬盘容量大小，单位：GB。该参数的设置步长为10。
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceCount(self):
        r"""购买实例数量，取值范围：[1-6]。购买支持最大数量6个。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        r"""购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
<li>后付费：只支持1</li>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def VpcId(self):
        r"""私有网络ID，形如vpc-xxxxxxxx（该参数当前必传）。有效的VpcId可通过登录控制台查询；也可以调用接口 [DescribeVpcEx](https://cloud.tencent.com/document/api/215/1372) ，从接口返回中的unVpcId字段获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络子网ID，形如subnet-xxxxxxxx（该参数当前必传）。有效的私有网络子网ID可通过登录控制台查询；也可以调用接口 [DescribeSubnets ](https://cloud.tencent.com/document/api/215/15784)，从接口返回中的unSubnetId字段获取。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceChargeType(self):
        r"""实例计费类型，目前支持：
<li>PREPAID：预付费，即包年包月。</li>
<li>POSTPAID_BY_HOUR：后付费，即按量计费。</li>
默认值：PREPAID。如果主实例为后付费，只读实例必须也为后付费。
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""代金券ID列表，目前仅支持指定一张代金券。
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def AutoRenewFlag(self):
        r"""续费标记：
<li>0：手动续费</li>
<li>1：自动续费</li>
默认值：0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ProjectId(self):
        r"""项目ID。默认值为0，表示归属默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ActivityId(self):
        r"""优惠活动ID
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID。
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def TagList(self):
        r"""实例需要绑定的Tag信息，默认为空；可以通过调用 [DescribeTags](https://cloud.tencent.com/document/api/651/35316) 返回值中的 Tags 字段来获取。
        :rtype: :class:`tencentcloud.postgres.v20170312.models.Tag`
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SecurityGroupIds(self):
        r"""实例所属安全组，该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。

        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def NeedSupportIpv6(self):
        r"""是否需要支持Ipv6：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :rtype: int
        """
        return self._NeedSupportIpv6

    @NeedSupportIpv6.setter
    def NeedSupportIpv6(self, NeedSupportIpv6):
        self._NeedSupportIpv6 = NeedSupportIpv6

    @property
    def Name(self):
        r"""实例名。仅支持长度小于60的中文/英文/数字/"_"/"-"
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DBVersion(self):
        warnings.warn("parameter `DBVersion` is deprecated", DeprecationWarning) 

        r"""不再需要指定，内核版本号与主实例保持一致
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        warnings.warn("parameter `DBVersion` is deprecated", DeprecationWarning) 

        self._DBVersion = DBVersion

    @property
    def DedicatedClusterId(self):
        r"""专属集群ID
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def DeletionProtection(self):
        r"""实例是否开启删除保护: true-开启删除保护；false-关闭删除保护。
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._MasterDBInstanceId = params.get("MasterDBInstanceId")
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ProjectId = params.get("ProjectId")
        self._ActivityId = params.get("ActivityId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        if params.get("TagList") is not None:
            self._TagList = Tag()
            self._TagList._deserialize(params.get("TagList"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._NeedSupportIpv6 = params.get("NeedSupportIpv6")
        self._Name = params.get("Name")
        self._DBVersion = params.get("DBVersion")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyDBInstanceResponse(AbstractModel):
    r"""CreateReadOnlyDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单号列表。每个实例对应一个订单号
        :type DealNames: list of str
        :param _BillId: 冻结流水号
        :type BillId: str
        :param _DBInstanceIdSet: 创建成功的实例ID集合，只在后付费情景下有返回值
        :type DBInstanceIdSet: list of str
        :param _BillingParameters: 入参有BillingParameters值时，出参才有值，值为商品下单的参数。
        :type BillingParameters: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealNames = None
        self._BillId = None
        self._DBInstanceIdSet = None
        self._BillingParameters = None
        self._RequestId = None

    @property
    def DealNames(self):
        r"""订单号列表。每个实例对应一个订单号
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BillId(self):
        r"""冻结流水号
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def DBInstanceIdSet(self):
        r"""创建成功的实例ID集合，只在后付费情景下有返回值
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def BillingParameters(self):
        r"""入参有BillingParameters值时，出参才有值，值为商品下单的参数。
        :rtype: str
        """
        return self._BillingParameters

    @BillingParameters.setter
    def BillingParameters(self, BillingParameters):
        self._BillingParameters = BillingParameters

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        self._BillId = params.get("BillId")
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._BillingParameters = params.get("BillingParameters")
        self._RequestId = params.get("RequestId")


class CreateReadOnlyGroupNetworkAccessRequest(AbstractModel):
    r"""CreateReadOnlyGroupNetworkAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: RO组ID，形如：pgrogrp-4t9c6g7k。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :type ReadOnlyGroupId: str
        :param _VpcId: 私有网络统一 ID。
        :type VpcId: str
        :param _SubnetId: 子网ID。
        :type SubnetId: str
        :param _IsAssignVip: 是否指定分配vip true-指定分配  false-自动分配。
        :type IsAssignVip: bool
        :param _Vip: 目标VIP地址。当不指定该参数，且IsAssignVip为true时，默认自动分配Vip。
        :type Vip: str
        """
        self._ReadOnlyGroupId = None
        self._VpcId = None
        self._SubnetId = None
        self._IsAssignVip = None
        self._Vip = None

    @property
    def ReadOnlyGroupId(self):
        r"""RO组ID，形如：pgrogrp-4t9c6g7k。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def VpcId(self):
        r"""私有网络统一 ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def IsAssignVip(self):
        r"""是否指定分配vip true-指定分配  false-自动分配。
        :rtype: bool
        """
        return self._IsAssignVip

    @IsAssignVip.setter
    def IsAssignVip(self, IsAssignVip):
        self._IsAssignVip = IsAssignVip

    @property
    def Vip(self):
        r"""目标VIP地址。当不指定该参数，且IsAssignVip为true时，默认自动分配Vip。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._IsAssignVip = params.get("IsAssignVip")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyGroupNetworkAccessResponse(AbstractModel):
    r"""CreateReadOnlyGroupNetworkAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateReadOnlyGroupRequest(AbstractModel):
    r"""CreateReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MasterDBInstanceId: 主实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type MasterDBInstanceId: str
        :param _Name: 只读组名称。仅支持长度小于60的中文/英文/数字/"_"/"-"。
        :type Name: str
        :param _ProjectId: 项目ID。默认值为0，表示归属于默认项目。
        :type ProjectId: int
        :param _VpcId: 私有网络ID。注：默认使用基础网络，当前不支持基础网络，故该参数必填。
        :type VpcId: str
        :param _SubnetId: 子网ID。注：默认使用基础网络，当前不支持基础网络，故该参数必填。
        :type SubnetId: str
        :param _ReplayLagEliminate: 延迟时间大小开关：0关、1开。该参数必填。
        :type ReplayLagEliminate: int
        :param _ReplayLatencyEliminate: 延迟空间大小开关： 0关、1开。该参数的填写需要与ReplayLagEliminate一致。
        :type ReplayLatencyEliminate: int
        :param _MaxReplayLag: 延迟时间大小阈值，取值为正整数，单位s。当ReplayLagEliminate为1时，该参数必填；当ReplayLagEliminate为0时，该参数需填0。
        :type MaxReplayLag: int
        :param _MaxReplayLatency: 延迟空间大小阈值，取值为正整数，单位MB。当ReplayLatencyEliminate为1时，该参数必填；当ReplayLatencyEliminate为0时，该参数需填0。
        :type MaxReplayLatency: int
        :param _MinDelayEliminateReserve: 延迟剔除最小保留实例数。取值范围[0,100]。当ReplayLatencyEliminate为1时，该参数必填；当ReplayLagEliminate为0时，该参数无效。
        :type MinDelayEliminateReserve: int
        :param _SecurityGroupIds: 安全组id
        :type SecurityGroupIds: list of str
        """
        self._MasterDBInstanceId = None
        self._Name = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._ReplayLagEliminate = None
        self._ReplayLatencyEliminate = None
        self._MaxReplayLag = None
        self._MaxReplayLatency = None
        self._MinDelayEliminateReserve = None
        self._SecurityGroupIds = None

    @property
    def MasterDBInstanceId(self):
        r"""主实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._MasterDBInstanceId

    @MasterDBInstanceId.setter
    def MasterDBInstanceId(self, MasterDBInstanceId):
        self._MasterDBInstanceId = MasterDBInstanceId

    @property
    def Name(self):
        r"""只读组名称。仅支持长度小于60的中文/英文/数字/"_"/"-"。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProjectId(self):
        r"""项目ID。默认值为0，表示归属于默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        r"""私有网络ID。注：默认使用基础网络，当前不支持基础网络，故该参数必填。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID。注：默认使用基础网络，当前不支持基础网络，故该参数必填。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ReplayLagEliminate(self):
        r"""延迟时间大小开关：0关、1开。该参数必填。
        :rtype: int
        """
        return self._ReplayLagEliminate

    @ReplayLagEliminate.setter
    def ReplayLagEliminate(self, ReplayLagEliminate):
        self._ReplayLagEliminate = ReplayLagEliminate

    @property
    def ReplayLatencyEliminate(self):
        r"""延迟空间大小开关： 0关、1开。该参数的填写需要与ReplayLagEliminate一致。
        :rtype: int
        """
        return self._ReplayLatencyEliminate

    @ReplayLatencyEliminate.setter
    def ReplayLatencyEliminate(self, ReplayLatencyEliminate):
        self._ReplayLatencyEliminate = ReplayLatencyEliminate

    @property
    def MaxReplayLag(self):
        r"""延迟时间大小阈值，取值为正整数，单位s。当ReplayLagEliminate为1时，该参数必填；当ReplayLagEliminate为0时，该参数需填0。
        :rtype: int
        """
        return self._MaxReplayLag

    @MaxReplayLag.setter
    def MaxReplayLag(self, MaxReplayLag):
        self._MaxReplayLag = MaxReplayLag

    @property
    def MaxReplayLatency(self):
        r"""延迟空间大小阈值，取值为正整数，单位MB。当ReplayLatencyEliminate为1时，该参数必填；当ReplayLatencyEliminate为0时，该参数需填0。
        :rtype: int
        """
        return self._MaxReplayLatency

    @MaxReplayLatency.setter
    def MaxReplayLatency(self, MaxReplayLatency):
        self._MaxReplayLatency = MaxReplayLatency

    @property
    def MinDelayEliminateReserve(self):
        r"""延迟剔除最小保留实例数。取值范围[0,100]。当ReplayLatencyEliminate为1时，该参数必填；当ReplayLagEliminate为0时，该参数无效。
        :rtype: int
        """
        return self._MinDelayEliminateReserve

    @MinDelayEliminateReserve.setter
    def MinDelayEliminateReserve(self, MinDelayEliminateReserve):
        self._MinDelayEliminateReserve = MinDelayEliminateReserve

    @property
    def SecurityGroupIds(self):
        r"""安全组id
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._MasterDBInstanceId = params.get("MasterDBInstanceId")
        self._Name = params.get("Name")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ReplayLagEliminate = params.get("ReplayLagEliminate")
        self._ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self._MaxReplayLag = params.get("MaxReplayLag")
        self._MaxReplayLatency = params.get("MaxReplayLatency")
        self._MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyGroupResponse(AbstractModel):
    r"""CreateReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReadOnlyGroupId = None
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DBBackup(AbstractModel):
    r"""数据库备份信息

    """

    def __init__(self):
        r"""
        :param _Id: 备份文件唯一标识
        :type Id: int
        :param _StartTime: 文件生成的开始时间
        :type StartTime: str
        :param _EndTime: 文件生成的结束时间
        :type EndTime: str
        :param _Size: 文件大小(K)
        :type Size: int
        :param _Strategy: 策略（0-实例备份；1-多库备份）
        :type Strategy: int
        :param _Way: 类型（0-定时）
        :type Way: int
        :param _Type: 备份方式（1-完整）
        :type Type: int
        :param _Status: 状态（1-创建中；2-成功；3-失败）
        :type Status: int
        :param _DbList: DB列表
        :type DbList: list of str
        :param _InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param _ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param _SetId: 备份集ID
        :type SetId: str
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Strategy = None
        self._Way = None
        self._Type = None
        self._Status = None
        self._DbList = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._SetId = None

    @property
    def Id(self):
        r"""备份文件唯一标识
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        r"""文件生成的开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""文件生成的结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        r"""文件大小(K)
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Strategy(self):
        r"""策略（0-实例备份；1-多库备份）
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Way(self):
        r"""类型（0-定时）
        :rtype: int
        """
        return self._Way

    @Way.setter
    def Way(self, Way):
        self._Way = Way

    @property
    def Type(self):
        r"""备份方式（1-完整）
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""状态（1-创建中；2-成功；3-失败）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DbList(self):
        r"""DB列表
        :rtype: list of str
        """
        return self._DbList

    @DbList.setter
    def DbList(self, DbList):
        self._DbList = DbList

    @property
    def InternalAddr(self):
        r"""内网下载地址
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""外网下载地址
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def SetId(self):
        r"""备份集ID
        :rtype: str
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Strategy = params.get("Strategy")
        self._Way = params.get("Way")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._DbList = params.get("DbList")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    r"""描述实例的详细信息

    """

    def __init__(self):
        r"""
        :param _Region: 实例所属地域，如: ap-guangzhou，对应RegionSet的Region字段。
        :type Region: str
        :param _Zone: 实例所属可用区， 如：ap-guangzhou-3，对应ZoneSet的Zone字段。
        :type Zone: str
        :param _VpcId: 私有网络ID，形如vpc-e6w23k31。有效的VpcId可通过登录控制台查询；也可以调用接口 [DescribeVpcs](https://cloud.tencent.com/document/api/215/15778) ，从接口返回中的unVpcId字段获取。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如subnet-51lcif9y。有效的私有网络子网ID可通过登录控制台查询；也可以调用接口 [DescribeSubnets ](https://cloud.tencent.com/document/api/215/15784)，从接口返回中的unSubnetId字段获取。
        :type SubnetId: str
        :param _DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param _DBInstanceName: 实例名称。
        :type DBInstanceName: str
        :param _DBInstanceStatus: 实例状态，分别为：applying（申请中）、init(待初始化)、initing(初始化中)、running(运行中)、limited run（受限运行）、isolating（隔离中）、isolated（已隔离）、disisolating（解隔离中）、recycling（回收中）、recycled（已回收）、job running（任务执行中）、offline（下线）、migrating（迁移中）、expanding（扩容中）、waitSwitch（等待切换）、switching（切换中）、readonly（只读）、restarting（重启中）、network changing（网络变更中）、upgrading（内核版本升级中）、audit-switching（审计状态变更中）、primary-switching（主备切换中）、offlining(下线中)、deployment changing（可用区变更中）、cloning（恢复数据中）、parameter modifying（参数修改中）、log-switching（日志状态变更中）、restoring（恢复中）、expanding（变配中）
        :type DBInstanceStatus: str
        :param _DBInstanceMemory: 实例分配的内存大小，单位：GB
        :type DBInstanceMemory: int
        :param _DBInstanceStorage: 实例分配的存储空间大小，单位：GB
        :type DBInstanceStorage: int
        :param _DBInstanceCpu: 实例分配的CPU数量，单位：个
        :type DBInstanceCpu: int
        :param _DBInstanceClass: 售卖规格ID
        :type DBInstanceClass: str
        :param _DBMajorVersion: PostgreSQL大版本号，版本信息可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)获取，目前支持10，11，12，13，14，15这几个大版本。
        :type DBMajorVersion: str
        :param _DBVersion: PostgreSQL社区大版本+小版本号，如12.4，版本信息可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)获取。
        :type DBVersion: str
        :param _DBKernelVersion: PostgreSQL内核版本号，如v12.7_r1.8，版本信息可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)获取。
        :type DBKernelVersion: str
        :param _DBInstanceType: 实例类型，类型有：
<li>primary：主实例</li>
<li>readonly：只读实例</li>
<li>guard：灾备实例</li>
<li>temp：临时实例</li>
        :type DBInstanceType: str
        :param _DBInstanceVersion: 实例版本，目前只支持standard（双机高可用版, 一主一从）。
        :type DBInstanceVersion: str
        :param _DBCharset: 实例字符集，目前只支持：
<li> UTF8</li>
<li> LATIN1</li>
        :type DBCharset: str
        :param _CreateTime: 实例创建时间。
        :type CreateTime: str
        :param _UpdateTime: 实例执行最后一次更新的时间。
        :type UpdateTime: str
        :param _ExpireTime: 实例到期时间。
        :type ExpireTime: str
        :param _IsolatedTime: 实例隔离时间。
        :type IsolatedTime: str
        :param _PayType: 计费模式：
<li>prepaid：包年包月,预付费</li>
<li>postpaid：按量计费，后付费</li>
        :type PayType: str
        :param _AutoRenew: 是否自动续费：
<li>0：手动续费</li>
<li>1：自动续费</li>
默认值：0
        :type AutoRenew: int
        :param _DBInstanceNetInfo: 实例网络连接信息。
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param _Type: 机器类型。
        :type Type: str
        :param _AppId: 用户的AppId。
        :type AppId: int
        :param _Uid: 实例的Uid。
        :type Uid: int
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _TagList: 实例绑定的标签信息。
        :type TagList: list of Tag
        :param _MasterDBInstanceId: 主实例信息，仅在实例为只读实例时返回。
        :type MasterDBInstanceId: str
        :param _ReadOnlyInstanceNum: 只读实例数量。
        :type ReadOnlyInstanceNum: int
        :param _StatusInReadonlyGroup: 只读实例在只读组中的状态。
        :type StatusInReadonlyGroup: str
        :param _OfflineTime: 下线时间。
        :type OfflineTime: str
        :param _DBNodeSet: 实例的节点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DBNodeSet: list of DBNode
        :param _IsSupportTDE: 实例是否支持TDE数据加密：
<li>0：不支持</li>
<li>1：支持</li>
默认值：0
TDE数据加密可参考[数据透明加密概述](https://cloud.tencent.com/document/product/409/71748)
        :type IsSupportTDE: int
        :param _DBEngine: 数据库引擎，支持：
<li>postgresql：云数据库PostgreSQL</li>
<li>mssql_compatible：MSSQL兼容-云数据库PostgreSQL</li>
默认值：postgresql
        :type DBEngine: str
        :param _DBEngineConfig: 数据库引擎的配置信息，配置格式如下：
{"$key1":"$value1", "$key2":"$value2"}
各引擎支持如下：
mssql_compatible引擎：
<li>migrationMode：数据库模式，可选参数，可取值：single-db（单数据库模式），multi-db（多数据库模式）。默认为single-db。</li>
<li>defaultLocale：排序区域规则，可选参数，在初始化后不可修改，默认为en_US，可选值如下：
"af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN"。</li>
<li>serverCollationName：排序规则名称，可选参数，在初始化后不可修改，默认为sql_latin1_general_cp1_ci_as，可选值如下："bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as"。</li>
        :type DBEngineConfig: str
        :param _NetworkAccessList: 实例网络信息列表（此字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAccessList: list of NetworkAccess
        :param _SupportIpv6: 实例是否支持Ipv6：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :type SupportIpv6: int
        :param _ExpandedCpu: 实例已经弹性扩容的cpu核数
        :type ExpandedCpu: int
        :param _DeletionProtection: 实例是否开启删除保护，取值如下：
- true：开启删除保护
- false：关闭删除保护
        :type DeletionProtection: bool
        """
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._DBInstanceId = None
        self._DBInstanceName = None
        self._DBInstanceStatus = None
        self._DBInstanceMemory = None
        self._DBInstanceStorage = None
        self._DBInstanceCpu = None
        self._DBInstanceClass = None
        self._DBMajorVersion = None
        self._DBVersion = None
        self._DBKernelVersion = None
        self._DBInstanceType = None
        self._DBInstanceVersion = None
        self._DBCharset = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ExpireTime = None
        self._IsolatedTime = None
        self._PayType = None
        self._AutoRenew = None
        self._DBInstanceNetInfo = None
        self._Type = None
        self._AppId = None
        self._Uid = None
        self._ProjectId = None
        self._TagList = None
        self._MasterDBInstanceId = None
        self._ReadOnlyInstanceNum = None
        self._StatusInReadonlyGroup = None
        self._OfflineTime = None
        self._DBNodeSet = None
        self._IsSupportTDE = None
        self._DBEngine = None
        self._DBEngineConfig = None
        self._NetworkAccessList = None
        self._SupportIpv6 = None
        self._ExpandedCpu = None
        self._DeletionProtection = None

    @property
    def Region(self):
        r"""实例所属地域，如: ap-guangzhou，对应RegionSet的Region字段。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""实例所属可用区， 如：ap-guangzhou-3，对应ZoneSet的Zone字段。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""私有网络ID，形如vpc-e6w23k31。有效的VpcId可通过登录控制台查询；也可以调用接口 [DescribeVpcs](https://cloud.tencent.com/document/api/215/15778) ，从接口返回中的unVpcId字段获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络子网ID，形如subnet-51lcif9y。有效的私有网络子网ID可通过登录控制台查询；也可以调用接口 [DescribeSubnets ](https://cloud.tencent.com/document/api/215/15784)，从接口返回中的unSubnetId字段获取。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DBInstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DBInstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._DBInstanceName

    @DBInstanceName.setter
    def DBInstanceName(self, DBInstanceName):
        self._DBInstanceName = DBInstanceName

    @property
    def DBInstanceStatus(self):
        r"""实例状态，分别为：applying（申请中）、init(待初始化)、initing(初始化中)、running(运行中)、limited run（受限运行）、isolating（隔离中）、isolated（已隔离）、disisolating（解隔离中）、recycling（回收中）、recycled（已回收）、job running（任务执行中）、offline（下线）、migrating（迁移中）、expanding（扩容中）、waitSwitch（等待切换）、switching（切换中）、readonly（只读）、restarting（重启中）、network changing（网络变更中）、upgrading（内核版本升级中）、audit-switching（审计状态变更中）、primary-switching（主备切换中）、offlining(下线中)、deployment changing（可用区变更中）、cloning（恢复数据中）、parameter modifying（参数修改中）、log-switching（日志状态变更中）、restoring（恢复中）、expanding（变配中）
        :rtype: str
        """
        return self._DBInstanceStatus

    @DBInstanceStatus.setter
    def DBInstanceStatus(self, DBInstanceStatus):
        self._DBInstanceStatus = DBInstanceStatus

    @property
    def DBInstanceMemory(self):
        r"""实例分配的内存大小，单位：GB
        :rtype: int
        """
        return self._DBInstanceMemory

    @DBInstanceMemory.setter
    def DBInstanceMemory(self, DBInstanceMemory):
        self._DBInstanceMemory = DBInstanceMemory

    @property
    def DBInstanceStorage(self):
        r"""实例分配的存储空间大小，单位：GB
        :rtype: int
        """
        return self._DBInstanceStorage

    @DBInstanceStorage.setter
    def DBInstanceStorage(self, DBInstanceStorage):
        self._DBInstanceStorage = DBInstanceStorage

    @property
    def DBInstanceCpu(self):
        r"""实例分配的CPU数量，单位：个
        :rtype: int
        """
        return self._DBInstanceCpu

    @DBInstanceCpu.setter
    def DBInstanceCpu(self, DBInstanceCpu):
        self._DBInstanceCpu = DBInstanceCpu

    @property
    def DBInstanceClass(self):
        r"""售卖规格ID
        :rtype: str
        """
        return self._DBInstanceClass

    @DBInstanceClass.setter
    def DBInstanceClass(self, DBInstanceClass):
        self._DBInstanceClass = DBInstanceClass

    @property
    def DBMajorVersion(self):
        r"""PostgreSQL大版本号，版本信息可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)获取，目前支持10，11，12，13，14，15这几个大版本。
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBVersion(self):
        r"""PostgreSQL社区大版本+小版本号，如12.4，版本信息可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)获取。
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def DBKernelVersion(self):
        r"""PostgreSQL内核版本号，如v12.7_r1.8，版本信息可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)获取。
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def DBInstanceType(self):
        r"""实例类型，类型有：
<li>primary：主实例</li>
<li>readonly：只读实例</li>
<li>guard：灾备实例</li>
<li>temp：临时实例</li>
        :rtype: str
        """
        return self._DBInstanceType

    @DBInstanceType.setter
    def DBInstanceType(self, DBInstanceType):
        self._DBInstanceType = DBInstanceType

    @property
    def DBInstanceVersion(self):
        r"""实例版本，目前只支持standard（双机高可用版, 一主一从）。
        :rtype: str
        """
        return self._DBInstanceVersion

    @DBInstanceVersion.setter
    def DBInstanceVersion(self, DBInstanceVersion):
        self._DBInstanceVersion = DBInstanceVersion

    @property
    def DBCharset(self):
        r"""实例字符集，目前只支持：
<li> UTF8</li>
<li> LATIN1</li>
        :rtype: str
        """
        return self._DBCharset

    @DBCharset.setter
    def DBCharset(self, DBCharset):
        self._DBCharset = DBCharset

    @property
    def CreateTime(self):
        r"""实例创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""实例执行最后一次更新的时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ExpireTime(self):
        r"""实例到期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsolatedTime(self):
        r"""实例隔离时间。
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def PayType(self):
        r"""计费模式：
<li>prepaid：包年包月,预付费</li>
<li>postpaid：按量计费，后付费</li>
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def AutoRenew(self):
        r"""是否自动续费：
<li>0：手动续费</li>
<li>1：自动续费</li>
默认值：0
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def DBInstanceNetInfo(self):
        r"""实例网络连接信息。
        :rtype: list of DBInstanceNetInfo
        """
        return self._DBInstanceNetInfo

    @DBInstanceNetInfo.setter
    def DBInstanceNetInfo(self, DBInstanceNetInfo):
        self._DBInstanceNetInfo = DBInstanceNetInfo

    @property
    def Type(self):
        r"""机器类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppId(self):
        r"""用户的AppId。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uid(self):
        r"""实例的Uid。
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def ProjectId(self):
        r"""项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagList(self):
        r"""实例绑定的标签信息。
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def MasterDBInstanceId(self):
        r"""主实例信息，仅在实例为只读实例时返回。
        :rtype: str
        """
        return self._MasterDBInstanceId

    @MasterDBInstanceId.setter
    def MasterDBInstanceId(self, MasterDBInstanceId):
        self._MasterDBInstanceId = MasterDBInstanceId

    @property
    def ReadOnlyInstanceNum(self):
        r"""只读实例数量。
        :rtype: int
        """
        return self._ReadOnlyInstanceNum

    @ReadOnlyInstanceNum.setter
    def ReadOnlyInstanceNum(self, ReadOnlyInstanceNum):
        self._ReadOnlyInstanceNum = ReadOnlyInstanceNum

    @property
    def StatusInReadonlyGroup(self):
        r"""只读实例在只读组中的状态。
        :rtype: str
        """
        return self._StatusInReadonlyGroup

    @StatusInReadonlyGroup.setter
    def StatusInReadonlyGroup(self, StatusInReadonlyGroup):
        self._StatusInReadonlyGroup = StatusInReadonlyGroup

    @property
    def OfflineTime(self):
        r"""下线时间。
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def DBNodeSet(self):
        r"""实例的节点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DBNode
        """
        return self._DBNodeSet

    @DBNodeSet.setter
    def DBNodeSet(self, DBNodeSet):
        self._DBNodeSet = DBNodeSet

    @property
    def IsSupportTDE(self):
        r"""实例是否支持TDE数据加密：
<li>0：不支持</li>
<li>1：支持</li>
默认值：0
TDE数据加密可参考[数据透明加密概述](https://cloud.tencent.com/document/product/409/71748)
        :rtype: int
        """
        return self._IsSupportTDE

    @IsSupportTDE.setter
    def IsSupportTDE(self, IsSupportTDE):
        self._IsSupportTDE = IsSupportTDE

    @property
    def DBEngine(self):
        r"""数据库引擎，支持：
<li>postgresql：云数据库PostgreSQL</li>
<li>mssql_compatible：MSSQL兼容-云数据库PostgreSQL</li>
默认值：postgresql
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def DBEngineConfig(self):
        r"""数据库引擎的配置信息，配置格式如下：
{"$key1":"$value1", "$key2":"$value2"}
各引擎支持如下：
mssql_compatible引擎：
<li>migrationMode：数据库模式，可选参数，可取值：single-db（单数据库模式），multi-db（多数据库模式）。默认为single-db。</li>
<li>defaultLocale：排序区域规则，可选参数，在初始化后不可修改，默认为en_US，可选值如下：
"af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN"。</li>
<li>serverCollationName：排序规则名称，可选参数，在初始化后不可修改，默认为sql_latin1_general_cp1_ci_as，可选值如下："bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as"。</li>
        :rtype: str
        """
        return self._DBEngineConfig

    @DBEngineConfig.setter
    def DBEngineConfig(self, DBEngineConfig):
        self._DBEngineConfig = DBEngineConfig

    @property
    def NetworkAccessList(self):
        r"""实例网络信息列表（此字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of NetworkAccess
        """
        return self._NetworkAccessList

    @NetworkAccessList.setter
    def NetworkAccessList(self, NetworkAccessList):
        self._NetworkAccessList = NetworkAccessList

    @property
    def SupportIpv6(self):
        r"""实例是否支持Ipv6：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :rtype: int
        """
        return self._SupportIpv6

    @SupportIpv6.setter
    def SupportIpv6(self, SupportIpv6):
        self._SupportIpv6 = SupportIpv6

    @property
    def ExpandedCpu(self):
        r"""实例已经弹性扩容的cpu核数
        :rtype: int
        """
        return self._ExpandedCpu

    @ExpandedCpu.setter
    def ExpandedCpu(self, ExpandedCpu):
        self._ExpandedCpu = ExpandedCpu

    @property
    def DeletionProtection(self):
        r"""实例是否开启删除保护，取值如下：
- true：开启删除保护
- false：关闭删除保护
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DBInstanceId = params.get("DBInstanceId")
        self._DBInstanceName = params.get("DBInstanceName")
        self._DBInstanceStatus = params.get("DBInstanceStatus")
        self._DBInstanceMemory = params.get("DBInstanceMemory")
        self._DBInstanceStorage = params.get("DBInstanceStorage")
        self._DBInstanceCpu = params.get("DBInstanceCpu")
        self._DBInstanceClass = params.get("DBInstanceClass")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBVersion = params.get("DBVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._DBInstanceType = params.get("DBInstanceType")
        self._DBInstanceVersion = params.get("DBInstanceVersion")
        self._DBCharset = params.get("DBCharset")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._IsolatedTime = params.get("IsolatedTime")
        self._PayType = params.get("PayType")
        self._AutoRenew = params.get("AutoRenew")
        if params.get("DBInstanceNetInfo") is not None:
            self._DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self._DBInstanceNetInfo.append(obj)
        self._Type = params.get("Type")
        self._AppId = params.get("AppId")
        self._Uid = params.get("Uid")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._MasterDBInstanceId = params.get("MasterDBInstanceId")
        self._ReadOnlyInstanceNum = params.get("ReadOnlyInstanceNum")
        self._StatusInReadonlyGroup = params.get("StatusInReadonlyGroup")
        self._OfflineTime = params.get("OfflineTime")
        if params.get("DBNodeSet") is not None:
            self._DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self._DBNodeSet.append(obj)
        self._IsSupportTDE = params.get("IsSupportTDE")
        self._DBEngine = params.get("DBEngine")
        self._DBEngineConfig = params.get("DBEngineConfig")
        if params.get("NetworkAccessList") is not None:
            self._NetworkAccessList = []
            for item in params.get("NetworkAccessList"):
                obj = NetworkAccess()
                obj._deserialize(item)
                self._NetworkAccessList.append(obj)
        self._SupportIpv6 = params.get("SupportIpv6")
        self._ExpandedCpu = params.get("ExpandedCpu")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstanceNetInfo(AbstractModel):
    r"""描述实例的网络连接信息。

    """

    def __init__(self):
        r"""
        :param _Address: DNS域名
        :type Address: str
        :param _Ip: IP地址
        :type Ip: str
        :param _Port: 连接Port地址
        :type Port: int
        :param _NetType: 网络类型，1、inner（基础网络内网地址）；2、private（私有网络内网地址）；3、public（基础网络或私有网络的外网地址）；
        :type NetType: str
        :param _Status: 网络连接状态，1、initing（未开通）；2、opened（已开通）；3、closed（已关闭）；4、opening（开通中）；5、closing（关闭中）；
        :type Status: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _ProtocolType: 连接数据库的协议类型，当前支持：postgresql、mssql（MSSQL兼容语法）
        :type ProtocolType: str
        """
        self._Address = None
        self._Ip = None
        self._Port = None
        self._NetType = None
        self._Status = None
        self._VpcId = None
        self._SubnetId = None
        self._ProtocolType = None

    @property
    def Address(self):
        r"""DNS域名
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Ip(self):
        r"""IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""连接Port地址
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NetType(self):
        r"""网络类型，1、inner（基础网络内网地址）；2、private（私有网络内网地址）；3、public（基础网络或私有网络的外网地址）；
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Status(self):
        r"""网络连接状态，1、initing（未开通）；2、opened（已开通）；3、closed（已关闭）；4、opening（开通中）；5、closing（关闭中）；
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VpcId(self):
        r"""私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProtocolType(self):
        r"""连接数据库的协议类型，当前支持：postgresql、mssql（MSSQL兼容语法）
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._NetType = params.get("NetType")
        self._Status = params.get("Status")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProtocolType = params.get("ProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBNode(AbstractModel):
    r"""描述实例节点信息，包括节点类型、节点所在可用区、节点所在专属集群。

    """

    def __init__(self):
        r"""
        :param _Role: 节点类型，值可以为：
Primary，代表主节点；
Standby，代表备节点。
        :type Role: str
        :param _Zone: 节点所在可用区，例如 ap-guangzhou-1。
        :type Zone: str
        :param _DedicatedClusterId: 专属集群ID
        :type DedicatedClusterId: str
        """
        self._Role = None
        self._Zone = None
        self._DedicatedClusterId = None

    @property
    def Role(self):
        r"""节点类型，值可以为：
Primary，代表主节点；
Standby，代表备节点。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Zone(self):
        r"""节点所在可用区，例如 ap-guangzhou-1。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DedicatedClusterId(self):
        r"""专属集群ID
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Zone = params.get("Zone")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    r"""描述数据库详细信息，包括所有者、字符编码等

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名
        :type DatabaseName: str
        :param _DatabaseOwner: 数据库所有者
        :type DatabaseOwner: str
        :param _Encoding: 数据库字符编码
        :type Encoding: str
        :param _Collate: 数据库排序规则
        :type Collate: str
        :param _Ctype: 数据库字符分类
        :type Ctype: str
        :param _AllowConn: 数据库是否允许连接
        :type AllowConn: bool
        :param _ConnLimit: 数据库最大连接数，-1表示无限制
        :type ConnLimit: int
        :param _Privileges: 数据库权限列表
        :type Privileges: str
        """
        self._DatabaseName = None
        self._DatabaseOwner = None
        self._Encoding = None
        self._Collate = None
        self._Ctype = None
        self._AllowConn = None
        self._ConnLimit = None
        self._Privileges = None

    @property
    def DatabaseName(self):
        r"""数据库名
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatabaseOwner(self):
        r"""数据库所有者
        :rtype: str
        """
        return self._DatabaseOwner

    @DatabaseOwner.setter
    def DatabaseOwner(self, DatabaseOwner):
        self._DatabaseOwner = DatabaseOwner

    @property
    def Encoding(self):
        r"""数据库字符编码
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Collate(self):
        r"""数据库排序规则
        :rtype: str
        """
        return self._Collate

    @Collate.setter
    def Collate(self, Collate):
        self._Collate = Collate

    @property
    def Ctype(self):
        r"""数据库字符分类
        :rtype: str
        """
        return self._Ctype

    @Ctype.setter
    def Ctype(self, Ctype):
        self._Ctype = Ctype

    @property
    def AllowConn(self):
        r"""数据库是否允许连接
        :rtype: bool
        """
        return self._AllowConn

    @AllowConn.setter
    def AllowConn(self, AllowConn):
        self._AllowConn = AllowConn

    @property
    def ConnLimit(self):
        r"""数据库最大连接数，-1表示无限制
        :rtype: int
        """
        return self._ConnLimit

    @ConnLimit.setter
    def ConnLimit(self, ConnLimit):
        self._ConnLimit = ConnLimit

    @property
    def Privileges(self):
        r"""数据库权限列表
        :rtype: str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._DatabaseOwner = params.get("DatabaseOwner")
        self._Encoding = params.get("Encoding")
        self._Collate = params.get("Collate")
        self._Ctype = params.get("Ctype")
        self._AllowConn = params.get("AllowConn")
        self._ConnLimit = params.get("ConnLimit")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseObject(AbstractModel):
    r"""描述数据库中某个对象所属的类型、是在哪个数据库、模式、表中的对象。

    """

    def __init__(self):
        r"""
        :param _ObjectType: 支持使用的数据库对象类型有：account,database,schema,sequence,procedure,type,function,table,view,matview,column。
        :type ObjectType: str
        :param _ObjectName: 所描述的数据库对象名称
        :type ObjectName: str
        :param _DatabaseName: 所要描述的数据库对象，所属的数据库名称。当描述对象类型不为database时，此参数必选。
        :type DatabaseName: str
        :param _SchemaName: 所要描述的数据库对象，所属的模式名称。当描述对象不为database、schema时，此参数必选。
        :type SchemaName: str
        :param _TableName: 所要描述的数据库对象，所属的表名称。当描述的对象类型为column时，此参数必填。
        :type TableName: str
        """
        self._ObjectType = None
        self._ObjectName = None
        self._DatabaseName = None
        self._SchemaName = None
        self._TableName = None

    @property
    def ObjectType(self):
        r"""支持使用的数据库对象类型有：account,database,schema,sequence,procedure,type,function,table,view,matview,column。
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def ObjectName(self):
        r"""所描述的数据库对象名称
        :rtype: str
        """
        return self._ObjectName

    @ObjectName.setter
    def ObjectName(self, ObjectName):
        self._ObjectName = ObjectName

    @property
    def DatabaseName(self):
        r"""所要描述的数据库对象，所属的数据库名称。当描述对象类型不为database时，此参数必选。
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SchemaName(self):
        r"""所要描述的数据库对象，所属的模式名称。当描述对象不为database、schema时，此参数必选。
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableName(self):
        r"""所要描述的数据库对象，所属的表名称。当描述的对象类型为column时，此参数必填。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._ObjectType = params.get("ObjectType")
        self._ObjectName = params.get("ObjectName")
        self._DatabaseName = params.get("DatabaseName")
        self._SchemaName = params.get("SchemaName")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    r"""指定账号对数据库对象拥有的权限列表

    """

    def __init__(self):
        r"""
        :param _Object: 数据库对象，当ObjectType为database时，DatabaseName/SchemaName/TableName可为空；当ObjectType为schema时，SchemaName/TableName可为空；当ObjectType为column时，TableName不可为空，其余情况均可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Object: :class:`tencentcloud.postgres.v20170312.models.DatabaseObject`
        :param _PrivilegeSet: 指定账号对数据库对象拥有的权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivilegeSet: list of str
        """
        self._Object = None
        self._PrivilegeSet = None

    @property
    def Object(self):
        r"""数据库对象，当ObjectType为database时，DatabaseName/SchemaName/TableName可为空；当ObjectType为schema时，SchemaName/TableName可为空；当ObjectType为column时，TableName不可为空，其余情况均可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DatabaseObject`
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def PrivilegeSet(self):
        r"""指定账号对数据库对象拥有的权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PrivilegeSet

    @PrivilegeSet.setter
    def PrivilegeSet(self, PrivilegeSet):
        self._PrivilegeSet = PrivilegeSet


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self._Object = DatabaseObject()
            self._Object._deserialize(params.get("Object"))
        self._PrivilegeSet = params.get("PrivilegeSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedCluster(AbstractModel):
    r"""专属集群相关信息，用于查询用户的专属集群列表

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 专属集群ID
        :type DedicatedClusterId: str
        :param _Name: 专属集群名称
        :type Name: str
        :param _Zone: 专属集群所在可用区
        :type Zone: str
        :param _StandbyDedicatedClusterSet: 灾备集群
        :type StandbyDedicatedClusterSet: list of str
        :param _InstanceCount: 实例数量
        :type InstanceCount: int
        :param _CpuTotal: Cpu总数量
        :type CpuTotal: int
        :param _CpuAvailable: Cpu可用数量
        :type CpuAvailable: int
        :param _MemTotal: 内存总量，单位GB
        :type MemTotal: int
        :param _MemAvailable: 内存可用量，单位GB
        :type MemAvailable: int
        :param _DiskTotal: 磁盘总量，单位GB
        :type DiskTotal: int
        :param _DiskAvailable: 磁盘可用量，单位GB
        :type DiskAvailable: int
        """
        self._DedicatedClusterId = None
        self._Name = None
        self._Zone = None
        self._StandbyDedicatedClusterSet = None
        self._InstanceCount = None
        self._CpuTotal = None
        self._CpuAvailable = None
        self._MemTotal = None
        self._MemAvailable = None
        self._DiskTotal = None
        self._DiskAvailable = None

    @property
    def DedicatedClusterId(self):
        r"""专属集群ID
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Name(self):
        r"""专属集群名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        r"""专属集群所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def StandbyDedicatedClusterSet(self):
        r"""灾备集群
        :rtype: list of str
        """
        return self._StandbyDedicatedClusterSet

    @StandbyDedicatedClusterSet.setter
    def StandbyDedicatedClusterSet(self, StandbyDedicatedClusterSet):
        self._StandbyDedicatedClusterSet = StandbyDedicatedClusterSet

    @property
    def InstanceCount(self):
        r"""实例数量
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def CpuTotal(self):
        r"""Cpu总数量
        :rtype: int
        """
        return self._CpuTotal

    @CpuTotal.setter
    def CpuTotal(self, CpuTotal):
        self._CpuTotal = CpuTotal

    @property
    def CpuAvailable(self):
        r"""Cpu可用数量
        :rtype: int
        """
        return self._CpuAvailable

    @CpuAvailable.setter
    def CpuAvailable(self, CpuAvailable):
        self._CpuAvailable = CpuAvailable

    @property
    def MemTotal(self):
        r"""内存总量，单位GB
        :rtype: int
        """
        return self._MemTotal

    @MemTotal.setter
    def MemTotal(self, MemTotal):
        self._MemTotal = MemTotal

    @property
    def MemAvailable(self):
        r"""内存可用量，单位GB
        :rtype: int
        """
        return self._MemAvailable

    @MemAvailable.setter
    def MemAvailable(self, MemAvailable):
        self._MemAvailable = MemAvailable

    @property
    def DiskTotal(self):
        r"""磁盘总量，单位GB
        :rtype: int
        """
        return self._DiskTotal

    @DiskTotal.setter
    def DiskTotal(self, DiskTotal):
        self._DiskTotal = DiskTotal

    @property
    def DiskAvailable(self):
        r"""磁盘可用量，单位GB
        :rtype: int
        """
        return self._DiskAvailable

    @DiskAvailable.setter
    def DiskAvailable(self, DiskAvailable):
        self._DiskAvailable = DiskAvailable


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._StandbyDedicatedClusterSet = params.get("StandbyDedicatedClusterSet")
        self._InstanceCount = params.get("InstanceCount")
        self._CpuTotal = params.get("CpuTotal")
        self._CpuAvailable = params.get("CpuAvailable")
        self._MemTotal = params.get("MemTotal")
        self._MemAvailable = params.get("MemAvailable")
        self._DiskTotal = params.get("DiskTotal")
        self._DiskAvailable = params.get("DiskAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    r"""DeleteAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _UserName: 删除的账号名称。	可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :type UserName: str
        """
        self._DBInstanceId = None
        self._UserName = None

    @property
    def DBInstanceId(self):
        r"""实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""删除的账号名称。	可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    r"""DeleteAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteBackupPlanRequest(AbstractModel):
    r"""DeleteBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _PlanId: 备份计划的ID。可通过[DescribeBackupPlans](https://cloud.tencent.com/document/api/409/68069)接口获取
        :type PlanId: str
        """
        self._DBInstanceId = None
        self._PlanId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def PlanId(self):
        r"""备份计划的ID。可通过[DescribeBackupPlans](https://cloud.tencent.com/document/api/409/68069)接口获取
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupPlanResponse(AbstractModel):
    r"""DeleteBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteBaseBackupRequest(AbstractModel):
    r"""DeleteBaseBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _BaseBackupId: 数据备份ID。可通过[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)接口获取。7天内自动备份集不允许删除。
        :type BaseBackupId: str
        """
        self._DBInstanceId = None
        self._BaseBackupId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def BaseBackupId(self):
        r"""数据备份ID。可通过[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)接口获取。7天内自动备份集不允许删除。
        :rtype: str
        """
        return self._BaseBackupId

    @BaseBackupId.setter
    def BaseBackupId(self, BaseBackupId):
        self._BaseBackupId = BaseBackupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._BaseBackupId = params.get("BaseBackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBaseBackupResponse(AbstractModel):
    r"""DeleteBaseBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDBInstanceNetworkAccessRequest(AbstractModel):
    r"""DeleteDBInstanceNetworkAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如：postgres-6bwgamo3。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _VpcId: 私有网络统一 ID，若是基础网络则传"0"。
        :type VpcId: str
        :param _SubnetId: 子网ID，若是基础网络则传"0"。
        :type SubnetId: str
        :param _Vip: 目标VIP地址。
        :type Vip: str
        """
        self._DBInstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如：postgres-6bwgamo3。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def VpcId(self):
        r"""私有网络统一 ID，若是基础网络则传"0"。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID，若是基础网络则传"0"。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        r"""目标VIP地址。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBInstanceNetworkAccessResponse(AbstractModel):
    r"""DeleteDBInstanceNetworkAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteLogBackupRequest(AbstractModel):
    r"""DeleteLogBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _LogBackupId: 日志备份ID。可通过[DescribeLogBackups](https://cloud.tencent.com/document/api/409/89021)接口获取。注：7天内自动备份集不允许删除。
        :type LogBackupId: str
        """
        self._DBInstanceId = None
        self._LogBackupId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def LogBackupId(self):
        r"""日志备份ID。可通过[DescribeLogBackups](https://cloud.tencent.com/document/api/409/89021)接口获取。注：7天内自动备份集不允许删除。
        :rtype: str
        """
        return self._LogBackupId

    @LogBackupId.setter
    def LogBackupId(self, LogBackupId):
        self._LogBackupId = LogBackupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._LogBackupId = params.get("LogBackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogBackupResponse(AbstractModel):
    r"""DeleteLogBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteParameterTemplateRequest(AbstractModel):
    r"""DeleteParameterTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID，用于唯一确认待操作的参数模板。可通过[DescribeParameterTemplates](https://cloud.tencent.com/document/api/409/84067)接口获取
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""参数模板ID，用于唯一确认待操作的参数模板。可通过[DescribeParameterTemplates](https://cloud.tencent.com/document/api/409/84067)接口获取
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParameterTemplateResponse(AbstractModel):
    r"""DeleteParameterTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteReadOnlyGroupNetworkAccessRequest(AbstractModel):
    r"""DeleteReadOnlyGroupNetworkAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: RO组ID，形如：pgrogrp-4t9c6g7k。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :type ReadOnlyGroupId: str
        :param _VpcId: 私有网络统一 ID，若是基础网络则传"0"。
        :type VpcId: str
        :param _SubnetId: 子网ID，若是基础网络则传"0"。
        :type SubnetId: str
        :param _Vip: 目标VIP地址。
        :type Vip: str
        """
        self._ReadOnlyGroupId = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None

    @property
    def ReadOnlyGroupId(self):
        r"""RO组ID，形如：pgrogrp-4t9c6g7k。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def VpcId(self):
        r"""私有网络统一 ID，若是基础网络则传"0"。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID，若是基础网络则传"0"。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        r"""目标VIP地址。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReadOnlyGroupNetworkAccessResponse(AbstractModel):
    r"""DeleteReadOnlyGroupNetworkAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteReadOnlyGroupRequest(AbstractModel):
    r"""DeleteReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 待删除只读组ID
        :type ReadOnlyGroupId: str
        """
        self._ReadOnlyGroupId = None

    @property
    def ReadOnlyGroupId(self):
        r"""待删除只读组ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReadOnlyGroupResponse(AbstractModel):
    r"""DeleteReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    r"""DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _UserName: 查询此账号对某数据库对象所拥有的权限信息。账号名可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :type UserName: str
        :param _DatabaseObjectSet: 要查询的数据库对象信息
        :type DatabaseObjectSet: list of DatabaseObject
        """
        self._DBInstanceId = None
        self._UserName = None
        self._DatabaseObjectSet = None

    @property
    def DBInstanceId(self):
        r"""实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""查询此账号对某数据库对象所拥有的权限信息。账号名可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DatabaseObjectSet(self):
        r"""要查询的数据库对象信息
        :rtype: list of DatabaseObject
        """
        return self._DatabaseObjectSet

    @DatabaseObjectSet.setter
    def DatabaseObjectSet(self, DatabaseObjectSet):
        self._DatabaseObjectSet = DatabaseObjectSet


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        if params.get("DatabaseObjectSet") is not None:
            self._DatabaseObjectSet = []
            for item in params.get("DatabaseObjectSet"):
                obj = DatabaseObject()
                obj._deserialize(item)
                self._DatabaseObjectSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    r"""DescribeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PrivilegeSet: 用户拥有数据库user_database的CREATE、CONNECT、TEMPORARY权限
        :type PrivilegeSet: list of DatabasePrivilege
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PrivilegeSet = None
        self._RequestId = None

    @property
    def PrivilegeSet(self):
        r"""用户拥有数据库user_database的CREATE、CONNECT、TEMPORARY权限
        :rtype: list of DatabasePrivilege
        """
        return self._PrivilegeSet

    @PrivilegeSet.setter
    def PrivilegeSet(self, PrivilegeSet):
        self._PrivilegeSet = PrivilegeSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PrivilegeSet") is not None:
            self._PrivilegeSet = []
            for item in params.get("PrivilegeSet"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._PrivilegeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    r"""DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _Limit: 分页返回，每页最大返回数目，默认20，取值范围为1-100
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param _OrderBy: 返回数据按照创建时间或者用户名排序。取值支持createTime、name、updateTime。createTime-按照创建时间排序；name-按照用户名排序; updateTime-按照更新时间排序。
默认值：createTime
        :type OrderBy: str
        :param _OrderByType: 返回结果是升序还是降序。取值只能为desc或者asc。desc-降序；asc-升序
默认值：desc
        :type OrderByType: str
        """
        self._DBInstanceId = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Limit(self):
        r"""分页返回，每页最大返回数目，默认20，取值范围为1-100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""返回数据按照创建时间或者用户名排序。取值支持createTime、name、updateTime。createTime-按照创建时间排序；name-按照用户名排序; updateTime-按照更新时间排序。
默认值：createTime
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""返回结果是升序还是降序。取值只能为desc或者asc。desc-降序；asc-升序
默认值：desc
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    r"""DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 本次调用接口共返回了多少条数据。
        :type TotalCount: int
        :param _Details: 账号列表详细信息。当CreateTime项为0000-00-00 00:00:00时，意味着对应账号是直连数据库创建的，并非通过CreateAccount接口创建。
        :type Details: list of AccountInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""本次调用接口共返回了多少条数据。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        r"""账号列表详细信息。当CreateTime项为0000-00-00 00:00:00时，意味着对应账号是直连数据库创建的，并非通过CreateAccount接口创建。
        :rtype: list of AccountInfo
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = AccountInfo()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAvailableRecoveryTimeRequest(AbstractModel):
    r"""DescribeAvailableRecoveryTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableRecoveryTimeResponse(AbstractModel):
    r"""DescribeAvailableRecoveryTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecoveryBeginTime: 可恢复的最早时间，时区为东八区（UTC+8）。
        :type RecoveryBeginTime: str
        :param _RecoveryEndTime: 可恢复的最晚时间，时区为东八区（UTC+8）。
        :type RecoveryEndTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecoveryBeginTime = None
        self._RecoveryEndTime = None
        self._RequestId = None

    @property
    def RecoveryBeginTime(self):
        r"""可恢复的最早时间，时区为东八区（UTC+8）。
        :rtype: str
        """
        return self._RecoveryBeginTime

    @RecoveryBeginTime.setter
    def RecoveryBeginTime(self, RecoveryBeginTime):
        self._RecoveryBeginTime = RecoveryBeginTime

    @property
    def RecoveryEndTime(self):
        r"""可恢复的最晚时间，时区为东八区（UTC+8）。
        :rtype: str
        """
        return self._RecoveryEndTime

    @RecoveryEndTime.setter
    def RecoveryEndTime(self, RecoveryEndTime):
        self._RecoveryEndTime = RecoveryEndTime

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecoveryBeginTime = params.get("RecoveryBeginTime")
        self._RecoveryEndTime = params.get("RecoveryEndTime")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    r"""DescribeBackupDownloadRestriction请求参数结构体

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    r"""DescribeBackupDownloadRestriction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RestrictionType: 备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。
        :type RestrictionType: str
        :param _VpcRestrictionEffect: vpc限制效力，ALLOW 允许；DENY 拒绝。
        :type VpcRestrictionEffect: str
        :param _VpcIdSet: 允许或拒绝下载备份文件的vpcId列表。
        :type VpcIdSet: list of str
        :param _IpRestrictionEffect: ip限制效力，ALLOW 允许；DENY 拒绝。
        :type IpRestrictionEffect: str
        :param _IpSet: 允许或拒绝下载备份文件的ip列表。
        :type IpSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RestrictionType = None
        self._VpcRestrictionEffect = None
        self._VpcIdSet = None
        self._IpRestrictionEffect = None
        self._IpSet = None
        self._RequestId = None

    @property
    def RestrictionType(self):
        r"""备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。
        :rtype: str
        """
        return self._RestrictionType

    @RestrictionType.setter
    def RestrictionType(self, RestrictionType):
        self._RestrictionType = RestrictionType

    @property
    def VpcRestrictionEffect(self):
        r"""vpc限制效力，ALLOW 允许；DENY 拒绝。
        :rtype: str
        """
        return self._VpcRestrictionEffect

    @VpcRestrictionEffect.setter
    def VpcRestrictionEffect(self, VpcRestrictionEffect):
        self._VpcRestrictionEffect = VpcRestrictionEffect

    @property
    def VpcIdSet(self):
        r"""允许或拒绝下载备份文件的vpcId列表。
        :rtype: list of str
        """
        return self._VpcIdSet

    @VpcIdSet.setter
    def VpcIdSet(self, VpcIdSet):
        self._VpcIdSet = VpcIdSet

    @property
    def IpRestrictionEffect(self):
        r"""ip限制效力，ALLOW 允许；DENY 拒绝。
        :rtype: str
        """
        return self._IpRestrictionEffect

    @IpRestrictionEffect.setter
    def IpRestrictionEffect(self, IpRestrictionEffect):
        self._IpRestrictionEffect = IpRestrictionEffect

    @property
    def IpSet(self):
        r"""允许或拒绝下载备份文件的ip列表。
        :rtype: list of str
        """
        return self._IpSet

    @IpSet.setter
    def IpSet(self, IpSet):
        self._IpSet = IpSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RestrictionType = params.get("RestrictionType")
        self._VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self._VpcIdSet = params.get("VpcIdSet")
        self._IpRestrictionEffect = params.get("IpRestrictionEffect")
        self._IpSet = params.get("IpSet")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadURLRequest(AbstractModel):
    r"""DescribeBackupDownloadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _BackupType: 备份类型，目前支持：LogBackup，BaseBackup。
        :type BackupType: str
        :param _BackupId: 备份的唯一ID。
        :type BackupId: str
        :param _URLExpireTime: 链接的有效时间，取值为[0,36]，默认为12小时。
        :type URLExpireTime: int
        :param _BackupDownloadRestriction: 备份下载限制
        :type BackupDownloadRestriction: :class:`tencentcloud.postgres.v20170312.models.BackupDownloadRestriction`
        """
        self._DBInstanceId = None
        self._BackupType = None
        self._BackupId = None
        self._URLExpireTime = None
        self._BackupDownloadRestriction = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def BackupType(self):
        r"""备份类型，目前支持：LogBackup，BaseBackup。
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupId(self):
        r"""备份的唯一ID。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def URLExpireTime(self):
        r"""链接的有效时间，取值为[0,36]，默认为12小时。
        :rtype: int
        """
        return self._URLExpireTime

    @URLExpireTime.setter
    def URLExpireTime(self, URLExpireTime):
        self._URLExpireTime = URLExpireTime

    @property
    def BackupDownloadRestriction(self):
        r"""备份下载限制
        :rtype: :class:`tencentcloud.postgres.v20170312.models.BackupDownloadRestriction`
        """
        return self._BackupDownloadRestriction

    @BackupDownloadRestriction.setter
    def BackupDownloadRestriction(self, BackupDownloadRestriction):
        self._BackupDownloadRestriction = BackupDownloadRestriction


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._BackupType = params.get("BackupType")
        self._BackupId = params.get("BackupId")
        self._URLExpireTime = params.get("URLExpireTime")
        if params.get("BackupDownloadRestriction") is not None:
            self._BackupDownloadRestriction = BackupDownloadRestriction()
            self._BackupDownloadRestriction._deserialize(params.get("BackupDownloadRestriction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadURLResponse(AbstractModel):
    r"""DescribeBackupDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupDownloadURL: 备份的下载地址。
        :type BackupDownloadURL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupDownloadURL = None
        self._RequestId = None

    @property
    def BackupDownloadURL(self):
        r"""备份的下载地址。
        :rtype: str
        """
        return self._BackupDownloadURL

    @BackupDownloadURL.setter
    def BackupDownloadURL(self, BackupDownloadURL):
        self._BackupDownloadURL = BackupDownloadURL

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupDownloadURL = params.get("BackupDownloadURL")
        self._RequestId = params.get("RequestId")


class DescribeBackupOverviewRequest(AbstractModel):
    r"""DescribeBackupOverview请求参数结构体

    """


class DescribeBackupOverviewResponse(AbstractModel):
    r"""DescribeBackupOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalFreeSize: 总免费空间大小，单位byte。
        :type TotalFreeSize: int
        :param _UsedFreeSize: 已使用免费空间大小，单位byte。
        :type UsedFreeSize: int
        :param _UsedBillingSize: 已使用收费空间大小，单位byte。
        :type UsedBillingSize: int
        :param _LogBackupCount: 日志备份数量。
        :type LogBackupCount: int
        :param _LogBackupSize: 日志备份大小，单位byte。
        :type LogBackupSize: int
        :param _ManualBaseBackupCount: 手动创建的基础备份数量。
        :type ManualBaseBackupCount: int
        :param _ManualBaseBackupSize: 手动创建的基础备份大小，单位byte。
        :type ManualBaseBackupSize: int
        :param _AutoBaseBackupCount: 自动创建的基础备份数量。
        :type AutoBaseBackupCount: int
        :param _AutoBaseBackupSize: 自动创建的基础备份大小，单位byte。
        :type AutoBaseBackupSize: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalFreeSize = None
        self._UsedFreeSize = None
        self._UsedBillingSize = None
        self._LogBackupCount = None
        self._LogBackupSize = None
        self._ManualBaseBackupCount = None
        self._ManualBaseBackupSize = None
        self._AutoBaseBackupCount = None
        self._AutoBaseBackupSize = None
        self._RequestId = None

    @property
    def TotalFreeSize(self):
        r"""总免费空间大小，单位byte。
        :rtype: int
        """
        return self._TotalFreeSize

    @TotalFreeSize.setter
    def TotalFreeSize(self, TotalFreeSize):
        self._TotalFreeSize = TotalFreeSize

    @property
    def UsedFreeSize(self):
        r"""已使用免费空间大小，单位byte。
        :rtype: int
        """
        return self._UsedFreeSize

    @UsedFreeSize.setter
    def UsedFreeSize(self, UsedFreeSize):
        self._UsedFreeSize = UsedFreeSize

    @property
    def UsedBillingSize(self):
        r"""已使用收费空间大小，单位byte。
        :rtype: int
        """
        return self._UsedBillingSize

    @UsedBillingSize.setter
    def UsedBillingSize(self, UsedBillingSize):
        self._UsedBillingSize = UsedBillingSize

    @property
    def LogBackupCount(self):
        r"""日志备份数量。
        :rtype: int
        """
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def LogBackupSize(self):
        r"""日志备份大小，单位byte。
        :rtype: int
        """
        return self._LogBackupSize

    @LogBackupSize.setter
    def LogBackupSize(self, LogBackupSize):
        self._LogBackupSize = LogBackupSize

    @property
    def ManualBaseBackupCount(self):
        r"""手动创建的基础备份数量。
        :rtype: int
        """
        return self._ManualBaseBackupCount

    @ManualBaseBackupCount.setter
    def ManualBaseBackupCount(self, ManualBaseBackupCount):
        self._ManualBaseBackupCount = ManualBaseBackupCount

    @property
    def ManualBaseBackupSize(self):
        r"""手动创建的基础备份大小，单位byte。
        :rtype: int
        """
        return self._ManualBaseBackupSize

    @ManualBaseBackupSize.setter
    def ManualBaseBackupSize(self, ManualBaseBackupSize):
        self._ManualBaseBackupSize = ManualBaseBackupSize

    @property
    def AutoBaseBackupCount(self):
        r"""自动创建的基础备份数量。
        :rtype: int
        """
        return self._AutoBaseBackupCount

    @AutoBaseBackupCount.setter
    def AutoBaseBackupCount(self, AutoBaseBackupCount):
        self._AutoBaseBackupCount = AutoBaseBackupCount

    @property
    def AutoBaseBackupSize(self):
        r"""自动创建的基础备份大小，单位byte。
        :rtype: int
        """
        return self._AutoBaseBackupSize

    @AutoBaseBackupSize.setter
    def AutoBaseBackupSize(self, AutoBaseBackupSize):
        self._AutoBaseBackupSize = AutoBaseBackupSize

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalFreeSize = params.get("TotalFreeSize")
        self._UsedFreeSize = params.get("UsedFreeSize")
        self._UsedBillingSize = params.get("UsedBillingSize")
        self._LogBackupCount = params.get("LogBackupCount")
        self._LogBackupSize = params.get("LogBackupSize")
        self._ManualBaseBackupCount = params.get("ManualBaseBackupCount")
        self._ManualBaseBackupSize = params.get("ManualBaseBackupSize")
        self._AutoBaseBackupCount = params.get("AutoBaseBackupCount")
        self._AutoBaseBackupSize = params.get("AutoBaseBackupSize")
        self._RequestId = params.get("RequestId")


class DescribeBackupPlansRequest(AbstractModel):
    r"""DescribeBackupPlans请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupPlansResponse(AbstractModel):
    r"""DescribeBackupPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Plans: 实例的备份计划集
        :type Plans: list of BackupPlan
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Plans = None
        self._RequestId = None

    @property
    def Plans(self):
        r"""实例的备份计划集
        :rtype: list of BackupPlan
        """
        return self._Plans

    @Plans.setter
    def Plans(self, Plans):
        self._Plans = Plans

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Plans") is not None:
            self._Plans = []
            for item in params.get("Plans"):
                obj = BackupPlan()
                obj._deserialize(item)
                self._Plans.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupSummariesRequest(AbstractModel):
    r"""DescribeBackupSummaries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页显示数量，取值范围为1-100，默认为返回10条。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param _Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，支持模糊匹配，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
        :type Filters: list of Filter
        :param _OrderBy: 排序字段，支持TotalBackupSize - 备份总大小、LogBackupSize - 备份日志的大小、ManualBaseBackupSize - 手动备份数据大小、AutoBaseBackupSize - 自动备份数据大小。当不传入该参数时，默认不进行排序。
        :type OrderBy: str
        :param _OrderByType: 排序方式，包括升序：asc，降序：desc。默认值：asc。
        :type OrderByType: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Limit(self):
        r"""每页显示数量，取值范围为1-100，默认为返回10条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，支持模糊匹配，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""排序字段，支持TotalBackupSize - 备份总大小、LogBackupSize - 备份日志的大小、ManualBaseBackupSize - 手动备份数据大小、AutoBaseBackupSize - 自动备份数据大小。当不传入该参数时，默认不进行排序。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式，包括升序：asc，降序：desc。默认值：asc。
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupSummariesResponse(AbstractModel):
    r"""DescribeBackupSummaries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupSummarySet: 备份统计信息列表。
        :type BackupSummarySet: list of BackupSummary
        :param _TotalCount: 查询到的所有备份信息数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupSummarySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BackupSummarySet(self):
        r"""备份统计信息列表。
        :rtype: list of BackupSummary
        """
        return self._BackupSummarySet

    @BackupSummarySet.setter
    def BackupSummarySet(self, BackupSummarySet):
        self._BackupSummarySet = BackupSummarySet

    @property
    def TotalCount(self):
        r"""查询到的所有备份信息数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackupSummarySet") is not None:
            self._BackupSummarySet = []
            for item in params.get("BackupSummarySet"):
                obj = BackupSummary()
                obj._deserialize(item)
                self._BackupSummarySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBaseBackupsRequest(AbstractModel):
    r"""DescribeBaseBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinFinishTime: 备份的最小结束时间，形如2018-01-01 00:00:00。默认为7天前。
        :type MinFinishTime: str
        :param _MaxFinishTime: 备份的最大结束时间，形如2018-01-01 00:00:00。默认为当前时间。
        :type MaxFinishTime: str
        :param _Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，支持模糊匹配，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
base-backup-id：按照备份集ID过滤，类型为string。
db-instance-status：按实例状态过滤，类型为string。取值参考[DBInstance](https://cloud.tencent.com/document/api/409/16778#DBInstance)结构的DBInstanceStatus字段。
        :type Filters: list of Filter
        :param _Limit: 每页显示数量，取值范围为1-100，默认为返回10条。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param _OrderBy: 排序字段，支持StartTime,FinishTime,Size。默认值：StartTime。
        :type OrderBy: str
        :param _OrderByType: 排序方式，包括升序：asc，降序：desc。默认值：desc。
        :type OrderByType: str
        """
        self._MinFinishTime = None
        self._MaxFinishTime = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def MinFinishTime(self):
        r"""备份的最小结束时间，形如2018-01-01 00:00:00。默认为7天前。
        :rtype: str
        """
        return self._MinFinishTime

    @MinFinishTime.setter
    def MinFinishTime(self, MinFinishTime):
        self._MinFinishTime = MinFinishTime

    @property
    def MaxFinishTime(self):
        r"""备份的最大结束时间，形如2018-01-01 00:00:00。默认为当前时间。
        :rtype: str
        """
        return self._MaxFinishTime

    @MaxFinishTime.setter
    def MaxFinishTime(self, MaxFinishTime):
        self._MaxFinishTime = MaxFinishTime

    @property
    def Filters(self):
        r"""按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，支持模糊匹配，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
base-backup-id：按照备份集ID过滤，类型为string。
db-instance-status：按实例状态过滤，类型为string。取值参考[DBInstance](https://cloud.tencent.com/document/api/409/16778#DBInstance)结构的DBInstanceStatus字段。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""每页显示数量，取值范围为1-100，默认为返回10条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""排序字段，支持StartTime,FinishTime,Size。默认值：StartTime。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式，包括升序：asc，降序：desc。默认值：desc。
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._MinFinishTime = params.get("MinFinishTime")
        self._MaxFinishTime = params.get("MaxFinishTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaseBackupsResponse(AbstractModel):
    r"""DescribeBaseBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的数据备份数量。
        :type TotalCount: int
        :param _BaseBackupSet: 数据备份详细信息列表。
        :type BaseBackupSet: list of BaseBackup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BaseBackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询到的数据备份数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BaseBackupSet(self):
        r"""数据备份详细信息列表。
        :rtype: list of BaseBackup
        """
        return self._BaseBackupSet

    @BaseBackupSet.setter
    def BaseBackupSet(self, BaseBackupSet):
        self._BaseBackupSet = BaseBackupSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BaseBackupSet") is not None:
            self._BaseBackupSet = []
            for item in params.get("BaseBackupSet"):
                obj = BaseBackup()
                obj._deserialize(item)
                self._BaseBackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassesRequest(AbstractModel):
    r"""DescribeClasses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称。可以通过接口[DescribeZones](https://cloud.tencent.com/document/product/409/16769)获取。
        :type Zone: str
        :param _DBEngine: 数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
        :type DBEngine: str
        :param _DBMajorVersion: 数据库主版本号。例如12，13，可以通过接口[DescribeDBVersions](https://cloud.tencent.com/document/product/409/89018)获取。
        :type DBMajorVersion: str
        """
        self._Zone = None
        self._DBEngine = None
        self._DBMajorVersion = None

    @property
    def Zone(self):
        r"""可用区名称。可以通过接口[DescribeZones](https://cloud.tencent.com/document/product/409/16769)获取。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DBEngine(self):
        r"""数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def DBMajorVersion(self):
        r"""数据库主版本号。例如12，13，可以通过接口[DescribeDBVersions](https://cloud.tencent.com/document/product/409/89018)获取。
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DBEngine = params.get("DBEngine")
        self._DBMajorVersion = params.get("DBMajorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassesResponse(AbstractModel):
    r"""DescribeClasses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClassInfoSet: 数据库规格列表
        :type ClassInfoSet: list of ClassInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClassInfoSet = None
        self._RequestId = None

    @property
    def ClassInfoSet(self):
        r"""数据库规格列表
        :rtype: list of ClassInfo
        """
        return self._ClassInfoSet

    @ClassInfoSet.setter
    def ClassInfoSet(self, ClassInfoSet):
        self._ClassInfoSet = ClassInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self._ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self._ClassInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloneDBInstanceSpecRequest(AbstractModel):
    r"""DescribeCloneDBInstanceSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _BackupSetId: 基础备份集ID，可通过[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)接口获取。此入参和RecoveryTargetTime必须选择一个传入。如与RecoveryTargetTime参数同时设置，则以此参数为准。
        :type BackupSetId: str
        :param _RecoveryTargetTime: 恢复目标时间，此入参和BackupSetId必须选择一个传入。时区以东八区（UTC+8）为准。
        :type RecoveryTargetTime: str
        """
        self._DBInstanceId = None
        self._BackupSetId = None
        self._RecoveryTargetTime = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def BackupSetId(self):
        r"""基础备份集ID，可通过[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)接口获取。此入参和RecoveryTargetTime必须选择一个传入。如与RecoveryTargetTime参数同时设置，则以此参数为准。
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def RecoveryTargetTime(self):
        r"""恢复目标时间，此入参和BackupSetId必须选择一个传入。时区以东八区（UTC+8）为准。
        :rtype: str
        """
        return self._RecoveryTargetTime

    @RecoveryTargetTime.setter
    def RecoveryTargetTime(self, RecoveryTargetTime):
        self._RecoveryTargetTime = RecoveryTargetTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._BackupSetId = params.get("BackupSetId")
        self._RecoveryTargetTime = params.get("RecoveryTargetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloneDBInstanceSpecResponse(AbstractModel):
    r"""DescribeCloneDBInstanceSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MinSpecCode: 可购买的最小规格码。
        :type MinSpecCode: str
        :param _MinStorage: 可购买的最小磁盘容量，单位GB。
        :type MinStorage: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MinSpecCode = None
        self._MinStorage = None
        self._RequestId = None

    @property
    def MinSpecCode(self):
        r"""可购买的最小规格码。
        :rtype: str
        """
        return self._MinSpecCode

    @MinSpecCode.setter
    def MinSpecCode(self, MinSpecCode):
        self._MinSpecCode = MinSpecCode

    @property
    def MinStorage(self):
        r"""可购买的最小磁盘容量，单位GB。
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MinSpecCode = params.get("MinSpecCode")
        self._MinStorage = params.get("MinStorage")
        self._RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    r"""DescribeDBBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-4wdeb0zv。
        :type DBInstanceId: str
        :param _Type: 备份方式（1-全量）。目前只支持全量，取值为1。
        :type Type: int
        :param _StartTime: 查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :type StartTime: str
        :param _EndTime: 查询结束时间，形如2018-06-10 17:06:38
        :type EndTime: str
        :param _Limit: 备份列表分页返回，每页返回数量，默认为 20，最小为1，最大值为 100。（当该参数不传或者传0时按默认值处理）
        :type Limit: int
        :param _Offset: 返回结果中的第几页，从第0页开始。默认为0。
        :type Offset: int
        """
        self._DBInstanceId = None
        self._Type = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-4wdeb0zv。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Type(self):
        r"""备份方式（1-全量）。目前只支持全量，取值为1。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        r"""查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，形如2018-06-10 17:06:38
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""备份列表分页返回，每页返回数量，默认为 20，最小为1，最大值为 100。（当该参数不传或者传0时按默认值处理）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""返回结果中的第几页，从第0页开始。默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBBackupsResponse(AbstractModel):
    r"""DescribeDBBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回备份列表中备份文件的个数
        :type TotalCount: int
        :param _BackupList: 备份列表
        :type BackupList: list of DBBackup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""返回备份列表中备份文件的个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupList(self):
        r"""备份列表
        :rtype: list of DBBackup
        """
        return self._BackupList

    @BackupList.setter
    def BackupList(self, BackupList):
        self._BackupList = BackupList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self._BackupList = []
            for item in params.get("BackupList"):
                obj = DBBackup()
                obj._deserialize(item)
                self._BackupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBErrlogsRequest(AbstractModel):
    r"""DescribeDBErrlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _StartTime: 查询起始时间，形如2018-01-01 00:00:00。日志保留时间默认为7天，起始时间不能超出保留时间范围。	
        :type StartTime: str
        :param _EndTime: 查询结束时间，形如2018-01-01 00:00:00。	
        :type EndTime: str
        :param _DatabaseName: 数据库名字。
        :type DatabaseName: str
        :param _SearchKeys: 搜索关键字。
        :type SearchKeys: list of str
        :param _Limit: 每页显示数量，取值范围为1-100。默认值为50。	
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。默认值为0。	
        :type Offset: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._DatabaseName = None
        self._SearchKeys = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""查询起始时间，形如2018-01-01 00:00:00。日志保留时间默认为7天，起始时间不能超出保留时间范围。	
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，形如2018-01-01 00:00:00。	
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DatabaseName(self):
        r"""数据库名字。
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SearchKeys(self):
        r"""搜索关键字。
        :rtype: list of str
        """
        return self._SearchKeys

    @SearchKeys.setter
    def SearchKeys(self, SearchKeys):
        self._SearchKeys = SearchKeys

    @property
    def Limit(self):
        r"""每页显示数量，取值范围为1-100。默认值为50。	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。默认值为0。	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DatabaseName = params.get("DatabaseName")
        self._SearchKeys = params.get("SearchKeys")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBErrlogsResponse(AbstractModel):
    r"""DescribeDBErrlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的日志数量，最大值为10000条。
        :type TotalCount: int
        :param _Details: 错误日志详细信息集合。
        :type Details: list of ErrLogDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询到的日志数量，最大值为10000条。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        r"""错误日志详细信息集合。
        :rtype: list of ErrLogDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ErrLogDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceAttributeRequest(AbstractModel):
    r"""DescribeDBInstanceAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceAttributeResponse(AbstractModel):
    r"""DescribeDBInstanceAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstance: 实例详细信息。
        :type DBInstance: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DBInstance = None
        self._RequestId = None

    @property
    def DBInstance(self):
        r"""实例详细信息。
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        """
        return self._DBInstance

    @DBInstance.setter
    def DBInstance(self, DBInstance):
        self._DBInstance = DBInstance

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DBInstance") is not None:
            self._DBInstance = DBInstance()
            self._DBInstance._deserialize(params.get("DBInstance"))
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceHAConfigRequest(AbstractModel):
    r"""DescribeDBInstanceHAConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceHAConfigResponse(AbstractModel):
    r"""DescribeDBInstanceHAConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SyncMode: 主从同步方式：
<li>Semi-sync：半同步</li>
<li>Async：异步</li>
        :type SyncMode: str
        :param _MaxStandbyLatency: 高可用备机最大延迟数据量。备节点延迟数据量小于等于该值，且备节点延迟时间小于等于MaxStandbyLag时，可以切换为主节点。
<li>单位：byte</li>
<li>参数范围：[1073741824, 322122547200]</li>
        :type MaxStandbyLatency: int
        :param _MaxStandbyLag: 高可用备机最大延迟时间。备节点延迟时间小于等于该值，且备节点延迟数据量小于等于MaxStandbyLatency时，可以切换为主节点。
<li>单位：s</li>
<li>参数范围：[5, 10]</li>
        :type MaxStandbyLag: int
        :param _MaxSyncStandbyLatency: 同步备机最大延迟数据量。备机延迟数据量小于等于该值，且该备机延迟时间小于等于MaxSyncStandbyLag时，则该备机采用同步复制；否则，采用异步复制。
该参数值针对SyncMode设置为Semi-sync的实例有效。
异步实例该字段返回null。
半同步实例禁止退化为异步复制时，该字段返回null。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSyncStandbyLatency: int
        :param _MaxSyncStandbyLag: 同步备机最大延迟时间。备机延迟时间小于等于该值，且该备机延迟数据量小于等于MaxSyncStandbyLatency时，则该备机采用同步复制；否则，采用异步复制。
该参数值针对SyncMode设置为Semi-sync的实例有效。
异步实例不返回该字段。
半同步实例禁止退化为异步复制时，不返回该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSyncStandbyLag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SyncMode = None
        self._MaxStandbyLatency = None
        self._MaxStandbyLag = None
        self._MaxSyncStandbyLatency = None
        self._MaxSyncStandbyLag = None
        self._RequestId = None

    @property
    def SyncMode(self):
        r"""主从同步方式：
<li>Semi-sync：半同步</li>
<li>Async：异步</li>
        :rtype: str
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def MaxStandbyLatency(self):
        r"""高可用备机最大延迟数据量。备节点延迟数据量小于等于该值，且备节点延迟时间小于等于MaxStandbyLag时，可以切换为主节点。
<li>单位：byte</li>
<li>参数范围：[1073741824, 322122547200]</li>
        :rtype: int
        """
        return self._MaxStandbyLatency

    @MaxStandbyLatency.setter
    def MaxStandbyLatency(self, MaxStandbyLatency):
        self._MaxStandbyLatency = MaxStandbyLatency

    @property
    def MaxStandbyLag(self):
        r"""高可用备机最大延迟时间。备节点延迟时间小于等于该值，且备节点延迟数据量小于等于MaxStandbyLatency时，可以切换为主节点。
<li>单位：s</li>
<li>参数范围：[5, 10]</li>
        :rtype: int
        """
        return self._MaxStandbyLag

    @MaxStandbyLag.setter
    def MaxStandbyLag(self, MaxStandbyLag):
        self._MaxStandbyLag = MaxStandbyLag

    @property
    def MaxSyncStandbyLatency(self):
        r"""同步备机最大延迟数据量。备机延迟数据量小于等于该值，且该备机延迟时间小于等于MaxSyncStandbyLag时，则该备机采用同步复制；否则，采用异步复制。
该参数值针对SyncMode设置为Semi-sync的实例有效。
异步实例该字段返回null。
半同步实例禁止退化为异步复制时，该字段返回null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxSyncStandbyLatency

    @MaxSyncStandbyLatency.setter
    def MaxSyncStandbyLatency(self, MaxSyncStandbyLatency):
        self._MaxSyncStandbyLatency = MaxSyncStandbyLatency

    @property
    def MaxSyncStandbyLag(self):
        r"""同步备机最大延迟时间。备机延迟时间小于等于该值，且该备机延迟数据量小于等于MaxSyncStandbyLatency时，则该备机采用同步复制；否则，采用异步复制。
该参数值针对SyncMode设置为Semi-sync的实例有效。
异步实例不返回该字段。
半同步实例禁止退化为异步复制时，不返回该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxSyncStandbyLag

    @MaxSyncStandbyLag.setter
    def MaxSyncStandbyLag(self, MaxSyncStandbyLag):
        self._MaxSyncStandbyLag = MaxSyncStandbyLag

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SyncMode = params.get("SyncMode")
        self._MaxStandbyLatency = params.get("MaxStandbyLatency")
        self._MaxStandbyLag = params.get("MaxStandbyLag")
        self._MaxSyncStandbyLatency = params.get("MaxSyncStandbyLatency")
        self._MaxSyncStandbyLag = params.get("MaxSyncStandbyLag")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceParametersRequest(AbstractModel):
    r"""DescribeDBInstanceParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _ParamName: 查询指定参数详情。ParamName为空或不传，默认返回全部参数列表
        :type ParamName: str
        """
        self._DBInstanceId = None
        self._ParamName = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ParamName(self):
        r"""查询指定参数详情。ParamName为空或不传，默认返回全部参数列表
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ParamName = params.get("ParamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceParametersResponse(AbstractModel):
    r"""DescribeDBInstanceParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数列表总数
        :type TotalCount: int
        :param _Detail: 参数列表返回详情
        :type Detail: list of ParamInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Detail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""参数列表总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Detail(self):
        r"""参数列表返回详情
        :rtype: list of ParamInfo
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceSSLConfigRequest(AbstractModel):
    r"""DescribeDBInstanceSSLConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-6bwgamo3。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-6bwgamo3。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceSSLConfigResponse(AbstractModel):
    r"""DescribeDBInstanceSSLConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SSLEnabled: true 代表开通 ，false 代表未开通
        :type SSLEnabled: bool
        :param _CAUrl: 云端根证书下载链接
        :type CAUrl: str
        :param _ConnectAddress: 服务器证书中配置的内网或外网连接地址
        :type ConnectAddress: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SSLEnabled = None
        self._CAUrl = None
        self._ConnectAddress = None
        self._RequestId = None

    @property
    def SSLEnabled(self):
        r"""true 代表开通 ，false 代表未开通
        :rtype: bool
        """
        return self._SSLEnabled

    @SSLEnabled.setter
    def SSLEnabled(self, SSLEnabled):
        self._SSLEnabled = SSLEnabled

    @property
    def CAUrl(self):
        r"""云端根证书下载链接
        :rtype: str
        """
        return self._CAUrl

    @CAUrl.setter
    def CAUrl(self, CAUrl):
        self._CAUrl = CAUrl

    @property
    def ConnectAddress(self):
        r"""服务器证书中配置的内网或外网连接地址
        :rtype: str
        """
        return self._ConnectAddress

    @ConnectAddress.setter
    def ConnectAddress(self, ConnectAddress):
        self._ConnectAddress = ConnectAddress

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SSLEnabled = params.get("SSLEnabled")
        self._CAUrl = params.get("CAUrl")
        self._ConnectAddress = params.get("ConnectAddress")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceSecurityGroupsRequest(AbstractModel):
    r"""DescribeDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。DBInstanceId和ReadOnlyGroupId至少传一个；如果都传，忽略ReadOnlyGroupId。
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: 只读组ID，可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取。DBInstanceId和ReadOnlyGroupId至少传一个；如果要查询只读组关联的安全组，只传ReadOnlyGroupId。
        :type ReadOnlyGroupId: str
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def DBInstanceId(self):
        r"""实例ID，可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。DBInstanceId和ReadOnlyGroupId至少传一个；如果都传，忽略ReadOnlyGroupId。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID，可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取。DBInstanceId和ReadOnlyGroupId至少传一个；如果要查询只读组关联的安全组，只传ReadOnlyGroupId。
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceSecurityGroupsResponse(AbstractModel):
    r"""DescribeDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupSet: 安全组信息数组
        :type SecurityGroupSet: list of SecurityGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroupSet = None
        self._RequestId = None

    @property
    def SecurityGroupSet(self):
        r"""安全组信息数组
        :rtype: list of SecurityGroup
        """
        return self._SecurityGroupSet

    @SecurityGroupSet.setter
    def SecurityGroupSet(self, SecurityGroupSet):
        self._SecurityGroupSet = SecurityGroupSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self._SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._SecurityGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    r"""DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string
db-instance-name：按照实例名过滤，支持模糊匹配，类型为string
db-project-id：按照项目ID过滤，类型为integer
db-pay-mode：按照实例付费模式过滤，prepaid - 预付费；postpaid - 后付费。类型为string
db-tag-key：按照标签键过滤，类型为string
db-private-ip： 按照实例私有网络IP过滤，类型为string
db-public-address： 按照实例外网地址过滤，类型为string
db-dedicated-cluster-id: 按照私有集群Id过滤，类型为string
        :type Filters: list of Filter
        :param _Limit: 每页显示数量，取值范围为0-100，传入0时，取默认配置。默认为返回10条。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param _OrderBy: 排序指标，如实例名、创建时间等，支持DBInstanceId,CreateTime,Name,EndTime。默认值：CreateTime。
        :type OrderBy: str
        :param _OrderByType: 排序方式，包括升序：asc、降序：desc。默认值：asc。
        :type OrderByType: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Filters(self):
        r"""按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string
db-instance-name：按照实例名过滤，支持模糊匹配，类型为string
db-project-id：按照项目ID过滤，类型为integer
db-pay-mode：按照实例付费模式过滤，prepaid - 预付费；postpaid - 后付费。类型为string
db-tag-key：按照标签键过滤，类型为string
db-private-ip： 按照实例私有网络IP过滤，类型为string
db-public-address： 按照实例外网地址过滤，类型为string
db-dedicated-cluster-id: 按照私有集群Id过滤，类型为string
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""每页显示数量，取值范围为0-100，传入0时，取默认配置。默认为返回10条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""排序指标，如实例名、创建时间等，支持DBInstanceId,CreateTime,Name,EndTime。默认值：CreateTime。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式，包括升序：asc、降序：desc。默认值：asc。
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    r"""DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的实例数量。
        :type TotalCount: int
        :param _DBInstanceSet: 实例详细信息集合。
        :type DBInstanceSet: list of DBInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询到的实例数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstanceSet(self):
        r"""实例详细信息集合。
        :rtype: list of DBInstance
        """
        return self._DBInstanceSet

    @DBInstanceSet.setter
    def DBInstanceSet(self, DBInstanceSet):
        self._DBInstanceSet = DBInstanceSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DBInstanceSet") is not None:
            self._DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = DBInstance()
                obj._deserialize(item)
                self._DBInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBVersionsRequest(AbstractModel):
    r"""DescribeDBVersions请求参数结构体

    """


class DescribeDBVersionsResponse(AbstractModel):
    r"""DescribeDBVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionSet: 数据库版本号信息列表
        :type VersionSet: list of Version
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionSet = None
        self._RequestId = None

    @property
    def VersionSet(self):
        r"""数据库版本号信息列表
        :rtype: list of Version
        """
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VersionSet") is not None:
            self._VersionSet = []
            for item in params.get("VersionSet"):
                obj = Version()
                obj._deserialize(item)
                self._VersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBXlogsRequest(AbstractModel):
    r"""DescribeDBXlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-4wdeb0zv。
        :type DBInstanceId: str
        :param _StartTime: 查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :type StartTime: str
        :param _EndTime: 查询结束时间，形如2018-06-10 17:06:38
        :type EndTime: str
        :param _Offset: 分页返回，表示返回第几页的条目。从第0页开始计数。
        :type Offset: int
        :param _Limit: 分页返回，表示每页有多少条目。取值为1-100。
        :type Limit: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-4wdeb0zv。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，形如2018-06-10 17:06:38
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""分页返回，表示返回第几页的条目。从第0页开始计数。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页返回，表示每页有多少条目。取值为1-100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBXlogsResponse(AbstractModel):
    r"""DescribeDBXlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表示此次返回结果有多少条数据。
        :type TotalCount: int
        :param _XlogList: Xlog列表
        :type XlogList: list of Xlog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._XlogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""表示此次返回结果有多少条数据。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def XlogList(self):
        r"""Xlog列表
        :rtype: list of Xlog
        """
        return self._XlogList

    @XlogList.setter
    def XlogList(self, XlogList):
        self._XlogList = XlogList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("XlogList") is not None:
            self._XlogList = []
            for item in params.get("XlogList"):
                obj = Xlog()
                obj._deserialize(item)
                self._XlogList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    r"""DescribeDatabaseObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _ObjectType: 查询的对象类型。支持查询的数据对象有：database,schema,sequence,procedure,type,function,table,view,matview,column。
        :type ObjectType: str
        :param _Limit: 单次显示数量，默认20。可选范围为[0,100]。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。	
        :type Offset: int
        :param _DatabaseName: 查询对象所属的数据库。当查询对象类型不为database时，此参数必填。
        :type DatabaseName: str
        :param _SchemaName: 查询对象所属的模式。当查询对象类型不为database、schema时，此参数必填。
        :type SchemaName: str
        :param _TableName: 查询对象所属的表。当查询对象类型为column时，此参数必填。
        :type TableName: str
        """
        self._DBInstanceId = None
        self._ObjectType = None
        self._Limit = None
        self._Offset = None
        self._DatabaseName = None
        self._SchemaName = None
        self._TableName = None

    @property
    def DBInstanceId(self):
        r"""实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ObjectType(self):
        r"""查询的对象类型。支持查询的数据对象有：database,schema,sequence,procedure,type,function,table,view,matview,column。
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def Limit(self):
        r"""单次显示数量，默认20。可选范围为[0,100]。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DatabaseName(self):
        r"""查询对象所属的数据库。当查询对象类型不为database时，此参数必填。
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SchemaName(self):
        r"""查询对象所属的模式。当查询对象类型不为database、schema时，此参数必填。
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableName(self):
        r"""查询对象所属的表。当查询对象类型为column时，此参数必填。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ObjectType = params.get("ObjectType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DatabaseName = params.get("DatabaseName")
        self._SchemaName = params.get("SchemaName")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    r"""DescribeDatabaseObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ObjectSet: 查询对象列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectSet: list of str
        :param _TotalCount: 查询对象总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ObjectSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ObjectSet(self):
        r"""查询对象列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ObjectSet

    @ObjectSet.setter
    def ObjectSet(self, ObjectSet):
        self._ObjectSet = ObjectSet

    @property
    def TotalCount(self):
        r"""查询对象总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ObjectSet = params.get("ObjectSet")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    r"""DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/product/409/16773)接口获取
        :type DBInstanceId: str
        :param _Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：database-name：按照数据库名称过滤，类型为string。此处使用模糊匹配搜索符合条件的数据库。
        :type Filters: list of Filter
        :param _Offset: 数据偏移量，从0开始。	
        :type Offset: int
        :param _Limit: 单次显示数量。建议最大取值100。
默认值：20
        :type Limit: int
        """
        self._DBInstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/product/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Filters(self):
        r"""按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：database-name：按照数据库名称过滤，类型为string。此处使用模糊匹配搜索符合条件的数据库。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""单次显示数量。建议最大取值100。
默认值：20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    r"""DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 数据库信息
        :type Items: list of str
        :param _TotalCount: 数据库总数
        :type TotalCount: int
        :param _Databases: 数据库详情列表
        :type Databases: list of Database
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._Databases = None
        self._RequestId = None

    @property
    def Items(self):
        r"""数据库信息
        :rtype: list of str
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""数据库总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Databases(self):
        r"""数据库详情列表
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Items = params.get("Items")
        self._TotalCount = params.get("TotalCount")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClustersRequest(AbstractModel):
    r"""DescribeDedicatedClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
dedicated-cluster-id: 按照专属集群ID筛选，类型为string
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        r"""按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
dedicated-cluster-id: 按照专属集群ID筛选，类型为string
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClustersResponse(AbstractModel):
    r"""DescribeDedicatedClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterSet: 专属集群信息
        :type DedicatedClusterSet: list of DedicatedCluster
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DedicatedClusterSet = None
        self._RequestId = None

    @property
    def DedicatedClusterSet(self):
        r"""专属集群信息
        :rtype: list of DedicatedCluster
        """
        return self._DedicatedClusterSet

    @DedicatedClusterSet.setter
    def DedicatedClusterSet(self, DedicatedClusterSet):
        self._DedicatedClusterSet = DedicatedClusterSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DedicatedClusterSet") is not None:
            self._DedicatedClusterSet = []
            for item in params.get("DedicatedClusterSet"):
                obj = DedicatedCluster()
                obj._deserialize(item)
                self._DedicatedClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDefaultParametersRequest(AbstractModel):
    r"""DescribeDefaultParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBMajorVersion: 数据库版本，大版本号，例如11，12，13。可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)接口获取
        :type DBMajorVersion: str
        :param _DBEngine: 数据库引擎，例如：postgresql,mssql_compatible
        :type DBEngine: str
        """
        self._DBMajorVersion = None
        self._DBEngine = None

    @property
    def DBMajorVersion(self):
        r"""数据库版本，大版本号，例如11，12，13。可从[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)接口获取
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBEngine(self):
        r"""数据库引擎，例如：postgresql,mssql_compatible
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine


    def _deserialize(self, params):
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBEngine = params.get("DBEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultParametersResponse(AbstractModel):
    r"""DescribeDefaultParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数个数
        :type TotalCount: int
        :param _ParamInfoSet: 参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamInfoSet: list of ParamInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ParamInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""参数个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ParamInfoSet(self):
        r"""参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamInfo
        """
        return self._ParamInfoSet

    @ParamInfoSet.setter
    def ParamInfoSet(self, ParamInfoSet):
        self._ParamInfoSet = ParamInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ParamInfoSet") is not None:
            self._ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEncryptionKeysRequest(AbstractModel):
    r"""DescribeEncryptionKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEncryptionKeysResponse(AbstractModel):
    r"""DescribeEncryptionKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EncryptionKeys: 实例密钥信息列表。
        :type EncryptionKeys: list of EncryptionKey
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EncryptionKeys = None
        self._RequestId = None

    @property
    def EncryptionKeys(self):
        r"""实例密钥信息列表。
        :rtype: list of EncryptionKey
        """
        return self._EncryptionKeys

    @EncryptionKeys.setter
    def EncryptionKeys(self, EncryptionKeys):
        self._EncryptionKeys = EncryptionKeys

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EncryptionKeys") is not None:
            self._EncryptionKeys = []
            for item in params.get("EncryptionKeys"):
                obj = EncryptionKey()
                obj._deserialize(item)
                self._EncryptionKeys.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogBackupsRequest(AbstractModel):
    r"""DescribeLogBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinFinishTime: 备份的最小结束时间，形如2018-01-01 00:00:00。默认为7天前。
        :type MinFinishTime: str
        :param _MaxFinishTime: 备份的最大结束时间，形如2018-01-01 00:00:00。默认为当前时间。
        :type MaxFinishTime: str
        :param _Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，支持模糊匹配，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
db-instance-status：按实例状态过滤，类型为string。取值参考[DBInstance](https://cloud.tencent.com/document/api/409/16778#DBInstance)结构的DBInstanceStatus字段。
        :type Filters: list of Filter
        :param _Limit: 每页显示数量，取值范围为1-100，默认为返回10条。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param _OrderBy: 排序字段，支持StartTime,FinishTime,Size。默认值：StartTime
        :type OrderBy: str
        :param _OrderByType: 排序方式，包括升序：asc，降序：desc。默认值：desc。
        :type OrderByType: str
        """
        self._MinFinishTime = None
        self._MaxFinishTime = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def MinFinishTime(self):
        r"""备份的最小结束时间，形如2018-01-01 00:00:00。默认为7天前。
        :rtype: str
        """
        return self._MinFinishTime

    @MinFinishTime.setter
    def MinFinishTime(self, MinFinishTime):
        self._MinFinishTime = MinFinishTime

    @property
    def MaxFinishTime(self):
        r"""备份的最大结束时间，形如2018-01-01 00:00:00。默认为当前时间。
        :rtype: str
        """
        return self._MaxFinishTime

    @MaxFinishTime.setter
    def MaxFinishTime(self, MaxFinishTime):
        self._MaxFinishTime = MaxFinishTime

    @property
    def Filters(self):
        r"""按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，支持模糊匹配，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
db-instance-status：按实例状态过滤，类型为string。取值参考[DBInstance](https://cloud.tencent.com/document/api/409/16778#DBInstance)结构的DBInstanceStatus字段。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""每页显示数量，取值范围为1-100，默认为返回10条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""排序字段，支持StartTime,FinishTime,Size。默认值：StartTime
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式，包括升序：asc，降序：desc。默认值：desc。
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._MinFinishTime = params.get("MinFinishTime")
        self._MaxFinishTime = params.get("MaxFinishTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogBackupsResponse(AbstractModel):
    r"""DescribeLogBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的日志备份数量。
        :type TotalCount: int
        :param _LogBackupSet: 日志备份详细信息列表。
        :type LogBackupSet: list of LogBackup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LogBackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询到的日志备份数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogBackupSet(self):
        r"""日志备份详细信息列表。
        :rtype: list of LogBackup
        """
        return self._LogBackupSet

    @LogBackupSet.setter
    def LogBackupSet(self, LogBackupSet):
        self._LogBackupSet = LogBackupSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LogBackupSet") is not None:
            self._LogBackupSet = []
            for item in params.get("LogBackupSet"):
                obj = LogBackup()
                obj._deserialize(item)
                self._LogBackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaintainTimeWindowRequest(AbstractModel):
    r"""DescribeMaintainTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaintainTimeWindowResponse(AbstractModel):
    r"""DescribeMaintainTimeWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param _MaintainStartTime: 维护开始时间。时区为东八区（UTC+8）
        :type MaintainStartTime: str
        :param _MaintainDuration: 维护持续时间。单位：小时
        :type MaintainDuration: int
        :param _MaintainWeekDays: 维护周期
        :type MaintainWeekDays: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DBInstanceId = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None
        self._RequestId = None

    @property
    def DBInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def MaintainStartTime(self):
        r"""维护开始时间。时区为东八区（UTC+8）
        :rtype: str
        """
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        r"""维护持续时间。单位：小时
        :rtype: int
        """
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        r"""维护周期
        :rtype: list of str
        """
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    r"""DescribeOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单名集合
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        r"""订单名集合
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    r"""DescribeOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 订单数量
        :type TotalCount: int
        :param _Deals: 订单数组
        :type Deals: list of PgDeal
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Deals = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""订单数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Deals(self):
        r"""订单数组
        :rtype: list of PgDeal
        """
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = PgDeal()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeParameterTemplateAttributesRequest(AbstractModel):
    r"""DescribeParameterTemplateAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID。可通过[DescribeParameterTemplates](https://cloud.tencent.com/document/api/409/84067)接口获取
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""参数模板ID。可通过[DescribeParameterTemplates](https://cloud.tencent.com/document/api/409/84067)接口获取
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParameterTemplateAttributesResponse(AbstractModel):
    r"""DescribeParameterTemplateAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID
        :type TemplateId: str
        :param _TotalCount: 参数模板包含的参数个数
        :type TotalCount: int
        :param _ParamInfoSet: 参数模板包含的参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamInfoSet: list of ParamInfo
        :param _TemplateName: 参数模板名称
        :type TemplateName: str
        :param _DBMajorVersion: 参数模板适用的数据库版本
        :type DBMajorVersion: str
        :param _DBEngine: 参数模板适用的数据库引擎
        :type DBEngine: str
        :param _TemplateDescription: 参数模板描述
        :type TemplateDescription: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._TotalCount = None
        self._ParamInfoSet = None
        self._TemplateName = None
        self._DBMajorVersion = None
        self._DBEngine = None
        self._TemplateDescription = None
        self._RequestId = None

    @property
    def TemplateId(self):
        r"""参数模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TotalCount(self):
        r"""参数模板包含的参数个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ParamInfoSet(self):
        r"""参数模板包含的参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamInfo
        """
        return self._ParamInfoSet

    @ParamInfoSet.setter
    def ParamInfoSet(self, ParamInfoSet):
        self._ParamInfoSet = ParamInfoSet

    @property
    def TemplateName(self):
        r"""参数模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def DBMajorVersion(self):
        r"""参数模板适用的数据库版本
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBEngine(self):
        r"""参数模板适用的数据库引擎
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def TemplateDescription(self):
        r"""参数模板描述
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TotalCount = params.get("TotalCount")
        if params.get("ParamInfoSet") is not None:
            self._ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamInfoSet.append(obj)
        self._TemplateName = params.get("TemplateName")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBEngine = params.get("DBEngine")
        self._TemplateDescription = params.get("TemplateDescription")
        self._RequestId = params.get("RequestId")


class DescribeParameterTemplatesRequest(AbstractModel):
    r"""DescribeParameterTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，目前支持的过滤条件有：TemplateName, TemplateId，DBMajorVersion，DBEngine。TemplateName不支持模糊匹配。
        :type Filters: list of Filter
        :param _Limit: 每页显示数量，[0，100]，默认 20
        :type Limit: int
        :param _Offset: 数据偏移量
        :type Offset: int
        :param _OrderBy: 排序指标，枚举值，支持：CreateTime，TemplateName，DBMajorVersion。如果不指定该参数，默认将按照参数模板的编号倒序排列，也就是说最新添加的参数模板会排在最前面。
        :type OrderBy: str
        :param _OrderByType: 排序方式，枚举值，支持：asc（升序） ，desc（降序）。默认值为asc。当未指定OrderBy时，该参数失效，此时排序方式为OrderBy参数描述中给出的默认排序方式。
        :type OrderByType: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Filters(self):
        r"""过滤条件，目前支持的过滤条件有：TemplateName, TemplateId，DBMajorVersion，DBEngine。TemplateName不支持模糊匹配。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""每页显示数量，[0，100]，默认 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""排序指标，枚举值，支持：CreateTime，TemplateName，DBMajorVersion。如果不指定该参数，默认将按照参数模板的编号倒序排列，也就是说最新添加的参数模板会排在最前面。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式，枚举值，支持：asc（升序） ，desc（降序）。默认值为asc。当未指定OrderBy时，该参数失效，此时排序方式为OrderBy参数描述中给出的默认排序方式。
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParameterTemplatesResponse(AbstractModel):
    r"""DescribeParameterTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的参数模板总数
        :type TotalCount: int
        :param _ParameterTemplateSet: 参数模板列表
        :type ParameterTemplateSet: list of ParameterTemplate
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ParameterTemplateSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合查询条件的参数模板总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ParameterTemplateSet(self):
        r"""参数模板列表
        :rtype: list of ParameterTemplate
        """
        return self._ParameterTemplateSet

    @ParameterTemplateSet.setter
    def ParameterTemplateSet(self, ParameterTemplateSet):
        self._ParameterTemplateSet = ParameterTemplateSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ParameterTemplateSet") is not None:
            self._ParameterTemplateSet = []
            for item in params.get("ParameterTemplateSet"):
                obj = ParameterTemplate()
                obj._deserialize(item)
                self._ParameterTemplateSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeParamsEventRequest(AbstractModel):
    r"""DescribeParamsEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamsEventResponse(AbstractModel):
    r"""DescribeParamsEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数修改事件总数，以参数为统计粒度
        :type TotalCount: int
        :param _EventItems: 实例参数修改事件详情
        :type EventItems: list of EventItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EventItems = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""参数修改事件总数，以参数为统计粒度
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EventItems(self):
        r"""实例参数修改事件详情
        :rtype: list of EventItem
        """
        return self._EventItems

    @EventItems.setter
    def EventItems(self, EventItems):
        self._EventItems = EventItems

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EventItems") is not None:
            self._EventItems = []
            for item in params.get("EventItems"):
                obj = EventItem()
                obj._deserialize(item)
                self._EventItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    r"""DescribeProductConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称
        :type Zone: str
        :param _DBEngine: 数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
如不指定默认使用postgresql。
        :type DBEngine: str
        """
        self._Zone = None
        self._DBEngine = None

    @property
    def Zone(self):
        r"""可用区名称
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DBEngine(self):
        r"""数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
如不指定默认使用postgresql。
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DBEngine = params.get("DBEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductConfigResponse(AbstractModel):
    r"""DescribeProductConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpecInfoList: 售卖规格列表。
        :type SpecInfoList: list of SpecInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpecInfoList = None
        self._RequestId = None

    @property
    def SpecInfoList(self):
        r"""售卖规格列表。
        :rtype: list of SpecInfo
        """
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupsRequest(AbstractModel):
    r"""DescribeReadOnlyGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-master-instance-id：按照主实例过滤，类型为string。
read-only-group-id：按照只读组ID过滤，类型为string。
注：该参数的过滤条件中，db-master-instance-id为必须指定项。
        :type Filters: list of Filter
        :param _PageSize: 查询每一页的条数，默认为10，最大值99。
        :type PageSize: int
        :param _PageNumber: 查询的页码，默认为1
        :type PageNumber: int
        :param _OrderBy: 查询排序依据，目前支持:ROGroupId,CreateTime,Name。默认值CreateTime
        :type OrderBy: str
        :param _OrderByType: 查询排序依据类型，目前支持:desc,asc。默认值asc。
        :type OrderByType: str
        """
        self._Filters = None
        self._PageSize = None
        self._PageNumber = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Filters(self):
        r"""按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-master-instance-id：按照主实例过滤，类型为string。
read-only-group-id：按照只读组ID过滤，类型为string。
注：该参数的过滤条件中，db-master-instance-id为必须指定项。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def PageSize(self):
        r"""查询每一页的条数，默认为10，最大值99。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""查询的页码，默认为1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def OrderBy(self):
        r"""查询排序依据，目前支持:ROGroupId,CreateTime,Name。默认值CreateTime
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""查询排序依据类型，目前支持:desc,asc。默认值asc。
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupsResponse(AbstractModel):
    r"""DescribeReadOnlyGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupList: 只读组列表
        :type ReadOnlyGroupList: list of ReadOnlyGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReadOnlyGroupList = None
        self._RequestId = None

    @property
    def ReadOnlyGroupList(self):
        r"""只读组列表
        :rtype: list of ReadOnlyGroup
        """
        return self._ReadOnlyGroupList

    @ReadOnlyGroupList.setter
    def ReadOnlyGroupList(self, ReadOnlyGroupList):
        self._ReadOnlyGroupList = ReadOnlyGroupList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReadOnlyGroupList") is not None:
            self._ReadOnlyGroupList = []
            for item in params.get("ReadOnlyGroupList"):
                obj = ReadOnlyGroup()
                obj._deserialize(item)
                self._ReadOnlyGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    r"""DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    r"""DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的结果数量。
        :type TotalCount: int
        :param _RegionSet: 地域信息集合。
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""返回的结果数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        r"""地域信息集合。
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryAnalysisRequest(AbstractModel):
    r"""DescribeSlowQueryAnalysis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _StartTime: 查询起始时间，形如2018-01-01 00:00:00。日志保留时间默认为7天，起始时间不能超出保留时间范围。
        :type StartTime: str
        :param _EndTime: 查询结束时间，形如2018-01-01 00:00:00。
        :type EndTime: str
        :param _DatabaseName: 数据库名字。	
        :type DatabaseName: str
        :param _OrderBy: 排序字段，取值范围[CallNum,CostTime,AvgCostTime]。默认值为CallNum。
        :type OrderBy: str
        :param _OrderByType: 排序方式，包括升序：asc 降序：desc。默认值为desc。
        :type OrderByType: str
        :param _Limit: 每页显示数量，取值范围为1-100。默认值为50。	
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。默认值为0。
        :type Offset: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._DatabaseName = None
        self._OrderBy = None
        self._OrderByType = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""查询起始时间，形如2018-01-01 00:00:00。日志保留时间默认为7天，起始时间不能超出保留时间范围。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，形如2018-01-01 00:00:00。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DatabaseName(self):
        r"""数据库名字。	
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def OrderBy(self):
        r"""排序字段，取值范围[CallNum,CostTime,AvgCostTime]。默认值为CallNum。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式，包括升序：asc 降序：desc。默认值为desc。
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Limit(self):
        r"""每页显示数量，取值范围为1-100。默认值为50。	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DatabaseName = params.get("DatabaseName")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryAnalysisResponse(AbstractModel):
    r"""DescribeSlowQueryAnalysis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的总条数，最大值为10000条。
        :type TotalCount: int
        :param _Detail: 查询到的慢SQL统计分析详细信息集合。
        :type Detail: :class:`tencentcloud.postgres.v20170312.models.Detail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Detail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询到的总条数，最大值为10000条。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Detail(self):
        r"""查询到的慢SQL统计分析详细信息集合。
        :rtype: :class:`tencentcloud.postgres.v20170312.models.Detail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Detail") is not None:
            self._Detail = Detail()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryListRequest(AbstractModel):
    r"""DescribeSlowQueryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _StartTime: 查询起始时间，形如2018-01-01 00:00:00。日志保留时间默认为7天，起始时间不能超出保留时间范围。
        :type StartTime: str
        :param _EndTime: 查询结束时间，形如2018-01-01 00:00:00。	
        :type EndTime: str
        :param _DatabaseName: 数据库名字。	
        :type DatabaseName: str
        :param _OrderByType: 排序方式，包括升序：asc 降序：desc。默认值为desc。	
        :type OrderByType: str
        :param _OrderBy: 排序字段，取值范围[SessionStartTime,Duration]。默认值为SessionStartTime。
        :type OrderBy: str
        :param _Limit: 每页显示数量，取值范围为1-100。默认值为50。	
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。默认值为0。	
        :type Offset: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._DatabaseName = None
        self._OrderByType = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""查询起始时间，形如2018-01-01 00:00:00。日志保留时间默认为7天，起始时间不能超出保留时间范围。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，形如2018-01-01 00:00:00。	
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DatabaseName(self):
        r"""数据库名字。	
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def OrderByType(self):
        r"""排序方式，包括升序：asc 降序：desc。默认值为desc。	
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def OrderBy(self):
        r"""排序字段，取值范围[SessionStartTime,Duration]。默认值为SessionStartTime。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        r"""每页显示数量，取值范围为1-100。默认值为50。	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。默认值为0。	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DatabaseName = params.get("DatabaseName")
        self._OrderByType = params.get("OrderByType")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryListResponse(AbstractModel):
    r"""DescribeSlowQueryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的慢日志数量，最大值为10000条。	
        :type TotalCount: int
        :param _DurationAnalysis: 查询到的慢日志耗时分段分析结果。
        :type DurationAnalysis: list of DurationAnalysis
        :param _RawSlowQueryList: 查询到的慢日志详细信息集合。
        :type RawSlowQueryList: list of RawSlowQuery
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DurationAnalysis = None
        self._RawSlowQueryList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询到的慢日志数量，最大值为10000条。	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DurationAnalysis(self):
        r"""查询到的慢日志耗时分段分析结果。
        :rtype: list of DurationAnalysis
        """
        return self._DurationAnalysis

    @DurationAnalysis.setter
    def DurationAnalysis(self, DurationAnalysis):
        self._DurationAnalysis = DurationAnalysis

    @property
    def RawSlowQueryList(self):
        r"""查询到的慢日志详细信息集合。
        :rtype: list of RawSlowQuery
        """
        return self._RawSlowQueryList

    @RawSlowQueryList.setter
    def RawSlowQueryList(self, RawSlowQueryList):
        self._RawSlowQueryList = RawSlowQueryList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DurationAnalysis") is not None:
            self._DurationAnalysis = []
            for item in params.get("DurationAnalysis"):
                obj = DurationAnalysis()
                obj._deserialize(item)
                self._DurationAnalysis.append(obj)
        if params.get("RawSlowQueryList") is not None:
            self._RawSlowQueryList = []
            for item in params.get("RawSlowQueryList"):
                obj = RawSlowQuery()
                obj._deserialize(item)
                self._RawSlowQueryList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    r"""DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 按照任务ID进行查询。其余云API中返回的FlowId和TaskId等价。
        :type TaskId: int
        :param _DBInstanceId: 按照数据库实例ID进行查询。
        :type DBInstanceId: str
        :param _MinStartTime: 任务的最早开始时间，形如2024-08-23 00:00:00,默认只展示180天内的数据。
        :type MinStartTime: str
        :param _MaxStartTime: 任务的最晚开始时间，形如2024-08-23 00:00:00，默认为当前时间。
        :type MaxStartTime: str
        :param _Limit: 每页显示数量，取值范围为1-100，默认为返回20条。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param _OrderBy: 排序字段，支持StartTime,EndTime，默认为StartTime。
        :type OrderBy: str
        :param _OrderByType: 排序方式，包括升序：asc，降序：desc，默认为desc。
        :type OrderByType: str
        """
        self._TaskId = None
        self._DBInstanceId = None
        self._MinStartTime = None
        self._MaxStartTime = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def TaskId(self):
        r"""按照任务ID进行查询。其余云API中返回的FlowId和TaskId等价。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DBInstanceId(self):
        r"""按照数据库实例ID进行查询。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def MinStartTime(self):
        r"""任务的最早开始时间，形如2024-08-23 00:00:00,默认只展示180天内的数据。
        :rtype: str
        """
        return self._MinStartTime

    @MinStartTime.setter
    def MinStartTime(self, MinStartTime):
        self._MinStartTime = MinStartTime

    @property
    def MaxStartTime(self):
        r"""任务的最晚开始时间，形如2024-08-23 00:00:00，默认为当前时间。
        :rtype: str
        """
        return self._MaxStartTime

    @MaxStartTime.setter
    def MaxStartTime(self, MaxStartTime):
        self._MaxStartTime = MaxStartTime

    @property
    def Limit(self):
        r"""每页显示数量，取值范围为1-100，默认为返回20条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""数据偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""排序字段，支持StartTime,EndTime，默认为StartTime。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式，包括升序：asc，降序：desc，默认为desc。
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DBInstanceId = params.get("DBInstanceId")
        self._MinStartTime = params.get("MinStartTime")
        self._MaxStartTime = params.get("MaxStartTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    r"""DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的任务数量
        :type TotalCount: int
        :param _TaskSet: 任务信息列表
        :type TaskSet: list of TaskSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询到的任务数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskSet(self):
        r"""任务信息列表
        :rtype: list of TaskSet
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSet()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    r"""DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    r"""DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的结果数量。
        :type TotalCount: int
        :param _ZoneSet: 可用区信息集合。
        :type ZoneSet: list of ZoneInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""返回的结果数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneSet(self):
        r"""可用区信息集合。
        :rtype: list of ZoneInfo
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyDBInstanceRequest(AbstractModel):
    r"""DestroyDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 待下线实例ID
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""待下线实例ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDBInstanceResponse(AbstractModel):
    r"""DestroyDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Detail(AbstractModel):
    r"""慢SQL 统计分析接口返回详情

    """

    def __init__(self):
        r"""
        :param _TotalTime: 输入时间范围内所有慢sql执行的总时间，单位毫秒（ms）
        :type TotalTime: float
        :param _TotalCallNum: 输入时间范围内所有慢sql总条数
        :type TotalCallNum: int
        :param _AnalysisItems: 慢SQL统计分析列表
        :type AnalysisItems: list of AnalysisItems
        """
        self._TotalTime = None
        self._TotalCallNum = None
        self._AnalysisItems = None

    @property
    def TotalTime(self):
        r"""输入时间范围内所有慢sql执行的总时间，单位毫秒（ms）
        :rtype: float
        """
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def TotalCallNum(self):
        r"""输入时间范围内所有慢sql总条数
        :rtype: int
        """
        return self._TotalCallNum

    @TotalCallNum.setter
    def TotalCallNum(self, TotalCallNum):
        self._TotalCallNum = TotalCallNum

    @property
    def AnalysisItems(self):
        r"""慢SQL统计分析列表
        :rtype: list of AnalysisItems
        """
        return self._AnalysisItems

    @AnalysisItems.setter
    def AnalysisItems(self, AnalysisItems):
        self._AnalysisItems = AnalysisItems


    def _deserialize(self, params):
        self._TotalTime = params.get("TotalTime")
        self._TotalCallNum = params.get("TotalCallNum")
        if params.get("AnalysisItems") is not None:
            self._AnalysisItems = []
            for item in params.get("AnalysisItems"):
                obj = AnalysisItems()
                obj._deserialize(item)
                self._AnalysisItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisIsolateDBInstancesRequest(AbstractModel):
    r"""DisIsolateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: 实例ID列表。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。支持同时解隔离多个实例。
        :type DBInstanceIdSet: list of str
        :param _Period: 购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
<li>后付费：该参数不生效</li>
        :type Period: int
        :param _AutoVoucher: 是否使用代金券：
<li>true：使用</li>
<li>false：不使用</li>
默认值：false
        :type AutoVoucher: bool
        :param _VoucherIds: 代金券id列表。
        :type VoucherIds: list of str
        """
        self._DBInstanceIdSet = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None

    @property
    def DBInstanceIdSet(self):
        r"""实例ID列表。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。支持同时解隔离多个实例。
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def Period(self):
        r"""购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
<li>后付费：该参数不生效</li>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        r"""是否使用代金券：
<li>true：使用</li>
<li>false：不使用</li>
默认值：false
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""代金券id列表。
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisIsolateDBInstancesResponse(AbstractModel):
    r"""DisIsolateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DurationAnalysis(AbstractModel):
    r"""慢SQL耗时分段分析

    """

    def __init__(self):
        r"""
        :param _TimeSegment: 慢SQL耗时，时段
        :type TimeSegment: str
        :param _Count: 对应时段区间慢SQL 条数
        :type Count: int
        """
        self._TimeSegment = None
        self._Count = None

    @property
    def TimeSegment(self):
        r"""慢SQL耗时，时段
        :rtype: str
        """
        return self._TimeSegment

    @TimeSegment.setter
    def TimeSegment(self, TimeSegment):
        self._TimeSegment = TimeSegment

    @property
    def Count(self):
        r"""对应时段区间慢SQL 条数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._TimeSegment = params.get("TimeSegment")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptionKey(AbstractModel):
    r"""KMS密钥信息

    """

    def __init__(self):
        r"""
        :param _KeyId: KMS实例加密的KeyId。
        :type KeyId: str
        :param _KeyAlias: KMS实例加密Key的别名。
        :type KeyAlias: str
        :param _DEKCipherTextBlob: 实例加密密钥DEK的密文。
        :type DEKCipherTextBlob: str
        :param _IsEnabled: 密钥是否启用，1-启用， 0-未启用。
        :type IsEnabled: int
        :param _KeyRegion: KMS密钥所在地域。
        :type KeyRegion: str
        :param _CreateTime: DEK密钥创建时间。
        :type CreateTime: str
        :param _KMSClusterId: 密钥所在的KMS服务集群Id，为空表示密钥在默认的KMS集群中，不为空表示在指定的KMS服务集群中
        :type KMSClusterId: str
        """
        self._KeyId = None
        self._KeyAlias = None
        self._DEKCipherTextBlob = None
        self._IsEnabled = None
        self._KeyRegion = None
        self._CreateTime = None
        self._KMSClusterId = None

    @property
    def KeyId(self):
        r"""KMS实例加密的KeyId。
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyAlias(self):
        r"""KMS实例加密Key的别名。
        :rtype: str
        """
        return self._KeyAlias

    @KeyAlias.setter
    def KeyAlias(self, KeyAlias):
        self._KeyAlias = KeyAlias

    @property
    def DEKCipherTextBlob(self):
        r"""实例加密密钥DEK的密文。
        :rtype: str
        """
        return self._DEKCipherTextBlob

    @DEKCipherTextBlob.setter
    def DEKCipherTextBlob(self, DEKCipherTextBlob):
        self._DEKCipherTextBlob = DEKCipherTextBlob

    @property
    def IsEnabled(self):
        r"""密钥是否启用，1-启用， 0-未启用。
        :rtype: int
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def KeyRegion(self):
        r"""KMS密钥所在地域。
        :rtype: str
        """
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion

    @property
    def CreateTime(self):
        r"""DEK密钥创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def KMSClusterId(self):
        r"""密钥所在的KMS服务集群Id，为空表示密钥在默认的KMS集群中，不为空表示在指定的KMS服务集群中
        :rtype: str
        """
        return self._KMSClusterId

    @KMSClusterId.setter
    def KMSClusterId(self, KMSClusterId):
        self._KMSClusterId = KMSClusterId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyAlias = params.get("KeyAlias")
        self._DEKCipherTextBlob = params.get("DEKCipherTextBlob")
        self._IsEnabled = params.get("IsEnabled")
        self._KeyRegion = params.get("KeyRegion")
        self._CreateTime = params.get("CreateTime")
        self._KMSClusterId = params.get("KMSClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrLogDetail(AbstractModel):
    r"""错误日志详情

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _Database: 数据库名字
        :type Database: str
        :param _ErrTime: 错误发生时间
        :type ErrTime: str
        :param _ErrMsg: 错误消息
        :type ErrMsg: str
        """
        self._UserName = None
        self._Database = None
        self._ErrTime = None
        self._ErrMsg = None

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        r"""数据库名字
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def ErrTime(self):
        r"""错误发生时间
        :rtype: str
        """
        return self._ErrTime

    @ErrTime.setter
    def ErrTime(self, ErrTime):
        self._ErrTime = ErrTime

    @property
    def ErrMsg(self):
        r"""错误消息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._ErrTime = params.get("ErrTime")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    r"""参数修改事件信息

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
        :type ParamName: str
        :param _OldValue: 原参数值
        :type OldValue: str
        :param _NewValue: 本次修改期望参数值
        :type NewValue: str
        :param _ModifyTime: 后台参数修改开始时间
        :type ModifyTime: str
        :param _EffectiveTime: 后台参数生效开始时间
        :type EffectiveTime: str
        :param _State: 修改状态。枚举值：in progress、success、paused
        :type State: str
        :param _Operator: 操作者（一般为用户sub UIN）
        :type Operator: str
        :param _EventLog: 时间日志。
        :type EventLog: str
        """
        self._ParamName = None
        self._OldValue = None
        self._NewValue = None
        self._ModifyTime = None
        self._EffectiveTime = None
        self._State = None
        self._Operator = None
        self._EventLog = None

    @property
    def ParamName(self):
        r"""参数名
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def OldValue(self):
        r"""原参数值
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        r"""本次修改期望参数值
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def ModifyTime(self):
        r"""后台参数修改开始时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def EffectiveTime(self):
        r"""后台参数生效开始时间
        :rtype: str
        """
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def State(self):
        r"""修改状态。枚举值：in progress、success、paused
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Operator(self):
        r"""操作者（一般为用户sub UIN）
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def EventLog(self):
        r"""时间日志。
        :rtype: str
        """
        return self._EventLog

    @EventLog.setter
    def EventLog(self, EventLog):
        self._EventLog = EventLog


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        self._ModifyTime = params.get("ModifyTime")
        self._EffectiveTime = params.get("EffectiveTime")
        self._State = params.get("State")
        self._Operator = params.get("Operator")
        self._EventLog = params.get("EventLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventItem(AbstractModel):
    r"""修改参数条目，以参数为维度

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
        :type ParamName: str
        :param _EventCount: 修改事件数
        :type EventCount: int
        :param _EventDetail: 修改时间详情
        :type EventDetail: list of EventInfo
        """
        self._ParamName = None
        self._EventCount = None
        self._EventDetail = None

    @property
    def ParamName(self):
        r"""参数名
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def EventCount(self):
        r"""修改事件数
        :rtype: int
        """
        return self._EventCount

    @EventCount.setter
    def EventCount(self, EventCount):
        self._EventCount = EventCount

    @property
    def EventDetail(self):
        r"""修改时间详情
        :rtype: list of EventInfo
        """
        return self._EventDetail

    @EventDetail.setter
    def EventDetail(self, EventDetail):
        self._EventDetail = EventDetail


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._EventCount = params.get("EventCount")
        if params.get("EventDetail") is not None:
            self._EventDetail = []
            for item in params.get("EventDetail"):
                obj = EventInfo()
                obj._deserialize(item)
                self._EventDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称等
    * 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    * 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤键的名称。
        :type Name: str
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤键的名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""一个或者多个过滤值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    r"""InquiryPriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称。该参数可以通过调用[ DescribeZones](https://cloud.tencent.com/document/product/409/16769) 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param _SpecCode: 规格ID。该参数可以通过调用[DescribeClasses](https://cloud.tencent.com/document/product/409/89019)接口的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param _Storage: 存储容量大小，单位：GB。该参数的设置步长为10。
        :type Storage: int
        :param _InstanceCount: 实例数量。目前最大数量不超过100，如需一次性创建更多实例，请联系客服支持。
        :type InstanceCount: int
        :param _Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值。
        :type Period: int
        :param _Pid: 【弃字段，不再生效】，计费ID。该参数可以通过调用DescribeProductConfig接口的返回值中的Pid字段来获取。
        :type Pid: int
        :param _InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月）和 POSTPAID（按量计费）。
默认值：PREPAID
        :type InstanceChargeType: str
        :param _InstanceType: 实例类型，默认primary，支持如下：
primary（双机高可用（一主一从））
readonly（只读实例）
        :type InstanceType: str
        :param _DBEngine: DB引擎，默认postgresql，支持如下：
postgresql（云数据库PostgreSQL）
mssql_compatible（MSSQL兼容-云数据库PostgreSQL）
        :type DBEngine: str
        """
        self._Zone = None
        self._SpecCode = None
        self._Storage = None
        self._InstanceCount = None
        self._Period = None
        self._Pid = None
        self._InstanceChargeType = None
        self._InstanceType = None
        self._DBEngine = None

    @property
    def Zone(self):
        r"""可用区名称。该参数可以通过调用[ DescribeZones](https://cloud.tencent.com/document/product/409/16769) 接口的返回值中的Zone字段来获取。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecCode(self):
        r"""规格ID。该参数可以通过调用[DescribeClasses](https://cloud.tencent.com/document/product/409/89019)接口的返回值中的SpecCode字段来获取。
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""存储容量大小，单位：GB。该参数的设置步长为10。
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceCount(self):
        r"""实例数量。目前最大数量不超过100，如需一次性创建更多实例，请联系客服支持。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        r"""购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Pid(self):
        r"""【弃字段，不再生效】，计费ID。该参数可以通过调用DescribeProductConfig接口的返回值中的Pid字段来获取。
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def InstanceChargeType(self):
        r"""实例计费类型。目前支持：PREPAID（预付费，即包年包月）和 POSTPAID（按量计费）。
默认值：PREPAID
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceType(self):
        r"""实例类型，默认primary，支持如下：
primary（双机高可用（一主一从））
readonly（只读实例）
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DBEngine(self):
        r"""DB引擎，默认postgresql，支持如下：
postgresql（云数据库PostgreSQL）
mssql_compatible（MSSQL兼容-云数据库PostgreSQL）
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._Pid = params.get("Pid")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceType = params.get("InstanceType")
        self._DBEngine = params.get("DBEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    r"""InquiryPriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 刊例价，单位：分
        :type OriginalPrice: int
        :param _Price: 折后实际付款金额，单位：分
        :type Price: int
        :param _Currency: 币种。例如，CNY：人民币。
        :type Currency: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._Currency = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        r"""刊例价，单位：分
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        r"""折后实际付款金额，单位：分
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Currency(self):
        r"""币种。例如，CNY：人民币。
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewDBInstanceRequest(AbstractModel):
    r"""InquiryPriceRenewDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)获取。
（此接口仅支持预付费实例的查询）
        :type DBInstanceId: str
        :param _Period: 续费周期，按月计算
        :type Period: int
        """
        self._DBInstanceId = None
        self._Period = None

    @property
    def DBInstanceId(self):
        r"""实例ID，可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)获取。
（此接口仅支持预付费实例的查询）
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Period(self):
        r"""续费周期，按月计算
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewDBInstanceResponse(AbstractModel):
    r"""InquiryPriceRenewDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 刊例价，单位为分。如24650表示246.5元
        :type OriginalPrice: int
        :param _Price: 折后实际付款金额，单位为分。如24650表示246.5元
        :type Price: int
        :param _Currency: 币种。例如，CNY：人民币。
        :type Currency: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._Currency = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        r"""刊例价，单位为分。如24650表示246.5元
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        r"""折后实际付款金额，单位为分。如24650表示246.5元
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Currency(self):
        r"""币种。例如，CNY：人民币。
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    r"""InquiryPriceUpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Storage: 实例的磁盘大小，单位GB
        :type Storage: int
        :param _Memory: 实例的内存大小，单位GB
        :type Memory: int
        :param _DBInstanceId: 实例ID，形如postgres-hez4fh0v。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _InstanceChargeType: 实例计费类型。
        :type InstanceChargeType: str
        :param _Cpu: 实例的Cpu大小，单位Core。
不传入此参数时，默认根据Memory确定的售卖规格所对应的Cpu进行设置。如Memory为2，支持的售卖规格有1核2GiB，则不传入Cpu时，Cpu默认为1。
        :type Cpu: int
        """
        self._Storage = None
        self._Memory = None
        self._DBInstanceId = None
        self._InstanceChargeType = None
        self._Cpu = None

    @property
    def Storage(self):
        r"""实例的磁盘大小，单位GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Memory(self):
        r"""实例的内存大小，单位GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-hez4fh0v。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def InstanceChargeType(self):
        warnings.warn("parameter `InstanceChargeType` is deprecated", DeprecationWarning) 

        r"""实例计费类型。
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        warnings.warn("parameter `InstanceChargeType` is deprecated", DeprecationWarning) 

        self._InstanceChargeType = InstanceChargeType

    @property
    def Cpu(self):
        r"""实例的Cpu大小，单位Core。
不传入此参数时，默认根据Memory确定的售卖规格所对应的Cpu进行设置。如Memory为2，支持的售卖规格有1核2GiB，则不传入Cpu时，Cpu默认为1。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._Storage = params.get("Storage")
        self._Memory = params.get("Memory")
        self._DBInstanceId = params.get("DBInstanceId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    r"""InquiryPriceUpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 刊例价费用
        :type OriginalPrice: int
        :param _Price: 折后实际付款金额
        :type Price: int
        :param _Currency: 币种。例如，CNY：人民币。
        :type Currency: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._Currency = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        r"""刊例价费用
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        r"""折后实际付款金额
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Currency(self):
        r"""币种。例如，CNY：人民币。
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class IsolateDBInstancesRequest(AbstractModel):
    r"""IsolateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: 实例ID集合。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。注意：不推荐同时隔离多个实例。建议每次操作仅传入单个实例ID。
        :type DBInstanceIdSet: list of str
        """
        self._DBInstanceIdSet = None

    @property
    def DBInstanceIdSet(self):
        r"""实例ID集合。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。注意：不推荐同时隔离多个实例。建议每次操作仅传入单个实例ID。
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstancesResponse(AbstractModel):
    r"""IsolateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class LockAccountRequest(AbstractModel):
    r"""LockAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。	
        :type DBInstanceId: str
        :param _UserName: 账号名称。
        :type UserName: str
        """
        self._DBInstanceId = None
        self._UserName = None

    @property
    def DBInstanceId(self):
        r"""实例ID。	
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""账号名称。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockAccountResponse(AbstractModel):
    r"""LockAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class LogBackup(AbstractModel):
    r"""数据库日志备份信息

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param _Id: 备份文件唯一标识。
        :type Id: str
        :param _Name: 备份文件名称。
        :type Name: str
        :param _BackupMethod: 备份方式。枚举值，physical - 物理备份；logical - 逻辑备份。
        :type BackupMethod: str
        :param _BackupMode: 备份模式。枚举值，manual - 手动备份；automatic - 自动备份 。
        :type BackupMode: str
        :param _State: 备份任务状态。枚举值：init、running、finished、failed、canceled
        :type State: str
        :param _Size: 备份集大小，单位bytes。
        :type Size: int
        :param _StartTime: 备份的开始时间。
        :type StartTime: str
        :param _FinishTime: 备份的结束时间。
        :type FinishTime: str
        :param _ExpireTime: 备份的过期时间。
        :type ExpireTime: str
        """
        self._DBInstanceId = None
        self._Id = None
        self._Name = None
        self._BackupMethod = None
        self._BackupMode = None
        self._State = None
        self._Size = None
        self._StartTime = None
        self._FinishTime = None
        self._ExpireTime = None

    @property
    def DBInstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Id(self):
        r"""备份文件唯一标识。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""备份文件名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BackupMethod(self):
        r"""备份方式。枚举值，physical - 物理备份；logical - 逻辑备份。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupMode(self):
        r"""备份模式。枚举值，manual - 手动备份；automatic - 自动备份 。
        :rtype: str
        """
        return self._BackupMode

    @BackupMode.setter
    def BackupMode(self, BackupMode):
        self._BackupMode = BackupMode

    @property
    def State(self):
        r"""备份任务状态。枚举值：init、running、finished、failed、canceled
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Size(self):
        r"""备份集大小，单位bytes。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def StartTime(self):
        r"""备份的开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        r"""备份的结束时间。
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def ExpireTime(self):
        r"""备份的过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupMode = params.get("BackupMode")
        self._State = params.get("State")
        self._Size = params.get("Size")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesRequest(AbstractModel):
    r"""ModifyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _UserName: 修改此账号对某数据库对象的权限。可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :type UserName: str
        :param _ModifyPrivilegeSet: 修改的权限信息，支持批量修改，一次最高修改50条。
        :type ModifyPrivilegeSet: list of ModifyPrivilege
        """
        self._DBInstanceId = None
        self._UserName = None
        self._ModifyPrivilegeSet = None

    @property
    def DBInstanceId(self):
        r"""实例ID。	可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""修改此账号对某数据库对象的权限。可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ModifyPrivilegeSet(self):
        r"""修改的权限信息，支持批量修改，一次最高修改50条。
        :rtype: list of ModifyPrivilege
        """
        return self._ModifyPrivilegeSet

    @ModifyPrivilegeSet.setter
    def ModifyPrivilegeSet(self, ModifyPrivilegeSet):
        self._ModifyPrivilegeSet = ModifyPrivilegeSet


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        if params.get("ModifyPrivilegeSet") is not None:
            self._ModifyPrivilegeSet = []
            for item in params.get("ModifyPrivilegeSet"):
                obj = ModifyPrivilege()
                obj._deserialize(item)
                self._ModifyPrivilegeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    r"""ModifyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAccountRemarkRequest(AbstractModel):
    r"""ModifyAccountRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-4wdeb0zv
        :type DBInstanceId: str
        :param _UserName: 实例用户名
        :type UserName: str
        :param _Remark: 用户UserName对应的新备注
        :type Remark: str
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Remark = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-4wdeb0zv
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""实例用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Remark(self):
        r"""用户UserName对应的新备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountRemarkResponse(AbstractModel):
    r"""ModifyAccountRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    r"""ModifyBackupDownloadRestriction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RestrictionType: 备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。当该参数取值为CUSTOMIZE时，Vpc限制和Ip限制需要至少填写一项。
        :type RestrictionType: str
        :param _VpcRestrictionEffect: vpc限制效力，ALLOW 允许；DENY 拒绝。
        :type VpcRestrictionEffect: str
        :param _VpcIdSet: 允许或拒绝下载备份文件的vpcId列表。
**注意：**该入参会全量替换存量已有集合，非增量更新。修改需传入预期的全量集合。
        :type VpcIdSet: list of str
        :param _IpRestrictionEffect: ip限制效力，ALLOW 允许；DENY 拒绝。
        :type IpRestrictionEffect: str
        :param _IpSet: 允许或拒绝下载备份文件的ip列表。
**注意：**该入参会全量替换存量已有集合，非增量更新。修改需传入预期的全量集合。
        :type IpSet: list of str
        """
        self._RestrictionType = None
        self._VpcRestrictionEffect = None
        self._VpcIdSet = None
        self._IpRestrictionEffect = None
        self._IpSet = None

    @property
    def RestrictionType(self):
        r"""备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。当该参数取值为CUSTOMIZE时，Vpc限制和Ip限制需要至少填写一项。
        :rtype: str
        """
        return self._RestrictionType

    @RestrictionType.setter
    def RestrictionType(self, RestrictionType):
        self._RestrictionType = RestrictionType

    @property
    def VpcRestrictionEffect(self):
        r"""vpc限制效力，ALLOW 允许；DENY 拒绝。
        :rtype: str
        """
        return self._VpcRestrictionEffect

    @VpcRestrictionEffect.setter
    def VpcRestrictionEffect(self, VpcRestrictionEffect):
        self._VpcRestrictionEffect = VpcRestrictionEffect

    @property
    def VpcIdSet(self):
        r"""允许或拒绝下载备份文件的vpcId列表。
**注意：**该入参会全量替换存量已有集合，非增量更新。修改需传入预期的全量集合。
        :rtype: list of str
        """
        return self._VpcIdSet

    @VpcIdSet.setter
    def VpcIdSet(self, VpcIdSet):
        self._VpcIdSet = VpcIdSet

    @property
    def IpRestrictionEffect(self):
        r"""ip限制效力，ALLOW 允许；DENY 拒绝。
        :rtype: str
        """
        return self._IpRestrictionEffect

    @IpRestrictionEffect.setter
    def IpRestrictionEffect(self, IpRestrictionEffect):
        self._IpRestrictionEffect = IpRestrictionEffect

    @property
    def IpSet(self):
        r"""允许或拒绝下载备份文件的ip列表。
**注意：**该入参会全量替换存量已有集合，非增量更新。修改需传入预期的全量集合。
        :rtype: list of str
        """
        return self._IpSet

    @IpSet.setter
    def IpSet(self, IpSet):
        self._IpSet = IpSet


    def _deserialize(self, params):
        self._RestrictionType = params.get("RestrictionType")
        self._VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self._VpcIdSet = params.get("VpcIdSet")
        self._IpRestrictionEffect = params.get("IpRestrictionEffect")
        self._IpSet = params.get("IpSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    r"""ModifyBackupDownloadRestriction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBackupPlanRequest(AbstractModel):
    r"""ModifyBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _MinBackupStartTime: 实例最早开始备份时间
        :type MinBackupStartTime: str
        :param _MaxBackupStartTime: 实例最晚开始备份时间
        :type MaxBackupStartTime: str
        :param _BaseBackupRetentionPeriod: 实例备份保留时长，取值范围为7-1830，单位是天
        :type BaseBackupRetentionPeriod: int
        :param _BackupPeriod: 实例备份周期，若是星期维度，格式为小写星期英文单词，且至少设置两天备份；若是按月维度，格式为数字字符，如["1","2"]。
        :type BackupPeriod: list of str
        :param _LogBackupRetentionPeriod: 实例日志备份保留时长，取值范围为7-1830，单位是天
        :type LogBackupRetentionPeriod: int
        :param _PlanId: 备份计划ID，用于指明要修改哪个备份计划，不传则是修改默认备份计划。
        :type PlanId: str
        :param _PlanName: 要修改的备份计划名称。
        :type PlanName: str
        """
        self._DBInstanceId = None
        self._MinBackupStartTime = None
        self._MaxBackupStartTime = None
        self._BaseBackupRetentionPeriod = None
        self._BackupPeriod = None
        self._LogBackupRetentionPeriod = None
        self._PlanId = None
        self._PlanName = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def MinBackupStartTime(self):
        r"""实例最早开始备份时间
        :rtype: str
        """
        return self._MinBackupStartTime

    @MinBackupStartTime.setter
    def MinBackupStartTime(self, MinBackupStartTime):
        self._MinBackupStartTime = MinBackupStartTime

    @property
    def MaxBackupStartTime(self):
        r"""实例最晚开始备份时间
        :rtype: str
        """
        return self._MaxBackupStartTime

    @MaxBackupStartTime.setter
    def MaxBackupStartTime(self, MaxBackupStartTime):
        self._MaxBackupStartTime = MaxBackupStartTime

    @property
    def BaseBackupRetentionPeriod(self):
        r"""实例备份保留时长，取值范围为7-1830，单位是天
        :rtype: int
        """
        return self._BaseBackupRetentionPeriod

    @BaseBackupRetentionPeriod.setter
    def BaseBackupRetentionPeriod(self, BaseBackupRetentionPeriod):
        self._BaseBackupRetentionPeriod = BaseBackupRetentionPeriod

    @property
    def BackupPeriod(self):
        r"""实例备份周期，若是星期维度，格式为小写星期英文单词，且至少设置两天备份；若是按月维度，格式为数字字符，如["1","2"]。
        :rtype: list of str
        """
        return self._BackupPeriod

    @BackupPeriod.setter
    def BackupPeriod(self, BackupPeriod):
        self._BackupPeriod = BackupPeriod

    @property
    def LogBackupRetentionPeriod(self):
        r"""实例日志备份保留时长，取值范围为7-1830，单位是天
        :rtype: int
        """
        return self._LogBackupRetentionPeriod

    @LogBackupRetentionPeriod.setter
    def LogBackupRetentionPeriod(self, LogBackupRetentionPeriod):
        self._LogBackupRetentionPeriod = LogBackupRetentionPeriod

    @property
    def PlanId(self):
        r"""备份计划ID，用于指明要修改哪个备份计划，不传则是修改默认备份计划。
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        r"""要修改的备份计划名称。
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._MinBackupStartTime = params.get("MinBackupStartTime")
        self._MaxBackupStartTime = params.get("MaxBackupStartTime")
        self._BaseBackupRetentionPeriod = params.get("BaseBackupRetentionPeriod")
        self._BackupPeriod = params.get("BackupPeriod")
        self._LogBackupRetentionPeriod = params.get("LogBackupRetentionPeriod")
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupPlanResponse(AbstractModel):
    r"""ModifyBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBaseBackupExpireTimeRequest(AbstractModel):
    r"""ModifyBaseBackupExpireTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _BaseBackupId: 数据备份ID。可通过[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)接口获取
        :type BaseBackupId: str
        :param _NewExpireTime: 新过期时间。
        :type NewExpireTime: str
        """
        self._DBInstanceId = None
        self._BaseBackupId = None
        self._NewExpireTime = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def BaseBackupId(self):
        r"""数据备份ID。可通过[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)接口获取
        :rtype: str
        """
        return self._BaseBackupId

    @BaseBackupId.setter
    def BaseBackupId(self, BaseBackupId):
        self._BaseBackupId = BaseBackupId

    @property
    def NewExpireTime(self):
        r"""新过期时间。
        :rtype: str
        """
        return self._NewExpireTime

    @NewExpireTime.setter
    def NewExpireTime(self, NewExpireTime):
        self._NewExpireTime = NewExpireTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._BaseBackupId = params.get("BaseBackupId")
        self._NewExpireTime = params.get("NewExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBaseBackupExpireTimeResponse(AbstractModel):
    r"""ModifyBaseBackupExpireTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceChargeTypeRequest(AbstractModel):
    r"""ModifyDBInstanceChargeType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _InstanceChargeType: 实例计费类型，目前支持：
<li>PREPAID：预付费，即包年包月</li>
<li>POSTPAID_BY_HOUR：后付费，即按量计费</li>
默认值：PREPAID
        :type InstanceChargeType: str
        :param _Period: 购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
<li>后付费：只支持1</li>
        :type Period: int
        :param _AutoRenewFlag: 续费标记：
<li>0：手动续费</li>
<li>1：自动续费</li>
默认值：0
        :type AutoRenewFlag: int
        :param _AutoVoucher: 是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :type AutoVoucher: int
        """
        self._DBInstanceId = None
        self._InstanceChargeType = None
        self._Period = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def InstanceChargeType(self):
        r"""实例计费类型，目前支持：
<li>PREPAID：预付费，即包年包月</li>
<li>POSTPAID_BY_HOUR：后付费，即按量计费</li>
默认值：PREPAID
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Period(self):
        r"""购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
<li>后付费：只支持1</li>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoRenewFlag(self):
        r"""续费标记：
<li>0：手动续费</li>
<li>1：自动续费</li>
默认值：0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Period = params.get("Period")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceChargeTypeResponse(AbstractModel):
    r"""ModifyDBInstanceChargeType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""订单名
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceDeletionProtectionRequest(AbstractModel):
    r"""ModifyDBInstanceDeletionProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例 ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _DeletionProtection: 开启或关闭实例删除保护。true - 开启 ；false - 关闭。
        :type DeletionProtection: bool
        """
        self._DBInstanceId = None
        self._DeletionProtection = None

    @property
    def DBInstanceId(self):
        r"""实例 ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DeletionProtection(self):
        r"""开启或关闭实例删除保护。true - 开启 ；false - 关闭。
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceDeletionProtectionResponse(AbstractModel):
    r"""ModifyDBInstanceDeletionProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceDeploymentRequest(AbstractModel):
    r"""ModifyDBInstanceDeployment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _DBNodeSet: 实例节点部署信息，支持多可用区部署时需要指定每个节点的部署可用区信息。
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :type DBNodeSet: list of DBNode
        :param _SwitchTag: 指定实例配置完成变更后的切换时间。
<li>0：立即切换 </li>
<li>1：指定时间切换</li>
<li>2：维护时间窗口内切换</li>

        :type SwitchTag: int
        :param _SwitchStartTime: 切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchStartTime: str
        :param _SwitchEndTime: 切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchEndTime: str
        """
        self._DBInstanceId = None
        self._DBNodeSet = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DBNodeSet(self):
        r"""实例节点部署信息，支持多可用区部署时需要指定每个节点的部署可用区信息。
可用区信息可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/409/16769) 接口的返回值中的Zone字段来获取。
        :rtype: list of DBNode
        """
        return self._DBNodeSet

    @DBNodeSet.setter
    def DBNodeSet(self, DBNodeSet):
        self._DBNodeSet = DBNodeSet

    @property
    def SwitchTag(self):
        r"""指定实例配置完成变更后的切换时间。
<li>0：立即切换 </li>
<li>1：指定时间切换</li>
<li>2：维护时间窗口内切换</li>

        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        if params.get("DBNodeSet") is not None:
            self._DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self._DBNodeSet.append(obj)
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceDeploymentResponse(AbstractModel):
    r"""ModifyDBInstanceDeployment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceHAConfigRequest(AbstractModel):
    r"""ModifyDBInstanceHAConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _SyncMode: 主从同步方式：
<li>Semi-sync：半同步</li>
<li>Async：异步</li>

        :type SyncMode: str
        :param _MaxStandbyLatency: 高可用备机最大延迟数据量。备节点延迟数据量小于等于该值，且备节点延迟时间小于等于MaxStandbyLag时，可以切换为主节点。
<li>单位：byte</li>
<li>参数范围：[1073741824, 322122547200]</li>
        :type MaxStandbyLatency: int
        :param _MaxStandbyLag: 高可用备机最大延迟时间。备节点延迟时间小于等于该值，且备节点延迟数据量小于等于MaxStandbyLatency时，可以切换为主节点。
<li>单位：s</li>
<li>参数范围：[5, 10]</li>
        :type MaxStandbyLag: int
        :param _MaxSyncStandbyLatency: 同步备机最大延迟数据量。备机延迟数据量小于等于该值，且该备机延迟时间小于等于MaxSyncStandbyLag时，则该备机采用同步复制；否则，采用异步复制。
该参数值针对SyncMode设置为Semi-sync的实例有效。
半同步实例禁止退化为异步复制时，不设置MaxSyncStandbyLatency、MaxSyncStandbyLag。
半同步实例允许退化异步复制时，PostgreSQL 9版本的实例须设置MaxSyncStandbyLatency且不设置MaxSyncStandbyLag，PostgreSQL 10及以上版本的实例须设置MaxSyncStandbyLatency、MaxSyncStandbyLag。
        :type MaxSyncStandbyLatency: int
        :param _MaxSyncStandbyLag: 同步备机最大延迟时间。备机延迟时间小于等于该值，且该备机延迟数据量小于等于MaxSyncStandbyLatency时，则该备机采用同步复制；否则，采用异步复制。
该参数值针对SyncMode设置为Semi-sync的实例有效。
半同步实例禁止退化为异步复制时，不设置MaxSyncStandbyLatency、MaxSyncStandbyLag。
半同步实例允许退化异步复制时，PostgreSQL 9版本的实例须设置MaxSyncStandbyLatency且不设置MaxSyncStandbyLag，PostgreSQL 10及以上版本的实例须设置MaxSyncStandbyLatency、MaxSyncStandbyLag，
        :type MaxSyncStandbyLag: int
        """
        self._DBInstanceId = None
        self._SyncMode = None
        self._MaxStandbyLatency = None
        self._MaxStandbyLag = None
        self._MaxSyncStandbyLatency = None
        self._MaxSyncStandbyLag = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def SyncMode(self):
        r"""主从同步方式：
<li>Semi-sync：半同步</li>
<li>Async：异步</li>

        :rtype: str
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def MaxStandbyLatency(self):
        r"""高可用备机最大延迟数据量。备节点延迟数据量小于等于该值，且备节点延迟时间小于等于MaxStandbyLag时，可以切换为主节点。
<li>单位：byte</li>
<li>参数范围：[1073741824, 322122547200]</li>
        :rtype: int
        """
        return self._MaxStandbyLatency

    @MaxStandbyLatency.setter
    def MaxStandbyLatency(self, MaxStandbyLatency):
        self._MaxStandbyLatency = MaxStandbyLatency

    @property
    def MaxStandbyLag(self):
        r"""高可用备机最大延迟时间。备节点延迟时间小于等于该值，且备节点延迟数据量小于等于MaxStandbyLatency时，可以切换为主节点。
<li>单位：s</li>
<li>参数范围：[5, 10]</li>
        :rtype: int
        """
        return self._MaxStandbyLag

    @MaxStandbyLag.setter
    def MaxStandbyLag(self, MaxStandbyLag):
        self._MaxStandbyLag = MaxStandbyLag

    @property
    def MaxSyncStandbyLatency(self):
        r"""同步备机最大延迟数据量。备机延迟数据量小于等于该值，且该备机延迟时间小于等于MaxSyncStandbyLag时，则该备机采用同步复制；否则，采用异步复制。
该参数值针对SyncMode设置为Semi-sync的实例有效。
半同步实例禁止退化为异步复制时，不设置MaxSyncStandbyLatency、MaxSyncStandbyLag。
半同步实例允许退化异步复制时，PostgreSQL 9版本的实例须设置MaxSyncStandbyLatency且不设置MaxSyncStandbyLag，PostgreSQL 10及以上版本的实例须设置MaxSyncStandbyLatency、MaxSyncStandbyLag。
        :rtype: int
        """
        return self._MaxSyncStandbyLatency

    @MaxSyncStandbyLatency.setter
    def MaxSyncStandbyLatency(self, MaxSyncStandbyLatency):
        self._MaxSyncStandbyLatency = MaxSyncStandbyLatency

    @property
    def MaxSyncStandbyLag(self):
        r"""同步备机最大延迟时间。备机延迟时间小于等于该值，且该备机延迟数据量小于等于MaxSyncStandbyLatency时，则该备机采用同步复制；否则，采用异步复制。
该参数值针对SyncMode设置为Semi-sync的实例有效。
半同步实例禁止退化为异步复制时，不设置MaxSyncStandbyLatency、MaxSyncStandbyLag。
半同步实例允许退化异步复制时，PostgreSQL 9版本的实例须设置MaxSyncStandbyLatency且不设置MaxSyncStandbyLag，PostgreSQL 10及以上版本的实例须设置MaxSyncStandbyLatency、MaxSyncStandbyLag，
        :rtype: int
        """
        return self._MaxSyncStandbyLag

    @MaxSyncStandbyLag.setter
    def MaxSyncStandbyLag(self, MaxSyncStandbyLag):
        self._MaxSyncStandbyLag = MaxSyncStandbyLag


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._SyncMode = params.get("SyncMode")
        self._MaxStandbyLatency = params.get("MaxStandbyLatency")
        self._MaxStandbyLag = params.get("MaxStandbyLag")
        self._MaxSyncStandbyLatency = params.get("MaxSyncStandbyLatency")
        self._MaxSyncStandbyLag = params.get("MaxSyncStandbyLag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceHAConfigResponse(AbstractModel):
    r"""ModifyDBInstanceHAConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    r"""ModifyDBInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 数据库实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _InstanceName: 实例名称，仅支持长度小于60的中文/英文/数字/"_"/"-"。

        :type InstanceName: str
        """
        self._DBInstanceId = None
        self._InstanceName = None

    @property
    def DBInstanceId(self):
        r"""数据库实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def InstanceName(self):
        r"""实例名称，仅支持长度小于60的中文/英文/数字/"_"/"-"。

        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    r"""ModifyDBInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceParametersRequest(AbstractModel):
    r"""ModifyDBInstanceParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _ParamList: 待修改参数及期望值。
        :type ParamList: list of ParamEntry
        """
        self._DBInstanceId = None
        self._ParamList = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ParamList(self):
        r"""待修改参数及期望值。
        :rtype: list of ParamEntry
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamEntry()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceParametersResponse(AbstractModel):
    r"""ModifyDBInstanceParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceReadOnlyGroupRequest(AbstractModel):
    r"""ModifyDBInstanceReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: 当前实例所在只读组ID
        :type ReadOnlyGroupId: str
        :param _NewReadOnlyGroupId: 实例修改的目标只读组ID
        :type NewReadOnlyGroupId: str
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None
        self._NewReadOnlyGroupId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""当前实例所在只读组ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def NewReadOnlyGroupId(self):
        r"""实例修改的目标只读组ID
        :rtype: str
        """
        return self._NewReadOnlyGroupId

    @NewReadOnlyGroupId.setter
    def NewReadOnlyGroupId(self, NewReadOnlyGroupId):
        self._NewReadOnlyGroupId = NewReadOnlyGroupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._NewReadOnlyGroupId = params.get("NewReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceReadOnlyGroupResponse(AbstractModel):
    r"""ModifyDBInstanceReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSSLConfigRequest(AbstractModel):
    r"""ModifyDBInstanceSSLConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例 ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _SSLEnabled: 开启或关闭SSL。true - 开启 ；false - 关闭。
        :type SSLEnabled: bool
        :param _ConnectAddress: SSL证书保护的唯一连接地址，若为主实例，可设置为内外网IP地址；若为只读实例，可设置为实例IP或只读组IP。在开启SSL或修改SSL保护的连接地址时，该参数为必传项；在关闭SSL时，该参数将被忽略。
        :type ConnectAddress: str
        """
        self._DBInstanceId = None
        self._SSLEnabled = None
        self._ConnectAddress = None

    @property
    def DBInstanceId(self):
        r"""实例 ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def SSLEnabled(self):
        r"""开启或关闭SSL。true - 开启 ；false - 关闭。
        :rtype: bool
        """
        return self._SSLEnabled

    @SSLEnabled.setter
    def SSLEnabled(self, SSLEnabled):
        self._SSLEnabled = SSLEnabled

    @property
    def ConnectAddress(self):
        r"""SSL证书保护的唯一连接地址，若为主实例，可设置为内外网IP地址；若为只读实例，可设置为实例IP或只读组IP。在开启SSL或修改SSL保护的连接地址时，该参数为必传项；在关闭SSL时，该参数将被忽略。
        :rtype: str
        """
        return self._ConnectAddress

    @ConnectAddress.setter
    def ConnectAddress(self, ConnectAddress):
        self._ConnectAddress = ConnectAddress


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._SSLEnabled = params.get("SSLEnabled")
        self._ConnectAddress = params.get("ConnectAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSSLConfigResponse(AbstractModel):
    r"""ModifyDBInstanceSSLConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    r"""ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIdSet: 实例或只读组要绑定的安全组列表。
安全组信息可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来查询。
**注意：**该入参会全量替换存量已有集合，非增量更新。修改需传入预期的全量集合。
        :type SecurityGroupIdSet: list of str
        :param _DBInstanceId: 实例ID，可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。DBInstanceId和ReadOnlyGroupId至少传一个；如果都传，忽略ReadOnlyGroupId。
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: 只读组ID，可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取。DBInstanceId和ReadOnlyGroupId至少传一个；如果要修改只读组关联的安全组，只传ReadOnlyGroupId
        :type ReadOnlyGroupId: str
        """
        self._SecurityGroupIdSet = None
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def SecurityGroupIdSet(self):
        r"""实例或只读组要绑定的安全组列表。
安全组信息可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来查询。
**注意：**该入参会全量替换存量已有集合，非增量更新。修改需传入预期的全量集合。
        :rtype: list of str
        """
        return self._SecurityGroupIdSet

    @SecurityGroupIdSet.setter
    def SecurityGroupIdSet(self, SecurityGroupIdSet):
        self._SecurityGroupIdSet = SecurityGroupIdSet

    @property
    def DBInstanceId(self):
        r"""实例ID，可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。DBInstanceId和ReadOnlyGroupId至少传一个；如果都传，忽略ReadOnlyGroupId。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID，可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取。DBInstanceId和ReadOnlyGroupId至少传一个；如果要修改只读组关联的安全组，只传ReadOnlyGroupId
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    r"""ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSpecRequest(AbstractModel):
    r"""ModifyDBInstanceSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如：postgres-6bwgamo3。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _Memory: 修改后的实例内存大小，单位GiB。
        :type Memory: int
        :param _Storage: 修改后的实例磁盘大小，单位GiB。该参数的设置步长为10。
        :type Storage: int
        :param _AutoVoucher: 是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param _ActivityId: 活动ID。
        :type ActivityId: int
        :param _SwitchTag: 指定实例配置完成变更后的切换时间。
<li>0：立即切换 </li>
<li>1：指定时间切换</li>
<li>2：维护时间窗口内</li>切换
默认值：0 
        :type SwitchTag: int
        :param _SwitchStartTime: 切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchStartTime: str
        :param _SwitchEndTime: 切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchEndTime: str
        :param _Cpu: 修改后的实例CPU大小，单位Core。不填写该参数时，默认根据Memory确定Cpu大小。如Memory为2，支持的规格有1核2GiB，则不传入Cpu时，Cpu默认为1。
        :type Cpu: int
        """
        self._DBInstanceId = None
        self._Memory = None
        self._Storage = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ActivityId = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None
        self._Cpu = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如：postgres-6bwgamo3。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Memory(self):
        r"""修改后的实例内存大小，单位GiB。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""修改后的实例磁盘大小，单位GiB。该参数的设置步长为10。
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""代金券ID列表，目前仅支持指定一张代金券。
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ActivityId(self):
        r"""活动ID。
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def SwitchTag(self):
        r"""指定实例配置完成变更后的切换时间。
<li>0：立即切换 </li>
<li>1：指定时间切换</li>
<li>2：维护时间窗口内</li>切换
默认值：0 
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime

    @property
    def Cpu(self):
        r"""修改后的实例CPU大小，单位Core。不填写该参数时，默认根据Memory确定Cpu大小。如Memory为2，支持的规格有1核2GiB，则不传入Cpu时，Cpu默认为1。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._ActivityId = params.get("ActivityId")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSpecResponse(AbstractModel):
    r"""ModifyDBInstanceSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单号。
        :type DealName: str
        :param _BillId: 冻结流水号。
        :type BillId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._BillId = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""订单号。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def BillId(self):
        r"""冻结流水号。
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._BillId = params.get("BillId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    r"""ModifyDBInstancesProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: 实例ID集合。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。支持同时操作多个实例。
        :type DBInstanceIdSet: list of str
        :param _ProjectId: 所属新项目的ID。可通过[DescribeProjects](https://cloud.tencent.com/document/api/651/78725)获取
        :type ProjectId: str
        """
        self._DBInstanceIdSet = None
        self._ProjectId = None

    @property
    def DBInstanceIdSet(self):
        r"""实例ID集合。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。支持同时操作多个实例。
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def ProjectId(self):
        r"""所属新项目的ID。可通过[DescribeProjects](https://cloud.tencent.com/document/api/651/78725)获取
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    r"""ModifyDBInstancesProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 转移项目成功的实例个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        r"""转移项目成功的实例个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseOwnerRequest(AbstractModel):
    r"""ModifyDatabaseOwner请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _DatabaseName: 数据库名称。可通过[DescribeDatabases](https://cloud.tencent.com/document/api/409/43353)接口获取
        :type DatabaseName: str
        :param _DatabaseOwner: 数据库新所有者。可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :type DatabaseOwner: str
        """
        self._DBInstanceId = None
        self._DatabaseName = None
        self._DatabaseOwner = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DatabaseName(self):
        r"""数据库名称。可通过[DescribeDatabases](https://cloud.tencent.com/document/api/409/43353)接口获取
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatabaseOwner(self):
        r"""数据库新所有者。可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :rtype: str
        """
        return self._DatabaseOwner

    @DatabaseOwner.setter
    def DatabaseOwner(self, DatabaseOwner):
        self._DatabaseOwner = DatabaseOwner


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._DatabaseName = params.get("DatabaseName")
        self._DatabaseOwner = params.get("DatabaseOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseOwnerResponse(AbstractModel):
    r"""ModifyDatabaseOwner返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMaintainTimeWindowRequest(AbstractModel):
    r"""ModifyMaintainTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _MaintainStartTime: 维护开始时间。时区为东八区（UTC+8）
        :type MaintainStartTime: str
        :param _MaintainDuration: 维护持续时间。单位：小时。取值范围：[1,4]
        :type MaintainDuration: int
        :param _MaintainWeekDays: 维护周期
        :type MaintainWeekDays: list of str
        """
        self._DBInstanceId = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def MaintainStartTime(self):
        r"""维护开始时间。时区为东八区（UTC+8）
        :rtype: str
        """
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        r"""维护持续时间。单位：小时。取值范围：[1,4]
        :rtype: int
        """
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        r"""维护周期
        :rtype: list of str
        """
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintainTimeWindowResponse(AbstractModel):
    r"""ModifyMaintainTimeWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyParameterTemplateRequest(AbstractModel):
    r"""ModifyParameterTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID，用于唯一确认参数模板，不可修改。可通过[DescribeParameterTemplates](https://cloud.tencent.com/document/api/409/84067)接口获取
        :type TemplateId: str
        :param _TemplateName: 参数模板名称，长度为1～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@  注：若该字段为空    ，则保持原参数模板名称
        :type TemplateName: str
        :param _TemplateDescription: 参数模板描述，长度为0～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@  注：若不传入该参数，则保持原参数模板描述
        :type TemplateDescription: str
        :param _ModifyParamEntrySet: 需要修改或添加的参数集合，注：同一参数不能同时出现在修改添加集合和删除集合中
        :type ModifyParamEntrySet: list of ParamEntry
        :param _DeleteParamSet: 需要从模板中删除的参数集合，注：同一参数不能同时出现在修改添加集合和删除集合中
        :type DeleteParamSet: list of str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._ModifyParamEntrySet = None
        self._DeleteParamSet = None

    @property
    def TemplateId(self):
        r"""参数模板ID，用于唯一确认参数模板，不可修改。可通过[DescribeParameterTemplates](https://cloud.tencent.com/document/api/409/84067)接口获取
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""参数模板名称，长度为1～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@  注：若该字段为空    ，则保持原参数模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        r"""参数模板描述，长度为0～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@  注：若不传入该参数，则保持原参数模板描述
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def ModifyParamEntrySet(self):
        r"""需要修改或添加的参数集合，注：同一参数不能同时出现在修改添加集合和删除集合中
        :rtype: list of ParamEntry
        """
        return self._ModifyParamEntrySet

    @ModifyParamEntrySet.setter
    def ModifyParamEntrySet(self, ModifyParamEntrySet):
        self._ModifyParamEntrySet = ModifyParamEntrySet

    @property
    def DeleteParamSet(self):
        r"""需要从模板中删除的参数集合，注：同一参数不能同时出现在修改添加集合和删除集合中
        :rtype: list of str
        """
        return self._DeleteParamSet

    @DeleteParamSet.setter
    def DeleteParamSet(self, DeleteParamSet):
        self._DeleteParamSet = DeleteParamSet


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        if params.get("ModifyParamEntrySet") is not None:
            self._ModifyParamEntrySet = []
            for item in params.get("ModifyParamEntrySet"):
                obj = ParamEntry()
                obj._deserialize(item)
                self._ModifyParamEntrySet.append(obj)
        self._DeleteParamSet = params.get("DeleteParamSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParameterTemplateResponse(AbstractModel):
    r"""ModifyParameterTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPrivilege(AbstractModel):
    r"""用于修改数据库对象的权限，其中包含了数据库对象描述的数据结构、需要修改的权限列表以及修改的类型等。

    """

    def __init__(self):
        r"""
        :param _DatabasePrivilege: 要修改的数据库对象及权限列表
        :type DatabasePrivilege: :class:`tencentcloud.postgres.v20170312.models.DatabasePrivilege`
        :param _ModifyType: 修改的方式，当前仅支持grantObject、revokeObject、alterRole。grantObject代表授权、revokeObject代表收回权、alterRole代表修改账号类型。
        :type ModifyType: str
        :param _IsCascade: 当ModifyType为revokeObject才需要此参数，参数为true时，撤销权限会级联撤销。默认为false。
        :type IsCascade: bool
        """
        self._DatabasePrivilege = None
        self._ModifyType = None
        self._IsCascade = None

    @property
    def DatabasePrivilege(self):
        r"""要修改的数据库对象及权限列表
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DatabasePrivilege`
        """
        return self._DatabasePrivilege

    @DatabasePrivilege.setter
    def DatabasePrivilege(self, DatabasePrivilege):
        self._DatabasePrivilege = DatabasePrivilege

    @property
    def ModifyType(self):
        r"""修改的方式，当前仅支持grantObject、revokeObject、alterRole。grantObject代表授权、revokeObject代表收回权、alterRole代表修改账号类型。
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def IsCascade(self):
        r"""当ModifyType为revokeObject才需要此参数，参数为true时，撤销权限会级联撤销。默认为false。
        :rtype: bool
        """
        return self._IsCascade

    @IsCascade.setter
    def IsCascade(self, IsCascade):
        self._IsCascade = IsCascade


    def _deserialize(self, params):
        if params.get("DatabasePrivilege") is not None:
            self._DatabasePrivilege = DatabasePrivilege()
            self._DatabasePrivilege._deserialize(params.get("DatabasePrivilege"))
        self._ModifyType = params.get("ModifyType")
        self._IsCascade = params.get("IsCascade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyDBInstanceWeightRequest(AbstractModel):
    r"""ModifyReadOnlyDBInstanceWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: 只读组ID。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :type ReadOnlyGroupId: str
        :param _Weight: 只读实例在只读组中的流量权重(1-50)
        :type Weight: int
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None
        self._Weight = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def Weight(self):
        r"""只读实例在只读组中的流量权重(1-50)
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyDBInstanceWeightResponse(AbstractModel):
    r"""ModifyReadOnlyDBInstanceWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyReadOnlyGroupConfigRequest(AbstractModel):
    r"""ModifyReadOnlyGroupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 只读组ID。
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 只读组名称。仅支持长度小于60的中文/英文/数字/"_"/"-"
        :type ReadOnlyGroupName: str
        :param _ReplayLagEliminate: 延迟时间配置开关：0关、1开
        :type ReplayLagEliminate: int
        :param _ReplayLatencyEliminate: 延迟日志大小配置开关：0关、1开
        :type ReplayLatencyEliminate: int
        :param _MaxReplayLatency: 延迟日志大小阈值，单位MB。当开启延迟日志大小配置，应输入正整数
        :type MaxReplayLatency: int
        :param _MaxReplayLag: 延迟时间大小阈值，单位s。当开启延迟时间配置时，应输入正整数。
        :type MaxReplayLag: int
        :param _Rebalance: 自动负载均衡开关：0关、1开
        :type Rebalance: int
        :param _MinDelayEliminateReserve: 延迟剔除最小保留实例数。取值范围[0,100]
        :type MinDelayEliminateReserve: int
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._ReplayLagEliminate = None
        self._ReplayLatencyEliminate = None
        self._MaxReplayLatency = None
        self._MaxReplayLag = None
        self._Rebalance = None
        self._MinDelayEliminateReserve = None

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID。
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""只读组名称。仅支持长度小于60的中文/英文/数字/"_"/"-"
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ReplayLagEliminate(self):
        r"""延迟时间配置开关：0关、1开
        :rtype: int
        """
        return self._ReplayLagEliminate

    @ReplayLagEliminate.setter
    def ReplayLagEliminate(self, ReplayLagEliminate):
        self._ReplayLagEliminate = ReplayLagEliminate

    @property
    def ReplayLatencyEliminate(self):
        r"""延迟日志大小配置开关：0关、1开
        :rtype: int
        """
        return self._ReplayLatencyEliminate

    @ReplayLatencyEliminate.setter
    def ReplayLatencyEliminate(self, ReplayLatencyEliminate):
        self._ReplayLatencyEliminate = ReplayLatencyEliminate

    @property
    def MaxReplayLatency(self):
        r"""延迟日志大小阈值，单位MB。当开启延迟日志大小配置，应输入正整数
        :rtype: int
        """
        return self._MaxReplayLatency

    @MaxReplayLatency.setter
    def MaxReplayLatency(self, MaxReplayLatency):
        self._MaxReplayLatency = MaxReplayLatency

    @property
    def MaxReplayLag(self):
        r"""延迟时间大小阈值，单位s。当开启延迟时间配置时，应输入正整数。
        :rtype: int
        """
        return self._MaxReplayLag

    @MaxReplayLag.setter
    def MaxReplayLag(self, MaxReplayLag):
        self._MaxReplayLag = MaxReplayLag

    @property
    def Rebalance(self):
        r"""自动负载均衡开关：0关、1开
        :rtype: int
        """
        return self._Rebalance

    @Rebalance.setter
    def Rebalance(self, Rebalance):
        self._Rebalance = Rebalance

    @property
    def MinDelayEliminateReserve(self):
        r"""延迟剔除最小保留实例数。取值范围[0,100]
        :rtype: int
        """
        return self._MinDelayEliminateReserve

    @MinDelayEliminateReserve.setter
    def MinDelayEliminateReserve(self, MinDelayEliminateReserve):
        self._MinDelayEliminateReserve = MinDelayEliminateReserve


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._ReplayLagEliminate = params.get("ReplayLagEliminate")
        self._ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self._MaxReplayLatency = params.get("MaxReplayLatency")
        self._MaxReplayLag = params.get("MaxReplayLag")
        self._Rebalance = params.get("Rebalance")
        self._MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyGroupConfigResponse(AbstractModel):
    r"""ModifyReadOnlyGroupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySwitchTimePeriodRequest(AbstractModel):
    r"""ModifySwitchTimePeriod请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 处于等待切换状态中的实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _SwitchTag: 入参取值为 0 ，代表立即切换。
        :type SwitchTag: int
        """
        self._DBInstanceId = None
        self._SwitchTag = None

    @property
    def DBInstanceId(self):
        r"""处于等待切换状态中的实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def SwitchTag(self):
        r"""入参取值为 0 ，代表立即切换。
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._SwitchTag = params.get("SwitchTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySwitchTimePeriodResponse(AbstractModel):
    r"""ModifySwitchTimePeriod返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NetworkAccess(AbstractModel):
    r"""网络相关信息。（该数据结构已废弃，网络相关信息使用DBInstanceNetInfo）

    """

    def __init__(self):
        r"""
        :param _ResourceId: 网络资源id，实例id或RO组id
        :type ResourceId: str
        :param _ResourceType: 资源类型，1-实例 2-RO组
        :type ResourceType: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _Vip: IPV4地址
        :type Vip: str
        :param _Vip6: IPV6地址
        :type Vip6: str
        :param _Vport: 访问端口
        :type Vport: int
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _VpcStatus: 网络状态，1-申请中，2-使用中，3-删除中，4-已删除
        :type VpcStatus: int
        """
        self._ResourceId = None
        self._ResourceType = None
        self._VpcId = None
        self._Vip = None
        self._Vip6 = None
        self._Vport = None
        self._SubnetId = None
        self._VpcStatus = None

    @property
    def ResourceId(self):
        r"""网络资源id，实例id或RO组id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型，1-实例 2-RO组
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def VpcId(self):
        r"""私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        r"""IPV4地址
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vip6(self):
        r"""IPV6地址
        :rtype: str
        """
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def Vport(self):
        r"""访问端口
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def SubnetId(self):
        r"""子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcStatus(self):
        r"""网络状态，1-申请中，2-使用中，3-删除中，4-已删除
        :rtype: int
        """
        return self._VpcStatus

    @VpcStatus.setter
    def VpcStatus(self, VpcStatus):
        self._VpcStatus = VpcStatus


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._VpcId = params.get("VpcId")
        self._Vip = params.get("Vip")
        self._Vip6 = params.get("Vip6")
        self._Vport = params.get("Vport")
        self._SubnetId = params.get("SubnetId")
        self._VpcStatus = params.get("VpcStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAccountCAMRequest(AbstractModel):
    r"""OpenAccountCAM请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 数据库实例ID
        :type DBInstanceId: str
        :param _UserName: 需要开启CAM服务的账号名称
        :type UserName: str
        """
        self._DBInstanceId = None
        self._UserName = None

    @property
    def DBInstanceId(self):
        r"""数据库实例ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""需要开启CAM服务的账号名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAccountCAMResponse(AbstractModel):
    r"""OpenAccountCAM返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OpenDBExtranetAccessRequest(AbstractModel):
    r"""OpenDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-hez4fh0v。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。
        :type DBInstanceId: str
        :param _IsIpv6: 是否开通Ipv6外网，1：是，0：否
默认值：0
        :type IsIpv6: int
        """
        self._DBInstanceId = None
        self._IsIpv6 = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-hez4fh0v。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def IsIpv6(self):
        r"""是否开通Ipv6外网，1：是，0：否
默认值：0
        :rtype: int
        """
        return self._IsIpv6

    @IsIpv6.setter
    def IsIpv6(self, IsIpv6):
        self._IsIpv6 = IsIpv6


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._IsIpv6 = params.get("IsIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessResponse(AbstractModel):
    r"""OpenDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ParamEntry(AbstractModel):
    r"""批量修改参数

    """

    def __init__(self):
        r"""
        :param _Name: 参数名
        :type Name: str
        :param _ExpectedValue: 修改参数值。入参均以字符串形式传递，例如：小数”0.1“、整数”1000“、枚举”replica“
        :type ExpectedValue: str
        """
        self._Name = None
        self._ExpectedValue = None

    @property
    def Name(self):
        r"""参数名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ExpectedValue(self):
        r"""修改参数值。入参均以字符串形式传递，例如：小数”0.1“、整数”1000“、枚举”replica“
        :rtype: str
        """
        return self._ExpectedValue

    @ExpectedValue.setter
    def ExpectedValue(self, ExpectedValue):
        self._ExpectedValue = ExpectedValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ExpectedValue = params.get("ExpectedValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    r"""参数详情

    """

    def __init__(self):
        r"""
        :param _ID: 参数ID
        :type ID: int
        :param _Name: 参数名
        :type Name: str
        :param _ParamValueType: 参数值类型：integer（整型）、real（浮点型）、bool（布尔型）、enum（枚举类型）、mutil_enum（枚举类型、支持多选）。
当参数类型为integer（整型）、real（浮点型）时，参数的取值范围根据返回值的Max、Min确定； 
当参数类型为bool（布尔型）时，参数设置值取值范围是true | false； 
当参数类型为enum（枚举类型）、mutil_enum（多枚举类型）时，参数的取值范围由返回值中的EnumValue确定。
        :type ParamValueType: str
        :param _Unit: 参数值 单位。参数没有单位时，该字段返回空
        :type Unit: str
        :param _DefaultValue: 参数默认值。以字符串形式返回
        :type DefaultValue: str
        :param _CurrentValue: 参数当前运行值。以字符串形式返回
        :type CurrentValue: str
        :param _Max: 数值类型（integer、real）参数，取值下界
        :type Max: float
        :param _EnumValue: 枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        :param _Min: 数值类型（integer、real）参数，取值上界
        :type Min: float
        :param _ParamDescriptionCH: 参数中文描述
        :type ParamDescriptionCH: str
        :param _ParamDescriptionEN: 参数英文描述
        :type ParamDescriptionEN: str
        :param _NeedReboot: 参数修改，是否重启生效。（true为需要，false为不需要）
        :type NeedReboot: bool
        :param _ClassificationCN: 参数中文分类
        :type ClassificationCN: str
        :param _ClassificationEN: 参数英文分类
        :type ClassificationEN: str
        :param _SpecRelated: 是否和规格相关。（true为相关，false为不想关）
        :type SpecRelated: bool
        :param _Advanced: 是否为重点参数。（true为重点参数，修改是需要重点关注，可能会影响实例性能）
        :type Advanced: bool
        :param _LastModifyTime: 参数最后一次修改时间
        :type LastModifyTime: str
        :param _StandbyRelated: 参数主备制约，0：无主备制约关系，1:备机参数值需比主机大，2:主机参数值需比备机大
        :type StandbyRelated: int
        :param _VersionRelationSet: 参数版本关联信息，内容为相应内核版本下的参数详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionRelationSet: list of ParamVersionRelation
        :param _SpecRelationSet: 参数规格关联信息，内容为相应规格下的参数详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecRelationSet: list of ParamSpecRelation
        """
        self._ID = None
        self._Name = None
        self._ParamValueType = None
        self._Unit = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Max = None
        self._EnumValue = None
        self._Min = None
        self._ParamDescriptionCH = None
        self._ParamDescriptionEN = None
        self._NeedReboot = None
        self._ClassificationCN = None
        self._ClassificationEN = None
        self._SpecRelated = None
        self._Advanced = None
        self._LastModifyTime = None
        self._StandbyRelated = None
        self._VersionRelationSet = None
        self._SpecRelationSet = None

    @property
    def ID(self):
        r"""参数ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""参数名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamValueType(self):
        r"""参数值类型：integer（整型）、real（浮点型）、bool（布尔型）、enum（枚举类型）、mutil_enum（枚举类型、支持多选）。
当参数类型为integer（整型）、real（浮点型）时，参数的取值范围根据返回值的Max、Min确定； 
当参数类型为bool（布尔型）时，参数设置值取值范围是true | false； 
当参数类型为enum（枚举类型）、mutil_enum（多枚举类型）时，参数的取值范围由返回值中的EnumValue确定。
        :rtype: str
        """
        return self._ParamValueType

    @ParamValueType.setter
    def ParamValueType(self, ParamValueType):
        self._ParamValueType = ParamValueType

    @property
    def Unit(self):
        r"""参数值 单位。参数没有单位时，该字段返回空
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def DefaultValue(self):
        r"""参数默认值。以字符串形式返回
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        r"""参数当前运行值。以字符串形式返回
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Max(self):
        r"""数值类型（integer、real）参数，取值下界
        :rtype: float
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def EnumValue(self):
        r"""枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Min(self):
        r"""数值类型（integer、real）参数，取值上界
        :rtype: float
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ParamDescriptionCH(self):
        r"""参数中文描述
        :rtype: str
        """
        return self._ParamDescriptionCH

    @ParamDescriptionCH.setter
    def ParamDescriptionCH(self, ParamDescriptionCH):
        self._ParamDescriptionCH = ParamDescriptionCH

    @property
    def ParamDescriptionEN(self):
        r"""参数英文描述
        :rtype: str
        """
        return self._ParamDescriptionEN

    @ParamDescriptionEN.setter
    def ParamDescriptionEN(self, ParamDescriptionEN):
        self._ParamDescriptionEN = ParamDescriptionEN

    @property
    def NeedReboot(self):
        r"""参数修改，是否重启生效。（true为需要，false为不需要）
        :rtype: bool
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def ClassificationCN(self):
        r"""参数中文分类
        :rtype: str
        """
        return self._ClassificationCN

    @ClassificationCN.setter
    def ClassificationCN(self, ClassificationCN):
        self._ClassificationCN = ClassificationCN

    @property
    def ClassificationEN(self):
        r"""参数英文分类
        :rtype: str
        """
        return self._ClassificationEN

    @ClassificationEN.setter
    def ClassificationEN(self, ClassificationEN):
        self._ClassificationEN = ClassificationEN

    @property
    def SpecRelated(self):
        r"""是否和规格相关。（true为相关，false为不想关）
        :rtype: bool
        """
        return self._SpecRelated

    @SpecRelated.setter
    def SpecRelated(self, SpecRelated):
        self._SpecRelated = SpecRelated

    @property
    def Advanced(self):
        r"""是否为重点参数。（true为重点参数，修改是需要重点关注，可能会影响实例性能）
        :rtype: bool
        """
        return self._Advanced

    @Advanced.setter
    def Advanced(self, Advanced):
        self._Advanced = Advanced

    @property
    def LastModifyTime(self):
        r"""参数最后一次修改时间
        :rtype: str
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def StandbyRelated(self):
        r"""参数主备制约，0：无主备制约关系，1:备机参数值需比主机大，2:主机参数值需比备机大
        :rtype: int
        """
        return self._StandbyRelated

    @StandbyRelated.setter
    def StandbyRelated(self, StandbyRelated):
        self._StandbyRelated = StandbyRelated

    @property
    def VersionRelationSet(self):
        r"""参数版本关联信息，内容为相应内核版本下的参数详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamVersionRelation
        """
        return self._VersionRelationSet

    @VersionRelationSet.setter
    def VersionRelationSet(self, VersionRelationSet):
        self._VersionRelationSet = VersionRelationSet

    @property
    def SpecRelationSet(self):
        r"""参数规格关联信息，内容为相应规格下的参数详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamSpecRelation
        """
        return self._SpecRelationSet

    @SpecRelationSet.setter
    def SpecRelationSet(self, SpecRelationSet):
        self._SpecRelationSet = SpecRelationSet


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._ParamValueType = params.get("ParamValueType")
        self._Unit = params.get("Unit")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Max = params.get("Max")
        self._EnumValue = params.get("EnumValue")
        self._Min = params.get("Min")
        self._ParamDescriptionCH = params.get("ParamDescriptionCH")
        self._ParamDescriptionEN = params.get("ParamDescriptionEN")
        self._NeedReboot = params.get("NeedReboot")
        self._ClassificationCN = params.get("ClassificationCN")
        self._ClassificationEN = params.get("ClassificationEN")
        self._SpecRelated = params.get("SpecRelated")
        self._Advanced = params.get("Advanced")
        self._LastModifyTime = params.get("LastModifyTime")
        self._StandbyRelated = params.get("StandbyRelated")
        if params.get("VersionRelationSet") is not None:
            self._VersionRelationSet = []
            for item in params.get("VersionRelationSet"):
                obj = ParamVersionRelation()
                obj._deserialize(item)
                self._VersionRelationSet.append(obj)
        if params.get("SpecRelationSet") is not None:
            self._SpecRelationSet = []
            for item in params.get("SpecRelationSet"):
                obj = ParamSpecRelation()
                obj._deserialize(item)
                self._SpecRelationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamSpecRelation(AbstractModel):
    r"""各规格下的参数信息

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _Memory: 参数信息所属规格
        :type Memory: str
        :param _Value: 参数在该规格下的默认值
        :type Value: str
        :param _Unit: 参数值单位。参数没有单位时，该字段返回空
        :type Unit: str
        :param _Max: 数值类型（integer、real）参数，取值上界
        :type Max: float
        :param _Min: 数值类型（integer、real）参数，取值下界
        :type Min: float
        :param _EnumValue: 枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        """
        self._Name = None
        self._Memory = None
        self._Value = None
        self._Unit = None
        self._Max = None
        self._Min = None
        self._EnumValue = None

    @property
    def Name(self):
        r"""参数名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Memory(self):
        r"""参数信息所属规格
        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Value(self):
        r"""参数在该规格下的默认值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        r"""参数值单位。参数没有单位时，该字段返回空
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Max(self):
        r"""数值类型（integer、real）参数，取值上界
        :rtype: float
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        r"""数值类型（integer、real）参数，取值下界
        :rtype: float
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        r"""枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Memory = params.get("Memory")
        self._Value = params.get("Value")
        self._Unit = params.get("Unit")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamVersionRelation(AbstractModel):
    r"""各版本下的参数信息

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _DBKernelVersion: 参数信息所属内核版本
        :type DBKernelVersion: str
        :param _Value: 参数在该版本该规格下的默认值
        :type Value: str
        :param _Unit: 参数值单位。参数没有单位时，该字段返回空
        :type Unit: str
        :param _Max: 数值类型（integer、real）参数，取值上界
        :type Max: float
        :param _Min: 数值类型（integer、real）参数，取值下界
        :type Min: float
        :param _EnumValue: 枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        """
        self._Name = None
        self._DBKernelVersion = None
        self._Value = None
        self._Unit = None
        self._Max = None
        self._Min = None
        self._EnumValue = None

    @property
    def Name(self):
        r"""参数名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DBKernelVersion(self):
        r"""参数信息所属内核版本
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def Value(self):
        r"""参数在该版本该规格下的默认值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        r"""参数值单位。参数没有单位时，该字段返回空
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Max(self):
        r"""数值类型（integer、real）参数，取值上界
        :rtype: float
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        r"""数值类型（integer、real）参数，取值下界
        :rtype: float
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        r"""枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._Value = params.get("Value")
        self._Unit = params.get("Unit")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterTemplate(AbstractModel):
    r"""参数模板的基本信息

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID
        :type TemplateId: str
        :param _TemplateName: 参数模板名称
        :type TemplateName: str
        :param _DBMajorVersion: 参数模板适用的数据库版本
        :type DBMajorVersion: str
        :param _DBEngine: 参数模板适用的数据库引擎
        :type DBEngine: str
        :param _TemplateDescription: 参数模板描述
        :type TemplateDescription: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._DBMajorVersion = None
        self._DBEngine = None
        self._TemplateDescription = None

    @property
    def TemplateId(self):
        r"""参数模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""参数模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def DBMajorVersion(self):
        r"""参数模板适用的数据库版本
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBEngine(self):
        r"""参数模板适用的数据库引擎
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def TemplateDescription(self):
        r"""参数模板描述
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBEngine = params.get("DBEngine")
        self._TemplateDescription = params.get("TemplateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PgDeal(AbstractModel):
    r"""订单详情

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名
        :type DealName: str
        :param _OwnerUin: 所属用户
        :type OwnerUin: str
        :param _Count: 订单涉及多少个实例
        :type Count: int
        :param _PayMode: 付费模式。1-预付费；0-后付费
        :type PayMode: int
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _DBInstanceIdSet: 实例ID数组
        :type DBInstanceIdSet: list of str
        """
        self._DealName = None
        self._OwnerUin = None
        self._Count = None
        self._PayMode = None
        self._FlowId = None
        self._DBInstanceIdSet = None

    @property
    def DealName(self):
        r"""订单名
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def OwnerUin(self):
        r"""所属用户
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Count(self):
        r"""订单涉及多少个实例
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def PayMode(self):
        r"""付费模式。1-预付费；0-后付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def FlowId(self):
        r"""异步任务流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DBInstanceIdSet(self):
        r"""实例ID数组
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._OwnerUin = params.get("OwnerUin")
        self._Count = params.get("Count")
        self._PayMode = params.get("PayMode")
        self._FlowId = params.get("FlowId")
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyRule(AbstractModel):
    r"""安全组规则信息

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param _CidrIp: 来源或目的 IP 或 IP 段，例如172.16.0.0/12
        :type CidrIp: str
        :param _PortRange: 端口
        :type PortRange: str
        :param _IpProtocol: 网络协议，支持 UDP、TCP 等
        :type IpProtocol: str
        :param _Description: 规则描述
        :type Description: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Description = None

    @property
    def Action(self):
        r"""策略，ACCEPT 或者 DROP
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        r"""来源或目的 IP 或 IP 段，例如172.16.0.0/12
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        r"""端口
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        r"""网络协议，支持 UDP、TCP 等
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawSlowQuery(AbstractModel):
    r"""慢SQL查询接口返回 慢SQL列表详情

    """

    def __init__(self):
        r"""
        :param _RawQuery: 慢SQL 语句
        :type RawQuery: str
        :param _DatabaseName: 慢SQL 查询的数据库
        :type DatabaseName: str
        :param _Duration: 慢SQL执行 耗时
        :type Duration: float
        :param _ClientAddr: 执行慢SQL的客户端
        :type ClientAddr: str
        :param _UserName: 执行慢SQL的用户名
        :type UserName: str
        :param _SessionStartTime: 慢SQL执行的开始时间
        :type SessionStartTime: str
        """
        self._RawQuery = None
        self._DatabaseName = None
        self._Duration = None
        self._ClientAddr = None
        self._UserName = None
        self._SessionStartTime = None

    @property
    def RawQuery(self):
        r"""慢SQL 语句
        :rtype: str
        """
        return self._RawQuery

    @RawQuery.setter
    def RawQuery(self, RawQuery):
        self._RawQuery = RawQuery

    @property
    def DatabaseName(self):
        r"""慢SQL 查询的数据库
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Duration(self):
        r"""慢SQL执行 耗时
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ClientAddr(self):
        r"""执行慢SQL的客户端
        :rtype: str
        """
        return self._ClientAddr

    @ClientAddr.setter
    def ClientAddr(self, ClientAddr):
        self._ClientAddr = ClientAddr

    @property
    def UserName(self):
        r"""执行慢SQL的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def SessionStartTime(self):
        r"""慢SQL执行的开始时间
        :rtype: str
        """
        return self._SessionStartTime

    @SessionStartTime.setter
    def SessionStartTime(self, SessionStartTime):
        self._SessionStartTime = SessionStartTime


    def _deserialize(self, params):
        self._RawQuery = params.get("RawQuery")
        self._DatabaseName = params.get("DatabaseName")
        self._Duration = params.get("Duration")
        self._ClientAddr = params.get("ClientAddr")
        self._UserName = params.get("UserName")
        self._SessionStartTime = params.get("SessionStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyGroup(AbstractModel):
    r"""只读组信息

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 只读组标识
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 只读组名字
        :type ReadOnlyGroupName: str
        :param _ProjectId: 项目id
        :type ProjectId: int
        :param _MasterDBInstanceId: 主实例id
        :type MasterDBInstanceId: str
        :param _MinDelayEliminateReserve: 最小保留实例数
        :type MinDelayEliminateReserve: int
        :param _MaxReplayLatency: 延迟空间大小阈值。单位MB。
        :type MaxReplayLatency: int
        :param _ReplayLatencyEliminate: 延迟大小开关。0 - 关闭； 1 - 开启。
        :type ReplayLatencyEliminate: int
        :param _MaxReplayLag: 延迟时间大小阈值，单位：秒。
        :type MaxReplayLag: float
        :param _ReplayLagEliminate: 延迟时间开关。0 - 关闭； 1 - 开启。
        :type ReplayLagEliminate: int
        :param _VpcId: 虚拟网络id
        :type VpcId: str
        :param _SubnetId: 子网id
        :type SubnetId: str
        :param _Region: 地域id
        :type Region: str
        :param _Zone: 地区id
        :type Zone: str
        :param _Status: 状态。枚举值：creating、ok、modifying、deleting、deleted
        :type Status: str
        :param _ReadOnlyDBInstanceList: 实例详细信息
        :type ReadOnlyDBInstanceList: list of DBInstance
        :param _Rebalance: 自动负载均衡开关
        :type Rebalance: int
        :param _DBInstanceNetInfo: 网络信息
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param _NetworkAccessList: 只读组网络信息列表（此字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAccessList: list of NetworkAccess
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._ProjectId = None
        self._MasterDBInstanceId = None
        self._MinDelayEliminateReserve = None
        self._MaxReplayLatency = None
        self._ReplayLatencyEliminate = None
        self._MaxReplayLag = None
        self._ReplayLagEliminate = None
        self._VpcId = None
        self._SubnetId = None
        self._Region = None
        self._Zone = None
        self._Status = None
        self._ReadOnlyDBInstanceList = None
        self._Rebalance = None
        self._DBInstanceNetInfo = None
        self._NetworkAccessList = None

    @property
    def ReadOnlyGroupId(self):
        r"""只读组标识
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""只读组名字
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def MasterDBInstanceId(self):
        r"""主实例id
        :rtype: str
        """
        return self._MasterDBInstanceId

    @MasterDBInstanceId.setter
    def MasterDBInstanceId(self, MasterDBInstanceId):
        self._MasterDBInstanceId = MasterDBInstanceId

    @property
    def MinDelayEliminateReserve(self):
        r"""最小保留实例数
        :rtype: int
        """
        return self._MinDelayEliminateReserve

    @MinDelayEliminateReserve.setter
    def MinDelayEliminateReserve(self, MinDelayEliminateReserve):
        self._MinDelayEliminateReserve = MinDelayEliminateReserve

    @property
    def MaxReplayLatency(self):
        r"""延迟空间大小阈值。单位MB。
        :rtype: int
        """
        return self._MaxReplayLatency

    @MaxReplayLatency.setter
    def MaxReplayLatency(self, MaxReplayLatency):
        self._MaxReplayLatency = MaxReplayLatency

    @property
    def ReplayLatencyEliminate(self):
        r"""延迟大小开关。0 - 关闭； 1 - 开启。
        :rtype: int
        """
        return self._ReplayLatencyEliminate

    @ReplayLatencyEliminate.setter
    def ReplayLatencyEliminate(self, ReplayLatencyEliminate):
        self._ReplayLatencyEliminate = ReplayLatencyEliminate

    @property
    def MaxReplayLag(self):
        r"""延迟时间大小阈值，单位：秒。
        :rtype: float
        """
        return self._MaxReplayLag

    @MaxReplayLag.setter
    def MaxReplayLag(self, MaxReplayLag):
        self._MaxReplayLag = MaxReplayLag

    @property
    def ReplayLagEliminate(self):
        r"""延迟时间开关。0 - 关闭； 1 - 开启。
        :rtype: int
        """
        return self._ReplayLagEliminate

    @ReplayLagEliminate.setter
    def ReplayLagEliminate(self, ReplayLagEliminate):
        self._ReplayLagEliminate = ReplayLagEliminate

    @property
    def VpcId(self):
        r"""虚拟网络id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Region(self):
        r"""地域id
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""地区id
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        r"""状态。枚举值：creating、ok、modifying、deleting、deleted
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReadOnlyDBInstanceList(self):
        r"""实例详细信息
        :rtype: list of DBInstance
        """
        return self._ReadOnlyDBInstanceList

    @ReadOnlyDBInstanceList.setter
    def ReadOnlyDBInstanceList(self, ReadOnlyDBInstanceList):
        self._ReadOnlyDBInstanceList = ReadOnlyDBInstanceList

    @property
    def Rebalance(self):
        r"""自动负载均衡开关
        :rtype: int
        """
        return self._Rebalance

    @Rebalance.setter
    def Rebalance(self, Rebalance):
        self._Rebalance = Rebalance

    @property
    def DBInstanceNetInfo(self):
        r"""网络信息
        :rtype: list of DBInstanceNetInfo
        """
        return self._DBInstanceNetInfo

    @DBInstanceNetInfo.setter
    def DBInstanceNetInfo(self, DBInstanceNetInfo):
        self._DBInstanceNetInfo = DBInstanceNetInfo

    @property
    def NetworkAccessList(self):
        r"""只读组网络信息列表（此字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of NetworkAccess
        """
        return self._NetworkAccessList

    @NetworkAccessList.setter
    def NetworkAccessList(self, NetworkAccessList):
        self._NetworkAccessList = NetworkAccessList


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._ProjectId = params.get("ProjectId")
        self._MasterDBInstanceId = params.get("MasterDBInstanceId")
        self._MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        self._MaxReplayLatency = params.get("MaxReplayLatency")
        self._ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self._MaxReplayLag = params.get("MaxReplayLag")
        self._ReplayLagEliminate = params.get("ReplayLagEliminate")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        if params.get("ReadOnlyDBInstanceList") is not None:
            self._ReadOnlyDBInstanceList = []
            for item in params.get("ReadOnlyDBInstanceList"):
                obj = DBInstance()
                obj._deserialize(item)
                self._ReadOnlyDBInstanceList.append(obj)
        self._Rebalance = params.get("Rebalance")
        if params.get("DBInstanceNetInfo") is not None:
            self._DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self._DBInstanceNetInfo.append(obj)
        if params.get("NetworkAccessList") is not None:
            self._NetworkAccessList = []
            for item in params.get("NetworkAccessList"):
                obj = NetworkAccess()
                obj._deserialize(item)
                self._NetworkAccessList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebalanceReadOnlyGroupRequest(AbstractModel):
    r"""RebalanceReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 只读组ID。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :type ReadOnlyGroupId: str
        """
        self._ReadOnlyGroupId = None

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebalanceReadOnlyGroupResponse(AbstractModel):
    r"""RebalanceReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RefreshAccountPasswordRequest(AbstractModel):
    r"""RefreshAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param _UserName: 账号名称
        :type UserName: str
        """
        self._DBInstanceId = None
        self._UserName = None

    @property
    def DBInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""账号名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshAccountPasswordResponse(AbstractModel):
    r"""RefreshAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    r"""描述地域的编码和状态等信息

    """

    def __init__(self):
        r"""
        :param _Region: 该地域对应的英文名称
        :type Region: str
        :param _RegionName: 该地域对应的中文名称
        :type RegionName: str
        :param _RegionId: 该地域对应的数字编号
        :type RegionId: int
        :param _RegionState: 可用状态，UNAVAILABLE表示不可用，AVAILABLE表示可用
        :type RegionState: str
        :param _SupportInternational: 该地域是否支持国际站售卖，0：不支持，1：支持
        :type SupportInternational: int
        """
        self._Region = None
        self._RegionName = None
        self._RegionId = None
        self._RegionState = None
        self._SupportInternational = None

    @property
    def Region(self):
        r"""该地域对应的英文名称
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        r"""该地域对应的中文名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        r"""该地域对应的数字编号
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionState(self):
        r"""可用状态，UNAVAILABLE表示不可用，AVAILABLE表示可用
        :rtype: str
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def SupportInternational(self):
        r"""该地域是否支持国际站售卖，0：不支持，1：支持
        :rtype: int
        """
        return self._SupportInternational

    @SupportInternational.setter
    def SupportInternational(self, SupportInternational):
        self._SupportInternational = SupportInternational


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._RegionState = params.get("RegionState")
        self._SupportInternational = params.get("SupportInternational")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDBInstanceFromReadOnlyGroupRequest(AbstractModel):
    r"""RemoveDBInstanceFromReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: 只读组ID。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :type ReadOnlyGroupId: str
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""只读组ID。可通过[DescribeReadOnlyGroups](https://cloud.tencent.com/document/api/409/52599)接口获取
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDBInstanceFromReadOnlyGroupResponse(AbstractModel):
    r"""RemoveDBInstanceFromReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RenewInstanceRequest(AbstractModel):
    r"""RenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。仅支持预付费（包年包月）实例。
        :type DBInstanceId: str
        :param _Period: 购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
        :type Period: int
        :param _AutoVoucher: 是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表，目前仅支持指定一张代金券
        :type VoucherIds: list of str
        """
        self._DBInstanceId = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-6fego161。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。仅支持预付费（包年包月）实例。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Period(self):
        r"""购买时长，单位：月。
<li>预付费：支持1,2,3,4,5,6,7,8,9,10,11,12,24,36</li>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券：
<li>0：否</li>
<li>1：是</li>
默认值：0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""代金券ID列表，目前仅支持指定一张代金券
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    r"""RenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""订单名
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    r"""ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-4wdeb0zv。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _UserName: 实例账户名。可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :type UserName: str
        :param _Password: UserName账户对应的新密码。
密码设置规则如下：
- 长度8~ 32位，推荐使用12位以上的密码
- 不能以" / "开头
- 必须包含以下四项:
  1.    小写字母a ~ z
  2.    大写字母 A ～ Z
  3.    数字 0 ～ 9
  4.    特殊字符 ()`~!@#$%^&*-+=_|{}[]:<>,.?/
        :type Password: str
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-4wdeb0zv。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""实例账户名。可通过[DescribeAccounts](https://cloud.tencent.com/document/api/409/18109)接口获取
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""UserName账户对应的新密码。
密码设置规则如下：
- 长度8~ 32位，推荐使用12位以上的密码
- 不能以" / "开头
- 必须包含以下四项:
  1.    小写字母a ~ z
  2.    大写字母 A ～ Z
  3.    数字 0 ～ 9
  4.    特殊字符 ()`~!@#$%^&*-+=_|{}[]:<>,.?/
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    r"""ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RestartDBInstanceRequest(AbstractModel):
    r"""RestartDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID，形如postgres-6r233v55。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""实例ID，形如postgres-6r233v55。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstanceResponse(AbstractModel):
    r"""RestartDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，FlowId等同于TaskId
        :type FlowId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID，FlowId等同于TaskId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RestoreDBInstanceObjectsRequest(AbstractModel):
    r"""RestoreDBInstanceObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _RestoreObjects: 需要恢复的对象列表。假设需要恢复的对象名为user，则恢复后的名称为user_bak_${LinuxTime}。${LinuxTime}无法指定，由系统根据任务发起的linux时间设定。
        :type RestoreObjects: list of str
        :param _BackupSetId: 恢复所用备份集。BackupSetId与RestoreTargetTime有且只能传一个。可通过[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)接口获取
        :type BackupSetId: str
        :param _RestoreTargetTime: 恢复目标时间，北京时间。BackupSetId与RestoreTargetTime有且只能传一个。
        :type RestoreTargetTime: str
        """
        self._DBInstanceId = None
        self._RestoreObjects = None
        self._BackupSetId = None
        self._RestoreTargetTime = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def RestoreObjects(self):
        r"""需要恢复的对象列表。假设需要恢复的对象名为user，则恢复后的名称为user_bak_${LinuxTime}。${LinuxTime}无法指定，由系统根据任务发起的linux时间设定。
        :rtype: list of str
        """
        return self._RestoreObjects

    @RestoreObjects.setter
    def RestoreObjects(self, RestoreObjects):
        self._RestoreObjects = RestoreObjects

    @property
    def BackupSetId(self):
        r"""恢复所用备份集。BackupSetId与RestoreTargetTime有且只能传一个。可通过[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)接口获取
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def RestoreTargetTime(self):
        r"""恢复目标时间，北京时间。BackupSetId与RestoreTargetTime有且只能传一个。
        :rtype: str
        """
        return self._RestoreTargetTime

    @RestoreTargetTime.setter
    def RestoreTargetTime(self, RestoreTargetTime):
        self._RestoreTargetTime = RestoreTargetTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._RestoreObjects = params.get("RestoreObjects")
        self._BackupSetId = params.get("BackupSetId")
        self._RestoreTargetTime = params.get("RestoreTargetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreDBInstanceObjectsResponse(AbstractModel):
    r"""RestoreDBInstanceObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    r"""安全组信息

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Inbound: 入站规则
        :type Inbound: list of PolicyRule
        :param _Outbound: 出站规则
        :type Outbound: list of PolicyRule
        :param _SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param _SecurityGroupDescription: 安全组备注
        :type SecurityGroupDescription: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._Inbound = None
        self._Outbound = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupDescription = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Inbound(self):
        r"""入站规则
        :rtype: list of PolicyRule
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        r"""出站规则
        :rtype: list of PolicyRule
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        r"""安全组ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        r"""安全组名称
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupDescription(self):
        r"""安全组备注
        :rtype: str
        """
        return self._SecurityGroupDescription

    @SecurityGroupDescription.setter
    def SecurityGroupDescription(self, SecurityGroupDescription):
        self._SecurityGroupDescription = SecurityGroupDescription


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self._Outbound.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupDescription = params.get("SecurityGroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewFlagRequest(AbstractModel):
    r"""SetAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: 实例ID集合。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。仅支持预付费（包年包月）的实例。支持同时操作多个实例。
        :type DBInstanceIdSet: list of str
        :param _AutoRenewFlag: 续费标记。0-正常续费；1-自动续费；2-到期不续费
        :type AutoRenewFlag: int
        """
        self._DBInstanceIdSet = None
        self._AutoRenewFlag = None

    @property
    def DBInstanceIdSet(self):
        r"""实例ID集合。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取。仅支持预付费（包年包月）的实例。支持同时操作多个实例。
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def AutoRenewFlag(self):
        r"""续费标记。0-正常续费；1-自动续费；2-到期不续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewFlagResponse(AbstractModel):
    r"""SetAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 设置成功的实例个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        r"""设置成功的实例个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class SpecInfo(AbstractModel):
    r"""描述某个地域下某个可用区的可售卖规格详细信息。

    """

    def __init__(self):
        r"""
        :param _Region: 地域英文编码，对应RegionSet的Region字段
        :type Region: str
        :param _Zone: 区域英文编码，对应ZoneSet的Zone字段
        :type Zone: str
        :param _SpecItemInfoList: 规格详细信息列表
        :type SpecItemInfoList: list of SpecItemInfo
        :param _SupportKMSRegions: 支持KMS的地域
        :type SupportKMSRegions: list of str
        """
        self._Region = None
        self._Zone = None
        self._SpecItemInfoList = None
        self._SupportKMSRegions = None

    @property
    def Region(self):
        r"""地域英文编码，对应RegionSet的Region字段
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""区域英文编码，对应ZoneSet的Zone字段
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecItemInfoList(self):
        r"""规格详细信息列表
        :rtype: list of SpecItemInfo
        """
        return self._SpecItemInfoList

    @SpecItemInfoList.setter
    def SpecItemInfoList(self, SpecItemInfoList):
        self._SpecItemInfoList = SpecItemInfoList

    @property
    def SupportKMSRegions(self):
        r"""支持KMS的地域
        :rtype: list of str
        """
        return self._SupportKMSRegions

    @SupportKMSRegions.setter
    def SupportKMSRegions(self, SupportKMSRegions):
        self._SupportKMSRegions = SupportKMSRegions


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        if params.get("SpecItemInfoList") is not None:
            self._SpecItemInfoList = []
            for item in params.get("SpecItemInfoList"):
                obj = SpecItemInfo()
                obj._deserialize(item)
                self._SpecItemInfoList.append(obj)
        self._SupportKMSRegions = params.get("SupportKMSRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecItemInfo(AbstractModel):
    r"""描述一种规格的信息

    """

    def __init__(self):
        r"""
        :param _SpecCode: 规格ID
        :type SpecCode: str
        :param _Version: PostgreSQL的版本编号
        :type Version: str
        :param _VersionName: 内核编号对应的完整版本名称
        :type VersionName: str
        :param _Cpu: CPU核数
        :type Cpu: int
        :param _Memory: 内存大小，单位：MB
        :type Memory: int
        :param _MaxStorage: 该规格所支持最大存储容量，单位：GB
        :type MaxStorage: int
        :param _MinStorage: 该规格所支持最小存储容量，单位：GB
        :type MinStorage: int
        :param _Qps: 该规格的预估QPS
        :type Qps: int
        :param _Pid: 【该字段废弃】
        :type Pid: int
        :param _Type: 机器类型
        :type Type: str
        :param _MajorVersion: PostgreSQL的主要版本编号
        :type MajorVersion: str
        :param _KernelVersion: PostgreSQL的内核版本编号
        :type KernelVersion: str
        :param _IsSupportTDE: 是否支持TDE数据加密功能，0-不支持，1-支持
        :type IsSupportTDE: int
        """
        self._SpecCode = None
        self._Version = None
        self._VersionName = None
        self._Cpu = None
        self._Memory = None
        self._MaxStorage = None
        self._MinStorage = None
        self._Qps = None
        self._Pid = None
        self._Type = None
        self._MajorVersion = None
        self._KernelVersion = None
        self._IsSupportTDE = None

    @property
    def SpecCode(self):
        r"""规格ID
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Version(self):
        r"""PostgreSQL的版本编号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionName(self):
        r"""内核编号对应的完整版本名称
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Cpu(self):
        r"""CPU核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""内存大小，单位：MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def MaxStorage(self):
        r"""该规格所支持最大存储容量，单位：GB
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def MinStorage(self):
        r"""该规格所支持最小存储容量，单位：GB
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def Qps(self):
        r"""该规格的预估QPS
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Pid(self):
        r"""【该字段废弃】
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Type(self):
        r"""机器类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MajorVersion(self):
        r"""PostgreSQL的主要版本编号
        :rtype: str
        """
        return self._MajorVersion

    @MajorVersion.setter
    def MajorVersion(self, MajorVersion):
        self._MajorVersion = MajorVersion

    @property
    def KernelVersion(self):
        r"""PostgreSQL的内核版本编号
        :rtype: str
        """
        return self._KernelVersion

    @KernelVersion.setter
    def KernelVersion(self, KernelVersion):
        self._KernelVersion = KernelVersion

    @property
    def IsSupportTDE(self):
        r"""是否支持TDE数据加密功能，0-不支持，1-支持
        :rtype: int
        """
        return self._IsSupportTDE

    @IsSupportTDE.setter
    def IsSupportTDE(self, IsSupportTDE):
        self._IsSupportTDE = IsSupportTDE


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._Version = params.get("Version")
        self._VersionName = params.get("VersionName")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._MaxStorage = params.get("MaxStorage")
        self._MinStorage = params.get("MinStorage")
        self._Qps = params.get("Qps")
        self._Pid = params.get("Pid")
        self._Type = params.get("Type")
        self._MajorVersion = params.get("MajorVersion")
        self._KernelVersion = params.get("KernelVersion")
        self._IsSupportTDE = params.get("IsSupportTDE")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstancePrimaryRequest(AbstractModel):
    r"""SwitchDBInstancePrimary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _Force: 是否强制切换。强制切换时只要备节点可访问，无论主备延迟多大都会发起切换。只有SwitchTag为0时，才可使用立即切换。
<li>默认：false</li>
        :type Force: bool
        :param _SwitchTag: 指定实例配置完成变更后的切换时间。
<li>0：立即切换 </li>
<li>1：指定时间切换</li>
<li>2：维护时间窗口内切换</li>
默认值：0 
        :type SwitchTag: int
        :param _SwitchStartTime: 切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchStartTime: str
        :param _SwitchEndTime: 切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。SwitchStartTime和SwitchEndTime时间窗口不能小于30分钟。
        :type SwitchEndTime: str
        """
        self._DBInstanceId = None
        self._Force = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Force(self):
        r"""是否强制切换。强制切换时只要备节点可访问，无论主备延迟多大都会发起切换。只有SwitchTag为0时，才可使用立即切换。
<li>默认：false</li>
        :rtype: bool
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def SwitchTag(self):
        r"""指定实例配置完成变更后的切换时间。
<li>0：立即切换 </li>
<li>1：指定时间切换</li>
<li>2：维护时间窗口内切换</li>
默认值：0 
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。SwitchStartTime和SwitchEndTime时间窗口不能小于30分钟。
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Force = params.get("Force")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstancePrimaryResponse(AbstractModel):
    r"""SwitchDBInstancePrimary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    r"""实例绑定的标签信息，包含标签键TagKey和标签值TagValue

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
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
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
        


class TaskDetail(AbstractModel):
    r"""任务的详情信息

    """

    def __init__(self):
        r"""
        :param _CurrentStep: 当前执行的子任务步骤名称。
        :type CurrentStep: str
        :param _AllSteps: 当前任务所拥有的子步骤描述。
        :type AllSteps: str
        :param _Input: 任务的输入参数。
        :type Input: str
        :param _Output: 任务的输出参数。
        :type Output: str
        :param _SwitchTag: 指定实例配置完成变更后的切换时间，默认值：0
0:   此任务不需要切换
1：立即切换
2：指定时间切换
3：维护时间窗口内切换。
        :type SwitchTag: int
        :param _SwitchTime: 指定的切换时间。
        :type SwitchTime: str
        :param _Message: 任务的提示信息。
        :type Message: str
        """
        self._CurrentStep = None
        self._AllSteps = None
        self._Input = None
        self._Output = None
        self._SwitchTag = None
        self._SwitchTime = None
        self._Message = None

    @property
    def CurrentStep(self):
        r"""当前执行的子任务步骤名称。
        :rtype: str
        """
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def AllSteps(self):
        r"""当前任务所拥有的子步骤描述。
        :rtype: str
        """
        return self._AllSteps

    @AllSteps.setter
    def AllSteps(self, AllSteps):
        self._AllSteps = AllSteps

    @property
    def Input(self):
        r"""任务的输入参数。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        r"""任务的输出参数。
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def SwitchTag(self):
        r"""指定实例配置完成变更后的切换时间，默认值：0
0:   此任务不需要切换
1：立即切换
2：指定时间切换
3：维护时间窗口内切换。
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchTime(self):
        r"""指定的切换时间。
        :rtype: str
        """
        return self._SwitchTime

    @SwitchTime.setter
    def SwitchTime(self, SwitchTime):
        self._SwitchTime = SwitchTime

    @property
    def Message(self):
        r"""任务的提示信息。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._CurrentStep = params.get("CurrentStep")
        self._AllSteps = params.get("AllSteps")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchTime = params.get("SwitchTime")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSet(AbstractModel):
    r"""任务列表信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _TaskType: 任务的类型。
        :type TaskType: str
        :param _DBInstanceId: 任务实例的实例ID。
        :type DBInstanceId: str
        :param _StartTime: 任务的开始时间。
        :type StartTime: str
        :param _EndTime: 任务的结束时间。
        :type EndTime: str
        :param _Status: 任务的运行状态，包括Running,Success,WaitSwitch,Fail,Pause。
        :type Status: str
        :param _Progress: 任务的执行进度，取值范围0-100。
        :type Progress: int
        :param _TaskDetail: 任务的详情信息
        :type TaskDetail: :class:`tencentcloud.postgres.v20170312.models.TaskDetail`
        """
        self._TaskId = None
        self._TaskType = None
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Progress = None
        self._TaskDetail = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        r"""任务的类型。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def DBInstanceId(self):
        r"""任务实例的实例ID。
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""任务的开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""任务的结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""任务的运行状态，包括Running,Success,WaitSwitch,Fail,Pause。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        r"""任务的执行进度，取值范围0-100。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskDetail(self):
        r"""任务的详情信息
        :rtype: :class:`tencentcloud.postgres.v20170312.models.TaskDetail`
        """
        return self._TaskDetail

    @TaskDetail.setter
    def TaskDetail(self, TaskDetail):
        self._TaskDetail = TaskDetail


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        if params.get("TaskDetail") is not None:
            self._TaskDetail = TaskDetail()
            self._TaskDetail._deserialize(params.get("TaskDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockAccountRequest(AbstractModel):
    r"""UnlockAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。	
        :type DBInstanceId: str
        :param _UserName: 账号名称。
        :type UserName: str
        """
        self._DBInstanceId = None
        self._UserName = None

    @property
    def DBInstanceId(self):
        r"""实例ID。	
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""账号名称。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockAccountResponse(AbstractModel):
    r"""UnlockAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceKernelVersionRequest(AbstractModel):
    r"""UpgradeDBInstanceKernelVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _TargetDBKernelVersion: 升级的目标内核版本号。可以通过接口[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)的返回字段AvailableUpgradeTarget获取。

        :type TargetDBKernelVersion: str
        :param _SwitchTag: 指定实例升级内核版本号完成后的切换时间。可选值:
<li>0：立即切换</li>
<li>1：指定时间切换</li>
<li>2：维护时间窗口内切换</li>
默认值：0 
        :type SwitchTag: int
        :param _SwitchStartTime: 切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchStartTime: str
        :param _SwitchEndTime: 切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。SwitchStartTime和SwitchEndTime时间窗口不能小于30分钟。
        :type SwitchEndTime: str
        :param _DryRun: 是否对本次升级实例内核版本号操作执行预检查。
<li>true：执行预检查操作，不升级内核版本号。检查项目包含请求参数、内核版本号兼容性、实例参数等。</li>
<li>false：发送正常请求（默认值），通过检查后直接升级内核版本号。</li>
默认值：false
        :type DryRun: bool
        """
        self._DBInstanceId = None
        self._TargetDBKernelVersion = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None
        self._DryRun = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def TargetDBKernelVersion(self):
        r"""升级的目标内核版本号。可以通过接口[DescribeDBVersions](https://cloud.tencent.com/document/api/409/89018)的返回字段AvailableUpgradeTarget获取。

        :rtype: str
        """
        return self._TargetDBKernelVersion

    @TargetDBKernelVersion.setter
    def TargetDBKernelVersion(self, TargetDBKernelVersion):
        self._TargetDBKernelVersion = TargetDBKernelVersion

    @property
    def SwitchTag(self):
        r"""指定实例升级内核版本号完成后的切换时间。可选值:
<li>0：立即切换</li>
<li>1：指定时间切换</li>
<li>2：维护时间窗口内切换</li>
默认值：0 
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。SwitchStartTime和SwitchEndTime时间窗口不能小于30分钟。
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime

    @property
    def DryRun(self):
        r"""是否对本次升级实例内核版本号操作执行预检查。
<li>true：执行预检查操作，不升级内核版本号。检查项目包含请求参数、内核版本号兼容性、实例参数等。</li>
<li>false：发送正常请求（默认值），通过检查后直接升级内核版本号。</li>
默认值：false
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._TargetDBKernelVersion = params.get("TargetDBKernelVersion")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceKernelVersionResponse(AbstractModel):
    r"""UpgradeDBInstanceKernelVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceMajorVersionRequest(AbstractModel):
    r"""UpgradeDBInstanceMajorVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: 实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :type DBInstanceId: str
        :param _TargetDBKernelVersion: 目标内核版本号，可以通过API [DescribeDBVersions](https://cloud.tencent.com/document/product/409/89018)获取可以升级的目标内核版本号。
        :type TargetDBKernelVersion: str
        :param _UpgradeCheck: 是否为校验模式，若UpgradeCheck为True，表示仅进行内核版本兼容性检查，不会进行实质性的升级操作，对原实例无影响。检查结果可以通过升级日志查看。
        :type UpgradeCheck: bool
        :param _BackupBeforeUpgrade: 升级前备份选项。True，表示升级前需要创建全量备份，False，表示升级前不需要创建全量备份。当实例已有备份集可以恢复到升级前的状态时，可选择False，否则需要指定为True。UpgradeCheck为True时，此参数无效。
        :type BackupBeforeUpgrade: bool
        :param _StatisticsRefreshOption: 统计信息收集选项，对主例运行 ANALYZE 以在升级后更新系统统计信息。可选值包括，
0：不需要收集统计信息；
1：实例恢复写之前收集统计信息；
3：实例恢复写之后收集统计信息。
UpgradeCheck为True时，此参数无效。
        :type StatisticsRefreshOption: int
        :param _ExtensionUpgradeOption: 插件升级选项，pg_upgrade不会升级任何插件，需要在升级完成后在创建过插件的库上执行"ALTER EXTENSION UPDATE"。发起升级实例大版本时可以指定在实例恢复写前/后是否需要升级任务自动升级插件版本。可选值包括：
0：不需要自动升级插件；
1：恢复写之前升级插件；
2：恢复写之后升级插件。
UpgradeCheck为True时，此参数无效。
        :type ExtensionUpgradeOption: int
        :param _UpgradeTimeOption: 升级时间选项，升级过程中会有一段时间实例只读，并会有一次秒级闪断，发起升级时需要选择这段影响的时间窗。可选值包括：
0：自动执行，不需要指定时间窗；
1：指定本次升级任务的时间窗，通过参数UpgradeTimeBegin和UpgradeTimeEnd设置；
2：在实例运维时间窗内执行。
UpgradeCheck为True时，此参数无效。
        :type UpgradeTimeOption: int
        :param _UpgradeTimeBegin: 升级时间窗开始时间，时间格式：HH:MM:SS，例如：01:00:00。当UpgradeTimeOption为1时，该参数有效。
UpgradeCheck为True时，此参数无效。
        :type UpgradeTimeBegin: str
        :param _UpgradeTimeEnd: 升级时间窗截止时间，时间格式：HH:MM:SS，例如：02:00:00。当UpgradeTimeOption为1时，该参数有效。
UpgradeCheck为True时，此参数无效。
        :type UpgradeTimeEnd: str
        """
        self._DBInstanceId = None
        self._TargetDBKernelVersion = None
        self._UpgradeCheck = None
        self._BackupBeforeUpgrade = None
        self._StatisticsRefreshOption = None
        self._ExtensionUpgradeOption = None
        self._UpgradeTimeOption = None
        self._UpgradeTimeBegin = None
        self._UpgradeTimeEnd = None

    @property
    def DBInstanceId(self):
        r"""实例ID。可通过[DescribeDBInstances](https://cloud.tencent.com/document/api/409/16773)接口获取
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def TargetDBKernelVersion(self):
        r"""目标内核版本号，可以通过API [DescribeDBVersions](https://cloud.tencent.com/document/product/409/89018)获取可以升级的目标内核版本号。
        :rtype: str
        """
        return self._TargetDBKernelVersion

    @TargetDBKernelVersion.setter
    def TargetDBKernelVersion(self, TargetDBKernelVersion):
        self._TargetDBKernelVersion = TargetDBKernelVersion

    @property
    def UpgradeCheck(self):
        r"""是否为校验模式，若UpgradeCheck为True，表示仅进行内核版本兼容性检查，不会进行实质性的升级操作，对原实例无影响。检查结果可以通过升级日志查看。
        :rtype: bool
        """
        return self._UpgradeCheck

    @UpgradeCheck.setter
    def UpgradeCheck(self, UpgradeCheck):
        self._UpgradeCheck = UpgradeCheck

    @property
    def BackupBeforeUpgrade(self):
        r"""升级前备份选项。True，表示升级前需要创建全量备份，False，表示升级前不需要创建全量备份。当实例已有备份集可以恢复到升级前的状态时，可选择False，否则需要指定为True。UpgradeCheck为True时，此参数无效。
        :rtype: bool
        """
        return self._BackupBeforeUpgrade

    @BackupBeforeUpgrade.setter
    def BackupBeforeUpgrade(self, BackupBeforeUpgrade):
        self._BackupBeforeUpgrade = BackupBeforeUpgrade

    @property
    def StatisticsRefreshOption(self):
        r"""统计信息收集选项，对主例运行 ANALYZE 以在升级后更新系统统计信息。可选值包括，
0：不需要收集统计信息；
1：实例恢复写之前收集统计信息；
3：实例恢复写之后收集统计信息。
UpgradeCheck为True时，此参数无效。
        :rtype: int
        """
        return self._StatisticsRefreshOption

    @StatisticsRefreshOption.setter
    def StatisticsRefreshOption(self, StatisticsRefreshOption):
        self._StatisticsRefreshOption = StatisticsRefreshOption

    @property
    def ExtensionUpgradeOption(self):
        r"""插件升级选项，pg_upgrade不会升级任何插件，需要在升级完成后在创建过插件的库上执行"ALTER EXTENSION UPDATE"。发起升级实例大版本时可以指定在实例恢复写前/后是否需要升级任务自动升级插件版本。可选值包括：
0：不需要自动升级插件；
1：恢复写之前升级插件；
2：恢复写之后升级插件。
UpgradeCheck为True时，此参数无效。
        :rtype: int
        """
        return self._ExtensionUpgradeOption

    @ExtensionUpgradeOption.setter
    def ExtensionUpgradeOption(self, ExtensionUpgradeOption):
        self._ExtensionUpgradeOption = ExtensionUpgradeOption

    @property
    def UpgradeTimeOption(self):
        r"""升级时间选项，升级过程中会有一段时间实例只读，并会有一次秒级闪断，发起升级时需要选择这段影响的时间窗。可选值包括：
0：自动执行，不需要指定时间窗；
1：指定本次升级任务的时间窗，通过参数UpgradeTimeBegin和UpgradeTimeEnd设置；
2：在实例运维时间窗内执行。
UpgradeCheck为True时，此参数无效。
        :rtype: int
        """
        return self._UpgradeTimeOption

    @UpgradeTimeOption.setter
    def UpgradeTimeOption(self, UpgradeTimeOption):
        self._UpgradeTimeOption = UpgradeTimeOption

    @property
    def UpgradeTimeBegin(self):
        r"""升级时间窗开始时间，时间格式：HH:MM:SS，例如：01:00:00。当UpgradeTimeOption为1时，该参数有效。
UpgradeCheck为True时，此参数无效。
        :rtype: str
        """
        return self._UpgradeTimeBegin

    @UpgradeTimeBegin.setter
    def UpgradeTimeBegin(self, UpgradeTimeBegin):
        self._UpgradeTimeBegin = UpgradeTimeBegin

    @property
    def UpgradeTimeEnd(self):
        r"""升级时间窗截止时间，时间格式：HH:MM:SS，例如：02:00:00。当UpgradeTimeOption为1时，该参数有效。
UpgradeCheck为True时，此参数无效。
        :rtype: str
        """
        return self._UpgradeTimeEnd

    @UpgradeTimeEnd.setter
    def UpgradeTimeEnd(self, UpgradeTimeEnd):
        self._UpgradeTimeEnd = UpgradeTimeEnd


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._TargetDBKernelVersion = params.get("TargetDBKernelVersion")
        self._UpgradeCheck = params.get("UpgradeCheck")
        self._BackupBeforeUpgrade = params.get("BackupBeforeUpgrade")
        self._StatisticsRefreshOption = params.get("StatisticsRefreshOption")
        self._ExtensionUpgradeOption = params.get("ExtensionUpgradeOption")
        self._UpgradeTimeOption = params.get("UpgradeTimeOption")
        self._UpgradeTimeBegin = params.get("UpgradeTimeBegin")
        self._UpgradeTimeEnd = params.get("UpgradeTimeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceMajorVersionResponse(AbstractModel):
    r"""UpgradeDBInstanceMajorVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Version(AbstractModel):
    r"""数据库版本号信息

    """

    def __init__(self):
        r"""
        :param _DBEngine: 数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
        :type DBEngine: str
        :param _DBVersion: 数据库版本，例如：12.4
        :type DBVersion: str
        :param _DBMajorVersion: 数据库主要版本，例如：12
        :type DBMajorVersion: str
        :param _DBKernelVersion: 数据库内核版本，例如：v12.4_r1.3
        :type DBKernelVersion: str
        :param _SupportedFeatureNames: 数据库内核支持的特性列表。例如，
TDE：支持数据加密。
        :type SupportedFeatureNames: list of str
        :param _Status: 数据库版本状态，包括：
AVAILABLE：可用；
UPGRADE_ONLY：不可创建，此版本仅可升级至高版本；
DEPRECATED：已弃用。
        :type Status: str
        :param _AvailableUpgradeTarget: 该数据库版本（DBKernelVersion）可以升级到的版本号列表。其中包含可升级的小版本号和可升级的大版本号（完整内核版本格式示例：v15.1_v1.6）。
        :type AvailableUpgradeTarget: list of str
        """
        self._DBEngine = None
        self._DBVersion = None
        self._DBMajorVersion = None
        self._DBKernelVersion = None
        self._SupportedFeatureNames = None
        self._Status = None
        self._AvailableUpgradeTarget = None

    @property
    def DBEngine(self):
        r"""数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def DBVersion(self):
        r"""数据库版本，例如：12.4
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def DBMajorVersion(self):
        r"""数据库主要版本，例如：12
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBKernelVersion(self):
        r"""数据库内核版本，例如：v12.4_r1.3
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def SupportedFeatureNames(self):
        r"""数据库内核支持的特性列表。例如，
TDE：支持数据加密。
        :rtype: list of str
        """
        return self._SupportedFeatureNames

    @SupportedFeatureNames.setter
    def SupportedFeatureNames(self, SupportedFeatureNames):
        self._SupportedFeatureNames = SupportedFeatureNames

    @property
    def Status(self):
        r"""数据库版本状态，包括：
AVAILABLE：可用；
UPGRADE_ONLY：不可创建，此版本仅可升级至高版本；
DEPRECATED：已弃用。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AvailableUpgradeTarget(self):
        r"""该数据库版本（DBKernelVersion）可以升级到的版本号列表。其中包含可升级的小版本号和可升级的大版本号（完整内核版本格式示例：v15.1_v1.6）。
        :rtype: list of str
        """
        return self._AvailableUpgradeTarget

    @AvailableUpgradeTarget.setter
    def AvailableUpgradeTarget(self, AvailableUpgradeTarget):
        self._AvailableUpgradeTarget = AvailableUpgradeTarget


    def _deserialize(self, params):
        self._DBEngine = params.get("DBEngine")
        self._DBVersion = params.get("DBVersion")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._SupportedFeatureNames = params.get("SupportedFeatureNames")
        self._Status = params.get("Status")
        self._AvailableUpgradeTarget = params.get("AvailableUpgradeTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Xlog(AbstractModel):
    r"""数据库Xlog信息

    """

    def __init__(self):
        r"""
        :param _Id: 备份文件唯一标识
        :type Id: int
        :param _StartTime: 文件生成的开始时间
        :type StartTime: str
        :param _EndTime: 文件生成的结束时间
        :type EndTime: str
        :param _InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param _ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param _Size: 备份文件大小
        :type Size: int
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._Size = None

    @property
    def Id(self):
        r"""备份文件唯一标识
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        r"""文件生成的开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""文件生成的结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternalAddr(self):
        r"""内网下载地址
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""外网下载地址
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Size(self):
        r"""备份文件大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    r"""描述可用区的编码和状态信息

    """

    def __init__(self):
        r"""
        :param _Zone: 该可用区的英文名称
        :type Zone: str
        :param _ZoneName: 该可用区的中文名称
        :type ZoneName: str
        :param _ZoneId: 该可用区对应的数字编号
        :type ZoneId: int
        :param _ZoneState: 可用状态包含，
UNAVAILABLE：不可用。
AVAILABLE：可用。
SELLOUT：售罄。
SUPPORTMODIFYONLY：支持变配。
        :type ZoneState: str
        :param _ZoneSupportIpv6: 该可用区是否支持Ipv6
        :type ZoneSupportIpv6: int
        :param _StandbyZoneSet: 该可用区对应的备可用区集合
注意：此字段可能返回 null，表示取不到有效值。
        :type StandbyZoneSet: list of str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._ZoneState = None
        self._ZoneSupportIpv6 = None
        self._StandbyZoneSet = None

    @property
    def Zone(self):
        r"""该可用区的英文名称
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""该可用区的中文名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        r"""该可用区对应的数字编号
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        r"""可用状态包含，
UNAVAILABLE：不可用。
AVAILABLE：可用。
SELLOUT：售罄。
SUPPORTMODIFYONLY：支持变配。
        :rtype: str
        """
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState

    @property
    def ZoneSupportIpv6(self):
        r"""该可用区是否支持Ipv6
        :rtype: int
        """
        return self._ZoneSupportIpv6

    @ZoneSupportIpv6.setter
    def ZoneSupportIpv6(self, ZoneSupportIpv6):
        self._ZoneSupportIpv6 = ZoneSupportIpv6

    @property
    def StandbyZoneSet(self):
        r"""该可用区对应的备可用区集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._StandbyZoneSet

    @StandbyZoneSet.setter
    def StandbyZoneSet(self, StandbyZoneSet):
        self._StandbyZoneSet = StandbyZoneSet


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        self._ZoneSupportIpv6 = params.get("ZoneSupportIpv6")
        self._StandbyZoneSet = params.get("StandbyZoneSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        