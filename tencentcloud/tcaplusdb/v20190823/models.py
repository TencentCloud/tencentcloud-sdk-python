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


class Application(AbstractModel):
    """审批申请单

    """

    def __init__(self):
        """
        :param ApplicationId: 审批单号\n        :type ApplicationId: str\n        :param ApplicationType: 申请类型\n        :type ApplicationType: int\n        :param ClusterId: 集群Id\n        :type ClusterId: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param TableGroupName: 表格组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupName: str\n        :param TableName: 表格名称\n        :type TableName: str\n        :param Applicant: 申请人\n        :type Applicant: str\n        :param CreatedTime: 建单时间\n        :type CreatedTime: str\n        :param ApplicationStatus: 处理状态 -1 撤回 0-待审核 1-已经审核并提交任务 2-已驳回\n        :type ApplicationStatus: int\n        :param TableGroupId: 表格组Id\n        :type TableGroupId: str\n        :param TaskId: 已提交的任务Id，未提交申请为0\n        :type TaskId: str\n        :param TableInstanceId: 腾讯云上table的唯一键
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableInstanceId: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param ExecuteUser: 审批人
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExecuteUser: str\n        :param ExecuteStatus: 执行状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExecuteStatus: str\n        :param CanCensor: 该申请单是否可以被当前用户审批
注意：此字段可能返回 null，表示取不到有效值。\n        :type CanCensor: bool\n        :param CanWithdrawal: 该申请单是否可以被当前用户撤回
注意：此字段可能返回 null，表示取不到有效值。\n        :type CanWithdrawal: bool\n        """
        self.ApplicationId = None
        self.ApplicationType = None
        self.ClusterId = None
        self.ClusterName = None
        self.TableGroupName = None
        self.TableName = None
        self.Applicant = None
        self.CreatedTime = None
        self.ApplicationStatus = None
        self.TableGroupId = None
        self.TaskId = None
        self.TableInstanceId = None
        self.UpdateTime = None
        self.ExecuteUser = None
        self.ExecuteStatus = None
        self.CanCensor = None
        self.CanWithdrawal = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.TableGroupName = params.get("TableGroupName")
        self.TableName = params.get("TableName")
        self.Applicant = params.get("Applicant")
        self.CreatedTime = params.get("CreatedTime")
        self.ApplicationStatus = params.get("ApplicationStatus")
        self.TableGroupId = params.get("TableGroupId")
        self.TaskId = params.get("TaskId")
        self.TableInstanceId = params.get("TableInstanceId")
        self.UpdateTime = params.get("UpdateTime")
        self.ExecuteUser = params.get("ExecuteUser")
        self.ExecuteStatus = params.get("ExecuteStatus")
        self.CanCensor = params.get("CanCensor")
        self.CanWithdrawal = params.get("CanWithdrawal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyResult(AbstractModel):
    """更新申请单结果

    """

    def __init__(self):
        """
        :param ApplicationId: 申请单id\n        :type ApplicationId: str\n        :param ApplicationType: 申请类型\n        :type ApplicationType: int\n        :param ApplicationStatus: 处理状态 0-待审核 1-已经审核并提交任务 2-已驳回
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationStatus: int\n        :param TaskId: 已提交的任务Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
        self.ApplicationId = None
        self.ApplicationType = None
        self.ApplicationStatus = None
        self.TaskId = None
        self.Error = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationType = params.get("ApplicationType")
        self.ApplicationStatus = params.get("ApplicationStatus")
        self.TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyStatus(AbstractModel):
    """申请单id及其状态

    """

    def __init__(self):
        """
        :param ApplicationId: 集群id-申请单id\n        :type ApplicationId: str\n        :param ApplicationStatus: 处理状态-1-撤回 1-通过 2-驳回，非0状态的申请单不可改变状态。\n        :type ApplicationStatus: int\n        :param ApplicationType: 申请单类型\n        :type ApplicationType: int\n        :param ClusterId: 集群Id\n        :type ClusterId: str\n        """
        self.ApplicationId = None
        self.ApplicationStatus = None
        self.ApplicationType = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationStatus = params.get("ApplicationStatus")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearTablesRequest(AbstractModel):
    """ClearTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表所属集群实例ID\n        :type ClusterId: str\n        :param SelectedTables: 待清理表信息列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearTablesResponse(AbstractModel):
    """ClearTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 清除表结果数量\n        :type TotalCount: int\n        :param TableResults: 清除表结果列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ClusterInfo(AbstractModel):
    """集群详细信息

    """

    def __init__(self):
        """
        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param Region: 集群所在地域\n        :type Region: str\n        :param IdlType: 集群数据描述语言类型，如：`PROTO`,`TDR`\n        :type IdlType: str\n        :param NetworkType: 网络类型\n        :type NetworkType: str\n        :param VpcId: 集群关联的用户私有网络实例ID\n        :type VpcId: str\n        :param SubnetId: 集群关联的用户子网实例ID\n        :type SubnetId: str\n        :param CreatedTime: 创建时间\n        :type CreatedTime: str\n        :param Password: 集群密码\n        :type Password: str\n        :param PasswordStatus: 密码状态\n        :type PasswordStatus: str\n        :param ApiAccessId: TcaplusDB SDK连接参数，接入ID\n        :type ApiAccessId: str\n        :param ApiAccessIp: TcaplusDB SDK连接参数，接入地址\n        :type ApiAccessIp: str\n        :param ApiAccessPort: TcaplusDB SDK连接参数，接入端口\n        :type ApiAccessPort: int\n        :param OldPasswordExpireTime: 如果PasswordStatus是unmodifiable说明有旧密码还未过期，此字段将显示旧密码过期的时间，否则为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type OldPasswordExpireTime: str\n        :param ApiAccessIpv6: TcaplusDB SDK连接参数，接入ipv6地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAccessIpv6: str\n        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterType: int\n        :param ClusterStatus: 集群状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterStatus: int\n        :param ReadCapacityUnit: 读CU
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReadCapacityUnit: int\n        :param WriteCapacityUnit: 写CU
注意：此字段可能返回 null，表示取不到有效值。\n        :type WriteCapacityUnit: int\n        :param DiskVolume: 磁盘容量
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskVolume: int\n        :param ServerList: 独占server机器信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerList: list of ServerDetailInfo\n        :param ProxyList: 独占proxy机器信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProxyList: list of ProxyDetailInfo\n        :param Censorship: 是否开启审核 0-不开启 1-开启\n        :type Censorship: int\n        :param DbaUins: 审批人uin列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type DbaUins: list of str\n        """
        self.ClusterName = None
        self.ClusterId = None
        self.Region = None
        self.IdlType = None
        self.NetworkType = None
        self.VpcId = None
        self.SubnetId = None
        self.CreatedTime = None
        self.Password = None
        self.PasswordStatus = None
        self.ApiAccessId = None
        self.ApiAccessIp = None
        self.ApiAccessPort = None
        self.OldPasswordExpireTime = None
        self.ApiAccessIpv6 = None
        self.ClusterType = None
        self.ClusterStatus = None
        self.ReadCapacityUnit = None
        self.WriteCapacityUnit = None
        self.DiskVolume = None
        self.ServerList = None
        self.ProxyList = None
        self.Censorship = None
        self.DbaUins = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.ClusterId = params.get("ClusterId")
        self.Region = params.get("Region")
        self.IdlType = params.get("IdlType")
        self.NetworkType = params.get("NetworkType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CreatedTime = params.get("CreatedTime")
        self.Password = params.get("Password")
        self.PasswordStatus = params.get("PasswordStatus")
        self.ApiAccessId = params.get("ApiAccessId")
        self.ApiAccessIp = params.get("ApiAccessIp")
        self.ApiAccessPort = params.get("ApiAccessPort")
        self.OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self.ApiAccessIpv6 = params.get("ApiAccessIpv6")
        self.ClusterType = params.get("ClusterType")
        self.ClusterStatus = params.get("ClusterStatus")
        self.ReadCapacityUnit = params.get("ReadCapacityUnit")
        self.WriteCapacityUnit = params.get("WriteCapacityUnit")
        self.DiskVolume = params.get("DiskVolume")
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = ServerDetailInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyDetailInfo()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        self.Censorship = params.get("Censorship")
        self.DbaUins = params.get("DbaUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareIdlFilesRequest(AbstractModel):
    """CompareIdlFiles请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待修改表格所在集群ID\n        :type ClusterId: str\n        :param SelectedTables: 待修改表格列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param ExistingIdlFiles: 选中的已上传IDL文件列表，与NewIdlFiles必选其一\n        :type ExistingIdlFiles: list of IdlFileInfo\n        :param NewIdlFiles: 本次上传IDL文件列表，与ExistingIdlFiles必选其一\n        :type NewIdlFiles: list of IdlFileInfo\n        """
        self.ClusterId = None
        self.SelectedTables = None
        self.ExistingIdlFiles = None
        self.NewIdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("ExistingIdlFiles") is not None:
            self.ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self.NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.NewIdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareIdlFilesResponse(AbstractModel):
    """CompareIdlFiles返回参数结构体

    """

    def __init__(self):
        """
        :param IdlFiles: 本次上传校验所有的IDL文件信息列表\n        :type IdlFiles: list of IdlFileInfo\n        :param TotalCount: 本次校验合法的表格数量\n        :type TotalCount: int\n        :param TableInfos: 读取IDL描述文件后,根据用户指示的所选中表格解析校验结果\n        :type TableInfos: list of ParsedTableInfoNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IdlFiles = None
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class CompareTablesInfo(AbstractModel):
    """比较表格的Meta信息

    """

    def __init__(self):
        """
        :param SrcTableClusterId: 源表格的集群id\n        :type SrcTableClusterId: str\n        :param SrcTableGroupId: 源表格的表格组id\n        :type SrcTableGroupId: str\n        :param SrcTableName: 源表格的表名\n        :type SrcTableName: str\n        :param DstTableClusterId: 目标表格的集群id\n        :type DstTableClusterId: str\n        :param DstTableGroupId: 目标表格的表格组id\n        :type DstTableGroupId: str\n        :param DstTableName: 目标表格的表名\n        :type DstTableName: str\n        :param SrcTableInstanceId: 源表格的实例id\n        :type SrcTableInstanceId: str\n        :param DstTableInstanceId: 目标表格的实例id\n        :type DstTableInstanceId: str\n        """
        self.SrcTableClusterId = None
        self.SrcTableGroupId = None
        self.SrcTableName = None
        self.DstTableClusterId = None
        self.DstTableGroupId = None
        self.DstTableName = None
        self.SrcTableInstanceId = None
        self.DstTableInstanceId = None


    def _deserialize(self, params):
        self.SrcTableClusterId = params.get("SrcTableClusterId")
        self.SrcTableGroupId = params.get("SrcTableGroupId")
        self.SrcTableName = params.get("SrcTableName")
        self.DstTableClusterId = params.get("DstTableClusterId")
        self.DstTableGroupId = params.get("DstTableGroupId")
        self.DstTableName = params.get("DstTableName")
        self.SrcTableInstanceId = params.get("SrcTableInstanceId")
        self.DstTableInstanceId = params.get("DstTableInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待创建备份表所属集群ID\n        :type ClusterId: str\n        :param SelectedTables: 待创建备份表信息列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param Remark: 备注信息\n        :type Remark: str\n        """
        self.ClusterId = None
        self.SelectedTables = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        """
        :param TaskIds: 创建的备份任务ID列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskIds: list of str\n        :param ApplicationIds: 创建的备份申请ID列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskIds = None
        self.ApplicationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.ApplicationIds = params.get("ApplicationIds")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param IdlType: 集群数据描述语言类型，如：`PROTO`，`TDR`或`MIX`\n        :type IdlType: str\n        :param ClusterName: 集群名称，可使用中文或英文字符，最大长度32个字符\n        :type ClusterName: str\n        :param VpcId: 集群所绑定的私有网络实例ID，形如：vpc-f49l6u0z\n        :type VpcId: str\n        :param SubnetId: 集群所绑定的子网实例ID，形如：subnet-pxir56ns\n        :type SubnetId: str\n        :param Password: 集群访问密码，必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母\n        :type Password: str\n        :param ResourceTags: 集群标签列表\n        :type ResourceTags: list of TagInfoUnit\n        :param Ipv6Enable: 集群是否开启IPv6功能\n        :type Ipv6Enable: int\n        :param ServerList: 独占集群占用的svr机器\n        :type ServerList: list of MachineInfo\n        :param ProxyList: 独占集群占用的proxy机器\n        :type ProxyList: list of MachineInfo\n        :param ClusterType: 集群类型1共享2独占\n        :type ClusterType: int\n        """
        self.IdlType = None
        self.ClusterName = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.ResourceTags = None
        self.Ipv6Enable = None
        self.ServerList = None
        self.ProxyList = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.IdlType = params.get("IdlType")
        self.ClusterName = params.get("ClusterName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.Ipv6Enable = params.get("Ipv6Enable")
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        self.ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateSnapshotsRequest(AbstractModel):
    """CreateSnapshots请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格所属集群id\n        :type ClusterId: str\n        :param SelectedTables: 快照列表\n        :type SelectedTables: list of SnapshotInfo\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotsResponse(AbstractModel):
    """CreateSnapshots返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批量创建的快照数量\n        :type TotalCount: int\n        :param TableResults: 批量创建的快照结果列表\n        :type TableResults: list of SnapshotResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class CreateTableGroupRequest(AbstractModel):
    """CreateTableGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格组所属集群ID\n        :type ClusterId: str\n        :param TableGroupName: 表格组名称，可以采用中文、英文或数字字符，最大长度32个字符\n        :type TableGroupName: str\n        :param TableGroupId: 表格组ID，可以由用户指定，但在同一个集群内不能重复，如果不指定则采用自增的模式\n        :type TableGroupId: str\n        :param ResourceTags: 表格组标签列表\n        :type ResourceTags: list of TagInfoUnit\n        """
        self.ClusterId = None
        self.TableGroupName = None
        self.TableGroupId = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupName = params.get("TableGroupName")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableGroupResponse(AbstractModel):
    """CreateTableGroup返回参数结构体

    """

    def __init__(self):
        """
        :param TableGroupId: 创建成功的表格组ID\n        :type TableGroupId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TableGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.RequestId = params.get("RequestId")


class CreateTablesRequest(AbstractModel):
    """CreateTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待创建表格所属集群ID\n        :type ClusterId: str\n        :param IdlFiles: 用户选定的建表格IDL文件列表\n        :type IdlFiles: list of IdlFileInfo\n        :param SelectedTables: 待创建表格信息列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param ResourceTags: 表格标签列表\n        :type ResourceTags: list of TagInfoUnit\n        """
        self.ClusterId = None
        self.IdlFiles = None
        self.SelectedTables = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTablesResponse(AbstractModel):
    """CreateTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批量创建表格结果数量\n        :type TotalCount: int\n        :param TableResults: 批量创建表格结果列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待删除的集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 删除集群生成的任务ID\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteIdlFilesRequest(AbstractModel):
    """DeleteIdlFiles请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: IDL所属集群ID\n        :type ClusterId: str\n        :param IdlFiles: 待删除的IDL文件信息列表\n        :type IdlFiles: list of IdlFileInfo\n        """
        self.ClusterId = None
        self.IdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIdlFilesResponse(AbstractModel):
    """DeleteIdlFiles返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果记录数量\n        :type TotalCount: int\n        :param IdlFileInfos: 删除结果\n        :type IdlFileInfos: list of IdlFileInfoWithoutContent\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.IdlFileInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IdlFileInfos") is not None:
            self.IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfoWithoutContent()
                obj._deserialize(item)
                self.IdlFileInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格所属集群id\n        :type ClusterId: str\n        :param SelectedTables: 删除的快照列表\n        :type SelectedTables: list of SnapshotInfoNew\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批量删除的快照数量\n        :type TotalCount: int\n        :param TableResults: 批量删除的快照结果\n        :type TableResults: list of SnapshotResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteTableGroupRequest(AbstractModel):
    """DeleteTableGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格组所属的集群ID\n        :type ClusterId: str\n        :param TableGroupId: 表格组ID\n        :type TableGroupId: str\n        """
        self.ClusterId = None
        self.TableGroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableGroupResponse(AbstractModel):
    """DeleteTableGroup返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 删除表格组所创建的任务ID\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteTableIndexRequest(AbstractModel):
    """DeleteTableIndex请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格所属集群实例ID\n        :type ClusterId: str\n        :param SelectedTables: 待删除分布式索引的表格列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableIndexResponse(AbstractModel):
    """DeleteTableIndex返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 删除表格分布式索引结果数量\n        :type TotalCount: int\n        :param TableResults: 删除表格分布式索引结果列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteTablesRequest(AbstractModel):
    """DeleteTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待删除表所在集群ID\n        :type ClusterId: str\n        :param SelectedTables: 待删除表信息列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTablesResponse(AbstractModel):
    """DeleteTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 删除表结果数量\n        :type TotalCount: int\n        :param TableResults: 删除表结果详情列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID，用于获取指定集群的单据\n        :type ClusterId: str\n        :param Limit: 分页\n        :type Limit: int\n        :param Offset: 分页\n        :type Offset: int\n        :param CensorStatus: 申请单状态，用于过滤\n        :type CensorStatus: int\n        :param TableGroupId: 表格组id，用于过滤\n        :type TableGroupId: str\n        :param TableName: 表格名，用于过滤\n        :type TableName: str\n        :param Applicant: 申请人uin，用于过滤\n        :type Applicant: str\n        :param ApplyType: 申请类型，用于过滤\n        :type ApplyType: int\n        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.CensorStatus = None
        self.TableGroupId = None
        self.TableName = None
        self.Applicant = None
        self.ApplyType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.CensorStatus = params.get("CensorStatus")
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.Applicant = params.get("Applicant")
        self.ApplyType = params.get("ApplyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications返回参数结构体

    """

    def __init__(self):
        """
        :param Applications: 申请单列表\n        :type Applications: list of Application\n        :param TotalCount: 申请单个数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Applications = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Applications") is not None:
            self.Applications = []
            for item in params.get("Applications"):
                obj = Application()
                obj._deserialize(item)
                self.Applications.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClusterTagsRequest(AbstractModel):
    """DescribeClusterTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterIds: 集群ID列表\n        :type ClusterIds: list of str\n        """
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterTagsResponse(AbstractModel):
    """DescribeClusterTags返回参数结构体

    """

    def __init__(self):
        """
        :param Rows: 集群标签信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rows: list of TagsInfoOfCluster\n        :param TotalCount: 返回结果个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Rows = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfCluster()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterIds: 指定查询的集群ID列表\n        :type ClusterIds: list of str\n        :param Filters: 查询过滤条件\n        :type Filters: list of Filter\n        :param Offset: 查询列表偏移量\n        :type Offset: int\n        :param Limit: 查询列表返回记录数，默认值20\n        :type Limit: int\n        :param Ipv6Enable: 是否启用Ipv6\n        :type Ipv6Enable: int\n        """
        self.ClusterIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Ipv6Enable = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群实例数\n        :type TotalCount: int\n        :param Clusters: 集群实例列表\n        :type Clusters: list of ClusterInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIdlFileInfosRequest(AbstractModel):
    """DescribeIdlFileInfos请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 文件所属集群ID\n        :type ClusterId: str\n        :param TableGroupIds: 文件所属表格组ID\n        :type TableGroupIds: list of str\n        :param IdlFileIds: 指定文件ID列表\n        :type IdlFileIds: list of str\n        :param Offset: 查询列表偏移量\n        :type Offset: int\n        :param Limit: 查询列表返回记录数\n        :type Limit: int\n        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.IdlFileIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        self.IdlFileIds = params.get("IdlFileIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdlFileInfosResponse(AbstractModel):
    """DescribeIdlFileInfos返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 文件数量\n        :type TotalCount: int\n        :param IdlFileInfos: 文件详情列表\n        :type IdlFileInfos: list of IdlFileInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.IdlFileInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IdlFileInfos") is not None:
            self.IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFileInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineRequest(AbstractModel):
    """DescribeMachine请求参数结构体

    """

    def __init__(self):
        """
        :param Ipv6Enable: 不为0，表示查询支持ipv6的机器\n        :type Ipv6Enable: int\n        """
        self.Ipv6Enable = None


    def _deserialize(self, params):
        self.Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineResponse(AbstractModel):
    """DescribeMachine返回参数结构体

    """

    def __init__(self):
        """
        :param PoolList: 独占机器资源列表\n        :type PoolList: list of PoolInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PoolList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PoolList") is not None:
            self.PoolList = []
            for item in params.get("PoolList"):
                obj = PoolInfo()
                obj._deserialize(item)
                self.PoolList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 可用区详情结果数量\n        :type TotalCount: int\n        :param RegionInfos: 可用区详情结果列表\n        :type RegionInfos: list of RegionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.RegionInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionInfos") is not None:
            self.RegionInfos = []
            for item in params.get("RegionInfos"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格所属集群id\n        :type ClusterId: str\n        :param TableGroupId: 所属表格组ID\n        :type TableGroupId: str\n        :param TableName: 表名称\n        :type TableName: str\n        :param SnapshotName: 快照名称\n        :type SnapshotName: str\n        """
        self.ClusterId = None
        self.TableGroupId = None
        self.TableName = None
        self.SnapshotName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 快照数量\n        :type TotalCount: int\n        :param TableResults: 快照结果列表\n        :type TableResults: list of SnapshotResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableGroupTagsRequest(AbstractModel):
    """DescribeTableGroupTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待查询标签表格组所属集群ID\n        :type ClusterId: str\n        :param TableGroupIds: 待查询标签表格组ID列表\n        :type TableGroupIds: list of str\n        """
        self.ClusterId = None
        self.TableGroupIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableGroupTagsResponse(AbstractModel):
    """DescribeTableGroupTags返回参数结构体

    """

    def __init__(self):
        """
        :param Rows: 表格组标签信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rows: list of TagsInfoOfTableGroup\n        :param TotalCount: 返回结果个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Rows = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfTableGroup()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTableGroupsRequest(AbstractModel):
    """DescribeTableGroups请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格组所属集群ID\n        :type ClusterId: str\n        :param TableGroupIds: 表格组ID列表\n        :type TableGroupIds: list of str\n        :param Filters: 过滤条件，本接口支持：TableGroupName，TableGroupId\n        :type Filters: list of Filter\n        :param Offset: 查询列表偏移量\n        :type Offset: int\n        :param Limit: 查询列表返回记录数\n        :type Limit: int\n        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
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
        


class DescribeTableGroupsResponse(AbstractModel):
    """DescribeTableGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格组数量\n        :type TotalCount: int\n        :param TableGroups: 表格组信息列表\n        :type TableGroups: list of TableGroupInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableGroups") is not None:
            self.TableGroups = []
            for item in params.get("TableGroups"):
                obj = TableGroupInfo()
                obj._deserialize(item)
                self.TableGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableTagsRequest(AbstractModel):
    """DescribeTableTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格所属集群ID\n        :type ClusterId: str\n        :param SelectedTables: 表格列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableTagsResponse(AbstractModel):
    """DescribeTableTags返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回结果总数\n        :type TotalCount: int\n        :param Rows: 表格标签信息列表\n        :type Rows: list of TagsInfoOfTable\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfTable()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesInRecycleRequest(AbstractModel):
    """DescribeTablesInRecycle请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待查询表格所属集群ID\n        :type ClusterId: str\n        :param TableGroupIds: 待查询表格所属表格组ID列表\n        :type TableGroupIds: list of str\n        :param Filters: 过滤条件，本接口支持：TableName，TableInstanceId\n        :type Filters: list of Filter\n        :param Offset: 查询结果偏移量\n        :type Offset: int\n        :param Limit: 查询结果返回记录数量\n        :type Limit: int\n        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
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
        


class DescribeTablesInRecycleResponse(AbstractModel):
    """DescribeTablesInRecycle返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格数量\n        :type TotalCount: int\n        :param TableInfos: 表格详情结果列表\n        :type TableInfos: list of TableInfoNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待查询表格所属集群ID\n        :type ClusterId: str\n        :param TableGroupIds: 待查询表格所属表格组ID列表\n        :type TableGroupIds: list of str\n        :param SelectedTables: 待查询表格信息列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param Filters: 过滤条件，本接口支持：TableName，TableInstanceId\n        :type Filters: list of Filter\n        :param Offset: 查询结果偏移量\n        :type Offset: int\n        :param Limit: 查询结果返回记录数量\n        :type Limit: int\n        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.SelectedTables = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
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
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格数量\n        :type TotalCount: int\n        :param TableInfos: 表格详情结果列表\n        :type TableInfos: list of TableInfoNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterIds: 需要查询任务所属的集群ID列表\n        :type ClusterIds: list of str\n        :param TaskIds: 需要查询的任务ID列表\n        :type TaskIds: list of str\n        :param Filters: 过滤条件，本接口支持：Content，TaskType, Operator, Time\n        :type Filters: list of Filter\n        :param Offset: 查询列表偏移量\n        :type Offset: int\n        :param Limit: 查询列表返回记录数\n        :type Limit: int\n        """
        self.ClusterIds = None
        self.TaskIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        self.TaskIds = params.get("TaskIds")
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
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 任务数量\n        :type TotalCount: int\n        :param TaskInfos: 查询到的任务详情列表\n        :type TaskInfos: list of TaskInfoNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TaskInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = TaskInfoNew()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUinInWhitelistRequest(AbstractModel):
    """DescribeUinInWhitelist请求参数结构体

    """


class DescribeUinInWhitelistResponse(AbstractModel):
    """DescribeUinInWhitelist返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询结果：`FALSE` 否；`TRUE` 是\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableRestProxyRequest(AbstractModel):
    """DisableRestProxy请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 对应appid\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRestProxyResponse(AbstractModel):
    """DisableRestProxy返回参数结构体

    """

    def __init__(self):
        """
        :param RestProxyStatus: RestProxy的状态，0为关闭，1为开启中，2为开启，3为关闭中\n        :type RestProxyStatus: int\n        :param TaskId: TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RestProxyStatus = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RestProxyStatus = params.get("RestProxyStatus")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EnableRestProxyRequest(AbstractModel):
    """EnableRestProxy请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 对应于appid\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRestProxyResponse(AbstractModel):
    """EnableRestProxy返回参数结构体

    """

    def __init__(self):
        """
        :param RestProxyStatus: RestProxy的状态，0为关闭，1为开启中，2为开启，3为关闭中\n        :type RestProxyStatus: int\n        :param TaskId: TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RestProxyStatus = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RestProxyStatus = params.get("RestProxyStatus")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ErrorInfo(AbstractModel):
    """描述每个实例（应用，大区或表）处理过程中可能出现的错误详情。

    """

    def __init__(self):
        """
        :param Code: 错误码\n        :type Code: str\n        :param Message: 错误信息\n        :type Message: str\n        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldInfo(AbstractModel):
    """表格字段信息列表

    """

    def __init__(self):
        """
        :param FieldName: 表格字段名称\n        :type FieldName: str\n        :param IsPrimaryKey: 字段是否是主键字段\n        :type IsPrimaryKey: str\n        :param FieldType: 字段类型\n        :type FieldType: str\n        :param FieldSize: 字段长度\n        :type FieldSize: int\n        """
        self.FieldName = None
        self.IsPrimaryKey = None
        self.FieldType = None
        self.FieldSize = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.IsPrimaryKey = params.get("IsPrimaryKey")
        self.FieldType = params.get("FieldType")
        self.FieldSize = params.get("FieldSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        """
        :param Name: 过滤字段名\n        :type Name: str\n        :param Value: 过滤字段值\n        :type Value: str\n        :param Values: 过滤字段值\n        :type Values: list of str\n        """
        self.Name = None
        self.Value = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdlFileInfo(AbstractModel):
    """表定义描述文件详情，包含文件内容

    """

    def __init__(self):
        """
        :param FileName: 文件名称，不包含扩展名\n        :type FileName: str\n        :param FileType: 数据描述语言（IDL）类型\n        :type FileType: str\n        :param FileExtType: 文件扩展名\n        :type FileExtType: str\n        :param FileSize: 文件大小（Bytes）\n        :type FileSize: int\n        :param FileId: 文件ID，对于已上传的文件有意义
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileId: int\n        :param FileContent: 文件内容，对于本次新上传的文件有意义
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileContent: str\n        """
        self.FileName = None
        self.FileType = None
        self.FileExtType = None
        self.FileSize = None
        self.FileId = None
        self.FileContent = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileId = params.get("FileId")
        self.FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdlFileInfoWithoutContent(AbstractModel):
    """表定义描述文件详情，不包含文件内容

    """

    def __init__(self):
        """
        :param FileName: 文件名称，不包含扩展名
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileName: str\n        :param FileType: 数据描述语言（IDL）类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileType: str\n        :param FileExtType: 文件扩展名
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileExtType: str\n        :param FileSize: 文件大小（Bytes）
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileSize: int\n        :param FileId: 文件ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileId: int\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
        self.FileName = None
        self.FileType = None
        self.FileExtType = None
        self.FileSize = None
        self.FileId = None
        self.Error = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileId = params.get("FileId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSnapshotsRequest(AbstractModel):
    """ImportSnapshots请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格所属的集群id\n        :type ClusterId: str\n        :param Snapshots: 用于导入的快照信息\n        :type Snapshots: :class:`tencentcloud.tcaplusdb.v20190823.models.SnapshotInfo`\n        :param ImportSpecialKey: 是否导入部分记录，TRUE表示导入部分记录，FALSE表示全表导入\n        :type ImportSpecialKey: str\n        :param ImportOriginTable: 是否导入到当前表，TRUE表示导入到当前表，FALSE表示导入到新表\n        :type ImportOriginTable: str\n        :param KeyFile: 部分记录的key文件\n        :type KeyFile: :class:`tencentcloud.tcaplusdb.v20190823.models.KeyFile`\n        :param NewTableGroupId: 如果导入到新表，此为新表所属的表格组id\n        :type NewTableGroupId: str\n        :param NewTableName: 如果导入到新表，此为新表的表名，系统会以该名称自动创建一张结构相同的空表\n        :type NewTableName: str\n        """
        self.ClusterId = None
        self.Snapshots = None
        self.ImportSpecialKey = None
        self.ImportOriginTable = None
        self.KeyFile = None
        self.NewTableGroupId = None
        self.NewTableName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Snapshots") is not None:
            self.Snapshots = SnapshotInfo()
            self.Snapshots._deserialize(params.get("Snapshots"))
        self.ImportSpecialKey = params.get("ImportSpecialKey")
        self.ImportOriginTable = params.get("ImportOriginTable")
        if params.get("KeyFile") is not None:
            self.KeyFile = KeyFile()
            self.KeyFile._deserialize(params.get("KeyFile"))
        self.NewTableGroupId = params.get("NewTableGroupId")
        self.NewTableName = params.get("NewTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSnapshotsResponse(AbstractModel):
    """ImportSnapshots返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: TaskId由 AppInstanceId-taskId 组成，以区分不同集群的任务
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class KeyFile(AbstractModel):
    """部分key导入快照数据时所需要的key文件

    """

    def __init__(self):
        """
        :param FileName: key文件名称\n        :type FileName: str\n        :param FileExtType: key文件扩展名\n        :type FileExtType: str\n        :param FileContent: key文件内容\n        :type FileContent: str\n        :param FileSize: key文件大小\n        :type FileSize: int\n        """
        self.FileName = None
        self.FileExtType = None
        self.FileContent = None
        self.FileSize = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileExtType = params.get("FileExtType")
        self.FileContent = params.get("FileContent")
        self.FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineInfo(AbstractModel):
    """机器类型和数量

    """

    def __init__(self):
        """
        :param MachineType: 机器类型\n        :type MachineType: str\n        :param MachineNum: 机器数量\n        :type MachineNum: int\n        """
        self.MachineType = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTableResult(AbstractModel):
    """合服结果

    """

    def __init__(self):
        """
        :param TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param Error: 成功时此字段返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param Table: 对比的表格信息\n        :type Table: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`\n        :param ApplicationId: 申请单Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        """
        self.TaskId = None
        self.Error = None
        self.Table = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        if params.get("Table") is not None:
            self.Table = CompareTablesInfo()
            self.Table._deserialize(params.get("Table"))
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTablesDataRequest(AbstractModel):
    """MergeTablesData请求参数结构体

    """

    def __init__(self):
        """
        :param SelectedTables: 选取的表格\n        :type SelectedTables: list of MergeTablesInfo\n        :param IsOnlyCompare: true只做对比，false既对比又执行\n        :type IsOnlyCompare: bool\n        """
        self.SelectedTables = None
        self.IsOnlyCompare = None


    def _deserialize(self, params):
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = MergeTablesInfo()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.IsOnlyCompare = params.get("IsOnlyCompare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTablesDataResponse(AbstractModel):
    """MergeTablesData返回参数结构体

    """

    def __init__(self):
        """
        :param Results: 合服结果集\n        :type Results: list of MergeTableResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = MergeTableResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class MergeTablesInfo(AbstractModel):
    """合服请求入参

    """

    def __init__(self):
        """
        :param MergeTables: 合服的表格信息\n        :type MergeTables: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`\n        :param CheckIndex: 是否检查索引\n        :type CheckIndex: bool\n        """
        self.MergeTables = None
        self.CheckIndex = None


    def _deserialize(self, params):
        if params.get("MergeTables") is not None:
            self.MergeTables = CompareTablesInfo()
            self.MergeTables._deserialize(params.get("MergeTables"))
        self.CheckIndex = params.get("CheckIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCensorshipRequest(AbstractModel):
    """ModifyCensorship请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param Censorship: 集群是否开启审核 0-关闭 1-开启\n        :type Censorship: int\n        :param Uins: 审批人uin列表\n        :type Uins: list of str\n        """
        self.ClusterId = None
        self.Censorship = None
        self.Uins = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Censorship = params.get("Censorship")
        self.Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCensorshipResponse(AbstractModel):
    """ModifyCensorship返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param Uins: 已加入审批人的uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uins: list of str\n        :param Censorship: 集群是否开启审核 0-关闭 1-开启\n        :type Censorship: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ClusterId = None
        self.Uins = None
        self.Censorship = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Uins = params.get("Uins")
        self.Censorship = params.get("Censorship")
        self.RequestId = params.get("RequestId")


class ModifyClusterMachineRequest(AbstractModel):
    """ModifyClusterMachine请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param ServerList: svr占用的机器\n        :type ServerList: list of MachineInfo\n        :param ProxyList: proxy占用的机器\n        :type ProxyList: list of MachineInfo\n        :param ClusterType: 集群类型1共享集群2独占集群\n        :type ClusterType: int\n        """
        self.ClusterId = None
        self.ServerList = None
        self.ProxyList = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        self.ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterMachineResponse(AbstractModel):
    """ModifyClusterMachine返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 需要修改名称的集群ID\n        :type ClusterId: str\n        :param ClusterName: 需要修改的集群名称，可使用中文或英文字符，最大长度32个字符\n        :type ClusterName: str\n        """
        self.ClusterId = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterPasswordRequest(AbstractModel):
    """ModifyClusterPassword请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 需要修改密码的集群ID\n        :type ClusterId: str\n        :param OldPassword: 集群旧密码\n        :type OldPassword: str\n        :param OldPasswordExpireTime: 集群旧密码预期失效时间\n        :type OldPasswordExpireTime: str\n        :param NewPassword: 集群新密码，密码必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母\n        :type NewPassword: str\n        :param Mode: 更新模式： `1` 更新密码；`2` 更新旧密码失效时间，默认为`1` 模式\n        :type Mode: str\n        """
        self.ClusterId = None
        self.OldPassword = None
        self.OldPasswordExpireTime = None
        self.NewPassword = None
        self.Mode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.OldPassword = params.get("OldPassword")
        self.OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self.NewPassword = params.get("NewPassword")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterPasswordResponse(AbstractModel):
    """ModifyClusterPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterTagsRequest(AbstractModel):
    """ModifyClusterTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待修改标签的集群ID\n        :type ClusterId: str\n        :param ReplaceTags: 待增加或修改的标签列表\n        :type ReplaceTags: list of TagInfoUnit\n        :param DeleteTags: 待删除的标签\n        :type DeleteTags: list of TagInfoUnit\n        """
        self.ClusterId = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterTagsResponse(AbstractModel):
    """ModifyClusterTags返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifySnapshotsRequest(AbstractModel):
    """ModifySnapshots请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格所属集群id\n        :type ClusterId: str\n        :param SelectedTables: 快照列表\n        :type SelectedTables: list of SnapshotInfoNew\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotsResponse(AbstractModel):
    """ModifySnapshots返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批量创建的快照数量\n        :type TotalCount: int\n        :param TableResults: 批量创建的快照结果列表\n        :type TableResults: list of SnapshotResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTableGroupNameRequest(AbstractModel):
    """ModifyTableGroupName请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格组所属的集群ID\n        :type ClusterId: str\n        :param TableGroupId: 待修改名称的表格组ID\n        :type TableGroupId: str\n        :param TableGroupName: 新的表格组名称，可以使用中英文字符和符号\n        :type TableGroupName: str\n        """
        self.ClusterId = None
        self.TableGroupId = None
        self.TableGroupName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableGroupNameResponse(AbstractModel):
    """ModifyTableGroupName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTableGroupTagsRequest(AbstractModel):
    """ModifyTableGroupTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待修改标签表格组所属集群ID\n        :type ClusterId: str\n        :param TableGroupId: 待修改标签表格组ID\n        :type TableGroupId: str\n        :param ReplaceTags: 待增加或修改的标签列表\n        :type ReplaceTags: list of TagInfoUnit\n        :param DeleteTags: 待删除的标签\n        :type DeleteTags: list of TagInfoUnit\n        """
        self.ClusterId = None
        self.TableGroupId = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableGroupTagsResponse(AbstractModel):
    """ModifyTableGroupTags返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyTableMemosRequest(AbstractModel):
    """ModifyTableMemos请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表所属集群实例ID\n        :type ClusterId: str\n        :param TableMemos: 选定表详情列表\n        :type TableMemos: list of SelectedTableInfoNew\n        """
        self.ClusterId = None
        self.TableMemos = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("TableMemos") is not None:
            self.TableMemos = []
            for item in params.get("TableMemos"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.TableMemos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableMemosResponse(AbstractModel):
    """ModifyTableMemos返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表备注修改结果数量\n        :type TotalCount: int\n        :param TableResults: 表备注修改结果列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTableQuotasRequest(AbstractModel):
    """ModifyTableQuotas请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 带扩缩容表所属集群ID\n        :type ClusterId: str\n        :param TableQuotas: 已选中待修改的表配额列表\n        :type TableQuotas: list of SelectedTableInfoNew\n        """
        self.ClusterId = None
        self.TableQuotas = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("TableQuotas") is not None:
            self.TableQuotas = []
            for item in params.get("TableQuotas"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.TableQuotas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableQuotasResponse(AbstractModel):
    """ModifyTableQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 扩缩容结果数量\n        :type TotalCount: int\n        :param TableResults: 扩缩容结果列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTableTagsRequest(AbstractModel):
    """ModifyTableTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待修改标签表格所属集群ID\n        :type ClusterId: str\n        :param SelectedTables: 待修改标签表格列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param ReplaceTags: 待增加或修改的标签列表\n        :type ReplaceTags: list of TagInfoUnit\n        :param DeleteTags: 待删除的标签列表\n        :type DeleteTags: list of TagInfoUnit\n        """
        self.ClusterId = None
        self.SelectedTables = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableTagsResponse(AbstractModel):
    """ModifyTableTags返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回结果总数\n        :type TotalCount: int\n        :param TableResults: 返回结果\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTablesRequest(AbstractModel):
    """ModifyTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待修改表格所在集群ID\n        :type ClusterId: str\n        :param IdlFiles: 选中的改表IDL文件\n        :type IdlFiles: list of IdlFileInfo\n        :param SelectedTables: 待改表格列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
        self.ClusterId = None
        self.IdlFiles = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTablesResponse(AbstractModel):
    """ModifyTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 修改表结果数量\n        :type TotalCount: int\n        :param TableResults: 修改表结果列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ParsedTableInfoNew(AbstractModel):
    """从IDL表描述文件中解析出来的表信息

    """

    def __init__(self):
        """
        :param TableIdlType: 表格描述语言类型：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableIdlType: str\n        :param TableInstanceId: 表格实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableInstanceId: str\n        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableName: str\n        :param TableType: 表格数据结构类型：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableType: str\n        :param KeyFields: 主键字段信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyFields: str\n        :param OldKeyFields: 原主键字段信息，改表校验时有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type OldKeyFields: str\n        :param ValueFields: 非主键字段信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValueFields: str\n        :param OldValueFields: 原非主键字段信息，改表校验时有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type OldValueFields: str\n        :param TableGroupId: 所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupId: str\n        :param SumKeyFieldSize: 主键字段总大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type SumKeyFieldSize: int\n        :param SumValueFieldSize: 非主键字段总大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type SumValueFieldSize: int\n        :param IndexKeySet: 索引键集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type IndexKeySet: str\n        :param ShardingKeySet: 分表因子集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShardingKeySet: str\n        :param TdrVersion: TDR版本号
注意：此字段可能返回 null，表示取不到有效值。\n        :type TdrVersion: int\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param ListElementNum: LIST类型表格元素个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListElementNum: int\n        :param SortFieldNum: SORTLIST类型表格排序字段个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type SortFieldNum: int\n        :param SortRule: SORTLIST类型表格排序顺序
注意：此字段可能返回 null，表示取不到有效值。\n        :type SortRule: int\n        """
        self.TableIdlType = None
        self.TableInstanceId = None
        self.TableName = None
        self.TableType = None
        self.KeyFields = None
        self.OldKeyFields = None
        self.ValueFields = None
        self.OldValueFields = None
        self.TableGroupId = None
        self.SumKeyFieldSize = None
        self.SumValueFieldSize = None
        self.IndexKeySet = None
        self.ShardingKeySet = None
        self.TdrVersion = None
        self.Error = None
        self.ListElementNum = None
        self.SortFieldNum = None
        self.SortRule = None


    def _deserialize(self, params):
        self.TableIdlType = params.get("TableIdlType")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.KeyFields = params.get("KeyFields")
        self.OldKeyFields = params.get("OldKeyFields")
        self.ValueFields = params.get("ValueFields")
        self.OldValueFields = params.get("OldValueFields")
        self.TableGroupId = params.get("TableGroupId")
        self.SumKeyFieldSize = params.get("SumKeyFieldSize")
        self.SumValueFieldSize = params.get("SumValueFieldSize")
        self.IndexKeySet = params.get("IndexKeySet")
        self.ShardingKeySet = params.get("ShardingKeySet")
        self.TdrVersion = params.get("TdrVersion")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.ListElementNum = params.get("ListElementNum")
        self.SortFieldNum = params.get("SortFieldNum")
        self.SortRule = params.get("SortRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoolInfo(AbstractModel):
    """center资源池中的机器信息

    """

    def __init__(self):
        """
        :param PoolUid: 唯一id\n        :type PoolUid: int\n        :param Ipv6Enable: 是否支持ipv6\n        :type Ipv6Enable: int\n        :param AvailableAppCount: 剩余可用app\n        :type AvailableAppCount: int\n        :param ServerList: svr机器列表\n        :type ServerList: list of ServerMachineInfo\n        :param ProxyList: proxy机器列表\n        :type ProxyList: list of ProxyMachineInfo\n        """
        self.PoolUid = None
        self.Ipv6Enable = None
        self.AvailableAppCount = None
        self.ServerList = None
        self.ProxyList = None


    def _deserialize(self, params):
        self.PoolUid = params.get("PoolUid")
        self.Ipv6Enable = params.get("Ipv6Enable")
        self.AvailableAppCount = params.get("AvailableAppCount")
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = ServerMachineInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyMachineInfo()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyDetailInfo(AbstractModel):
    """独占的proxy详细信息

    """

    def __init__(self):
        """
        :param ProxyUid: proxy的唯一id\n        :type ProxyUid: str\n        :param MachineType: 机器类型\n        :type MachineType: str\n        :param ProcessSpeed: 请求包速度\n        :type ProcessSpeed: int\n        :param AverageProcessDelay: 请求包时延\n        :type AverageProcessDelay: int\n        :param SlowProcessSpeed: 慢处理包速度\n        :type SlowProcessSpeed: int\n        """
        self.ProxyUid = None
        self.MachineType = None
        self.ProcessSpeed = None
        self.AverageProcessDelay = None
        self.SlowProcessSpeed = None


    def _deserialize(self, params):
        self.ProxyUid = params.get("ProxyUid")
        self.MachineType = params.get("MachineType")
        self.ProcessSpeed = params.get("ProcessSpeed")
        self.AverageProcessDelay = params.get("AverageProcessDelay")
        self.SlowProcessSpeed = params.get("SlowProcessSpeed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyMachineInfo(AbstractModel):
    """proxy机器信息

    """

    def __init__(self):
        """
        :param ProxyUid: 唯一id\n        :type ProxyUid: str\n        :param MachineType: 机器类型\n        :type MachineType: str\n        """
        self.ProxyUid = None
        self.MachineType = None


    def _deserialize(self, params):
        self.ProxyUid = params.get("ProxyUid")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverRecycleTablesRequest(AbstractModel):
    """RecoverRecycleTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表所在集群ID\n        :type ClusterId: str\n        :param SelectedTables: 待恢复表信息\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverRecycleTablesResponse(AbstractModel):
    """RecoverRecycleTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 恢复表结果数量\n        :type TotalCount: int\n        :param TableResults: 恢复表信息列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """TcaplusDB服务地域信息详情

    """

    def __init__(self):
        """
        :param RegionName: 地域Ap-Code\n        :type RegionName: str\n        :param RegionAbbr: 地域缩写\n        :type RegionAbbr: str\n        :param RegionId: 地域ID\n        :type RegionId: int\n        :param Ipv6Enable: 是否支持ipv6，0:不支持，1:支持\n        :type Ipv6Enable: int\n        """
        self.RegionName = None
        self.RegionAbbr = None
        self.RegionId = None
        self.Ipv6Enable = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.RegionAbbr = params.get("RegionAbbr")
        self.RegionId = params.get("RegionId")
        self.Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTablesRequest(AbstractModel):
    """RollbackTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待回档表格所在集群ID\n        :type ClusterId: str\n        :param SelectedTables: 待回档表格列表\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param RollbackTime: 待回档时间\n        :type RollbackTime: str\n        :param Mode: 回档模式，支持：`KEYS`\n        :type Mode: str\n        """
        self.ClusterId = None
        self.SelectedTables = None
        self.RollbackTime = None
        self.Mode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.RollbackTime = params.get("RollbackTime")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTablesResponse(AbstractModel):
    """RollbackTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格回档任务结果数量\n        :type TotalCount: int\n        :param TableResults: 表格回档任务结果列表\n        :type TableResults: list of TableRollbackResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableRollbackResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class SelectedTableInfoNew(AbstractModel):
    """被选中的表信息

    """

    def __init__(self):
        """
        :param TableGroupId: 表所属表格组ID\n        :type TableGroupId: str\n        :param TableName: 表格名称\n        :type TableName: str\n        :param TableInstanceId: 表实例ID\n        :type TableInstanceId: str\n        :param TableIdlType: 表格描述语言类型：`PROTO`或`TDR`\n        :type TableIdlType: str\n        :param TableType: 表格数据结构类型：`GENERIC`或`LIST`\n        :type TableType: str\n        :param ListElementNum: LIST表元素个数\n        :type ListElementNum: int\n        :param ReservedVolume: 表格预留容量（GB）\n        :type ReservedVolume: int\n        :param ReservedReadQps: 表格预留读CU\n        :type ReservedReadQps: int\n        :param ReservedWriteQps: 表格预留写CU\n        :type ReservedWriteQps: int\n        :param Memo: 表格备注信息\n        :type Memo: str\n        :param FileName: Key回档文件名，回档专用\n        :type FileName: str\n        :param FileExtType: Key回档文件扩展名，回档专用\n        :type FileExtType: str\n        :param FileSize: Key回档文件大小，回档专用\n        :type FileSize: int\n        :param FileContent: Key回档文件内容，回档专用\n        :type FileContent: str\n        """
        self.TableGroupId = None
        self.TableName = None
        self.TableInstanceId = None
        self.TableIdlType = None
        self.TableType = None
        self.ListElementNum = None
        self.ReservedVolume = None
        self.ReservedReadQps = None
        self.ReservedWriteQps = None
        self.Memo = None
        self.FileName = None
        self.FileExtType = None
        self.FileSize = None
        self.FileContent = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableIdlType = params.get("TableIdlType")
        self.TableType = params.get("TableType")
        self.ListElementNum = params.get("ListElementNum")
        self.ReservedVolume = params.get("ReservedVolume")
        self.ReservedReadQps = params.get("ReservedReadQps")
        self.ReservedWriteQps = params.get("ReservedWriteQps")
        self.Memo = params.get("Memo")
        self.FileName = params.get("FileName")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedTableWithField(AbstractModel):
    """附带被选中字段信息的表格列表

    """

    def __init__(self):
        """
        :param TableGroupId: 表所属表格组ID\n        :type TableGroupId: str\n        :param TableName: 表格名称\n        :type TableName: str\n        :param TableInstanceId: 表实例ID\n        :type TableInstanceId: str\n        :param TableIdlType: 表格描述语言类型：`PROTO`或`TDR`\n        :type TableIdlType: str\n        :param TableType: 表格数据结构类型：`GENERIC`或`LIST`\n        :type TableType: str\n        :param SelectedFields: 待创建索引的字段列表\n        :type SelectedFields: list of FieldInfo\n        :param ShardNum: 索引分片数\n        :type ShardNum: int\n        """
        self.TableGroupId = None
        self.TableName = None
        self.TableInstanceId = None
        self.TableIdlType = None
        self.TableType = None
        self.SelectedFields = None
        self.ShardNum = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableIdlType = params.get("TableIdlType")
        self.TableType = params.get("TableType")
        if params.get("SelectedFields") is not None:
            self.SelectedFields = []
            for item in params.get("SelectedFields"):
                obj = FieldInfo()
                obj._deserialize(item)
                self.SelectedFields.append(obj)
        self.ShardNum = params.get("ShardNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerDetailInfo(AbstractModel):
    """server独占机器的详细信息

    """

    def __init__(self):
        """
        :param ServerUid: svr唯一id\n        :type ServerUid: str\n        :param MachineType: 机器类型\n        :type MachineType: str\n        :param MemoryRate: 内存占用量\n        :type MemoryRate: int\n        :param DiskRate: 磁盘占用量\n        :type DiskRate: int\n        :param ReadNum: 读次数\n        :type ReadNum: int\n        :param WriteNum: 写次数\n        :type WriteNum: int\n        """
        self.ServerUid = None
        self.MachineType = None
        self.MemoryRate = None
        self.DiskRate = None
        self.ReadNum = None
        self.WriteNum = None


    def _deserialize(self, params):
        self.ServerUid = params.get("ServerUid")
        self.MachineType = params.get("MachineType")
        self.MemoryRate = params.get("MemoryRate")
        self.DiskRate = params.get("DiskRate")
        self.ReadNum = params.get("ReadNum")
        self.WriteNum = params.get("WriteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerMachineInfo(AbstractModel):
    """svr的机器列表ServerList

    """

    def __init__(self):
        """
        :param ServerUid: 机器唯一id\n        :type ServerUid: str\n        :param MachineType: 机器类型\n        :type MachineType: str\n        """
        self.ServerUid = None
        self.MachineType = None


    def _deserialize(self, params):
        self.ServerUid = params.get("ServerUid")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableIndexRequest(AbstractModel):
    """SetTableIndex请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表所属集群实例ID\n        :type ClusterId: str\n        :param SelectedTables: 待创建分布式索引表格列表\n        :type SelectedTables: list of SelectedTableWithField\n        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableWithField()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableIndexResponse(AbstractModel):
    """SetTableIndex返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格分布式索引创建结果数量\n        :type TotalCount: int\n        :param TableResults: 表格分布式索引创建结果列表\n        :type TableResults: list of TableResultNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    """快照列表

    """

    def __init__(self):
        """
        :param TableGroupId: 所属表格组ID\n        :type TableGroupId: str\n        :param TableName: 表名称\n        :type TableName: str\n        :param SnapshotName: 快照名称\n        :type SnapshotName: str\n        :param SnapshotTime: 快照时间点\n        :type SnapshotTime: str\n        :param SnapshotDeadTime: 快照过期时间点\n        :type SnapshotDeadTime: str\n        """
        self.TableGroupId = None
        self.TableName = None
        self.SnapshotName = None
        self.SnapshotTime = None
        self.SnapshotDeadTime = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.SnapshotName = params.get("SnapshotName")
        self.SnapshotTime = params.get("SnapshotTime")
        self.SnapshotDeadTime = params.get("SnapshotDeadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotInfoNew(AbstractModel):
    """新的快照过期时间

    """

    def __init__(self):
        """
        :param TableGroupId: 所属表格组ID\n        :type TableGroupId: str\n        :param TableName: 表名称\n        :type TableName: str\n        :param SnapshotName: 快照名称\n        :type SnapshotName: str\n        :param SnapshotDeadTime: 快照过期时间点\n        :type SnapshotDeadTime: str\n        """
        self.TableGroupId = None
        self.TableName = None
        self.SnapshotName = None
        self.SnapshotDeadTime = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.SnapshotName = params.get("SnapshotName")
        self.SnapshotDeadTime = params.get("SnapshotDeadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    """创建快照结果

    """

    def __init__(self):
        """
        :param TableGroupId: 表格所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupId: str\n        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableName: str\n        :param TaskId: 任务ID，对于创建单任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param SnapshotName: 快照名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SnapshotName: str\n        :param SnapshotTime: 快照的时间点
注意：此字段可能返回 null，表示取不到有效值。\n        :type SnapshotTime: str\n        :param SnapshotDeadTime: 快照的过期时间点
注意：此字段可能返回 null，表示取不到有效值。\n        :type SnapshotDeadTime: str\n        :param SnapshotCreateTime: 快照创建时间点
注意：此字段可能返回 null，表示取不到有效值。\n        :type SnapshotCreateTime: str\n        :param SnapshotSize: 快照大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type SnapshotSize: int\n        :param SnapshotStatus: 快照状态，0 生成中 1 正常 2 删除中 3 已失效 4 回档使用中
注意：此字段可能返回 null，表示取不到有效值。\n        :type SnapshotStatus: int\n        """
        self.TableGroupId = None
        self.TableName = None
        self.TaskId = None
        self.Error = None
        self.SnapshotName = None
        self.SnapshotTime = None
        self.SnapshotDeadTime = None
        self.SnapshotCreateTime = None
        self.SnapshotSize = None
        self.SnapshotStatus = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.SnapshotName = params.get("SnapshotName")
        self.SnapshotTime = params.get("SnapshotTime")
        self.SnapshotDeadTime = params.get("SnapshotDeadTime")
        self.SnapshotCreateTime = params.get("SnapshotCreateTime")
        self.SnapshotSize = params.get("SnapshotSize")
        self.SnapshotStatus = params.get("SnapshotStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableGroupInfo(AbstractModel):
    """表格组详细信息

    """

    def __init__(self):
        """
        :param TableGroupId: 表格组ID\n        :type TableGroupId: str\n        :param TableGroupName: 表格组名称\n        :type TableGroupName: str\n        :param CreatedTime: 表格组创建时间\n        :type CreatedTime: str\n        :param TableCount: 表格组包含的表格数量\n        :type TableCount: int\n        :param TotalSize: 表格组包含的表格存储总量（MB）\n        :type TotalSize: int\n        """
        self.TableGroupId = None
        self.TableGroupName = None
        self.CreatedTime = None
        self.TableCount = None
        self.TotalSize = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")
        self.CreatedTime = params.get("CreatedTime")
        self.TableCount = params.get("TableCount")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfoNew(AbstractModel):
    """表格详情信息

    """

    def __init__(self):
        """
        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableName: str\n        :param TableInstanceId: 表格实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableInstanceId: str\n        :param TableType: 表格数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableType: str\n        :param TableIdlType: 表格数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableIdlType: str\n        :param ClusterId: 表格所属集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 表格所属集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param TableGroupId: 表格所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupId: str\n        :param TableGroupName: 表格所属表格组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupName: str\n        :param KeyStruct: 表格主键字段结构json字符串
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyStruct: str\n        :param ValueStruct: 表格非主键字段结构json字符串
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValueStruct: str\n        :param ShardingKeySet: 表格分表因子集合，对PROTO类型表格有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShardingKeySet: str\n        :param IndexStruct: 表格索引键字段集合，对PROTO类型表格有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type IndexStruct: str\n        :param ListElementNum: LIST类型表格元素个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListElementNum: int\n        :param IdlFiles: 表格所关联IDL文件信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type IdlFiles: list of IdlFileInfo\n        :param ReservedVolume: 表格预留容量（GB）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedVolume: int\n        :param ReservedReadQps: 表格预留读CU
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedReadQps: int\n        :param ReservedWriteQps: 表格预留写CU
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedWriteQps: int\n        :param TableSize: 表格实际数据量大小（MB）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableSize: int\n        :param Status: 表格状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param CreatedTime: 表格创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param UpdatedTime: 表格最后一次修改时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdatedTime: str\n        :param Memo: 表格备注信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Memo: str\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param ApiAccessId: TcaplusDB SDK数据访问接入ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAccessId: str\n        :param SortFieldNum: SORTLIST类型表格排序字段个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type SortFieldNum: int\n        :param SortRule: SORTLIST类型表格排序顺序
注意：此字段可能返回 null，表示取不到有效值。\n        :type SortRule: int\n        :param DbClusterInfoStruct: 表格分布式索引信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type DbClusterInfoStruct: str\n        """
        self.TableName = None
        self.TableInstanceId = None
        self.TableType = None
        self.TableIdlType = None
        self.ClusterId = None
        self.ClusterName = None
        self.TableGroupId = None
        self.TableGroupName = None
        self.KeyStruct = None
        self.ValueStruct = None
        self.ShardingKeySet = None
        self.IndexStruct = None
        self.ListElementNum = None
        self.IdlFiles = None
        self.ReservedVolume = None
        self.ReservedReadQps = None
        self.ReservedWriteQps = None
        self.TableSize = None
        self.Status = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.Memo = None
        self.Error = None
        self.ApiAccessId = None
        self.SortFieldNum = None
        self.SortRule = None
        self.DbClusterInfoStruct = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")
        self.KeyStruct = params.get("KeyStruct")
        self.ValueStruct = params.get("ValueStruct")
        self.ShardingKeySet = params.get("ShardingKeySet")
        self.IndexStruct = params.get("IndexStruct")
        self.ListElementNum = params.get("ListElementNum")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.ReservedVolume = params.get("ReservedVolume")
        self.ReservedReadQps = params.get("ReservedReadQps")
        self.ReservedWriteQps = params.get("ReservedWriteQps")
        self.TableSize = params.get("TableSize")
        self.Status = params.get("Status")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Memo = params.get("Memo")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.ApiAccessId = params.get("ApiAccessId")
        self.SortFieldNum = params.get("SortFieldNum")
        self.SortRule = params.get("SortRule")
        self.DbClusterInfoStruct = params.get("DbClusterInfoStruct")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableResultNew(AbstractModel):
    """表处理结果信息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表格实例ID，形如：tcaplus-3be64cbb
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableInstanceId: str\n        :param TaskId: 任务ID，对于创建单任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableName: str\n        :param TableType: 表格数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableType: str\n        :param TableIdlType: 表数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableIdlType: str\n        :param TableGroupId: 表格所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupId: str\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param TaskIds: 任务ID列表，对于创建多任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskIds: list of str\n        :param ApplicationId: 腾讯云申请审核单Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        """
        self.TableInstanceId = None
        self.TaskId = None
        self.TableName = None
        self.TableType = None
        self.TableIdlType = None
        self.TableGroupId = None
        self.Error = None
        self.TaskIds = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TaskId = params.get("TaskId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.TaskIds = params.get("TaskIds")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableRollbackResultNew(AbstractModel):
    """表格回档结果信息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表格实例ID，形如：tcaplus-3be64cbb
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableInstanceId: str\n        :param TaskId: 任务ID，对于创建单任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableName: str\n        :param TableType: 表格数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableType: str\n        :param TableIdlType: 表格数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableIdlType: str\n        :param TableGroupId: 表格所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupId: str\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param TaskIds: 任务ID列表，对于创建多任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskIds: list of str\n        :param FileId: 上传的key文件ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileId: str\n        :param SuccKeyNum: 校验成功Key数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccKeyNum: int\n        :param TotalKeyNum: Key文件中包含总的Key数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalKeyNum: int\n        """
        self.TableInstanceId = None
        self.TaskId = None
        self.TableName = None
        self.TableType = None
        self.TableIdlType = None
        self.TableGroupId = None
        self.Error = None
        self.TaskIds = None
        self.FileId = None
        self.SuccKeyNum = None
        self.TotalKeyNum = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TaskId = params.get("TaskId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.TaskIds = params.get("TaskIds")
        self.FileId = params.get("FileId")
        self.SuccKeyNum = params.get("SuccKeyNum")
        self.TotalKeyNum = params.get("TotalKeyNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfoUnit(AbstractModel):
    """标签信息单元

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagValue: str\n        """
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
        


class TagsInfoOfCluster(AbstractModel):
    """集群的标签信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of TagInfoUnit\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
        self.ClusterId = None
        self.Tags = None
        self.Error = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfTable(AbstractModel):
    """表格标签信息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表格实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableInstanceId: str\n        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableName: str\n        :param TableGroupId: 表格组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupId: str\n        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of TagInfoUnit\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
        self.TableInstanceId = None
        self.TableName = None
        self.TableGroupId = None
        self.Tags = None
        self.Error = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableName = params.get("TableName")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfTableGroup(AbstractModel):
    """表格组标签信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param TableGroupId: 表格组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableGroupId: str\n        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of TagInfoUnit\n        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
        self.ClusterId = None
        self.TableGroupId = None
        self.Tags = None
        self.Error = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfoNew(AbstractModel):
    """任务信息详情

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: str\n        :param TaskType: 任务类型\n        :type TaskType: str\n        :param TransId: 任务所关联的TcaplusDB内部事务ID\n        :type TransId: str\n        :param ClusterId: 任务所属集群ID\n        :type ClusterId: str\n        :param ClusterName: 任务所属集群名称\n        :type ClusterName: str\n        :param Progress: 任务进度\n        :type Progress: int\n        :param StartTime: 任务创建时间\n        :type StartTime: str\n        :param UpdateTime: 任务最后更新时间\n        :type UpdateTime: str\n        :param Operator: 操作者\n        :type Operator: str\n        :param Content: 任务详情\n        :type Content: str\n        """
        self.TaskId = None
        self.TaskType = None
        self.TransId = None
        self.ClusterId = None
        self.ClusterName = None
        self.Progress = None
        self.StartTime = None
        self.UpdateTime = None
        self.Operator = None
        self.Content = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.TransId = params.get("TransId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Progress = params.get("Progress")
        self.StartTime = params.get("StartTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Operator = params.get("Operator")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApplyRequest(AbstractModel):
    """UpdateApply请求参数结构体

    """

    def __init__(self):
        """
        :param ApplyStatus: 申请单状态\n        :type ApplyStatus: list of ApplyStatus\n        """
        self.ApplyStatus = None


    def _deserialize(self, params):
        if params.get("ApplyStatus") is not None:
            self.ApplyStatus = []
            for item in params.get("ApplyStatus"):
                obj = ApplyStatus()
                obj._deserialize(item)
                self.ApplyStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApplyResponse(AbstractModel):
    """UpdateApply返回参数结构体

    """

    def __init__(self):
        """
        :param ApplyResults: 已更新的申请单列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplyResults: list of ApplyResult\n        :param TotalCount: 更新数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ApplyResults = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplyResults") is not None:
            self.ApplyResults = []
            for item in params.get("ApplyResults"):
                obj = ApplyResult()
                obj._deserialize(item)
                self.ApplyResults.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class VerifyIdlFilesRequest(AbstractModel):
    """VerifyIdlFiles请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待创建表格的集群ID\n        :type ClusterId: str\n        :param TableGroupId: 待创建表格的表格组ID\n        :type TableGroupId: str\n        :param ExistingIdlFiles: 曾经上传过的IDL文件信息列表，与NewIdlFiles至少有一者\n        :type ExistingIdlFiles: list of IdlFileInfo\n        :param NewIdlFiles: 待上传的IDL文件信息列表，与ExistingIdlFiles至少有一者\n        :type NewIdlFiles: list of IdlFileInfo\n        """
        self.ClusterId = None
        self.TableGroupId = None
        self.ExistingIdlFiles = None
        self.NewIdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("ExistingIdlFiles") is not None:
            self.ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self.NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.NewIdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyIdlFilesResponse(AbstractModel):
    """VerifyIdlFiles返回参数结构体

    """

    def __init__(self):
        """
        :param IdlFiles: 本次上传校验所有的IDL文件信息列表\n        :type IdlFiles: list of IdlFileInfo\n        :param TotalCount: 读取IDL描述文件后解析出的合法表数量，不包含已经创建的表\n        :type TotalCount: int\n        :param TableInfos: 读取IDL描述文件后解析出的合法表列表，不包含已经创建的表\n        :type TableInfos: list of ParsedTableInfoNew\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IdlFiles = None
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")