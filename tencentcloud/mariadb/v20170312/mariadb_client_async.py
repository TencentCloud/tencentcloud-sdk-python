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
from tencentcloud.mariadb.v20170312 import models
from typing import Dict


class MariadbClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'mariadb.tencentcloudapi.com'
    _service = 'mariadb'

    async def ActivateHourDBInstance(
            self,
            request: models.ActivateHourDBInstanceRequest,
            opts: Dict = None,
    ) -> models.ActivateHourDBInstanceResponse:
        """
        解隔离MariaDB按量计费实例
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateHourDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateHourDBInstanceResponse
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
        
    async def CreateDBInstance(
            self,
            request: models.CreateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceResponse:
        """
        本接口（CreateDBInstance）用于创建包年包月的MariaDB云数据库实例，可通过传入实例规格、数据库版本号、购买时长和数量等信息创建云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDedicatedClusterDBInstance(
            self,
            request: models.CreateDedicatedClusterDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDedicatedClusterDBInstanceResponse:
        """
        创建Mariadb独享集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDedicatedClusterDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDedicatedClusterDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHourDBInstance(
            self,
            request: models.CreateHourDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateHourDBInstanceResponse:
        """
        创建MariaDB按量计费实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHourDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHourDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTmpInstances(
            self,
            request: models.CreateTmpInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateTmpInstancesResponse:
        """
        本接口（CreateTmpInstances）用于创建临时实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTmpInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTmpInstancesResponse
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
        
    async def DescribeBackupTime(
            self,
            request: models.DescribeBackupTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupTimeResponse:
        """
        本接口（DescribeBackupTime）用于获取云数据库的备份时间。后台系统将根据此配置定期进行实例备份。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogTime(
            self,
            request: models.DescribeBinlogTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogTimeResponse:
        """
        本接口（DescribeBinlogTime）用于查询可回档时间范围。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogTimeResponse
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
        
    async def DescribeDBInstanceDetail(
            self,
            request: models.DescribeDBInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceDetailResponse:
        """
        本接口(DescribeDBInstanceDetail)用于查询指定实例的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceSpecs(
            self,
            request: models.DescribeDBInstanceSpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceSpecsResponse:
        """
        本接口(DescribeDBInstanceSpecs)用于查询可创建的云数据库可售卖的规格配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceSpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceSpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        本接口（DescribeDBInstances）用于查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。
        如果不指定任何筛选条件，则默认返回20条实例记录，单次请求最多支持返回100条实例记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
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
        本接口（DescribeFlow）用于查询流程状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodeInfo(
            self,
            request: models.DescribeInstanceNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodeInfoResponse:
        """
        本接口（DescribeInstanceNodeInfo）用于获取数据库实例主备节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodeInfoResponse
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
        
    async def DescribeOrders(
            self,
            request: models.DescribeOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrdersResponse:
        """
        本接口（DescribeOrders）用于查询云数据库订单信息。传入订单ID来查询订单关联的云数据库实例，和对应的任务流程ID。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrice(
            self,
            request: models.DescribePriceRequest,
            opts: Dict = None,
    ) -> models.DescribePriceResponse:
        """
        本接口（DescribePrice）用于在购买实例前，查询实例的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePriceResponse
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
        
    async def DescribeRenewalPrice(
            self,
            request: models.DescribeRenewalPriceRequest,
            opts: Dict = None,
    ) -> models.DescribeRenewalPriceResponse:
        """
        本接口（DescribeRenewalPrice）用于在续费云数据库实例时，查询续费的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRenewalPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRenewalPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSaleInfo(
            self,
            request: models.DescribeSaleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSaleInfoResponse:
        """
        本接口(DescribeSaleInfo)用于查询云数据库可售卖的地域和可用区信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSaleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSaleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpgradePrice(
            self,
            request: models.DescribeUpgradePriceRequest,
            opts: Dict = None,
    ) -> models.DescribeUpgradePriceResponse:
        """
        本接口（DescribeUpgradePrice）用于在扩容云数据库实例时，查询变配的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpgradePrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpgradePriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyDBInstance(
            self,
            request: models.DestroyDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyDBInstanceResponse:
        """
        本接口(DestroyDBInstance)用于销毁已隔离的包年包月实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyHourDBInstance(
            self,
            request: models.DestroyHourDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyHourDBInstanceResponse:
        """
        本接口（DestroyHourDBInstance）用于销毁MariaDB按量计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyHourDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyHourDBInstanceResponse
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
        相当于在mysqld中执行flush logs，完成切分的binlog将展示在实例控制台binlog列表里。
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
        
    async def InitDBInstances(
            self,
            request: models.InitDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InitDBInstancesResponse:
        """
        本接口(InitDBInstances)用于初始化云数据库实例，包括设置默认字符集、表名大小写敏感等。
        """
        
        kwargs = {}
        kwargs["action"] = "InitDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InitDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstance(
            self,
            request: models.IsolateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstanceResponse:
        """
        本接口(IsolateDBInstance)用于隔离云数据库MariaDB实例（包年包月），隔离后不能通过IP和端口访问数据库。隔离的实例可在回收站中进行开机。若为欠费隔离，请尽快进行充值。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstanceResponse
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
        
    async def IsolateHourDBInstance(
            self,
            request: models.IsolateHourDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateHourDBInstanceResponse:
        """
        隔离MariaDB按量计费实例
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateHourDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateHourDBInstanceResponse
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
        
    async def ModifyBackupTime(
            self,
            request: models.ModifyBackupTimeRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupTimeResponse:
        """
        本接口（ModifyBackupTime）用于设置云数据库实例的备份时间。后台系统将根据此配置定期进行实例备份。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupTimeResponse
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
        本接口（ModifyDBInstanceName）用于修改云数据库实例的名称。
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
        本接口（ModifyInstanceNetwork）用于修改实例所属网络
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
        该接口用于对实例修改删除保护属性
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
        本接口（ModifyInstanceVip）用于修改实例VIP
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
        
    async def ModifyLogFileRetentionPeriod(
            self,
            request: models.ModifyLogFileRetentionPeriodRequest,
            opts: Dict = None,
    ) -> models.ModifyLogFileRetentionPeriodResponse:
        """
        本接口(ModifyLogFileRetentionPeriod)用于修改数据库备份日志保存天数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogFileRetentionPeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogFileRetentionPeriodResponse
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
        
    async def ModifySyncTaskAttribute(
            self,
            request: models.ModifySyncTaskAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySyncTaskAttributeResponse:
        """
        本接口 (ModifySyncTaskAttribute) 用于修改同步任务的属性（目前只支持修改任务名称）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySyncTaskAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySyncTaskAttributeResponse
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
        
    async def RenewDBInstance(
            self,
            request: models.RenewDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewDBInstanceResponse:
        """
        本接口（RenewDBInstance）用于续费云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDBInstanceResponse
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
        
    async def RestartDBInstances(
            self,
            request: models.RestartDBInstancesRequest,
            opts: Dict = None,
    ) -> models.RestartDBInstancesResponse:
        """
        本接口（RestartDBInstances）用于重启数据库实例
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDBInstanceHA(
            self,
            request: models.SwitchDBInstanceHARequest,
            opts: Dict = None,
    ) -> models.SwitchDBInstanceHAResponse:
        """
        本接口（SwitchDBInstanceHA）用于发起实例主备切换。
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
        本接口（TerminateDedicatedDBInstance）用于销毁已隔离的独享云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDedicatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDedicatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstance(
            self,
            request: models.UpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceResponse:
        """
        本接口(UpgradeDBInstance)用于扩容云数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDedicatedDBInstance(
            self,
            request: models.UpgradeDedicatedDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDedicatedDBInstanceResponse:
        """
        本接口(UpgradeDedicatedDBInstance)用于扩容独享云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDedicatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDedicatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeHourDBInstance(
            self,
            request: models.UpgradeHourDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeHourDBInstanceResponse:
        """
        升级MariaDB按量计费实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeHourDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeHourDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)