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


class ApplyDiskBackupRequest(AbstractModel):
    r"""ApplyDiskBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID，可通过[DescribeDisks](https://cloud.tencent.com/document/api/1207/66093)接口查询。
        :type DiskId: str
        :param _DiskBackupId: 云硬盘备份点ID，可通过[DescribeDiskBackups](https://cloud.tencent.com/document/api/1207/84379)接口查询。
        :type DiskBackupId: str
        """
        self._DiskId = None
        self._DiskBackupId = None

    @property
    def DiskId(self):
        r"""云硬盘ID，可通过[DescribeDisks](https://cloud.tencent.com/document/api/1207/66093)接口查询。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupId(self):
        r"""云硬盘备份点ID，可通过[DescribeDiskBackups](https://cloud.tencent.com/document/api/1207/84379)接口查询。
        :rtype: str
        """
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskBackupId = params.get("DiskBackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyDiskBackupResponse(AbstractModel):
    r"""ApplyDiskBackup返回参数结构体

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


class ApplyFirewallTemplateRequest(AbstractModel):
    r"""ApplyFirewallTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :type TemplateId: str
        :param _ApplyInstances: 应用防火墙模板的实例列表。列表长度最大值是100。
        :type ApplyInstances: list of InstanceIdentifier
        """
        self._TemplateId = None
        self._ApplyInstances = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ApplyInstances(self):
        r"""应用防火墙模板的实例列表。列表长度最大值是100。
        :rtype: list of InstanceIdentifier
        """
        return self._ApplyInstances

    @ApplyInstances.setter
    def ApplyInstances(self, ApplyInstances):
        self._ApplyInstances = ApplyInstances


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("ApplyInstances") is not None:
            self._ApplyInstances = []
            for item in params.get("ApplyInstances"):
                obj = InstanceIdentifier()
                obj._deserialize(item)
                self._ApplyInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyFirewallTemplateResponse(AbstractModel):
    r"""ApplyFirewallTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。
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


class ApplyInstanceSnapshotRequest(AbstractModel):
    r"""ApplyInstanceSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/product/1207/47573) 接口返回值中的 InstanceId	获取。
        :type InstanceId: str
        :param _SnapshotId: 快照 ID。可通过 [DescribeSnapshots](https://cloud.tencent.com/document/product/1207/54388) 接口返回值中的 SnapshotId		获取。
        :type SnapshotId: str
        """
        self._InstanceId = None
        self._SnapshotId = None

    @property
    def InstanceId(self):
        r"""实例 ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/product/1207/47573) 接口返回值中的 InstanceId	获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SnapshotId(self):
        r"""快照 ID。可通过 [DescribeSnapshots](https://cloud.tencent.com/document/product/1207/54388) 接口返回值中的 SnapshotId		获取。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SnapshotId = params.get("SnapshotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInstanceSnapshotResponse(AbstractModel):
    r"""ApplyInstanceSnapshot返回参数结构体

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


