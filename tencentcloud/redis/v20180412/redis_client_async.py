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
from tencentcloud.redis.v20180412 import models
from typing import Dict


class RedisClient(AbstractClient):
    _apiVersion = '2018-04-12'
    _endpoint = 'redis.tencentcloudapi.com'
    _service = 'redis'

    async def AddReplicationInstance(
            self,
            request: models.AddReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.AddReplicationInstanceResponse:
        """
        本接口（AddReplicationInstance）用于为全球复制组添加实例成员。
        """
        
        kwargs = {}
        kwargs["action"] = "AddReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateWanAddress(
            self,
            request: models.AllocateWanAddressRequest,
            opts: Dict = None,
    ) -> models.AllocateWanAddressResponse:
        """
        本接口（AllocateWanAddress）用于开通实例外网访问。
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateWanAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateWanAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyParamsTemplate(
            self,
            request: models.ApplyParamsTemplateRequest,
            opts: Dict = None,
    ) -> models.ApplyParamsTemplateResponse:
        """
        本接口（ApplyParamsTemplate）用于应用参数模板到实例。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyParamsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyParamsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        本接口 (AssociateSecurityGroups) 用于将一个安全组绑定于一个或多个数据库实例。创建实例时，未配置安全组，建议通过该接口，绑定安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeInstanceRole(
            self,
            request: models.ChangeInstanceRoleRequest,
            opts: Dict = None,
    ) -> models.ChangeInstanceRoleResponse:
        """
        本接口（ChangeInstanceRole）用于更换复制组内实例的角色。
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeInstanceRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeInstanceRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeMasterInstance(
            self,
            request: models.ChangeMasterInstanceRequest,
            opts: Dict = None,
    ) -> models.ChangeMasterInstanceResponse:
        """
        该接口（ChangeMasterInstance）用于将复制组内只读实例设置为主实例。
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeMasterInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeMasterInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeReplicaToMaster(
            self,
            request: models.ChangeReplicaToMasterRequest,
            opts: Dict = None,
    ) -> models.ChangeReplicaToMasterResponse:
        """
        本接口（ChangeReplicaToMaster）适用于实例副本组提主或副本提主。
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeReplicaToMaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeReplicaToMasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CleanUpInstance(
            self,
            request: models.CleanUpInstanceRequest,
            opts: Dict = None,
    ) -> models.CleanUpInstanceResponse:
        """
        本接口（CleanUpInstance）用于立即下线回收站的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CleanUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CleanUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearInstance(
            self,
            request: models.ClearInstanceRequest,
            opts: Dict = None,
    ) -> models.ClearInstanceResponse:
        """
        本接口（ClearInstance）用于清空实例数据。
        """
        
        kwargs = {}
        kwargs["action"] = "ClearInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneInstances(
            self,
            request: models.CloneInstancesRequest,
            opts: Dict = None,
    ) -> models.CloneInstancesResponse:
        """
        本接口（CloneInstances）用于基于当前实例的备份文件克隆一个完整的新实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CloneInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseSSL(
            self,
            request: models.CloseSSLRequest,
            opts: Dict = None,
    ) -> models.CloseSSLResponse:
        """
        本接口（CloseSSL）用于关闭SSL加密认证。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceAccount(
            self,
            request: models.CreateInstanceAccountRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceAccountResponse:
        """
        本接口（CreateInstanceAccount）用于自定义访问实例的账号。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstances(
            self,
            request: models.CreateInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateInstancesResponse:
        """
        本接口（CreateInstances）用于创建 Redis 实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateParamTemplate(
            self,
            request: models.CreateParamTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateParamTemplateResponse:
        """
        该接口（CreateParamTemplate）用于创建参数模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReplicationGroup(
            self,
            request: models.CreateReplicationGroupRequest,
            opts: Dict = None,
    ) -> models.CreateReplicationGroupResponse:
        """
        本接口（CreateReplicationGroup）用于创建复制组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReplicationGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReplicationGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstanceAccount(
            self,
            request: models.DeleteInstanceAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceAccountResponse:
        """
        本接口（DeleteInstanceAccount）用于删除实例子账号。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstanceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParamTemplate(
            self,
            request: models.DeleteParamTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParamTemplateResponse:
        """
        本接口（DeleteParamTemplate）用于删除参数模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReplicationInstance(
            self,
            request: models.DeleteReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteReplicationInstanceResponse:
        """
        本接口（DeleteReplicationInstance）移除复制组成员。注：该接口下线中，请使用 [RemoveReplicationInstance](https://cloud.tencent.com/document/product/239/90099)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoBackupConfig(
            self,
            request: models.DescribeAutoBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoBackupConfigResponse:
        """
        本接口（DescribeAutoBackupConfig）用于获取自动备份配置规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDetail(
            self,
            request: models.DescribeBackupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDetailResponse:
        """
        本接口（DescribeBackupDetail）用于查询实例的备份信息详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadRestriction(
            self,
            request: models.DescribeBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadRestrictionResponse:
        """
        本接口（DescribeBackupDownloadRestriction）用于查询当前地域数据库备份文件的下载地址。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupUrl(
            self,
            request: models.DescribeBackupUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupUrlResponse:
        """
        本接口（DescribeBackupUrl）用于查询备份 Rdb 文件的下载地址。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthRange(
            self,
            request: models.DescribeBandwidthRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthRangeResponse:
        """
        本接口（DescribeBandwidthRange）用于查询实例带宽信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCommonDBInstances(
            self,
            request: models.DescribeCommonDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeCommonDBInstancesResponse:
        """
        本接口（DescribeCommonDBInstances）用于查询Redis实例列表信息。当前该接口已废弃。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCommonDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCommonDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        本接口（DescribeDBSecurityGroups）用于查询实例的安全组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalReplicationArea(
            self,
            request: models.DescribeGlobalReplicationAreaRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalReplicationAreaResponse:
        """
        本接口（DescribeGlobalReplicationArea）用于查询全球复制支持地域信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalReplicationArea"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalReplicationAreaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceAccount(
            self,
            request: models.DescribeInstanceAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceAccountResponse:
        """
        本接口（DescribeInstanceAccount）用于查看实例账号信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceBackups(
            self,
            request: models.DescribeInstanceBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceBackupsResponse:
        """
        本接口（DescribeInstanceBackups）用于查询实例备份列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDTSInfo(
            self,
            request: models.DescribeInstanceDTSInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDTSInfoResponse:
        """
        本接口（DescribeInstanceDTSInfo）用于查询实例 DTS 信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDTSInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDTSInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDealDetail(
            self,
            request: models.DescribeInstanceDealDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDealDetailResponse:
        """
        本接口（DescribeInstanceDealDetail）用于查询订单信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDealDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDealDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceEvents(
            self,
            request: models.DescribeInstanceEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceEventsResponse:
        """
        本接口（DescribeInstanceEvents）用于查询 Redis 实例事件信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogDelivery(
            self,
            request: models.DescribeInstanceLogDeliveryRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogDeliveryResponse:
        """
        本接口（DescribeInstanceLogDelivery）用于查询实例的日志投递配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorBigKey(
            self,
            request: models.DescribeInstanceMonitorBigKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorBigKeyResponse:
        """
        腾讯云数据库 Redis 已经于2022年10月31日下线查询实例大 Key 接口。具体公告，请参见[查询实例大 Key 接口下线公告](https://cloud.tencent.com/document/product/239/81005)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorBigKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorBigKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorBigKeySizeDist(
            self,
            request: models.DescribeInstanceMonitorBigKeySizeDistRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorBigKeySizeDistResponse:
        """
        腾讯云数据库 Redis 已经于2022年10月31日下线查询实例大 Key 接口。具体公告，请参见 [查询实例大 Key 接口下线公告](https://cloud.tencent.com/document/product/239/81005)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorBigKeySizeDist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorBigKeySizeDistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorBigKeyTypeDist(
            self,
            request: models.DescribeInstanceMonitorBigKeyTypeDistRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorBigKeyTypeDistResponse:
        """
        腾讯云数据库 Redis 已经于2022年10月31日下线查询实例大 Key 接口。具体公告，请参见 [查询实例大 Key 接口下线公告](https://cloud.tencent.com/document/product/239/81005)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorBigKeyTypeDist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorBigKeyTypeDistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorHotKey(
            self,
            request: models.DescribeInstanceMonitorHotKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorHotKeyResponse:
        """
        本接口（DescribeInstanceMonitorHotKey）用于查询实例热Key。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorHotKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorHotKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorSIP(
            self,
            request: models.DescribeInstanceMonitorSIPRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorSIPResponse:
        """
        该接口已下线，请使用数据库智能管家 DBbrain 接口 [DescribeProxyProcessStatistics](https://cloud.tencent.com/document/product/1130/84544) 获取实例访问来源。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorSIP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorSIPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorTookDist(
            self,
            request: models.DescribeInstanceMonitorTookDistRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorTookDistResponse:
        """
        本接口（DescribeInstanceMonitorTookDist）用于查询实例访问的耗时分布。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorTookDist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorTookDistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorTopNCmd(
            self,
            request: models.DescribeInstanceMonitorTopNCmdRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorTopNCmdResponse:
        """
        本接口（DescribeInstanceMonitorTopNCmd）用于查询实例访问命令。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorTopNCmd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorTopNCmdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorTopNCmdTook(
            self,
            request: models.DescribeInstanceMonitorTopNCmdTookRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorTopNCmdTookResponse:
        """
        本接口（DescribeInstanceMonitorTopNCmdTook）用于查询实例 CPU 耗时。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorTopNCmdTook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorTopNCmdTookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodeInfo(
            self,
            request: models.DescribeInstanceNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodeInfoResponse:
        """
        本接口（DescribeInstanceNodeInfo）用于查询实例节点信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParamRecords(
            self,
            request: models.DescribeInstanceParamRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamRecordsResponse:
        """
        本接口（DescribeInstanceParamRecords）用于查询参数修改历史列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParamRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParams(
            self,
            request: models.DescribeInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamsResponse:
        """
        本接口（DescribeInstanceParams）用于查询实例参数列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSecurityGroup(
            self,
            request: models.DescribeInstanceSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSecurityGroupResponse:
        """
        本接口（DescribeInstanceSecurityGroup）用于查询实例安全组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceShards(
            self,
            request: models.DescribeInstanceShardsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceShardsResponse:
        """
        本接口（DescribeInstanceShards）用于获取集群架构实例的分片信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceShards"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceShardsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSpecBandwidth(
            self,
            request: models.DescribeInstanceSpecBandwidthRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSpecBandwidthResponse:
        """
        本接口（DescribeInstanceSpecBandwidth）用于查询或计算带宽规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSpecBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSpecBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSupportFeature(
            self,
            request: models.DescribeInstanceSupportFeatureRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSupportFeatureResponse:
        """
        本接口（DescribeInstanceSupportFeature）用于查询实例支持的功能特性。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSupportFeature"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSupportFeatureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceZoneInfo(
            self,
            request: models.DescribeInstanceZoneInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceZoneInfoResponse:
        """
        本接口（DescribeInstanceZoneInfo）用于查询 Redis 节点详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceZoneInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceZoneInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        本接口（DescribeInstances）用于查询Redis实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintenanceWindow(
            self,
            request: models.DescribeMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintenanceWindowResponse:
        """
        本接口（DescribeMaintenanceWindow）用于查询实例维护时间窗。在实例需要进行版本升级或者架构升级的时候，会在维护时间窗时间内进行切换
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplateInfo(
            self,
            request: models.DescribeParamTemplateInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplateInfoResponse:
        """
        本接口（DescribeParamTemplateInfo）用于查询参数模板详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplates(
            self,
            request: models.DescribeParamTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplatesResponse:
        """
        本接口（DescribeParamTemplates）用于查询参数模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductInfo(
            self,
            request: models.DescribeProductInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProductInfoResponse:
        """
        本接口（DescribeProductInfo）用于查询全地域 Redis 的售卖规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroup(
            self,
            request: models.DescribeProjectSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupResponse:
        """
        本接口（DescribeProjectSecurityGroup）用于查询项目安全组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        本接口（DescribeProjectSecurityGroups）用于查询项目的安全组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySlowLog(
            self,
            request: models.DescribeProxySlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySlowLogResponse:
        """
        本接口（DescribeProxySlowLog）用于查询代理慢查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisClusterOverview(
            self,
            request: models.DescribeRedisClusterOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisClusterOverviewResponse:
        """
        本接口（DescribeRedisClusterOverview）用于查询 Redis 独享集群概览信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisClusterOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisClusterOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisClusters(
            self,
            request: models.DescribeRedisClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisClustersResponse:
        """
        本接口（DescribeRedisClusters）用于查询Redis独享集群列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationGroup(
            self,
            request: models.DescribeReplicationGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationGroupResponse:
        """
        本接口（DescribeReplicationGroup）用于查询复制组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationGroupInstance(
            self,
            request: models.DescribeReplicationGroupInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationGroupInstanceResponse:
        """
        本接口（DescribeReplicationGroupInstance）用于查询复制组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationGroupInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationGroupInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSSLStatus(
            self,
            request: models.DescribeSSLStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSSLStatusResponse:
        """
        本接口（DescribeSSLStatus）用于查询实例 SSL 认证相关信息，包括开启状态、配置状态、证书地址等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecondLevelBackupInfo(
            self,
            request: models.DescribeSecondLevelBackupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecondLevelBackupInfoResponse:
        """
        本接口（DescribeSecondLevelBackupInfo）用于查询实例秒级备份信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecondLevelBackupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecondLevelBackupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLog(
            self,
            request: models.DescribeSlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogResponse:
        """
        本接口（DescribeSlowLog）查询实例慢查询记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskInfo(
            self,
            request: models.DescribeTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskInfoResponse:
        """
        本接口（DescribeTaskInfo）用于获取指定任务的执行情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskList(
            self,
            request: models.DescribeTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskListResponse:
        """
        本接口（DescribeTaskList）用于查询指定实例的任务列表信息。

        - 可查询近30天内任务列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTendisSlowLog(
            self,
            request: models.DescribeTendisSlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeTendisSlowLogResponse:
        """
        本接口（DescribeTendisSlowLog）用于查询 Tendis 实例慢查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTendisSlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTendisSlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPostpaidInstance(
            self,
            request: models.DestroyPostpaidInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyPostpaidInstanceResponse:
        """
        本接口（DestroyPostpaidInstance）用于销毁按量计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPostpaidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPostpaidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPrepaidInstance(
            self,
            request: models.DestroyPrepaidInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyPrepaidInstanceResponse:
        """
        本接口（DestroyPrepaidInstance）用于退还包年包月计费的 Redis 实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPrepaidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPrepaidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableReplicaReadonly(
            self,
            request: models.DisableReplicaReadonlyRequest,
            opts: Dict = None,
    ) -> models.DisableReplicaReadonlyResponse:
        """
        本接口（DisableReplicaReadonly）用于禁用读写分离功能。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableReplicaReadonly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableReplicaReadonlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        本接口（DisassociateSecurityGroups）用于安全组批量解绑实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableReplicaReadonly(
            self,
            request: models.EnableReplicaReadonlyRequest,
            opts: Dict = None,
    ) -> models.EnableReplicaReadonlyResponse:
        """
        本接口（EnableReplicaReadonly）用于启用读写分离功能。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableReplicaReadonly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableReplicaReadonlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateInstance(
            self,
            request: models.InquiryPriceCreateInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateInstanceResponse:
        """
        本接口（InquiryPriceCreateInstance）用于查询新购实例价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewInstance(
            self,
            request: models.InquiryPriceRenewInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewInstanceResponse:
        """
        本接口（InquiryPriceRenewInstance）用于查询包年包月计费实例的续费价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceUpgradeInstance(
            self,
            request: models.InquiryPriceUpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceUpgradeInstanceResponse:
        """
        本接口（InquiryPriceUpgradeInstance）用于查询实例扩容价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillMasterGroup(
            self,
            request: models.KillMasterGroupRequest,
            opts: Dict = None,
    ) -> models.KillMasterGroupResponse:
        """
        本接口（KillMasterGroup）用于模拟故障。
        """
        
        kwargs = {}
        kwargs["action"] = "KillMasterGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillMasterGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManualBackupInstance(
            self,
            request: models.ManualBackupInstanceRequest,
            opts: Dict = None,
    ) -> models.ManualBackupInstanceResponse:
        """
        本接口（ManualBackupInstance）用于手动备份Redis实例。
        """
        
        kwargs = {}
        kwargs["action"] = "ManualBackupInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManualBackupInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModfiyInstancePassword(
            self,
            request: models.ModfiyInstancePasswordRequest,
            opts: Dict = None,
    ) -> models.ModfiyInstancePasswordResponse:
        """
        本接口（ModfiyInstancePassword）用于修改实例访问密码。鉴于该接口名存在拼写错误，现已更正为（[ModifyInstancePassword](https://cloud.tencent.com/document/product/239/111555)）接口，推荐使用更正后的接口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModfiyInstancePassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModfiyInstancePasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoBackupConfig(
            self,
            request: models.ModifyAutoBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoBackupConfigResponse:
        """
        本接口（ModifyAutoBackupConfig）用于设置自动备份的配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupDownloadRestriction(
            self,
            request: models.ModifyBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadRestrictionResponse:
        """
        本接口（ModifyBackupDownloadRestriction）用于修改备份文件下载的网络信息与地址。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConnectionConfig(
            self,
            request: models.ModifyConnectionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyConnectionConfigResponse:
        """
        本接口（ModifyConnectionConfig）用于修改实例的连接配置，包括带宽和最大连接数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConnectionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConnectionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        本接口（ModifyDBInstanceSecurityGroups）用于对实例原有的安全组列表进行修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        本接口（ModifyInstance）用于修改实例相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceAccount(
            self,
            request: models.ModifyInstanceAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceAccountResponse:
        """
        本接口（ModifyInstanceAccount）用于修改实例账号。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceAvailabilityZones(
            self,
            request: models.ModifyInstanceAvailabilityZonesRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceAvailabilityZonesResponse:
        """
        本接口（ModifyInstanceAvailabilityZones）用于变更实例可用区
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceAvailabilityZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceAvailabilityZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceBackupMode(
            self,
            request: models.ModifyInstanceBackupModeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceBackupModeResponse:
        """
        本接口（ModifyInstanceBackupMode）用于修改实例的备份模式。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceBackupMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceBackupModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceEvent(
            self,
            request: models.ModifyInstanceEventRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceEventResponse:
        """
        本接口（ModifyInstanceEvent）用于修改实例的运维事件的执行计划。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceLogDelivery(
            self,
            request: models.ModifyInstanceLogDeliveryRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceLogDeliveryResponse:
        """
        本接口（ModifyInstanceLogDelivery）用于开启或关闭投递实例日志到CLS。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceLogDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceLogDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParams(
            self,
            request: models.ModifyInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamsResponse:
        """
        本接口（ModifyInstanceParams）用于修改 Redis 实例的参数配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancePassword(
            self,
            request: models.ModifyInstancePasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancePasswordResponse:
        """
        本接口（ModifyInstancePassword）用于修改实例访问密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancePassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancePasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceReadOnly(
            self,
            request: models.ModifyInstanceReadOnlyRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceReadOnlyResponse:
        """
        本接口（ModifyInstanceReadOnly）用于设置实例输入模式。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceReadOnly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceReadOnlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintenanceWindow(
            self,
            request: models.ModifyMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintenanceWindowResponse:
        """
        本接口（ModifyMaintenanceWindow）用于修改实例维护时间窗时间，需要进行版本升级或者架构升级的实例，会在维护时间窗内进行时间切换。注意：已经发起版本升级或者架构升级的实例，无法修改维护时间窗。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkConfig(
            self,
            request: models.ModifyNetworkConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkConfigResponse:
        """
        本接口（ModifyNetworkConfig）用于修改实例网络配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyParamTemplate(
            self,
            request: models.ModifyParamTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyParamTemplateResponse:
        """
        本接口（ModifyParamTemplate）用于修改参数模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReplicationGroup(
            self,
            request: models.ModifyReplicationGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyReplicationGroupResponse:
        """
        本接口（ModifyReplicationGroup）用于修改复制组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReplicationGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReplicationGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenSSL(
            self,
            request: models.OpenSSLRequest,
            opts: Dict = None,
    ) -> models.OpenSSLResponse:
        """
        本接口（OpenSSL）用于开启 SSL 加密认证功能。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseWanAddress(
            self,
            request: models.ReleaseWanAddressRequest,
            opts: Dict = None,
    ) -> models.ReleaseWanAddressResponse:
        """
        本接口（ReleaseWanAddress）用于关闭外网访问。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseWanAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseWanAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveReplicationGroup(
            self,
            request: models.RemoveReplicationGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveReplicationGroupResponse:
        """
        本接口（RemoveReplicationGroup）用于删除复制组。
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveReplicationGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveReplicationGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveReplicationInstance(
            self,
            request: models.RemoveReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.RemoveReplicationInstanceResponse:
        """
        本接口（RemoveReplicationInstance）用于移除复制组中的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstance(
            self,
            request: models.RenewInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewInstanceResponse:
        """
        本接口（RenewInstance）可用于为实例续费。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetPassword(
            self,
            request: models.ResetPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetPasswordResponse:
        """
        本接口（ResetPassword）用于重置实例访问密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreInstance(
            self,
            request: models.RestoreInstanceRequest,
            opts: Dict = None,
    ) -> models.RestoreInstanceResponse:
        """
        本接口（RestoreInstance）用于恢复实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartupInstance(
            self,
            request: models.StartupInstanceRequest,
            opts: Dict = None,
    ) -> models.StartupInstanceResponse:
        """
        本接口（StartupInstance）用于实例解隔离。
        """
        
        kwargs = {}
        kwargs["action"] = "StartupInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartupInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchAccessNewInstance(
            self,
            request: models.SwitchAccessNewInstanceRequest,
            opts: Dict = None,
    ) -> models.SwitchAccessNewInstanceResponse:
        """
        本接口（SwitchAccessNewInstance）针对处于时间窗口中待切换操作的实例，用户可主动发起该操作。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchAccessNewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchAccessNewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchInstanceVip(
            self,
            request: models.SwitchInstanceVipRequest,
            opts: Dict = None,
    ) -> models.SwitchInstanceVipResponse:
        """
        在通过 DTS 支持跨可用区灾备的场景中，通过该接口（SwitchInstanceVip）交换实例 VIP 完成实例灾备切换。交换 VIP 后目标实例可写，源和目标实例VIP互换，同时源与目标实例间 DTS 同步任务断开。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchInstanceVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchInstanceVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchProxy(
            self,
            request: models.SwitchProxyRequest,
            opts: Dict = None,
    ) -> models.SwitchProxyResponse:
        """
        本接口（SwitchProxy）为 Proxy 模拟故障接口。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        本接口（UpgradeInstance）用于变更实例的配置规格。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstanceVersion(
            self,
            request: models.UpgradeInstanceVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceVersionResponse:
        """
        本接口（UpgradeInstanceVersion）用于将当前实例升级到更高版本，或者将当前标准架构升级至集群架构。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstanceVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeProxyVersion(
            self,
            request: models.UpgradeProxyVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeProxyVersionResponse:
        """
        本接口（UpgradeProxyVersion）用于升级实例 Proxy 版本。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeProxyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeProxyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeSmallVersion(
            self,
            request: models.UpgradeSmallVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeSmallVersionResponse:
        """
        本接口（UpgradeSmallVersion）用于实例小版本升级。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeSmallVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeSmallVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeVersionToMultiAvailabilityZones(
            self,
            request: models.UpgradeVersionToMultiAvailabilityZonesRequest,
            opts: Dict = None,
    ) -> models.UpgradeVersionToMultiAvailabilityZonesResponse:
        """
        本接口（UpgradeVersionToMultiAvailabilityZones）用于升级实例支持多AZ。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeVersionToMultiAvailabilityZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeVersionToMultiAvailabilityZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)