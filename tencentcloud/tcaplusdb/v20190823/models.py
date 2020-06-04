# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class ClearTablesRequest(AbstractModel):
    """ClearTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表所属集群实例ID
        :type ClusterId: str
        :param SelectedTables: 待清理表信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
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


class ClearTablesResponse(AbstractModel):
    """ClearTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 清除表结果数量
        :type TotalCount: int
        :param TableResults: 清除表结果列表
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Region: 集群所在地域
        :type Region: str
        :param IdlType: 集群数据描述语言类型，如：`PROTO`,`TDR`
        :type IdlType: str
        :param NetworkType: 网络类型
        :type NetworkType: str
        :param VpcId: 集群关联的用户私有网络实例ID
        :type VpcId: str
        :param SubnetId: 集群关联的用户子网实例ID
        :type SubnetId: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param Password: 集群密码
        :type Password: str
        :param PasswordStatus: 密码状态
        :type PasswordStatus: str
        :param ApiAccessId: TcaplusDB SDK连接参数，接入ID
        :type ApiAccessId: str
        :param ApiAccessIp: TcaplusDB SDK连接参数，接入地址
        :type ApiAccessIp: str
        :param ApiAccessPort: TcaplusDB SDK连接参数，接入端口
        :type ApiAccessPort: int
        :param OldPasswordExpireTime: 如果PasswordStatus是unmodifiable说明有旧密码还未过期，此字段将显示旧密码过期的时间，否则为空
注意：此字段可能返回 null，表示取不到有效值。
        :type OldPasswordExpireTime: str
        """
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


class CompareIdlFilesRequest(AbstractModel):
    """CompareIdlFiles请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待修改表格所在集群ID
        :type ClusterId: str
        :param SelectedTables: 待修改表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param ExistingIdlFiles: 选中的已上传IDL文件列表，与NewIdlFiles必选其一
        :type ExistingIdlFiles: list of IdlFileInfo
        :param NewIdlFiles: 本次上传IDL文件列表，与ExistingIdlFiles必选其一
        :type NewIdlFiles: list of IdlFileInfo
        """
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


class CompareIdlFilesResponse(AbstractModel):
    """CompareIdlFiles返回参数结构体

    """

    def __init__(self):
        """
        :param IdlFiles: 本次上传校验所有的IDL文件信息列表
        :type IdlFiles: list of IdlFileInfo
        :param TotalCount: 本次校验合法的表格数量
        :type TotalCount: int
        :param TableInfos: 读取IDL描述文件后,根据用户指示的所选中表格解析校验结果
        :type TableInfos: list of ParsedTableInfoNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待创建备份表所属集群ID
        :type ClusterId: str
        :param SelectedTables: 待创建备份表信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param Remark: 备注信息
        :type Remark: str
        """
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


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        """
        :param TaskIds: 创建的备份任务ID列表
        :type TaskIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param IdlType: 集群数据描述语言类型，如：`PROTO`，`TDR`或`MIX`
        :type IdlType: str
        :param ClusterName: 集群名称，可使用中文或英文字符，最大长度32个字符
        :type ClusterName: str
        :param VpcId: 集群所绑定的私有网络实例ID，形如：vpc-f49l6u0z
        :type VpcId: str
        :param SubnetId: 集群所绑定的子网实例ID，形如：subnet-pxir56ns
        :type SubnetId: str
        :param Password: 集群访问密码，必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母
        :type Password: str
        :param ResourceTags: 集群标签列表
        :type ResourceTags: list of TagInfoUnit
        """
        self.IdlType = None
        self.ClusterName = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.ResourceTags = None


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


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateTableGroupRequest(AbstractModel):
    """CreateTableGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格组所属集群ID
        :type ClusterId: str
        :param TableGroupName: 表格组名称，可以采用中文、英文或数字字符，最大长度32个字符
        :type TableGroupName: str
        :param TableGroupId: 表格组ID，可以由用户指定，但在同一个集群内不能重复，如果不指定则采用自增的模式
        :type TableGroupId: str
        :param ResourceTags: 表格组标签列表
        :type ResourceTags: list of TagInfoUnit
        """
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


class CreateTableGroupResponse(AbstractModel):
    """CreateTableGroup返回参数结构体

    """

    def __init__(self):
        """
        :param TableGroupId: 创建成功的表格组ID
        :type TableGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 待创建表格所属集群ID
        :type ClusterId: str
        :param IdlFiles: 用户选定的建表格IDL文件列表
        :type IdlFiles: list of IdlFileInfo
        :param SelectedTables: 待创建表格信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param ResourceTags: 表格标签列表
        :type ResourceTags: list of TagInfoUnit
        """
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


class CreateTablesResponse(AbstractModel):
    """CreateTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批量创建表格结果数量
        :type TotalCount: int
        :param TableResults: 批量创建表格结果列表
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 待删除的集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 删除集群生成的任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: IDL所属集群ID
        :type ClusterId: str
        :param IdlFiles: 待删除的IDL文件信息列表
        :type IdlFiles: list of IdlFileInfo
        """
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


class DeleteIdlFilesResponse(AbstractModel):
    """DeleteIdlFiles返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果记录数量
        :type TotalCount: int
        :param IdlFileInfos: 删除结果
        :type IdlFileInfos: list of IdlFileInfoWithoutContent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DeleteTableGroupRequest(AbstractModel):
    """DeleteTableGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格组所属的集群ID
        :type ClusterId: str
        :param TableGroupId: 表格组ID
        :type TableGroupId: str
        """
        self.ClusterId = None
        self.TableGroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")


