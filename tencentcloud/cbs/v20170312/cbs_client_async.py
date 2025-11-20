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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.cbs.v20170312 import models
from typing import Dict


class CbsClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cbs.tencentcloudapi.com'
    _service = 'cbs'

    async def ApplyDiskBackup(
            self,
            request: models.ApplyDiskBackupRequest,
            opts: Dict = None,
    ) -> models.ApplyDiskBackupResponse:
        """
        本接口（ApplyDiskBackup）用于回滚备份点到原云硬盘。

        * 仅支持回滚到原云硬盘上。对于数据盘备份点，如果您需要复制备份点数据到其它云硬盘上，请先使用[CreateSnapshot](/document/product/362/15648) 将备份点转换为快照，然后使用[CreateDisks](/document/product/362/16312) 接口创建新的弹性云硬盘，将快照数据复制到新购云硬盘上。
        * 用于回滚的备份点必须处于NORMAL状态。备份点状态可以通过[DescribeDiskBackups](/document/product/362/80278)接口查询，见输出参数中BackupState字段解释。
        * 如果是弹性云硬盘，则云硬盘必须处于未挂载状态，云硬盘挂载状态可以通[DescribeDisks](/document/product/362/16315)接口查询，见Attached字段解释；如果是随实例一起购买的非弹性云硬盘，则实例必须处于关机状态，实例状态可以通过[DescribeInstancesStatus](/document/product/213/15738)接口查询。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyDiskBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyDiskBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplySnapshot(
            self,
            request: models.ApplySnapshotRequest,
            opts: Dict = None,
    ) -> models.ApplySnapshotResponse:
        """
        本接口（ApplySnapshot）用于回滚快照到原云硬盘。

        * 仅支持回滚到原云硬盘上。对于数据盘快照，如果您需要复制快照数据到其它云硬盘上，请使用[CreateDisks](/document/product/362/16312)接口创建新的弹性云盘，将快照数据复制到新购云盘上。
        * 用于回滚的快照必须处于NORMAL状态。快照状态可以通过[DescribeSnapshots](/document/product/362/15647)接口查询，见输出参数中SnapshotState字段解释。
        * 如果是弹性云盘，则云盘必须处于未挂载状态，云硬盘挂载状态可以通过[DescribeDisks](/document/product/362/16315)接口查询，见Attached字段解释；如果是随实例一起购买的非弹性云盘，则实例必须处于关机状态，实例状态可以通过[DescribeInstancesStatus](/document/product/213/15738)接口查询。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplySnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplySnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplySnapshotGroup(
            self,
            request: models.ApplySnapshotGroupRequest,
            opts: Dict = None,
    ) -> models.ApplySnapshotGroupResponse:
        """
        本接口（ApplySnapshotGroup）用于回滚快照组，将实例恢复到创建快照组时刻的状态。
        * 1.可选择快照组全部或部分盘进行回滚；
        * 2.如果回滚的盘中包含已挂载的盘，要求这些盘必须挂载在同一实例上，且要求该实例已关机才能回滚；
        * 3.回滚为异步操作，接口返回成功不代表回滚成功，可通过调DescribeSnapshotGroups接口查询快照组的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplySnapshotGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplySnapshotGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachDisks(
            self,
            request: models.AttachDisksRequest,
            opts: Dict = None,
    ) -> models.AttachDisksResponse:
        """
        本接口（AttachDisks）用于挂载云硬盘。

        * 支持批量操作，将多块云盘挂载到同一云主机。如果多个云盘中存在不允许挂载的云盘，则操作不执行，返回特定的错误码。
        * 本接口为异步接口，当挂载云盘的请求成功返回时，表示后台已发起挂载云盘的操作，可通过接口[DescribeDisks](/document/product/362/16315)来查询对应云盘的状态，如果云盘的状态由“ATTACHING”变为“ATTACHED”，则为挂载成功。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindAutoSnapshotPolicy(
            self,
            request: models.BindAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.BindAutoSnapshotPolicyResponse:
        """
        本接口（BindAutoSnapshotPolicy）用于绑定云硬盘到指定的定期快照策略。

        * 每个地域下的定期快照策略配额限制请参考文档[定期快照](/document/product/362/8191)。
        * 当已绑定定期快照策略的云硬盘处于未使用状态（即弹性云盘未挂载或非弹性云盘的主机处于关机状态）将不会创建定期快照。
        """
        
        kwargs = {}
        kwargs["action"] = "BindAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopySnapshotCrossRegions(
            self,
            request: models.CopySnapshotCrossRegionsRequest,
            opts: Dict = None,
    ) -> models.CopySnapshotCrossRegionsResponse:
        """
        本接口（CopySnapshotCrossRegions）用于快照跨地域复制。

        * 本接口为异步接口，当跨地域复制的请求下发成功后会返回一个新的快照ID，此时快照未立即复制到目标地域，可请求目标地域的[DescribeSnapshots](/document/product/362/15647)接口查询新快照的状态，判断是否复制完成。如果快照的状态为“NORMAL”，表示快照复制完成。
        * 本接口实现的快照跨地域复制操作将产生跨地域流量，预计2025年第三季度会针对此功能进行商业化计费；请留意后续站内信公告，避免产生预期外扣费。
        """
        
        kwargs = {}
        kwargs["action"] = "CopySnapshotCrossRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopySnapshotCrossRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoSnapshotPolicy(
            self,
            request: models.CreateAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAutoSnapshotPolicyResponse:
        """
        本接口（CreateAutoSnapshotPolicy）用于创建定期快照策略。

        * 每个地域可创建的定期快照策略数量限制请参考文档[定期快照](/document/product/362/8191)。
        * 每个地域可创建的快照有数量和容量的限制，具体请见腾讯云控制台快照页面提示，如果快照超配额，定期快照创建会失败。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDiskBackup(
            self,
            request: models.CreateDiskBackupRequest,
            opts: Dict = None,
    ) -> models.CreateDiskBackupResponse:
        """
        为云硬盘创建一个备份点。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDiskBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDiskBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDisks(
            self,
            request: models.CreateDisksRequest,
            opts: Dict = None,
    ) -> models.CreateDisksResponse:
        """
        本接口（CreateDisks）用于创建云硬盘。

        * 预付费云盘的购买会预先扣除本次云盘购买所需金额，在调用本接口前请确保账户余额充足。
        * 本接口支持传入数据盘快照来创建云盘，实现将快照数据复制到新购云盘上。
        * 本接口为异步接口，当创建请求下发成功后会返回一个新建的云盘ID列表，此时云盘的创建并未立即完成。可以通过调用[DescribeDisks](/document/product/362/16315)接口根据DiskId查询对应云盘，如果能查到云盘，且状态为'UNATTACHED'或'ATTACHED'，则表示创建成功。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshot(
            self,
            request: models.CreateSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotResponse:
        """
        本接口（CreateSnapshot）用于对指定云盘创建快照。

        * 只有具有快照能力的云硬盘才能创建快照。云硬盘是否具有快照能力可由[DescribeDisks](/document/product/362/16315)接口查询，见SnapshotAbility字段。
        * 可创建快照数量限制见[产品使用限制](https://cloud.tencent.com/doc/product/362/5145)。
        * 当前支持将备份点转化为普通快照，转化之后可能会收取快照使用费用，备份点不保留，其占用的备份点配额也将被释放。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshotGroup(
            self,
            request: models.CreateSnapshotGroupRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotGroupResponse:
        """
        本接口（CreateSnapshotGroup）用于创建快照组。
        * 创建快照组的云硬盘列表必须挂载在同一实例上；
        * 可选择挂载在实例上的全部或部分盘创建快照组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshotGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoSnapshotPolicies(
            self,
            request: models.DeleteAutoSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoSnapshotPoliciesResponse:
        """
        本接口（DeleteAutoSnapshotPolicies）用于删除定期快照策略。

        *  支持批量操作。如果多个定期快照策略存在无法删除的，则操作不执行，以特定错误码返回。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDiskBackups(
            self,
            request: models.DeleteDiskBackupsRequest,
            opts: Dict = None,
    ) -> models.DeleteDiskBackupsResponse:
        """
        批量删除指定的云硬盘备份点。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDiskBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDiskBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshotGroup(
            self,
            request: models.DeleteSnapshotGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotGroupResponse:
        """
        本接口（DeleteSnapshotGroup）用于删除快照组，一次调用仅支持删除一个快照组。
        * 默认会删除快照组内的所有快照；
        * 如果快照组内的快照有关联镜像，则删除失败，所有快照均不会删除；如果需要同时删除快照绑定的镜像，可传入参数DeleteBindImages等于true。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshotGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshots(
            self,
            request: models.DeleteSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotsResponse:
        """
        本接口（DeleteSnapshots）用于删除快照。

        * 快照必须处于NORMAL状态，快照状态可以通过[DescribeSnapshots](/document/product/362/15647)接口查询，见输出参数中SnapshotState字段解释。
        * 支持批量操作。如果多个快照存在无法删除的快照，则操作不执行，以特定的错误码返回。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoSnapshotPolicies(
            self,
            request: models.DescribeAutoSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoSnapshotPoliciesResponse:
        """
        本接口（DescribeAutoSnapshotPolicies）用于查询定期快照策略。

        * 可以根据定期快照策略ID、名称或者状态等信息来查询定期快照策略的详细信息，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的定期快照策略表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskAssociatedAutoSnapshotPolicy(
            self,
            request: models.DescribeDiskAssociatedAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskAssociatedAutoSnapshotPolicyResponse:
        """
        本接口（DescribeDiskAssociatedAutoSnapshotPolicy）用于查询云盘绑定的定期快照策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskAssociatedAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskAssociatedAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskBackups(
            self,
            request: models.DescribeDiskBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskBackupsResponse:
        """
        本接口（DescribeDiskBackups）用于查询备份点的详细信息。

        根据备份点ID、创建备份点的云硬盘ID、创建备份点的云硬盘类型等对结果进行过滤，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器Filter。
        如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的备份点列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskConfigQuota(
            self,
            request: models.DescribeDiskConfigQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskConfigQuotaResponse:
        """
        本接口（DescribeDiskConfigQuota）用于查询云硬盘配额。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskConfigQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskConfigQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskStoragePool(
            self,
            request: models.DescribeDiskStoragePoolRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskStoragePoolResponse:
        """
        本接口（DescribeDiskStoragePool）查询用户的云硬盘独享集群列表。

        * 可以根据独享集群ID(CdcId)、可用区(zone)等信息来查询和过滤云硬盘独享集群详细信息，不同的过滤条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的云硬盘独享集群列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskStoragePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskStoragePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisks(
            self,
            request: models.DescribeDisksRequest,
            opts: Dict = None,
    ) -> models.DescribeDisksResponse:
        """
        本接口（DescribeDisks）用于查询云硬盘列表。

        * 可以根据云硬盘ID、云硬盘类型或者云硬盘状态等信息来查询云硬盘的详细信息，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的云硬盘列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesDiskNum(
            self,
            request: models.DescribeInstancesDiskNumRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesDiskNumResponse:
        """
        本接口（DescribeInstancesDiskNum）用于查询实例已挂载云硬盘数量。

        * 支持批量操作，当传入多个云服务器实例ID，返回结果会分别列出每个云服务器挂载的云硬盘数量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesDiskNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesDiskNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotGroups(
            self,
            request: models.DescribeSnapshotGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotGroupsResponse:
        """
        本接口（DescribeSnapshotGroups）用于查询快照组列表。
        * 可以根据快照组ID、快照组状态、快照组关联的快照ID等来查询快照组列表，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的快照组列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotOverview(
            self,
            request: models.DescribeSnapshotOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotOverviewResponse:
        """
        该接口用于查询用户快照使用概览，包括快照总容量、计费容量等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotSharePermission(
            self,
            request: models.DescribeSnapshotSharePermissionRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotSharePermissionResponse:
        """
        本接口（DescribeSnapshotSharePermission）用于查询快照的分享信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotSharePermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotSharePermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshots(
            self,
            request: models.DescribeSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsResponse:
        """
        本接口（DescribeSnapshots）用于查询快照的详细信息。

        * 根据快照ID、创建快照的云硬盘ID、创建快照的云硬盘类型等对结果进行过滤，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        *  如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的快照列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachDisks(
            self,
            request: models.DetachDisksRequest,
            opts: Dict = None,
    ) -> models.DetachDisksResponse:
        """
        本接口（DetachDisks）用于卸载云硬盘。

        * 支持批量操作，卸载挂载在同一主机上的多块云盘。如果多块云盘中存在不允许卸载的云盘，则操作不执行，返回特定的错误码。
        * 本接口为异步接口，当请求成功返回时，云盘并未立即从主机卸载，可通过接口[DescribeDisks](/document/product/362/16315)来查询对应云盘的状态，如果云盘的状态由“ATTACHED”变为“UNATTACHED”，则为卸载成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSnapOverview(
            self,
            request: models.GetSnapOverviewRequest,
            opts: Dict = None,
    ) -> models.GetSnapOverviewResponse:
        """
        为进一步规范化API命名，该接口决定预下线，新接口命名为：DescribeSnapshotOverview

        获取快照概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetSnapOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSnapOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InitializeDisks(
            self,
            request: models.InitializeDisksRequest,
            opts: Dict = None,
    ) -> models.InitializeDisksResponse:
        """
        重新初始化云硬盘至云硬盘初始创建时的状态。使用云硬盘的重新初始化功能时需要注意以下4点：
        1. 如果云硬盘是由快照创建的，则重新初始化会通过此快照重新回滚此云硬盘，即将云硬盘恢复为与快照一致的状态；
        2. 如果云硬盘不是通过快照创建的，则重新初始化会清空此云硬盘的数据；请在重新初始化云硬盘前检查并备份必要的数据；
        3. 当前仅未挂载的、非共享属性的数据盘云硬盘支持重新初始化；
        4. 当创建此云硬盘的原始快照被删除时，不再支持重新初始化此云硬盘。
        """
        
        kwargs = {}
        kwargs["action"] = "InitializeDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InitializeDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModifyDiskBackupQuota(
            self,
            request: models.InquirePriceModifyDiskBackupQuotaRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyDiskBackupQuotaResponse:
        """
        本接口（InquirePricePriceModifyDiskBackupQuota）用于修改云硬盘备份点配额询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModifyDiskBackupQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyDiskBackupQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModifyDiskExtraPerformance(
            self,
            request: models.InquirePriceModifyDiskExtraPerformanceRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyDiskExtraPerformanceResponse:
        """
        本接口（InquirePriceModifyDiskExtraPerformance）用于调整云硬盘额外性能询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModifyDiskExtraPerformance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyDiskExtraPerformanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateDisks(
            self,
            request: models.InquiryPriceCreateDisksRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateDisksResponse:
        """
        本接口（InquiryPriceCreateDisks）用于创建云硬盘询价。

        * 支持查询创建多块云硬盘的价格，此时返回结果为总价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewDisks(
            self,
            request: models.InquiryPriceRenewDisksRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewDisksResponse:
        """
        本接口（InquiryPriceRenewDisks）用于续费云硬盘询价。

        * 只支持查询预付费模式的弹性云盘续费价格。
        * 支持与挂载实例一起续费的场景，需要在[DiskChargePrepaid](/document/product/362/15669#DiskChargePrepaid)参数中指定CurInstanceDeadline，此时会按对齐到实例续费后的到期时间来续费询价。
        * 支持为多块云盘指定不同的续费时长，此时返回的价格为多块云盘续费的总价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceResizeDisk(
            self,
            request: models.InquiryPriceResizeDiskRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceResizeDiskResponse:
        """
        本接口（InquiryPriceResizeDisk）用于扩容云硬盘询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceResizeDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceResizeDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoSnapshotPolicyAttribute(
            self,
            request: models.ModifyAutoSnapshotPolicyAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoSnapshotPolicyAttributeResponse:
        """
        本接口（ModifyAutoSnapshotPolicyAttribute）用于修改定期快照策略属性。

        * 可通过该接口修改定期快照策略的执行策略、名称、是否激活等属性。
        * 修改保留天数时必须保证不与是否永久保留属性冲突，否则整个操作失败，以特定的错误码返回。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoSnapshotPolicyAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoSnapshotPolicyAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiskAttributes(
            self,
            request: models.ModifyDiskAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyDiskAttributesResponse:
        """
        * 只支持修改弹性云盘的项目ID。随云主机创建的云硬盘项目ID与云主机联动。是否是弹性云盘可以通过[DescribeDisks](/document/product/362/16315)接口查询，见输出参数中Portable字段解释。
        * “云硬盘名称”仅为方便用户自己管理之用，腾讯云并不以此名称作为提交工单或是进行云盘管理操作的依据。
        * 支持批量操作，如果传入多个云盘ID，则所有云盘修改为同一属性。如果存在不允许操作的云盘，则操作不执行，以特定错误码返回。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiskAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiskAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiskBackupQuota(
            self,
            request: models.ModifyDiskBackupQuotaRequest,
            opts: Dict = None,
    ) -> models.ModifyDiskBackupQuotaResponse:
        """
        此接口 (ModifyDiskBackupQuota) 用于修改云硬盘备份点配额。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiskBackupQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiskBackupQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiskExtraPerformance(
            self,
            request: models.ModifyDiskExtraPerformanceRequest,
            opts: Dict = None,
    ) -> models.ModifyDiskExtraPerformanceResponse:
        """
        本接口（ModifyDiskExtraPerformance）用于调整云硬盘额外的性能。

        * 目前仅支持增强型SSD云硬盘(CLOUD_HSSD)和极速型SSD云硬盘（CLOUD_TSSD）。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiskExtraPerformance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiskExtraPerformanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDisksChargeType(
            self,
            request: models.ModifyDisksChargeTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyDisksChargeTypeResponse:
        """
        本接口 (ModifyDisksChargeType) 用于切换云硬盘的计费模式。

        非弹性云硬盘不支持此接口，请通过修改实例计费模式接口将实例连同非弹性云硬盘一起转换。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDisksChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDisksChargeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDisksRenewFlag(
            self,
            request: models.ModifyDisksRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyDisksRenewFlagResponse:
        """
        本接口（ModifyDisksRenewFlag）用于修改云硬盘续费标识，支持批量修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDisksRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDisksRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotAttribute(
            self,
            request: models.ModifySnapshotAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotAttributeResponse:
        """
        本接口（ModifySnapshotAttribute）用于修改指定快照的属性。

        * 本接口支持修改快照名称及到期时间，以及将非永久快照修改为永久快照。
        * “快照名称”仅为方便用户管理之用，腾讯云并不以此名称作为提交工单或是进行快照管理操作的依据。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotsSharePermission(
            self,
            request: models.ModifySnapshotsSharePermissionRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotsSharePermissionResponse:
        """
        本接口（ModifySnapshotsSharePermission）用于修改快照分享信息。

        分享快照后，被分享账户可以通过该快照创建云硬盘。
        * 每个快照最多可分享给50个账户。
        * 分享快照无法更改名称，描述，仅可用于创建云硬盘。
        * 只支持分享到对方账户相同地域。
        * 仅支持分享数据盘快照。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotsSharePermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotsSharePermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDisk(
            self,
            request: models.RenewDiskRequest,
            opts: Dict = None,
    ) -> models.RenewDiskResponse:
        """
        本接口（RenewDisk）用于续费云硬盘。

        * 只支持预付费的云硬盘。云硬盘类型可以通过[DescribeDisks](/document/product/362/16315)接口查询，见输出参数中DiskChargeType字段解释。
        * 支持与挂载实例一起续费的场景，需要在[DiskChargePrepaid](/document/product/362/15669#DiskChargePrepaid)参数中指定CurInstanceDeadline，此时会按对齐到子机续费后的到期时间来续费。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeDisk(
            self,
            request: models.ResizeDiskRequest,
            opts: Dict = None,
    ) -> models.ResizeDiskResponse:
        """
        本接口（ResizeDisk）用于扩容云硬盘。

        * 只支持扩容弹性云盘。云硬盘类型可以通过[DescribeDisks](/document/product/362/16315)接口查询，见输出参数中Portable字段解释。非弹性云硬盘需通过[ResizeInstanceDisks](/document/product/213/15731)接口扩容。
        * 本接口为异步接口，接口成功返回时，云盘并未立即扩容到指定大小，可通过接口[DescribeDisks](/document/product/362/16315)来查询对应云盘的状态，如果云盘的状态为“EXPANDING”，表示正在扩容中。
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDisks(
            self,
            request: models.TerminateDisksRequest,
            opts: Dict = None,
    ) -> models.TerminateDisksResponse:
        """
        本接口（TerminateDisks）用于退还云硬盘。

        * 不再使用的云盘，可通过本接口主动退还。
        * 本接口支持退还预付费云盘和按小时后付费云盘。按小时后付费云盘可直接退还，预付费云盘需符合退还规则。
        * 支持批量操作，每次请求批量云硬盘的上限为100。如果批量云盘存在不允许操作的，请求会以特定错误码返回。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindAutoSnapshotPolicy(
            self,
            request: models.UnbindAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.UnbindAutoSnapshotPolicyResponse:
        """
        本接口（UnbindAutoSnapshotPolicy）用于解除云硬盘绑定的定期快照策略。

        * 支持批量操作，可一次解除多个云盘与同一定期快照策略的绑定。
        * 如果传入的云盘未绑定到当前定期快照策略，接口将自动跳过，仅解绑与当前定期快照策略绑定的云盘。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)