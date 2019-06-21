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


class ApplySnapshotRequest(AbstractModel):
    """ApplySnapshot请求参数结构体

    """

    def __init__(self):
        """
        :param SnapshotId: 快照ID, 可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :type SnapshotId: str
        :param DiskId: 快照原云硬盘ID，可通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        """
        self.SnapshotId = None
        self.DiskId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.DiskId = params.get("DiskId")


class ApplySnapshotResponse(AbstractModel):
    """ApplySnapshot返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachDetail(AbstractModel):
    """描述一个实例已挂载和可挂载数据盘的数量。

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param AttachedDiskCount: 实例已挂载数据盘的数量。
        :type AttachedDiskCount: int
        :param MaxAttachCount: 实例最大可挂载数据盘的数量。
        :type MaxAttachCount: int
        """
        self.InstanceId = None
        self.AttachedDiskCount = None
        self.MaxAttachCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AttachedDiskCount = params.get("AttachedDiskCount")
        self.MaxAttachCount = params.get("MaxAttachCount")


class AttachDisksRequest(AbstractModel):
    """AttachDisks请求参数结构体

    """

    def __init__(self):
        """
        :param DiskIds: 将要被挂载的弹性云盘ID。通过[DescribeDisks](/document/product/362/16315)接口查询。单次最多可挂载10块弹性云盘。
        :type DiskIds: list of str
        :param InstanceId: 云服务器实例ID。云盘将被挂载到此云服务器上，通过[DescribeInstances](/document/product/213/15728)接口查询。
        :type InstanceId: str
        :param DeleteWithInstance: 可选参数，不传该参数则仅执行挂载操作。传入`True`时，会在挂载成功后将云硬盘设置为随云主机销毁模式，仅对按量计费云硬盘有效。
        :type DeleteWithInstance: bool
        """
        self.DiskIds = None
        self.InstanceId = None
        self.DeleteWithInstance = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.InstanceId = params.get("InstanceId")
        self.DeleteWithInstance = params.get("DeleteWithInstance")


class AttachDisksResponse(AbstractModel):
    """AttachDisks返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AutoSnapshotPolicy(AbstractModel):
    """描述了定期快照策略的详细信息

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyId: 定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param AutoSnapshotPolicyName: 定期快照策略名称。
        :type AutoSnapshotPolicyName: str
        :param AutoSnapshotPolicyState: 定期快照策略的状态。取值范围：<br><li>NORMAL：正常<br><li>ISOLATED：已隔离。
        :type AutoSnapshotPolicyState: str
        :param IsActivated: 定期快照策略是否激活。
        :type IsActivated: bool
        :param IsPermanent: 使用该定期快照策略创建出来的快照是否永久保留。
        :type IsPermanent: bool
        :param RetentionDays: 使用该定期快照策略创建出来的快照保留天数。
        :type RetentionDays: int
        :param CreateTime: 定期快照策略的创建时间。
        :type CreateTime: str
        :param NextTriggerTime: 定期快照下次触发的时间。
        :type NextTriggerTime: str
        :param Policy: 定期快照的执行策略。
        :type Policy: list of Policy
        :param DiskIdSet: 已绑定当前定期快照策略的云盘ID列表。
        :type DiskIdSet: list of str
        """
        self.AutoSnapshotPolicyId = None
        self.AutoSnapshotPolicyName = None
        self.AutoSnapshotPolicyState = None
        self.IsActivated = None
        self.IsPermanent = None
        self.RetentionDays = None
        self.CreateTime = None
        self.NextTriggerTime = None
        self.Policy = None
        self.DiskIdSet = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self.AutoSnapshotPolicyState = params.get("AutoSnapshotPolicyState")
        self.IsActivated = params.get("IsActivated")
        self.IsPermanent = params.get("IsPermanent")
        self.RetentionDays = params.get("RetentionDays")
        self.CreateTime = params.get("CreateTime")
        self.NextTriggerTime = params.get("NextTriggerTime")
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self.Policy.append(obj)
        self.DiskIdSet = params.get("DiskIdSet")


class BindAutoSnapshotPolicyRequest(AbstractModel):
    """BindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyId: 要绑定的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param DiskIds: 要绑定的云硬盘ID列表，一次请求最多绑定80块云盘。
        :type DiskIds: list of str
        """
        self.AutoSnapshotPolicyId = None
        self.DiskIds = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.DiskIds = params.get("DiskIds")


class BindAutoSnapshotPolicyResponse(AbstractModel):
    """BindAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    """CreateAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Policy: 定期快照的执行策略。
        :type Policy: list of Policy
        :param AutoSnapshotPolicyName: 要创建的定期快照策略名。不传则默认为“未命名”。最大长度不能超60个字节。
        :type AutoSnapshotPolicyName: str
        :param IsActivated: 是否激活定期快照策略，FALSE表示未激活，TRUE表示激活，默认为TRUE。
        :type IsActivated: bool
        :param IsPermanent: 通过该定期快照策略创建的快照是否永久保留。FALSE表示非永久保留，TRUE表示永久保留，默认为FALSE。
        :type IsPermanent: bool
        :param RetentionDays: 通过该定期快照策略创建的快照保留天数，默认保留7天。如果指定本参数，则IsPermanent入参不可指定为TRUE，否则会产生冲突。
        :type RetentionDays: int
        :param DryRun: 是否创建定期快照的执行策略。TRUE表示只需获取首次开始备份的时间，不实际创建定期快照策略，FALSE表示创建，默认为FALSE。
        :type DryRun: bool
        """
        self.Policy = None
        self.AutoSnapshotPolicyName = None
        self.IsActivated = None
        self.IsPermanent = None
        self.RetentionDays = None
        self.DryRun = None


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self.Policy.append(obj)
        self.AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self.IsActivated = params.get("IsActivated")
        self.IsPermanent = params.get("IsPermanent")
        self.RetentionDays = params.get("RetentionDays")
        self.DryRun = params.get("DryRun")


class CreateAutoSnapshotPolicyResponse(AbstractModel):
    """CreateAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyId: 新创建的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param NextTriggerTime: 首次开始备份的时间。
        :type NextTriggerTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoSnapshotPolicyId = None
        self.NextTriggerTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.NextTriggerTime = params.get("NextTriggerTime")
        self.RequestId = params.get("RequestId")


