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
from tencentcloud.dcdb.v20180411 import models
from typing import Dict


class DcdbClient(AbstractClient):
    _apiVersion = '2018-04-11'
    _endpoint = 'dcdb.tencentcloudapi.com'
    _service = 'dcdb'

    async def ActiveHourDCDBInstance(
            self,
            request: models.ActiveHourDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.ActiveHourDCDBInstanceResponse:
        """
        解隔离TDSQL按量计费实例
        """
        
        kwargs = {}
        kwargs["action"] = "ActiveHourDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActiveHourDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        本接口 (AssociateSecurityGroups) 用于安全组批量绑定云资源。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelDcnJob(
            self,
            request: models.CancelDcnJobRequest,
            opts: Dict = None,
    ) -> models.CancelDcnJobResponse:
        """
        本接口（CancelDcnJob）用于取消DCN同步
        """
        
        kwargs = {}
        kwargs["action"] = "CancelDcnJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelDcnJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelOnlineDDLJob(
            self,
            request: models.CancelOnlineDDLJobRequest,
            opts: Dict = None,
    ) -> models.CancelOnlineDDLJobResponse:
        """
        取消 Online DDL 任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelOnlineDDLJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelOnlineDDLJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneAccount(
            self,
            request: models.CloneAccountRequest,
            opts: Dict = None,
    ) -> models.CloneAccountResponse:
        """
        本接口（CloneAccount）用于克隆实例账户。
        """
        
        kwargs = {}
        kwargs["action"] = "CloneAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseDBExtranetAccess(
            self,
            request: models.CloseDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.CloseDBExtranetAccessResponse:
        """
        本接口(CloseDBExtranetAccess)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问，查询实例列表接口将不返回对应实例的外网域名和端口信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyAccountPrivileges(
            self,
            request: models.CopyAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.CopyAccountPrivilegesResponse:
        """
        本接口（CopyAccountPrivileges）用于复制云数据库账号的权限。
        注意：相同用户名，不同Host是不同的账号，Readonly属性相同的账号之间才能复制权限。
        """
        
        kwargs = {}
        kwargs["action"] = "CopyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccount(
            self,
            request: models.CreateAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAccountResponse:
        """
        本接口（CreateAccount）用于创建云数据库账号。一个实例可以创建多个不同的账号，相同的用户名+不同的host是不同的账号。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDCDBInstance(
            self,
            request: models.CreateDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDCDBInstanceResponse:
        """
        本接口（CreateDCDBInstance）用于创建包年包月的TDSQL实例，可通过传入实例规格、数据库版本号、购买时长等信息创建云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDedicatedClusterDCDBInstance(
            self,
            request: models.CreateDedicatedClusterDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDedicatedClusterDCDBInstanceResponse:
        """
        创建TDSQL独享集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDedicatedClusterDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDedicatedClusterDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHourDCDBInstance(
            self,
            request: models.CreateHourDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateHourDCDBInstanceResponse:
        """
        创建TDSQL按量计费实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHourDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHourDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOnlineDDLJob(
            self,
            request: models.CreateOnlineDDLJobRequest,
            opts: Dict = None,
    ) -> models.CreateOnlineDDLJobResponse:
        """
        创建在线DDL任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOnlineDDLJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOnlineDDLJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTmpDCDBInstance(
            self,
            request: models.CreateTmpDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateTmpDCDBInstanceResponse:
        """
        回档TDSQL实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTmpDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTmpDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccount(
            self,
            request: models.DeleteAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountResponse:
        """
        本接口（DeleteAccount）用于删除云数据库账号。用户名+host唯一确定一个账号。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivileges(
            self,
            request: models.DescribeAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegesResponse:
        """
        本接口（DescribeAccountPrivileges）用于查询云数据库账号权限。
        注意：注意：相同用户名，不同Host是不同的账号。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        本接口（DescribeAccounts）用于查询指定云数据库实例的账号列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupConfigs(
            self,
            request: models.DescribeBackupConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupConfigsResponse:
        """
        本接口(DescribeBackupConfigs)用于查询数据库备份配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupFiles(
            self,
            request: models.DescribeBackupFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupFilesResponse:
        """
        本接口(DescribeBackupFiles)用于查看备份文件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBEncryptAttributes(
            self,
            request: models.DescribeDBEncryptAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBEncryptAttributesResponse:
        """
        本接口(DescribeDBEncryptAttributes)用于查询实例数据加密状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBEncryptAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBEncryptAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBLogFiles(
            self,
            request: models.DescribeDBLogFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBLogFilesResponse:
        """
        本接口(DescribeDBLogFiles)用于获取数据库的各种日志列表，包括冷备、binlog、errlog和slowlog。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBLogFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBLogFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBParameters(
            self,
            request: models.DescribeDBParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDBParametersResponse:
        """
        本接口(DescribeDBParameters)用于获取数据库的当前参数设置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        本接口（DescribeDBSecurityGroups）用于查询实例安全组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSlowLogs(
            self,
            request: models.DescribeDBSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSlowLogsResponse:
        """
        本接口(DescribeDBSlowLogs)用于查询慢查询日志列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSyncMode(
            self,
            request: models.DescribeDBSyncModeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSyncModeResponse:
        """
        本接口（DescribeDBSyncMode）用于查询云数据库实例的同步模式。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSyncMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSyncModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBTmpInstances(
            self,
            request: models.DescribeDBTmpInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBTmpInstancesResponse:
        """
        本接口（DescribeDBTmpInstances）用于获取实例回档生成的临时实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBTmpInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBTmpInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBBinlogTime(
            self,
            request: models.DescribeDCDBBinlogTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBBinlogTimeResponse:
        """
        获取实例回档时可选的时间范围
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBBinlogTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBBinlogTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBInstanceDetail(
            self,
            request: models.DescribeDCDBInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBInstanceDetailResponse:
        """
        本接口（DescribeDCDBInstanceDetail）用于获取TDSQL实例详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBInstanceNodeInfo(
            self,
            request: models.DescribeDCDBInstanceNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBInstanceNodeInfoResponse:
        """
        本接口（DescribeDCDBInstanceNodeInfo）用于获取实例节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBInstanceNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBInstanceNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBInstances(
            self,
            request: models.DescribeDCDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBInstancesResponse:
        """
        查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。
        如果不指定任何筛选条件，则默认返回10条实例记录，单次请求最多支持返回100条实例记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBPrice(
            self,
            request: models.DescribeDCDBPriceRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBPriceResponse:
        """
        本接口（DescribeDCDBPrice）用于在购买实例前，查询实例的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBRenewalPrice(
            self,
            request: models.DescribeDCDBRenewalPriceRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBRenewalPriceResponse:
        """
        本接口（DescribeDCDBRenewalPrice）用于在续费分布式数据库实例时，查询续费的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBRenewalPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBRenewalPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBSaleInfo(
            self,
            request: models.DescribeDCDBSaleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBSaleInfoResponse:
        """
        本接口(DescribeDCDBSaleInfo)用于查询分布式数据库可售卖的地域和可用区信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBSaleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBSaleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBShards(
            self,
            request: models.DescribeDCDBShardsRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBShardsResponse:
        """
        本接口（DescribeDCDBShards）用于查询云数据库实例的分片信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBShards"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBShardsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDCDBUpgradePrice(
            self,
            request: models.DescribeDCDBUpgradePriceRequest,
            opts: Dict = None,
    ) -> models.DescribeDCDBUpgradePriceResponse:
        """
        本接口（DescribeDCDBUpgradePrice）用于查询变配分布式数据库实例价格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDCDBUpgradePrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDCDBUpgradePriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseObjects(
            self,
            request: models.DescribeDatabaseObjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseObjectsResponse:
        """
        本接口（DescribeDatabaseObjects）用于查询云数据库实例的数据库中的对象列表，包含表、存储过程、视图和函数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseTable(
            self,
            request: models.DescribeDatabaseTableRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseTableResponse:
        """
        本接口（DescribeDatabaseTable）用于查询云数据库实例的表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        本接口（DescribeDatabases）用于查询云数据库实例的数据库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDcnDetail(
            self,
            request: models.DescribeDcnDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDcnDetailResponse:
        """
        获取实例灾备详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDcnDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDcnDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileDownloadUrl(
            self,
            request: models.DescribeFileDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeFileDownloadUrlResponse:
        """
        本接口(DescribeFileDownloadUrl)用于获取数据库指定备份或日志文件的下载连接。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlow(
            self,
            request: models.DescribeFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowResponse:
        """
        本接口（DescribeFlow）用于查询流程状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSSLAttributes(
            self,
            request: models.DescribeInstanceSSLAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSSLAttributesResponse:
        """
        本接口（DescribeInstanceSSLAttributes）用于拉取实例SSL认证属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSSLAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSSLAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogFileRetentionPeriod(
            self,
            request: models.DescribeLogFileRetentionPeriodRequest,
            opts: Dict = None,
    ) -> models.DescribeLogFileRetentionPeriodResponse:
        """
        本接口(DescribeLogFileRetentionPeriod)用于查看数据库备份日志的备份天数的设置情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogFileRetentionPeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogFileRetentionPeriodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOnlineDDLJob(
            self,
            request: models.DescribeOnlineDDLJobRequest,
            opts: Dict = None,
    ) -> models.DescribeOnlineDDLJobResponse:
        """
        查询Online DDL 任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOnlineDDLJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOnlineDDLJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrders(
            self,
            request: models.DescribeOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrdersResponse:
        """
        本接口（DescribeOrders）用于查询分布式数据库订单信息。传入订单ID来查询订单关联的分布式数据库实例，和对应的任务流程ID。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessList(
            self,
            request: models.DescribeProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessListResponse:
        """
        本接口 (DescribeProcessList) 用于查询当前正在运行的线程（连接/查询）信息。

        - 可以根据客户端IP，DB，执行时间等信息来查询实例正在运行的线程信息。过滤信息详细请见过滤器Filter。
        - 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的线程信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        本接口（DescribeProjectSecurityGroups）用于查询项目安全组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        本接口（DescribeProjects）用于查询项目列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShardSpec(
            self,
            request: models.DescribeShardSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeShardSpecResponse:
        """
        查询可创建的分布式数据库可售卖的分片规格配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShardSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShardSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserTasks(
            self,
            request: models.DescribeUserTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeUserTasksResponse:
        """
        本接口（DescribeUserTasks）用于拉取用户任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyDCDBInstance(
            self,
            request: models.DestroyDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyDCDBInstanceResponse:
        """
        本接口(DestroyDCDBInstance)用于销毁已隔离的TDSQL包年包月实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyHourDCDBInstance(
            self,
            request: models.DestroyHourDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyHourDCDBInstanceResponse:
        """
        本接口（DestroyHourDCDBInstance）用于TDSQL销毁按量计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyHourDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyHourDCDBInstanceResponse
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
        
    async def FlushBinlog(
            self,
            request: models.FlushBinlogRequest,
            opts: Dict = None,
    ) -> models.FlushBinlogResponse:
        """
        相当于在所有分片的mysqld中执行flush logs，完成切分的binlog将展示在各个分片控制台binlog列表里。
        """
        
        kwargs = {}
        kwargs["action"] = "FlushBinlog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FlushBinlogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GrantAccountPrivileges(
            self,
            request: models.GrantAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.GrantAccountPrivilegesResponse:
        """
        本接口（GrantAccountPrivileges）用于给云数据库账号赋权。
        注意：相同用户名，不同Host是不同的账号。
        """
        
        kwargs = {}
        kwargs["action"] = "GrantAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GrantAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InitDCDBInstances(
            self,
            request: models.InitDCDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InitDCDBInstancesResponse:
        """
        本接口(InitDCDBInstances)用于初始化云数据库实例，包括设置默认字符集、表名大小写敏感等。
        """
        
        kwargs = {}
        kwargs["action"] = "InitDCDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InitDCDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDCDBInstance(
            self,
            request: models.IsolateDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDCDBInstanceResponse:
        """
        本接口(IsolateDCDBInstance)用于隔离分布式数据库TDSQL实例（包年包月），隔离后不能通过IP和端口访问数据库。隔离的实例可在回收站中进行开机。若为欠费隔离，请尽快进行充值。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDedicatedDBInstance(
            self,
            request: models.IsolateDedicatedDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDedicatedDBInstanceResponse:
        """
        本接口（IsolateDedicatedDBInstance）用于隔离独享云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDedicatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDedicatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateHourDCDBInstance(
            self,
            request: models.IsolateHourDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateHourDCDBInstanceResponse:
        """
        隔离TDSQL按量计费实例
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateHourDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateHourDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillSession(
            self,
            request: models.KillSessionRequest,
            opts: Dict = None,
    ) -> models.KillSessionResponse:
        """
        本接口（KillSession）用于杀死指定会话。
        """
        
        kwargs = {}
        kwargs["action"] = "KillSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountConfig(
            self,
            request: models.ModifyAccountConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountConfigResponse:
        """
        修改账号的一些配置，比如 max_user_connections
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountDescription(
            self,
            request: models.ModifyAccountDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountDescriptionResponse:
        """
        本接口（ModifyAccountDescription）用于修改云数据库账号备注。
        注意：相同用户名，不同Host是不同的账号。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPrivileges(
            self,
            request: models.ModifyAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPrivilegesResponse:
        """
        本接口(ModifyAccountPrivileges)用于修改云数据库的账户的权限信息。

        **注意**
        - 系统保留库："mysql"，只开放["SELECT"]权限
        - 只读账号授予读写权限会报错
        - 不传权限参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupConfigs(
            self,
            request: models.ModifyBackupConfigsRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupConfigsResponse:
        """
        本接口(ModifyBackupConfigs)用于修改数据库备份配置信息。

        1. 修改数据库超期备份配置，目前按年、按月、按日只支持一种，存在互斥关系，如当前策略按年备份，如果传入按月备份策略将会覆盖当前的按年备份策略，务必注意。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBEncryptAttributes(
            self,
            request: models.ModifyDBEncryptAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyDBEncryptAttributesResponse:
        """
        本接口(ModifyDBEncryptAttributes)用于修改实例数据加密。
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
        本接口（ModifyDBInstanceName）用于修改实例名字
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        本接口（ModifyDBInstanceSecurityGroups）用于修改云数据库安全组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstancesProject(
            self,
            request: models.ModifyDBInstancesProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstancesProjectResponse:
        """
        本接口（ModifyDBInstancesProject）用于修改云数据库实例所属项目。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstancesProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstancesProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBParameters(
            self,
            request: models.ModifyDBParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyDBParametersResponse:
        """
        本接口(ModifyDBParameters)用于修改数据库参数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBSyncMode(
            self,
            request: models.ModifyDBSyncModeRequest,
            opts: Dict = None,
    ) -> models.ModifyDBSyncModeResponse:
        """
        本接口（ModifyDBSyncMode）用于修改云数据库实例的同步模式。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBSyncMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBSyncModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceNetwork(
            self,
            request: models.ModifyInstanceNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNetworkResponse:
        """
        本接口（ModifyInstanceNetwork）用于修改实例所属网络。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceProtectedProperty(
            self,
            request: models.ModifyInstanceProtectedPropertyRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceProtectedPropertyResponse:
        """
        该接口用于修改实例的保护属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceProtectedProperty"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceProtectedPropertyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceSSLAttributes(
            self,
            request: models.ModifyInstanceSSLAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceSSLAttributesResponse:
        """
        本接口  （ModifyInstanceSSLAttributes）用于修改实例SSL认证功能属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceSSLAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceSSLAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceVip(
            self,
            request: models.ModifyInstanceVipRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceVipResponse:
        """
        本接口（ModifyInstanceVip）用于修改实例Vip
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceVport(
            self,
            request: models.ModifyInstanceVportRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceVportResponse:
        """
        本接口（ModifyInstanceVport）用于修改实例VPORT
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRealServerAccessStrategy(
            self,
            request: models.ModifyRealServerAccessStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyRealServerAccessStrategyResponse:
        """
        本接口(ModifyRealServerAccessStrategy)用于修改云数据库的VPCGW到RS的访问策略。

        **注意**
        - 修改策略后只对新建立的连接生效，老连接不受影响
        - 就近访问只针对实例是跨可用区部署有用，单可用区部署实例就近与否并无作用
        - DB每个Node对应一个proxy，如果开启就近访问，将会把连接集中到对应可用区的proxy上，可能造成热点问题，这种情况下如果是线上业务，请务必根据自己的业务请求量测试符合预期后再进行就近策略变更
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRealServerAccessStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRealServerAccessStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenDBExtranetAccess(
            self,
            request: models.OpenDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.OpenDBExtranetAccessResponse:
        """
        本接口（OpenDBExtranetAccess）用于开通云数据库实例的外网访问。开通外网访问后，您可通过外网域名和端口访问实例，可使用查询实例列表接口获取外网域名和端口信息。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDCDBInstance(
            self,
            request: models.RenewDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewDCDBInstanceResponse:
        """
        本接口（RenewDCDBInstance）用于续费分布式数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        本接口（ResetAccountPassword）用于重置云数据库账号的密码。
        注意：相同用户名，不同Host是不同的账号。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDBInstanceHA(
            self,
            request: models.SwitchDBInstanceHARequest,
            opts: Dict = None,
    ) -> models.SwitchDBInstanceHAResponse:
        """
        本接口(SwitchDBInstanceHA)用于实例主备切换。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDBInstanceHA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDBInstanceHAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDedicatedDBInstance(
            self,
            request: models.TerminateDedicatedDBInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateDedicatedDBInstanceResponse:
        """
        本接口（TerminateDedicatedDBInstance）用于销毁已隔离的独享分布式数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDedicatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDedicatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDCDBInstance(
            self,
            request: models.UpgradeDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDCDBInstanceResponse:
        """
        本接口（UpgradeDCDBInstance）用于升级分布式数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDedicatedDCDBInstance(
            self,
            request: models.UpgradeDedicatedDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDedicatedDCDBInstanceResponse:
        """
        本接口（UpgradeDedicatedDCDBInstance）用于升级TDSQL独享集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDedicatedDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDedicatedDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeHourDCDBInstance(
            self,
            request: models.UpgradeHourDCDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeHourDCDBInstanceResponse:
        """
        本接口（UpgradeHourDCDBInstance）用于升级分布式数据库TDSQL按量计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeHourDCDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeHourDCDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)