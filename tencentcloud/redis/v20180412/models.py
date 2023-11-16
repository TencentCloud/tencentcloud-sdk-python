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


class Account(AbstractModel):
    """子账号信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _AccountName: 账号名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param _Remark: 账号描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Privilege: 读写权限策略。
- r：只读。
- w：只写。
- rw：读写。
注意：此字段可能返回 null，表示取不到有效值。
        :type Privilege: str
        :param _ReadonlyPolicy: 只读路由策略。
- master：主节点。
- replication：从节点。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadonlyPolicy: list of str
        :param _Status: 子账号状态.
- 1：账号变更中。
- 2：账号有效。
- 4：账号已删除。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._InstanceId = None
        self._AccountName = None
        self._Remark = None
        self._Privilege = None
        self._ReadonlyPolicy = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def ReadonlyPolicy(self):
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._Remark = params.get("Remark")
        self._Privilege = params.get("Privilege")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddReplicationInstanceRequest(AbstractModel):
    """AddReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID。
        :type GroupId: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceRole: 给复制组添加的实例分配角色。<ul><li>rw：可读写。</li><li>r：只读。</li></ul>
        :type InstanceRole: str
        """
        self._GroupId = None
        self._InstanceId = None
        self._InstanceRole = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRole(self):
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
    """AddReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class AllocateWanAddressRequest(AbstractModel):
    """AllocateWanAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """AllocateWanAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _WanStatus: 开通外网的状态
        :type WanStatus: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._WanStatus = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._WanStatus = params.get("WanStatus")
        self._RequestId = params.get("RequestId")


class ApplyParamsTemplateRequest(AbstractModel):
    """ApplyParamsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param _TemplateId: 应用的参数模板ID
        :type TemplateId: str
        """
        self._InstanceIds = None
        self._TemplateId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def TemplateId(self):
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
    """ApplyParamsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 任务ID
        :type TaskIds: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskIds = None
        self._RequestId = None

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        self._RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _SecurityGroupId: 要绑定的安全组ID，类似sg-efil73jd。
        :type SecurityGroupId: str
        :param _InstanceIds: 被绑定的实例ID，类似ins-lesecurk，支持指定多个实例。
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
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
    """AssociateSecurityGroups返回参数结构体

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


class BackupDownloadInfo(AbstractModel):
    """备份文件下载信息

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
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def InnerDownloadUrl(self):
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
    """已配置的备份文件下载地址对应的 VPC 信息。

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
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcList(self):
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
    """大Key详情

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
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
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
    """大Key类型分布详情

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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
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
        


class ChangeInstanceRoleRequest(AbstractModel):
    """ChangeInstanceRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID
        :type GroupId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceRole: 实例角色，rw可读写，r只读
        :type InstanceRole: str
        """
        self._GroupId = None
        self._InstanceId = None
        self._InstanceRole = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRole(self):
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
    """ChangeInstanceRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ChangeMasterInstanceRequest(AbstractModel):
    """ChangeMasterInstance请求参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForceSwitch(self):
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
    """ChangeMasterInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ChangeReplicaToMasterRequest(AbstractModel):
    """ChangeReplicaToMaster请求参数结构体

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupId(self):
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
    """ChangeReplicaToMaster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CleanUpInstanceRequest(AbstractModel):
    """CleanUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """CleanUpInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ClearInstanceRequest(AbstractModel):
    """ClearInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Password: redis的实例密码（免密实例不需要传密码，非免密实例必传）
        :type Password: str
        """
        self._InstanceId = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearInstanceResponse(AbstractModel):
    """ClearInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CloneInstancesRequest(AbstractModel):
    """CloneInstances请求参数结构体

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
        :param _SecurityGroupIdList: 安全组ID。请登录控制台，在<b>安全组</b>页面获取安全组 ID 信息。
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

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupIdList(self):
        return self._SecurityGroupIdList

    @SecurityGroupIdList.setter
    def SecurityGroupIdList(self, SecurityGroupIdList):
        self._SecurityGroupIdList = SecurityGroupIdList

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

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
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def AlarmPolicyList(self):
        return self._AlarmPolicyList

    @AlarmPolicyList.setter
    def AlarmPolicyList(self, AlarmPolicyList):
        self._AlarmPolicyList = AlarmPolicyList


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneInstancesResponse(AbstractModel):
    """CloneInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 请求任务 ID。
        :type DealId: str
        :param _InstanceIds: 克隆实例的 ID。
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CloseSSLRequest(AbstractModel):
    """CloseSSL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """CloseSSL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CommandTake(AbstractModel):
    """命令耗时

    """

    def __init__(self):
        r"""
        :param _Cmd: 命令
        :type Cmd: str
        :param _Took: 耗时
        :type Took: int
        """
        self._Cmd = None
        self._Took = None

    @property
    def Cmd(self):
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Took(self):
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
    """CreateInstanceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AccountName: 子账号名称
        :type AccountName: str
        :param _AccountPassword: 1.长度8-30位,推荐使用12位以上的密码
2.不能以"/"开头
3.至少包含两项
    a.小写字母a-z
    b.大写字母A-Z
    c.数字0-9
    d.()`~!@#$%^&*-+=_|{}[]:;<>,.?/
        :type AccountPassword: str
        :param _ReadonlyPolicy: 路由策略：填写master或者replication，表示主节点或者从节点
        :type ReadonlyPolicy: list of str
        :param _Privilege: 读写策略：填写r、rw，表示只读、读写
        :type Privilege: str
        :param _Remark: 子账号描述信息
        :type Remark: str
        """
        self._InstanceId = None
        self._AccountName = None
        self._AccountPassword = None
        self._ReadonlyPolicy = None
        self._Privilege = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def ReadonlyPolicy(self):
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Privilege = params.get("Privilege")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceAccountResponse(AbstractModel):
    """CreateInstanceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeId: 实例类型。
<ul><li>2：Redis 2.8 内存版（标准架构）。</li><li>3：CKV 3.2 内存版（标准架构）。</li><li>4：CKV 3.2 内存版（集群架构）。</li><li>6：Redis 4.0 内存版（标准架构）。</li><li>7：Redis 4.0 内存版（集群架构）。</li><li>8：Redis 5.0 内存版（标准架构）。</li><li>9：Redis 5.0 内存版（集群架构）。</li><li>15：Redis 6.2 内存版（标准架构）。</li><li>16：Redis 6.2 内存版（集群架构）。</li></ul>
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
- 当实例类型**TypeId**为Redis 2.8 内存版标准架构、Redis 4.0、5.0、6.0内存版标准架构或集群架构时，其密码复杂度要求为：8-30个字符，至少包含小写字母、大写字母、数字和字符()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种，不能以"/"开头。
- 当实例类型**TypeId**为CKV 3.2 内存版标准架构或集群架构时，其密码复杂度为：8-30个字符，必须包含字母和数字，且 不包含其他字符。
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
        :param _SecurityGroupIdList: 安全组 ID 数组。请通过[DescribeInstanceSecurityGroup](https://cloud.tencent.com/document/product/239/34447)接口获取实例的安全组 ID。
        :type SecurityGroupIdList: list of str
        :param _VPort: 用户自定义的网络端口。默认为6379，范围为 [1024,65535]。
        :type VPort: int
        :param _RedisShardNum: 实例分片数量。
- 标准版实例无需配置该参数。
- 集群版实例，分片数量范围为：[1、3、5、8、12、16、24、32、40、48、64、80、96、128]。
        :type RedisShardNum: int
        :param _RedisReplicasNum: 实例副本数量。
- Redis 内存版 4.0、5.0、6.2 标准架构和集群架构支持副本数量范围为[1,5]。
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
        :param _ProductVersion: 指定实例的产品版本。
- local：本地盘版。
- cloud：云盘版，
- cdc：独享集群版。如果不传默认发货为本地盘版本。
        :type ProductVersion: str
        :param _RedisClusterId: 独享集群 ID。当**ProductVersion**设置为**cdc**时，该参数必须设置。
        :type RedisClusterId: str
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

    @property
    def TypeId(self):
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def SecurityGroupIdList(self):
        return self._SecurityGroupIdList

    @SecurityGroupIdList.setter
    def SecurityGroupIdList(self, SecurityGroupIdList):
        self._SecurityGroupIdList = SecurityGroupIdList

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def ReplicasReadonly(self):
        return self._ReplicasReadonly

    @ReplicasReadonly.setter
    def ReplicasReadonly(self, ReplicasReadonly):
        self._ReplicasReadonly = ReplicasReadonly

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ProductVersion(self):
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def RedisClusterId(self):
        return self._RedisClusterId

    @RedisClusterId.setter
    def RedisClusterId(self, RedisClusterId):
        self._RedisClusterId = RedisClusterId


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 交易的ID。
        :type DealId: str
        :param _InstanceIds: 实例ID。
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 参数模板名称。
        :type Name: str
        :param _Description: 参数模板描述。
        :type Description: str
        :param _ProductType: 产品类型：1 – Redis2.8内存版（集群架构），2 – Redis2.8内存版（标准架构），3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，5 – Redis2.8内存版（单机），6 – Redis4.0内存版（标准架构），7 – Redis4.0内存版（集群架构），8 – Redis5.0内存版（标准架构），9 – Redis5.0内存版（集群架构）。创建模板时必填，从源模板复制则不需要传入该参数。
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ParamList(self):
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
    """CreateParamTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板 ID。
        :type TemplateId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateReplicationGroupRequest(AbstractModel):
    """CreateReplicationGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定复制组中的主实例ID。
        :type InstanceId: str
        :param _GroupName: 复制组名称。名称只支持长度为2-64个字符的中文、英文、数字、下划线_、分隔符-。
        :type GroupName: str
        :param _Remark: 备注信息。
        :type Remark: str
        """
        self._InstanceId = None
        self._GroupName = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Remark(self):
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
    """CreateReplicationGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DelayDistribution(AbstractModel):
    """延时分布详情

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
        return self._Ladder

    @Ladder.setter
    def Ladder(self, Ladder):
        self._Ladder = Ladder

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
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
    """DeleteInstanceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AccountName: 子账号名称
        :type AccountName: str
        """
        self._InstanceId = None
        self._AccountName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
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
    """DeleteInstanceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板 ID。
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
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
    """DeleteParamTemplate返回参数结构体

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


