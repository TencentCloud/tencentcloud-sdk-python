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


class Application(AbstractModel):
    r"""审批申请单

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 审批单号
        :type ApplicationId: str
        :param _ApplicationType: 申请类型
        :type ApplicationType: int
        :param _ClusterId: 集群Id
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _TableGroupName: 表格组名称
        :type TableGroupName: str
        :param _TableName: 表格名称
        :type TableName: str
        :param _Applicant: 申请人
        :type Applicant: str
        :param _CreatedTime: 建单时间
        :type CreatedTime: str
        :param _ApplicationStatus: 处理状态 -1 撤回 0-待审核 1-已经审核并提交任务 2-已驳回
        :type ApplicationStatus: int
        :param _TableGroupId: 表格组Id
        :type TableGroupId: str
        :param _TaskId: 已提交的任务Id，未提交申请为0
        :type TaskId: str
        :param _TableInstanceId: 腾讯云上table的唯一键
        :type TableInstanceId: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _ExecuteUser: 审批人
        :type ExecuteUser: str
        :param _ExecuteStatus: 执行状态
        :type ExecuteStatus: str
        :param _CanCensor: 该申请单是否可以被当前用户审批
        :type CanCensor: bool
        :param _CanWithdrawal: 该申请单是否可以被当前用户撤回
        :type CanWithdrawal: bool
        """
        self._ApplicationId = None
        self._ApplicationType = None
        self._ClusterId = None
        self._ClusterName = None
        self._TableGroupName = None
        self._TableName = None
        self._Applicant = None
        self._CreatedTime = None
        self._ApplicationStatus = None
        self._TableGroupId = None
        self._TaskId = None
        self._TableInstanceId = None
        self._UpdateTime = None
        self._ExecuteUser = None
        self._ExecuteStatus = None
        self._CanCensor = None
        self._CanWithdrawal = None

    @property
    def ApplicationId(self):
        r"""审批单号
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationType(self):
        r"""申请类型
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ClusterId(self):
        r"""集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TableGroupName(self):
        r"""表格组名称
        :rtype: str
        """
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Applicant(self):
        r"""申请人
        :rtype: str
        """
        return self._Applicant

    @Applicant.setter
    def Applicant(self, Applicant):
        self._Applicant = Applicant

    @property
    def CreatedTime(self):
        r"""建单时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ApplicationStatus(self):
        r"""处理状态 -1 撤回 0-待审核 1-已经审核并提交任务 2-已驳回
        :rtype: int
        """
        return self._ApplicationStatus

    @ApplicationStatus.setter
    def ApplicationStatus(self, ApplicationStatus):
        self._ApplicationStatus = ApplicationStatus

    @property
    def TableGroupId(self):
        r"""表格组Id
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TaskId(self):
        r"""已提交的任务Id，未提交申请为0
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TableInstanceId(self):
        r"""腾讯云上table的唯一键
        :rtype: str
        """
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ExecuteUser(self):
        r"""审批人
        :rtype: str
        """
        return self._ExecuteUser

    @ExecuteUser.setter
    def ExecuteUser(self, ExecuteUser):
        self._ExecuteUser = ExecuteUser

    @property
    def ExecuteStatus(self):
        r"""执行状态
        :rtype: str
        """
        return self._ExecuteStatus

    @ExecuteStatus.setter
    def ExecuteStatus(self, ExecuteStatus):
        self._ExecuteStatus = ExecuteStatus

    @property
    def CanCensor(self):
        r"""该申请单是否可以被当前用户审批
        :rtype: bool
        """
        return self._CanCensor

    @CanCensor.setter
    def CanCensor(self, CanCensor):
        self._CanCensor = CanCensor

    @property
    def CanWithdrawal(self):
        r"""该申请单是否可以被当前用户撤回
        :rtype: bool
        """
        return self._CanWithdrawal

    @CanWithdrawal.setter
    def CanWithdrawal(self, CanWithdrawal):
        self._CanWithdrawal = CanWithdrawal


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationType = params.get("ApplicationType")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TableGroupName = params.get("TableGroupName")
        self._TableName = params.get("TableName")
        self._Applicant = params.get("Applicant")
        self._CreatedTime = params.get("CreatedTime")
        self._ApplicationStatus = params.get("ApplicationStatus")
        self._TableGroupId = params.get("TableGroupId")
        self._TaskId = params.get("TaskId")
        self._TableInstanceId = params.get("TableInstanceId")
        self._UpdateTime = params.get("UpdateTime")
        self._ExecuteUser = params.get("ExecuteUser")
        self._ExecuteStatus = params.get("ExecuteStatus")
        self._CanCensor = params.get("CanCensor")
        self._CanWithdrawal = params.get("CanWithdrawal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyResult(AbstractModel):
    r"""更新申请单结果

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 申请单id
        :type ApplicationId: str
        :param _ApplicationType: 申请类型
        :type ApplicationType: int
        :param _ApplicationStatus: 处理状态 0-待审核 1-已经审核并提交任务 2-已驳回
        :type ApplicationStatus: int
        :param _TaskId: 已提交的任务Id
        :type TaskId: str
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._ApplicationId = None
        self._ApplicationType = None
        self._ApplicationStatus = None
        self._TaskId = None
        self._Error = None

    @property
    def ApplicationId(self):
        r"""申请单id
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationType(self):
        r"""申请类型
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ApplicationStatus(self):
        r"""处理状态 0-待审核 1-已经审核并提交任务 2-已驳回
        :rtype: int
        """
        return self._ApplicationStatus

    @ApplicationStatus.setter
    def ApplicationStatus(self, ApplicationStatus):
        self._ApplicationStatus = ApplicationStatus

    @property
    def TaskId(self):
        r"""已提交的任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationType = params.get("ApplicationType")
        self._ApplicationStatus = params.get("ApplicationStatus")
        self._TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyStatus(AbstractModel):
    r"""申请单id及其状态

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 集群id-申请单id
        :type ApplicationId: str
        :param _ApplicationStatus: 处理状态-1-撤回 1-通过 2-驳回，非0状态的申请单不可改变状态。
        :type ApplicationStatus: int
        :param _ApplicationType: 申请单类型
        :type ApplicationType: int
        :param _ClusterId: 集群Id
        :type ClusterId: str
        """
        self._ApplicationId = None
        self._ApplicationStatus = None
        self._ApplicationType = None
        self._ClusterId = None

    @property
    def ApplicationId(self):
        r"""集群id-申请单id
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationStatus(self):
        r"""处理状态-1-撤回 1-通过 2-驳回，非0状态的申请单不可改变状态。
        :rtype: int
        """
        return self._ApplicationStatus

    @ApplicationStatus.setter
    def ApplicationStatus(self, ApplicationStatus):
        self._ApplicationStatus = ApplicationStatus

    @property
    def ApplicationType(self):
        r"""申请单类型
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ClusterId(self):
        r"""集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationStatus = params.get("ApplicationStatus")
        self._ApplicationType = params.get("ApplicationType")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupExpireRuleInfo(AbstractModel):
    r"""备份保留策略详情
    集群策略： ClueterId=集群Id， TableGroupId=-1,  TableName="-1"
    集群+表格组策略： ClueterId=集群Id， TableGroupId=表格组Id,  TableName="-1"
    集群+表格组+表格策略： ClueterId=集群Id， TableGroupId=表格组Id,  TableName="表格名"

    FileTag=0 txh引擎文件， =1 ulog流水文件， 当要设置为=1时， 这两项不可变 TableGroupId=-1和TableName="-1"
    ExpireDay为大于等于1，小于999的整形数字
    OperType=0 代表动作为新增， =1 代表动作为删除， =2 代表动作为修改， 其中0和2可以混用，后端实现兼容

    """

    def __init__(self):
        r"""
        :param _TableGroupId: 所属表格组ID
        :type TableGroupId: str
        :param _TableName: 表名称
        :type TableName: str
        :param _FileTag: 文件标签，见上面描述
        :type FileTag: int
        :param _ExpireDay: 淘汰天数，见上面描述
        :type ExpireDay: int
        :param _OperType: 操作类型，见上面描述
        :type OperType: int
        """
        self._TableGroupId = None
        self._TableName = None
        self._FileTag = None
        self._ExpireDay = None
        self._OperType = None

    @property
    def TableGroupId(self):
        r"""所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def FileTag(self):
        r"""文件标签，见上面描述
        :rtype: int
        """
        return self._FileTag

    @FileTag.setter
    def FileTag(self, FileTag):
        self._FileTag = FileTag

    @property
    def ExpireDay(self):
        r"""淘汰天数，见上面描述
        :rtype: int
        """
        return self._ExpireDay

    @ExpireDay.setter
    def ExpireDay(self, ExpireDay):
        self._ExpireDay = ExpireDay

    @property
    def OperType(self):
        r"""操作类型，见上面描述
        :rtype: int
        """
        return self._OperType

    @OperType.setter
    def OperType(self, OperType):
        self._OperType = OperType


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._FileTag = params.get("FileTag")
        self._ExpireDay = params.get("ExpireDay")
        self._OperType = params.get("OperType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupRecords(AbstractModel):
    r"""备份记录
    作为出参时，每个字段都会填充
    作为入参时， 原封不动将每个字段填回结构体， 注意只有FIleTag=OSDATA才可以调用此接口

    """

    def __init__(self):
        r"""
        :param _ZoneId: 表格组ID
        :type ZoneId: int
        :param _TableName: 表名称
        :type TableName: str
        :param _BackupType: 备份源
        :type BackupType: str
        :param _FileTag: 文件标签：TCAPLUS_FULL或OSDATA
        :type FileTag: str
        :param _ShardCount: 分片数量
        :type ShardCount: int
        :param _BackupBatchTime: 备份批次日期
        :type BackupBatchTime: str
        :param _BackupFileSize: 备份文件汇总大小
        :type BackupFileSize: int
        :param _BackupSuccRate: 备份成功率
        :type BackupSuccRate: str
        :param _BackupExpireTime: 备份文件过期时间
        :type BackupExpireTime: str
        :param _AppId: 业务ID
        :type AppId: int
        """
        self._ZoneId = None
        self._TableName = None
        self._BackupType = None
        self._FileTag = None
        self._ShardCount = None
        self._BackupBatchTime = None
        self._BackupFileSize = None
        self._BackupSuccRate = None
        self._BackupExpireTime = None
        self._AppId = None

    @property
    def ZoneId(self):
        r"""表格组ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TableName(self):
        r"""表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def BackupType(self):
        r"""备份源
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def FileTag(self):
        r"""文件标签：TCAPLUS_FULL或OSDATA
        :rtype: str
        """
        return self._FileTag

    @FileTag.setter
    def FileTag(self, FileTag):
        self._FileTag = FileTag

    @property
    def ShardCount(self):
        r"""分片数量
        :rtype: int
        """
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def BackupBatchTime(self):
        r"""备份批次日期
        :rtype: str
        """
        return self._BackupBatchTime

    @BackupBatchTime.setter
    def BackupBatchTime(self, BackupBatchTime):
        self._BackupBatchTime = BackupBatchTime

    @property
    def BackupFileSize(self):
        r"""备份文件汇总大小
        :rtype: int
        """
        return self._BackupFileSize

    @BackupFileSize.setter
    def BackupFileSize(self, BackupFileSize):
        self._BackupFileSize = BackupFileSize

    @property
    def BackupSuccRate(self):
        r"""备份成功率
        :rtype: str
        """
        return self._BackupSuccRate

    @BackupSuccRate.setter
    def BackupSuccRate(self, BackupSuccRate):
        self._BackupSuccRate = BackupSuccRate

    @property
    def BackupExpireTime(self):
        r"""备份文件过期时间
        :rtype: str
        """
        return self._BackupExpireTime

    @BackupExpireTime.setter
    def BackupExpireTime(self, BackupExpireTime):
        self._BackupExpireTime = BackupExpireTime

    @property
    def AppId(self):
        r"""业务ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TableName = params.get("TableName")
        self._BackupType = params.get("BackupType")
        self._FileTag = params.get("FileTag")
        self._ShardCount = params.get("ShardCount")
        self._BackupBatchTime = params.get("BackupBatchTime")
        self._BackupFileSize = params.get("BackupFileSize")
        self._BackupSuccRate = params.get("BackupSuccRate")
        self._BackupExpireTime = params.get("BackupExpireTime")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearTablesRequest(AbstractModel):
    r"""ClearTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表所属集群实例ID
        :type ClusterId: str
        :param _SelectedTables: 待清理表信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表所属集群实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待清理表信息列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearTablesResponse(AbstractModel):
    r"""ClearTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 清除表结果数量
        :type TotalCount: int
        :param _TableResults: 清除表结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""清除表结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""清除表结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ClusterInfo(AbstractModel):
    r"""集群详细信息

    """

    def __init__(self):
        r"""
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Region: 集群所在地域
        :type Region: str
        :param _IdlType: 集群数据描述语言类型，如：`PROTO`,`TDR`
        :type IdlType: str
        :param _NetworkType: 网络类型
        :type NetworkType: str
        :param _VpcId: 集群关联的用户私有网络实例ID
        :type VpcId: str
        :param _SubnetId: 集群关联的用户子网实例ID
        :type SubnetId: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _Password: 集群密码
        :type Password: str
        :param _PasswordStatus: 密码状态
        :type PasswordStatus: str
        :param _ApiAccessId: TcaplusDB SDK连接参数，接入ID
        :type ApiAccessId: str
        :param _ApiAccessIp: TcaplusDB SDK连接参数，接入地址
        :type ApiAccessIp: str
        :param _ApiAccessPort: TcaplusDB SDK连接参数，接入端口
        :type ApiAccessPort: int
        :param _OldPasswordExpireTime: 如果PasswordStatus是unmodifiable说明有旧密码还未过期，此字段将显示旧密码过期的时间，否则为空
        :type OldPasswordExpireTime: str
        :param _ApiAccessIpv6: TcaplusDB SDK连接参数，接入ipv6地址
        :type ApiAccessIpv6: str
        :param _ClusterType: 集群类型，0,1:共享集群; 2:独立集群
        :type ClusterType: int
        :param _ClusterStatus: 集群状态, 0：表示正常运行中，1：表示冻结隔离一般欠费进入此状态，2：表示待回收，一般用户主动触发删除进入这个状态，3：待释放，进入这个状态，表示可以释放此表占用的资源了，4：变更中
        :type ClusterStatus: int
        :param _ReadCapacityUnit: 读CU
        :type ReadCapacityUnit: int
        :param _WriteCapacityUnit: 写CU
        :type WriteCapacityUnit: int
        :param _DiskVolume: 磁盘容量
        :type DiskVolume: int
        :param _ServerList: 独占server机器信息
        :type ServerList: list of ServerDetailInfo
        :param _ProxyList: 独占proxy机器信息
        :type ProxyList: list of ProxyDetailInfo
        :param _Censorship: 是否开启审核 0-不开启 1-开启
        :type Censorship: int
        :param _DbaUins: 审批人uin列表
        :type DbaUins: list of str
        :param _DataFlowStatus: 是否开启了数据订阅
        :type DataFlowStatus: int
        :param _KafkaInfo: 数据订阅的kafka信息
        :type KafkaInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.KafkaInfo`
        :param _TxhBackupExpireDay: 集群Txh备份文件多少天后过期删除
        :type TxhBackupExpireDay: int
        :param _UlogBackupExpireDay: 集群Ulog备份文件多少天后过期删除
        :type UlogBackupExpireDay: int
        :param _IsReadOnlyUlogBackupExpireDay: 集群Ulog备份文件过期策略是否为只读， 0： UlogBackupExpire是只读，不可修改， 1： UlogBackupExpire可以修改（当前业务存在Svrid第二段等于clusterid的机器）
        :type IsReadOnlyUlogBackupExpireDay: int
        :param _RestProxyStatus: restproxy状态
        :type RestProxyStatus: int
        :param _ShardTotalNum: 该集群shard总数
        :type ShardTotalNum: int
        :param _ShardUsedNum: 已使用的shard总数
        :type ShardUsedNum: int
        """
        self._ClusterName = None
        self._ClusterId = None
        self._Region = None
        self._IdlType = None
        self._NetworkType = None
        self._VpcId = None
        self._SubnetId = None
        self._CreatedTime = None
        self._Password = None
        self._PasswordStatus = None
        self._ApiAccessId = None
        self._ApiAccessIp = None
        self._ApiAccessPort = None
        self._OldPasswordExpireTime = None
        self._ApiAccessIpv6 = None
        self._ClusterType = None
        self._ClusterStatus = None
        self._ReadCapacityUnit = None
        self._WriteCapacityUnit = None
        self._DiskVolume = None
        self._ServerList = None
        self._ProxyList = None
        self._Censorship = None
        self._DbaUins = None
        self._DataFlowStatus = None
        self._KafkaInfo = None
        self._TxhBackupExpireDay = None
        self._UlogBackupExpireDay = None
        self._IsReadOnlyUlogBackupExpireDay = None
        self._RestProxyStatus = None
        self._ShardTotalNum = None
        self._ShardUsedNum = None

    @property
    def ClusterName(self):
        r"""集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterId(self):
        r"""集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Region(self):
        r"""集群所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IdlType(self):
        r"""集群数据描述语言类型，如：`PROTO`,`TDR`
        :rtype: str
        """
        return self._IdlType

    @IdlType.setter
    def IdlType(self, IdlType):
        self._IdlType = IdlType

    @property
    def NetworkType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def VpcId(self):
        r"""集群关联的用户私有网络实例ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""集群关联的用户子网实例ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Password(self):
        r"""集群密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordStatus(self):
        r"""密码状态
        :rtype: str
        """
        return self._PasswordStatus

    @PasswordStatus.setter
    def PasswordStatus(self, PasswordStatus):
        self._PasswordStatus = PasswordStatus

    @property
    def ApiAccessId(self):
        r"""TcaplusDB SDK连接参数，接入ID
        :rtype: str
        """
        return self._ApiAccessId

    @ApiAccessId.setter
    def ApiAccessId(self, ApiAccessId):
        self._ApiAccessId = ApiAccessId

    @property
    def ApiAccessIp(self):
        r"""TcaplusDB SDK连接参数，接入地址
        :rtype: str
        """
        return self._ApiAccessIp

    @ApiAccessIp.setter
    def ApiAccessIp(self, ApiAccessIp):
        self._ApiAccessIp = ApiAccessIp

    @property
    def ApiAccessPort(self):
        r"""TcaplusDB SDK连接参数，接入端口
        :rtype: int
        """
        return self._ApiAccessPort

    @ApiAccessPort.setter
    def ApiAccessPort(self, ApiAccessPort):
        self._ApiAccessPort = ApiAccessPort

    @property
    def OldPasswordExpireTime(self):
        r"""如果PasswordStatus是unmodifiable说明有旧密码还未过期，此字段将显示旧密码过期的时间，否则为空
        :rtype: str
        """
        return self._OldPasswordExpireTime

    @OldPasswordExpireTime.setter
    def OldPasswordExpireTime(self, OldPasswordExpireTime):
        self._OldPasswordExpireTime = OldPasswordExpireTime

    @property
    def ApiAccessIpv6(self):
        r"""TcaplusDB SDK连接参数，接入ipv6地址
        :rtype: str
        """
        return self._ApiAccessIpv6

    @ApiAccessIpv6.setter
    def ApiAccessIpv6(self, ApiAccessIpv6):
        self._ApiAccessIpv6 = ApiAccessIpv6

    @property
    def ClusterType(self):
        r"""集群类型，0,1:共享集群; 2:独立集群
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterStatus(self):
        r"""集群状态, 0：表示正常运行中，1：表示冻结隔离一般欠费进入此状态，2：表示待回收，一般用户主动触发删除进入这个状态，3：待释放，进入这个状态，表示可以释放此表占用的资源了，4：变更中
        :rtype: int
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def ReadCapacityUnit(self):
        r"""读CU
        :rtype: int
        """
        return self._ReadCapacityUnit

    @ReadCapacityUnit.setter
    def ReadCapacityUnit(self, ReadCapacityUnit):
        self._ReadCapacityUnit = ReadCapacityUnit

    @property
    def WriteCapacityUnit(self):
        r"""写CU
        :rtype: int
        """
        return self._WriteCapacityUnit

    @WriteCapacityUnit.setter
    def WriteCapacityUnit(self, WriteCapacityUnit):
        self._WriteCapacityUnit = WriteCapacityUnit

    @property
    def DiskVolume(self):
        r"""磁盘容量
        :rtype: int
        """
        return self._DiskVolume

    @DiskVolume.setter
    def DiskVolume(self, DiskVolume):
        self._DiskVolume = DiskVolume

    @property
    def ServerList(self):
        r"""独占server机器信息
        :rtype: list of ServerDetailInfo
        """
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def ProxyList(self):
        r"""独占proxy机器信息
        :rtype: list of ProxyDetailInfo
        """
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList

    @property
    def Censorship(self):
        r"""是否开启审核 0-不开启 1-开启
        :rtype: int
        """
        return self._Censorship

    @Censorship.setter
    def Censorship(self, Censorship):
        self._Censorship = Censorship

    @property
    def DbaUins(self):
        r"""审批人uin列表
        :rtype: list of str
        """
        return self._DbaUins

    @DbaUins.setter
    def DbaUins(self, DbaUins):
        self._DbaUins = DbaUins

    @property
    def DataFlowStatus(self):
        r"""是否开启了数据订阅
        :rtype: int
        """
        return self._DataFlowStatus

    @DataFlowStatus.setter
    def DataFlowStatus(self, DataFlowStatus):
        self._DataFlowStatus = DataFlowStatus

    @property
    def KafkaInfo(self):
        r"""数据订阅的kafka信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.KafkaInfo`
        """
        return self._KafkaInfo

    @KafkaInfo.setter
    def KafkaInfo(self, KafkaInfo):
        self._KafkaInfo = KafkaInfo

    @property
    def TxhBackupExpireDay(self):
        r"""集群Txh备份文件多少天后过期删除
        :rtype: int
        """
        return self._TxhBackupExpireDay

    @TxhBackupExpireDay.setter
    def TxhBackupExpireDay(self, TxhBackupExpireDay):
        self._TxhBackupExpireDay = TxhBackupExpireDay

    @property
    def UlogBackupExpireDay(self):
        r"""集群Ulog备份文件多少天后过期删除
        :rtype: int
        """
        return self._UlogBackupExpireDay

    @UlogBackupExpireDay.setter
    def UlogBackupExpireDay(self, UlogBackupExpireDay):
        self._UlogBackupExpireDay = UlogBackupExpireDay

    @property
    def IsReadOnlyUlogBackupExpireDay(self):
        r"""集群Ulog备份文件过期策略是否为只读， 0： UlogBackupExpire是只读，不可修改， 1： UlogBackupExpire可以修改（当前业务存在Svrid第二段等于clusterid的机器）
        :rtype: int
        """
        return self._IsReadOnlyUlogBackupExpireDay

    @IsReadOnlyUlogBackupExpireDay.setter
    def IsReadOnlyUlogBackupExpireDay(self, IsReadOnlyUlogBackupExpireDay):
        self._IsReadOnlyUlogBackupExpireDay = IsReadOnlyUlogBackupExpireDay

    @property
    def RestProxyStatus(self):
        r"""restproxy状态
        :rtype: int
        """
        return self._RestProxyStatus

    @RestProxyStatus.setter
    def RestProxyStatus(self, RestProxyStatus):
        self._RestProxyStatus = RestProxyStatus

    @property
    def ShardTotalNum(self):
        r"""该集群shard总数
        :rtype: int
        """
        return self._ShardTotalNum

    @ShardTotalNum.setter
    def ShardTotalNum(self, ShardTotalNum):
        self._ShardTotalNum = ShardTotalNum

    @property
    def ShardUsedNum(self):
        r"""已使用的shard总数
        :rtype: int
        """
        return self._ShardUsedNum

    @ShardUsedNum.setter
    def ShardUsedNum(self, ShardUsedNum):
        self._ShardUsedNum = ShardUsedNum


    def _deserialize(self, params):
        self._ClusterName = params.get("ClusterName")
        self._ClusterId = params.get("ClusterId")
        self._Region = params.get("Region")
        self._IdlType = params.get("IdlType")
        self._NetworkType = params.get("NetworkType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CreatedTime = params.get("CreatedTime")
        self._Password = params.get("Password")
        self._PasswordStatus = params.get("PasswordStatus")
        self._ApiAccessId = params.get("ApiAccessId")
        self._ApiAccessIp = params.get("ApiAccessIp")
        self._ApiAccessPort = params.get("ApiAccessPort")
        self._OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self._ApiAccessIpv6 = params.get("ApiAccessIpv6")
        self._ClusterType = params.get("ClusterType")
        self._ClusterStatus = params.get("ClusterStatus")
        self._ReadCapacityUnit = params.get("ReadCapacityUnit")
        self._WriteCapacityUnit = params.get("WriteCapacityUnit")
        self._DiskVolume = params.get("DiskVolume")
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = ServerDetailInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyDetailInfo()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        self._Censorship = params.get("Censorship")
        self._DbaUins = params.get("DbaUins")
        self._DataFlowStatus = params.get("DataFlowStatus")
        if params.get("KafkaInfo") is not None:
            self._KafkaInfo = KafkaInfo()
            self._KafkaInfo._deserialize(params.get("KafkaInfo"))
        self._TxhBackupExpireDay = params.get("TxhBackupExpireDay")
        self._UlogBackupExpireDay = params.get("UlogBackupExpireDay")
        self._IsReadOnlyUlogBackupExpireDay = params.get("IsReadOnlyUlogBackupExpireDay")
        self._RestProxyStatus = params.get("RestProxyStatus")
        self._ShardTotalNum = params.get("ShardTotalNum")
        self._ShardUsedNum = params.get("ShardUsedNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareIdlFilesRequest(AbstractModel):
    r"""CompareIdlFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待修改表格所在集群ID
        :type ClusterId: str
        :param _SelectedTables: 待修改表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param _ExistingIdlFiles: 选中的已上传IDL文件列表，与NewIdlFiles必选其一
        :type ExistingIdlFiles: list of IdlFileInfo
        :param _NewIdlFiles: 本次上传IDL文件列表，与ExistingIdlFiles必选其一
        :type NewIdlFiles: list of IdlFileInfo
        """
        self._ClusterId = None
        self._SelectedTables = None
        self._ExistingIdlFiles = None
        self._NewIdlFiles = None

    @property
    def ClusterId(self):
        r"""待修改表格所在集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待修改表格列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def ExistingIdlFiles(self):
        r"""选中的已上传IDL文件列表，与NewIdlFiles必选其一
        :rtype: list of IdlFileInfo
        """
        return self._ExistingIdlFiles

    @ExistingIdlFiles.setter
    def ExistingIdlFiles(self, ExistingIdlFiles):
        self._ExistingIdlFiles = ExistingIdlFiles

    @property
    def NewIdlFiles(self):
        r"""本次上传IDL文件列表，与ExistingIdlFiles必选其一
        :rtype: list of IdlFileInfo
        """
        return self._NewIdlFiles

    @NewIdlFiles.setter
    def NewIdlFiles(self, NewIdlFiles):
        self._NewIdlFiles = NewIdlFiles


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        if params.get("ExistingIdlFiles") is not None:
            self._ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self._NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._NewIdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareIdlFilesResponse(AbstractModel):
    r"""CompareIdlFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdlFiles: 本次上传校验所有的IDL文件信息列表
        :type IdlFiles: list of IdlFileInfo
        :param _TotalCount: 本次校验合法的表格数量
        :type TotalCount: int
        :param _TableInfos: 读取IDL描述文件后,根据用户指示的所选中表格解析校验结果
        :type TableInfos: list of ParsedTableInfoNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdlFiles = None
        self._TotalCount = None
        self._TableInfos = None
        self._RequestId = None

    @property
    def IdlFiles(self):
        r"""本次上传校验所有的IDL文件信息列表
        :rtype: list of IdlFileInfo
        """
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def TotalCount(self):
        r"""本次校验合法的表格数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableInfos(self):
        r"""读取IDL描述文件后,根据用户指示的所选中表格解析校验结果
        :rtype: list of ParsedTableInfoNew
        """
        return self._TableInfos

    @TableInfos.setter
    def TableInfos(self, TableInfos):
        self._TableInfos = TableInfos

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
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self._TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self._TableInfos.append(obj)
        self._RequestId = params.get("RequestId")


class CompareTablesInfo(AbstractModel):
    r"""比较表格的Meta信息

    """

    def __init__(self):
        r"""
        :param _SrcTableClusterId: 源表格的集群id
        :type SrcTableClusterId: str
        :param _SrcTableGroupId: 源表格的表格组id
        :type SrcTableGroupId: str
        :param _SrcTableName: 源表格的表名
        :type SrcTableName: str
        :param _DstTableClusterId: 目标表格的集群id
        :type DstTableClusterId: str
        :param _DstTableGroupId: 目标表格的表格组id
        :type DstTableGroupId: str
        :param _DstTableName: 目标表格的表名
        :type DstTableName: str
        :param _SrcTableInstanceId: 源表格的实例id
        :type SrcTableInstanceId: str
        :param _DstTableInstanceId: 目标表格的实例id
        :type DstTableInstanceId: str
        """
        self._SrcTableClusterId = None
        self._SrcTableGroupId = None
        self._SrcTableName = None
        self._DstTableClusterId = None
        self._DstTableGroupId = None
        self._DstTableName = None
        self._SrcTableInstanceId = None
        self._DstTableInstanceId = None

    @property
    def SrcTableClusterId(self):
        r"""源表格的集群id
        :rtype: str
        """
        return self._SrcTableClusterId

    @SrcTableClusterId.setter
    def SrcTableClusterId(self, SrcTableClusterId):
        self._SrcTableClusterId = SrcTableClusterId

    @property
    def SrcTableGroupId(self):
        r"""源表格的表格组id
        :rtype: str
        """
        return self._SrcTableGroupId

    @SrcTableGroupId.setter
    def SrcTableGroupId(self, SrcTableGroupId):
        self._SrcTableGroupId = SrcTableGroupId

    @property
    def SrcTableName(self):
        r"""源表格的表名
        :rtype: str
        """
        return self._SrcTableName

    @SrcTableName.setter
    def SrcTableName(self, SrcTableName):
        self._SrcTableName = SrcTableName

    @property
    def DstTableClusterId(self):
        r"""目标表格的集群id
        :rtype: str
        """
        return self._DstTableClusterId

    @DstTableClusterId.setter
    def DstTableClusterId(self, DstTableClusterId):
        self._DstTableClusterId = DstTableClusterId

    @property
    def DstTableGroupId(self):
        r"""目标表格的表格组id
        :rtype: str
        """
        return self._DstTableGroupId

    @DstTableGroupId.setter
    def DstTableGroupId(self, DstTableGroupId):
        self._DstTableGroupId = DstTableGroupId

    @property
    def DstTableName(self):
        r"""目标表格的表名
        :rtype: str
        """
        return self._DstTableName

    @DstTableName.setter
    def DstTableName(self, DstTableName):
        self._DstTableName = DstTableName

    @property
    def SrcTableInstanceId(self):
        r"""源表格的实例id
        :rtype: str
        """
        return self._SrcTableInstanceId

    @SrcTableInstanceId.setter
    def SrcTableInstanceId(self, SrcTableInstanceId):
        self._SrcTableInstanceId = SrcTableInstanceId

    @property
    def DstTableInstanceId(self):
        r"""目标表格的实例id
        :rtype: str
        """
        return self._DstTableInstanceId

    @DstTableInstanceId.setter
    def DstTableInstanceId(self, DstTableInstanceId):
        self._DstTableInstanceId = DstTableInstanceId


    def _deserialize(self, params):
        self._SrcTableClusterId = params.get("SrcTableClusterId")
        self._SrcTableGroupId = params.get("SrcTableGroupId")
        self._SrcTableName = params.get("SrcTableName")
        self._DstTableClusterId = params.get("DstTableClusterId")
        self._DstTableGroupId = params.get("DstTableGroupId")
        self._DstTableName = params.get("DstTableName")
        self._SrcTableInstanceId = params.get("SrcTableInstanceId")
        self._DstTableInstanceId = params.get("DstTableInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupRequest(AbstractModel):
    r"""CreateBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待创建备份表所属集群ID
        :type ClusterId: str
        :param _SelectedTables: 待创建备份表信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._ClusterId = None
        self._SelectedTables = None
        self._Remark = None

    @property
    def ClusterId(self):
        r"""待创建备份表所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待创建备份表信息列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    r"""CreateBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 创建的备份任务ID列表
        :type TaskIds: list of str
        :param _ApplicationIds: 创建的备份申请ID列表
        :type ApplicationIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskIds = None
        self._ApplicationIds = None
        self._RequestId = None

    @property
    def TaskIds(self):
        r"""创建的备份任务ID列表
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def ApplicationIds(self):
        r"""创建的备份申请ID列表
        :rtype: list of str
        """
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds

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
        self._TaskIds = params.get("TaskIds")
        self._ApplicationIds = params.get("ApplicationIds")
        self._RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    r"""CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdlType: 集群数据描述语言类型，如：`PROTO`，`TDR`或`MIX`
        :type IdlType: str
        :param _ClusterName: 集群名称，可使用中文或英文字符，最大长度32个字符
        :type ClusterName: str
        :param _VpcId: 集群所绑定的私有网络实例ID，形如：vpc-f49l6u0z
        :type VpcId: str
        :param _SubnetId: 集群所绑定的子网实例ID，形如：subnet-pxir56ns
        :type SubnetId: str
        :param _Password: 集群访问密码，必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母
        :type Password: str
        :param _ResourceTags: 集群标签列表
        :type ResourceTags: list of TagInfoUnit
        :param _Ipv6Enable: 集群是否开启IPv6功能
        :type Ipv6Enable: int
        :param _ServerList: 独占集群占用的svr机器
        :type ServerList: list of MachineInfo
        :param _ProxyList: 独占集群占用的proxy机器
        :type ProxyList: list of MachineInfo
        :param _ClusterType: 集群类型1共享2独占
        :type ClusterType: int
        :param _AuthType: 密码认证类型，0 静态认证， 1 签名认证
        :type AuthType: int
        """
        self._IdlType = None
        self._ClusterName = None
        self._VpcId = None
        self._SubnetId = None
        self._Password = None
        self._ResourceTags = None
        self._Ipv6Enable = None
        self._ServerList = None
        self._ProxyList = None
        self._ClusterType = None
        self._AuthType = None

    @property
    def IdlType(self):
        r"""集群数据描述语言类型，如：`PROTO`，`TDR`或`MIX`
        :rtype: str
        """
        return self._IdlType

    @IdlType.setter
    def IdlType(self, IdlType):
        self._IdlType = IdlType

    @property
    def ClusterName(self):
        r"""集群名称，可使用中文或英文字符，最大长度32个字符
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def VpcId(self):
        r"""集群所绑定的私有网络实例ID，形如：vpc-f49l6u0z
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""集群所绑定的子网实例ID，形如：subnet-pxir56ns
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Password(self):
        r"""集群访问密码，必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ResourceTags(self):
        r"""集群标签列表
        :rtype: list of TagInfoUnit
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Ipv6Enable(self):
        r"""集群是否开启IPv6功能
        :rtype: int
        """
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable

    @property
    def ServerList(self):
        r"""独占集群占用的svr机器
        :rtype: list of MachineInfo
        """
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def ProxyList(self):
        r"""独占集群占用的proxy机器
        :rtype: list of MachineInfo
        """
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList

    @property
    def ClusterType(self):
        r"""集群类型1共享2独占
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def AuthType(self):
        r"""密码认证类型，0 静态认证， 1 签名认证
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType


    def _deserialize(self, params):
        self._IdlType = params.get("IdlType")
        self._ClusterName = params.get("ClusterName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Password = params.get("Password")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Ipv6Enable = params.get("Ipv6Enable")
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        self._ClusterType = params.get("ClusterType")
        self._AuthType = params.get("AuthType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    r"""CreateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        r"""集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class CreateSnapshotsRequest(AbstractModel):
    r"""CreateSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格所属集群id
        :type ClusterId: str
        :param _SelectedTables: 快照列表
        :type SelectedTables: list of SnapshotInfo
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表格所属集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""快照列表
        :rtype: list of SnapshotInfo
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotsResponse(AbstractModel):
    r"""CreateSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 批量创建的快照数量
        :type TotalCount: int
        :param _TableResults: 批量创建的快照结果列表
        :type TableResults: list of SnapshotResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""批量创建的快照数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""批量创建的快照结果列表
        :rtype: list of SnapshotResult
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class CreateTableGroupRequest(AbstractModel):
    r"""CreateTableGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格组所属集群ID
        :type ClusterId: str
        :param _TableGroupName: 表格组名称，可以采用中文、英文或数字字符，最大长度32个字符
        :type TableGroupName: str
        :param _TableGroupId: 表格组ID，可以由用户指定，但在同一个集群内不能重复，如果不指定则采用自增的模式
        :type TableGroupId: str
        :param _ResourceTags: 表格组标签列表
        :type ResourceTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._TableGroupName = None
        self._TableGroupId = None
        self._ResourceTags = None

    @property
    def ClusterId(self):
        r"""表格组所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupName(self):
        r"""表格组名称，可以采用中文、英文或数字字符，最大长度32个字符
        :rtype: str
        """
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName

    @property
    def TableGroupId(self):
        r"""表格组ID，可以由用户指定，但在同一个集群内不能重复，如果不指定则采用自增的模式
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def ResourceTags(self):
        r"""表格组标签列表
        :rtype: list of TagInfoUnit
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupName = params.get("TableGroupName")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableGroupResponse(AbstractModel):
    r"""CreateTableGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableGroupId: 创建成功的表格组ID
        :type TableGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableGroupId = None
        self._RequestId = None

    @property
    def TableGroupId(self):
        r"""创建成功的表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

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
        self._TableGroupId = params.get("TableGroupId")
        self._RequestId = params.get("RequestId")


class CreateTablesRequest(AbstractModel):
    r"""CreateTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待创建表格所属集群ID
        :type ClusterId: str
        :param _IdlFiles: 用户选定的建表格IDL文件列表
        :type IdlFiles: list of IdlFileInfo
        :param _SelectedTables: 待创建表格信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param _ResourceTags: 表格标签列表
        :type ResourceTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._IdlFiles = None
        self._SelectedTables = None
        self._ResourceTags = None

    @property
    def ClusterId(self):
        r"""待创建表格所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IdlFiles(self):
        r"""用户选定的建表格IDL文件列表
        :rtype: list of IdlFileInfo
        """
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def SelectedTables(self):
        r"""待创建表格信息列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def ResourceTags(self):
        r"""表格标签列表
        :rtype: list of TagInfoUnit
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTablesResponse(AbstractModel):
    r"""CreateTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 批量创建表格结果数量
        :type TotalCount: int
        :param _TableResults: 批量创建表格结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""批量创建表格结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""批量创建表格结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteBackupRecordsRequest(AbstractModel):
    r"""DeleteBackupRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待删除备份记录的所在集群ID
        :type ClusterId: str
        :param _BackupRecords: 待删除备份记录的详情
        :type BackupRecords: list of BackupRecords
        """
        self._ClusterId = None
        self._BackupRecords = None

    @property
    def ClusterId(self):
        r"""待删除备份记录的所在集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupRecords(self):
        r"""待删除备份记录的详情
        :rtype: list of BackupRecords
        """
        return self._BackupRecords

    @BackupRecords.setter
    def BackupRecords(self, BackupRecords):
        self._BackupRecords = BackupRecords


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("BackupRecords") is not None:
            self._BackupRecords = []
            for item in params.get("BackupRecords"):
                obj = BackupRecords()
                obj._deserialize(item)
                self._BackupRecords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupRecordsResponse(AbstractModel):
    r"""DeleteBackupRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :rtype: str
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


class DeleteClusterRequest(AbstractModel):
    r"""DeleteCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待删除的集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        r"""待删除的集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    r"""DeleteCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 删除集群生成的任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""删除集群生成的任务ID
        :rtype: str
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


class DeleteIdlFilesRequest(AbstractModel):
    r"""DeleteIdlFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: IDL所属集群ID
        :type ClusterId: str
        :param _IdlFiles: 待删除的IDL文件信息列表
        :type IdlFiles: list of IdlFileInfo
        """
        self._ClusterId = None
        self._IdlFiles = None

    @property
    def ClusterId(self):
        r"""IDL所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IdlFiles(self):
        r"""待删除的IDL文件信息列表
        :rtype: list of IdlFileInfo
        """
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIdlFilesResponse(AbstractModel):
    r"""DeleteIdlFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果记录数量
        :type TotalCount: int
        :param _IdlFileInfos: 删除结果
        :type IdlFileInfos: list of IdlFileInfoWithoutContent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._IdlFileInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""结果记录数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IdlFileInfos(self):
        r"""删除结果
        :rtype: list of IdlFileInfoWithoutContent
        """
        return self._IdlFileInfos

    @IdlFileInfos.setter
    def IdlFileInfos(self, IdlFileInfos):
        self._IdlFileInfos = IdlFileInfos

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
        if params.get("IdlFileInfos") is not None:
            self._IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfoWithoutContent()
                obj._deserialize(item)
                self._IdlFileInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    r"""DeleteSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格所属集群id
        :type ClusterId: str
        :param _SelectedTables: 删除的快照列表
        :type SelectedTables: list of SnapshotInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表格所属集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""删除的快照列表
        :rtype: list of SnapshotInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    r"""DeleteSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 批量删除的快照数量
        :type TotalCount: int
        :param _TableResults: 批量删除的快照结果
        :type TableResults: list of SnapshotResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""批量删除的快照数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""批量删除的快照结果
        :rtype: list of SnapshotResult
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteTableDataFlowRequest(AbstractModel):
    r"""DeleteTableDataFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格所属集群实例ID
        :type ClusterId: str
        :param _SelectedTables: 待删除分布式索引的表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表格所属集群实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待删除分布式索引的表格列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableDataFlowResponse(AbstractModel):
    r"""DeleteTableDataFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 删除表格分布式索引结果数量
        :type TotalCount: int
        :param _TableResults: 删除表格分布式索引结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""删除表格分布式索引结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""删除表格分布式索引结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteTableGroupRequest(AbstractModel):
    r"""DeleteTableGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格组所属的集群ID
        :type ClusterId: str
        :param _TableGroupId: 表格组ID
        :type TableGroupId: str
        """
        self._ClusterId = None
        self._TableGroupId = None

    @property
    def ClusterId(self):
        r"""表格组所属的集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        r"""表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableGroupResponse(AbstractModel):
    r"""DeleteTableGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 删除表格组所创建的任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""删除表格组所创建的任务ID
        :rtype: str
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


class DeleteTableIndexRequest(AbstractModel):
    r"""DeleteTableIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格所属集群实例ID
        :type ClusterId: str
        :param _SelectedTables: 待删除分布式索引的表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表格所属集群实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待删除分布式索引的表格列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableIndexResponse(AbstractModel):
    r"""DeleteTableIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 删除表格分布式索引结果数量
        :type TotalCount: int
        :param _TableResults: 删除表格分布式索引结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""删除表格分布式索引结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""删除表格分布式索引结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteTablesRequest(AbstractModel):
    r"""DeleteTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待删除表所在集群ID
        :type ClusterId: str
        :param _SelectedTables: 待删除表信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""待删除表所在集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待删除表信息列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTablesResponse(AbstractModel):
    r"""DeleteTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 删除表结果数量
        :type TotalCount: int
        :param _TableResults: 删除表结果详情列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""删除表结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""删除表结果详情列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    r"""DescribeApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID，用于获取指定集群的单据
        :type ClusterId: str
        :param _Limit: 分页，限制当前返回多少条记录，大于等于10
        :type Limit: int
        :param _Offset: 分页，从多少条数据开始返回
        :type Offset: int
        :param _CensorStatus: 申请单状态，用于过滤，0-待审核 1-已经审核并提交任务 2-已驳回
        :type CensorStatus: int
        :param _TableGroupId: 表格组id，用于过滤
        :type TableGroupId: str
        :param _TableName: 表格名，用于过滤
        :type TableName: str
        :param _Applicant: 申请人uin，用于过滤
        :type Applicant: str
        :param _ApplyType: 申请类型，用于过滤，0加表 1删除表 2清理表 3修改表 4表重建 5存储层扩缩容 6接入层扩缩容 7复制表数据 8key回档
        :type ApplyType: int
        """
        self._ClusterId = None
        self._Limit = None
        self._Offset = None
        self._CensorStatus = None
        self._TableGroupId = None
        self._TableName = None
        self._Applicant = None
        self._ApplyType = None

    @property
    def ClusterId(self):
        r"""集群ID，用于获取指定集群的单据
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Limit(self):
        r"""分页，限制当前返回多少条记录，大于等于10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页，从多少条数据开始返回
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CensorStatus(self):
        r"""申请单状态，用于过滤，0-待审核 1-已经审核并提交任务 2-已驳回
        :rtype: int
        """
        return self._CensorStatus

    @CensorStatus.setter
    def CensorStatus(self, CensorStatus):
        self._CensorStatus = CensorStatus

    @property
    def TableGroupId(self):
        r"""表格组id，用于过滤
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表格名，用于过滤
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Applicant(self):
        r"""申请人uin，用于过滤
        :rtype: str
        """
        return self._Applicant

    @Applicant.setter
    def Applicant(self, Applicant):
        self._Applicant = Applicant

    @property
    def ApplyType(self):
        r"""申请类型，用于过滤，0加表 1删除表 2清理表 3修改表 4表重建 5存储层扩缩容 6接入层扩缩容 7复制表数据 8key回档
        :rtype: int
        """
        return self._ApplyType

    @ApplyType.setter
    def ApplyType(self, ApplyType):
        self._ApplyType = ApplyType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CensorStatus = params.get("CensorStatus")
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._Applicant = params.get("Applicant")
        self._ApplyType = params.get("ApplyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    r"""DescribeApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Applications: 申请单列表
        :type Applications: list of Application
        :param _TotalCount: 申请单个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Applications = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Applications(self):
        r"""申请单列表
        :rtype: list of Application
        """
        return self._Applications

    @Applications.setter
    def Applications(self, Applications):
        self._Applications = Applications

    @property
    def TotalCount(self):
        r"""申请单个数
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
        if params.get("Applications") is not None:
            self._Applications = []
            for item in params.get("Applications"):
                obj = Application()
                obj._deserialize(item)
                self._Applications.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBackupRecordsRequest(AbstractModel):
    r"""DescribeBackupRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID，用于获取指定集群的单据
        :type ClusterId: str
        :param _Limit: 分页
        :type Limit: int
        :param _Offset: 分页
        :type Offset: int
        :param _TableGroupId: 表格组id，用于过滤
        :type TableGroupId: str
        :param _TableName: 表格名，用于过滤
        :type TableName: str
        """
        self._ClusterId = None
        self._Limit = None
        self._Offset = None
        self._TableGroupId = None
        self._TableName = None

    @property
    def ClusterId(self):
        r"""集群ID，用于获取指定集群的单据
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Limit(self):
        r"""分页
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TableGroupId(self):
        r"""表格组id，用于过滤
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表格名，用于过滤
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupRecordsResponse(AbstractModel):
    r"""DescribeBackupRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupRecords: 备份记录详情
        :type BackupRecords: list of BackupRecords
        :param _TotalCount: 返回记录条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupRecords = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BackupRecords(self):
        r"""备份记录详情
        :rtype: list of BackupRecords
        """
        return self._BackupRecords

    @BackupRecords.setter
    def BackupRecords(self, BackupRecords):
        self._BackupRecords = BackupRecords

    @property
    def TotalCount(self):
        r"""返回记录条数
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
        if params.get("BackupRecords") is not None:
            self._BackupRecords = []
            for item in params.get("BackupRecords"):
                obj = BackupRecords()
                obj._deserialize(item)
                self._BackupRecords.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClusterTagsRequest(AbstractModel):
    r"""DescribeClusterTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: 集群ID列表
        :type ClusterIds: list of str
        """
        self._ClusterIds = None

    @property
    def ClusterIds(self):
        r"""集群ID列表
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterTagsResponse(AbstractModel):
    r"""DescribeClusterTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rows: 集群标签信息列表
        :type Rows: list of TagsInfoOfCluster
        :param _TotalCount: 返回结果个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rows = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Rows(self):
        r"""集群标签信息列表
        :rtype: list of TagsInfoOfCluster
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def TotalCount(self):
        r"""返回结果个数
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
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfCluster()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    r"""DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: 指定查询的集群ID列表
        :type ClusterIds: list of str
        :param _Filters: 查询过滤条件
        :type Filters: list of Filter
        :param _Offset: 查询列表偏移量
        :type Offset: int
        :param _Limit: 查询列表返回记录数，默认值20
        :type Limit: int
        :param _Ipv6Enable: 是否启用Ipv6
        :type Ipv6Enable: int
        """
        self._ClusterIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Ipv6Enable = None

    @property
    def ClusterIds(self):
        r"""指定查询的集群ID列表
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def Filters(self):
        r"""查询过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询列表偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询列表返回记录数，默认值20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Ipv6Enable(self):
        r"""是否启用Ipv6
        :rtype: int
        """
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    r"""DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集群实例数
        :type TotalCount: int
        :param _Clusters: 集群实例列表
        :type Clusters: list of ClusterInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Clusters = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""集群实例数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Clusters(self):
        r"""集群实例列表
        :rtype: list of ClusterInfo
        """
        return self._Clusters

    @Clusters.setter
    def Clusters(self, Clusters):
        self._Clusters = Clusters

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
        if params.get("Clusters") is not None:
            self._Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self._Clusters.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIdlFileInfosRequest(AbstractModel):
    r"""DescribeIdlFileInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 文件所属集群ID
        :type ClusterId: str
        :param _TableGroupIds: 文件所属表格组ID
        :type TableGroupIds: list of str
        :param _IdlFileIds: 指定文件ID列表
        :type IdlFileIds: list of str
        :param _Offset: 查询列表偏移量
        :type Offset: int
        :param _Limit: 查询列表返回记录数
        :type Limit: int
        """
        self._ClusterId = None
        self._TableGroupIds = None
        self._IdlFileIds = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        r"""文件所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        r"""文件所属表格组ID
        :rtype: list of str
        """
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds

    @property
    def IdlFileIds(self):
        r"""指定文件ID列表
        :rtype: list of str
        """
        return self._IdlFileIds

    @IdlFileIds.setter
    def IdlFileIds(self, IdlFileIds):
        self._IdlFileIds = IdlFileIds

    @property
    def Offset(self):
        r"""查询列表偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询列表返回记录数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
        self._IdlFileIds = params.get("IdlFileIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdlFileInfosResponse(AbstractModel):
    r"""DescribeIdlFileInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 文件数量
        :type TotalCount: int
        :param _IdlFileInfos: 文件详情列表
        :type IdlFileInfos: list of IdlFileInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._IdlFileInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""文件数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IdlFileInfos(self):
        r"""文件详情列表
        :rtype: list of IdlFileInfo
        """
        return self._IdlFileInfos

    @IdlFileInfos.setter
    def IdlFileInfos(self, IdlFileInfos):
        self._IdlFileInfos = IdlFileInfos

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
        if params.get("IdlFileInfos") is not None:
            self._IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFileInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineRequest(AbstractModel):
    r"""DescribeMachine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ipv6Enable: 不为0，表示查询支持ipv6的机器
        :type Ipv6Enable: int
        """
        self._Ipv6Enable = None

    @property
    def Ipv6Enable(self):
        r"""不为0，表示查询支持ipv6的机器
        :rtype: int
        """
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable


    def _deserialize(self, params):
        self._Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineResponse(AbstractModel):
    r"""DescribeMachine返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PoolList: 独占机器资源列表
        :type PoolList: list of PoolInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PoolList = None
        self._RequestId = None

    @property
    def PoolList(self):
        r"""独占机器资源列表
        :rtype: list of PoolInfo
        """
        return self._PoolList

    @PoolList.setter
    def PoolList(self, PoolList):
        self._PoolList = PoolList

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
        if params.get("PoolList") is not None:
            self._PoolList = []
            for item in params.get("PoolList"):
                obj = PoolInfo()
                obj._deserialize(item)
                self._PoolList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    r"""DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    r"""DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可用区详情结果数量
        :type TotalCount: int
        :param _RegionInfos: 可用区详情结果列表
        :type RegionInfos: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""可用区详情结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionInfos(self):
        r"""可用区详情结果列表
        :rtype: list of RegionInfo
        """
        return self._RegionInfos

    @RegionInfos.setter
    def RegionInfos(self, RegionInfos):
        self._RegionInfos = RegionInfos

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
        if params.get("RegionInfos") is not None:
            self._RegionInfos = []
            for item in params.get("RegionInfos"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    r"""DescribeSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格所属集群id
        :type ClusterId: str
        :param _TableGroupId: 所属表格组ID
        :type TableGroupId: str
        :param _TableName: 表名称
        :type TableName: str
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _SelectedTables: 批量拉取快照的表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._TableName = None
        self._SnapshotName = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表格所属集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        r"""所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def SnapshotName(self):
        r"""快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SelectedTables(self):
        r"""批量拉取快照的表格列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._SnapshotName = params.get("SnapshotName")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    r"""DescribeSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 快照数量
        :type TotalCount: int
        :param _TableResults: 快照结果列表
        :type TableResults: list of SnapshotResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""快照数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""快照结果列表
        :rtype: list of SnapshotResult
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTableGroupTagsRequest(AbstractModel):
    r"""DescribeTableGroupTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待查询标签表格组所属集群ID
        :type ClusterId: str
        :param _TableGroupIds: 待查询标签表格组ID列表
        :type TableGroupIds: list of str
        """
        self._ClusterId = None
        self._TableGroupIds = None

    @property
    def ClusterId(self):
        r"""待查询标签表格组所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        r"""待查询标签表格组ID列表
        :rtype: list of str
        """
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableGroupTagsResponse(AbstractModel):
    r"""DescribeTableGroupTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rows: 表格组标签信息列表
        :type Rows: list of TagsInfoOfTableGroup
        :param _TotalCount: 返回结果个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rows = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Rows(self):
        r"""表格组标签信息列表
        :rtype: list of TagsInfoOfTableGroup
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def TotalCount(self):
        r"""返回结果个数
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
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfTableGroup()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTableGroupsRequest(AbstractModel):
    r"""DescribeTableGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格组所属集群ID
        :type ClusterId: str
        :param _TableGroupIds: 表格组ID列表
        :type TableGroupIds: list of str
        :param _Filters: 过滤条件，本接口支持：TableGroupName，TableGroupId
        :type Filters: list of Filter
        :param _Offset: 查询列表偏移量
        :type Offset: int
        :param _Limit: 查询列表返回记录数
        :type Limit: int
        """
        self._ClusterId = None
        self._TableGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        r"""表格组所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        r"""表格组ID列表
        :rtype: list of str
        """
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds

    @property
    def Filters(self):
        r"""过滤条件，本接口支持：TableGroupName，TableGroupId
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询列表偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询列表返回记录数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
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
        


class DescribeTableGroupsResponse(AbstractModel):
    r"""DescribeTableGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表格组数量
        :type TotalCount: int
        :param _TableGroups: 表格组信息列表
        :type TableGroups: list of TableGroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""表格组数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableGroups(self):
        r"""表格组信息列表
        :rtype: list of TableGroupInfo
        """
        return self._TableGroups

    @TableGroups.setter
    def TableGroups(self, TableGroups):
        self._TableGroups = TableGroups

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
        if params.get("TableGroups") is not None:
            self._TableGroups = []
            for item in params.get("TableGroups"):
                obj = TableGroupInfo()
                obj._deserialize(item)
                self._TableGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTableTagsRequest(AbstractModel):
    r"""DescribeTableTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格所属集群ID
        :type ClusterId: str
        :param _SelectedTables: 表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表格所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""表格列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableTagsResponse(AbstractModel):
    r"""DescribeTableTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回结果总数
        :type TotalCount: int
        :param _Rows: 表格标签信息列表
        :type Rows: list of TagsInfoOfTable
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""返回结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        r"""表格标签信息列表
        :rtype: list of TagsInfoOfTable
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

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
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfTable()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesInRecycleRequest(AbstractModel):
    r"""DescribeTablesInRecycle请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待查询表格所属集群ID
        :type ClusterId: str
        :param _TableGroupIds: 待查询表格所属表格组ID列表
        :type TableGroupIds: list of str
        :param _Filters: 过滤条件，本接口支持：TableName，TableInstanceId
        :type Filters: list of Filter
        :param _Offset: 查询结果偏移量
        :type Offset: int
        :param _Limit: 查询结果返回记录数量
        :type Limit: int
        """
        self._ClusterId = None
        self._TableGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        r"""待查询表格所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        r"""待查询表格所属表格组ID列表
        :rtype: list of str
        """
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds

    @property
    def Filters(self):
        r"""过滤条件，本接口支持：TableName，TableInstanceId
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询结果偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果返回记录数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
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
        


class DescribeTablesInRecycleResponse(AbstractModel):
    r"""DescribeTablesInRecycle返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表格数量
        :type TotalCount: int
        :param _TableInfos: 表格详情结果列表
        :type TableInfos: list of TableInfoNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""表格数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableInfos(self):
        r"""表格详情结果列表
        :rtype: list of TableInfoNew
        """
        return self._TableInfos

    @TableInfos.setter
    def TableInfos(self, TableInfos):
        self._TableInfos = TableInfos

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
        if params.get("TableInfos") is not None:
            self._TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self._TableInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    r"""DescribeTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待查询表格所属集群ID
        :type ClusterId: str
        :param _TableGroupIds: 待查询表格所属表格组ID列表
        :type TableGroupIds: list of str
        :param _SelectedTables: 待查询表格信息列表，用户不用关注，过滤请使用filter
        :type SelectedTables: list of SelectedTableInfoNew
        :param _Filters: 过滤条件，本接口支持：TableName，TableInstanceId
        :type Filters: list of Filter
        :param _Offset: 查询结果偏移量
        :type Offset: int
        :param _Limit: 查询结果返回记录数量
        :type Limit: int
        """
        self._ClusterId = None
        self._TableGroupIds = None
        self._SelectedTables = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        r"""待查询表格所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        r"""待查询表格所属表格组ID列表
        :rtype: list of str
        """
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds

    @property
    def SelectedTables(self):
        r"""待查询表格信息列表，用户不用关注，过滤请使用filter
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def Filters(self):
        r"""过滤条件，本接口支持：TableName，TableInstanceId
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询结果偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果返回记录数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
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
        


class DescribeTablesResponse(AbstractModel):
    r"""DescribeTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表格数量
        :type TotalCount: int
        :param _TableInfos: 表格详情结果列表
        :type TableInfos: list of TableInfoNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""表格数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableInfos(self):
        r"""表格详情结果列表
        :rtype: list of TableInfoNew
        """
        return self._TableInfos

    @TableInfos.setter
    def TableInfos(self, TableInfos):
        self._TableInfos = TableInfos

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
        if params.get("TableInfos") is not None:
            self._TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self._TableInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    r"""DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: 需要查询任务所属的集群ID列表
        :type ClusterIds: list of str
        :param _TaskIds: 需要查询的任务ID列表
        :type TaskIds: list of str
        :param _Filters: 过滤条件，本接口支持：Content，TaskType, Operator, Time
        :type Filters: list of Filter
        :param _Offset: 查询列表偏移量
        :type Offset: int
        :param _Limit: 查询列表返回记录数
        :type Limit: int
        """
        self._ClusterIds = None
        self._TaskIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterIds(self):
        r"""需要查询任务所属的集群ID列表
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def TaskIds(self):
        r"""需要查询的任务ID列表
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def Filters(self):
        r"""过滤条件，本接口支持：Content，TaskType, Operator, Time
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询列表偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询列表返回记录数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._TaskIds = params.get("TaskIds")
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
        


class DescribeTasksResponse(AbstractModel):
    r"""DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务数量
        :type TotalCount: int
        :param _TaskInfos: 查询到的任务详情列表
        :type TaskInfos: list of TaskInfoNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""任务数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskInfos(self):
        r"""查询到的任务详情列表
        :rtype: list of TaskInfoNew
        """
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

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
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = TaskInfoNew()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUinInWhitelistRequest(AbstractModel):
    r"""DescribeUinInWhitelist请求参数结构体

    """


class DescribeUinInWhitelistResponse(AbstractModel):
    r"""DescribeUinInWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询结果：`FALSE` 否；`TRUE` 是
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""查询结果：`FALSE` 否；`TRUE` 是
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DisableRestProxyRequest(AbstractModel):
    r"""DisableRestProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 对应appid
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        r"""对应appid
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRestProxyResponse(AbstractModel):
    r"""DisableRestProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RestProxyStatus: RestProxy的状态，0为关闭，1为开启中，2为开启，3为关闭中
        :type RestProxyStatus: int
        :param _TaskId: TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RestProxyStatus = None
        self._TaskId = None
        self._RequestId = None

    @property
    def RestProxyStatus(self):
        r"""RestProxy的状态，0为关闭，1为开启中，2为开启，3为关闭中
        :rtype: int
        """
        return self._RestProxyStatus

    @RestProxyStatus.setter
    def RestProxyStatus(self, RestProxyStatus):
        self._RestProxyStatus = RestProxyStatus

    @property
    def TaskId(self):
        r"""TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :rtype: str
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
        self._RestProxyStatus = params.get("RestProxyStatus")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class EnableRestProxyRequest(AbstractModel):
    r"""EnableRestProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID。
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        r"""集群 ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRestProxyResponse(AbstractModel):
    r"""EnableRestProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RestProxyStatus: RestProxy的状态，0为关闭，1为开启中，2为开启，3为关闭中
        :type RestProxyStatus: int
        :param _TaskId: TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RestProxyStatus = None
        self._TaskId = None
        self._RequestId = None

    @property
    def RestProxyStatus(self):
        r"""RestProxy的状态，0为关闭，1为开启中，2为开启，3为关闭中
        :rtype: int
        """
        return self._RestProxyStatus

    @RestProxyStatus.setter
    def RestProxyStatus(self, RestProxyStatus):
        self._RestProxyStatus = RestProxyStatus

    @property
    def TaskId(self):
        r"""TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :rtype: str
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
        self._RestProxyStatus = params.get("RestProxyStatus")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ErrorInfo(AbstractModel):
    r"""描述每个实例（应用，大区或表）处理过程中可能出现的错误详情。

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: str
        :param _Message: 错误信息
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        r"""错误码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldInfo(AbstractModel):
    r"""表格字段信息列表

    """

    def __init__(self):
        r"""
        :param _FieldName: 表格字段名称
        :type FieldName: str
        :param _IsPrimaryKey: 字段是否是主键字段
        :type IsPrimaryKey: str
        :param _FieldType: 字段类型
        :type FieldType: str
        :param _FieldSize: 字段长度
        :type FieldSize: int
        """
        self._FieldName = None
        self._IsPrimaryKey = None
        self._FieldType = None
        self._FieldSize = None

    @property
    def FieldName(self):
        r"""表格字段名称
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def IsPrimaryKey(self):
        r"""字段是否是主键字段
        :rtype: str
        """
        return self._IsPrimaryKey

    @IsPrimaryKey.setter
    def IsPrimaryKey(self, IsPrimaryKey):
        self._IsPrimaryKey = IsPrimaryKey

    @property
    def FieldType(self):
        r"""字段类型
        :rtype: str
        """
        return self._FieldType

    @FieldType.setter
    def FieldType(self, FieldType):
        self._FieldType = FieldType

    @property
    def FieldSize(self):
        r"""字段长度
        :rtype: int
        """
        return self._FieldSize

    @FieldSize.setter
    def FieldSize(self, FieldSize):
        self._FieldSize = FieldSize


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._IsPrimaryKey = params.get("IsPrimaryKey")
        self._FieldType = params.get("FieldType")
        self._FieldSize = params.get("FieldSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名
        :type Name: str
        :param _Value: 过滤字段值
        :type Value: str
        :param _Values: 过滤字段值
        :type Values: list of str
        """
        self._Name = None
        self._Value = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤字段名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""过滤字段值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Values(self):
        r"""过滤字段值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdlFileInfo(AbstractModel):
    r"""表定义描述文件详情，包含文件内容

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名称，不包含扩展名
        :type FileName: str
        :param _FileType: 数据描述语言（IDL）类型
        :type FileType: str
        :param _FileExtType: 文件扩展名
        :type FileExtType: str
        :param _FileSize: 文件大小（Bytes）
        :type FileSize: int
        :param _FileId: 文件ID，对于已上传的文件有意义
        :type FileId: int
        :param _FileContent: 文件内容，对于本次新上传的文件有意义
        :type FileContent: str
        """
        self._FileName = None
        self._FileType = None
        self._FileExtType = None
        self._FileSize = None
        self._FileId = None
        self._FileContent = None

    @property
    def FileName(self):
        r"""文件名称，不包含扩展名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""数据描述语言（IDL）类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileExtType(self):
        r"""文件扩展名
        :rtype: str
        """
        return self._FileExtType

    @FileExtType.setter
    def FileExtType(self, FileExtType):
        self._FileExtType = FileExtType

    @property
    def FileSize(self):
        r"""文件大小（Bytes）
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileId(self):
        r"""文件ID，对于已上传的文件有意义
        :rtype: int
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileContent(self):
        r"""文件内容，对于本次新上传的文件有意义
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._FileExtType = params.get("FileExtType")
        self._FileSize = params.get("FileSize")
        self._FileId = params.get("FileId")
        self._FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdlFileInfoWithoutContent(AbstractModel):
    r"""表定义描述文件详情，不包含文件内容

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名称，不包含扩展名
        :type FileName: str
        :param _FileType: 数据描述语言（IDL）类型
        :type FileType: str
        :param _FileExtType: 文件扩展名
        :type FileExtType: str
        :param _FileSize: 文件大小（Bytes）
        :type FileSize: int
        :param _FileId: 文件ID
        :type FileId: int
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._FileName = None
        self._FileType = None
        self._FileExtType = None
        self._FileSize = None
        self._FileId = None
        self._Error = None

    @property
    def FileName(self):
        r"""文件名称，不包含扩展名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""数据描述语言（IDL）类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileExtType(self):
        r"""文件扩展名
        :rtype: str
        """
        return self._FileExtType

    @FileExtType.setter
    def FileExtType(self, FileExtType):
        self._FileExtType = FileExtType

    @property
    def FileSize(self):
        r"""文件大小（Bytes）
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileId(self):
        r"""文件ID
        :rtype: int
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._FileExtType = params.get("FileExtType")
        self._FileSize = params.get("FileSize")
        self._FileId = params.get("FileId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSnapshotsRequest(AbstractModel):
    r"""ImportSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格所属的集群id
        :type ClusterId: str
        :param _Snapshots: 用于导入的快照信息
        :type Snapshots: :class:`tencentcloud.tcaplusdb.v20190823.models.SnapshotInfo`
        :param _ImportSpecialKey: 是否导入部分记录，TRUE表示导入部分记录，FALSE表示全表导入
        :type ImportSpecialKey: str
        :param _ImportOriginTable: 是否导入到当前表，TRUE表示导入到当前表，FALSE表示导入到新表
        :type ImportOriginTable: str
        :param _KeyFile: 部分记录的key文件
        :type KeyFile: :class:`tencentcloud.tcaplusdb.v20190823.models.KeyFile`
        :param _NewTableGroupId: 如果导入到新表，此为新表所属的表格组id
        :type NewTableGroupId: str
        :param _NewTableName: 如果导入到新表，此为新表的表名，系统会以该名称自动创建一张结构相同的空表
        :type NewTableName: str
        """
        self._ClusterId = None
        self._Snapshots = None
        self._ImportSpecialKey = None
        self._ImportOriginTable = None
        self._KeyFile = None
        self._NewTableGroupId = None
        self._NewTableName = None

    @property
    def ClusterId(self):
        r"""表格所属的集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Snapshots(self):
        r"""用于导入的快照信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SnapshotInfo`
        """
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots

    @property
    def ImportSpecialKey(self):
        r"""是否导入部分记录，TRUE表示导入部分记录，FALSE表示全表导入
        :rtype: str
        """
        return self._ImportSpecialKey

    @ImportSpecialKey.setter
    def ImportSpecialKey(self, ImportSpecialKey):
        self._ImportSpecialKey = ImportSpecialKey

    @property
    def ImportOriginTable(self):
        r"""是否导入到当前表，TRUE表示导入到当前表，FALSE表示导入到新表
        :rtype: str
        """
        return self._ImportOriginTable

    @ImportOriginTable.setter
    def ImportOriginTable(self, ImportOriginTable):
        self._ImportOriginTable = ImportOriginTable

    @property
    def KeyFile(self):
        r"""部分记录的key文件
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.KeyFile`
        """
        return self._KeyFile

    @KeyFile.setter
    def KeyFile(self, KeyFile):
        self._KeyFile = KeyFile

    @property
    def NewTableGroupId(self):
        r"""如果导入到新表，此为新表所属的表格组id
        :rtype: str
        """
        return self._NewTableGroupId

    @NewTableGroupId.setter
    def NewTableGroupId(self, NewTableGroupId):
        self._NewTableGroupId = NewTableGroupId

    @property
    def NewTableName(self):
        r"""如果导入到新表，此为新表的表名，系统会以该名称自动创建一张结构相同的空表
        :rtype: str
        """
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Snapshots") is not None:
            self._Snapshots = SnapshotInfo()
            self._Snapshots._deserialize(params.get("Snapshots"))
        self._ImportSpecialKey = params.get("ImportSpecialKey")
        self._ImportOriginTable = params.get("ImportOriginTable")
        if params.get("KeyFile") is not None:
            self._KeyFile = KeyFile()
            self._KeyFile._deserialize(params.get("KeyFile"))
        self._NewTableGroupId = params.get("NewTableGroupId")
        self._NewTableName = params.get("NewTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSnapshotsResponse(AbstractModel):
    r"""ImportSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :type TaskId: str
        :param _ApplicationId: ApplicationId由 AppInstanceId-applicationId 组成，以区分不同集群的申请
        :type ApplicationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ApplicationId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ApplicationId(self):
        r"""ApplicationId由 AppInstanceId-applicationId 组成，以区分不同集群的申请
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

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
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class KafkaInfo(AbstractModel):
    r"""ckafka地址信息

    """

    def __init__(self):
        r"""
        :param _Address: Kafka address
        :type Address: str
        :param _Topic: Kafka topic
        :type Topic: str
        :param _User: kafka username
        :type User: str
        :param _Password: kafka password
        :type Password: str
        :param _Instance: ckafka实例
        :type Instance: str
        :param _IsVpc: 是否走VPC
        :type IsVpc: int
        """
        self._Address = None
        self._Topic = None
        self._User = None
        self._Password = None
        self._Instance = None
        self._IsVpc = None

    @property
    def Address(self):
        r"""Kafka address
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Topic(self):
        r"""Kafka topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def User(self):
        r"""kafka username
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        r"""kafka password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Instance(self):
        r"""ckafka实例
        :rtype: str
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def IsVpc(self):
        r"""是否走VPC
        :rtype: int
        """
        return self._IsVpc

    @IsVpc.setter
    def IsVpc(self, IsVpc):
        self._IsVpc = IsVpc


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Topic = params.get("Topic")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Instance = params.get("Instance")
        self._IsVpc = params.get("IsVpc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyFile(AbstractModel):
    r"""部分key导入快照数据时所需要的key文件

    """

    def __init__(self):
        r"""
        :param _FileName: key文件名称
        :type FileName: str
        :param _FileExtType: key文件扩展名
        :type FileExtType: str
        :param _FileContent: key文件内容
        :type FileContent: str
        :param _FileSize: key文件大小
        :type FileSize: int
        """
        self._FileName = None
        self._FileExtType = None
        self._FileContent = None
        self._FileSize = None

    @property
    def FileName(self):
        r"""key文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileExtType(self):
        r"""key文件扩展名
        :rtype: str
        """
        return self._FileExtType

    @FileExtType.setter
    def FileExtType(self, FileExtType):
        self._FileExtType = FileExtType

    @property
    def FileContent(self):
        r"""key文件内容
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileSize(self):
        r"""key文件大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileExtType = params.get("FileExtType")
        self._FileContent = params.get("FileContent")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineInfo(AbstractModel):
    r"""机器类型和数量

    """

    def __init__(self):
        r"""
        :param _MachineType: 机器类型
        :type MachineType: str
        :param _MachineNum: 机器数量
        :type MachineNum: int
        """
        self._MachineType = None
        self._MachineNum = None

    @property
    def MachineType(self):
        r"""机器类型
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineNum(self):
        r"""机器数量
        :rtype: int
        """
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTableResult(AbstractModel):
    r"""合服结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _Error: 成功时此字段返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _Table: 对比的表格信息
        :type Table: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`
        :param _ApplicationId: 申请单Id
        :type ApplicationId: str
        """
        self._TaskId = None
        self._Error = None
        self._Table = None
        self._ApplicationId = None

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Error(self):
        r"""成功时此字段返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def Table(self):
        r"""对比的表格信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def ApplicationId(self):
        r"""申请单Id
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        if params.get("Table") is not None:
            self._Table = CompareTablesInfo()
            self._Table._deserialize(params.get("Table"))
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTablesDataRequest(AbstractModel):
    r"""MergeTablesData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SelectedTables: 选取的表格
        :type SelectedTables: list of MergeTablesInfo
        :param _IsOnlyCompare: true只做对比，false既对比又执行
        :type IsOnlyCompare: bool
        """
        self._SelectedTables = None
        self._IsOnlyCompare = None

    @property
    def SelectedTables(self):
        r"""选取的表格
        :rtype: list of MergeTablesInfo
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def IsOnlyCompare(self):
        r"""true只做对比，false既对比又执行
        :rtype: bool
        """
        return self._IsOnlyCompare

    @IsOnlyCompare.setter
    def IsOnlyCompare(self, IsOnlyCompare):
        self._IsOnlyCompare = IsOnlyCompare


    def _deserialize(self, params):
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = MergeTablesInfo()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        self._IsOnlyCompare = params.get("IsOnlyCompare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTablesDataResponse(AbstractModel):
    r"""MergeTablesData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 合服结果集
        :type Results: list of MergeTableResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        r"""合服结果集
        :rtype: list of MergeTableResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

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
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = MergeTableResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class MergeTablesInfo(AbstractModel):
    r"""合服请求入参

    """

    def __init__(self):
        r"""
        :param _MergeTables: 合服的表格信息
        :type MergeTables: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`
        :param _CheckIndex: 是否检查索引
        :type CheckIndex: bool
        """
        self._MergeTables = None
        self._CheckIndex = None

    @property
    def MergeTables(self):
        r"""合服的表格信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`
        """
        return self._MergeTables

    @MergeTables.setter
    def MergeTables(self, MergeTables):
        self._MergeTables = MergeTables

    @property
    def CheckIndex(self):
        r"""是否检查索引
        :rtype: bool
        """
        return self._CheckIndex

    @CheckIndex.setter
    def CheckIndex(self, CheckIndex):
        self._CheckIndex = CheckIndex


    def _deserialize(self, params):
        if params.get("MergeTables") is not None:
            self._MergeTables = CompareTablesInfo()
            self._MergeTables._deserialize(params.get("MergeTables"))
        self._CheckIndex = params.get("CheckIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCensorshipRequest(AbstractModel):
    r"""ModifyCensorship请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Censorship: 集群是否开启审核 0-关闭 1-开启
        :type Censorship: int
        :param _Uins: 审批人uin列表
        :type Uins: list of str
        """
        self._ClusterId = None
        self._Censorship = None
        self._Uins = None

    @property
    def ClusterId(self):
        r"""集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Censorship(self):
        r"""集群是否开启审核 0-关闭 1-开启
        :rtype: int
        """
        return self._Censorship

    @Censorship.setter
    def Censorship(self, Censorship):
        self._Censorship = Censorship

    @property
    def Uins(self):
        r"""审批人uin列表
        :rtype: list of str
        """
        return self._Uins

    @Uins.setter
    def Uins(self, Uins):
        self._Uins = Uins


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Censorship = params.get("Censorship")
        self._Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCensorshipResponse(AbstractModel):
    r"""ModifyCensorship返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Uins: 已加入审批人的uin
        :type Uins: list of str
        :param _Censorship: 集群是否开启审核 0-关闭 1-开启
        :type Censorship: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._Uins = None
        self._Censorship = None
        self._RequestId = None

    @property
    def ClusterId(self):
        r"""集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Uins(self):
        r"""已加入审批人的uin
        :rtype: list of str
        """
        return self._Uins

    @Uins.setter
    def Uins(self, Uins):
        self._Uins = Uins

    @property
    def Censorship(self):
        r"""集群是否开启审核 0-关闭 1-开启
        :rtype: int
        """
        return self._Censorship

    @Censorship.setter
    def Censorship(self, Censorship):
        self._Censorship = Censorship

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
        self._ClusterId = params.get("ClusterId")
        self._Uins = params.get("Uins")
        self._Censorship = params.get("Censorship")
        self._RequestId = params.get("RequestId")


class ModifyClusterMachineRequest(AbstractModel):
    r"""ModifyClusterMachine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ServerList: svr占用的机器
        :type ServerList: list of MachineInfo
        :param _ProxyList: proxy占用的机器
        :type ProxyList: list of MachineInfo
        :param _ClusterType: 集群类型1共享集群2独占集群
        :type ClusterType: int
        """
        self._ClusterId = None
        self._ServerList = None
        self._ProxyList = None
        self._ClusterType = None

    @property
    def ClusterId(self):
        r"""集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServerList(self):
        r"""svr占用的机器
        :rtype: list of MachineInfo
        """
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def ProxyList(self):
        r"""proxy占用的机器
        :rtype: list of MachineInfo
        """
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList

    @property
    def ClusterType(self):
        r"""集群类型1共享集群2独占集群
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        self._ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterMachineResponse(AbstractModel):
    r"""ModifyClusterMachine返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        r"""集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class ModifyClusterNameRequest(AbstractModel):
    r"""ModifyClusterName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 需要修改名称的集群ID
        :type ClusterId: str
        :param _ClusterName: 需要修改的集群名称，可使用中文或英文字符，最大长度32个字符
        :type ClusterName: str
        """
        self._ClusterId = None
        self._ClusterName = None

    @property
    def ClusterId(self):
        r"""需要修改名称的集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""需要修改的集群名称，可使用中文或英文字符，最大长度32个字符
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    r"""ModifyClusterName返回参数结构体

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


class ModifyClusterPasswordRequest(AbstractModel):
    r"""ModifyClusterPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 需要修改密码的集群ID
        :type ClusterId: str
        :param _OldPassword: 集群旧密码
        :type OldPassword: str
        :param _OldPasswordExpireTime: 集群旧密码预期失效时间
        :type OldPasswordExpireTime: str
        :param _NewPassword: 集群新密码，密码必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母
        :type NewPassword: str
        :param _Mode: 更新模式： `1` 更新密码；`2` 更新旧密码失效时间，默认为`1` 模式
        :type Mode: str
        """
        self._ClusterId = None
        self._OldPassword = None
        self._OldPasswordExpireTime = None
        self._NewPassword = None
        self._Mode = None

    @property
    def ClusterId(self):
        r"""需要修改密码的集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def OldPassword(self):
        r"""集群旧密码
        :rtype: str
        """
        return self._OldPassword

    @OldPassword.setter
    def OldPassword(self, OldPassword):
        self._OldPassword = OldPassword

    @property
    def OldPasswordExpireTime(self):
        r"""集群旧密码预期失效时间
        :rtype: str
        """
        return self._OldPasswordExpireTime

    @OldPasswordExpireTime.setter
    def OldPasswordExpireTime(self, OldPasswordExpireTime):
        self._OldPasswordExpireTime = OldPasswordExpireTime

    @property
    def NewPassword(self):
        r"""集群新密码，密码必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母
        :rtype: str
        """
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword

    @property
    def Mode(self):
        r"""更新模式： `1` 更新密码；`2` 更新旧密码失效时间，默认为`1` 模式
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._OldPassword = params.get("OldPassword")
        self._OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self._NewPassword = params.get("NewPassword")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterPasswordResponse(AbstractModel):
    r"""ModifyClusterPassword返回参数结构体

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


class ModifyClusterTagsRequest(AbstractModel):
    r"""ModifyClusterTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待修改标签的集群ID
        :type ClusterId: str
        :param _ReplaceTags: 待增加或修改的标签列表
        :type ReplaceTags: list of TagInfoUnit
        :param _DeleteTags: 待删除的标签
        :type DeleteTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def ClusterId(self):
        r"""待修改标签的集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ReplaceTags(self):
        r"""待增加或修改的标签列表
        :rtype: list of TagInfoUnit
        """
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        r"""待删除的标签
        :rtype: list of TagInfoUnit
        """
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterTagsResponse(AbstractModel):
    r"""ModifyClusterTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
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


class ModifySnapshotsRequest(AbstractModel):
    r"""ModifySnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格所属集群id
        :type ClusterId: str
        :param _SelectedTables: 快照列表
        :type SelectedTables: list of SnapshotInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表格所属集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""快照列表
        :rtype: list of SnapshotInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotsResponse(AbstractModel):
    r"""ModifySnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 批量修改的快照数量
        :type TotalCount: int
        :param _TableResults: 批量修改的快照结果列表
        :type TableResults: list of SnapshotResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""批量修改的快照数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""批量修改的快照结果列表
        :rtype: list of SnapshotResult
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyTableGroupNameRequest(AbstractModel):
    r"""ModifyTableGroupName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表格组所属的集群ID
        :type ClusterId: str
        :param _TableGroupId: 待修改名称的表格组ID
        :type TableGroupId: str
        :param _TableGroupName: 新的表格组名称，可以使用中英文字符和符号
        :type TableGroupName: str
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._TableGroupName = None

    @property
    def ClusterId(self):
        r"""表格组所属的集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        r"""待修改名称的表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableGroupName(self):
        r"""新的表格组名称，可以使用中英文字符和符号
        :rtype: str
        """
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        self._TableGroupName = params.get("TableGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableGroupNameResponse(AbstractModel):
    r"""ModifyTableGroupName返回参数结构体

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


class ModifyTableGroupTagsRequest(AbstractModel):
    r"""ModifyTableGroupTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待修改标签表格组所属集群ID
        :type ClusterId: str
        :param _TableGroupId: 待修改标签表格组ID
        :type TableGroupId: str
        :param _ReplaceTags: 待增加或修改的标签列表
        :type ReplaceTags: list of TagInfoUnit
        :param _DeleteTags: 待删除的标签
        :type DeleteTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def ClusterId(self):
        r"""待修改标签表格组所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        r"""待修改标签表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def ReplaceTags(self):
        r"""待增加或修改的标签列表
        :rtype: list of TagInfoUnit
        """
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        r"""待删除的标签
        :rtype: list of TagInfoUnit
        """
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableGroupTagsResponse(AbstractModel):
    r"""ModifyTableGroupTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
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


class ModifyTableMemosRequest(AbstractModel):
    r"""ModifyTableMemos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表所属集群实例ID
        :type ClusterId: str
        :param _TableMemos: 选定表详情列表
        :type TableMemos: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._TableMemos = None

    @property
    def ClusterId(self):
        r"""表所属集群实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableMemos(self):
        r"""选定表详情列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._TableMemos

    @TableMemos.setter
    def TableMemos(self, TableMemos):
        self._TableMemos = TableMemos


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("TableMemos") is not None:
            self._TableMemos = []
            for item in params.get("TableMemos"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._TableMemos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableMemosResponse(AbstractModel):
    r"""ModifyTableMemos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表备注修改结果数量
        :type TotalCount: int
        :param _TableResults: 表备注修改结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""表备注修改结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""表备注修改结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyTableQuotasRequest(AbstractModel):
    r"""ModifyTableQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 带扩缩容表所属集群ID
        :type ClusterId: str
        :param _TableQuotas: 已选中待修改的表配额列表
        :type TableQuotas: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._TableQuotas = None

    @property
    def ClusterId(self):
        r"""带扩缩容表所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableQuotas(self):
        r"""已选中待修改的表配额列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._TableQuotas

    @TableQuotas.setter
    def TableQuotas(self, TableQuotas):
        self._TableQuotas = TableQuotas


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("TableQuotas") is not None:
            self._TableQuotas = []
            for item in params.get("TableQuotas"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._TableQuotas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableQuotasResponse(AbstractModel):
    r"""ModifyTableQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 扩缩容结果数量
        :type TotalCount: int
        :param _TableResults: 扩缩容结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""扩缩容结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""扩缩容结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyTableTagsRequest(AbstractModel):
    r"""ModifyTableTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待修改标签表格所属集群ID
        :type ClusterId: str
        :param _SelectedTables: 待修改标签表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param _ReplaceTags: 待增加或修改的标签列表
        :type ReplaceTags: list of TagInfoUnit
        :param _DeleteTags: 待删除的标签列表
        :type DeleteTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._SelectedTables = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def ClusterId(self):
        r"""待修改标签表格所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待修改标签表格列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def ReplaceTags(self):
        r"""待增加或修改的标签列表
        :rtype: list of TagInfoUnit
        """
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        r"""待删除的标签列表
        :rtype: list of TagInfoUnit
        """
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableTagsResponse(AbstractModel):
    r"""ModifyTableTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回结果总数
        :type TotalCount: int
        :param _TableResults: 返回结果
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""返回结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""返回结果
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyTablesRequest(AbstractModel):
    r"""ModifyTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待修改表格所在集群ID
        :type ClusterId: str
        :param _IdlFiles: 选中的改表IDL文件
        :type IdlFiles: list of IdlFileInfo
        :param _SelectedTables: 待改表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._IdlFiles = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""待修改表格所在集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IdlFiles(self):
        r"""选中的改表IDL文件
        :rtype: list of IdlFileInfo
        """
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def SelectedTables(self):
        r"""待改表格列表
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTablesResponse(AbstractModel):
    r"""ModifyTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 修改表结果数量
        :type TotalCount: int
        :param _TableResults: 修改表结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""修改表结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""修改表结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ParsedTableInfoNew(AbstractModel):
    r"""从IDL表描述文件中解析出来的表信息

    """

    def __init__(self):
        r"""
        :param _TableIdlType: 表格描述语言类型：`PROTO`或`TDR`
        :type TableIdlType: str
        :param _TableInstanceId: 表格实例ID
        :type TableInstanceId: str
        :param _TableName: 表格名称
        :type TableName: str
        :param _TableType: 表格数据结构类型：`GENERIC`或`LIST`
        :type TableType: str
        :param _KeyFields: 主键字段信息
        :type KeyFields: str
        :param _OldKeyFields: 原主键字段信息，改表校验时有效
        :type OldKeyFields: str
        :param _ValueFields: 非主键字段信息
        :type ValueFields: str
        :param _OldValueFields: 原非主键字段信息，改表校验时有效
        :type OldValueFields: str
        :param _TableGroupId: 所属表格组ID
        :type TableGroupId: str
        :param _SumKeyFieldSize: 主键字段总大小
        :type SumKeyFieldSize: int
        :param _SumValueFieldSize: 非主键字段总大小
        :type SumValueFieldSize: int
        :param _IndexKeySet: 索引键集合
        :type IndexKeySet: str
        :param _ShardingKeySet: 分表因子集合
        :type ShardingKeySet: str
        :param _TdrVersion: TDR版本号
        :type TdrVersion: int
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _ListElementNum: LIST类型表格元素个数
        :type ListElementNum: int
        :param _SortFieldNum: SORTLIST类型表格排序字段个数
        :type SortFieldNum: int
        :param _SortRule: SORTLIST类型表格排序顺序
        :type SortRule: int
        """
        self._TableIdlType = None
        self._TableInstanceId = None
        self._TableName = None
        self._TableType = None
        self._KeyFields = None
        self._OldKeyFields = None
        self._ValueFields = None
        self._OldValueFields = None
        self._TableGroupId = None
        self._SumKeyFieldSize = None
        self._SumValueFieldSize = None
        self._IndexKeySet = None
        self._ShardingKeySet = None
        self._TdrVersion = None
        self._Error = None
        self._ListElementNum = None
        self._SortFieldNum = None
        self._SortRule = None

    @property
    def TableIdlType(self):
        r"""表格描述语言类型：`PROTO`或`TDR`
        :rtype: str
        """
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableInstanceId(self):
        r"""表格实例ID
        :rtype: str
        """
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableType(self):
        r"""表格数据结构类型：`GENERIC`或`LIST`
        :rtype: str
        """
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def KeyFields(self):
        r"""主键字段信息
        :rtype: str
        """
        return self._KeyFields

    @KeyFields.setter
    def KeyFields(self, KeyFields):
        self._KeyFields = KeyFields

    @property
    def OldKeyFields(self):
        r"""原主键字段信息，改表校验时有效
        :rtype: str
        """
        return self._OldKeyFields

    @OldKeyFields.setter
    def OldKeyFields(self, OldKeyFields):
        self._OldKeyFields = OldKeyFields

    @property
    def ValueFields(self):
        r"""非主键字段信息
        :rtype: str
        """
        return self._ValueFields

    @ValueFields.setter
    def ValueFields(self, ValueFields):
        self._ValueFields = ValueFields

    @property
    def OldValueFields(self):
        r"""原非主键字段信息，改表校验时有效
        :rtype: str
        """
        return self._OldValueFields

    @OldValueFields.setter
    def OldValueFields(self, OldValueFields):
        self._OldValueFields = OldValueFields

    @property
    def TableGroupId(self):
        r"""所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def SumKeyFieldSize(self):
        r"""主键字段总大小
        :rtype: int
        """
        return self._SumKeyFieldSize

    @SumKeyFieldSize.setter
    def SumKeyFieldSize(self, SumKeyFieldSize):
        self._SumKeyFieldSize = SumKeyFieldSize

    @property
    def SumValueFieldSize(self):
        r"""非主键字段总大小
        :rtype: int
        """
        return self._SumValueFieldSize

    @SumValueFieldSize.setter
    def SumValueFieldSize(self, SumValueFieldSize):
        self._SumValueFieldSize = SumValueFieldSize

    @property
    def IndexKeySet(self):
        r"""索引键集合
        :rtype: str
        """
        return self._IndexKeySet

    @IndexKeySet.setter
    def IndexKeySet(self, IndexKeySet):
        self._IndexKeySet = IndexKeySet

    @property
    def ShardingKeySet(self):
        r"""分表因子集合
        :rtype: str
        """
        return self._ShardingKeySet

    @ShardingKeySet.setter
    def ShardingKeySet(self, ShardingKeySet):
        self._ShardingKeySet = ShardingKeySet

    @property
    def TdrVersion(self):
        r"""TDR版本号
        :rtype: int
        """
        return self._TdrVersion

    @TdrVersion.setter
    def TdrVersion(self, TdrVersion):
        self._TdrVersion = TdrVersion

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def ListElementNum(self):
        r"""LIST类型表格元素个数
        :rtype: int
        """
        return self._ListElementNum

    @ListElementNum.setter
    def ListElementNum(self, ListElementNum):
        self._ListElementNum = ListElementNum

    @property
    def SortFieldNum(self):
        r"""SORTLIST类型表格排序字段个数
        :rtype: int
        """
        return self._SortFieldNum

    @SortFieldNum.setter
    def SortFieldNum(self, SortFieldNum):
        self._SortFieldNum = SortFieldNum

    @property
    def SortRule(self):
        r"""SORTLIST类型表格排序顺序
        :rtype: int
        """
        return self._SortRule

    @SortRule.setter
    def SortRule(self, SortRule):
        self._SortRule = SortRule


    def _deserialize(self, params):
        self._TableIdlType = params.get("TableIdlType")
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableName = params.get("TableName")
        self._TableType = params.get("TableType")
        self._KeyFields = params.get("KeyFields")
        self._OldKeyFields = params.get("OldKeyFields")
        self._ValueFields = params.get("ValueFields")
        self._OldValueFields = params.get("OldValueFields")
        self._TableGroupId = params.get("TableGroupId")
        self._SumKeyFieldSize = params.get("SumKeyFieldSize")
        self._SumValueFieldSize = params.get("SumValueFieldSize")
        self._IndexKeySet = params.get("IndexKeySet")
        self._ShardingKeySet = params.get("ShardingKeySet")
        self._TdrVersion = params.get("TdrVersion")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._ListElementNum = params.get("ListElementNum")
        self._SortFieldNum = params.get("SortFieldNum")
        self._SortRule = params.get("SortRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoolInfo(AbstractModel):
    r"""center资源池中的机器信息

    """

    def __init__(self):
        r"""
        :param _PoolUid: 唯一id
        :type PoolUid: int
        :param _Ipv6Enable: 是否支持ipv6
        :type Ipv6Enable: int
        :param _AvailableAppCount: 剩余可用app
        :type AvailableAppCount: int
        :param _ServerList: svr机器列表
        :type ServerList: list of ServerMachineInfo
        :param _ProxyList: proxy机器列表
        :type ProxyList: list of ProxyMachineInfo
        """
        self._PoolUid = None
        self._Ipv6Enable = None
        self._AvailableAppCount = None
        self._ServerList = None
        self._ProxyList = None

    @property
    def PoolUid(self):
        r"""唯一id
        :rtype: int
        """
        return self._PoolUid

    @PoolUid.setter
    def PoolUid(self, PoolUid):
        self._PoolUid = PoolUid

    @property
    def Ipv6Enable(self):
        r"""是否支持ipv6
        :rtype: int
        """
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable

    @property
    def AvailableAppCount(self):
        r"""剩余可用app
        :rtype: int
        """
        return self._AvailableAppCount

    @AvailableAppCount.setter
    def AvailableAppCount(self, AvailableAppCount):
        self._AvailableAppCount = AvailableAppCount

    @property
    def ServerList(self):
        r"""svr机器列表
        :rtype: list of ServerMachineInfo
        """
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def ProxyList(self):
        r"""proxy机器列表
        :rtype: list of ProxyMachineInfo
        """
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList


    def _deserialize(self, params):
        self._PoolUid = params.get("PoolUid")
        self._Ipv6Enable = params.get("Ipv6Enable")
        self._AvailableAppCount = params.get("AvailableAppCount")
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = ServerMachineInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyMachineInfo()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyDetailInfo(AbstractModel):
    r"""独占的proxy详细信息

    """

    def __init__(self):
        r"""
        :param _ProxyUid: proxy的唯一id
        :type ProxyUid: str
        :param _MachineType: 机器类型
        :type MachineType: str
        :param _ProcessSpeed: 请求包速度
        :type ProcessSpeed: int
        :param _AverageProcessDelay: 请求包时延
        :type AverageProcessDelay: int
        :param _SlowProcessSpeed: 慢处理包速度
        :type SlowProcessSpeed: int
        :param _Version: 版本
        :type Version: str
        """
        self._ProxyUid = None
        self._MachineType = None
        self._ProcessSpeed = None
        self._AverageProcessDelay = None
        self._SlowProcessSpeed = None
        self._Version = None

    @property
    def ProxyUid(self):
        r"""proxy的唯一id
        :rtype: str
        """
        return self._ProxyUid

    @ProxyUid.setter
    def ProxyUid(self, ProxyUid):
        self._ProxyUid = ProxyUid

    @property
    def MachineType(self):
        r"""机器类型
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def ProcessSpeed(self):
        r"""请求包速度
        :rtype: int
        """
        return self._ProcessSpeed

    @ProcessSpeed.setter
    def ProcessSpeed(self, ProcessSpeed):
        self._ProcessSpeed = ProcessSpeed

    @property
    def AverageProcessDelay(self):
        r"""请求包时延
        :rtype: int
        """
        return self._AverageProcessDelay

    @AverageProcessDelay.setter
    def AverageProcessDelay(self, AverageProcessDelay):
        self._AverageProcessDelay = AverageProcessDelay

    @property
    def SlowProcessSpeed(self):
        r"""慢处理包速度
        :rtype: int
        """
        return self._SlowProcessSpeed

    @SlowProcessSpeed.setter
    def SlowProcessSpeed(self, SlowProcessSpeed):
        self._SlowProcessSpeed = SlowProcessSpeed

    @property
    def Version(self):
        r"""版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._ProxyUid = params.get("ProxyUid")
        self._MachineType = params.get("MachineType")
        self._ProcessSpeed = params.get("ProcessSpeed")
        self._AverageProcessDelay = params.get("AverageProcessDelay")
        self._SlowProcessSpeed = params.get("SlowProcessSpeed")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyMachineInfo(AbstractModel):
    r"""proxy机器信息

    """

    def __init__(self):
        r"""
        :param _ProxyUid: 唯一id
        :type ProxyUid: str
        :param _MachineType: 机器类型
        :type MachineType: str
        :param _AvailableCount: 可分配proxy资源数
        :type AvailableCount: int
        """
        self._ProxyUid = None
        self._MachineType = None
        self._AvailableCount = None

    @property
    def ProxyUid(self):
        r"""唯一id
        :rtype: str
        """
        return self._ProxyUid

    @ProxyUid.setter
    def ProxyUid(self, ProxyUid):
        self._ProxyUid = ProxyUid

    @property
    def MachineType(self):
        r"""机器类型
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def AvailableCount(self):
        r"""可分配proxy资源数
        :rtype: int
        """
        return self._AvailableCount

    @AvailableCount.setter
    def AvailableCount(self, AvailableCount):
        self._AvailableCount = AvailableCount


    def _deserialize(self, params):
        self._ProxyUid = params.get("ProxyUid")
        self._MachineType = params.get("MachineType")
        self._AvailableCount = params.get("AvailableCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverRecycleTablesRequest(AbstractModel):
    r"""RecoverRecycleTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表所在集群ID
        :type ClusterId: str
        :param _SelectedTables: 待恢复表信息
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表所在集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待恢复表信息
        :rtype: list of SelectedTableInfoNew
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverRecycleTablesResponse(AbstractModel):
    r"""RecoverRecycleTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 恢复表结果数量
        :type TotalCount: int
        :param _TableResults: 恢复表信息列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""恢复表结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""恢复表信息列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    r"""TcaplusDB服务地域信息详情

    """

    def __init__(self):
        r"""
        :param _RegionName: 地域Ap-Code
        :type RegionName: str
        :param _RegionAbbr: 地域缩写
        :type RegionAbbr: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _Ipv6Enable: 是否支持ipv6，0:不支持，1:支持
        :type Ipv6Enable: int
        """
        self._RegionName = None
        self._RegionAbbr = None
        self._RegionId = None
        self._Ipv6Enable = None

    @property
    def RegionName(self):
        r"""地域Ap-Code
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionAbbr(self):
        r"""地域缩写
        :rtype: str
        """
        return self._RegionAbbr

    @RegionAbbr.setter
    def RegionAbbr(self, RegionAbbr):
        self._RegionAbbr = RegionAbbr

    @property
    def RegionId(self):
        r"""地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Ipv6Enable(self):
        r"""是否支持ipv6，0:不支持，1:支持
        :rtype: int
        """
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable


    def _deserialize(self, params):
        self._RegionName = params.get("RegionName")
        self._RegionAbbr = params.get("RegionAbbr")
        self._RegionId = params.get("RegionId")
        self._Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedTableInfoNew(AbstractModel):
    r"""被选中的表信息

    """

    def __init__(self):
        r"""
        :param _TableGroupId: 表所属表格组ID
        :type TableGroupId: str
        :param _TableName: 表格名称
        :type TableName: str
        :param _TableInstanceId: 表实例ID
        :type TableInstanceId: str
        :param _TableIdlType: 表格描述语言类型：`PROTO`或`TDR`
        :type TableIdlType: str
        :param _TableType: 表格数据结构类型：`GENERIC`或`LIST`
        :type TableType: str
        :param _ListElementNum: LIST表元素个数
        :type ListElementNum: int
        :param _ReservedVolume: 表格预留容量（GB）
        :type ReservedVolume: int
        :param _ReservedReadQps: 表格预留读CU
        :type ReservedReadQps: int
        :param _ReservedWriteQps: 表格预留写CU
        :type ReservedWriteQps: int
        :param _Memo: 表格备注信息
        :type Memo: str
        :param _FileName: Key回档文件名，回档专用
        :type FileName: str
        :param _FileExtType: Key回档文件扩展名，回档专用
        :type FileExtType: str
        :param _FileSize: Key回档文件大小，回档专用
        :type FileSize: int
        :param _FileContent: Key回档文件内容，回档专用
        :type FileContent: str
        """
        self._TableGroupId = None
        self._TableName = None
        self._TableInstanceId = None
        self._TableIdlType = None
        self._TableType = None
        self._ListElementNum = None
        self._ReservedVolume = None
        self._ReservedReadQps = None
        self._ReservedWriteQps = None
        self._Memo = None
        self._FileName = None
        self._FileExtType = None
        self._FileSize = None
        self._FileContent = None

    @property
    def TableGroupId(self):
        r"""表所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableInstanceId(self):
        r"""表实例ID
        :rtype: str
        """
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableIdlType(self):
        r"""表格描述语言类型：`PROTO`或`TDR`
        :rtype: str
        """
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableType(self):
        r"""表格数据结构类型：`GENERIC`或`LIST`
        :rtype: str
        """
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def ListElementNum(self):
        r"""LIST表元素个数
        :rtype: int
        """
        return self._ListElementNum

    @ListElementNum.setter
    def ListElementNum(self, ListElementNum):
        self._ListElementNum = ListElementNum

    @property
    def ReservedVolume(self):
        r"""表格预留容量（GB）
        :rtype: int
        """
        return self._ReservedVolume

    @ReservedVolume.setter
    def ReservedVolume(self, ReservedVolume):
        self._ReservedVolume = ReservedVolume

    @property
    def ReservedReadQps(self):
        r"""表格预留读CU
        :rtype: int
        """
        return self._ReservedReadQps

    @ReservedReadQps.setter
    def ReservedReadQps(self, ReservedReadQps):
        self._ReservedReadQps = ReservedReadQps

    @property
    def ReservedWriteQps(self):
        r"""表格预留写CU
        :rtype: int
        """
        return self._ReservedWriteQps

    @ReservedWriteQps.setter
    def ReservedWriteQps(self, ReservedWriteQps):
        self._ReservedWriteQps = ReservedWriteQps

    @property
    def Memo(self):
        r"""表格备注信息
        :rtype: str
        """
        return self._Memo

    @Memo.setter
    def Memo(self, Memo):
        self._Memo = Memo

    @property
    def FileName(self):
        r"""Key回档文件名，回档专用
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileExtType(self):
        r"""Key回档文件扩展名，回档专用
        :rtype: str
        """
        return self._FileExtType

    @FileExtType.setter
    def FileExtType(self, FileExtType):
        self._FileExtType = FileExtType

    @property
    def FileSize(self):
        r"""Key回档文件大小，回档专用
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileContent(self):
        r"""Key回档文件内容，回档专用
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableIdlType = params.get("TableIdlType")
        self._TableType = params.get("TableType")
        self._ListElementNum = params.get("ListElementNum")
        self._ReservedVolume = params.get("ReservedVolume")
        self._ReservedReadQps = params.get("ReservedReadQps")
        self._ReservedWriteQps = params.get("ReservedWriteQps")
        self._Memo = params.get("Memo")
        self._FileName = params.get("FileName")
        self._FileExtType = params.get("FileExtType")
        self._FileSize = params.get("FileSize")
        self._FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedTableWithField(AbstractModel):
    r"""附带被选中字段信息的表格列表

    """

    def __init__(self):
        r"""
        :param _TableGroupId: 表所属表格组ID
        :type TableGroupId: str
        :param _TableName: 表格名称
        :type TableName: str
        :param _TableInstanceId: 表实例ID
        :type TableInstanceId: str
        :param _TableIdlType: 表格描述语言类型：`PROTO`或`TDR`
        :type TableIdlType: str
        :param _TableType: 表格数据结构类型：`GENERIC`或`LIST`
        :type TableType: str
        :param _SelectedFields: 待创建索引、缓写、数据订阅的字段列表
        :type SelectedFields: list of FieldInfo
        :param _ShardNum: 索引分片数
        :type ShardNum: int
        :param _KafkaInfo: ckafka实例信息
        :type KafkaInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.KafkaInfo`
        """
        self._TableGroupId = None
        self._TableName = None
        self._TableInstanceId = None
        self._TableIdlType = None
        self._TableType = None
        self._SelectedFields = None
        self._ShardNum = None
        self._KafkaInfo = None

    @property
    def TableGroupId(self):
        r"""表所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableInstanceId(self):
        r"""表实例ID
        :rtype: str
        """
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableIdlType(self):
        r"""表格描述语言类型：`PROTO`或`TDR`
        :rtype: str
        """
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableType(self):
        r"""表格数据结构类型：`GENERIC`或`LIST`
        :rtype: str
        """
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def SelectedFields(self):
        r"""待创建索引、缓写、数据订阅的字段列表
        :rtype: list of FieldInfo
        """
        return self._SelectedFields

    @SelectedFields.setter
    def SelectedFields(self, SelectedFields):
        self._SelectedFields = SelectedFields

    @property
    def ShardNum(self):
        r"""索引分片数
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def KafkaInfo(self):
        r"""ckafka实例信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.KafkaInfo`
        """
        return self._KafkaInfo

    @KafkaInfo.setter
    def KafkaInfo(self, KafkaInfo):
        self._KafkaInfo = KafkaInfo


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableIdlType = params.get("TableIdlType")
        self._TableType = params.get("TableType")
        if params.get("SelectedFields") is not None:
            self._SelectedFields = []
            for item in params.get("SelectedFields"):
                obj = FieldInfo()
                obj._deserialize(item)
                self._SelectedFields.append(obj)
        self._ShardNum = params.get("ShardNum")
        if params.get("KafkaInfo") is not None:
            self._KafkaInfo = KafkaInfo()
            self._KafkaInfo._deserialize(params.get("KafkaInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerDetailInfo(AbstractModel):
    r"""server独占机器的详细信息

    """

    def __init__(self):
        r"""
        :param _ServerUid: svr唯一id
        :type ServerUid: str
        :param _MachineType: 机器类型
        :type MachineType: str
        :param _MemoryRate: 内存占用量
        :type MemoryRate: int
        :param _DiskRate: 磁盘占用量
        :type DiskRate: int
        :param _ReadNum: 读次数
        :type ReadNum: int
        :param _WriteNum: 写次数
        :type WriteNum: int
        :param _Version: 版本
        :type Version: str
        """
        self._ServerUid = None
        self._MachineType = None
        self._MemoryRate = None
        self._DiskRate = None
        self._ReadNum = None
        self._WriteNum = None
        self._Version = None

    @property
    def ServerUid(self):
        r"""svr唯一id
        :rtype: str
        """
        return self._ServerUid

    @ServerUid.setter
    def ServerUid(self, ServerUid):
        self._ServerUid = ServerUid

    @property
    def MachineType(self):
        r"""机器类型
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MemoryRate(self):
        r"""内存占用量
        :rtype: int
        """
        return self._MemoryRate

    @MemoryRate.setter
    def MemoryRate(self, MemoryRate):
        self._MemoryRate = MemoryRate

    @property
    def DiskRate(self):
        r"""磁盘占用量
        :rtype: int
        """
        return self._DiskRate

    @DiskRate.setter
    def DiskRate(self, DiskRate):
        self._DiskRate = DiskRate

    @property
    def ReadNum(self):
        r"""读次数
        :rtype: int
        """
        return self._ReadNum

    @ReadNum.setter
    def ReadNum(self, ReadNum):
        self._ReadNum = ReadNum

    @property
    def WriteNum(self):
        r"""写次数
        :rtype: int
        """
        return self._WriteNum

    @WriteNum.setter
    def WriteNum(self, WriteNum):
        self._WriteNum = WriteNum

    @property
    def Version(self):
        r"""版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._ServerUid = params.get("ServerUid")
        self._MachineType = params.get("MachineType")
        self._MemoryRate = params.get("MemoryRate")
        self._DiskRate = params.get("DiskRate")
        self._ReadNum = params.get("ReadNum")
        self._WriteNum = params.get("WriteNum")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerMachineInfo(AbstractModel):
    r"""svr的机器列表ServerList

    """

    def __init__(self):
        r"""
        :param _ServerUid: 机器唯一id
        :type ServerUid: str
        :param _MachineType: 机器类型
        :type MachineType: str
        """
        self._ServerUid = None
        self._MachineType = None

    @property
    def ServerUid(self):
        r"""机器唯一id
        :rtype: str
        """
        return self._ServerUid

    @ServerUid.setter
    def ServerUid(self, ServerUid):
        self._ServerUid = ServerUid

    @property
    def MachineType(self):
        r"""机器类型
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._ServerUid = params.get("ServerUid")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetBackupExpireRuleRequest(AbstractModel):
    r"""SetBackupExpireRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表所属集群实例ID
        :type ClusterId: str
        :param _BackupExpireRules: 淘汰策略数组
        :type BackupExpireRules: list of BackupExpireRuleInfo
        """
        self._ClusterId = None
        self._BackupExpireRules = None

    @property
    def ClusterId(self):
        r"""表所属集群实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupExpireRules(self):
        r"""淘汰策略数组
        :rtype: list of BackupExpireRuleInfo
        """
        return self._BackupExpireRules

    @BackupExpireRules.setter
    def BackupExpireRules(self, BackupExpireRules):
        self._BackupExpireRules = BackupExpireRules


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("BackupExpireRules") is not None:
            self._BackupExpireRules = []
            for item in params.get("BackupExpireRules"):
                obj = BackupExpireRuleInfo()
                obj._deserialize(item)
                self._BackupExpireRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetBackupExpireRuleResponse(AbstractModel):
    r"""SetBackupExpireRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
        :rtype: str
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


class SetTableDataFlowRequest(AbstractModel):
    r"""SetTableDataFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表所属集群实例ID
        :type ClusterId: str
        :param _SelectedTables: 待创建分布式索引表格列表
        :type SelectedTables: list of SelectedTableWithField
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表所属集群实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待创建分布式索引表格列表
        :rtype: list of SelectedTableWithField
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableWithField()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableDataFlowResponse(AbstractModel):
    r"""SetTableDataFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表格数据订阅创建结果数量
        :type TotalCount: int
        :param _TableResults: 表格数据订阅创建结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""表格数据订阅创建结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""表格数据订阅创建结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class SetTableIndexRequest(AbstractModel):
    r"""SetTableIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 表所属集群实例ID
        :type ClusterId: str
        :param _SelectedTables: 待创建分布式索引表格列表
        :type SelectedTables: list of SelectedTableWithField
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        r"""表所属集群实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        r"""待创建分布式索引表格列表
        :rtype: list of SelectedTableWithField
        """
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableWithField()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableIndexResponse(AbstractModel):
    r"""SetTableIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表格分布式索引创建结果数量
        :type TotalCount: int
        :param _TableResults: 表格分布式索引创建结果列表
        :type TableResults: list of TableResultNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""表格分布式索引创建结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        r"""表格分布式索引创建结果列表
        :rtype: list of TableResultNew
        """
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

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
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    r"""快照列表

    """

    def __init__(self):
        r"""
        :param _TableGroupId: 所属表格组ID
        :type TableGroupId: str
        :param _TableName: 表名称
        :type TableName: str
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _SnapshotTime: 快照时间点
        :type SnapshotTime: str
        :param _SnapshotDeadTime: 快照过期时间点
        :type SnapshotDeadTime: str
        """
        self._TableGroupId = None
        self._TableName = None
        self._SnapshotName = None
        self._SnapshotTime = None
        self._SnapshotDeadTime = None

    @property
    def TableGroupId(self):
        r"""所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def SnapshotName(self):
        r"""快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotTime(self):
        r"""快照时间点
        :rtype: str
        """
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def SnapshotDeadTime(self):
        r"""快照过期时间点
        :rtype: str
        """
        return self._SnapshotDeadTime

    @SnapshotDeadTime.setter
    def SnapshotDeadTime(self, SnapshotDeadTime):
        self._SnapshotDeadTime = SnapshotDeadTime


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotTime = params.get("SnapshotTime")
        self._SnapshotDeadTime = params.get("SnapshotDeadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotInfoNew(AbstractModel):
    r"""新的快照过期时间

    """

    def __init__(self):
        r"""
        :param _TableGroupId: 所属表格组ID
        :type TableGroupId: str
        :param _TableName: 表名称
        :type TableName: str
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _SnapshotDeadTime: 快照过期时间点
        :type SnapshotDeadTime: str
        """
        self._TableGroupId = None
        self._TableName = None
        self._SnapshotName = None
        self._SnapshotDeadTime = None

    @property
    def TableGroupId(self):
        r"""所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def SnapshotName(self):
        r"""快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotDeadTime(self):
        r"""快照过期时间点
        :rtype: str
        """
        return self._SnapshotDeadTime

    @SnapshotDeadTime.setter
    def SnapshotDeadTime(self, SnapshotDeadTime):
        self._SnapshotDeadTime = SnapshotDeadTime


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotDeadTime = params.get("SnapshotDeadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    r"""创建快照结果

    """

    def __init__(self):
        r"""
        :param _TableGroupId: 表格所属表格组ID
        :type TableGroupId: str
        :param _TableName: 表格名称
        :type TableName: str
        :param _TaskId: 任务ID，对于创建单任务的接口有效
        :type TaskId: str
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _SnapshotTime: 快照的时间点
        :type SnapshotTime: str
        :param _SnapshotDeadTime: 快照的过期时间点
        :type SnapshotDeadTime: str
        :param _SnapshotCreateTime: 快照创建时间点
        :type SnapshotCreateTime: str
        :param _SnapshotSize: 快照大小
        :type SnapshotSize: int
        :param _SnapshotStatus: 快照状态，0 生成中 1 正常 2 删除中 3 已失效 4 回档使用中
        :type SnapshotStatus: int
        :param _ApplicationId: 申请单ID
        :type ApplicationId: str
        """
        self._TableGroupId = None
        self._TableName = None
        self._TaskId = None
        self._Error = None
        self._SnapshotName = None
        self._SnapshotTime = None
        self._SnapshotDeadTime = None
        self._SnapshotCreateTime = None
        self._SnapshotSize = None
        self._SnapshotStatus = None
        self._ApplicationId = None

    @property
    def TableGroupId(self):
        r"""表格所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TaskId(self):
        r"""任务ID，对于创建单任务的接口有效
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def SnapshotName(self):
        r"""快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotTime(self):
        r"""快照的时间点
        :rtype: str
        """
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def SnapshotDeadTime(self):
        r"""快照的过期时间点
        :rtype: str
        """
        return self._SnapshotDeadTime

    @SnapshotDeadTime.setter
    def SnapshotDeadTime(self, SnapshotDeadTime):
        self._SnapshotDeadTime = SnapshotDeadTime

    @property
    def SnapshotCreateTime(self):
        r"""快照创建时间点
        :rtype: str
        """
        return self._SnapshotCreateTime

    @SnapshotCreateTime.setter
    def SnapshotCreateTime(self, SnapshotCreateTime):
        self._SnapshotCreateTime = SnapshotCreateTime

    @property
    def SnapshotSize(self):
        r"""快照大小
        :rtype: int
        """
        return self._SnapshotSize

    @SnapshotSize.setter
    def SnapshotSize(self, SnapshotSize):
        self._SnapshotSize = SnapshotSize

    @property
    def SnapshotStatus(self):
        r"""快照状态，0 生成中 1 正常 2 删除中 3 已失效 4 回档使用中
        :rtype: int
        """
        return self._SnapshotStatus

    @SnapshotStatus.setter
    def SnapshotStatus(self, SnapshotStatus):
        self._SnapshotStatus = SnapshotStatus

    @property
    def ApplicationId(self):
        r"""申请单ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotTime = params.get("SnapshotTime")
        self._SnapshotDeadTime = params.get("SnapshotDeadTime")
        self._SnapshotCreateTime = params.get("SnapshotCreateTime")
        self._SnapshotSize = params.get("SnapshotSize")
        self._SnapshotStatus = params.get("SnapshotStatus")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncTableField(AbstractModel):
    r"""缓写表字段名称的映射

    """

    def __init__(self):
        r"""
        :param _SourceName: TcaplusDB表字段名称
        :type SourceName: str
        :param _TargetName: 目标缓写表的字段名称
        :type TargetName: str
        """
        self._SourceName = None
        self._TargetName = None

    @property
    def SourceName(self):
        r"""TcaplusDB表字段名称
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def TargetName(self):
        r"""目标缓写表的字段名称
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName


    def _deserialize(self, params):
        self._SourceName = params.get("SourceName")
        self._TargetName = params.get("TargetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncTableInfo(AbstractModel):
    r"""TcaplusDB的缓写表信息

    """

    def __init__(self):
        r"""
        :param _TargetTableSplitNum: 目标缓写表的分表数目
        :type TargetTableSplitNum: int
        :param _TargetTableNamePrefix: 目标缓写表名前缀
        :type TargetTableNamePrefix: list of str
        :param _TargetSyncDBInstanceId: 缓写数据库实例ID
        :type TargetSyncDBInstanceId: str
        :param _TargetDatabaseName: 缓写表所在数据库名称
        :type TargetDatabaseName: str
        :param _Status: 缓写状态，0：创建中，1：进行中，2：关闭，-1：被删除
        :type Status: int
        :param _ClusterId: 表格所在集群ID
        :type ClusterId: str
        :param _TableGroupId: 表格所在表格组ID
        :type TableGroupId: int
        :param _TableName: 表格名称
        :type TableName: str
        :param _TableId: 表格ID
        :type TableId: str
        :param _KeyFieldMapping: TcaplusDB表主键字段到目标缓写表字段的映射
        :type KeyFieldMapping: list of SyncTableField
        :param _ValueFieldMapping: TcaplusDB表字段到目标缓写表字段的映射
        :type ValueFieldMapping: list of SyncTableField
        """
        self._TargetTableSplitNum = None
        self._TargetTableNamePrefix = None
        self._TargetSyncDBInstanceId = None
        self._TargetDatabaseName = None
        self._Status = None
        self._ClusterId = None
        self._TableGroupId = None
        self._TableName = None
        self._TableId = None
        self._KeyFieldMapping = None
        self._ValueFieldMapping = None

    @property
    def TargetTableSplitNum(self):
        r"""目标缓写表的分表数目
        :rtype: int
        """
        return self._TargetTableSplitNum

    @TargetTableSplitNum.setter
    def TargetTableSplitNum(self, TargetTableSplitNum):
        self._TargetTableSplitNum = TargetTableSplitNum

    @property
    def TargetTableNamePrefix(self):
        r"""目标缓写表名前缀
        :rtype: list of str
        """
        return self._TargetTableNamePrefix

    @TargetTableNamePrefix.setter
    def TargetTableNamePrefix(self, TargetTableNamePrefix):
        self._TargetTableNamePrefix = TargetTableNamePrefix

    @property
    def TargetSyncDBInstanceId(self):
        r"""缓写数据库实例ID
        :rtype: str
        """
        return self._TargetSyncDBInstanceId

    @TargetSyncDBInstanceId.setter
    def TargetSyncDBInstanceId(self, TargetSyncDBInstanceId):
        self._TargetSyncDBInstanceId = TargetSyncDBInstanceId

    @property
    def TargetDatabaseName(self):
        r"""缓写表所在数据库名称
        :rtype: str
        """
        return self._TargetDatabaseName

    @TargetDatabaseName.setter
    def TargetDatabaseName(self, TargetDatabaseName):
        self._TargetDatabaseName = TargetDatabaseName

    @property
    def Status(self):
        r"""缓写状态，0：创建中，1：进行中，2：关闭，-1：被删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterId(self):
        r"""表格所在集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        r"""表格所在表格组ID
        :rtype: int
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableId(self):
        r"""表格ID
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def KeyFieldMapping(self):
        r"""TcaplusDB表主键字段到目标缓写表字段的映射
        :rtype: list of SyncTableField
        """
        return self._KeyFieldMapping

    @KeyFieldMapping.setter
    def KeyFieldMapping(self, KeyFieldMapping):
        self._KeyFieldMapping = KeyFieldMapping

    @property
    def ValueFieldMapping(self):
        r"""TcaplusDB表字段到目标缓写表字段的映射
        :rtype: list of SyncTableField
        """
        return self._ValueFieldMapping

    @ValueFieldMapping.setter
    def ValueFieldMapping(self, ValueFieldMapping):
        self._ValueFieldMapping = ValueFieldMapping


    def _deserialize(self, params):
        self._TargetTableSplitNum = params.get("TargetTableSplitNum")
        self._TargetTableNamePrefix = params.get("TargetTableNamePrefix")
        self._TargetSyncDBInstanceId = params.get("TargetSyncDBInstanceId")
        self._TargetDatabaseName = params.get("TargetDatabaseName")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._TableId = params.get("TableId")
        if params.get("KeyFieldMapping") is not None:
            self._KeyFieldMapping = []
            for item in params.get("KeyFieldMapping"):
                obj = SyncTableField()
                obj._deserialize(item)
                self._KeyFieldMapping.append(obj)
        if params.get("ValueFieldMapping") is not None:
            self._ValueFieldMapping = []
            for item in params.get("ValueFieldMapping"):
                obj = SyncTableField()
                obj._deserialize(item)
                self._ValueFieldMapping.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableGroupInfo(AbstractModel):
    r"""表格组详细信息

    """

    def __init__(self):
        r"""
        :param _TableGroupId: 表格组ID
        :type TableGroupId: str
        :param _TableGroupName: 表格组名称
        :type TableGroupName: str
        :param _CreatedTime: 表格组创建时间
        :type CreatedTime: str
        :param _TableCount: 表格组包含的表格数量
        :type TableCount: int
        :param _TotalSize: 表格组包含的表格存储总量（MB）
        :type TotalSize: int
        :param _TxhBackupExpireDay: 表格Txh备份文件多少天后过期删除
        :type TxhBackupExpireDay: int
        :param _EnableMysql: 是否开启mysql负载均衡,0未开启 1开启中 2已开启
        :type EnableMysql: int
        :param _MysqlConnIp: mysql负载均衡vip
        :type MysqlConnIp: str
        :param _MysqlConnPort: mysql负载均衡vport
        :type MysqlConnPort: int
        """
        self._TableGroupId = None
        self._TableGroupName = None
        self._CreatedTime = None
        self._TableCount = None
        self._TotalSize = None
        self._TxhBackupExpireDay = None
        self._EnableMysql = None
        self._MysqlConnIp = None
        self._MysqlConnPort = None

    @property
    def TableGroupId(self):
        r"""表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableGroupName(self):
        r"""表格组名称
        :rtype: str
        """
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName

    @property
    def CreatedTime(self):
        r"""表格组创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def TableCount(self):
        r"""表格组包含的表格数量
        :rtype: int
        """
        return self._TableCount

    @TableCount.setter
    def TableCount(self, TableCount):
        self._TableCount = TableCount

    @property
    def TotalSize(self):
        r"""表格组包含的表格存储总量（MB）
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def TxhBackupExpireDay(self):
        r"""表格Txh备份文件多少天后过期删除
        :rtype: int
        """
        return self._TxhBackupExpireDay

    @TxhBackupExpireDay.setter
    def TxhBackupExpireDay(self, TxhBackupExpireDay):
        self._TxhBackupExpireDay = TxhBackupExpireDay

    @property
    def EnableMysql(self):
        r"""是否开启mysql负载均衡,0未开启 1开启中 2已开启
        :rtype: int
        """
        return self._EnableMysql

    @EnableMysql.setter
    def EnableMysql(self, EnableMysql):
        self._EnableMysql = EnableMysql

    @property
    def MysqlConnIp(self):
        r"""mysql负载均衡vip
        :rtype: str
        """
        return self._MysqlConnIp

    @MysqlConnIp.setter
    def MysqlConnIp(self, MysqlConnIp):
        self._MysqlConnIp = MysqlConnIp

    @property
    def MysqlConnPort(self):
        r"""mysql负载均衡vport
        :rtype: int
        """
        return self._MysqlConnPort

    @MysqlConnPort.setter
    def MysqlConnPort(self, MysqlConnPort):
        self._MysqlConnPort = MysqlConnPort


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableGroupName = params.get("TableGroupName")
        self._CreatedTime = params.get("CreatedTime")
        self._TableCount = params.get("TableCount")
        self._TotalSize = params.get("TotalSize")
        self._TxhBackupExpireDay = params.get("TxhBackupExpireDay")
        self._EnableMysql = params.get("EnableMysql")
        self._MysqlConnIp = params.get("MysqlConnIp")
        self._MysqlConnPort = params.get("MysqlConnPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfoNew(AbstractModel):
    r"""表格详情信息

    """

    def __init__(self):
        r"""
        :param _TableName: 表格名称
        :type TableName: str
        :param _TableInstanceId: 表格实例ID
        :type TableInstanceId: str
        :param _TableType: 表格数据结构类型，如：`GENERIC`或`LIST`
        :type TableType: str
        :param _TableIdlType: 表格数据描述语言（IDL）类型，如：`PROTO`或`TDR`
        :type TableIdlType: str
        :param _ClusterId: 表格所属集群ID
        :type ClusterId: str
        :param _ClusterName: 表格所属集群名称
        :type ClusterName: str
        :param _TableGroupId: 表格所属表格组ID
        :type TableGroupId: str
        :param _TableGroupName: 表格所属表格组名称
        :type TableGroupName: str
        :param _KeyStruct: 表格主键字段结构json字符串
        :type KeyStruct: str
        :param _ValueStruct: 表格非主键字段结构json字符串
        :type ValueStruct: str
        :param _ShardingKeySet: 表格分表因子集合，对PROTO类型表格有效
        :type ShardingKeySet: str
        :param _IndexStruct: 表格索引键字段集合，对PROTO类型表格有效
        :type IndexStruct: str
        :param _ListElementNum: LIST类型表格元素个数
        :type ListElementNum: int
        :param _IdlFiles: 表格所关联IDL文件信息列表
        :type IdlFiles: list of IdlFileInfo
        :param _ReservedVolume: 表格预留容量（GB）
        :type ReservedVolume: int
        :param _ReservedReadQps: 表格预留读CU
        :type ReservedReadQps: int
        :param _ReservedWriteQps: 表格预留写CU
        :type ReservedWriteQps: int
        :param _TableSize: 表格实际数据量大小（MB）
        :type TableSize: int
        :param _Status: 表格状态
        :type Status: str
        :param _CreatedTime: 表格创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 表格最后一次修改时间
        :type UpdatedTime: str
        :param _Memo: 表格备注信息
        :type Memo: str
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _ApiAccessId: TcaplusDB SDK数据访问接入ID
        :type ApiAccessId: str
        :param _SortFieldNum: SORTLIST类型表格排序字段个数
        :type SortFieldNum: int
        :param _SortRule: SORTLIST类型表格排序顺序
        :type SortRule: int
        :param _DbClusterInfoStruct: 表格分布式索引/缓写、kafka数据订阅信息
        :type DbClusterInfoStruct: str
        :param _TxhBackupExpireDay: 表格Txh备份文件多少天后过期删除
        :type TxhBackupExpireDay: int
        :param _SyncTableInfo: 表格的缓写信息
        :type SyncTableInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.SyncTableInfo`
        :param _ShardNum: 表格分片数量
        :type ShardNum: int
        """
        self._TableName = None
        self._TableInstanceId = None
        self._TableType = None
        self._TableIdlType = None
        self._ClusterId = None
        self._ClusterName = None
        self._TableGroupId = None
        self._TableGroupName = None
        self._KeyStruct = None
        self._ValueStruct = None
        self._ShardingKeySet = None
        self._IndexStruct = None
        self._ListElementNum = None
        self._IdlFiles = None
        self._ReservedVolume = None
        self._ReservedReadQps = None
        self._ReservedWriteQps = None
        self._TableSize = None
        self._Status = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._Memo = None
        self._Error = None
        self._ApiAccessId = None
        self._SortFieldNum = None
        self._SortRule = None
        self._DbClusterInfoStruct = None
        self._TxhBackupExpireDay = None
        self._SyncTableInfo = None
        self._ShardNum = None

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableInstanceId(self):
        r"""表格实例ID
        :rtype: str
        """
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableType(self):
        r"""表格数据结构类型，如：`GENERIC`或`LIST`
        :rtype: str
        """
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def TableIdlType(self):
        r"""表格数据描述语言（IDL）类型，如：`PROTO`或`TDR`
        :rtype: str
        """
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def ClusterId(self):
        r"""表格所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""表格所属集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TableGroupId(self):
        r"""表格所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableGroupName(self):
        r"""表格所属表格组名称
        :rtype: str
        """
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName

    @property
    def KeyStruct(self):
        r"""表格主键字段结构json字符串
        :rtype: str
        """
        return self._KeyStruct

    @KeyStruct.setter
    def KeyStruct(self, KeyStruct):
        self._KeyStruct = KeyStruct

    @property
    def ValueStruct(self):
        r"""表格非主键字段结构json字符串
        :rtype: str
        """
        return self._ValueStruct

    @ValueStruct.setter
    def ValueStruct(self, ValueStruct):
        self._ValueStruct = ValueStruct

    @property
    def ShardingKeySet(self):
        r"""表格分表因子集合，对PROTO类型表格有效
        :rtype: str
        """
        return self._ShardingKeySet

    @ShardingKeySet.setter
    def ShardingKeySet(self, ShardingKeySet):
        self._ShardingKeySet = ShardingKeySet

    @property
    def IndexStruct(self):
        r"""表格索引键字段集合，对PROTO类型表格有效
        :rtype: str
        """
        return self._IndexStruct

    @IndexStruct.setter
    def IndexStruct(self, IndexStruct):
        self._IndexStruct = IndexStruct

    @property
    def ListElementNum(self):
        r"""LIST类型表格元素个数
        :rtype: int
        """
        return self._ListElementNum

    @ListElementNum.setter
    def ListElementNum(self, ListElementNum):
        self._ListElementNum = ListElementNum

    @property
    def IdlFiles(self):
        r"""表格所关联IDL文件信息列表
        :rtype: list of IdlFileInfo
        """
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def ReservedVolume(self):
        r"""表格预留容量（GB）
        :rtype: int
        """
        return self._ReservedVolume

    @ReservedVolume.setter
    def ReservedVolume(self, ReservedVolume):
        self._ReservedVolume = ReservedVolume

    @property
    def ReservedReadQps(self):
        r"""表格预留读CU
        :rtype: int
        """
        return self._ReservedReadQps

    @ReservedReadQps.setter
    def ReservedReadQps(self, ReservedReadQps):
        self._ReservedReadQps = ReservedReadQps

    @property
    def ReservedWriteQps(self):
        r"""表格预留写CU
        :rtype: int
        """
        return self._ReservedWriteQps

    @ReservedWriteQps.setter
    def ReservedWriteQps(self, ReservedWriteQps):
        self._ReservedWriteQps = ReservedWriteQps

    @property
    def TableSize(self):
        r"""表格实际数据量大小（MB）
        :rtype: int
        """
        return self._TableSize

    @TableSize.setter
    def TableSize(self, TableSize):
        self._TableSize = TableSize

    @property
    def Status(self):
        r"""表格状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""表格创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""表格最后一次修改时间
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Memo(self):
        r"""表格备注信息
        :rtype: str
        """
        return self._Memo

    @Memo.setter
    def Memo(self, Memo):
        self._Memo = Memo

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def ApiAccessId(self):
        r"""TcaplusDB SDK数据访问接入ID
        :rtype: str
        """
        return self._ApiAccessId

    @ApiAccessId.setter
    def ApiAccessId(self, ApiAccessId):
        self._ApiAccessId = ApiAccessId

    @property
    def SortFieldNum(self):
        r"""SORTLIST类型表格排序字段个数
        :rtype: int
        """
        return self._SortFieldNum

    @SortFieldNum.setter
    def SortFieldNum(self, SortFieldNum):
        self._SortFieldNum = SortFieldNum

    @property
    def SortRule(self):
        r"""SORTLIST类型表格排序顺序
        :rtype: int
        """
        return self._SortRule

    @SortRule.setter
    def SortRule(self, SortRule):
        self._SortRule = SortRule

    @property
    def DbClusterInfoStruct(self):
        r"""表格分布式索引/缓写、kafka数据订阅信息
        :rtype: str
        """
        return self._DbClusterInfoStruct

    @DbClusterInfoStruct.setter
    def DbClusterInfoStruct(self, DbClusterInfoStruct):
        self._DbClusterInfoStruct = DbClusterInfoStruct

    @property
    def TxhBackupExpireDay(self):
        r"""表格Txh备份文件多少天后过期删除
        :rtype: int
        """
        return self._TxhBackupExpireDay

    @TxhBackupExpireDay.setter
    def TxhBackupExpireDay(self, TxhBackupExpireDay):
        self._TxhBackupExpireDay = TxhBackupExpireDay

    @property
    def SyncTableInfo(self):
        r"""表格的缓写信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SyncTableInfo`
        """
        return self._SyncTableInfo

    @SyncTableInfo.setter
    def SyncTableInfo(self, SyncTableInfo):
        self._SyncTableInfo = SyncTableInfo

    @property
    def ShardNum(self):
        r"""表格分片数量
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableType = params.get("TableType")
        self._TableIdlType = params.get("TableIdlType")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TableGroupId = params.get("TableGroupId")
        self._TableGroupName = params.get("TableGroupName")
        self._KeyStruct = params.get("KeyStruct")
        self._ValueStruct = params.get("ValueStruct")
        self._ShardingKeySet = params.get("ShardingKeySet")
        self._IndexStruct = params.get("IndexStruct")
        self._ListElementNum = params.get("ListElementNum")
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        self._ReservedVolume = params.get("ReservedVolume")
        self._ReservedReadQps = params.get("ReservedReadQps")
        self._ReservedWriteQps = params.get("ReservedWriteQps")
        self._TableSize = params.get("TableSize")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._Memo = params.get("Memo")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._ApiAccessId = params.get("ApiAccessId")
        self._SortFieldNum = params.get("SortFieldNum")
        self._SortRule = params.get("SortRule")
        self._DbClusterInfoStruct = params.get("DbClusterInfoStruct")
        self._TxhBackupExpireDay = params.get("TxhBackupExpireDay")
        if params.get("SyncTableInfo") is not None:
            self._SyncTableInfo = SyncTableInfo()
            self._SyncTableInfo._deserialize(params.get("SyncTableInfo"))
        self._ShardNum = params.get("ShardNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableResultNew(AbstractModel):
    r"""表处理结果信息

    """

    def __init__(self):
        r"""
        :param _TableInstanceId: 表格实例ID，形如：tcaplus-3be64cbb
        :type TableInstanceId: str
        :param _TaskId: 任务ID，对于创建单任务的接口有效
        :type TaskId: str
        :param _TableName: 表格名称
        :type TableName: str
        :param _TableType: 表格数据结构类型，如：`GENERIC`或`LIST`
        :type TableType: str
        :param _TableIdlType: 表数据描述语言（IDL）类型，如：`PROTO`或`TDR`
        :type TableIdlType: str
        :param _TableGroupId: 表格所属表格组ID
        :type TableGroupId: str
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _TaskIds: 任务ID列表，对于创建多任务的接口有效
        :type TaskIds: list of str
        :param _ApplicationId: 腾讯云申请审核单Id
        :type ApplicationId: str
        """
        self._TableInstanceId = None
        self._TaskId = None
        self._TableName = None
        self._TableType = None
        self._TableIdlType = None
        self._TableGroupId = None
        self._Error = None
        self._TaskIds = None
        self._ApplicationId = None

    @property
    def TableInstanceId(self):
        r"""表格实例ID，形如：tcaplus-3be64cbb
        :rtype: str
        """
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TaskId(self):
        r"""任务ID，对于创建单任务的接口有效
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableType(self):
        r"""表格数据结构类型，如：`GENERIC`或`LIST`
        :rtype: str
        """
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def TableIdlType(self):
        r"""表数据描述语言（IDL）类型，如：`PROTO`或`TDR`
        :rtype: str
        """
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableGroupId(self):
        r"""表格所属表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def TaskIds(self):
        r"""任务ID列表，对于创建多任务的接口有效
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def ApplicationId(self):
        r"""腾讯云申请审核单Id
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._TableInstanceId = params.get("TableInstanceId")
        self._TaskId = params.get("TaskId")
        self._TableName = params.get("TableName")
        self._TableType = params.get("TableType")
        self._TableIdlType = params.get("TableIdlType")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._TaskIds = params.get("TaskIds")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfoUnit(AbstractModel):
    r"""标签信息单元

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
        


class TagsInfoOfCluster(AbstractModel):
    r"""集群的标签信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Tags: 标签信息
        :type Tags: list of TagInfoUnit
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._ClusterId = None
        self._Tags = None
        self._Error = None

    @property
    def ClusterId(self):
        r"""集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Tags(self):
        r"""标签信息
        :rtype: list of TagInfoUnit
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfTable(AbstractModel):
    r"""表格标签信息

    """

    def __init__(self):
        r"""
        :param _TableInstanceId: 表格实例ID
        :type TableInstanceId: str
        :param _TableName: 表格名称
        :type TableName: str
        :param _TableGroupId: 表格组ID
        :type TableGroupId: str
        :param _Tags: 标签信息
        :type Tags: list of TagInfoUnit
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._TableInstanceId = None
        self._TableName = None
        self._TableGroupId = None
        self._Tags = None
        self._Error = None

    @property
    def TableInstanceId(self):
        r"""表格实例ID
        :rtype: str
        """
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableName(self):
        r"""表格名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableGroupId(self):
        r"""表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def Tags(self):
        r"""标签信息
        :rtype: list of TagInfoUnit
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableName = params.get("TableName")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfTableGroup(AbstractModel):
    r"""表格组标签信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _TableGroupId: 表格组ID
        :type TableGroupId: str
        :param _Tags: 标签信息
        :type Tags: list of TagInfoUnit
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._Tags = None
        self._Error = None

    @property
    def ClusterId(self):
        r"""集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        r"""表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def Tags(self):
        r"""标签信息
        :rtype: list of TagInfoUnit
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfoNew(AbstractModel):
    r"""任务信息详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _TransId: 任务所关联的TcaplusDB内部事务ID
        :type TransId: str
        :param _ClusterId: 任务所属集群ID
        :type ClusterId: str
        :param _ClusterName: 任务所属集群名称
        :type ClusterName: str
        :param _Progress: 任务进度
        :type Progress: int
        :param _StartTime: 任务创建时间
        :type StartTime: str
        :param _UpdateTime: 任务最后更新时间
        :type UpdateTime: str
        :param _Operator: 操作者
        :type Operator: str
        :param _Content: 任务详情
        :type Content: str
        :param _TableGroupId: 表格组ID
        :type TableGroupId: str
        :param _TableGroupName: 表格组名称
        :type TableGroupName: str
        :param _TableName: 表名称
        :type TableName: str
        """
        self._TaskId = None
        self._TaskType = None
        self._TransId = None
        self._ClusterId = None
        self._ClusterName = None
        self._Progress = None
        self._StartTime = None
        self._UpdateTime = None
        self._Operator = None
        self._Content = None
        self._TableGroupId = None
        self._TableGroupName = None
        self._TableName = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        r"""任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TransId(self):
        r"""任务所关联的TcaplusDB内部事务ID
        :rtype: str
        """
        return self._TransId

    @TransId.setter
    def TransId(self, TransId):
        self._TransId = TransId

    @property
    def ClusterId(self):
        r"""任务所属集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""任务所属集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Progress(self):
        r"""任务进度
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StartTime(self):
        r"""任务创建时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def UpdateTime(self):
        r"""任务最后更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Operator(self):
        r"""操作者
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Content(self):
        r"""任务详情
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def TableGroupId(self):
        r"""表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableGroupName(self):
        r"""表格组名称
        :rtype: str
        """
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName

    @property
    def TableName(self):
        r"""表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._TransId = params.get("TransId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Progress = params.get("Progress")
        self._StartTime = params.get("StartTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Operator = params.get("Operator")
        self._Content = params.get("Content")
        self._TableGroupId = params.get("TableGroupId")
        self._TableGroupName = params.get("TableGroupName")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApplyRequest(AbstractModel):
    r"""UpdateApply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyStatus: 申请单状态
        :type ApplyStatus: list of ApplyStatus
        """
        self._ApplyStatus = None

    @property
    def ApplyStatus(self):
        r"""申请单状态
        :rtype: list of ApplyStatus
        """
        return self._ApplyStatus

    @ApplyStatus.setter
    def ApplyStatus(self, ApplyStatus):
        self._ApplyStatus = ApplyStatus


    def _deserialize(self, params):
        if params.get("ApplyStatus") is not None:
            self._ApplyStatus = []
            for item in params.get("ApplyStatus"):
                obj = ApplyStatus()
                obj._deserialize(item)
                self._ApplyStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApplyResponse(AbstractModel):
    r"""UpdateApply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyResults: 已更新的申请单列表
        :type ApplyResults: list of ApplyResult
        :param _TotalCount: 更新数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplyResults = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApplyResults(self):
        r"""已更新的申请单列表
        :rtype: list of ApplyResult
        """
        return self._ApplyResults

    @ApplyResults.setter
    def ApplyResults(self, ApplyResults):
        self._ApplyResults = ApplyResults

    @property
    def TotalCount(self):
        r"""更新数量
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
        if params.get("ApplyResults") is not None:
            self._ApplyResults = []
            for item in params.get("ApplyResults"):
                obj = ApplyResult()
                obj._deserialize(item)
                self._ApplyResults.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class VerifyIdlFilesRequest(AbstractModel):
    r"""VerifyIdlFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待创建表格的集群ID
        :type ClusterId: str
        :param _TableGroupId: 待创建表格的表格组ID
        :type TableGroupId: str
        :param _ExistingIdlFiles: 曾经上传过的IDL文件信息列表，与NewIdlFiles至少有一者
        :type ExistingIdlFiles: list of IdlFileInfo
        :param _NewIdlFiles: 待上传的IDL文件信息列表，与ExistingIdlFiles至少有一者
        :type NewIdlFiles: list of IdlFileInfo
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._ExistingIdlFiles = None
        self._NewIdlFiles = None

    @property
    def ClusterId(self):
        r"""待创建表格的集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        r"""待创建表格的表格组ID
        :rtype: str
        """
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def ExistingIdlFiles(self):
        r"""曾经上传过的IDL文件信息列表，与NewIdlFiles至少有一者
        :rtype: list of IdlFileInfo
        """
        return self._ExistingIdlFiles

    @ExistingIdlFiles.setter
    def ExistingIdlFiles(self, ExistingIdlFiles):
        self._ExistingIdlFiles = ExistingIdlFiles

    @property
    def NewIdlFiles(self):
        r"""待上传的IDL文件信息列表，与ExistingIdlFiles至少有一者
        :rtype: list of IdlFileInfo
        """
        return self._NewIdlFiles

    @NewIdlFiles.setter
    def NewIdlFiles(self, NewIdlFiles):
        self._NewIdlFiles = NewIdlFiles


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("ExistingIdlFiles") is not None:
            self._ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self._NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._NewIdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyIdlFilesResponse(AbstractModel):
    r"""VerifyIdlFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdlFiles: 本次上传校验所有的IDL文件信息列表
        :type IdlFiles: list of IdlFileInfo
        :param _TotalCount: 读取IDL描述文件后解析出的合法表数量，不包含已经创建的表
        :type TotalCount: int
        :param _TableInfos: 读取IDL描述文件后解析出的合法表列表，不包含已经创建的表
        :type TableInfos: list of ParsedTableInfoNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdlFiles = None
        self._TotalCount = None
        self._TableInfos = None
        self._RequestId = None

    @property
    def IdlFiles(self):
        r"""本次上传校验所有的IDL文件信息列表
        :rtype: list of IdlFileInfo
        """
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def TotalCount(self):
        r"""读取IDL描述文件后解析出的合法表数量，不包含已经创建的表
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableInfos(self):
        r"""读取IDL描述文件后解析出的合法表列表，不包含已经创建的表
        :rtype: list of ParsedTableInfoNew
        """
        return self._TableInfos

    @TableInfos.setter
    def TableInfos(self, TableInfos):
        self._TableInfos = TableInfos

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
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self._TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self._TableInfos.append(obj)
        self._RequestId = params.get("RequestId")