class CreateDisksRequest(AbstractModel):
    """CreateDisks请求参数结构体

    """

    def __init__(self):
        """
        :param DiskType: 硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘。
        :type DiskType: str
        :param DiskChargeType: 云硬盘计费类型。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>CDCPAID：独享集群付费<br>各类型价格请参考云硬盘[价格总览](/document/product/362/2413)。
        :type DiskChargeType: str
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目。若不指定项目，将在默认项目下进行创建。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param DiskName: 云盘显示名称。不传则默认为“未命名”。最大长度不能超60个字节。
        :type DiskName: str
        :param DiskCount: 创建云硬盘数量，不传则默认为1。单次请求最多可创建的云盘数有限制，具体参见[云硬盘使用限制](https://cloud.tencent.com/doc/product/362/5145)。
        :type DiskCount: int
        :param DiskChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数指定包年包月云盘的购买时长、是否设置自动续费等属性。<br>创建预付费云盘该参数必传，创建按小时后付费云盘无需传该参数。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param DiskSize: 云硬盘大小，单位为GB。<br><li>如果传入`SnapshotId`则可不传`DiskSize`，此时新建云盘的大小为快照大小<br><li>如果传入`SnapshotId`同时传入`DiskSize`，则云盘大小必须大于或等于快照大小<br><li>云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        :param SnapshotId: 快照ID，如果传入则根据此快照创建云硬盘，快照类型必须为数据盘快照，可通过[DescribeSnapshots](/document/product/362/15647)接口查询快照，见输出参数DiskUsage解释。
        :type SnapshotId: str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param Encrypt: 传入该参数用于创建加密云盘，取值固定为ENCRYPT。
        :type Encrypt: str
        :param Tags: 云盘绑定的标签。
        :type Tags: list of Tag
        :param Shareable: 可选参数，默认为False。传入True时，云盘将创建为共享型云盘。
        :type Shareable: bool
        """
        self.DiskType = None
        self.DiskChargeType = None
        self.Placement = None
        self.DiskName = None
        self.DiskCount = None
        self.DiskChargePrepaid = None
        self.DiskSize = None
        self.SnapshotId = None
        self.ClientToken = None
        self.Encrypt = None
        self.Tags = None
        self.Shareable = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskChargeType = params.get("DiskChargeType")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.DiskName = params.get("DiskName")
        self.DiskCount = params.get("DiskCount")
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DiskSize = params.get("DiskSize")
        self.SnapshotId = params.get("SnapshotId")
        self.ClientToken = params.get("ClientToken")
        self.Encrypt = params.get("Encrypt")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Shareable = params.get("Shareable")


class CreateDisksResponse(AbstractModel):
    """CreateDisks返回参数结构体

    """

    def __init__(self):
        """
        :param DiskIdSet: 创建的云硬盘ID列表。
        :type DiskIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiskIdSet = params.get("DiskIdSet")
        self.RequestId = params.get("RequestId")


class CreateSnapshotRequest(AbstractModel):
    """CreateSnapshot请求参数结构体

    """

    def __init__(self):
        """
        :param DiskId: 需要创建快照的云硬盘ID，可通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        :param SnapshotName: 快照名称，不传则新快照名称默认为“未命名”。
        :type SnapshotName: str
        """
        self.DiskId = None
        self.SnapshotName = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.SnapshotName = params.get("SnapshotName")


class CreateSnapshotResponse(AbstractModel):
    """CreateSnapshot返回参数结构体

    """

    def __init__(self):
        """
        :param SnapshotId: 新创建的快照ID。
        :type SnapshotId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.RequestId = params.get("RequestId")


class DeleteAutoSnapshotPoliciesRequest(AbstractModel):
    """DeleteAutoSnapshotPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyIds: 要删除的定期快照策略ID列表。
        :type AutoSnapshotPolicyIds: list of str
        """
        self.AutoSnapshotPolicyIds = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")


class DeleteAutoSnapshotPoliciesResponse(AbstractModel):
    """DeleteAutoSnapshotPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots请求参数结构体

    """

    def __init__(self):
        """
        :param SnapshotIds: 要删除的快照ID列表，可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :type SnapshotIds: list of str
        """
        self.SnapshotIds = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    """DescribeAutoSnapshotPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyIds: 要查询的定期快照策略ID列表。参数不支持同时指定`AutoSnapshotPolicyIds`和`Filters`。
        :type AutoSnapshotPolicyIds: list of str
        :param Filters: 过滤条件。参数不支持同时指定`AutoSnapshotPolicyIds`和`Filters`。<br><li>auto-snapshot-policy-id - Array of String - 是否必填：否 -（过滤条件）按定期快照策略ID进行过滤。定期快照策略ID形如：`asp-11112222`。<br><li>auto-snapshot-policy-state - Array of String - 是否必填：否 -（过滤条件）按定期快照策略的状态进行过滤。定期快照策略ID形如：`asp-11112222`。(NORMAL：正常 | ISOLATED：已隔离。)<br><li>auto-snapshot-policy-name - Array of String - 是否必填：否 -（过滤条件）按定期快照策略名称进行过滤。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/362/13158)中的相关小节。
        :type Limit: int
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/362/13158)中的相关小节。
        :type Offset: int
        :param Order: 输出定期快照列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        :param OrderField: 定期快照列表排序的依据字段。取值范围：<br><li>CREATETIME：依据定期快照的创建时间排序<br>默认按创建时间排序。
        :type OrderField: str
        """
        self.AutoSnapshotPolicyIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeAutoSnapshotPoliciesResponse(AbstractModel):
    """DescribeAutoSnapshotPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 有效的定期快照策略数量。
        :type TotalCount: int
        :param AutoSnapshotPolicySet: 定期快照策略列表。
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoSnapshotPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self.AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self.AutoSnapshotPolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskAssociatedAutoSnapshotPolicyRequest(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param DiskId: 要查询的云硬盘ID。
        :type DiskId: str
        """
        self.DiskId = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")