class DeleteReplicationInstanceRequest(AbstractModel):
    """DeleteReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID
        :type GroupId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SyncType: 数据同步类型，true:需要数据强同步,false:不需要强同步，仅限删除主实例
        :type SyncType: bool
        """
        self._GroupId = None
        self._InstanceId = None
        self._SyncType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SyncType(self):
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
    """DeleteReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeAutoBackupConfigRequest(AbstractModel):
    """DescribeAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeAutoBackupConfig返回参数结构体

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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def BackupStorageDays(self):
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays

    @property
    def BinlogStorageDays(self):
        return self._BinlogStorageDays

    @BinlogStorageDays.setter
    def BinlogStorageDays(self, BinlogStorageDays):
        self._BinlogStorageDays = BinlogStorageDays

    @property
    def RequestId(self):
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


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadRestriction请求参数结构体

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadRestriction返回参数结构体

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
        :param _LimitIp: 自定义的可下载备份文件的 VPC ID。当参数**LimitType**为**Customize **时，显示该参数。
        :type LimitIp: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp

    @property
    def RequestId(self):
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
    """DescribeBackupUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def LimitType(self):
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
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
    """DescribeBackupUrl返回参数结构体

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
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupInfos: list of BackupDownloadInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._InnerDownloadUrl = None
        self._Filenames = None
        self._BackupInfos = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def InnerDownloadUrl(self):
        return self._InnerDownloadUrl

    @InnerDownloadUrl.setter
    def InnerDownloadUrl(self, InnerDownloadUrl):
        self._InnerDownloadUrl = InnerDownloadUrl

    @property
    def Filenames(self):
        return self._Filenames

    @Filenames.setter
    def Filenames(self, Filenames):
        self._Filenames = Filenames

    @property
    def BackupInfos(self):
        return self._BackupInfos

    @BackupInfos.setter
    def BackupInfos(self, BackupInfos):
        self._BackupInfos = BackupInfos

    @property
    def RequestId(self):
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
    """DescribeBandwidthRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeBandwidthRange返回参数结构体

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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaseBandwidth = None
        self._AddBandwidth = None
        self._MinAddBandwidth = None
        self._MaxAddBandwidth = None
        self._RequestId = None

    @property
    def BaseBandwidth(self):
        return self._BaseBandwidth

    @BaseBandwidth.setter
    def BaseBandwidth(self, BaseBandwidth):
        self._BaseBandwidth = BaseBandwidth

    @property
    def AddBandwidth(self):
        return self._AddBandwidth

    @AddBandwidth.setter
    def AddBandwidth(self, AddBandwidth):
        self._AddBandwidth = AddBandwidth

    @property
    def MinAddBandwidth(self):
        return self._MinAddBandwidth

    @MinAddBandwidth.setter
    def MinAddBandwidth(self, MinAddBandwidth):
        self._MinAddBandwidth = MinAddBandwidth

    @property
    def MaxAddBandwidth(self):
        return self._MaxAddBandwidth

    @MaxAddBandwidth.setter
    def MaxAddBandwidth(self, MaxAddBandwidth):
        self._MaxAddBandwidth = MaxAddBandwidth

    @property
    def RequestId(self):
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
    """DescribeCommonDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcIds: vpc网络ID信息列表
        :type VpcIds: list of int
        :param _SubnetIds: 子网ID信息列表
        :type SubnetIds: list of int
        :param _PayMode: 计费类型过滤列表；0表示包年包月，1表示按量计费
        :type PayMode: int
        :param _InstanceIds: 实例ID过滤信息列表
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
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def UniqVpcIds(self):
        return self._UniqVpcIds

    @UniqVpcIds.setter
    def UniqVpcIds(self, UniqVpcIds):
        self._UniqVpcIds = UniqVpcIds

    @property
    def UniqSubnetIds(self):
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

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
    """DescribeCommonDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例数
        :type TotalCount: int
        :param _InstanceDetails: 实例信息
        :type InstanceDetails: list of RedisCommonInstanceList
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceDetails(self):
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def RequestId(self):
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
    """DescribeDBSecurityGroups请求参数结构体

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
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
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
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组规则。
        :type Groups: list of SecurityGroup
        :param _VIP: 实例内网IPv4地址。
        :type VIP: str
        :param _VPort: 内网端口。
        :type VPort: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def RequestId(self):
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


class DescribeInstanceAccountRequest(AbstractModel):
    """DescribeInstanceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _Limit: 分页大小。
        :type Limit: int
        :param _Offset: 分页偏移量。取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    """DescribeInstanceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Accounts: 账号详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Accounts: list of Account
        :param _TotalCount: 账号个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Accounts = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
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
    """DescribeInstanceBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页输出的备份列表大小。默认大小为20，最大值为 100。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _InstanceId: 待操作的实例ID，可通过 DescribeInstance 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _BeginTime: 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type BeginTime: str
        :param _EndTime: 结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceName(self):
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
    """DescribeInstanceBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 备份总数。
        :type TotalCount: int
        :param _BackupSet: 实例的备份数组。
        :type BackupSet: list of RedisBackupSet
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupSet(self):
        return self._BackupSet

    @BackupSet.setter
    def BackupSet(self, BackupSet):
        self._BackupSet = BackupSet

    @property
    def RequestId(self):
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
    """DescribeInstanceDTSInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeInstanceDTSInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: DTS任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _JobName: DTS任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param _Status: 任务状态,取值为：1-创建中(Creating),3-校验中(Checking)4-校验通过(CheckPass),5-校验不通过（CheckNotPass）,7-任务运行(Running),8-准备完成（ReadyComplete）,9-任务成功（Success）,10-任务失败（Failed）,11-撤销中（Stopping）,12-完成中（Completing）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _Offset: 同步时延，单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _CutDownTime: 断开时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CutDownTime: str
        :param _SrcInfo: 源实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInfo: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`
        :param _DstInfo: 目标实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DstInfo: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CutDownTime(self):
        return self._CutDownTime

    @CutDownTime.setter
    def CutDownTime(self, CutDownTime):
        self._CutDownTime = CutDownTime

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
    def RequestId(self):
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
    """详细DTS实例信息

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _SetId: 仓库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SetId: int
        :param _ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _Type: 实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Vip: 实例访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
    def Status(self):
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
    """DescribeInstanceDealDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealIds: 订单交易ID数组，即 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的输出参数DealId。
        :type DealIds: list of str
        """
        self._DealIds = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailResponse(AbstractModel):
    """DescribeInstanceDealDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealDetails: 订单详细信息。
        :type DealDetails: list of TradeDealDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealDetails = None
        self._RequestId = None

    @property
    def DealDetails(self):
        return self._DealDetails

    @DealDetails.setter
    def DealDetails(self, DealDetails):
        self._DealDetails = DealDetails

    @property
    def RequestId(self):
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


class DescribeInstanceMonitorBigKeyRequest(AbstractModel):
    """DescribeInstanceMonitorBigKey请求参数结构体

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReqType(self):
        return self._ReqType

    @ReqType.setter
    def ReqType(self, ReqType):
        self._ReqType = ReqType

    @property
    def Date(self):
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
    """DescribeInstanceMonitorBigKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 大Key详细信息
        :type Data: list of BigKeyInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstanceMonitorBigKeySizeDist请求参数结构体

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
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
    """DescribeInstanceMonitorBigKeySizeDist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 大Key大小分布详情
        :type Data: list of DelayDistribution
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstanceMonitorBigKeyTypeDist请求参数结构体

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
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
    """DescribeInstanceMonitorBigKeyTypeDist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 大Key类型分布详细信息
        :type Data: list of BigKeyTypeInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstanceMonitorHotKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _SpanType: 时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
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
    """DescribeInstanceMonitorHotKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 热Key详细信息
        :type Data: list of HotKeyInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstanceMonitorSIP请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeInstanceMonitorSIP返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 访问来源信息
        :type Data: list of SourceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstanceMonitorTookDist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Date: 时间；例如："20190219"
        :type Date: str
        :param _SpanType: 时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时
        :type SpanType: int
        """
        self._InstanceId = None
        self._Date = None
        self._SpanType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def SpanType(self):
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
    """DescribeInstanceMonitorTookDist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 时延分布信息
        :type Data: list of DelayDistribution
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstanceMonitorTopNCmd请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _SpanType: 时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
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
    """DescribeInstanceMonitorTopNCmd返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 访问命令信息
        :type Data: list of SourceCommand
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstanceMonitorTopNCmdTook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SpanType: 时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
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
    """DescribeInstanceMonitorTopNCmdTook返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 耗时详细信息
        :type Data: list of CommandTake
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstanceNodeInfo请求参数结构体

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    """DescribeInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyCount: Proxy节点数量。
        :type ProxyCount: int
        :param _Proxy: Proxy节点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Proxy: list of ProxyNodes
        :param _RedisCount: Redis节点数量。
        :type RedisCount: int
        :param _Redis: Redis节点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Redis: list of RedisNodes
        :param _TendisCount: 该参数不再使用，请忽略。
        :type TendisCount: int
        :param _Tendis: 该参数不再使用，请忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tendis: list of TendisNodes
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def Proxy(self):
        return self._Proxy

    @Proxy.setter
    def Proxy(self, Proxy):
        self._Proxy = Proxy

    @property
    def RedisCount(self):
        return self._RedisCount

    @RedisCount.setter
    def RedisCount(self, RedisCount):
        self._RedisCount = RedisCount

    @property
    def Redis(self):
        return self._Redis

    @Redis.setter
    def Redis(self, Redis):
        self._Redis = Redis

    @property
    def TendisCount(self):
        return self._TendisCount

    @TendisCount.setter
    def TendisCount(self, TendisCount):
        self._TendisCount = TendisCount

    @property
    def Tendis(self):
        return self._Tendis

    @Tendis.setter
    def Tendis(self, Tendis):
        self._Tendis = Tendis

    @property
    def RequestId(self):
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
    """DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量，取Limit整数倍
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    """DescribeInstanceParamRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总的修改历史记录数。
        :type TotalCount: int
        :param _InstanceParamHistory: 修改历史记录信息。
        :type InstanceParamHistory: list of InstanceParamHistory
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceParamHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceParamHistory(self):
        return self._InstanceParamHistory

    @InstanceParamHistory.setter
    def InstanceParamHistory(self, InstanceParamHistory):
        self._InstanceParamHistory = InstanceParamHistory

    @property
    def RequestId(self):
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
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeInstanceParams返回参数结构体

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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceEnumParam(self):
        return self._InstanceEnumParam

    @InstanceEnumParam.setter
    def InstanceEnumParam(self, InstanceEnumParam):
        self._InstanceEnumParam = InstanceEnumParam

    @property
    def InstanceIntegerParam(self):
        return self._InstanceIntegerParam

    @InstanceIntegerParam.setter
    def InstanceIntegerParam(self, InstanceIntegerParam):
        self._InstanceIntegerParam = InstanceIntegerParam

    @property
    def InstanceTextParam(self):
        return self._InstanceTextParam

    @InstanceTextParam.setter
    def InstanceTextParam(self, InstanceTextParam):
        self._InstanceTextParam = InstanceTextParam

    @property
    def InstanceMultiParam(self):
        return self._InstanceMultiParam

    @InstanceMultiParam.setter
    def InstanceMultiParam(self, InstanceMultiParam):
        self._InstanceMultiParam = InstanceMultiParam

    @property
    def RequestId(self):
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
    """DescribeInstanceSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。例如;["crs-f2ho5rsz\n"]
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
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
    """DescribeInstanceSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSecurityGroupsDetail: 实例安全组信息。
        :type InstanceSecurityGroupsDetail: list of InstanceSecurityGroupDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSecurityGroupsDetail = None
        self._RequestId = None

    @property
    def InstanceSecurityGroupsDetail(self):
        return self._InstanceSecurityGroupsDetail

    @InstanceSecurityGroupsDetail.setter
    def InstanceSecurityGroupsDetail(self, InstanceSecurityGroupsDetail):
        self._InstanceSecurityGroupsDetail = InstanceSecurityGroupsDetail

    @property
    def RequestId(self):
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
    """DescribeInstanceShards请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _FilterSlave: 是否过滤掉从节信息。