class DeleteTableGroupResponse(AbstractModel):
    """DeleteTableGroup返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 删除表格组所创建的任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteTablesRequest(AbstractModel):
    """DeleteTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待删除表所在集群ID
        :type ClusterId: str
        :param SelectedTables: 待删除表信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
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


class DeleteTablesResponse(AbstractModel):
    """DeleteTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 删除表结果数量
        :type TotalCount: int
        :param TableResults: 删除表结果详情列表
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeClusterTagsRequest(AbstractModel):
    """DescribeClusterTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterIds: 集群ID列表
        :type ClusterIds: list of str
        """
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")


class DescribeClusterTagsResponse(AbstractModel):
    """DescribeClusterTags返回参数结构体

    """

    def __init__(self):
        """
        :param Rows: 集群标签信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rows: list of TagsInfoOfCluster
        :param TotalCount: 返回结果个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterIds: 指定查询的集群ID列表
        :type ClusterIds: list of str
        :param Filters: 查询过滤条件
        :type Filters: list of Filter
        :param Offset: 查询列表偏移量
        :type Offset: int
        :param Limit: 查询列表返回记录数，默认值20
        :type Limit: int
        """
        self.ClusterIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


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


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群实例数
        :type TotalCount: int
        :param Clusters: 集群实例列表
        :type Clusters: list of ClusterInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 文件所属集群ID
        :type ClusterId: str
        :param TableGroupIds: 文件所属表格组ID
        :type TableGroupIds: list of str
        :param IdlFileIds: 指定文件ID列表
        :type IdlFileIds: list of str
        :param Offset: 查询列表偏移量
        :type Offset: int
        :param Limit: 查询列表返回记录数
        :type Limit: int
        """
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


class DescribeIdlFileInfosResponse(AbstractModel):
    """DescribeIdlFileInfos返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 文件数量
        :type TotalCount: int
        :param IdlFileInfos: 文件详情列表
        :type IdlFileInfos: list of IdlFileInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 可用区详情结果数量
        :type TotalCount: int
        :param RegionInfos: 可用区详情结果列表
        :type RegionInfos: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeTableGroupTagsRequest(AbstractModel):
    """DescribeTableGroupTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待查询标签表格组所属集群ID
        :type ClusterId: str
        :param TableGroupIds: 待查询标签表格组ID列表
        :type TableGroupIds: list of str
        """
        self.ClusterId = None
        self.TableGroupIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")


class DescribeTableGroupTagsResponse(AbstractModel):
    """DescribeTableGroupTags返回参数结构体

    """

    def __init__(self):
        """
        :param Rows: 表格组标签信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rows: list of TagsInfoOfTableGroup
        :param TotalCount: 返回结果个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 表格组所属集群ID
        :type ClusterId: str
        :param TableGroupIds: 表格组ID列表
        :type TableGroupIds: list of str
        :param Filters: 过滤条件，本接口支持：TableGroupName，TableGroupId
        :type Filters: list of Filter
        :param Offset: 查询列表偏移量
        :type Offset: int
        :param Limit: 查询列表返回记录数
        :type Limit: int
        """
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


class DescribeTableGroupsResponse(AbstractModel):
    """DescribeTableGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格组数量
        :type TotalCount: int
        :param TableGroups: 表格组信息列表
        :type TableGroups: list of TableGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 表格所属集群ID
        :type ClusterId: str
        :param SelectedTables: 表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
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