class DescribeDiskAssociatedAutoSnapshotPolicyResponse(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 云盘绑定的定期快照数量。
        :type TotalCount: int
        :param AutoSnapshotPolicySet: 云盘绑定的定期快照列表。
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoSnapshotPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self.AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self.AutoSnapshotPolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskConfigQuotaRequest(AbstractModel):
    """DescribeDiskConfigQuota请求参数结构体

    """

    def __init__(self):
        """
        :param InquiryType: 查询类别，取值范围。<br><li>INQUIRY_CBS_CONFIG：查询云盘配置列表<br><li>INQUIRY_CVM_CONFIG：查询云盘与实例搭配的配置列表。
        :type InquiryType: str
        :param Zones: 查询一个或多个[可用区](/document/product/213/15753#ZoneInfo)下的配置。
        :type Zones: list of str
        :param DiskChargeType: 付费模式。取值范围：<br><li>PREPAID：预付费<br><li>POSTPAID_BY_HOUR：后付费。
        :type DiskChargeType: str
        :param DiskTypes: 硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘。
        :type DiskTypes: list of str
        :param DiskUsage: 系统盘或数据盘。取值范围：<br><li>SYSTEM_DISK：表示系统盘<br><li>DATA_DISK：表示数据盘。
        :type DiskUsage: str
        :param InstanceFamilies: 按照实例机型系列过滤。实例机型系列形如：S1、I1、M1等。详见[实例类型](https://cloud.tencent.com/document/product/213/11518)
        :type InstanceFamilies: list of str
        :param CPU: 实例CPU核数。
        :type CPU: int
        :param Memory: 实例内存大小。
        :type Memory: int
        """
        self.InquiryType = None
        self.Zones = None
        self.DiskChargeType = None
        self.DiskTypes = None
        self.DiskUsage = None
        self.InstanceFamilies = None
        self.CPU = None
        self.Memory = None


    def _deserialize(self, params):
        self.InquiryType = params.get("InquiryType")
        self.Zones = params.get("Zones")
        self.DiskChargeType = params.get("DiskChargeType")
        self.DiskTypes = params.get("DiskTypes")
        self.DiskUsage = params.get("DiskUsage")
        self.InstanceFamilies = params.get("InstanceFamilies")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")


class DescribeDiskConfigQuotaResponse(AbstractModel):
    """DescribeDiskConfigQuota返回参数结构体

    """

    def __init__(self):
        """
        :param DiskConfigSet: 云盘配置列表。
        :type DiskConfigSet: list of DiskConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskConfigSet") is not None:
            self.DiskConfigSet = []
            for item in params.get("DiskConfigSet"):
                obj = DiskConfig()
                obj._deserialize(item)
                self.DiskConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskOperationLogsRequest(AbstractModel):
    """DescribeDiskOperationLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。支持以下条件：
<li>disk-id - Array of String - 是否必填：是 - 按云盘ID过滤，每个请求最多可指定10个云盘ID。
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeDiskOperationLogsResponse(AbstractModel):
    """DescribeDiskOperationLogs返回参数结构体

    """

    def __init__(self):
        """
        :param DiskOperationLogSet: 云盘的操作日志列表。
        :type DiskOperationLogSet: list of DiskOperationLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskOperationLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskOperationLogSet") is not None:
            self.DiskOperationLogSet = []
            for item in params.get("DiskOperationLogSet"):
                obj = DiskOperationLog()
                obj._deserialize(item)
                self.DiskOperationLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    """DescribeDisks请求参数结构体

    """

    def __init__(self):
        """
        :param DiskIds: 按照一个或者多个云硬盘ID查询。云硬盘ID形如：`disk-11112222`，此参数的具体格式可参考API[简介](/document/product/362/15633)的ids.N一节）。参数不支持同时指定`DiskIds`和`Filters`。
        :type DiskIds: list of str
        :param Filters: 过滤条件。参数不支持同时指定`DiskIds`和`Filters`。<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按云盘类型过滤。 (SYSTEM_DISK：表示系统盘 | DATA_DISK：表示数据盘)<br><li>disk-charge-type - Array of String - 是否必填：否 -（过滤条件）按照云硬盘计费模式过滤。 (PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费。)<br><li>portable - Array of String - 是否必填：否 -（过滤条件）按是否为弹性云盘过滤。 (TRUE：表示弹性云盘 | FALSE：表示非弹性云盘。)<br><li>project-id - Array of Integer - 是否必填：否 -（过滤条件）按云硬盘所属项目ID过滤。<br><li>disk-id - Array of String - 是否必填：否 -（过滤条件）按照云硬盘ID过滤。云盘ID形如：`disk-11112222`。<br><li>disk-name - Array of String - 是否必填：否 -（过滤条件）按照云盘名称过滤。<br><li>disk-type - Array of String - 是否必填：否 -（过滤条件）按照云盘介质类型过滤。(CLOUD_BASIC：表示普通云硬盘 | CLOUD_PREMIUM：表示高性能云硬盘。| CLOUD_SSD：SSD表示SSD云硬盘。)<br><li>disk-state - Array of String - 是否必填：否 -（过滤条件）按照云盘状态过滤。(UNATTACHED：未挂载 | ATTACHING：挂载中 | ATTACHED：已挂载 | DETACHING：解挂中 | EXPANDING：扩容中 | ROLLBACKING：回滚中 | TORECYCLE：待回收。)<br><li>instance-id - Array of String - 是否必填：否 -（过滤条件）按照云盘挂载的云主机实例ID过滤。可根据此参数查询挂载在指定云主机下的云硬盘。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按照[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>instance-ip-address - Array of String - 是否必填：否 -（过滤条件）按云盘所挂载云主机的内网或外网IP过滤。<br><li>instance-name - Array of String - 是否必填：否 -（过滤条件）按云盘所挂载的实例名称过滤。<br><li>tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键进行过滤。<br><li>tag-value - Array of String - 是否必填：否 -（过滤条件）照标签值进行过滤。<br><li>tag:tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param Order: 输出云盘列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        :param OrderField: 云盘列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据云盘的创建时间排序<br><li>DEADLINE：依据云盘的到期时间排序<br>默认按云盘创建时间排序。
        :type OrderField: str
        :param ReturnBindAutoSnapshotPolicy: 云盘详情中是否需要返回云盘绑定的定期快照策略ID，TRUE表示需要返回，FALSE表示不返回。
        :type ReturnBindAutoSnapshotPolicy: bool
        """
        self.DiskIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.ReturnBindAutoSnapshotPolicy = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.ReturnBindAutoSnapshotPolicy = params.get("ReturnBindAutoSnapshotPolicy")


class DescribeDisksResponse(AbstractModel):
    """DescribeDisks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的云硬盘数量。
        :type TotalCount: int
        :param DiskSet: 云硬盘的详细信息列表。
        :type DiskSet: list of Disk
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DiskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DiskSet") is not None:
            self.DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self.DiskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesDiskNumRequest(AbstractModel):
    """DescribeInstancesDiskNum请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 云服务器实例ID，通过[DescribeInstances](/document/product/213/15728)接口查询。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeInstancesDiskNumResponse(AbstractModel):
    """DescribeInstancesDiskNum返回参数结构体

    """

    def __init__(self):
        """
        :param AttachDetail: 各个云服务器已挂载和可挂载弹性云盘的数量。
        :type AttachDetail: list of AttachDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AttachDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttachDetail") is not None:
            self.AttachDetail = []
            for item in params.get("AttachDetail"):
                obj = AttachDetail()
                obj._deserialize(item)
                self.AttachDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotOperationLogsRequest(AbstractModel):
    """DescribeSnapshotOperationLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。支持以下条件：
<li>snapshot-id - Array of String - 是否必填：是 - 按快照ID过滤，每个请求最多可指定10个快照ID。
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeSnapshotOperationLogsResponse(AbstractModel):
    """DescribeSnapshotOperationLogs返回参数结构体

    """

    def __init__(self):
        """
        :param SnapshotOperationLogSet: 快照操作日志列表。
        :type SnapshotOperationLogSet: list of SnapshotOperationLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotOperationLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SnapshotOperationLogSet") is not None:
            self.SnapshotOperationLogSet = []
            for item in params.get("SnapshotOperationLogSet"):
                obj = SnapshotOperationLog()
                obj._deserialize(item)
                self.SnapshotOperationLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots请求参数结构体

    """

    def __init__(self):
        """
        :param SnapshotIds: 要查询快照的ID列表。参数不支持同时指定`SnapshotIds`和`Filters`。
        :type SnapshotIds: list of str
        :param Filters: 过滤条件。参数不支持同时指定`SnapshotIds`和`Filters`。<br><li>snapshot-id - Array of String - 是否必填：否 -（过滤条件）按照快照的ID过滤。快照ID形如：`snap-11112222`。<br><li>snapshot-name - Array of String - 是否必填：否 -（过滤条件）按照快照名称过滤。<br><li>snapshot-state - Array of String - 是否必填：否 -（过滤条件）按照快照状态过滤。 (NORMAL：正常 | CREATING：创建中 | ROLLBACKING：回滚中。)<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按创建快照的云盘类型过滤。 (SYSTEM_DISK：代表系统盘 | DATA_DISK：代表数据盘。)<br><li>project-id  - Array of String - 是否必填：否 -（过滤条件）按云硬盘所属项目ID过滤。<br><li>disk-id  - Array of String - 是否必填：否 -（过滤条件）按照创建快照的云硬盘ID过滤。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按照[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>encrypt - Array of String - 是否必填：否 -（过滤条件）按是否加密盘快照过滤。 (TRUE：表示加密盘快照 | FALSE：表示非加密盘快照。)
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param Order: 输出云盘列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        :param OrderField: 快照列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据快照的创建时间排序<br>默认按创建时间排序。
        :type OrderField: str
        """
        self.SnapshotIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 快照的数量。
        :type TotalCount: int
        :param SnapshotSet: 快照的详情列表。
        :type SnapshotSet: list of Snapshot
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotSet") is not None:
            self.SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self.SnapshotSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachDisksRequest(AbstractModel):
    """DetachDisks请求参数结构体

    """

    def __init__(self):
        """
        :param DiskIds: 将要解挂的云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询，单次请求最多可解挂10块弹性云盘。
        :type DiskIds: list of str
        :param InstanceId: 对于非共享型云盘，会忽略该参数；对于共享型云盘，该参数表示要从哪个CVM实例上解挂云盘。
        :type InstanceId: str
        """
        self.DiskIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.InstanceId = params.get("InstanceId")


class DetachDisksResponse(AbstractModel):
    """DetachDisks返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Disk(AbstractModel):
    """描述了云硬盘的详细信息

    """

    def __init__(self):
        """
        :param DiskId: 云硬盘ID。
        :type DiskId: str
        :param DiskUsage: 云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :type DiskUsage: str
        :param DiskChargeType: 付费模式。取值范围：<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：后付费，即按量计费。
        :type DiskChargeType: str
        :param Portable: 是否为弹性云盘，false表示非弹性云盘，true表示弹性云盘。
        :type Portable: bool
        :param Placement: 云硬盘所在的位置。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param SnapshotAbility: 云盘是否具备创建快照的能力。取值范围：<br><li>false表示不具备<br><li>true表示具备。
        :type SnapshotAbility: bool
        :param DiskName: 云硬盘名称。
        :type DiskName: str
        :param DiskSize: 云硬盘大小，单位GB。
        :type DiskSize: int
        :param DiskState: 云盘状态。取值范围：<br><li>UNATTACHED：未挂载<br><li>ATTACHING：挂载中<br><li>ATTACHED：已挂载<br><li>DETACHING：解挂中<br><li>EXPANDING：扩容中<br><li>ROLLBACKING：回滚中<br><li>TORECYCLE：待回收<br><li>DUMPING：拷贝硬盘中。
        :type DiskState: str
        :param DiskType: 云盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：SSD表示SSD云硬盘。
        :type DiskType: str
        :param Attached: 云盘是否挂载到云主机上。取值范围：<br><li>false:表示未挂载<br><li>true:表示已挂载。
        :type Attached: bool
        :param InstanceId: 云硬盘挂载的云主机ID。
        :type InstanceId: str
        :param CreateTime: 云硬盘的创建时间。
        :type CreateTime: str
        :param DeadlineTime: 云硬盘的到期时间。
        :type DeadlineTime: str
        :param Rollbacking: 云盘是否处于快照回滚状态。取值范围：<br><li>false:表示不处于快照回滚状态<br><li>true:表示处于快照回滚状态。
        :type Rollbacking: bool
        :param RollbackPercent: 云盘快照回滚的进度。
        :type RollbackPercent: int
        :param Encrypt: 云盘是否为加密盘。取值范围：<br><li>false:表示非加密盘<br><li>true:表示加密盘。
        :type Encrypt: bool
        :param AutoRenewFlagError: 云盘已挂载到子机，且子机与云盘都是包年包月。<br><li>true：子机设置了自动续费标识，但云盘未设置<br><li>false：云盘自动续费标识正常。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlagError: bool
        :param RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        :param DeadlineError: 在云盘已挂载到实例，且实例与云盘都是包年包月的条件下，此字段才有意义。<br><li>true:云盘到期时间早于实例。<br><li>false：云盘到期时间晚于实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadlineError: bool
        :param IsReturnable: 判断预付费的云盘是否支持主动退还。<br><li>true:支持主动退还<br><li>false:不支持主动退还。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsReturnable: bool
        :param ReturnFailCode: 预付费云盘在不支持主动退还的情况下，该参数表明不支持主动退还的具体原因。取值范围：<br><li>1：云硬盘已经退还<br><li>2：云硬盘已过期<br><li>3：云盘不支持退还<br><li>8：超过可退还数量的限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnFailCode: int
        :param AutoSnapshotPolicyIds: 云盘关联的定期快照ID。只有在调用DescribeDisks接口时，入参ReturnBindAutoSnapshotPolicy取值为TRUE才会返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSnapshotPolicyIds: list of str
        :param Tags: 与云盘绑定的标签，云盘未绑定标签则取值为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param DeleteWithInstance: 云盘是否与挂载的实例一起销毁。<br><li>true:销毁实例时会同时销毁云盘，只支持按小时后付费云盘。<br><li>false：销毁实例时不销毁云盘。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param DifferDaysOfDeadline: 当前时间距离盘到期的天数（仅对预付费盘有意义）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DifferDaysOfDeadline: int
        :param Migrating: 云盘是否处于类型变更中。取值范围：<br><li>false:表示云盘不处于类型变更中<br><li>true:表示云盘已发起类型变更，正处于迁移中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Migrating: bool
        :param MigratePercent: 云盘类型变更的迁移进度，取值0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type MigratePercent: int
        :param Shareable: 云盘是否为共享型云盘。
        :type Shareable: bool
        :param InstanceIdList: 对于非共享型云盘，该参数为空数组。对于共享型云盘，则表示该云盘当前被挂载到的CVM实例InstanceId
        :type InstanceIdList: list of str
        """
        self.DiskId = None
        self.DiskUsage = None
        self.DiskChargeType = None
        self.Portable = None
        self.Placement = None
        self.SnapshotAbility = None
        self.DiskName = None
        self.DiskSize = None
        self.DiskState = None
        self.DiskType = None
        self.Attached = None
        self.InstanceId = None
        self.CreateTime = None
        self.DeadlineTime = None
        self.Rollbacking = None
        self.RollbackPercent = None
        self.Encrypt = None
        self.AutoRenewFlagError = None
        self.RenewFlag = None
        self.DeadlineError = None
        self.IsReturnable = None
        self.ReturnFailCode = None
        self.AutoSnapshotPolicyIds = None
        self.Tags = None
        self.DeleteWithInstance = None
        self.DifferDaysOfDeadline = None
        self.Migrating = None
        self.MigratePercent = None
        self.Shareable = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskChargeType = params.get("DiskChargeType")
        self.Portable = params.get("Portable")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.SnapshotAbility = params.get("SnapshotAbility")
        self.DiskName = params.get("DiskName")
        self.DiskSize = params.get("DiskSize")
        self.DiskState = params.get("DiskState")
        self.DiskType = params.get("DiskType")
        self.Attached = params.get("Attached")
        self.InstanceId = params.get("InstanceId")
        self.CreateTime = params.get("CreateTime")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Rollbacking = params.get("Rollbacking")
        self.RollbackPercent = params.get("RollbackPercent")
        self.Encrypt = params.get("Encrypt")
        self.AutoRenewFlagError = params.get("AutoRenewFlagError")
        self.RenewFlag = params.get("RenewFlag")
        self.DeadlineError = params.get("DeadlineError")
        self.IsReturnable = params.get("IsReturnable")
        self.ReturnFailCode = params.get("ReturnFailCode")
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.DifferDaysOfDeadline = params.get("DifferDaysOfDeadline")
        self.Migrating = params.get("Migrating")
        self.MigratePercent = params.get("MigratePercent")
        self.Shareable = params.get("Shareable")
        self.InstanceIdList = params.get("InstanceIdList")


class DiskChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        """
        :param Period: 购买云盘的时长，默认单位为月，取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>默认取值：NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费。
        :type RenewFlag: str
        :param CurInstanceDeadline: 需要将云盘的到期时间与挂载的子机对齐时，可传入该参数。该参数表示子机当前的到期时间，此时Period如果传入，则表示子机需要续费的时长，云盘会自动按对齐到子机续费后的到期时间续费，示例取值：2018-03-30 20:15:03。
        :type CurInstanceDeadline: str
        """
        self.Period = None
        self.RenewFlag = None
        self.CurInstanceDeadline = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        self.CurInstanceDeadline = params.get("CurInstanceDeadline")


class DiskConfig(AbstractModel):
    """云盘配置。

    """

    def __init__(self):
        """
        :param Available: 配置是否可用。
        :type Available: bool
        :param DiskType: 云盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：SSD表示SSD云硬盘。
        :type DiskType: str
        :param DiskUsage: 云盘类型。取值范围：<br><li>SYSTEM_DISK：表示系统盘<br><li>DATA_DISK：表示数据盘。
        :type DiskUsage: str
        :param DiskChargeType: 付费模式。取值范围：<br><li>PREPAID：表示预付费，即包年包月<br><li>POSTPAID_BY_HOUR：表示后付费，即按量计费。
        :type DiskChargeType: str
        :param MaxDiskSize: 最大可配置云盘大小，单位GB。
        :type MaxDiskSize: int
        :param MinDiskSize: 最小可配置云盘大小，单位GB。
        :type MinDiskSize: int
        :param Zone: 云硬盘所属的[可用区](/document/product/213/15753#ZoneInfo)。
        :type Zone: str
        :param DeviceClass: 实例机型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param InstanceFamily: 实例机型系列。详见[实例类型](https://cloud.tencent.com/document/product/213/11518)
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceFamily: str
        """
        self.Available = None
        self.DiskType = None
        self.DiskUsage = None
        self.DiskChargeType = None
        self.MaxDiskSize = None
        self.MinDiskSize = None
        self.Zone = None
        self.DeviceClass = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.Available = params.get("Available")
        self.DiskType = params.get("DiskType")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskChargeType = params.get("DiskChargeType")
        self.MaxDiskSize = params.get("MaxDiskSize")
        self.MinDiskSize = params.get("MinDiskSize")
        self.Zone = params.get("Zone")
        self.DeviceClass = params.get("DeviceClass")
        self.InstanceFamily = params.get("InstanceFamily")


class DiskOperationLog(AbstractModel):
    """云盘操作日志。

    """

    def __init__(self):
        """
        :param Operator: 操作者的UIN。
        :type Operator: str
        :param Operation: 操作类型。取值范围：
CBS_OPERATION_ATTACH：挂载云硬盘
CBS_OPERATION_DETACH：解挂云硬盘
CBS_OPERATION_RENEW：续费
CBS_OPERATION_EXPAND：扩容
CBS_OPERATION_CREATE：创建
CBS_OPERATION_ISOLATE：隔离
CBS_OPERATION_MODIFY：修改云硬盘属性
ASP_OPERATION_BIND：关联定期快照策略
ASP_OPERATION_UNBIND：取消关联定期快照策略
        :type Operation: str
        :param DiskId: 操作的云盘ID。
        :type DiskId: str
        :param OperationState: 操作的状态。取值范围：
SUCCESS :表示操作成功 
FAILED :表示操作失败 
PROCESSING :表示操作中。
        :type OperationState: str
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        """
        self.Operator = None
        self.Operation = None
        self.DiskId = None
        self.OperationState = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Operation = params.get("Operation")
        self.DiskId = params.get("DiskId")
        self.OperationState = params.get("OperationState")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Image(AbstractModel):
    """镜像。

    """

    def __init__(self):
        """
        :param ImageId: 镜像实例ID。
        :type ImageId: str
        :param ImageName: 镜像名称。
        :type ImageName: str
        """
        self.ImageId = None
        self.ImageName = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")


class InquiryPriceCreateDisksRequest(AbstractModel):
    """InquiryPriceCreateDisks请求参数结构体

    """

    def __init__(self):
        """
        :param DiskType: 云硬盘类型。取值范围：<br><li>普通云硬盘：CLOUD_BASIC<br><li>高性能云硬盘：CLOUD_PREMIUM<br><li>SSD云硬盘：CLOUD_SSD。
        :type DiskType: str
        :param DiskSize: 云硬盘大小，单位为GB。云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        :param DiskChargeType: 云硬盘计费类型。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费
        :type DiskChargeType: str
        :param DiskChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数指定包年包月云盘的购买时长、是否设置自动续费等属性。<br>创建预付费云盘该参数必传，创建按小时后付费云盘无需传该参数。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param DiskCount: 购买云盘的数量。不填则默认为1。
        :type DiskCount: int
        :param ProjectId: 云盘所属项目ID。
        :type ProjectId: int
        """
        self.DiskType = None
        self.DiskSize = None
        self.DiskChargeType = None
        self.DiskChargePrepaid = None
        self.DiskCount = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.DiskChargeType = params.get("DiskChargeType")
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DiskCount = params.get("DiskCount")
        self.ProjectId = params.get("ProjectId")


class InquiryPriceCreateDisksResponse(AbstractModel):
    """InquiryPriceCreateDisks返回参数结构体

    """

    def __init__(self):
        """
        :param DiskPrice: 描述了新购云盘的价格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = Price()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewDisksRequest(AbstractModel):
    """InquiryPriceRenewDisks请求参数结构体

    """

    def __init__(self):
        """
        :param DiskIds: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskIds: list of str
        :param DiskChargePrepaids: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月云盘的购买时长。如果在该参数中指定CurInstanceDeadline，则会按对齐到子机到期时间来续费。如果是批量续费询价，该参数与Disks参数一一对应，元素数量需保持一致。
        :type DiskChargePrepaids: list of DiskChargePrepaid
        :param NewDeadline: 指定云盘新的到期时间，形式如：2017-12-17 00:00:00。参数`NewDeadline`和`DiskChargePrepaids`是两种指定询价时长的方式，两者必传一个。
        :type NewDeadline: str
        :param ProjectId: 云盘所属项目ID。 如传入则仅用于鉴权。
        :type ProjectId: int
        """
        self.DiskIds = None
        self.DiskChargePrepaids = None
        self.NewDeadline = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        if params.get("DiskChargePrepaids") is not None:
            self.DiskChargePrepaids = []
            for item in params.get("DiskChargePrepaids"):
                obj = DiskChargePrepaid()
                obj._deserialize(item)
                self.DiskChargePrepaids.append(obj)
        self.NewDeadline = params.get("NewDeadline")
        self.ProjectId = params.get("ProjectId")


class InquiryPriceRenewDisksResponse(AbstractModel):
    """InquiryPriceRenewDisks返回参数结构体

    """

    def __init__(self):
        """
        :param DiskPrice: 描述了续费云盘的价格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = PrepayPrice()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResizeDiskRequest(AbstractModel):
    """InquiryPriceResizeDisk请求参数结构体

    """

    def __init__(self):
        """
        :param DiskId: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        :param DiskSize: 云硬盘扩容后的大小，单位为GB，不得小于当前云硬盘大小。云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        :param ProjectId: 云盘所属项目ID。 如传入则仅用于鉴权。
        :type ProjectId: int
        """
        self.DiskId = None
        self.DiskSize = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.ProjectId = params.get("ProjectId")


class InquiryPriceResizeDiskResponse(AbstractModel):
    """InquiryPriceResizeDisk返回参数结构体

    """

    def __init__(self):
        """
        :param DiskPrice: 描述了扩容云盘的价格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = PrepayPrice()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class ModifyAutoSnapshotPolicyAttributeRequest(AbstractModel):
    """ModifyAutoSnapshotPolicyAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyId: 定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param Policy: 定期快照的执行策略。
        :type Policy: list of Policy
        :param AutoSnapshotPolicyName: 要创建的定期快照策略名。不传则默认为“未命名”。最大长度不能超60个字节。
        :type AutoSnapshotPolicyName: str
        :param IsActivated: 是否激活定期快照策略，FALSE表示未激活，TRUE表示激活，默认为TRUE。
        :type IsActivated: bool
        :param IsPermanent: 通过该定期快照策略创建的快照是否永久保留。FALSE表示非永久保留，TRUE表示永久保留，默认为FALSE。
        :type IsPermanent: bool
        :param RetentionDays: 通过该定期快照策略创建的快照保留天数，该参数不可与`IsPermanent`参数冲突，即若定期快照策略设置为永久保留，`RetentionDays`应置0。
        :type RetentionDays: int
        """
        self.AutoSnapshotPolicyId = None
        self.Policy = None
        self.AutoSnapshotPolicyName = None
        self.IsActivated = None
        self.IsPermanent = None
        self.RetentionDays = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self.Policy.append(obj)
        self.AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self.IsActivated = params.get("IsActivated")
        self.IsPermanent = params.get("IsPermanent")
        self.RetentionDays = params.get("RetentionDays")


class ModifyAutoSnapshotPolicyAttributeResponse(AbstractModel):
    """ModifyAutoSnapshotPolicyAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDiskAttributesRequest(AbstractModel):
    """ModifyDiskAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param DiskIds: 一个或多个待操作的云硬盘ID。如果传入多个云盘ID，仅支持所有云盘修改为同一属性。
        :type DiskIds: list of str
        :param ProjectId: 新的云硬盘项目ID，只支持修改弹性云盘的项目ID。通过[DescribeProject](/document/api/378/4400)接口查询可用项目及其ID。
        :type ProjectId: int
        :param DiskName: 新的云硬盘名称。
        :type DiskName: str
        :param Portable: 是否为弹性云盘，FALSE表示非弹性云盘，TRUE表示弹性云盘。仅支持非弹性云盘修改为弹性云盘。
        :type Portable: bool
        :param DeleteWithInstance: 成功挂载到云主机后该云硬盘是否随云主机销毁，TRUE表示随云主机销毁，FALSE表示不随云主机销毁。仅支持按量计费云硬盘数据盘。
        :type DeleteWithInstance: bool
        :param DiskType: 变更云盘类型时，可传入该参数，表示变更的目标类型，取值范围：<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘。<br>当前不支持批量变更类型，即传入DiskType时，DiskIds仅支持传入一块云盘；<br>变更云盘类型时不支持同时变更其他属性。
        :type DiskType: str
        """
        self.DiskIds = None
        self.ProjectId = None
        self.DiskName = None
        self.Portable = None
        self.DeleteWithInstance = None
        self.DiskType = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.ProjectId = params.get("ProjectId")
        self.DiskName = params.get("DiskName")
        self.Portable = params.get("Portable")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.DiskType = params.get("DiskType")


class ModifyDiskAttributesResponse(AbstractModel):
    """ModifyDiskAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDisksRenewFlagRequest(AbstractModel):
    """ModifyDisksRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param DiskIds: 一个或多个待操作的云硬盘ID。
        :type DiskIds: list of str
        :param RenewFlag: 云盘的续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费。
        :type RenewFlag: str
        """
        self.DiskIds = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.RenewFlag = params.get("RenewFlag")


class ModifyDisksRenewFlagResponse(AbstractModel):
    """ModifyDisksRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotAttributeRequest(AbstractModel):
    """ModifySnapshotAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param SnapshotId: 快照ID, 可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :type SnapshotId: str
        :param SnapshotName: 新的快照名称。最长为60个字符。
        :type SnapshotName: str
        :param IsPermanent: 快照的保留时间，FALSE表示非永久保留，TRUE表示永久保留。仅支持将非永久快照修改为永久快照。
        :type IsPermanent: bool
        """
        self.SnapshotId = None
        self.SnapshotName = None
        self.IsPermanent = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.SnapshotName = params.get("SnapshotName")
        self.IsPermanent = params.get("IsPermanent")


class ModifySnapshotAttributeResponse(AbstractModel):
    """ModifySnapshotAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Placement(AbstractModel):
    """描述了实例的抽象位置，包括其所在的可用区，所属的项目，以及所属的独享集群的ID和名字。

    """

    def __init__(self):
        """
        :param Zone: 云硬盘所属的[可用区](/document/product/213/15753#ZoneInfo)。该参数也可以通过调用  [DescribeZones](/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param CdcId: 实例所属的独享集群ID。作为入参时，表示对指定的CdcId独享集群的资源进行操作，可为空。 作为出参时，表示资源所属的独享集群的ID，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        :param CageId: 围笼Id。作为入参时，表示对指定的CageId的资源进行操作，可为空。 作为出参时，表示资源所属围笼ID，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CageId: str
        :param CdcName: 独享集群名字。作为入参时，忽略。作为出参时，表示云硬盘所属的独享集群名，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcName: str
        """
        self.Zone = None
        self.ProjectId = None
        self.CdcId = None
        self.CageId = None
        self.CdcName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.CdcId = params.get("CdcId")
        self.CageId = params.get("CageId")
        self.CdcName = params.get("CdcName")


class Policy(AbstractModel):
    """描述了定期快照的执行策略。可理解为在DayOfWeek指定的那几天中，在Hour指定的小时执行该条定期快照策略。

    """

    def __init__(self):
        """
        :param DayOfWeek: 指定每周从周一到周日需要触发定期快照的日期，取值范围：[0, 6]。0表示周日触发，1-6分别表示周一至周六。
        :type DayOfWeek: list of int non-negative
        :param Hour: 指定定期快照策略的触发时间。单位为小时，取值范围：[0, 23]。00:00 ~ 23:00 共 24 个时间点可选，1表示 01:00，依此类推。
        :type Hour: list of int non-negative
        """
        self.DayOfWeek = None
        self.Hour = None


    def _deserialize(self, params):
        self.DayOfWeek = params.get("DayOfWeek")
        self.Hour = params.get("Hour")


class PrepayPrice(AbstractModel):
    """预付费订单的费用。

    """

    def __init__(self):
        """
        :param OriginalPrice: 预付费云盘或快照预支费用的原价，单位：元。
        :type OriginalPrice: float
        :param DiscountPrice: 预付费云盘或快照预支费用的折扣价，单位：元。
        :type DiscountPrice: float
        """
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")


class Price(AbstractModel):
    """描述预付费或后付费云盘的价格。

    """

    def __init__(self):
        """
        :param OriginalPrice: 预付费云盘预支费用的原价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param DiscountPrice: 预付费云盘预支费用的折扣价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param UnitPrice: 后付费云盘原单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param ChargeUnit: 后付费云盘的计价单元，取值范围：<br><li>HOUR：表示后付费云盘的计价单元是按小时计算。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param UnitPriceDiscount: 后付费云盘折扣单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.UnitPrice = None
        self.ChargeUnit = None
        self.UnitPriceDiscount = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")


class RenewDiskRequest(AbstractModel):
    """RenewDisk请求参数结构体

    """

    def __init__(self):
        """
        :param DiskChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月云盘的续费时长。<br>在云盘与挂载的实例一起续费的场景下，可以指定参数CurInstanceDeadline，此时云盘会按对齐到实例续费后的到期时间来续费。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param DiskId: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        """
        self.DiskChargePrepaid = None
        self.DiskId = None


    def _deserialize(self, params):
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DiskId = params.get("DiskId")


class RenewDiskResponse(AbstractModel):
    """RenewDisk返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResizeDiskRequest(AbstractModel):
    """ResizeDisk请求参数结构体

    """

    def __init__(self):
        """
        :param DiskId: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        :param DiskSize: 云硬盘扩容后的大小，单位为GB，必须大于当前云硬盘大小。云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        """
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")


class ResizeDiskResponse(AbstractModel):
    """ResizeDisk返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Snapshot(AbstractModel):
    """描述了快照的详细信息

    """

    def __init__(self):
        """
        :param SnapshotId: 快照ID。
        :type SnapshotId: str
        :param Placement: 快照所在的位置。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param DiskUsage: 创建此快照的云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :type DiskUsage: str
        :param DiskId: 创建此快照的云硬盘ID。
        :type DiskId: str
        :param DiskSize: 创建此快照的云硬盘大小，单位GB。
        :type DiskSize: int
        :param SnapshotState: 快照的状态。取值范围：<br><li>NORMAL：正常<br><li>CREATING：创建中<br><li>ROLLBACKING：回滚中<br><li>COPYING_FROM_REMOTE：跨地域复制快照拷贝中。
        :type SnapshotState: str
        :param SnapshotName: 快照名称，用户自定义的快照别名。调用[ModifySnapshotAttribute](/document/product/362/15650)可修改此字段。
        :type SnapshotName: str
        :param Percent: 快照创建进度百分比，快照创建成功后此字段恒为100。
        :type Percent: int
        :param CreateTime: 快照的创建时间。
        :type CreateTime: str
        :param DeadlineTime: 快照到期时间。如果快照为永久保留，此字段为空。
        :type DeadlineTime: str
        :param Encrypt: 是否为加密盘创建的快照。取值范围：<br><li>true：该快照为加密盘创建的<br><li>false:非加密盘创建的快照。
        :type Encrypt: bool
        :param IsPermanent: 是否为永久快照。取值范围：<br><li>true：永久快照<br><li>false：非永久快照。
        :type IsPermanent: bool
        :param CopyingToRegions: 快照正在跨地域复制的目的地域，默认取值为[]。
        :type CopyingToRegions: list of str
        :param CopyFromRemote: 是否为跨地域复制的快照。取值范围：<br><li>true：表示为跨地域复制的快照。<br><li>false:本地域的快照。
        :type CopyFromRemote: bool
        :param Images: 快照关联的镜像列表。
        :type Images: list of Image
        :param ImageCount: 快照关联的镜像个数。
        :type ImageCount: int
        """
        self.SnapshotId = None
        self.Placement = None
        self.DiskUsage = None
        self.DiskId = None
        self.DiskSize = None
        self.SnapshotState = None
        self.SnapshotName = None
        self.Percent = None
        self.CreateTime = None
        self.DeadlineTime = None
        self.Encrypt = None
        self.IsPermanent = None
        self.CopyingToRegions = None
        self.CopyFromRemote = None
        self.Images = None
        self.ImageCount = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.DiskUsage = params.get("DiskUsage")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.SnapshotState = params.get("SnapshotState")
        self.SnapshotName = params.get("SnapshotName")
        self.Percent = params.get("Percent")
        self.CreateTime = params.get("CreateTime")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Encrypt = params.get("Encrypt")
        self.IsPermanent = params.get("IsPermanent")
        self.CopyingToRegions = params.get("CopyingToRegions")
        self.CopyFromRemote = params.get("CopyFromRemote")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self.Images.append(obj)
        self.ImageCount = params.get("ImageCount")


class SnapshotOperationLog(AbstractModel):
    """快照操作日志。

    """

    def __init__(self):
        """
        :param Operator: 操作者的UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param Operation: 操作类型。取值范围：
SNAP_OPERATION_DELETE：删除快照
SNAP_OPERATION_ROLLBACK：回滚快照
SNAP_OPERATION_MODIFY：修改快照属性
SNAP_OPERATION_CREATE：创建快照
SNAP_OPERATION_COPY：跨地域复制快照
ASP_OPERATION_CREATE_SNAP：由定期快照策略创建快照
ASP_OPERATION_DELETE_SNAP：由定期快照策略删除快照
        :type Operation: str
        :param SnapshotId: 操作的快照ID。
        :type SnapshotId: str
        :param OperationState: 操作的状态。取值范围：
SUCCESS :表示操作成功 
FAILED :表示操作失败 
PROCESSING :表示操作中。
        :type OperationState: str
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        """
        self.Operator = None
        self.Operation = None
        self.SnapshotId = None
        self.OperationState = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Operation = params.get("Operation")
        self.SnapshotId = params.get("SnapshotId")
        self.OperationState = params.get("OperationState")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class Tag(AbstractModel):
    """标签。

    """

    def __init__(self):
        """
        :param Key: 标签健。
        :type Key: str
        :param Value: 标签值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TerminateDisksRequest(AbstractModel):
    """TerminateDisks请求参数结构体

    """

    def __init__(self):
        """
        :param DiskIds: 需退还的云盘ID列表。
        :type DiskIds: list of str
        """
        self.DiskIds = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")


class TerminateDisksResponse(AbstractModel):
    """TerminateDisks返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    """UnbindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param DiskIds: 要解绑定期快照策略的云盘ID列表。
        :type DiskIds: list of str
        :param AutoSnapshotPolicyId: 要解绑的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        """
        self.DiskIds = None
        self.AutoSnapshotPolicyId = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")


class UnbindAutoSnapshotPolicyResponse(AbstractModel):
    """UnbindAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")