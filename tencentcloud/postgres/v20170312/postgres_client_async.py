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
from tencentcloud.postgres.v20170312 import models
from typing import Dict


class PostgresClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'postgres.tencentcloudapi.com'
    _service = 'postgres'

    async def AddDBInstanceToReadOnlyGroup(
            self,
            request: models.AddDBInstanceToReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.AddDBInstanceToReadOnlyGroupResponse:
        """
        本接口（AddDBInstanceToReadOnlyGroup）用于添加只读实例到只读组
        """
        
        kwargs = {}
        kwargs["action"] = "AddDBInstanceToReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDBInstanceToReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneDBInstance(
            self,
            request: models.CloneDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CloneDBInstanceResponse:
        """
        用于克隆实例，支持指定备份集、指定时间点进行克隆。
        """
        
        kwargs = {}
        kwargs["action"] = "CloneDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAccountCAM(
            self,
            request: models.CloseAccountCAMRequest,
            opts: Dict = None,
    ) -> models.CloseAccountCAMResponse:
        """
        本接口用于关闭数据库账户的CAM验证服务。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAccountCAM"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAccountCAMResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseDBExtranetAccess(
            self,
            request: models.CloseDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.CloseDBExtranetAccessResponse:
        """
        本接口（CloseDBExtranetAccess）用于关闭实例公网地址。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccount(
            self,
            request: models.CreateAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAccountResponse:
        """
        此接口用于创建数据账号，返回的Oid为账号唯一标识。与数据库系统表pg_roles中记录的oid一致。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupPlan(
            self,
            request: models.CreateBackupPlanRequest,
            opts: Dict = None,
    ) -> models.CreateBackupPlanResponse:
        """
        此接口用于创建备份策略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaseBackup(
            self,
            request: models.CreateBaseBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBaseBackupResponse:
        """
        本接口（CreateBaseBackup）用于创建实例的数据备份。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaseBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaseBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstanceNetworkAccess(
            self,
            request: models.CreateDBInstanceNetworkAccessRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceNetworkAccessResponse:
        """
        本接口（CreateDBInstanceNetworkAccess）用于创建实例网络。单个实例允许创建的网络配置最多为2套，最少为1套。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstanceNetworkAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceNetworkAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatabase(
            self,
            request: models.CreateDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateDatabaseResponse:
        """
        此接口用于创建数据库，需指定数据库名及所有者。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstances(
            self,
            request: models.CreateInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateInstancesResponse:
        """
        本接口 (CreateInstances) 用于创建一个或者多个PostgreSQL实例，通过此接口创建的实例无需进行初始化，可直接使用。
        <li>实例创建成功后将自动开机启动，实例状态变为“运行中”。</li>
        <li>预付费实例的购买会预先扣除本次实例购买所需金额，按小时后付费实例购买会预先冻结本次实例购买一小时内所需金额，在调用本接口前请确保账户余额充足。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateParameterTemplate(
            self,
            request: models.CreateParameterTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateParameterTemplateResponse:
        """
        本接口 (CreateParameterTemplate) 用于创建参数模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateParameterTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateParameterTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReadOnlyDBInstance(
            self,
            request: models.CreateReadOnlyDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateReadOnlyDBInstanceResponse:
        """
        本接口(CreateReadOnlyDBInstance)用于创建只读实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReadOnlyDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReadOnlyDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReadOnlyGroup(
            self,
            request: models.CreateReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.CreateReadOnlyGroupResponse:
        """
        本接口（CreateReadOnlyGroup）用于创建只读组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReadOnlyGroupNetworkAccess(
            self,
            request: models.CreateReadOnlyGroupNetworkAccessRequest,
            opts: Dict = None,
    ) -> models.CreateReadOnlyGroupNetworkAccessResponse:
        """
        本接口（CreateReadOnlyGroupNetworkAccess）用于创建RO组的网络。创建网络的数量最多为2个。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReadOnlyGroupNetworkAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReadOnlyGroupNetworkAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccount(
            self,
            request: models.DeleteAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountResponse:
        """
        此接口用于删除数据库账号，需要同时输入Oid与UserName，避免误删。注：该接口可重入，如果账号已经不存在，调用此接口进行删除时不会报错。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupPlan(
            self,
            request: models.DeleteBackupPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupPlanResponse:
        """
        删除备份策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaseBackup(
            self,
            request: models.DeleteBaseBackupRequest,
            opts: Dict = None,
    ) -> models.DeleteBaseBackupResponse:
        """
        本接口（DeleteBaseBackup）用于删除实例指定数据备份。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaseBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaseBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBInstanceNetworkAccess(
            self,
            request: models.DeleteDBInstanceNetworkAccessRequest,
            opts: Dict = None,
    ) -> models.DeleteDBInstanceNetworkAccessResponse:
        """
        可对实例进行网络的删除操作（实例内至少保留一个网络）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBInstanceNetworkAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBInstanceNetworkAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogBackup(
            self,
            request: models.DeleteLogBackupRequest,
            opts: Dict = None,
    ) -> models.DeleteLogBackupResponse:
        """
        本接口（DeleteLogBackup）用于删除实例指定日志备份。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParameterTemplate(
            self,
            request: models.DeleteParameterTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParameterTemplateResponse:
        """
        本接口（DeleteParameterTemplate）主要用于删除某个参数模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParameterTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParameterTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReadOnlyGroup(
            self,
            request: models.DeleteReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteReadOnlyGroupResponse:
        """
        本接口(DeleteReadOnlyGroup)用于删除指定的只读组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReadOnlyGroupNetworkAccess(
            self,
            request: models.DeleteReadOnlyGroupNetworkAccessRequest,
            opts: Dict = None,
    ) -> models.DeleteReadOnlyGroupNetworkAccessResponse:
        """
        可对RO组进行网络的删除操作（网络数量至少保留1个）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReadOnlyGroupNetworkAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReadOnlyGroupNetworkAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivileges(
            self,
            request: models.DescribeAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegesResponse:
        """
        查询数据库账号对某数据库对象拥有的权限列表。
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
        本接口（DescribeAccounts）用于查询实例的数据库账号列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableRecoveryTime(
            self,
            request: models.DescribeAvailableRecoveryTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableRecoveryTimeResponse:
        """
        本接口（DescribeAvailableRecoveryTime）用于查询实例可恢复的时间范围。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableRecoveryTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableRecoveryTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadRestriction(
            self,
            request: models.DescribeBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadRestrictionResponse:
        """
        本接口（DescribeBackupDownloadRestriction）用于查询备份文件下载限制。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadURL(
            self,
            request: models.DescribeBackupDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadURLResponse:
        """
        本接口 (DescribeBackupDownloadURL) 用于查询指定备份集的下载地址，可包括全量备份集、增量日志备份集。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupOverview(
            self,
            request: models.DescribeBackupOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupOverviewResponse:
        """
        本接口（DescribeBackupOverview）用于查询用户的备份概览信息。返回用户当前备份个数、备份占用容量、免费容量、收费容量等信息（容量单位为字节）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupPlans(
            self,
            request: models.DescribeBackupPlansRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupPlansResponse:
        """
        本接口 (DescribeBackupPlans) 用于实例所有的备份计划查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupSummaries(
            self,
            request: models.DescribeBackupSummariesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupSummariesResponse:
        """
        本接口(DescribeBackupSummaries)用于查询实例备份的统计信息，返回以实例为维度的备份个数、占用容量等信息（容量单位为字节）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupSummaries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupSummariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaseBackups(
            self,
            request: models.DescribeBaseBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBaseBackupsResponse:
        """
        本接口（DescribeBaseBackups）用于查询数据备份列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaseBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaseBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClasses(
            self,
            request: models.DescribeClassesRequest,
            opts: Dict = None,
    ) -> models.DescribeClassesResponse:
        """
        本接口（DescribeClasses）用于查询实例售卖规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClasses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloneDBInstanceSpec(
            self,
            request: models.DescribeCloneDBInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeCloneDBInstanceSpecResponse:
        """
        本接口（DescribeCloneDBInstanceSpec）用于查询克隆实例可选择的最小规格，包括SpecCode和磁盘。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloneDBInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloneDBInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBBackups(
            self,
            request: models.DescribeDBBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBBackupsResponse:
        """
        本接口（DescribeDBBackups）用于查询实例备份列表。**本接口属于早期接口，已停止功能迭代，推荐使用接口**[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)**替代**。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBErrlogs(
            self,
            request: models.DescribeDBErrlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBErrlogsResponse:
        """
        本接口（DescribeDBErrlogs）用于查询错误日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBErrlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBErrlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceAttribute(
            self,
            request: models.DescribeDBInstanceAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceAttributeResponse:
        """
        本接口 (DescribeDBInstanceAttribute) 用于查询某个实例的详情信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceHAConfig(
            self,
            request: models.DescribeDBInstanceHAConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceHAConfigResponse:
        """
        本接口（DescribeDBInstanceHAConfig）用于查询实例HA配置信息。其中HA配置信息包括：
        <li>允许备节点切换为主节点的条件配置</li>
        <li>半同步实例使用同步复制或异步复制的条件配置</li>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceHAConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceHAConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceParameters(
            self,
            request: models.DescribeDBInstanceParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceParametersResponse:
        """
        本接口（DescribeDBInstanceAttribute）用于查询实例的参数信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceSSLConfig(
            self,
            request: models.DescribeDBInstanceSSLConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceSSLConfigResponse:
        """
        本接口用于查询实例SSL状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceSSLConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceSSLConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceSecurityGroups(
            self,
            request: models.DescribeDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceSecurityGroupsResponse:
        """
        本接口（DescribeDBInstanceSecurityGroups）用于查询实例安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        本接口 (DescribeDBInstances) 用于查询一个或多个实例的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBVersions(
            self,
            request: models.DescribeDBVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBVersionsResponse:
        """
        本接口（DescribeDBVersions）用于查询支持的数据库版本。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBXlogs(
            self,
            request: models.DescribeDBXlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBXlogsResponse:
        """
        本接口（DescribeDBXlogs）用于获取实例Xlog列表。 **本接口属于早期接口，已停止功能迭代，推荐使用接口**[DescribeLogBackups](https://cloud.tencent.com/document/api/409/89021)**替代**。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBXlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBXlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseObjects(
            self,
            request: models.DescribeDatabaseObjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseObjectsResponse:
        """
        本接口用于查询数据库对象列表。例如查询test数据库下的模式列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        接口（DescribeDatabases）用来查询实例的数据库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusters(
            self,
            request: models.DescribeDedicatedClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClustersResponse:
        """
        查询专属集群
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultParameters(
            self,
            request: models.DescribeDefaultParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultParametersResponse:
        """
        本接口（DescribeDefaultParameters）主要用于查询某个数据库版本和引擎支持的所有参数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEncryptionKeys(
            self,
            request: models.DescribeEncryptionKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeEncryptionKeysResponse:
        """
        本接口 （DescribeEncryptionKeys） 用于查询实例的密钥信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEncryptionKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEncryptionKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogBackups(
            self,
            request: models.DescribeLogBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogBackupsResponse:
        """
        本接口（DescribeLogBackups）用于查询日志备份列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintainTimeWindow(
            self,
            request: models.DescribeMaintainTimeWindowRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintainTimeWindowResponse:
        """
        本接口 (DescribeMaintainTimeWindow) 用于查询实例的维护时间窗口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintainTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintainTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrders(
            self,
            request: models.DescribeOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrdersResponse:
        """
        本接口（DescribeOrders）用于查询订单信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParameterTemplateAttributes(
            self,
            request: models.DescribeParameterTemplateAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeParameterTemplateAttributesResponse:
        """
        本接口（DescribeParameterTemplateAttributes）用于查询某个参数模板的具体内容，包括基本信息和参数信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParameterTemplateAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParameterTemplateAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParameterTemplates(
            self,
            request: models.DescribeParameterTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeParameterTemplatesResponse:
        """
        本接口 (DescribeParameterTemplates) 用于查询参数模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParameterTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParameterTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamsEvent(
            self,
            request: models.DescribeParamsEventRequest,
            opts: Dict = None,
    ) -> models.DescribeParamsEventResponse:
        """
        本接口（DescribeParamsEvent）用于查询参数修改事件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamsEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamsEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductConfig(
            self,
            request: models.DescribeProductConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeProductConfigResponse:
        """
        本接口（DescribeProductConfig）用于查询售卖规格配置。**本接口属于早期接口，已停止功能迭代，推荐使用新接口**[DescribeClasses](https://cloud.tencent.com/document/api/409/89019)**替代**。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroups(
            self,
            request: models.DescribeReadOnlyGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupsResponse:
        """
        本接口（DescribeReadOnlyGroups）用于查询只读组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupsResponse
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
        
    async def DescribeSlowQueryAnalysis(
            self,
            request: models.DescribeSlowQueryAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowQueryAnalysisResponse:
        """
        此接口（DescribeSlowQueryAnalysis）用于统计指定时间范围内的所有慢查询，根据SQL语句抽象参数后，进行聚合分析，并返回同类SQL列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowQueryAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowQueryAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowQueryList(
            self,
            request: models.DescribeSlowQueryListRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowQueryListResponse:
        """
        此接口（DescribeSlowQueryList）用于查询指定时间范围内的所有慢查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowQueryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowQueryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        本接口（DescribeTasks）用于查询任务列表，展示异步任务的执行进度。
        注：本接口中展示的步骤为总结性步骤，可能伴随着版本迭代进行调整，不建议作为关键逻辑使用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        本接口 (DescribeZones) 用于查询支持的可用区信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyDBInstance(
            self,
            request: models.DestroyDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyDBInstanceResponse:
        """
        本接口 (DestroyDBInstance) 用于彻底销毁指定DBInstanceId对应的实例，销毁后实例数据将彻底删除，无法找回，调用前请仔细确认要操作的实例。只能销毁隔离中的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisIsolateDBInstances(
            self,
            request: models.DisIsolateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DisIsolateDBInstancesResponse:
        """
        本接口（DisIsolateDBInstances）用于解隔离实例
        """
        
        kwargs = {}
        kwargs["action"] = "DisIsolateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisIsolateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateDBInstances(
            self,
            request: models.InquiryPriceCreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateDBInstancesResponse:
        """
        本接口 (InquiryPriceCreateDBInstances) 用于查询购买实例的价格信息。
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
        本接口（InquiryPriceRenewDBInstance）用于查询续费实例的价格。
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
        本接口（InquiryPriceUpgradeDBInstance）用于查询升级实例的价格。只支持按量计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstances(
            self,
            request: models.IsolateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstancesResponse:
        """
        本接口（IsolateDBInstances）用于隔离实例。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LockAccount(
            self,
            request: models.LockAccountRequest,
            opts: Dict = None,
    ) -> models.LockAccountResponse:
        """
        此接口用于锁定数据库账号，锁定后账号当前连接会断开，并且无法建立新连接。
        """
        
        kwargs = {}
        kwargs["action"] = "LockAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LockAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPrivileges(
            self,
            request: models.ModifyAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPrivilegesResponse:
        """
        修改某账号对某数据库对象的权限、修改账号类型。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountRemark(
            self,
            request: models.ModifyAccountRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountRemarkResponse:
        """
        本接口（ModifyAccountRemark）用于修改账号备注。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupDownloadRestriction(
            self,
            request: models.ModifyBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadRestrictionResponse:
        """
        本接口（ModifyBackupDownloadRestriction）用于修改备份文件下载限制。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupPlan(
            self,
            request: models.ModifyBackupPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupPlanResponse:
        """
        本接口 (ModifyBackupPlan) 用于实例备份计划的修改，默认是在每天的凌晨开始全量备份，备份保留时长是7天。可以根据此接口指定时间进行实例的备份。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaseBackupExpireTime(
            self,
            request: models.ModifyBaseBackupExpireTimeRequest,
            opts: Dict = None,
    ) -> models.ModifyBaseBackupExpireTimeResponse:
        """
        本接口（ModifyBaseBackupExpireTime）用于修改实例指定数据备份的过期时间。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaseBackupExpireTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaseBackupExpireTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceChargeType(
            self,
            request: models.ModifyDBInstanceChargeTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceChargeTypeResponse:
        """
        支持实例的计费类型转换（目前仅支持按量计费转包年包月）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceChargeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceDeletionProtection(
            self,
            request: models.ModifyDBInstanceDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceDeletionProtectionResponse:
        """
        本接口（DeletionProtection）用于开启或关闭实例销毁保护
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceDeployment(
            self,
            request: models.ModifyDBInstanceDeploymentRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceDeploymentResponse:
        """
        本接口（ModifyDBInstanceDeployment）用于修改节点可用区部署方式，仅支持主实例。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceDeployment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceDeploymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceHAConfig(
            self,
            request: models.ModifyDBInstanceHAConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceHAConfigResponse:
        """
        本接口（ModifyDBInstanceHAConfig）用于修改实例HA配置信息。其中HA配置信息包括：
        <li>允许备节点切换为主节点的条件配置</li>
        <li>半同步实例使用同步复制或异步复制的条件配置</li>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceHAConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceHAConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceName(
            self,
            request: models.ModifyDBInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNameResponse:
        """
        本接口（ModifyDBInstanceName）用于修改postgresql实例名字。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceParameters(
            self,
            request: models.ModifyDBInstanceParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceParametersResponse:
        """
        本接口 (ModifyDBInstanceParameters) 用于修改实例参数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceReadOnlyGroup(
            self,
            request: models.ModifyDBInstanceReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceReadOnlyGroupResponse:
        """
        本接口（ModifyDBInstanceReadOnlyGroup）用于修改实例所属的只读组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSSLConfig(
            self,
            request: models.ModifyDBInstanceSSLConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSSLConfigResponse:
        """
        本接口用于修改实例SSL配置，功能包含开启、关闭、修改SSL证书保护的连接地址。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSSLConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSSLConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        本接口（ModifyDBInstanceSecurityGroups）用于修改实例安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSpec(
            self,
            request: models.ModifyDBInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSpecResponse:
        """
        本接口（ModifyDBInstanceSpec）用于修改实例规格，包括内存、磁盘、Cpu。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstancesProject(
            self,
            request: models.ModifyDBInstancesProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstancesProjectResponse:
        """
        本接口（ModifyDBInstancesProject）用于修改实例所属项目。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstancesProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstancesProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseOwner(
            self,
            request: models.ModifyDatabaseOwnerRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseOwnerResponse:
        """
        修改数据库所有者
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintainTimeWindow(
            self,
            request: models.ModifyMaintainTimeWindowRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintainTimeWindowResponse:
        """
        本接口 (ModifyMaintainTimeWindow) 用于实例维护时间窗口的修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintainTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintainTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyParameterTemplate(
            self,
            request: models.ModifyParameterTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyParameterTemplateResponse:
        """
        本接口（ModifyParameterTemplate）主要用于修改参数模板名称，描述等配置，也可用于管理参数模板中的参数列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParameterTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParameterTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReadOnlyDBInstanceWeight(
            self,
            request: models.ModifyReadOnlyDBInstanceWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyReadOnlyDBInstanceWeightResponse:
        """
        本接口（ModifyReadOnlyDBInstanceWeight）用于修改只读实例权重
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReadOnlyDBInstanceWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReadOnlyDBInstanceWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReadOnlyGroupConfig(
            self,
            request: models.ModifyReadOnlyGroupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyReadOnlyGroupConfigResponse:
        """
        本接口(ModifyReadOnlyGroupConfig)用于更新只读组配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReadOnlyGroupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReadOnlyGroupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySwitchTimePeriod(
            self,
            request: models.ModifySwitchTimePeriodRequest,
            opts: Dict = None,
    ) -> models.ModifySwitchTimePeriodResponse:
        """
        当升级完成后，对处于等待切换状态下的实例，强制实例立即切换。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySwitchTimePeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySwitchTimePeriodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAccountCAM(
            self,
            request: models.OpenAccountCAMRequest,
            opts: Dict = None,
    ) -> models.OpenAccountCAMResponse:
        """
        本接口用于开启数据库账户的CAM验证服务。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAccountCAM"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAccountCAMResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenDBExtranetAccess(
            self,
            request: models.OpenDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.OpenDBExtranetAccessResponse:
        """
        本接口（OpenDBExtranetAccess）用于开通实例公网地址。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebalanceReadOnlyGroup(
            self,
            request: models.RebalanceReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.RebalanceReadOnlyGroupResponse:
        """
        本接口(RebalanceReadOnlyGroup)用于重新均衡 RO 组内实例的负载。注意，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库，谨慎操作。
        """
        
        kwargs = {}
        kwargs["action"] = "RebalanceReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebalanceReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshAccountPassword(
            self,
            request: models.RefreshAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.RefreshAccountPasswordResponse:
        """
        本接口用于对开启CAM验证的账户执行手动刷新密码。
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveDBInstanceFromReadOnlyGroup(
            self,
            request: models.RemoveDBInstanceFromReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveDBInstanceFromReadOnlyGroupResponse:
        """
        本接口（RemoveDBInstanceFromReadOnlyGroup）用户将只读实例从只读组中移除
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveDBInstanceFromReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveDBInstanceFromReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstance(
            self,
            request: models.RenewInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewInstanceResponse:
        """
        本接口（RenewInstance）用于续费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        本接口（ResetAccountPassword）用于重置实例的账户密码。
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
        本接口（RestartDBInstance）用于重启实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreDBInstanceObjects(
            self,
            request: models.RestoreDBInstanceObjectsRequest,
            opts: Dict = None,
    ) -> models.RestoreDBInstanceObjectsResponse:
        """
        根据备份集或恢复目标时间，在原实例上恢复数据库相关对象，例如数据库、表。
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreDBInstanceObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreDBInstanceObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAutoRenewFlag(
            self,
            request: models.SetAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.SetAutoRenewFlagResponse:
        """
        本接口（SetAutoRenewFlag）用于设置自动续费。
        """
        
        kwargs = {}
        kwargs["action"] = "SetAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDBInstancePrimary(
            self,
            request: models.SwitchDBInstancePrimaryRequest,
            opts: Dict = None,
    ) -> models.SwitchDBInstancePrimaryResponse:
        """
        本接口（SwitchDBInstancePrimary）用于切换实例主备关系。
        <li>通过主动发起切换，可以验证业务能否正确处理实例主备切换的场景</li>
        <li>通过使用强制切换，可以在备节点延迟不满足切换条件时，强制发起主从切换</li>
        <li>只有主实例可以执行该操作</li>
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDBInstancePrimary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDBInstancePrimaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnlockAccount(
            self,
            request: models.UnlockAccountRequest,
            opts: Dict = None,
    ) -> models.UnlockAccountResponse:
        """
        解除数据库账号的锁定，解锁后账号可以登录数据库。
        """
        
        kwargs = {}
        kwargs["action"] = "UnlockAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnlockAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceKernelVersion(
            self,
            request: models.UpgradeDBInstanceKernelVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceKernelVersionResponse:
        """
        本接口（UpgradeDBInstanceKernelVersion）用于升级实例的内核版本号。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceKernelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceKernelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceMajorVersion(
            self,
            request: models.UpgradeDBInstanceMajorVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceMajorVersionResponse:
        """
        本接口（UpgradeDBInstanceMajorVersion）用于升级实例内核大版本，例如从PostgreSQL 12升级到PostgreSQL 15。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceMajorVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceMajorVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)