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
from tencentcloud.sqlserver.v20180328 import models
from typing import Dict


class SqlserverClient(AbstractClient):
    _apiVersion = '2018-03-28'
    _endpoint = 'sqlserver.tencentcloudapi.com'
    _service = 'sqlserver'

    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        本接口(AssociateSecurityGroups)用于安全组批量绑定实例。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BalanceReadOnlyGroup(
            self,
            request: models.BalanceReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.BalanceReadOnlyGroupResponse:
        """
        本接口（BalanceReadOnlyGroup）用于根据预定义的权重平衡每个只读实例的路由权重。预定义权重可根据接口DescribeReadOnlyGroupAutoWeight查询。
        """
        
        kwargs = {}
        kwargs["action"] = "BalanceReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BalanceReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneDB(
            self,
            request: models.CloneDBRequest,
            opts: Dict = None,
    ) -> models.CloneDBResponse:
        """
        本接口（CloneDB）用于克隆数据库，只支持克隆到本实例，克隆时必须指定新库名称。
        """
        
        kwargs = {}
        kwargs["action"] = "CloneDB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneDBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseInterCommunication(
            self,
            request: models.CloseInterCommunicationRequest,
            opts: Dict = None,
    ) -> models.CloseInterCommunicationResponse:
        """
        本接口（CloseInterCommunication）用于关闭实例互通。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseInterCommunication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseInterCommunicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteExpansion(
            self,
            request: models.CompleteExpansionRequest,
            opts: Dict = None,
    ) -> models.CompleteExpansionResponse:
        """
        本接口（CompleteExpansion）在实例发起扩容后，实例状态处于“升级待切换”时，可立即完成实例升级切换操作，无需等待可维护时间窗。本接口需要在实例低峰时调用，在完全切换成功前，存在部分库不可访问的风险。
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteExpansion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteExpansionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteMigration(
            self,
            request: models.CompleteMigrationRequest,
            opts: Dict = None,
    ) -> models.CompleteMigrationResponse:
        """
        本接口（CompleteMigration）作用是完成一个迁移任务
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccount(
            self,
            request: models.CreateAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAccountResponse:
        """
        本接口（CreateAccount）用于创建实例账号
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackup(
            self,
            request: models.CreateBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupResponse:
        """
        本接口(CreateBackup)用于创建备份。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupMigration(
            self,
            request: models.CreateBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.CreateBackupMigrationResponse:
        """
        本接口（CreateBackupMigration）用于创建备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBasicDBInstances(
            self,
            request: models.CreateBasicDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateBasicDBInstancesResponse:
        """
        本接口（CreateBasicDBInstances）用于创建基础版实例 (云盘)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBasicDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBasicDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBusinessDBInstances(
            self,
            request: models.CreateBusinessDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateBusinessDBInstancesResponse:
        """
        本接口（CreateBusinessDBInstances）用于创建商业智能服务实例 (云盘)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBusinessDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBusinessDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBusinessIntelligenceFile(
            self,
            request: models.CreateBusinessIntelligenceFileRequest,
            opts: Dict = None,
    ) -> models.CreateBusinessIntelligenceFileResponse:
        """
        本接口（CreateBusinessIntelligenceFile）用于添加商业智能服务文件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBusinessIntelligenceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBusinessIntelligenceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudDBInstances(
            self,
            request: models.CreateCloudDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateCloudDBInstancesResponse:
        """
        本接口（CreateCloudDBInstances）用于创建高可用实例 (云盘)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudReadOnlyDBInstances(
            self,
            request: models.CreateCloudReadOnlyDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateCloudReadOnlyDBInstancesResponse:
        """
        本接口（CreateCloudReadOnlyDBInstances）用于创建只读实例 (云盘)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudReadOnlyDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudReadOnlyDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDB(
            self,
            request: models.CreateDBRequest,
            opts: Dict = None,
    ) -> models.CreateDBResponse:
        """
        本接口（CreateDB）用于创建数据库。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstances(
            self,
            request: models.CreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstancesResponse:
        """
        本接口（CreateDBInstances）用于创建高可用实例 (本地盘)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIncrementalMigration(
            self,
            request: models.CreateIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.CreateIncrementalMigrationResponse:
        """
        本接口（CreateIncrementalMigration）用于创建增量备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigration(
            self,
            request: models.CreateMigrationRequest,
            opts: Dict = None,
    ) -> models.CreateMigrationResponse:
        """
        本接口（CreateMigration）作用是创建一个迁移任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePublishSubscribe(
            self,
            request: models.CreatePublishSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreatePublishSubscribeResponse:
        """
        本接口（CreatePublishSubscribe）用于创建两个数据库之间的发布订阅关系。作为订阅者，不能再充当发布者，作为发布者可以有多个订阅者实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePublishSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePublishSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReadOnlyDBInstances(
            self,
            request: models.CreateReadOnlyDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateReadOnlyDBInstancesResponse:
        """
        本接口（CreateReadOnlyDBInstances）用于创建只读实例 (本地盘)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReadOnlyDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReadOnlyDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CutXEvents(
            self,
            request: models.CutXEventsRequest,
            opts: Dict = None,
    ) -> models.CutXEventsResponse:
        """
        本接口（CutXEvents）用于手动切割阻塞日志和死锁日志。
        """
        
        kwargs = {}
        kwargs["action"] = "CutXEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CutXEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccount(
            self,
            request: models.DeleteAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountResponse:
        """
        本接口（DeleteAccount）用于删除实例账号。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupMigration(
            self,
            request: models.DeleteBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupMigrationResponse:
        """
        本接口（DeleteBackupMigration）用于删除备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBusinessIntelligenceFile(
            self,
            request: models.DeleteBusinessIntelligenceFileRequest,
            opts: Dict = None,
    ) -> models.DeleteBusinessIntelligenceFileResponse:
        """
        本接口（DeleteBusinessIntelligenceFile）用于删除商业智能文件。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBusinessIntelligenceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBusinessIntelligenceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDB(
            self,
            request: models.DeleteDBRequest,
            opts: Dict = None,
    ) -> models.DeleteDBResponse:
        """
        本接口(DeleteDB)用于删除数据库。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBInstance(
            self,
            request: models.DeleteDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteDBInstanceResponse:
        """
        本接口（DeleteDBInstance）用于释放回收站中的SQL server实例(立即下线)。释放后的实例将保存一段时间后物理销毁。其发布订阅将自动解除，其ro副本将自动释放。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIncrementalMigration(
            self,
            request: models.DeleteIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.DeleteIncrementalMigrationResponse:
        """
        本接口（DeleteIncrementalMigration）用于删除增量备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMigration(
            self,
            request: models.DeleteMigrationRequest,
            opts: Dict = None,
    ) -> models.DeleteMigrationResponse:
        """
        本接口（DeleteMigration）用于删除迁移任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePublishSubscribe(
            self,
            request: models.DeletePublishSubscribeRequest,
            opts: Dict = None,
    ) -> models.DeletePublishSubscribeResponse:
        """
        本接口（DeletePublishSubscribe）用于删除两个数据库间的发布订阅关系。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePublishSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePublishSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRestoreTask(
            self,
            request: models.DeleteRestoreTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRestoreTaskResponse:
        """
        本接口(DeleteRestoreTask)用于删除回档任务记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRestoreTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRestoreTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivilegeByDB(
            self,
            request: models.DescribeAccountPrivilegeByDBRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegeByDBResponse:
        """
        本接口(DescribeAccountPrivilegeByDB)用于查询数据库关联的账号和权限信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountPrivilegeByDB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountPrivilegeByDBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        本接口（DescribeAccounts）用于拉取实例账户列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupByFlowId(
            self,
            request: models.DescribeBackupByFlowIdRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupByFlowIdResponse:
        """
        本接口(DescribeBackupByFlowId)用于通过备份创建流程的ID查询创建的备份详情，流程ID可从接口CreateBackup中获得。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupByFlowId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupByFlowIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupCommand(
            self,
            request: models.DescribeBackupCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupCommandResponse:
        """
        本接口（DescribeBackupCommand）用于查询以规范的格式创建备份的命令。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupFiles(
            self,
            request: models.DescribeBackupFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupFilesResponse:
        """
        本接口（DescribeBackupFiles）用于查询单库备份明细。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupMigration(
            self,
            request: models.DescribeBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupMigrationResponse:
        """
        本接口（DescribeBackupMigration）用于创建增量备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupMonitor(
            self,
            request: models.DescribeBackupMonitorRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupMonitorResponse:
        """
        本接口(DescribeBackupMonitor)用于查询备份空间使用详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupStatistical(
            self,
            request: models.DescribeBackupStatisticalRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupStatisticalResponse:
        """
        本接口(DescribeBackupStatistical)用于查询备份实时统计列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupStatistical"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupStatisticalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupSummary(
            self,
            request: models.DescribeBackupSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupSummaryResponse:
        """
        本接口(DescribeBackupSummary)用于查询数据库备份概览信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupUploadSize(
            self,
            request: models.DescribeBackupUploadSizeRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupUploadSizeResponse:
        """
        本接口（DescribeBackupUploadSize）用于查询上传的备份文件大小。在备份上传类型是COS_UPLOAD(备份放在业务的对象存储上)时有效。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupUploadSize"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupUploadSizeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackups(
            self,
            request: models.DescribeBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupsResponse:
        """
        本接口(DescribeBackups)用于查询备份列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBusinessIntelligenceFile(
            self,
            request: models.DescribeBusinessIntelligenceFileRequest,
            opts: Dict = None,
    ) -> models.DescribeBusinessIntelligenceFileResponse:
        """
        本接口（DescribeBusinessIntelligenceFile）用于查询商业智能服务需要的文件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBusinessIntelligenceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBusinessIntelligenceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCollationTimeZone(
            self,
            request: models.DescribeCollationTimeZoneRequest,
            opts: Dict = None,
    ) -> models.DescribeCollationTimeZoneResponse:
        """
        本接口(DescribeCollationTimeZone)用于查询实例支持的字符集和时区。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCollationTimeZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCollationTimeZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBackupStatistical(
            self,
            request: models.DescribeCrossBackupStatisticalRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBackupStatisticalResponse:
        """
        本接口(DescribeCrossBackupStatistical)用于查询跨地域备份实时统计列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBackupStatistical"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBackupStatisticalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossRegionZone(
            self,
            request: models.DescribeCrossRegionZoneRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossRegionZoneResponse:
        """
        本接口(DescribeCrossRegionZone)根据主实例查询备机的容灾地域和可用区。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossRegionZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossRegionZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossRegions(
            self,
            request: models.DescribeCrossRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossRegionsResponse:
        """
        本接口(DescribeCrossRegions)用于查询跨地域备份的目标地域。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCharsets(
            self,
            request: models.DescribeDBCharsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCharsetsResponse:
        """
        本接口（DescribeDBCharsets）用于查询实例支持的数据库字符集。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCharsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCharsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceInter(
            self,
            request: models.DescribeDBInstanceInterRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceInterResponse:
        """
        本接口（DescribeDBInstanceInter）用于查询互通实例的信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceInter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceInterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        本接口（DescribeDBInstances）用于查询实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstancesAttribute(
            self,
            request: models.DescribeDBInstancesAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesAttributeResponse:
        """
        本接口（DescribeDBInstancesAttribute）用于查询实例附属属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstancesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBPrivilegeByAccount(
            self,
            request: models.DescribeDBPrivilegeByAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeDBPrivilegeByAccountResponse:
        """
        本接口(DescribeDBPrivilegeByAccount)用于查询账号关联的数据库和权限信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBPrivilegeByAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBPrivilegeByAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBRestoreTime(
            self,
            request: models.DescribeDBRestoreTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBRestoreTimeResponse:
        """
        本接口（DescribeDBRestoreTime）用于查询可回档的数据库
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBRestoreTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBRestoreTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBs(
            self,
            request: models.DescribeDBsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBsResponse:
        """
        本接口（DescribeDBs）用于查询数据库列表。**已废弃，请使用接口DescribeDatabases**
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBsNormal(
            self,
            request: models.DescribeDBsNormalRequest,
            opts: Dict = None,
    ) -> models.DescribeDBsNormalResponse:
        """
        本接口(DescribeDBsNormal)用于查询数据库配置信息，此接口不包含数据库的关联账号。**此接口已废弃，请使用DescribeDatabasesNormal。**
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBsNormal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBsNormalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseNames(
            self,
            request: models.DescribeDatabaseNamesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseNamesResponse:
        """
        本接口（DescribeDatabaseNames）查询账户关联的数据库名称。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        本接口（DescribeDatabases）用于查询数据库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabasesNormal(
            self,
            request: models.DescribeDatabasesNormalRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesNormalResponse:
        """
        本接口(DescribeDBsNormal)用于查询数据库配置信息，此接口不包含数据库的关联账号
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabasesNormal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesNormalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowStatus(
            self,
            request: models.DescribeFlowStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowStatusResponse:
        """
        本接口(DescribeFlowStatus)用于查询流程状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHASwitchLog(
            self,
            request: models.DescribeHASwitchLogRequest,
            opts: Dict = None,
    ) -> models.DescribeHASwitchLogResponse:
        """
        本接口(DescribeHASwitchLog)用于手动主备切换。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHASwitchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHASwitchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIncrementalMigration(
            self,
            request: models.DescribeIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.DescribeIncrementalMigrationResponse:
        """
        本接口（DescribeIncrementalMigration）用于查询增量备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInquiryPriceParameter(
            self,
            request: models.DescribeInquiryPriceParameterRequest,
            opts: Dict = None,
    ) -> models.DescribeInquiryPriceParameterResponse:
        """
        本接口（DescribeInquiryPriceParameter）用于查询实例询价计费参数。当前接口查询实例新购的计费参数。内部接口用于活动页售卖场景。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInquiryPriceParameter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInquiryPriceParameterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceByOrders(
            self,
            request: models.DescribeInstanceByOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceByOrdersResponse:
        """
        本接口（DescribeInstanceByOrders）用于根据订单号查询资源ID
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceByOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceByOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParamRecords(
            self,
            request: models.DescribeInstanceParamRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamRecordsResponse:
        """
        该接口（DescribeInstanceParamRecords）用于查询实例参数修改历史。
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
        该接口（DescribeInstanceParams）用于查询实例的参数列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTasks(
            self,
            request: models.DescribeInstanceTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTasksResponse:
        """
        本接口（DescribeInstanceTasks）用于查询实例相关的异步任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTradeParameter(
            self,
            request: models.DescribeInstanceTradeParameterRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTradeParameterResponse:
        """
        本接口（DescribeInstanceTradeParameter）用于查询实例的计费参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTradeParameter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTradeParameterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintenanceSpan(
            self,
            request: models.DescribeMaintenanceSpanRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintenanceSpanResponse:
        """
        本接口（DescribeMaintenanceSpan）根据实例ID查询该实例的可维护时间窗。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintenanceSpan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintenanceSpanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationDatabases(
            self,
            request: models.DescribeMigrationDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationDatabasesResponse:
        """
        本接口（DescribeMigrationDatabases）的作用是查询待迁移数据库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationDetail(
            self,
            request: models.DescribeMigrationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationDetailResponse:
        """
        本接口（DescribeMigrationDetail）用于查询迁移任务的详细情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrations(
            self,
            request: models.DescribeMigrationsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationsResponse:
        """
        本接口（DescribeMigrations）根据输入的限定条件，查询符合条件的迁移任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrders(
            self,
            request: models.DescribeOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrdersResponse:
        """
        本接口（DescribeOrders）用于查询订单信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductConfig(
            self,
            request: models.DescribeProductConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeProductConfigResponse:
        """
        本接口（DescribeProductConfig）用于查询售卖规格配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductSpec(
            self,
            request: models.DescribeProductSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeProductSpecResponse:
        """
        本接口 (DescribeProductSpec) 用于查询全地域售卖规格配置（内部前端使用不公开）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublishSubscribe(
            self,
            request: models.DescribePublishSubscribeRequest,
            opts: Dict = None,
    ) -> models.DescribePublishSubscribeResponse:
        """
        本接口（DescribePublishSubscribe）用于查询发布订阅关系列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublishSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublishSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroupAutoWeight(
            self,
            request: models.DescribeReadOnlyGroupAutoWeightRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupAutoWeightResponse:
        """
        本接口（DescribeReadOnlyGroupAutoWeight）用于查询只读组的自动权重分配结果，在接口BalanceReadOnlyGroup接口中按照自动权重分配结果进行路由权重分配。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroupAutoWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupAutoWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroupByReadOnlyInstance(
            self,
            request: models.DescribeReadOnlyGroupByReadOnlyInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupByReadOnlyInstanceResponse:
        """
        本接口（DescribeReadOnlyGroupByReadOnlyInstance）用于通过只读副本实例ID查询其所在的只读组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroupByReadOnlyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupByReadOnlyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroupDetails(
            self,
            request: models.DescribeReadOnlyGroupDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupDetailsResponse:
        """
        本接口（DescribeReadOnlyGroupDetails）用于查询只读组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroupDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroupList(
            self,
            request: models.DescribeReadOnlyGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupListResponse:
        """
        本接口（DescribeReadOnlyGroupList）用于查询只读组列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        本接口 (DescribeRegions) 用于查询售卖地域信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegularBackupPlan(
            self,
            request: models.DescribeRegularBackupPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeRegularBackupPlanResponse:
        """
        本接口（DescribeRegularBackupPlan）用于查询实例定期备份保留计划
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegularBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegularBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRestoreTask(
            self,
            request: models.DescribeRestoreTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRestoreTaskResponse:
        """
        本接口（DescribeRestoreTask）用于查询回档任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRestoreTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRestoreTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRestoreTimeRange(
            self,
            request: models.DescribeRestoreTimeRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeRestoreTimeRangeResponse:
        """
        本接口(DescribeRestoreTimeRange)用于查询按照时间点可回档的时间范围。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRestoreTimeRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRestoreTimeRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollbackTime(
            self,
            request: models.DescribeRollbackTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeRollbackTimeResponse:
        """
        本接口（DescribeRollbackTime）用于查询实例可回档时间范围
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowlogs(
            self,
            request: models.DescribeSlowlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowlogsResponse:
        """
        本接口（DescribeSlowlogs）用于获取慢查询日志文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecSellStatus(
            self,
            request: models.DescribeSpecSellStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecSellStatusResponse:
        """
        本接口（DescribeSpecSellStatus）用于查询售卖规格状态信息，其中包括售卖状态，参考价格等(实际价格以询价接口为准)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecSellStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecSellStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpgradeInstanceCheck(
            self,
            request: models.DescribeUpgradeInstanceCheckRequest,
            opts: Dict = None,
    ) -> models.DescribeUpgradeInstanceCheckResponse:
        """
        本接口（DescribeUpgradeInstanceCheck）用于在实例变配前，预检查实例变配的影响情况等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpgradeInstanceCheck"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpgradeInstanceCheckResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUploadBackupInfo(
            self,
            request: models.DescribeUploadBackupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUploadBackupInfoResponse:
        """
        本接口（DescribeUploadBackupInfo）用于查询备份上传权限。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUploadBackupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUploadBackupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUploadIncrementalInfo(
            self,
            request: models.DescribeUploadIncrementalInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUploadIncrementalInfoResponse:
        """
        本接口（DescribeUploadIncrementalInfo）用于查询增量备份上传权限。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUploadIncrementalInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUploadIncrementalInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeXEvents(
            self,
            request: models.DescribeXEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeXEventsResponse:
        """
        本接口（DescribeXEvents）用于查询扩展事件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeXEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeXEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        本接口（DescribeZones）用于查询当前可售卖的可用区信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateDBInstances(
            self,
            request: models.InquiryPriceCreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateDBInstancesResponse:
        """
        本接口（InquiryPriceCreateDBInstances）用于查询申请实例价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewDBInstance(
            self,
            request: models.InquiryPriceRenewDBInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewDBInstanceResponse:
        """
        本接口（InquiryPriceRenewDBInstance）用于查询包年包月实例的续费价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceUpgradeDBInstance(
            self,
            request: models.InquiryPriceUpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceUpgradeDBInstanceResponse:
        """
        本接口（InquiryPriceUpgradeDBInstance）用于查询包年包月实例升级变配的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPrivilege(
            self,
            request: models.ModifyAccountPrivilegeRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPrivilegeResponse:
        """
        本接口（ModifyAccountPrivilege）用于修改实例账户权限。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivilege"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountRemark(
            self,
            request: models.ModifyAccountRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountRemarkResponse:
        """
        本接口（ModifyAccountRemark）用于修改账户备注。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupMigration(
            self,
            request: models.ModifyBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupMigrationResponse:
        """
        本接口（ModifyBackupMigration）用于修改备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupName(
            self,
            request: models.ModifyBackupNameRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupNameResponse:
        """
        本接口(ModifyBackupName)用于修改备份任务名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupStrategy(
            self,
            request: models.ModifyBackupStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupStrategyResponse:
        """
        本接口（ModifyBackupStrategy）用于修改备份策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloseWanIp(
            self,
            request: models.ModifyCloseWanIpRequest,
            opts: Dict = None,
    ) -> models.ModifyCloseWanIpResponse:
        """
        本接口(ModifyCloseWanIp)用于关闭实例外网。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloseWanIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloseWanIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCrossBackupStrategy(
            self,
            request: models.ModifyCrossBackupStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyCrossBackupStrategyResponse:
        """
        本接口(ModifyCrossBackupStrategy)用于开启、关闭地域备份策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCrossBackupStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCrossBackupStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBEncryptAttributes(
            self,
            request: models.ModifyDBEncryptAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyDBEncryptAttributesResponse:
        """
        本接口（ModifyDBEncryptAttributes）用于开启、关闭数据库的TDE加密功能。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBEncryptAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBEncryptAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceName(
            self,
            request: models.ModifyDBInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNameResponse:
        """
        本接口（ModifyDBInstanceName）用于修改实例名字。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceNetwork(
            self,
            request: models.ModifyDBInstanceNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNetworkResponse:
        """
        本接口（ModifyDBInstanceNetwork）用于修改运行中实例的网络，仅支持从VPC网络到VPC网络的转换
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceNote(
            self,
            request: models.ModifyDBInstanceNoteRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNoteResponse:
        """
        本接口（ModifyDBInstanceNote）用于修改实例备注信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceNote"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNoteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceProject(
            self,
            request: models.ModifyDBInstanceProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceProjectResponse:
        """
        本接口（ModifyDBInstanceProject）用于修改数据库实例所属项目。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceRenewFlag(
            self,
            request: models.ModifyDBInstanceRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceRenewFlagResponse:
        """
        本接口（ModifyDBInstanceRenewFlag）用于修改实例续费标记
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSSL(
            self,
            request: models.ModifyDBInstanceSSLRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSSLResponse:
        """
        本接口（ModifyDBInstanceSSL）用于开启\关闭\更新SSL加密
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBName(
            self,
            request: models.ModifyDBNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDBNameResponse:
        """
        本接口（ModifyDBName）用于更新数据库名。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBRemark(
            self,
            request: models.ModifyDBRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyDBRemarkResponse:
        """
        本接口（ModifyDBRemark）用于修改数据库备注。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDReadable(
            self,
            request: models.ModifyDReadableRequest,
            opts: Dict = None,
    ) -> models.ModifyDReadableResponse:
        """
        本接口（ModifyDReadable）用于开通或者关闭备机只读
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDReadable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDReadableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseCDC(
            self,
            request: models.ModifyDatabaseCDCRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseCDCResponse:
        """
        本接口(ModifyDatabaseCDC)用于开启、关闭数据库数据变更捕获(CDC)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseCDC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseCDCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseCT(
            self,
            request: models.ModifyDatabaseCTRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseCTResponse:
        """
        本接口(ModifyDatabaseCT)用于启用、禁用数据库数据变更跟踪(CT)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseCT"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseCTResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseMdf(
            self,
            request: models.ModifyDatabaseMdfRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseMdfResponse:
        """
        本接口(ModifyDatabaseMdf)用于收缩数据库mdf(Shrink mdf)。**本接口已废弃，请使用接口ModifyDatabaseShrinkMDF**。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseMdf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseMdfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabasePrivilege(
            self,
            request: models.ModifyDatabasePrivilegeRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabasePrivilegeResponse:
        """
        本接口（ModifyDatabasePrivilege）用于修改实例数据库权限。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabasePrivilege"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabasePrivilegeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseShrinkMDF(
            self,
            request: models.ModifyDatabaseShrinkMDFRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseShrinkMDFResponse:
        """
        本接口（ModifyDatabaseShrinkMDF）用于收缩数据库 mdf（Shrink mdf）。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseShrinkMDF"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseShrinkMDFResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIncrementalMigration(
            self,
            request: models.ModifyIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.ModifyIncrementalMigrationResponse:
        """
        本接口（ModifyIncrementalMigration）用于修改增量备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceEncryptAttributes(
            self,
            request: models.ModifyInstanceEncryptAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceEncryptAttributesResponse:
        """
        本接口（ModifyInstanceEncryptAttributes）用于开通实例的TDE加密功能。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceEncryptAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceEncryptAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParam(
            self,
            request: models.ModifyInstanceParamRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamResponse:
        """
        本接口(ModifyInstanceParam)用于修改云数据库实例的参数。
        <b>注意</b>：如果修改的参数是需要<b>重启实例</b>的，那么实例将会按照WaitSwitch参数的设置(可能是立即执行也可能在可维护时间窗内自动执行)在执行参数修改时<b>重启实例</b>。
        您可以通过DescribeInstanceParams接口查询修改参数时是否会重启实例，以免导致您的实例不符合预期重启。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintenanceSpan(
            self,
            request: models.ModifyMaintenanceSpanRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintenanceSpanResponse:
        """
        本接口（ModifyMaintenanceSpan）用于修改实例的可维护时间窗
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintenanceSpan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintenanceSpanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigration(
            self,
            request: models.ModifyMigrationRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrationResponse:
        """
        本接口（ModifyMigration）可以修改已有的迁移任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOpenWanIp(
            self,
            request: models.ModifyOpenWanIpRequest,
            opts: Dict = None,
    ) -> models.ModifyOpenWanIpResponse:
        """
        本接口(ModifyOpenWanIp)用于开通实例外网。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOpenWanIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOpenWanIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPublishSubscribe(
            self,
            request: models.ModifyPublishSubscribeRequest,
            opts: Dict = None,
    ) -> models.ModifyPublishSubscribeResponse:
        """
        本接口（ModifyPublishSubscribe）用于修改实例的发布订阅关系。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPublishSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPublishSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPublishSubscribeName(
            self,
            request: models.ModifyPublishSubscribeNameRequest,
            opts: Dict = None,
    ) -> models.ModifyPublishSubscribeNameResponse:
        """
        本接口（ModifyPublishSubscribeName）修改发布订阅的名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPublishSubscribeName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPublishSubscribeNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReadOnlyGroupDetails(
            self,
            request: models.ModifyReadOnlyGroupDetailsRequest,
            opts: Dict = None,
    ) -> models.ModifyReadOnlyGroupDetailsResponse:
        """
        本接口（ModifyReadOnlyGroupDetails）用于修改只读组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReadOnlyGroupDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReadOnlyGroupDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenInterCommunication(
            self,
            request: models.OpenInterCommunicationRequest,
            opts: Dict = None,
    ) -> models.OpenInterCommunicationResponse:
        """
        本接口（OpenInterCommunication）用于打开实例的互通，实例互通可以实现商业智能服务相互联通。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenInterCommunication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenInterCommunicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMigrationCheckProcess(
            self,
            request: models.QueryMigrationCheckProcessRequest,
            opts: Dict = None,
    ) -> models.QueryMigrationCheckProcessResponse:
        """
        本接口（QueryMigrationCheckProcess）的作用是查询迁移检查任务的进度，适用于迁移源的类型为TencentDB for SQLServer 的迁移方式
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMigrationCheckProcess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMigrationCheckProcessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecycleDBInstance(
            self,
            request: models.RecycleDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RecycleDBInstanceResponse:
        """
        本接口（RecycleDBInstance）用于主动回收已下线的SQLSERVER实例
        """
        
        kwargs = {}
        kwargs["action"] = "RecycleDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecycleDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecycleReadOnlyGroup(
            self,
            request: models.RecycleReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.RecycleReadOnlyGroupResponse:
        """
        本接口（RecycleReadOnlyGroup）立即回收只读组的资源，只读组占用的vip等资源将立即释放且不可找回。
        """
        
        kwargs = {}
        kwargs["action"] = "RecycleReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecycleReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveBackups(
            self,
            request: models.RemoveBackupsRequest,
            opts: Dict = None,
    ) -> models.RemoveBackupsResponse:
        """
        本接口（RemoveBackups）可以删除用户手动创建的备份文件。待删除的备份策略可以是实例备份，也可以是多库备份。
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDBInstance(
            self,
            request: models.RenewDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewDBInstanceResponse:
        """
        本接口（RenewDBInstance）用于续费实例。当被续费实例是按量计费实例时，则按量计费实例转为包年包月计费方式。
        按量计费实例转包年包月询价可通过(InquiryPriceRenewDBInstance)接口获得。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewPostpaidDBInstance(
            self,
            request: models.RenewPostpaidDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewPostpaidDBInstanceResponse:
        """
        本接口（RenewPostpaidDBInstance）用于将通过接口TerminateDBInstance手动隔离的按量计费实例从回收站中恢复。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewPostpaidDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewPostpaidDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        本接口（ResetAccountPassword）用于重置实例的账号密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDBInstance(
            self,
            request: models.RestartDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartDBInstanceResponse:
        """
        本接口（RestartDBInstance）用于重启数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreInstance(
            self,
            request: models.RestoreInstanceRequest,
            opts: Dict = None,
    ) -> models.RestoreInstanceResponse:
        """
        本接口（RestoreInstance）用于按照备份集回档数据库。
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackInstance(
            self,
            request: models.RollbackInstanceRequest,
            opts: Dict = None,
    ) -> models.RollbackInstanceResponse:
        """
        本接口（RollbackInstance）用于按照时间点回档实例
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunMigration(
            self,
            request: models.RunMigrationRequest,
            opts: Dict = None,
    ) -> models.RunMigrationResponse:
        """
        本接口（RunMigration）用于启动迁移任务，开始迁移
        """
        
        kwargs = {}
        kwargs["action"] = "RunMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartBackupMigration(
            self,
            request: models.StartBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.StartBackupMigrationResponse:
        """
        本接口（StartBackupMigration）用于启动备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StartBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartIncrementalMigration(
            self,
            request: models.StartIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.StartIncrementalMigrationResponse:
        """
        本接口（StartIncrementalMigration）用于启动增量备份导入任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StartIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstanceXEvent(
            self,
            request: models.StartInstanceXEventRequest,
            opts: Dict = None,
    ) -> models.StartInstanceXEventResponse:
        """
        本接口（StartInstanceXEvent）用于开启、关闭扩展事件。
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstanceXEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstanceXEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartMigrationCheck(
            self,
            request: models.StartMigrationCheckRequest,
            opts: Dict = None,
    ) -> models.StartMigrationCheckResponse:
        """
        本接口（StartMigrationCheck）的作用是启动一个迁移前的校验任务，适用于迁移源的类型为TencentDB for SQLServer 的迁移方式
        """
        
        kwargs = {}
        kwargs["action"] = "StartMigrationCheck"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartMigrationCheckResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMigration(
            self,
            request: models.StopMigrationRequest,
            opts: Dict = None,
    ) -> models.StopMigrationResponse:
        """
        本接口（StopMigration）作用是中止一个迁移任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchCloudInstanceHA(
            self,
            request: models.SwitchCloudInstanceHARequest,
            opts: Dict = None,
    ) -> models.SwitchCloudInstanceHAResponse:
        """
        本接口(SwitchCloudInstanceHA)用于手动主备切换。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchCloudInstanceHA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchCloudInstanceHAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDBInstance(
            self,
            request: models.TerminateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateDBInstanceResponse:
        """
        本接口(TerminateDBInstance)用于主动隔离实例，使得实例进入回收站。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstance(
            self,
            request: models.UpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceResponse:
        """
        本接口（UpgradeDBInstance）用于升级实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)