class AssociateInstancesKeyPairsRequest(AbstractModel):
    r"""AssociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 密钥对 ID 列表，每次请求批量密钥对的上限为 100。可通过[DescribeKeyPairs](https://cloud.tencent.com/document/api/1207/55540)接口返回值中的KeyId获取。
        :type KeyIds: list of str
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self._KeyIds = None
        self._InstanceIds = None

    @property
    def KeyIds(self):
        r"""密钥对 ID 列表，每次请求批量密钥对的上限为 100。可通过[DescribeKeyPairs](https://cloud.tencent.com/document/api/1207/55540)接口返回值中的KeyId获取。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateInstancesKeyPairsResponse(AbstractModel):
    r"""AssociateInstancesKeyPairs返回参数结构体

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


class AttachCcnRequest(AbstractModel):
    r"""AttachCcn请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CcnId: 云联网实例ID。可通过[DescribeCcns](https://cloud.tencent.com/document/product/215/19199)接口返回值中的CcnId获取。
        :type CcnId: str
        """
        self._CcnId = None

    @property
    def CcnId(self):
        r"""云联网实例ID。可通过[DescribeCcns](https://cloud.tencent.com/document/product/215/19199)接口返回值中的CcnId获取。
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnResponse(AbstractModel):
    r"""AttachCcn返回参数结构体

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


class AttachDetail(AbstractModel):
    r"""挂载信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AttachedDiskCount: 实例已挂载弹性云盘数量
        :type AttachedDiskCount: int
        :param _MaxAttachCount: 可挂载弹性云盘数量
        :type MaxAttachCount: int
        """
        self._InstanceId = None
        self._AttachedDiskCount = None
        self._MaxAttachCount = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttachedDiskCount(self):
        r"""实例已挂载弹性云盘数量
        :rtype: int
        """
        return self._AttachedDiskCount

    @AttachedDiskCount.setter
    def AttachedDiskCount(self, AttachedDiskCount):
        self._AttachedDiskCount = AttachedDiskCount

    @property
    def MaxAttachCount(self):
        r"""可挂载弹性云盘数量
        :rtype: int
        """
        return self._MaxAttachCount

    @MaxAttachCount.setter
    def MaxAttachCount(self, MaxAttachCount):
        self._MaxAttachCount = MaxAttachCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AttachedDiskCount = params.get("AttachedDiskCount")
        self._MaxAttachCount = params.get("MaxAttachCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksRequest(AbstractModel):
    r"""AttachDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :type DiskIds: list of str
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _RenewFlag: 自动续费标识。取值范围：

NOTIFY_AND_AUTO_RENEW：通知过期且自动续费。 NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费。 DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知。

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，云盘到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._DiskIds = None
        self._InstanceId = None
        self._RenewFlag = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围：

NOTIFY_AND_AUTO_RENEW：通知过期且自动续费。 NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费。 DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知。

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，云盘到期后将按月自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._InstanceId = params.get("InstanceId")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksResponse(AbstractModel):
    r"""AttachDisks返回参数结构体

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


class AutoMountConfiguration(AbstractModel):
    r"""自动挂载并初始化该数据盘。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待挂载的实例ID。指定的实例必须与指定的数据盘处于同一可用区，实例状态必须处于“运行中”状态，且实例必须支持[自动化助手](https://cloud.tencent.com/document/product/1340/50752)。
        :type InstanceId: str
        :param _MountPoint: 实例内的挂载点。仅Linux操作系统的实例可传入该参数, 不传则默认挂载在“/data/disk”路径下。
        :type MountPoint: str
        :param _FileSystemType: 文件系统类型。取值: “ext4”、“xfs”。仅Linux操作系统的实例可传入该参数, 不传则默认为“ext4”。
        :type FileSystemType: str
        """
        self._InstanceId = None
        self._MountPoint = None
        self._FileSystemType = None

    @property
    def InstanceId(self):
        r"""待挂载的实例ID。指定的实例必须与指定的数据盘处于同一可用区，实例状态必须处于“运行中”状态，且实例必须支持[自动化助手](https://cloud.tencent.com/document/product/1340/50752)。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MountPoint(self):
        r"""实例内的挂载点。仅Linux操作系统的实例可传入该参数, 不传则默认挂载在“/data/disk”路径下。
        :rtype: str
        """
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def FileSystemType(self):
        r"""文件系统类型。取值: “ext4”、“xfs”。仅Linux操作系统的实例可传入该参数, 不传则默认为“ext4”。
        :rtype: str
        """
        return self._FileSystemType

    @FileSystemType.setter
    def FileSystemType(self, FileSystemType):
        self._FileSystemType = FileSystemType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MountPoint = params.get("MountPoint")
        self._FileSystemType = params.get("FileSystemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Blueprint(AbstractModel):
    r"""描述了镜像信息。

    """

    def __init__(self):
        r"""
        :param _BlueprintId: 镜像 ID  ，是 Blueprint 的唯一标识。
        :type BlueprintId: str
        :param _DisplayTitle: 镜像对外展示标题。
        :type DisplayTitle: str
        :param _DisplayVersion: 镜像对外展示版本。
        :type DisplayVersion: str
        :param _Description: 镜像描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _OsName: 操作系统名称。
        :type OsName: str
        :param _Platform: 操作系统平台。
        :type Platform: str
        :param _PlatformType: 操作系统平台类型，如 LINUX_UNIX、WINDOWS。
        :type PlatformType: str
        :param _BlueprintType: 镜像类型，如 APP_OS（应用镜像）, PURE_OS（系统镜像）, DOCKER（容器）, PRIVATE（私有镜像）, SHARED（共享镜像）, GAME_PORTAL（游戏专区镜像）。
        :type BlueprintType: str
        :param _ImageUrl: 镜像图片 URL。
        :type ImageUrl: str
        :param _RequiredSystemDiskSize: 镜像所需系统盘大小，单位 GB。
        :type RequiredSystemDiskSize: int
        :param _BlueprintState: 镜像状态。
可选值：
NORMAL（正常）、SYNCING（同步中）、OFFLINE（下线）、CREATEFAILED（创建失败）、SYNCING_FAILED（目的地域同步失败）、ISOLATING（隔离中）、ISOLATED（已隔离）、DELETING（删除中）、DESTROYING（销毁中）。
        :type BlueprintState: str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _BlueprintName: 镜像名称。
        :type BlueprintName: str
        :param _SupportAutomationTools: 镜像是否支持自动化助手。
        :type SupportAutomationTools: bool
        :param _RequiredMemorySize: 镜像所需内存大小, 单位: GB
        :type RequiredMemorySize: int
        :param _ImageId: CVM镜像共享到轻量应用服务器轻量应用服务器后的CVM镜像ID。
        :type ImageId: str
        :param _CommunityUrl: 官方网站Url。
        :type CommunityUrl: str
        :param _GuideUrl: 指导文章Url。
        :type GuideUrl: str
        :param _SceneIdSet: 镜像关联使用场景Id列表。
        :type SceneIdSet: list of str
        :param _DockerVersion: Docker版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerVersion: str
        :param _BlueprintShared: 镜像是否已共享。
        :type BlueprintShared: bool
        :param _Tags: 镜像绑定的标签列表。
        :type Tags: list of Tag
        """
        self._BlueprintId = None
        self._DisplayTitle = None
        self._DisplayVersion = None
        self._Description = None
        self._OsName = None
        self._Platform = None
        self._PlatformType = None
        self._BlueprintType = None
        self._ImageUrl = None
        self._RequiredSystemDiskSize = None
        self._BlueprintState = None
        self._CreatedTime = None
        self._BlueprintName = None
        self._SupportAutomationTools = None
        self._RequiredMemorySize = None
        self._ImageId = None
        self._CommunityUrl = None
        self._GuideUrl = None
        self._SceneIdSet = None
        self._DockerVersion = None
        self._BlueprintShared = None
        self._Tags = None

    @property
    def BlueprintId(self):
        r"""镜像 ID  ，是 Blueprint 的唯一标识。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def DisplayTitle(self):
        r"""镜像对外展示标题。
        :rtype: str
        """
        return self._DisplayTitle

    @DisplayTitle.setter
    def DisplayTitle(self, DisplayTitle):
        self._DisplayTitle = DisplayTitle

    @property
    def DisplayVersion(self):
        r"""镜像对外展示版本。
        :rtype: str
        """
        return self._DisplayVersion

    @DisplayVersion.setter
    def DisplayVersion(self, DisplayVersion):
        self._DisplayVersion = DisplayVersion

    @property
    def Description(self):
        r"""镜像描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OsName(self):
        r"""操作系统名称。
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def Platform(self):
        r"""操作系统平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def PlatformType(self):
        r"""操作系统平台类型，如 LINUX_UNIX、WINDOWS。
        :rtype: str
        """
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def BlueprintType(self):
        r"""镜像类型，如 APP_OS（应用镜像）, PURE_OS（系统镜像）, DOCKER（容器）, PRIVATE（私有镜像）, SHARED（共享镜像）, GAME_PORTAL（游戏专区镜像）。
        :rtype: str
        """
        return self._BlueprintType

    @BlueprintType.setter
    def BlueprintType(self, BlueprintType):
        self._BlueprintType = BlueprintType

    @property
    def ImageUrl(self):
        r"""镜像图片 URL。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RequiredSystemDiskSize(self):
        r"""镜像所需系统盘大小，单位 GB。
        :rtype: int
        """
        return self._RequiredSystemDiskSize

    @RequiredSystemDiskSize.setter
    def RequiredSystemDiskSize(self, RequiredSystemDiskSize):
        self._RequiredSystemDiskSize = RequiredSystemDiskSize

    @property
    def BlueprintState(self):
        r"""镜像状态。
可选值：
NORMAL（正常）、SYNCING（同步中）、OFFLINE（下线）、CREATEFAILED（创建失败）、SYNCING_FAILED（目的地域同步失败）、ISOLATING（隔离中）、ISOLATED（已隔离）、DELETING（删除中）、DESTROYING（销毁中）。
        :rtype: str
        """
        return self._BlueprintState

    @BlueprintState.setter
    def BlueprintState(self, BlueprintState):
        self._BlueprintState = BlueprintState

    @property
    def CreatedTime(self):
        r"""创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def BlueprintName(self):
        r"""镜像名称。
        :rtype: str
        """
        return self._BlueprintName

    @BlueprintName.setter
    def BlueprintName(self, BlueprintName):
        self._BlueprintName = BlueprintName

    @property
    def SupportAutomationTools(self):
        r"""镜像是否支持自动化助手。
        :rtype: bool
        """
        return self._SupportAutomationTools

    @SupportAutomationTools.setter
    def SupportAutomationTools(self, SupportAutomationTools):
        self._SupportAutomationTools = SupportAutomationTools

    @property
    def RequiredMemorySize(self):
        r"""镜像所需内存大小, 单位: GB
        :rtype: int
        """
        return self._RequiredMemorySize

    @RequiredMemorySize.setter
    def RequiredMemorySize(self, RequiredMemorySize):
        self._RequiredMemorySize = RequiredMemorySize

    @property
    def ImageId(self):
        r"""CVM镜像共享到轻量应用服务器轻量应用服务器后的CVM镜像ID。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def CommunityUrl(self):
        r"""官方网站Url。
        :rtype: str
        """
        return self._CommunityUrl

    @CommunityUrl.setter
    def CommunityUrl(self, CommunityUrl):
        self._CommunityUrl = CommunityUrl

    @property
    def GuideUrl(self):
        r"""指导文章Url。
        :rtype: str
        """
        return self._GuideUrl

    @GuideUrl.setter
    def GuideUrl(self, GuideUrl):
        self._GuideUrl = GuideUrl

    @property
    def SceneIdSet(self):
        r"""镜像关联使用场景Id列表。
        :rtype: list of str
        """
        return self._SceneIdSet

    @SceneIdSet.setter
    def SceneIdSet(self, SceneIdSet):
        self._SceneIdSet = SceneIdSet

    @property
    def DockerVersion(self):
        r"""Docker版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DockerVersion

    @DockerVersion.setter
    def DockerVersion(self, DockerVersion):
        self._DockerVersion = DockerVersion

    @property
    def BlueprintShared(self):
        r"""镜像是否已共享。
        :rtype: bool
        """
        return self._BlueprintShared

    @BlueprintShared.setter
    def BlueprintShared(self, BlueprintShared):
        self._BlueprintShared = BlueprintShared

    @property
    def Tags(self):
        r"""镜像绑定的标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._DisplayTitle = params.get("DisplayTitle")
        self._DisplayVersion = params.get("DisplayVersion")
        self._Description = params.get("Description")
        self._OsName = params.get("OsName")
        self._Platform = params.get("Platform")
        self._PlatformType = params.get("PlatformType")
        self._BlueprintType = params.get("BlueprintType")
        self._ImageUrl = params.get("ImageUrl")
        self._RequiredSystemDiskSize = params.get("RequiredSystemDiskSize")
        self._BlueprintState = params.get("BlueprintState")
        self._CreatedTime = params.get("CreatedTime")
        self._BlueprintName = params.get("BlueprintName")
        self._SupportAutomationTools = params.get("SupportAutomationTools")
        self._RequiredMemorySize = params.get("RequiredMemorySize")
        self._ImageId = params.get("ImageId")
        self._CommunityUrl = params.get("CommunityUrl")
        self._GuideUrl = params.get("GuideUrl")
        self._SceneIdSet = params.get("SceneIdSet")
        self._DockerVersion = params.get("DockerVersion")
        self._BlueprintShared = params.get("BlueprintShared")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlueprintInstance(AbstractModel):
    r"""描述镜像实例信息。

    """

    def __init__(self):
        r"""
        :param _Blueprint: 镜像信息。
        :type Blueprint: :class:`tencentcloud.lighthouse.v20200324.models.Blueprint`
        :param _SoftwareSet: 软件列表。
        :type SoftwareSet: list of Software
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._Blueprint = None
        self._SoftwareSet = None
        self._InstanceId = None

    @property
    def Blueprint(self):
        r"""镜像信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.Blueprint`
        """
        return self._Blueprint

    @Blueprint.setter
    def Blueprint(self, Blueprint):
        self._Blueprint = Blueprint

    @property
    def SoftwareSet(self):
        r"""软件列表。
        :rtype: list of Software
        """
        return self._SoftwareSet

    @SoftwareSet.setter
    def SoftwareSet(self, SoftwareSet):
        self._SoftwareSet = SoftwareSet

    @property
    def InstanceId(self):
        r"""实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("Blueprint") is not None:
            self._Blueprint = Blueprint()
            self._Blueprint._deserialize(params.get("Blueprint"))
        if params.get("SoftwareSet") is not None:
            self._SoftwareSet = []
            for item in params.get("SoftwareSet"):
                obj = Software()
                obj._deserialize(item)
                self._SoftwareSet.append(obj)
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlueprintPrice(AbstractModel):
    r"""BlueprintPrice	自定义镜像的价格参数。

    """

    def __init__(self):
        r"""
        :param _OriginalBlueprintPrice: 镜像单价，原价。单位元。
        :type OriginalBlueprintPrice: float
        :param _OriginalPrice: 镜像总价，原价。单位元。
        :type OriginalPrice: float
        :param _Discount: 折扣。
        :type Discount: float
        :param _DiscountPrice: 镜像折扣后总价。单位元。
        :type DiscountPrice: float
        """
        self._OriginalBlueprintPrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None

    @property
    def OriginalBlueprintPrice(self):
        r"""镜像单价，原价。单位元。
        :rtype: float
        """
        return self._OriginalBlueprintPrice

    @OriginalBlueprintPrice.setter
    def OriginalBlueprintPrice(self, OriginalBlueprintPrice):
        self._OriginalBlueprintPrice = OriginalBlueprintPrice

    @property
    def OriginalPrice(self):
        r"""镜像总价，原价。单位元。
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        r"""折扣。
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        r"""镜像折扣后总价。单位元。
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._OriginalBlueprintPrice = params.get("OriginalBlueprintPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bundle(AbstractModel):
    r"""套餐信息。

    """

    def __init__(self):
        r"""
        :param _BundleId: 套餐 ID。
        :type BundleId: str
        :param _Memory: 内存大小，单位 GB。
        :type Memory: int
        :param _SystemDiskType: 系统盘类型。
取值范围： 
<li> CLOUD_SSD：SSD 云硬盘</li><li> CLOUD_PREMIUM：高性能云硬盘</li>
        :type SystemDiskType: str
        :param _SystemDiskSize: 系统盘大小。单位GB。
        :type SystemDiskSize: int
        :param _MonthlyTraffic: 每月网络流量，单位 GB。
        :type MonthlyTraffic: int
        :param _SupportLinuxUnixPlatform: 是否支持 Linux/Unix 平台。
        :type SupportLinuxUnixPlatform: bool
        :param _SupportWindowsPlatform: 是否支持 Windows 平台。
        :type SupportWindowsPlatform: bool
        :param _Price: 套餐当前单位价格信息。
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param _CPU: CPU 核数。
        :type CPU: int
        :param _InternetMaxBandwidthOut: 峰值带宽，单位 Mbps。
        :type InternetMaxBandwidthOut: int
        :param _InternetChargeType: 网络计费类型。
        :type InternetChargeType: str
        :param _BundleSalesState: 套餐售卖状态,取值:‘AVAILABLE’(可用) , ‘SOLD_OUT’(售罄)
        :type BundleSalesState: str
        :param _BundleType: 套餐类型。
取值范围：
<li>GENERAL_BUNDLE：通用型</li>
<li>STORAGE_BUNDLE：存储型</li>
<li>ENTERPRISE_BUNDLE：企业型</li>
<li>EXCLUSIVE_BUNDLE：专属型</li>
<li>BEFAST_BUNDLE：蜂驰型 </li>
<li>STARTER_BUNDLE：入门型</li>
<li>CAREFREE_BUNDLE：无忧型</li>
<li>RAZOR_SPEED_BUNDLE：锐驰型</li>
        :type BundleType: str
        :param _BundleTypeDescription: 套餐类型描述信息。
        :type BundleTypeDescription: str
        :param _BundleDisplayLabel: 套餐展示标签.
取值范围:
"ACTIVITY": 活动套餐,
"NORMAL": 普通套餐
"CAREFREE": 无忧套餐
        :type BundleDisplayLabel: str
        :param _TrafficUnlimited: 流量是否无上限。
        :type TrafficUnlimited: bool
        """
        self._BundleId = None
        self._Memory = None
        self._SystemDiskType = None
        self._SystemDiskSize = None
        self._MonthlyTraffic = None
        self._SupportLinuxUnixPlatform = None
        self._SupportWindowsPlatform = None
        self._Price = None
        self._CPU = None
        self._InternetMaxBandwidthOut = None
        self._InternetChargeType = None
        self._BundleSalesState = None
        self._BundleType = None
        self._BundleTypeDescription = None
        self._BundleDisplayLabel = None
        self._TrafficUnlimited = None

    @property
    def BundleId(self):
        r"""套餐 ID。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def Memory(self):
        r"""内存大小，单位 GB。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def SystemDiskType(self):
        r"""系统盘类型。
取值范围： 
<li> CLOUD_SSD：SSD 云硬盘</li><li> CLOUD_PREMIUM：高性能云硬盘</li>
        :rtype: str
        """
        return self._SystemDiskType

    @SystemDiskType.setter
    def SystemDiskType(self, SystemDiskType):
        self._SystemDiskType = SystemDiskType

    @property
    def SystemDiskSize(self):
        r"""系统盘大小。单位GB。
        :rtype: int
        """
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def MonthlyTraffic(self):
        r"""每月网络流量，单位 GB。
        :rtype: int
        """
        return self._MonthlyTraffic

    @MonthlyTraffic.setter
    def MonthlyTraffic(self, MonthlyTraffic):
        self._MonthlyTraffic = MonthlyTraffic

    @property
    def SupportLinuxUnixPlatform(self):
        r"""是否支持 Linux/Unix 平台。
        :rtype: bool
        """
        return self._SupportLinuxUnixPlatform

    @SupportLinuxUnixPlatform.setter
    def SupportLinuxUnixPlatform(self, SupportLinuxUnixPlatform):
        self._SupportLinuxUnixPlatform = SupportLinuxUnixPlatform

    @property
    def SupportWindowsPlatform(self):
        r"""是否支持 Windows 平台。
        :rtype: bool
        """
        return self._SupportWindowsPlatform

    @SupportWindowsPlatform.setter
    def SupportWindowsPlatform(self, SupportWindowsPlatform):
        self._SupportWindowsPlatform = SupportWindowsPlatform

    @property
    def Price(self):
        r"""套餐当前单位价格信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def CPU(self):
        r"""CPU 核数。
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def InternetMaxBandwidthOut(self):
        r"""峰值带宽，单位 Mbps。
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def InternetChargeType(self):
        r"""网络计费类型。
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def BundleSalesState(self):
        r"""套餐售卖状态,取值:‘AVAILABLE’(可用) , ‘SOLD_OUT’(售罄)
        :rtype: str
        """
        return self._BundleSalesState

    @BundleSalesState.setter
    def BundleSalesState(self, BundleSalesState):
        self._BundleSalesState = BundleSalesState

    @property
    def BundleType(self):
        r"""套餐类型。
取值范围：
<li>GENERAL_BUNDLE：通用型</li>
<li>STORAGE_BUNDLE：存储型</li>
<li>ENTERPRISE_BUNDLE：企业型</li>
<li>EXCLUSIVE_BUNDLE：专属型</li>
<li>BEFAST_BUNDLE：蜂驰型 </li>
<li>STARTER_BUNDLE：入门型</li>
<li>CAREFREE_BUNDLE：无忧型</li>
<li>RAZOR_SPEED_BUNDLE：锐驰型</li>
        :rtype: str
        """
        return self._BundleType

    @BundleType.setter
    def BundleType(self, BundleType):
        self._BundleType = BundleType

    @property
    def BundleTypeDescription(self):
        r"""套餐类型描述信息。
        :rtype: str
        """
        return self._BundleTypeDescription

    @BundleTypeDescription.setter
    def BundleTypeDescription(self, BundleTypeDescription):
        self._BundleTypeDescription = BundleTypeDescription

    @property
    def BundleDisplayLabel(self):
        r"""套餐展示标签.
取值范围:
"ACTIVITY": 活动套餐,
"NORMAL": 普通套餐
"CAREFREE": 无忧套餐
        :rtype: str
        """
        return self._BundleDisplayLabel

    @BundleDisplayLabel.setter
    def BundleDisplayLabel(self, BundleDisplayLabel):
        self._BundleDisplayLabel = BundleDisplayLabel

    @property
    def TrafficUnlimited(self):
        r"""流量是否无上限。
        :rtype: bool
        """
        return self._TrafficUnlimited

    @TrafficUnlimited.setter
    def TrafficUnlimited(self, TrafficUnlimited):
        self._TrafficUnlimited = TrafficUnlimited


    def _deserialize(self, params):
        self._BundleId = params.get("BundleId")
        self._Memory = params.get("Memory")
        self._SystemDiskType = params.get("SystemDiskType")
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._MonthlyTraffic = params.get("MonthlyTraffic")
        self._SupportLinuxUnixPlatform = params.get("SupportLinuxUnixPlatform")
        self._SupportWindowsPlatform = params.get("SupportWindowsPlatform")
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._CPU = params.get("CPU")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._InternetChargeType = params.get("InternetChargeType")
        self._BundleSalesState = params.get("BundleSalesState")
        self._BundleType = params.get("BundleType")
        self._BundleTypeDescription = params.get("BundleTypeDescription")
        self._BundleDisplayLabel = params.get("BundleDisplayLabel")
        self._TrafficUnlimited = params.get("TrafficUnlimited")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelShareBlueprintAcrossAccountsRequest(AbstractModel):
    r"""CancelShareBlueprintAcrossAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintId: 镜像ID, 可以通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回的BlueprintId获取。
        :type BlueprintId: str
        :param _AccountIds: 接收共享镜像的[账号ID](https://cloud.tencent.com/document/product/213/4944#.E8.8E.B7.E5.8F.96.E4.B8.BB.E8.B4.A6.E5.8F.B7.E7.9A.84.E8.B4.A6.E5.8F.B7-id)列表。账号ID不同于QQ号，查询用户账号ID请查看账号信息中的账号ID栏。账号个数取值最大为10。
        :type AccountIds: list of str
        """
        self._BlueprintId = None
        self._AccountIds = None

    @property
    def BlueprintId(self):
        r"""镜像ID, 可以通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回的BlueprintId获取。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def AccountIds(self):
        r"""接收共享镜像的[账号ID](https://cloud.tencent.com/document/product/213/4944#.E8.8E.B7.E5.8F.96.E4.B8.BB.E8.B4.A6.E5.8F.B7.E7.9A.84.E8.B4.A6.E5.8F.B7-id)列表。账号ID不同于QQ号，查询用户账号ID请查看账号信息中的账号ID栏。账号个数取值最大为10。
        :rtype: list of str
        """
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._AccountIds = params.get("AccountIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelShareBlueprintAcrossAccountsResponse(AbstractModel):
    r"""CancelShareBlueprintAcrossAccounts返回参数结构体

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


class CcnAttachedInstance(AbstractModel):
    r"""云联网关联的实例列表。

    """

    def __init__(self):
        r"""
        :param _CcnId: 云联网ID。
        :type CcnId: str
        :param _CidrBlock: 关联实例CIDR。
        :type CidrBlock: list of str
        :param _State: 关联实例状态：

•  PENDING：申请中
•  ACTIVE：已连接
•  EXPIRED：已过期
•  REJECTED：已拒绝
•  DELETED：已删除
•  FAILED：失败的（2小时后将异步强制解关联）
•  ATTACHING：关联中
•  DETACHING：解关联中
•  DETACHFAILED：解关联失败（2小时后将异步强制解关联）
        :type State: str
        :param _AttachedTime: 关联时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachedTime: str
        :param _Description: 备注
        :type Description: str
        """
        self._CcnId = None
        self._CidrBlock = None
        self._State = None
        self._AttachedTime = None
        self._Description = None

    @property
    def CcnId(self):
        r"""云联网ID。
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def CidrBlock(self):
        r"""关联实例CIDR。
        :rtype: list of str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def State(self):
        r"""关联实例状态：

•  PENDING：申请中
•  ACTIVE：已连接
•  EXPIRED：已过期
•  REJECTED：已拒绝
•  DELETED：已删除
•  FAILED：失败的（2小时后将异步强制解关联）
•  ATTACHING：关联中
•  DETACHING：解关联中
•  DETACHFAILED：解关联失败（2小时后将异步强制解关联）
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AttachedTime(self):
        r"""关联时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttachedTime

    @AttachedTime.setter
    def AttachedTime(self, AttachedTime):
        self._AttachedTime = AttachedTime

    @property
    def Description(self):
        r"""备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._CcnId = params.get("CcnId")
        self._CidrBlock = params.get("CidrBlock")
        self._State = params.get("State")
        self._AttachedTime = params.get("AttachedTime")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Command(AbstractModel):
    r"""用户执行TAT命令的数据结构。

    """

    def __init__(self):
        r"""
        :param _Content: Base64编码后的命令内容，长度不可超过64KB。
        :type Content: str
        :param _Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。
        :type Timeout: int
        :param _WorkingDirectory: 命令执行路径，对于 SHELL 命令默认为 /root，对于 POWERSHELL 命令默认为 C:\Program Files\qcloud\tat_agent\workdir。
        :type WorkingDirectory: str
        :param _Username: 在 Lighthouse 实例中执行命令的用户名称。
默认情况下，在 Linux 实例中以 root 用户执行命令；在Windows 实例中以 System 用户执行命令。
        :type Username: str
        """
        self._Content = None
        self._Timeout = None
        self._WorkingDirectory = None
        self._Username = None

    @property
    def Content(self):
        r"""Base64编码后的命令内容，长度不可超过64KB。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Timeout(self):
        r"""命令超时时间，默认60秒。取值范围[1, 86400]。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def WorkingDirectory(self):
        r"""命令执行路径，对于 SHELL 命令默认为 /root，对于 POWERSHELL 命令默认为 C:\Program Files\qcloud\tat_agent\workdir。
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Username(self):
        r"""在 Lighthouse 实例中执行命令的用户名称。
默认情况下，在 Linux 实例中以 root 用户执行命令；在Windows 实例中以 System 用户执行命令。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Timeout = params.get("Timeout")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerEnv(AbstractModel):
    r"""容器环境变量

    """

    def __init__(self):
        r"""
        :param _Key: 环境变量Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 环境变量值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""环境变量Key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""环境变量值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class CreateBlueprintRequest(AbstractModel):
    r"""CreateBlueprint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintName: 镜像名称。最大长度60。
        :type BlueprintName: str
        :param _Description: 镜像描述。最大长度60。
        :type Description: str
        :param _InstanceId: 需要制作镜像的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _ForcePowerOff: 是否执行强制关机以制作镜像。
取值范围：
True：表示关机之后制作镜像
False：表示开机状态制作镜像
默认取值：True
开机状态制作镜像，可能导致部分数据未备份，影响数据安全。
        :type ForcePowerOff: bool
        :param _Tags: 标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :type Tags: list of Tag
        """
        self._BlueprintName = None
        self._Description = None
        self._InstanceId = None
        self._ForcePowerOff = None
        self._Tags = None

    @property
    def BlueprintName(self):
        r"""镜像名称。最大长度60。
        :rtype: str
        """
        return self._BlueprintName

    @BlueprintName.setter
    def BlueprintName(self, BlueprintName):
        self._BlueprintName = BlueprintName

    @property
    def Description(self):
        r"""镜像描述。最大长度60。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InstanceId(self):
        r"""需要制作镜像的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForcePowerOff(self):
        r"""是否执行强制关机以制作镜像。
取值范围：
True：表示关机之后制作镜像
False：表示开机状态制作镜像
默认取值：True
开机状态制作镜像，可能导致部分数据未备份，影响数据安全。
        :rtype: bool
        """
        return self._ForcePowerOff

    @ForcePowerOff.setter
    def ForcePowerOff(self, ForcePowerOff):
        self._ForcePowerOff = ForcePowerOff

    @property
    def Tags(self):
        r"""标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._BlueprintName = params.get("BlueprintName")
        self._Description = params.get("Description")
        self._InstanceId = params.get("InstanceId")
        self._ForcePowerOff = params.get("ForcePowerOff")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlueprintResponse(AbstractModel):
    r"""CreateBlueprint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintId: 自定义镜像ID。
        :type BlueprintId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BlueprintId = None
        self._RequestId = None

    @property
    def BlueprintId(self):
        r"""自定义镜像ID。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._RequestId = params.get("RequestId")


class CreateDiskBackupRequest(AbstractModel):
    r"""CreateDiskBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID，可通过 [DescribeDisks](https://cloud.tencent.com/document/api/1207/66093) 接口返回值中的 DiskId 获取。 
        :type DiskId: str
        :param _DiskBackupName: 云硬盘备份点名称，最大长度为 90 。
        :type DiskBackupName: str
        :param _Tags: 标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :type Tags: list of Tag
        """
        self._DiskId = None
        self._DiskBackupName = None
        self._Tags = None

    @property
    def DiskId(self):
        r"""云硬盘ID，可通过 [DescribeDisks](https://cloud.tencent.com/document/api/1207/66093) 接口返回值中的 DiskId 获取。 
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupName(self):
        r"""云硬盘备份点名称，最大长度为 90 。
        :rtype: str
        """
        return self._DiskBackupName

    @DiskBackupName.setter
    def DiskBackupName(self, DiskBackupName):
        self._DiskBackupName = DiskBackupName

    @property
    def Tags(self):
        r"""标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskBackupName = params.get("DiskBackupName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDiskBackupResponse(AbstractModel):
    r"""CreateDiskBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: 备份点ID。
        :type DiskBackupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskBackupId = None
        self._RequestId = None

    @property
    def DiskBackupId(self):
        r"""备份点ID。
        :rtype: str
        """
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._RequestId = params.get("RequestId")


class CreateDisksRequest(AbstractModel):
    r"""CreateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区。可通过[DescribeZones](https://cloud.tencent.com/document/product/1207/57513)返回值中的Zone获取。
        :type Zone: str
        :param _DiskSize: 云硬盘大小, 单位: GB。
        :type DiskSize: int
        :param _DiskType: 云硬盘介质类型。取值: "CLOUD_PREMIUM"(高性能云盘), "CLOUD_SSD"(SSD云硬盘)。
        :type DiskType: str
        :param _DiskChargePrepaid: 云硬盘包年包月相关参数设置。
        :type DiskChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.DiskChargePrepaid`
        :param _DiskName: 云硬盘名称。最大长度60。
        :type DiskName: str
        :param _DiskCount: 云硬盘个数。取值范围: [1, 30]。默认值: 1。
        :type DiskCount: int
        :param _DiskBackupQuota: 指定云硬盘备份点配额，取值范围: [0, 500]。不传时默认为不带备份点配额。
        :type DiskBackupQuota: int
        :param _AutoVoucher: 是否自动使用代金券。默认不使用。
        :type AutoVoucher: bool
        :param _AutoMountConfiguration: 自动挂载并初始化数据盘。
        :type AutoMountConfiguration: :class:`tencentcloud.lighthouse.v20200324.models.AutoMountConfiguration`
        :param _Tags: 标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :type Tags: list of Tag
        """
        self._Zone = None
        self._DiskSize = None
        self._DiskType = None
        self._DiskChargePrepaid = None
        self._DiskName = None
        self._DiskCount = None
        self._DiskBackupQuota = None
        self._AutoVoucher = None
        self._AutoMountConfiguration = None
        self._Tags = None

    @property
    def Zone(self):
        r"""可用区。可通过[DescribeZones](https://cloud.tencent.com/document/product/1207/57513)返回值中的Zone获取。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DiskSize(self):
        r"""云硬盘大小, 单位: GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        r"""云硬盘介质类型。取值: "CLOUD_PREMIUM"(高性能云盘), "CLOUD_SSD"(SSD云硬盘)。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskChargePrepaid(self):
        r"""云硬盘包年包月相关参数设置。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DiskChargePrepaid`
        """
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskName(self):
        r"""云硬盘名称。最大长度60。
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def DiskCount(self):
        r"""云硬盘个数。取值范围: [1, 30]。默认值: 1。
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskBackupQuota(self):
        r"""指定云硬盘备份点配额，取值范围: [0, 500]。不传时默认为不带备份点配额。
        :rtype: int
        """
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券。默认不使用。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def AutoMountConfiguration(self):
        r"""自动挂载并初始化数据盘。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.AutoMountConfiguration`
        """
        return self._AutoMountConfiguration

    @AutoMountConfiguration.setter
    def AutoMountConfiguration(self, AutoMountConfiguration):
        self._AutoMountConfiguration = AutoMountConfiguration

    @property
    def Tags(self):
        r"""标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskName = params.get("DiskName")
        self._DiskCount = params.get("DiskCount")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        self._AutoVoucher = params.get("AutoVoucher")
        if params.get("AutoMountConfiguration") is not None:
            self._AutoMountConfiguration = AutoMountConfiguration()
            self._AutoMountConfiguration._deserialize(params.get("AutoMountConfiguration"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisksResponse(AbstractModel):
    r"""CreateDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIdSet: 当通过本接口来创建云硬盘时会返回该参数，表示一个或多个云硬盘ID。返回云硬盘ID列表并不代表云硬盘创建成功。

可根据 [DescribeDisks](https://cloud.tencent.com/document/product/1207/66093) 接口查询返回的DiskSet中对应云硬盘的ID的状态来判断创建是否完成；如果云硬盘状态由“PENDING”变为“UNATTACHED”或“ATTACHED”，则为创建成功。
        :type DiskIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskIdSet = None
        self._RequestId = None

    @property
    def DiskIdSet(self):
        r"""当通过本接口来创建云硬盘时会返回该参数，表示一个或多个云硬盘ID。返回云硬盘ID列表并不代表云硬盘创建成功。

可根据 [DescribeDisks](https://cloud.tencent.com/document/product/1207/66093) 接口查询返回的DiskSet中对应云硬盘的ID的状态来判断创建是否完成；如果云硬盘状态由“PENDING”变为“UNATTACHED”或“ATTACHED”，则为创建成功。
        :rtype: list of str
        """
        return self._DiskIdSet

    @DiskIdSet.setter
    def DiskIdSet(self, DiskIdSet):
        self._DiskIdSet = DiskIdSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiskIdSet = params.get("DiskIdSet")
        self._RequestId = params.get("RequestId")


class CreateFirewallRulesRequest(AbstractModel):
    r"""CreateFirewallRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _FirewallRules: 防火墙规则列表。
        :type FirewallRules: list of FirewallRule
        :param _FirewallVersion: 防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :type FirewallVersion: int
        """
        self._InstanceId = None
        self._FirewallRules = None
        self._FirewallVersion = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FirewallRules(self):
        r"""防火墙规则列表。
        :rtype: list of FirewallRule
        """
        return self._FirewallRules

    @FirewallRules.setter
    def FirewallRules(self, FirewallRules):
        self._FirewallRules = FirewallRules

    @property
    def FirewallVersion(self):
        r"""防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :rtype: int
        """
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self._FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._FirewallRules.append(obj)
        self._FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFirewallRulesResponse(AbstractModel):
    r"""CreateFirewallRules返回参数结构体

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


class CreateFirewallTemplateRequest(AbstractModel):
    r"""CreateFirewallTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _TemplateRules: 防火墙规则列表。
        :type TemplateRules: list of FirewallRule
        """
        self._TemplateName = None
        self._TemplateRules = None

    @property
    def TemplateName(self):
        r"""模板名称。
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateRules(self):
        r"""防火墙规则列表。
        :rtype: list of FirewallRule
        """
        return self._TemplateRules

    @TemplateRules.setter
    def TemplateRules(self, TemplateRules):
        self._TemplateRules = TemplateRules


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TemplateRules") is not None:
            self._TemplateRules = []
            for item in params.get("TemplateRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._TemplateRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFirewallTemplateResponse(AbstractModel):
    r"""CreateFirewallTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。
        :type TemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。
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


class CreateFirewallTemplateRulesRequest(AbstractModel):
    r"""CreateFirewallTemplateRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :type TemplateId: str
        :param _TemplateRules: 防火墙模板规则列表。
        :type TemplateRules: list of FirewallRule
        """
        self._TemplateId = None
        self._TemplateRules = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateRules(self):
        r"""防火墙模板规则列表。
        :rtype: list of FirewallRule
        """
        return self._TemplateRules

    @TemplateRules.setter
    def TemplateRules(self, TemplateRules):
        self._TemplateRules = TemplateRules


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("TemplateRules") is not None:
            self._TemplateRules = []
            for item in params.get("TemplateRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._TemplateRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFirewallTemplateRulesResponse(AbstractModel):
    r"""CreateFirewallTemplateRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateRuleIdSet: 规则ID列表。
        :type TemplateRuleIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateRuleIdSet = None
        self._RequestId = None

    @property
    def TemplateRuleIdSet(self):
        r"""规则ID列表。
        :rtype: list of str
        """
        return self._TemplateRuleIdSet

    @TemplateRuleIdSet.setter
    def TemplateRuleIdSet(self, TemplateRuleIdSet):
        self._TemplateRuleIdSet = TemplateRuleIdSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateRuleIdSet = params.get("TemplateRuleIdSet")
        self._RequestId = params.get("RequestId")


class CreateInstanceSnapshotRequest(AbstractModel):
    r"""CreateInstanceSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要创建快照的实例 ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/product/1207/47573) 接口返回值中的 InstanceId	获取。
        :type InstanceId: str
        :param _SnapshotName: 快照名称，最长为 60 个字符。
        :type SnapshotName: str
        :param _Tags: 标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :type Tags: list of Tag
        """
        self._InstanceId = None
        self._SnapshotName = None
        self._Tags = None

    @property
    def InstanceId(self):
        r"""需要创建快照的实例 ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/product/1207/47573) 接口返回值中的 InstanceId	获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SnapshotName(self):
        r"""快照名称，最长为 60 个字符。
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Tags(self):
        r"""标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SnapshotName = params.get("SnapshotName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceSnapshotResponse(AbstractModel):
    r"""CreateInstanceSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照 ID。
        :type SnapshotId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        r"""快照 ID。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    r"""CreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BundleId: 套餐ID。可以通过调用 [DescribeBundles](https://cloud.tencent.com/document/api/1207/47575) 接口获取。
        :type BundleId: str
        :param _BlueprintId: 镜像ID。可以通过调用 [DescribeBlueprints](https://cloud.tencent.com/document/api/1207/47689) 接口获取。
        :type BlueprintId: str
        :param _InstanceChargePrepaid: 当前实例仅支持预付费模式，即包年包月相关参数设置，单位（月）。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param _InstanceName: 实例显示名称。
        :type InstanceName: str
        :param _InstanceCount: 购买实例数量。包年包月实例取值范围：[1，30]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量
        :type InstanceCount: int
        :param _Zones: 可用区列表。
不填此参数，表示为随机可用区。
可通过 <a href="https://cloud.tencent.com/document/product/1207/57513" target="_blank">DescribeZones</a>接口获取指定地域下的可用区列表信息
        :type Zones: list of str
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _LoginConfiguration: 实例登录密码信息配置。默认缺失情况下代表用户选择实例创建后设置登录密码。
        :type LoginConfiguration: :class:`tencentcloud.lighthouse.v20200324.models.LoginConfiguration`
        :param _Containers: 要创建的容器配置列表。
        :type Containers: list of DockerContainerConfiguration
        :param _AutoVoucher: 是否自动使用代金券。默认不使用。
        :type AutoVoucher: bool
        :param _FirewallTemplateId: 防火墙模板ID。若不指定该参数，则使用默认防火墙策略。
        :type FirewallTemplateId: str
        :param _Tags: 标签键和标签值。
如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。
同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。
如果标签不存在会为您自动创建标签。
数组最多支持10个元素。
        :type Tags: list of Tag
        :param _InitCommand: 创建实例后自动执行的命令。
        :type InitCommand: :class:`tencentcloud.lighthouse.v20200324.models.Command`
        :param _DomainName: 主域名。
注意：域名指定后，仅支持购买一台实例（参数InstanceCount=1）。
        :type DomainName: str
        :param _Subdomain: 子域名。
注意：域名指定后，仅支持购买一台实例（参数InstanceCount=1）。
        :type Subdomain: str
        """
        self._BundleId = None
        self._BlueprintId = None
        self._InstanceChargePrepaid = None
        self._InstanceName = None
        self._InstanceCount = None
        self._Zones = None
        self._DryRun = None
        self._ClientToken = None
        self._LoginConfiguration = None
        self._Containers = None
        self._AutoVoucher = None
        self._FirewallTemplateId = None
        self._Tags = None
        self._InitCommand = None
        self._DomainName = None
        self._Subdomain = None

    @property
    def BundleId(self):
        r"""套餐ID。可以通过调用 [DescribeBundles](https://cloud.tencent.com/document/api/1207/47575) 接口获取。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BlueprintId(self):
        r"""镜像ID。可以通过调用 [DescribeBlueprints](https://cloud.tencent.com/document/api/1207/47689) 接口获取。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def InstanceChargePrepaid(self):
        r"""当前实例仅支持预付费模式，即包年包月相关参数设置，单位（月）。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。该参数必传。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceName(self):
        r"""实例显示名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceCount(self):
        r"""购买实例数量。包年包月实例取值范围：[1，30]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Zones(self):
        r"""可用区列表。
不填此参数，表示为随机可用区。
可通过 <a href="https://cloud.tencent.com/document/product/1207/57513" target="_blank">DescribeZones</a>接口获取指定地域下的可用区列表信息
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def DryRun(self):
        r"""是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ClientToken(self):
        r"""用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def LoginConfiguration(self):
        r"""实例登录密码信息配置。默认缺失情况下代表用户选择实例创建后设置登录密码。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.LoginConfiguration`
        """
        return self._LoginConfiguration

    @LoginConfiguration.setter
    def LoginConfiguration(self, LoginConfiguration):
        self._LoginConfiguration = LoginConfiguration

    @property
    def Containers(self):
        r"""要创建的容器配置列表。
        :rtype: list of DockerContainerConfiguration
        """
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券。默认不使用。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def FirewallTemplateId(self):
        r"""防火墙模板ID。若不指定该参数，则使用默认防火墙策略。
        :rtype: str
        """
        return self._FirewallTemplateId

    @FirewallTemplateId.setter
    def FirewallTemplateId(self, FirewallTemplateId):
        self._FirewallTemplateId = FirewallTemplateId

    @property
    def Tags(self):
        r"""标签键和标签值。
如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。
同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。
如果标签不存在会为您自动创建标签。
数组最多支持10个元素。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InitCommand(self):
        r"""创建实例后自动执行的命令。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.Command`
        """
        return self._InitCommand

    @InitCommand.setter
    def InitCommand(self, InitCommand):
        self._InitCommand = InitCommand

    @property
    def DomainName(self):
        r"""主域名。
注意：域名指定后，仅支持购买一台实例（参数InstanceCount=1）。
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Subdomain(self):
        r"""子域名。
注意：域名指定后，仅支持购买一台实例（参数InstanceCount=1）。
        :rtype: str
        """
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain


    def _deserialize(self, params):
        self._BundleId = params.get("BundleId")
        self._BlueprintId = params.get("BlueprintId")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceName = params.get("InstanceName")
        self._InstanceCount = params.get("InstanceCount")
        self._Zones = params.get("Zones")
        self._DryRun = params.get("DryRun")
        self._ClientToken = params.get("ClientToken")
        if params.get("LoginConfiguration") is not None:
            self._LoginConfiguration = LoginConfiguration()
            self._LoginConfiguration._deserialize(params.get("LoginConfiguration"))
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = DockerContainerConfiguration()
                obj._deserialize(item)
                self._Containers.append(obj)
        self._AutoVoucher = params.get("AutoVoucher")
        self._FirewallTemplateId = params.get("FirewallTemplateId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("InitCommand") is not None:
            self._InitCommand = Command()
            self._InitCommand._deserialize(params.get("InitCommand"))
        self._DomainName = params.get("DomainName")
        self._Subdomain = params.get("Subdomain")
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
        :param _InstanceIdSet: 当通过本接口来创建实例时会返回该参数，表示一个或多个实例ID。返回实例ID列表并不代表实例创建成功。

可根据<a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询返回的InstancesSet中对应实例的ID的状态来判断创建是否完成；如果实例状态由“启动中”变为“运行中”，则为创建成功。
        :type InstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        r"""当通过本接口来创建实例时会返回该参数，表示一个或多个实例ID。返回实例ID列表并不代表实例创建成功。

可根据<a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询返回的InstancesSet中对应实例的ID的状态来判断创建是否完成；如果实例状态由“启动中”变为“运行中”，则为创建成功。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    r"""CreateKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过 25 个字符。
        :type KeyName: str
        :param _Tags: 标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :type Tags: list of Tag
        """
        self._KeyName = None
        self._Tags = None

    @property
    def KeyName(self):
        r"""密钥对名称，可由数字，字母和下划线组成，长度不超过 25 个字符。
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def Tags(self):
        r"""标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    r"""CreateKeyPair返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyPair: 密钥对信息。
        :type KeyPair: :class:`tencentcloud.lighthouse.v20200324.models.KeyPair`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyPair = None
        self._RequestId = None

    @property
    def KeyPair(self):
        r"""密钥对信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.KeyPair`
        """
        return self._KeyPair

    @KeyPair.setter
    def KeyPair(self, KeyPair):
        self._KeyPair = KeyPair

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self._KeyPair = KeyPair()
            self._KeyPair._deserialize(params.get("KeyPair"))
        self._RequestId = params.get("RequestId")


class CreateMcpServerRequest(AbstractModel):
    r"""CreateMcpServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _Name: MCP Server名称。最大长度：64
        :type Name: str
        :param _Command: Base64编码后的MCP Server启动命令。最大长度：2048
        :type Command: str
        :param _Description: MCP Server备注。最大长度：2048
        :type Description: str
        :param _Envs: MCP Server环境变量。最大长度：10
        :type Envs: list of McpServerEnv
        :param _TransportType: 传输类型。枚举值如下：

<li>STREAMABLE_HTTP：HTTP协议的流式传输方式。未传传输类型字段时，默认创建此类型的MCP Server</li>
<li>SSE：Server-Sent Events，服务器发送事件</li>
        :type TransportType: str
        """
        self._InstanceId = None
        self._Name = None
        self._Command = None
        self._Description = None
        self._Envs = None
        self._TransportType = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""MCP Server名称。最大长度：64
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Command(self):
        r"""Base64编码后的MCP Server启动命令。最大长度：2048
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Description(self):
        r"""MCP Server备注。最大长度：2048
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Envs(self):
        r"""MCP Server环境变量。最大长度：10
        :rtype: list of McpServerEnv
        """
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def TransportType(self):
        r"""传输类型。枚举值如下：

<li>STREAMABLE_HTTP：HTTP协议的流式传输方式。未传传输类型字段时，默认创建此类型的MCP Server</li>
<li>SSE：Server-Sent Events，服务器发送事件</li>
        :rtype: str
        """
        return self._TransportType

    @TransportType.setter
    def TransportType(self, TransportType):
        self._TransportType = TransportType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Command = params.get("Command")
        self._Description = params.get("Description")
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = McpServerEnv()
                obj._deserialize(item)
                self._Envs.append(obj)
        self._TransportType = params.get("TransportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMcpServerResponse(AbstractModel):
    r"""CreateMcpServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _McpServerId: MCP Server ID。
        :type McpServerId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._McpServerId = None
        self._RequestId = None

    @property
    def McpServerId(self):
        r"""MCP Server ID。
        :rtype: str
        """
        return self._McpServerId

    @McpServerId.setter
    def McpServerId(self, McpServerId):
        self._McpServerId = McpServerId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._McpServerId = params.get("McpServerId")
        self._RequestId = params.get("RequestId")


class DataDiskPrice(AbstractModel):
    r"""数据盘价格

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID。
        :type DiskId: str
        :param _OriginalDiskPrice: 云硬盘单价。
        :type OriginalDiskPrice: float
        :param _OriginalPrice: 云硬盘总价。
        :type OriginalPrice: float
        :param _Discount: 折扣。
        :type Discount: float
        :param _DiscountPrice: 折后总价。
        :type DiscountPrice: float
        :param _InstanceId: 数据盘挂载的实例ID。
        :type InstanceId: str
        """
        self._DiskId = None
        self._OriginalDiskPrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None
        self._InstanceId = None

    @property
    def DiskId(self):
        r"""云硬盘ID。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def OriginalDiskPrice(self):
        r"""云硬盘单价。
        :rtype: float
        """
        return self._OriginalDiskPrice

    @OriginalDiskPrice.setter
    def OriginalDiskPrice(self, OriginalDiskPrice):
        self._OriginalDiskPrice = OriginalDiskPrice

    @property
    def OriginalPrice(self):
        r"""云硬盘总价。
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        r"""折扣。
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        r"""折后总价。
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def InstanceId(self):
        r"""数据盘挂载的实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._OriginalDiskPrice = params.get("OriginalDiskPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlueprintsRequest(AbstractModel):
    r"""DeleteBlueprints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintIds: 镜像ID列表。镜像ID，可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :type BlueprintIds: list of str
        """
        self._BlueprintIds = None

    @property
    def BlueprintIds(self):
        r"""镜像ID列表。镜像ID，可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :rtype: list of str
        """
        return self._BlueprintIds

    @BlueprintIds.setter
    def BlueprintIds(self, BlueprintIds):
        self._BlueprintIds = BlueprintIds


    def _deserialize(self, params):
        self._BlueprintIds = params.get("BlueprintIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlueprintsResponse(AbstractModel):
    r"""DeleteBlueprints返回参数结构体

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


class DeleteDiskBackupsRequest(AbstractModel):
    r"""DeleteDiskBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: 云硬盘备份点ID列表，可通过 [DescribeDiskBackups](https://cloud.tencent.com/document/api/1207/84379)接口查询。列表长度最大值为100。
        :type DiskBackupIds: list of str
        """
        self._DiskBackupIds = None

    @property
    def DiskBackupIds(self):
        r"""云硬盘备份点ID列表，可通过 [DescribeDiskBackups](https://cloud.tencent.com/document/api/1207/84379)接口查询。列表长度最大值为100。
        :rtype: list of str
        """
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds


    def _deserialize(self, params):
        self._DiskBackupIds = params.get("DiskBackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDiskBackupsResponse(AbstractModel):
    r"""DeleteDiskBackups返回参数结构体

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


class DeleteFirewallRulesRequest(AbstractModel):
    r"""DeleteFirewallRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _FirewallRules: 防火墙规则列表。
        :type FirewallRules: list of FirewallRule
        :param _FirewallVersion: 防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :type FirewallVersion: int
        """
        self._InstanceId = None
        self._FirewallRules = None
        self._FirewallVersion = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FirewallRules(self):
        r"""防火墙规则列表。
        :rtype: list of FirewallRule
        """
        return self._FirewallRules

    @FirewallRules.setter
    def FirewallRules(self, FirewallRules):
        self._FirewallRules = FirewallRules

    @property
    def FirewallVersion(self):
        r"""防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :rtype: int
        """
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self._FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._FirewallRules.append(obj)
        self._FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFirewallRulesResponse(AbstractModel):
    r"""DeleteFirewallRules返回参数结构体

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


class DeleteFirewallTemplateRequest(AbstractModel):
    r"""DeleteFirewallTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
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
        


class DeleteFirewallTemplateResponse(AbstractModel):
    r"""DeleteFirewallTemplate返回参数结构体

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


class DeleteFirewallTemplateRulesRequest(AbstractModel):
    r"""DeleteFirewallTemplateRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :type TemplateId: str
        :param _TemplateRuleIds: 防火墙模板规则ID列表。可通过[DescribeFirewallTemplateRules](https://cloud.tencent.com/document/product/1207/96875)接口返回值字段TemplateRuleSet获取。

        :type TemplateRuleIds: list of str
        """
        self._TemplateId = None
        self._TemplateRuleIds = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateRuleIds(self):
        r"""防火墙模板规则ID列表。可通过[DescribeFirewallTemplateRules](https://cloud.tencent.com/document/product/1207/96875)接口返回值字段TemplateRuleSet获取。

        :rtype: list of str
        """
        return self._TemplateRuleIds

    @TemplateRuleIds.setter
    def TemplateRuleIds(self, TemplateRuleIds):
        self._TemplateRuleIds = TemplateRuleIds


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateRuleIds = params.get("TemplateRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFirewallTemplateRulesResponse(AbstractModel):
    r"""DeleteFirewallTemplateRules返回参数结构体

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


class DeleteKeyPairsRequest(AbstractModel):
    r"""DeleteKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 密钥对 ID 列表，每次请求批量密钥对的上限为 10。可通过[DescribeKeyPairs](https://cloud.tencent.com/document/api/1207/55540)接口返回值中的KeyId获取。
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        r"""密钥对 ID 列表，每次请求批量密钥对的上限为 10。可通过[DescribeKeyPairs](https://cloud.tencent.com/document/api/1207/55540)接口返回值中的KeyId获取。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKeyPairsResponse(AbstractModel):
    r"""DeleteKeyPairs返回参数结构体

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


class DeleteSnapshotsRequest(AbstractModel):
    r"""DeleteSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: 要删除的快照 ID 列表，每次请求批量快照的上限为10个，可通过 <a href="https://cloud.tencent.com/document/product/1207/54388" target="_blank">DescribeSnapshots</a>查询。
        :type SnapshotIds: list of str
        """
        self._SnapshotIds = None

    @property
    def SnapshotIds(self):
        r"""要删除的快照 ID 列表，每次请求批量快照的上限为10个，可通过 <a href="https://cloud.tencent.com/document/product/1207/54388" target="_blank">DescribeSnapshots</a>查询。
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
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


class DeniedAction(AbstractModel):
    r"""限制操作。

    """

    def __init__(self):
        r"""
        :param _Action: 限制操作名。
        :type Action: str
        :param _Code: 限制操作消息码。
        :type Code: str
        :param _Message: 限制操作消息。
        :type Message: str
        """
        self._Action = None
        self._Code = None
        self._Message = None

    @property
    def Action(self):
        r"""限制操作名。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Code(self):
        r"""限制操作消息码。
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""限制操作消息。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllScenesRequest(AbstractModel):
    r"""DescribeAllScenes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneIds: 使用场景ID列表。可通过[DescribeAllScenes](https://cloud.tencent.com/document/product/1207/83513)接口返回值中的SceneId获取。
        :type SceneIds: list of str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._SceneIds = None
        self._Offset = None
        self._Limit = None

    @property
    def SceneIds(self):
        r"""使用场景ID列表。可通过[DescribeAllScenes](https://cloud.tencent.com/document/product/1207/83513)接口返回值中的SceneId获取。
        :rtype: list of str
        """
        return self._SceneIds

    @SceneIds.setter
    def SceneIds(self, SceneIds):
        self._SceneIds = SceneIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SceneIds = params.get("SceneIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllScenesResponse(AbstractModel):
    r"""DescribeAllScenes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneInfoSet: 使用场景详细信息列表。
        :type SceneInfoSet: list of SceneInfo
        :param _TotalCount: 使用场景详细信息总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SceneInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SceneInfoSet(self):
        r"""使用场景详细信息列表。
        :rtype: list of SceneInfo
        """
        return self._SceneInfoSet

    @SceneInfoSet.setter
    def SceneInfoSet(self, SceneInfoSet):
        self._SceneInfoSet = SceneInfoSet

    @property
    def TotalCount(self):
        r"""使用场景详细信息总数量。
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
        if params.get("SceneInfoSet") is not None:
            self._SceneInfoSet = []
            for item in params.get("SceneInfoSet"):
                obj = SceneInfo()
                obj._deserialize(item)
                self._SceneInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBlueprintInstancesRequest(AbstractModel):
    r"""DescribeBlueprintInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。 当前最多支持1个。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。 当前最多支持1个。
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
        


class DescribeBlueprintInstancesResponse(AbstractModel):
    r"""DescribeBlueprintInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的镜像实例数量。
        :type TotalCount: int
        :param _BlueprintInstanceSet: 镜像实例列表信息。
        :type BlueprintInstanceSet: list of BlueprintInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlueprintInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的镜像实例数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlueprintInstanceSet(self):
        r"""镜像实例列表信息。
        :rtype: list of BlueprintInstance
        """
        return self._BlueprintInstanceSet

    @BlueprintInstanceSet.setter
    def BlueprintInstanceSet(self, BlueprintInstanceSet):
        self._BlueprintInstanceSet = BlueprintInstanceSet

    @property
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
        if params.get("BlueprintInstanceSet") is not None:
            self._BlueprintInstanceSet = []
            for item in params.get("BlueprintInstanceSet"):
                obj = BlueprintInstance()
                obj._deserialize(item)
                self._BlueprintInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBlueprintsRequest(AbstractModel):
    r"""DescribeBlueprints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintIds: 镜像 ID 列表。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值字段BlueprintSet获取。列表长度最大值为100。
        :type BlueprintIds: list of str
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param _Filters: 过滤器列表。
<li>blueprint-id</li>按照【镜像 ID】进行过滤。
类型：String
必选：否
镜像 ID ，可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值字段BlueprintSet获取。
<li>blueprint-type</li>按照【镜像类型】进行过滤。
取值：APP_OS（应用镜像 ）；PURE_OS（系统镜像）；DOCKER（Docker容器镜像）；PRIVATE（自定义镜像）；SHARED（共享镜像）。
类型：String
必选：否
<li>platform-type</li>按照【镜像平台类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）。
类型：String
必选：否
<li>blueprint-name</li>按照【镜像名称】进行过滤。
类型：String
必选：否
<li>blueprint-state</li>按照【镜像状态】进行过滤。
类型：String
必选：否
镜像状态，可通过[数据结构Blueprint](https://cloud.tencent.com/document/api/1207/47576#Blueprint)中的BlueprintState来获取。
<li>scene-id</li>按照【使用场景Id】进行过滤。
类型：String
必选：否
场景Id，可通过[查看使用场景列表](https://cloud.tencent.com/document/product/1207/83512)接口获取。
<li>tag-key</li>
按照【标签键】进行过滤。 类型：String 必选：否
<li>tag-value</li>
按照【标签值】进行过滤。 类型：String 必选：否
<li>tag:tag-key</li>
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 100。参数不支持同时指定 BlueprintIds (可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值字段BlueprintSet获取BlueprintId)和 Filters 。
        :type Filters: list of Filter
        """
        self._BlueprintIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def BlueprintIds(self):
        r"""镜像 ID 列表。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值字段BlueprintSet获取。列表长度最大值为100。
        :rtype: list of str
        """
        return self._BlueprintIds

    @BlueprintIds.setter
    def BlueprintIds(self, BlueprintIds):
        self._BlueprintIds = BlueprintIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤器列表。
<li>blueprint-id</li>按照【镜像 ID】进行过滤。
类型：String
必选：否
镜像 ID ，可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值字段BlueprintSet获取。
<li>blueprint-type</li>按照【镜像类型】进行过滤。
取值：APP_OS（应用镜像 ）；PURE_OS（系统镜像）；DOCKER（Docker容器镜像）；PRIVATE（自定义镜像）；SHARED（共享镜像）。
类型：String
必选：否
<li>platform-type</li>按照【镜像平台类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）。
类型：String
必选：否
<li>blueprint-name</li>按照【镜像名称】进行过滤。
类型：String
必选：否
<li>blueprint-state</li>按照【镜像状态】进行过滤。
类型：String
必选：否
镜像状态，可通过[数据结构Blueprint](https://cloud.tencent.com/document/api/1207/47576#Blueprint)中的BlueprintState来获取。
<li>scene-id</li>按照【使用场景Id】进行过滤。
类型：String
必选：否
场景Id，可通过[查看使用场景列表](https://cloud.tencent.com/document/product/1207/83512)接口获取。
<li>tag-key</li>
按照【标签键】进行过滤。 类型：String 必选：否
<li>tag-value</li>
按照【标签值】进行过滤。 类型：String 必选：否
<li>tag:tag-key</li>
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 100。参数不支持同时指定 BlueprintIds (可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值字段BlueprintSet获取BlueprintId)和 Filters 。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BlueprintIds = params.get("BlueprintIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeBlueprintsResponse(AbstractModel):
    r"""DescribeBlueprints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的镜像数量。
        :type TotalCount: int
        :param _BlueprintSet: 镜像详细信息列表。
        :type BlueprintSet: list of Blueprint
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlueprintSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的镜像数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlueprintSet(self):
        r"""镜像详细信息列表。
        :rtype: list of Blueprint
        """
        return self._BlueprintSet

    @BlueprintSet.setter
    def BlueprintSet(self, BlueprintSet):
        self._BlueprintSet = BlueprintSet

    @property
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
        if params.get("BlueprintSet") is not None:
            self._BlueprintSet = []
            for item in params.get("BlueprintSet"):
                obj = Blueprint()
                obj._deserialize(item)
                self._BlueprintSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBundleDiscountRequest(AbstractModel):
    r"""DescribeBundleDiscount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BundleId: 套餐 ID。可通过[DescribeBundles](https://cloud.tencent.com/document/product/1207/47575)接口返回值中的BundleId获取。
        :type BundleId: str
        """
        self._BundleId = None

    @property
    def BundleId(self):
        r"""套餐 ID。可通过[DescribeBundles](https://cloud.tencent.com/document/product/1207/47575)接口返回值中的BundleId获取。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId


    def _deserialize(self, params):
        self._BundleId = params.get("BundleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBundleDiscountResponse(AbstractModel):
    r"""DescribeBundleDiscount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Currency: 币种：CNY人民币，USD 美元。
        :type Currency: str
        :param _DiscountDetail: 折扣梯度详情，每个梯度包含的信息有：时长，折扣数，总价，折扣价，折扣详情（用户折扣、官网折扣、最终折扣）。
        :type DiscountDetail: list of DiscountDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Currency = None
        self._DiscountDetail = None
        self._RequestId = None

    @property
    def Currency(self):
        r"""币种：CNY人民币，USD 美元。
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiscountDetail(self):
        r"""折扣梯度详情，每个梯度包含的信息有：时长，折扣数，总价，折扣价，折扣详情（用户折扣、官网折扣、最终折扣）。
        :rtype: list of DiscountDetail
        """
        return self._DiscountDetail

    @DiscountDetail.setter
    def DiscountDetail(self, DiscountDetail):
        self._DiscountDetail = DiscountDetail

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Currency = params.get("Currency")
        if params.get("DiscountDetail") is not None:
            self._DiscountDetail = []
            for item in params.get("DiscountDetail"):
                obj = DiscountDetail()
                obj._deserialize(item)
                self._DiscountDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBundlesRequest(AbstractModel):
    r"""DescribeBundles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BundleIds: 套餐 ID 列表。每次请求批量套餐的上限为 100。可通过[DescribeBundles](https://cloud.tencent.com/document/product/1207/47575)接口返回值中的BundleId获取。
        :type BundleIds: list of str
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param _Filters: 过滤器列表。
<li>bundle-id</li>按照【套餐 ID】进行过滤。
类型：String
必选：否
<li>support-platform-type</li>按照【系统类型】进行过滤。
取值： LINUX_UNIX(Linux/Unix系统) ;WINDOWS(Windows 系统)
类型：String
必选：否
<li>bundle-type</li>按照 【套餐类型进行过滤】。
取值：GENERAL_BUNDLE (通用型套餐); STORAGE_BUNDLE(存储型套餐);ENTERPRISE_BUNDLE( 企业型套餐);EXCLUSIVE_BUNDLE(专属型套餐);BEFAST_BUNDLE(蜂驰型套餐);STARTER_BUNDLE(入门型套餐);CAREFREE_BUNDLE(无忧型套餐);RAZOR_SPEED_BUNDLE(锐驰型套餐)
类型：String
必选：否
<li>bundle-state</li>按照【套餐状态】进行过滤。
取值: ONLINE(在线); OFFLINE(下线);
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 BundleIds 和 Filters。
        :type Filters: list of Filter
        :param _Zones: 可用区列表。默认为全部可用区。
<li>可用区可通过接口 [DescribeZones](https://cloud.tencent.com/document/product/1207/57513) 查询</li>
        :type Zones: list of str
        """
        self._BundleIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Zones = None

    @property
    def BundleIds(self):
        r"""套餐 ID 列表。每次请求批量套餐的上限为 100。可通过[DescribeBundles](https://cloud.tencent.com/document/product/1207/47575)接口返回值中的BundleId获取。
        :rtype: list of str
        """
        return self._BundleIds

    @BundleIds.setter
    def BundleIds(self, BundleIds):
        self._BundleIds = BundleIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤器列表。
<li>bundle-id</li>按照【套餐 ID】进行过滤。
类型：String
必选：否
<li>support-platform-type</li>按照【系统类型】进行过滤。
取值： LINUX_UNIX(Linux/Unix系统) ;WINDOWS(Windows 系统)
类型：String
必选：否
<li>bundle-type</li>按照 【套餐类型进行过滤】。
取值：GENERAL_BUNDLE (通用型套餐); STORAGE_BUNDLE(存储型套餐);ENTERPRISE_BUNDLE( 企业型套餐);EXCLUSIVE_BUNDLE(专属型套餐);BEFAST_BUNDLE(蜂驰型套餐);STARTER_BUNDLE(入门型套餐);CAREFREE_BUNDLE(无忧型套餐);RAZOR_SPEED_BUNDLE(锐驰型套餐)
类型：String
必选：否
<li>bundle-state</li>按照【套餐状态】进行过滤。
取值: ONLINE(在线); OFFLINE(下线);
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 BundleIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Zones(self):
        r"""可用区列表。默认为全部可用区。
<li>可用区可通过接口 [DescribeZones](https://cloud.tencent.com/document/product/1207/57513) 查询</li>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._BundleIds = params.get("BundleIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBundlesResponse(AbstractModel):
    r"""DescribeBundles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BundleSet: 套餐详细信息列表。
        :type BundleSet: list of Bundle
        :param _TotalCount: 符合要求的套餐总数，用于分页展示。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BundleSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BundleSet(self):
        r"""套餐详细信息列表。
        :rtype: list of Bundle
        """
        return self._BundleSet

    @BundleSet.setter
    def BundleSet(self, BundleSet):
        self._BundleSet = BundleSet

    @property
    def TotalCount(self):
        r"""符合要求的套餐总数，用于分页展示。
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
        if params.get("BundleSet") is not None:
            self._BundleSet = []
            for item in params.get("BundleSet"):
                obj = Bundle()
                obj._deserialize(item)
                self._BundleSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCcnAttachedInstancesRequest(AbstractModel):
    r"""DescribeCcnAttachedInstances请求参数结构体

    """


class DescribeCcnAttachedInstancesResponse(AbstractModel):
    r"""DescribeCcnAttachedInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CcnAttachedInstanceSet: 云联网关联的实例列表。
        :type CcnAttachedInstanceSet: list of CcnAttachedInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CcnAttachedInstanceSet = None
        self._RequestId = None

    @property
    def CcnAttachedInstanceSet(self):
        r"""云联网关联的实例列表。
        :rtype: list of CcnAttachedInstance
        """
        return self._CcnAttachedInstanceSet

    @CcnAttachedInstanceSet.setter
    def CcnAttachedInstanceSet(self, CcnAttachedInstanceSet):
        self._CcnAttachedInstanceSet = CcnAttachedInstanceSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CcnAttachedInstanceSet") is not None:
            self._CcnAttachedInstanceSet = []
            for item in params.get("CcnAttachedInstanceSet"):
                obj = CcnAttachedInstance()
                obj._deserialize(item)
                self._CcnAttachedInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskBackupsDeniedActionsRequest(AbstractModel):
    r"""DescribeDiskBackupsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: 云硬盘备份点 ID 列表, 可通过<a href="https://cloud.tencent.com/document/product/1207/84379" target="_blank">DescribeDiskBackups</a>接口查询。列表长度最大值为100。
        :type DiskBackupIds: list of str
        """
        self._DiskBackupIds = None

    @property
    def DiskBackupIds(self):
        r"""云硬盘备份点 ID 列表, 可通过<a href="https://cloud.tencent.com/document/product/1207/84379" target="_blank">DescribeDiskBackups</a>接口查询。列表长度最大值为100。
        :rtype: list of str
        """
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds


    def _deserialize(self, params):
        self._DiskBackupIds = params.get("DiskBackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskBackupsDeniedActionsResponse(AbstractModel):
    r"""DescribeDiskBackupsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupDeniedActionSet: 云硬盘备份点操作限制列表详细信息。
        :type DiskBackupDeniedActionSet: list of DiskBackupDeniedActions
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskBackupDeniedActionSet = None
        self._RequestId = None

    @property
    def DiskBackupDeniedActionSet(self):
        r"""云硬盘备份点操作限制列表详细信息。
        :rtype: list of DiskBackupDeniedActions
        """
        return self._DiskBackupDeniedActionSet

    @DiskBackupDeniedActionSet.setter
    def DiskBackupDeniedActionSet(self, DiskBackupDeniedActionSet):
        self._DiskBackupDeniedActionSet = DiskBackupDeniedActionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskBackupDeniedActionSet") is not None:
            self._DiskBackupDeniedActionSet = []
            for item in params.get("DiskBackupDeniedActionSet"):
                obj = DiskBackupDeniedActions()
                obj._deserialize(item)
                self._DiskBackupDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskBackupsRequest(AbstractModel):
    r"""DescribeDiskBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: 查询的云硬盘备份点ID列表。可通过[DescribeDiskBackups](https://cloud.tencent.com/document/product/1207/84379)接口返回值字段DiskBackupSet获取。列表长度最大值为100。参数不支持同时指定 DiskBackupIds 和 Filters。
        :type DiskBackupIds: list of str
        :param _Filters: 过滤器列表。
<li>disk-backup-id</li>按照【云硬盘备份点 ID】进行过滤。
类型：String
必选：否
<li>disk-id</li>按照【云硬盘 ID】进行过滤。
类型：String
必选：否
<li>disk-backup-state</li>按照【云硬盘备份点状态】进行过滤。
类型：String
必选：否
取值：参考数据结构 [DiskBackup](https://cloud.tencent.com/document/product/1207/47576#DiskBackup) 下的DiskBackupState取值。
<li>disk-usage</li>按照【云硬盘类型】进行过滤。
类型：String
必选：否
取值：
- SYSTEM_DISK - 系统盘
- DATA_DISK - 数据盘
<li>tag-key</li>
按照【标签键】进行过滤。 类型：String 必选：否
<li>tag-value</li>
按照【标签值】进行过滤。 类型：String 必选：否
<li>tag:tag-key</li>
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为5。参数不支持同时指定DiskBackupIds 和 Filters。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        """
        self._DiskBackupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def DiskBackupIds(self):
        r"""查询的云硬盘备份点ID列表。可通过[DescribeDiskBackups](https://cloud.tencent.com/document/product/1207/84379)接口返回值字段DiskBackupSet获取。列表长度最大值为100。参数不支持同时指定 DiskBackupIds 和 Filters。
        :rtype: list of str
        """
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds

    @property
    def Filters(self):
        r"""过滤器列表。
<li>disk-backup-id</li>按照【云硬盘备份点 ID】进行过滤。
类型：String
必选：否
<li>disk-id</li>按照【云硬盘 ID】进行过滤。
类型：String
必选：否
<li>disk-backup-state</li>按照【云硬盘备份点状态】进行过滤。
类型：String
必选：否
取值：参考数据结构 [DiskBackup](https://cloud.tencent.com/document/product/1207/47576#DiskBackup) 下的DiskBackupState取值。
<li>disk-usage</li>按照【云硬盘类型】进行过滤。
类型：String
必选：否
取值：
- SYSTEM_DISK - 系统盘
- DATA_DISK - 数据盘
<li>tag-key</li>
按照【标签键】进行过滤。 类型：String 必选：否
<li>tag-value</li>
按照【标签值】进行过滤。 类型：String 必选：否
<li>tag:tag-key</li>
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为5。参数不支持同时指定DiskBackupIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DiskBackupIds = params.get("DiskBackupIds")
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
        


class DescribeDiskBackupsResponse(AbstractModel):
    r"""DescribeDiskBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 云硬盘备份点的数量。
        :type TotalCount: int
        :param _DiskBackupSet: 云硬盘备份点信息列表。
        :type DiskBackupSet: list of DiskBackup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskBackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""云硬盘备份点的数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskBackupSet(self):
        r"""云硬盘备份点信息列表。
        :rtype: list of DiskBackup
        """
        return self._DiskBackupSet

    @DiskBackupSet.setter
    def DiskBackupSet(self, DiskBackupSet):
        self._DiskBackupSet = DiskBackupSet

    @property
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
        if params.get("DiskBackupSet") is not None:
            self._DiskBackupSet = []
            for item in params.get("DiskBackupSet"):
                obj = DiskBackup()
                obj._deserialize(item)
                self._DiskBackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskConfigsRequest(AbstractModel):
    r"""DescribeDiskConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤器列表。
<li>zone</li>按照【可用区】进行过滤。
类型：String
必选：否
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        r"""过滤器列表。
<li>zone</li>按照【可用区】进行过滤。
类型：String
必选：否
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
        


class DescribeDiskConfigsResponse(AbstractModel):
    r"""DescribeDiskConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskConfigSet: 云硬盘配置列表。
        :type DiskConfigSet: list of DiskConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskConfigSet = None
        self._RequestId = None

    @property
    def DiskConfigSet(self):
        r"""云硬盘配置列表。
        :rtype: list of DiskConfig
        """
        return self._DiskConfigSet

    @DiskConfigSet.setter
    def DiskConfigSet(self, DiskConfigSet):
        self._DiskConfigSet = DiskConfigSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskConfigSet") is not None:
            self._DiskConfigSet = []
            for item in params.get("DiskConfigSet"):
                obj = DiskConfig()
                obj._deserialize(item)
                self._DiskConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskDiscountRequest(AbstractModel):
    r"""DescribeDiskDiscount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskType: 云硬盘类型, 取值范围: CLOUD_PREMIUM: 高性能云硬盘，CLOUD_SSD: SSD云硬盘
        :type DiskType: str
        :param _DiskSize: 云硬盘大小, 单位: GB。
        :type DiskSize: int
        :param _DiskBackupQuota: 指定云硬盘备份点配额，不传时默认为不带备份点配额。目前只支持不带或设置[0 - 500]个云硬盘备份点配额。
        :type DiskBackupQuota: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskBackupQuota = None

    @property
    def DiskType(self):
        r"""云硬盘类型, 取值范围: CLOUD_PREMIUM: 高性能云硬盘，CLOUD_SSD: SSD云硬盘
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""云硬盘大小, 单位: GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskBackupQuota(self):
        r"""指定云硬盘备份点配额，不传时默认为不带备份点配额。目前只支持不带或设置[0 - 500]个云硬盘备份点配额。
        :rtype: int
        """
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskDiscountResponse(AbstractModel):
    r"""DescribeDiskDiscount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Currency: 币种：CNY人民币，USD 美元。
        :type Currency: str
        :param _DiscountDetail: 折扣梯度详情，每个梯度包含的信息有：时长，折扣数，总价，折扣价，折扣详情（用户折扣、官网折扣、最终折扣）。
        :type DiscountDetail: list of DiscountDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Currency = None
        self._DiscountDetail = None
        self._RequestId = None

    @property
    def Currency(self):
        r"""币种：CNY人民币，USD 美元。
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiscountDetail(self):
        r"""折扣梯度详情，每个梯度包含的信息有：时长，折扣数，总价，折扣价，折扣详情（用户折扣、官网折扣、最终折扣）。
        :rtype: list of DiscountDetail
        """
        return self._DiscountDetail

    @DiscountDetail.setter
    def DiscountDetail(self, DiscountDetail):
        self._DiscountDetail = DiscountDetail

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Currency = params.get("Currency")
        if params.get("DiscountDetail") is not None:
            self._DiscountDetail = []
            for item in params.get("DiscountDetail"):
                obj = DiscountDetail()
                obj._deserialize(item)
                self._DiscountDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisksDeniedActionsRequest(AbstractModel):
    r"""DescribeDisksDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksDeniedActionsResponse(AbstractModel):
    r"""DescribeDisksDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskDeniedActionSet: 云硬盘操作限制列表详细信息。
        :type DiskDeniedActionSet: list of DiskDeniedActions
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskDeniedActionSet = None
        self._RequestId = None

    @property
    def DiskDeniedActionSet(self):
        r"""云硬盘操作限制列表详细信息。
        :rtype: list of DiskDeniedActions
        """
        return self._DiskDeniedActionSet

    @DiskDeniedActionSet.setter
    def DiskDeniedActionSet(self, DiskDeniedActionSet):
        self._DiskDeniedActionSet = DiskDeniedActionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskDeniedActionSet") is not None:
            self._DiskDeniedActionSet = []
            for item in params.get("DiskDeniedActionSet"):
                obj = DiskDeniedActions()
                obj._deserialize(item)
                self._DiskDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    r"""DescribeDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值字段KeyPairSet获取。列表长度最大值为100。
        :type DiskIds: list of str
        :param _Filters: 过滤器列表。
disk-id
按照【云硬盘 ID】进行过滤。
类型：String
必选：否
instance-id
按照【实例ID】进行过滤。
类型：String
必选：否
disk-name
按照【云硬盘名称】进行过滤。
类型：String
必选：否
zone
按照【可用区】进行过滤。
类型：String
必选：否
disk-usage
按照【云硬盘类型】进行过滤。
类型：String
必选：否
取值：SYSTEM_DISK（系统盘）或 DATA_DISK（数据盘）
disk-state
按照【云硬盘状态】进行过滤。
类型：String
必选：否
取值：参考数据结构[Disk](https://cloud.tencent.com/document/api/1207/47576#Disk)中DiskState取值。
tag-key
按照【标签键】进行过滤。 类型：String 必选：否
tag-value
按照【标签值】进行过滤。 类型：String 必选：否
tag:tag-key
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 100。参数不支持同时指定 DiskIds 和 Filters。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _OrderField: 云硬盘列表排序的依据字段。取值范围："CREATED_TIME"：依据云硬盘的创建时间排序。 "EXPIRED_TIME"：依据云硬盘的到期时间排序。"DISK_SIZE"：依据云硬盘的大小排序。默认按云硬盘创建时间排序。
        :type OrderField: str
        :param _Order: 输出云硬盘列表的排列顺序。取值范围："ASC"：升序排列。 "DESC"：降序排列。默认按降序排列。
        :type Order: str
        """
        self._DiskIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderField = None
        self._Order = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值字段KeyPairSet获取。列表长度最大值为100。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Filters(self):
        r"""过滤器列表。
disk-id
按照【云硬盘 ID】进行过滤。
类型：String
必选：否
instance-id
按照【实例ID】进行过滤。
类型：String
必选：否
disk-name
按照【云硬盘名称】进行过滤。
类型：String
必选：否
zone
按照【可用区】进行过滤。
类型：String
必选：否
disk-usage
按照【云硬盘类型】进行过滤。
类型：String
必选：否
取值：SYSTEM_DISK（系统盘）或 DATA_DISK（数据盘）
disk-state
按照【云硬盘状态】进行过滤。
类型：String
必选：否
取值：参考数据结构[Disk](https://cloud.tencent.com/document/api/1207/47576#Disk)中DiskState取值。
tag-key
按照【标签键】进行过滤。 类型：String 必选：否
tag-value
按照【标签值】进行过滤。 类型：String 必选：否
tag:tag-key
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 100。参数不支持同时指定 DiskIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderField(self):
        r"""云硬盘列表排序的依据字段。取值范围："CREATED_TIME"：依据云硬盘的创建时间排序。 "EXPIRED_TIME"：依据云硬盘的到期时间排序。"DISK_SIZE"：依据云硬盘的大小排序。默认按云硬盘创建时间排序。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""输出云硬盘列表的排列顺序。取值范围："ASC"：升序排列。 "DESC"：降序排列。默认按降序排列。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    r"""DescribeDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskSet: 云硬盘信息列表。
        :type DiskSet: list of Disk
        :param _TotalCount: 符合条件的云硬盘信息数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DiskSet(self):
        r"""云硬盘信息列表。
        :rtype: list of Disk
        """
        return self._DiskSet

    @DiskSet.setter
    def DiskSet(self, DiskSet):
        self._DiskSet = DiskSet

    @property
    def TotalCount(self):
        r"""符合条件的云硬盘信息数量。
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
        if params.get("DiskSet") is not None:
            self._DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self._DiskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDisksReturnableRequest(AbstractModel):
    r"""DescribeDisksReturnable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。每次批量请求云硬盘的上限为 10。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :type DiskIds: list of str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._DiskIds = None
        self._Limit = None
        self._Offset = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。每次批量请求云硬盘的上限为 10。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksReturnableResponse(AbstractModel):
    r"""DescribeDisksReturnable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskReturnableSet: 可退还云硬盘详细信息列表。
        :type DiskReturnableSet: list of DiskReturnable
        :param _TotalCount: 符合条件的云硬盘数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskReturnableSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DiskReturnableSet(self):
        r"""可退还云硬盘详细信息列表。
        :rtype: list of DiskReturnable
        """
        return self._DiskReturnableSet

    @DiskReturnableSet.setter
    def DiskReturnableSet(self, DiskReturnableSet):
        self._DiskReturnableSet = DiskReturnableSet

    @property
    def TotalCount(self):
        r"""符合条件的云硬盘数量。
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
        if params.get("DiskReturnableSet") is not None:
            self._DiskReturnableSet = []
            for item in params.get("DiskReturnableSet"):
                obj = DiskReturnable()
                obj._deserialize(item)
                self._DiskReturnableSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDockerActivitiesRequest(AbstractModel):
    r"""DescribeDockerActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ActivityIds: Docker活动ID列表。可通过[DescribeDockerActivities](https://cloud.tencent.com/document/product/1207/95476)接口返回值中的ActivityId获取。
        :type ActivityIds: list of str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _CreatedTimeBegin: 活动创建时间的起始值，时间戳秒数。
        :type CreatedTimeBegin: int
        :param _CreatedTimeEnd: 活动创建时间的结束值，时间戳秒数。
        :type CreatedTimeEnd: int
        """
        self._InstanceId = None
        self._ActivityIds = None
        self._Offset = None
        self._Limit = None
        self._CreatedTimeBegin = None
        self._CreatedTimeEnd = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ActivityIds(self):
        r"""Docker活动ID列表。可通过[DescribeDockerActivities](https://cloud.tencent.com/document/product/1207/95476)接口返回值中的ActivityId获取。
        :rtype: list of str
        """
        return self._ActivityIds

    @ActivityIds.setter
    def ActivityIds(self, ActivityIds):
        self._ActivityIds = ActivityIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreatedTimeBegin(self):
        r"""活动创建时间的起始值，时间戳秒数。
        :rtype: int
        """
        return self._CreatedTimeBegin

    @CreatedTimeBegin.setter
    def CreatedTimeBegin(self, CreatedTimeBegin):
        self._CreatedTimeBegin = CreatedTimeBegin

    @property
    def CreatedTimeEnd(self):
        r"""活动创建时间的结束值，时间戳秒数。
        :rtype: int
        """
        return self._CreatedTimeEnd

    @CreatedTimeEnd.setter
    def CreatedTimeEnd(self, CreatedTimeEnd):
        self._CreatedTimeEnd = CreatedTimeEnd


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ActivityIds = params.get("ActivityIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreatedTimeBegin = params.get("CreatedTimeBegin")
        self._CreatedTimeEnd = params.get("CreatedTimeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDockerActivitiesResponse(AbstractModel):
    r"""DescribeDockerActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量。
        :type TotalCount: int
        :param _DockerActivitySet: Docker活动列表。
        :type DockerActivitySet: list of DockerActivity
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DockerActivitySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DockerActivitySet(self):
        r"""Docker活动列表。
        :rtype: list of DockerActivity
        """
        return self._DockerActivitySet

    @DockerActivitySet.setter
    def DockerActivitySet(self, DockerActivitySet):
        self._DockerActivitySet = DockerActivitySet

    @property
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
        if params.get("DockerActivitySet") is not None:
            self._DockerActivitySet = []
            for item in params.get("DockerActivitySet"):
                obj = DockerActivity()
                obj._deserialize(item)
                self._DockerActivitySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDockerContainerConfigurationRequest(AbstractModel):
    r"""DescribeDockerContainerConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerId: 容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerId: str
        """
        self._InstanceId = None
        self._ContainerId = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerId(self):
        r"""容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: str
        """
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerId = params.get("ContainerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDockerContainerConfigurationResponse(AbstractModel):
    r"""DescribeDockerContainerConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerConfiguration: Docker容器配置信息。
        :type ContainerConfiguration: :class:`tencentcloud.lighthouse.v20200324.models.DockerContainerConfiguration`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ContainerConfiguration = None
        self._RequestId = None

    @property
    def ContainerConfiguration(self):
        r"""Docker容器配置信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DockerContainerConfiguration`
        """
        return self._ContainerConfiguration

    @ContainerConfiguration.setter
    def ContainerConfiguration(self, ContainerConfiguration):
        self._ContainerConfiguration = ContainerConfiguration

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ContainerConfiguration") is not None:
            self._ContainerConfiguration = DockerContainerConfiguration()
            self._ContainerConfiguration._deserialize(params.get("ContainerConfiguration"))
        self._RequestId = params.get("RequestId")


class DescribeDockerContainerDetailRequest(AbstractModel):
    r"""DescribeDockerContainerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerId: 容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerId: str
        """
        self._InstanceId = None
        self._ContainerId = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerId(self):
        r"""容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: str
        """
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerId = params.get("ContainerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDockerContainerDetailResponse(AbstractModel):
    r"""DescribeDockerContainerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerDetail: Docker容器详情，json字符串base64编码。
        :type ContainerDetail: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ContainerDetail = None
        self._RequestId = None

    @property
    def ContainerDetail(self):
        r"""Docker容器详情，json字符串base64编码。
        :rtype: str
        """
        return self._ContainerDetail

    @ContainerDetail.setter
    def ContainerDetail(self, ContainerDetail):
        self._ContainerDetail = ContainerDetail

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ContainerDetail = params.get("ContainerDetail")
        self._RequestId = params.get("RequestId")


class DescribeDockerContainersRequest(AbstractModel):
    r"""DescribeDockerContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerIds: 容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。参数不支持同时指定 ContainerIds 和 Filters。
        :type ContainerIds: list of str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤器列表。
<li>container-id</li>按照【容器ID】进行过滤。
类型：String
必选：否
<li>container-name</li>按照【容器名称】进行过滤。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 ContainerIds 和 Filters。
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._ContainerIds = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerIds(self):
        r"""容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。参数不支持同时指定 ContainerIds 和 Filters。
        :rtype: list of str
        """
        return self._ContainerIds

    @ContainerIds.setter
    def ContainerIds(self, ContainerIds):
        self._ContainerIds = ContainerIds

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""过滤器列表。
<li>container-id</li>按照【容器ID】进行过滤。
类型：String
必选：否
<li>container-name</li>按照【容器名称】进行过滤。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 ContainerIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerIds = params.get("ContainerIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeDockerContainersResponse(AbstractModel):
    r"""DescribeDockerContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量。
        :type TotalCount: int
        :param _DockerContainerSet: 容器列表。
        :type DockerContainerSet: list of DockerContainer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DockerContainerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DockerContainerSet(self):
        r"""容器列表。
        :rtype: list of DockerContainer
        """
        return self._DockerContainerSet

    @DockerContainerSet.setter
    def DockerContainerSet(self, DockerContainerSet):
        self._DockerContainerSet = DockerContainerSet

    @property
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
        if params.get("DockerContainerSet") is not None:
            self._DockerContainerSet = []
            for item in params.get("DockerContainerSet"):
                obj = DockerContainer()
                obj._deserialize(item)
                self._DockerContainerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirewallRulesRequest(AbstractModel):
    r"""DescribeFirewallRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirewallRulesResponse(AbstractModel):
    r"""DescribeFirewallRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的防火墙规则数量。
        :type TotalCount: int
        :param _FirewallRuleSet: 防火墙规则详细信息列表。
        :type FirewallRuleSet: list of FirewallRuleInfo
        :param _FirewallVersion: 防火墙版本号。
        :type FirewallVersion: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._FirewallRuleSet = None
        self._FirewallVersion = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的防火墙规则数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def FirewallRuleSet(self):
        r"""防火墙规则详细信息列表。
        :rtype: list of FirewallRuleInfo
        """
        return self._FirewallRuleSet

    @FirewallRuleSet.setter
    def FirewallRuleSet(self, FirewallRuleSet):
        self._FirewallRuleSet = FirewallRuleSet

    @property
    def FirewallVersion(self):
        r"""防火墙版本号。
        :rtype: int
        """
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion

    @property
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
        if params.get("FirewallRuleSet") is not None:
            self._FirewallRuleSet = []
            for item in params.get("FirewallRuleSet"):
                obj = FirewallRuleInfo()
                obj._deserialize(item)
                self._FirewallRuleSet.append(obj)
        self._FirewallVersion = params.get("FirewallVersion")
        self._RequestId = params.get("RequestId")


class DescribeFirewallRulesTemplateRequest(AbstractModel):
    r"""DescribeFirewallRulesTemplate请求参数结构体

    """


class DescribeFirewallRulesTemplateResponse(AbstractModel):
    r"""DescribeFirewallRulesTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的防火墙规则数量。
        :type TotalCount: int
        :param _FirewallRuleSet: 防火墙规则详细信息列表。
        :type FirewallRuleSet: list of FirewallRuleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._FirewallRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的防火墙规则数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def FirewallRuleSet(self):
        r"""防火墙规则详细信息列表。
        :rtype: list of FirewallRuleInfo
        """
        return self._FirewallRuleSet

    @FirewallRuleSet.setter
    def FirewallRuleSet(self, FirewallRuleSet):
        self._FirewallRuleSet = FirewallRuleSet

    @property
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
        if params.get("FirewallRuleSet") is not None:
            self._FirewallRuleSet = []
            for item in params.get("FirewallRuleSet"):
                obj = FirewallRuleInfo()
                obj._deserialize(item)
                self._FirewallRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirewallTemplateApplyRecordsRequest(AbstractModel):
    r"""DescribeFirewallTemplateApplyRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :type TemplateId: str
        :param _TaskIds: 应用防火墙模板任务ID列表。可通过[ApplyFirewallTemplate](https://cloud.tencent.com/document/product/1207/96883)接口返回值TaskId字段获取。
        :type TaskIds: list of str
        """
        self._TemplateId = None
        self._TaskIds = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TaskIds(self):
        r"""应用防火墙模板任务ID列表。可通过[ApplyFirewallTemplate](https://cloud.tencent.com/document/product/1207/96883)接口返回值TaskId字段获取。
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirewallTemplateApplyRecordsResponse(AbstractModel):
    r"""DescribeFirewallTemplateApplyRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyRecordSet: 防火墙模板应用记录列表。
        :type ApplyRecordSet: list of FirewallTemplateApplyRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplyRecordSet = None
        self._RequestId = None

    @property
    def ApplyRecordSet(self):
        r"""防火墙模板应用记录列表。
        :rtype: list of FirewallTemplateApplyRecord
        """
        return self._ApplyRecordSet

    @ApplyRecordSet.setter
    def ApplyRecordSet(self, ApplyRecordSet):
        self._ApplyRecordSet = ApplyRecordSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApplyRecordSet") is not None:
            self._ApplyRecordSet = []
            for item in params.get("ApplyRecordSet"):
                obj = FirewallTemplateApplyRecord()
                obj._deserialize(item)
                self._ApplyRecordSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirewallTemplateQuotaRequest(AbstractModel):
    r"""DescribeFirewallTemplateQuota请求参数结构体

    """


class DescribeFirewallTemplateQuotaResponse(AbstractModel):
    r"""DescribeFirewallTemplateQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Available: 当前可用配额。
        :type Available: int
        :param _Total: 总配额。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Available = None
        self._Total = None
        self._RequestId = None

    @property
    def Available(self):
        r"""当前可用配额。
        :rtype: int
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Total(self):
        r"""总配额。
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
        self._Available = params.get("Available")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFirewallTemplateRuleQuotaRequest(AbstractModel):
    r"""DescribeFirewallTemplateRuleQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
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
        


class DescribeFirewallTemplateRuleQuotaResponse(AbstractModel):
    r"""DescribeFirewallTemplateRuleQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Available: 当前可用配额。
        :type Available: int
        :param _Total: 总配额。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Available = None
        self._Total = None
        self._RequestId = None

    @property
    def Available(self):
        r"""当前可用配额。
        :rtype: int
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Total(self):
        r"""总配额。
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
        self._Available = params.get("Available")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFirewallTemplateRulesRequest(AbstractModel):
    r"""DescribeFirewallTemplateRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID列表。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。列表长度最大值为100。
        :type TemplateId: str
        :param _TemplateRuleIds: 防火墙模板规则ID列表。可通过[DescribeFirewallTemplateRules](https://cloud.tencent.com/document/product/1207/96875)接口返回值字段TemplateRuleSet获取。列表长度最大值为100。
        :type TemplateRuleIds: list of str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._TemplateId = None
        self._TemplateRuleIds = None
        self._Offset = None
        self._Limit = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID列表。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。列表长度最大值为100。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateRuleIds(self):
        r"""防火墙模板规则ID列表。可通过[DescribeFirewallTemplateRules](https://cloud.tencent.com/document/product/1207/96875)接口返回值字段TemplateRuleSet获取。列表长度最大值为100。
        :rtype: list of str
        """
        return self._TemplateRuleIds

    @TemplateRuleIds.setter
    def TemplateRuleIds(self, TemplateRuleIds):
        self._TemplateRuleIds = TemplateRuleIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateRuleIds = params.get("TemplateRuleIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirewallTemplateRulesResponse(AbstractModel):
    r"""DescribeFirewallTemplateRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 防火墙模板规则总数量。
        :type TotalCount: int
        :param _TemplateRuleSet: 防火墙模板规则信息列表。
        :type TemplateRuleSet: list of FirewallTemplateRuleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TemplateRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""防火墙模板规则总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TemplateRuleSet(self):
        r"""防火墙模板规则信息列表。
        :rtype: list of FirewallTemplateRuleInfo
        """
        return self._TemplateRuleSet

    @TemplateRuleSet.setter
    def TemplateRuleSet(self, TemplateRuleSet):
        self._TemplateRuleSet = TemplateRuleSet

    @property
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
        if params.get("TemplateRuleSet") is not None:
            self._TemplateRuleSet = []
            for item in params.get("TemplateRuleSet"):
                obj = FirewallTemplateRuleInfo()
                obj._deserialize(item)
                self._TemplateRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirewallTemplatesRequest(AbstractModel):
    r"""DescribeFirewallTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateIds: 防火墙模板ID列表。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。列表长度最大值为100。
        :type TemplateIds: list of str
        :param _Filters: 过滤器列表。
<li>template-id</li>按照【防火墙模板所属的ID】进行过滤。
类型：String
必选：否
<li>template-name</li>按照【防火墙模板所属的名称】进行过滤。
类型：String
必选：否
<li>template-type</li>按照【防火墙模板的类型】进行过滤。
类型：String
必选：否
取值: "PRIVATE"(个人模板)
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 100。参数不支持同时指定 TemplateIds 和 Filters。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._TemplateIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def TemplateIds(self):
        r"""防火墙模板ID列表。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。列表长度最大值为100。
        :rtype: list of str
        """
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds

    @property
    def Filters(self):
        r"""过滤器列表。
<li>template-id</li>按照【防火墙模板所属的ID】进行过滤。
类型：String
必选：否
<li>template-name</li>按照【防火墙模板所属的名称】进行过滤。
类型：String
必选：否
<li>template-type</li>按照【防火墙模板的类型】进行过滤。
类型：String
必选：否
取值: "PRIVATE"(个人模板)
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 100。参数不支持同时指定 TemplateIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TemplateIds = params.get("TemplateIds")
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
        


class DescribeFirewallTemplatesResponse(AbstractModel):
    r"""DescribeFirewallTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 模板总数量。
        :type TotalCount: int
        :param _TemplateSet: 防火墙模板列表。
        :type TemplateSet: list of FirewallTemplate
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TemplateSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""模板总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TemplateSet(self):
        r"""防火墙模板列表。
        :rtype: list of FirewallTemplate
        """
        return self._TemplateSet

    @TemplateSet.setter
    def TemplateSet(self, TemplateSet):
        self._TemplateSet = TemplateSet

    @property
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
        if params.get("TemplateSet") is not None:
            self._TemplateSet = []
            for item in params.get("TemplateSet"):
                obj = FirewallTemplate()
                obj._deserialize(item)
                self._TemplateSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGeneralResourceQuotasRequest(AbstractModel):
    r"""DescribeGeneralResourceQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceNames: 资源名列表，可取值:
- GENERAL_BUNDLE_INSTANCE 通用型套餐实例
- STORAGE_BUNDLE_INSTANCE 存储型套餐实例 
- ENTERPRISE_BUNDLE_INSTANCE 企业型套餐实例 
- EXCLUSIVE_BUNDLE_INSTANCE 专属型套餐实例
- BEFAST_BUNDLE_INSTANCE 蜂驰型套餐实例
- STARTER_BUNDLE_INSTANCE 入门型套餐实例
- HK_EXCLUSIVE_BUNDLE_INSTANCE 中国香港专属型套餐实例
- CAREFREE_BUNDLE_INSTANCE 无忧型套餐实例
- EXCLUSIVE_BUNDLE_02_INSTANCE 境外专属Ⅱ型
- NEWCOMER_BUNDLE_INSTANCE 新客专享型
- GAME_PORTAL_BUNDLE_INSTANCE 游戏专区实例
- ECONOMY_BUNDLE_INSTANCE 经济型套餐实例
- BUDGET_BUNDLE_INSTANCE 特惠型套餐实例
- RAZOR_SPEED_BUNDLE_INSTANCE 锐驰套餐实例
- BANDWIDTH_BUNDLE_INSTANCE 带宽型套餐实例
- USER_KEY_PAIR 密钥对
- SNAPSHOT 快照
- BLUEPRINT 自定义镜像
- FREE_BLUEPRINT 免费自定义镜像
- DATA_DISK 数据盘
        :type ResourceNames: list of str
        """
        self._ResourceNames = None

    @property
    def ResourceNames(self):
        r"""资源名列表，可取值:
- GENERAL_BUNDLE_INSTANCE 通用型套餐实例
- STORAGE_BUNDLE_INSTANCE 存储型套餐实例 
- ENTERPRISE_BUNDLE_INSTANCE 企业型套餐实例 
- EXCLUSIVE_BUNDLE_INSTANCE 专属型套餐实例
- BEFAST_BUNDLE_INSTANCE 蜂驰型套餐实例
- STARTER_BUNDLE_INSTANCE 入门型套餐实例
- HK_EXCLUSIVE_BUNDLE_INSTANCE 中国香港专属型套餐实例
- CAREFREE_BUNDLE_INSTANCE 无忧型套餐实例
- EXCLUSIVE_BUNDLE_02_INSTANCE 境外专属Ⅱ型
- NEWCOMER_BUNDLE_INSTANCE 新客专享型
- GAME_PORTAL_BUNDLE_INSTANCE 游戏专区实例
- ECONOMY_BUNDLE_INSTANCE 经济型套餐实例
- BUDGET_BUNDLE_INSTANCE 特惠型套餐实例
- RAZOR_SPEED_BUNDLE_INSTANCE 锐驰套餐实例
- BANDWIDTH_BUNDLE_INSTANCE 带宽型套餐实例
- USER_KEY_PAIR 密钥对
- SNAPSHOT 快照
- BLUEPRINT 自定义镜像
- FREE_BLUEPRINT 免费自定义镜像
- DATA_DISK 数据盘
        :rtype: list of str
        """
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames


    def _deserialize(self, params):
        self._ResourceNames = params.get("ResourceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralResourceQuotasResponse(AbstractModel):
    r"""DescribeGeneralResourceQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GeneralResourceQuotaSet: 通用资源配额详细信息列表。
        :type GeneralResourceQuotaSet: list of GeneralResourceQuota
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GeneralResourceQuotaSet = None
        self._RequestId = None

    @property
    def GeneralResourceQuotaSet(self):
        r"""通用资源配额详细信息列表。
        :rtype: list of GeneralResourceQuota
        """
        return self._GeneralResourceQuotaSet

    @GeneralResourceQuotaSet.setter
    def GeneralResourceQuotaSet(self, GeneralResourceQuotaSet):
        self._GeneralResourceQuotaSet = GeneralResourceQuotaSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GeneralResourceQuotaSet") is not None:
            self._GeneralResourceQuotaSet = []
            for item in params.get("GeneralResourceQuotaSet"):
                obj = GeneralResourceQuota()
                obj._deserialize(item)
                self._GeneralResourceQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImagesToShareRequest(AbstractModel):
    r"""DescribeImagesToShare请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageIds: CVM镜像 ID 列表。可通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回值中的ImageId获取。
        :type ImageIds: list of str
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param _Filters: 过滤器列表。
<li>image-id</li>按照【CVM镜像ID】进行过滤。
类型：String
必选：否

<li>image-name</li>按照【CVM镜像名称】进行过滤。
类型：String
必选：否

<li>image-type</li>按照【CVM镜像类型】进行过滤。
类型：String
必选：否
取值范围：
PRIVATE_IMAGE: 私有镜像 (本账户创建的镜像)
PUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)
SHARED_IMAGE: 共享镜像(其他账户共享给本账户的镜像) 。

每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
参数不可以同时指定ImageIds和Filters。
        :type Filters: list of Filter
        """
        self._ImageIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ImageIds(self):
        r"""CVM镜像 ID 列表。可通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回值中的ImageId获取。
        :rtype: list of str
        """
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤器列表。
<li>image-id</li>按照【CVM镜像ID】进行过滤。
类型：String
必选：否

<li>image-name</li>按照【CVM镜像名称】进行过滤。
类型：String
必选：否

<li>image-type</li>按照【CVM镜像类型】进行过滤。
类型：String
必选：否
取值范围：
PRIVATE_IMAGE: 私有镜像 (本账户创建的镜像)
PUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)
SHARED_IMAGE: 共享镜像(其他账户共享给本账户的镜像) 。

每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
参数不可以同时指定ImageIds和Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeImagesToShareResponse(AbstractModel):
    r"""DescribeImagesToShare返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的镜像数量。
        :type TotalCount: int
        :param _ImageSet: CVM镜像详细信息列表。
        :type ImageSet: list of Image
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ImageSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的镜像数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ImageSet(self):
        r"""CVM镜像详细信息列表。
        :rtype: list of Image
        """
        return self._ImageSet

    @ImageSet.setter
    def ImageSet(self, ImageSet):
        self._ImageSet = ImageSet

    @property
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
        if params.get("ImageSet") is not None:
            self._ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self._ImageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    r"""DescribeInstanceVncUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    r"""DescribeInstanceVncUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceVncUrl: 实例的管理终端地址。
        :type InstanceVncUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceVncUrl = None
        self._RequestId = None

    @property
    def InstanceVncUrl(self):
        r"""实例的管理终端地址。
        :rtype: str
        """
        return self._InstanceVncUrl

    @InstanceVncUrl.setter
    def InstanceVncUrl(self, InstanceVncUrl):
        self._InstanceVncUrl = InstanceVncUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceVncUrl = params.get("InstanceVncUrl")
        self._RequestId = params.get("RequestId")


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    r"""DescribeInstancesDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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
        


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    r"""DescribeInstancesDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceDeniedActionSet: 实例操作限制列表详细信息。
        :type InstanceDeniedActionSet: list of InstanceDeniedActions
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceDeniedActionSet = None
        self._RequestId = None

    @property
    def InstanceDeniedActionSet(self):
        r"""实例操作限制列表详细信息。
        :rtype: list of InstanceDeniedActions
        """
        return self._InstanceDeniedActionSet

    @InstanceDeniedActionSet.setter
    def InstanceDeniedActionSet(self, InstanceDeniedActionSet):
        self._InstanceDeniedActionSet = InstanceDeniedActionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceDeniedActionSet") is not None:
            self._InstanceDeniedActionSet = []
            for item in params.get("InstanceDeniedActionSet"):
                obj = InstanceDeniedActions()
                obj._deserialize(item)
                self._InstanceDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesDiskNumRequest(AbstractModel):
    r"""DescribeInstancesDiskNum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表。每次请求批量实例的上限为 100。
可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""实例ID列表。每次请求批量实例的上限为 100。
可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
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
        


class DescribeInstancesDiskNumResponse(AbstractModel):
    r"""DescribeInstancesDiskNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttachDetailSet: 挂载信息列表
        :type AttachDetailSet: list of AttachDetail
        :param _TotalCount: 挂载信息数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttachDetailSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AttachDetailSet(self):
        r"""挂载信息列表
        :rtype: list of AttachDetail
        """
        return self._AttachDetailSet

    @AttachDetailSet.setter
    def AttachDetailSet(self, AttachDetailSet):
        self._AttachDetailSet = AttachDetailSet

    @property
    def TotalCount(self):
        r"""挂载信息数量
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
        if params.get("AttachDetailSet") is not None:
            self._AttachDetailSet = []
            for item in params.get("AttachDetailSet"):
                obj = AttachDetail()
                obj._deserialize(item)
                self._AttachDetailSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param _Filters: 过滤器列表。
<li>instance-name</li>按照【实例名称】进行过滤。
类型：String
必选：否
<li>private-ip-address</li>按照【实例主网卡的内网 IP】进行过滤。
类型：String
必选：否
<li>public-ip-address</li>按照【实例主网卡的公网 IP】进行过滤。
类型：String
必选：否
<li>zone</li>按照【可用区】进行过滤。
类型：String
必选：否
<li>instance-state</li>按照【实例状态】进行过滤。
类型：String
必选：否
<li>tag-key</li>按照【标签键】进行过滤。
类型：String
必选：否
<li>tag-value</li>按照【标签值】进行过滤。
类型：String
必选：否
<li> tag:tag-key</li>按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 100。参数不支持同时指定 InstanceIds 和 Filters。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param _OrderField: 指定排序字段 。取值范围： "EXPIRED_TIME"：依据实例的到期时间排序。 
 不传入此字段时, 优先返回实例状态为“待回收”的实例, 其余实例以“创建时间”倒序返回。
        :type OrderField: str
        :param _Order: 输出实例列表的排列顺序。取值范围：
"ASC"：升序排列。
"DESC"：降序排列。
默认按升序排序。当传入该字段时，必须指定OrderField。
        :type Order: str
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        r"""过滤器列表。
<li>instance-name</li>按照【实例名称】进行过滤。
类型：String
必选：否
<li>private-ip-address</li>按照【实例主网卡的内网 IP】进行过滤。
类型：String
必选：否
<li>public-ip-address</li>按照【实例主网卡的公网 IP】进行过滤。
类型：String
必选：否
<li>zone</li>按照【可用区】进行过滤。
类型：String
必选：否
<li>instance-state</li>按照【实例状态】进行过滤。
类型：String
必选：否
<li>tag-key</li>按照【标签键】进行过滤。
类型：String
必选：否
<li>tag-value</li>按照【标签值】进行过滤。
类型：String
必选：否
<li> tag:tag-key</li>按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 100。参数不支持同时指定 InstanceIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        r"""指定排序字段 。取值范围： "EXPIRED_TIME"：依据实例的到期时间排序。 
 不传入此字段时, 优先返回实例状态为“待回收”的实例, 其余实例以“创建时间”倒序返回。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""输出实例列表的排列顺序。取值范围：
"ASC"：升序排列。
"DESC"：降序排列。
默认按升序排序。当传入该字段时，必须指定OrderField。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
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
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _InstanceSet: 实例详细信息列表。
        :type InstanceSet: list of Instance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的实例数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        r"""实例详细信息列表。
        :rtype: list of Instance
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
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesReturnableRequest(AbstractModel):
    r"""DescribeInstancesReturnable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesReturnableResponse(AbstractModel):
    r"""DescribeInstancesReturnable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _InstanceReturnableSet: 可退还实例详细信息列表。
        :type InstanceReturnableSet: list of InstanceReturnable
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceReturnableSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的实例数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceReturnableSet(self):
        r"""可退还实例详细信息列表。
        :rtype: list of InstanceReturnable
        """
        return self._InstanceReturnableSet

    @InstanceReturnableSet.setter
    def InstanceReturnableSet(self, InstanceReturnableSet):
        self._InstanceReturnableSet = InstanceReturnableSet

    @property
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
        if params.get("InstanceReturnableSet") is not None:
            self._InstanceReturnableSet = []
            for item in params.get("InstanceReturnableSet"):
                obj = InstanceReturnable()
                obj._deserialize(item)
                self._InstanceReturnableSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesTrafficPackagesRequest(AbstractModel):
    r"""DescribeInstancesTrafficPackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesTrafficPackagesResponse(AbstractModel):
    r"""DescribeInstancesTrafficPackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例流量包详情数量。
        :type TotalCount: int
        :param _InstanceTrafficPackageSet: 实例流量包详情列表。
        :type InstanceTrafficPackageSet: list of InstanceTrafficPackage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceTrafficPackageSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的实例流量包详情数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceTrafficPackageSet(self):
        r"""实例流量包详情列表。
        :rtype: list of InstanceTrafficPackage
        """
        return self._InstanceTrafficPackageSet

    @InstanceTrafficPackageSet.setter
    def InstanceTrafficPackageSet(self, InstanceTrafficPackageSet):
        self._InstanceTrafficPackageSet = InstanceTrafficPackageSet

    @property
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
        if params.get("InstanceTrafficPackageSet") is not None:
            self._InstanceTrafficPackageSet = []
            for item in params.get("InstanceTrafficPackageSet"):
                obj = InstanceTrafficPackage()
                obj._deserialize(item)
                self._InstanceTrafficPackageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKeyPairsRequest(AbstractModel):
    r"""DescribeKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 密钥对 ID 列表。可通过[DescribeKeyPairs](https://cloud.tencent.com/document/product/1207/55540)接口返回值字段KeyPairSet获取。列表长度最大值为100。
        :type KeyIds: list of str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Filters: 过滤器列表。
<li>key-id</li>按照【密钥对ID】进行过滤。
类型：String
必选：否
<li>key-name</li>按照【密钥对名称】进行过滤（支持模糊匹配）。
类型：String
必选：否
<li>tag-key</li>
按照【标签键】进行过滤。 类型：String 必选：否
<li>tag-value</li>
按照【标签值】进行过滤。 类型：String 必选：否
<li>tag:tag-key</li>
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 KeyIds 和 Filters。
        :type Filters: list of Filter
        """
        self._KeyIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def KeyIds(self):
        r"""密钥对 ID 列表。可通过[DescribeKeyPairs](https://cloud.tencent.com/document/product/1207/55540)接口返回值字段KeyPairSet获取。列表长度最大值为100。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤器列表。
<li>key-id</li>按照【密钥对ID】进行过滤。
类型：String
必选：否
<li>key-name</li>按照【密钥对名称】进行过滤（支持模糊匹配）。
类型：String
必选：否
<li>tag-key</li>
按照【标签键】进行过滤。 类型：String 必选：否
<li>tag-value</li>
按照【标签值】进行过滤。 类型：String 必选：否
<li>tag:tag-key</li>
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 KeyIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeKeyPairsResponse(AbstractModel):
    r"""DescribeKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的密钥对数量。
        :type TotalCount: int
        :param _KeyPairSet: 密钥对详细信息列表。
        :type KeyPairSet: list of KeyPair
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KeyPairSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的密钥对数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KeyPairSet(self):
        r"""密钥对详细信息列表。
        :rtype: list of KeyPair
        """
        return self._KeyPairSet

    @KeyPairSet.setter
    def KeyPairSet(self, KeyPairSet):
        self._KeyPairSet = KeyPairSet

    @property
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
        if params.get("KeyPairSet") is not None:
            self._KeyPairSet = []
            for item in params.get("KeyPairSet"):
                obj = KeyPair()
                obj._deserialize(item)
                self._KeyPairSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMcpServerTemplatesRequest(AbstractModel):
    r"""DescribeMcpServerTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤器列表。
<li>name-description</li>按照MCP Server模板名称或描述进行过滤（支持模糊匹配）。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        r"""过滤器列表。
<li>name-description</li>按照MCP Server模板名称或描述进行过滤（支持模糊匹配）。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMcpServerTemplatesResponse(AbstractModel):
    r"""DescribeMcpServerTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _McpServerTemplateSet: MCP Server模板列表。
        :type McpServerTemplateSet: list of McpServerTemplate
        :param _TotalCount: 符合条件的MCP Server模板数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._McpServerTemplateSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def McpServerTemplateSet(self):
        r"""MCP Server模板列表。
        :rtype: list of McpServerTemplate
        """
        return self._McpServerTemplateSet

    @McpServerTemplateSet.setter
    def McpServerTemplateSet(self, McpServerTemplateSet):
        self._McpServerTemplateSet = McpServerTemplateSet

    @property
    def TotalCount(self):
        r"""符合条件的MCP Server模板数量。
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
        if params.get("McpServerTemplateSet") is not None:
            self._McpServerTemplateSet = []
            for item in params.get("McpServerTemplateSet"):
                obj = McpServerTemplate()
                obj._deserialize(item)
                self._McpServerTemplateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMcpServersRequest(AbstractModel):
    r"""DescribeMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _McpServerIds: MCP Server ID列表。列表为空时此条件不生效。最大长度：10
        :type McpServerIds: list of str
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        """
        self._InstanceId = None
        self._McpServerIds = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def McpServerIds(self):
        r"""MCP Server ID列表。列表为空时此条件不生效。最大长度：10
        :rtype: list of str
        """
        return self._McpServerIds

    @McpServerIds.setter
    def McpServerIds(self, McpServerIds):
        self._McpServerIds = McpServerIds

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._McpServerIds = params.get("McpServerIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMcpServersResponse(AbstractModel):
    r"""DescribeMcpServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _McpServerSet: MCP Server列表。
        :type McpServerSet: list of McpServer
        :param _TotalCount: 符合条件的MCP Server数量。
        :type TotalCount: int
        :param _InstanceId: 实例 ID。	
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._McpServerSet = None
        self._TotalCount = None
        self._InstanceId = None
        self._InstanceName = None
        self._RequestId = None

    @property
    def McpServerSet(self):
        r"""MCP Server列表。
        :rtype: list of McpServer
        """
        return self._McpServerSet

    @McpServerSet.setter
    def McpServerSet(self, McpServerSet):
        self._McpServerSet = McpServerSet

    @property
    def TotalCount(self):
        r"""符合条件的MCP Server数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("McpServerSet") is not None:
            self._McpServerSet = []
            for item in params.get("McpServerSet"):
                obj = McpServer()
                obj._deserialize(item)
                self._McpServerSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._RequestId = params.get("RequestId")


class DescribeModifyInstanceBundlesRequest(AbstractModel):
    r"""DescribeModifyInstanceBundles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _Filters: 过滤器列表。
<li>bundle-id</li>按照【套餐 ID】进行过滤。
类型：String
必选：否
可通过<a href="https://cloud.tencent.com/document/product/1207/47575"> DescribeBundles </a>接口返回值中的 BundleId 获取。
<li>support-platform-type</li>按照【系统类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）
类型：String
必选：否
<li>bundle-type</li>按照 【套餐类型进行过滤】。
取值：GENERAL_BUNDLE (通用型套餐); STORAGE_BUNDLE(存储型套餐);ENTERPRISE_BUNDLE( 企业型套餐);EXCLUSIVE_BUNDLE(专属型套餐);BEFAST_BUNDLE(蜂驰型套餐);STARTER_BUNDLE(入门型套餐);ECONOMY_BUNDLE(经济型套餐);RAZOR_SPEED_BUNDLE(锐驰型套餐)
类型：String
必选：否
<li>bundle-state</li>按照【套餐状态】进行过滤。
取值: ‘ONLINE’(在线); ‘OFFLINE’(下线);
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""实例 ID。可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        r"""过滤器列表。
<li>bundle-id</li>按照【套餐 ID】进行过滤。
类型：String
必选：否
可通过<a href="https://cloud.tencent.com/document/product/1207/47575"> DescribeBundles </a>接口返回值中的 BundleId 获取。
<li>support-platform-type</li>按照【系统类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）
类型：String
必选：否
<li>bundle-type</li>按照 【套餐类型进行过滤】。
取值：GENERAL_BUNDLE (通用型套餐); STORAGE_BUNDLE(存储型套餐);ENTERPRISE_BUNDLE( 企业型套餐);EXCLUSIVE_BUNDLE(专属型套餐);BEFAST_BUNDLE(蜂驰型套餐);STARTER_BUNDLE(入门型套餐);ECONOMY_BUNDLE(经济型套餐);RAZOR_SPEED_BUNDLE(锐驰型套餐)
类型：String
必选：否
<li>bundle-state</li>按照【套餐状态】进行过滤。
取值: ‘ONLINE’(在线); ‘OFFLINE’(下线);
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
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
        


class DescribeModifyInstanceBundlesResponse(AbstractModel):
    r"""DescribeModifyInstanceBundles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的套餐数量。
        :type TotalCount: int
        :param _ModifyBundleSet: 变更套餐详细信息。
        :type ModifyBundleSet: list of ModifyBundle
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ModifyBundleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的套餐数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ModifyBundleSet(self):
        r"""变更套餐详细信息。
        :rtype: list of ModifyBundle
        """
        return self._ModifyBundleSet

    @ModifyBundleSet.setter
    def ModifyBundleSet(self, ModifyBundleSet):
        self._ModifyBundleSet = ModifyBundleSet

    @property
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
        if params.get("ModifyBundleSet") is not None:
            self._ModifyBundleSet = []
            for item in params.get("ModifyBundleSet"):
                obj = ModifyBundle()
                obj._deserialize(item)
                self._ModifyBundleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    r"""DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    r"""DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 地域数量。
        :type TotalCount: int
        :param _RegionSet: 地域信息列表。
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""地域数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        r"""地域信息列表。
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


class DescribeResetInstanceBlueprintsRequest(AbstractModel):
    r"""DescribeResetInstanceBlueprints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param _Filters: 过滤器列表。
<li>blueprint-id</li>按照【镜像 ID】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/47689">DescribeBlueprints</a> 接口返回值中的 BlueprintId 获取。
<li>blueprint-type</li>按照【镜像类型】进行过滤。
取值： APP_OS（应用镜像 ）；PURE_OS（ 系统镜像）；PRIVATE（自定义镜像）;DOCKER（Docker容器镜像）；SHARED（共享镜像）。
类型：String
必选：否
<li>platform-type</li>按照【镜像平台类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）。
类型：String
必选：否
<li>blueprint-name</li>按照【镜像名称】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/47689">DescribeBlueprints</a> 接口返回值中的 BlueprintName 获取。
<li>blueprint-state</li>按照【镜像状态】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/47689">DescribeBlueprints</a> 接口返回值中的 BlueprintState 获取。

每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤器列表。
<li>blueprint-id</li>按照【镜像 ID】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/47689">DescribeBlueprints</a> 接口返回值中的 BlueprintId 获取。
<li>blueprint-type</li>按照【镜像类型】进行过滤。
取值： APP_OS（应用镜像 ）；PURE_OS（ 系统镜像）；PRIVATE（自定义镜像）;DOCKER（Docker容器镜像）；SHARED（共享镜像）。
类型：String
必选：否
<li>platform-type</li>按照【镜像平台类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）。
类型：String
必选：否
<li>blueprint-name</li>按照【镜像名称】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/47689">DescribeBlueprints</a> 接口返回值中的 BlueprintName 获取。
<li>blueprint-state</li>按照【镜像状态】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/47689">DescribeBlueprints</a> 接口返回值中的 BlueprintState 获取。

每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeResetInstanceBlueprintsResponse(AbstractModel):
    r"""DescribeResetInstanceBlueprints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的镜像数量。
        :type TotalCount: int
        :param _ResetInstanceBlueprintSet: 镜像重置信息列表
        :type ResetInstanceBlueprintSet: list of ResetInstanceBlueprint
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResetInstanceBlueprintSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的镜像数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResetInstanceBlueprintSet(self):
        r"""镜像重置信息列表
        :rtype: list of ResetInstanceBlueprint
        """
        return self._ResetInstanceBlueprintSet

    @ResetInstanceBlueprintSet.setter
    def ResetInstanceBlueprintSet(self, ResetInstanceBlueprintSet):
        self._ResetInstanceBlueprintSet = ResetInstanceBlueprintSet

    @property
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
        if params.get("ResetInstanceBlueprintSet") is not None:
            self._ResetInstanceBlueprintSet = []
            for item in params.get("ResetInstanceBlueprintSet"):
                obj = ResetInstanceBlueprint()
                obj._deserialize(item)
                self._ResetInstanceBlueprintSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScenesRequest(AbstractModel):
    r"""DescribeScenes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneIds: 使用场景ID列表。可通过[DescribeScenes](https://cloud.tencent.com/document/product/1207/83512)接口返回值中的SceneId获取。
        :type SceneIds: list of str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._SceneIds = None
        self._Offset = None
        self._Limit = None

    @property
    def SceneIds(self):
        r"""使用场景ID列表。可通过[DescribeScenes](https://cloud.tencent.com/document/product/1207/83512)接口返回值中的SceneId获取。
        :rtype: list of str
        """
        return self._SceneIds

    @SceneIds.setter
    def SceneIds(self, SceneIds):
        self._SceneIds = SceneIds

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SceneIds = params.get("SceneIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenesResponse(AbstractModel):
    r"""DescribeScenes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneSet: 使用场景列表。
        :type SceneSet: list of Scene
        :param _TotalCount: 使用场景总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SceneSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SceneSet(self):
        r"""使用场景列表。
        :rtype: list of Scene
        """
        return self._SceneSet

    @SceneSet.setter
    def SceneSet(self, SceneSet):
        self._SceneSet = SceneSet

    @property
    def TotalCount(self):
        r"""使用场景总数量。
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
        if params.get("SceneSet") is not None:
            self._SceneSet = []
            for item in params.get("SceneSet"):
                obj = Scene()
                obj._deserialize(item)
                self._SceneSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsDeniedActionsRequest(AbstractModel):
    r"""DescribeSnapshotsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: 快照 ID 列表,每次请求批量快照的上限是100个。 可通过 <a href="https://cloud.tencent.com/document/product/1207/54388" target="_blank">DescribeSnapshots</a> 查询。
        :type SnapshotIds: list of str
        """
        self._SnapshotIds = None

    @property
    def SnapshotIds(self):
        r"""快照 ID 列表,每次请求批量快照的上限是100个。 可通过 <a href="https://cloud.tencent.com/document/product/1207/54388" target="_blank">DescribeSnapshots</a> 查询。
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsDeniedActionsResponse(AbstractModel):
    r"""DescribeSnapshotsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotDeniedActionSet: 快照操作限制列表详细信息。
        :type SnapshotDeniedActionSet: list of SnapshotDeniedActions
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotDeniedActionSet = None
        self._RequestId = None

    @property
    def SnapshotDeniedActionSet(self):
        r"""快照操作限制列表详细信息。
        :rtype: list of SnapshotDeniedActions
        """
        return self._SnapshotDeniedActionSet

    @SnapshotDeniedActionSet.setter
    def SnapshotDeniedActionSet(self, SnapshotDeniedActionSet):
        self._SnapshotDeniedActionSet = SnapshotDeniedActionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SnapshotDeniedActionSet") is not None:
            self._SnapshotDeniedActionSet = []
            for item in params.get("SnapshotDeniedActionSet"):
                obj = SnapshotDeniedActions()
                obj._deserialize(item)
                self._SnapshotDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    r"""DescribeSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: 要查询快照的 ID 列表。每次请求批量快照的上限为 100。 
可通过 [DescribeSnapshots](https://cloud.tencent.com/document/product/1207/54388) 接口返回值中的 SnapshotId		获取。
参数不支持同时指定 SnapshotIds 和 Filters。
        :type SnapshotIds: list of str
        :param _Filters: 过滤器列表。
<li>snapshot-id</li>按照【快照 ID】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/54388">DescribeSnapshots</a> 接口返回值中的 SnapshotId 获取。
<li>disk-id</li>按照【磁盘 ID】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/66093">DescribeDisks</a> 接口返回值中的 DiskId 获取。
<li>snapshot-name</li>按照【快照名称】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/54388">DescribeSnapshots</a> 接口返回值中的 SnapshotName 获取。
<li>instance-id</li>按照【实例 ID 】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
<li>tag-key</li>
按照【标签键】进行过滤。 类型：String 必选：否
<li>tag-value</li>
按照【标签值】进行过滤。 类型：String 必选：否
<li>tag:tag-key</li>
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 SnapshotIds 和 Filters。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._SnapshotIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def SnapshotIds(self):
        r"""要查询快照的 ID 列表。每次请求批量快照的上限为 100。 
可通过 [DescribeSnapshots](https://cloud.tencent.com/document/product/1207/54388) 接口返回值中的 SnapshotId		获取。
参数不支持同时指定 SnapshotIds 和 Filters。
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def Filters(self):
        r"""过滤器列表。
<li>snapshot-id</li>按照【快照 ID】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/54388">DescribeSnapshots</a> 接口返回值中的 SnapshotId 获取。
<li>disk-id</li>按照【磁盘 ID】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/66093">DescribeDisks</a> 接口返回值中的 DiskId 获取。
<li>snapshot-name</li>按照【快照名称】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/54388">DescribeSnapshots</a> 接口返回值中的 SnapshotName 获取。
<li>instance-id</li>按照【实例 ID 】进行过滤。
类型：String
必选：否
可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
<li>tag-key</li>
按照【标签键】进行过滤。 类型：String 必选：否
<li>tag-value</li>
按照【标签值】进行过滤。 类型：String 必选：否
<li>tag:tag-key</li>
按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 SnapshotIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
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
        


class DescribeSnapshotsResponse(AbstractModel):
    r"""DescribeSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 快照的数量。
        :type TotalCount: int
        :param _SnapshotSet: 快照的详情列表。
        :type SnapshotSet: list of Snapshot
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SnapshotSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""快照的数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotSet(self):
        r"""快照的详情列表。
        :rtype: list of Snapshot
        """
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

    @property
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
        if params.get("SnapshotSet") is not None:
            self._SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self._SnapshotSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    r"""DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderField: 可用区列表排序的依据字段。取值范围：
<li>ZONE：依据可用区排序。</li>
<li>INSTANCE_DISPLAY_LABEL：依据可用区展示标签排序，可用区展示标签包括：HIDDEN（隐藏）、NORMAL（普通）、SELECTED（默认选中），默认采用的升序排列为：['HIDDEN', 'NORMAL', 'SELECTED']。
默认按可用区排序。</li>
        :type OrderField: str
        :param _Order: 输出可用区列表的排列顺序。取值范围：
<li>ASC：升序排列。 </li>
<li>DESC：降序排列。</li>
默认按升序排列。
        :type Order: str
        """
        self._OrderField = None
        self._Order = None

    @property
    def OrderField(self):
        r"""可用区列表排序的依据字段。取值范围：
<li>ZONE：依据可用区排序。</li>
<li>INSTANCE_DISPLAY_LABEL：依据可用区展示标签排序，可用区展示标签包括：HIDDEN（隐藏）、NORMAL（普通）、SELECTED（默认选中），默认采用的升序排列为：['HIDDEN', 'NORMAL', 'SELECTED']。
默认按可用区排序。</li>
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""输出可用区列表的排列顺序。取值范围：
<li>ASC：升序排列。 </li>
<li>DESC：降序排列。</li>
默认按升序排列。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    r"""DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可用区数量
        :type TotalCount: int
        :param _ZoneInfoSet: 可用区详细信息列表
        :type ZoneInfoSet: list of ZoneInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""可用区数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneInfoSet(self):
        r"""可用区详细信息列表
        :rtype: list of ZoneInfo
        """
        return self._ZoneInfoSet

    @ZoneInfoSet.setter
    def ZoneInfoSet(self, ZoneInfoSet):
        self._ZoneInfoSet = ZoneInfoSet

    @property
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
        if params.get("ZoneInfoSet") is not None:
            self._ZoneInfoSet = []
            for item in params.get("ZoneInfoSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DestinationRegionBlueprint(AbstractModel):
    r"""目标地域镜像信息。

    """

    def __init__(self):
        r"""
        :param _Region: 目标地域。
        :type Region: str
        :param _BlueprintId: 目标地域镜像ID。
        :type BlueprintId: str
        """
        self._Region = None
        self._BlueprintId = None

    @property
    def Region(self):
        r"""目标地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BlueprintId(self):
        r"""目标地域镜像ID。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._BlueprintId = params.get("BlueprintId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnRequest(AbstractModel):
    r"""DetachCcn请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CcnId: 云联网实例ID。可通过[DescribeCcnAttachedInstances](https://cloud.tencent.com/document/product/1207/58797)接口返回值中的CcnId获取。
        :type CcnId: str
        """
        self._CcnId = None

    @property
    def CcnId(self):
        r"""云联网实例ID。可通过[DescribeCcnAttachedInstances](https://cloud.tencent.com/document/product/1207/58797)接口返回值中的CcnId获取。
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnResponse(AbstractModel):
    r"""DetachCcn返回参数结构体

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


class DetachDisksRequest(AbstractModel):
    r"""DetachDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachDisksResponse(AbstractModel):
    r"""DetachDisks返回参数结构体

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


class DetailPrice(AbstractModel):
    r"""计费项目明细。

    """

    def __init__(self):
        r"""
        :param _PriceName: 描述计费项目名称，目前取值
<li>"DiskSpace"代表云硬盘空间收费项。</li>
<li>"DiskBackupQuota"代表数据盘备份点配额收费项。</li>
<li>"Instance"代表实例收费项。</li>
<li>"SystemDiskBackupQuota"代表系统盘备份点配额收费项。</li>
        :type PriceName: str
        :param _OriginUnitPrice: 计费项维度单价。
        :type OriginUnitPrice: float
        :param _OriginalPrice: 计费项维度总价。
        :type OriginalPrice: float
        :param _Discount: 计费项维度折扣。
        :type Discount: float
        :param _DiscountPrice: 计费项维度折后总价。
        :type DiscountPrice: float
        """
        self._PriceName = None
        self._OriginUnitPrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None

    @property
    def PriceName(self):
        r"""描述计费项目名称，目前取值
<li>"DiskSpace"代表云硬盘空间收费项。</li>
<li>"DiskBackupQuota"代表数据盘备份点配额收费项。</li>
<li>"Instance"代表实例收费项。</li>
<li>"SystemDiskBackupQuota"代表系统盘备份点配额收费项。</li>
        :rtype: str
        """
        return self._PriceName

    @PriceName.setter
    def PriceName(self, PriceName):
        self._PriceName = PriceName

    @property
    def OriginUnitPrice(self):
        r"""计费项维度单价。
        :rtype: float
        """
        return self._OriginUnitPrice

    @OriginUnitPrice.setter
    def OriginUnitPrice(self, OriginUnitPrice):
        self._OriginUnitPrice = OriginUnitPrice

    @property
    def OriginalPrice(self):
        r"""计费项维度总价。
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        r"""计费项维度折扣。
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        r"""计费项维度折后总价。
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._PriceName = params.get("PriceName")
        self._OriginUnitPrice = params.get("OriginUnitPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    r"""DisassociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 密钥对 ID 列表，每次请求批量密钥对的上限为 100。可通过[DescribeKeyPairs](https://cloud.tencent.com/document/api/1207/55540)接口返回值中的KeyId获取。
        :type KeyIds: list of str
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self._KeyIds = None
        self._InstanceIds = None

    @property
    def KeyIds(self):
        r"""密钥对 ID 列表，每次请求批量密钥对的上限为 100。可通过[DescribeKeyPairs](https://cloud.tencent.com/document/api/1207/55540)接口返回值中的KeyId获取。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    r"""DisassociateInstancesKeyPairs返回参数结构体

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


class DiscountDetail(AbstractModel):
    r"""套餐折扣详情（仅用于控制台调用询价相关接口返回）。

    """

    def __init__(self):
        r"""
        :param _TimeSpan: 计费时长。
        :type TimeSpan: int
        :param _TimeUnit: 时间单位。
取值为：
- m - 月
- d - 日
        :type TimeUnit: str
        :param _TotalCost: 总价。
        :type TotalCost: float
        :param _RealTotalCost: 折后总价。
        :type RealTotalCost: float
        :param _Discount: 折扣。
        :type Discount: float
        :param _PolicyDetail: 具体折扣详情。
        :type PolicyDetail: :class:`tencentcloud.lighthouse.v20200324.models.PolicyDetail`
        """
        self._TimeSpan = None
        self._TimeUnit = None
        self._TotalCost = None
        self._RealTotalCost = None
        self._Discount = None
        self._PolicyDetail = None

    @property
    def TimeSpan(self):
        r"""计费时长。
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""时间单位。
取值为：
- m - 月
- d - 日
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TotalCost(self):
        r"""总价。
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        r"""折后总价。
        :rtype: float
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Discount(self):
        r"""折扣。
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def PolicyDetail(self):
        r"""具体折扣详情。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.PolicyDetail`
        """
        return self._PolicyDetail

    @PolicyDetail.setter
    def PolicyDetail(self, PolicyDetail):
        self._PolicyDetail = PolicyDetail


    def _deserialize(self, params):
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._TotalCost = params.get("TotalCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Discount = params.get("Discount")
        if params.get("PolicyDetail") is not None:
            self._PolicyDetail = PolicyDetail()
            self._PolicyDetail._deserialize(params.get("PolicyDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Disk(AbstractModel):
    r"""云硬盘信息。

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID。
        :type DiskId: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Zone: 可用区。
        :type Zone: str
        :param _DiskName: 云硬盘名称。
        :type DiskName: str
        :param _DiskUsage: 云硬盘类型。
枚举值：
<li> SYSTEM_DISK: 系统盘 </li>
<li> DATA_DISK: 数据盘 </li>

        :type DiskUsage: str
        :param _DiskType: 云硬盘介质类型。
枚举值:
<li> CLOUD_BASIC: 普通云硬盘 </li>
<li> CLOUD_PREMIUM: 高性能云硬盘 </li>
<li> CLOUD_SSD: SSD云硬盘 </li>
        :type DiskType: str
        :param _DiskChargeType: 云硬盘付费类型。
<li> PREPAID: 预付费 </li>
<li> POSTPAID_BY_HOUR: 按小时后付费 </li>
        :type DiskChargeType: str
        :param _DiskSize: 云硬盘大小, 单位GB。
        :type DiskSize: int
        :param _RenewFlag: 续费标识。
        :type RenewFlag: str
        :param _DiskState: 云硬盘状态，取值范围：
<li>PENDING：创建中。 </li>
<li>UNATTACHED：待挂载。</li>
<li>ATTACHING：挂载中。</li>
<li>ATTACHED：已挂载。</li>
<li>DETACHING：卸载中。 </li>
<li> SHUTDOWN：已隔离。</li>
<li> CREATED_FAILED：创建失败。</li>
<li>TERMINATING：销毁中。</li>
<li> DELETING：删除中。</li>
<li> FREEZING：冻结中。</li>
        :type DiskState: str
        :param _Attached: 云硬盘挂载状态。
        :type Attached: bool
        :param _DeleteWithInstance: 是否随实例释放。
        :type DeleteWithInstance: bool
        :param _LatestOperation: 上一次操作。
        :type LatestOperation: str
        :param _LatestOperationState: 上一次操作状态。
        :type LatestOperationState: str
        :param _LatestOperationRequestId: 上一次请求ID。
        :type LatestOperationRequestId: str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ExpiredTime: 到期时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param _IsolatedTime: 隔离时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param _DiskBackupCount: 云硬盘的已有备份点数量。
        :type DiskBackupCount: int
        :param _DiskBackupQuota: 云硬盘的备份点配额数量。
        :type DiskBackupQuota: int
        :param _Tags: 云硬盘绑定的标签列表。
        :type Tags: list of Tag
        """
        self._DiskId = None
        self._InstanceId = None
        self._Zone = None
        self._DiskName = None
        self._DiskUsage = None
        self._DiskType = None
        self._DiskChargeType = None
        self._DiskSize = None
        self._RenewFlag = None
        self._DiskState = None
        self._Attached = None
        self._DeleteWithInstance = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._IsolatedTime = None
        self._DiskBackupCount = None
        self._DiskBackupQuota = None
        self._Tags = None

    @property
    def DiskId(self):
        r"""云硬盘ID。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def InstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        r"""可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DiskName(self):
        r"""云硬盘名称。
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def DiskUsage(self):
        r"""云硬盘类型。
枚举值：
<li> SYSTEM_DISK: 系统盘 </li>
<li> DATA_DISK: 数据盘 </li>

        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskType(self):
        r"""云硬盘介质类型。
枚举值:
<li> CLOUD_BASIC: 普通云硬盘 </li>
<li> CLOUD_PREMIUM: 高性能云硬盘 </li>
<li> CLOUD_SSD: SSD云硬盘 </li>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskChargeType(self):
        r"""云硬盘付费类型。
<li> PREPAID: 预付费 </li>
<li> POSTPAID_BY_HOUR: 按小时后付费 </li>
        :rtype: str
        """
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskSize(self):
        r"""云硬盘大小, 单位GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def RenewFlag(self):
        r"""续费标识。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def DiskState(self):
        r"""云硬盘状态，取值范围：
<li>PENDING：创建中。 </li>
<li>UNATTACHED：待挂载。</li>
<li>ATTACHING：挂载中。</li>
<li>ATTACHED：已挂载。</li>
<li>DETACHING：卸载中。 </li>
<li> SHUTDOWN：已隔离。</li>
<li> CREATED_FAILED：创建失败。</li>
<li>TERMINATING：销毁中。</li>
<li> DELETING：删除中。</li>
<li> FREEZING：冻结中。</li>
        :rtype: str
        """
        return self._DiskState

    @DiskState.setter
    def DiskState(self, DiskState):
        self._DiskState = DiskState

    @property
    def Attached(self):
        r"""云硬盘挂载状态。
        :rtype: bool
        """
        return self._Attached

    @Attached.setter
    def Attached(self, Attached):
        self._Attached = Attached

    @property
    def DeleteWithInstance(self):
        r"""是否随实例释放。
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def LatestOperation(self):
        r"""上一次操作。
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        r"""上一次操作状态。
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        r"""上一次请求ID。
        :rtype: str
        """
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def CreatedTime(self):
        r"""创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        r"""到期时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def IsolatedTime(self):
        r"""隔离时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def DiskBackupCount(self):
        r"""云硬盘的已有备份点数量。
        :rtype: int
        """
        return self._DiskBackupCount

    @DiskBackupCount.setter
    def DiskBackupCount(self, DiskBackupCount):
        self._DiskBackupCount = DiskBackupCount

    @property
    def DiskBackupQuota(self):
        r"""云硬盘的备份点配额数量。
        :rtype: int
        """
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota

    @property
    def Tags(self):
        r"""云硬盘绑定的标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._DiskName = params.get("DiskName")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskType = params.get("DiskType")
        self._DiskChargeType = params.get("DiskChargeType")
        self._DiskSize = params.get("DiskSize")
        self._RenewFlag = params.get("RenewFlag")
        self._DiskState = params.get("DiskState")
        self._Attached = params.get("Attached")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._IsolatedTime = params.get("IsolatedTime")
        self._DiskBackupCount = params.get("DiskBackupCount")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskBackup(AbstractModel):
    r"""描述了云硬盘备份点相关信息。

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: 云硬盘备份点ID。
        :type DiskBackupId: str
        :param _DiskUsage: 创建此云硬盘备份点的云硬盘类型。取值：<li>DATA_DISK：数据盘</li>
        :type DiskUsage: str
        :param _DiskId: 创建此云硬盘备份点的云硬盘 ID。
        :type DiskId: str
        :param _DiskSize: 创建此云硬盘备份点的云硬盘大小，单位 GB。
        :type DiskSize: int
        :param _DiskBackupName: 云硬盘备份点名称，用户自定义的云硬盘备份点别名。
        :type DiskBackupName: str
        :param _DiskBackupState: 云硬盘备份点的状态。取值范围：
<li>NORMAL：正常。 </li>
<li>CREATING：创建中。</li>
<li>ROLLBACKING：回滚中。</li>
<li>DELETING：删除中。</li>
        :type DiskBackupState: str
        :param _Percent: 创建或回滚云硬盘备份点进度百分比，成功后此字段取值为 100。
        :type Percent: int
        :param _LatestOperation: 上一次操作
        :type LatestOperation: str
        :param _LatestOperationState: 上一次操作状态
        :type LatestOperationState: str
        :param _LatestOperationRequestId: 上一次请求ID
        :type LatestOperationRequestId: str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :type CreatedTime: str
        :param _Tags: 云硬盘备份点绑定的标签列表。
        :type Tags: list of Tag
        """
        self._DiskBackupId = None
        self._DiskUsage = None
        self._DiskId = None
        self._DiskSize = None
        self._DiskBackupName = None
        self._DiskBackupState = None
        self._Percent = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._CreatedTime = None
        self._Tags = None

    @property
    def DiskBackupId(self):
        r"""云硬盘备份点ID。
        :rtype: str
        """
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def DiskUsage(self):
        r"""创建此云硬盘备份点的云硬盘类型。取值：<li>DATA_DISK：数据盘</li>
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskId(self):
        r"""创建此云硬盘备份点的云硬盘 ID。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        r"""创建此云硬盘备份点的云硬盘大小，单位 GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskBackupName(self):
        r"""云硬盘备份点名称，用户自定义的云硬盘备份点别名。
        :rtype: str
        """
        return self._DiskBackupName

    @DiskBackupName.setter
    def DiskBackupName(self, DiskBackupName):
        self._DiskBackupName = DiskBackupName

    @property
    def DiskBackupState(self):
        r"""云硬盘备份点的状态。取值范围：
<li>NORMAL：正常。 </li>
<li>CREATING：创建中。</li>
<li>ROLLBACKING：回滚中。</li>
<li>DELETING：删除中。</li>
        :rtype: str
        """
        return self._DiskBackupState

    @DiskBackupState.setter
    def DiskBackupState(self, DiskBackupState):
        self._DiskBackupState = DiskBackupState

    @property
    def Percent(self):
        r"""创建或回滚云硬盘备份点进度百分比，成功后此字段取值为 100。
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def LatestOperation(self):
        r"""上一次操作
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        r"""上一次操作状态
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        r"""上一次请求ID
        :rtype: str
        """
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def CreatedTime(self):
        r"""创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        r"""云硬盘备份点绑定的标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._DiskBackupName = params.get("DiskBackupName")
        self._DiskBackupState = params.get("DiskBackupState")
        self._Percent = params.get("Percent")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskBackupDeniedActions(AbstractModel):
    r"""云硬盘备份点操作限制列表。

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: 云硬盘备份点ID。
        :type DiskBackupId: str
        :param _DeniedActions: 操作限制列表。
        :type DeniedActions: list of DeniedAction
        """
        self._DiskBackupId = None
        self._DeniedActions = None

    @property
    def DiskBackupId(self):
        r"""云硬盘备份点ID。
        :rtype: str
        """
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def DeniedActions(self):
        r"""操作限制列表。
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskChargePrepaid(AbstractModel):
    r"""云硬盘包年包月相关参数设置

    """

    def __init__(self):
        r"""
        :param _Period: 新购周期。
可选值：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：
- NOTIFY_AND_AUTO_RENEW：通知过期且自动续费。
- NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费。
- DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知。

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，云硬盘到期后将按月自动续费。
        :type RenewFlag: str
        :param _TimeUnit: 新购单位.。
可选值：m - 月。
默认值：m - 月。
        :type TimeUnit: str
        """
        self._Period = None
        self._RenewFlag = None
        self._TimeUnit = None

    @property
    def Period(self):
        r"""新购周期。
可选值：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围：
- NOTIFY_AND_AUTO_RENEW：通知过期且自动续费。
- NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费。
- DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知。

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，云硬盘到期后将按月自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeUnit(self):
        r"""新购单位.。
可选值：m - 月。
默认值：m - 月。
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskConfig(AbstractModel):
    r"""云硬盘配置

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区。
        :type Zone: str
        :param _DiskType: 云硬盘类型。枚举值如下：

<li>CLOUD_BASIC：普通云硬盘</li>
<li>CLOUD_PREMIUM：高性能云硬盘</li>
<li>CLOUD_SSD：SSD云硬盘</li>
        :type DiskType: str
        :param _DiskSalesState: 云硬盘可售卖状态。
        :type DiskSalesState: str
        :param _MaxDiskSize: 最大云硬盘大小。
        :type MaxDiskSize: int
        :param _MinDiskSize: 最小云硬盘大小。
        :type MinDiskSize: int
        :param _DiskStepSize: 云硬盘步长。
        :type DiskStepSize: int
        """
        self._Zone = None
        self._DiskType = None
        self._DiskSalesState = None
        self._MaxDiskSize = None
        self._MinDiskSize = None
        self._DiskStepSize = None

    @property
    def Zone(self):
        r"""可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DiskType(self):
        r"""云硬盘类型。枚举值如下：

<li>CLOUD_BASIC：普通云硬盘</li>
<li>CLOUD_PREMIUM：高性能云硬盘</li>
<li>CLOUD_SSD：SSD云硬盘</li>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSalesState(self):
        r"""云硬盘可售卖状态。
        :rtype: str
        """
        return self._DiskSalesState

    @DiskSalesState.setter
    def DiskSalesState(self, DiskSalesState):
        self._DiskSalesState = DiskSalesState

    @property
    def MaxDiskSize(self):
        r"""最大云硬盘大小。
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MinDiskSize(self):
        r"""最小云硬盘大小。
        :rtype: int
        """
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def DiskStepSize(self):
        r"""云硬盘步长。
        :rtype: int
        """
        return self._DiskStepSize

    @DiskStepSize.setter
    def DiskStepSize(self, DiskStepSize):
        self._DiskStepSize = DiskStepSize


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DiskType = params.get("DiskType")
        self._DiskSalesState = params.get("DiskSalesState")
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._MinDiskSize = params.get("MinDiskSize")
        self._DiskStepSize = params.get("DiskStepSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskDeniedActions(AbstractModel):
    r"""磁盘操作限制列表详细信息

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID。
        :type DiskId: str
        :param _DeniedActions: 操作限制列表。
        :type DeniedActions: list of DeniedAction
        """
        self._DiskId = None
        self._DeniedActions = None

    @property
    def DiskId(self):
        r"""云硬盘ID。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DeniedActions(self):
        r"""操作限制列表。
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskPrice(AbstractModel):
    r"""云硬盘价格

    """

    def __init__(self):
        r"""
        :param _OriginalDiskPrice: 云硬盘单价。
        :type OriginalDiskPrice: float
        :param _OriginalPrice: 云硬盘总价。
        :type OriginalPrice: float
        :param _Discount: 折扣。
        :type Discount: float
        :param _DiscountPrice: 折后总价。
        :type DiscountPrice: float
        :param _DetailPrices: 计费项目明细列表。
        :type DetailPrices: list of DetailPrice
        """
        self._OriginalDiskPrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None
        self._DetailPrices = None

    @property
    def OriginalDiskPrice(self):
        r"""云硬盘单价。
        :rtype: float
        """
        return self._OriginalDiskPrice

    @OriginalDiskPrice.setter
    def OriginalDiskPrice(self, OriginalDiskPrice):
        self._OriginalDiskPrice = OriginalDiskPrice

    @property
    def OriginalPrice(self):
        r"""云硬盘总价。
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        r"""折扣。
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        r"""折后总价。
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def DetailPrices(self):
        r"""计费项目明细列表。
        :rtype: list of DetailPrice
        """
        return self._DetailPrices

    @DetailPrices.setter
    def DetailPrices(self, DetailPrices):
        self._DetailPrices = DetailPrices


    def _deserialize(self, params):
        self._OriginalDiskPrice = params.get("OriginalDiskPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        if params.get("DetailPrices") is not None:
            self._DetailPrices = []
            for item in params.get("DetailPrices"):
                obj = DetailPrice()
                obj._deserialize(item)
                self._DetailPrices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskReturnable(AbstractModel):
    r"""可退还云硬盘详细信息

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID。
        :type DiskId: str
        :param _IsReturnable: 云硬盘是否可退还。
        :type IsReturnable: bool
        :param _ReturnFailCode: 云硬盘退还失败错误码。
        :type ReturnFailCode: int
        :param _ReturnFailMessage: 云硬盘退还失败错误信息。
        :type ReturnFailMessage: str
        """
        self._DiskId = None
        self._IsReturnable = None
        self._ReturnFailCode = None
        self._ReturnFailMessage = None

    @property
    def DiskId(self):
        r"""云硬盘ID。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def IsReturnable(self):
        r"""云硬盘是否可退还。
        :rtype: bool
        """
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def ReturnFailCode(self):
        r"""云硬盘退还失败错误码。
        :rtype: int
        """
        return self._ReturnFailCode

    @ReturnFailCode.setter
    def ReturnFailCode(self, ReturnFailCode):
        self._ReturnFailCode = ReturnFailCode

    @property
    def ReturnFailMessage(self):
        r"""云硬盘退还失败错误信息。
        :rtype: str
        """
        return self._ReturnFailMessage

    @ReturnFailMessage.setter
    def ReturnFailMessage(self, ReturnFailMessage):
        self._ReturnFailMessage = ReturnFailMessage


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._IsReturnable = params.get("IsReturnable")
        self._ReturnFailCode = params.get("ReturnFailCode")
        self._ReturnFailMessage = params.get("ReturnFailMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DockerActivity(AbstractModel):
    r"""Docker活动信息

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动ID。
        :type ActivityId: str
        :param _ActivityName: 活动名称。
        :type ActivityName: str
        :param _ActivityState: 活动状态。取值范围： 
<li>INIT：表示初始化，活动尚未执行</li>
<li>OPERATING：表示活动执行中</li>
<li>SUCCESS：表示活动执行成功</li>
<li>FAILED：表示活动执行失败</li>
        :type ActivityState: str
        :param _ActivityCommandOutput: 活动执行的命令输出，以base64编码。
        :type ActivityCommandOutput: str
        :param _ContainerIds: 容器ID列表。
        :type ContainerIds: list of str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。
        :type CreatedTime: str
        :param _EndTime: 结束时间。按照 ISO8601 标准表示，并且使用 UTC 时间。
        :type EndTime: str
        """
        self._ActivityId = None
        self._ActivityName = None
        self._ActivityState = None
        self._ActivityCommandOutput = None
        self._ContainerIds = None
        self._CreatedTime = None
        self._EndTime = None

    @property
    def ActivityId(self):
        r"""活动ID。
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityName(self):
        r"""活动名称。
        :rtype: str
        """
        return self._ActivityName

    @ActivityName.setter
    def ActivityName(self, ActivityName):
        self._ActivityName = ActivityName

    @property
    def ActivityState(self):
        r"""活动状态。取值范围： 
<li>INIT：表示初始化，活动尚未执行</li>
<li>OPERATING：表示活动执行中</li>
<li>SUCCESS：表示活动执行成功</li>
<li>FAILED：表示活动执行失败</li>
        :rtype: str
        """
        return self._ActivityState

    @ActivityState.setter
    def ActivityState(self, ActivityState):
        self._ActivityState = ActivityState

    @property
    def ActivityCommandOutput(self):
        r"""活动执行的命令输出，以base64编码。
        :rtype: str
        """
        return self._ActivityCommandOutput

    @ActivityCommandOutput.setter
    def ActivityCommandOutput(self, ActivityCommandOutput):
        self._ActivityCommandOutput = ActivityCommandOutput

    @property
    def ContainerIds(self):
        r"""容器ID列表。
        :rtype: list of str
        """
        return self._ContainerIds

    @ContainerIds.setter
    def ContainerIds(self, ContainerIds):
        self._ContainerIds = ContainerIds

    @property
    def CreatedTime(self):
        r"""创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def EndTime(self):
        r"""结束时间。按照 ISO8601 标准表示，并且使用 UTC 时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._ActivityName = params.get("ActivityName")
        self._ActivityState = params.get("ActivityState")
        self._ActivityCommandOutput = params.get("ActivityCommandOutput")
        self._ContainerIds = params.get("ContainerIds")
        self._CreatedTime = params.get("CreatedTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DockerContainer(AbstractModel):
    r"""Docker容器信息

    """

    def __init__(self):
        r"""
        :param _ContainerId: 容器ID
        :type ContainerId: str
        :param _ContainerName: 容器名称
        :type ContainerName: str
        :param _ContainerImage: 容器镜像地址
        :type ContainerImage: str
        :param _Command: 容器Command
        :type Command: str
        :param _Status: 容器状态描述
        :type Status: str
        :param _State: 容器状态，和docker的容器状态保持一致，当前取值有：created（已创建）、restarting（重启中）、running（运行中）、removing（迁移中）、paused（暂停）、exited（停止）和dead（死亡）

        :type State: str
        :param _PublishPortSet: 容器端口主机端口映射列表
        :type PublishPortSet: list of DockerContainerPublishPort
        :param _VolumeSet: 容器挂载本地卷列表
        :type VolumeSet: list of DockerContainerVolume
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。
        :type CreatedTime: str
        """
        self._ContainerId = None
        self._ContainerName = None
        self._ContainerImage = None
        self._Command = None
        self._Status = None
        self._State = None
        self._PublishPortSet = None
        self._VolumeSet = None
        self._CreatedTime = None

    @property
    def ContainerId(self):
        r"""容器ID
        :rtype: str
        """
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId

    @property
    def ContainerName(self):
        r"""容器名称
        :rtype: str
        """
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def ContainerImage(self):
        r"""容器镜像地址
        :rtype: str
        """
        return self._ContainerImage

    @ContainerImage.setter
    def ContainerImage(self, ContainerImage):
        self._ContainerImage = ContainerImage

    @property
    def Command(self):
        r"""容器Command
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Status(self):
        r"""容器状态描述
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def State(self):
        r"""容器状态，和docker的容器状态保持一致，当前取值有：created（已创建）、restarting（重启中）、running（运行中）、removing（迁移中）、paused（暂停）、exited（停止）和dead（死亡）

        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def PublishPortSet(self):
        r"""容器端口主机端口映射列表
        :rtype: list of DockerContainerPublishPort
        """
        return self._PublishPortSet

    @PublishPortSet.setter
    def PublishPortSet(self, PublishPortSet):
        self._PublishPortSet = PublishPortSet

    @property
    def VolumeSet(self):
        r"""容器挂载本地卷列表
        :rtype: list of DockerContainerVolume
        """
        return self._VolumeSet

    @VolumeSet.setter
    def VolumeSet(self, VolumeSet):
        self._VolumeSet = VolumeSet

    @property
    def CreatedTime(self):
        r"""创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._ContainerId = params.get("ContainerId")
        self._ContainerName = params.get("ContainerName")
        self._ContainerImage = params.get("ContainerImage")
        self._Command = params.get("Command")
        self._Status = params.get("Status")
        self._State = params.get("State")
        if params.get("PublishPortSet") is not None:
            self._PublishPortSet = []
            for item in params.get("PublishPortSet"):
                obj = DockerContainerPublishPort()
                obj._deserialize(item)
                self._PublishPortSet.append(obj)
        if params.get("VolumeSet") is not None:
            self._VolumeSet = []
            for item in params.get("VolumeSet"):
                obj = DockerContainerVolume()
                obj._deserialize(item)
                self._VolumeSet.append(obj)
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DockerContainerConfiguration(AbstractModel):
    r"""Docker容器创建时的配置

    """

    def __init__(self):
        r"""
        :param _ContainerImage: 容器镜像地址
        :type ContainerImage: str
        :param _ContainerName: 容器名称
        :type ContainerName: str
        :param _Envs: 环境变量列表
        :type Envs: list of ContainerEnv
        :param _PublishPorts: 容器端口主机端口映射列表
        :type PublishPorts: list of DockerContainerPublishPort
        :param _Volumes: 容器加载本地卷列表
        :type Volumes: list of DockerContainerVolume
        :param _Command: 运行的命令
        :type Command: str
        :param _RestartPolicy: 容器重启策略。
- no -默认策略，在容器退出时不重启容器
- on-failure -在容器非正常退出时（退出状态非0），才会重启容器
- on-failure:3 -在容器非正常退出时重启容器，最多重启3次
- always -在容器退出时总是重启容器
        :type RestartPolicy: str
        """
        self._ContainerImage = None
        self._ContainerName = None
        self._Envs = None
        self._PublishPorts = None
        self._Volumes = None
        self._Command = None
        self._RestartPolicy = None

    @property
    def ContainerImage(self):
        r"""容器镜像地址
        :rtype: str
        """
        return self._ContainerImage

    @ContainerImage.setter
    def ContainerImage(self, ContainerImage):
        self._ContainerImage = ContainerImage

    @property
    def ContainerName(self):
        r"""容器名称
        :rtype: str
        """
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def Envs(self):
        r"""环境变量列表
        :rtype: list of ContainerEnv
        """
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def PublishPorts(self):
        r"""容器端口主机端口映射列表
        :rtype: list of DockerContainerPublishPort
        """
        return self._PublishPorts

    @PublishPorts.setter
    def PublishPorts(self, PublishPorts):
        self._PublishPorts = PublishPorts

    @property
    def Volumes(self):
        r"""容器加载本地卷列表
        :rtype: list of DockerContainerVolume
        """
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def Command(self):
        r"""运行的命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def RestartPolicy(self):
        r"""容器重启策略。
- no -默认策略，在容器退出时不重启容器
- on-failure -在容器非正常退出时（退出状态非0），才会重启容器
- on-failure:3 -在容器非正常退出时重启容器，最多重启3次
- always -在容器退出时总是重启容器
        :rtype: str
        """
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy


    def _deserialize(self, params):
        self._ContainerImage = params.get("ContainerImage")
        self._ContainerName = params.get("ContainerName")
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = ContainerEnv()
                obj._deserialize(item)
                self._Envs.append(obj)
        if params.get("PublishPorts") is not None:
            self._PublishPorts = []
            for item in params.get("PublishPorts"):
                obj = DockerContainerPublishPort()
                obj._deserialize(item)
                self._PublishPorts.append(obj)
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = DockerContainerVolume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        self._Command = params.get("Command")
        self._RestartPolicy = params.get("RestartPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DockerContainerPublishPort(AbstractModel):
    r"""Docker容器映射的端口

    """

    def __init__(self):
        r"""
        :param _HostPort: 主机端口
        :type HostPort: int
        :param _ContainerPort: 容器端口
        :type ContainerPort: int
        :param _Ip: 对外绑定IP，默认0.0.0.0
        :type Ip: str
        :param _Protocol: 协议，默认tcp，支持tcp/udp/sctp
        :type Protocol: str
        """
        self._HostPort = None
        self._ContainerPort = None
        self._Ip = None
        self._Protocol = None

    @property
    def HostPort(self):
        r"""主机端口
        :rtype: int
        """
        return self._HostPort

    @HostPort.setter
    def HostPort(self, HostPort):
        self._HostPort = HostPort

    @property
    def ContainerPort(self):
        r"""容器端口
        :rtype: int
        """
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def Ip(self):
        r"""对外绑定IP，默认0.0.0.0
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Protocol(self):
        r"""协议，默认tcp，支持tcp/udp/sctp
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._HostPort = params.get("HostPort")
        self._ContainerPort = params.get("ContainerPort")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DockerContainerVolume(AbstractModel):
    r"""Docker容器挂载卷

    """

    def __init__(self):
        r"""
        :param _ContainerPath: 容器路径
        :type ContainerPath: str
        :param _HostPath: 主机路径
        :type HostPath: str
        """
        self._ContainerPath = None
        self._HostPath = None

    @property
    def ContainerPath(self):
        r"""容器路径
        :rtype: str
        """
        return self._ContainerPath

    @ContainerPath.setter
    def ContainerPath(self, ContainerPath):
        self._ContainerPath = ContainerPath

    @property
    def HostPath(self):
        r"""主机路径
        :rtype: str
        """
        return self._HostPath

    @HostPath.setter
    def HostPath(self, HostPath):
        self._HostPath = HostPath


    def _deserialize(self, params):
        self._ContainerPath = params.get("ContainerPath")
        self._HostPath = params.get("HostPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r""">描述键值对过滤器，用于条件过滤查询。例如过滤名称等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以DescribeInstances接口的`Filter`为例。若我们需要查询实例名称（`instance-name`）为test ***并且*** 实例内网IP（`private-ip-address`）为10.10.10.10的实例时，可如下实现：
    ```
    Filters.0.Name=instance-name
    &Filters.0.Values.0=test
    &Filters.1.Name=private-ip-address
    &Filters.1.Values.0=10.10.10.10
    ```

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""需要过滤的字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""字段的过滤值。
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
        


class FirewallRule(AbstractModel):
    r"""描述防火墙规则信息。

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议，取值：TCP，UDP，ICMP，ALL，ICMPv6。

- 使用ICMP协议时，只支持CidrBlock，不支持使用Port、Ipv6CidrBlock参数；
- 使用ICMPv6协议时，只支持Ipv6CidrBlock，不支持使用Port、Ipv6CidrBlock参数；
        :type Protocol: str
        :param _Port: 端口，取值：ALL，单独的端口，逗号分隔的离散端口，减号分隔的端口范围。注意：单独的端口与离散端口不能同时存在。
        :type Port: str
        :param _CidrBlock: IPv4网段或 IPv4地址(互斥)。
示例值：0.0.0.0/0。

和Ipv6CidrBlock互斥，两者都不指定时，如果Protocol不是ICMPv6，则取默认值0.0.0.0/0。
        :type CidrBlock: str
        :param _Ipv6CidrBlock: IPv6网段或IPv6地址(互斥)。
示例值：::/0。

和CidrBlock互斥，两者都不指定时，如果Protocol是ICMPv6，则取默认值::/0。
        :type Ipv6CidrBlock: str
        :param _Action: 取值：ACCEPT（允许），DROP（拒绝）。默认为 ACCEPT。
        :type Action: str
        :param _FirewallRuleDescription: 防火墙规则描述。
        :type FirewallRuleDescription: str
        """
        self._Protocol = None
        self._Port = None
        self._CidrBlock = None
        self._Ipv6CidrBlock = None
        self._Action = None
        self._FirewallRuleDescription = None

    @property
    def Protocol(self):
        r"""协议，取值：TCP，UDP，ICMP，ALL，ICMPv6。

- 使用ICMP协议时，只支持CidrBlock，不支持使用Port、Ipv6CidrBlock参数；
- 使用ICMPv6协议时，只支持Ipv6CidrBlock，不支持使用Port、Ipv6CidrBlock参数；
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""端口，取值：ALL，单独的端口，逗号分隔的离散端口，减号分隔的端口范围。注意：单独的端口与离散端口不能同时存在。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CidrBlock(self):
        r"""IPv4网段或 IPv4地址(互斥)。
示例值：0.0.0.0/0。

和Ipv6CidrBlock互斥，两者都不指定时，如果Protocol不是ICMPv6，则取默认值0.0.0.0/0。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Ipv6CidrBlock(self):
        r"""IPv6网段或IPv6地址(互斥)。
示例值：::/0。

和CidrBlock互斥，两者都不指定时，如果Protocol是ICMPv6，则取默认值::/0。
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

    @property
    def Action(self):
        r"""取值：ACCEPT（允许），DROP（拒绝）。默认为 ACCEPT。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def FirewallRuleDescription(self):
        r"""防火墙规则描述。
        :rtype: str
        """
        return self._FirewallRuleDescription

    @FirewallRuleDescription.setter
    def FirewallRuleDescription(self, FirewallRuleDescription):
        self._FirewallRuleDescription = FirewallRuleDescription


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._CidrBlock = params.get("CidrBlock")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self._Action = params.get("Action")
        self._FirewallRuleDescription = params.get("FirewallRuleDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallRuleInfo(AbstractModel):
    r"""描述防火墙规则详细信息。

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型，取值：自定义，HTTP(80)，HTTPS(443)，Linux登录(22)，Windows登录(3389)，MySQL(3306)，SQL Server(1433)，全部TCP，全部UDP，Ping-ICMP，Windows登录优化 (3389)，FTP (21)，Ping，Ping (IPv6)，ALL。
        :type AppType: str
        :param _Protocol: 协议，取值：TCP，UDP，ICMP，ICMPv6，ALL。
        :type Protocol: str
        :param _Port: 端口，取值：ALL，单独的端口，逗号分隔的离散端口，减号分隔的端口范围。
        :type Port: str
        :param _CidrBlock: IPv4网段或 IPv4地址(互斥)。
示例值：0.0.0.0/0。

和Ipv6CidrBlock互斥，两者都不指定时，如果Protocol不是ICMPv6，则取默认值0.0.0.0/0。
        :type CidrBlock: str
        :param _Ipv6CidrBlock: IPv6网段或IPv6地址(互斥)。
示例值：::/0。

和CidrBlock互斥，两者都不指定时，如果Protocol是ICMPv6，则取默认值::/0。
        :type Ipv6CidrBlock: str
        :param _Action: 取值：ACCEPT，DROP。默认为 ACCEPT。
        :type Action: str
        :param _FirewallRuleDescription: 防火墙规则描述。
        :type FirewallRuleDescription: str
        """
        self._AppType = None
        self._Protocol = None
        self._Port = None
        self._CidrBlock = None
        self._Ipv6CidrBlock = None
        self._Action = None
        self._FirewallRuleDescription = None

    @property
    def AppType(self):
        r"""应用类型，取值：自定义，HTTP(80)，HTTPS(443)，Linux登录(22)，Windows登录(3389)，MySQL(3306)，SQL Server(1433)，全部TCP，全部UDP，Ping-ICMP，Windows登录优化 (3389)，FTP (21)，Ping，Ping (IPv6)，ALL。
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def Protocol(self):
        r"""协议，取值：TCP，UDP，ICMP，ICMPv6，ALL。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""端口，取值：ALL，单独的端口，逗号分隔的离散端口，减号分隔的端口范围。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CidrBlock(self):
        r"""IPv4网段或 IPv4地址(互斥)。
示例值：0.0.0.0/0。

和Ipv6CidrBlock互斥，两者都不指定时，如果Protocol不是ICMPv6，则取默认值0.0.0.0/0。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Ipv6CidrBlock(self):
        r"""IPv6网段或IPv6地址(互斥)。
示例值：::/0。

和CidrBlock互斥，两者都不指定时，如果Protocol是ICMPv6，则取默认值::/0。
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

    @property
    def Action(self):
        r"""取值：ACCEPT，DROP。默认为 ACCEPT。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def FirewallRuleDescription(self):
        r"""防火墙规则描述。
        :rtype: str
        """
        return self._FirewallRuleDescription

    @FirewallRuleDescription.setter
    def FirewallRuleDescription(self, FirewallRuleDescription):
        self._FirewallRuleDescription = FirewallRuleDescription


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._CidrBlock = params.get("CidrBlock")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self._Action = params.get("Action")
        self._FirewallRuleDescription = params.get("FirewallRuleDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallTemplate(AbstractModel):
    r"""防火墙模板信息。

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID。
        :type TemplateId: str
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _TemplateType: 模板类型。取值: "PRIVATE"(个人模板)
        :type TemplateType: str
        :param _TemplateState: 模板状态。取值: "NORMAL"(正常)
        :type TemplateState: str
        :param _CreatedTime: 模板创建时间。
        :type CreatedTime: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateType = None
        self._TemplateState = None
        self._CreatedTime = None

    @property
    def TemplateId(self):
        r"""模板ID。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""模板名称。
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateType(self):
        r"""模板类型。取值: "PRIVATE"(个人模板)
        :rtype: str
        """
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def TemplateState(self):
        r"""模板状态。取值: "NORMAL"(正常)
        :rtype: str
        """
        return self._TemplateState

    @TemplateState.setter
    def TemplateState(self, TemplateState):
        self._TemplateState = TemplateState

    @property
    def CreatedTime(self):
        r"""模板创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateType = params.get("TemplateType")
        self._TemplateState = params.get("TemplateState")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallTemplateApplyRecord(AbstractModel):
    r"""防火墙模板应用记录。

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _ApplyTime: 应用模板的时间。
        :type ApplyTime: str
        :param _TemplateRuleSet: 模板规则列表。
        :type TemplateRuleSet: list of FirewallTemplateRule
        :param _ApplyState: 应用模板的执行状态。

- SUCCESS：成功
- RUNNING：运行中
- FAILED：失败
        :type ApplyState: str
        :param _SuccessCount: 应用成功的实例数量。
        :type SuccessCount: int
        :param _FailedCount: 应用失败的实例数量。
        :type FailedCount: int
        :param _RunningCount: 正在应用中的实例数量。
        :type RunningCount: int
        :param _ApplyDetailSet: 应用模板的执行细节。
        :type ApplyDetailSet: list of FirewallTemplateApplyRecordDetail
        """
        self._TaskId = None
        self._ApplyTime = None
        self._TemplateRuleSet = None
        self._ApplyState = None
        self._SuccessCount = None
        self._FailedCount = None
        self._RunningCount = None
        self._ApplyDetailSet = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ApplyTime(self):
        r"""应用模板的时间。
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def TemplateRuleSet(self):
        r"""模板规则列表。
        :rtype: list of FirewallTemplateRule
        """
        return self._TemplateRuleSet

    @TemplateRuleSet.setter
    def TemplateRuleSet(self, TemplateRuleSet):
        self._TemplateRuleSet = TemplateRuleSet

    @property
    def ApplyState(self):
        r"""应用模板的执行状态。

- SUCCESS：成功
- RUNNING：运行中
- FAILED：失败
        :rtype: str
        """
        return self._ApplyState

    @ApplyState.setter
    def ApplyState(self, ApplyState):
        self._ApplyState = ApplyState

    @property
    def SuccessCount(self):
        r"""应用成功的实例数量。
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailedCount(self):
        r"""应用失败的实例数量。
        :rtype: int
        """
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount

    @property
    def RunningCount(self):
        r"""正在应用中的实例数量。
        :rtype: int
        """
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def ApplyDetailSet(self):
        r"""应用模板的执行细节。
        :rtype: list of FirewallTemplateApplyRecordDetail
        """
        return self._ApplyDetailSet

    @ApplyDetailSet.setter
    def ApplyDetailSet(self, ApplyDetailSet):
        self._ApplyDetailSet = ApplyDetailSet


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ApplyTime = params.get("ApplyTime")
        if params.get("TemplateRuleSet") is not None:
            self._TemplateRuleSet = []
            for item in params.get("TemplateRuleSet"):
                obj = FirewallTemplateRule()
                obj._deserialize(item)
                self._TemplateRuleSet.append(obj)
        self._ApplyState = params.get("ApplyState")
        self._SuccessCount = params.get("SuccessCount")
        self._FailedCount = params.get("FailedCount")
        self._RunningCount = params.get("RunningCount")
        if params.get("ApplyDetailSet") is not None:
            self._ApplyDetailSet = []
            for item in params.get("ApplyDetailSet"):
                obj = FirewallTemplateApplyRecordDetail()
                obj._deserialize(item)
                self._ApplyDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallTemplateApplyRecordDetail(AbstractModel):
    r"""防火墙模板应用记录详情。

    """

    def __init__(self):
        r"""
        :param _Instance: 实例标识信息。
        :type Instance: :class:`tencentcloud.lighthouse.v20200324.models.InstanceIdentifier`
        :param _ApplyState: 防火墙模板应用状态。

- SUCCESS：成功
- FAILED：失败
- RUNNING：运行中
        :type ApplyState: str
        :param _ErrorMessage: 防火墙模板应用错误信息。
        :type ErrorMessage: str
        """
        self._Instance = None
        self._ApplyState = None
        self._ErrorMessage = None

    @property
    def Instance(self):
        r"""实例标识信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InstanceIdentifier`
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def ApplyState(self):
        r"""防火墙模板应用状态。

- SUCCESS：成功
- FAILED：失败
- RUNNING：运行中
        :rtype: str
        """
        return self._ApplyState

    @ApplyState.setter
    def ApplyState(self, ApplyState):
        self._ApplyState = ApplyState

    @property
    def ErrorMessage(self):
        r"""防火墙模板应用错误信息。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        if params.get("Instance") is not None:
            self._Instance = InstanceIdentifier()
            self._Instance._deserialize(params.get("Instance"))
        self._ApplyState = params.get("ApplyState")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallTemplateRule(AbstractModel):
    r"""防火墙模板规则信息

    """

    def __init__(self):
        r"""
        :param _TemplateRuleId: 防火墙模板规则ID。
        :type TemplateRuleId: str
        :param _FirewallRule: 防火墙规则。
        :type FirewallRule: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRule`
        """
        self._TemplateRuleId = None
        self._FirewallRule = None

    @property
    def TemplateRuleId(self):
        r"""防火墙模板规则ID。
        :rtype: str
        """
        return self._TemplateRuleId

    @TemplateRuleId.setter
    def TemplateRuleId(self, TemplateRuleId):
        self._TemplateRuleId = TemplateRuleId

    @property
    def FirewallRule(self):
        r"""防火墙规则。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRule`
        """
        return self._FirewallRule

    @FirewallRule.setter
    def FirewallRule(self, FirewallRule):
        self._FirewallRule = FirewallRule


    def _deserialize(self, params):
        self._TemplateRuleId = params.get("TemplateRuleId")
        if params.get("FirewallRule") is not None:
            self._FirewallRule = FirewallRule()
            self._FirewallRule._deserialize(params.get("FirewallRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallTemplateRuleInfo(AbstractModel):
    r"""防火墙模板规则信息

    """

    def __init__(self):
        r"""
        :param _TemplateRuleId: 防火墙模板规则ID。
        :type TemplateRuleId: str
        :param _FirewallRuleInfo: 防火墙规则信息。
        :type FirewallRuleInfo: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRuleInfo`
        """
        self._TemplateRuleId = None
        self._FirewallRuleInfo = None

    @property
    def TemplateRuleId(self):
        r"""防火墙模板规则ID。
        :rtype: str
        """
        return self._TemplateRuleId

    @TemplateRuleId.setter
    def TemplateRuleId(self, TemplateRuleId):
        self._TemplateRuleId = TemplateRuleId

    @property
    def FirewallRuleInfo(self):
        r"""防火墙规则信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRuleInfo`
        """
        return self._FirewallRuleInfo

    @FirewallRuleInfo.setter
    def FirewallRuleInfo(self, FirewallRuleInfo):
        self._FirewallRuleInfo = FirewallRuleInfo


    def _deserialize(self, params):
        self._TemplateRuleId = params.get("TemplateRuleId")
        if params.get("FirewallRuleInfo") is not None:
            self._FirewallRuleInfo = FirewallRuleInfo()
            self._FirewallRuleInfo._deserialize(params.get("FirewallRuleInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralResourceQuota(AbstractModel):
    r"""描述通用资源配额信息。

    """

    def __init__(self):
        r"""
        :param _ResourceName: 资源名称。
        :type ResourceName: str
        :param _ResourceQuotaAvailable: 资源当前可用数量。
        :type ResourceQuotaAvailable: int
        :param _ResourceQuotaTotal: 资源总数量。
        :type ResourceQuotaTotal: int
        """
        self._ResourceName = None
        self._ResourceQuotaAvailable = None
        self._ResourceQuotaTotal = None

    @property
    def ResourceName(self):
        r"""资源名称。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceQuotaAvailable(self):
        r"""资源当前可用数量。
        :rtype: int
        """
        return self._ResourceQuotaAvailable

    @ResourceQuotaAvailable.setter
    def ResourceQuotaAvailable(self, ResourceQuotaAvailable):
        self._ResourceQuotaAvailable = ResourceQuotaAvailable

    @property
    def ResourceQuotaTotal(self):
        r"""资源总数量。
        :rtype: int
        """
        return self._ResourceQuotaTotal

    @ResourceQuotaTotal.setter
    def ResourceQuotaTotal(self, ResourceQuotaTotal):
        self._ResourceQuotaTotal = ResourceQuotaTotal


    def _deserialize(self, params):
        self._ResourceName = params.get("ResourceName")
        self._ResourceQuotaAvailable = params.get("ResourceQuotaAvailable")
        self._ResourceQuotaTotal = params.get("ResourceQuotaTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    r"""CVM镜像信息。

    """

    def __init__(self):
        r"""
        :param _ImageId: CVM镜像 ID ，是Image的唯一标识。
        :type ImageId: str
        :param _ImageName: 镜像名称。
        :type ImageName: str
        :param _ImageDescription: 镜像描述。
        :type ImageDescription: str
        :param _ImageSize: 镜像大小。单位GB。
        :type ImageSize: int
        :param _ImageSource: 镜像来源。
<li>CREATE_IMAGE：自定义镜像</li>
<li>EXTERNAL_IMPORT：外部导入镜像</li>
        :type ImageSource: str
        :param _ImageClass: 镜像分类
<li>SystemImage：系统盘镜像</li>
<li>InstanceImage：整机镜像</li>
        :type ImageClass: str
        :param _ImageState: 镜像状态
CREATING:创建中
NORMAL:正常
CREATEFAILED:创建失败
USING:使用中
SYNCING:同步中
IMPORTING:导入中
IMPORTFAILED:导入失败
        :type ImageState: str
        :param _IsSupportCloudinit: 镜像是否支持Cloudinit。
        :type IsSupportCloudinit: bool
        :param _Architecture: 镜像架构。
        :type Architecture: str
        :param _OsName: 镜像操作系统。
        :type OsName: str
        :param _Platform: 镜像来源平台。
        :type Platform: str
        :param _CreatedTime: 镜像创建时间。
        :type CreatedTime: str
        :param _IsShareable: 镜像是否可共享到轻量应用服务器。
        :type IsShareable: bool
        :param _UnshareableReason: 不可共享的原因。
        :type UnshareableReason: str
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageDescription = None
        self._ImageSize = None
        self._ImageSource = None
        self._ImageClass = None
        self._ImageState = None
        self._IsSupportCloudinit = None
        self._Architecture = None
        self._OsName = None
        self._Platform = None
        self._CreatedTime = None
        self._IsShareable = None
        self._UnshareableReason = None

    @property
    def ImageId(self):
        r"""CVM镜像 ID ，是Image的唯一标识。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        r"""镜像名称。
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        r"""镜像描述。
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ImageSize(self):
        r"""镜像大小。单位GB。
        :rtype: int
        """
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def ImageSource(self):
        r"""镜像来源。
<li>CREATE_IMAGE：自定义镜像</li>
<li>EXTERNAL_IMPORT：外部导入镜像</li>
        :rtype: str
        """
        return self._ImageSource

    @ImageSource.setter
    def ImageSource(self, ImageSource):
        self._ImageSource = ImageSource

    @property
    def ImageClass(self):
        r"""镜像分类
<li>SystemImage：系统盘镜像</li>
<li>InstanceImage：整机镜像</li>
        :rtype: str
        """
        return self._ImageClass

    @ImageClass.setter
    def ImageClass(self, ImageClass):
        self._ImageClass = ImageClass

    @property
    def ImageState(self):
        r"""镜像状态
CREATING:创建中
NORMAL:正常
CREATEFAILED:创建失败
USING:使用中
SYNCING:同步中
IMPORTING:导入中
IMPORTFAILED:导入失败
        :rtype: str
        """
        return self._ImageState

    @ImageState.setter
    def ImageState(self, ImageState):
        self._ImageState = ImageState

    @property
    def IsSupportCloudinit(self):
        r"""镜像是否支持Cloudinit。
        :rtype: bool
        """
        return self._IsSupportCloudinit

    @IsSupportCloudinit.setter
    def IsSupportCloudinit(self, IsSupportCloudinit):
        self._IsSupportCloudinit = IsSupportCloudinit

    @property
    def Architecture(self):
        r"""镜像架构。
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def OsName(self):
        r"""镜像操作系统。
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def Platform(self):
        r"""镜像来源平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def CreatedTime(self):
        r"""镜像创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def IsShareable(self):
        r"""镜像是否可共享到轻量应用服务器。
        :rtype: bool
        """
        return self._IsShareable

    @IsShareable.setter
    def IsShareable(self, IsShareable):
        self._IsShareable = IsShareable

    @property
    def UnshareableReason(self):
        r"""不可共享的原因。
        :rtype: str
        """
        return self._UnshareableReason

    @UnshareableReason.setter
    def UnshareableReason(self, UnshareableReason):
        self._UnshareableReason = UnshareableReason


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        self._ImageSize = params.get("ImageSize")
        self._ImageSource = params.get("ImageSource")
        self._ImageClass = params.get("ImageClass")
        self._ImageState = params.get("ImageState")
        self._IsSupportCloudinit = params.get("IsSupportCloudinit")
        self._Architecture = params.get("Architecture")
        self._OsName = params.get("OsName")
        self._Platform = params.get("Platform")
        self._CreatedTime = params.get("CreatedTime")
        self._IsShareable = params.get("IsShareable")
        self._UnshareableReason = params.get("UnshareableReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairRequest(AbstractModel):
    r"""ImportKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过 25 个字符。
        :type KeyName: str
        :param _PublicKey: 密钥对的公钥内容， OpenSSH RSA 格式。
        :type PublicKey: str
        :param _Tags: 标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :type Tags: list of Tag
        """
        self._KeyName = None
        self._PublicKey = None
        self._Tags = None

    @property
    def KeyName(self):
        r"""密钥对名称，可由数字，字母和下划线组成，长度不超过 25 个字符。
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def PublicKey(self):
        r"""密钥对的公钥内容， OpenSSH RSA 格式。
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Tags(self):
        r"""标签键和标签值。 如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。 如果标签不存在会为您自动创建标签。 数组最多支持10个元素。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._PublicKey = params.get("PublicKey")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairResponse(AbstractModel):
    r"""ImportKeyPair返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥对 ID。
        :type KeyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._RequestId = None

    @property
    def KeyId(self):
        r"""密钥对 ID。
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class InquirePriceCreateBlueprintRequest(AbstractModel):
    r"""InquirePriceCreateBlueprint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintCount: 自定义镜像的个数。默认值为1。
        :type BlueprintCount: int
        """
        self._BlueprintCount = None

    @property
    def BlueprintCount(self):
        r"""自定义镜像的个数。默认值为1。
        :rtype: int
        """
        return self._BlueprintCount

    @BlueprintCount.setter
    def BlueprintCount(self, BlueprintCount):
        self._BlueprintCount = BlueprintCount


    def _deserialize(self, params):
        self._BlueprintCount = params.get("BlueprintCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateBlueprintResponse(AbstractModel):
    r"""InquirePriceCreateBlueprint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintPrice: 自定义镜像的价格参数。
        :type BlueprintPrice: :class:`tencentcloud.lighthouse.v20200324.models.BlueprintPrice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BlueprintPrice = None
        self._RequestId = None

    @property
    def BlueprintPrice(self):
        r"""自定义镜像的价格参数。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.BlueprintPrice`
        """
        return self._BlueprintPrice

    @BlueprintPrice.setter
    def BlueprintPrice(self, BlueprintPrice):
        self._BlueprintPrice = BlueprintPrice

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BlueprintPrice") is not None:
            self._BlueprintPrice = BlueprintPrice()
            self._BlueprintPrice._deserialize(params.get("BlueprintPrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceCreateDisksRequest(AbstractModel):
    r"""InquirePriceCreateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskSize: 云硬盘大小, 单位: GB。
        :type DiskSize: int
        :param _DiskType: 云硬盘介质类型。取值: "CLOUD_PREMIUM"(高性能云盘), "CLOUD_SSD"(SSD云硬盘)。
        :type DiskType: str
        :param _DiskChargePrepaid: 新购云硬盘包年包月相关参数设置。
        :type DiskChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.DiskChargePrepaid`
        :param _DiskCount: 云硬盘个数, 默认值: 1。
        :type DiskCount: int
        :param _DiskBackupQuota: 指定云硬盘备份点配额，不传时默认为不带备份点配额。
取值范围：0 到 500
        :type DiskBackupQuota: int
        """
        self._DiskSize = None
        self._DiskType = None
        self._DiskChargePrepaid = None
        self._DiskCount = None
        self._DiskBackupQuota = None

    @property
    def DiskSize(self):
        r"""云硬盘大小, 单位: GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        r"""云硬盘介质类型。取值: "CLOUD_PREMIUM"(高性能云盘), "CLOUD_SSD"(SSD云硬盘)。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskChargePrepaid(self):
        r"""新购云硬盘包年包月相关参数设置。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DiskChargePrepaid`
        """
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskCount(self):
        r"""云硬盘个数, 默认值: 1。
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskBackupQuota(self):
        r"""指定云硬盘备份点配额，不传时默认为不带备份点配额。
取值范围：0 到 500
        :rtype: int
        """
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskCount = params.get("DiskCount")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDisksResponse(AbstractModel):
    r"""InquirePriceCreateDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskPrice: 云硬盘价格。
        :type DiskPrice: :class:`tencentcloud.lighthouse.v20200324.models.DiskPrice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        r"""云硬盘价格。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DiskPrice`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = DiskPrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceCreateInstancesRequest(AbstractModel):
    r"""InquirePriceCreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BundleId: 实例的套餐 ID。可以通过调用[DescribeBundles](https://cloud.tencent.com/document/api/1207/47575)接口获取。
        :type BundleId: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param _InstanceCount: 创建数量，默认为 1。
        :type InstanceCount: int
        :param _BlueprintId: 应用镜像 ID，使用收费应用镜像时必填。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :type BlueprintId: str
        """
        self._BundleId = None
        self._InstanceChargePrepaid = None
        self._InstanceCount = None
        self._BlueprintId = None

    @property
    def BundleId(self):
        r"""实例的套餐 ID。可以通过调用[DescribeBundles](https://cloud.tencent.com/document/api/1207/47575)接口获取。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def InstanceChargePrepaid(self):
        r"""预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceCount(self):
        r"""创建数量，默认为 1。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def BlueprintId(self):
        r"""应用镜像 ID，使用收费应用镜像时必填。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId


    def _deserialize(self, params):
        self._BundleId = params.get("BundleId")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceCount = params.get("InstanceCount")
        self._BlueprintId = params.get("BlueprintId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateInstancesResponse(AbstractModel):
    r"""InquirePriceCreateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 询价信息。
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        r"""询价信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquirePriceRenewDisksRequest(AbstractModel):
    r"""InquirePriceRenewDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。每次批量请求云硬盘的上限为 1。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :type DiskIds: list of str
        :param _RenewDiskChargePrepaid: 续费云硬盘包年包月相关参数设置。
        :type RenewDiskChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.RenewDiskChargePrepaid`
        """
        self._DiskIds = None
        self._RenewDiskChargePrepaid = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。每次批量请求云硬盘的上限为 1。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def RenewDiskChargePrepaid(self):
        r"""续费云硬盘包年包月相关参数设置。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RenewDiskChargePrepaid`
        """
        return self._RenewDiskChargePrepaid

    @RenewDiskChargePrepaid.setter
    def RenewDiskChargePrepaid(self, RenewDiskChargePrepaid):
        self._RenewDiskChargePrepaid = RenewDiskChargePrepaid


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("RenewDiskChargePrepaid") is not None:
            self._RenewDiskChargePrepaid = RenewDiskChargePrepaid()
            self._RenewDiskChargePrepaid._deserialize(params.get("RenewDiskChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewDisksResponse(AbstractModel):
    r"""InquirePriceRenewDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskPrice: 云硬盘价格。
        :type DiskPrice: :class:`tencentcloud.lighthouse.v20200324.models.DiskPrice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        r"""云硬盘价格。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DiskPrice`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = DiskPrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceRenewInstancesRequest(AbstractModel):
    r"""InquirePriceRenewInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 待续费的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573 )接口返回值中的InstanceId获取。每次请求批量实例的上限为50。
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param _RenewDataDisk: 是否续费数据盘。默认值: false, 即不续费。
        :type RenewDataDisk: bool
        :param _AlignInstanceExpiredTime: 数据盘是否对齐实例到期时间。默认值: false, 即不对齐。
        :type AlignInstanceExpiredTime: bool
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None
        self._RenewDataDisk = None
        self._AlignInstanceExpiredTime = None

    @property
    def InstanceIds(self):
        r"""待续费的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573 )接口返回值中的InstanceId获取。每次请求批量实例的上限为50。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        r"""预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def RenewDataDisk(self):
        r"""是否续费数据盘。默认值: false, 即不续费。
        :rtype: bool
        """
        return self._RenewDataDisk

    @RenewDataDisk.setter
    def RenewDataDisk(self, RenewDataDisk):
        self._RenewDataDisk = RenewDataDisk

    @property
    def AlignInstanceExpiredTime(self):
        r"""数据盘是否对齐实例到期时间。默认值: false, 即不对齐。
        :rtype: bool
        """
        return self._AlignInstanceExpiredTime

    @AlignInstanceExpiredTime.setter
    def AlignInstanceExpiredTime(self, AlignInstanceExpiredTime):
        self._AlignInstanceExpiredTime = AlignInstanceExpiredTime


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._RenewDataDisk = params.get("RenewDataDisk")
        self._AlignInstanceExpiredTime = params.get("AlignInstanceExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewInstancesResponse(AbstractModel):
    r"""InquirePriceRenewInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 询价信息。默认为列表中第一个实例的价格信息。
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param _DataDiskPriceSet: 数据盘价格信息列表。
        :type DataDiskPriceSet: list of DataDiskPrice
        :param _InstancePriceDetailSet: 待续费实例价格列表。
        :type InstancePriceDetailSet: list of InstancePriceDetail
        :param _TotalPrice: 总计价格。
        :type TotalPrice: :class:`tencentcloud.lighthouse.v20200324.models.TotalPrice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._DataDiskPriceSet = None
        self._InstancePriceDetailSet = None
        self._TotalPrice = None
        self._RequestId = None

    @property
    def Price(self):
        r"""询价信息。默认为列表中第一个实例的价格信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def DataDiskPriceSet(self):
        r"""数据盘价格信息列表。
        :rtype: list of DataDiskPrice
        """
        return self._DataDiskPriceSet

    @DataDiskPriceSet.setter
    def DataDiskPriceSet(self, DataDiskPriceSet):
        self._DataDiskPriceSet = DataDiskPriceSet

    @property
    def InstancePriceDetailSet(self):
        r"""待续费实例价格列表。
        :rtype: list of InstancePriceDetail
        """
        return self._InstancePriceDetailSet

    @InstancePriceDetailSet.setter
    def InstancePriceDetailSet(self, InstancePriceDetailSet):
        self._InstancePriceDetailSet = InstancePriceDetailSet

    @property
    def TotalPrice(self):
        r"""总计价格。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.TotalPrice`
        """
        return self._TotalPrice

    @TotalPrice.setter
    def TotalPrice(self, TotalPrice):
        self._TotalPrice = TotalPrice

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        if params.get("DataDiskPriceSet") is not None:
            self._DataDiskPriceSet = []
            for item in params.get("DataDiskPriceSet"):
                obj = DataDiskPrice()
                obj._deserialize(item)
                self._DataDiskPriceSet.append(obj)
        if params.get("InstancePriceDetailSet") is not None:
            self._InstancePriceDetailSet = []
            for item in params.get("InstancePriceDetailSet"):
                obj = InstancePriceDetail()
                obj._deserialize(item)
                self._InstancePriceDetailSet.append(obj)
        if params.get("TotalPrice") is not None:
            self._TotalPrice = TotalPrice()
            self._TotalPrice._deserialize(params.get("TotalPrice"))
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    r"""描述了实例信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _BundleId: 套餐 ID。
        :type BundleId: str
        :param _BlueprintId: 镜像 ID。
        :type BlueprintId: str
        :param _CPU: 实例的 CPU 核数，单位：核。
        :type CPU: int
        :param _Memory: 实例内存容量，单位：GB 。
        :type Memory: int
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _InstanceChargeType: 实例计费模式。取值范围： 
PREPAID：表示预付费，即包年包月。
        :type InstanceChargeType: str
        :param _SystemDisk: 实例系统盘信息。
        :type SystemDisk: :class:`tencentcloud.lighthouse.v20200324.models.SystemDisk`
        :param _PrivateAddresses: 实例主网卡的内网 IP。 
注意：此字段可能返回 空，表示取不到有效值。
        :type PrivateAddresses: list of str
        :param _PublicAddresses: 实例主网卡的公网 IP。 
注意：此字段可能返回 空，表示取不到有效值。
        :type PublicAddresses: list of str
        :param _InternetAccessible: 实例带宽信息。
        :type InternetAccessible: :class:`tencentcloud.lighthouse.v20200324.models.InternetAccessible`
        :param _RenewFlag: 自动续费标识。取值范围： 
NOTIFY_AND_MANUAL_RENEW：表示通知即将过期，但不自动续费  
NOTIFY_AND_AUTO_RENEW：表示通知即将过期，而且自动续费 DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知。
        :type RenewFlag: str
        :param _LoginSettings: 实例登录设置。
        :type LoginSettings: :class:`tencentcloud.lighthouse.v20200324.models.LoginSettings`
        :param _InstanceState: 实例状态。取值范围： 
<li>PENDING：表示创建中</li><li>LAUNCH_FAILED：表示创建失败</li><li>RUNNING：表示运行中</li><li>STOPPED：表示关机</li><li>STARTING：表示开机中</li><li>STOPPING：表示关机中</li><li>REBOOTING：表示重启中</li><li>SHUTDOWN：表示停止待销毁</li><li>TERMINATING：表示销毁中</li><li>DELETING：表示删除中</li><li>FREEZING：表示冻结中</li><li>ENTER_RESCUE_MODE：表示进入救援模式中</li><li>RESCUE_MODE：表示救援模式</li><li>EXIT_RESCUE_MODE：表示退出救援模式中</li>
        :type InstanceState: str
        :param _Uuid: 实例全局唯一 ID。
        :type Uuid: str
        :param _LatestOperation: 实例的最新操作。例：StopInstances、ResetInstance。注意：此字段可能返回 空值，表示取不到有效值。
        :type LatestOperation: str
        :param _LatestOperationState: 实例的最新操作状态。取值范围： 
SUCCESS：表示操作成功 
OPERATING：表示操作执行中 
FAILED：表示操作失败 
注意：此字段可能返回 空值，表示取不到有效值。
        :type LatestOperationState: str
        :param _LatestOperationRequestId: 实例最新操作的唯一请求 ID。 
注意：此字段可能返回 空值，表示取不到有效值。
        :type LatestOperationRequestId: str
        :param _LatestOperationStartedTime: 实例最新操作的开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationStartedTime: str
        :param _IsolatedTime: 隔离时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ExpiredTime: 到期时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ 。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param _PlatformType: 操作系统平台类型，如 LINUX_UNIX、WINDOWS。
        :type PlatformType: str
        :param _Platform: 操作系统平台。
        :type Platform: str
        :param _OsName: 操作系统名称。
        :type OsName: str
        :param _Zone: 可用区。
        :type Zone: str
        :param _Tags: 实例绑定的标签列表。
        :type Tags: list of Tag
        :param _InstanceRestrictState: 实例封禁状态。取值范围：
<li>NORMAL实例正常。</li><li>NETWORK_RESTRICT：网络封禁。</li>
        :type InstanceRestrictState: str
        :param _SupportIpv6Detail: 描述实例是否支持IPv6。
        :type SupportIpv6Detail: :class:`tencentcloud.lighthouse.v20200324.models.SupportIpv6Detail`
        :param _PublicIpv6Addresses: 公网IPv6地址列表。
        :type PublicIpv6Addresses: list of str
        :param _InitInvocationId: 创建实例后自动执行TAT命令的调用ID。
        :type InitInvocationId: str
        :param _InstanceViolationDetail: 实例违规详情。
        :type InstanceViolationDetail: :class:`tencentcloud.lighthouse.v20200324.models.InstanceViolationDetail`
        """
        self._InstanceId = None
        self._BundleId = None
        self._BlueprintId = None
        self._CPU = None
        self._Memory = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._SystemDisk = None
        self._PrivateAddresses = None
        self._PublicAddresses = None
        self._InternetAccessible = None
        self._RenewFlag = None
        self._LoginSettings = None
        self._InstanceState = None
        self._Uuid = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._LatestOperationStartedTime = None
        self._IsolatedTime = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._PlatformType = None
        self._Platform = None
        self._OsName = None
        self._Zone = None
        self._Tags = None
        self._InstanceRestrictState = None
        self._SupportIpv6Detail = None
        self._PublicIpv6Addresses = None
        self._InitInvocationId = None
        self._InstanceViolationDetail = None

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
    def BundleId(self):
        r"""套餐 ID。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BlueprintId(self):
        r"""镜像 ID。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def CPU(self):
        r"""实例的 CPU 核数，单位：核。
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        r"""实例内存容量，单位：GB 。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

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
    def InstanceChargeType(self):
        r"""实例计费模式。取值范围： 
PREPAID：表示预付费，即包年包月。
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SystemDisk(self):
        r"""实例系统盘信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def PrivateAddresses(self):
        r"""实例主网卡的内网 IP。 
注意：此字段可能返回 空，表示取不到有效值。
        :rtype: list of str
        """
        return self._PrivateAddresses

    @PrivateAddresses.setter
    def PrivateAddresses(self, PrivateAddresses):
        self._PrivateAddresses = PrivateAddresses

    @property
    def PublicAddresses(self):
        r"""实例主网卡的公网 IP。 
注意：此字段可能返回 空，表示取不到有效值。
        :rtype: list of str
        """
        return self._PublicAddresses

    @PublicAddresses.setter
    def PublicAddresses(self, PublicAddresses):
        self._PublicAddresses = PublicAddresses

    @property
    def InternetAccessible(self):
        r"""实例带宽信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围： 
NOTIFY_AND_MANUAL_RENEW：表示通知即将过期，但不自动续费  
NOTIFY_AND_AUTO_RENEW：表示通知即将过期，而且自动续费 DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def LoginSettings(self):
        r"""实例登录设置。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def InstanceState(self):
        r"""实例状态。取值范围： 
<li>PENDING：表示创建中</li><li>LAUNCH_FAILED：表示创建失败</li><li>RUNNING：表示运行中</li><li>STOPPED：表示关机</li><li>STARTING：表示开机中</li><li>STOPPING：表示关机中</li><li>REBOOTING：表示重启中</li><li>SHUTDOWN：表示停止待销毁</li><li>TERMINATING：表示销毁中</li><li>DELETING：表示删除中</li><li>FREEZING：表示冻结中</li><li>ENTER_RESCUE_MODE：表示进入救援模式中</li><li>RESCUE_MODE：表示救援模式</li><li>EXIT_RESCUE_MODE：表示退出救援模式中</li>
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Uuid(self):
        r"""实例全局唯一 ID。
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def LatestOperation(self):
        r"""实例的最新操作。例：StopInstances、ResetInstance。注意：此字段可能返回 空值，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        r"""实例的最新操作状态。取值范围： 
SUCCESS：表示操作成功 
OPERATING：表示操作执行中 
FAILED：表示操作失败 
注意：此字段可能返回 空值，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        r"""实例最新操作的唯一请求 ID。 
注意：此字段可能返回 空值，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def LatestOperationStartedTime(self):
        r"""实例最新操作的开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperationStartedTime

    @LatestOperationStartedTime.setter
    def LatestOperationStartedTime(self, LatestOperationStartedTime):
        self._LatestOperationStartedTime = LatestOperationStartedTime

    @property
    def IsolatedTime(self):
        r"""隔离时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def CreatedTime(self):
        r"""创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        r"""到期时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ 。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def PlatformType(self):
        r"""操作系统平台类型，如 LINUX_UNIX、WINDOWS。
        :rtype: str
        """
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def Platform(self):
        r"""操作系统平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def OsName(self):
        r"""操作系统名称。
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def Zone(self):
        r"""可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Tags(self):
        r"""实例绑定的标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceRestrictState(self):
        r"""实例封禁状态。取值范围：
<li>NORMAL实例正常。</li><li>NETWORK_RESTRICT：网络封禁。</li>
        :rtype: str
        """
        return self._InstanceRestrictState

    @InstanceRestrictState.setter
    def InstanceRestrictState(self, InstanceRestrictState):
        self._InstanceRestrictState = InstanceRestrictState

    @property
    def SupportIpv6Detail(self):
        r"""描述实例是否支持IPv6。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.SupportIpv6Detail`
        """
        return self._SupportIpv6Detail

    @SupportIpv6Detail.setter
    def SupportIpv6Detail(self, SupportIpv6Detail):
        self._SupportIpv6Detail = SupportIpv6Detail

    @property
    def PublicIpv6Addresses(self):
        r"""公网IPv6地址列表。
        :rtype: list of str
        """
        return self._PublicIpv6Addresses

    @PublicIpv6Addresses.setter
    def PublicIpv6Addresses(self, PublicIpv6Addresses):
        self._PublicIpv6Addresses = PublicIpv6Addresses

    @property
    def InitInvocationId(self):
        r"""创建实例后自动执行TAT命令的调用ID。
        :rtype: str
        """
        return self._InitInvocationId

    @InitInvocationId.setter
    def InitInvocationId(self, InitInvocationId):
        self._InitInvocationId = InitInvocationId

    @property
    def InstanceViolationDetail(self):
        r"""实例违规详情。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InstanceViolationDetail`
        """
        return self._InstanceViolationDetail

    @InstanceViolationDetail.setter
    def InstanceViolationDetail(self, InstanceViolationDetail):
        self._InstanceViolationDetail = InstanceViolationDetail


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BundleId = params.get("BundleId")
        self._BlueprintId = params.get("BlueprintId")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._PrivateAddresses = params.get("PrivateAddresses")
        self._PublicAddresses = params.get("PublicAddresses")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._RenewFlag = params.get("RenewFlag")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._InstanceState = params.get("InstanceState")
        self._Uuid = params.get("Uuid")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._LatestOperationStartedTime = params.get("LatestOperationStartedTime")
        self._IsolatedTime = params.get("IsolatedTime")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._PlatformType = params.get("PlatformType")
        self._Platform = params.get("Platform")
        self._OsName = params.get("OsName")
        self._Zone = params.get("Zone")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceRestrictState = params.get("InstanceRestrictState")
        if params.get("SupportIpv6Detail") is not None:
            self._SupportIpv6Detail = SupportIpv6Detail()
            self._SupportIpv6Detail._deserialize(params.get("SupportIpv6Detail"))
        self._PublicIpv6Addresses = params.get("PublicIpv6Addresses")
        self._InitInvocationId = params.get("InitInvocationId")
        if params.get("InstanceViolationDetail") is not None:
            self._InstanceViolationDetail = InstanceViolationDetail()
            self._InstanceViolationDetail._deserialize(params.get("InstanceViolationDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    r"""描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。
- 创建实例时，取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
- 续费实例时，取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li><br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费</li><br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知</li><br><br>默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        r"""购买实例的时长，单位：月。
- 创建实例时，取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
- 续费实例时，取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li><br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费</li><br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知</li><br><br>默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDeniedActions(AbstractModel):
    r"""实例操作限制列表。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _DeniedActions: 操作限制列表。
        :type DeniedActions: list of DeniedAction
        """
        self._InstanceId = None
        self._DeniedActions = None

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
    def DeniedActions(self):
        r"""操作限制列表。
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIdentifier(AbstractModel):
    r"""实例标识信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Region: 实例地域。
        :type Region: str
        """
        self._InstanceId = None
        self._Region = None

    @property
    def InstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Region(self):
        r"""实例地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePrice(AbstractModel):
    r"""关于Lighthouse Instance实例的价格信息。

    """

    def __init__(self):
        r"""
        :param _OriginalBundlePrice: 套餐单价原价。
        :type OriginalBundlePrice: float
        :param _OriginalPrice: 原价。
        :type OriginalPrice: float
        :param _Discount: 折扣。
        :type Discount: float
        :param _DiscountPrice: 折后价。
        :type DiscountPrice: float
        :param _Currency: 价格货币单位。取值范围CNY:人民币。USD:美元。
        :type Currency: str
        :param _DetailPrices: 计费项目明细。
        :type DetailPrices: list of DetailPrice
        """
        self._OriginalBundlePrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None
        self._Currency = None
        self._DetailPrices = None

    @property
    def OriginalBundlePrice(self):
        r"""套餐单价原价。
        :rtype: float
        """
        return self._OriginalBundlePrice

    @OriginalBundlePrice.setter
    def OriginalBundlePrice(self, OriginalBundlePrice):
        self._OriginalBundlePrice = OriginalBundlePrice

    @property
    def OriginalPrice(self):
        r"""原价。
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        r"""折扣。
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        r"""折后价。
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Currency(self):
        r"""价格货币单位。取值范围CNY:人民币。USD:美元。
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DetailPrices(self):
        r"""计费项目明细。
        :rtype: list of DetailPrice
        """
        return self._DetailPrices

    @DetailPrices.setter
    def DetailPrices(self, DetailPrices):
        self._DetailPrices = DetailPrices


    def _deserialize(self, params):
        self._OriginalBundlePrice = params.get("OriginalBundlePrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Currency = params.get("Currency")
        if params.get("DetailPrices") is not None:
            self._DetailPrices = []
            for item in params.get("DetailPrices"):
                obj = DetailPrice()
                obj._deserialize(item)
                self._DetailPrices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePriceDetail(AbstractModel):
    r"""实例价格详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstancePrice: 询价信息。
        :type InstancePrice: :class:`tencentcloud.lighthouse.v20200324.models.InstancePrice`
        :param _DiscountDetail: 折扣梯度详情，每个梯度包含的信息有：时长，折扣数，总价，折扣价，折扣详情（用户折扣、官网折扣、最终折扣）。
        :type DiscountDetail: list of DiscountDetail
        """
        self._InstanceId = None
        self._InstancePrice = None
        self._DiscountDetail = None

    @property
    def InstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstancePrice(self):
        r"""询价信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InstancePrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def DiscountDetail(self):
        r"""折扣梯度详情，每个梯度包含的信息有：时长，折扣数，总价，折扣价，折扣详情（用户折扣、官网折扣、最终折扣）。
        :rtype: list of DiscountDetail
        """
        return self._DiscountDetail

    @DiscountDetail.setter
    def DiscountDetail(self, DiscountDetail):
        self._DiscountDetail = DiscountDetail


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("InstancePrice") is not None:
            self._InstancePrice = InstancePrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("DiscountDetail") is not None:
            self._DiscountDetail = []
            for item in params.get("DiscountDetail"):
                obj = DiscountDetail()
                obj._deserialize(item)
                self._DiscountDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceReturnable(AbstractModel):
    r"""实例可退还信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _IsReturnable: 实例是否可退还。
        :type IsReturnable: bool
        :param _ReturnFailCode: 实例退还失败错误码。取值:
0: 可以退还
1: 资源已退货。
2: 资源已到期
3: 资源购买超过5天不支持退款
4: 非预付费资源不支持退款
8: 退货数量超出限额
9: 涉及活动订单不支持退款
10: 资源不支持自助退，请走工单退款
11: 涉及推广奖励渠道订单，请提工单咨询
12: 根据业务侧产品规定，该资源不允许退款
        :type ReturnFailCode: int
        :param _ReturnFailMessage: 实例退还失败错误信息。
        :type ReturnFailMessage: str
        """
        self._InstanceId = None
        self._IsReturnable = None
        self._ReturnFailCode = None
        self._ReturnFailMessage = None

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
    def IsReturnable(self):
        r"""实例是否可退还。
        :rtype: bool
        """
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def ReturnFailCode(self):
        r"""实例退还失败错误码。取值:
0: 可以退还
1: 资源已退货。
2: 资源已到期
3: 资源购买超过5天不支持退款
4: 非预付费资源不支持退款
8: 退货数量超出限额
9: 涉及活动订单不支持退款
10: 资源不支持自助退，请走工单退款
11: 涉及推广奖励渠道订单，请提工单咨询
12: 根据业务侧产品规定，该资源不允许退款
        :rtype: int
        """
        return self._ReturnFailCode

    @ReturnFailCode.setter
    def ReturnFailCode(self, ReturnFailCode):
        self._ReturnFailCode = ReturnFailCode

    @property
    def ReturnFailMessage(self):
        r"""实例退还失败错误信息。
        :rtype: str
        """
        return self._ReturnFailMessage

    @ReturnFailMessage.setter
    def ReturnFailMessage(self, ReturnFailMessage):
        self._ReturnFailMessage = ReturnFailMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IsReturnable = params.get("IsReturnable")
        self._ReturnFailCode = params.get("ReturnFailCode")
        self._ReturnFailMessage = params.get("ReturnFailMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTrafficPackage(AbstractModel):
    r"""实例流量包详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _TrafficPackageSet: 流量包详情列表。
        :type TrafficPackageSet: list of TrafficPackage
        """
        self._InstanceId = None
        self._TrafficPackageSet = None

    @property
    def InstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TrafficPackageSet(self):
        r"""流量包详情列表。
        :rtype: list of TrafficPackage
        """
        return self._TrafficPackageSet

    @TrafficPackageSet.setter
    def TrafficPackageSet(self, TrafficPackageSet):
        self._TrafficPackageSet = TrafficPackageSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("TrafficPackageSet") is not None:
            self._TrafficPackageSet = []
            for item in params.get("TrafficPackageSet"):
                obj = TrafficPackage()
                obj._deserialize(item)
                self._TrafficPackageSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceViolationDetail(AbstractModel):
    r"""实例违规详情。

    """

    def __init__(self):
        r"""
        :param _Source:  来源：RESTRICT：封禁、FREEZW：冻结
        :type Source: str
        :param _State: 是否允许自助解封：1是，2否
        :type State: str
        :param _Reason: 违规类型
        :type Reason: str
        :param _Content: 违规内容（URL、关联域名）
        :type Content: str
        """
        self._Source = None
        self._State = None
        self._Reason = None
        self._Content = None

    @property
    def Source(self):
        r""" 来源：RESTRICT：封禁、FREEZW：冻结
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def State(self):
        r"""是否允许自助解封：1是，2否
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Reason(self):
        r"""违规类型
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Content(self):
        r"""违规内容（URL、关联域名）
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._State = params.get("State")
        self._Reason = params.get("Reason")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    r"""描述了启动配置创建实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等。

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费类型，取值范围：
<li>按流量包付费：TRAFFIC_POSTPAID_BY_HOUR</li>
<li>按带宽付费： BANDWIDTH_POSTPAID_BY_HOUR</li>
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: 是否分配公网 IP。
        :type PublicIpAssigned: bool
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None

    @property
    def InternetChargeType(self):
        r"""网络计费类型，取值范围：
<li>按流量包付费：TRAFFIC_POSTPAID_BY_HOUR</li>
<li>按带宽付费： BANDWIDTH_POSTPAID_BY_HOUR</li>
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        r"""公网出带宽上限，单位：Mbps。
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        r"""是否分配公网 IP。
        :rtype: bool
        """
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDisksRequest(AbstractModel):
    r"""IsolateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。一个或多个待操作的云硬盘ID。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。每次请求退还数据盘数量总计上限为20。
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。一个或多个待操作的云硬盘ID。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。每次请求退还数据盘数量总计上限为20。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDisksResponse(AbstractModel):
    r"""IsolateDisks返回参数结构体

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


class IsolateInstancesRequest(AbstractModel):
    r"""IsolateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表。一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。每次请求退还实例和数据盘数量总计上限为20。
        :type InstanceIds: list of str
        :param _IsolateDataDisk: 是否退还挂载的数据盘。取值范围：
TRUE：表示退还实例同时退还其挂载的数据盘。
FALSE：表示退还实例同时不再退还其挂载的数据盘。
默认取值：TRUE。
        :type IsolateDataDisk: bool
        """
        self._InstanceIds = None
        self._IsolateDataDisk = None

    @property
    def InstanceIds(self):
        r"""实例ID列表。一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。每次请求退还实例和数据盘数量总计上限为20。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def IsolateDataDisk(self):
        r"""是否退还挂载的数据盘。取值范围：
TRUE：表示退还实例同时退还其挂载的数据盘。
FALSE：表示退还实例同时不再退还其挂载的数据盘。
默认取值：TRUE。
        :rtype: bool
        """
        return self._IsolateDataDisk

    @IsolateDataDisk.setter
    def IsolateDataDisk(self, IsolateDataDisk):
        self._IsolateDataDisk = IsolateDataDisk


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._IsolateDataDisk = params.get("IsolateDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstancesResponse(AbstractModel):
    r"""IsolateInstances返回参数结构体

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


class KeyPair(AbstractModel):
    r"""描述密钥对信息。

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥对 ID ，是密钥对的唯一标识。
        :type KeyId: str
        :param _KeyName: 密钥对名称。
        :type KeyName: str
        :param _PublicKey: 密钥对的纯文本公钥。
        :type PublicKey: str
        :param _AssociatedInstanceIds: 密钥对关联的实例 ID 列表。
        :type AssociatedInstanceIds: list of str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _PrivateKey: 密钥对私钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        :param _Tags: 密钥对绑定的标签列表。
        :type Tags: list of Tag
        """
        self._KeyId = None
        self._KeyName = None
        self._PublicKey = None
        self._AssociatedInstanceIds = None
        self._CreatedTime = None
        self._PrivateKey = None
        self._Tags = None

    @property
    def KeyId(self):
        r"""密钥对 ID ，是密钥对的唯一标识。
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyName(self):
        r"""密钥对名称。
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def PublicKey(self):
        r"""密钥对的纯文本公钥。
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def AssociatedInstanceIds(self):
        r"""密钥对关联的实例 ID 列表。
        :rtype: list of str
        """
        return self._AssociatedInstanceIds

    @AssociatedInstanceIds.setter
    def AssociatedInstanceIds(self, AssociatedInstanceIds):
        self._AssociatedInstanceIds = AssociatedInstanceIds

    @property
    def CreatedTime(self):
        r"""创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def PrivateKey(self):
        r"""密钥对私钥。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def Tags(self):
        r"""密钥对绑定的标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyName = params.get("KeyName")
        self._PublicKey = params.get("PublicKey")
        self._AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self._CreatedTime = params.get("CreatedTime")
        self._PrivateKey = params.get("PrivateKey")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginConfiguration(AbstractModel):
    r"""实例密码登录配置信息。

    """

    def __init__(self):
        r"""
        :param _AutoGeneratePassword: <li>"YES"代表选择自动生成密码，这时不指定Password字段。</li>
<li>"NO"代表选择自定义密码，这时要指定Password字段。</li>
        :type AutoGeneratePassword: str
        :param _Password: 实例登录密码。具体按照操作系统的复杂度要求。 

`LINUX_UNIX` 实例密码必须 8-30 位，推荐使用 12 位以上密码，不能包含空格，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：<br>
<li>小写字母：[a-z]</li>
<li>大写字母：[A-Z]</li>
<li>数字：0-9</li>
<li>特殊字符： ()\`\~!@#$%^&\*-+=\_|{}[]:;' <>,.?/</li> 

`WINDOWS` 实例密码必须 12-30 位，不能包含空格，不能以“/”开头且不包括用户名，至少包含以下字符中的三种不同字符：<br>
<li>小写字母：[a-z]</li>
<li>大写字母：[A-Z]</li>
<li>数字：0-9</li>
<li>特殊字符：()\`~!@#$%^&\*-+=\_|{}[]:;' <>,.?/</li> 
        :type Password: str
        :param _KeyIds: 密钥ID列表，最多同时指定5个密钥。关联密钥后，就可以通过对应的私钥来访问实例。密钥与密码不能同时指定，同时WINDOWS操作系统不支持指定密钥。密钥ID列表可以通过[DescribeKeyPairs](https://cloud.tencent.com/document/product/1207/55540)接口获取。
        :type KeyIds: list of str
        """
        self._AutoGeneratePassword = None
        self._Password = None
        self._KeyIds = None

    @property
    def AutoGeneratePassword(self):
        r"""<li>"YES"代表选择自动生成密码，这时不指定Password字段。</li>
<li>"NO"代表选择自定义密码，这时要指定Password字段。</li>
        :rtype: str
        """
        return self._AutoGeneratePassword

    @AutoGeneratePassword.setter
    def AutoGeneratePassword(self, AutoGeneratePassword):
        self._AutoGeneratePassword = AutoGeneratePassword

    @property
    def Password(self):
        r"""实例登录密码。具体按照操作系统的复杂度要求。 

`LINUX_UNIX` 实例密码必须 8-30 位，推荐使用 12 位以上密码，不能包含空格，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：<br>
<li>小写字母：[a-z]</li>
<li>大写字母：[A-Z]</li>
<li>数字：0-9</li>
<li>特殊字符： ()\`\~!@#$%^&\*-+=\_|{}[]:;' <>,.?/</li> 

`WINDOWS` 实例密码必须 12-30 位，不能包含空格，不能以“/”开头且不包括用户名，至少包含以下字符中的三种不同字符：<br>
<li>小写字母：[a-z]</li>
<li>大写字母：[A-Z]</li>
<li>数字：0-9</li>
<li>特殊字符：()\`~!@#$%^&\*-+=\_|{}[]:;' <>,.?/</li> 
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        r"""密钥ID列表，最多同时指定5个密钥。关联密钥后，就可以通过对应的私钥来访问实例。密钥与密码不能同时指定，同时WINDOWS操作系统不支持指定密钥。密钥ID列表可以通过[DescribeKeyPairs](https://cloud.tencent.com/document/product/1207/55540)接口获取。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._AutoGeneratePassword = params.get("AutoGeneratePassword")
        self._Password = params.get("Password")
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    r"""描述了实例登录相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _KeyIds: 密钥 ID 列表。关联密钥后，就可以通过对应的私钥来访问实例。注意：此字段可能返回 []，表示取不到有效值。
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        r"""密钥 ID 列表。关联密钥后，就可以通过对应的私钥来访问实例。注意：此字段可能返回 []，表示取不到有效值。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpServer(AbstractModel):
    r"""MCP Server信息

    """

    def __init__(self):
        r"""
        :param _McpServerId: MCP Server ID
        :type McpServerId: str
        :param _Name: MCP Server名称。最大长度：64
        :type Name: str
        :param _McpServerType: MCP Server类型。枚举值如下：

<li>PUBLIC_PACKAGE：公共包安装</li>
<li>AGENT_GENERATED：AI生成</li>
        :type McpServerType: str
        :param _IconUrl: MCP Server图标地址
        :type IconUrl: str
        :param _Command: Base64编码后的MCP Server启动命令。最大长度：2048
        :type Command: str
        :param _State: MCP Server状态。枚举值如下：

<li>PENDING：表示创建中</li>
<li>LAUNCH_FAILED：表示创建失败</li>
<li>RUNNING：表示运行中</li>
<li>STOPPED：表示关闭</li>
<li>STARTING：表示开启中</li>
<li>STOPPING：表示关闭中</li>
<li>RESTARTING：表示重启中</li>
<li>REMOVING：表示删除中</li>
<li>UNKNOWN：表示未知</li>
<li>ENV_ERROR：表示环境错误</li>
        :type State: str
        :param _ServerUrl: MCP Server访问地址。传输类型 TransportType 为 STREAMABLE_HTTP 时以 /mcp结尾，为 SSE 时以 /sse结尾。
        :type ServerUrl: str
        :param _Config: MCP Server配置
        :type Config: str
        :param _Description: MCP Server备注
        :type Description: str
        :param _CreatedTime: MCP Server创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :type CreatedTime: str
        :param _UpdatedTime: MCP Server修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :type UpdatedTime: str
        :param _EnvSet: MCP Server环境变量
        :type EnvSet: list of McpServerEnv
        :param _TransportType: 传输类型。枚举值如下：

<li>STREAMABLE_HTTP：HTTP协议的流式传输方式</li>
<li>SSE：Server-Sent Events，服务器发送事件</li>
        :type TransportType: str
        """
        self._McpServerId = None
        self._Name = None
        self._McpServerType = None
        self._IconUrl = None
        self._Command = None
        self._State = None
        self._ServerUrl = None
        self._Config = None
        self._Description = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._EnvSet = None
        self._TransportType = None

    @property
    def McpServerId(self):
        r"""MCP Server ID
        :rtype: str
        """
        return self._McpServerId

    @McpServerId.setter
    def McpServerId(self, McpServerId):
        self._McpServerId = McpServerId

    @property
    def Name(self):
        r"""MCP Server名称。最大长度：64
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def McpServerType(self):
        r"""MCP Server类型。枚举值如下：

<li>PUBLIC_PACKAGE：公共包安装</li>
<li>AGENT_GENERATED：AI生成</li>
        :rtype: str
        """
        return self._McpServerType

    @McpServerType.setter
    def McpServerType(self, McpServerType):
        self._McpServerType = McpServerType

    @property
    def IconUrl(self):
        r"""MCP Server图标地址
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Command(self):
        r"""Base64编码后的MCP Server启动命令。最大长度：2048
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def State(self):
        r"""MCP Server状态。枚举值如下：

<li>PENDING：表示创建中</li>
<li>LAUNCH_FAILED：表示创建失败</li>
<li>RUNNING：表示运行中</li>
<li>STOPPED：表示关闭</li>
<li>STARTING：表示开启中</li>
<li>STOPPING：表示关闭中</li>
<li>RESTARTING：表示重启中</li>
<li>REMOVING：表示删除中</li>
<li>UNKNOWN：表示未知</li>
<li>ENV_ERROR：表示环境错误</li>
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ServerUrl(self):
        r"""MCP Server访问地址。传输类型 TransportType 为 STREAMABLE_HTTP 时以 /mcp结尾，为 SSE 时以 /sse结尾。
        :rtype: str
        """
        return self._ServerUrl

    @ServerUrl.setter
    def ServerUrl(self, ServerUrl):
        self._ServerUrl = ServerUrl

    @property
    def Config(self):
        r"""MCP Server配置
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Description(self):
        r"""MCP Server备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedTime(self):
        r"""MCP Server创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""MCP Server修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def EnvSet(self):
        r"""MCP Server环境变量
        :rtype: list of McpServerEnv
        """
        return self._EnvSet

    @EnvSet.setter
    def EnvSet(self, EnvSet):
        self._EnvSet = EnvSet

    @property
    def TransportType(self):
        r"""传输类型。枚举值如下：

<li>STREAMABLE_HTTP：HTTP协议的流式传输方式</li>
<li>SSE：Server-Sent Events，服务器发送事件</li>
        :rtype: str
        """
        return self._TransportType

    @TransportType.setter
    def TransportType(self, TransportType):
        self._TransportType = TransportType


    def _deserialize(self, params):
        self._McpServerId = params.get("McpServerId")
        self._Name = params.get("Name")
        self._McpServerType = params.get("McpServerType")
        self._IconUrl = params.get("IconUrl")
        self._Command = params.get("Command")
        self._State = params.get("State")
        self._ServerUrl = params.get("ServerUrl")
        self._Config = params.get("Config")
        self._Description = params.get("Description")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        if params.get("EnvSet") is not None:
            self._EnvSet = []
            for item in params.get("EnvSet"):
                obj = McpServerEnv()
                obj._deserialize(item)
                self._EnvSet.append(obj)
        self._TransportType = params.get("TransportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpServerEnv(AbstractModel):
    r"""MCP Server环境变量

    """

    def __init__(self):
        r"""
        :param _Key: MCP Server的环境变量键。最大长度：128
        :type Key: str
        :param _Value: MCP Server的环境变量值。最大长度：1024。该字段可能存储密钥，出参时将固定返回“**********”，避免明文泄露。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""MCP Server的环境变量键。最大长度：128
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""MCP Server的环境变量值。最大长度：1024。该字段可能存储密钥，出参时将固定返回“**********”，避免明文泄露。
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
        


class McpServerTemplate(AbstractModel):
    r"""MCP Server模板

    """

    def __init__(self):
        r"""
        :param _Name: MCP Server名称
        :type Name: str
        :param _Command: Base64编码之后的MCP Server启动命令。
        :type Command: str
        :param _Description: 描述
        :type Description: str
        :param _IconUrl: MCP Server图标地址
        :type IconUrl: str
        :param _CommunityUrl: MCP Server社区地址
        :type CommunityUrl: str
        :param _PlatformUrl: MCP Server关联的开发平台地址或开放平台地址
        :type PlatformUrl: str
        :param _EnvSet: MCP Server环境变量
        :type EnvSet: list of McpServerTemplateEnv
        """
        self._Name = None
        self._Command = None
        self._Description = None
        self._IconUrl = None
        self._CommunityUrl = None
        self._PlatformUrl = None
        self._EnvSet = None

    @property
    def Name(self):
        r"""MCP Server名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Command(self):
        r"""Base64编码之后的MCP Server启动命令。
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IconUrl(self):
        r"""MCP Server图标地址
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def CommunityUrl(self):
        r"""MCP Server社区地址
        :rtype: str
        """
        return self._CommunityUrl

    @CommunityUrl.setter
    def CommunityUrl(self, CommunityUrl):
        self._CommunityUrl = CommunityUrl

    @property
    def PlatformUrl(self):
        r"""MCP Server关联的开发平台地址或开放平台地址
        :rtype: str
        """
        return self._PlatformUrl

    @PlatformUrl.setter
    def PlatformUrl(self, PlatformUrl):
        self._PlatformUrl = PlatformUrl

    @property
    def EnvSet(self):
        r"""MCP Server环境变量
        :rtype: list of McpServerTemplateEnv
        """
        return self._EnvSet

    @EnvSet.setter
    def EnvSet(self, EnvSet):
        self._EnvSet = EnvSet


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Command = params.get("Command")
        self._Description = params.get("Description")
        self._IconUrl = params.get("IconUrl")
        self._CommunityUrl = params.get("CommunityUrl")
        self._PlatformUrl = params.get("PlatformUrl")
        if params.get("EnvSet") is not None:
            self._EnvSet = []
            for item in params.get("EnvSet"):
                obj = McpServerTemplateEnv()
                obj._deserialize(item)
                self._EnvSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpServerTemplateEnv(AbstractModel):
    r"""MCP Server模板环境变量

    """

    def __init__(self):
        r"""
        :param _Key: MCP Server模板的环境变量键
        :type Key: str
        :param _Value: MCP Server模板的环境变量值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""MCP Server模板的环境变量键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""MCP Server模板的环境变量值
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
        


class ModifyBlueprintAttributeRequest(AbstractModel):
    r"""ModifyBlueprintAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintId: 镜像 ID。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :type BlueprintId: str
        :param _BlueprintName: 设置新的镜像名称。最大长度60。
        :type BlueprintName: str
        :param _Description: 设置新的镜像描述。最大长度60。
        :type Description: str
        """
        self._BlueprintId = None
        self._BlueprintName = None
        self._Description = None

    @property
    def BlueprintId(self):
        r"""镜像 ID。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def BlueprintName(self):
        r"""设置新的镜像名称。最大长度60。
        :rtype: str
        """
        return self._BlueprintName

    @BlueprintName.setter
    def BlueprintName(self, BlueprintName):
        self._BlueprintName = BlueprintName

    @property
    def Description(self):
        r"""设置新的镜像描述。最大长度60。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._BlueprintName = params.get("BlueprintName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlueprintAttributeResponse(AbstractModel):
    r"""ModifyBlueprintAttribute返回参数结构体

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


class ModifyBundle(AbstractModel):
    r"""描述了实例可变更的套餐。

    """

    def __init__(self):
        r"""
        :param _ModifyPrice: 更改实例套餐后需要补的差价。
        :type ModifyPrice: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param _ModifyBundleState: 变更套餐状态。取值：
<li>SOLD_OUT：套餐售罄</li>
<li>AVAILABLE：支持套餐变更</li>
<li>UNAVAILABLE：暂不支持套餐变更</li>
        :type ModifyBundleState: str
        :param _Bundle: 套餐信息。
        :type Bundle: :class:`tencentcloud.lighthouse.v20200324.models.Bundle`
        :param _NotSupportModifyMessage: 不支持套餐变更原因信息。变更套餐状态为"AVAILABLE"时, 该信息为空
        :type NotSupportModifyMessage: str
        """
        self._ModifyPrice = None
        self._ModifyBundleState = None
        self._Bundle = None
        self._NotSupportModifyMessage = None

    @property
    def ModifyPrice(self):
        r"""更改实例套餐后需要补的差价。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        """
        return self._ModifyPrice

    @ModifyPrice.setter
    def ModifyPrice(self, ModifyPrice):
        self._ModifyPrice = ModifyPrice

    @property
    def ModifyBundleState(self):
        r"""变更套餐状态。取值：
<li>SOLD_OUT：套餐售罄</li>
<li>AVAILABLE：支持套餐变更</li>
<li>UNAVAILABLE：暂不支持套餐变更</li>
        :rtype: str
        """
        return self._ModifyBundleState

    @ModifyBundleState.setter
    def ModifyBundleState(self, ModifyBundleState):
        self._ModifyBundleState = ModifyBundleState

    @property
    def Bundle(self):
        r"""套餐信息。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.Bundle`
        """
        return self._Bundle

    @Bundle.setter
    def Bundle(self, Bundle):
        self._Bundle = Bundle

    @property
    def NotSupportModifyMessage(self):
        r"""不支持套餐变更原因信息。变更套餐状态为"AVAILABLE"时, 该信息为空
        :rtype: str
        """
        return self._NotSupportModifyMessage

    @NotSupportModifyMessage.setter
    def NotSupportModifyMessage(self, NotSupportModifyMessage):
        self._NotSupportModifyMessage = NotSupportModifyMessage


    def _deserialize(self, params):
        if params.get("ModifyPrice") is not None:
            self._ModifyPrice = Price()
            self._ModifyPrice._deserialize(params.get("ModifyPrice"))
        self._ModifyBundleState = params.get("ModifyBundleState")
        if params.get("Bundle") is not None:
            self._Bundle = Bundle()
            self._Bundle._deserialize(params.get("Bundle"))
        self._NotSupportModifyMessage = params.get("NotSupportModifyMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskBackupsAttributeRequest(AbstractModel):
    r"""ModifyDiskBackupsAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: 云硬盘备份点ID，可通过 [DescribeDiskBackups](https://cloud.tencent.com/document/api/1207/84379) 接口返回值中的 DiskBackupId 获取。列表长度最大值为100。
        :type DiskBackupIds: list of str
        :param _DiskBackupName: 云硬盘备份点名称，最大长度 90 。
        :type DiskBackupName: str
        """
        self._DiskBackupIds = None
        self._DiskBackupName = None

    @property
    def DiskBackupIds(self):
        r"""云硬盘备份点ID，可通过 [DescribeDiskBackups](https://cloud.tencent.com/document/api/1207/84379) 接口返回值中的 DiskBackupId 获取。列表长度最大值为100。
        :rtype: list of str
        """
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds

    @property
    def DiskBackupName(self):
        r"""云硬盘备份点名称，最大长度 90 。
        :rtype: str
        """
        return self._DiskBackupName

    @DiskBackupName.setter
    def DiskBackupName(self, DiskBackupName):
        self._DiskBackupName = DiskBackupName


    def _deserialize(self, params):
        self._DiskBackupIds = params.get("DiskBackupIds")
        self._DiskBackupName = params.get("DiskBackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskBackupsAttributeResponse(AbstractModel):
    r"""ModifyDiskBackupsAttribute返回参数结构体

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


class ModifyDisksAttributeRequest(AbstractModel):
    r"""ModifyDisksAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :type DiskIds: list of str
        :param _DiskName: 云硬盘名称。
        :type DiskName: str
        """
        self._DiskIds = None
        self._DiskName = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskName(self):
        r"""云硬盘名称。
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DiskName = params.get("DiskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksAttributeResponse(AbstractModel):
    r"""ModifyDisksAttribute返回参数结构体

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


class ModifyDisksBackupQuotaRequest(AbstractModel):
    r"""ModifyDisksBackupQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表，可通过[DescribeDisks](https://cloud.tencent.com/document/api/1207/66093)接口查询。列表最大长度为15。
        :type DiskIds: list of str
        :param _DiskBackupQuota: 云硬盘备份点配额。取值范围: [0, 500]。调整后的配额必须大于等于已存在的备份点数量。
        :type DiskBackupQuota: int
        """
        self._DiskIds = None
        self._DiskBackupQuota = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表，可通过[DescribeDisks](https://cloud.tencent.com/document/api/1207/66093)接口查询。列表最大长度为15。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskBackupQuota(self):
        r"""云硬盘备份点配额。取值范围: [0, 500]。调整后的配额必须大于等于已存在的备份点数量。
        :rtype: int
        """
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksBackupQuotaResponse(AbstractModel):
    r"""ModifyDisksBackupQuota返回参数结构体

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


class ModifyDisksRenewFlagRequest(AbstractModel):
    r"""ModifyDisksRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :type DiskIds: list of str
        :param _RenewFlag: 自动续费标识。取值范围：

- NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
- NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
- DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._DiskIds = None
        self._RenewFlag = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。每次批量请求云硬盘的上限为 100。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围：

- NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
- NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
- DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksRenewFlagResponse(AbstractModel):
    r"""ModifyDisksRenewFlag返回参数结构体

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


class ModifyDockerContainerRequest(AbstractModel):
    r"""ModifyDockerContainer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerId: 容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerId: str
        :param _Envs: 环境变量列表
        :type Envs: list of ContainerEnv
        :param _PublishPorts: 容器端口主机端口映射列表
        :type PublishPorts: list of DockerContainerPublishPort
        :param _Volumes: 容器加载本地卷列表
        :type Volumes: list of DockerContainerVolume
        :param _Command: 运行的命令
        :type Command: str
        :param _RestartPolicy: 容器重启策略，对应docker "--restart"参数。

枚举值:
no: 不自动重启。默认策略。
on-failure[:max-retries]: 当容器退出码非0时重启容器。使用max-retries限制重启次数，比如on-failure:10，限制最多重启10次。
always: 只要容器退出就重启。
unless-stopped: 始终重新启动容器，包括在守护进程启动时，除非容器在 Docker 守护进程停止之前进入停止状态。
        :type RestartPolicy: str
        """
        self._InstanceId = None
        self._ContainerId = None
        self._Envs = None
        self._PublishPorts = None
        self._Volumes = None
        self._Command = None
        self._RestartPolicy = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerId(self):
        r"""容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: str
        """
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId

    @property
    def Envs(self):
        r"""环境变量列表
        :rtype: list of ContainerEnv
        """
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def PublishPorts(self):
        r"""容器端口主机端口映射列表
        :rtype: list of DockerContainerPublishPort
        """
        return self._PublishPorts

    @PublishPorts.setter
    def PublishPorts(self, PublishPorts):
        self._PublishPorts = PublishPorts

    @property
    def Volumes(self):
        r"""容器加载本地卷列表
        :rtype: list of DockerContainerVolume
        """
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def Command(self):
        r"""运行的命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def RestartPolicy(self):
        r"""容器重启策略，对应docker "--restart"参数。

枚举值:
no: 不自动重启。默认策略。
on-failure[:max-retries]: 当容器退出码非0时重启容器。使用max-retries限制重启次数，比如on-failure:10，限制最多重启10次。
always: 只要容器退出就重启。
unless-stopped: 始终重新启动容器，包括在守护进程启动时，除非容器在 Docker 守护进程停止之前进入停止状态。
        :rtype: str
        """
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerId = params.get("ContainerId")
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = ContainerEnv()
                obj._deserialize(item)
                self._Envs.append(obj)
        if params.get("PublishPorts") is not None:
            self._PublishPorts = []
            for item in params.get("PublishPorts"):
                obj = DockerContainerPublishPort()
                obj._deserialize(item)
                self._PublishPorts.append(obj)
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = DockerContainerVolume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        self._Command = params.get("Command")
        self._RestartPolicy = params.get("RestartPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDockerContainerResponse(AbstractModel):
    r"""ModifyDockerContainer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DockerActivityId: Docker活动ID。
        :type DockerActivityId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DockerActivityId = None
        self._RequestId = None

    @property
    def DockerActivityId(self):
        r"""Docker活动ID。
        :rtype: str
        """
        return self._DockerActivityId

    @DockerActivityId.setter
    def DockerActivityId(self, DockerActivityId):
        self._DockerActivityId = DockerActivityId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DockerActivityId = params.get("DockerActivityId")
        self._RequestId = params.get("RequestId")


class ModifyFirewallRuleDescriptionRequest(AbstractModel):
    r"""ModifyFirewallRuleDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _FirewallRule: 防火墙规则。
        :type FirewallRule: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRule`
        :param _FirewallVersion: 防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :type FirewallVersion: int
        """
        self._InstanceId = None
        self._FirewallRule = None
        self._FirewallVersion = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/1207/47573) 接口返回值中的 InstanceId 获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FirewallRule(self):
        r"""防火墙规则。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRule`
        """
        return self._FirewallRule

    @FirewallRule.setter
    def FirewallRule(self, FirewallRule):
        self._FirewallRule = FirewallRule

    @property
    def FirewallVersion(self):
        r"""防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :rtype: int
        """
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FirewallRule") is not None:
            self._FirewallRule = FirewallRule()
            self._FirewallRule._deserialize(params.get("FirewallRule"))
        self._FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFirewallRuleDescriptionResponse(AbstractModel):
    r"""ModifyFirewallRuleDescription返回参数结构体

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


class ModifyFirewallRulesRequest(AbstractModel):
    r"""ModifyFirewallRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。实例的ID可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _FirewallRules: 防火墙规则列表。列表长度最大值是100。
        :type FirewallRules: list of FirewallRule
        :param _FirewallVersion: 防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :type FirewallVersion: int
        """
        self._InstanceId = None
        self._FirewallRules = None
        self._FirewallVersion = None

    @property
    def InstanceId(self):
        r"""实例 ID。实例的ID可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FirewallRules(self):
        r"""防火墙规则列表。列表长度最大值是100。
        :rtype: list of FirewallRule
        """
        return self._FirewallRules

    @FirewallRules.setter
    def FirewallRules(self, FirewallRules):
        self._FirewallRules = FirewallRules

    @property
    def FirewallVersion(self):
        r"""防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :rtype: int
        """
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self._FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._FirewallRules.append(obj)
        self._FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFirewallRulesResponse(AbstractModel):
    r"""ModifyFirewallRules返回参数结构体

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


class ModifyFirewallTemplateRequest(AbstractModel):
    r"""ModifyFirewallTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :type TemplateId: str
        :param _TemplateName: 防火墙模板名称。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :type TemplateName: str
        """
        self._TemplateId = None
        self._TemplateName = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""防火墙模板名称。可通过[DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874)接口返回值字段TemplateSet获取。
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFirewallTemplateResponse(AbstractModel):
    r"""ModifyFirewallTemplate返回参数结构体

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


class ModifyImageSharePermissionRequest(AbstractModel):
    r"""ModifyImageSharePermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像 ID。可通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回值中的ImageId获取。
        :type ImageId: str
        :param _Permission: 共享属性，包括 SHARE，CANCEL。其中SHARE代表共享，CANCEL代表取消共享。
        :type Permission: str
        """
        self._ImageId = None
        self._Permission = None

    @property
    def ImageId(self):
        r"""镜像 ID。可通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回值中的ImageId获取。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Permission(self):
        r"""共享属性，包括 SHARE，CANCEL。其中SHARE代表共享，CANCEL代表取消共享。
        :rtype: str
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._Permission = params.get("Permission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSharePermissionResponse(AbstractModel):
    r"""ModifyImageSharePermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintId: CVM自定义镜像共享到轻量应用服务器后的镜像ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type BlueprintId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BlueprintId = None
        self._RequestId = None

    @property
    def BlueprintId(self):
        r"""CVM自定义镜像共享到轻量应用服务器后的镜像ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._RequestId = params.get("RequestId")


class ModifyInstancesAttributeRequest(AbstractModel):
    r"""ModifyInstancesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param _InstanceName: 实例名称。可任意命名，但不得超过 60 个字符。
        :type InstanceName: str
        """
        self._InstanceIds = None
        self._InstanceName = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceName(self):
        r"""实例名称。可任意命名，但不得超过 60 个字符。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    r"""ModifyInstancesAttribute返回参数结构体

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


class ModifyInstancesBundleRequest(AbstractModel):
    r"""ModifyInstancesBundle请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表。一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。每次请求批量实例的上限为15。
        :type InstanceIds: list of str
        :param _BundleId: 待变更的套餐Id。注意不可和当前要升配的实例套餐ID相同。可通过[DescribeBundles](https://cloud.tencent.com/document/api/1207/47575)接口返回值中的BundleId获取。
        :type BundleId: str
        :param _AutoVoucher: 是否自动抵扣代金券。取值范围：
true：表示自动抵扣代金券
false：表示不自动抵扣代金券
默认取值：false。
        :type AutoVoucher: bool
        """
        self._InstanceIds = None
        self._BundleId = None
        self._AutoVoucher = None

    @property
    def InstanceIds(self):
        r"""实例ID列表。一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。每次请求批量实例的上限为15。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def BundleId(self):
        r"""待变更的套餐Id。注意不可和当前要升配的实例套餐ID相同。可通过[DescribeBundles](https://cloud.tencent.com/document/api/1207/47575)接口返回值中的BundleId获取。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def AutoVoucher(self):
        r"""是否自动抵扣代金券。取值范围：
true：表示自动抵扣代金券
false：表示不自动抵扣代金券
默认取值：false。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._BundleId = params.get("BundleId")
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesBundleResponse(AbstractModel):
    r"""ModifyInstancesBundle返回参数结构体

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


class ModifyInstancesRenewFlagRequest(AbstractModel):
    r"""ModifyInstancesRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param _RenewFlag: 自动续费标识。取值范围：

- NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
- NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
- DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._InstanceIds = None
        self._RenewFlag = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围：

- NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
- NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
- DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesRenewFlagResponse(AbstractModel):
    r"""ModifyInstancesRenewFlag返回参数结构体

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


class ModifyMcpServerRequest(AbstractModel):
    r"""ModifyMcpServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可以通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _McpServerId: MCP Server ID。可以通[DescribeMcpServers](https://cloud.tencent.com/document/product/1207/122837)接口返回值中的McpServerId获取。
        :type McpServerId: str
        :param _Name: MCP Server名称。最大长度：64
        :type Name: str
        :param _Command: Base64编码后的MCP Server启动命令。最大长度：2048
        :type Command: str
        :param _Description: MCP Server备注。最大长度：2048
        :type Description: str
        :param _Envs: MCP Server环境变量。最大长度：10。用于完整替换MCP Server的环境变量。当该字段为空时，系统将清除当前所有环境变量。若无需修改环境变量，请勿传递该字段。
        :type Envs: list of McpServerEnv
        :param _TransportType: 传输类型。枚举值如下：

<li>STREAMABLE_HTTP：HTTP协议的流式传输方式</li>
<li>SSE：Server-Sent Events，服务器发送事件</li>
        :type TransportType: str
        """
        self._InstanceId = None
        self._McpServerId = None
        self._Name = None
        self._Command = None
        self._Description = None
        self._Envs = None
        self._TransportType = None

    @property
    def InstanceId(self):
        r"""实例ID。可以通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def McpServerId(self):
        r"""MCP Server ID。可以通[DescribeMcpServers](https://cloud.tencent.com/document/product/1207/122837)接口返回值中的McpServerId获取。
        :rtype: str
        """
        return self._McpServerId

    @McpServerId.setter
    def McpServerId(self, McpServerId):
        self._McpServerId = McpServerId

    @property
    def Name(self):
        r"""MCP Server名称。最大长度：64
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Command(self):
        r"""Base64编码后的MCP Server启动命令。最大长度：2048
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Description(self):
        r"""MCP Server备注。最大长度：2048
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Envs(self):
        r"""MCP Server环境变量。最大长度：10。用于完整替换MCP Server的环境变量。当该字段为空时，系统将清除当前所有环境变量。若无需修改环境变量，请勿传递该字段。
        :rtype: list of McpServerEnv
        """
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def TransportType(self):
        r"""传输类型。枚举值如下：

<li>STREAMABLE_HTTP：HTTP协议的流式传输方式</li>
<li>SSE：Server-Sent Events，服务器发送事件</li>
        :rtype: str
        """
        return self._TransportType

    @TransportType.setter
    def TransportType(self, TransportType):
        self._TransportType = TransportType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._McpServerId = params.get("McpServerId")
        self._Name = params.get("Name")
        self._Command = params.get("Command")
        self._Description = params.get("Description")
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = McpServerEnv()
                obj._deserialize(item)
                self._Envs.append(obj)
        self._TransportType = params.get("TransportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMcpServerResponse(AbstractModel):
    r"""ModifyMcpServer返回参数结构体

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


class ModifySnapshotAttributeRequest(AbstractModel):
    r"""ModifySnapshotAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照 ID, 可通过 <a href="https://cloud.tencent.com/document/product/1207/54388">DescribeSnapshots</a> 查询。
        :type SnapshotId: str
        :param _SnapshotName: 新的快照名称，最长为 60 个字符。
        :type SnapshotName: str
        """
        self._SnapshotId = None
        self._SnapshotName = None

    @property
    def SnapshotId(self):
        r"""快照 ID, 可通过 <a href="https://cloud.tencent.com/document/product/1207/54388">DescribeSnapshots</a> 查询。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotName(self):
        r"""新的快照名称，最长为 60 个字符。
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotAttributeResponse(AbstractModel):
    r"""ModifySnapshotAttribute返回参数结构体

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


class PolicyDetail(AbstractModel):
    r"""折扣详情信息。

    """

    def __init__(self):
        r"""
        :param _UserDiscount: 用户折扣。
        :type UserDiscount: float
        :param _CommonDiscount: 公共折扣。
        :type CommonDiscount: float
        :param _FinalDiscount: 最终折扣。
        :type FinalDiscount: float
        :param _ActivityDiscount: 活动折扣。取值为null，表示无有效值，即没有折扣。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityDiscount: float
        :param _DiscountType: 折扣类型。
user：用户折扣; common：官网折扣; activity：活动折扣。 取值为null，表示无有效值，即没有折扣。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountType: str
        """
        self._UserDiscount = None
        self._CommonDiscount = None
        self._FinalDiscount = None
        self._ActivityDiscount = None
        self._DiscountType = None

    @property
    def UserDiscount(self):
        r"""用户折扣。
        :rtype: float
        """
        return self._UserDiscount

    @UserDiscount.setter
    def UserDiscount(self, UserDiscount):
        self._UserDiscount = UserDiscount

    @property
    def CommonDiscount(self):
        r"""公共折扣。
        :rtype: float
        """
        return self._CommonDiscount

    @CommonDiscount.setter
    def CommonDiscount(self, CommonDiscount):
        self._CommonDiscount = CommonDiscount

    @property
    def FinalDiscount(self):
        r"""最终折扣。
        :rtype: float
        """
        return self._FinalDiscount

    @FinalDiscount.setter
    def FinalDiscount(self, FinalDiscount):
        self._FinalDiscount = FinalDiscount

    @property
    def ActivityDiscount(self):
        r"""活动折扣。取值为null，表示无有效值，即没有折扣。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._ActivityDiscount

    @ActivityDiscount.setter
    def ActivityDiscount(self, ActivityDiscount):
        self._ActivityDiscount = ActivityDiscount

    @property
    def DiscountType(self):
        r"""折扣类型。
user：用户折扣; common：官网折扣; activity：活动折扣。 取值为null，表示无有效值，即没有折扣。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiscountType

    @DiscountType.setter
    def DiscountType(self, DiscountType):
        self._DiscountType = DiscountType


    def _deserialize(self, params):
        self._UserDiscount = params.get("UserDiscount")
        self._CommonDiscount = params.get("CommonDiscount")
        self._FinalDiscount = params.get("FinalDiscount")
        self._ActivityDiscount = params.get("ActivityDiscount")
        self._DiscountType = params.get("DiscountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    r"""价格信息

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 实例价格。
        :type InstancePrice: :class:`tencentcloud.lighthouse.v20200324.models.InstancePrice`
        """
        self._InstancePrice = None

    @property
    def InstancePrice(self):
        r"""实例价格。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InstancePrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = InstancePrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesRequest(AbstractModel):
    r"""RebootInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param _StopType: 关机类型。
取值范围：
- SOFT：表示软关机 
- HARD：表示硬关机 
- SOFT_FIRST：表示优先软关机，失败再执行硬关机  

默认取值：SOFT_FIRST。
        :type StopType: str
        """
        self._InstanceIds = None
        self._StopType = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def StopType(self):
        r"""关机类型。
取值范围：
- SOFT：表示软关机 
- HARD：表示硬关机 
- SOFT_FIRST：表示优先软关机，失败再执行硬关机  

默认取值：SOFT_FIRST。
        :rtype: str
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    r"""RebootInstances返回参数结构体

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
    r"""描述地域信息。

    """

    def __init__(self):
        r"""
        :param _Region: 地域名称，例如，ap-guangzhou。
        :type Region: str
        :param _RegionName: 地域描述，例如，华南地区(广州)。
        :type RegionName: str
        :param _RegionState: 地域是否可用状态，取值仅为AVAILABLE（表示可用状态）。
        :type RegionState: str
        :param _IsChinaMainland: 是否中国大陆地域
        :type IsChinaMainland: bool
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None
        self._IsChinaMainland = None

    @property
    def Region(self):
        r"""地域名称，例如，ap-guangzhou。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        r"""地域描述，例如，华南地区(广州)。
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        r"""地域是否可用状态，取值仅为AVAILABLE（表示可用状态）。
        :rtype: str
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def IsChinaMainland(self):
        r"""是否中国大陆地域
        :rtype: bool
        """
        return self._IsChinaMainland

    @IsChinaMainland.setter
    def IsChinaMainland(self, IsChinaMainland):
        self._IsChinaMainland = IsChinaMainland


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        self._IsChinaMainland = params.get("IsChinaMainland")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDockerContainersRequest(AbstractModel):
    r"""RemoveDockerContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerIds: 容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerIds: list of str
        """
        self._InstanceId = None
        self._ContainerIds = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerIds(self):
        r"""容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: list of str
        """
        return self._ContainerIds

    @ContainerIds.setter
    def ContainerIds(self, ContainerIds):
        self._ContainerIds = ContainerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerIds = params.get("ContainerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDockerContainersResponse(AbstractModel):
    r"""RemoveDockerContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DockerActivityId: Docker活动ID。
        :type DockerActivityId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DockerActivityId = None
        self._RequestId = None

    @property
    def DockerActivityId(self):
        r"""Docker活动ID。
        :rtype: str
        """
        return self._DockerActivityId

    @DockerActivityId.setter
    def DockerActivityId(self, DockerActivityId):
        self._DockerActivityId = DockerActivityId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DockerActivityId = params.get("DockerActivityId")
        self._RequestId = params.get("RequestId")


class RemoveMcpServersRequest(AbstractModel):
    r"""RemoveMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可以通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _McpServerIds: MCP Server ID列表。可通过DescribeMcpServers接口返回值中的McpServerId获取。最大长度：10
        :type McpServerIds: list of str
        """
        self._InstanceId = None
        self._McpServerIds = None

    @property
    def InstanceId(self):
        r"""实例ID。可以通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def McpServerIds(self):
        r"""MCP Server ID列表。可通过DescribeMcpServers接口返回值中的McpServerId获取。最大长度：10
        :rtype: list of str
        """
        return self._McpServerIds

    @McpServerIds.setter
    def McpServerIds(self, McpServerIds):
        self._McpServerIds = McpServerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._McpServerIds = params.get("McpServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveMcpServersResponse(AbstractModel):
    r"""RemoveMcpServers返回参数结构体

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


class RenameDockerContainerRequest(AbstractModel):
    r"""RenameDockerContainer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerId: 容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerId: str
        :param _ContainerName: 容器新的名称。
        :type ContainerName: str
        """
        self._InstanceId = None
        self._ContainerId = None
        self._ContainerName = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerId(self):
        r"""容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: str
        """
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId

    @property
    def ContainerName(self):
        r"""容器新的名称。
        :rtype: str
        """
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerId = params.get("ContainerId")
        self._ContainerName = params.get("ContainerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameDockerContainerResponse(AbstractModel):
    r"""RenameDockerContainer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DockerActivityId: Docker活动ID。
        :type DockerActivityId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DockerActivityId = None
        self._RequestId = None

    @property
    def DockerActivityId(self):
        r"""Docker活动ID。
        :rtype: str
        """
        return self._DockerActivityId

    @DockerActivityId.setter
    def DockerActivityId(self, DockerActivityId):
        self._DockerActivityId = DockerActivityId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DockerActivityId = params.get("DockerActivityId")
        self._RequestId = params.get("RequestId")


class RenewDiskChargePrepaid(AbstractModel):
    r"""续费云硬盘包年包月相关参数设置。

    """

    def __init__(self):
        r"""
        :param _Period: 续费周期。
单位：月。
取值范围: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36]
        :type Period: int
        :param _RenewFlag: 自动续费标识。
取值范围：
<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知</li>
默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，云硬盘到期后将按月自动续费。
        :type RenewFlag: str
        :param _TimeUnit: 周期单位。取值范围：“m”(月)。默认值: "m"。
        :type TimeUnit: str
        :param _CurInstanceDeadline: 当前实例到期时间。如“2018-01-01 00:00:00”。
指定该参数即可对齐云硬盘所挂载的实例到期时间。
该参数与Period必须指定其一，且不支持同时指定。
该参数值必须大于入参中云硬盘的过期时间。
        :type CurInstanceDeadline: str
        """
        self._Period = None
        self._RenewFlag = None
        self._TimeUnit = None
        self._CurInstanceDeadline = None

    @property
    def Period(self):
        r"""续费周期。
单位：月。
取值范围: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36]
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""自动续费标识。
取值范围：
<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不自动续费，且不通知</li>
默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，云硬盘到期后将按月自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeUnit(self):
        r"""周期单位。取值范围：“m”(月)。默认值: "m"。
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def CurInstanceDeadline(self):
        r"""当前实例到期时间。如“2018-01-01 00:00:00”。
指定该参数即可对齐云硬盘所挂载的实例到期时间。
该参数与Period必须指定其一，且不支持同时指定。
该参数值必须大于入参中云硬盘的过期时间。
        :rtype: str
        """
        return self._CurInstanceDeadline

    @CurInstanceDeadline.setter
    def CurInstanceDeadline(self, CurInstanceDeadline):
        self._CurInstanceDeadline = CurInstanceDeadline


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeUnit = params.get("TimeUnit")
        self._CurInstanceDeadline = params.get("CurInstanceDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDisksRequest(AbstractModel):
    r"""RenewDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。一个或多个待操作的云硬盘ID。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。每次请求续费数据盘数量总计上限为50。
        :type DiskIds: list of str
        :param _RenewDiskChargePrepaid: 续费云硬盘包年包月相关参数设置。
        :type RenewDiskChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.RenewDiskChargePrepaid`
        :param _AutoVoucher: 是否自动使用代金券。默认不使用。
        :type AutoVoucher: bool
        """
        self._DiskIds = None
        self._RenewDiskChargePrepaid = None
        self._AutoVoucher = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。一个或多个待操作的云硬盘ID。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。每次请求续费数据盘数量总计上限为50。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def RenewDiskChargePrepaid(self):
        r"""续费云硬盘包年包月相关参数设置。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RenewDiskChargePrepaid`
        """
        return self._RenewDiskChargePrepaid

    @RenewDiskChargePrepaid.setter
    def RenewDiskChargePrepaid(self, RenewDiskChargePrepaid):
        self._RenewDiskChargePrepaid = RenewDiskChargePrepaid

    @property
    def AutoVoucher(self):
        r"""是否自动使用代金券。默认不使用。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("RenewDiskChargePrepaid") is not None:
            self._RenewDiskChargePrepaid = RenewDiskChargePrepaid()
            self._RenewDiskChargePrepaid._deserialize(params.get("RenewDiskChargePrepaid"))
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDisksResponse(AbstractModel):
    r"""RenewDisks返回参数结构体

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


class RenewInstancesRequest(AbstractModel):
    r"""RenewInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表。一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param _RenewDataDisk: 是否续费弹性数据盘。取值范围：
TRUE：表示续费实例同时续费其挂载的数据盘
FALSE：表示续费实例同时不再续费其挂载的数据盘
默认取值：TRUE。
        :type RenewDataDisk: bool
        :param _AutoVoucher: 是否自动抵扣代金券。取值范围：
TRUE：表示自动抵扣代金券
FALSE：表示不自动抵扣代金券
默认取值：FALSE。
        :type AutoVoucher: bool
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None
        self._RenewDataDisk = None
        self._AutoVoucher = None

    @property
    def InstanceIds(self):
        r"""实例ID列表。一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。每次请求批量实例的上限为100。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        r"""预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def RenewDataDisk(self):
        r"""是否续费弹性数据盘。取值范围：
TRUE：表示续费实例同时续费其挂载的数据盘
FALSE：表示续费实例同时不再续费其挂载的数据盘
默认取值：TRUE。
        :rtype: bool
        """
        return self._RenewDataDisk

    @RenewDataDisk.setter
    def RenewDataDisk(self, RenewDataDisk):
        self._RenewDataDisk = RenewDataDisk

    @property
    def AutoVoucher(self):
        r"""是否自动抵扣代金券。取值范围：
TRUE：表示自动抵扣代金券
FALSE：表示不自动抵扣代金券
默认取值：FALSE。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._RenewDataDisk = params.get("RenewDataDisk")
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstancesResponse(AbstractModel):
    r"""RenewInstances返回参数结构体

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


class ReplaceFirewallTemplateRuleRequest(AbstractModel):
    r"""ReplaceFirewallTemplateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过 [DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874) 接口返回值中的 TemplateId 获取。
        :type TemplateId: str
        :param _TemplateRuleId: 防火墙模板规则ID。可通过 [DescribeFirewallTemplateRules](https://cloud.tencent.com/document/product/1207/96875) 接口返回值中的 TemplateRuleId 获取。
        :type TemplateRuleId: str
        :param _TemplateRule: 替换后的防火墙模板规则。
        :type TemplateRule: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRule`
        """
        self._TemplateId = None
        self._TemplateRuleId = None
        self._TemplateRule = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过 [DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874) 接口返回值中的 TemplateId 获取。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateRuleId(self):
        r"""防火墙模板规则ID。可通过 [DescribeFirewallTemplateRules](https://cloud.tencent.com/document/product/1207/96875) 接口返回值中的 TemplateRuleId 获取。
        :rtype: str
        """
        return self._TemplateRuleId

    @TemplateRuleId.setter
    def TemplateRuleId(self, TemplateRuleId):
        self._TemplateRuleId = TemplateRuleId

    @property
    def TemplateRule(self):
        r"""替换后的防火墙模板规则。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRule`
        """
        return self._TemplateRule

    @TemplateRule.setter
    def TemplateRule(self, TemplateRule):
        self._TemplateRule = TemplateRule


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateRuleId = params.get("TemplateRuleId")
        if params.get("TemplateRule") is not None:
            self._TemplateRule = FirewallRule()
            self._TemplateRule._deserialize(params.get("TemplateRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceFirewallTemplateRuleResponse(AbstractModel):
    r"""ReplaceFirewallTemplateRule返回参数结构体

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


class RerunDockerContainerRequest(AbstractModel):
    r"""RerunDockerContainer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerConfiguration: 重新创建的容器配置。
        :type ContainerConfiguration: :class:`tencentcloud.lighthouse.v20200324.models.DockerContainerConfiguration`
        :param _ContainerId: 容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerId: str
        """
        self._InstanceId = None
        self._ContainerConfiguration = None
        self._ContainerId = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerConfiguration(self):
        r"""重新创建的容器配置。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DockerContainerConfiguration`
        """
        return self._ContainerConfiguration

    @ContainerConfiguration.setter
    def ContainerConfiguration(self, ContainerConfiguration):
        self._ContainerConfiguration = ContainerConfiguration

    @property
    def ContainerId(self):
        r"""容器ID。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: str
        """
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ContainerConfiguration") is not None:
            self._ContainerConfiguration = DockerContainerConfiguration()
            self._ContainerConfiguration._deserialize(params.get("ContainerConfiguration"))
        self._ContainerId = params.get("ContainerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerunDockerContainerResponse(AbstractModel):
    r"""RerunDockerContainer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DockerActivityId: Docker活动ID。
        :type DockerActivityId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DockerActivityId = None
        self._RequestId = None

    @property
    def DockerActivityId(self):
        r"""Docker活动ID。
        :rtype: str
        """
        return self._DockerActivityId

    @DockerActivityId.setter
    def DockerActivityId(self, DockerActivityId):
        self._DockerActivityId = DockerActivityId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DockerActivityId = params.get("DockerActivityId")
        self._RequestId = params.get("RequestId")


class ResetAttachCcnRequest(AbstractModel):
    r"""ResetAttachCcn请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CcnId: 云联网实例ID。可通过[DescribeCcns](https://cloud.tencent.com/document/product/215/19199)接口返回值中的CcnId获取。
        :type CcnId: str
        """
        self._CcnId = None

    @property
    def CcnId(self):
        r"""云联网实例ID。可通过[DescribeCcns](https://cloud.tencent.com/document/product/215/19199)接口返回值中的CcnId获取。
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAttachCcnResponse(AbstractModel):
    r"""ResetAttachCcn返回参数结构体

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


class ResetFirewallTemplateRulesRequest(AbstractModel):
    r"""ResetFirewallTemplateRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 防火墙模板ID。可通过 [DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874) 接口返回值中的 TemplateId	获取。
        :type TemplateId: str
        :param _TemplateRules: 重置后的防火墙模板规则列表。每次请求批量防火墙规则的上限为 100。
        :type TemplateRules: list of FirewallRule
        """
        self._TemplateId = None
        self._TemplateRules = None

    @property
    def TemplateId(self):
        r"""防火墙模板ID。可通过 [DescribeFirewallTemplates](https://cloud.tencent.com/document/product/1207/96874) 接口返回值中的 TemplateId	获取。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateRules(self):
        r"""重置后的防火墙模板规则列表。每次请求批量防火墙规则的上限为 100。
        :rtype: list of FirewallRule
        """
        return self._TemplateRules

    @TemplateRules.setter
    def TemplateRules(self, TemplateRules):
        self._TemplateRules = TemplateRules


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("TemplateRules") is not None:
            self._TemplateRules = []
            for item in params.get("TemplateRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._TemplateRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetFirewallTemplateRulesResponse(AbstractModel):
    r"""ResetFirewallTemplateRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateRuleIdSet: 重置后的规则ID列表。
        :type TemplateRuleIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateRuleIdSet = None
        self._RequestId = None

    @property
    def TemplateRuleIdSet(self):
        r"""重置后的规则ID列表。
        :rtype: list of str
        """
        return self._TemplateRuleIdSet

    @TemplateRuleIdSet.setter
    def TemplateRuleIdSet(self, TemplateRuleIdSet):
        self._TemplateRuleIdSet = TemplateRuleIdSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateRuleIdSet = params.get("TemplateRuleIdSet")
        self._RequestId = params.get("RequestId")


class ResetInstanceBlueprint(AbstractModel):
    r"""描述了镜像重置信息

    """

    def __init__(self):
        r"""
        :param _BlueprintInfo: 镜像详细信息
        :type BlueprintInfo: :class:`tencentcloud.lighthouse.v20200324.models.Blueprint`
        :param _IsResettable: 实例镜像是否可重置为目标镜像。
取值：
true（允许）
false（不允许）
        :type IsResettable: bool
        :param _NonResettableMessage: 不可重置信息.当镜像可重置时为""
        :type NonResettableMessage: str
        """
        self._BlueprintInfo = None
        self._IsResettable = None
        self._NonResettableMessage = None

    @property
    def BlueprintInfo(self):
        r"""镜像详细信息
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.Blueprint`
        """
        return self._BlueprintInfo

    @BlueprintInfo.setter
    def BlueprintInfo(self, BlueprintInfo):
        self._BlueprintInfo = BlueprintInfo

    @property
    def IsResettable(self):
        r"""实例镜像是否可重置为目标镜像。
取值：
true（允许）
false（不允许）
        :rtype: bool
        """
        return self._IsResettable

    @IsResettable.setter
    def IsResettable(self, IsResettable):
        self._IsResettable = IsResettable

    @property
    def NonResettableMessage(self):
        r"""不可重置信息.当镜像可重置时为""
        :rtype: str
        """
        return self._NonResettableMessage

    @NonResettableMessage.setter
    def NonResettableMessage(self, NonResettableMessage):
        self._NonResettableMessage = NonResettableMessage


    def _deserialize(self, params):
        if params.get("BlueprintInfo") is not None:
            self._BlueprintInfo = Blueprint()
            self._BlueprintInfo._deserialize(params.get("BlueprintInfo"))
        self._IsResettable = params.get("IsResettable")
        self._NonResettableMessage = params.get("NonResettableMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceRequest(AbstractModel):
    r"""ResetInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _BlueprintId: 镜像 ID。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :type BlueprintId: str
        :param _Containers: 要创建的容器配置列表。
注意：仅重装的镜像类型为Docker时支持传入该参数。
        :type Containers: list of DockerContainerConfiguration
        :param _LoginConfiguration: 实例登录信息配置。默认缺失情况下代表用户选择实例创建后设置登录密码或绑定密钥。
        :type LoginConfiguration: :class:`tencentcloud.lighthouse.v20200324.models.LoginConfiguration`
        """
        self._InstanceId = None
        self._BlueprintId = None
        self._Containers = None
        self._LoginConfiguration = None

    @property
    def InstanceId(self):
        r"""实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BlueprintId(self):
        r"""镜像 ID。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def Containers(self):
        r"""要创建的容器配置列表。
注意：仅重装的镜像类型为Docker时支持传入该参数。
        :rtype: list of DockerContainerConfiguration
        """
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def LoginConfiguration(self):
        r"""实例登录信息配置。默认缺失情况下代表用户选择实例创建后设置登录密码或绑定密钥。
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.LoginConfiguration`
        """
        return self._LoginConfiguration

    @LoginConfiguration.setter
    def LoginConfiguration(self, LoginConfiguration):
        self._LoginConfiguration = LoginConfiguration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BlueprintId = params.get("BlueprintId")
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = DockerContainerConfiguration()
                obj._deserialize(item)
                self._Containers.append(obj)
        if params.get("LoginConfiguration") is not None:
            self._LoginConfiguration = LoginConfiguration()
            self._LoginConfiguration._deserialize(params.get("LoginConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceResponse(AbstractModel):
    r"""ResetInstance返回参数结构体

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


class ResetInstancesPasswordRequest(AbstractModel):
    r"""ResetInstancesPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
        :type InstanceIds: list of str
        :param _Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：</br> `LINUX_UNIX` 实例密码必须 8-30 位，推荐使用 12 位以上密码，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：</br> <li>小写字母：[a-z]</br></li> <li>大写字母：[A-Z]</br></li> <li>数字：0-9</br></li> <li>特殊字符： ()\`\~!@#$%^&\*-+=\_|{}[]:;' <>,.?/</li></br> `WINDOWS` 实例密码必须 12-30 位，不能以“/”开头且不包括用户名，至少包含以下字符中的三种不同字符</br> <li>小写字母：[a-z]</br></li> <li>大写字母：[A-Z]</br></li> <li>数字： 0-9</br></li> <li>特殊字符：()\`~!@#$%^&\*-+=\_|{}[]:;' <>,.?/</br></li> <li>如果实例即包含 `LINUX_UNIX` 实例又包含 `WINDOWS` 实例，则密码复杂度限制按照 `WINDOWS` 实例的限制。</li>
        :type Password: str
        :param _UserName: 待重置密码的实例操作系统用户名。不得超过 64 个字符。
        :type UserName: str
        """
        self._InstanceIds = None
        self._Password = None
        self._UserName = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过 <a href="https://cloud.tencent.com/document/product/1207/47573">DescribeInstances</a> 接口返回值中的 InstanceId 获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Password(self):
        r"""实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：</br> `LINUX_UNIX` 实例密码必须 8-30 位，推荐使用 12 位以上密码，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：</br> <li>小写字母：[a-z]</br></li> <li>大写字母：[A-Z]</br></li> <li>数字：0-9</br></li> <li>特殊字符： ()\`\~!@#$%^&\*-+=\_|{}[]:;' <>,.?/</li></br> `WINDOWS` 实例密码必须 12-30 位，不能以“/”开头且不包括用户名，至少包含以下字符中的三种不同字符</br> <li>小写字母：[a-z]</br></li> <li>大写字母：[A-Z]</br></li> <li>数字： 0-9</br></li> <li>特殊字符：()\`~!@#$%^&\*-+=\_|{}[]:;' <>,.?/</br></li> <li>如果实例即包含 `LINUX_UNIX` 实例又包含 `WINDOWS` 实例，则密码复杂度限制按照 `WINDOWS` 实例的限制。</li>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def UserName(self):
        r"""待重置密码的实例操作系统用户名。不得超过 64 个字符。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Password = params.get("Password")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    r"""ResetInstancesPassword返回参数结构体

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


class ResizeDisksRequest(AbstractModel):
    r"""ResizeDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表，可通过[DescribeDisks](https://cloud.tencent.com/document/api/1207/66093)接口查询。列表最大长度为15。
        :type DiskIds: list of str
        :param _DiskSize: 扩容后的云硬盘大小。单位: GB。高性能云硬盘大小取值范围：[10, 4000] ,SSD云硬盘大小取值范围：[20, 4000]。扩容后的云硬盘大小必须大于当前云硬盘大小。
        :type DiskSize: int
        """
        self._DiskIds = None
        self._DiskSize = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表，可通过[DescribeDisks](https://cloud.tencent.com/document/api/1207/66093)接口查询。列表最大长度为15。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskSize(self):
        r"""扩容后的云硬盘大小。单位: GB。高性能云硬盘大小取值范围：[10, 4000] ,SSD云硬盘大小取值范围：[20, 4000]。扩容后的云硬盘大小必须大于当前云硬盘大小。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDisksResponse(AbstractModel):
    r"""ResizeDisks返回参数结构体

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


class RestartDockerContainersRequest(AbstractModel):
    r"""RestartDockerContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerIds: 容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerIds: list of str
        """
        self._InstanceId = None
        self._ContainerIds = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerIds(self):
        r"""容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: list of str
        """
        return self._ContainerIds

    @ContainerIds.setter
    def ContainerIds(self, ContainerIds):
        self._ContainerIds = ContainerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerIds = params.get("ContainerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDockerContainersResponse(AbstractModel):
    r"""RestartDockerContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DockerActivityId: Docker活动ID。
        :type DockerActivityId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DockerActivityId = None
        self._RequestId = None

    @property
    def DockerActivityId(self):
        r"""Docker活动ID。
        :rtype: str
        """
        return self._DockerActivityId

    @DockerActivityId.setter
    def DockerActivityId(self, DockerActivityId):
        self._DockerActivityId = DockerActivityId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DockerActivityId = params.get("DockerActivityId")
        self._RequestId = params.get("RequestId")


class RestartMcpServersRequest(AbstractModel):
    r"""RestartMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _McpServerIds: MCP Server ID列表。可通过DescribeMcpServers接口返回值中的McpServerId获取。最大长度：10
        :type McpServerIds: list of str
        """
        self._InstanceId = None
        self._McpServerIds = None

    @property
    def InstanceId(self):
        r"""实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def McpServerIds(self):
        r"""MCP Server ID列表。可通过DescribeMcpServers接口返回值中的McpServerId获取。最大长度：10
        :rtype: list of str
        """
        return self._McpServerIds

    @McpServerIds.setter
    def McpServerIds(self, McpServerIds):
        self._McpServerIds = McpServerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._McpServerIds = params.get("McpServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartMcpServersResponse(AbstractModel):
    r"""RestartMcpServers返回参数结构体

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


class RunDockerContainersRequest(AbstractModel):
    r"""RunDockerContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _Containers: 要创建的容器列表。
        :type Containers: list of DockerContainerConfiguration
        """
        self._InstanceId = None
        self._Containers = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Containers(self):
        r"""要创建的容器列表。
        :rtype: list of DockerContainerConfiguration
        """
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = DockerContainerConfiguration()
                obj._deserialize(item)
                self._Containers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunDockerContainersResponse(AbstractModel):
    r"""RunDockerContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DockerActivitySet: Docker活动ID列表。
        :type DockerActivitySet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DockerActivitySet = None
        self._RequestId = None

    @property
    def DockerActivitySet(self):
        r"""Docker活动ID列表。
        :rtype: list of str
        """
        return self._DockerActivitySet

    @DockerActivitySet.setter
    def DockerActivitySet(self, DockerActivitySet):
        self._DockerActivitySet = DockerActivitySet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DockerActivitySet = params.get("DockerActivitySet")
        self._RequestId = params.get("RequestId")


class Scene(AbstractModel):
    r"""使用场景信息

    """

    def __init__(self):
        r"""
        :param _SceneId: 使用场景Id
        :type SceneId: str
        :param _DisplayName: 使用场景展示名称
        :type DisplayName: str
        :param _Description: 使用场景描述
        :type Description: str
        """
        self._SceneId = None
        self._DisplayName = None
        self._Description = None

    @property
    def SceneId(self):
        r"""使用场景Id
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def DisplayName(self):
        r"""使用场景展示名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        r"""使用场景描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneInfo(AbstractModel):
    r"""使用场景详细信息

    """

    def __init__(self):
        r"""
        :param _SceneId: 使用场景Id。
        :type SceneId: str
        :param _DisplayName: 使用场景展示名称。
        :type DisplayName: str
        :param _Description: 使用场景描述信息。
        :type Description: str
        """
        self._SceneId = None
        self._DisplayName = None
        self._Description = None

    @property
    def SceneId(self):
        r"""使用场景Id。
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def DisplayName(self):
        r"""使用场景展示名称。
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        r"""使用场景描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareBlueprintAcrossAccountsRequest(AbstractModel):
    r"""ShareBlueprintAcrossAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintId: 镜像ID, 可以通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回的BlueprintId获取。
        :type BlueprintId: str
        :param _AccountIds: 接收共享镜像的[账号ID](https://cloud.tencent.com/document/product/213/4944#.E8.8E.B7.E5.8F.96.E4.B8.BB.E8.B4.A6.E5.8F.B7.E7.9A.84.E8.B4.A6.E5.8F.B7-id)列表。账号ID不同于QQ号，查询用户账号ID请查看账号信息中的账号ID栏。账号个数取值最大为10。
        :type AccountIds: list of str
        """
        self._BlueprintId = None
        self._AccountIds = None

    @property
    def BlueprintId(self):
        r"""镜像ID, 可以通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回的BlueprintId获取。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def AccountIds(self):
        r"""接收共享镜像的[账号ID](https://cloud.tencent.com/document/product/213/4944#.E8.8E.B7.E5.8F.96.E4.B8.BB.E8.B4.A6.E5.8F.B7.E7.9A.84.E8.B4.A6.E5.8F.B7-id)列表。账号ID不同于QQ号，查询用户账号ID请查看账号信息中的账号ID栏。账号个数取值最大为10。
        :rtype: list of str
        """
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._AccountIds = params.get("AccountIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareBlueprintAcrossAccountsResponse(AbstractModel):
    r"""ShareBlueprintAcrossAccounts返回参数结构体

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


class Snapshot(AbstractModel):
    r"""描述了快照相关信息。

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照 ID。
        :type SnapshotId: str
        :param _DiskUsage: 创建此快照的磁盘类型。取值：<li>SYSTEM_DISK：系统盘</li>
        :type DiskUsage: str
        :param _DiskId: 创建此快照的磁盘 ID。
        :type DiskId: str
        :param _DiskSize: 创建此快照的磁盘大小，单位 GB。
        :type DiskSize: int
        :param _SnapshotName: 快照名称，用户自定义的快照别名。
        :type SnapshotName: str
        :param _SnapshotState: 快照的状态。取值范围：
<li>NORMAL：正常 </li>
<li>CREATING：创建中</li>
<li>ROLLBACKING：回滚中。</li>
        :type SnapshotState: str
        :param _Percent: 创建或回滚快照进度百分比，成功后此字段取值为 100。
        :type Percent: int
        :param _LatestOperation: 快照的最新操作，只有创建、回滚快照时记录。
取值如 CreateInstanceSnapshot，RollbackInstanceSnapshot。
        :type LatestOperation: str
        :param _LatestOperationState: 快照的最新操作状态，只有创建、回滚快照时记录。
取值范围：
<li>SUCCESS：表示操作成功</li>
<li>OPERATING：表示操作执行中</li>
<li>FAILED：表示操作失败</li>
        :type LatestOperationState: str
        :param _LatestOperationRequestId: 快照最新操作的唯一请求 ID，只有创建、回滚快照时记录。
        :type LatestOperationRequestId: str
        :param _CreatedTime: 快照的创建时间。
        :type CreatedTime: str
        :param _Tags: 快照绑定的标签列表。
        :type Tags: list of Tag
        """
        self._SnapshotId = None
        self._DiskUsage = None
        self._DiskId = None
        self._DiskSize = None
        self._SnapshotName = None
        self._SnapshotState = None
        self._Percent = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._CreatedTime = None
        self._Tags = None

    @property
    def SnapshotId(self):
        r"""快照 ID。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskUsage(self):
        r"""创建此快照的磁盘类型。取值：<li>SYSTEM_DISK：系统盘</li>
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskId(self):
        r"""创建此快照的磁盘 ID。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        r"""创建此快照的磁盘大小，单位 GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def SnapshotName(self):
        r"""快照名称，用户自定义的快照别名。
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotState(self):
        r"""快照的状态。取值范围：
<li>NORMAL：正常 </li>
<li>CREATING：创建中</li>
<li>ROLLBACKING：回滚中。</li>
        :rtype: str
        """
        return self._SnapshotState

    @SnapshotState.setter
    def SnapshotState(self, SnapshotState):
        self._SnapshotState = SnapshotState

    @property
    def Percent(self):
        r"""创建或回滚快照进度百分比，成功后此字段取值为 100。
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def LatestOperation(self):
        r"""快照的最新操作，只有创建、回滚快照时记录。
取值如 CreateInstanceSnapshot，RollbackInstanceSnapshot。
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        r"""快照的最新操作状态，只有创建、回滚快照时记录。
取值范围：
<li>SUCCESS：表示操作成功</li>
<li>OPERATING：表示操作执行中</li>
<li>FAILED：表示操作失败</li>
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        r"""快照最新操作的唯一请求 ID，只有创建、回滚快照时记录。
        :rtype: str
        """
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def CreatedTime(self):
        r"""快照的创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        r"""快照绑定的标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotState = params.get("SnapshotState")
        self._Percent = params.get("Percent")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotDeniedActions(AbstractModel):
    r"""快照操作限制列表。

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照 ID。
        :type SnapshotId: str
        :param _DeniedActions: 操作限制列表。
        :type DeniedActions: list of DeniedAction
        """
        self._SnapshotId = None
        self._DeniedActions = None

    @property
    def SnapshotId(self):
        r"""快照 ID。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DeniedActions(self):
        r"""操作限制列表。
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Software(AbstractModel):
    r"""描述镜像软件信息。

    """

    def __init__(self):
        r"""
        :param _Name: 软件名称。
        :type Name: str
        :param _Version: 软件版本。
        :type Version: str
        :param _ImageUrl: 软件图片 URL。
        :type ImageUrl: str
        :param _InstallDir: 软件安装目录。
        :type InstallDir: str
        :param _DetailSet: 软件详情列表。
        :type DetailSet: list of SoftwareDetail
        """
        self._Name = None
        self._Version = None
        self._ImageUrl = None
        self._InstallDir = None
        self._DetailSet = None

    @property
    def Name(self):
        r"""软件名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        r"""软件版本。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ImageUrl(self):
        r"""软件图片 URL。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def InstallDir(self):
        r"""软件安装目录。
        :rtype: str
        """
        return self._InstallDir

    @InstallDir.setter
    def InstallDir(self, InstallDir):
        self._InstallDir = InstallDir

    @property
    def DetailSet(self):
        r"""软件详情列表。
        :rtype: list of SoftwareDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._ImageUrl = params.get("ImageUrl")
        self._InstallDir = params.get("InstallDir")
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = SoftwareDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoftwareDetail(AbstractModel):
    r"""描述镜像软件详细信息。

    """

    def __init__(self):
        r"""
        :param _Key: 软件的属性标识
        :type Key: str
        :param _Title: 软件的属性标识描述
        :type Title: str
        :param _Value: 软件的属性值
        :type Value: str
        """
        self._Key = None
        self._Title = None
        self._Value = None

    @property
    def Key(self):
        r"""软件的属性标识
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Title(self):
        r"""软件的属性标识描述
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Value(self):
        r"""软件的属性值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Title = params.get("Title")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartDockerContainersRequest(AbstractModel):
    r"""StartDockerContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerIds: 容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerIds: list of str
        """
        self._InstanceId = None
        self._ContainerIds = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerIds(self):
        r"""容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: list of str
        """
        return self._ContainerIds

    @ContainerIds.setter
    def ContainerIds(self, ContainerIds):
        self._ContainerIds = ContainerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerIds = params.get("ContainerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartDockerContainersResponse(AbstractModel):
    r"""StartDockerContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DockerActivityId: Docker活动ID。
        :type DockerActivityId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DockerActivityId = None
        self._RequestId = None

    @property
    def DockerActivityId(self):
        r"""Docker活动ID。
        :rtype: str
        """
        return self._DockerActivityId

    @DockerActivityId.setter
    def DockerActivityId(self, DockerActivityId):
        self._DockerActivityId = DockerActivityId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DockerActivityId = params.get("DockerActivityId")
        self._RequestId = params.get("RequestId")


class StartInstancesRequest(AbstractModel):
    r"""StartInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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
        


class StartInstancesResponse(AbstractModel):
    r"""StartInstances返回参数结构体

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


class StartMcpServersRequest(AbstractModel):
    r"""StartMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _McpServerIds: MCP Server ID列表。可通过DescribeMcpServers接口返回值中的McpServerId获取。最大长度：10
        :type McpServerIds: list of str
        """
        self._InstanceId = None
        self._McpServerIds = None

    @property
    def InstanceId(self):
        r"""实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def McpServerIds(self):
        r"""MCP Server ID列表。可通过DescribeMcpServers接口返回值中的McpServerId获取。最大长度：10
        :rtype: list of str
        """
        return self._McpServerIds

    @McpServerIds.setter
    def McpServerIds(self, McpServerIds):
        self._McpServerIds = McpServerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._McpServerIds = params.get("McpServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMcpServersResponse(AbstractModel):
    r"""StartMcpServers返回参数结构体

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


class StopDockerContainersRequest(AbstractModel):
    r"""StopDockerContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _ContainerIds: 容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :type ContainerIds: list of str
        """
        self._InstanceId = None
        self._ContainerIds = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/product/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ContainerIds(self):
        r"""容器ID列表。可通过[DescribeDockerContainers](https://cloud.tencent.com/document/product/1207/95473)接口返回值中的ContainerId获取。
        :rtype: list of str
        """
        return self._ContainerIds

    @ContainerIds.setter
    def ContainerIds(self, ContainerIds):
        self._ContainerIds = ContainerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ContainerIds = params.get("ContainerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDockerContainersResponse(AbstractModel):
    r"""StopDockerContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DockerActivityId: Docker活动ID。
        :type DockerActivityId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DockerActivityId = None
        self._RequestId = None

    @property
    def DockerActivityId(self):
        r"""Docker活动ID。
        :rtype: str
        """
        return self._DockerActivityId

    @DockerActivityId.setter
    def DockerActivityId(self, DockerActivityId):
        self._DockerActivityId = DockerActivityId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DockerActivityId = params.get("DockerActivityId")
        self._RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    r"""StopInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param _StopType: 关机类型。取值范围： 
<li>SOFT：表示软关机</li>
<li>HARD：表示硬关机 </li>
<li>SOFT_FIRST：表示优先软关机，失败再执行硬关机 </li>

默认取值：SOFT_FIRST
        :type StopType: str
        """
        self._InstanceIds = None
        self._StopType = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def StopType(self):
        r"""关机类型。取值范围： 
<li>SOFT：表示软关机</li>
<li>HARD：表示硬关机 </li>
<li>SOFT_FIRST：表示优先软关机，失败再执行硬关机 </li>

默认取值：SOFT_FIRST
        :rtype: str
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    r"""StopInstances返回参数结构体

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


class StopMcpServersRequest(AbstractModel):
    r"""StopMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param _McpServerIds: MCP Server ID列表。可通过DescribeMcpServers接口返回值中的McpServerId获取。最大长度：10
        :type McpServerIds: list of str
        """
        self._InstanceId = None
        self._McpServerIds = None

    @property
    def InstanceId(self):
        r"""实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def McpServerIds(self):
        r"""MCP Server ID列表。可通过DescribeMcpServers接口返回值中的McpServerId获取。最大长度：10
        :rtype: list of str
        """
        return self._McpServerIds

    @McpServerIds.setter
    def McpServerIds(self, McpServerIds):
        self._McpServerIds = McpServerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._McpServerIds = params.get("McpServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMcpServersResponse(AbstractModel):
    r"""StopMcpServers返回参数结构体

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


class SupportIpv6Detail(AbstractModel):
    r"""实例支持IPv6详情描述。

    """

    def __init__(self):
        r"""
        :param _IsSupport: 是否支持开启IPv6。
        :type IsSupport: bool
        :param _Detail: 详情。

当IsSupport为True，Detail枚举值为:

EFFECTIVE_IMMEDIATELY: 立即生效

EFFECTIVE_AFTER_REBOOT: 分配过程需要开关机，用户需备份数据

 

当IsSupport为False，Detail枚举值为:

HAD_BEEN_ASSIGNED: 已分配IPv6地址

REGION_NOT_SUPPORT: 地域不支持

BLUEPRINT_NOT_SUPPORT: 镜像不支持

BUNDLE_INSTANCE_NOT_SUPPORT: 套餐实例不支持

BUNDLE_BANDWIDTH_NOT_SUPPORT: 套餐带宽不支持
        :type Detail: str
        :param _Message: 提示信息。
        :type Message: str
        """
        self._IsSupport = None
        self._Detail = None
        self._Message = None

    @property
    def IsSupport(self):
        r"""是否支持开启IPv6。
        :rtype: bool
        """
        return self._IsSupport

    @IsSupport.setter
    def IsSupport(self, IsSupport):
        self._IsSupport = IsSupport

    @property
    def Detail(self):
        r"""详情。

当IsSupport为True，Detail枚举值为:

EFFECTIVE_IMMEDIATELY: 立即生效

EFFECTIVE_AFTER_REBOOT: 分配过程需要开关机，用户需备份数据

 

当IsSupport为False，Detail枚举值为:

HAD_BEEN_ASSIGNED: 已分配IPv6地址

REGION_NOT_SUPPORT: 地域不支持

BLUEPRINT_NOT_SUPPORT: 镜像不支持

BUNDLE_INSTANCE_NOT_SUPPORT: 套餐实例不支持

BUNDLE_BANDWIDTH_NOT_SUPPORT: 套餐带宽不支持
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Message(self):
        r"""提示信息。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._IsSupport = params.get("IsSupport")
        self._Detail = params.get("Detail")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncBlueprintRequest(AbstractModel):
    r"""SyncBlueprint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BlueprintId: 镜像ID。
        :type BlueprintId: str
        :param _DestinationRegions: 同步镜像的目的地域列表。
        :type DestinationRegions: list of str
        """
        self._BlueprintId = None
        self._DestinationRegions = None

    @property
    def BlueprintId(self):
        r"""镜像ID。
        :rtype: str
        """
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def DestinationRegions(self):
        r"""同步镜像的目的地域列表。
        :rtype: list of str
        """
        return self._DestinationRegions

    @DestinationRegions.setter
    def DestinationRegions(self, DestinationRegions):
        self._DestinationRegions = DestinationRegions


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._DestinationRegions = params.get("DestinationRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncBlueprintResponse(AbstractModel):
    r"""SyncBlueprint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DestinationRegionBlueprintSet: 目标地域镜像信息。
        :type DestinationRegionBlueprintSet: list of DestinationRegionBlueprint
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DestinationRegionBlueprintSet = None
        self._RequestId = None

    @property
    def DestinationRegionBlueprintSet(self):
        r"""目标地域镜像信息。
        :rtype: list of DestinationRegionBlueprint
        """
        return self._DestinationRegionBlueprintSet

    @DestinationRegionBlueprintSet.setter
    def DestinationRegionBlueprintSet(self, DestinationRegionBlueprintSet):
        self._DestinationRegionBlueprintSet = DestinationRegionBlueprintSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DestinationRegionBlueprintSet") is not None:
            self._DestinationRegionBlueprintSet = []
            for item in params.get("DestinationRegionBlueprintSet"):
                obj = DestinationRegionBlueprint()
                obj._deserialize(item)
                self._DestinationRegionBlueprintSet.append(obj)
        self._RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    r"""描述了操作系统所在块设备即系统盘的信息。

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。
取值范围： 
<li> LOCAL_BASIC：本地硬盘</li><li> LOCAL_SSD：本地 SSD 硬盘</li><li> CLOUD_BASIC：普通云硬盘</li><li> CLOUD_SSD：SSD 云硬盘</li><li> CLOUD_PREMIUM：高性能云硬盘</li>
        :type DiskType: str
        :param _DiskSize: 系统盘大小，单位：GB。
        :type DiskSize: int
        :param _DiskId: 系统盘ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskId: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskId = None

    @property
    def DiskType(self):
        r"""系统盘类型。
取值范围： 
<li> LOCAL_BASIC：本地硬盘</li><li> LOCAL_SSD：本地 SSD 硬盘</li><li> CLOUD_BASIC：普通云硬盘</li><li> CLOUD_SSD：SSD 云硬盘</li><li> CLOUD_PREMIUM：高性能云硬盘</li>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""系统盘大小，单位：GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        r"""系统盘ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
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
        


class TerminateDisksRequest(AbstractModel):
    r"""TerminateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID列表。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
每次批量请求云硬盘的上限数量为100。
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        r"""云硬盘ID列表。可通过[DescribeDisks](https://cloud.tencent.com/document/product/1207/66093)接口返回值中的DiskId获取。
每次批量请求云硬盘的上限数量为100。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksResponse(AbstractModel):
    r"""TerminateDisks返回参数结构体

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


class TerminateInstancesRequest(AbstractModel):
    r"""TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""实例ID列表。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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
        


class TerminateInstancesResponse(AbstractModel):
    r"""TerminateInstances返回参数结构体

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


class TotalPrice(AbstractModel):
    r"""总计价格信息

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 原始总计价格。
        :type OriginalPrice: float
        :param _DiscountPrice: 折扣总计价格。
        :type DiscountPrice: float
        """
        self._OriginalPrice = None
        self._DiscountPrice = None

    @property
    def OriginalPrice(self):
        r"""原始总计价格。
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        r"""折扣总计价格。
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficPackage(AbstractModel):
    r"""流量包详情

    """

    def __init__(self):
        r"""
        :param _TrafficPackageId: 流量包ID。
        :type TrafficPackageId: str
        :param _TrafficUsed: 流量包生效周期内已使用流量，单位字节。
        :type TrafficUsed: int
        :param _TrafficPackageTotal: 流量包生效周期内的总流量，单位字节。
        :type TrafficPackageTotal: int
        :param _TrafficPackageRemaining: 流量包生效周期内的剩余流量，单位字节。
        :type TrafficPackageRemaining: int
        :param _TrafficOverflow: 流量包生效周期内超出流量包额度的流量，单位字节。
        :type TrafficOverflow: int
        :param _StartTime: 流量包生效周期开始时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :type StartTime: str
        :param _EndTime: 流量包生效周期结束时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :type EndTime: str
        :param _Deadline: 流量包到期时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :type Deadline: str
        :param _Status: 流量包状态：
<li>NETWORK_NORMAL：正常</li>
<li>OVERDUE_NETWORK_DISABLED：欠费断网</li>
        :type Status: str
        """
        self._TrafficPackageId = None
        self._TrafficUsed = None
        self._TrafficPackageTotal = None
        self._TrafficPackageRemaining = None
        self._TrafficOverflow = None
        self._StartTime = None
        self._EndTime = None
        self._Deadline = None
        self._Status = None

    @property
    def TrafficPackageId(self):
        r"""流量包ID。
        :rtype: str
        """
        return self._TrafficPackageId

    @TrafficPackageId.setter
    def TrafficPackageId(self, TrafficPackageId):
        self._TrafficPackageId = TrafficPackageId

    @property
    def TrafficUsed(self):
        r"""流量包生效周期内已使用流量，单位字节。
        :rtype: int
        """
        return self._TrafficUsed

    @TrafficUsed.setter
    def TrafficUsed(self, TrafficUsed):
        self._TrafficUsed = TrafficUsed

    @property
    def TrafficPackageTotal(self):
        r"""流量包生效周期内的总流量，单位字节。
        :rtype: int
        """
        return self._TrafficPackageTotal

    @TrafficPackageTotal.setter
    def TrafficPackageTotal(self, TrafficPackageTotal):
        self._TrafficPackageTotal = TrafficPackageTotal

    @property
    def TrafficPackageRemaining(self):
        r"""流量包生效周期内的剩余流量，单位字节。
        :rtype: int
        """
        return self._TrafficPackageRemaining

    @TrafficPackageRemaining.setter
    def TrafficPackageRemaining(self, TrafficPackageRemaining):
        self._TrafficPackageRemaining = TrafficPackageRemaining

    @property
    def TrafficOverflow(self):
        r"""流量包生效周期内超出流量包额度的流量，单位字节。
        :rtype: int
        """
        return self._TrafficOverflow

    @TrafficOverflow.setter
    def TrafficOverflow(self, TrafficOverflow):
        self._TrafficOverflow = TrafficOverflow

    @property
    def StartTime(self):
        r"""流量包生效周期开始时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""流量包生效周期结束时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Deadline(self):
        r"""流量包到期时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def Status(self):
        r"""流量包状态：
<li>NETWORK_NORMAL：正常</li>
<li>OVERDUE_NETWORK_DISABLED：欠费断网</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TrafficPackageId = params.get("TrafficPackageId")
        self._TrafficUsed = params.get("TrafficUsed")
        self._TrafficPackageTotal = params.get("TrafficPackageTotal")
        self._TrafficPackageRemaining = params.get("TrafficPackageRemaining")
        self._TrafficOverflow = params.get("TrafficOverflow")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Deadline = params.get("Deadline")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    r"""可用区详细信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _ZoneName: 可用区中文名称
        :type ZoneName: str
        :param _InstanceDisplayLabel: 实例购买页可用区展示标签
        :type InstanceDisplayLabel: str
        """
        self._Zone = None
        self._ZoneName = None
        self._InstanceDisplayLabel = None

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""可用区中文名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceDisplayLabel(self):
        r"""实例购买页可用区展示标签
        :rtype: str
        """
        return self._InstanceDisplayLabel

    @InstanceDisplayLabel.setter
    def InstanceDisplayLabel(self, InstanceDisplayLabel):
        self._InstanceDisplayLabel = InstanceDisplayLabel


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._InstanceDisplayLabel = params.get("InstanceDisplayLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        