class DescribeTableTagsResponse(AbstractModel):
    """DescribeTableTags返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回结果总数
        :type TotalCount: int
        :param Rows: 表格标签信息列表
        :type Rows: list of TagsInfoOfTable
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 待查询表格所属集群ID
        :type ClusterId: str
        :param TableGroupIds: 待查询表格所属表格组ID列表
        :type TableGroupIds: list of str
        :param Filters: 过滤条件，本接口支持：TableName，TableInstanceId
        :type Filters: list of Filter
        :param Offset: 查询结果偏移量
        :type Offset: int
        :param Limit: 查询结果返回记录数量
        :type Limit: int
        """
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


class DescribeTablesInRecycleResponse(AbstractModel):
    """DescribeTablesInRecycle返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格数量
        :type TotalCount: int
        :param TableInfos: 表格详情结果列表
        :type TableInfos: list of TableInfoNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 待查询表格所属集群ID
        :type ClusterId: str
        :param TableGroupIds: 待查询表格所属表格组ID列表
        :type TableGroupIds: list of str
        :param SelectedTables: 待查询表格信息列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param Filters: 过滤条件，本接口支持：TableName，TableInstanceId
        :type Filters: list of Filter
        :param Offset: 查询结果偏移量
        :type Offset: int
        :param Limit: 查询结果返回记录数量
        :type Limit: int
        """
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


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格数量
        :type TotalCount: int
        :param TableInfos: 表格详情结果列表
        :type TableInfos: list of TableInfoNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterIds: 需要查询任务所属的集群ID列表
        :type ClusterIds: list of str
        :param TaskIds: 需要查询的任务ID列表
        :type TaskIds: list of str
        :param Filters: 过滤条件，本接口支持：Content，TaskType, Operator, Time
        :type Filters: list of Filter
        :param Offset: 查询列表偏移量
        :type Offset: int
        :param Limit: 查询列表返回记录数
        :type Limit: int
        """
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


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 任务数量
        :type TotalCount: int
        :param TaskInfos: 查询到的任务详情列表
        :type TaskInfos: list of TaskInfoNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Result: 查询结果：`FALSE` 否；`TRUE` 是
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ErrorInfo(AbstractModel):
    """描述每个实例（应用，大区或表）处理过程中可能出现的错误详情。

    """

    def __init__(self):
        """
        :param Code: 错误码
        :type Code: str
        :param Message: 错误信息
        :type Message: str
        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        """
        :param Name: 过滤字段名
        :type Name: str
        :param Value: 过滤字段值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class IdlFileInfo(AbstractModel):
    """表定义描述文件详情，包含文件内容

    """

    def __init__(self):
        """
        :param FileName: 文件名称，不包含扩展名
        :type FileName: str
        :param FileType: 数据描述语言（IDL）类型
        :type FileType: str
        :param FileExtType: 文件扩展名
        :type FileExtType: str
        :param FileSize: 文件大小（Bytes）
        :type FileSize: int
        :param FileId: 文件ID，对于已上传的文件有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: int
        :param FileContent: 文件内容，对于本次新上传的文件有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type FileContent: str
        """
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


class IdlFileInfoWithoutContent(AbstractModel):
    """表定义描述文件详情，不包含文件内容

    """

    def __init__(self):
        """
        :param FileName: 文件名称，不包含扩展名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileType: 数据描述语言（IDL）类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param FileExtType: 文件扩展名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileExtType: str
        :param FileSize: 文件大小（Bytes）
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param FileId: 文件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: int
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
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


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 需要修改名称的集群ID
        :type ClusterId: str
        :param ClusterName: 需要修改的集群名称，可使用中文或英文字符，最大长度32个字符
        :type ClusterName: str
        """
        self.ClusterId = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterPasswordRequest(AbstractModel):
    """ModifyClusterPassword请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 需要修改密码的集群ID
        :type ClusterId: str
        :param OldPassword: 集群旧密码
        :type OldPassword: str
        :param OldPasswordExpireTime: 集群旧密码预期失效时间
        :type OldPasswordExpireTime: str
        :param NewPassword: 集群新密码，密码必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母
        :type NewPassword: str
        :param Mode: 更新模式： `1` 更新密码；`2` 更新旧密码失效时间，默认为`1` 模式
        :type Mode: str
        """
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


class ModifyClusterPasswordResponse(AbstractModel):
    """ModifyClusterPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterTagsRequest(AbstractModel):
    """ModifyClusterTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待修改标签的集群ID
        :type ClusterId: str
        :param ReplaceTags: 待增加或修改的标签列表
        :type ReplaceTags: list of TagInfoUnit
        :param DeleteTags: 待删除的标签
        :type DeleteTags: list of TagInfoUnit
        """
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


