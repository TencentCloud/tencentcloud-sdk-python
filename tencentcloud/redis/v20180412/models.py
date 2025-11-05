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


class Account(AbstractModel):
    r"""子账号信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _AccountName: 账号名称。
        :type AccountName: str
        :param _Remark: 账号描述信息。
        :type Remark: str
        :param _Privilege: 读写权限策略。
- r：只读。
- w：只写。
- rw：读写。
        :type Privilege: str
        :param _ReadonlyPolicy: 只读路由策略。
- master：主节点。
- replication：从节点。
        :type ReadonlyPolicy: list of str
        :param _Status: 子账号状态.
- 1：账号变更中。
- 2：账号有效。
- 4：账号已删除。
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._InstanceId = None
        self._AccountName = None
        self._Remark = None
        self._Privilege = None
        self._ReadonlyPolicy = None
        self._Status = None
        self._CreateTime = None

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        r"""账号名称。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Remark(self):
        r"""账号描述信息。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Privilege(self):
        r"""读写权限策略。
- r：只读。
- w：只写。
- rw：读写。
        :rtype: str
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def ReadonlyPolicy(self):
        r"""只读路由策略。
- master：主节点。
- replication：从节点。
        :rtype: list of str
        """
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Status(self):
        r"""子账号状态.
- 1：账号变更中。
- 2：账号有效。
- 4：账号已删除。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._Remark = params.get("Remark")
        self._Privilege = params.get("Privilege")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddReplicationInstanceRequest(AbstractModel):
    r"""AddReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID。请登录[Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication)页面获取复制组 ID。
        :type GroupId: str
        :param _InstanceId: 实例ID。
- 添加复制组实例有地域与可用区限制。具体信息，请参见[使用限制](https://cloud.tencent.com/document/product/239/71934)。
- 当前仅4.0、5.0 Redis 版集群架构的实例支持加入复制组。
- 请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制需加入复制组的实例 ID。
        :type InstanceId: str
        :param _InstanceRole: 给复制组添加的实例分配角色。<ul><li>rw：可读写。</li><li>r：只读。</li></ul>
        :type InstanceRole: str
        """
        self._GroupId = None
        self._InstanceId = None
        self._InstanceRole = None

    @property
    def GroupId(self):
        r"""复制组ID。请登录[Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication)页面获取复制组 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        r"""实例ID。
- 添加复制组实例有地域与可用区限制。具体信息，请参见[使用限制](https://cloud.tencent.com/document/product/239/71934)。
- 当前仅4.0、5.0 Redis 版集群架构的实例支持加入复制组。
- 请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制需加入复制组的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRole(self):
        r"""给复制组添加的实例分配角色。<ul><li>rw：可读写。</li><li>r：只读。</li></ul>
        :rtype: str
        """
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceRole = params.get("InstanceRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddReplicationInstanceResponse(AbstractModel):
    r"""AddReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步流程ID。
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


class AllocateWanAddressRequest(AbstractModel):
    r"""AllocateWanAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateWanAddressResponse(AbstractModel):
    r"""AllocateWanAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _WanStatus: 开通外网的状态
        :type WanStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._WanStatus = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""异步流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def WanStatus(self):
        r"""开通外网的状态
        :rtype: str
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

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
        self._WanStatus = params.get("WanStatus")
        self._RequestId = params.get("RequestId")


class ApplyParamsTemplateRequest(AbstractModel):
    r"""ApplyParamsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceIds: list of str
        :param _TemplateId: 应用的参数模板ID。
- 请通过接口 [DescribeParamTemplateInfo](https://cloud.tencent.com/document/product/239/58748) 的返回参数 **TemplateId** 获取参数模板 ID。
- 仅当参数模板版本与目标实例的架构版本一致时，操作才能成功执行。版本不匹配将触发执行错误。
        :type TemplateId: str
        """
        self._InstanceIds = None
        self._TemplateId = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def TemplateId(self):
        r"""应用的参数模板ID。
- 请通过接口 [DescribeParamTemplateInfo](https://cloud.tencent.com/document/product/239/58748) 的返回参数 **TemplateId** 获取参数模板 ID。
- 仅当参数模板版本与目标实例的架构版本一致时，操作才能成功执行。版本不匹配将触发执行错误。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyParamsTemplateResponse(AbstractModel):
    r"""ApplyParamsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 任务ID
        :type TaskIds: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskIds = None
        self._RequestId = None

    @property
    def TaskIds(self):
        r"""任务ID
        :rtype: list of int
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

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
        self._RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    r"""AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _SecurityGroupId: 要绑定的安全组ID，请在[控制台安全组](https://console.cloud.tencent.com/vpc/security-group)页面获取安全组 ID。
        :type SecurityGroupId: str
        :param _InstanceIds: 被绑定的实例ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID，支持指定多个实例。
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        r"""数据库引擎名称，本接口取值：redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        r"""要绑定的安全组ID，请在[控制台安全组](https://console.cloud.tencent.com/vpc/security-group)页面获取安全组 ID。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        r"""被绑定的实例ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID，支持指定多个实例。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    r"""AssociateSecurityGroups返回参数结构体

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


class AvailableRegion(AbstractModel):
    r"""可使用的地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _AvailableZones: 可用区信息
        :type AvailableZones: list of str
        """
        self._Region = None
        self._AvailableZones = None

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AvailableZones(self):
        r"""可用区信息
        :rtype: list of str
        """
        return self._AvailableZones

    @AvailableZones.setter
    def AvailableZones(self, AvailableZones):
        self._AvailableZones = AvailableZones


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._AvailableZones = params.get("AvailableZones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadInfo(AbstractModel):
    r"""备份文件下载信息

    """

    def __init__(self):
        r"""
        :param _FileName: 备份文件名称。
        :type FileName: str
        :param _FileSize: 备份文件大小，单位B，如果为0，表示无效。
        :type FileSize: int
        :param _DownloadUrl: 备份文件外网下载地址。下载地址的有效时长为6小时，过期后请重新获取。
        :type DownloadUrl: str
        :param _InnerDownloadUrl: 备份文件内网下载地址。下载地址的有效时长为6小时，过期后请重新获取。
        :type InnerDownloadUrl: str
        """
        self._FileName = None
        self._FileSize = None
        self._DownloadUrl = None
        self._InnerDownloadUrl = None

    @property
    def FileName(self):
        r"""备份文件名称。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""备份文件大小，单位B，如果为0，表示无效。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DownloadUrl(self):
        r"""备份文件外网下载地址。下载地址的有效时长为6小时，过期后请重新获取。
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def InnerDownloadUrl(self):
        r"""备份文件内网下载地址。下载地址的有效时长为6小时，过期后请重新获取。
        :rtype: str
        """
        return self._InnerDownloadUrl

    @InnerDownloadUrl.setter
    def InnerDownloadUrl(self, InnerDownloadUrl):
        self._InnerDownloadUrl = InnerDownloadUrl


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._DownloadUrl = params.get("DownloadUrl")
        self._InnerDownloadUrl = params.get("InnerDownloadUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupLimitVpcItem(AbstractModel):
    r"""已配置的备份文件下载地址对应的 VPC 信息。

    """

    def __init__(self):
        r"""
        :param _Region: 备份文件的下载地址对应VPC 所属的地域。
        :type Region: str
        :param _VpcList: 备份文件下载地址的 VPC 列表。
        :type VpcList: list of str
        """
        self._Region = None
        self._VpcList = None

    @property
    def Region(self):
        r"""备份文件的下载地址对应VPC 所属的地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcList(self):
        r"""备份文件下载地址的 VPC 列表。
        :rtype: list of str
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcList = params.get("VpcList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BigKeyInfo(AbstractModel):
    r"""大Key详情

    """

    def __init__(self):
        r"""
        :param _DB: 所属的database
        :type DB: int
        :param _Key: 大Key
        :type Key: str
        :param _Type: 类型
        :type Type: str
        :param _Size: 大小
        :type Size: int
        :param _Updatetime: 数据时间戳
        :type Updatetime: int
        """
        self._DB = None
        self._Key = None
        self._Type = None
        self._Size = None
        self._Updatetime = None

    @property
    def DB(self):
        r"""所属的database
        :rtype: int
        """
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def Key(self):
        r"""大Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        r"""类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        r"""大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
        r"""数据时间戳
        :rtype: int
        """
        return self._Updatetime

    @Updatetime.setter
    def Updatetime(self, Updatetime):
        self._Updatetime = Updatetime


    def _deserialize(self, params):
        self._DB = params.get("DB")
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Size = params.get("Size")
        self._Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BigKeyTypeInfo(AbstractModel):
    r"""大Key类型分布详情

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: str
        :param _Count: 数量
        :type Count: int
        :param _Size: 大小
        :type Size: int
        :param _Updatetime: 时间戳
        :type Updatetime: int
        """
        self._Type = None
        self._Count = None
        self._Size = None
        self._Updatetime = None

    @property
    def Type(self):
        r"""类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        r"""数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Size(self):
        r"""大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
        r"""时间戳
        :rtype: int
        """
        return self._Updatetime

    @Updatetime.setter
    def Updatetime(self, Updatetime):
        self._Updatetime = Updatetime


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        self._Size = params.get("Size")
        self._Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CDCResource(AbstractModel):
    r"""redis独享集群详细信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户的Appid
        :type AppId: int
        :param _RegionId: 地域id
        :type RegionId: int
        :param _ZoneId: 可用区id
        :type ZoneId: int
        :param _RedisClusterId: redis独享集群id
        :type RedisClusterId: str
        :param _PayMode: 计费模式，1-包年包月，0-按量计费
        :type PayMode: int
        :param _ProjectId: 项目id
        :type ProjectId: int
        :param _AutoRenewFlag: 自动续费标识，0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费
        :type AutoRenewFlag: int
        :param _ClusterName: 独享集群名称
        :type ClusterName: str
        :param _StartTime: 实例创建时间
        :type StartTime: str
        :param _EndTime: 实例到期时间
        :type EndTime: str
        :param _Status: 集群状态：1-流程中，2-运行中，3-已隔离
        :type Status: int
        :param _BaseBundles: 基础管控资源包
        :type BaseBundles: list of ResourceBundle
        :param _ResourceBundles: 资源包列表
        :type ResourceBundles: list of ResourceBundle
        :param _DedicatedClusterId: 所属本地专有集群id
        :type DedicatedClusterId: str
        """
        self._AppId = None
        self._RegionId = None
        self._ZoneId = None
        self._RedisClusterId = None
        self._PayMode = None
        self._ProjectId = None
        self._AutoRenewFlag = None
        self._ClusterName = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._BaseBundles = None
        self._ResourceBundles = None
        self._DedicatedClusterId = None

    @property
    def AppId(self):
        r"""用户的Appid
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RegionId(self):
        r"""地域id
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""可用区id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RedisClusterId(self):
        r"""redis独享集群id
        :rtype: str
        """
        return self._RedisClusterId

    @RedisClusterId.setter
    def RedisClusterId(self, RedisClusterId):
        self._RedisClusterId = RedisClusterId

    @property
    def PayMode(self):
        r"""计费模式，1-包年包月，0-按量计费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

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
    def AutoRenewFlag(self):
        r"""自动续费标识，0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ClusterName(self):
        r"""独享集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def StartTime(self):
        r"""实例创建时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""实例到期时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""集群状态：1-流程中，2-运行中，3-已隔离
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BaseBundles(self):
        r"""基础管控资源包
        :rtype: list of ResourceBundle
        """
        return self._BaseBundles

    @BaseBundles.setter
    def BaseBundles(self, BaseBundles):
        self._BaseBundles = BaseBundles

    @property
    def ResourceBundles(self):
        r"""资源包列表
        :rtype: list of ResourceBundle
        """
        return self._ResourceBundles

    @ResourceBundles.setter
    def ResourceBundles(self, ResourceBundles):
        self._ResourceBundles = ResourceBundles

    @property
    def DedicatedClusterId(self):
        r"""所属本地专有集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._RedisClusterId = params.get("RedisClusterId")
        self._PayMode = params.get("PayMode")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ClusterName = params.get("ClusterName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        if params.get("BaseBundles") is not None:
            self._BaseBundles = []
            for item in params.get("BaseBundles"):
                obj = ResourceBundle()
                obj._deserialize(item)
                self._BaseBundles.append(obj)
        if params.get("ResourceBundles") is not None:
            self._ResourceBundles = []
            for item in params.get("ResourceBundles"):
                obj = ResourceBundle()
                obj._deserialize(item)
                self._ResourceBundles.append(obj)
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeInstanceRoleRequest(AbstractModel):
    r"""ChangeInstanceRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID。请登录[Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication)页面获取复制组 ID。
        :type GroupId: str
        :param _InstanceId: 实例ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _InstanceRole: 实例角色。
- rw：可读写。
- r：只读。
        :type InstanceRole: str
        """
        self._GroupId = None
        self._InstanceId = None
        self._InstanceRole = None

    @property
    def GroupId(self):
        r"""复制组ID。请登录[Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication)页面获取复制组 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        r"""实例ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRole(self):
        r"""实例角色。
- rw：可读写。
- r：只读。
        :rtype: str
        """
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceRole = params.get("InstanceRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeInstanceRoleResponse(AbstractModel):
    r"""ChangeInstanceRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步流程ID
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


class ChangeMasterInstanceRequest(AbstractModel):
    r"""ChangeMasterInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID。创建复制组时，系统自动分配的 ID，是复制组的唯一标识。例如：crs-rpl-m3zt****，请登录[Redis 控制台](https://console.cloud.tencent.com/redis/replication)的全球复制组列表获取复制组 ID。

        :type GroupId: str
        :param _InstanceId: 指定待提升为主实例的只读实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。


        :type InstanceId: str
        :param _ForceSwitch: 标识是否强制提主。
- true：强制提主。
- false：不强制提主。
        :type ForceSwitch: bool
        """
        self._GroupId = None
        self._InstanceId = None
        self._ForceSwitch = None

    @property
    def GroupId(self):
        r"""复制组ID。创建复制组时，系统自动分配的 ID，是复制组的唯一标识。例如：crs-rpl-m3zt****，请登录[Redis 控制台](https://console.cloud.tencent.com/redis/replication)的全球复制组列表获取复制组 ID。

        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        r"""指定待提升为主实例的只读实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。


        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForceSwitch(self):
        r"""标识是否强制提主。
- true：强制提主。
- false：不强制提主。
        :rtype: bool
        """
        return self._ForceSwitch

    @ForceSwitch.setter
    def ForceSwitch(self, ForceSwitch):
        self._ForceSwitch = ForceSwitch


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._InstanceId = params.get("InstanceId")
        self._ForceSwitch = params.get("ForceSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeMasterInstanceResponse(AbstractModel):
    r"""ChangeMasterInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步流程ID。
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


class ChangeReplicaToMasterRequest(AbstractModel):
    r"""ChangeReplicaToMaster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :type InstanceId: str
        :param _GroupId: 副本节点组 ID，请通过接口[DescribeInstanceZoneInfo](https://cloud.tencent.com/document/product/239/50312)获取多 AZ备节点组的 ID 信息。单 AZ，则无需配置该参数。
        :type GroupId: int
        """
        self._InstanceId = None
        self._GroupId = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupId(self):
        r"""副本节点组 ID，请通过接口[DescribeInstanceZoneInfo](https://cloud.tencent.com/document/product/239/50312)获取多 AZ备节点组的 ID 信息。单 AZ，则无需配置该参数。
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeReplicaToMasterResponse(AbstractModel):
    r"""ChangeReplicaToMaster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
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


class CleanUpInstanceRequest(AbstractModel):
    r"""CleanUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录 [Redis 控制台回收站](https://console.cloud.tencent.com/redis/recycle)的实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录 [Redis 控制台回收站](https://console.cloud.tencent.com/redis/recycle)的实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CleanUpInstanceResponse(AbstractModel):
    r"""CleanUpInstance返回参数结构体

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


class ClearInstanceRequest(AbstractModel):
    r"""ClearInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Password: 实例访问密码。
- 免密访问：无需配置。
- 密码认证：必须配置。字符个数为[8,64]，至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种，不能以"/"开头。
        :type Password: str
        :param _EncryptPassword: 是否加密密码
        :type EncryptPassword: bool
        """
        self._InstanceId = None
        self._Password = None
        self._EncryptPassword = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        r"""实例访问密码。
- 免密访问：无需配置。
- 密码认证：必须配置。字符个数为[8,64]，至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种，不能以"/"开头。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EncryptPassword(self):
        r"""是否加密密码
        :rtype: bool
        """
        return self._EncryptPassword

    @EncryptPassword.setter
    def EncryptPassword(self, EncryptPassword):
        self._EncryptPassword = EncryptPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._EncryptPassword = params.get("EncryptPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearInstanceResponse(AbstractModel):
    r"""ClearInstance返回参数结构体

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


class CloneInstancesRequest(AbstractModel):
    r"""CloneInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定待克隆的源实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _GoodsNum: 单次克隆实例的数量。
- 包年包月每次购买最大数量为100。
- 按量计费每次购买最大数量为30。
        :type GoodsNum: int
        :param _ZoneId: 克隆实例所属的可用区ID。当前所支持的可用区 ID，请参见[地域和可用区](https://cloud.tencent.com/document/product/239/4106) 。
        :type ZoneId: int
        :param _BillingMode: 付费方式。<ul><li>0：按量计费。</li><li>1：包年包月。</li></ul>
        :type BillingMode: int
        :param _Period: 购买实例时长。<ul><li>单位：月。</li><li>付费方式选择包年包月计费时，取值范围为[1,2,3,4,5,6,7,8,9,10,11,12,24,36,48,60]。</li><li>付费方式选择按量计费时，设置为1。</li></ul>
        :type Period: int
        :param _SecurityGroupIdList: 安全组ID。请通过 [DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447) 接口获取实例的安全组 ID。
        :type SecurityGroupIdList: list of str
        :param _BackupId: 克隆实例使用的备份ID。请通过接口[DescribeInstanceBackups](https://cloud.tencent.com/document/product/239/20011)获取备份ID。
        :type BackupId: str
        :param _NoAuth: 配置克隆实例是否支持免密访问。开启 SSL 与外网均不支持免密访问。<ul><li>true：免密实例，</li><li>false：非免密实例。默认为非免密实例。</li></ul>
        :type NoAuth: bool
        :param _VpcId: 配置克隆实例的私有网络ID。如果未配置该参数，默认选择基础网络。
        :type VpcId: str
        :param _SubnetId: 配置克隆实例所属私有网络的子网。基础网络时该参数无需配置。
        :type SubnetId: str
        :param _InstanceName: 克隆实例的名称。<br>仅支持长度小于60的中文、英文或者数字，短划线"-"、下划线"_"。</br>
        :type InstanceName: str
        :param _Password: 克隆实例的访问密码。<ul><li>当输入参数<b>NoAuth</b>为<b>true</b>时，可不设置该参数。</li><li>当实例为Redis2.8、4.0和5.0时，其密码格式为：8-30个字符，至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种，不能以"/"开头；</li><li>当实例为CKV 3.2时，其密码格式为：8-30个字符，必须包含字母和数字，且不包含其他字符。</li></ul>
        :type Password: str
        :param _AutoRenew: 自动续费标识。<ul><li>0：默认状态，手动续费。</li><li>1：自动续费。</li><li>2：不自动续费，到期自动隔离。</li></ul>
        :type AutoRenew: int
        :param _VPort: 用户自定义的端口，默认为6379，取值范围[1024,65535]。
        :type VPort: int
        :param _NodeSet: 实例的节点信息。<ul><li>目前支持配置节点的类型（主节点或者副本节点），及其节点的可用区信息。具体信息，请参见[RedisNodeInfo](https://cloud.tencent.com/document/product/239/20022#RedisNodeInfo)。</li><li>单可用区部署可不配置该参数。</li></ul>
        :type NodeSet: list of RedisNodeInfo
        :param _ProjectId: 项目 ID。登录[Redis 控制台](https://console.cloud.tencent.com/redis#/)，可在右上角的<b>账号中心</b> > <b>项目管理</b>中查找项目ID。
        :type ProjectId: int
        :param _ResourceTags: 克隆实例需绑定的标签。
        :type ResourceTags: list of ResourceTag
        :param _TemplateId: 指定克隆实例相关的参数模板 ID。
- 若不配置该参数，则系统会依据所选择的兼容版本及架构，自动适配对应的默认模板。
- 请通过[DescribeParamTemplates](https://cloud.tencent.com/document/product/239/58750)接口，查询实例的参数模板列表，获取模板 ID 编号。
        :type TemplateId: str
        :param _AlarmPolicyList: 指定克隆实例的告警策略 ID。请登录[腾讯云可观测平台控制台](https://console.cloud.tencent.com/monitor/alarm2/policy)，在 <b>告警管理</b> > <b>策略管理</b>页面获取策略 ID 信息。
        :type AlarmPolicyList: list of str
        :param _CloneTime: 克隆指定恢复数据的时间。
仅支持已开通秒级备份的实例

        :type CloneTime: str
        :param _EncryptPassword: 是否加密密码
        :type EncryptPassword: bool
        """
        self._InstanceId = None
        self._GoodsNum = None
        self._ZoneId = None
        self._BillingMode = None
        self._Period = None
        self._SecurityGroupIdList = None
        self._BackupId = None
        self._NoAuth = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceName = None
        self._Password = None
        self._AutoRenew = None
        self._VPort = None
        self._NodeSet = None
        self._ProjectId = None
        self._ResourceTags = None
        self._TemplateId = None
        self._AlarmPolicyList = None
        self._CloneTime = None
        self._EncryptPassword = None

    @property
    def InstanceId(self):
        r"""指定待克隆的源实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GoodsNum(self):
        r"""单次克隆实例的数量。
- 包年包月每次购买最大数量为100。
- 按量计费每次购买最大数量为30。
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def ZoneId(self):
        r"""克隆实例所属的可用区ID。当前所支持的可用区 ID，请参见[地域和可用区](https://cloud.tencent.com/document/product/239/4106) 。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def BillingMode(self):
        r"""付费方式。<ul><li>0：按量计费。</li><li>1：包年包月。</li></ul>
        :rtype: int
        """
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def Period(self):
        r"""购买实例时长。<ul><li>单位：月。</li><li>付费方式选择包年包月计费时，取值范围为[1,2,3,4,5,6,7,8,9,10,11,12,24,36,48,60]。</li><li>付费方式选择按量计费时，设置为1。</li></ul>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupIdList(self):
        r"""安全组ID。请通过 [DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447) 接口获取实例的安全组 ID。
        :rtype: list of str
        """
        return self._SecurityGroupIdList

    @SecurityGroupIdList.setter
    def SecurityGroupIdList(self, SecurityGroupIdList):
        self._SecurityGroupIdList = SecurityGroupIdList

    @property
    def BackupId(self):
        r"""克隆实例使用的备份ID。请通过接口[DescribeInstanceBackups](https://cloud.tencent.com/document/product/239/20011)获取备份ID。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def NoAuth(self):
        r"""配置克隆实例是否支持免密访问。开启 SSL 与外网均不支持免密访问。<ul><li>true：免密实例，</li><li>false：非免密实例。默认为非免密实例。</li></ul>
        :rtype: bool
        """
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def VpcId(self):
        r"""配置克隆实例的私有网络ID。如果未配置该参数，默认选择基础网络。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""配置克隆实例所属私有网络的子网。基础网络时该参数无需配置。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceName(self):
        r"""克隆实例的名称。<br>仅支持长度小于60的中文、英文或者数字，短划线"-"、下划线"_"。</br>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Password(self):
        r"""克隆实例的访问密码。<ul><li>当输入参数<b>NoAuth</b>为<b>true</b>时，可不设置该参数。</li><li>当实例为Redis2.8、4.0和5.0时，其密码格式为：8-30个字符，至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种，不能以"/"开头；</li><li>当实例为CKV 3.2时，其密码格式为：8-30个字符，必须包含字母和数字，且不包含其他字符。</li></ul>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AutoRenew(self):
        r"""自动续费标识。<ul><li>0：默认状态，手动续费。</li><li>1：自动续费。</li><li>2：不自动续费，到期自动隔离。</li></ul>
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def VPort(self):
        r"""用户自定义的端口，默认为6379，取值范围[1024,65535]。
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def NodeSet(self):
        r"""实例的节点信息。<ul><li>目前支持配置节点的类型（主节点或者副本节点），及其节点的可用区信息。具体信息，请参见[RedisNodeInfo](https://cloud.tencent.com/document/product/239/20022#RedisNodeInfo)。</li><li>单可用区部署可不配置该参数。</li></ul>
        :rtype: list of RedisNodeInfo
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def ProjectId(self):
        r"""项目 ID。登录[Redis 控制台](https://console.cloud.tencent.com/redis#/)，可在右上角的<b>账号中心</b> > <b>项目管理</b>中查找项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceTags(self):
        r"""克隆实例需绑定的标签。
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def TemplateId(self):
        r"""指定克隆实例相关的参数模板 ID。
- 若不配置该参数，则系统会依据所选择的兼容版本及架构，自动适配对应的默认模板。
- 请通过[DescribeParamTemplates](https://cloud.tencent.com/document/product/239/58750)接口，查询实例的参数模板列表，获取模板 ID 编号。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def AlarmPolicyList(self):
        r"""指定克隆实例的告警策略 ID。请登录[腾讯云可观测平台控制台](https://console.cloud.tencent.com/monitor/alarm2/policy)，在 <b>告警管理</b> > <b>策略管理</b>页面获取策略 ID 信息。
        :rtype: list of str
        """
        return self._AlarmPolicyList

    @AlarmPolicyList.setter
    def AlarmPolicyList(self, AlarmPolicyList):
        self._AlarmPolicyList = AlarmPolicyList

    @property
    def CloneTime(self):
        r"""克隆指定恢复数据的时间。
仅支持已开通秒级备份的实例

        :rtype: str
        """
        return self._CloneTime

    @CloneTime.setter
    def CloneTime(self, CloneTime):
        self._CloneTime = CloneTime

    @property
    def EncryptPassword(self):
        r"""是否加密密码
        :rtype: bool
        """
        return self._EncryptPassword

    @EncryptPassword.setter
    def EncryptPassword(self, EncryptPassword):
        self._EncryptPassword = EncryptPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GoodsNum = params.get("GoodsNum")
        self._ZoneId = params.get("ZoneId")
        self._BillingMode = params.get("BillingMode")
        self._Period = params.get("Period")
        self._SecurityGroupIdList = params.get("SecurityGroupIdList")
        self._BackupId = params.get("BackupId")
        self._NoAuth = params.get("NoAuth")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceName = params.get("InstanceName")
        self._Password = params.get("Password")
        self._AutoRenew = params.get("AutoRenew")
        self._VPort = params.get("VPort")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._ProjectId = params.get("ProjectId")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._TemplateId = params.get("TemplateId")
        self._AlarmPolicyList = params.get("AlarmPolicyList")
        self._CloneTime = params.get("CloneTime")
        self._EncryptPassword = params.get("EncryptPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneInstancesResponse(AbstractModel):
    r"""CloneInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 交易的ID。
        :type DealId: str
        :param _InstanceIds: 克隆实例的 ID。
        :type InstanceIds: list of str
        :param _DealName: 订单号。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._DealName = None
        self._RequestId = None

    @property
    def DealId(self):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        r"""交易的ID。
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        self._DealId = DealId

    @property
    def InstanceIds(self):
        r"""克隆实例的 ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CloseSSLRequest(AbstractModel):
    r"""CloseSSL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseSSLResponse(AbstractModel):
    r"""CloseSSL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

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


class CommandTake(AbstractModel):
    r"""命令耗时

    """

    def __init__(self):
        r"""
        :param _Cmd: 命令名。
        :type Cmd: str
        :param _Took: 耗时时长。单位：ms。
        :type Took: int
        """
        self._Cmd = None
        self._Took = None

    @property
    def Cmd(self):
        r"""命令名。
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Took(self):
        r"""耗时时长。单位：ms。
        :rtype: int
        """
        return self._Took

    @Took.setter
    def Took(self, Took):
        self._Took = Took


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        self._Took = params.get("Took")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceAccountRequest(AbstractModel):
    r"""CreateInstanceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _AccountName: 自定义的访问数据库的账号名称。
- 仅由字母、数字、下划线、中划线组成。
- 长度不能大于32位。
        :type AccountName: str
        :param _AccountPassword: 设置自定义账号的密码。密码复杂度要求如下：
- 字符个数为[8,64]。
- 至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的两种。
- 不能以"/"开头。

        :type AccountPassword: str
        :param _ReadonlyPolicy: 指定账号的读请求路由分发至主节点或副本节点。未开启副本只读，不支持选择副本节点。
- master：主节点
- replication：副本节点
        :type ReadonlyPolicy: list of str
        :param _Privilege: 账户读写权限，支持选择只读与读写权限。
- r：只读。
- rw: 读写。
        :type Privilege: str
        :param _Remark: 账号备注描述信息，长度为[0,64] 字节，支持中文。
        :type Remark: str
        :param _EncryptPassword: 是否加密密码
        :type EncryptPassword: bool
        """
        self._InstanceId = None
        self._AccountName = None
        self._AccountPassword = None
        self._ReadonlyPolicy = None
        self._Privilege = None
        self._Remark = None
        self._EncryptPassword = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        r"""自定义的访问数据库的账号名称。
- 仅由字母、数字、下划线、中划线组成。
- 长度不能大于32位。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        r"""设置自定义账号的密码。密码复杂度要求如下：
- 字符个数为[8,64]。
- 至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的两种。
- 不能以"/"开头。

        :rtype: str
        """
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def ReadonlyPolicy(self):
        r"""指定账号的读请求路由分发至主节点或副本节点。未开启副本只读，不支持选择副本节点。
- master：主节点
- replication：副本节点
        :rtype: list of str
        """
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Privilege(self):
        r"""账户读写权限，支持选择只读与读写权限。
- r：只读。
- rw: 读写。
        :rtype: str
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def Remark(self):
        r"""账号备注描述信息，长度为[0,64] 字节，支持中文。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def EncryptPassword(self):
        r"""是否加密密码
        :rtype: bool
        """
        return self._EncryptPassword

    @EncryptPassword.setter
    def EncryptPassword(self, EncryptPassword):
        self._EncryptPassword = EncryptPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Privilege = params.get("Privilege")
        self._Remark = params.get("Remark")
        self._EncryptPassword = params.get("EncryptPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceAccountResponse(AbstractModel):
    r"""CreateInstanceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

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


class CreateInstancesRequest(AbstractModel):
    r"""CreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeId: 实例类型。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
- 200：Memcached 1.6 内存版（集群架构）。
**说明**：CKV 版本当前有存量用户使用，暂时保留。
        :type TypeId: int
        :param _MemSize: 内存容量，单位为MB， 数值需为1024的整数倍。具体规格，请通过 [DescribeProductInfo](https://cloud.tencent.com/document/api/239/30600) 接口查询全地域的售卖规格。
- **TypeId**为标准架构时，**MemSize**是实例总内存容量；
- **TypeId**为集群架构时，**MemSize**是单分片内存容量。
        :type MemSize: int
        :param _GoodsNum: 实例数量，单次购买实例数量。具体信息，请通过 [DescribeProductInfo](https://cloud.tencent.com/document/api/239/30600) 接口查询全地域的售卖规格。
        :type GoodsNum: int
        :param _Period: 购买实例的时长。
- 若 **BillingMode**为**1**，即计费方式为包年包月时，需设置该参数，指定所购买实例的时长。单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
- 若 **BillingMode**为**0**，即计费方式为按量计费时，该参数配置为1。
        :type Period: int
        :param _BillingMode: 计费方式。
- 0：按量计费。
- 1：包年包月。
        :type BillingMode: int
        :param _ZoneId: 实例所属的可用区ID，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
        :type ZoneId: int
        :param _Password: 访问实例的密码。
- 当输入参数**NoAuth**为**true**时，指设置实例为免密码访问，Password可不用配置，否则Password为必填参数。
- 当实例类型**TypeId**为Redis 2.8 内存版标准架构、Redis 4.0、5.0、6.2、7.0内存版标准架构或集群架构时，其密码复杂度要求为：8-64个字符，至少包含小写字母、大写字母、数字和字符()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种，不能以"/"开头。
- 当实例类型**TypeId**为CKV 3.2 内存版标准架构或集群架构时，其密码复杂度为：8-30个字符，必须包含字母和数字，且不包含其他字符。
        :type Password: str
        :param _VpcId: 私有网络ID。如果不配置该参数则默认选择基础网络。请登录 [私有网络](https://console.cloud.tencent.com/vpc)控制台查询具体的ID。
        :type VpcId: str
        :param _SubnetId: 私有网络VPC的子网。基础网络下， 该参数无需配置。请登录 [私有网络](https://console.cloud.tencent.com/vpc)控制台查询子网列表获取具体的 ID。
        :type SubnetId: str
        :param _ProjectId: 项目 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)，在右上角的账户信息菜单中，选择**项目管理**查询项目 ID。
        :type ProjectId: int
        :param _AutoRenew: 自动续费标识。
- 0：默认状态（手动续费）。
- 1：自动续费。
- 2：到期不续费。
        :type AutoRenew: int
        :param _SecurityGroupIdList: 安全组 ID 数组。
- 安全组是一种虚拟防火墙，对云数据库实例的网络访问进行控制。创建实例时，建议绑定相应的安全组。
- 请通过 [DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447) 接口获取实例的安全组 ID。
        :type SecurityGroupIdList: list of str
        :param _VPort: 用户自定义的网络端口。默认为6379，范围为 [1024,65535]。
        :type VPort: int
        :param _RedisShardNum: 实例分片数量。
- 标准版实例无需配置该参数。
- 集群版实例，分片数量范围为：[1、3、5、8、12、16、24、32、40、48、64、80、96、128]。
        :type RedisShardNum: int
        :param _RedisReplicasNum: 实例副本数量。
- Redis 内存版 4.0、5.0、6.2、7.0 标准架构和集群架构支持副本数量范围为[1,5]。
- Redis 2.8标准版、CKV标准版只支持1副本。
        :type RedisReplicasNum: int
        :param _ReplicasReadonly: 标识实例是否需支持副本只读。
- Redis 2.8 标准版、CKV标准版不支持副本只读。
- 开启副本只读，实例将自动读写分离，写请求路由到主节点，读请求路由到副本节点。
- 如需开启副本只读，建议副本数量大于等于2。
        :type ReplicasReadonly: bool
        :param _InstanceName: 实例名称。命名要求：仅支持长度小于60的中文、英文或者数字，短划线"-"、下划线"_"。
        :type InstanceName: str
        :param _NoAuth: 配置实例是否支持免密码访问。
- true：免密访问实例。
- false：非免密访问实例。默认为非免密方式，仅VPC网络的实例支持免密码访问。
        :type NoAuth: bool
        :param _NodeSet: 实例的节点信息，包含节点 ID、节点类型、节点可用区 ID等。具体信息，请参见[RedisNodeInfo ](https://cloud.tencent.com/document/product/239/20022)。
目前支持传入节点的类型（主节点或者副本节点），节点的可用区。单可用区部署不需要传递此参数。
        :type NodeSet: list of RedisNodeInfo
        :param _ResourceTags: 给实例设定标签。
        :type ResourceTags: list of ResourceTag
        :param _ZoneName: 指定实例所属的可用区名称。具体信息，请参见[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
        :type ZoneName: str
        :param _TemplateId: 指定实例相关的参数模板 ID。
- 若不配置该参数，则系统会依据所选择的兼容版本及架构，自动适配对应的默认模板。
- 请通过[DescribeParamTemplates](https://cloud.tencent.com/document/product/239/58750)接口，查询实例的参数模板列表，获取模板 ID 编号。
        :type TemplateId: str
        :param _DryRun: 内部参数，标识创建实例是否需要检查。
- false ：默认值。发送正常请求，通过检查后直接创建实例。
- true：发送检查请求，不会创建实例。
        :type DryRun: bool
        :param _ProductVersion: 指实例部署模式。
- local：传统架构，默认为 local。
- cdc：独享集群。
- cloud：云原生，当前已暂停售卖。
        :type ProductVersion: str
        :param _RedisClusterId: 独享集群 ID。

- 当 **ProductVersion** 设置为 **cdc** 时，该参数必须设置。
- 请通过接口[ DescribeRedisClusters](https://cloud.tencent.com/document/product/239/109628) 获取集群 ID。
        :type RedisClusterId: str
        :param _AlarmPolicyList: 告警策略 ID 数组。

- 请登录[腾讯云可观测平台-告警管理-策略管理](https://console.cloud.tencent.com/monitor/alarm/policy)获取告警策略 ID。
- 若不配置该参数，则绑定默认告警策略。默认告警策略具体信息，请登录[腾讯云可观测平台-告警管理-策略管理](https://console.cloud.tencent.com/monitor/alarm/policy)查看。
        :type AlarmPolicyList: list of str
        :param _EncryptPassword: 是否加密密码
        :type EncryptPassword: bool
        """
        self._TypeId = None
        self._MemSize = None
        self._GoodsNum = None
        self._Period = None
        self._BillingMode = None
        self._ZoneId = None
        self._Password = None
        self._VpcId = None
        self._SubnetId = None
        self._ProjectId = None
        self._AutoRenew = None
        self._SecurityGroupIdList = None
        self._VPort = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._ReplicasReadonly = None
        self._InstanceName = None
        self._NoAuth = None
        self._NodeSet = None
        self._ResourceTags = None
        self._ZoneName = None
        self._TemplateId = None
        self._DryRun = None
        self._ProductVersion = None
        self._RedisClusterId = None
        self._AlarmPolicyList = None
        self._EncryptPassword = None

    @property
    def TypeId(self):
        r"""实例类型。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
- 200：Memcached 1.6 内存版（集群架构）。
**说明**：CKV 版本当前有存量用户使用，暂时保留。
        :rtype: int
        """
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def MemSize(self):
        r"""内存容量，单位为MB， 数值需为1024的整数倍。具体规格，请通过 [DescribeProductInfo](https://cloud.tencent.com/document/api/239/30600) 接口查询全地域的售卖规格。
- **TypeId**为标准架构时，**MemSize**是实例总内存容量；
- **TypeId**为集群架构时，**MemSize**是单分片内存容量。
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def GoodsNum(self):
        r"""实例数量，单次购买实例数量。具体信息，请通过 [DescribeProductInfo](https://cloud.tencent.com/document/api/239/30600) 接口查询全地域的售卖规格。
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Period(self):
        r"""购买实例的时长。
- 若 **BillingMode**为**1**，即计费方式为包年包月时，需设置该参数，指定所购买实例的时长。单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
- 若 **BillingMode**为**0**，即计费方式为按量计费时，该参数配置为1。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def BillingMode(self):
        r"""计费方式。
- 0：按量计费。
- 1：包年包月。
        :rtype: int
        """
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ZoneId(self):
        r"""实例所属的可用区ID，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Password(self):
        r"""访问实例的密码。
- 当输入参数**NoAuth**为**true**时，指设置实例为免密码访问，Password可不用配置，否则Password为必填参数。
- 当实例类型**TypeId**为Redis 2.8 内存版标准架构、Redis 4.0、5.0、6.2、7.0内存版标准架构或集群架构时，其密码复杂度要求为：8-64个字符，至少包含小写字母、大写字母、数字和字符()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种，不能以"/"开头。
- 当实例类型**TypeId**为CKV 3.2 内存版标准架构或集群架构时，其密码复杂度为：8-30个字符，必须包含字母和数字，且不包含其他字符。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def VpcId(self):
        r"""私有网络ID。如果不配置该参数则默认选择基础网络。请登录 [私有网络](https://console.cloud.tencent.com/vpc)控制台查询具体的ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络VPC的子网。基础网络下， 该参数无需配置。请登录 [私有网络](https://console.cloud.tencent.com/vpc)控制台查询子网列表获取具体的 ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        r"""项目 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)，在右上角的账户信息菜单中，选择**项目管理**查询项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenew(self):
        r"""自动续费标识。
- 0：默认状态（手动续费）。
- 1：自动续费。
- 2：到期不续费。
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def SecurityGroupIdList(self):
        r"""安全组 ID 数组。
- 安全组是一种虚拟防火墙，对云数据库实例的网络访问进行控制。创建实例时，建议绑定相应的安全组。
- 请通过 [DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447) 接口获取实例的安全组 ID。
        :rtype: list of str
        """
        return self._SecurityGroupIdList

    @SecurityGroupIdList.setter
    def SecurityGroupIdList(self, SecurityGroupIdList):
        self._SecurityGroupIdList = SecurityGroupIdList

    @property
    def VPort(self):
        r"""用户自定义的网络端口。默认为6379，范围为 [1024,65535]。
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def RedisShardNum(self):
        r"""实例分片数量。
- 标准版实例无需配置该参数。
- 集群版实例，分片数量范围为：[1、3、5、8、12、16、24、32、40、48、64、80、96、128]。
        :rtype: int
        """
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        r"""实例副本数量。
- Redis 内存版 4.0、5.0、6.2、7.0 标准架构和集群架构支持副本数量范围为[1,5]。
- Redis 2.8标准版、CKV标准版只支持1副本。
        :rtype: int
        """
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def ReplicasReadonly(self):
        r"""标识实例是否需支持副本只读。
- Redis 2.8 标准版、CKV标准版不支持副本只读。
- 开启副本只读，实例将自动读写分离，写请求路由到主节点，读请求路由到副本节点。
- 如需开启副本只读，建议副本数量大于等于2。
        :rtype: bool
        """
        return self._ReplicasReadonly

    @ReplicasReadonly.setter
    def ReplicasReadonly(self, ReplicasReadonly):
        self._ReplicasReadonly = ReplicasReadonly

    @property
    def InstanceName(self):
        r"""实例名称。命名要求：仅支持长度小于60的中文、英文或者数字，短划线"-"、下划线"_"。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NoAuth(self):
        r"""配置实例是否支持免密码访问。
- true：免密访问实例。
- false：非免密访问实例。默认为非免密方式，仅VPC网络的实例支持免密码访问。
        :rtype: bool
        """
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def NodeSet(self):
        r"""实例的节点信息，包含节点 ID、节点类型、节点可用区 ID等。具体信息，请参见[RedisNodeInfo ](https://cloud.tencent.com/document/product/239/20022)。
目前支持传入节点的类型（主节点或者副本节点），节点的可用区。单可用区部署不需要传递此参数。
        :rtype: list of RedisNodeInfo
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def ResourceTags(self):
        r"""给实例设定标签。
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ZoneName(self):
        r"""指定实例所属的可用区名称。具体信息，请参见[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def TemplateId(self):
        r"""指定实例相关的参数模板 ID。
- 若不配置该参数，则系统会依据所选择的兼容版本及架构，自动适配对应的默认模板。
- 请通过[DescribeParamTemplates](https://cloud.tencent.com/document/product/239/58750)接口，查询实例的参数模板列表，获取模板 ID 编号。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DryRun(self):
        r"""内部参数，标识创建实例是否需要检查。
- false ：默认值。发送正常请求，通过检查后直接创建实例。
- true：发送检查请求，不会创建实例。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ProductVersion(self):
        r"""指实例部署模式。
- local：传统架构，默认为 local。
- cdc：独享集群。
- cloud：云原生，当前已暂停售卖。
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def RedisClusterId(self):
        r"""独享集群 ID。

- 当 **ProductVersion** 设置为 **cdc** 时，该参数必须设置。
- 请通过接口[ DescribeRedisClusters](https://cloud.tencent.com/document/product/239/109628) 获取集群 ID。
        :rtype: str
        """
        return self._RedisClusterId

    @RedisClusterId.setter
    def RedisClusterId(self, RedisClusterId):
        self._RedisClusterId = RedisClusterId

    @property
    def AlarmPolicyList(self):
        r"""告警策略 ID 数组。

- 请登录[腾讯云可观测平台-告警管理-策略管理](https://console.cloud.tencent.com/monitor/alarm/policy)获取告警策略 ID。
- 若不配置该参数，则绑定默认告警策略。默认告警策略具体信息，请登录[腾讯云可观测平台-告警管理-策略管理](https://console.cloud.tencent.com/monitor/alarm/policy)查看。
        :rtype: list of str
        """
        return self._AlarmPolicyList

    @AlarmPolicyList.setter
    def AlarmPolicyList(self, AlarmPolicyList):
        self._AlarmPolicyList = AlarmPolicyList

    @property
    def EncryptPassword(self):
        r"""是否加密密码
        :rtype: bool
        """
        return self._EncryptPassword

    @EncryptPassword.setter
    def EncryptPassword(self, EncryptPassword):
        self._EncryptPassword = EncryptPassword


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        self._MemSize = params.get("MemSize")
        self._GoodsNum = params.get("GoodsNum")
        self._Period = params.get("Period")
        self._BillingMode = params.get("BillingMode")
        self._ZoneId = params.get("ZoneId")
        self._Password = params.get("Password")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenew = params.get("AutoRenew")
        self._SecurityGroupIdList = params.get("SecurityGroupIdList")
        self._VPort = params.get("VPort")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._ReplicasReadonly = params.get("ReplicasReadonly")
        self._InstanceName = params.get("InstanceName")
        self._NoAuth = params.get("NoAuth")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._ZoneName = params.get("ZoneName")
        self._TemplateId = params.get("TemplateId")
        self._DryRun = params.get("DryRun")
        self._ProductVersion = params.get("ProductVersion")
        self._RedisClusterId = params.get("RedisClusterId")
        self._AlarmPolicyList = params.get("AlarmPolicyList")
        self._EncryptPassword = params.get("EncryptPassword")
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
        :param _DealId: 交易的ID。
        :type DealId: str
        :param _InstanceIds: 实例ID。
        :type InstanceIds: list of str
        :param _DealName: 订单号。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._DealName = None
        self._RequestId = None

    @property
    def DealId(self):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        r"""交易的ID。
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        self._DealId = DealId

    @property
    def InstanceIds(self):
        r"""实例ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    r"""CreateParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 参数模板名称。字符长度要求为[2,64]。
        :type Name: str
        :param _Description: 参数模板描述。
        :type Description: str
        :param _ProductType: 产品类型。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
        :type ProductType: int
        :param _TemplateId: 源参数模板 ID。
        :type TemplateId: str
        :param _ParamList: 参数列表。
        :type ParamList: list of InstanceParam
        """
        self._Name = None
        self._Description = None
        self._ProductType = None
        self._TemplateId = None
        self._ParamList = None

    @property
    def Name(self):
        r"""参数模板名称。字符长度要求为[2,64]。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""参数模板描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductType(self):
        r"""产品类型。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def TemplateId(self):
        r"""源参数模板 ID。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ParamList(self):
        r"""参数列表。
        :rtype: list of InstanceParam
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ProductType = params.get("ProductType")
        self._TemplateId = params.get("TemplateId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    r"""CreateParamTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板 ID。
        :type TemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        r"""参数模板 ID。
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


class CreateReplicationGroupRequest(AbstractModel):
    r"""CreateReplicationGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定复制组中的主实例ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _GroupName: 配置复制组名称。仅支持长度为2-64个字符的中文、英文、数字、下划线_、分隔符-。
        :type GroupName: str
        :param _Remark: 备注信息。
        :type Remark: str
        """
        self._InstanceId = None
        self._GroupName = None
        self._Remark = None

    @property
    def InstanceId(self):
        r"""指定复制组中的主实例ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        r"""配置复制组名称。仅支持长度为2-64个字符的中文、英文、数字、下划线_、分隔符-。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Remark(self):
        r"""备注信息。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupName = params.get("GroupName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplicationGroupResponse(AbstractModel):
    r"""CreateReplicationGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID。
        :type TaskId: int
        :param _GroupId: 复制组string型id
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._GroupId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步流程ID。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GroupId(self):
        r"""复制组string型id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class DelayDistribution(AbstractModel):
    r"""延时分布详情

    """

    def __init__(self):
        r"""
        :param _Ladder: 指延时分布阶梯，其与延时区间的对应关系如下所示。
- 1：[0ms,1ms]。
- 5： [1ms,5ms]。
- 10： [5ms,10ms]。
- 50： [10ms,50ms]。
- 200：[50ms,200ms]。
- -1： [200ms,∞]。
        :type Ladder: int
        :param _Size: 延时处于当前分布阶梯的命令数量，单位：个。
        :type Size: int
        :param _Updatetime: 修改时间。
        :type Updatetime: int
        """
        self._Ladder = None
        self._Size = None
        self._Updatetime = None

    @property
    def Ladder(self):
        r"""指延时分布阶梯，其与延时区间的对应关系如下所示。
- 1：[0ms,1ms]。
- 5： [1ms,5ms]。
- 10： [5ms,10ms]。
- 50： [10ms,50ms]。
- 200：[50ms,200ms]。
- -1： [200ms,∞]。
        :rtype: int
        """
        return self._Ladder

    @Ladder.setter
    def Ladder(self, Ladder):
        self._Ladder = Ladder

    @property
    def Size(self):
        r"""延时处于当前分布阶梯的命令数量，单位：个。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
        r"""修改时间。
        :rtype: int
        """
        return self._Updatetime

    @Updatetime.setter
    def Updatetime(self, Updatetime):
        self._Updatetime = Updatetime


    def _deserialize(self, params):
        self._Ladder = params.get("Ladder")
        self._Size = params.get("Size")
        self._Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceAccountRequest(AbstractModel):
    r"""DeleteInstanceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _AccountName: 子账号名称。请登录[Redis控制台](https://console.cloud.tencent.com/redis)，切换至**账号管理**页面获取。具体信息，请参见[管理账号](https://cloud.tencent.com/document/product/239/36710)。
        :type AccountName: str
        """
        self._InstanceId = None
        self._AccountName = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        r"""子账号名称。请登录[Redis控制台](https://console.cloud.tencent.com/redis)，切换至**账号管理**页面获取。具体信息，请参见[管理账号](https://cloud.tencent.com/document/product/239/36710)。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceAccountResponse(AbstractModel):
    r"""DeleteInstanceAccount返回参数结构体

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


class DeleteParamTemplateRequest(AbstractModel):
    r"""DeleteParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板 ID。请登录 [Redis 控制台的参数模板](https://console.cloud.tencent.com/redis/templates)页面获取模板 ID。
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""参数模板 ID。请登录 [Redis 控制台的参数模板](https://console.cloud.tencent.com/redis/templates)页面获取模板 ID。
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
        


class DeleteParamTemplateResponse(AbstractModel):
    r"""DeleteParamTemplate返回参数结构体

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


class DeleteReplicationInstanceRequest(AbstractModel):
    r"""DeleteReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID。请登录[Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication)页面获取复制组 ID。
        :type GroupId: str
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _SyncType: 数据同步类型。
- true：需要数据强同步。
- false：不需要强同步，仅限删除主实例。
        :type SyncType: bool
        """
        self._GroupId = None
        self._InstanceId = None
        self._SyncType = None

    @property
    def GroupId(self):
        r"""复制组ID。请登录[Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication)页面获取复制组 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SyncType(self):
        r"""数据同步类型。
- true：需要数据强同步。
- false：不需要强同步，仅限删除主实例。
        :rtype: bool
        """
        return self._SyncType

    @SyncType.setter
    def SyncType(self, SyncType):
        self._SyncType = SyncType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._InstanceId = params.get("InstanceId")
        self._SyncType = params.get("SyncType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReplicationInstanceResponse(AbstractModel):
    r"""DeleteReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID
        :rtype: float
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


class DescribeAutoBackupConfigRequest(AbstractModel):
    r"""DescribeAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoBackupConfigResponse(AbstractModel):
    r"""DescribeAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoBackupType: 该参数因兼容性问题暂时保留，请忽略。
        :type AutoBackupType: int
        :param _WeekDays: 备份周期，默认为每天自动备份，Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param _TimePeriod: 备份任务发起时间段。
        :type TimePeriod: str
        :param _BackupStorageDays: 全量备份文件保存天数。默认为7天。如需保存更多天数，请[提交工单](https://console.cloud.tencent.com/workorder/category)申请。
        :type BackupStorageDays: int
        :param _BinlogStorageDays: 该参数不再使用，请忽略。
        :type BinlogStorageDays: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoBackupType = None
        self._WeekDays = None
        self._TimePeriod = None
        self._BackupStorageDays = None
        self._BinlogStorageDays = None
        self._RequestId = None

    @property
    def AutoBackupType(self):
        r"""该参数因兼容性问题暂时保留，请忽略。
        :rtype: int
        """
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType

    @property
    def WeekDays(self):
        r"""备份周期，默认为每天自动备份，Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        r"""备份任务发起时间段。
        :rtype: str
        """
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def BackupStorageDays(self):
        r"""全量备份文件保存天数。默认为7天。如需保存更多天数，请[提交工单](https://console.cloud.tencent.com/workorder/category)申请。
        :rtype: int
        """
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays

    @property
    def BinlogStorageDays(self):
        r"""该参数不再使用，请忽略。
        :rtype: int
        """
        return self._BinlogStorageDays

    @BinlogStorageDays.setter
    def BinlogStorageDays(self, BinlogStorageDays):
        self._BinlogStorageDays = BinlogStorageDays

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
        self._AutoBackupType = params.get("AutoBackupType")
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        self._BackupStorageDays = params.get("BackupStorageDays")
        self._BinlogStorageDays = params.get("BinlogStorageDays")
        self._RequestId = params.get("RequestId")


class DescribeBackupDetailRequest(AbstractModel):
    r"""DescribeBackupDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _BackupId: 备份 ID，可通过接口 [DescribeInstanceBackups](https://cloud.tencent.com/document/product/239/20011) 返回的参数 **RedisBackupSet** 获取。
        :type BackupId: str
        """
        self._InstanceId = None
        self._BackupId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        r"""备份 ID，可通过接口 [DescribeInstanceBackups](https://cloud.tencent.com/document/product/239/20011) 返回的参数 **RedisBackupSet** 获取。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDetailResponse(AbstractModel):
    r"""DescribeBackupDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份 ID。
        :type BackupId: str
        :param _StartTime: 备份开始时间。
        :type StartTime: str
        :param _EndTime: 备份结束时间。
        :type EndTime: str
        :param _BackupType: 备份方式。 

- 1：手动备份。
-  0：自动备份。
        :type BackupType: str
        :param _Status: 备份状态。 

- 1：备份被其它流程锁定。
- 2：备份正常，没有被任何流程锁定。
- -1：备份已过期。
- 3：备份正在被导出。
- 4：备份导出成功。
        :type Status: int
        :param _Remark: 备份的备注信息。
        :type Remark: str
        :param _Locked: 备份是否被锁定。

- 0：未被锁定。
- 1：已被锁定。
        :type Locked: int
        :param _BackupSize: 备份文件大小。单位：Byte。
        :type BackupSize: int
        :param _InstanceType: 实例类型。
        :type InstanceType: int
        :param _MemSize: 单分片内存规格大小，单位：MB。
        :type MemSize: int
        :param _ShardNum: 分片数量。
        :type ShardNum: int
        :param _ReplicasNum: 副本数量。
        :type ReplicasNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupId = None
        self._StartTime = None
        self._EndTime = None
        self._BackupType = None
        self._Status = None
        self._Remark = None
        self._Locked = None
        self._BackupSize = None
        self._InstanceType = None
        self._MemSize = None
        self._ShardNum = None
        self._ReplicasNum = None
        self._RequestId = None

    @property
    def BackupId(self):
        r"""备份 ID。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def StartTime(self):
        r"""备份开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""备份结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BackupType(self):
        r"""备份方式。 

- 1：手动备份。
-  0：自动备份。
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def Status(self):
        r"""备份状态。 

- 1：备份被其它流程锁定。
- 2：备份正常，没有被任何流程锁定。
- -1：备份已过期。
- 3：备份正在被导出。
- 4：备份导出成功。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        r"""备份的备注信息。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Locked(self):
        r"""备份是否被锁定。

- 0：未被锁定。
- 1：已被锁定。
        :rtype: int
        """
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def BackupSize(self):
        r"""备份文件大小。单位：Byte。
        :rtype: int
        """
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def InstanceType(self):
        r"""实例类型。
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MemSize(self):
        r"""单分片内存规格大小，单位：MB。
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def ShardNum(self):
        r"""分片数量。
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def ReplicasNum(self):
        r"""副本数量。
        :rtype: int
        """
        return self._ReplicasNum

    @ReplicasNum.setter
    def ReplicasNum(self, ReplicasNum):
        self._ReplicasNum = ReplicasNum

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
        self._BackupId = params.get("BackupId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._BackupType = params.get("BackupType")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._Locked = params.get("Locked")
        self._BackupSize = params.get("BackupSize")
        self._InstanceType = params.get("InstanceType")
        self._MemSize = params.get("MemSize")
        self._ShardNum = params.get("ShardNum")
        self._ReplicasNum = params.get("ReplicasNum")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    r"""DescribeBackupDownloadRestriction请求参数结构体

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    r"""DescribeBackupDownloadRestriction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LimitType: 下载备份文件的网络限制类型：

- NoLimit：不限制，腾讯云内外网均可以下载备份文件。
-  LimitOnlyIntranet：仅腾讯云自动分配的内网地址可下载备份文件。
- Customize：指用户自定义的私有网络可下载备份文件。
        :type LimitType: str
        :param _VpcComparisonSymbol: 该参数仅支持输入 In，表示自定义的**LimitVpc**可以下载备份文件。
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: 标识自定义的 LimitIp 地址是否可下载备份文件。

- In: 自定义的 IP 地址可以下载。
- NotIn: 自定义的 IP 不可以下载。
        :type IpComparisonSymbol: str
        :param _LimitVpc: 自定义的可下载备份文件的 VPC ID。当参数**LimitType**为**Customize **时，显示该参数。
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: 自定义的可下载备份文件的 VPC IP 地址。当参数**LimitType**为**Customize **时，显示该参数。
        :type LimitIp: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None
        self._RequestId = None

    @property
    def LimitType(self):
        r"""下载备份文件的网络限制类型：

- NoLimit：不限制，腾讯云内外网均可以下载备份文件。
-  LimitOnlyIntranet：仅腾讯云自动分配的内网地址可下载备份文件。
- Customize：指用户自定义的私有网络可下载备份文件。
        :rtype: str
        """
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        r"""该参数仅支持输入 In，表示自定义的**LimitVpc**可以下载备份文件。
        :rtype: str
        """
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        r"""标识自定义的 LimitIp 地址是否可下载备份文件。

- In: 自定义的 IP 地址可以下载。
- NotIn: 自定义的 IP 不可以下载。
        :rtype: str
        """
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        r"""自定义的可下载备份文件的 VPC ID。当参数**LimitType**为**Customize **时，显示该参数。
        :rtype: list of BackupLimitVpcItem
        """
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        r"""自定义的可下载备份文件的 VPC IP 地址。当参数**LimitType**为**Customize **时，显示该参数。
        :rtype: list of str
        """
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp

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
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        self._RequestId = params.get("RequestId")


class DescribeBackupUrlRequest(AbstractModel):
    r"""DescribeBackupUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _BackupId: 备份 ID，可通过 [DescribeInstanceBackups ](https://cloud.tencent.com/document/product/239/20011)接口返回的参数 RedisBackupSet 获取。
        :type BackupId: str
        :param _LimitType: 下载备份文件的网络限制类型，如果不配置该参数，则使用用户自定义的配置。
- NoLimit：不限制，腾讯云内外网均可以下载备份文件。
-  LimitOnlyIntranet：仅腾讯云自动分配的内网地址可下载备份文件。
- Customize：指用户自定义的私有网络可下载备份文件。
        :type LimitType: str
        :param _VpcComparisonSymbol: 该参数仅支持输入 In，表示自定义的**LimitVpc**可以下载备份文件。
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: 标识自定义的 LimitIp 地址是否可下载备份文件。
- In: 自定义的 IP 地址可以下载。默认为 In。
- NotIn: 自定义的 IP 不可以下载。
        :type IpComparisonSymbol: str
        :param _LimitVpc: 自定义的可下载备份文件的 VPC ID。当参数**LimitType**为**Customize **时，需配置该参数。
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: 自定义的可下载备份文件的 VPC IP 地址。当参数**LimitType**为**Customize **时，需配置该参数。
        :type LimitIp: list of str
        """
        self._InstanceId = None
        self._BackupId = None
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        r"""备份 ID，可通过 [DescribeInstanceBackups ](https://cloud.tencent.com/document/product/239/20011)接口返回的参数 RedisBackupSet 获取。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def LimitType(self):
        r"""下载备份文件的网络限制类型，如果不配置该参数，则使用用户自定义的配置。
- NoLimit：不限制，腾讯云内外网均可以下载备份文件。
-  LimitOnlyIntranet：仅腾讯云自动分配的内网地址可下载备份文件。
- Customize：指用户自定义的私有网络可下载备份文件。
        :rtype: str
        """
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        r"""该参数仅支持输入 In，表示自定义的**LimitVpc**可以下载备份文件。
        :rtype: str
        """
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        r"""标识自定义的 LimitIp 地址是否可下载备份文件。
- In: 自定义的 IP 地址可以下载。默认为 In。
- NotIn: 自定义的 IP 不可以下载。
        :rtype: str
        """
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        r"""自定义的可下载备份文件的 VPC ID。当参数**LimitType**为**Customize **时，需配置该参数。
        :rtype: list of BackupLimitVpcItem
        """
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        r"""自定义的可下载备份文件的 VPC IP 地址。当参数**LimitType**为**Customize **时，需配置该参数。
        :rtype: list of str
        """
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupUrlResponse(AbstractModel):
    r"""DescribeBackupUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 外网下载地址（6小时内链接有效），该字段正在逐步废弃中。
        :type DownloadUrl: list of str
        :param _InnerDownloadUrl: 内网下载地址（6小时内链接有效），该字段正在逐步废弃中。
        :type InnerDownloadUrl: list of str
        :param _Filenames: 文件名称，该字段正在逐步废弃中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Filenames: list of str
        :param _BackupInfos: 备份文件信息列表。
        :type BackupInfos: list of BackupDownloadInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._InnerDownloadUrl = None
        self._Filenames = None
        self._BackupInfos = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        warnings.warn("parameter `DownloadUrl` is deprecated", DeprecationWarning) 

        r"""外网下载地址（6小时内链接有效），该字段正在逐步废弃中。
        :rtype: list of str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        warnings.warn("parameter `DownloadUrl` is deprecated", DeprecationWarning) 

        self._DownloadUrl = DownloadUrl

    @property
    def InnerDownloadUrl(self):
        warnings.warn("parameter `InnerDownloadUrl` is deprecated", DeprecationWarning) 

        r"""内网下载地址（6小时内链接有效），该字段正在逐步废弃中。
        :rtype: list of str
        """
        return self._InnerDownloadUrl

    @InnerDownloadUrl.setter
    def InnerDownloadUrl(self, InnerDownloadUrl):
        warnings.warn("parameter `InnerDownloadUrl` is deprecated", DeprecationWarning) 

        self._InnerDownloadUrl = InnerDownloadUrl

    @property
    def Filenames(self):
        warnings.warn("parameter `Filenames` is deprecated", DeprecationWarning) 

        r"""文件名称，该字段正在逐步废弃中。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Filenames

    @Filenames.setter
    def Filenames(self, Filenames):
        warnings.warn("parameter `Filenames` is deprecated", DeprecationWarning) 

        self._Filenames = Filenames

    @property
    def BackupInfos(self):
        r"""备份文件信息列表。
        :rtype: list of BackupDownloadInfo
        """
        return self._BackupInfos

    @BackupInfos.setter
    def BackupInfos(self, BackupInfos):
        self._BackupInfos = BackupInfos

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
        self._DownloadUrl = params.get("DownloadUrl")
        self._InnerDownloadUrl = params.get("InnerDownloadUrl")
        self._Filenames = params.get("Filenames")
        if params.get("BackupInfos") is not None:
            self._BackupInfos = []
            for item in params.get("BackupInfos"):
                obj = BackupDownloadInfo()
                obj._deserialize(item)
                self._BackupInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBandwidthRangeRequest(AbstractModel):
    r"""DescribeBandwidthRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBandwidthRangeResponse(AbstractModel):
    r"""DescribeBandwidthRange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BaseBandwidth: 标准带宽。指购买实例时，系统为每个节点分配的带宽。
        :type BaseBandwidth: int
        :param _AddBandwidth: 指实例的附加带宽。标准带宽不满足需求的情况下，用户可自行增加的带宽。<ul><li>开启副本只读时，实例总带宽 = 附加带宽 * 分片数 + 标准带宽 * 分片数 * Max ([只读副本数量, 1])，标准架构的分片数 = 1。</li><li>没有开启副本只读时，实例总带宽 = 附加带宽 * 分片数 + 标准带宽 * 分片数，标准架构的分片数 = 1。</li></ul>
        :type AddBandwidth: int
        :param _MinAddBandwidth: 附加带宽设置下限。
        :type MinAddBandwidth: int
        :param _MaxAddBandwidth: 附加带宽设置上限。
        :type MaxAddBandwidth: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaseBandwidth = None
        self._AddBandwidth = None
        self._MinAddBandwidth = None
        self._MaxAddBandwidth = None
        self._RequestId = None

    @property
    def BaseBandwidth(self):
        r"""标准带宽。指购买实例时，系统为每个节点分配的带宽。
        :rtype: int
        """
        return self._BaseBandwidth

    @BaseBandwidth.setter
    def BaseBandwidth(self, BaseBandwidth):
        self._BaseBandwidth = BaseBandwidth

    @property
    def AddBandwidth(self):
        r"""指实例的附加带宽。标准带宽不满足需求的情况下，用户可自行增加的带宽。<ul><li>开启副本只读时，实例总带宽 = 附加带宽 * 分片数 + 标准带宽 * 分片数 * Max ([只读副本数量, 1])，标准架构的分片数 = 1。</li><li>没有开启副本只读时，实例总带宽 = 附加带宽 * 分片数 + 标准带宽 * 分片数，标准架构的分片数 = 1。</li></ul>
        :rtype: int
        """
        return self._AddBandwidth

    @AddBandwidth.setter
    def AddBandwidth(self, AddBandwidth):
        self._AddBandwidth = AddBandwidth

    @property
    def MinAddBandwidth(self):
        r"""附加带宽设置下限。
        :rtype: int
        """
        return self._MinAddBandwidth

    @MinAddBandwidth.setter
    def MinAddBandwidth(self, MinAddBandwidth):
        self._MinAddBandwidth = MinAddBandwidth

    @property
    def MaxAddBandwidth(self):
        r"""附加带宽设置上限。
        :rtype: int
        """
        return self._MaxAddBandwidth

    @MaxAddBandwidth.setter
    def MaxAddBandwidth(self, MaxAddBandwidth):
        self._MaxAddBandwidth = MaxAddBandwidth

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
        self._BaseBandwidth = params.get("BaseBandwidth")
        self._AddBandwidth = params.get("AddBandwidth")
        self._MinAddBandwidth = params.get("MinAddBandwidth")
        self._MaxAddBandwidth = params.get("MaxAddBandwidth")
        self._RequestId = params.get("RequestId")


class DescribeCommonDBInstancesRequest(AbstractModel):
    r"""DescribeCommonDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcIds: vpc网络ID信息列表
        :type VpcIds: list of int
        :param _SubnetIds: 子网ID信息列表
        :type SubnetIds: list of int
        :param _PayMode: 计费类型过滤列表；0表示包年包月，1表示按量计费
        :type PayMode: int
        :param _InstanceIds: 实例ID过滤信息列表，数组最大长度限制为100
        :type InstanceIds: list of str
        :param _InstanceNames: 实例名称过滤信息列表
        :type InstanceNames: list of str
        :param _Status: 实例状态信息过滤列表
        :type Status: list of str
        :param _OrderBy: 排序字段
        :type OrderBy: str
        :param _OrderByType: 排序方式
        :type OrderByType: str
        :param _Vips: 实例vip信息列表
        :type Vips: list of str
        :param _UniqVpcIds: vpc网络ID信息列表
        :type UniqVpcIds: list of str
        :param _UniqSubnetIds: 子网统一ID列表
        :type UniqSubnetIds: list of str
        :param _Limit: 数量限制，默认推荐100
        :type Limit: int
        :param _Offset: 偏移量，默认0
        :type Offset: int
        """
        self._VpcIds = None
        self._SubnetIds = None
        self._PayMode = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._Status = None
        self._OrderBy = None
        self._OrderByType = None
        self._Vips = None
        self._UniqVpcIds = None
        self._UniqSubnetIds = None
        self._Limit = None
        self._Offset = None

    @property
    def VpcIds(self):
        r"""vpc网络ID信息列表
        :rtype: list of int
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def SubnetIds(self):
        r"""子网ID信息列表
        :rtype: list of int
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def PayMode(self):
        r"""计费类型过滤列表；0表示包年包月，1表示按量计费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceIds(self):
        r"""实例ID过滤信息列表，数组最大长度限制为100
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        r"""实例名称过滤信息列表
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def Status(self):
        r"""实例状态信息过滤列表
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderBy(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Vips(self):
        r"""实例vip信息列表
        :rtype: list of str
        """
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def UniqVpcIds(self):
        r"""vpc网络ID信息列表
        :rtype: list of str
        """
        return self._UniqVpcIds

    @UniqVpcIds.setter
    def UniqVpcIds(self, UniqVpcIds):
        self._UniqVpcIds = UniqVpcIds

    @property
    def UniqSubnetIds(self):
        r"""子网统一ID列表
        :rtype: list of str
        """
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def Limit(self):
        r"""数量限制，默认推荐100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._VpcIds = params.get("VpcIds")
        self._SubnetIds = params.get("SubnetIds")
        self._PayMode = params.get("PayMode")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._Status = params.get("Status")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Vips = params.get("Vips")
        self._UniqVpcIds = params.get("UniqVpcIds")
        self._UniqSubnetIds = params.get("UniqSubnetIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCommonDBInstancesResponse(AbstractModel):
    r"""DescribeCommonDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例数
        :type TotalCount: int
        :param _InstanceDetails: 实例信息
        :type InstanceDetails: list of RedisCommonInstanceList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""实例数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceDetails(self):
        r"""实例信息
        :rtype: list of RedisCommonInstanceList
        """
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

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
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = RedisCommonInstanceList()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    r"""DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :type InstanceId: str
        """
        self._Product = None
        self._InstanceId = None

    @property
    def Product(self):
        r"""数据库引擎名称，本接口取值：redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    r"""DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组规则。
        :type Groups: list of SecurityGroup
        :param _VIP: 实例内网IPv4地址。
        :type VIP: str
        :param _VPort: 内网端口。
        :type VPort: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        r"""安全组规则。
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        r"""实例内网IPv4地址。
        :rtype: str
        """
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        r"""内网端口。
        :rtype: str
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._VIP = params.get("VIP")
        self._VPort = params.get("VPort")
        self._RequestId = params.get("RequestId")


class DescribeGlobalReplicationAreaRequest(AbstractModel):
    r"""DescribeGlobalReplicationArea请求参数结构体

    """


class DescribeGlobalReplicationAreaResponse(AbstractModel):
    r"""DescribeGlobalReplicationArea返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableRegions: 可用地域信息
        :type AvailableRegions: list of AvailableRegion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableRegions = None
        self._RequestId = None

    @property
    def AvailableRegions(self):
        r"""可用地域信息
        :rtype: list of AvailableRegion
        """
        return self._AvailableRegions

    @AvailableRegions.setter
    def AvailableRegions(self, AvailableRegions):
        self._AvailableRegions = AvailableRegions

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
        if params.get("AvailableRegions") is not None:
            self._AvailableRegions = []
            for item in params.get("AvailableRegions"):
                obj = AvailableRegion()
                obj._deserialize(item)
                self._AvailableRegions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceAccountRequest(AbstractModel):
    r"""DescribeInstanceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Limit: 分页大小。默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param _Offset: 分页偏移量。取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""分页大小。默认值为20，最小值为1，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量。取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAccountResponse(AbstractModel):
    r"""DescribeInstanceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Accounts: 账号详细信息。
        :type Accounts: list of Account
        :param _TotalCount: 账号个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Accounts = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Accounts(self):
        r"""账号详细信息。
        :rtype: list of Account
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def TotalCount(self):
        r"""账号个数。
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
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstanceBackupsRequest(AbstractModel):
    r"""DescribeInstanceBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页输出的备份列表大小。默认大小为20，最大值为 100。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _InstanceId: 待操作的实例ID，可通过 DescribeInstance 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _BeginTime: 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表，查询时间最大跨度30天。
        :type BeginTime: str
        :param _EndTime: 结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表，查询时间最大跨度30天。
        :type EndTime: str
        :param _Status: 备份任务的状态：
1：备份在流程中。
2：备份正常。
3：备份转RDB文件处理中。
4：已完成RDB转换。
-1：备份已过期。
-2：备份已删除。
        :type Status: list of int
        :param _InstanceName: 实例名称，支持根据实例名称模糊搜索。
        :type InstanceName: str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._Status = None
        self._InstanceName = None

    @property
    def Limit(self):
        r"""每页输出的备份列表大小。默认大小为20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceId(self):
        r"""待操作的实例ID，可通过 DescribeInstance 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        r"""开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表，查询时间最大跨度30天。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表，查询时间最大跨度30天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""备份任务的状态：
1：备份在流程中。
2：备份正常。
3：备份转RDB文件处理中。
4：已完成RDB转换。
-1：备份已过期。
-2：备份已删除。
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceName(self):
        r"""实例名称，支持根据实例名称模糊搜索。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceBackupsResponse(AbstractModel):
    r"""DescribeInstanceBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 备份总数。
        :type TotalCount: int
        :param _BackupSet: 实例的备份数组。
        :type BackupSet: list of RedisBackupSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""备份总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupSet(self):
        r"""实例的备份数组。
        :rtype: list of RedisBackupSet
        """
        return self._BackupSet

    @BackupSet.setter
    def BackupSet(self, BackupSet):
        self._BackupSet = BackupSet

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
        if params.get("BackupSet") is not None:
            self._BackupSet = []
            for item in params.get("BackupSet"):
                obj = RedisBackupSet()
                obj._deserialize(item)
                self._BackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceDTSInfoRequest(AbstractModel):
    r"""DescribeInstanceDTSInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDTSInfoResponse(AbstractModel):
    r"""DescribeInstanceDTSInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: DTS任务ID
        :type JobId: str
        :param _JobName: DTS任务名称
        :type JobName: str
        :param _Status: 任务状态,取值为：1-创建中(Creating),3-校验中(Checking)4-校验通过(CheckPass),5-校验不通过（CheckNotPass）,7-任务运行(Running),8-准备完成（ReadyComplete）,9-任务成功（Success）,10-任务失败（Failed）,11-撤销中（Stopping）,12-完成中（Completing）
        :type Status: int
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _Offset: 同步时延，单位：字节
        :type Offset: int
        :param _CutDownTime: 断开时间
        :type CutDownTime: str
        :param _SrcInfo: 源实例信息
        :type SrcInfo: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`
        :param _DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._JobName = None
        self._Status = None
        self._StatusDesc = None
        self._Offset = None
        self._CutDownTime = None
        self._SrcInfo = None
        self._DstInfo = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""DTS任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        r"""DTS任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Status(self):
        r"""任务状态,取值为：1-创建中(Creating),3-校验中(Checking)4-校验通过(CheckPass),5-校验不通过（CheckNotPass）,7-任务运行(Running),8-准备完成（ReadyComplete）,9-任务成功（Success）,10-任务失败（Failed）,11-撤销中（Stopping）,12-完成中（Completing）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Offset(self):
        r"""同步时延，单位：字节
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CutDownTime(self):
        r"""断开时间
        :rtype: str
        """
        return self._CutDownTime

    @CutDownTime.setter
    def CutDownTime(self, CutDownTime):
        self._CutDownTime = CutDownTime

    @property
    def SrcInfo(self):
        r"""源实例信息
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        r"""目标实例信息
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

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
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Offset = params.get("Offset")
        self._CutDownTime = params.get("CutDownTime")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = DescribeInstanceDTSInstanceInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DescribeInstanceDTSInstanceInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceDTSInstanceInfo(AbstractModel):
    r"""详细DTS实例信息

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域 ID。
        :type RegionId: int
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _SetId: 仓库ID。
        :type SetId: int
        :param _ZoneId: 可用区ID。
        :type ZoneId: int
        :param _Type: 实例类型。
        :type Type: int
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Vip: 实例访问地址。
        :type Vip: str
        :param _Status: 状态。
        :type Status: int
        """
        self._RegionId = None
        self._InstanceId = None
        self._SetId = None
        self._ZoneId = None
        self._Type = None
        self._InstanceName = None
        self._Vip = None
        self._Status = None

    @property
    def RegionId(self):
        r"""地域 ID。
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SetId(self):
        r"""仓库ID。
        :rtype: int
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def ZoneId(self):
        r"""可用区ID。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Type(self):
        r"""实例类型。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        r"""实例访问地址。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Status(self):
        r"""状态。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._InstanceId = params.get("InstanceId")
        self._SetId = params.get("SetId")
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailRequest(AbstractModel):
    r"""DescribeInstanceDealDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealIds: 订单号，即 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的输出参数DealId。数组最大长度限制为10
        :type DealIds: list of str
        :param _DealName: 订单号，即 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的输出参数DealName。数组最大长度限制为10
        :type DealName: str
        """
        self._DealIds = None
        self._DealName = None

    @property
    def DealIds(self):
        warnings.warn("parameter `DealIds` is deprecated", DeprecationWarning) 

        r"""订单号，即 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的输出参数DealId。数组最大长度限制为10
        :rtype: list of str
        """
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        warnings.warn("parameter `DealIds` is deprecated", DeprecationWarning) 

        self._DealIds = DealIds

    @property
    def DealName(self):
        r"""订单号，即 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的输出参数DealName。数组最大长度限制为10
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailResponse(AbstractModel):
    r"""DescribeInstanceDealDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealDetails: 订单详细信息。
        :type DealDetails: list of TradeDealDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealDetails = None
        self._RequestId = None

    @property
    def DealDetails(self):
        r"""订单详细信息。
        :rtype: list of TradeDealDetail
        """
        return self._DealDetails

    @DealDetails.setter
    def DealDetails(self, DealDetails):
        self._DealDetails = DealDetails

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
        if params.get("DealDetails") is not None:
            self._DealDetails = []
            for item in params.get("DealDetails"):
                obj = TradeDealDetail()
                obj._deserialize(item)
                self._DealDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceEventsRequest(AbstractModel):
    r"""DescribeInstanceEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionStartDate: 配置查询事件执行计划的起始日期，查询日期最大跨度30天。
        :type ExecutionStartDate: str
        :param _ExecutionEndDate: 配置查询事件执行计划的结束日期，查询日期最大跨度30天。
        :type ExecutionEndDate: str
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _PageSize: 输出每页显示事件的数量。
- 默认值：10。
- 取值范围：[1,100]。
        :type PageSize: int
        :param _PageNo: 配置查询事件的输出页码，即支持根据PageNo（页码）与 PageSize （每页输出数量）查询某一页的事件。
- 默认值：1。
- 取值范围：大于0 的正整数。
        :type PageNo: int
        :param _Status: 事件当前状态。
- Waiting：未到达执行日期或不在维护时间窗内的事件。
- Running：在维护时间窗内，正在执行维护的事件。
- Finished：已全部完成维护的事件。
- Canceled：已取消执行的事件。
        :type Status: list of str
        :param _EventTypes: 事件类型，当前仅支持配置实例迁移、资源腾挪、机房裁撤相关的运维操作。该参数仅支持配置为 **InstanceMigration**。
        :type EventTypes: list of str
        :param _Grades: 配置查询事件等级。事件等级根据其影响严重程度和紧急程度进行分级，由重至轻依次为关键、重要、中等、一般。
- Critical：关键
- High：重要
- Middle：中等
- Low：一般
        :type Grades: list of str
        """
        self._ExecutionStartDate = None
        self._ExecutionEndDate = None
        self._InstanceId = None
        self._PageSize = None
        self._PageNo = None
        self._Status = None
        self._EventTypes = None
        self._Grades = None

    @property
    def ExecutionStartDate(self):
        r"""配置查询事件执行计划的起始日期，查询日期最大跨度30天。
        :rtype: str
        """
        return self._ExecutionStartDate

    @ExecutionStartDate.setter
    def ExecutionStartDate(self, ExecutionStartDate):
        self._ExecutionStartDate = ExecutionStartDate

    @property
    def ExecutionEndDate(self):
        r"""配置查询事件执行计划的结束日期，查询日期最大跨度30天。
        :rtype: str
        """
        return self._ExecutionEndDate

    @ExecutionEndDate.setter
    def ExecutionEndDate(self, ExecutionEndDate):
        self._ExecutionEndDate = ExecutionEndDate

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PageSize(self):
        r"""输出每页显示事件的数量。
- 默认值：10。
- 取值范围：[1,100]。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        r"""配置查询事件的输出页码，即支持根据PageNo（页码）与 PageSize （每页输出数量）查询某一页的事件。
- 默认值：1。
- 取值范围：大于0 的正整数。
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Status(self):
        r"""事件当前状态。
- Waiting：未到达执行日期或不在维护时间窗内的事件。
- Running：在维护时间窗内，正在执行维护的事件。
- Finished：已全部完成维护的事件。
- Canceled：已取消执行的事件。
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventTypes(self):
        r"""事件类型，当前仅支持配置实例迁移、资源腾挪、机房裁撤相关的运维操作。该参数仅支持配置为 **InstanceMigration**。
        :rtype: list of str
        """
        return self._EventTypes

    @EventTypes.setter
    def EventTypes(self, EventTypes):
        self._EventTypes = EventTypes

    @property
    def Grades(self):
        r"""配置查询事件等级。事件等级根据其影响严重程度和紧急程度进行分级，由重至轻依次为关键、重要、中等、一般。
- Critical：关键
- High：重要
- Middle：中等
- Low：一般
        :rtype: list of str
        """
        return self._Grades

    @Grades.setter
    def Grades(self, Grades):
        self._Grades = Grades


    def _deserialize(self, params):
        self._ExecutionStartDate = params.get("ExecutionStartDate")
        self._ExecutionEndDate = params.get("ExecutionEndDate")
        self._InstanceId = params.get("InstanceId")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._Status = params.get("Status")
        self._EventTypes = params.get("EventTypes")
        self._Grades = params.get("Grades")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceEventsResponse(AbstractModel):
    r"""DescribeInstanceEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RedisInstanceEvents: 实例事件信息
        :type RedisInstanceEvents: list of RedisInstanceEvent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RedisInstanceEvents = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RedisInstanceEvents(self):
        r"""实例事件信息
        :rtype: list of RedisInstanceEvent
        """
        return self._RedisInstanceEvents

    @RedisInstanceEvents.setter
    def RedisInstanceEvents(self, RedisInstanceEvents):
        self._RedisInstanceEvents = RedisInstanceEvents

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
        if params.get("RedisInstanceEvents") is not None:
            self._RedisInstanceEvents = []
            for item in params.get("RedisInstanceEvents"):
                obj = RedisInstanceEvent()
                obj._deserialize(item)
                self._RedisInstanceEvents.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceLogDeliveryRequest(AbstractModel):
    r"""DescribeInstanceLogDelivery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogDeliveryResponse(AbstractModel):
    r"""DescribeInstanceLogDelivery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SlowLog: 实例慢日志投递信息。
        :type SlowLog: :class:`tencentcloud.redis.v20180412.models.LogDeliveryInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SlowLog = None
        self._RequestId = None

    @property
    def SlowLog(self):
        r"""实例慢日志投递信息。
        :rtype: :class:`tencentcloud.redis.v20180412.models.LogDeliveryInfo`
        """
        return self._SlowLog

    @SlowLog.setter
    def SlowLog(self, SlowLog):
        self._SlowLog = SlowLog

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
        if params.get("SlowLog") is not None:
            self._SlowLog = LogDeliveryInfo()
            self._SlowLog._deserialize(params.get("SlowLog"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyRequest(AbstractModel):
    r"""DescribeInstanceMonitorBigKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _ReqType: 请求类型：1——string类型，2——所有类型
        :type ReqType: int
        :param _Date: 时间；例如："20190219"
        :type Date: str
        """
        self._InstanceId = None
        self._ReqType = None
        self._Date = None

    @property
    def InstanceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReqType(self):
        r"""请求类型：1——string类型，2——所有类型
        :rtype: int
        """
        return self._ReqType

    @ReqType.setter
    def ReqType(self, ReqType):
        self._ReqType = ReqType

    @property
    def Date(self):
        r"""时间；例如："20190219"
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReqType = params.get("ReqType")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeyResponse(AbstractModel):
    r"""DescribeInstanceMonitorBigKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 大Key详细信息
        :type Data: list of BigKeyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""大Key详细信息
        :rtype: list of BigKeyInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BigKeyInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeySizeDistRequest(AbstractModel):
    r"""DescribeInstanceMonitorBigKeySizeDist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Date: 时间；例如："20190219"
        :type Date: str
        """
        self._InstanceId = None
        self._Date = None

    @property
    def InstanceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        r"""时间；例如："20190219"
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeySizeDistResponse(AbstractModel):
    r"""DescribeInstanceMonitorBigKeySizeDist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 大Key大小分布详情
        :type Data: list of DelayDistribution
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""大Key大小分布详情
        :rtype: list of DelayDistribution
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyTypeDistRequest(AbstractModel):
    r"""DescribeInstanceMonitorBigKeyTypeDist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Date: 时间；例如："20190219"
        :type Date: str
        """
        self._InstanceId = None
        self._Date = None

    @property
    def InstanceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        r"""时间；例如："20190219"
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeyTypeDistResponse(AbstractModel):
    r"""DescribeInstanceMonitorBigKeyTypeDist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 大Key类型分布详细信息
        :type Data: list of BigKeyTypeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""大Key类型分布详细信息
        :rtype: list of BigKeyTypeInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BigKeyTypeInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorHotKeyRequest(AbstractModel):
    r"""DescribeInstanceMonitorHotKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _SpanType: 查询时间范围。
- 1：实时。
- 2：近30分钟。
- 3：近6小时。
- 4：近24小时。
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
        r"""查询时间范围。
- 1：实时。
- 2：近30分钟。
- 3：近6小时。
- 4：近24小时。
        :rtype: int
        """
        return self._SpanType

    @SpanType.setter
    def SpanType(self, SpanType):
        self._SpanType = SpanType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorHotKeyResponse(AbstractModel):
    r"""DescribeInstanceMonitorHotKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 热 Key 详细信息。
        :type Data: list of HotKeyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""热 Key 详细信息。
        :rtype: list of HotKeyInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = HotKeyInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorSIPRequest(AbstractModel):
    r"""DescribeInstanceMonitorSIP请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorSIPResponse(AbstractModel):
    r"""DescribeInstanceMonitorSIP返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 访问来源信息
        :type Data: list of SourceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""访问来源信息
        :rtype: list of SourceInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SourceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorTookDistRequest(AbstractModel):
    r"""DescribeInstanceMonitorTookDist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Date: 查询时间日期。
        :type Date: str
        :param _SpanType: 时间范围。
- 1：实时。
- 2：近30分钟。
- 3：近6小时。
- 4：近24小时。
        :type SpanType: int
        """
        self._InstanceId = None
        self._Date = None
        self._SpanType = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        r"""查询时间日期。
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def SpanType(self):
        r"""时间范围。
- 1：实时。
- 2：近30分钟。
- 3：近6小时。
- 4：近24小时。
        :rtype: int
        """
        return self._SpanType

    @SpanType.setter
    def SpanType(self, SpanType):
        self._SpanType = SpanType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        self._SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTookDistResponse(AbstractModel):
    r"""DescribeInstanceMonitorTookDist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 时延分布信息。
        :type Data: list of DelayDistribution
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""时延分布信息。
        :rtype: list of DelayDistribution
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdRequest(AbstractModel):
    r"""DescribeInstanceMonitorTopNCmd请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _SpanType: 时间范围。
- 1：实时。
- 2：近30分钟。
- 3：近6小时。
- 4：近24小时。
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
        r"""时间范围。
- 1：实时。
- 2：近30分钟。
- 3：近6小时。
- 4：近24小时。
        :rtype: int
        """
        return self._SpanType

    @SpanType.setter
    def SpanType(self, SpanType):
        self._SpanType = SpanType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTopNCmdResponse(AbstractModel):
    r"""DescribeInstanceMonitorTopNCmd返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 访问命令信息
        :type Data: list of SourceCommand
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""访问命令信息
        :rtype: list of SourceCommand
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SourceCommand()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdTookRequest(AbstractModel):
    r"""DescribeInstanceMonitorTopNCmdTook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _SpanType: 查询时间范围。
- 1：实时。
- 2：近30分钟。
- 3：近6小时。
- 4：近24小时。
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
        r"""查询时间范围。
- 1：实时。
- 2：近30分钟。
- 3：近6小时。
- 4：近24小时。
        :rtype: int
        """
        return self._SpanType

    @SpanType.setter
    def SpanType(self, SpanType):
        self._SpanType = SpanType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTopNCmdTookResponse(AbstractModel):
    r"""DescribeInstanceMonitorTopNCmdTook返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 耗时详细信息
        :type Data: list of CommandTake
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""耗时详细信息
        :rtype: list of CommandTake
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CommandTake()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    r"""DescribeInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Limit: 列表大小。每页输出的节点信息大小。默认为 20，最多输出1000条。该字段已不再使用，请忽略。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。该字段已不再使用，请忽略。
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""列表大小。每页输出的节点信息大小。默认为 20，最多输出1000条。该字段已不再使用，请忽略。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。该字段已不再使用，请忽略。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodeInfoResponse(AbstractModel):
    r"""DescribeInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyCount: Proxy节点数量。
        :type ProxyCount: int
        :param _Proxy: Proxy节点信息。
        :type Proxy: list of ProxyNodes
        :param _RedisCount: Redis节点数量。
        :type RedisCount: int
        :param _Redis: Redis节点信息。
        :type Redis: list of RedisNodes
        :param _TendisCount: 该参数不再使用，请忽略。
        :type TendisCount: int
        :param _Tendis: 该参数不再使用，请忽略。
        :type Tendis: list of TendisNodes
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyCount = None
        self._Proxy = None
        self._RedisCount = None
        self._Redis = None
        self._TendisCount = None
        self._Tendis = None
        self._RequestId = None

    @property
    def ProxyCount(self):
        r"""Proxy节点数量。
        :rtype: int
        """
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def Proxy(self):
        r"""Proxy节点信息。
        :rtype: list of ProxyNodes
        """
        return self._Proxy

    @Proxy.setter
    def Proxy(self, Proxy):
        self._Proxy = Proxy

    @property
    def RedisCount(self):
        r"""Redis节点数量。
        :rtype: int
        """
        return self._RedisCount

    @RedisCount.setter
    def RedisCount(self, RedisCount):
        self._RedisCount = RedisCount

    @property
    def Redis(self):
        r"""Redis节点信息。
        :rtype: list of RedisNodes
        """
        return self._Redis

    @Redis.setter
    def Redis(self, Redis):
        self._Redis = Redis

    @property
    def TendisCount(self):
        r"""该参数不再使用，请忽略。
        :rtype: int
        """
        return self._TendisCount

    @TendisCount.setter
    def TendisCount(self, TendisCount):
        self._TendisCount = TendisCount

    @property
    def Tendis(self):
        r"""该参数不再使用，请忽略。
        :rtype: list of TendisNodes
        """
        return self._Tendis

    @Tendis.setter
    def Tendis(self, Tendis):
        self._Tendis = Tendis

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
        self._ProxyCount = params.get("ProxyCount")
        if params.get("Proxy") is not None:
            self._Proxy = []
            for item in params.get("Proxy"):
                obj = ProxyNodes()
                obj._deserialize(item)
                self._Proxy.append(obj)
        self._RedisCount = params.get("RedisCount")
        if params.get("Redis") is not None:
            self._Redis = []
            for item in params.get("Redis"):
                obj = RedisNodes()
                obj._deserialize(item)
                self._Redis.append(obj)
        self._TendisCount = params.get("TendisCount")
        if params.get("Tendis") is not None:
            self._Tendis = []
            for item in params.get("Tendis"):
                obj = TendisNodes()
                obj._deserialize(item)
                self._Tendis.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    r"""DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Limit: 分页大小。默认为100，最大值为 200。
        :type Limit: int
        :param _Offset: 偏移量，取Limit整数倍，默认值为0。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""实例 ID 。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""分页大小。默认为100，最大值为 200。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，取Limit整数倍，默认值为0。计算公式：offset=limit*(页码-1)。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    r"""DescribeInstanceParamRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总的修改历史记录数。
        :type TotalCount: int
        :param _InstanceParamHistory: 修改历史记录信息。
        :type InstanceParamHistory: list of InstanceParamHistory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceParamHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总的修改历史记录数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceParamHistory(self):
        r"""修改历史记录信息。
        :rtype: list of InstanceParamHistory
        """
        return self._InstanceParamHistory

    @InstanceParamHistory.setter
    def InstanceParamHistory(self, InstanceParamHistory):
        self._InstanceParamHistory = InstanceParamHistory

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
        if params.get("InstanceParamHistory") is not None:
            self._InstanceParamHistory = []
            for item in params.get("InstanceParamHistory"):
                obj = InstanceParamHistory()
                obj._deserialize(item)
                self._InstanceParamHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    r"""DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    r"""DescribeInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数列表总数量。
        :type TotalCount: int
        :param _InstanceEnumParam: 实例枚举类型参数。
        :type InstanceEnumParam: list of InstanceEnumParam
        :param _InstanceIntegerParam: 实例整型参数。
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param _InstanceTextParam: 实例字符型参数。
        :type InstanceTextParam: list of InstanceTextParam
        :param _InstanceMultiParam: 实例多选项型参数。
        :type InstanceMultiParam: list of InstanceMultiParam
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceEnumParam = None
        self._InstanceIntegerParam = None
        self._InstanceTextParam = None
        self._InstanceMultiParam = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""参数列表总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceEnumParam(self):
        r"""实例枚举类型参数。
        :rtype: list of InstanceEnumParam
        """
        return self._InstanceEnumParam

    @InstanceEnumParam.setter
    def InstanceEnumParam(self, InstanceEnumParam):
        self._InstanceEnumParam = InstanceEnumParam

    @property
    def InstanceIntegerParam(self):
        r"""实例整型参数。
        :rtype: list of InstanceIntegerParam
        """
        return self._InstanceIntegerParam

    @InstanceIntegerParam.setter
    def InstanceIntegerParam(self, InstanceIntegerParam):
        self._InstanceIntegerParam = InstanceIntegerParam

    @property
    def InstanceTextParam(self):
        r"""实例字符型参数。
        :rtype: list of InstanceTextParam
        """
        return self._InstanceTextParam

    @InstanceTextParam.setter
    def InstanceTextParam(self, InstanceTextParam):
        self._InstanceTextParam = InstanceTextParam

    @property
    def InstanceMultiParam(self):
        r"""实例多选项型参数。
        :rtype: list of InstanceMultiParam
        """
        return self._InstanceMultiParam

    @InstanceMultiParam.setter
    def InstanceMultiParam(self, InstanceMultiParam):
        self._InstanceMultiParam = InstanceMultiParam

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
        if params.get("InstanceEnumParam") is not None:
            self._InstanceEnumParam = []
            for item in params.get("InstanceEnumParam"):
                obj = InstanceEnumParam()
                obj._deserialize(item)
                self._InstanceEnumParam.append(obj)
        if params.get("InstanceIntegerParam") is not None:
            self._InstanceIntegerParam = []
            for item in params.get("InstanceIntegerParam"):
                obj = InstanceIntegerParam()
                obj._deserialize(item)
                self._InstanceIntegerParam.append(obj)
        if params.get("InstanceTextParam") is not None:
            self._InstanceTextParam = []
            for item in params.get("InstanceTextParam"):
                obj = InstanceTextParam()
                obj._deserialize(item)
                self._InstanceTextParam.append(obj)
        if params.get("InstanceMultiParam") is not None:
            self._InstanceMultiParam = []
            for item in params.get("InstanceMultiParam"):
                obj = InstanceMultiParam()
                obj._deserialize(item)
                self._InstanceMultiParam.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceSecurityGroupRequest(AbstractModel):
    r"""DescribeInstanceSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表，数组长度限制[0,100]。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表，数组长度限制[0,100]。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSecurityGroupResponse(AbstractModel):
    r"""DescribeInstanceSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSecurityGroupsDetail: 实例安全组信息。
        :type InstanceSecurityGroupsDetail: list of InstanceSecurityGroupDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSecurityGroupsDetail = None
        self._RequestId = None

    @property
    def InstanceSecurityGroupsDetail(self):
        r"""实例安全组信息。
        :rtype: list of InstanceSecurityGroupDetail
        """
        return self._InstanceSecurityGroupsDetail

    @InstanceSecurityGroupsDetail.setter
    def InstanceSecurityGroupsDetail(self, InstanceSecurityGroupsDetail):
        self._InstanceSecurityGroupsDetail = InstanceSecurityGroupsDetail

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
        if params.get("InstanceSecurityGroupsDetail") is not None:
            self._InstanceSecurityGroupsDetail = []
            for item in params.get("InstanceSecurityGroupsDetail"):
                obj = InstanceSecurityGroupDetail()
                obj._deserialize(item)
                self._InstanceSecurityGroupsDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceShardsRequest(AbstractModel):
    r"""DescribeInstanceShards请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _FilterSlave: 指定是否过滤掉从节信息。
- true；过滤从节点。
- false：不过滤。默认为 false。
        :type FilterSlave: bool
        """
        self._InstanceId = None
        self._FilterSlave = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FilterSlave(self):
        r"""指定是否过滤掉从节信息。
- true；过滤从节点。
- false：不过滤。默认为 false。
        :rtype: bool
        """
        return self._FilterSlave

    @FilterSlave.setter
    def FilterSlave(self, FilterSlave):
        self._FilterSlave = FilterSlave


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FilterSlave = params.get("FilterSlave")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceShardsResponse(AbstractModel):
    r"""DescribeInstanceShards返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceShards: 实例分片列表信息，包括：节点信息、节点ID、Key数量、使用容量、容量倾斜率等信息。
        :type InstanceShards: list of InstanceClusterShard
        :param _TotalCount: 实例分片节点数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceShards = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceShards(self):
        r"""实例分片列表信息，包括：节点信息、节点ID、Key数量、使用容量、容量倾斜率等信息。
        :rtype: list of InstanceClusterShard
        """
        return self._InstanceShards

    @InstanceShards.setter
    def InstanceShards(self, InstanceShards):
        self._InstanceShards = InstanceShards

    @property
    def TotalCount(self):
        r"""实例分片节点数量。
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
        if params.get("InstanceShards") is not None:
            self._InstanceShards = []
            for item in params.get("InstanceShards"):
                obj = InstanceClusterShard()
                obj._deserialize(item)
                self._InstanceShards.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstanceSpecBandwidthRequest(AbstractModel):
    r"""DescribeInstanceSpecBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。填写实例id或者规格，两者必选其一。
        :type InstanceId: str
        :param _ShardSize: 分片大小，单位：MB
        :type ShardSize: int
        :param _ShardNum: 分片数量。
        :type ShardNum: int
        :param _ReplicateNum: 复制组数量。
        :type ReplicateNum: int
        :param _ReadOnlyWeight: 只读权重。
- 100：开启从只读。
- 0：关闭从只读。
        :type ReadOnlyWeight: int
        :param _Type: 实例类型，同 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的Type。
        :type Type: int
        """
        self._InstanceId = None
        self._ShardSize = None
        self._ShardNum = None
        self._ReplicateNum = None
        self._ReadOnlyWeight = None
        self._Type = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。填写实例id或者规格，两者必选其一。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardSize(self):
        r"""分片大小，单位：MB
        :rtype: int
        """
        return self._ShardSize

    @ShardSize.setter
    def ShardSize(self, ShardSize):
        self._ShardSize = ShardSize

    @property
    def ShardNum(self):
        r"""分片数量。
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def ReplicateNum(self):
        r"""复制组数量。
        :rtype: int
        """
        return self._ReplicateNum

    @ReplicateNum.setter
    def ReplicateNum(self, ReplicateNum):
        self._ReplicateNum = ReplicateNum

    @property
    def ReadOnlyWeight(self):
        r"""只读权重。
- 100：开启从只读。
- 0：关闭从只读。
        :rtype: int
        """
        return self._ReadOnlyWeight

    @ReadOnlyWeight.setter
    def ReadOnlyWeight(self, ReadOnlyWeight):
        self._ReadOnlyWeight = ReadOnlyWeight

    @property
    def Type(self):
        r"""实例类型，同 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的Type。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardSize = params.get("ShardSize")
        self._ShardNum = params.get("ShardNum")
        self._ReplicateNum = params.get("ReplicateNum")
        self._ReadOnlyWeight = params.get("ReadOnlyWeight")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSpecBandwidthResponse(AbstractModel):
    r"""DescribeInstanceSpecBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Bandwidth: 基础带宽。
        :type Bandwidth: int
        :param _ClientLimit: 链接限制。
        :type ClientLimit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Bandwidth = None
        self._ClientLimit = None
        self._RequestId = None

    @property
    def Bandwidth(self):
        r"""基础带宽。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ClientLimit(self):
        r"""链接限制。
        :rtype: int
        """
        return self._ClientLimit

    @ClientLimit.setter
    def ClientLimit(self, ClientLimit):
        self._ClientLimit = ClientLimit

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
        self._Bandwidth = params.get("Bandwidth")
        self._ClientLimit = params.get("ClientLimit")
        self._RequestId = params.get("RequestId")


class DescribeInstanceSupportFeatureRequest(AbstractModel):
    r"""DescribeInstanceSupportFeature请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _FeatureName: 支持查询的功能特性如下所示。
- read-local-node-only：就近接入。
- multi-account：多账号管理。
- auto-failback：故障恢复场景，主节点是否开启自动回切。
        :type FeatureName: str
        """
        self._InstanceId = None
        self._FeatureName = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FeatureName(self):
        r"""支持查询的功能特性如下所示。
- read-local-node-only：就近接入。
- multi-account：多账号管理。
- auto-failback：故障恢复场景，主节点是否开启自动回切。
        :rtype: str
        """
        return self._FeatureName

    @FeatureName.setter
    def FeatureName(self, FeatureName):
        self._FeatureName = FeatureName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FeatureName = params.get("FeatureName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSupportFeatureResponse(AbstractModel):
    r"""DescribeInstanceSupportFeature返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Support: 是否支持
        :type Support: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Support = None
        self._RequestId = None

    @property
    def Support(self):
        r"""是否支持
        :rtype: bool
        """
        return self._Support

    @Support.setter
    def Support(self, Support):
        self._Support = Support

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
        self._Support = params.get("Support")
        self._RequestId = params.get("RequestId")


class DescribeInstanceZoneInfoRequest(AbstractModel):
    r"""DescribeInstanceZoneInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceZoneInfoResponse(AbstractModel):
    r"""DescribeInstanceZoneInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例节点组的个数。
        :type TotalCount: int
        :param _ReplicaGroups: 实例节点组列表。
        :type ReplicaGroups: list of ReplicaGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReplicaGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""实例节点组的个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReplicaGroups(self):
        r"""实例节点组列表。
        :rtype: list of ReplicaGroup
        """
        return self._ReplicaGroups

    @ReplicaGroups.setter
    def ReplicaGroups(self, ReplicaGroups):
        self._ReplicaGroups = ReplicaGroups

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
        if params.get("ReplicaGroups") is not None:
            self._ReplicaGroups = []
            for item in params.get("ReplicaGroups"):
                obj = ReplicaGroup()
                obj._deserialize(item)
                self._ReplicaGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页输出实例的数量，参数默认值20，最大值为1000。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。


        :type InstanceId: str
        :param _OrderBy: 实例列表排序依据，枚举值如下所示：
- projectId：依据项目ID排序。
- createtime：依据实例创建时间排序。
- instancename：依据实例名称排序。
- type：依据实例类型排序。
- curDeadline：依据实例到期时间排序。
        :type OrderBy: str
        :param _OrderType: 实例排序方式，默认为倒序排序。
- 1：倒序。
- 0：顺序。
        :type OrderType: int
        :param _VpcIds: 私有网络 ID 数组。如果不配置该参数或设置数组为空则默认选择基础网络。例如47525。该参数暂时保留，可忽略。请根据 UniqVpcIds 参数格式设置私有网络ID数组。
        :type VpcIds: list of str
        :param _SubnetIds: 私有网络所属子网 ID 数组，例如：56854。该参数暂时保留，可忽略。请根据 UniqSubnetIds 参数格式设置私有网络子网 ID 数组。
        :type SubnetIds: list of str
        :param _SearchKey: 设置模糊查询关键字段，仅实例名称支持模糊查询。
        :type SearchKey: str
        :param _ProjectIds: 项目 ID 组成的数组。
        :type ProjectIds: list of int
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _UniqVpcIds: 私有网络 ID 数组。如果不配置该参数或者设置数组为空则默认选择基础网络，如：vpc-sad23jfdfk。
        :type UniqVpcIds: list of str
        :param _UniqSubnetIds: 私有网络所属子网 ID 数组，如：subnet-fdj24n34j2。
        :type UniqSubnetIds: list of str
        :param _RegionIds: 地域 ID 数组，该参数已经弃用，可通过公共参数Region查询对应地域。
        :type RegionIds: list of int
        :param _Status: 实例状态。
- 0：待初始化。
- 1：流程中。
- 2：运行中。
- -2：已隔离。
- -3：待删除。
        :type Status: list of int
        :param _TypeVersion: 实例架构版本。
- 1：单机版。
- 2：主从版。
- 3：集群版。
        :type TypeVersion: int
        :param _EngineName: 存储引擎信息。可设置为Redis-2.8、Redis-4.0、Redis-5.0、Redis-6.0 或者 CKV。
        :type EngineName: str
        :param _AutoRenew: 续费模式。
- 0：手动续费。
- 1：自动续费。
- 2：到期不再续费。
        :type AutoRenew: list of int
        :param _BillingMode: 计费模式。
- postpaid：按量计费。
- prepaid：包年包月。
        :type BillingMode: str
        :param _Type: 实例类型。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 5：Redis 2.8 内存版（单机）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
- 200:Memcached 1.6 内存版（集群架构）。
        :type Type: int
        :param _SearchKeys: 该参数为数组类型，支持配置实例名称、实例 ID、IP地址，其中实例名称为模糊匹配，实例 ID 和 IP 地址精确匹配。

- 数组中每一个元素取并集进行匹配查询。
- **InstanceId** 与 **SearchKeys** 同时配置，则取二者交集进行匹配查询。
        :type SearchKeys: list of str
        :param _TypeList: 内部参数，用户可忽略。
        :type TypeList: list of int
        :param _MonitorVersion: 内部参数，用户可忽略。
        :type MonitorVersion: str
        :param _InstanceTags: 根据标签的 Key 和 Value 筛选资源。该参数不配置或者数组设置为空值，则不根据标签进行过滤。
        :type InstanceTags: list of InstanceTagInfo
        :param _TagKeys: 根据标签的 Key 筛选资源，该参数不配置或者数组设置为空值，则不根据标签Key进行过滤。
        :type TagKeys: list of str
        :param _ProductVersions: 实例的产品版本。如果该参数不配置或者数组设置为空值，则默认不依据此参数过滤实例。
- local：本地盘版。
- cdc：独享集群版。
        :type ProductVersions: list of str
        :param _InstanceIds: 批量查询指定的实例 ID，返回结果已 Limit 限制为主。
        :type InstanceIds: list of str
        :param _AzMode: 可用区模式。
- singleaz：单可用区。
- multiaz：多可用区。
        :type AzMode: str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceId = None
        self._OrderBy = None
        self._OrderType = None
        self._VpcIds = None
        self._SubnetIds = None
        self._SearchKey = None
        self._ProjectIds = None
        self._InstanceName = None
        self._UniqVpcIds = None
        self._UniqSubnetIds = None
        self._RegionIds = None
        self._Status = None
        self._TypeVersion = None
        self._EngineName = None
        self._AutoRenew = None
        self._BillingMode = None
        self._Type = None
        self._SearchKeys = None
        self._TypeList = None
        self._MonitorVersion = None
        self._InstanceTags = None
        self._TagKeys = None
        self._ProductVersions = None
        self._InstanceIds = None
        self._AzMode = None

    @property
    def Limit(self):
        r"""每页输出实例的数量，参数默认值20，最大值为1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。


        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OrderBy(self):
        r"""实例列表排序依据，枚举值如下所示：
- projectId：依据项目ID排序。
- createtime：依据实例创建时间排序。
- instancename：依据实例名称排序。
- type：依据实例类型排序。
- curDeadline：依据实例到期时间排序。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""实例排序方式，默认为倒序排序。
- 1：倒序。
- 0：顺序。
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def VpcIds(self):
        r"""私有网络 ID 数组。如果不配置该参数或设置数组为空则默认选择基础网络。例如47525。该参数暂时保留，可忽略。请根据 UniqVpcIds 参数格式设置私有网络ID数组。
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def SubnetIds(self):
        r"""私有网络所属子网 ID 数组，例如：56854。该参数暂时保留，可忽略。请根据 UniqSubnetIds 参数格式设置私有网络子网 ID 数组。
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SearchKey(self):
        r"""设置模糊查询关键字段，仅实例名称支持模糊查询。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        r"""项目 ID 组成的数组。
        :rtype: list of int
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def InstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def UniqVpcIds(self):
        r"""私有网络 ID 数组。如果不配置该参数或者设置数组为空则默认选择基础网络，如：vpc-sad23jfdfk。
        :rtype: list of str
        """
        return self._UniqVpcIds

    @UniqVpcIds.setter
    def UniqVpcIds(self, UniqVpcIds):
        self._UniqVpcIds = UniqVpcIds

    @property
    def UniqSubnetIds(self):
        r"""私有网络所属子网 ID 数组，如：subnet-fdj24n34j2。
        :rtype: list of str
        """
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def RegionIds(self):
        r"""地域 ID 数组，该参数已经弃用，可通过公共参数Region查询对应地域。
        :rtype: list of int
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def Status(self):
        r"""实例状态。
- 0：待初始化。
- 1：流程中。
- 2：运行中。
- -2：已隔离。
- -3：待删除。
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TypeVersion(self):
        r"""实例架构版本。
- 1：单机版。
- 2：主从版。
- 3：集群版。
        :rtype: int
        """
        return self._TypeVersion

    @TypeVersion.setter
    def TypeVersion(self, TypeVersion):
        self._TypeVersion = TypeVersion

    @property
    def EngineName(self):
        r"""存储引擎信息。可设置为Redis-2.8、Redis-4.0、Redis-5.0、Redis-6.0 或者 CKV。
        :rtype: str
        """
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def AutoRenew(self):
        r"""续费模式。
- 0：手动续费。
- 1：自动续费。
- 2：到期不再续费。
        :rtype: list of int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def BillingMode(self):
        r"""计费模式。
- postpaid：按量计费。
- prepaid：包年包月。
        :rtype: str
        """
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def Type(self):
        r"""实例类型。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 5：Redis 2.8 内存版（单机）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
- 200:Memcached 1.6 内存版（集群架构）。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SearchKeys(self):
        r"""该参数为数组类型，支持配置实例名称、实例 ID、IP地址，其中实例名称为模糊匹配，实例 ID 和 IP 地址精确匹配。

- 数组中每一个元素取并集进行匹配查询。
- **InstanceId** 与 **SearchKeys** 同时配置，则取二者交集进行匹配查询。
        :rtype: list of str
        """
        return self._SearchKeys

    @SearchKeys.setter
    def SearchKeys(self, SearchKeys):
        self._SearchKeys = SearchKeys

    @property
    def TypeList(self):
        r"""内部参数，用户可忽略。
        :rtype: list of int
        """
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList

    @property
    def MonitorVersion(self):
        r"""内部参数，用户可忽略。
        :rtype: str
        """
        return self._MonitorVersion

    @MonitorVersion.setter
    def MonitorVersion(self, MonitorVersion):
        self._MonitorVersion = MonitorVersion

    @property
    def InstanceTags(self):
        r"""根据标签的 Key 和 Value 筛选资源。该参数不配置或者数组设置为空值，则不根据标签进行过滤。
        :rtype: list of InstanceTagInfo
        """
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def TagKeys(self):
        r"""根据标签的 Key 筛选资源，该参数不配置或者数组设置为空值，则不根据标签Key进行过滤。
        :rtype: list of str
        """
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def ProductVersions(self):
        r"""实例的产品版本。如果该参数不配置或者数组设置为空值，则默认不依据此参数过滤实例。
- local：本地盘版。
- cdc：独享集群版。
        :rtype: list of str
        """
        return self._ProductVersions

    @ProductVersions.setter
    def ProductVersions(self, ProductVersions):
        self._ProductVersions = ProductVersions

    @property
    def InstanceIds(self):
        r"""批量查询指定的实例 ID，返回结果已 Limit 限制为主。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AzMode(self):
        r"""可用区模式。
- singleaz：单可用区。
- multiaz：多可用区。
        :rtype: str
        """
        return self._AzMode

    @AzMode.setter
    def AzMode(self, AzMode):
        self._AzMode = AzMode


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceId = params.get("InstanceId")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._VpcIds = params.get("VpcIds")
        self._SubnetIds = params.get("SubnetIds")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._InstanceName = params.get("InstanceName")
        self._UniqVpcIds = params.get("UniqVpcIds")
        self._UniqSubnetIds = params.get("UniqSubnetIds")
        self._RegionIds = params.get("RegionIds")
        self._Status = params.get("Status")
        self._TypeVersion = params.get("TypeVersion")
        self._EngineName = params.get("EngineName")
        self._AutoRenew = params.get("AutoRenew")
        self._BillingMode = params.get("BillingMode")
        self._Type = params.get("Type")
        self._SearchKeys = params.get("SearchKeys")
        self._TypeList = params.get("TypeList")
        self._MonitorVersion = params.get("MonitorVersion")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        self._TagKeys = params.get("TagKeys")
        self._ProductVersions = params.get("ProductVersions")
        self._InstanceIds = params.get("InstanceIds")
        self._AzMode = params.get("AzMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    r"""DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数量。
        :type TotalCount: int
        :param _InstanceSet: 实例详细信息列表。
        :type InstanceSet: list of InstanceSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""实例总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        r"""实例详细信息列表。
        :rtype: list of InstanceSet
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = InstanceSet()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaintenanceWindowRequest(AbstractModel):
    r"""DescribeMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaintenanceWindowResponse(AbstractModel):
    r"""DescribeMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 维护时间窗开始时间。取值范围为"00:00-23:00"的任意时间点，如03:24。
        :type StartTime: str
        :param _EndTime: 维护时间窗结束时间。
- 取值范围为"00:00-23:00"的任意时间点，如：04:24。
- 维护时间持续时长最小为30分钟，最大为3小时。
- 结束时间务必是基于开始时间向后的时间。
        :type EndTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""维护时间窗开始时间。取值范围为"00:00-23:00"的任意时间点，如03:24。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""维护时间窗结束时间。
- 取值范围为"00:00-23:00"的任意时间点，如：04:24。
- 维护时间持续时长最小为30分钟，最大为3小时。
- 结束时间务必是基于开始时间向后的时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    r"""DescribeParamTemplateInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 指定查询的参数模板 ID。请通过接口[DescribeParamTemplates](https://cloud.tencent.com/document/product/239/58750)获取参数模板列表信息。
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""指定查询的参数模板 ID。请通过接口[DescribeParamTemplates](https://cloud.tencent.com/document/product/239/58750)获取参数模板列表信息。
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
        


class DescribeParamTemplateInfoResponse(AbstractModel):
    r"""DescribeParamTemplateInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数模板的参数数量。
        :type TotalCount: int
        :param _TemplateId: 参数模板 ID。
        :type TemplateId: str
        :param _Name: 参数模板名称。
        :type Name: str
        :param _ProductType: 产品类型。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 5：Redis 2.8 内存版（单机）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
        :type ProductType: int
        :param _Description: 参数模板描述。
        :type Description: str
        :param _Items: 参数详情。包含：参数的名称，当前运行值，默认值，最大值、最小值、枚举值等信息。
        :type Items: list of ParameterDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TemplateId = None
        self._Name = None
        self._ProductType = None
        self._Description = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""参数模板的参数数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TemplateId(self):
        r"""参数模板 ID。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        r"""参数模板名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductType(self):
        r"""产品类型。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 5：Redis 2.8 内存版（单机）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def Description(self):
        r"""参数模板描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Items(self):
        r"""参数详情。包含：参数的名称，当前运行值，默认值，最大值、最小值、枚举值等信息。
        :rtype: list of ParameterDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._ProductType = params.get("ProductType")
        self._Description = params.get("Description")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    r"""DescribeParamTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductTypes: 产品类型数组。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
        :type ProductTypes: list of int
        :param _TemplateNames: 模板名称数组。数组最大长度限制为50
        :type TemplateNames: list of str
        :param _TemplateIds: 模板ID数组。数组最大长度限制为50
        :type TemplateIds: list of str
        """
        self._ProductTypes = None
        self._TemplateNames = None
        self._TemplateIds = None

    @property
    def ProductTypes(self):
        r"""产品类型数组。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
        :rtype: list of int
        """
        return self._ProductTypes

    @ProductTypes.setter
    def ProductTypes(self, ProductTypes):
        self._ProductTypes = ProductTypes

    @property
    def TemplateNames(self):
        r"""模板名称数组。数组最大长度限制为50
        :rtype: list of str
        """
        return self._TemplateNames

    @TemplateNames.setter
    def TemplateNames(self, TemplateNames):
        self._TemplateNames = TemplateNames

    @property
    def TemplateIds(self):
        r"""模板ID数组。数组最大长度限制为50
        :rtype: list of str
        """
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds


    def _deserialize(self, params):
        self._ProductTypes = params.get("ProductTypes")
        self._TemplateNames = params.get("TemplateNames")
        self._TemplateIds = params.get("TemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    r"""DescribeParamTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该用户的参数模板数量。
        :type TotalCount: int
        :param _Items: 参数模板详情。
        :type Items: list of ParamTemplateInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""该用户的参数模板数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""参数模板详情。
        :rtype: list of ParamTemplateInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    r"""DescribeProductInfo请求参数结构体

    """


class DescribeProductInfoResponse(AbstractModel):
    r"""DescribeProductInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 地域售卖信息。即使指定具体地域，也返回所有地域的售卖信息。
        :type RegionSet: list of RegionConf
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        r"""地域售卖信息。即使指定具体地域，也返回所有地域的售卖信息。
        :rtype: list of RegionConf
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
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionConf()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupRequest(AbstractModel):
    r"""DescribeProjectSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 指定查询的项目 ID。
- 0：默认项目。
- -1：所有项目。
- 大于0：特定项目。请登录[Redis控制台的项目管理](https://console.cloud.tencent.com/project)页面，在**项目名称**中复制项目 ID。
        :type ProjectId: int
        :param _SecurityGroupId: 安全组 ID，通过接口[DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447)的返回参数 **InstanceSecurityGroupsDetail** 的子参数 **SecurityGroupId** 获取。
        :type SecurityGroupId: str
        """
        self._ProjectId = None
        self._SecurityGroupId = None

    @property
    def ProjectId(self):
        r"""指定查询的项目 ID。
- 0：默认项目。
- -1：所有项目。
- 大于0：特定项目。请登录[Redis控制台的项目管理](https://console.cloud.tencent.com/project)页面，在**项目名称**中复制项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupId(self):
        r"""安全组 ID，通过接口[DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447)的返回参数 **InstanceSecurityGroupsDetail** 的子参数 **SecurityGroupId** 获取。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupResponse(AbstractModel):
    r"""DescribeProjectSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupDetails: 项目安全组
        :type SecurityGroupDetails: list of SecurityGroupDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroupDetails = None
        self._RequestId = None

    @property
    def SecurityGroupDetails(self):
        r"""项目安全组
        :rtype: list of SecurityGroupDetail
        """
        return self._SecurityGroupDetails

    @SecurityGroupDetails.setter
    def SecurityGroupDetails(self, SecurityGroupDetails):
        self._SecurityGroupDetails = SecurityGroupDetails

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
        if params.get("SecurityGroupDetails") is not None:
            self._SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self._SecurityGroupDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    r"""DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _ProjectId: 项目 ID，请登录[Redis控制台的项目管理](https://console.cloud.tencent.com/project)页面，在**项目名称**中复制项目 ID。
        :type ProjectId: int
        :param _Offset: 偏移量，取值为Limit的整数倍。
        :type Offset: int
        :param _Limit: 拉取数量限制，默认 20。
        :type Limit: int
        :param _SearchKey: 搜索条件，支持安全组 ID 或者安全组名称。
        :type SearchKey: str
        """
        self._Product = None
        self._ProjectId = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None

    @property
    def Product(self):
        r"""数据库引擎名称，本接口取值：redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProjectId(self):
        r"""项目 ID，请登录[Redis控制台的项目管理](https://console.cloud.tencent.com/project)页面，在**项目名称**中复制项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Offset(self):
        r"""偏移量，取值为Limit的整数倍。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""拉取数量限制，默认 20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        r"""搜索条件，支持安全组 ID 或者安全组名称。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProjectId = params.get("ProjectId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    r"""DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组规则。
        :type Groups: list of SecurityGroup
        :param _Total: 符合条件的安全组总数量。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        r"""安全组规则。
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        r"""符合条件的安全组总数量。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProxySlowLogRequest(AbstractModel):
    r"""DescribeProxySlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :type InstanceId: str
        :param _BeginTime: 慢查询的开始时间，查询时间最大跨度30天。
        :type BeginTime: str
        :param _EndTime: 慢查询的结束时间，查询时间最大跨度30天。
        :type EndTime: str
        :param _MinQueryTime: 慢查询阈值。取值为大于0 的正整数。单位：毫秒。
        :type MinQueryTime: int
        :param _Limit: 每页输出的任务列表大小。默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param _Offset: 分页偏移量。默认为0。取值为 Limit 整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._MinQueryTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        r"""慢查询的开始时间，查询时间最大跨度30天。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""慢查询的结束时间，查询时间最大跨度30天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        r"""慢查询阈值。取值为大于0 的正整数。单位：毫秒。
        :rtype: int
        """
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

    @property
    def Limit(self):
        r"""每页输出的任务列表大小。默认值为20，最小值为1，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量。默认为0。取值为 Limit 整数倍。计算公式：offset=limit*(页码-1)。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._MinQueryTime = params.get("MinQueryTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySlowLogResponse(AbstractModel):
    r"""DescribeProxySlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 慢查询总数。
        :type TotalCount: int
        :param _InstanceProxySlowLogDetail: 慢查询详情，注意：TotalCount大于1W，即慢日志超过1万条，不支持返回日志详情，返回数据为空。 建议缩小BeginTime和EndTime的时间间隔，多次查询。
        :type InstanceProxySlowLogDetail: list of InstanceProxySlowlogDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceProxySlowLogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""慢查询总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceProxySlowLogDetail(self):
        r"""慢查询详情，注意：TotalCount大于1W，即慢日志超过1万条，不支持返回日志详情，返回数据为空。 建议缩小BeginTime和EndTime的时间间隔，多次查询。
        :rtype: list of InstanceProxySlowlogDetail
        """
        return self._InstanceProxySlowLogDetail

    @InstanceProxySlowLogDetail.setter
    def InstanceProxySlowLogDetail(self, InstanceProxySlowLogDetail):
        self._InstanceProxySlowLogDetail = InstanceProxySlowLogDetail

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
        if params.get("InstanceProxySlowLogDetail") is not None:
            self._InstanceProxySlowLogDetail = []
            for item in params.get("InstanceProxySlowLogDetail"):
                obj = InstanceProxySlowlogDetail()
                obj._deserialize(item)
                self._InstanceProxySlowLogDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRedisClusterOverviewRequest(AbstractModel):
    r"""DescribeRedisClusterOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 本地专用集群 ID，请登录[专用集群控制台](https://console.cloud.tencent.com/cdc/dedicatedcluster/index?rid=1
)实例列表获取集群 ID。
        :type DedicatedClusterId: str
        """
        self._DedicatedClusterId = None

    @property
    def DedicatedClusterId(self):
        r"""本地专用集群 ID，请登录[专用集群控制台](https://console.cloud.tencent.com/cdc/dedicatedcluster/index?rid=1
)实例列表获取集群 ID。
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisClusterOverviewResponse(AbstractModel):
    r"""DescribeRedisClusterOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalBundle: 资源包总数
        :type TotalBundle: int
        :param _TotalMemory: 资源包总内存大小，单位：GB
        :type TotalMemory: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalBundle = None
        self._TotalMemory = None
        self._RequestId = None

    @property
    def TotalBundle(self):
        r"""资源包总数
        :rtype: int
        """
        return self._TotalBundle

    @TotalBundle.setter
    def TotalBundle(self, TotalBundle):
        self._TotalBundle = TotalBundle

    @property
    def TotalMemory(self):
        r"""资源包总内存大小，单位：GB
        :rtype: int
        """
        return self._TotalMemory

    @TotalMemory.setter
    def TotalMemory(self, TotalMemory):
        self._TotalMemory = TotalMemory

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
        self._TotalBundle = params.get("TotalBundle")
        self._TotalMemory = params.get("TotalMemory")
        self._RequestId = params.get("RequestId")


class DescribeRedisClustersRequest(AbstractModel):
    r"""DescribeRedisClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RedisClusterIds: Redis独享集群 ID。请登录[专用集群控制台](https://console.cloud.tencent.com/cdc/dedicatedcluster/index?rid=1
)切换至**云服务管理**页面，在下拉框选择**云数据库 Redis**，可获取独享集群ID。
        :type RedisClusterIds: list of str
        :param _Status: 集群状态。
- 1：流程。
- 2：运行中。
- 3：已隔离。
        :type Status: list of int
        :param _ProjectIds: 项目ID数组。请登录[项目管理](https://console.cloud.tencent.com/project)页面，在**项目名称**中复制项目 ID。
        :type ProjectIds: list of int
        :param _AutoRenewFlag: 续费模式。
- 0：默认状态，手动续费。
- 1：自动续费。
- 2：明确不自动续费。
        :type AutoRenewFlag: list of int
        :param _ClusterName: Redis 独享集群名称。
        :type ClusterName: str
        :param _SearchKey: 搜索关键词：支持集群 ID、集群名称。
        :type SearchKey: str
        :param _Limit: 分页限制返回大小，不传则默认为20。
        :type Limit: int
        :param _Offset: 偏移量，取Limit整数倍
        :type Offset: int
        :param _DedicatedClusterId: 本地专用集群 ID，请登录[专用集群控制台](https://console.cloud.tencent.com/cdc/dedicatedcluster/index?rid=1
)实例列表获取集群 ID。
        :type DedicatedClusterId: str
        """
        self._RedisClusterIds = None
        self._Status = None
        self._ProjectIds = None
        self._AutoRenewFlag = None
        self._ClusterName = None
        self._SearchKey = None
        self._Limit = None
        self._Offset = None
        self._DedicatedClusterId = None

    @property
    def RedisClusterIds(self):
        r"""Redis独享集群 ID。请登录[专用集群控制台](https://console.cloud.tencent.com/cdc/dedicatedcluster/index?rid=1
)切换至**云服务管理**页面，在下拉框选择**云数据库 Redis**，可获取独享集群ID。
        :rtype: list of str
        """
        return self._RedisClusterIds

    @RedisClusterIds.setter
    def RedisClusterIds(self, RedisClusterIds):
        self._RedisClusterIds = RedisClusterIds

    @property
    def Status(self):
        r"""集群状态。
- 1：流程。
- 2：运行中。
- 3：已隔离。
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectIds(self):
        r"""项目ID数组。请登录[项目管理](https://console.cloud.tencent.com/project)页面，在**项目名称**中复制项目 ID。
        :rtype: list of int
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def AutoRenewFlag(self):
        r"""续费模式。
- 0：默认状态，手动续费。
- 1：自动续费。
- 2：明确不自动续费。
        :rtype: list of int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ClusterName(self):
        r"""Redis 独享集群名称。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def SearchKey(self):
        r"""搜索关键词：支持集群 ID、集群名称。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Limit(self):
        r"""分页限制返回大小，不传则默认为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，取Limit整数倍
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DedicatedClusterId(self):
        r"""本地专用集群 ID，请登录[专用集群控制台](https://console.cloud.tencent.com/cdc/dedicatedcluster/index?rid=1
)实例列表获取集群 ID。
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._RedisClusterIds = params.get("RedisClusterIds")
        self._Status = params.get("Status")
        self._ProjectIds = params.get("ProjectIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ClusterName = params.get("ClusterName")
        self._SearchKey = params.get("SearchKey")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisClustersResponse(AbstractModel):
    r"""DescribeRedisClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 集群总数
        :type Total: int
        :param _Resources: CDC集群资源列表
        :type Resources: list of CDCResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Resources = None
        self._RequestId = None

    @property
    def Total(self):
        r"""集群总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Resources(self):
        r"""CDC集群资源列表
        :rtype: list of CDCResource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

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
        self._Total = params.get("Total")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = CDCResource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReplicationGroupInstanceRequest(AbstractModel):
    r"""DescribeReplicationGroupInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationGroupInstanceResponse(AbstractModel):
    r"""DescribeReplicationGroupInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: AppID。
        :type AppId: int
        :param _RegionId: 地域数字编号。
        :type RegionId: int
        :param _GroupId: 复制组字符串ID。
        :type GroupId: str
        :param _GroupName: 复制组名称。
        :type GroupName: str
        :param _InstanceRole: 实例复制组角色。
- r:  备实例
- rw: 主实例
        :type InstanceRole: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._RegionId = None
        self._GroupId = None
        self._GroupName = None
        self._InstanceRole = None
        self._RequestId = None

    @property
    def AppId(self):
        r"""AppID。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RegionId(self):
        r"""地域数字编号。
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def GroupId(self):
        r"""复制组字符串ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""复制组名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceRole(self):
        r"""实例复制组角色。
- r:  备实例
- rw: 主实例
        :rtype: str
        """
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

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
        self._AppId = params.get("AppId")
        self._RegionId = params.get("RegionId")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._InstanceRole = params.get("InstanceRole")
        self._RequestId = params.get("RequestId")


class DescribeReplicationGroupRequest(AbstractModel):
    r"""DescribeReplicationGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页输出实例列表的大小。取值为大于0 的正整数，默认为20。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _GroupId: 指定复制组 ID。例如：crs-rpl-m3zt****。请登录[Redis 控制台](https://console.cloud.tencent.com/redis/replication)的全球复制组列表获取复制组 ID。
        :type GroupId: str
        :param _SearchKey: 模糊查询的关键字，可以设置为复制组ID或复制组名称进行模糊查询。请登录[Redis 控制台](https://console.cloud.tencent.com/redis/replication)的全球复制组列表获取复制组 ID及名称。
        :type SearchKey: str
        """
        self._Limit = None
        self._Offset = None
        self._GroupId = None
        self._SearchKey = None

    @property
    def Limit(self):
        r"""每页输出实例列表的大小。取值为大于0 的正整数，默认为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def GroupId(self):
        r"""指定复制组 ID。例如：crs-rpl-m3zt****。请登录[Redis 控制台](https://console.cloud.tencent.com/redis/replication)的全球复制组列表获取复制组 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchKey(self):
        r"""模糊查询的关键字，可以设置为复制组ID或复制组名称进行模糊查询。请登录[Redis 控制台](https://console.cloud.tencent.com/redis/replication)的全球复制组列表获取复制组 ID及名称。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._GroupId = params.get("GroupId")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationGroupResponse(AbstractModel):
    r"""DescribeReplicationGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 复制组数量。
        :type TotalCount: int
        :param _Groups: 复制组信息。
        :type Groups: list of Groups
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""复制组数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        r"""复制组信息。
        :rtype: list of Groups
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = Groups()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSSLStatusRequest(AbstractModel):
    r"""DescribeSSLStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSSLStatusResponse(AbstractModel):
    r"""DescribeSSLStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertDownloadUrl: SSL 证书下载地址。
        :type CertDownloadUrl: str
        :param _UrlExpiredTime: 证书下载链接到期时间。
        :type UrlExpiredTime: str
        :param _SSLConfig: 标识实例开启 SSL 功能。
- true：开启 。
- false：关闭。
        :type SSLConfig: bool
        :param _FeatureSupport: 标识实例是否支持 SSL特性。
- true：支持。
- false：不支持。
        :type FeatureSupport: bool
        :param _Status: 说明配置 SSL 的状态。
- 1: 配置中。
- 2：配置成功。
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertDownloadUrl = None
        self._UrlExpiredTime = None
        self._SSLConfig = None
        self._FeatureSupport = None
        self._Status = None
        self._RequestId = None

    @property
    def CertDownloadUrl(self):
        r"""SSL 证书下载地址。
        :rtype: str
        """
        return self._CertDownloadUrl

    @CertDownloadUrl.setter
    def CertDownloadUrl(self, CertDownloadUrl):
        self._CertDownloadUrl = CertDownloadUrl

    @property
    def UrlExpiredTime(self):
        r"""证书下载链接到期时间。
        :rtype: str
        """
        return self._UrlExpiredTime

    @UrlExpiredTime.setter
    def UrlExpiredTime(self, UrlExpiredTime):
        self._UrlExpiredTime = UrlExpiredTime

    @property
    def SSLConfig(self):
        r"""标识实例开启 SSL 功能。
- true：开启 。
- false：关闭。
        :rtype: bool
        """
        return self._SSLConfig

    @SSLConfig.setter
    def SSLConfig(self, SSLConfig):
        self._SSLConfig = SSLConfig

    @property
    def FeatureSupport(self):
        r"""标识实例是否支持 SSL特性。
- true：支持。
- false：不支持。
        :rtype: bool
        """
        return self._FeatureSupport

    @FeatureSupport.setter
    def FeatureSupport(self, FeatureSupport):
        self._FeatureSupport = FeatureSupport

    @property
    def Status(self):
        r"""说明配置 SSL 的状态。
- 1: 配置中。
- 2：配置成功。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._CertDownloadUrl = params.get("CertDownloadUrl")
        self._UrlExpiredTime = params.get("UrlExpiredTime")
        self._SSLConfig = params.get("SSLConfig")
        self._FeatureSupport = params.get("FeatureSupport")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeSecondLevelBackupInfoRequest(AbstractModel):
    r"""DescribeSecondLevelBackupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _BackupTimestamp: 秒级备份时间戳。
- 设置范围：支持7天内任意秒级时间点。
-  时间戳格式：Unix 时间戳。
        :type BackupTimestamp: int
        """
        self._InstanceId = None
        self._BackupTimestamp = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupTimestamp(self):
        r"""秒级备份时间戳。
- 设置范围：支持7天内任意秒级时间点。
-  时间戳格式：Unix 时间戳。
        :rtype: int
        """
        return self._BackupTimestamp

    @BackupTimestamp.setter
    def BackupTimestamp(self, BackupTimestamp):
        self._BackupTimestamp = BackupTimestamp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupTimestamp = params.get("BackupTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecondLevelBackupInfoResponse(AbstractModel):
    r"""DescribeSecondLevelBackupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份记录ID。
        :type BackupId: str
        :param _BackupTimestamp: 备份时间戳。
        :type BackupTimestamp: int
        :param _MissingTimestamps: 备份不存在的时间戳范围。
注意：此字段可能返回 null，表示取不到有效值。
        :type MissingTimestamps: list of SecondLevelBackupMissingTimestamps
        :param _StartTimestamp: 实例开启秒级备份的时间戳。
        :type StartTimestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupId = None
        self._BackupTimestamp = None
        self._MissingTimestamps = None
        self._StartTimestamp = None
        self._RequestId = None

    @property
    def BackupId(self):
        r"""备份记录ID。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupTimestamp(self):
        r"""备份时间戳。
        :rtype: int
        """
        return self._BackupTimestamp

    @BackupTimestamp.setter
    def BackupTimestamp(self, BackupTimestamp):
        self._BackupTimestamp = BackupTimestamp

    @property
    def MissingTimestamps(self):
        r"""备份不存在的时间戳范围。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SecondLevelBackupMissingTimestamps
        """
        return self._MissingTimestamps

    @MissingTimestamps.setter
    def MissingTimestamps(self, MissingTimestamps):
        self._MissingTimestamps = MissingTimestamps

    @property
    def StartTimestamp(self):
        r"""实例开启秒级备份的时间戳。
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

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
        self._BackupId = params.get("BackupId")
        self._BackupTimestamp = params.get("BackupTimestamp")
        if params.get("MissingTimestamps") is not None:
            self._MissingTimestamps = []
            for item in params.get("MissingTimestamps"):
                obj = SecondLevelBackupMissingTimestamps()
                obj._deserialize(item)
                self._MissingTimestamps.append(obj)
        self._StartTimestamp = params.get("StartTimestamp")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    r"""DescribeSlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :type InstanceId: str
        :param _BeginTime: 预查询慢日志的起始时间，查询时间最大跨度30天。
        :type BeginTime: str
        :param _EndTime: 预查询慢日志的结束时间，查询时间最大跨度30天
        :type EndTime: str
        :param _MinQueryTime: 慢查询平均执行时间阈值。取值为大于0 的正整数。单位：毫秒。
        :type MinQueryTime: int
        :param _Limit: 每个页面展示的慢查询条数，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param _Offset: 慢查询条数的偏移量。默认为0。取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _Role: 节点所属角色。
- master：主节点。
- slave：从节点。
        :type Role: str
        """
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._MinQueryTime = None
        self._Limit = None
        self._Offset = None
        self._Role = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        r"""预查询慢日志的起始时间，查询时间最大跨度30天。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""预查询慢日志的结束时间，查询时间最大跨度30天
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        r"""慢查询平均执行时间阈值。取值为大于0 的正整数。单位：毫秒。
        :rtype: int
        """
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

    @property
    def Limit(self):
        r"""每个页面展示的慢查询条数，默认值为20，最小值为1，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""慢查询条数的偏移量。默认为0。取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Role(self):
        r"""节点所属角色。
- master：主节点。
- slave：从节点。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._MinQueryTime = params.get("MinQueryTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogResponse(AbstractModel):
    r"""DescribeSlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 慢查询总数。
        :type TotalCount: int
        :param _InstanceSlowlogDetail: 已废弃，该参数存在命名不规范问题，后续用参数InstanceSlowLogDetail取代。慢查询详情。
        :type InstanceSlowlogDetail: list of InstanceSlowlogDetail
        :param _InstanceSlowLogDetail: 慢查询详情，注意：TotalCount大于1W，即慢日志超过1万条，不支持返回日志详情，返回数据为空。 建议缩小BeginTime和EndTime的时间间隔，多次查询。
        :type InstanceSlowLogDetail: list of InstanceSlowlogDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSlowlogDetail = None
        self._InstanceSlowLogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""慢查询总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSlowlogDetail(self):
        warnings.warn("parameter `InstanceSlowlogDetail` is deprecated", DeprecationWarning) 

        r"""已废弃，该参数存在命名不规范问题，后续用参数InstanceSlowLogDetail取代。慢查询详情。
        :rtype: list of InstanceSlowlogDetail
        """
        return self._InstanceSlowlogDetail

    @InstanceSlowlogDetail.setter
    def InstanceSlowlogDetail(self, InstanceSlowlogDetail):
        warnings.warn("parameter `InstanceSlowlogDetail` is deprecated", DeprecationWarning) 

        self._InstanceSlowlogDetail = InstanceSlowlogDetail

    @property
    def InstanceSlowLogDetail(self):
        r"""慢查询详情，注意：TotalCount大于1W，即慢日志超过1万条，不支持返回日志详情，返回数据为空。 建议缩小BeginTime和EndTime的时间间隔，多次查询。
        :rtype: list of InstanceSlowlogDetail
        """
        return self._InstanceSlowLogDetail

    @InstanceSlowLogDetail.setter
    def InstanceSlowLogDetail(self, InstanceSlowLogDetail):
        self._InstanceSlowLogDetail = InstanceSlowLogDetail

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
        if params.get("InstanceSlowlogDetail") is not None:
            self._InstanceSlowlogDetail = []
            for item in params.get("InstanceSlowlogDetail"):
                obj = InstanceSlowlogDetail()
                obj._deserialize(item)
                self._InstanceSlowlogDetail.append(obj)
        if params.get("InstanceSlowLogDetail") is not None:
            self._InstanceSlowLogDetail = []
            for item in params.get("InstanceSlowLogDetail"):
                obj = InstanceSlowlogDetail()
                obj._deserialize(item)
                self._InstanceSlowLogDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    r"""DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID, 请通过接口[DescribeTaskList](https://cloud.tencent.com/document/product/239/39374) 的返回参数 **Tasks** 的子参数 **TaskId** 获取。
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务 ID, 请通过接口[DescribeTaskList](https://cloud.tencent.com/document/product/239/39374) 的返回参数 **Tasks** 的子参数 **TaskId** 获取。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    r"""DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。
- preparing：待执行。
- running：执行中。
- succeed：成功。
- failed：失败。
- error：执行出错。
        :type Status: str
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _TaskType: 任务类型。常见的类型包含：新建类型、配置变更、关闭实例、清空实例、重置密码、版本升级、备份实例、改变网络类型、实例可用区迁移、手动提主等。
        :type TaskType: str
        :param _InstanceId: 实例的 ID。
        :type InstanceId: str
        :param _TaskMessage: 任务执行返回的信息，执行错误时显示错误信息。执行中或执行成功则为空。
        :type TaskMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._StartTime = None
        self._TaskType = None
        self._InstanceId = None
        self._TaskMessage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。
- preparing：待执行。
- running：执行中。
- succeed：成功。
- failed：失败。
- error：执行出错。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""任务开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskType(self):
        r"""任务类型。常见的类型包含：新建类型、配置变更、关闭实例、清空实例、重置密码、版本升级、备份实例、改变网络类型、实例可用区迁移、手动提主等。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InstanceId(self):
        r"""实例的 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskMessage(self):
        r"""任务执行返回的信息，执行错误时显示错误信息。执行中或执行成功则为空。
        :rtype: str
        """
        return self._TaskMessage

    @TaskMessage.setter
    def TaskMessage(self, TaskMessage):
        self._TaskMessage = TaskMessage

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
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._TaskType = params.get("TaskType")
        self._InstanceId = params.get("InstanceId")
        self._TaskMessage = params.get("TaskMessage")
        self._RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    r"""DescribeTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例名称。
        :type InstanceName: str
        :param _Limit: 每页输出的任务列表大小。默认为 20，最多输出100条。
        :type Limit: int
        :param _Offset: 分页偏移量。取值需为 Limit 的整数倍：offset=limit*(页码-1)，默认值为0。
        :type Offset: int
        :param _ProjectIds: 该字段已废弃, 请忽略, 项目 ID
        :type ProjectIds: list of int
        :param _TaskTypes: 任务类型。

- FLOW_CREATE: "001"，新建实例。
- FLOW_RESIZE ： "002"，配置变更。
- FLOW_CLOSE："003"，关闭实例。
- FLOW_CLEAN： "004"，清空实例。
- FLOW_STARTUP："005"，实例启用。
- FLOW_DELETE："006"，删除实例。
- FLOW_SETPWD："007"，重置密码。
- FLOW_EXPORTBACKUP："009"，导出备份文件。
- FLOW_RESTOREBACKUP："010"，恢复备份。
- FLOW_BACKUPINSTANCE："012"，备份实例。
- FLOW_MIGRATEINSTANCE："013"，迁移实例。
- FLOW_DELBACKUP："014"，删除备份。
- FLOW_EXCHANGEINSTANCE： "016"，切换实例流程。
- FLOW_AUTOBACKUP："017"，自动备份实例。
- FLOW_MIGRATECHECK： "022"，迁移参数校验。
- FLOW_MIGRATETASK："023"，数据迁移中。
- FLOW_CLEANDB："025"，清空某个数据库。
- FLOW_CLONEBACKUP："026"，克隆备份。
- FLOW_CHANGEVIP： "027"，改变vip地址。
- FLOW_EXPORSHR ："028"，扩缩容。
- FLOW_ADDNODES："029"，加（减）节点。
- FLOW_CHANGENET："031"，改变网络类型。
- FLOW_MODIFYINSTACEREADONLY："033"，只读策略变更。
- FLOW_MODIFYINSTANCEPARAMS："034"，修改实例参数。
- FLOW_MODIFYINSTANCEPASSWORDFREE："035"，设置免密。
- FLOW_SWITCHINSTANCEVIP："036"，实例VIP切换。
- FLOW_MODIFYINSTANCEACCOUNT："037"，实例账号变更。
- FLOW_MODIFYINSTANCEBANDWIDTH："038"，实例带宽变更。
- FLOW_ENABLEINSTANCE_REPLICATE："039"，开启副本只读。
- FLOW_DISABLEINSTANCE_REPLICATE："040"，关闭副本只读。
- FLOW_UpgradeArch："041"，实例架构升级，主从升集群。
- FLOW_DowngradeArch： "042"，实例架构降级，集群降主从。
- FLOW_UpgradeVersion： "043"，版本升级。
- FLOW_MODIFYCONNECTIONCONFIG："044"，带宽连接数调整，
- FLOW_CLEARNETWORK："045"，更换网络，
- FLOW_REMOVE_BACKUP_FILE："046"，删除备份。
- FLOW_UPGRADE_SUPPORT_MULTI_AZ："047"，升级实例支持多可用区。
- FLOW_SHUTDOWN_MASTER："048"，模拟故障。
- FLOW_CHANGE_REPLICA_TO_MASTER："049"，手动提主。
- FLOW_CODE_ADD_REPLICATION_INSTANCE："050"，新增复制组。
- FLOW_OPEN_WAN："052"，开通外网。
- FLOW_CLOSE_WAN："053"，关闭外网FLOW_UPDATE_WAN："054"，更新外网。
- FLOW_CODE_DELETE_REPLICATION_INSTANCE："055"，解绑复制组。
- FLOW_CODE_CHANGE_MASTER_INSTANCE："056"，复制组实例切主。
- FLOW_CODE_CHANGE_INSTANCE_ROLE： "057"，更改复制组实例角色。
- FLOW_MIGRATE_NODE："058"，迁移节点。
- FLOW_SWITCH_NODE："059"，切换节点。
- FLOW_UPGRADE_SMALL_VERSION："060"，升级 Redis版本。
- FLOW_UPGRADE_PROXY_VERSION："061"，升级 Proxy 版本。
- FLOW_MODIFY_INSTANCE_NETWORK： "062"，实例修改网络。
- FLOW_MIGRATE_PROXY_NODE："063"，迁移proxy节点。
- FLOW_MIGRATION_INSTANCE_ZONE："066"，实例可用区迁移中。
- FLOW_UPGRADE_INSTANCE_CACHE_AND_PROXY： "067"，实例版本升级中。
- FLOW_MODIFY_PROXY_NUM："069"，加（减）Proxy 节点。
- FLOW_MODIFYBACKUPMOD："070"，变更实例备份模式。
        :type TaskTypes: list of str
        :param _BeginTime: 任务执行的起始时间，格式如：2021-12-30 00:00:00，支持查询近30天内数据。
        :type BeginTime: str
        :param _EndTime: 任务运行的终止时间。格式如：2021-12-30 20:59:35，支持查询近30天内数据。
        :type EndTime: str
        :param _TaskStatus: 该参数为内部使用，请忽略。
        :type TaskStatus: list of int
        :param _Result: 任务执行状态。
- 0：任务初始化。
- 1：执行中。
- 2：完成。
- 4：失败。
        :type Result: list of int
        :param _OperatorUin: 该字段已废弃，使用OperateUin代替，请忽略。
        :type OperatorUin: list of int
        :param _OperateUin: 操作者账号 ID，UIN。
        :type OperateUin: list of str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Limit = None
        self._Offset = None
        self._ProjectIds = None
        self._TaskTypes = None
        self._BeginTime = None
        self._EndTime = None
        self._TaskStatus = None
        self._Result = None
        self._OperatorUin = None
        self._OperateUin = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Limit(self):
        r"""每页输出的任务列表大小。默认为 20，最多输出100条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量。取值需为 Limit 的整数倍：offset=limit*(页码-1)，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ProjectIds(self):
        warnings.warn("parameter `ProjectIds` is deprecated", DeprecationWarning) 

        r"""该字段已废弃, 请忽略, 项目 ID
        :rtype: list of int
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        warnings.warn("parameter `ProjectIds` is deprecated", DeprecationWarning) 

        self._ProjectIds = ProjectIds

    @property
    def TaskTypes(self):
        r"""任务类型。

- FLOW_CREATE: "001"，新建实例。
- FLOW_RESIZE ： "002"，配置变更。
- FLOW_CLOSE："003"，关闭实例。
- FLOW_CLEAN： "004"，清空实例。
- FLOW_STARTUP："005"，实例启用。
- FLOW_DELETE："006"，删除实例。
- FLOW_SETPWD："007"，重置密码。
- FLOW_EXPORTBACKUP："009"，导出备份文件。
- FLOW_RESTOREBACKUP："010"，恢复备份。
- FLOW_BACKUPINSTANCE："012"，备份实例。
- FLOW_MIGRATEINSTANCE："013"，迁移实例。
- FLOW_DELBACKUP："014"，删除备份。
- FLOW_EXCHANGEINSTANCE： "016"，切换实例流程。
- FLOW_AUTOBACKUP："017"，自动备份实例。
- FLOW_MIGRATECHECK： "022"，迁移参数校验。
- FLOW_MIGRATETASK："023"，数据迁移中。
- FLOW_CLEANDB："025"，清空某个数据库。
- FLOW_CLONEBACKUP："026"，克隆备份。
- FLOW_CHANGEVIP： "027"，改变vip地址。
- FLOW_EXPORSHR ："028"，扩缩容。
- FLOW_ADDNODES："029"，加（减）节点。
- FLOW_CHANGENET："031"，改变网络类型。
- FLOW_MODIFYINSTACEREADONLY："033"，只读策略变更。
- FLOW_MODIFYINSTANCEPARAMS："034"，修改实例参数。
- FLOW_MODIFYINSTANCEPASSWORDFREE："035"，设置免密。
- FLOW_SWITCHINSTANCEVIP："036"，实例VIP切换。
- FLOW_MODIFYINSTANCEACCOUNT："037"，实例账号变更。
- FLOW_MODIFYINSTANCEBANDWIDTH："038"，实例带宽变更。
- FLOW_ENABLEINSTANCE_REPLICATE："039"，开启副本只读。
- FLOW_DISABLEINSTANCE_REPLICATE："040"，关闭副本只读。
- FLOW_UpgradeArch："041"，实例架构升级，主从升集群。
- FLOW_DowngradeArch： "042"，实例架构降级，集群降主从。
- FLOW_UpgradeVersion： "043"，版本升级。
- FLOW_MODIFYCONNECTIONCONFIG："044"，带宽连接数调整，
- FLOW_CLEARNETWORK："045"，更换网络，
- FLOW_REMOVE_BACKUP_FILE："046"，删除备份。
- FLOW_UPGRADE_SUPPORT_MULTI_AZ："047"，升级实例支持多可用区。
- FLOW_SHUTDOWN_MASTER："048"，模拟故障。
- FLOW_CHANGE_REPLICA_TO_MASTER："049"，手动提主。
- FLOW_CODE_ADD_REPLICATION_INSTANCE："050"，新增复制组。
- FLOW_OPEN_WAN："052"，开通外网。
- FLOW_CLOSE_WAN："053"，关闭外网FLOW_UPDATE_WAN："054"，更新外网。
- FLOW_CODE_DELETE_REPLICATION_INSTANCE："055"，解绑复制组。
- FLOW_CODE_CHANGE_MASTER_INSTANCE："056"，复制组实例切主。
- FLOW_CODE_CHANGE_INSTANCE_ROLE： "057"，更改复制组实例角色。
- FLOW_MIGRATE_NODE："058"，迁移节点。
- FLOW_SWITCH_NODE："059"，切换节点。
- FLOW_UPGRADE_SMALL_VERSION："060"，升级 Redis版本。
- FLOW_UPGRADE_PROXY_VERSION："061"，升级 Proxy 版本。
- FLOW_MODIFY_INSTANCE_NETWORK： "062"，实例修改网络。
- FLOW_MIGRATE_PROXY_NODE："063"，迁移proxy节点。
- FLOW_MIGRATION_INSTANCE_ZONE："066"，实例可用区迁移中。
- FLOW_UPGRADE_INSTANCE_CACHE_AND_PROXY： "067"，实例版本升级中。
- FLOW_MODIFY_PROXY_NUM："069"，加（减）Proxy 节点。
- FLOW_MODIFYBACKUPMOD："070"，变更实例备份模式。
        :rtype: list of str
        """
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def BeginTime(self):
        r"""任务执行的起始时间，格式如：2021-12-30 00:00:00，支持查询近30天内数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""任务运行的终止时间。格式如：2021-12-30 20:59:35，支持查询近30天内数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskStatus(self):
        r"""该参数为内部使用，请忽略。
        :rtype: list of int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Result(self):
        r"""任务执行状态。
- 0：任务初始化。
- 1：执行中。
- 2：完成。
- 4：失败。
        :rtype: list of int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def OperatorUin(self):
        warnings.warn("parameter `OperatorUin` is deprecated", DeprecationWarning) 

        r"""该字段已废弃，使用OperateUin代替，请忽略。
        :rtype: list of int
        """
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        warnings.warn("parameter `OperatorUin` is deprecated", DeprecationWarning) 

        self._OperatorUin = OperatorUin

    @property
    def OperateUin(self):
        r"""操作者账号 ID，UIN。
        :rtype: list of str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProjectIds = params.get("ProjectIds")
        self._TaskTypes = params.get("TaskTypes")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TaskStatus = params.get("TaskStatus")
        self._Result = params.get("Result")
        self._OperatorUin = params.get("OperatorUin")
        self._OperateUin = params.get("OperateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskListResponse(AbstractModel):
    r"""DescribeTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数。
        :type TotalCount: int
        :param _Tasks: 任务详细信息。
        :type Tasks: list of TaskInfoDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""任务总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        r"""任务详细信息。
        :rtype: list of TaskInfoDetail
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfoDetail()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTendisSlowLogRequest(AbstractModel):
    r"""DescribeTendisSlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Tendis控制台](https://console.cloud.tencent.com/tendis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _BeginTime: 开始时间：2019-09-08 12:12:41，查询时间最大跨度30天。
        :type BeginTime: str
        :param _EndTime: 结束时间：2019-09-09 12:12:41，查询时间最大跨度30天。
        :type EndTime: str
        :param _MinQueryTime: 慢查询阈值，取值为大于0的正整数，单位：毫秒。
        :type MinQueryTime: int
        :param _Limit: 页面大小。默认为20，最小为1，最大为100。
        :type Limit: int
        :param _Offset: 分页偏移量。默认为0，取值为 Limit 整数倍，计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._MinQueryTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Tendis控制台](https://console.cloud.tencent.com/tendis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        r"""开始时间：2019-09-08 12:12:41，查询时间最大跨度30天。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""结束时间：2019-09-09 12:12:41，查询时间最大跨度30天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        r"""慢查询阈值，取值为大于0的正整数，单位：毫秒。
        :rtype: int
        """
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

    @property
    def Limit(self):
        r"""页面大小。默认为20，最小为1，最大为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量。默认为0，取值为 Limit 整数倍，计算公式：offset=limit*(页码-1)。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._MinQueryTime = params.get("MinQueryTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTendisSlowLogResponse(AbstractModel):
    r"""DescribeTendisSlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 慢查询总数
        :type TotalCount: int
        :param _TendisSlowLogDetail: 慢查询详情，注意：TotalCount大于1W，即慢日志超过1万条，不支持返回日志详情，返回数据为空。 建议缩小BeginTime和EndTime的时间间隔，多次查询。
        :type TendisSlowLogDetail: list of TendisSlowLogDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TendisSlowLogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""慢查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TendisSlowLogDetail(self):
        r"""慢查询详情，注意：TotalCount大于1W，即慢日志超过1万条，不支持返回日志详情，返回数据为空。 建议缩小BeginTime和EndTime的时间间隔，多次查询。
        :rtype: list of TendisSlowLogDetail
        """
        return self._TendisSlowLogDetail

    @TendisSlowLogDetail.setter
    def TendisSlowLogDetail(self, TendisSlowLogDetail):
        self._TendisSlowLogDetail = TendisSlowLogDetail

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
        if params.get("TendisSlowLogDetail") is not None:
            self._TendisSlowLogDetail = []
            for item in params.get("TendisSlowLogDetail"):
                obj = TendisSlowLogDetail()
                obj._deserialize(item)
                self._TendisSlowLogDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyPostpaidInstanceRequest(AbstractModel):
    r"""DestroyPostpaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制按量计费的实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制按量计费的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPostpaidInstanceResponse(AbstractModel):
    r"""DestroyPostpaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务Id
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


class DestroyPrepaidInstanceRequest(AbstractModel):
    r"""DestroyPrepaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPrepaidInstanceResponse(AbstractModel):
    r"""DestroyPrepaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单Id
        :type DealId: str
        :param _DealName: 订单号。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._DealName = None
        self._RequestId = None

    @property
    def DealId(self):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        r"""订单Id
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        self._DealId = DealId

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
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class DisableReplicaReadonlyRequest(AbstractModel):
    r"""DisableReplicaReadonly请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableReplicaReadonlyResponse(AbstractModel):
    r"""DisableReplicaReadonly返回参数结构体

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


class DisassociateSecurityGroupsRequest(AbstractModel):
    r"""DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _SecurityGroupId: 安全组 ID，请通过接口[DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447)的返回参数InstanceSecurityGroupsDetail 的子参数**SecurityGroupId**获取。
        :type SecurityGroupId: str
        :param _InstanceIds: 实例ID列表，一个或者多个实例 ID 组成的数组。请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        r"""数据库引擎名称，本接口取值：redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        r"""安全组 ID，请通过接口[DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447)的返回参数InstanceSecurityGroupsDetail 的子参数**SecurityGroupId**获取。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        r"""实例ID列表，一个或者多个实例 ID 组成的数组。请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    r"""DisassociateSecurityGroups返回参数结构体

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


class EnableReplicaReadonlyRequest(AbstractModel):
    r"""EnableReplicaReadonly请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _ReadonlyPolicy: 只读路由策略。
- master：表示只读路由至主节点。
- replication：表示只读路由至从节点。默认值为：replication。
        :type ReadonlyPolicy: list of str
        """
        self._InstanceId = None
        self._ReadonlyPolicy = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadonlyPolicy(self):
        r"""只读路由策略。
- master：表示只读路由至主节点。
- replication：表示只读路由至从节点。默认值为：replication。
        :rtype: list of str
        """
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableReplicaReadonlyResponse(AbstractModel):
    r"""EnableReplicaReadonly返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 错误：ERROR，正确OK（已废弃）
        :type Status: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Status(self):
        warnings.warn("parameter `Status` is deprecated", DeprecationWarning) 

        r"""错误：ERROR，正确OK（已废弃）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        warnings.warn("parameter `Status` is deprecated", DeprecationWarning) 

        self._Status = Status

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
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Groups(AbstractModel):
    r"""复制组信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户 APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。
        :type AppId: int
        :param _RegionId: 地域ID 。
- 1：广州 
- 4：上海 
- 5：中国香港 
- 7：上海金融 
- 8：北京 
- 9：新加坡
- 11：深圳金融
- 15：美西（硅谷）
- 16：成都 
- 17：德国 
- 18：韩国 
- 19：重庆 
- 22：美东（弗吉尼亚）
- 23：泰国 
- 25：日本
        :type RegionId: int
        :param _GroupId: 复制组 ID。格式如：crs-rpl-deind****。
        :type GroupId: str
        :param _GroupName: 复制组名称。
        :type GroupName: str
        :param _Status: 复制组状态。
- 37：绑定复制组中。
- 38：复制组重连中。
- 51：解绑复制组中。
- 52：复制组实例切主中。
- 53：角色变更中。
        :type Status: int
        :param _InstanceCount: 复制组数量。
        :type InstanceCount: int
        :param _Instances: 复制组中的实例信息。
        :type Instances: list of Instances
        :param _Remark: 备注信息。
        :type Remark: str
        """
        self._AppId = None
        self._RegionId = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None
        self._InstanceCount = None
        self._Instances = None
        self._Remark = None

    @property
    def AppId(self):
        r"""用户 APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RegionId(self):
        r"""地域ID 。
- 1：广州 
- 4：上海 
- 5：中国香港 
- 7：上海金融 
- 8：北京 
- 9：新加坡
- 11：深圳金融
- 15：美西（硅谷）
- 16：成都 
- 17：德国 
- 18：韩国 
- 19：重庆 
- 22：美东（弗吉尼亚）
- 23：泰国 
- 25：日本
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def GroupId(self):
        r"""复制组 ID。格式如：crs-rpl-deind****。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""复制组名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        r"""复制组状态。
- 37：绑定复制组中。
- 38：复制组重连中。
- 51：解绑复制组中。
- 52：复制组实例切主中。
- 53：角色变更中。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceCount(self):
        r"""复制组数量。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Instances(self):
        r"""复制组中的实例信息。
        :rtype: list of Instances
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def Remark(self):
        r"""备注信息。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._RegionId = params.get("RegionId")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        self._InstanceCount = params.get("InstanceCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instances()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HotKeyInfo(AbstractModel):
    r"""热Key详细信息

    """

    def __init__(self):
        r"""
        :param _Key: 热 Key 的名称。
        :type Key: str
        :param _Type: Key 类型。
        :type Type: str
        :param _Count: 某段时间内热 Key 的访问次数
        :type Count: int
        """
        self._Key = None
        self._Type = None
        self._Count = None

    @property
    def Key(self):
        r"""热 Key 的名称。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        r"""Key 类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        r"""某段时间内热 Key 的访问次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inbound(AbstractModel):
    r"""安全组入站规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT或者DROP。
        :type Action: str
        :param _AddressModule: 地址组id代表的地址集合。
        :type AddressModule: str
        :param _CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。
        :type CidrIp: str
        :param _Desc: 描述。
        :type Desc: str
        :param _IpProtocol: 网络协议，支持udp、tcp等。
        :type IpProtocol: str
        :param _PortRange: 端口。
        :type PortRange: str
        :param _ServiceModule: 服务组id代表的协议和端口集合。
        :type ServiceModule: str
        :param _Id: 安全组id代表的地址集合。
        :type Id: str
        """
        self._Action = None
        self._AddressModule = None
        self._CidrIp = None
        self._Desc = None
        self._IpProtocol = None
        self._PortRange = None
        self._ServiceModule = None
        self._Id = None

    @property
    def Action(self):
        r"""策略，ACCEPT或者DROP。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        r"""地址组id代表的地址集合。
        :rtype: str
        """
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        r"""来源Ip或Ip段，例如192.168.0.0/16。
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        r"""描述。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        r"""网络协议，支持udp、tcp等。
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        r"""端口。
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        r"""服务组id代表的协议和端口集合。
        :rtype: str
        """
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
        r"""安全组id代表的地址集合。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._AddressModule = params.get("AddressModule")
        self._CidrIp = params.get("CidrIp")
        self._Desc = params.get("Desc")
        self._IpProtocol = params.get("IpProtocol")
        self._PortRange = params.get("PortRange")
        self._ServiceModule = params.get("ServiceModule")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceRequest(AbstractModel):
    r"""InquiryPriceCreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeId: 实例类型。
- 2：Redis 2.8 内存版（标准架构）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
- 200:Memcached 1.6 内存版（集群架构）。
        :type TypeId: int
        :param _MemSize: 内存容量，单位为MB， 数值需为1024的整数倍，具体规格以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。
TypeId为标准架构时，MemSize是实例总内存容量；TypeId为集群架构时，MemSize是单分片内存容量。
        :type MemSize: int
        :param _GoodsNum: 实例数量，单次购买实例数量以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。
        :type GoodsNum: int
        :param _Period: 购买时长，在创建包年包月实例的时候需要填写，按量计费实例填1即可，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :type Period: int
        :param _BillingMode: 付费方式。
- 0：按量计费。
- 1：包年包月。
        :type BillingMode: int
        :param _ZoneId: 实例所属的可用区 ID，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
**说明**：请在 **ZoneId** 与 **ZoneName** 中至少指定一个参数。
        :type ZoneId: int
        :param _RedisShardNum: 实例分片数量。
- 标准架构需要配置分片数量为1。
- 集群架构分片数量支持设置为1、3、5、8、12、16、24、32、40、48、64、80、96、128。
        :type RedisShardNum: int
        :param _RedisReplicasNum: 实例副本数量。取值范围为：1、2、3、4、5。
        :type RedisReplicasNum: int
        :param _ReplicasReadonly: 是否支持副本只读。Redis2.8标准架构、CKV标准架构无需填写。
- true：无需支持副本只读。
- false：需支持。
        :type ReplicasReadonly: bool
        :param _ZoneName: 实例所属的可用区名称，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
**说明**：请在 **ZoneId** 与 **ZoneName** 中至少指定一个参数。
        :type ZoneName: str
        :param _ProductVersion: 部署方式。
- local：本地盘版，默认为 local。
- cloud：云盘版。
- cdc：独享集群版。
        :type ProductVersion: str
        """
        self._TypeId = None
        self._MemSize = None
        self._GoodsNum = None
        self._Period = None
        self._BillingMode = None
        self._ZoneId = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._ReplicasReadonly = None
        self._ZoneName = None
        self._ProductVersion = None

    @property
    def TypeId(self):
        r"""实例类型。
- 2：Redis 2.8 内存版（标准架构）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
- 200:Memcached 1.6 内存版（集群架构）。
        :rtype: int
        """
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def MemSize(self):
        r"""内存容量，单位为MB， 数值需为1024的整数倍，具体规格以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。
TypeId为标准架构时，MemSize是实例总内存容量；TypeId为集群架构时，MemSize是单分片内存容量。
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def GoodsNum(self):
        r"""实例数量，单次购买实例数量以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Period(self):
        r"""购买时长，在创建包年包月实例的时候需要填写，按量计费实例填1即可，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def BillingMode(self):
        r"""付费方式。
- 0：按量计费。
- 1：包年包月。
        :rtype: int
        """
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ZoneId(self):
        r"""实例所属的可用区 ID，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
**说明**：请在 **ZoneId** 与 **ZoneName** 中至少指定一个参数。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RedisShardNum(self):
        r"""实例分片数量。
- 标准架构需要配置分片数量为1。
- 集群架构分片数量支持设置为1、3、5、8、12、16、24、32、40、48、64、80、96、128。
        :rtype: int
        """
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        r"""实例副本数量。取值范围为：1、2、3、4、5。
        :rtype: int
        """
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def ReplicasReadonly(self):
        r"""是否支持副本只读。Redis2.8标准架构、CKV标准架构无需填写。
- true：无需支持副本只读。
- false：需支持。
        :rtype: bool
        """
        return self._ReplicasReadonly

    @ReplicasReadonly.setter
    def ReplicasReadonly(self, ReplicasReadonly):
        self._ReplicasReadonly = ReplicasReadonly

    @property
    def ZoneName(self):
        r"""实例所属的可用区名称，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
**说明**：请在 **ZoneId** 与 **ZoneName** 中至少指定一个参数。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ProductVersion(self):
        r"""部署方式。
- local：本地盘版，默认为 local。
- cloud：云盘版。
- cdc：独享集群版。
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        self._MemSize = params.get("MemSize")
        self._GoodsNum = params.get("GoodsNum")
        self._Period = params.get("Period")
        self._BillingMode = params.get("BillingMode")
        self._ZoneId = params.get("ZoneId")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._ReplicasReadonly = params.get("ReplicasReadonly")
        self._ZoneName = params.get("ZoneName")
        self._ProductVersion = params.get("ProductVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceResponse(AbstractModel):
    r"""InquiryPriceCreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 价格
        :type Price: float
        :param _HighPrecisionPrice: 高精度价格
        :type HighPrecisionPrice: float
        :param _Currency: 币种
        :type Currency: str
        :param _AmountUnit: 价格金额单位

- pent: 分
- microPent: 微分
        :type AmountUnit: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._HighPrecisionPrice = None
        self._Currency = None
        self._AmountUnit = None
        self._RequestId = None

    @property
    def Price(self):
        r"""价格
        :rtype: float
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def HighPrecisionPrice(self):
        r"""高精度价格
        :rtype: float
        """
        return self._HighPrecisionPrice

    @HighPrecisionPrice.setter
    def HighPrecisionPrice(self, HighPrecisionPrice):
        self._HighPrecisionPrice = HighPrecisionPrice

    @property
    def Currency(self):
        r"""币种
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def AmountUnit(self):
        r"""价格金额单位

- pent: 分
- microPent: 微分
        :rtype: str
        """
        return self._AmountUnit

    @AmountUnit.setter
    def AmountUnit(self, AmountUnit):
        self._AmountUnit = AmountUnit

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
        self._Price = params.get("Price")
        self._HighPrecisionPrice = params.get("HighPrecisionPrice")
        self._Currency = params.get("Currency")
        self._AmountUnit = params.get("AmountUnit")
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    r"""InquiryPriceRenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 包年包月实例的购买时长。
- 单位：月。
- 取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :type Period: int
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis)在实例列表复制包年包月实例 ID。
        :type InstanceId: str
        """
        self._Period = None
        self._InstanceId = None

    @property
    def Period(self):
        r"""包年包月实例的购买时长。
- 单位：月。
- 取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis)在实例列表复制包年包月实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstanceResponse(AbstractModel):
    r"""InquiryPriceRenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 价格
        :type Price: float
        :param _HighPrecisionPrice: 高精度价格
        :type HighPrecisionPrice: float
        :param _Currency: 币种
        :type Currency: str
        :param _AmountUnit: 价格金额单位

- pent: 分
- microPent: 微分
        :type AmountUnit: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._HighPrecisionPrice = None
        self._Currency = None
        self._AmountUnit = None
        self._RequestId = None

    @property
    def Price(self):
        r"""价格
        :rtype: float
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def HighPrecisionPrice(self):
        r"""高精度价格
        :rtype: float
        """
        return self._HighPrecisionPrice

    @HighPrecisionPrice.setter
    def HighPrecisionPrice(self, HighPrecisionPrice):
        self._HighPrecisionPrice = HighPrecisionPrice

    @property
    def Currency(self):
        r"""币种
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def AmountUnit(self):
        r"""价格金额单位

- pent: 分
- microPent: 微分
        :rtype: str
        """
        return self._AmountUnit

    @AmountUnit.setter
    def AmountUnit(self, AmountUnit):
        self._AmountUnit = AmountUnit

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
        self._Price = params.get("Price")
        self._HighPrecisionPrice = params.get("HighPrecisionPrice")
        self._Currency = params.get("Currency")
        self._AmountUnit = params.get("AmountUnit")
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeInstanceRequest(AbstractModel):
    r"""InquiryPriceUpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _MemSize: 分片大小，单位：MB。
        :type MemSize: int
        :param _RedisShardNum: 分片数量。
- 实例为标准架构，RedisShardNum 默认为1。
- Redis 2.8主从版、CKV主从版和 Redis 2.8单机版不需要填写。
        :type RedisShardNum: int
        :param _RedisReplicasNum: 副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写。
        :type RedisReplicasNum: int
        """
        self._InstanceId = None
        self._MemSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MemSize(self):
        r"""分片大小，单位：MB。
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def RedisShardNum(self):
        r"""分片数量。
- 实例为标准架构，RedisShardNum 默认为1。
- Redis 2.8主从版、CKV主从版和 Redis 2.8单机版不需要填写。
        :rtype: int
        """
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        r"""副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写。
        :rtype: int
        """
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MemSize = params.get("MemSize")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeInstanceResponse(AbstractModel):
    r"""InquiryPriceUpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 价格
        :type Price: float
        :param _HighPrecisionPrice: 高精度价格
        :type HighPrecisionPrice: float
        :param _Currency: 币种
        :type Currency: str
        :param _AmountUnit: 价格金额单位

- pent: 分
- microPent: 微分
        :type AmountUnit: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._HighPrecisionPrice = None
        self._Currency = None
        self._AmountUnit = None
        self._RequestId = None

    @property
    def Price(self):
        r"""价格
        :rtype: float
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def HighPrecisionPrice(self):
        r"""高精度价格
        :rtype: float
        """
        return self._HighPrecisionPrice

    @HighPrecisionPrice.setter
    def HighPrecisionPrice(self, HighPrecisionPrice):
        self._HighPrecisionPrice = HighPrecisionPrice

    @property
    def Currency(self):
        r"""币种
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def AmountUnit(self):
        r"""价格金额单位

- pent: 分
- microPent: 微分
        :rtype: str
        """
        return self._AmountUnit

    @AmountUnit.setter
    def AmountUnit(self, AmountUnit):
        self._AmountUnit = AmountUnit

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
        self._Price = params.get("Price")
        self._HighPrecisionPrice = params.get("HighPrecisionPrice")
        self._Currency = params.get("Currency")
        self._AmountUnit = params.get("AmountUnit")
        self._RequestId = params.get("RequestId")


class InstanceClusterNode(AbstractModel):
    r"""实例节点类型

    """

    def __init__(self):
        r"""
        :param _Name: 节点组名称。
        :type Name: str
        :param _RunId: 实例运行时节点 ID。
        :type RunId: str
        :param _Role: 集群角色。
- 0：master。
- 1：slave。
        :type Role: int
        :param _Status: 节点状态。
- 0：readwrite,。
- 1：read。
- 2：backup。
        :type Status: int
        :param _Connected: 服务状态。
0-down。
1-on
        :type Connected: int
        :param _CreateTime: 节点创建时间。
        :type CreateTime: str
        :param _DownTime: 节点下线时间。
        :type DownTime: str
        :param _Slots: 节点 Slot 分布区间。
        :type Slots: str
        :param _Keys: 节点 Key分布。
        :type Keys: int
        :param _Qps: 节点 QPS。分片节点每秒执行次数。单位：次/秒。
        :type Qps: int
        :param _QpsSlope: 节点 QPS 倾斜度。
        :type QpsSlope: float
        :param _Storage: 节点存储。
        :type Storage: int
        :param _StorageSlope: 节点存储倾斜度。
        :type StorageSlope: float
        """
        self._Name = None
        self._RunId = None
        self._Role = None
        self._Status = None
        self._Connected = None
        self._CreateTime = None
        self._DownTime = None
        self._Slots = None
        self._Keys = None
        self._Qps = None
        self._QpsSlope = None
        self._Storage = None
        self._StorageSlope = None

    @property
    def Name(self):
        r"""节点组名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RunId(self):
        r"""实例运行时节点 ID。
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def Role(self):
        r"""集群角色。
- 0：master。
- 1：slave。
        :rtype: int
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        r"""节点状态。
- 0：readwrite,。
- 1：read。
- 2：backup。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Connected(self):
        r"""服务状态。
0-down。
1-on
        :rtype: int
        """
        return self._Connected

    @Connected.setter
    def Connected(self, Connected):
        self._Connected = Connected

    @property
    def CreateTime(self):
        r"""节点创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DownTime(self):
        r"""节点下线时间。
        :rtype: str
        """
        return self._DownTime

    @DownTime.setter
    def DownTime(self, DownTime):
        self._DownTime = DownTime

    @property
    def Slots(self):
        r"""节点 Slot 分布区间。
        :rtype: str
        """
        return self._Slots

    @Slots.setter
    def Slots(self, Slots):
        self._Slots = Slots

    @property
    def Keys(self):
        r"""节点 Key分布。
        :rtype: int
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Qps(self):
        r"""节点 QPS。分片节点每秒执行次数。单位：次/秒。
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def QpsSlope(self):
        r"""节点 QPS 倾斜度。
        :rtype: float
        """
        return self._QpsSlope

    @QpsSlope.setter
    def QpsSlope(self, QpsSlope):
        self._QpsSlope = QpsSlope

    @property
    def Storage(self):
        r"""节点存储。
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageSlope(self):
        r"""节点存储倾斜度。
        :rtype: float
        """
        return self._StorageSlope

    @StorageSlope.setter
    def StorageSlope(self, StorageSlope):
        self._StorageSlope = StorageSlope


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RunId = params.get("RunId")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._Connected = params.get("Connected")
        self._CreateTime = params.get("CreateTime")
        self._DownTime = params.get("DownTime")
        self._Slots = params.get("Slots")
        self._Keys = params.get("Keys")
        self._Qps = params.get("Qps")
        self._QpsSlope = params.get("QpsSlope")
        self._Storage = params.get("Storage")
        self._StorageSlope = params.get("StorageSlope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceClusterShard(AbstractModel):
    r"""实例分片列表信息

    """

    def __init__(self):
        r"""
        :param _ShardName: 分片节点名称。
        :type ShardName: str
        :param _ShardId: 分片节点序号。
        :type ShardId: str
        :param _Role: 分片节点的角色。
- 0：主节点。
- 1：副本节点。
        :type Role: int
        :param _Keys: Key数量。
        :type Keys: int
        :param _Slots: Slot信息。
        :type Slots: str
        :param _Storage: 已使用容量。
        :type Storage: int
        :param _StorageSlope: 容量倾斜率。
        :type StorageSlope: float
        :param _Runid: 该字段因拼写不规范问题，建议使用RunId取代。含义：实例运行时节点 ID。
        :type Runid: str
        :param _RunId: 实例运行时节点 ID。
        :type RunId: str
        :param _Connected: 服务状态。
- 0：down。
- 1：on。
        :type Connected: int
        :param _ZoneId: 可用区信息。
        :type ZoneId: str
        :param _ReplicasNodeId: 节点组 ID。
        :type ReplicasNodeId: int
        """
        self._ShardName = None
        self._ShardId = None
        self._Role = None
        self._Keys = None
        self._Slots = None
        self._Storage = None
        self._StorageSlope = None
        self._Runid = None
        self._RunId = None
        self._Connected = None
        self._ZoneId = None
        self._ReplicasNodeId = None

    @property
    def ShardName(self):
        r"""分片节点名称。
        :rtype: str
        """
        return self._ShardName

    @ShardName.setter
    def ShardName(self, ShardName):
        self._ShardName = ShardName

    @property
    def ShardId(self):
        r"""分片节点序号。
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Role(self):
        r"""分片节点的角色。
- 0：主节点。
- 1：副本节点。
        :rtype: int
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Keys(self):
        r"""Key数量。
        :rtype: int
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Slots(self):
        r"""Slot信息。
        :rtype: str
        """
        return self._Slots

    @Slots.setter
    def Slots(self, Slots):
        self._Slots = Slots

    @property
    def Storage(self):
        r"""已使用容量。
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageSlope(self):
        r"""容量倾斜率。
        :rtype: float
        """
        return self._StorageSlope

    @StorageSlope.setter
    def StorageSlope(self, StorageSlope):
        self._StorageSlope = StorageSlope

    @property
    def Runid(self):
        r"""该字段因拼写不规范问题，建议使用RunId取代。含义：实例运行时节点 ID。
        :rtype: str
        """
        return self._Runid

    @Runid.setter
    def Runid(self, Runid):
        self._Runid = Runid

    @property
    def RunId(self):
        r"""实例运行时节点 ID。
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def Connected(self):
        r"""服务状态。
- 0：down。
- 1：on。
        :rtype: int
        """
        return self._Connected

    @Connected.setter
    def Connected(self, Connected):
        self._Connected = Connected

    @property
    def ZoneId(self):
        r"""可用区信息。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ReplicasNodeId(self):
        r"""节点组 ID。
        :rtype: int
        """
        return self._ReplicasNodeId

    @ReplicasNodeId.setter
    def ReplicasNodeId(self, ReplicasNodeId):
        self._ReplicasNodeId = ReplicasNodeId


    def _deserialize(self, params):
        self._ShardName = params.get("ShardName")
        self._ShardId = params.get("ShardId")
        self._Role = params.get("Role")
        self._Keys = params.get("Keys")
        self._Slots = params.get("Slots")
        self._Storage = params.get("Storage")
        self._StorageSlope = params.get("StorageSlope")
        self._Runid = params.get("Runid")
        self._RunId = params.get("RunId")
        self._Connected = params.get("Connected")
        self._ZoneId = params.get("ZoneId")
        self._ReplicasNodeId = params.get("ReplicasNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnumParam(AbstractModel):
    r"""实例枚举类型参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称。
        :type ParamName: str
        :param _ValueType: 参数类型，例如：Enum。
        :type ValueType: str
        :param _NeedRestart: 参数值修改后是否需要重启。
- true：需要。
- false：不需要。
        :type NeedRestart: str
        :param _DefaultValue: 参数默认值。
        :type DefaultValue: str
        :param _CurrentValue: 参数当前运行值。
        :type CurrentValue: str
        :param _Tips: 参数说明。
        :type Tips: str
        :param _EnumValue: 参数可取的值。
        :type EnumValue: list of str
        :param _Status: 参数修改状态。
- 1: 修改中。
- 2：修改完成。
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._EnumValue = None
        self._Status = None

    @property
    def ParamName(self):
        r"""参数名称。
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        r"""参数类型，例如：Enum。
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        r"""参数值修改后是否需要重启。
- true：需要。
- false：不需要。
        :rtype: str
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        r"""参数默认值。
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        r"""参数当前运行值。
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        r"""参数说明。
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def EnumValue(self):
        r"""参数可取的值。
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        r"""参数修改状态。
- 1: 修改中。
- 2：修改完成。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._EnumValue = params.get("EnumValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIntegerParam(AbstractModel):
    r"""实例整型参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
        :type ParamName: str
        :param _ValueType: 参数类型：integer
        :type ValueType: str
        :param _NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param _DefaultValue: 参数默认值
        :type DefaultValue: str
        :param _CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param _Tips: 参数说明
        :type Tips: str
        :param _Min: 参数最小值
        :type Min: str
        :param _Max: 参数最大值
        :type Max: str
        :param _Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        :param _Unit: 参数单位
        :type Unit: str
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._Min = None
        self._Max = None
        self._Status = None
        self._Unit = None

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
    def ValueType(self):
        r"""参数类型：integer
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        r"""修改后是否需要重启：true，false
        :rtype: str
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        r"""参数默认值
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        r"""当前运行参数值
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        r"""参数说明
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def Min(self):
        r"""参数最小值
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        r"""参数最大值
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Status(self):
        r"""参数状态, 1: 修改中， 2：修改完成
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Unit(self):
        r"""参数单位
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._Status = params.get("Status")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMultiParam(AbstractModel):
    r"""实例多选项类型参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称。
        :type ParamName: str
        :param _ValueType: 参数类型。例如：multi。
        :type ValueType: str
        :param _NeedRestart: 参数修改后是否需要重启。
- true：需要。
- false：不需要。
        :type NeedRestart: str
        :param _DefaultValue: 参数默认值。
        :type DefaultValue: str
        :param _CurrentValue: 当前运行参数值。
        :type CurrentValue: str
        :param _Tips: 参数说明。
        :type Tips: str
        :param _EnumValue: 参数枚举值。
        :type EnumValue: list of str
        :param _Status: 参数修改的状态。
- 1：修改中。
- 2：修改完成。
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._EnumValue = None
        self._Status = None

    @property
    def ParamName(self):
        r"""参数名称。
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        r"""参数类型。例如：multi。
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        r"""参数修改后是否需要重启。
- true：需要。
- false：不需要。
        :rtype: str
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        r"""参数默认值。
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        r"""当前运行参数值。
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        r"""参数说明。
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def EnumValue(self):
        r"""参数枚举值。
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        r"""参数修改的状态。
- 1：修改中。
- 2：修改完成。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._EnumValue = params.get("EnumValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    r"""实例节点

    """

    def __init__(self):
        r"""
        :param _Id: 实例 ID。
        :type Id: int
        :param _InstanceClusterNode: 节点详细信息。
        :type InstanceClusterNode: list of InstanceClusterNode
        """
        self._Id = None
        self._InstanceClusterNode = None

    @property
    def Id(self):
        r"""实例 ID。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceClusterNode(self):
        r"""节点详细信息。
        :rtype: list of InstanceClusterNode
        """
        return self._InstanceClusterNode

    @InstanceClusterNode.setter
    def InstanceClusterNode(self, InstanceClusterNode):
        self._InstanceClusterNode = InstanceClusterNode


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("InstanceClusterNode") is not None:
            self._InstanceClusterNode = []
            for item in params.get("InstanceClusterNode"):
                obj = InstanceClusterNode()
                obj._deserialize(item)
                self._InstanceClusterNode.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParam(AbstractModel):
    r"""实例参数

    """

    def __init__(self):
        r"""
        :param _Key: 设置参数的名称。例如timeout。当前支持自定义的参数，请参见<a href="https://cloud.tencent.com/document/product/239/49925">参数配置</a>。
        :type Key: str
        :param _Value: 设置参数名称对应的运行值。例如timeout对应运行值可设置为120， 单位为秒（s）。指当客户端连接闲置时间达到120 s时，将关闭连接。更多参数取值信息，请参见<a href="https://cloud.tencent.com/document/product/239/49925">参数配置</a>。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""设置参数的名称。例如timeout。当前支持自定义的参数，请参见<a href="https://cloud.tencent.com/document/product/239/49925">参数配置</a>。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""设置参数名称对应的运行值。例如timeout对应运行值可设置为120， 单位为秒（s）。指当客户端连接闲置时间达到120 s时，将关闭连接。更多参数取值信息，请参见<a href="https://cloud.tencent.com/document/product/239/49925">参数配置</a>。
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
        


class InstanceParamHistory(AbstractModel):
    r"""实例参数修改历史

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称。
        :type ParamName: str
        :param _PreValue: 参数修改之前的值。
        :type PreValue: str
        :param _NewValue: 参数修改之后的值。
        :type NewValue: str
        :param _Status: 参数配置状态。
- 1：参数配置修改中。
- 2：参数配置修改成功。
- 3：参数配置修改失败。
        :type Status: int
        :param _ModifyTime: 修改时间。
        :type ModifyTime: str
        """
        self._ParamName = None
        self._PreValue = None
        self._NewValue = None
        self._Status = None
        self._ModifyTime = None

    @property
    def ParamName(self):
        r"""参数名称。
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def PreValue(self):
        r"""参数修改之前的值。
        :rtype: str
        """
        return self._PreValue

    @PreValue.setter
    def PreValue(self, PreValue):
        self._PreValue = PreValue

    @property
    def NewValue(self):
        r"""参数修改之后的值。
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def Status(self):
        r"""参数配置状态。
- 1：参数配置修改中。
- 2：参数配置修改成功。
- 3：参数配置修改失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        r"""修改时间。
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._PreValue = params.get("PreValue")
        self._NewValue = params.get("NewValue")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceProxySlowlogDetail(AbstractModel):
    r"""代理慢查询详情

    """

    def __init__(self):
        r"""
        :param _Duration: 慢查询耗时时长。单位：毫秒。
        :type Duration: int
        :param _Client: 客户端地址。
        :type Client: str
        :param _Command: 慢查询的命令。
        :type Command: str
        :param _CommandLine: 慢查询详细命令行信息。
        :type CommandLine: str
        :param _ExecuteTime: 执行时间。
        :type ExecuteTime: str
        :param _RecvClientEnd: 收客户端请求时长(ms)
        :type RecvClientEnd: int
        :param _SendClientEnd: 发送客户端请求时长(ms)
        :type SendClientEnd: int
        """
        self._Duration = None
        self._Client = None
        self._Command = None
        self._CommandLine = None
        self._ExecuteTime = None
        self._RecvClientEnd = None
        self._SendClientEnd = None

    @property
    def Duration(self):
        r"""慢查询耗时时长。单位：毫秒。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Client(self):
        r"""客户端地址。
        :rtype: str
        """
        return self._Client

    @Client.setter
    def Client(self, Client):
        self._Client = Client

    @property
    def Command(self):
        r"""慢查询的命令。
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        r"""慢查询详细命令行信息。
        :rtype: str
        """
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def ExecuteTime(self):
        r"""执行时间。
        :rtype: str
        """
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime

    @property
    def RecvClientEnd(self):
        r"""收客户端请求时长(ms)
        :rtype: int
        """
        return self._RecvClientEnd

    @RecvClientEnd.setter
    def RecvClientEnd(self, RecvClientEnd):
        self._RecvClientEnd = RecvClientEnd

    @property
    def SendClientEnd(self):
        r"""发送客户端请求时长(ms)
        :rtype: int
        """
        return self._SendClientEnd

    @SendClientEnd.setter
    def SendClientEnd(self, SendClientEnd):
        self._SendClientEnd = SendClientEnd


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._Client = params.get("Client")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._ExecuteTime = params.get("ExecuteTime")
        self._RecvClientEnd = params.get("RecvClientEnd")
        self._SendClientEnd = params.get("SendClientEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSecurityGroupDetail(AbstractModel):
    r"""实例安全组信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _SecurityGroupDetails: 安全组信息，包括：安全组 ID、安全组名称、安全组出入站规则。
        :type SecurityGroupDetails: list of SecurityGroupDetail
        """
        self._InstanceId = None
        self._SecurityGroupDetails = None

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupDetails(self):
        r"""安全组信息，包括：安全组 ID、安全组名称、安全组出入站规则。
        :rtype: list of SecurityGroupDetail
        """
        return self._SecurityGroupDetails

    @SecurityGroupDetails.setter
    def SecurityGroupDetails(self, SecurityGroupDetails):
        self._SecurityGroupDetails = SecurityGroupDetails


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("SecurityGroupDetails") is not None:
            self._SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self._SecurityGroupDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSet(AbstractModel):
    r"""实例详细信息列表。

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Appid: 用户AppId。AppId是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 AppId。

        :type Appid: int
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _RegionId: 地域 ID。<ul><li>1：广州。</li><li>4：上海。</li><li>5：中国香港。</li><li>7：上海金融。</li> <li>8：北京。</li> <li>9：新加坡。</li> <li>11：深圳金融。</li> <li>15：美西（硅谷）。</li><li>16：成都。</li><li>17：法兰克福。</li><li>18：首尔。</li><li>19：重庆。</li><li>22：美东（弗吉尼亚）。</li><li>23：曼谷。</li><li>25：东京。</li></ul>
        :type RegionId: int
        :param _ZoneId: 区域 ID。
        :type ZoneId: int
        :param _VpcId: vpc网络 ID，例如75101。
        :type VpcId: int
        :param _SubnetId: vpc网络下子网ID，如：46315。
        :type SubnetId: int
        :param _Status: 实例当前状态。<ul><li>0：待初始化。</li><li>1：实例在流程中。</li><li>2：实例运行中。</li><li>-2：实例已隔离。</li><li>-3：实例待删除。</li></ul>
        :type Status: int
        :param _WanIp: 实例 VIP。
        :type WanIp: str
        :param _Port: 实例端口号。
        :type Port: int
        :param _Createtime: 实例创建时间。格式如：2020-01-15 10:20:00。
        :type Createtime: str
        :param _Size: 实例内存容量大小。单位：MB，1MB=1024KB。
        :type Size: float
        :param _SizeUsed: 该字段已废弃。请使用腾讯云可观测平台API 接口 [GetMonitorData](https://cloud.tencent.com/document/product/248/31014) 获取实例已使用的内存容量。
        :type SizeUsed: float
        :param _Type: 实例类型。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 5：Redis 2.8 内存版（单机）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
- 200:Memcached 1.6 内存版（集群架构）。
        :type Type: int
        :param _AutoRenewFlag: 实例是否设置自动续费标识。<ul><li>1：设置自动续费。</li><li>0：未设置自动续费。</li></ul>
        :type AutoRenewFlag: int
        :param _DeadlineTime: 包年包月计费实例到期的时间。
        :type DeadlineTime: str
        :param _Engine: 引擎：社区版Redis、腾讯云CKV。
        :type Engine: str
        :param _ProductType: 产品类型。<ul><li>standalone：标准版。</li><li>cluster ：集群版。</li></ul>
        :type ProductType: str
        :param _UniqVpcId: vpc网络id，例如vpc-fk33jsf43kgv。
        :type UniqVpcId: str
        :param _UniqSubnetId: vpc网络下子网id，例如：subnet-fd3j6l35mm0。
        :type UniqSubnetId: str
        :param _BillingMode: 计费模式。<ul><li>0：按量计费。</li><li>1：包年包月。</li></ul>
        :type BillingMode: int
        :param _InstanceTitle: 实例运行状态描述：如”实例运行中“。
        :type InstanceTitle: str
        :param _OfflineTime: 已隔离实例默认下线时间。按量计费实例隔离后默认两小时后下线，包年包月默认7天后下线。格式如：2020-02-15 10:20:00。
        :type OfflineTime: str
        :param _SubStatus: 流程中的实例返回的子状态。
- 0：磁盘读写状态。
- 1：磁盘超限只读状态。
        :type SubStatus: int
        :param _Tags: 反亲和性标签。
        :type Tags: list of str
        :param _InstanceNode: 实例节点信息。
        :type InstanceNode: list of InstanceNode
        :param _RedisShardSize: 分片大小。
        :type RedisShardSize: int
        :param _RedisShardNum: 分片数量。
        :type RedisShardNum: int
        :param _RedisReplicasNum: 副本数量。
        :type RedisReplicasNum: int
        :param _PriceId: 计费 ID。
        :type PriceId: int
        :param _CloseTime: 实例隔离开始的时间。
        :type CloseTime: str
        :param _SlaveReadWeight: 从节点读取权重。
- 0：表示关闭副本只读。
- 100：表示开启副本只读。
        :type SlaveReadWeight: int
        :param _InstanceTags: 实例关联的标签信息。
        :type InstanceTags: list of InstanceTagInfo
        :param _ProjectName: 项目名称。
        :type ProjectName: str
        :param _NoAuth: 是否为免密实例。<ul><li>true：免密实例。</li><li>false：非免密实例。</li></ul>
        :type NoAuth: bool
        :param _ClientLimit: 客户端连接数。
        :type ClientLimit: int
        :param _DtsStatus: DTS状态（内部参数，用户可忽略）。
        :type DtsStatus: int
        :param _NetLimit: 分片带宽上限，单位MB。
        :type NetLimit: int
        :param _PasswordFree: 免密实例标识（内部参数，用户可忽略）。
        :type PasswordFree: int
        :param _Vip6: 该参数存在命名不规范问题，建议用参数IPv6取代。内部参数，用户可忽略。
        :type Vip6: str
        :param _IPv6: 内部参数，用户可忽略。
        :type IPv6: str
        :param _ReadOnly: 实例只读标识（内部参数，用户可忽略）。
        :type ReadOnly: int
        :param _RemainBandwidthDuration: 内部参数，用户可忽略。
        :type RemainBandwidthDuration: str
        :param _DiskSize: Redis实例请忽略该参数。
        :type DiskSize: int
        :param _MonitorVersion: 监控版本。<ul><li>1m：1分钟粒度监控。目前该监控粒度已下线，具体信息，请参见[云数据库 Redis 1分钟粒度下线公告](https://cloud.tencent.com/document/product/239/80653)。</li><li>5s：5秒粒度监控。</li></ul>
        :type MonitorVersion: str
        :param _ClientLimitMin: 客户端最大连接数可设置的最小值。
        :type ClientLimitMin: int
        :param _ClientLimitMax: 客户端最大连接数可设置的最大值。
        :type ClientLimitMax: int
        :param _NodeSet: 实例的节点详细信息。
只有多可用区实例会返回。
        :type NodeSet: list of RedisNodeInfo
        :param _Region: 实例所在的地域信息，比如ap-guangzhou。
        :type Region: str
        :param _WanAddress: 外网地址。
        :type WanAddress: str
        :param _PolarisServer: 北极星服务地址，内部使用。
        :type PolarisServer: str
        :param _RedisClusterId: CDC Redis集群ID。
        :type RedisClusterId: str
        :param _DedicatedClusterId: CDC 集群ID。
        :type DedicatedClusterId: str
        :param _ProductVersion: 产品版本。<ul><li>local：本地盘。</li><li>cloud：云盘版。</li><li>cdc：CDC 集群版本。</li></ul>
        :type ProductVersion: str
        :param _CurrentProxyVersion: 实例当前Proxy版本。
        :type CurrentProxyVersion: str
        :param _CurrentRedisVersion: 实例当前Cache小版本。如果实例加入全球复制组，显示全球复制的内核版本。
        :type CurrentRedisVersion: str
        :param _UpgradeProxyVersion: 实例可升级Proxy版本。
        :type UpgradeProxyVersion: str
        :param _UpgradeRedisVersion: 实例可升级Cache小版本。
        :type UpgradeRedisVersion: str
        :param _BackupMode: 备份模式：- SecondLevelBackup   秒级备份- NormalLevelBackup    普通备份
        :type BackupMode: str
        :param _DeleteProtectionSwitch: 删除保护开关，0关闭，1开启
        :type DeleteProtectionSwitch: int
        """
        self._InstanceName = None
        self._InstanceId = None
        self._Appid = None
        self._ProjectId = None
        self._RegionId = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._WanIp = None
        self._Port = None
        self._Createtime = None
        self._Size = None
        self._SizeUsed = None
        self._Type = None
        self._AutoRenewFlag = None
        self._DeadlineTime = None
        self._Engine = None
        self._ProductType = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._BillingMode = None
        self._InstanceTitle = None
        self._OfflineTime = None
        self._SubStatus = None
        self._Tags = None
        self._InstanceNode = None
        self._RedisShardSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._PriceId = None
        self._CloseTime = None
        self._SlaveReadWeight = None
        self._InstanceTags = None
        self._ProjectName = None
        self._NoAuth = None
        self._ClientLimit = None
        self._DtsStatus = None
        self._NetLimit = None
        self._PasswordFree = None
        self._Vip6 = None
        self._IPv6 = None
        self._ReadOnly = None
        self._RemainBandwidthDuration = None
        self._DiskSize = None
        self._MonitorVersion = None
        self._ClientLimitMin = None
        self._ClientLimitMax = None
        self._NodeSet = None
        self._Region = None
        self._WanAddress = None
        self._PolarisServer = None
        self._RedisClusterId = None
        self._DedicatedClusterId = None
        self._ProductVersion = None
        self._CurrentProxyVersion = None
        self._CurrentRedisVersion = None
        self._UpgradeProxyVersion = None
        self._UpgradeRedisVersion = None
        self._BackupMode = None
        self._DeleteProtectionSwitch = None

    @property
    def InstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Appid(self):
        r"""用户AppId。AppId是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 AppId。

        :rtype: int
        """
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def ProjectId(self):
        r"""项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        r"""地域 ID。<ul><li>1：广州。</li><li>4：上海。</li><li>5：中国香港。</li><li>7：上海金融。</li> <li>8：北京。</li> <li>9：新加坡。</li> <li>11：深圳金融。</li> <li>15：美西（硅谷）。</li><li>16：成都。</li><li>17：法兰克福。</li><li>18：首尔。</li><li>19：重庆。</li><li>22：美东（弗吉尼亚）。</li><li>23：曼谷。</li><li>25：东京。</li></ul>
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""区域 ID。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        r"""vpc网络 ID，例如75101。
        :rtype: int
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""vpc网络下子网ID，如：46315。
        :rtype: int
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        r"""实例当前状态。<ul><li>0：待初始化。</li><li>1：实例在流程中。</li><li>2：实例运行中。</li><li>-2：实例已隔离。</li><li>-3：实例待删除。</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WanIp(self):
        r"""实例 VIP。
        :rtype: str
        """
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def Port(self):
        r"""实例端口号。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Createtime(self):
        r"""实例创建时间。格式如：2020-01-15 10:20:00。
        :rtype: str
        """
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def Size(self):
        r"""实例内存容量大小。单位：MB，1MB=1024KB。
        :rtype: float
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def SizeUsed(self):
        warnings.warn("parameter `SizeUsed` is deprecated", DeprecationWarning) 

        r"""该字段已废弃。请使用腾讯云可观测平台API 接口 [GetMonitorData](https://cloud.tencent.com/document/product/248/31014) 获取实例已使用的内存容量。
        :rtype: float
        """
        return self._SizeUsed

    @SizeUsed.setter
    def SizeUsed(self, SizeUsed):
        warnings.warn("parameter `SizeUsed` is deprecated", DeprecationWarning) 

        self._SizeUsed = SizeUsed

    @property
    def Type(self):
        r"""实例类型。
- 2：Redis 2.8 内存版（标准架构）。
- 3：CKV 3.2 内存版（标准架构）。
- 4：CKV 3.2 内存版（集群架构）。
- 5：Redis 2.8 内存版（单机）。
- 6：Redis 4.0 内存版（标准架构）。
- 7：Redis 4.0 内存版（集群架构）。
- 8：Redis 5.0 内存版（标准架构）。
- 9：Redis 5.0 内存版（集群架构）。
- 15：Redis 6.2 内存版（标准架构）。
- 16：Redis 6.2 内存版（集群架构）。
- 17：Redis 7.0 内存版（标准架构）。
- 18：Redis 7.0 内存版（集群架构）。
- 200:Memcached 1.6 内存版（集群架构）。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AutoRenewFlag(self):
        r"""实例是否设置自动续费标识。<ul><li>1：设置自动续费。</li><li>0：未设置自动续费。</li></ul>
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DeadlineTime(self):
        r"""包年包月计费实例到期的时间。
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Engine(self):
        r"""引擎：社区版Redis、腾讯云CKV。
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def ProductType(self):
        r"""产品类型。<ul><li>standalone：标准版。</li><li>cluster ：集群版。</li></ul>
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def UniqVpcId(self):
        r"""vpc网络id，例如vpc-fk33jsf43kgv。
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        r"""vpc网络下子网id，例如：subnet-fd3j6l35mm0。
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def BillingMode(self):
        r"""计费模式。<ul><li>0：按量计费。</li><li>1：包年包月。</li></ul>
        :rtype: int
        """
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def InstanceTitle(self):
        r"""实例运行状态描述：如”实例运行中“。
        :rtype: str
        """
        return self._InstanceTitle

    @InstanceTitle.setter
    def InstanceTitle(self, InstanceTitle):
        self._InstanceTitle = InstanceTitle

    @property
    def OfflineTime(self):
        r"""已隔离实例默认下线时间。按量计费实例隔离后默认两小时后下线，包年包月默认7天后下线。格式如：2020-02-15 10:20:00。
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def SubStatus(self):
        r"""流程中的实例返回的子状态。
- 0：磁盘读写状态。
- 1：磁盘超限只读状态。
        :rtype: int
        """
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus

    @property
    def Tags(self):
        r"""反亲和性标签。
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceNode(self):
        r"""实例节点信息。
        :rtype: list of InstanceNode
        """
        return self._InstanceNode

    @InstanceNode.setter
    def InstanceNode(self, InstanceNode):
        self._InstanceNode = InstanceNode

    @property
    def RedisShardSize(self):
        r"""分片大小。
        :rtype: int
        """
        return self._RedisShardSize

    @RedisShardSize.setter
    def RedisShardSize(self, RedisShardSize):
        self._RedisShardSize = RedisShardSize

    @property
    def RedisShardNum(self):
        r"""分片数量。
        :rtype: int
        """
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        r"""副本数量。
        :rtype: int
        """
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def PriceId(self):
        r"""计费 ID。
        :rtype: int
        """
        return self._PriceId

    @PriceId.setter
    def PriceId(self, PriceId):
        self._PriceId = PriceId

    @property
    def CloseTime(self):
        r"""实例隔离开始的时间。
        :rtype: str
        """
        return self._CloseTime

    @CloseTime.setter
    def CloseTime(self, CloseTime):
        self._CloseTime = CloseTime

    @property
    def SlaveReadWeight(self):
        r"""从节点读取权重。
- 0：表示关闭副本只读。
- 100：表示开启副本只读。
        :rtype: int
        """
        return self._SlaveReadWeight

    @SlaveReadWeight.setter
    def SlaveReadWeight(self, SlaveReadWeight):
        self._SlaveReadWeight = SlaveReadWeight

    @property
    def InstanceTags(self):
        r"""实例关联的标签信息。
        :rtype: list of InstanceTagInfo
        """
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def ProjectName(self):
        r"""项目名称。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def NoAuth(self):
        r"""是否为免密实例。<ul><li>true：免密实例。</li><li>false：非免密实例。</li></ul>
        :rtype: bool
        """
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def ClientLimit(self):
        r"""客户端连接数。
        :rtype: int
        """
        return self._ClientLimit

    @ClientLimit.setter
    def ClientLimit(self, ClientLimit):
        self._ClientLimit = ClientLimit

    @property
    def DtsStatus(self):
        r"""DTS状态（内部参数，用户可忽略）。
        :rtype: int
        """
        return self._DtsStatus

    @DtsStatus.setter
    def DtsStatus(self, DtsStatus):
        self._DtsStatus = DtsStatus

    @property
    def NetLimit(self):
        r"""分片带宽上限，单位MB。
        :rtype: int
        """
        return self._NetLimit

    @NetLimit.setter
    def NetLimit(self, NetLimit):
        self._NetLimit = NetLimit

    @property
    def PasswordFree(self):
        r"""免密实例标识（内部参数，用户可忽略）。
        :rtype: int
        """
        return self._PasswordFree

    @PasswordFree.setter
    def PasswordFree(self, PasswordFree):
        self._PasswordFree = PasswordFree

    @property
    def Vip6(self):
        r"""该参数存在命名不规范问题，建议用参数IPv6取代。内部参数，用户可忽略。
        :rtype: str
        """
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def IPv6(self):
        r"""内部参数，用户可忽略。
        :rtype: str
        """
        return self._IPv6

    @IPv6.setter
    def IPv6(self, IPv6):
        self._IPv6 = IPv6

    @property
    def ReadOnly(self):
        r"""实例只读标识（内部参数，用户可忽略）。
        :rtype: int
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def RemainBandwidthDuration(self):
        r"""内部参数，用户可忽略。
        :rtype: str
        """
        return self._RemainBandwidthDuration

    @RemainBandwidthDuration.setter
    def RemainBandwidthDuration(self, RemainBandwidthDuration):
        self._RemainBandwidthDuration = RemainBandwidthDuration

    @property
    def DiskSize(self):
        r"""Redis实例请忽略该参数。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MonitorVersion(self):
        r"""监控版本。<ul><li>1m：1分钟粒度监控。目前该监控粒度已下线，具体信息，请参见[云数据库 Redis 1分钟粒度下线公告](https://cloud.tencent.com/document/product/239/80653)。</li><li>5s：5秒粒度监控。</li></ul>
        :rtype: str
        """
        return self._MonitorVersion

    @MonitorVersion.setter
    def MonitorVersion(self, MonitorVersion):
        self._MonitorVersion = MonitorVersion

    @property
    def ClientLimitMin(self):
        r"""客户端最大连接数可设置的最小值。
        :rtype: int
        """
        return self._ClientLimitMin

    @ClientLimitMin.setter
    def ClientLimitMin(self, ClientLimitMin):
        self._ClientLimitMin = ClientLimitMin

    @property
    def ClientLimitMax(self):
        r"""客户端最大连接数可设置的最大值。
        :rtype: int
        """
        return self._ClientLimitMax

    @ClientLimitMax.setter
    def ClientLimitMax(self, ClientLimitMax):
        self._ClientLimitMax = ClientLimitMax

    @property
    def NodeSet(self):
        r"""实例的节点详细信息。
只有多可用区实例会返回。
        :rtype: list of RedisNodeInfo
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def Region(self):
        r"""实例所在的地域信息，比如ap-guangzhou。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def WanAddress(self):
        r"""外网地址。
        :rtype: str
        """
        return self._WanAddress

    @WanAddress.setter
    def WanAddress(self, WanAddress):
        self._WanAddress = WanAddress

    @property
    def PolarisServer(self):
        r"""北极星服务地址，内部使用。
        :rtype: str
        """
        return self._PolarisServer

    @PolarisServer.setter
    def PolarisServer(self, PolarisServer):
        self._PolarisServer = PolarisServer

    @property
    def RedisClusterId(self):
        r"""CDC Redis集群ID。
        :rtype: str
        """
        return self._RedisClusterId

    @RedisClusterId.setter
    def RedisClusterId(self, RedisClusterId):
        self._RedisClusterId = RedisClusterId

    @property
    def DedicatedClusterId(self):
        r"""CDC 集群ID。
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def ProductVersion(self):
        r"""产品版本。<ul><li>local：本地盘。</li><li>cloud：云盘版。</li><li>cdc：CDC 集群版本。</li></ul>
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def CurrentProxyVersion(self):
        r"""实例当前Proxy版本。
        :rtype: str
        """
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def CurrentRedisVersion(self):
        r"""实例当前Cache小版本。如果实例加入全球复制组，显示全球复制的内核版本。
        :rtype: str
        """
        return self._CurrentRedisVersion

    @CurrentRedisVersion.setter
    def CurrentRedisVersion(self, CurrentRedisVersion):
        self._CurrentRedisVersion = CurrentRedisVersion

    @property
    def UpgradeProxyVersion(self):
        r"""实例可升级Proxy版本。
        :rtype: str
        """
        return self._UpgradeProxyVersion

    @UpgradeProxyVersion.setter
    def UpgradeProxyVersion(self, UpgradeProxyVersion):
        self._UpgradeProxyVersion = UpgradeProxyVersion

    @property
    def UpgradeRedisVersion(self):
        r"""实例可升级Cache小版本。
        :rtype: str
        """
        return self._UpgradeRedisVersion

    @UpgradeRedisVersion.setter
    def UpgradeRedisVersion(self, UpgradeRedisVersion):
        self._UpgradeRedisVersion = UpgradeRedisVersion

    @property
    def BackupMode(self):
        r"""备份模式：- SecondLevelBackup   秒级备份- NormalLevelBackup    普通备份
        :rtype: str
        """
        return self._BackupMode

    @BackupMode.setter
    def BackupMode(self, BackupMode):
        self._BackupMode = BackupMode

    @property
    def DeleteProtectionSwitch(self):
        r"""删除保护开关，0关闭，1开启
        :rtype: int
        """
        return self._DeleteProtectionSwitch

    @DeleteProtectionSwitch.setter
    def DeleteProtectionSwitch(self, DeleteProtectionSwitch):
        self._DeleteProtectionSwitch = DeleteProtectionSwitch


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._Appid = params.get("Appid")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._WanIp = params.get("WanIp")
        self._Port = params.get("Port")
        self._Createtime = params.get("Createtime")
        self._Size = params.get("Size")
        self._SizeUsed = params.get("SizeUsed")
        self._Type = params.get("Type")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._DeadlineTime = params.get("DeadlineTime")
        self._Engine = params.get("Engine")
        self._ProductType = params.get("ProductType")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._BillingMode = params.get("BillingMode")
        self._InstanceTitle = params.get("InstanceTitle")
        self._OfflineTime = params.get("OfflineTime")
        self._SubStatus = params.get("SubStatus")
        self._Tags = params.get("Tags")
        if params.get("InstanceNode") is not None:
            self._InstanceNode = []
            for item in params.get("InstanceNode"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._InstanceNode.append(obj)
        self._RedisShardSize = params.get("RedisShardSize")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._PriceId = params.get("PriceId")
        self._CloseTime = params.get("CloseTime")
        self._SlaveReadWeight = params.get("SlaveReadWeight")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        self._ProjectName = params.get("ProjectName")
        self._NoAuth = params.get("NoAuth")
        self._ClientLimit = params.get("ClientLimit")
        self._DtsStatus = params.get("DtsStatus")
        self._NetLimit = params.get("NetLimit")
        self._PasswordFree = params.get("PasswordFree")
        self._Vip6 = params.get("Vip6")
        self._IPv6 = params.get("IPv6")
        self._ReadOnly = params.get("ReadOnly")
        self._RemainBandwidthDuration = params.get("RemainBandwidthDuration")
        self._DiskSize = params.get("DiskSize")
        self._MonitorVersion = params.get("MonitorVersion")
        self._ClientLimitMin = params.get("ClientLimitMin")
        self._ClientLimitMax = params.get("ClientLimitMax")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._Region = params.get("Region")
        self._WanAddress = params.get("WanAddress")
        self._PolarisServer = params.get("PolarisServer")
        self._RedisClusterId = params.get("RedisClusterId")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._ProductVersion = params.get("ProductVersion")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._CurrentRedisVersion = params.get("CurrentRedisVersion")
        self._UpgradeProxyVersion = params.get("UpgradeProxyVersion")
        self._UpgradeRedisVersion = params.get("UpgradeRedisVersion")
        self._BackupMode = params.get("BackupMode")
        self._DeleteProtectionSwitch = params.get("DeleteProtectionSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSlowlogDetail(AbstractModel):
    r"""慢查询详情

    """

    def __init__(self):
        r"""
        :param _Duration: 慢查询耗时
        :type Duration: int
        :param _Client: 客户端地址
        :type Client: str
        :param _Command: 命令
        :type Command: str
        :param _CommandLine: 详细命令行信息
        :type CommandLine: str
        :param _ExecuteTime: 执行时间
        :type ExecuteTime: str
        :param _Node: 节点ID
        :type Node: str
        """
        self._Duration = None
        self._Client = None
        self._Command = None
        self._CommandLine = None
        self._ExecuteTime = None
        self._Node = None

    @property
    def Duration(self):
        r"""慢查询耗时
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Client(self):
        r"""客户端地址
        :rtype: str
        """
        return self._Client

    @Client.setter
    def Client(self, Client):
        self._Client = Client

    @property
    def Command(self):
        r"""命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        r"""详细命令行信息
        :rtype: str
        """
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def ExecuteTime(self):
        r"""执行时间
        :rtype: str
        """
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime

    @property
    def Node(self):
        r"""节点ID
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._Client = params.get("Client")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._ExecuteTime = params.get("ExecuteTime")
        self._Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTagInfo(AbstractModel):
    r"""实例标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键。
        :type TagKey: str
        :param _TagValue: 标签值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值。
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
        


class InstanceTextParam(AbstractModel):
    r"""实例字符型参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称。
        :type ParamName: str
        :param _ValueType: 参数类型。例如：text。
        :type ValueType: str
        :param _NeedRestart: 参数修改后是否需要重启。
- true：需要。
- false：不需要。
        :type NeedRestart: str
        :param _DefaultValue: 参数默认值。
        :type DefaultValue: str
        :param _CurrentValue: 参数当前运行值。
        :type CurrentValue: str
        :param _Tips: 参数说明。
        :type Tips: str
        :param _TextValue: 参数可取值。
        :type TextValue: list of str
        :param _Status: 参数修改状态。
- 1: 修改中。
- 2：修改完成。
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._TextValue = None
        self._Status = None

    @property
    def ParamName(self):
        r"""参数名称。
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        r"""参数类型。例如：text。
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        r"""参数修改后是否需要重启。
- true：需要。
- false：不需要。
        :rtype: str
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        r"""参数默认值。
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        r"""参数当前运行值。
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        r"""参数说明。
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def TextValue(self):
        r"""参数可取值。
        :rtype: list of str
        """
        return self._TextValue

    @TextValue.setter
    def TextValue(self, TextValue):
        self._TextValue = TextValue

    @property
    def Status(self):
        r"""参数修改状态。
- 1: 修改中。
- 2：修改完成。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._TextValue = params.get("TextValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instances(AbstractModel):
    r"""复制组实例

    """

    def __init__(self):
        r"""
        :param _AppId: 用户APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。
        :type AppId: int
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _RegionId: 地域ID。<ul><li>1：广州。</li><li>4：上海。</li><li> 5：香港。</li>  <li> 7：上海金融。</li> <li> 8：北京。</li> <li> 9：新加坡。</li> <li> 11：深圳金融。</li> <li> 15：美西（硅谷）。</li> </ul>
        :type RegionId: int
        :param _ZoneId: 区域 ID。
        :type ZoneId: int
        :param _RedisReplicasNum: 副本数量。
        :type RedisReplicasNum: int
        :param _RedisShardNum: 分片数量。
        :type RedisShardNum: int
        :param _RedisShardSize: 分片内存大小。
        :type RedisShardSize: int
        :param _DiskSize: 实例的磁盘大小。
        :type DiskSize: int
        :param _Engine: 引擎：社区版Redis、腾讯云CKV。
        :type Engine: str
        :param _Role: 实例读写权限。<ul><li>rw：可读写。</li><li>r：只读。</li></ul>
        :type Role: str
        :param _Vip: 实例 VIP 地址。
        :type Vip: str
        :param _Vip6: 该参数存在命名不规范问题，建议用参数IPv6取代。内部参数，用户可忽略。
        :type Vip6: str
        :param _IPv6: 内部参数，用户可忽略。
        :type IPv6: str
        :param _VpcID: VPC 网络ID，如：75101。
        :type VpcID: int
        :param _VPort: 实例端口。
        :type VPort: int
        :param _Status: 实例状态。<ul><li>0：待初始化。</li><li>1：流程中。</li><li>2：运行中。</li><li>-2：已隔离。</li><li>-3：待删除。</li></ul>
        :type Status: int
        :param _GrocerySysId: 仓库ID。
        :type GrocerySysId: int
        :param _ProductType: 实例类型。
- 2：Redis 2.8内存版（标准架构）。
- 3：CKV 3.2内存版（标准架构）。
- 4：CKV 3.2内存版（集群架构）。
- 5：Redis 2.8内存版（单机）。
- 6：Redis 4.0内存版（标准架构）。
- 7：Redis 4.0内存版（集群架构）。
- 8：Redis 5.0内存版（标准架构）。
- 9：Redis 5.0内存版（集群架构）。
- 15：Redis 6.2内存版（标准架构）。
- 16：Redis 6.2内存版（集群架构）。
        :type ProductType: int
        :param _CreateTime: 实例加入复制组的时间。
        :type CreateTime: str
        :param _UpdateTime: 复制组中实例更新的时间。
        :type UpdateTime: str
        """
        self._AppId = None
        self._InstanceId = None
        self._InstanceName = None
        self._RegionId = None
        self._ZoneId = None
        self._RedisReplicasNum = None
        self._RedisShardNum = None
        self._RedisShardSize = None
        self._DiskSize = None
        self._Engine = None
        self._Role = None
        self._Vip = None
        self._Vip6 = None
        self._IPv6 = None
        self._VpcID = None
        self._VPort = None
        self._Status = None
        self._GrocerySysId = None
        self._ProductType = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def AppId(self):
        r"""用户APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegionId(self):
        r"""地域ID。<ul><li>1：广州。</li><li>4：上海。</li><li> 5：香港。</li>  <li> 7：上海金融。</li> <li> 8：北京。</li> <li> 9：新加坡。</li> <li> 11：深圳金融。</li> <li> 15：美西（硅谷）。</li> </ul>
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""区域 ID。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RedisReplicasNum(self):
        r"""副本数量。
        :rtype: int
        """
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def RedisShardNum(self):
        r"""分片数量。
        :rtype: int
        """
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisShardSize(self):
        r"""分片内存大小。
        :rtype: int
        """
        return self._RedisShardSize

    @RedisShardSize.setter
    def RedisShardSize(self, RedisShardSize):
        self._RedisShardSize = RedisShardSize

    @property
    def DiskSize(self):
        r"""实例的磁盘大小。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Engine(self):
        r"""引擎：社区版Redis、腾讯云CKV。
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Role(self):
        r"""实例读写权限。<ul><li>rw：可读写。</li><li>r：只读。</li></ul>
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Vip(self):
        r"""实例 VIP 地址。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vip6(self):
        r"""该参数存在命名不规范问题，建议用参数IPv6取代。内部参数，用户可忽略。
        :rtype: str
        """
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def IPv6(self):
        r"""内部参数，用户可忽略。
        :rtype: str
        """
        return self._IPv6

    @IPv6.setter
    def IPv6(self, IPv6):
        self._IPv6 = IPv6

    @property
    def VpcID(self):
        r"""VPC 网络ID，如：75101。
        :rtype: int
        """
        return self._VpcID

    @VpcID.setter
    def VpcID(self, VpcID):
        self._VpcID = VpcID

    @property
    def VPort(self):
        r"""实例端口。
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def Status(self):
        r"""实例状态。<ul><li>0：待初始化。</li><li>1：流程中。</li><li>2：运行中。</li><li>-2：已隔离。</li><li>-3：待删除。</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GrocerySysId(self):
        r"""仓库ID。
        :rtype: int
        """
        return self._GrocerySysId

    @GrocerySysId.setter
    def GrocerySysId(self, GrocerySysId):
        self._GrocerySysId = GrocerySysId

    @property
    def ProductType(self):
        r"""实例类型。
- 2：Redis 2.8内存版（标准架构）。
- 3：CKV 3.2内存版（标准架构）。
- 4：CKV 3.2内存版（集群架构）。
- 5：Redis 2.8内存版（单机）。
- 6：Redis 4.0内存版（标准架构）。
- 7：Redis 4.0内存版（集群架构）。
- 8：Redis 5.0内存版（标准架构）。
- 9：Redis 5.0内存版（集群架构）。
- 15：Redis 6.2内存版（标准架构）。
- 16：Redis 6.2内存版（集群架构）。
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def CreateTime(self):
        r"""实例加入复制组的时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""复制组中实例更新的时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisShardSize = params.get("RedisShardSize")
        self._DiskSize = params.get("DiskSize")
        self._Engine = params.get("Engine")
        self._Role = params.get("Role")
        self._Vip = params.get("Vip")
        self._Vip6 = params.get("Vip6")
        self._IPv6 = params.get("IPv6")
        self._VpcID = params.get("VpcID")
        self._VPort = params.get("VPort")
        self._Status = params.get("Status")
        self._GrocerySysId = params.get("GrocerySysId")
        self._ProductType = params.get("ProductType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMasterGroupRequest(AbstractModel):
    r"""KillMasterGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Password: 该参数用于配置指定实例的访问密码。若为免密认证，该参数则无需配置。密码复杂度要求如下所示。
- 长度8-30位,推荐使用12位以上的密码
- 不能以"/"开头
- 至少包含小写字母a-z、大写字母A-Z、数字0-9及其 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/中的两项。
        :type Password: str
        :param _ShardIds: 分片集群的分片 ID。请通过接口[DescribeInstanceNodeInfo](https://cloud.tencent.com/document/product/239/48603) 的返回参数 **Redis** 中的 **ClusterId** 获取。
        :type ShardIds: list of int
        """
        self._InstanceId = None
        self._Password = None
        self._ShardIds = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        r"""该参数用于配置指定实例的访问密码。若为免密认证，该参数则无需配置。密码复杂度要求如下所示。
- 长度8-30位,推荐使用12位以上的密码
- 不能以"/"开头
- 至少包含小写字母a-z、大写字母A-Z、数字0-9及其 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/中的两项。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ShardIds(self):
        r"""分片集群的分片 ID。请通过接口[DescribeInstanceNodeInfo](https://cloud.tencent.com/document/product/239/48603) 的返回参数 **Redis** 中的 **ClusterId** 获取。
        :rtype: list of int
        """
        return self._ShardIds

    @ShardIds.setter
    def ShardIds(self, ShardIds):
        self._ShardIds = ShardIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._ShardIds = params.get("ShardIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMasterGroupResponse(AbstractModel):
    r"""KillMasterGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
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


class LogDeliveryInfo(AbstractModel):
    r"""日志投递信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 日志投递开启状态，开启：true，关闭：false
        :type Enabled: bool
        :param _LogsetId: 日志集ID。
        :type LogsetId: str
        :param _TopicId: 日志主题ID。
        :type TopicId: str
        :param _LogRegion: 日志集所在地域
        :type LogRegion: str
        """
        self._Enabled = None
        self._LogsetId = None
        self._TopicId = None
        self._LogRegion = None

    @property
    def Enabled(self):
        r"""日志投递开启状态，开启：true，关闭：false
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def LogsetId(self):
        r"""日志集ID。
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        r"""日志主题ID。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogRegion(self):
        r"""日志集所在地域
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._LogRegion = params.get("LogRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualBackupInstanceRequest(AbstractModel):
    r"""ManualBackupInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Remark: 手动备份任务的备注信息。
        :type Remark: str
        :param _StorageDays: 备份数据的保存天数。
- 单位：天；默认值为7天；取值范围：[0.1825]。如果超过 7天，请[提交工单](https://console.cloud.tencent.com/workorder/category)申请。
- 如果不配置该参数，默认与自动备份的保留时间一致。
- 如果未设置自动备份，默认为7天。
        :type StorageDays: int
        """
        self._InstanceId = None
        self._Remark = None
        self._StorageDays = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Remark(self):
        r"""手动备份任务的备注信息。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def StorageDays(self):
        r"""备份数据的保存天数。
- 单位：天；默认值为7天；取值范围：[0.1825]。如果超过 7天，请[提交工单](https://console.cloud.tencent.com/workorder/category)申请。
- 如果不配置该参数，默认与自动备份的保留时间一致。
- 如果未设置自动备份，默认为7天。
        :rtype: int
        """
        return self._StorageDays

    @StorageDays.setter
    def StorageDays(self, StorageDays):
        self._StorageDays = StorageDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Remark = params.get("Remark")
        self._StorageDays = params.get("StorageDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualBackupInstanceResponse(AbstractModel):
    r"""ManualBackupInstance返回参数结构体

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


class ModfiyInstancePasswordRequest(AbstractModel):
    r"""ModfiyInstancePassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _OldPassword: 实例旧密码。
        :type OldPassword: str
        :param _Password: 实例新密码。密码复杂度要求如下：
- 长度8 - 64位, 推荐使用12位以上的密码。
- 不能以"/"开头。
- 至少包含小写字母a - z、大写字母A - Z、数字0 - 9、特殊字符 ()~!@#$%^&*-+=_|{}[]:;<>,.?/中的两项。
        :type Password: str
        :param _EncryptPassword: 是否加密密码
        :type EncryptPassword: bool
        """
        self._InstanceId = None
        self._OldPassword = None
        self._Password = None
        self._EncryptPassword = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldPassword(self):
        r"""实例旧密码。
        :rtype: str
        """
        return self._OldPassword

    @OldPassword.setter
    def OldPassword(self, OldPassword):
        self._OldPassword = OldPassword

    @property
    def Password(self):
        r"""实例新密码。密码复杂度要求如下：
- 长度8 - 64位, 推荐使用12位以上的密码。
- 不能以"/"开头。
- 至少包含小写字母a - z、大写字母A - Z、数字0 - 9、特殊字符 ()~!@#$%^&*-+=_|{}[]:;<>,.?/中的两项。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EncryptPassword(self):
        r"""是否加密密码
        :rtype: bool
        """
        return self._EncryptPassword

    @EncryptPassword.setter
    def EncryptPassword(self, EncryptPassword):
        self._EncryptPassword = EncryptPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldPassword = params.get("OldPassword")
        self._Password = params.get("Password")
        self._EncryptPassword = params.get("EncryptPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModfiyInstancePasswordResponse(AbstractModel):
    r"""ModfiyInstancePassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID。
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


class ModifyAutoBackupConfigRequest(AbstractModel):
    r"""ModifyAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :type InstanceId: str
        :param _WeekDays: 设置自动备份周期。可设置为Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。该参数暂不支持修改。
        :type WeekDays: list of str
        :param _TimePeriod: 备份时间段。可设置为每个整点。格式如：00:00-01:00, 01:00-02:00...... 23:00-00:00。
        :type TimePeriod: str
        :param _AutoBackupType: 自动备份类型。目前仅能配置为：1 ，指定时备份。
        :type AutoBackupType: int
        :param _BackupStorageDays: 全量备份文件保存天数。 仅支持设置为 7，单位：天。如需更长天数，请[提交工单](https://console.cloud.tencent.com/workorder/category)申请。
        :type BackupStorageDays: int
        """
        self._InstanceId = None
        self._WeekDays = None
        self._TimePeriod = None
        self._AutoBackupType = None
        self._BackupStorageDays = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WeekDays(self):
        r"""设置自动备份周期。可设置为Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。该参数暂不支持修改。
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        r"""备份时间段。可设置为每个整点。格式如：00:00-01:00, 01:00-02:00...... 23:00-00:00。
        :rtype: str
        """
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def AutoBackupType(self):
        r"""自动备份类型。目前仅能配置为：1 ，指定时备份。
        :rtype: int
        """
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType

    @property
    def BackupStorageDays(self):
        r"""全量备份文件保存天数。 仅支持设置为 7，单位：天。如需更长天数，请[提交工单](https://console.cloud.tencent.com/workorder/category)申请。
        :rtype: int
        """
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        self._AutoBackupType = params.get("AutoBackupType")
        self._BackupStorageDays = params.get("BackupStorageDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupConfigResponse(AbstractModel):
    r"""ModifyAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoBackupType: 自动备份类型。目前仅能配置为：1 ，指定时备份。
        :type AutoBackupType: int
        :param _WeekDays: 自动备份周期。取值为：Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param _TimePeriod: 自动定时备份时间段。格式如：00:00-01:00, 01:00-02:00...... 23:00-00:00。
        :type TimePeriod: str
        :param _BackupStorageDays: 全量备份文件保存天数,单位：天。
        :type BackupStorageDays: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoBackupType = None
        self._WeekDays = None
        self._TimePeriod = None
        self._BackupStorageDays = None
        self._RequestId = None

    @property
    def AutoBackupType(self):
        r"""自动备份类型。目前仅能配置为：1 ，指定时备份。
        :rtype: int
        """
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType

    @property
    def WeekDays(self):
        r"""自动备份周期。取值为：Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        r"""自动定时备份时间段。格式如：00:00-01:00, 01:00-02:00...... 23:00-00:00。
        :rtype: str
        """
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def BackupStorageDays(self):
        r"""全量备份文件保存天数,单位：天。
        :rtype: int
        """
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays

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
        self._AutoBackupType = params.get("AutoBackupType")
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        self._BackupStorageDays = params.get("BackupStorageDays")
        self._RequestId = params.get("RequestId")


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    r"""ModifyBackupDownloadRestriction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LimitType: 下载备份文件的网络限制类型：

- NoLimit：不限制，腾讯云内外网均可以下载备份文件。
-  LimitOnlyIntranet：仅腾讯云自动分配的内网地址可下载备份文件。
- Customize：指用户自定义的私有网络可下载备份文件。
        :type LimitType: str
        :param _VpcComparisonSymbol: 该参数仅支持输入 In，表示自定义的**LimitVpc**可以下载备份文件。
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: 标识自定义的 LimitIp 地址是否可下载备份文件。

- In: 自定义的 IP 地址可以下载。
- NotIn: 自定义的 IP 不可以下载。
        :type IpComparisonSymbol: str
        :param _LimitVpc: 自定义的可下载备份文件的 VPC ID。当参数**LimitType**为**Customize **时，需配置该参数。
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: 自定义的可下载备份文件的 VPC IP 地址。当参数**LimitType**为**Customize **时，需配置该参数。

        :type LimitIp: list of str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None

    @property
    def LimitType(self):
        r"""下载备份文件的网络限制类型：

- NoLimit：不限制，腾讯云内外网均可以下载备份文件。
-  LimitOnlyIntranet：仅腾讯云自动分配的内网地址可下载备份文件。
- Customize：指用户自定义的私有网络可下载备份文件。
        :rtype: str
        """
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        r"""该参数仅支持输入 In，表示自定义的**LimitVpc**可以下载备份文件。
        :rtype: str
        """
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        r"""标识自定义的 LimitIp 地址是否可下载备份文件。

- In: 自定义的 IP 地址可以下载。
- NotIn: 自定义的 IP 不可以下载。
        :rtype: str
        """
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        r"""自定义的可下载备份文件的 VPC ID。当参数**LimitType**为**Customize **时，需配置该参数。
        :rtype: list of BackupLimitVpcItem
        """
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        r"""自定义的可下载备份文件的 VPC IP 地址。当参数**LimitType**为**Customize **时，需配置该参数。

        :rtype: list of str
        """
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
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


class ModifyConnectionConfigRequest(AbstractModel):
    r"""ModifyConnectionConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Bandwidth: 附加带宽，大于0，单位MB。
**说明**：Bandwidth 和 ClientLimit 参数不能同时为空，您必须至少选择其中一个进行配置。
        :type Bandwidth: int
        :param _ClientLimit: 单分片的总连接数。
- 未开启副本只读时，下限为10000，上限为40000。
- 开启副本只读时，下限为10000，上限为10000×(只读副本数+3)。
**说明**：Bandwidth 和 ClientLimit 参数不能同时为空，您必须至少选择其中一个进行配置。
        :type ClientLimit: int
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._ClientLimit = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        r"""附加带宽，大于0，单位MB。
**说明**：Bandwidth 和 ClientLimit 参数不能同时为空，您必须至少选择其中一个进行配置。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ClientLimit(self):
        r"""单分片的总连接数。
- 未开启副本只读时，下限为10000，上限为40000。
- 开启副本只读时，下限为10000，上限为10000×(只读副本数+3)。
**说明**：Bandwidth 和 ClientLimit 参数不能同时为空，您必须至少选择其中一个进行配置。
        :rtype: int
        """
        return self._ClientLimit

    @ClientLimit.setter
    def ClientLimit(self, ClientLimit):
        self._ClientLimit = ClientLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        self._ClientLimit = params.get("ClientLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConnectionConfigResponse(AbstractModel):
    r"""ModifyConnectionConfig返回参数结构体

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
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _SecurityGroupIds: 更换为新的安全组 ID 列表，即一个或者多个安全组 ID 组成的数组。
- 若实例第一次配置安全组，请使用接口[AssociateSecurityGroups](https://cloud.tencent.com/document/product/239/41260)先绑定安全组。
- 更换安全组，请在[控制台安全组](https://console.cloud.tencent.com/vpc/security-group)页面获取安全组 ID。
  **注意：**该入参会全量替换存量已有集合，非增量更新。修改需传入预期的全量集合。
        :type SecurityGroupIds: list of str
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._Product = None
        self._SecurityGroupIds = None
        self._InstanceId = None

    @property
    def Product(self):
        r"""数据库引擎名称，本接口取值：redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupIds(self):
        r"""更换为新的安全组 ID 列表，即一个或者多个安全组 ID 组成的数组。
- 若实例第一次配置安全组，请使用接口[AssociateSecurityGroups](https://cloud.tencent.com/document/product/239/41260)先绑定安全组。
- 更换安全组，请在[控制台安全组](https://console.cloud.tencent.com/vpc/security-group)页面获取安全组 ID。
  **注意：**该入参会全量替换存量已有集合，非增量更新。修改需传入预期的全量集合。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceId = params.get("InstanceId")
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


class ModifyInstanceAccountRequest(AbstractModel):
    r"""ModifyInstanceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _AccountName: 指定需修改的账号。
- root：指在创建 Redis 数据库实例时自动生成的账号。用户无法修改其读写权限，仅可修改其请求路由策略。
- 自定义的账号：用户在实例创建成功后手动创建的账号。用户可以随时修改其读写权限与请求路由策略。
        :type AccountName: str
        :param _AccountPassword: 指定所修改账号访问的密码。
        :type AccountPassword: str
        :param _Remark: 账号描述信息
        :type Remark: str
        :param _ReadonlyPolicy: 指定所修改账号读写请求路由的策略。
- master：表示读写请求路由至主节点。
- replication：表示读写请求路由至从节点。
        :type ReadonlyPolicy: list of str
        :param _Privilege: 指定所修改账号的读写权限。
- r：只读。
- w：只写。
- rw：读写。
        :type Privilege: str
        :param _NoAuth: 指定是否将默认账号（root）设置为免密账号。自定义账号不支持免密访问。
- true：默认账号（root）设置为免密账号。
- false：默认账号（root）不设置为免密账号。
        :type NoAuth: bool
        :param _EncryptPassword: 指定所修改的账号是否加密密码
        :type EncryptPassword: bool
        """
        self._InstanceId = None
        self._AccountName = None
        self._AccountPassword = None
        self._Remark = None
        self._ReadonlyPolicy = None
        self._Privilege = None
        self._NoAuth = None
        self._EncryptPassword = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        r"""指定需修改的账号。
- root：指在创建 Redis 数据库实例时自动生成的账号。用户无法修改其读写权限，仅可修改其请求路由策略。
- 自定义的账号：用户在实例创建成功后手动创建的账号。用户可以随时修改其读写权限与请求路由策略。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        r"""指定所修改账号访问的密码。
        :rtype: str
        """
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def Remark(self):
        r"""账号描述信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ReadonlyPolicy(self):
        r"""指定所修改账号读写请求路由的策略。
- master：表示读写请求路由至主节点。
- replication：表示读写请求路由至从节点。
        :rtype: list of str
        """
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Privilege(self):
        r"""指定所修改账号的读写权限。
- r：只读。
- w：只写。
- rw：读写。
        :rtype: str
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def NoAuth(self):
        r"""指定是否将默认账号（root）设置为免密账号。自定义账号不支持免密访问。
- true：默认账号（root）设置为免密账号。
- false：默认账号（root）不设置为免密账号。
        :rtype: bool
        """
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def EncryptPassword(self):
        r"""指定所修改的账号是否加密密码
        :rtype: bool
        """
        return self._EncryptPassword

    @EncryptPassword.setter
    def EncryptPassword(self, EncryptPassword):
        self._EncryptPassword = EncryptPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._Remark = params.get("Remark")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Privilege = params.get("Privilege")
        self._NoAuth = params.get("NoAuth")
        self._EncryptPassword = params.get("EncryptPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAccountResponse(AbstractModel):
    r"""ModifyInstanceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

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


class ModifyInstanceAvailabilityZonesRequest(AbstractModel):
    r"""ModifyInstanceAvailabilityZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****，请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _SwitchOption: 切换时间。
- 1：维护时间窗切换。
- 2：立即切换。
        :type SwitchOption: int
        :param _NodeSet: 实例的节点信息，包含节点 ID、节点类型、节点可用区 ID等。具体信息，请参见[RedisNodeInfo ](https://cloud.tencent.com/document/product/239/20022)。
单可用区实例无需传NodeId，多可用区实例NodeId必传
        :type NodeSet: list of RedisNodeInfo
        """
        self._InstanceId = None
        self._SwitchOption = None
        self._NodeSet = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****，请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SwitchOption(self):
        r"""切换时间。
- 1：维护时间窗切换。
- 2：立即切换。
        :rtype: int
        """
        return self._SwitchOption

    @SwitchOption.setter
    def SwitchOption(self, SwitchOption):
        self._SwitchOption = SwitchOption

    @property
    def NodeSet(self):
        r"""实例的节点信息，包含节点 ID、节点类型、节点可用区 ID等。具体信息，请参见[RedisNodeInfo ](https://cloud.tencent.com/document/product/239/20022)。
单可用区实例无需传NodeId，多可用区实例NodeId必传
        :rtype: list of RedisNodeInfo
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SwitchOption = params.get("SwitchOption")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAvailabilityZonesResponse(AbstractModel):
    r"""ModifyInstanceAvailabilityZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。	
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

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


class ModifyInstanceBackupModeRequest(AbstractModel):
    r"""ModifyInstanceBackupMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例的ID。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _BackupMode: 备份模式：
- SecondLevelBackup   秒级备份。
- NormalLevelBackup    普通备份。
        :type BackupMode: str
        """
        self._InstanceId = None
        self._BackupMode = None

    @property
    def InstanceId(self):
        r"""实例的ID。请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMode(self):
        r"""备份模式：
- SecondLevelBackup   秒级备份。
- NormalLevelBackup    普通备份。
        :rtype: str
        """
        return self._BackupMode

    @BackupMode.setter
    def BackupMode(self, BackupMode):
        self._BackupMode = BackupMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMode = params.get("BackupMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceBackupModeResponse(AbstractModel):
    r"""ModifyInstanceBackupMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID。
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


class ModifyInstanceEventRequest(AbstractModel):
    r"""ModifyInstanceEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _EventId: 事件 ID。请通过 [DescribeInstanceEvents](https://cloud.tencent.com/document/product/239/104779) 获取需修改的事件 ID。
        :type EventId: int
        :param _StartTime: 修改事件执行的计划开始时间。
        :type StartTime: str
        :param _EndTime: 修改事件计划执行的结束时间。开始时间配置之后，结束时间只能选择在开始时间之后的 30 分钟、1 小时、1.5 小时、2 小时和 3 小时之内。
        :type EndTime: str
        :param _ExecutionDate: 修改事件执行计划的开始日期。
        :type ExecutionDate: str
        :param _Status: 修改事件的运行状态。该参数当前仅支持设置为 **Canceled**， 即取消执行当前事件。可通过 DescribeInstanceEvents 接口查询当前事件的运行状态与事件级别。
- 事件级别为Critical（关键）或 High（重要）类事件不支持取消。即严重的事件必须执行，不可取消。
- 仅运行状态为 Waiting （待执行的事件）的事件，才能执行取消操作。
        :type Status: str
        """
        self._InstanceId = None
        self._EventId = None
        self._StartTime = None
        self._EndTime = None
        self._ExecutionDate = None
        self._Status = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventId(self):
        r"""事件 ID。请通过 [DescribeInstanceEvents](https://cloud.tencent.com/document/product/239/104779) 获取需修改的事件 ID。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def StartTime(self):
        r"""修改事件执行的计划开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""修改事件计划执行的结束时间。开始时间配置之后，结束时间只能选择在开始时间之后的 30 分钟、1 小时、1.5 小时、2 小时和 3 小时之内。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExecutionDate(self):
        r"""修改事件执行计划的开始日期。
        :rtype: str
        """
        return self._ExecutionDate

    @ExecutionDate.setter
    def ExecutionDate(self, ExecutionDate):
        self._ExecutionDate = ExecutionDate

    @property
    def Status(self):
        r"""修改事件的运行状态。该参数当前仅支持设置为 **Canceled**， 即取消执行当前事件。可通过 DescribeInstanceEvents 接口查询当前事件的运行状态与事件级别。
- 事件级别为Critical（关键）或 High（重要）类事件不支持取消。即严重的事件必须执行，不可取消。
- 仅运行状态为 Waiting （待执行的事件）的事件，才能执行取消操作。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EventId = params.get("EventId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExecutionDate = params.get("ExecutionDate")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceEventResponse(AbstractModel):
    r"""ModifyInstanceEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventId: 事件 ID。
        :type EventId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventId = None
        self._RequestId = None

    @property
    def EventId(self):
        r"""事件 ID。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

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
        self._EventId = params.get("EventId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceLogDeliveryRequest(AbstractModel):
    r"""ModifyInstanceLogDelivery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _LogType: 日志类型。当前仅支持设置为slowlog，指慢查询日志。
        :type LogType: str
        :param _Enabled: 日志投递开启状态。
- true：开启。
- false：关闭。
        :type Enabled: bool
        :param _LogsetId: 投递的日志集ID。通过接口[DescribeLogsets](https://cloud.tencent.com/document/api/614/58624)获取到日志集ID。
        :type LogsetId: str
        :param _TopicId: 投递的日志主题ID。通过接口[DescribeTopics](https://cloud.tencent.com/document/api/614/56454)获取到日志主题ID。
        :type TopicId: str
        :param _LogsetName: 日志集名称。**LogsetId**为空时必传，系统会以LogsetName为名称来创建新的日志集并投递日志。
        :type LogsetName: str
        :param _TopicName: 日志主题名称。**TopicId**为空时必传，系统会以TopicName为名称来创建新的日志主题并投递日志。
        :type TopicName: str
        :param _LogRegion: 日志集所在地域，不传默认使用实例所在地域。
        :type LogRegion: str
        :param _Period: 日志存储时间，默认为30天，可选范围1-3600天。
        :type Period: int
        :param _CreateIndex: 创建日志主题时，是否创建索引。
        :type CreateIndex: bool
        """
        self._InstanceId = None
        self._LogType = None
        self._Enabled = None
        self._LogsetId = None
        self._TopicId = None
        self._LogsetName = None
        self._TopicName = None
        self._LogRegion = None
        self._Period = None
        self._CreateIndex = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogType(self):
        r"""日志类型。当前仅支持设置为slowlog，指慢查询日志。
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Enabled(self):
        r"""日志投递开启状态。
- true：开启。
- false：关闭。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def LogsetId(self):
        r"""投递的日志集ID。通过接口[DescribeLogsets](https://cloud.tencent.com/document/api/614/58624)获取到日志集ID。
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        r"""投递的日志主题ID。通过接口[DescribeTopics](https://cloud.tencent.com/document/api/614/56454)获取到日志主题ID。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetName(self):
        r"""日志集名称。**LogsetId**为空时必传，系统会以LogsetName为名称来创建新的日志集并投递日志。
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicName(self):
        r"""日志主题名称。**TopicId**为空时必传，系统会以TopicName为名称来创建新的日志主题并投递日志。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def LogRegion(self):
        r"""日志集所在地域，不传默认使用实例所在地域。
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def Period(self):
        r"""日志存储时间，默认为30天，可选范围1-3600天。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def CreateIndex(self):
        r"""创建日志主题时，是否创建索引。
        :rtype: bool
        """
        return self._CreateIndex

    @CreateIndex.setter
    def CreateIndex(self, CreateIndex):
        self._CreateIndex = CreateIndex


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogType = params.get("LogType")
        self._Enabled = params.get("Enabled")
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._LogsetName = params.get("LogsetName")
        self._TopicName = params.get("TopicName")
        self._LogRegion = params.get("LogRegion")
        self._Period = params.get("Period")
        self._CreateIndex = params.get("CreateIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceLogDeliveryResponse(AbstractModel):
    r"""ModifyInstanceLogDelivery返回参数结构体

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


class ModifyInstanceParamsRequest(AbstractModel):
    r"""ModifyInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _InstanceParams: 实例修改的参数列表。
        :type InstanceParams: list of InstanceParam
        """
        self._InstanceId = None
        self._InstanceParams = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceParams(self):
        r"""实例修改的参数列表。
        :rtype: list of InstanceParam
        """
        return self._InstanceParams

    @InstanceParams.setter
    def InstanceParams(self, InstanceParams):
        self._InstanceParams = InstanceParams


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("InstanceParams") is not None:
            self._InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InstanceParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamsResponse(AbstractModel):
    r"""ModifyInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Changed: 说明修改参数配置是否成功。<br><li>true：指修改成功；</li><li>false：指修改失败。</li>
        :type Changed: bool
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Changed = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Changed(self):
        r"""说明修改参数配置是否成功。<br><li>true：指修改成功；</li><li>false：指修改失败。</li>
        :rtype: bool
        """
        return self._Changed

    @Changed.setter
    def Changed(self, Changed):
        self._Changed = Changed

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
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Changed = params.get("Changed")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstancePasswordRequest(AbstractModel):
    r"""ModifyInstancePassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _OldPassword: 实例旧密码。
        :type OldPassword: str
        :param _Password: 实例新密码。密码复杂度要求如下：
- 长度8 - 30位, 推荐使用12位以上的密码。
- 不能以"/"开头。
- 至少包含小写字母a - z、大写字母A - Z、数字0 - 9、特殊字符 ()~!@#$%^&*-+=_|{}[]:;<>,.?/中的两项。
        :type Password: str
        """
        self._InstanceId = None
        self._OldPassword = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldPassword(self):
        r"""实例旧密码。
        :rtype: str
        """
        return self._OldPassword

    @OldPassword.setter
    def OldPassword(self, OldPassword):
        self._OldPassword = OldPassword

    @property
    def Password(self):
        r"""实例新密码。密码复杂度要求如下：
- 长度8 - 30位, 推荐使用12位以上的密码。
- 不能以"/"开头。
- 至少包含小写字母a - z、大写字母A - Z、数字0 - 9、特殊字符 ()~!@#$%^&*-+=_|{}[]:;<>,.?/中的两项。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldPassword = params.get("OldPassword")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancePasswordResponse(AbstractModel):
    r"""ModifyInstancePassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID。
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


class ModifyInstanceReadOnlyRequest(AbstractModel):
    r"""ModifyInstanceReadOnly请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _InputMode: 实例输入模式。
- 0：读写。
- 1：只读。
        :type InputMode: str
        """
        self._InstanceId = None
        self._InputMode = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InputMode(self):
        r"""实例输入模式。
- 0：读写。
- 1：只读。
        :rtype: str
        """
        return self._InputMode

    @InputMode.setter
    def InputMode(self, InputMode):
        self._InputMode = InputMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InputMode = params.get("InputMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceReadOnlyResponse(AbstractModel):
    r"""ModifyInstanceReadOnly返回参数结构体

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


class ModifyInstanceRequest(AbstractModel):
    r"""ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operation: 修改实例操作。如填写：
- rename：表示实例重命名。
- modifyProject：修改实例所属项目。
- modifyAutoRenew：修改实例续费标记。
- modifyDeleteProtectionSwitch：修改实例删除保护。
        :type Operation: str
        :param _InstanceIds: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。每次请求的实例数量的上限为10。
        :type InstanceIds: list of str
        :param _InstanceNames: 实例的新名称。名称只支持长度为60个字符的中文、英文、数字、下划线_、分隔符-。
        :type InstanceNames: list of str
        :param _ProjectId: 项目 ID，请登录[Redis控制台的项目管理](https://console.cloud.tencent.com/project)页面，在**项目名称**中复制项目 ID。
        :type ProjectId: int
        :param _AutoRenews: 自动续费标识。
- 0：默认状态，指手动续费。
- 1：自动续费。
- 2：明确不自动续费。
        :type AutoRenews: list of int
        :param _DeleteProtectionSwitches: 删除保护开关。- 0：默认状态，指关闭。- 1：开关打开。
        :type DeleteProtectionSwitches: list of int
        :param _InstanceId: 目前在废弃中，存量用户还可以使用，建议新用户使用 InstanceIds。
        :type InstanceId: str
        :param _InstanceName: 已经废弃
        :type InstanceName: str
        :param _AutoRenew: 已经废弃。
        :type AutoRenew: int
        """
        self._Operation = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._ProjectId = None
        self._AutoRenews = None
        self._DeleteProtectionSwitches = None
        self._InstanceId = None
        self._InstanceName = None
        self._AutoRenew = None

    @property
    def Operation(self):
        r"""修改实例操作。如填写：
- rename：表示实例重命名。
- modifyProject：修改实例所属项目。
- modifyAutoRenew：修改实例续费标记。
- modifyDeleteProtectionSwitch：修改实例删除保护。
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstanceIds(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。每次请求的实例数量的上限为10。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        r"""实例的新名称。名称只支持长度为60个字符的中文、英文、数字、下划线_、分隔符-。
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def ProjectId(self):
        r"""项目 ID，请登录[Redis控制台的项目管理](https://console.cloud.tencent.com/project)页面，在**项目名称**中复制项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenews(self):
        r"""自动续费标识。
- 0：默认状态，指手动续费。
- 1：自动续费。
- 2：明确不自动续费。
        :rtype: list of int
        """
        return self._AutoRenews

    @AutoRenews.setter
    def AutoRenews(self, AutoRenews):
        self._AutoRenews = AutoRenews

    @property
    def DeleteProtectionSwitches(self):
        r"""删除保护开关。- 0：默认状态，指关闭。- 1：开关打开。
        :rtype: list of int
        """
        return self._DeleteProtectionSwitches

    @DeleteProtectionSwitches.setter
    def DeleteProtectionSwitches(self, DeleteProtectionSwitches):
        self._DeleteProtectionSwitches = DeleteProtectionSwitches

    @property
    def InstanceId(self):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        r"""目前在废弃中，存量用户还可以使用，建议新用户使用 InstanceIds。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        warnings.warn("parameter `InstanceName` is deprecated", DeprecationWarning) 

        r"""已经废弃
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        warnings.warn("parameter `InstanceName` is deprecated", DeprecationWarning) 

        self._InstanceName = InstanceName

    @property
    def AutoRenew(self):
        warnings.warn("parameter `AutoRenew` is deprecated", DeprecationWarning) 

        r"""已经废弃。
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        warnings.warn("parameter `AutoRenew` is deprecated", DeprecationWarning) 

        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenews = params.get("AutoRenews")
        self._DeleteProtectionSwitches = params.get("DeleteProtectionSwitches")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    r"""ModifyInstance返回参数结构体

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


class ModifyMaintenanceWindowRequest(AbstractModel):
    r"""ModifyMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _StartTime: 维护时间窗起始时间，如：17:00。
        :type StartTime: str
        :param _EndTime: 维护时间窗结束时间，如：19:00。
**说明：**维护时间窗时长，当前支持：30分钟、1小时、1.5小时、2小时、3小时。
        :type EndTime: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""维护时间窗起始时间，如：17:00。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""维护时间窗结束时间，如：19:00。
**说明：**维护时间窗时长，当前支持：30分钟、1小时、1.5小时、2小时、3小时。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceWindowResponse(AbstractModel):
    r"""ModifyMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 修改状态：success 或者 failed
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""修改状态：success 或者 failed
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyNetworkConfigRequest(AbstractModel):
    r"""ModifyNetworkConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Operation: 指预修改网络的类别，包括：
- changeVip：指切换私有网络，包含其内网IPv4地址及端口。
- changeVpc：指切换私有网络所属子网。
- changeBaseToVpc：指基础网络切换为私有网络。
- changeVPort：指仅修改实例网络端口。
        :type Operation: str
        :param _Vip: 指实例私有网络内网 IPv4 地址。当**Operation**为**changeVip**时，需配置该参数。
        :type Vip: str
        :param _VpcId: 指修改后的私有网络 ID。
- 当**Operation**为**changeVpc**或**changeBaseToVpc**时，需配置该参数。
- 请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)，切换至**实例详情**页面，在**网络信息**区域，单击所属网络后面的私有网络名称，获取私有网络 ID。

        :type VpcId: str
        :param _SubnetId: 指修改后的私有网络所属子网 ID。
- 当**Operation**为**changeVpc**或**changeBaseToVpc**时，需配置该参数。
- 请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)，切换至**实例详情**页面，在**网络信息**区域，单击所属网络后面的子网名称，获取子网ID。
        :type SubnetId: str
        :param _Recycle: 原内网 IPv4 地址保留时长。
- 单位：天。
- 取值范围：0、1、2、3、7、15。
**说明**：保留时长不设置或者设置为0，原网络地址将立即释放。
        :type Recycle: int
        :param _VPort: 指修改后的网络端口。当**Operation**为**changeVPort**或**changeVip**时，需配置该参数。取值范围为[1024,65535]。
        :type VPort: int
        """
        self._InstanceId = None
        self._Operation = None
        self._Vip = None
        self._VpcId = None
        self._SubnetId = None
        self._Recycle = None
        self._VPort = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Operation(self):
        r"""指预修改网络的类别，包括：
- changeVip：指切换私有网络，包含其内网IPv4地址及端口。
- changeVpc：指切换私有网络所属子网。
- changeBaseToVpc：指基础网络切换为私有网络。
- changeVPort：指仅修改实例网络端口。
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Vip(self):
        r"""指实例私有网络内网 IPv4 地址。当**Operation**为**changeVip**时，需配置该参数。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VpcId(self):
        r"""指修改后的私有网络 ID。
- 当**Operation**为**changeVpc**或**changeBaseToVpc**时，需配置该参数。
- 请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)，切换至**实例详情**页面，在**网络信息**区域，单击所属网络后面的私有网络名称，获取私有网络 ID。

        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""指修改后的私有网络所属子网 ID。
- 当**Operation**为**changeVpc**或**changeBaseToVpc**时，需配置该参数。
- 请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)，切换至**实例详情**页面，在**网络信息**区域，单击所属网络后面的子网名称，获取子网ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Recycle(self):
        r"""原内网 IPv4 地址保留时长。
- 单位：天。
- 取值范围：0、1、2、3、7、15。
**说明**：保留时长不设置或者设置为0，原网络地址将立即释放。
        :rtype: int
        """
        return self._Recycle

    @Recycle.setter
    def Recycle(self, Recycle):
        self._Recycle = Recycle

    @property
    def VPort(self):
        r"""指修改后的网络端口。当**Operation**为**changeVPort**或**changeVip**时，需配置该参数。取值范围为[1024,65535]。
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Operation = params.get("Operation")
        self._Vip = params.get("Vip")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Recycle = params.get("Recycle")
        self._VPort = params.get("VPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkConfigResponse(AbstractModel):
    r"""ModifyNetworkConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 执行状态，请忽略该参数。
        :type Status: bool
        :param _SubnetId: 指实例新私有网络所属子网 ID。
        :type SubnetId: str
        :param _VpcId: 指实例新的私有网络ID。
        :type VpcId: str
        :param _Vip: 指实例新的内网 IPv4 地址。
        :type Vip: str
        :param _TaskId: 任务 ID。获取**taskId**，通过接口 [DescribeTaskInfo](https://cloud.tencent.com/document/product/239/30601) 查询任务执行状态。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._SubnetId = None
        self._VpcId = None
        self._Vip = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Status(self):
        r"""执行状态，请忽略该参数。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        r"""指实例新私有网络所属子网 ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""指实例新的私有网络ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        r"""指实例新的内网 IPv4 地址。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def TaskId(self):
        r"""任务 ID。获取**taskId**，通过接口 [DescribeTaskInfo](https://cloud.tencent.com/document/product/239/30601) 查询任务执行状态。
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
        self._Status = params.get("Status")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Vip = params.get("Vip")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyParamTemplateRequest(AbstractModel):
    r"""ModifyParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 源参数模板 ID。 请通过接口[DescribeParamTemplateInfo](https://cloud.tencent.com/document/product/239/58748)的返回参数 **TemplateId** 获取参数模板 ID。 
        :type TemplateId: str
        :param _Name: 参数模板修改后的新名称。
        :type Name: str
        :param _Description: 参数模板修改后的新描述。
        :type Description: str
        :param _ParamList: 修改后的新参数列表。
        :type ParamList: list of InstanceParam
        """
        self._TemplateId = None
        self._Name = None
        self._Description = None
        self._ParamList = None

    @property
    def TemplateId(self):
        r"""源参数模板 ID。 请通过接口[DescribeParamTemplateInfo](https://cloud.tencent.com/document/product/239/58748)的返回参数 **TemplateId** 获取参数模板 ID。 
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        r"""参数模板修改后的新名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""参数模板修改后的新描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamList(self):
        r"""修改后的新参数列表。
        :rtype: list of InstanceParam
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    r"""ModifyParamTemplate返回参数结构体

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


class ModifyReplicationGroupRequest(AbstractModel):
    r"""ModifyReplicationGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID。请登录[Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication)页面获取复制组 ID。
        :type GroupId: str
        :param _GroupName: 修改后的复制组名称。
        :type GroupName: str
        :param _Remark: 备注描述。
        :type Remark: str
        """
        self._GroupId = None
        self._GroupName = None
        self._Remark = None

    @property
    def GroupId(self):
        r"""复制组ID。请登录[Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication)页面获取复制组 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""修改后的复制组名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Remark(self):
        r"""备注描述。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReplicationGroupResponse(AbstractModel):
    r"""ModifyReplicationGroup返回参数结构体

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


class OpenSSLRequest(AbstractModel):
    r"""OpenSSL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenSSLResponse(AbstractModel):
    r"""OpenSSL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

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


class Outbound(AbstractModel):
    r"""安全组出站规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT或者DROP。
        :type Action: str
        :param _AddressModule: 地址组id代表的地址集合。
        :type AddressModule: str
        :param _CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。
        :type CidrIp: str
        :param _Desc: 描述。
        :type Desc: str
        :param _IpProtocol: 网络协议，支持udp、tcp等。
        :type IpProtocol: str
        :param _PortRange: 端口。
        :type PortRange: str
        :param _ServiceModule: 服务组id代表的协议和端口集合。
        :type ServiceModule: str
        :param _Id: 安全组id代表的地址集合。
        :type Id: str
        """
        self._Action = None
        self._AddressModule = None
        self._CidrIp = None
        self._Desc = None
        self._IpProtocol = None
        self._PortRange = None
        self._ServiceModule = None
        self._Id = None

    @property
    def Action(self):
        r"""策略，ACCEPT或者DROP。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        r"""地址组id代表的地址集合。
        :rtype: str
        """
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        r"""来源Ip或Ip段，例如192.168.0.0/16。
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        r"""描述。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        r"""网络协议，支持udp、tcp等。
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        r"""端口。
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        r"""服务组id代表的协议和端口集合。
        :rtype: str
        """
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
        r"""安全组id代表的地址集合。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._AddressModule = params.get("AddressModule")
        self._CidrIp = params.get("CidrIp")
        self._Desc = params.get("Desc")
        self._IpProtocol = params.get("IpProtocol")
        self._PortRange = params.get("PortRange")
        self._ServiceModule = params.get("ServiceModule")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateInfo(AbstractModel):
    r"""参数模板信息

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板 ID。
        :type TemplateId: str
        :param _Name: 参数模板名称。
        :type Name: str
        :param _Description: 参数模板描述。
        :type Description: str
        :param _ProductType: 实例类型。
- 2：Redis 2.8内存版（标准架构）。
- 3：CKV 3.2内存版（标准架构）。
- 4：CKV 3.2内存版（集群架构）。
- 5：Redis 2.8内存版（单机）。
- 6：Redis 4.0内存版（标准架构）。
- 7：Redis 4.0内存版（集群架构）。
- 8：Redis 5.0内存版（标准架构）。
- 9：Redis 5.0内存版（集群架构）。
- 15：Redis 6.2内存版（标准架构）。
- 16：Redis 6.2内存版（集群架构）。
        :type ProductType: int
        """
        self._TemplateId = None
        self._Name = None
        self._Description = None
        self._ProductType = None

    @property
    def TemplateId(self):
        r"""参数模板 ID。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        r"""参数模板名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""参数模板描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductType(self):
        r"""实例类型。
- 2：Redis 2.8内存版（标准架构）。
- 3：CKV 3.2内存版（标准架构）。
- 4：CKV 3.2内存版（集群架构）。
- 5：Redis 2.8内存版（单机）。
- 6：Redis 4.0内存版（标准架构）。
- 7：Redis 4.0内存版（集群架构）。
- 8：Redis 5.0内存版（标准架构）。
- 9：Redis 5.0内存版（集群架构）。
- 15：Redis 6.2内存版（标准架构）。
- 16：Redis 6.2内存版（集群架构）。
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ProductType = params.get("ProductType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    r"""Redis参数模板参数详情

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称。
        :type Name: str
        :param _ParamType: 参数类型。
        :type ParamType: str
        :param _Default: 参数默认值。
        :type Default: str
        :param _Description: 参数描述。
        :type Description: str
        :param _CurrentValue: 参数当前值。
        :type CurrentValue: str
        :param _NeedReboot: 修改参数后，是否需要重启数据库以使参数生效。
- 0：不需要重启。
- 1：需要重启。
        :type NeedReboot: int
        :param _Max: 参数允许的最大值。
        :type Max: str
        :param _Min: 参数允许的最小值。
        :type Min: str
        :param _EnumValue: 参数可选枚举值。如果为非枚举参数，则为空。
        :type EnumValue: list of str
        """
        self._Name = None
        self._ParamType = None
        self._Default = None
        self._Description = None
        self._CurrentValue = None
        self._NeedReboot = None
        self._Max = None
        self._Min = None
        self._EnumValue = None

    @property
    def Name(self):
        r"""参数名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamType(self):
        r"""参数类型。
        :rtype: str
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Default(self):
        r"""参数默认值。
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        r"""参数描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        r"""参数当前值。
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        r"""修改参数后，是否需要重启数据库以使参数生效。
- 0：不需要重启。
- 1：需要重启。
        :rtype: int
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        r"""参数允许的最大值。
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        r"""参数允许的最小值。
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        r"""参数可选枚举值。如果为非枚举参数，则为空。
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ParamType = params.get("ParamType")
        self._Default = params.get("Default")
        self._Description = params.get("Description")
        self._CurrentValue = params.get("CurrentValue")
        self._NeedReboot = params.get("NeedReboot")
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
        


class ProductConf(AbstractModel):
    r"""产品信息

    """

    def __init__(self):
        r"""
        :param _Type: 产品类型。
- 2：Redis 2.8内存版（标准架构）。
- 3：CKV 3.2内存版（标准架构）。
- 4：CKV 3.2内存版（集群架构）。
- 5：Redis 2.8内存版（单机）。
- 6：Redis 4.0内存版（标准架构）。
- 7：Redis 4.0内存版（集群架构）。
- 8：Redis 5.0内存版（标准架构）。
- 9：Redis 5.0内存版（集群架构）。
- 15：Redis 6.2内存版（标准架构）。
- 16：Redis 6.2内存版（集群架构）。
        :type Type: int
        :param _TypeName: 产品名称。包括：Redis 主从版、CKV 主从版、CKV 集群版、Redis 单机版、Redis 集群版。
        :type TypeName: str
        :param _MinBuyNum: 购买时的最小数量。
        :type MinBuyNum: int
        :param _MaxBuyNum: 购买时的最大数量。
        :type MaxBuyNum: int
        :param _Saleout: 产品是否售罄。
- true：售罄。
- false：未售罄。
        :type Saleout: bool
        :param _Engine: 产品引擎。Redis 或者 CKV。
        :type Engine: str
        :param _Version: 兼容版本。包括：Redis-2.8、Redis-3.2、Redis-4.0、Redis-5.0、Redis-6.2。
        :type Version: str
        :param _TotalSize: 规格总大小，单位GB。
        :type TotalSize: list of str
        :param _ShardSize: 每个分片大小，单位GB。
        :type ShardSize: list of str
        :param _ReplicaNum: 副本数量。
        :type ReplicaNum: list of str
        :param _ShardNum: 分片数量。
        :type ShardNum: list of str
        :param _PayMode: 支持的计费模式。
- 1：包年包月。
- 0：按量计费。
        :type PayMode: str
        :param _EnableRepicaReadOnly: 该参数名因存在拼写不规范的问题，建议使用**EnableReplicaReadOnly**参数取代。其含义为是否支持副本只读。
- true：支持副本只读。
- false：不支持。
        :type EnableRepicaReadOnly: bool
        :param _EnableReplicaReadOnly: 是否支持副本只读。
- true：支持副本只读。
- false：不支持。
        :type EnableReplicaReadOnly: bool
        """
        self._Type = None
        self._TypeName = None
        self._MinBuyNum = None
        self._MaxBuyNum = None
        self._Saleout = None
        self._Engine = None
        self._Version = None
        self._TotalSize = None
        self._ShardSize = None
        self._ReplicaNum = None
        self._ShardNum = None
        self._PayMode = None
        self._EnableRepicaReadOnly = None
        self._EnableReplicaReadOnly = None

    @property
    def Type(self):
        r"""产品类型。
- 2：Redis 2.8内存版（标准架构）。
- 3：CKV 3.2内存版（标准架构）。
- 4：CKV 3.2内存版（集群架构）。
- 5：Redis 2.8内存版（单机）。
- 6：Redis 4.0内存版（标准架构）。
- 7：Redis 4.0内存版（集群架构）。
- 8：Redis 5.0内存版（标准架构）。
- 9：Redis 5.0内存版（集群架构）。
- 15：Redis 6.2内存版（标准架构）。
- 16：Redis 6.2内存版（集群架构）。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeName(self):
        r"""产品名称。包括：Redis 主从版、CKV 主从版、CKV 集群版、Redis 单机版、Redis 集群版。
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def MinBuyNum(self):
        r"""购买时的最小数量。
        :rtype: int
        """
        return self._MinBuyNum

    @MinBuyNum.setter
    def MinBuyNum(self, MinBuyNum):
        self._MinBuyNum = MinBuyNum

    @property
    def MaxBuyNum(self):
        r"""购买时的最大数量。
        :rtype: int
        """
        return self._MaxBuyNum

    @MaxBuyNum.setter
    def MaxBuyNum(self, MaxBuyNum):
        self._MaxBuyNum = MaxBuyNum

    @property
    def Saleout(self):
        r"""产品是否售罄。
- true：售罄。
- false：未售罄。
        :rtype: bool
        """
        return self._Saleout

    @Saleout.setter
    def Saleout(self, Saleout):
        self._Saleout = Saleout

    @property
    def Engine(self):
        r"""产品引擎。Redis 或者 CKV。
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Version(self):
        r"""兼容版本。包括：Redis-2.8、Redis-3.2、Redis-4.0、Redis-5.0、Redis-6.2。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def TotalSize(self):
        r"""规格总大小，单位GB。
        :rtype: list of str
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def ShardSize(self):
        r"""每个分片大小，单位GB。
        :rtype: list of str
        """
        return self._ShardSize

    @ShardSize.setter
    def ShardSize(self, ShardSize):
        self._ShardSize = ShardSize

    @property
    def ReplicaNum(self):
        r"""副本数量。
        :rtype: list of str
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def ShardNum(self):
        r"""分片数量。
        :rtype: list of str
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def PayMode(self):
        r"""支持的计费模式。
- 1：包年包月。
- 0：按量计费。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def EnableRepicaReadOnly(self):
        warnings.warn("parameter `EnableRepicaReadOnly` is deprecated", DeprecationWarning) 

        r"""该参数名因存在拼写不规范的问题，建议使用**EnableReplicaReadOnly**参数取代。其含义为是否支持副本只读。
- true：支持副本只读。
- false：不支持。
        :rtype: bool
        """
        return self._EnableRepicaReadOnly

    @EnableRepicaReadOnly.setter
    def EnableRepicaReadOnly(self, EnableRepicaReadOnly):
        warnings.warn("parameter `EnableRepicaReadOnly` is deprecated", DeprecationWarning) 

        self._EnableRepicaReadOnly = EnableRepicaReadOnly

    @property
    def EnableReplicaReadOnly(self):
        r"""是否支持副本只读。
- true：支持副本只读。
- false：不支持。
        :rtype: bool
        """
        return self._EnableReplicaReadOnly

    @EnableReplicaReadOnly.setter
    def EnableReplicaReadOnly(self, EnableReplicaReadOnly):
        self._EnableReplicaReadOnly = EnableReplicaReadOnly


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TypeName = params.get("TypeName")
        self._MinBuyNum = params.get("MinBuyNum")
        self._MaxBuyNum = params.get("MaxBuyNum")
        self._Saleout = params.get("Saleout")
        self._Engine = params.get("Engine")
        self._Version = params.get("Version")
        self._TotalSize = params.get("TotalSize")
        self._ShardSize = params.get("ShardSize")
        self._ReplicaNum = params.get("ReplicaNum")
        self._ShardNum = params.get("ShardNum")
        self._PayMode = params.get("PayMode")
        self._EnableRepicaReadOnly = params.get("EnableRepicaReadOnly")
        self._EnableReplicaReadOnly = params.get("EnableReplicaReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodes(AbstractModel):
    r"""Proxy节点信息。

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点 ID。
        :type NodeId: str
        :param _ZoneId: 可用区 ID。
        :type ZoneId: int
        """
        self._NodeId = None
        self._ZoneId = None

    @property
    def NodeId(self):
        r"""节点 ID。
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def ZoneId(self):
        r"""可用区 ID。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisBackupSet(AbstractModel):
    r"""实例的备份数组

    """

    def __init__(self):
        r"""
        :param _StartTime: 备份开始时间。
        :type StartTime: str
        :param _BackupId: 备份任务ID。
        :type BackupId: str
        :param _BackupType: 备份类型。
- 1：凌晨系统发起的自动备份。
- 0：用户发起的手动备份。
        :type BackupType: str
        :param _Status: 备份状态。 
- 1：备份被其它流程锁定。
- 2：备份正常，没有被任何流程锁定。
- -1：备份已过期。
- 3：备份正在被导出。
- 4：备份导出成功。
        :type Status: int
        :param _Remark: 备份的备注信息。
        :type Remark: str
        :param _Locked: 备份是否被锁定。
- 0：未被锁定。
- 1：已被锁定。
        :type Locked: int
        :param _BackupSize: 内部字段，用户可忽略。
        :type BackupSize: int
        :param _FullBackup: 内部字段，用户可忽略。
        :type FullBackup: int
        :param _InstanceType: 内部字段，用户可忽略。
        :type InstanceType: int
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Region: 本地备份所在地域。
        :type Region: str
        :param _EndTime: 备份结束时间。
        :type EndTime: str
        :param _FileType: 备份文件类型。
        :type FileType: str
        :param _ExpireTime: 备份文件过期时间。
        :type ExpireTime: str
        """
        self._StartTime = None
        self._BackupId = None
        self._BackupType = None
        self._Status = None
        self._Remark = None
        self._Locked = None
        self._BackupSize = None
        self._FullBackup = None
        self._InstanceType = None
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._EndTime = None
        self._FileType = None
        self._ExpireTime = None

    @property
    def StartTime(self):
        r"""备份开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def BackupId(self):
        r"""备份任务ID。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupType(self):
        r"""备份类型。
- 1：凌晨系统发起的自动备份。
- 0：用户发起的手动备份。
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def Status(self):
        r"""备份状态。 
- 1：备份被其它流程锁定。
- 2：备份正常，没有被任何流程锁定。
- -1：备份已过期。
- 3：备份正在被导出。
- 4：备份导出成功。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        r"""备份的备注信息。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Locked(self):
        r"""备份是否被锁定。
- 0：未被锁定。
- 1：已被锁定。
        :rtype: int
        """
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def BackupSize(self):
        r"""内部字段，用户可忽略。
        :rtype: int
        """
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def FullBackup(self):
        r"""内部字段，用户可忽略。
        :rtype: int
        """
        return self._FullBackup

    @FullBackup.setter
    def FullBackup(self, FullBackup):
        self._FullBackup = FullBackup

    @property
    def InstanceType(self):
        r"""内部字段，用户可忽略。
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        r"""本地备份所在地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EndTime(self):
        r"""备份结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FileType(self):
        r"""备份文件类型。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def ExpireTime(self):
        r"""备份文件过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._BackupId = params.get("BackupId")
        self._BackupType = params.get("BackupType")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._Locked = params.get("Locked")
        self._BackupSize = params.get("BackupSize")
        self._FullBackup = params.get("FullBackup")
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._EndTime = params.get("EndTime")
        self._FileType = params.get("FileType")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisCommonInstanceList(AbstractModel):
    r"""单个实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _AppId: 用户APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。
        :type AppId: int
        :param _ProjectId: 实例所属项目 ID。
        :type ProjectId: int
        :param _Region: 实例接入区域。
        :type Region: str
        :param _Zone: 实例接入可用区。
        :type Zone: str
        :param _VpcId: 实例私有网络 ID。
        :type VpcId: str
        :param _SubnetId: 私有网络所属子网 ID。
        :type SubnetId: str
        :param _Status: 实例状态信息。
- 1-流程中。
- 2-运行中。
- -2-实例已隔离。
- -3-实例待回收。
- -4-实例已删除。
        :type Status: str
        :param _Vips: 实例私有网络 IP 地址。
        :type Vips: list of str
        :param _Vport: 实例网络端口。
        :type Vport: int
        :param _Createtime: 实例创建时间。
        :type Createtime: str
        :param _PayMode: 计费类型。
- 0：按量计费。
- 1：包年包月。
        :type PayMode: int
        :param _NetType: 网络类型。
- 0：基础网络。
- 1：VPC 网络。
        :type NetType: int
        """
        self._InstanceName = None
        self._InstanceId = None
        self._AppId = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._Vips = None
        self._Vport = None
        self._Createtime = None
        self._PayMode = None
        self._NetType = None

    @property
    def InstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AppId(self):
        r"""用户APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProjectId(self):
        r"""实例所属项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        r"""实例接入区域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""实例接入可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""实例私有网络 ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络所属子网 ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        r"""实例状态信息。
- 1-流程中。
- 2-运行中。
- -2-实例已隔离。
- -3-实例待回收。
- -4-实例已删除。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vips(self):
        r"""实例私有网络 IP 地址。
        :rtype: list of str
        """
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def Vport(self):
        r"""实例网络端口。
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Createtime(self):
        r"""实例创建时间。
        :rtype: str
        """
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def PayMode(self):
        r"""计费类型。
- 0：按量计费。
- 1：包年包月。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def NetType(self):
        r"""网络类型。
- 0：基础网络。
- 1：VPC 网络。
        :rtype: int
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._AppId = params.get("AppId")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._Vips = params.get("Vips")
        self._Vport = params.get("Vport")
        self._Createtime = params.get("Createtime")
        self._PayMode = params.get("PayMode")
        self._NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisInstanceEvent(AbstractModel):
    r"""实例事件信息

    """

    def __init__(self):
        r"""
        :param _ID: 事件 ID。
        :type ID: int
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Type: 事件类型，当前仅支持配置实例迁移、资源腾挪、机房裁撤相关的运维操作。该参数仅支持配置为 **InstanceMigration**。
        :type Type: str
        :param _Grade: 事件等级根据其影响严重程度和紧急程度进行分级，由重至轻依次为关键、重要、中等、一般。
- Critical：关键
- High：重要
- Middle：中等
- Low：一般
        :type Grade: str
        :param _ExecutionDate: 事件计划执行日期。
        :type ExecutionDate: str
        :param _StartTime: 事件计划执行开始时间。
        :type StartTime: str
        :param _EndTime: 事件计划执行结束时间。
        :type EndTime: str
        :param _LatestExecutionDate: 运维事件最迟执行的日期，即该事件必须在该日期之前完成，否则可能会对业务产生影响。
        :type LatestExecutionDate: str
        :param _Status: 事件当前状态。
- Waiting：未到达执行日期或不在维护时间窗内的事件。
- Running：在维护时间窗内，正在执行维护的事件。
- Finished：已全部完成维护的事件。
- Canceled：已取消执行的事件。
        :type Status: str
        :param _TaskEndTime: 事件执行任务完成时间。
        :type TaskEndTime: str
        :param _EffectInfo: 事件影响信息。
        :type EffectInfo: str
        :param _InitialExecutionDate: 事件最初计划执行日期。
        :type InitialExecutionDate: str
        """
        self._ID = None
        self._InstanceId = None
        self._InstanceName = None
        self._Type = None
        self._Grade = None
        self._ExecutionDate = None
        self._StartTime = None
        self._EndTime = None
        self._LatestExecutionDate = None
        self._Status = None
        self._TaskEndTime = None
        self._EffectInfo = None
        self._InitialExecutionDate = None

    @property
    def ID(self):
        r"""事件 ID。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Type(self):
        r"""事件类型，当前仅支持配置实例迁移、资源腾挪、机房裁撤相关的运维操作。该参数仅支持配置为 **InstanceMigration**。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Grade(self):
        r"""事件等级根据其影响严重程度和紧急程度进行分级，由重至轻依次为关键、重要、中等、一般。
- Critical：关键
- High：重要
- Middle：中等
- Low：一般
        :rtype: str
        """
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def ExecutionDate(self):
        r"""事件计划执行日期。
        :rtype: str
        """
        return self._ExecutionDate

    @ExecutionDate.setter
    def ExecutionDate(self, ExecutionDate):
        self._ExecutionDate = ExecutionDate

    @property
    def StartTime(self):
        r"""事件计划执行开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""事件计划执行结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def LatestExecutionDate(self):
        r"""运维事件最迟执行的日期，即该事件必须在该日期之前完成，否则可能会对业务产生影响。
        :rtype: str
        """
        return self._LatestExecutionDate

    @LatestExecutionDate.setter
    def LatestExecutionDate(self, LatestExecutionDate):
        self._LatestExecutionDate = LatestExecutionDate

    @property
    def Status(self):
        r"""事件当前状态。
- Waiting：未到达执行日期或不在维护时间窗内的事件。
- Running：在维护时间窗内，正在执行维护的事件。
- Finished：已全部完成维护的事件。
- Canceled：已取消执行的事件。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskEndTime(self):
        r"""事件执行任务完成时间。
        :rtype: str
        """
        return self._TaskEndTime

    @TaskEndTime.setter
    def TaskEndTime(self, TaskEndTime):
        self._TaskEndTime = TaskEndTime

    @property
    def EffectInfo(self):
        r"""事件影响信息。
        :rtype: str
        """
        return self._EffectInfo

    @EffectInfo.setter
    def EffectInfo(self, EffectInfo):
        self._EffectInfo = EffectInfo

    @property
    def InitialExecutionDate(self):
        r"""事件最初计划执行日期。
        :rtype: str
        """
        return self._InitialExecutionDate

    @InitialExecutionDate.setter
    def InitialExecutionDate(self, InitialExecutionDate):
        self._InitialExecutionDate = InitialExecutionDate


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Type = params.get("Type")
        self._Grade = params.get("Grade")
        self._ExecutionDate = params.get("ExecutionDate")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._LatestExecutionDate = params.get("LatestExecutionDate")
        self._Status = params.get("Status")
        self._TaskEndTime = params.get("TaskEndTime")
        self._EffectInfo = params.get("EffectInfo")
        self._InitialExecutionDate = params.get("InitialExecutionDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNode(AbstractModel):
    r"""Redis节点的运行信息

    """

    def __init__(self):
        r"""
        :param _Keys: Redis 节点上 Key 的个数。
        :type Keys: int
        :param _Slot: Redis 节点 Slot 分布范围。例如：0-5460。
        :type Slot: str
        :param _NodeId: 节点的序列 ID。
        :type NodeId: str
        :param _Status: 节点的状态。
        :type Status: str
        :param _Role: 节点角色。
        :type Role: str
        """
        self._Keys = None
        self._Slot = None
        self._NodeId = None
        self._Status = None
        self._Role = None

    @property
    def Keys(self):
        r"""Redis 节点上 Key 的个数。
        :rtype: int
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Slot(self):
        r"""Redis 节点 Slot 分布范围。例如：0-5460。
        :rtype: str
        """
        return self._Slot

    @Slot.setter
    def Slot(self, Slot):
        self._Slot = Slot

    @property
    def NodeId(self):
        r"""节点的序列 ID。
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Status(self):
        r"""节点的状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Role(self):
        r"""节点角色。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._Keys = params.get("Keys")
        self._Slot = params.get("Slot")
        self._NodeId = params.get("NodeId")
        self._Status = params.get("Status")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodeInfo(AbstractModel):
    r"""描述 Redis 实例的主节点或者副本节点信息。

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型。<ul><li>0：为主节点。</li><li>1：为副本节点。</li></ul>
        :type NodeType: int
        :param _NodeId: 主节点或者副本节点的 ID。<ul><li>该参数用于创建 Redis 实例接口[CreateInstances](https://cloud.tencent.com/document/product/239/20026) 并不需要设置，而用于变更实例配置的接口 [UpgradeInstance](https://cloud.tencent.com/document/product/239/20013) 删除副本时才需要设置。</li><li>该参数可使用接口 [DescribeInstances](https://cloud.tencent.com/document/product/239/20018) 获取Integer类型的节点 ID。</li></ul>
        :type NodeId: int
        :param _ZoneId: 主节点或者副本节点的可用区 ID。
        :type ZoneId: int
        :param _ZoneName: 主节点或者副本节点的可用区名称。
        :type ZoneName: str
        """
        self._NodeType = None
        self._NodeId = None
        self._ZoneId = None
        self._ZoneName = None

    @property
    def NodeType(self):
        r"""节点类型。<ul><li>0：为主节点。</li><li>1：为副本节点。</li></ul>
        :rtype: int
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeId(self):
        r"""主节点或者副本节点的 ID。<ul><li>该参数用于创建 Redis 实例接口[CreateInstances](https://cloud.tencent.com/document/product/239/20026) 并不需要设置，而用于变更实例配置的接口 [UpgradeInstance](https://cloud.tencent.com/document/product/239/20013) 删除副本时才需要设置。</li><li>该参数可使用接口 [DescribeInstances](https://cloud.tencent.com/document/product/239/20018) 获取Integer类型的节点 ID。</li></ul>
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def ZoneId(self):
        r"""主节点或者副本节点的可用区 ID。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""主节点或者副本节点的可用区名称。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeId = params.get("NodeId")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodes(AbstractModel):
    r"""Redis节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点 ID。
        :type NodeId: str
        :param _NodeRole: 节点角色。
        :type NodeRole: str
        :param _ClusterId: 分片 ID。
        :type ClusterId: int
        :param _ZoneId: 可用区 ID。
        :type ZoneId: int
        """
        self._NodeId = None
        self._NodeRole = None
        self._ClusterId = None
        self._ZoneId = None

    @property
    def NodeId(self):
        r"""节点 ID。
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeRole(self):
        r"""节点角色。
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def ClusterId(self):
        r"""分片 ID。
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ZoneId(self):
        r"""可用区 ID。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeRole = params.get("NodeRole")
        self._ClusterId = params.get("ClusterId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionConf(AbstractModel):
    r"""地域信息

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _RegionShortName: 地域简称
        :type RegionShortName: str
        :param _Area: 地域所在大区名称
        :type Area: str
        :param _ZoneSet: 可用区信息
        :type ZoneSet: list of ZoneCapacityConf
        """
        self._RegionId = None
        self._RegionName = None
        self._RegionShortName = None
        self._Area = None
        self._ZoneSet = None

    @property
    def RegionId(self):
        r"""地域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""地域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionShortName(self):
        r"""地域简称
        :rtype: str
        """
        return self._RegionShortName

    @RegionShortName.setter
    def RegionShortName(self, RegionShortName):
        self._RegionShortName = RegionShortName

    @property
    def Area(self):
        r"""地域所在大区名称
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ZoneSet(self):
        r"""可用区信息
        :rtype: list of ZoneCapacityConf
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RegionShortName = params.get("RegionShortName")
        self._Area = params.get("Area")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneCapacityConf()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseWanAddressRequest(AbstractModel):
    r"""ReleaseWanAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseWanAddressResponse(AbstractModel):
    r"""ReleaseWanAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _WanStatus: 关闭外网的状态
        :type WanStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._WanStatus = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""异步流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def WanStatus(self):
        r"""关闭外网的状态
        :rtype: str
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

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
        self._WanStatus = params.get("WanStatus")
        self._RequestId = params.get("RequestId")


class RemoveReplicationGroupRequest(AbstractModel):
    r"""RemoveReplicationGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID。请登录 [Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication) 页面获取复制组 ID。
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        r"""复制组ID。请登录 [Redis控制台的全球复制](https://console.cloud.tencent.com/redis/replication) 页面获取复制组 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveReplicationGroupResponse(AbstractModel):
    r"""RemoveReplicationGroup返回参数结构体

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


class RemoveReplicationInstanceRequest(AbstractModel):
    r"""RemoveReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组 ID。例如：crs-rpl-m3zt****。请登录[Redis 控制台](https://console.cloud.tencent.com/redis/replication)的全球复制组列表获取复制组 ID。

        :type GroupId: str
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _SyncType: 数据同步类型。
- true：需数据强同步。
- false：无需强同步，仅限删除主实例。
        :type SyncType: bool
        """
        self._GroupId = None
        self._InstanceId = None
        self._SyncType = None

    @property
    def GroupId(self):
        r"""复制组 ID。例如：crs-rpl-m3zt****。请登录[Redis 控制台](https://console.cloud.tencent.com/redis/replication)的全球复制组列表获取复制组 ID。

        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SyncType(self):
        r"""数据同步类型。
- true：需数据强同步。
- false：无需强同步，仅限删除主实例。
        :rtype: bool
        """
        return self._SyncType

    @SyncType.setter
    def SyncType(self, SyncType):
        self._SyncType = SyncType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._InstanceId = params.get("InstanceId")
        self._SyncType = params.get("SyncType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveReplicationInstanceResponse(AbstractModel):
    r"""RemoveReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
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


class RenewInstanceRequest(AbstractModel):
    r"""RenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 购买时长。
- 单位：月。
- 取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :type Period: int
        :param _InstanceId: 实例 ID，请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _ModifyPayMode: 标识是否修改计费模式。
- 当前实例计费模式为按量计费方式，预转换为包年包月而续费，请指定该参数为 <b>prepaid</b>。
- 当前实例计费模式为包年包月方式，可不设置该参数。
        :type ModifyPayMode: str
        """
        self._Period = None
        self._InstanceId = None
        self._ModifyPayMode = None

    @property
    def Period(self):
        r"""购买时长。
- 单位：月。
- 取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceId(self):
        r"""实例 ID，请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ModifyPayMode(self):
        r"""标识是否修改计费模式。
- 当前实例计费模式为按量计费方式，预转换为包年包月而续费，请指定该参数为 <b>prepaid</b>。
- 当前实例计费模式为包年包月方式，可不设置该参数。
        :rtype: str
        """
        return self._ModifyPayMode

    @ModifyPayMode.setter
    def ModifyPayMode(self, ModifyPayMode):
        self._ModifyPayMode = ModifyPayMode


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._InstanceId = params.get("InstanceId")
        self._ModifyPayMode = params.get("ModifyPayMode")
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
        :param _DealId: 交易ID。
        :type DealId: str
        :param _DealName: 订单号。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._DealName = None
        self._RequestId = None

    @property
    def DealId(self):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        r"""交易ID。
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        self._DealId = DealId

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
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ReplicaGroup(AbstractModel):
    r"""实例节点组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 节点组 ID。
        :type GroupId: int
        :param _GroupName: 节点组的名称，主节点为空。
        :type GroupName: str
        :param _ZoneId: 节点的可用区ID，比如ap-guangzhou-1
        :type ZoneId: str
        :param _Role: 节点组类型，master为主节点，replica为副本节点。
        :type Role: str
        :param _RedisNodes: 节点组节点列表
        :type RedisNodes: list of RedisNode
        """
        self._GroupId = None
        self._GroupName = None
        self._ZoneId = None
        self._Role = None
        self._RedisNodes = None

    @property
    def GroupId(self):
        r"""节点组 ID。
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""节点组的名称，主节点为空。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ZoneId(self):
        r"""节点的可用区ID，比如ap-guangzhou-1
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Role(self):
        r"""节点组类型，master为主节点，replica为副本节点。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RedisNodes(self):
        r"""节点组节点列表
        :rtype: list of RedisNode
        """
        return self._RedisNodes

    @RedisNodes.setter
    def RedisNodes(self, RedisNodes):
        self._RedisNodes = RedisNodes


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ZoneId = params.get("ZoneId")
        self._Role = params.get("Role")
        if params.get("RedisNodes") is not None:
            self._RedisNodes = []
            for item in params.get("RedisNodes"):
                obj = RedisNode()
                obj._deserialize(item)
                self._RedisNodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    r"""ResetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Password: 重置的密码。若切换为免密实例时，可不配置该参数。
- 长度8-32位, 推荐使用12位以上的密码。
- 不能以"/"开头。
- 至少包含小写字母a- z、大写字母A - Z、数字0 - 9、特殊字符 ()~!@#$%^&*-+=_|{}[]:;<>,.?/中的两项。
        :type Password: str
        :param _NoAuth: 是否切换免密实例。
- false：切换为非免密码实例。默认 false。
- true：切换为免密码实例。
        :type NoAuth: bool
        :param _EncryptPassword: 是否加密密码。
- false：非加密密码。默认 false。
- true：加密密码。
        :type EncryptPassword: bool
        """
        self._InstanceId = None
        self._Password = None
        self._NoAuth = None
        self._EncryptPassword = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        r"""重置的密码。若切换为免密实例时，可不配置该参数。
- 长度8-32位, 推荐使用12位以上的密码。
- 不能以"/"开头。
- 至少包含小写字母a- z、大写字母A - Z、数字0 - 9、特殊字符 ()~!@#$%^&*-+=_|{}[]:;<>,.?/中的两项。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NoAuth(self):
        r"""是否切换免密实例。
- false：切换为非免密码实例。默认 false。
- true：切换为免密码实例。
        :rtype: bool
        """
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def EncryptPassword(self):
        r"""是否加密密码。
- false：非加密密码。默认 false。
- true：加密密码。
        :rtype: bool
        """
        return self._EncryptPassword

    @EncryptPassword.setter
    def EncryptPassword(self, EncryptPassword):
        self._EncryptPassword = EncryptPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._NoAuth = params.get("NoAuth")
        self._EncryptPassword = params.get("EncryptPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    r"""ResetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID（修改密码时的任务ID，如果时切换免密码或者非免密码实例，则无需关注此返回值）
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID（修改密码时的任务ID，如果时切换免密码或者非免密码实例，则无需关注此返回值）
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


class ResourceBundle(AbstractModel):
    r"""redis独享集群资源包

    """

    def __init__(self):
        r"""
        :param _ResourceBundleName: 资源包名称
        :type ResourceBundleName: str
        :param _AvailableMemory: 可售卖内存，单位：GB
        :type AvailableMemory: int
        :param _Count: 资源包个数
        :type Count: int
        """
        self._ResourceBundleName = None
        self._AvailableMemory = None
        self._Count = None

    @property
    def ResourceBundleName(self):
        r"""资源包名称
        :rtype: str
        """
        return self._ResourceBundleName

    @ResourceBundleName.setter
    def ResourceBundleName(self, ResourceBundleName):
        self._ResourceBundleName = ResourceBundleName

    @property
    def AvailableMemory(self):
        r"""可售卖内存，单位：GB
        :rtype: int
        """
        return self._AvailableMemory

    @AvailableMemory.setter
    def AvailableMemory(self, AvailableMemory):
        self._AvailableMemory = AvailableMemory

    @property
    def Count(self):
        r"""资源包个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._ResourceBundleName = params.get("ResourceBundleName")
        self._AvailableMemory = params.get("AvailableMemory")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTag(AbstractModel):
    r"""API购买实例绑定标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签Key。
        :type TagKey: str
        :param _TagValue: 标签 Key 对应的 Value。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签Key。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签 Key 对应的 Value。
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
        


class RestoreInstanceRequest(AbstractModel):
    r"""RestoreInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待操作的实例ID，可通过 [DescribeInstances](https://cloud.tencent.com/document/product/239/20018) 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _BackupId: 备份ID，可通过 [DescribeInstanceBackups](https://cloud.tencent.com/document/product/239/20011) 接口返回的参数 RedisBackupSet 获取。
        :type BackupId: str
        :param _Password: 实例密码，恢复实例时，需要校验实例密码（免密实例不需要传密码）
        :type Password: str
        """
        self._InstanceId = None
        self._BackupId = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""待操作的实例ID，可通过 [DescribeInstances](https://cloud.tencent.com/document/product/239/20018) 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        r"""备份ID，可通过 [DescribeInstanceBackups](https://cloud.tencent.com/document/product/239/20011) 接口返回的参数 RedisBackupSet 获取。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def Password(self):
        r"""实例密码，恢复实例时，需要校验实例密码（免密实例不需要传密码）
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreInstanceResponse(AbstractModel):
    r"""RestoreInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可通过 DescribeTaskInfo 接口查询任务执行状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID，可通过 DescribeTaskInfo 接口查询任务执行状态
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


class SecondLevelBackupMissingTimestamps(AbstractModel):
    r"""秒级备份不存在的时间戳范围

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 开始时间戳
        :type StartTimeStamp: int
        :param _EndTimeStamp: 结束时间戳
        :type EndTimeStamp: int
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None

    @property
    def StartTimeStamp(self):
        r"""开始时间戳
        :rtype: int
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        r"""结束时间戳
        :rtype: int
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    r"""安全组规则

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss。
        :type CreateTime: str
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称。
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组备注。
        :type SecurityGroupRemark: str
        :param _Outbound: 出站规则。
        :type Outbound: list of Outbound
        :param _Inbound: 入站规则。
        :type Inbound: list of Inbound
        """
        self._CreateTime = None
        self._ProjectId = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Outbound = None
        self._Inbound = None

    @property
    def CreateTime(self):
        r"""创建时间，时间格式：yyyy-mm-dd hh:mm:ss。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def SecurityGroupId(self):
        r"""安全组ID。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        r"""安全组名称。
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        r"""安全组备注。
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Outbound(self):
        r"""出站规则。
        :rtype: list of Outbound
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def Inbound(self):
        r"""入站规则。
        :rtype: list of Inbound
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupDetail(AbstractModel):
    r"""安全组详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _CreateTime: 创建安全组的时间。
        :type CreateTime: str
        :param _SecurityGroupId: 安全组 ID。
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称。
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组标记。
        :type SecurityGroupRemark: str
        :param _InboundRule: 安全组入站规则，即控制访问数据库的来源。
        :type InboundRule: list of SecurityGroupsInboundAndOutbound
        :param _OutboundRule: 安全组出站规则。
        :type OutboundRule: list of SecurityGroupsInboundAndOutbound
        """
        self._ProjectId = None
        self._CreateTime = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._InboundRule = None
        self._OutboundRule = None

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
    def CreateTime(self):
        r"""创建安全组的时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityGroupId(self):
        r"""安全组 ID。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        r"""安全组名称。
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        r"""安全组标记。
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def InboundRule(self):
        r"""安全组入站规则，即控制访问数据库的来源。
        :rtype: list of SecurityGroupsInboundAndOutbound
        """
        return self._InboundRule

    @InboundRule.setter
    def InboundRule(self, InboundRule):
        self._InboundRule = InboundRule

    @property
    def OutboundRule(self):
        r"""安全组出站规则。
        :rtype: list of SecurityGroupsInboundAndOutbound
        """
        return self._OutboundRule

    @OutboundRule.setter
    def OutboundRule(self, OutboundRule):
        self._OutboundRule = OutboundRule


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("InboundRule") is not None:
            self._InboundRule = []
            for item in params.get("InboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self._InboundRule.append(obj)
        if params.get("OutboundRule") is not None:
            self._OutboundRule = []
            for item in params.get("OutboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self._OutboundRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupsInboundAndOutbound(AbstractModel):
    r"""安全组出入规则

    """

    def __init__(self):
        r"""
        :param _Action: 标识出入数据库的IP与端口是否被允许。
- ACCEPT：允许。
- DROP：不允许。
        :type Action: str
        :param _Ip: 出入数据库的IP地址
        :type Ip: str
        :param _Port: 端口号。
        :type Port: str
        :param _Proto: 协议类型。
        :type Proto: str
        """
        self._Action = None
        self._Ip = None
        self._Port = None
        self._Proto = None

    @property
    def Action(self):
        r"""标识出入数据库的IP与端口是否被允许。
- ACCEPT：允许。
- DROP：不允许。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Ip(self):
        r"""出入数据库的IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""端口号。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Proto(self):
        r"""协议类型。
        :rtype: str
        """
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Proto = params.get("Proto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceCommand(AbstractModel):
    r"""访问命令

    """

    def __init__(self):
        r"""
        :param _Cmd: 命令名称。
        :type Cmd: str
        :param _Count: 执行次数。
        :type Count: int
        """
        self._Cmd = None
        self._Count = None

    @property
    def Cmd(self):
        r"""命令名称。
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Count(self):
        r"""执行次数。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceInfo(AbstractModel):
    r"""访问来源信息

    """

    def __init__(self):
        r"""
        :param _Ip: 来源 IP 地址。
        :type Ip: str
        :param _Conn: 客户端连接数量。
        :type Conn: int
        :param _Cmd: 命令
        :type Cmd: int
        """
        self._Ip = None
        self._Conn = None
        self._Cmd = None

    @property
    def Ip(self):
        r"""来源 IP 地址。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Conn(self):
        r"""客户端连接数量。
        :rtype: int
        """
        return self._Conn

    @Conn.setter
    def Conn(self, Conn):
        self._Conn = Conn

    @property
    def Cmd(self):
        r"""命令
        :rtype: int
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Conn = params.get("Conn")
        self._Cmd = params.get("Cmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartupInstanceRequest(AbstractModel):
    r"""StartupInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在回收站复制需解隔离的实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在回收站复制需解隔离的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartupInstanceResponse(AbstractModel):
    r"""StartupInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 该字段已废弃，请通过查询实例接口获取到的状态来判断实例是否已解隔离
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        warnings.warn("parameter `TaskId` is deprecated", DeprecationWarning) 

        r"""该字段已废弃，请通过查询实例接口获取到的状态来判断实例是否已解隔离
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        warnings.warn("parameter `TaskId` is deprecated", DeprecationWarning) 

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


class SwitchAccessNewInstanceRequest(AbstractModel):
    r"""SwitchAccessNewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
示例值：crs-asdasdas
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
示例值：crs-asdasdas
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchAccessNewInstanceResponse(AbstractModel):
    r"""SwitchAccessNewInstance返回参数结构体

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


class SwitchInstanceVipRequest(AbstractModel):
    r"""SwitchInstanceVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcInstanceId: 源实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type SrcInstanceId: str
        :param _DstInstanceId: 目标实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type DstInstanceId: str
        :param _TimeDelay: 单位为秒。源实例与目标实例间DTS已断开时间。如果 DTS 断开时间大于TimeDelay，则不切换VIP，建议尽量根据业务设置一个可接受的值。
        :type TimeDelay: int
        :param _ForceSwitch: 在 DTS 断开的情况下是否强制切换。
- 1：强制切换。
- 0：不强制切换。
        :type ForceSwitch: int
        :param _SwitchTime: now: 立即切换，syncComplete：等待同步完成后切换
        :type SwitchTime: str
        """
        self._SrcInstanceId = None
        self._DstInstanceId = None
        self._TimeDelay = None
        self._ForceSwitch = None
        self._SwitchTime = None

    @property
    def SrcInstanceId(self):
        r"""源实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def DstInstanceId(self):
        r"""目标实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._DstInstanceId

    @DstInstanceId.setter
    def DstInstanceId(self, DstInstanceId):
        self._DstInstanceId = DstInstanceId

    @property
    def TimeDelay(self):
        r"""单位为秒。源实例与目标实例间DTS已断开时间。如果 DTS 断开时间大于TimeDelay，则不切换VIP，建议尽量根据业务设置一个可接受的值。
        :rtype: int
        """
        return self._TimeDelay

    @TimeDelay.setter
    def TimeDelay(self, TimeDelay):
        self._TimeDelay = TimeDelay

    @property
    def ForceSwitch(self):
        r"""在 DTS 断开的情况下是否强制切换。
- 1：强制切换。
- 0：不强制切换。
        :rtype: int
        """
        return self._ForceSwitch

    @ForceSwitch.setter
    def ForceSwitch(self, ForceSwitch):
        self._ForceSwitch = ForceSwitch

    @property
    def SwitchTime(self):
        r"""now: 立即切换，syncComplete：等待同步完成后切换
        :rtype: str
        """
        return self._SwitchTime

    @SwitchTime.setter
    def SwitchTime(self, SwitchTime):
        self._SwitchTime = SwitchTime


    def _deserialize(self, params):
        self._SrcInstanceId = params.get("SrcInstanceId")
        self._DstInstanceId = params.get("DstInstanceId")
        self._TimeDelay = params.get("TimeDelay")
        self._ForceSwitch = params.get("ForceSwitch")
        self._SwitchTime = params.get("SwitchTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchInstanceVipResponse(AbstractModel):
    r"""SwitchInstanceVip返回参数结构体

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


class SwitchProxyRequest(AbstractModel):
    r"""SwitchProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _ProxyID: 实例 ProxyID，请通过接口[DescribeInstanceNodeInfo](https://cloud.tencent.com/document/product/239/48603)的返回参数**Proxy**中的**NodeId**获取。  
        :type ProxyID: str
        :param _ProxyIDList: 实例 ProxyID列表，请通过接口[DescribeInstanceNodeInfo](https://cloud.tencent.com/document/product/239/48603)的返回参数**Proxy**中的**NodeId**获取。
        :type ProxyIDList: list of str
        """
        self._InstanceId = None
        self._ProxyID = None
        self._ProxyIDList = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyID(self):
        r"""实例 ProxyID，请通过接口[DescribeInstanceNodeInfo](https://cloud.tencent.com/document/product/239/48603)的返回参数**Proxy**中的**NodeId**获取。  
        :rtype: str
        """
        return self._ProxyID

    @ProxyID.setter
    def ProxyID(self, ProxyID):
        self._ProxyID = ProxyID

    @property
    def ProxyIDList(self):
        r"""实例 ProxyID列表，请通过接口[DescribeInstanceNodeInfo](https://cloud.tencent.com/document/product/239/48603)的返回参数**Proxy**中的**NodeId**获取。
        :rtype: list of str
        """
        return self._ProxyIDList

    @ProxyIDList.setter
    def ProxyIDList(self, ProxyIDList):
        self._ProxyIDList = ProxyIDList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyID = params.get("ProxyID")
        self._ProxyIDList = params.get("ProxyIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchProxyResponse(AbstractModel):
    r"""SwitchProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

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


class TaskInfoDetail(AbstractModel):
    r"""任务信息详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _TaskType: 任务类型。
- FLOW_CREATE: "001"，新建实例
- FLOW_RESIZE ： "002"，配置变更
- FLOW_CLOSE："003"，关闭实例
- FLOW_CLEAN： "004"，清空实例
- FLOW_STARTUP："005"，实例启用。
- FLOW_DELETE："006"，删除实例。
- FLOW_SETPWD："007"，重置密码。
- FLOW_EXPORTBACKUP："009"，导出备份文件。
- FLOW_RESTOREBACKUP："010"，恢复备份。
- FLOW_BACKUPINSTANCE："012"，备份实例。
- FLOW_MIGRATEINSTANCE："013"，迁移实例。
- FLOW_DELBACKUP："014"，删除备份。
- FLOW_EXCHANGEINSTANCE： "016"，切换实例流程。
- FLOW_AUTOBACKUP："017"，自动备份实例。
- FLOW_MIGRATECHECK： "022"，迁移参数校验。
- FLOW_MIGRATETASK："023"，数据迁移中。
- FLOW_CLEANDB："025"，清空数据库。
- FLOW_CLONEBACKUP："026"，克隆备份。
- FLOW_CHANGEVIP： "027"，改变vip地址。
- FLOW_EXPORSHR ："028"，扩缩容。
- FLOW_ADDNODES："029"，加（减）节点。
- FLOW_CHANGENET："031"，改变网络类型。
- FLOW_MODIFYINSTACEREADONLY："033"，只读策略变更。
- FLOW_MODIFYINSTANCEPARAMS："034"，修改实例参数。
- FLOW_MODIFYINSTANCEPASSWORDFREE："035"，设置免密。
- FLOW_SWITCHINSTANCEVIP："036"，实例VIP切换。
- FLOW_MODIFYINSTANCEACCOUNT："037"，实例账号变更。
- FLOW_MODIFYINSTANCEBANDWIDTH："038"，实例带宽变更。
- FLOW_ENABLEINSTANCE_REPLICATE："039"，开启副本只读。
- FLOW_DISABLEINSTANCE_REPLICATE："040"，关闭副本只读。
- FLOW_UpgradeArch："041"，实例架构升级，主从升集群。
- FLOW_DowngradeArch： "042"，实例架构降级，集群降主从。
- FLOW_UpgradeVersion： "043"，版本升级。
- FLOW_MODIFYCONNECTIONCONFIG："044"，带宽连接数调整。
- FLOW_CLEARNETWORK："045"，更换网络，
- FLOW_REMOVE_BACKUP_FILE："046"，删除备份。
- FLOW_UPGRADE_SUPPORT_MULTI_AZ："047"，升级实例支持多可用区。
- FLOW_SHUTDOWN_MASTER："048"，模拟故障。
- FLOW_CHANGE_REPLICA_TO_MASTER："049"，手动提主。
- FLOW_CODE_ADD_REPLICATION_INSTANCE："050"，新增复制组。
- FLOW_OPEN_WAN："052"，开通外网。
- FLOW_CLOSE_WAN："053"，关闭外网
- FLOW_CODE_DELETE_REPLICATION_INSTANCE："055"，解绑复制组。
- FLOW_CODE_CHANGE_MASTER_INSTANCE："056"，复制组实例切主。
- FLOW_CODE_CHANGE_INSTANCE_ROLE： "057"，更改复制组实例角色。
- FLOW_MIGRATE_NODE："058"，迁移节点。
- FLOW_SWITCH_NODE："059"，切换节点。
- FLOW_UPGRADE_SMALL_VERSION："060"，升级 Redis版本。
- FLOW_UPGRADE_PROXY_VERSION："061"，升级 Proxy 版本。
- FLOW_MODIFY_INSTANCE_NETWORK： "062"，实例修改网络。
- FLOW_MIGRATE_PROXY_NODE："063"，迁移 proxy节点。
- FLOW_MIGRATION_INSTANCE_ZONE："066"，实例可用区迁移中。
- FLOW_UPGRADE_INSTANCE_CACHE_AND_PROXY： "067"，实例版本升级中。
- FLOW_MODIFY_PROXY_NUM："069"，加（减）Proxy 节点。
- FLOW_MODIFYBACKUPMOD："070"，变更实例备份模式。
        :type TaskType: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _Progress: 任务进度。
        :type Progress: float
        :param _EndTime: 任务执行结束时间。
        :type EndTime: str
        :param _Result: 任务执行状态。

0：任务初始化。
1：执行中。
2：完成。
4：失败。
        :type Result: int
        """
        self._TaskId = None
        self._StartTime = None
        self._TaskType = None
        self._InstanceName = None
        self._InstanceId = None
        self._ProjectId = None
        self._Progress = None
        self._EndTime = None
        self._Result = None

    @property
    def TaskId(self):
        r"""任务 ID。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def StartTime(self):
        r"""任务开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskType(self):
        r"""任务类型。
- FLOW_CREATE: "001"，新建实例
- FLOW_RESIZE ： "002"，配置变更
- FLOW_CLOSE："003"，关闭实例
- FLOW_CLEAN： "004"，清空实例
- FLOW_STARTUP："005"，实例启用。
- FLOW_DELETE："006"，删除实例。
- FLOW_SETPWD："007"，重置密码。
- FLOW_EXPORTBACKUP："009"，导出备份文件。
- FLOW_RESTOREBACKUP："010"，恢复备份。
- FLOW_BACKUPINSTANCE："012"，备份实例。
- FLOW_MIGRATEINSTANCE："013"，迁移实例。
- FLOW_DELBACKUP："014"，删除备份。
- FLOW_EXCHANGEINSTANCE： "016"，切换实例流程。
- FLOW_AUTOBACKUP："017"，自动备份实例。
- FLOW_MIGRATECHECK： "022"，迁移参数校验。
- FLOW_MIGRATETASK："023"，数据迁移中。
- FLOW_CLEANDB："025"，清空数据库。
- FLOW_CLONEBACKUP："026"，克隆备份。
- FLOW_CHANGEVIP： "027"，改变vip地址。
- FLOW_EXPORSHR ："028"，扩缩容。
- FLOW_ADDNODES："029"，加（减）节点。
- FLOW_CHANGENET："031"，改变网络类型。
- FLOW_MODIFYINSTACEREADONLY："033"，只读策略变更。
- FLOW_MODIFYINSTANCEPARAMS："034"，修改实例参数。
- FLOW_MODIFYINSTANCEPASSWORDFREE："035"，设置免密。
- FLOW_SWITCHINSTANCEVIP："036"，实例VIP切换。
- FLOW_MODIFYINSTANCEACCOUNT："037"，实例账号变更。
- FLOW_MODIFYINSTANCEBANDWIDTH："038"，实例带宽变更。
- FLOW_ENABLEINSTANCE_REPLICATE："039"，开启副本只读。
- FLOW_DISABLEINSTANCE_REPLICATE："040"，关闭副本只读。
- FLOW_UpgradeArch："041"，实例架构升级，主从升集群。
- FLOW_DowngradeArch： "042"，实例架构降级，集群降主从。
- FLOW_UpgradeVersion： "043"，版本升级。
- FLOW_MODIFYCONNECTIONCONFIG："044"，带宽连接数调整。
- FLOW_CLEARNETWORK："045"，更换网络，
- FLOW_REMOVE_BACKUP_FILE："046"，删除备份。
- FLOW_UPGRADE_SUPPORT_MULTI_AZ："047"，升级实例支持多可用区。
- FLOW_SHUTDOWN_MASTER："048"，模拟故障。
- FLOW_CHANGE_REPLICA_TO_MASTER："049"，手动提主。
- FLOW_CODE_ADD_REPLICATION_INSTANCE："050"，新增复制组。
- FLOW_OPEN_WAN："052"，开通外网。
- FLOW_CLOSE_WAN："053"，关闭外网
- FLOW_CODE_DELETE_REPLICATION_INSTANCE："055"，解绑复制组。
- FLOW_CODE_CHANGE_MASTER_INSTANCE："056"，复制组实例切主。
- FLOW_CODE_CHANGE_INSTANCE_ROLE： "057"，更改复制组实例角色。
- FLOW_MIGRATE_NODE："058"，迁移节点。
- FLOW_SWITCH_NODE："059"，切换节点。
- FLOW_UPGRADE_SMALL_VERSION："060"，升级 Redis版本。
- FLOW_UPGRADE_PROXY_VERSION："061"，升级 Proxy 版本。
- FLOW_MODIFY_INSTANCE_NETWORK： "062"，实例修改网络。
- FLOW_MIGRATE_PROXY_NODE："063"，迁移 proxy节点。
- FLOW_MIGRATION_INSTANCE_ZONE："066"，实例可用区迁移中。
- FLOW_UPGRADE_INSTANCE_CACHE_AND_PROXY： "067"，实例版本升级中。
- FLOW_MODIFY_PROXY_NUM："069"，加（减）Proxy 节点。
- FLOW_MODIFYBACKUPMOD："070"，变更实例备份模式。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InstanceName(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProjectId(self):
        r"""项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Progress(self):
        r"""任务进度。
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def EndTime(self):
        r"""任务执行结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Result(self):
        r"""任务执行状态。

0：任务初始化。
1：执行中。
2：完成。
4：失败。
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._StartTime = params.get("StartTime")
        self._TaskType = params.get("TaskType")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._ProjectId = params.get("ProjectId")
        self._Progress = params.get("Progress")
        self._EndTime = params.get("EndTime")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisNodes(AbstractModel):
    r"""tendis节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID
        :type NodeId: str
        :param _NodeRole: 节点角色
        :type NodeRole: str
        :param _ZoneId: 可用区 ID。	
        :type ZoneId: int
        """
        self._NodeId = None
        self._NodeRole = None
        self._ZoneId = None

    @property
    def NodeId(self):
        r"""节点ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeRole(self):
        r"""节点角色
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def ZoneId(self):
        r"""可用区 ID。	
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeRole = params.get("NodeRole")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisSlowLogDetail(AbstractModel):
    r"""Tendis慢查询详情

    """

    def __init__(self):
        r"""
        :param _ExecuteTime: 执行时间
        :type ExecuteTime: str
        :param _Duration: 慢查询耗时（毫秒）
        :type Duration: int
        :param _Command: 命令
        :type Command: str
        :param _CommandLine: 详细命令行信息
        :type CommandLine: str
        :param _Node: 节点ID
        :type Node: str
        """
        self._ExecuteTime = None
        self._Duration = None
        self._Command = None
        self._CommandLine = None
        self._Node = None

    @property
    def ExecuteTime(self):
        r"""执行时间
        :rtype: str
        """
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime

    @property
    def Duration(self):
        r"""慢查询耗时（毫秒）
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Command(self):
        r"""命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        r"""详细命令行信息
        :rtype: str
        """
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def Node(self):
        r"""节点ID
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node


    def _deserialize(self, params):
        self._ExecuteTime = params.get("ExecuteTime")
        self._Duration = params.get("Duration")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeDealDetail(AbstractModel):
    r"""订单交易信息

    """

    def __init__(self):
        r"""
        :param _DealId: 订单号ID，调用云API时使用此ID
        :type DealId: str
        :param _DealName: 长订单ID，反馈订单问题给官方客服使用此ID
        :type DealName: str
        :param _ZoneId: 可用区id
        :type ZoneId: int
        :param _GoodsNum: 订单关联的实例数
        :type GoodsNum: int
        :param _Creater: 创建用户uin
        :type Creater: str
        :param _CreatTime: 订单创建时间
        :type CreatTime: str
        :param _OverdueTime: 订单超时时间
        :type OverdueTime: str
        :param _EndTime: 订单完成时间
        :type EndTime: str
        :param _Status: 订单状态 1：未支付 2:已支付，未发货 3:发货中 4:发货成功 5:发货失败 6:已退款 7:已关闭订单 8:订单过期 9:订单已失效 10:产品已失效 11:代付拒绝 12:支付中
        :type Status: int
        :param _Description: 订单状态描述
        :type Description: str
        :param _Price: 订单实际总价，单位：分
        :type Price: int
        :param _InstanceIds: 实例ID
        :type InstanceIds: list of str
        """
        self._DealId = None
        self._DealName = None
        self._ZoneId = None
        self._GoodsNum = None
        self._Creater = None
        self._CreatTime = None
        self._OverdueTime = None
        self._EndTime = None
        self._Status = None
        self._Description = None
        self._Price = None
        self._InstanceIds = None

    @property
    def DealId(self):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        r"""订单号ID，调用云API时使用此ID
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        self._DealId = DealId

    @property
    def DealName(self):
        r"""长订单ID，反馈订单问题给官方客服使用此ID
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def ZoneId(self):
        r"""可用区id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GoodsNum(self):
        r"""订单关联的实例数
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Creater(self):
        r"""创建用户uin
        :rtype: str
        """
        return self._Creater

    @Creater.setter
    def Creater(self, Creater):
        self._Creater = Creater

    @property
    def CreatTime(self):
        r"""订单创建时间
        :rtype: str
        """
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime

    @property
    def OverdueTime(self):
        r"""订单超时时间
        :rtype: str
        """
        return self._OverdueTime

    @OverdueTime.setter
    def OverdueTime(self, OverdueTime):
        self._OverdueTime = OverdueTime

    @property
    def EndTime(self):
        r"""订单完成时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""订单状态 1：未支付 2:已支付，未发货 3:发货中 4:发货成功 5:发货失败 6:已退款 7:已关闭订单 8:订单过期 9:订单已失效 10:产品已失效 11:代付拒绝 12:支付中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        r"""订单状态描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Price(self):
        r"""订单实际总价，单位：分
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def InstanceIds(self):
        r"""实例ID
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        self._ZoneId = params.get("ZoneId")
        self._GoodsNum = params.get("GoodsNum")
        self._Creater = params.get("Creater")
        self._CreatTime = params.get("CreatTime")
        self._OverdueTime = params.get("OverdueTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._Price = params.get("Price")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    r"""UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待变更实例 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _MemSize: 指实例每个分片内存变更后的大小。
- 单位 MB。
- 每次只能修改参数MemSize、RedisShardNum和RedisReplicasNum其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。
- 缩容时，缩容后的规格务必要大于等于使用容量的1.3倍，否则将执行失败。
        :type MemSize: int
        :param _RedisShardNum: 指实例变更后的分片数量。
- 标准架构不需要配置该参数，集群架构为必填参数。
- 集群架构，每次只能修改参数RedisShardNum、MemSize和RedisReplicasNum其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。
        :type RedisShardNum: int
        :param _RedisReplicasNum: 指实例变更后的副本数量。
- 每次只能修改参数 RedisReplicasNum、MemSize 和 RedisShardNum 其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。
- 多AZ实例修改副本时必须要传入 NodeSet。
        :type RedisReplicasNum: int
        :param _NodeSet: 多AZ实例，增加副本时的节点信息，包括副本的 ID 编号及可用区信息。非多AZ实例不需要配置该参数。
        :type NodeSet: list of RedisNodeInfo
        :param _SwitchOption: 切换时间。 
- 1：维护时间窗操作：指升级规格在设置的维护时间窗内执行。请通过接口[DescribeMaintenanceWindow](https://cloud.tencent.com/document/product/239/46336)查询设置的维护时间窗时间段。增减副本、增减分片、扩缩内存均支持在维护时间窗执行操作。维护时间窗升级规格正在分地域逐步测试发布中，部分区域已支持，未覆盖地域若需紧急接入，请[提交工单](https://console.cloud.tencent.com/workorder/category)申请白名单。
- 2：立即操作：操作将立即执行，无需等待维护时间窗。系统默认设置为立即操作。
        :type SwitchOption: int
        """
        self._InstanceId = None
        self._MemSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._NodeSet = None
        self._SwitchOption = None

    @property
    def InstanceId(self):
        r"""待变更实例 ID。请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MemSize(self):
        r"""指实例每个分片内存变更后的大小。
- 单位 MB。
- 每次只能修改参数MemSize、RedisShardNum和RedisReplicasNum其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。
- 缩容时，缩容后的规格务必要大于等于使用容量的1.3倍，否则将执行失败。
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def RedisShardNum(self):
        r"""指实例变更后的分片数量。
- 标准架构不需要配置该参数，集群架构为必填参数。
- 集群架构，每次只能修改参数RedisShardNum、MemSize和RedisReplicasNum其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。
        :rtype: int
        """
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        r"""指实例变更后的副本数量。
- 每次只能修改参数 RedisReplicasNum、MemSize 和 RedisShardNum 其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。
- 多AZ实例修改副本时必须要传入 NodeSet。
        :rtype: int
        """
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def NodeSet(self):
        r"""多AZ实例，增加副本时的节点信息，包括副本的 ID 编号及可用区信息。非多AZ实例不需要配置该参数。
        :rtype: list of RedisNodeInfo
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def SwitchOption(self):
        r"""切换时间。 
- 1：维护时间窗操作：指升级规格在设置的维护时间窗内执行。请通过接口[DescribeMaintenanceWindow](https://cloud.tencent.com/document/product/239/46336)查询设置的维护时间窗时间段。增减副本、增减分片、扩缩内存均支持在维护时间窗执行操作。维护时间窗升级规格正在分地域逐步测试发布中，部分区域已支持，未覆盖地域若需紧急接入，请[提交工单](https://console.cloud.tencent.com/workorder/category)申请白名单。
- 2：立即操作：操作将立即执行，无需等待维护时间窗。系统默认设置为立即操作。
        :rtype: int
        """
        return self._SwitchOption

    @SwitchOption.setter
    def SwitchOption(self, SwitchOption):
        self._SwitchOption = SwitchOption


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MemSize = params.get("MemSize")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._SwitchOption = params.get("SwitchOption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    r"""UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单ID。
        :type DealId: str
        :param _DealName: 订单号。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._DealName = None
        self._RequestId = None

    @property
    def DealId(self):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        r"""订单ID。
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        self._DealId = DealId

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
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class UpgradeInstanceVersionRequest(AbstractModel):
    r"""UpgradeInstanceVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetInstanceType: 目标实例类型，同 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的**TypeId**，即实例要变更的目标类型。
- Redis 4.0 及以上的版本，支持相同版本的实例从标准架构升级至集群架构，例如，支持 Redis 4.0 标准架构升级至 Redis 4.0 集群架构。
- 不支持跨版本架构升级，例如，Redis 4.0 标准架构升级至 Redis 5.0 集群架构。
- 不支持 Redis 2.8 版本升级架构。
- 不支持从集群架构降级至标准架构。

        :type TargetInstanceType: str
        :param _SwitchOption: 切换时间。
- 1：维护时间窗切换。
- 2：立即切换。
        :type SwitchOption: int
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****，请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._TargetInstanceType = None
        self._SwitchOption = None
        self._InstanceId = None

    @property
    def TargetInstanceType(self):
        r"""目标实例类型，同 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的**TypeId**，即实例要变更的目标类型。
- Redis 4.0 及以上的版本，支持相同版本的实例从标准架构升级至集群架构，例如，支持 Redis 4.0 标准架构升级至 Redis 4.0 集群架构。
- 不支持跨版本架构升级，例如，Redis 4.0 标准架构升级至 Redis 5.0 集群架构。
- 不支持 Redis 2.8 版本升级架构。
- 不支持从集群架构降级至标准架构。

        :rtype: str
        """
        return self._TargetInstanceType

    @TargetInstanceType.setter
    def TargetInstanceType(self, TargetInstanceType):
        self._TargetInstanceType = TargetInstanceType

    @property
    def SwitchOption(self):
        r"""切换时间。
- 1：维护时间窗切换。
- 2：立即切换。
        :rtype: int
        """
        return self._SwitchOption

    @SwitchOption.setter
    def SwitchOption(self, SwitchOption):
        self._SwitchOption = SwitchOption

    @property
    def InstanceId(self):
        r"""指定实例 ID。例如：crs-xjhsdj****，请登录[Redis控制台](https://console.cloud.tencent.com/redis#/)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._TargetInstanceType = params.get("TargetInstanceType")
        self._SwitchOption = params.get("SwitchOption")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceVersionResponse(AbstractModel):
    r"""UpgradeInstanceVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单ID
        :type DealId: str
        :param _DealName: 订单号。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._DealName = None
        self._RequestId = None

    @property
    def DealId(self):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        r"""订单ID
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        warnings.warn("parameter `DealId` is deprecated", DeprecationWarning) 

        self._DealId = DealId

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
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class UpgradeProxyVersionRequest(AbstractModel):
    r"""UpgradeProxyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _CurrentProxyVersion: 当前 Proxy 版本。请通过 [DescribeInstances](https://cloud.tencent.com/document/product/239/20018) 接口获取实例当前 Proxy 版本。
        :type CurrentProxyVersion: str
        :param _UpgradeProxyVersion: 可升级的 Redis 版本。请通过 [DescribeInstances](https://cloud.tencent.com/document/product/239/20018) 接口获取实例可升级的 Redis 版本。
        :type UpgradeProxyVersion: str
        :param _InstanceTypeUpgradeNow: 指定是否立即升级。
- 1：立即升级。
- 0：维护时间窗口升级。
        :type InstanceTypeUpgradeNow: int
        """
        self._InstanceId = None
        self._CurrentProxyVersion = None
        self._UpgradeProxyVersion = None
        self._InstanceTypeUpgradeNow = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CurrentProxyVersion(self):
        r"""当前 Proxy 版本。请通过 [DescribeInstances](https://cloud.tencent.com/document/product/239/20018) 接口获取实例当前 Proxy 版本。
        :rtype: str
        """
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def UpgradeProxyVersion(self):
        r"""可升级的 Redis 版本。请通过 [DescribeInstances](https://cloud.tencent.com/document/product/239/20018) 接口获取实例可升级的 Redis 版本。
        :rtype: str
        """
        return self._UpgradeProxyVersion

    @UpgradeProxyVersion.setter
    def UpgradeProxyVersion(self, UpgradeProxyVersion):
        self._UpgradeProxyVersion = UpgradeProxyVersion

    @property
    def InstanceTypeUpgradeNow(self):
        r"""指定是否立即升级。
- 1：立即升级。
- 0：维护时间窗口升级。
        :rtype: int
        """
        return self._InstanceTypeUpgradeNow

    @InstanceTypeUpgradeNow.setter
    def InstanceTypeUpgradeNow(self, InstanceTypeUpgradeNow):
        self._InstanceTypeUpgradeNow = InstanceTypeUpgradeNow


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._UpgradeProxyVersion = params.get("UpgradeProxyVersion")
        self._InstanceTypeUpgradeNow = params.get("InstanceTypeUpgradeNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeProxyVersionResponse(AbstractModel):
    r"""UpgradeProxyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""异步流程ID
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


class UpgradeSmallVersionRequest(AbstractModel):
    r"""UpgradeSmallVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _CurrentRedisVersion: 当前 Redis 小版本。小版本信息，请参见[升级实例版本](https://cloud.tencent.com/document/product/239/46457)。
        :type CurrentRedisVersion: str
        :param _UpgradeRedisVersion: 升级后的 Redis 小版本。小版本信息，请参见[升级实例版本](https://cloud.tencent.com/document/product/239/46457)。
        :type UpgradeRedisVersion: str
        :param _InstanceTypeUpgradeNow: 指定是否立即升级。
- 1：立即升级。
- 0：维护时间窗口升级。
        :type InstanceTypeUpgradeNow: int
        """
        self._InstanceId = None
        self._CurrentRedisVersion = None
        self._UpgradeRedisVersion = None
        self._InstanceTypeUpgradeNow = None

    @property
    def InstanceId(self):
        r"""实例 ID，请登录[Redis控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CurrentRedisVersion(self):
        r"""当前 Redis 小版本。小版本信息，请参见[升级实例版本](https://cloud.tencent.com/document/product/239/46457)。
        :rtype: str
        """
        return self._CurrentRedisVersion

    @CurrentRedisVersion.setter
    def CurrentRedisVersion(self, CurrentRedisVersion):
        self._CurrentRedisVersion = CurrentRedisVersion

    @property
    def UpgradeRedisVersion(self):
        r"""升级后的 Redis 小版本。小版本信息，请参见[升级实例版本](https://cloud.tencent.com/document/product/239/46457)。
        :rtype: str
        """
        return self._UpgradeRedisVersion

    @UpgradeRedisVersion.setter
    def UpgradeRedisVersion(self, UpgradeRedisVersion):
        self._UpgradeRedisVersion = UpgradeRedisVersion

    @property
    def InstanceTypeUpgradeNow(self):
        r"""指定是否立即升级。
- 1：立即升级。
- 0：维护时间窗口升级。
        :rtype: int
        """
        return self._InstanceTypeUpgradeNow

    @InstanceTypeUpgradeNow.setter
    def InstanceTypeUpgradeNow(self, InstanceTypeUpgradeNow):
        self._InstanceTypeUpgradeNow = InstanceTypeUpgradeNow


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CurrentRedisVersion = params.get("CurrentRedisVersion")
        self._UpgradeRedisVersion = params.get("UpgradeRedisVersion")
        self._InstanceTypeUpgradeNow = params.get("InstanceTypeUpgradeNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeSmallVersionResponse(AbstractModel):
    r"""UpgradeSmallVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""异步流程ID
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


class UpgradeVersionToMultiAvailabilityZonesRequest(AbstractModel):
    r"""UpgradeVersionToMultiAvailabilityZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _UpgradeProxyAndRedisServer: 升级多可用区之后是否支持就近访问功能。
- true：支持就近访问功能。升级过程，需同时升级 Proxy 版本和 Redis 内核小版本，涉及数据搬迁，可能会长达数小时。
- false：无需支持就近访问功能。升级多可用区仅涉及管理元数据迁移，对服务没有影响，升级过程通常在3分钟内完成。默认为 false。
        :type UpgradeProxyAndRedisServer: bool
        """
        self._InstanceId = None
        self._UpgradeProxyAndRedisServer = None

    @property
    def InstanceId(self):
        r"""实例ID，请登录 [Redis 控制台](https://console.cloud.tencent.com/redis/instance/list)在实例列表复制实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeProxyAndRedisServer(self):
        r"""升级多可用区之后是否支持就近访问功能。
- true：支持就近访问功能。升级过程，需同时升级 Proxy 版本和 Redis 内核小版本，涉及数据搬迁，可能会长达数小时。
- false：无需支持就近访问功能。升级多可用区仅涉及管理元数据迁移，对服务没有影响，升级过程通常在3分钟内完成。默认为 false。
        :rtype: bool
        """
        return self._UpgradeProxyAndRedisServer

    @UpgradeProxyAndRedisServer.setter
    def UpgradeProxyAndRedisServer(self, UpgradeProxyAndRedisServer):
        self._UpgradeProxyAndRedisServer = UpgradeProxyAndRedisServer


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpgradeProxyAndRedisServer = params.get("UpgradeProxyAndRedisServer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeVersionToMultiAvailabilityZonesResponse(AbstractModel):
    r"""UpgradeVersionToMultiAvailabilityZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""任务ID
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


class ZoneCapacityConf(AbstractModel):
    r"""可用区内产品信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区ID：如ap-guangzhou-3
        :type ZoneId: str
        :param _ZoneName: 可用区名称。
        :type ZoneName: str
        :param _IsSaleout: 可用区是否售罄。
        :type IsSaleout: bool
        :param _IsDefault: 是否为默认可用区。
        :type IsDefault: bool
        :param _NetWorkType: 网络类型。
- basenet：基础网络。
- vpcnet -- VPC网络。
        :type NetWorkType: list of str
        :param _ProductSet: 可用区内产品规格等信息
        :type ProductSet: list of ProductConf
        :param _OldZoneId: 可用区ID：如100003
        :type OldZoneId: int
        """
        self._ZoneId = None
        self._ZoneName = None
        self._IsSaleout = None
        self._IsDefault = None
        self._NetWorkType = None
        self._ProductSet = None
        self._OldZoneId = None

    @property
    def ZoneId(self):
        r"""可用区ID：如ap-guangzhou-3
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""可用区名称。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def IsSaleout(self):
        r"""可用区是否售罄。
        :rtype: bool
        """
        return self._IsSaleout

    @IsSaleout.setter
    def IsSaleout(self, IsSaleout):
        self._IsSaleout = IsSaleout

    @property
    def IsDefault(self):
        r"""是否为默认可用区。
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def NetWorkType(self):
        r"""网络类型。
- basenet：基础网络。
- vpcnet -- VPC网络。
        :rtype: list of str
        """
        return self._NetWorkType

    @NetWorkType.setter
    def NetWorkType(self, NetWorkType):
        self._NetWorkType = NetWorkType

    @property
    def ProductSet(self):
        r"""可用区内产品规格等信息
        :rtype: list of ProductConf
        """
        return self._ProductSet

    @ProductSet.setter
    def ProductSet(self, ProductSet):
        self._ProductSet = ProductSet

    @property
    def OldZoneId(self):
        r"""可用区ID：如100003
        :rtype: int
        """
        return self._OldZoneId

    @OldZoneId.setter
    def OldZoneId(self, OldZoneId):
        self._OldZoneId = OldZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._IsSaleout = params.get("IsSaleout")
        self._IsDefault = params.get("IsDefault")
        self._NetWorkType = params.get("NetWorkType")
        if params.get("ProductSet") is not None:
            self._ProductSet = []
            for item in params.get("ProductSet"):
                obj = ProductConf()
                obj._deserialize(item)
                self._ProductSet.append(obj)
        self._OldZoneId = params.get("OldZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        