- true；过滤从节点。
- false：不过滤。
        :type FilterSlave: bool
        """
        self._InstanceId = None
        self._FilterSlave = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FilterSlave(self):
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
    """DescribeInstanceShards返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceShards: 实例分片列表信息，包括：节点信息、节点ID、Key数量、使用容量、容量倾斜率等信息。
        :type InstanceShards: list of InstanceClusterShard
        :param _TotalCount: 实例分片节点数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceShards = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceShards(self):
        return self._InstanceShards

    @InstanceShards.setter
    def InstanceShards(self, InstanceShards):
        self._InstanceShards = InstanceShards

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
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


class DescribeInstanceZoneInfoRequest(AbstractModel):
    """DescribeInstanceZoneInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeInstanceZoneInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例节点组的个数。
        :type TotalCount: int
        :param _ReplicaGroups: 实例节点组列表。
        :type ReplicaGroups: list of ReplicaGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReplicaGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReplicaGroups(self):
        return self._ReplicaGroups

    @ReplicaGroups.setter
    def ReplicaGroups(self, ReplicaGroups):
        self._ReplicaGroups = ReplicaGroups

    @property
    def RequestId(self):
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
    """DescribeInstances请求参数结构体

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def VpcIds(self):
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def UniqVpcIds(self):
        return self._UniqVpcIds

    @UniqVpcIds.setter
    def UniqVpcIds(self, UniqVpcIds):
        self._UniqVpcIds = UniqVpcIds

    @property
    def UniqSubnetIds(self):
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def RegionIds(self):
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TypeVersion(self):
        return self._TypeVersion

    @TypeVersion.setter
    def TypeVersion(self, TypeVersion):
        self._TypeVersion = TypeVersion

    @property
    def EngineName(self):
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SearchKeys(self):
        return self._SearchKeys

    @SearchKeys.setter
    def SearchKeys(self, SearchKeys):
        self._SearchKeys = SearchKeys

    @property
    def TypeList(self):
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList

    @property
    def MonitorVersion(self):
        return self._MonitorVersion

    @MonitorVersion.setter
    def MonitorVersion(self, MonitorVersion):
        self._MonitorVersion = MonitorVersion

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def ProductVersions(self):
        return self._ProductVersions

    @ProductVersions.setter
    def ProductVersions(self, ProductVersions):
        self._ProductVersions = ProductVersions

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AzMode(self):
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
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数量。
        :type TotalCount: int
        :param _InstanceSet: 实例详细信息列表。
        :type InstanceSet: list of InstanceSet
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
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
    """DescribeMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 维护时间窗起始时间，如：17:00
        :type StartTime: str
        :param _EndTime: 维护时间窗结束时间，如：19:00
        :type EndTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 指定查询的参数模板 ID。请通过接口[DescribeParamTemplates](https://cloud.tencent.com/document/product/239/58750)获取参数模板列表信息。
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
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
    """DescribeParamTemplateInfo返回参数结构体

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
        :param _Description: 参数模板描述。
        :type Description: str
        :param _Items: 参数详情。包含：参数的名称，当前运行值，默认值，最大值、最小值、枚举值等信息。
        :type Items: list of ParameterDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
    """DescribeParamTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductTypes: 产品类型数组。产品类型：1 – Redis2.8内存版（集群架构），2 – Redis2.8内存版（标准架构），3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，5 – Redis2.8内存版（单机），6 – Redis4.0内存版（标准架构），7 – Redis4.0内存版（集群架构），8 – Redis5.0内存版（标准架构），9 – Redis5.0内存版（集群架构）
        :type ProductTypes: list of int
        :param _TemplateNames: 模板名称数组。
        :type TemplateNames: list of str
        :param _TemplateIds: 模板ID数组。
        :type TemplateIds: list of str
        """
        self._ProductTypes = None
        self._TemplateNames = None
        self._TemplateIds = None

    @property
    def ProductTypes(self):
        return self._ProductTypes

    @ProductTypes.setter
    def ProductTypes(self, ProductTypes):
        self._ProductTypes = ProductTypes

    @property
    def TemplateNames(self):
        return self._TemplateNames

    @TemplateNames.setter
    def TemplateNames(self, TemplateNames):
        self._TemplateNames = TemplateNames

    @property
    def TemplateIds(self):
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
    """DescribeParamTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该用户的参数模板数量。
        :type TotalCount: int
        :param _Items: 参数模板详情。
        :type Items: list of ParamTemplateInfo
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
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    """DescribeProductInfo请求参数结构体

    """


class DescribeProductInfoResponse(AbstractModel):
    """DescribeProductInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 地域售卖信息。
        :type RegionSet: list of RegionConf
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
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
    """DescribeProjectSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 0:默认项目；-1 所有项目; >0: 特定项目
        :type ProjectId: int
        :param _SecurityGroupId: 安全组Id
        :type SecurityGroupId: str
        """
        self._ProjectId = None
        self._SecurityGroupId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupId(self):
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
    """DescribeProjectSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupDetails: 项目安全组
        :type SecurityGroupDetails: list of SecurityGroupDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroupDetails = None
        self._RequestId = None

    @property
    def SecurityGroupDetails(self):
        return self._SecurityGroupDetails

    @SecurityGroupDetails.setter
    def SecurityGroupDetails(self, SecurityGroupDetails):
        self._SecurityGroupDetails = SecurityGroupDetails

    @property
    def RequestId(self):
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
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _ProjectId: 项目 ID。
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
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def SearchKey(self):
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
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组规则。
        :type Groups: list of SecurityGroup
        :param _Total: 符合条件的安全组总数量。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
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
    """DescribeProxySlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :type InstanceId: str
        :param _BeginTime: 慢查询的开始时间。
        :type BeginTime: str
        :param _EndTime: 慢查询的结束时间。
        :type EndTime: str
        :param _MinQueryTime: 慢查询阈值，单位：毫秒。
        :type MinQueryTime: int
        :param _Limit: 分页大小。默认为 20，取值范围[20,1000]。
        :type Limit: int
        :param _Offset: 偏移量，取Limit整数倍。
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

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
    """DescribeProxySlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 慢查询总数。
        :type TotalCount: int
        :param _InstanceProxySlowLogDetail: 慢查询详情。
        :type InstanceProxySlowLogDetail: list of InstanceProxySlowlogDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceProxySlowLogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceProxySlowLogDetail(self):
        return self._InstanceProxySlowLogDetail

    @InstanceProxySlowLogDetail.setter
    def InstanceProxySlowLogDetail(self, InstanceProxySlowLogDetail):
        self._InstanceProxySlowLogDetail = InstanceProxySlowLogDetail

    @property
    def RequestId(self):
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


class DescribeReplicationGroupRequest(AbstractModel):
    """DescribeReplicationGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页输出实例列表的大小，参数默认值20。
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
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchKey(self):
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
    """DescribeReplicationGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 复制组数量。
        :type TotalCount: int
        :param _Groups: 复制组信息。
        :type Groups: list of Groups
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
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
    """DescribeSSLStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeSSLStatus返回参数结构体

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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._CertDownloadUrl

    @CertDownloadUrl.setter
    def CertDownloadUrl(self, CertDownloadUrl):
        self._CertDownloadUrl = CertDownloadUrl

    @property
    def UrlExpiredTime(self):
        return self._UrlExpiredTime

    @UrlExpiredTime.setter
    def UrlExpiredTime(self, UrlExpiredTime):
        self._UrlExpiredTime = UrlExpiredTime

    @property
    def SSLConfig(self):
        return self._SSLConfig

    @SSLConfig.setter
    def SSLConfig(self, SSLConfig):
        self._SSLConfig = SSLConfig

    @property
    def FeatureSupport(self):
        return self._FeatureSupport

    @FeatureSupport.setter
    def FeatureSupport(self, FeatureSupport):
        self._FeatureSupport = FeatureSupport

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
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