class ModifyClusterTagsResponse(AbstractModel):
    """ModifyClusterTags返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyTableGroupNameRequest(AbstractModel):
    """ModifyTableGroupName请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表格组所属的集群ID
        :type ClusterId: str
        :param TableGroupId: 待修改名称的表格组ID
        :type TableGroupId: str
        :param TableGroupName: 新的表格组名称，可以使用中英文字符和符号
        :type TableGroupName: str
        """
        self.ClusterId = None
        self.TableGroupId = None
        self.TableGroupName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")


class ModifyTableGroupNameResponse(AbstractModel):
    """ModifyTableGroupName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTableGroupTagsRequest(AbstractModel):
    """ModifyTableGroupTags请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待修改标签表格组所属集群ID
        :type ClusterId: str
        :param TableGroupId: 待修改标签表格组ID
        :type TableGroupId: str
        :param ReplaceTags: 待增加或修改的标签列表
        :type ReplaceTags: list of TagInfoUnit
        :param DeleteTags: 待删除的标签
        :type DeleteTags: list of TagInfoUnit
        """
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


class ModifyTableGroupTagsResponse(AbstractModel):
    """ModifyTableGroupTags返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 表所属集群实例ID
        :type ClusterId: str
        :param TableMemos: 选定表详情列表
        :type TableMemos: list of SelectedTableInfoNew
        """
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


class ModifyTableMemosResponse(AbstractModel):
    """ModifyTableMemos返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表备注修改结果数量
        :type TotalCount: int
        :param TableResults: 表备注修改结果列表
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 带扩缩容表所属集群ID
        :type ClusterId: str
        :param TableQuotas: 已选中待修改的表配额列表
        :type TableQuotas: list of SelectedTableInfoNew
        """
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


class ModifyTableQuotasResponse(AbstractModel):
    """ModifyTableQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 扩缩容结果数量
        :type TotalCount: int
        :param TableResults: 扩缩容结果列表
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 待修改标签表格所属集群ID
        :type ClusterId: str
        :param SelectedTables: 待修改标签表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param ReplaceTags: 待增加或修改的标签列表
        :type ReplaceTags: list of TagInfoUnit
        :param DeleteTags: 待删除的标签列表
        :type DeleteTags: list of TagInfoUnit
        """
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


class ModifyTableTagsResponse(AbstractModel):
    """ModifyTableTags返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回结果总数
        :type TotalCount: int
        :param TableResults: 返回结果
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ClusterId: 待修改表格所在集群ID
        :type ClusterId: str
        :param IdlFiles: 选中的改表IDL文件
        :type IdlFiles: list of IdlFileInfo
        :param SelectedTables: 待改表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        """
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


class ModifyTablesResponse(AbstractModel):
    """ModifyTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 修改表结果数量
        :type TotalCount: int
        :param TableResults: 修改表结果列表
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param TableInstanceId: 表格实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表格数据结构类型：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableType: str
        :param KeyFields: 主键字段信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyFields: str
        :param OldKeyFields: 原主键字段信息，改表校验时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type OldKeyFields: str
        :param ValueFields: 非主键字段信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueFields: str
        :param OldValueFields: 原非主键字段信息，改表校验时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type OldValueFields: str
        :param TableGroupId: 所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param SumKeyFieldSize: 主键字段总大小
注意：此字段可能返回 null，表示取不到有效值。
        :type SumKeyFieldSize: int
        :param SumValueFieldSize: 非主键字段总大小
注意：此字段可能返回 null，表示取不到有效值。
        :type SumValueFieldSize: int
        :param IndexKeySet: 索引键集合
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexKeySet: str
        :param ShardingKeySet: 分表因子集合
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardingKeySet: str
        :param TdrVersion: TDR版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type TdrVersion: int
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param ListElementNum: LIST类型表格元素个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ListElementNum: int
        :param SortFieldNum: SORTLIST类型表格排序字段个数
注意：此字段可能返回 null，表示取不到有效值。
        :type SortFieldNum: int
        :param SortRule: SORTLIST类型表格排序顺序
注意：此字段可能返回 null，表示取不到有效值。
        :type SortRule: int
        """
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


