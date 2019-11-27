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


class AppInfo(AbstractModel):
    """应用实例详细信息

    """

    def __init__(self):
        """
        :param AppName: 应用名称
        :type AppName: str
        :param ApplicationId: 应用实例ID
        :type ApplicationId: str
        :param Region: 所在地域
        :type Region: str
        :param IdlType: 数据描述语言类型，如：`PROTO`,`TDR`或`MIX`
        :type IdlType: str
        :param NetworkType: 网络类型
        :type NetworkType: str
        :param VpcId: 关联的用户私有网络实例ID
        :type VpcId: str
        :param SubnetId: 关联的用户子网实例ID
        :type SubnetId: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param Password: 应用密码
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
        self.AppName = None
        self.ApplicationId = None
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
        self.AppName = params.get("AppName")
        self.ApplicationId = params.get("ApplicationId")
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


class ClearTablesRequest(AbstractModel):
    """ClearTables请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 表所属应用实例ID
        :type ApplicationId: str
        :param SelectedTables: 待清理表信息列表
        :type SelectedTables: list of SelectedTableInfo
        """
        self.ApplicationId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfo()
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
        :type TableResults: list of TableResult
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
                obj = TableResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class CompareIdlFilesRequest(AbstractModel):
    """CompareIdlFiles请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 待修改表所在应用实例ID
        :type ApplicationId: str
        :param SelectedTables: 待修改表列表
        :type SelectedTables: list of SelectedTableInfo
        :param ExistingIdlFiles: 选中的已上传IDL文件列表，与NewIdlFiles必选其一
        :type ExistingIdlFiles: list of IdlFileInfo
        :param NewIdlFiles: 本次上传IDL文件列表，与ExistingIdlFiles必选其一
        :type NewIdlFiles: list of IdlFileInfo
        """
        self.ApplicationId = None
        self.SelectedTables = None
        self.ExistingIdlFiles = None
        self.NewIdlFiles = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfo()
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
        :param IdlFiles: 本次上传校验所有的Idl文件信息列表
        :type IdlFiles: list of IdlFileInfo
        :param TotalCount: 本次校验合法的表数量
        :type TotalCount: int
        :param TableInfos: 读取IDL描述文件后,根据用户指示的所选中表解析校验结果
        :type TableInfos: list of ParsedTableInfo
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
                obj = ParsedTableInfo()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class CreateAppRequest(AbstractModel):
    """CreateApp请求参数结构体

    """

    def __init__(self):
        """
        :param IdlType: 应用数据描述语言类型，如：`PROTO`，`TDR`或`MIX`
        :type IdlType: str
        :param AppName: 应用名称，可使用中文或英文字符，长度在30个字符以内
        :type AppName: str
        :param VpcId: 应用所绑定的私有网络实例ID，形如：vpc-f49l6u0z
        :type VpcId: str
        :param SubnetId: 应用所绑定的子网实例ID，形如：subnet-pxir56ns
        :type SubnetId: str
        :param Password: 应用访问密码，可使用英文和数字字符，长度为12~16个字符
        :type Password: str
        """
        self.IdlType = None
        self.AppName = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None


    def _deserialize(self, params):
        self.IdlType = params.get("IdlType")
        self.AppName = params.get("AppName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")


class CreateAppResponse(AbstractModel):
    """CreateApp返回参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.RequestId = params.get("RequestId")


class CreateTablesRequest(AbstractModel):
    """CreateTables请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 待创建表所属应用实例ID
        :type ApplicationId: str
        :param IdlFiles: 用户选定的建表IDL文件列表
        :type IdlFiles: list of IdlFileInfo
        :param SelectedTables: 待创建表信息列表
        :type SelectedTables: list of SelectedTableInfo
        """
        self.ApplicationId = None
        self.IdlFiles = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfo()
                obj._deserialize(item)
                self.SelectedTables.append(obj)


class CreateTablesResponse(AbstractModel):
    """CreateTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批量创建表结果数量
        :type TotalCount: int
        :param TableResults: 批量创建表结果列表
        :type TableResults: list of TableResult
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
                obj = TableResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 大区所属应用实例ID
        :type ApplicationId: str
        :param ZoneName: 大区名称，可以采用中文、英文或数字字符，长度不能超过30
        :type ZoneName: str
        :param LogicZoneId: 大区ID，可以由用户指定，但在同一个App内不能重复，如果不指定则采用自增的模式
        :type LogicZoneId: str
        """
        self.ApplicationId = None
        self.ZoneName = None
        self.LogicZoneId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ZoneName = params.get("ZoneName")
        self.LogicZoneId = params.get("LogicZoneId")