class DescribeSlowLogRequest(AbstractModel):
    """DescribeSlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。

        :type InstanceId: str
        :param _BeginTime: 预查询慢日志的起始时间。
        :type BeginTime: str
        :param _EndTime: 预查询慢日志的结束时间。
        :type EndTime: str
        :param _MinQueryTime: 慢查询平均执行时间阈值，单位：毫秒。
        :type MinQueryTime: int
        :param _Limit: 每个页面展示的慢查询条数，默认值为20。取值范围：[20,1000]。
        :type Limit: int
        :param _Offset: 慢查询条数的偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _Role: 节点所属角色。<ul><li>master：主节点。</li><li>slave：从节点。</li></ul>
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

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
    def Role(self):
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
    """DescribeSlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 慢查询总数。
        :type TotalCount: int
        :param _InstanceSlowlogDetail: 慢查询详情。
        :type InstanceSlowlogDetail: list of InstanceSlowlogDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSlowlogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSlowlogDetail(self):
        return self._InstanceSlowlogDetail

    @InstanceSlowlogDetail.setter
    def InstanceSlowlogDetail(self, InstanceSlowlogDetail):
        self._InstanceSlowlogDetail = InstanceSlowlogDetail

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
    """DescribeTaskInfo返回参数结构体

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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskMessage(self):
        return self._TaskMessage

    @TaskMessage.setter
    def TaskMessage(self, TaskMessage):
        self._TaskMessage = TaskMessage

    @property
    def RequestId(self):
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
    """DescribeTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定实例 ID。例如：crs-xjhsdj****。请登录[Redis控制台](https://console.cloud.tencent.com/redis)在实例列表复制实例 ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Limit: 每页输出的任务列表大小。默认为 20，最多输出100条。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _ProjectIds: 项目 ID。登录 [Redis 控制台](https://console.cloud.tencent.com/redis)，在右上角的账号信息下拉菜单中，选择**项目管理**，即可获取对应的项目 ID。
        :type ProjectIds: list of int
        :param _TaskTypes: 任务类型。
- FLOW_CREATE：创建实例。
- FLOW_MODIFYCONNECTIONCONFIG：调整带宽连接数。
- FLOW_MODIFYINSTANCEPASSWORDFREE：免密变更流程。
- FLOW_CLEARNETWORK：VPC退还中。
- FLOW_SETPWD：设置访问密码。
- FLOW_EXPORSHR：扩缩容流程。
- FLOW_UpgradeArch：实例架构升级流程。
- FLOW_MODIFYINSTANCEPARAMS：修改实例参数。
- FLOW_MODIFYINSTACEREADONLY：只读变更流程。
- FLOW_CLOSE：关闭实例。
- FLOW_DELETE：删除实例。
- FLOW_OPEN_WAN：开启外网。
- FLOW_CLEAN：清空实例。      
- FLOW_MODIFYINSTANCEACCOUNT：修改实例账号。
- FLOW_ENABLEINSTANCE_REPLICATE：开启副本只读。
- FLOW_DISABLEINSTANCE_REPLICATE: 关闭副本只读。
- FLOW_SWITCHINSTANCEVIP：交换实例 VIP。
- FLOW_CHANGE_REPLICA_TO_MSTER：副本节点升主节点。
- FLOW_BACKUPINSTANCE：备份实例。
        :type TaskTypes: list of str
        :param _BeginTime: 任务执行的起始时间。格式如：2021-12-30 00:00:00。
        :type BeginTime: str
        :param _EndTime: 任务运行的终止时间。格式如：2021-12-30 20:59:35
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
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def OperatorUin(self):
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin

    @property
    def OperateUin(self):
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
    """DescribeTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数。
        :type TotalCount: int
        :param _Tasks: 任务详细信息。
        :type Tasks: list of TaskInfoDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
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
    """DescribeTendisSlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id：crs-ngvou0i1
        :type InstanceId: str
        :param _BeginTime: 开始时间：2019-09-08 12:12:41
        :type BeginTime: str
        :param _EndTime: 结束时间：2019-09-09 12:12:41
        :type EndTime: str
        :param _MinQueryTime: 慢查询阈值（毫秒）
        :type MinQueryTime: int
        :param _Limit: 页面大小：默认20
        :type Limit: int
        :param _Offset: 偏移量，取Limit整数倍
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

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
    """DescribeTendisSlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 慢查询总数
        :type TotalCount: int
        :param _TendisSlowLogDetail: 慢查询详情
        :type TendisSlowLogDetail: list of TendisSlowLogDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TendisSlowLogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TendisSlowLogDetail(self):
        return self._TendisSlowLogDetail

    @TendisSlowLogDetail.setter
    def TendisSlowLogDetail(self, TendisSlowLogDetail):
        self._TendisSlowLogDetail = TendisSlowLogDetail

    @property
    def RequestId(self):
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
    """DestroyPostpaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DestroyPostpaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DestroyPrepaidInstanceRequest(AbstractModel):
    """DestroyPrepaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DestroyPrepaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单Id
        :type DealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class DisableReplicaReadonlyRequest(AbstractModel):
    """DisableReplicaReadonly请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例序号ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DisableReplicaReadonly返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _SecurityGroupId: 安全组 ID。
        :type SecurityGroupId: str
        :param _InstanceIds: 实例ID列表，一个或者多个实例 ID 组成的数组。
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
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
    """DisassociateSecurityGroups返回参数结构体

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


class EnableReplicaReadonlyRequest(AbstractModel):
    """EnableReplicaReadonly请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例序号ID
        :type InstanceId: str
        :param _ReadonlyPolicy: 账号路由策略：填写master或者replication，表示路由主节点，从节点；不填路由策略默认为写主节点，读从节点
        :type ReadonlyPolicy: list of str
        """
        self._InstanceId = None
        self._ReadonlyPolicy = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadonlyPolicy(self):
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
    """EnableReplicaReadonly返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 错误：ERROR，正确OK（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Groups(AbstractModel):
    """复制组信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户 APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。
        :type AppId: int
        :param _RegionId: 地域ID 。
- 1：广州 
- 4：上海 
- 5：中国香港 
- 6：多伦多 
- 7：上海金融 
- 8：北京 
- 9：新加坡
- 11：深圳金融
- 15：美西（硅谷）
- 16：成都 
- 17：德国 
- 18：韩国 
- 19：重庆 
- 21：印度 
- 22：美东（弗吉尼亚）
- 23：泰国 
- 25：日本
        :type RegionId: int
        :param _GroupId: 复制组 ID。格式如：crs-rpl-deind****。
        :type GroupId: str
        :param _GroupName: 复制组名称。
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of Instances
        :param _Remark: 备注信息。
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def Remark(self):
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
    """热Key详细信息

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
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
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
    """安全组入站规则

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
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
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
    """InquiryPriceCreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeId: 实例类型：2 – Redis2.8内存版(标准架构)，3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，6 – Redis4.0内存版(标准架构)，7 – Redis4.0内存版(集群架构)，8 – Redis5.0内存版(标准架构)，9 – Redis5.0内存版(集群架构)。
        :type TypeId: int
        :param _MemSize: 内存容量，单位为MB， 数值需为1024的整数倍，具体规格以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。
TypeId为标准架构时，MemSize是实例总内存容量；TypeId为集群架构时，MemSize是单分片内存容量。
        :type MemSize: int
        :param _GoodsNum: 实例数量，单次购买实例数量以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。
        :type GoodsNum: int
        :param _Period: 购买时长，在创建包年包月实例的时候需要填写，按量计费实例填1即可，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :type Period: int
        :param _BillingMode: 付费方式:0-按量计费，1-包年包月。
        :type BillingMode: int
        :param _ZoneId: 实例所属的可用区ID，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
        :type ZoneId: int
        :param _RedisShardNum: 实例分片数量，Redis2.8标准架构、CKV标准架构和Redis2.8单机版、Redis4.0标准架构不需要填写。
        :type RedisShardNum: int
        :param _RedisReplicasNum: 实例副本数量，Redis2.8标准架构、CKV标准架构和Redis2.8单机版不需要填写。
        :type RedisReplicasNum: int
        :param _ReplicasReadonly: 是否支持副本只读，Redis2.8标准架构、CKV标准架构和Redis2.8单机版不需要填写。
        :type ReplicasReadonly: bool
        :param _ZoneName: 实例所属的可用区名称，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。
        :type ZoneName: str
        :param _ProductVersion: "local"本地盘版，"cloud"云盘版，"cdc"独享集群版，如果不传默认询价为本地盘版本
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
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def ReplicasReadonly(self):
        return self._ReplicasReadonly

    @ReplicasReadonly.setter
    def ReplicasReadonly(self, ReplicasReadonly):
        self._ReplicasReadonly = ReplicasReadonly

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ProductVersion(self):
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
    """InquiryPriceCreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 价格，单位：分
注意：此字段可能返回 null，表示取不到有效值。
        :type Price: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    """InquiryPriceRenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 购买时长，单位：月
        :type Period: int
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._Period = None
        self._InstanceId = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceId(self):
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
    """InquiryPriceRenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 价格，单位：分
注意：此字段可能返回 null，表示取不到有效值。
        :type Price: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _MemSize: 分片大小 单位 MB
        :type MemSize: int
        :param _RedisShardNum: 分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写
        :type RedisShardNum: int
        :param _RedisReplicasNum: 副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写
        :type RedisReplicasNum: int
        """
        self._InstanceId = None
        self._MemSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
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
    """InquiryPriceUpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 价格，单位：分
注意：此字段可能返回 null，表示取不到有效值。
        :type Price: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InstanceClusterNode(AbstractModel):
    """实例节点类型

    """

    def __init__(self):
        r"""
        :param _Name: 节点名称。
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RunId(self):
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Connected(self):
        return self._Connected

    @Connected.setter
    def Connected(self, Connected):
        self._Connected = Connected

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DownTime(self):
        return self._DownTime

    @DownTime.setter
    def DownTime(self, DownTime):
        self._DownTime = DownTime

    @property
    def Slots(self):
        return self._Slots

    @Slots.setter
    def Slots(self, Slots):
        self._Slots = Slots

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def QpsSlope(self):
        return self._QpsSlope

    @QpsSlope.setter
    def QpsSlope(self, QpsSlope):
        self._QpsSlope = QpsSlope

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageSlope(self):
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
    """实例分片列表信息

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
        :param _Runid: 实例运行时节点 ID。
        :type Runid: str
        :param _Connected: 服务状态。
- 0：down。
- 1：on。
        :type Connected: int
        """
        self._ShardName = None
        self._ShardId = None
        self._Role = None
        self._Keys = None
        self._Slots = None
        self._Storage = None
        self._StorageSlope = None
        self._Runid = None
        self._Connected = None

    @property
    def ShardName(self):
        return self._ShardName

    @ShardName.setter
    def ShardName(self, ShardName):
        self._ShardName = ShardName

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Slots(self):
        return self._Slots

    @Slots.setter
    def Slots(self, Slots):
        self._Slots = Slots

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageSlope(self):
        return self._StorageSlope

    @StorageSlope.setter
    def StorageSlope(self, StorageSlope):
        self._StorageSlope = StorageSlope

    @property
    def Runid(self):
        return self._Runid

    @Runid.setter
    def Runid(self, Runid):
        self._Runid = Runid

    @property
    def Connected(self):
        return self._Connected

    @Connected.setter
    def Connected(self, Connected):
        self._Connected = Connected


    def _deserialize(self, params):
        self._ShardName = params.get("ShardName")
        self._ShardId = params.get("ShardId")
        self._Role = params.get("Role")
        self._Keys = params.get("Keys")
        self._Slots = params.get("Slots")
        self._Storage = params.get("Storage")
        self._StorageSlope = params.get("StorageSlope")
        self._Runid = params.get("Runid")
        self._Connected = params.get("Connected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnumParam(AbstractModel):
    """实例枚举类型参数描述

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
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
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
    """实例整型参数描述

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
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Unit(self):
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
    """实例多选项类型参数描述

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
        :param _EnumValue: 参数说明。
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
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
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
    """实例节点

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
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceClusterNode(self):
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
    """实例参数

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
        


class InstanceParamHistory(AbstractModel):
    """实例参数修改历史

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
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def PreValue(self):
        return self._PreValue

    @PreValue.setter
    def PreValue(self, PreValue):
        self._PreValue = PreValue

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
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
    """代理慢查询详情

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
        """
        self._Duration = None
        self._Client = None
        self._Command = None
        self._CommandLine = None
        self._ExecuteTime = None

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Client(self):
        return self._Client

    @Client.setter
    def Client(self, Client):
        self._Client = Client

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def ExecuteTime(self):
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._Client = params.get("Client")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._ExecuteTime = params.get("ExecuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSecurityGroupDetail(AbstractModel):
    """实例安全组信息

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupDetails(self):
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
    """实例详细信息列表。

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Appid: 用户APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。

        :type Appid: int
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _RegionId: 地域 ID。<ul><li>1：广州。</li><li>4：上海。</li><li>5：中国香港。</li><li>6：多伦多。</li> <li>7：上海金融。</li> <li>8：北京。</li> <li>9：新加坡。</li> <li>11：深圳金融。</li> <li>15：美西（硅谷）。</li><li>16：成都。</li><li>17：法兰克福。</li><li>18：首尔。</li><li>19：重庆。</li><li>21：孟买。</li><li>22：美东（弗吉尼亚）。</li><li>23：曼谷。</li><li>25：东京。</li></ul>
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
        :param _SubStatus: 流程中的实例，返回子状态。
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
        :type SlaveReadWeight: int
        :param _InstanceTags: 实例关联的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTags: list of InstanceTagInfo
        :param _ProjectName: 项目名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _NoAuth: 是否为免密实例。<ul><li>true：免密实例。</li><li>false：非免密实例。</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type NoAuth: bool
        :param _ClientLimit: 客户端连接数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimit: int
        :param _DtsStatus: DTS状态（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DtsStatus: int
        :param _NetLimit: 分片带宽上限，单位MB。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetLimit: int
        :param _PasswordFree: 免密实例标识（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type PasswordFree: int
        :param _Vip6: 内部参数，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip6: str
        :param _ReadOnly: 实例只读标识（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnly: int
        :param _RemainBandwidthDuration: 内部参数，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainBandwidthDuration: str
        :param _DiskSize: Redis实例请忽略该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _MonitorVersion: 监控版本。<ul><li>1m：1分钟粒度监控。目前该监控粒度已下线，具体信息，请参见[云数据库 Redis 1分钟粒度下线公告](https://cloud.tencent.com/document/product/239/80653)。</li><li>5s：5秒粒度监控。</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorVersion: str
        :param _ClientLimitMin: 客户端最大连接数可设置的最小值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimitMin: int
        :param _ClientLimitMax: 客户端最大连接数可设置的最大值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimitMax: int
        :param _NodeSet: 实例的节点详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of RedisNodeInfo
        :param _Region: 实例所在的地域信息，比如ap-guangzhou。
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _WanAddress: 外网地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type WanAddress: str
        :param _PolarisServer: 北极星服务地址，内部使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolarisServer: str
        :param _CurrentProxyVersion: 实例当前Proxy版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentProxyVersion: str
        :param _CurrentRedisVersion: 实例当前Cache小版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentRedisVersion: str
        :param _UpgradeProxyVersion: 实例可升级Proxy版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeProxyVersion: str
        :param _UpgradeRedisVersion: 实例可升级Cache小版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeRedisVersion: str
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
        self._CurrentProxyVersion = None
        self._CurrentRedisVersion = None
        self._UpgradeProxyVersion = None
        self._UpgradeRedisVersion = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WanIp(self):
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Createtime(self):
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def SizeUsed(self):
        return self._SizeUsed

    @SizeUsed.setter
    def SizeUsed(self, SizeUsed):
        self._SizeUsed = SizeUsed

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def InstanceTitle(self):
        return self._InstanceTitle

    @InstanceTitle.setter
    def InstanceTitle(self, InstanceTitle):
        self._InstanceTitle = InstanceTitle

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def SubStatus(self):
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceNode(self):
        return self._InstanceNode

    @InstanceNode.setter
    def InstanceNode(self, InstanceNode):
        self._InstanceNode = InstanceNode

    @property
    def RedisShardSize(self):
        return self._RedisShardSize

    @RedisShardSize.setter
    def RedisShardSize(self, RedisShardSize):
        self._RedisShardSize = RedisShardSize

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def PriceId(self):
        return self._PriceId

    @PriceId.setter
    def PriceId(self, PriceId):
        self._PriceId = PriceId

    @property
    def CloseTime(self):
        return self._CloseTime

    @CloseTime.setter
    def CloseTime(self, CloseTime):
        self._CloseTime = CloseTime

    @property
    def SlaveReadWeight(self):
        return self._SlaveReadWeight

    @SlaveReadWeight.setter
    def SlaveReadWeight(self, SlaveReadWeight):
        self._SlaveReadWeight = SlaveReadWeight

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def ClientLimit(self):
        return self._ClientLimit

    @ClientLimit.setter
    def ClientLimit(self, ClientLimit):
        self._ClientLimit = ClientLimit

    @property
    def DtsStatus(self):
        return self._DtsStatus

    @DtsStatus.setter
    def DtsStatus(self, DtsStatus):
        self._DtsStatus = DtsStatus

    @property
    def NetLimit(self):
        return self._NetLimit

    @NetLimit.setter
    def NetLimit(self, NetLimit):
        self._NetLimit = NetLimit

    @property
    def PasswordFree(self):
        return self._PasswordFree

    @PasswordFree.setter
    def PasswordFree(self, PasswordFree):
        self._PasswordFree = PasswordFree

    @property
    def Vip6(self):
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def RemainBandwidthDuration(self):
        return self._RemainBandwidthDuration

    @RemainBandwidthDuration.setter
    def RemainBandwidthDuration(self, RemainBandwidthDuration):
        self._RemainBandwidthDuration = RemainBandwidthDuration

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MonitorVersion(self):
        return self._MonitorVersion

    @MonitorVersion.setter
    def MonitorVersion(self, MonitorVersion):
        self._MonitorVersion = MonitorVersion

    @property
    def ClientLimitMin(self):
        return self._ClientLimitMin

    @ClientLimitMin.setter
    def ClientLimitMin(self, ClientLimitMin):
        self._ClientLimitMin = ClientLimitMin

    @property
    def ClientLimitMax(self):
        return self._ClientLimitMax

    @ClientLimitMax.setter
    def ClientLimitMax(self, ClientLimitMax):
        self._ClientLimitMax = ClientLimitMax

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def WanAddress(self):
        return self._WanAddress

    @WanAddress.setter
    def WanAddress(self, WanAddress):
        self._WanAddress = WanAddress

    @property
    def PolarisServer(self):
        return self._PolarisServer

    @PolarisServer.setter
    def PolarisServer(self, PolarisServer):
        self._PolarisServer = PolarisServer

    @property
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def CurrentRedisVersion(self):
        return self._CurrentRedisVersion

    @CurrentRedisVersion.setter
    def CurrentRedisVersion(self, CurrentRedisVersion):
        self._CurrentRedisVersion = CurrentRedisVersion

    @property
    def UpgradeProxyVersion(self):
        return self._UpgradeProxyVersion

    @UpgradeProxyVersion.setter
    def UpgradeProxyVersion(self, UpgradeProxyVersion):
        self._UpgradeProxyVersion = UpgradeProxyVersion

    @property
    def UpgradeRedisVersion(self):
        return self._UpgradeRedisVersion

    @UpgradeRedisVersion.setter
    def UpgradeRedisVersion(self, UpgradeRedisVersion):
        self._UpgradeRedisVersion = UpgradeRedisVersion


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
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._CurrentRedisVersion = params.get("CurrentRedisVersion")
        self._UpgradeProxyVersion = params.get("UpgradeProxyVersion")
        self._UpgradeRedisVersion = params.get("UpgradeRedisVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSlowlogDetail(AbstractModel):
    """慢查询详情

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
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Client(self):
        return self._Client

    @Client.setter
    def Client(self, Client):
        self._Client = Client

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def ExecuteTime(self):
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime

    @property
    def Node(self):
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
    """实例标签信息

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
        


class InstanceTextParam(AbstractModel):
    """实例字符型参数描述

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
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def TextValue(self):
        return self._TextValue

    @TextValue.setter
    def TextValue(self, TextValue):
        self._TextValue = TextValue

    @property
    def Status(self):
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
    """复制组实例

    """

    def __init__(self):
        r"""
        :param _AppId: 用户APPID。APPID是与账号ID有唯一对应关系的应用 ID，部分腾讯云产品会使用此 APPID。
        :type AppId: int
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _RegionId: 地域ID。<ul><li>1：广州。</li><li>4：上海。</li><li> 5：香港。</li> <li> 6：多伦多。</li> <li> 7：上海金融。</li> <li> 8：北京。</li> <li> 9：新加坡。</li> <li> 11：深圳金融。</li> <li> 15：美西（硅谷）。</li> </ul>
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
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _Engine: 引擎：社区版Redis、腾讯云CKV。
        :type Engine: str
        :param _Role: 实例读写权限。<ul><li>rw：可读写。</li><li>r：只读。</li></ul>
        :type Role: str
        :param _Vip: 实例 VIP 地址。
        :type Vip: str
        :param _Vip6: 内部参数，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip6: str
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
        self._VpcID = None
        self._VPort = None
        self._Status = None
        self._GrocerySysId = None
        self._ProductType = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisShardSize(self):
        return self._RedisShardSize

    @RedisShardSize.setter
    def RedisShardSize(self, RedisShardSize):
        self._RedisShardSize = RedisShardSize

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vip6(self):
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def VpcID(self):
        return self._VpcID

    @VpcID.setter
    def VpcID(self, VpcID):
        self._VpcID = VpcID

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GrocerySysId(self):
        return self._GrocerySysId

    @GrocerySysId.setter
    def GrocerySysId(self, GrocerySysId):
        self._GrocerySysId = GrocerySysId

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

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
    """KillMasterGroup请求参数结构体

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
        :param _ShardIds: 分片集群的分片 ID。
        :type ShardIds: list of int
        """
        self._InstanceId = None
        self._Password = None
        self._ShardIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ShardIds(self):
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
    """KillMasterGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ManualBackupInstanceRequest(AbstractModel):
    """ManualBackupInstance请求参数结构体

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def StorageDays(self):
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
    """ManualBackupInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModfiyInstancePasswordRequest(AbstractModel):
    """ModfiyInstancePassword请求参数结构体

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldPassword(self):
        return self._OldPassword

    @OldPassword.setter
    def OldPassword(self, OldPassword):
        self._OldPassword = OldPassword

    @property
    def Password(self):
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
        


class ModfiyInstancePasswordResponse(AbstractModel):
    """ModfiyInstancePassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyAutoBackupConfigRequest(AbstractModel):
    """ModifyAutoBackupConfig请求参数结构体

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
        """
        self._InstanceId = None
        self._WeekDays = None
        self._TimePeriod = None
        self._AutoBackupType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def AutoBackupType(self):
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        self._AutoBackupType = params.get("AutoBackupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupConfigResponse(AbstractModel):
    """ModifyAutoBackupConfig返回参数结构体

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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoBackupType = None
        self._WeekDays = None
        self._TimePeriod = None
        self._BackupStorageDays = None
        self._RequestId = None

    @property
    def AutoBackupType(self):
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def BackupStorageDays(self):
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays

    @property
    def RequestId(self):
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
    """ModifyBackupDownloadRestriction请求参数结构体

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
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
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
    """ModifyBackupDownloadRestriction返回参数结构体

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


class ModifyConnectionConfigRequest(AbstractModel):
    """ModifyConnectionConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例的ID，长度在12-36之间。
        :type InstanceId: str
        :param _Bandwidth: 附加带宽，大于0，单位MB。
        :type Bandwidth: int
        :param _ClientLimit: 单分片的总连接数。
未开启副本只读时，下限为10000，上限为40000；
开启副本只读时，下限为10000，上限为10000×(只读副本数+3)。
        :type ClientLimit: int
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._ClientLimit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ClientLimit(self):
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
    """ModifyConnectionConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：redis。
        :type Product: str
        :param _SecurityGroupIds: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._Product = None
        self._SecurityGroupIds = None
        self._InstanceId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceId(self):
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
    """ModifyDBInstanceSecurityGroups返回参数结构体

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


class ModifyInstanceAccountRequest(AbstractModel):
    """ModifyInstanceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AccountName: 子账号名称，如果要修改主账号，填root
        :type AccountName: str
        :param _AccountPassword: 子账号密码
        :type AccountPassword: str
        :param _Remark: 子账号描述信息
        :type Remark: str
        :param _ReadonlyPolicy: 路由策略：填写master或者replication，表示主节点或者从节点
        :type ReadonlyPolicy: list of str
        :param _Privilege: 子账号读写策略：填写r、w、rw，表示只读，只写，读写策略
        :type Privilege: str
        :param _NoAuth: true表示将主账号切换为免密账号，这里只适用于主账号，子账号不可免密
        :type NoAuth: bool
        """
        self._InstanceId = None
        self._AccountName = None
        self._AccountPassword = None
        self._Remark = None
        self._ReadonlyPolicy = None
        self._Privilege = None
        self._NoAuth = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ReadonlyPolicy(self):
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._Remark = params.get("Remark")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Privilege = params.get("Privilege")
        self._NoAuth = params.get("NoAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAccountResponse(AbstractModel):
    """ModifyInstanceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceParamsRequest(AbstractModel):
    """ModifyInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceParams: 实例修改的参数列表。
        :type InstanceParams: list of InstanceParam
        """
        self._InstanceId = None
        self._InstanceParams = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceParams(self):
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
    """ModifyInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Changed: 说明修改参数配置是否成功。<br><li>true：指修改成功；<br><li>false：指修改失败。<br>
        :type Changed: bool
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Changed = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Changed(self):
        return self._Changed

    @Changed.setter
    def Changed(self, Changed):
        self._Changed = Changed

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Changed = params.get("Changed")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceReadOnlyRequest(AbstractModel):
    """ModifyInstanceReadOnly请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InputMode: 实例输入模式，0：读写 1：只读
        :type InputMode: str
        """
        self._InstanceId = None
        self._InputMode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InputMode(self):
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
    """ModifyInstanceReadOnly返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operation: 修改实例操作，如填写：rename-表示实例重命名；modifyProject-修改实例所属项目；modifyAutoRenew-修改实例续费标记
        :type Operation: str
        :param _InstanceIds: 实例Id
        :type InstanceIds: list of str
        :param _InstanceNames: 实例的新名称
        :type InstanceNames: list of str
        :param _ProjectId: 项目Id
        :type ProjectId: int
        :param _AutoRenews: 自动续费标识。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费
        :type AutoRenews: list of int
        :param _InstanceId: 已经废弃
        :type InstanceId: str
        :param _InstanceName: 已经废弃
        :type InstanceName: str
        :param _AutoRenew: 已经废弃
        :type AutoRenew: int
        """
        self._Operation = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._ProjectId = None
        self._AutoRenews = None
        self._InstanceId = None
        self._InstanceName = None
        self._AutoRenew = None

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenews(self):
        return self._AutoRenews

    @AutoRenews.setter
    def AutoRenews(self, AutoRenews):
        self._AutoRenews = AutoRenews

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
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenews = params.get("AutoRenews")
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
    """ModifyInstance返回参数结构体

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


class ModifyMaintenanceWindowRequest(AbstractModel):
    """ModifyMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 维护时间窗起始时间，如：17:00
        :type StartTime: str
        :param _EndTime: 维护时间窗结束时间，如：19:00
        :type EndTime: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    """ModifyMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 修改状态：success 或者 failed
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyNetworkConfigRequest(AbstractModel):
    """ModifyNetworkConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Operation: 指预修改网络的类别，包括：
- changeVip：指切换私有网络，包含其内网IPv4地址及端口。
- changeVpc：指切换私有网络所属子网。
- changeBaseToVpc：指基础网络切换为私有网络。
- changeVPort：指仅修改实例网络端口。
        :type Operation: str
        :param _Vip: 指实例私有网络内网 IPv4 地址。当**Operation**为**changeVip**时，需配置该参数。
        :type Vip: str
        :param _VpcId: 指修改后的私有网络 ID，当**Operation**为**changeVpc**或**changeBaseToVpc**时，需配置该参数。
        :type VpcId: str
        :param _SubnetId: 指修改后的私有网络所属子网 ID，当**Operation**为**changeVpc**或**changeBaseToVpc**时，需配置该参数。
        :type SubnetId: str
        :param _Recycle: 原内网 IPv4 地址保留时长。
- 单位：天。
- 取值范围：0、1、2、3、7、15。

**说明**：设置原地址保留时长需最新版SDK，否则原地址将立即释放，查看SDK版本，请参见 [SDK中心](https://cloud.tencent.com/document/sdk)。
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

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
    def Recycle(self):
        return self._Recycle

    @Recycle.setter
    def Recycle(self, Recycle):
        self._Recycle = Recycle

    @property
    def VPort(self):
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
    """ModifyNetworkConfig返回参数结构体

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
        :param _TaskId: 任务 ID。可获取**taskId**，通过接口 **DescribeTaskInfo **查询任务执行状态。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
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
    """ModifyParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 源参数模板 ID。
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
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamList(self):
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
    """ModifyParamTemplate返回参数结构体

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


class OpenSSLRequest(AbstractModel):
    """OpenSSL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """OpenSSL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """安全组出站规则

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
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
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
    """参数模板信息

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
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductType(self):
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
    """Redis参数模板参数详情

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
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: str
        :param _Min: 参数允许的最小值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: str
        :param _EnumValue: 参数可选枚举值。如果为非枚举参数，则为空。
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
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
    """产品信息

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
        :param _Engine: 产品引擎。包括：腾讯云 CKV与社区版 Redis。
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
        :param _EnableRepicaReadOnly: 是否支持副本只读。
- true：支持副本只读。
- false：不支持。
        :type EnableRepicaReadOnly: bool
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

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def MinBuyNum(self):
        return self._MinBuyNum

    @MinBuyNum.setter
    def MinBuyNum(self, MinBuyNum):
        self._MinBuyNum = MinBuyNum

    @property
    def MaxBuyNum(self):
        return self._MaxBuyNum

    @MaxBuyNum.setter
    def MaxBuyNum(self, MaxBuyNum):
        self._MaxBuyNum = MaxBuyNum

    @property
    def Saleout(self):
        return self._Saleout

    @Saleout.setter
    def Saleout(self, Saleout):
        self._Saleout = Saleout

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def ShardSize(self):
        return self._ShardSize

    @ShardSize.setter
    def ShardSize(self, ShardSize):
        self._ShardSize = ShardSize

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def ShardNum(self):
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def EnableRepicaReadOnly(self):
        return self._EnableRepicaReadOnly

    @EnableRepicaReadOnly.setter
    def EnableRepicaReadOnly(self, EnableRepicaReadOnly):
        self._EnableRepicaReadOnly = EnableRepicaReadOnly


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodes(AbstractModel):
    """Proxy节点信息。

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        :param _ZoneId: 可用区 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        """
        self._NodeId = None
        self._ZoneId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def ZoneId(self):
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
    """实例的备份数组

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
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSize: int
        :param _FullBackup: 内部字段，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type FullBackup: int
        :param _InstanceType: 内部字段，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Locked(self):
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def BackupSize(self):
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def FullBackup(self):
        return self._FullBackup

    @FullBackup.setter
    def FullBackup(self, FullBackup):
        self._FullBackup = FullBackup

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

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
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def ExpireTime(self):
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
    """单个实例信息

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
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Createtime(self):
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def NetType(self):
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
        


class RedisNode(AbstractModel):
    """Redis节点的运行信息

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
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Slot(self):
        return self._Slot

    @Slot.setter
    def Slot(self, Slot):
        self._Slot = Slot

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Role(self):
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
    """描述 Redis 实例的主节点或者副本节点信息。

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
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
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
    """Redis节点信息

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
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ZoneId(self):
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
    """地域信息

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
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionShortName(self):
        return self._RegionShortName

    @RegionShortName.setter
    def RegionShortName(self, RegionShortName):
        self._RegionShortName = RegionShortName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ZoneSet(self):
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
    """ReleaseWanAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """ReleaseWanAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _WanStatus: 关闭外网的状态
        :type WanStatus: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._WanStatus = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._WanStatus = params.get("WanStatus")
        self._RequestId = params.get("RequestId")


class RemoveReplicationInstanceRequest(AbstractModel):
    """RemoveReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 复制组ID
        :type GroupId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SyncType: 数据同步类型，true:需要数据强同步,false:不需要强同步，仅限删除主实例
        :type SyncType: bool
        """
        self._GroupId = None
        self._InstanceId = None
        self._SyncType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SyncType(self):
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
    """RemoveReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 购买时长，单位：月。
        :type Period: int
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _ModifyPayMode: 标识是否修改计费模式。<ul><li>当前实例计费模式为按量计费方式，预转换为包年包月而续费，请指定该参数为 <b>prepaid</b>。</li><li>当前实例计费模式为包年包月方式，可不设置该参数。</li></ul>
        :type ModifyPayMode: str
        """
        self._Period = None
        self._InstanceId = None
        self._ModifyPayMode = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ModifyPayMode(self):
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
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 交易ID。
        :type DealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class ReplicaGroup(AbstractModel):
    """实例节点组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 节点组 ID。
        :type GroupId: int
        :param _GroupName: 节点组的名称，主节点为空。
        :type GroupName: str
        :param _ZoneId: 节点的可用区ID，比如ap-guangzhou-1
        :type ZoneId: str
        :param _Role: 节点组类型，master为主节点，replica为副本节点
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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RedisNodes(self):
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
    """ResetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Redis实例ID
        :type InstanceId: str
        :param _Password: 重置的密码（切换为免密实例时，可不传；其他情况必传）
        :type Password: str
        :param _NoAuth: 是否切换免密实例，false-切换为非免密码实例，true-切换为免密码实例；默认false
        :type NoAuth: bool
        """
        self._InstanceId = None
        self._Password = None
        self._NoAuth = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._NoAuth = params.get("NoAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    """ResetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID（修改密码时的任务ID，如果时切换免密码或者非免密码实例，则无需关注此返回值）
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """API购买实例绑定标签

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
        


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待操作的实例ID，可通过 DescribeInstances 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _BackupId: 备份ID，可通过 GetRedisBackupList 接口返回值中的 backupId 获取
        :type BackupId: str
        :param _Password: 实例密码，恢复实例时，需要校验实例密码（免密实例不需要传密码）
        :type Password: str
        """
        self._InstanceId = None
        self._BackupId = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def Password(self):
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
    """RestoreInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可通过 DescribeTaskInfo 接口查询任务执行状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组规则

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
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def Inbound(self):
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
    """安全组详情

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
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def InboundRule(self):
        return self._InboundRule

    @InboundRule.setter
    def InboundRule(self, InboundRule):
        self._InboundRule = InboundRule

    @property
    def OutboundRule(self):
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
    """安全组出入规则

    """

    def __init__(self):
        r"""
        :param _Action: 标识出入数据库的IP与端口是否被允许。
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
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

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
    def Proto(self):
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
    """访问命令

    """

    def __init__(self):
        r"""
        :param _Cmd: 命令
        :type Cmd: str
        :param _Count: 执行次数
        :type Count: int
        """
        self._Cmd = None
        self._Count = None

    @property
    def Cmd(self):
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Count(self):
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
    """访问来源信息

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
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Conn(self):
        return self._Conn

    @Conn.setter
    def Conn(self, Conn):
        self._Conn = Conn

    @property
    def Cmd(self):
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
    """StartupInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """StartupInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SwitchInstanceVipRequest(AbstractModel):
    """SwitchInstanceVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcInstanceId: 源实例ID
        :type SrcInstanceId: str
        :param _DstInstanceId: 目标实例ID
        :type DstInstanceId: str
        :param _TimeDelay: 单位为秒。源实例与目标实例间DTS已断开时间，如果DTS断开时间大于TimeDelay，则不切换VIP，建议尽量根据业务设置一个可接受的值。
        :type TimeDelay: int
        :param _ForceSwitch: 在DTS断开的情况下是否强制切换。1：强制切换，0：不强制切换
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
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def DstInstanceId(self):
        return self._DstInstanceId

    @DstInstanceId.setter
    def DstInstanceId(self, DstInstanceId):
        self._DstInstanceId = DstInstanceId

    @property
    def TimeDelay(self):
        return self._TimeDelay

    @TimeDelay.setter
    def TimeDelay(self, TimeDelay):
        self._TimeDelay = TimeDelay

    @property
    def ForceSwitch(self):
        return self._ForceSwitch

    @ForceSwitch.setter
    def ForceSwitch(self, ForceSwitch):
        self._ForceSwitch = ForceSwitch

    @property
    def SwitchTime(self):
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
    """SwitchInstanceVip返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SwitchProxyRequest(AbstractModel):
    """SwitchProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ProxyID: 实例ProxyID
        :type ProxyID: str
        """
        self._InstanceId = None
        self._ProxyID = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyID(self):
        return self._ProxyID

    @ProxyID.setter
    def ProxyID(self, ProxyID):
        self._ProxyID = ProxyID


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyID = params.get("ProxyID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchProxyResponse(AbstractModel):
    """SwitchProxy返回参数结构体

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


class TaskInfoDetail(AbstractModel):
    """任务信息详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _StartTime: 任务开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _TaskType: 任务类型。
- FLOW_CREATE：创建实例。
- FLOW_MODIFYCONNECTIONCONFIG：调整带宽连接数。
- FLOW_MODIFYINSTANCEPASSWORDFREE：免密变更流程。
- FLOW_CLEARNETWORK：VPC退还中。
- FLOW_SETPWD：设置访问密码。
- FLOW_EXPORSHR：扩缩容流程。
- FLOW_UpgradeArch：实例架构升级流程。
- FLOW_MODIFYINSTANCEPARAMS：修改实例参数。
- FLOW_MODIFYINSTACEREADONLY：只读变更流程。
- FLOW_CLOSE：关闭实例。
- FLOW_DELETE：删除实例。
- FLOW_OPEN_WAN：开启外网。
- FLOW_CLEAN：清空实例。      
- FLOW_MODIFYINSTANCEACCOUNT：修改实例账号。
- FLOW_ENABLEINSTANCE_REPLICATE：开启副本只读。
- FLOW_DISABLEINSTANCE_REPLICATE: 关闭副本只读。
- FLOW_SWITCHINSTANCEVIP：交换实例 VIP。
- FLOW_CHANGE_REPLICA_TO_MSTER：副本节点升主节点。
- FLOW_BACKUPINSTANCE：备份实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param _InstanceName: 实例名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _InstanceId: 实例 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _Progress: 任务进度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param _EndTime: 任务执行结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Result: 任务执行状态。

0：任务初始化。
1：执行中。
2：完成。
4：失败。
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Result(self):
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
    """tendis节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID
        :type NodeId: str
        :param _NodeRole: 节点角色
        :type NodeRole: str
        """
        self._NodeId = None
        self._NodeRole = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeRole = params.get("NodeRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisSlowLogDetail(AbstractModel):
    """Tendis慢查询详情

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
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def Node(self):
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
    """订单交易信息

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
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Creater(self):
        return self._Creater

    @Creater.setter
    def Creater(self, Creater):
        self._Creater = Creater

    @property
    def CreatTime(self):
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime

    @property
    def OverdueTime(self):
        return self._OverdueTime

    @OverdueTime.setter
    def OverdueTime(self, OverdueTime):
        self._OverdueTime = OverdueTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def InstanceIds(self):
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
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待变更实例 ID。
        :type InstanceId: str
        :param _MemSize: 指实例每个分片内存变更后的大小。<ul><li>单位 MB。</li><li>每次只能修改参数MemSize、RedisShardNum和RedisReplicasNum其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。</li><li>缩容时，缩容后的规格务必要大于等于使用容量的1.3倍，否则将执行失败。</li></ul>
        :type MemSize: int
        :param _RedisShardNum: 指实例变更后的分片数量。<ul><li>标准架构不需要配置该参数，集群架构为必填参数。</li><li>集群架构，每次只能修改参数RedisShardNum、MemSize和RedisReplicasNum其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。</li></ul>
        :type RedisShardNum: int
        :param _RedisReplicasNum: 指实例变更后的副本数量。<ul><li>每次只能修改参数RedisReplicasNum、MemSize和RedisShardNum其中的一个，不能同时修改。且修改其中一个参数时，其他两个参数需输入实例原有的配置规格。</li><li>多AZ实例修改副本时必须要传入NodeSet。</li></ul>
        :type RedisReplicasNum: int
        :param _NodeSet: 多AZ实例，增加副本时的附带信息，包括副本的可用区和副本的类型（NodeType为1）。非多AZ实例不需要配置该参数。
        :type NodeSet: list of RedisNodeInfo
        """
        self._InstanceId = None
        self._MemSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._NodeSet = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单ID。
        :type DealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class UpgradeInstanceVersionRequest(AbstractModel):
    """UpgradeInstanceVersion请求参数结构体

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
        return self._TargetInstanceType

    @TargetInstanceType.setter
    def TargetInstanceType(self, TargetInstanceType):
        self._TargetInstanceType = TargetInstanceType

    @property
    def SwitchOption(self):
        return self._SwitchOption

    @SwitchOption.setter
    def SwitchOption(self, SwitchOption):
        self._SwitchOption = SwitchOption

    @property
    def InstanceId(self):
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
    """UpgradeInstanceVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单ID
        :type DealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class UpgradeProxyVersionRequest(AbstractModel):
    """UpgradeProxyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _CurrentProxyVersion: 当前proxy版本
        :type CurrentProxyVersion: str
        :param _UpgradeProxyVersion: 可升级的redis版本
        :type UpgradeProxyVersion: str
        :param _InstanceTypeUpgradeNow: 1-立即升级   0-维护时间窗口升级
        :type InstanceTypeUpgradeNow: int
        """
        self._InstanceId = None
        self._CurrentProxyVersion = None
        self._UpgradeProxyVersion = None
        self._InstanceTypeUpgradeNow = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def UpgradeProxyVersion(self):
        return self._UpgradeProxyVersion

    @UpgradeProxyVersion.setter
    def UpgradeProxyVersion(self, UpgradeProxyVersion):
        self._UpgradeProxyVersion = UpgradeProxyVersion

    @property
    def InstanceTypeUpgradeNow(self):
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
    """UpgradeProxyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeSmallVersionRequest(AbstractModel):
    """UpgradeSmallVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _CurrentRedisVersion: 当前redis版本
        :type CurrentRedisVersion: str
        :param _UpgradeRedisVersion: 可升级的redis版本
        :type UpgradeRedisVersion: str
        :param _InstanceTypeUpgradeNow: 1-立即升级   0-维护时间窗口升级
        :type InstanceTypeUpgradeNow: int
        """
        self._InstanceId = None
        self._CurrentRedisVersion = None
        self._UpgradeRedisVersion = None
        self._InstanceTypeUpgradeNow = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CurrentRedisVersion(self):
        return self._CurrentRedisVersion

    @CurrentRedisVersion.setter
    def CurrentRedisVersion(self, CurrentRedisVersion):
        self._CurrentRedisVersion = CurrentRedisVersion

    @property
    def UpgradeRedisVersion(self):
        return self._UpgradeRedisVersion

    @UpgradeRedisVersion.setter
    def UpgradeRedisVersion(self, UpgradeRedisVersion):
        self._UpgradeRedisVersion = UpgradeRedisVersion

    @property
    def InstanceTypeUpgradeNow(self):
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
    """UpgradeSmallVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeVersionToMultiAvailabilityZonesRequest(AbstractModel):
    """UpgradeVersionToMultiAvailabilityZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _UpgradeProxyAndRedisServer: 升级多可用区之后是否支持就近访问功能。
<ul><li>true：支持就近访问功能。升级过程，需同时升级 Proxy 版本和 Redis 内核小版本，涉及数据搬迁，可能会长达数小时。</li><li>false：无需支持就近访问功能。升级多可用区仅涉及管理元数据迁移，对服务没有影响，升级过程通常在3分钟内完成。</li></ul>
        :type UpgradeProxyAndRedisServer: bool
        """
        self._InstanceId = None
        self._UpgradeProxyAndRedisServer = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeProxyAndRedisServer(self):
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
    """UpgradeVersionToMultiAvailabilityZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ZoneCapacityConf(AbstractModel):
    """可用区内产品信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区ID：如ap-guangzhou-3
        :type ZoneId: str
        :param _ZoneName: 可用区名称
        :type ZoneName: str
        :param _IsSaleout: 可用区是否售罄
        :type IsSaleout: bool
        :param _IsDefault: 是否为默认可用区
        :type IsDefault: bool
        :param _NetWorkType: 网络类型：basenet -- 基础网络；vpcnet -- VPC网络
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
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def IsSaleout(self):
        return self._IsSaleout

    @IsSaleout.setter
    def IsSaleout(self, IsSaleout):
        self._IsSaleout = IsSaleout

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def NetWorkType(self):
        return self._NetWorkType

    @NetWorkType.setter
    def NetWorkType(self, NetWorkType):
        self._NetWorkType = NetWorkType

    @property
    def ProductSet(self):
        return self._ProductSet

    @ProductSet.setter
    def ProductSet(self, ProductSet):
        self._ProductSet = ProductSet

    @property
    def OldZoneId(self):
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
        