class RecoverRecycleTablesRequest(AbstractModel):
    """RecoverRecycleTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 表所在集群ID
        :type ClusterId: str
        :param SelectedTables: 待恢复表信息
        :type SelectedTables: list of SelectedTableInfoNew
        """
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


class RecoverRecycleTablesResponse(AbstractModel):
    """RecoverRecycleTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 恢复表结果数量
        :type TotalCount: int
        :param TableResults: 恢复表信息列表
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param RegionName: 地域Ap-Code
        :type RegionName: str
        :param RegionAbbr: 地域缩写
        :type RegionAbbr: str
        :param RegionId: 地域ID
        :type RegionId: int
        """
        self.RegionName = None
        self.RegionAbbr = None
        self.RegionId = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.RegionAbbr = params.get("RegionAbbr")
        self.RegionId = params.get("RegionId")


class RollbackTablesRequest(AbstractModel):
    """RollbackTables请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待回档表格所在集群ID
        :type ClusterId: str
        :param SelectedTables: 待回档表格列表
        :type SelectedTables: list of SelectedTableInfoNew
        :param RollbackTime: 待回档时间
        :type RollbackTime: str
        :param Mode: 回档模式，支持：`KEYS`
        :type Mode: str
        """
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


class RollbackTablesResponse(AbstractModel):
    """RollbackTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表格回档任务结果数量
        :type TotalCount: int
        :param TableResults: 表格回档任务结果列表
        :type TableResults: list of TableRollbackResultNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param TableGroupId: 表所属表格组ID
        :type TableGroupId: str
        :param TableName: 表格名称
        :type TableName: str
        :param TableInstanceId: 表实例ID
        :type TableInstanceId: str
        :param TableIdlType: 表格描述语言类型：`PROTO`或`TDR`
        :type TableIdlType: str
        :param TableType: 表格数据结构类型：`GENERIC`或`LIST`
        :type TableType: str
        :param ListElementNum: LIST表元素个数
        :type ListElementNum: int
        :param ReservedVolume: 表格预留容量（GB）
        :type ReservedVolume: int
        :param ReservedReadQps: 表格预留读CU
        :type ReservedReadQps: int
        :param ReservedWriteQps: 表格预留写CU
        :type ReservedWriteQps: int
        :param Memo: 表格备注信息
        :type Memo: str
        :param FileName: Key回档文件名，回档专用
        :type FileName: str
        :param FileExtType: Key回档文件扩展名，回档专用
        :type FileExtType: str
        :param FileSize: Key回档文件大小，回档专用
        :type FileSize: int
        :param FileContent: Key回档文件内容，回档专用
        :type FileContent: str
        """
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


class TableGroupInfo(AbstractModel):
    """表格组详细信息

    """

    def __init__(self):
        """
        :param TableGroupId: 表格组ID
        :type TableGroupId: str
        :param TableGroupName: 表格组名称
        :type TableGroupName: str
        :param CreatedTime: 表格组创建时间
        :type CreatedTime: str
        :param TableCount: 表格组包含的表格数量
        :type TableCount: int
        :param TotalSize: 表格组包含的表格存储总量（MB）
        :type TotalSize: int
        """
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