class CreateZoneResponse(AbstractModel):
    """CreateZone返回参数结构体

    """

    def __init__(self):
        """
        :param LogicZoneId: 创建的大区ID
        :type LogicZoneId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogicZoneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogicZoneId = params.get("LogicZoneId")
        self.RequestId = params.get("RequestId")


class DeleteAppRequest(AbstractModel):
    """DeleteApp请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 待删除的应用实例ID
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")


class DeleteAppResponse(AbstractModel):
    """DeleteApp返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 删除应用生成的任务ID
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
        :param ApplicationId: 应用实例ID
        :type ApplicationId: str
        :param IdlFiles: 待删除的IDL文件信息列表
        :type IdlFiles: list of IdlFileInfo
        """
        self.ApplicationId = None
        self.IdlFiles = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
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


class DeleteTablesRequest(AbstractModel):
    """DeleteTables请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 待删除表所在应用实例ID
        :type ApplicationId: str
        :param SelectedTables: 待删除表信息列表
        :type SelectedTables: list of SelectedTableInfo
        """
        self.ApplicationId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfo()
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
        :type TableResults: list of TableResult
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
                obj = TableResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 大区所属的应用实例ID
        :type ApplicationId: str
        :param LogicZoneId: 大区ID
        :type LogicZoneId: str
        """
        self.ApplicationId = None
        self.LogicZoneId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.LogicZoneId = params.get("LogicZoneId")


class DeleteZoneResponse(AbstractModel):
    """DeleteZone返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 删除大区所创建的任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeAppsRequest(AbstractModel):
    """DescribeApps请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationIds: 指定查询的应用ID
        :type ApplicationIds: list of str
        :param Filters: 查询过滤条件
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 应用列表的大小，默认值20
        :type Limit: int
        """
        self.ApplicationIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationIds = params.get("ApplicationIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAppsResponse(AbstractModel):
    """DescribeApps返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 应用实例数
        :type TotalCount: int
        :param Apps: 应用实例列表
        :type Apps: list of AppInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Apps = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Apps") is not None:
            self.Apps = []
            for item in params.get("Apps"):
                obj = AppInfo()
                obj._deserialize(item)
                self.Apps.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIdlFileInfosRequest(AbstractModel):
    """DescribeIdlFileInfos请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 文件所属应用实例ID
        :type ApplicationId: str
        :param LogicZoneIds: 文件所属大区ID
        :type LogicZoneIds: list of str
        :param IdlFileIds: 指定文件ID
        :type IdlFileIds: list of str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 文件列表大小
        :type Limit: int
        """
        self.ApplicationId = None
        self.LogicZoneIds = None
        self.IdlFileIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.LogicZoneIds = params.get("LogicZoneIds")
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


class DescribeTablesInRecycleRequest(AbstractModel):
    """DescribeTablesInRecycle请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 待查询表所属应用实例ID
        :type ApplicationId: str
        :param LogicZoneIds: 待查询表所属大区列表
        :type LogicZoneIds: list of str
        :param Filters: 过滤条件，本接口支持：TableName，TableInstanceId
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 结果列表数量
        :type Limit: int
        """
        self.ApplicationId = None
        self.LogicZoneIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.LogicZoneIds = params.get("LogicZoneIds")
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
        :param TotalCount: 表数量
        :type TotalCount: int
        :param TableInfos: 表详情结果列表
        :type TableInfos: list of TableInfo
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
                obj = TableInfo()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 待查询表所属应用实例ID
        :type ApplicationId: str
        :param LogicZoneIds: 待查询表所属大区列表
        :type LogicZoneIds: list of str
        :param SelectedTables: 待查询表信息列表
        :type SelectedTables: list of SelectedTableInfo
        :param Filters: 过滤条件，本接口支持：TableName，TableInstanceId
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 结果列表数量
        :type Limit: int
        """
        self.ApplicationId = None
        self.LogicZoneIds = None
        self.SelectedTables = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.LogicZoneIds = params.get("LogicZoneIds")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfo()
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
        :param TotalCount: 表数量
        :type TotalCount: int
        :param TableInfos: 表详情结果列表
        :type TableInfos: list of TableInfo
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
                obj = TableInfo()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationIds: 需要查询任务所属的应用ID列表
        :type ApplicationIds: list of str
        :param TaskIds: 需要查询的任务ID列表
        :type TaskIds: list of str
        :param Filters: 过滤条件，本接口支持：Content，TaskType, Operator, Time
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 任务列表大小
        :type Limit: int
        """
        self.ApplicationIds = None
        self.TaskIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationIds = params.get("ApplicationIds")
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
        :type TaskInfos: list of TaskInfo
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
                obj = TaskInfo()
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


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 大区所属应用实例ID
        :type ApplicationId: str
        :param LogicZoneIds: 大区ID
        :type LogicZoneIds: list of str
        :param Filters: 过滤条件，本接口支持：ZoneName，ZoneId
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 大区列表大小
        :type Limit: int
        """
        self.ApplicationId = None
        self.LogicZoneIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.LogicZoneIds = params.get("LogicZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 大区数量
        :type TotalCount: int
        :param Zones: 大区信息列表
        :type Zones: list of ZoneInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Zones = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.Zones.append(obj)
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


class ModifyAppNameRequest(AbstractModel):
    """ModifyAppName请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 需要修改名称的应用实例ID
        :type ApplicationId: str
        :param AppName: 需要修改的应用名称，需要URLEncode
        :type AppName: str
        """
        self.ApplicationId = None
        self.AppName = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.AppName = params.get("AppName")


class ModifyAppNameResponse(AbstractModel):
    """ModifyAppName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAppPasswordRequest(AbstractModel):
    """ModifyAppPassword请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 需要修改密码的应用实例ID
        :type ApplicationId: str
        :param OldPassword: 应用旧密码
        :type OldPassword: str
        :param OldPasswordExpireTime: 应用旧密码预期失效时间
        :type OldPasswordExpireTime: str
        :param NewPassword: 应用新密码
        :type NewPassword: str
        :param Mode: 更新模式： `1` 更新密码；`2` 更新旧密码失效时间，默认为`1` 模式
        :type Mode: str
        """
        self.ApplicationId = None
        self.OldPassword = None
        self.OldPasswordExpireTime = None
        self.NewPassword = None
        self.Mode = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.OldPassword = params.get("OldPassword")
        self.OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self.NewPassword = params.get("NewPassword")
        self.Mode = params.get("Mode")


class ModifyAppPasswordResponse(AbstractModel):
    """ModifyAppPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTableMemosRequest(AbstractModel):
    """ModifyTableMemos请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 表所属应用实例ID
        :type ApplicationId: str
        :param TableMemos: 选定表详情列表
        :type TableMemos: list of SelectedTableInfo
        """
        self.ApplicationId = None
        self.TableMemos = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("TableMemos") is not None:
            self.TableMemos = []
            for item in params.get("TableMemos"):
                obj = SelectedTableInfo()
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
        :type TableResults: list of TableResult
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
                obj = TableResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTableQuotasRequest(AbstractModel):
    """ModifyTableQuotas请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 带扩缩容表所属应用实例ID
        :type ApplicationId: str
        :param TableQuotas: 已选中待修改的表配额列表
        :type TableQuotas: list of SelectedTableInfo
        """
        self.ApplicationId = None
        self.TableQuotas = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("TableQuotas") is not None:
            self.TableQuotas = []
            for item in params.get("TableQuotas"):
                obj = SelectedTableInfo()
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
        :type TableResults: list of TableResult
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
                obj = TableResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTablesRequest(AbstractModel):
    """ModifyTables请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 待修改表所在应用实例ID
        :type ApplicationId: str
        :param IdlFiles: 选中的改表IDL文件
        :type IdlFiles: list of IdlFileInfo
        :param SelectedTables: 待改表列表
        :type SelectedTables: list of SelectedTableInfo
        """
        self.ApplicationId = None
        self.IdlFiles = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfo()
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
        :type TableResults: list of TableResult
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
                obj = TableResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyZoneNameRequest(AbstractModel):
    """ModifyZoneName请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 大区所属的应用实例ID
        :type ApplicationId: str
        :param LogicZoneId: 待修改名称的大区ID
        :type LogicZoneId: str
        :param ZoneName: 新的大区名称
        :type ZoneName: str
        """
        self.ApplicationId = None
        self.LogicZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.LogicZoneId = params.get("LogicZoneId")
        self.ZoneName = params.get("ZoneName")


class ModifyZoneNameResponse(AbstractModel):
    """ModifyZoneName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ParsedTableInfo(AbstractModel):
    """从表描述文件中解析出来的表信息

    """

    def __init__(self):
        """
        :param TableIdlType: 表描述语言类型：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param TableInstanceId: 表实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表数据类型：`GENERIC`或`TDR`
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
        :param LogicZoneId: 所属大区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicZoneId: str
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
        """
        self.TableIdlType = None
        self.TableInstanceId = None
        self.TableName = None
        self.TableType = None
        self.KeyFields = None
        self.OldKeyFields = None
        self.ValueFields = None
        self.OldValueFields = None
        self.LogicZoneId = None
        self.SumKeyFieldSize = None
        self.SumValueFieldSize = None
        self.IndexKeySet = None
        self.ShardingKeySet = None
        self.TdrVersion = None
        self.Error = None


    def _deserialize(self, params):
        self.TableIdlType = params.get("TableIdlType")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.KeyFields = params.get("KeyFields")
        self.OldKeyFields = params.get("OldKeyFields")
        self.ValueFields = params.get("ValueFields")
        self.OldValueFields = params.get("OldValueFields")
        self.LogicZoneId = params.get("LogicZoneId")
        self.SumKeyFieldSize = params.get("SumKeyFieldSize")
        self.SumValueFieldSize = params.get("SumValueFieldSize")
        self.IndexKeySet = params.get("IndexKeySet")
        self.ShardingKeySet = params.get("ShardingKeySet")
        self.TdrVersion = params.get("TdrVersion")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))


class RecoverRecycleTablesRequest(AbstractModel):
    """RecoverRecycleTables请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 表所在应用实例ID
        :type ApplicationId: str
        :param SelectedTables: 待恢复表信息
        :type SelectedTables: list of SelectedTableInfo
        """
        self.ApplicationId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfo()
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
        :type TableResults: list of TableResult
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
                obj = TableResult()
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
        :param ApplicationId: 待回档表所在应用实例ID
        :type ApplicationId: str
        :param SelectedTables: 待回档表列表
        :type SelectedTables: list of SelectedTableInfo
        :param RollbackTime: 待回档时间
        :type RollbackTime: str
        :param Mode: 回档模式，支持：`KEYS`
        :type Mode: str
        """
        self.ApplicationId = None
        self.SelectedTables = None
        self.RollbackTime = None
        self.Mode = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfo()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.RollbackTime = params.get("RollbackTime")
        self.Mode = params.get("Mode")


class RollbackTablesResponse(AbstractModel):
    """RollbackTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表回档任务结果数量
        :type TotalCount: int
        :param TableResults: 表回档任务结果列表
        :type TableResults: list of TableRollbackResult
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
                obj = TableRollbackResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class SelectedTableInfo(AbstractModel):
    """被选中的表信息

    """

    def __init__(self):
        """
        :param LogicZoneId: 表所属大区ID
        :type LogicZoneId: str
        :param TableName: 表名称
        :type TableName: str
        :param TableInstanceId: 表实例ID
        :type TableInstanceId: str
        :param TableIdlType: 表描述语言类型：`PROTO`或`TDR`
        :type TableIdlType: str
        :param TableType: 表数据结构类型：`GENERIC`或`LIST`
        :type TableType: str
        :param ListElementNum: LIST表元素个数
        :type ListElementNum: int
        :param ReservedVolume: 表预留容量（GB）
        :type ReservedVolume: int
        :param ReservedReadQps: 表预留读QPS
        :type ReservedReadQps: int
        :param ReservedWriteQps: 表预留写QPS
        :type ReservedWriteQps: int
        :param Memo: 表备注信息
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
        self.LogicZoneId = None
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
        self.LogicZoneId = params.get("LogicZoneId")
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


class TableInfo(AbstractModel):
    """表详情信息

    """

    def __init__(self):
        """
        :param TableName: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableInstanceId: 表实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TableType: 表数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param ApplicationId: 表所属应用实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param AppName: 表所属应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param LogicZoneId: 表所属大区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicZoneId: str
        :param ZoneName: 表所属大区名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param KeyStruct: 表主键结构json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyStruct: str
        :param ValueStruct: 表非主键结构json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueStruct: str
        :param ShardingKeySet: 表分表因子集合，PROTO表有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardingKeySet: str
        :param IndexStruct: 表索引键集合，PROTO表有效
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStruct: str
        :param ListElementNum: LIST表元素个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ListElementNum: int
        :param IdlFiles: 表所关联IDL文件信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IdlFiles: list of IdlFileInfo
        :param ReservedVolume: 表预留容量（GB）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedVolume: int
        :param ReservedReadQps: 表预留读QPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedReadQps: int
        :param ReservedWriteQps: 表预留写QPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedWriteQps: int
        :param TableSize: 表实际数据量大小（MB）
注意：此字段可能返回 null，表示取不到有效值。
        :type TableSize: int
        :param Status: 表状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param CreatedTime: 表创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param UpdatedTime: 最后一次更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param Memo: 表备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Memo: str
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param ApiAccessId: Api接入ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAccessId: str
        """
        self.TableName = None
        self.TableInstanceId = None
        self.TableType = None
        self.TableIdlType = None
        self.ApplicationId = None
        self.AppName = None
        self.LogicZoneId = None
        self.ZoneName = None
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


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.ApplicationId = params.get("ApplicationId")
        self.AppName = params.get("AppName")
        self.LogicZoneId = params.get("LogicZoneId")
        self.ZoneName = params.get("ZoneName")
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


class TableResult(AbstractModel):
    """表处理结果信息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表实例ID，形如：tcaplus-3be64cbb
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TaskId: 任务ID，对于创建单任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param LogicZoneId: 表所属大区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicZoneId: str
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
        self.LogicZoneId = None
        self.Error = None
        self.TaskIds = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TaskId = params.get("TaskId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.LogicZoneId = params.get("LogicZoneId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.TaskIds = params.get("TaskIds")


class TableRollbackResult(AbstractModel):
    """表回档结果信息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表实例ID，形如：tcaplus-3be64cbb
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TaskId: 任务ID，对于创建单任务的接口有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表数据结构类型，如：`GENERIC`或`LIST`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表数据描述语言（IDL）类型，如：`PROTO`或`TDR`
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param LogicZoneId: 表所属大区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicZoneId: str
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
        self.LogicZoneId = None
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
        self.LogicZoneId = params.get("LogicZoneId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.TaskIds = params.get("TaskIds")
        self.FileId = params.get("FileId")
        self.SuccKeyNum = params.get("SuccKeyNum")
        self.TotalKeyNum = params.get("TotalKeyNum")


class TaskInfo(AbstractModel):
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
        :param ApplicationId: 任务所属应用实例ID
        :type ApplicationId: str
        :param AppName: 任务所属应用名称
        :type AppName: str
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
        self.ApplicationId = None
        self.AppName = None
        self.Progress = None
        self.StartTime = None
        self.UpdateTime = None
        self.Operator = None
        self.Content = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.TransId = params.get("TransId")
        self.ApplicationId = params.get("ApplicationId")
        self.AppName = params.get("AppName")
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
        :param ApplicationId: 待加表的应用实例ID
        :type ApplicationId: str
        :param LogicZoneId: 待加表的大区ID
        :type LogicZoneId: str
        :param ExistingIdlFiles: 曾经上传过的IDL文件信息列表，与NewIdlFiles至少有一者
        :type ExistingIdlFiles: list of IdlFileInfo
        :param NewIdlFiles: 待上传的IDL文件信息列表，与ExistingIdlFiles至少有一者
        :type NewIdlFiles: list of IdlFileInfo
        """
        self.ApplicationId = None
        self.LogicZoneId = None
        self.ExistingIdlFiles = None
        self.NewIdlFiles = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.LogicZoneId = params.get("LogicZoneId")
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
        :param IdlFiles: 本次上传校验所有的Idl文件信息列表
        :type IdlFiles: list of IdlFileInfo
        :param TotalCount: 读取Idl描述文件后解析出的合法表数量，不包含已经创建的表
        :type TotalCount: int
        :param TableInfos: 读取Idl描述文件后解析出的合法表列表，不包含已经创建的表
        :type TableInfos: list of ParsedTableInfo
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
                obj = ParsedTableInfo()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class ZoneInfo(AbstractModel):
    """大区详细信息

    """

    def __init__(self):
        """
        :param LogicZoneId: 大区ID
        :type LogicZoneId: str
        :param ZoneName: 大区名称
        :type ZoneName: str
        :param CreatedTime: 大区创建时间
        :type CreatedTime: str
        :param TableCount: 大区表格数量
        :type TableCount: int
        :param TotalSize: 大区表格存储总量（MB）
        :type TotalSize: int
        """
        self.LogicZoneId = None
        self.ZoneName = None
        self.CreatedTime = None
        self.TableCount = None
        self.TotalSize = None


    def _deserialize(self, params):
        self.LogicZoneId = params.get("LogicZoneId")
        self.ZoneName = params.get("ZoneName")
        self.CreatedTime = params.get("CreatedTime")
        self.TableCount = params.get("TableCount")
        self.TotalSize = params.get("TotalSize")