class TableInfoNew(AbstractModel):
    """表格详情信息

    """

    def __init__(self):
        """
        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableInstanceId: 表格实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TableType: 表格数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表格数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param ClusterId: 表格所属集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 表格所属集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param TableGroupId: 表格所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param TableGroupName: 表格所属表格组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableGroupName: str
        :param KeyStruct: 表格主键字段结构json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyStruct: str
        :param ValueStruct: 表格非主键字段结构json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueStruct: str
        :param ShardingKeySet: 表格分表因子集合，对PROTO类型表格有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardingKeySet: str
        :param IndexStruct: 表格索引键字段集合，对PROTO类型表格有效
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStruct: str
        :param ListElementNum: LIST类型表格元素个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ListElementNum: int
        :param IdlFiles: 表格所关联IDL文件信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IdlFiles: list of IdlFileInfo
        :param ReservedVolume: 表格预留容量（GB）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedVolume: int
        :param ReservedReadQps: 表格预留读CU
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedReadQps: int
        :param ReservedWriteQps: 表格预留写CU
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedWriteQps: int
        :param TableSize: 表格实际数据量大小（MB）
注意：此字段可能返回 null，表示取不到有效值。
        :type TableSize: int
        :param Status: 表格状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param CreatedTime: 表格创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param UpdatedTime: 表格最后一次修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param Memo: 表格备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Memo: str
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param ApiAccessId: TcaplusDB SDK数据访问接入ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAccessId: str
        :param SortFieldNum: SORTLIST类型表格排序字段个数
注意：此字段可能返回 null，表示取不到有效值。
        :type SortFieldNum: int
        :param SortRule: SORTLIST类型表格排序顺序
注意：此字段可能返回 null，表示取不到有效值。
        :type SortRule: int
        :param DbClusterInfoStruct: 表格分布式索引信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DbClusterInfoStruct: str
        """
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


class TableResultNew(AbstractModel):
    """表处理结果信息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表格实例ID，形如：tcaplus-3be64cbb
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TaskId: 任务ID，对于创建单任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表格数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param TableGroupId: 表格所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param TaskIds: 任务ID列表，对于创建多任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskIds: list of str
        """
        self.TableInstanceId = None
        self.TaskId = None
        self.TableName = None
        self.TableType = None
        self.TableIdlType = None
        self.TableGroupId = None
        self.Error = None
        self.TaskIds = None


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


class TableRollbackResultNew(AbstractModel):
    """表格回档结果信息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表格实例ID，形如：tcaplus-3be64cbb
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TaskId: 任务ID，对于创建单任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表格数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表格数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param TableGroupId: 表格所属表格组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param TaskIds: 任务ID列表，对于创建多任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskIds: list of str
        :param FileId: 上传的key文件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param SuccKeyNum: 校验成功Key数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccKeyNum: int
        :param TotalKeyNum: Key文件中包含总的Key数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalKeyNum: int
        """
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


class TagInfoUnit(AbstractModel):
    """标签信息单元

    """

    def __init__(self):
        """
        :param TagKey: 标签键
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


class TagsInfoOfCluster(AbstractModel):
    """集群的标签信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfoUnit
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
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


class TagsInfoOfTable(AbstractModel):
    """表格标签信息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表格实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TableName: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableGroupId: 表格组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfoUnit
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
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


class TagsInfoOfTableGroup(AbstractModel):
    """表格组标签信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param TableGroupId: 表格组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfoUnit
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
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


class TaskInfoNew(AbstractModel):
    """任务信息详情

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        :param TaskType: 任务类型
        :type TaskType: str
        :param TransId: 任务所关联的TcaplusDB内部事务ID
        :type TransId: str
        :param ClusterId: 任务所属集群ID
        :type ClusterId: str
        :param ClusterName: 任务所属集群名称
        :type ClusterName: str
        :param Progress: 任务进度
        :type Progress: int
        :param StartTime: 任务创建时间
        :type StartTime: str
        :param UpdateTime: 任务最后更新时间
        :type UpdateTime: str
        :param Operator: 操作者
        :type Operator: str
        :param Content: 任务详情
        :type Content: str
        """
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


class VerifyIdlFilesRequest(AbstractModel):
    """VerifyIdlFiles请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 待创建表格的集群ID
        :type ClusterId: str
        :param TableGroupId: 待创建表格的表格组ID
        :type TableGroupId: str
        :param ExistingIdlFiles: 曾经上传过的IDL文件信息列表，与NewIdlFiles至少有一者
        :type ExistingIdlFiles: list of IdlFileInfo
        :param NewIdlFiles: 待上传的IDL文件信息列表，与ExistingIdlFiles至少有一者
        :type NewIdlFiles: list of IdlFileInfo
        """
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


class VerifyIdlFilesResponse(AbstractModel):
    """VerifyIdlFiles返回参数结构体

    """

    def __init__(self):
        """
        :param IdlFiles: 本次上传校验所有的IDL文件信息列表
        :type IdlFiles: list of IdlFileInfo
        :param TotalCount: 读取IDL描述文件后解析出的合法表数量，不包含已经创建的表
        :type TotalCount: int
        :param TableInfos: 读取IDL描述文件后解析出的合法表列表，不包含已经创建的表
        :type TableInfos: list of ParsedTableInfoNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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