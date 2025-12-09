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
from tencentcloud.cdb.v20170320 import models
from typing import Dict


class CdbClient(AbstractClient):
    _apiVersion = '2017-03-20'
    _endpoint = 'cdb.tencentcloudapi.com'
    _service = 'cdb'

    async def AddTimeWindow(
            self,
            request: models.AddTimeWindowRequest,
            opts: Dict = None,
    ) -> models.AddTimeWindowResponse:
        """
        本接口（AddTimeWindow）用于添加云数据库实例的维护时间窗口，以指定实例在哪些时间段可以自动执行切换访问操作。
        """
        
        kwargs = {}
        kwargs["action"] = "AddTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AdjustCdbProxy(
            self,
            request: models.AdjustCdbProxyRequest,
            opts: Dict = None,
    ) -> models.AdjustCdbProxyResponse:
        """
        本接口（AdjustCdbProxy）用于调整数据库代理配置。
        """
        
        kwargs = {}
        kwargs["action"] = "AdjustCdbProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdjustCdbProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AdjustCdbProxyAddress(
            self,
            request: models.AdjustCdbProxyAddressRequest,
            opts: Dict = None,
    ) -> models.AdjustCdbProxyAddressResponse:
        """
        本接口（AdjustCdbProxyAddress）用于调整数据库代理地址配置。
        """
        
        kwargs = {}
        kwargs["action"] = "AdjustCdbProxyAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdjustCdbProxyAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AnalyzeAuditLogs(
            self,
            request: models.AnalyzeAuditLogsRequest,
            opts: Dict = None,
    ) -> models.AnalyzeAuditLogsResponse:
        """
        本接口（AnalyzeAuditLogs）用于在不同过滤条件下的审计日志结果集中，选定特定的数据列进行聚合统计。
        """
        
        kwargs = {}
        kwargs["action"] = "AnalyzeAuditLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AnalyzeAuditLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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
        
    async def BalanceRoGroupLoad(
            self,
            request: models.BalanceRoGroupLoadRequest,
            opts: Dict = None,
    ) -> models.BalanceRoGroupLoadResponse:
        """
        本接口(BalanceRoGroupLoad)用于重新均衡 RO 组内实例的负载。注意，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库，谨慎操作。
        """
        
        kwargs = {}
        kwargs["action"] = "BalanceRoGroupLoad"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BalanceRoGroupLoadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckMigrateCluster(
            self,
            request: models.CheckMigrateClusterRequest,
            opts: Dict = None,
    ) -> models.CheckMigrateClusterResponse:
        """
        本接口（CheckMigrateCluster）用于高可用实例一键迁移到云盘版校验。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckMigrateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckMigrateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAuditService(
            self,
            request: models.CloseAuditServiceRequest,
            opts: Dict = None,
    ) -> models.CloseAuditServiceResponse:
        """
        实例关闭审计服务
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseCDBProxy(
            self,
            request: models.CloseCDBProxyRequest,
            opts: Dict = None,
    ) -> models.CloseCDBProxyResponse:
        """
        本接口（CloseCDBProxy）用于关闭数据库代理。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseCDBProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseCDBProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseCdbProxyAddress(
            self,
            request: models.CloseCdbProxyAddressRequest,
            opts: Dict = None,
    ) -> models.CloseCdbProxyAddressResponse:
        """
        本接口（CloseCdbProxyAddress）用于请求关闭数据库代理地址。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseCdbProxyAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseCdbProxyAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseSSL(
            self,
            request: models.CloseSSLRequest,
            opts: Dict = None,
    ) -> models.CloseSSLResponse:
        """
        本接口（CloseSSL）用于关闭 SSL 连接功能。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseWanService(
            self,
            request: models.CloseWanServiceRequest,
            opts: Dict = None,
    ) -> models.CloseWanServiceResponse:
        """
        本接口(CloseWanService)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseWanService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseWanServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccounts(
            self,
            request: models.CreateAccountsRequest,
            opts: Dict = None,
    ) -> models.CreateAccountsResponse:
        """
        本接口（CreateAccounts）用于创建云数据库的账户，需要指定新的账户名和域名，以及所对应的密码，同时可以设置账号的备注信息以及最大可用连接数。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditLogFile(
            self,
            request: models.CreateAuditLogFileRequest,
            opts: Dict = None,
    ) -> models.CreateAuditLogFileResponse:
        """
        本接口（CreateAuditLogFile）用于创建云数据库实例的审计日志文件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditPolicy(
            self,
            request: models.CreateAuditPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAuditPolicyResponse:
        """
        本接口(CreateAuditPolicy)用于创建云数据库实例的审计策略，即将审计规则绑定到具体的云数据库实例上。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditRule(
            self,
            request: models.CreateAuditRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAuditRuleResponse:
        """
        不再支持审计规则创建

        本接口(CreateAuditRule)用于创建用户在当前地域的审计规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditRuleTemplate(
            self,
            request: models.CreateAuditRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAuditRuleTemplateResponse:
        """
        本接口（CreateAuditRuleTemplate）用于创建审计规则模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackup(
            self,
            request: models.CreateBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupResponse:
        """
        本接口（CreateBackup）用于创建数据库备份。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCdbProxy(
            self,
            request: models.CreateCdbProxyRequest,
            opts: Dict = None,
    ) -> models.CreateCdbProxyResponse:
        """
        本接口（CreateCdbProxy）用于主实例创建数据库代理。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCdbProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCdbProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCdbProxyAddress(
            self,
            request: models.CreateCdbProxyAddressRequest,
            opts: Dict = None,
    ) -> models.CreateCdbProxyAddressResponse:
        """
        本接口（CreateCdbProxyAddress）用于数据库代理增加代理地址。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCdbProxyAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCdbProxyAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloneInstance(
            self,
            request: models.CreateCloneInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateCloneInstanceResponse:
        """
        本接口（CreateCloneInstance）用于从目标源实例创建一个克隆实例，可以指定克隆实例回档到源实例的指定物理备份文件或者指定的回档时间点。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloneInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloneInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBImportJob(
            self,
            request: models.CreateDBImportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDBImportJobResponse:
        """
        本接口（CreateDBImportJob）用于创建云数据库数据导入任务。
        注意，用户进行数据导入任务的文件，必须提前上传到腾讯云。用户须在控制台进行文件导入。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBImportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBImportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstance(
            self,
            request: models.CreateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceResponse:
        """
        本接口（CreateDBInstance）用于创建包年包月的云数据库实例（包括主实例、灾备实例和只读实例），可通过传入实例规格、MySQL 版本号、购买时长和数量等信息创建云数据库实例。

        该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为1，且 TaskStatus 为0，表示实例已经发货成功。

        1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；
        2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；
        3. 支持创建 MySQL 5.5 、 MySQL 5.6 、 MySQL 5.7 、 MySQL 8.0 版本；
        4. 支持创建主实例、只读实例、灾备实例；
        5. 当入参指定 ParamTemplateId 或 AlarmPolicyList 时，需将SDK提升至最新版本方可支持；
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstanceHour(
            self,
            request: models.CreateDBInstanceHourRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceHourResponse:
        """
        本接口（CreateDBInstanceHour）用于创建按量计费的实例，可通过传入实例规格、MySQL 版本号和数量等信息创建云数据库实例，支持主实例、灾备实例和只读实例的创建。

        该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为 1，且 TaskStatus 为 0，表示实例已经发货成功。

        1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；
        2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；
        3. 支持创建 MySQL 5.5、MySQL 5.6 、MySQL 5.7 和 MySQL 8.0 版本；
        4. 支持创建主实例、灾备实例和只读实例；
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstanceHour"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceHourResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatabase(
            self,
            request: models.CreateDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateDatabaseResponse:
        """
        本接口(CreateDatabase)用于在云数据库实例中创建数据库。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeployGroup(
            self,
            request: models.CreateDeployGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDeployGroupResponse:
        """
        本接口（CreateDeployGroup）用于创建放置实例的置放群组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeployGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeployGroupResponse
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
        说明：参数模板为公共组件，配置完成后全地域生效。接口调用配置地域可选择广州、新加坡。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoInstanceIp(
            self,
            request: models.CreateRoInstanceIpRequest,
            opts: Dict = None,
    ) -> models.CreateRoInstanceIpResponse:
        """
        本接口(CreateRoInstanceIp)用于创建云数据库只读实例的独立VIP。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoInstanceIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoInstanceIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRotationPassword(
            self,
            request: models.CreateRotationPasswordRequest,
            opts: Dict = None,
    ) -> models.CreateRotationPasswordResponse:
        """
        本接口（CreateRotationPassword）用于开启密码轮转。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRotationPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRotationPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccounts(
            self,
            request: models.DeleteAccountsRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountsResponse:
        """
        本接口（DeleteAccounts）用于删除云数据库的账户。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditLogFile(
            self,
            request: models.DeleteAuditLogFileRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditLogFileResponse:
        """
        本接口(DeleteAuditLogFile)用于删除云数据库实例的审计日志文件。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditPolicy(
            self,
            request: models.DeleteAuditPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditPolicyResponse:
        """
        本接口(DeleteAuditPolicy)用于删除用户的审计策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditRule(
            self,
            request: models.DeleteAuditRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditRuleResponse:
        """
        不再支持审计规则创建

        本接口(DeleteAuditRule)用于删除用户的审计规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditRuleTemplates(
            self,
            request: models.DeleteAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditRuleTemplatesResponse:
        """
        本接口（DeleteAuditRuleTemplates）用于删除审计规则模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackup(
            self,
            request: models.DeleteBackupRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupResponse:
        """
        本接口（DeleteBackup）用于删除数据库备份。本接口只支持删除手动发起的备份。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDatabase(
            self,
            request: models.DeleteDatabaseRequest,
            opts: Dict = None,
    ) -> models.DeleteDatabaseResponse:
        """
        本接口(DeleteDatabase)用于在云数据库实例中删除数据库。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeployGroups(
            self,
            request: models.DeleteDeployGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteDeployGroupsResponse:
        """
        根据置放群组ID删除置放群组（置放群组中有资源存在时不能删除该置放群组）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeployGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeployGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParamTemplate(
            self,
            request: models.DeleteParamTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParamTemplateResponse:
        """
        该接口（DeleteParamTemplate）用于删除参数模板。
        说明：参数模板为公共组件，配置完成后全地域生效。接口调用配置地域可选择广州、新加坡。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRotationPassword(
            self,
            request: models.DeleteRotationPasswordRequest,
            opts: Dict = None,
    ) -> models.DeleteRotationPasswordResponse:
        """
        本接口（DeleteRotationPassword）用于关闭实例账户密码轮转。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRotationPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRotationPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTimeWindow(
            self,
            request: models.DeleteTimeWindowRequest,
            opts: Dict = None,
    ) -> models.DeleteTimeWindowResponse:
        """
        本接口（DeleteTimeWindow）用于删除云数据库实例的维护时间窗口。删除实例维护时间窗口之后，默认的维护时间窗为每天的03:00-04:00，数据校验延迟阈值为10秒，即当选择在维护时间窗口内切换访问新实例时，默认会在03:00-04:00点进行切换访问新实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivileges(
            self,
            request: models.DescribeAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegesResponse:
        """
        本接口（DescribeAccountPrivileges）用于查询云数据库账户支持的权限信息。
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
        本接口（DescribeAccounts）用于查询云数据库的所有账户信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncRequestInfo(
            self,
            request: models.DescribeAsyncRequestInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncRequestInfoResponse:
        """
        本接口(DescribeAsyncRequestInfo)用于查询云数据库实例异步任务的执行结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncRequestInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncRequestInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditConfig(
            self,
            request: models.DescribeAuditConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditConfigResponse:
        """
        本接口(DescribeAuditConfig)用于查询云数据库审计策略的服务配置，包括审计日志保存时长等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditInstanceList(
            self,
            request: models.DescribeAuditInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditInstanceListResponse:
        """
        本接口（DescribeAuditInstanceList）用于获取审计实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLogFiles(
            self,
            request: models.DescribeAuditLogFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogFilesResponse:
        """
        本接口（DescribeAuditLogFiles）用于查询云数据库实例的审计日志文件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLogFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLogs(
            self,
            request: models.DescribeAuditLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogsResponse:
        """
        本接口（DescribeAuditLogs）用于查询数据库审计日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditPolicies(
            self,
            request: models.DescribeAuditPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditPoliciesResponse:
        """
        本接口（DescribeAuditPolicies）用于查询云数据库实例的审计策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRuleTemplateModifyHistory(
            self,
            request: models.DescribeAuditRuleTemplateModifyHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRuleTemplateModifyHistoryResponse:
        """
        本接口（DescribeAuditRuleTemplateModifyHistory）用于查询规则模板变更记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRuleTemplateModifyHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRuleTemplateModifyHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRuleTemplates(
            self,
            request: models.DescribeAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRuleTemplatesResponse:
        """
        本接口（DescribeAuditRuleTemplates）用于查询审计规则模板信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRules(
            self,
            request: models.DescribeAuditRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRulesResponse:
        """
        不再支持审计规则创建

        本接口(DescribeAuditRules)用于查询用户在当前地域的审计规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupConfig(
            self,
            request: models.DescribeBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupConfigResponse:
        """
        本接口（DescribeBackupConfig）用于查询数据库备份配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDecryptionKey(
            self,
            request: models.DescribeBackupDecryptionKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDecryptionKeyResponse:
        """
        本接口（DescribeBackupDecryptionKey）用于查询备份文件解密密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDecryptionKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDecryptionKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadRestriction(
            self,
            request: models.DescribeBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadRestrictionResponse:
        """
        该接口用户查询当前地域用户设置的默认备份下载来源限制。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupEncryptionStatus(
            self,
            request: models.DescribeBackupEncryptionStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupEncryptionStatusResponse:
        """
        本接口(DescribeBackupEncryptionStatus)用于查询实例默认备份加密状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupEncryptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupEncryptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupOverview(
            self,
            request: models.DescribeBackupOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupOverviewResponse:
        """
        本接口(DescribeBackupOverview)用于查询用户的备份概览。返回用户当前备份总个数、备份总的占用容量、赠送的免费容量、计费容量（容量单位为字节）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupSummaries(
            self,
            request: models.DescribeBackupSummariesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupSummariesResponse:
        """
        本接口（DescribeBackupSummaries）用于查询备份的统计情况，返回以实例为维度的备份占用容量，以及每个实例的数据备份和日志备份的个数和容量（容量单位为字节）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupSummaries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupSummariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackups(
            self,
            request: models.DescribeBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupsResponse:
        """
        本接口(DescribeBackups)用于查询云数据库实例的备份数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogBackupOverview(
            self,
            request: models.DescribeBinlogBackupOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogBackupOverviewResponse:
        """
        本接口(DescribeBinlogBackupOverview)用于查询用户在当前地域总的日志备份概览。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogBackupOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogBackupOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogs(
            self,
            request: models.DescribeBinlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogsResponse:
        """
        本接口(DescribeBinlogs)用于查询云数据库实例的 binlog 文件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCPUExpandStrategyInfo(
            self,
            request: models.DescribeCPUExpandStrategyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCPUExpandStrategyInfoResponse:
        """
        通过该 API 可以查询实例的 CPU 弹性扩容信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCPUExpandStrategyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCPUExpandStrategyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdbProxyInfo(
            self,
            request: models.DescribeCdbProxyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCdbProxyInfoResponse:
        """
        本接口（DescribeCdbProxyInfo）用于查询数据库代理详情信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdbProxyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdbProxyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdbZoneConfig(
            self,
            request: models.DescribeCdbZoneConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeCdbZoneConfigResponse:
        """
        本接口(DescribeCdbZoneConfig)用于查询云数据库各地域可售卖的规格配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdbZoneConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdbZoneConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloneList(
            self,
            request: models.DescribeCloneListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloneListResponse:
        """
        本接口（DescribeCloneList）用于查询用户实例的克隆任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloneList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloneListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInfo(
            self,
            request: models.DescribeClusterInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInfoResponse:
        """
        本接口（DescribeClusterInfo）用于查询云盘版实例信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCpuExpandHistory(
            self,
            request: models.DescribeCpuExpandHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeCpuExpandHistoryResponse:
        """
        本接口（DescribeCpuExpandHistory）用于查询扩容历史。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCpuExpandHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCpuExpandHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBFeatures(
            self,
            request: models.DescribeDBFeaturesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBFeaturesResponse:
        """
        本接口（DescribeDBFeatures）用于查询云数据库版本属性，包括是否支持数据库加密、数据库审计等功能。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBFeatures"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBFeaturesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBImportRecords(
            self,
            request: models.DescribeDBImportRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBImportRecordsResponse:
        """
        本接口(DescribeDBImportRecords)用于查询云数据库导入任务操作日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBImportRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBImportRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceCharset(
            self,
            request: models.DescribeDBInstanceCharsetRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceCharsetResponse:
        """
        本接口(DescribeDBInstanceCharset)用于查询云数据库实例的字符集，获取字符集的名称。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceCharset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceCharsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceConfig(
            self,
            request: models.DescribeDBInstanceConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceConfigResponse:
        """
        本接口（DescribeDBInstanceConfig）用于查询云数据库实例的配置信息，包括同步模式，部署模式等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceGTID(
            self,
            request: models.DescribeDBInstanceGTIDRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceGTIDResponse:
        """
        本接口(DescribeDBInstanceGTID)用于查询云数据库实例是否开通了 GTID，不支持版本为 5.5 以及以下的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceGTID"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceGTIDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceInfo(
            self,
            request: models.DescribeDBInstanceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceInfoResponse:
        """
        本接口（DescribeDBInstanceInfo）用于查询实例基本信息（实例 ID，实例名称，是否开通加密），只读实例不支持查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceLogToCLS(
            self,
            request: models.DescribeDBInstanceLogToCLSRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceLogToCLSResponse:
        """
        本接口（DescribeDBInstanceLogToCLS）用于查询实例慢日志、错误日志投递CLS的配置，通过AppId、Region以及实例ID过滤出当前实例日志投递CLS的配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceLogToCLS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceLogToCLSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceRebootTime(
            self,
            request: models.DescribeDBInstanceRebootTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceRebootTimeResponse:
        """
        本接口（DescribeDBInstanceRebootTime）用于查询云数据库实例重启预计所需的时间。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceRebootTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceRebootTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        本接口（DescribeDBInstances）用于查询云数据库实例列表，支持通过项目 ID、实例 ID、访问地址、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。
        说明：通过本接口返回的可用区情况为购买时的情况，不随主动 HA 切换变化。如需了解实时可用区情况，请通过 [DescribeDBInstanceConfig](https://cloud.tencent.com/document/product/236/17491) 接口进行查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBPrice(
            self,
            request: models.DescribeDBPriceRequest,
            opts: Dict = None,
    ) -> models.DescribeDBPriceResponse:
        """
        本接口（DescribeDBPrice）用于查询购买或续费云数据库实例的价格，支持查询按量计费或者包年包月的价格。可传入实例类型、购买时长、购买数量、内存大小、硬盘大小和可用区信息等来查询实例价格。可传入实例名称来查询实例续费价格。

        注意：对某个地域进行询价，请使用对应地域的接入点，接入点信息请参照 <a href="https://cloud.tencent.com/document/api/236/15832">服务地址</a> 文档。例如：对广州地域进行询价，请把请求发到：cdb.ap-guangzhou.tencentcloudapi.com。同理对上海地域询价，把请求发到：cdb.ap-shanghai.tencentcloudapi.com。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBPriceResponse
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
        
    async def DescribeDBSwitchRecords(
            self,
            request: models.DescribeDBSwitchRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSwitchRecordsResponse:
        """
        本接口(DescribeDBSwitchRecords)用于查询云数据库实例切换记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSwitchRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSwitchRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataBackupOverview(
            self,
            request: models.DescribeDataBackupOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDataBackupOverviewResponse:
        """
        本接口(DescribeDataBackupOverview)用于查询用户在当前地域总的数据备份概览。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataBackupOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataBackupOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        本接口(DescribeDatabases)用于查询云数据库实例的数据库信息，仅支持主实例和灾备实例，不支持只读实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultParams(
            self,
            request: models.DescribeDefaultParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultParamsResponse:
        """
        该接口（DescribeDefaultParams）用于查询默认的可设置参数列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeployGroupList(
            self,
            request: models.DescribeDeployGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeployGroupListResponse:
        """
        本接口(DescribeDeployGroupList)用于查询用户的置放群组列表，可以指定置放群组 ID 或置放群组名称。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeployGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeployGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceMonitorInfo(
            self,
            request: models.DescribeDeviceMonitorInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceMonitorInfoResponse:
        """
        本接口（DescribeDeviceMonitorInfo）用于查询云数据库物理机当天的监控信息，暂只支持内存488G、硬盘6T的实例查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceMonitorInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceMonitorInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeErrorLogData(
            self,
            request: models.DescribeErrorLogDataRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorLogDataResponse:
        """
        根据检索条件查询实例错误日志详情。只能查询一个月之内的错误日志。
        使用时需要注意：可能存在单条错误日志太大，导致整个http请求的回包太大，进而引发接口超时。一旦发生超时，建议您缩小查询时的Limit参数值，从而降低包的大小，让接口能够及时返回内容。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeErrorLogData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorLogDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceAlarmEvents(
            self,
            request: models.DescribeInstanceAlarmEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceAlarmEventsResponse:
        """
        本接口（DescribeInstanceAlarmEvents）用于查询实例发生的事件信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceAlarmEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceAlarmEventsResponse
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
        
    async def DescribeInstancePasswordComplexity(
            self,
            request: models.DescribeInstancePasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancePasswordComplexityResponse:
        """
        该接口（DescribeInstancePasswordComplexity）用于查询实例的密码复杂度参数列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancePasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancePasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceUpgradeCheckJob(
            self,
            request: models.DescribeInstanceUpgradeCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceUpgradeCheckJobResponse:
        """
        该接口（DescribeInstanceUpgradeCheckJob）查询实例版本升级校验任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceUpgradeCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceUpgradeCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceUpgradeType(
            self,
            request: models.DescribeInstanceUpgradeTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceUpgradeTypeResponse:
        """
        本接口（DescribeInstanceUpgradeType）用于查询数据库实例升级类型。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceUpgradeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceUpgradeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLocalBinlogConfig(
            self,
            request: models.DescribeLocalBinlogConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLocalBinlogConfigResponse:
        """
        该接口用于查询实例本地binlog保留策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLocalBinlogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLocalBinlogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplateInfo(
            self,
            request: models.DescribeParamTemplateInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplateInfoResponse:
        """
        该接口（DescribeParamTemplateInfo）用于查询参数模板详情。
        说明：参数模板为公共组件，配置完成后全地域生效。接口调用配置地域可选择广州、新加坡。
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
        该接口（DescribeParamTemplates）查询参数模板列表。
        说明：参数模板为公共组件，配置完成后全地域生效。接口调用配置地域可选择广州、新加坡。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplatesResponse
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
        
    async def DescribeProxyCustomConf(
            self,
            request: models.DescribeProxyCustomConfRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyCustomConfResponse:
        """
        查询代理规格配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyCustomConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyCustomConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySupportParam(
            self,
            request: models.DescribeProxySupportParamRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySupportParamResponse:
        """
        本接口（DescribeProxySupportParam）用于查询实例支持代理版本和参数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySupportParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySupportParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRemoteBackupConfig(
            self,
            request: models.DescribeRemoteBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeRemoteBackupConfigResponse:
        """
        本接口(DescribeRemoteBackupConfig)用于查询数据库异地备份配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRemoteBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRemoteBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoGroups(
            self,
            request: models.DescribeRoGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeRoGroupsResponse:
        """
        本接口（DescribeRoGroups）用于查询云数据库实例的所有的 RO 组的信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoMinScale(
            self,
            request: models.DescribeRoMinScaleRequest,
            opts: Dict = None,
    ) -> models.DescribeRoMinScaleResponse:
        """
        本接口(DescribeRoMinScale)用于获取只读实例购买、升级时的最小规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoMinScale"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoMinScaleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollbackRangeTime(
            self,
            request: models.DescribeRollbackRangeTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeRollbackRangeTimeResponse:
        """
        本接口(DescribeRollbackRangeTime)用于查询云数据库实例可回档的时间范围。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackRangeTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackRangeTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollbackTaskDetail(
            self,
            request: models.DescribeRollbackTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRollbackTaskDetailResponse:
        """
        本接口（DescribeRollbackTaskDetail）用于查询云数据库实例回档任务详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSSLStatus(
            self,
            request: models.DescribeSSLStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSSLStatusResponse:
        """
        本接口（DescribeSSLStatus）用于查询 SSL 开通情况。如果已经开通 SSL ，会同步返回证书下载链接。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogData(
            self,
            request: models.DescribeSlowLogDataRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogDataResponse:
        """
        本接口（DescribeSlowLogData）用于使用条件检索实例的慢日志。只允许查看一个月之内的慢日志。
        使用时需要注意：可能存在单条慢日志太大，导致整个http请求的回包太大，进而引发接口超时。一旦发生超时，建议您缩小查询时的Limit参数值，从而降低包的大小，让接口能够及时返回内容。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogs(
            self,
            request: models.DescribeSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogsResponse:
        """
        本接口（DescribeSlowLogs）用于获取云数据库实例的慢查询日志。
        说明：若单次查询数据量过大，则有可能响应超时，建议缩短单次查询时间范围，如一小时，避免导致超时。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportedPrivileges(
            self,
            request: models.DescribeSupportedPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportedPrivilegesResponse:
        """
        本接口(DescribeSupportedPrivileges)用于查询云数据库的支持的权限信息，包括全局权限，数据库权限，表权限以及列权限。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportedPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportedPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableColumns(
            self,
            request: models.DescribeTableColumnsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableColumnsResponse:
        """
        本接口（DescribeTableColumns）用于查询云数据库实例的指定数据库表的列信息，仅支持主实例和灾备实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableColumns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableColumnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTables(
            self,
            request: models.DescribeTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesResponse:
        """
        本接口(DescribeTables)用于查询云数据库实例的数据库表信息，仅支持主实例和灾备实例，不支持只读实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagsOfInstanceIds(
            self,
            request: models.DescribeTagsOfInstanceIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsOfInstanceIdsResponse:
        """
        本接口（DescribeTagsOfInstanceIds）用于获取云数据库实例的标签信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagsOfInstanceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsOfInstanceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        本接口(DescribeTasks)用于查询云数据库实例任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimeWindow(
            self,
            request: models.DescribeTimeWindowRequest,
            opts: Dict = None,
    ) -> models.DescribeTimeWindowResponse:
        """
        本接口(DescribeTimeWindow)用于查询云数据库实例的维护时间窗口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUploadedFiles(
            self,
            request: models.DescribeUploadedFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeUploadedFilesResponse:
        """
        本接口(DescribeUploadedFiles)用于查询用户导入的SQL文件列表，全地域公共参数Region均为ap-shanghai。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUploadedFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUploadedFilesResponse
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
        
    async def InquiryPriceUpgradeInstances(
            self,
            request: models.InquiryPriceUpgradeInstancesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceUpgradeInstancesResponse:
        """
        本接口（InquiryPriceUpgradeInstances）用于查询云数据库实例升级的价格，支持查询按量计费或者包年包月实例的升级价格，实例类型支持主实例、灾备实例和只读实例。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpgradeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpgradeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstance(
            self,
            request: models.IsolateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstanceResponse:
        """
        本接口（IsolateDBInstance）用于隔离云数据库实例，隔离后不能通过IP和端口访问数据库。隔离的实例可在回收站中进行开机。若为欠费隔离，请尽快进行充值。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountDescription(
            self,
            request: models.ModifyAccountDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountDescriptionResponse:
        """
        本接口(ModifyAccountDescription)用于修改云数据库账户的备注信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountHost(
            self,
            request: models.ModifyAccountHostRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountHostResponse:
        """
        本接口(ModifyAccountHost)用于修改云数据库账户的主机。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountMaxUserConnections(
            self,
            request: models.ModifyAccountMaxUserConnectionsRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountMaxUserConnectionsResponse:
        """
        本接口（ModifyAccountMaxUserConnections）用于修改云数据库账户最大可用连接数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountMaxUserConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountMaxUserConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPassword(
            self,
            request: models.ModifyAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPasswordResponse:
        """
        本接口(ModifyAccountPassword)用于修改云数据库账户的密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPasswordResponse
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

        注意，修改账号权限时，需要传入该账号下的全量权限信息。用户可以先通过 [查询云数据库账户的权限信息
        ](https://cloud.tencent.com/document/api/236/17500) 查询该账号下的全量权限信息，然后进行权限修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditConfig(
            self,
            request: models.ModifyAuditConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditConfigResponse:
        """
        本接口(ModifyAuditConfig)用于修改云数据库审计策略的服务配置，包括审计日志保存时长等。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditRule(
            self,
            request: models.ModifyAuditRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditRuleResponse:
        """
        不再支持审计规则创建

        本接口(ModifyAuditRule)用于修改用户的审计规则。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditRuleTemplates(
            self,
            request: models.ModifyAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditRuleTemplatesResponse:
        """
        修改审计规则模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditService(
            self,
            request: models.ModifyAuditServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditServiceResponse:
        """
        本接口(ModifyAuditService)用于修改云数据库审计日志保存时长、审计规则等服务配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoRenewFlag(
            self,
            request: models.ModifyAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoRenewFlagResponse:
        """
        本接口（ModifyAutoRenewFlag）用于修改云数据库实例的自动续费标记。仅支持包年包月的实例设置自动续费标记。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupConfig(
            self,
            request: models.ModifyBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupConfigResponse:
        """
        本接口（ModifyBackupConfig）用于修改数据库备份配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupDownloadRestriction(
            self,
            request: models.ModifyBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadRestrictionResponse:
        """
        该接口用于修改用户当前地域的备份文件限制下载来源，可以设置内外网均可下载、仅内网可下载，或内网指定的vpc、ip可以下载。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupEncryptionStatus(
            self,
            request: models.ModifyBackupEncryptionStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupEncryptionStatusResponse:
        """
        本接口(ModifyBackupEncryptionStatus)用于设置实例备份文件是否加密。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupEncryptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupEncryptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCdbProxyAddressDesc(
            self,
            request: models.ModifyCdbProxyAddressDescRequest,
            opts: Dict = None,
    ) -> models.ModifyCdbProxyAddressDescResponse:
        """
        本接口（ModifyCdbProxyAddressDesc）用于修改代理地址描述信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCdbProxyAddressDesc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCdbProxyAddressDescResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCdbProxyAddressVipAndVPort(
            self,
            request: models.ModifyCdbProxyAddressVipAndVPortRequest,
            opts: Dict = None,
    ) -> models.ModifyCdbProxyAddressVipAndVPortResponse:
        """
        本接口（ModifyCdbProxyAddressVipAndVPort）用于修改数据库代理地址VPC信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCdbProxyAddressVipAndVPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCdbProxyAddressVipAndVPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCdbProxyParam(
            self,
            request: models.ModifyCdbProxyParamRequest,
            opts: Dict = None,
    ) -> models.ModifyCdbProxyParamResponse:
        """
        本接口（ModifyCdbProxyParam）用于配置数据库代理参数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCdbProxyParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCdbProxyParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceLogToCLS(
            self,
            request: models.ModifyDBInstanceLogToCLSRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceLogToCLSResponse:
        """
        开启/关闭CDB慢日志、错误日志投递CLS
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceLogToCLS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceLogToCLSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceModes(
            self,
            request: models.ModifyDBInstanceModesRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceModesResponse:
        """
        该接口（ModifyDBInstanceModes）用于更改云数据库的模式。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceModes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceModesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceName(
            self,
            request: models.ModifyDBInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNameResponse:
        """
        本接口(ModifyDBInstanceName)用于修改云数据库实例的名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceProject(
            self,
            request: models.ModifyDBInstanceProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceProjectResponse:
        """
        本接口(ModifyDBInstanceProject)用于修改云数据库实例的所属项目。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceReadOnlyStatus(
            self,
            request: models.ModifyDBInstanceReadOnlyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceReadOnlyStatusResponse:
        """
        本接口（ModifyDBInstanceReadOnlyStatus）用户设置MySQL云数据库实例为只读
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceReadOnlyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceReadOnlyStatusResponse
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
        
    async def ModifyDBInstanceVipVport(
            self,
            request: models.ModifyDBInstanceVipVportRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceVipVportResponse:
        """
        本接口（ModifyDBInstanceVipVport）用于修改云数据库实例的IP和端口号，也可进行基础网络转 VPC 网络和 VPC 网络下的子网变更。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceVipVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceVipVportResponse
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
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancePasswordComplexity(
            self,
            request: models.ModifyInstancePasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancePasswordComplexityResponse:
        """
        本接口（ModifyInstancePasswordComplexity）用于修改云数据库实例的密码复杂度。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancePasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancePasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceTag(
            self,
            request: models.ModifyInstanceTagRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceTagResponse:
        """
        本接口(ModifyInstanceTag)用于对实例标签进行添加、修改或者删除。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLocalBinlogConfig(
            self,
            request: models.ModifyLocalBinlogConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyLocalBinlogConfigResponse:
        """
        本接口（ModifyLocalBinlogConfig）用于修改实例本地 binlog 保留策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLocalBinlogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLocalBinlogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNameOrDescByDpId(
            self,
            request: models.ModifyNameOrDescByDpIdRequest,
            opts: Dict = None,
    ) -> models.ModifyNameOrDescByDpIdResponse:
        """
        修改置放群组的名称或者描述
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNameOrDescByDpId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNameOrDescByDpIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyParamTemplate(
            self,
            request: models.ModifyParamTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyParamTemplateResponse:
        """
        该接口（ModifyParamTemplate）用于修改参数模板。
        说明：参数模板为公共组件，配置完成后全地域生效。接口调用配置地域可选择广州、新加坡。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectMode(
            self,
            request: models.ModifyProtectModeRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectModeResponse:
        """
        该接口（ModifyProtectMode）用于修改实例的同步方式。
        说明：仅专属集群可调用，该接口即将下线。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRemoteBackupConfig(
            self,
            request: models.ModifyRemoteBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyRemoteBackupConfigResponse:
        """
        本接口(ModifyRemoteBackupConfig)用于修改数据库异地备份配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRemoteBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRemoteBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoGroupInfo(
            self,
            request: models.ModifyRoGroupInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyRoGroupInfoResponse:
        """
        本接口（ModifyRoGroupInfo）用于更新云数据库只读组的信息。包括设置实例延迟超限剔除策略，设置只读实例读权重，设置复制延迟时间等。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoGroupVipVport(
            self,
            request: models.ModifyRoGroupVipVportRequest,
            opts: Dict = None,
    ) -> models.ModifyRoGroupVipVportResponse:
        """
        该接口（ModifyRoGroupVipVport）用于修改Ro组的vip和vport。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoGroupVipVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoGroupVipVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTimeWindow(
            self,
            request: models.ModifyTimeWindowRequest,
            opts: Dict = None,
    ) -> models.ModifyTimeWindowResponse:
        """
        本接口(ModifyTimeWindow)用于更新云数据库实例的维护时间窗口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineIsolatedInstances(
            self,
            request: models.OfflineIsolatedInstancesRequest,
            opts: Dict = None,
    ) -> models.OfflineIsolatedInstancesResponse:
        """
        本接口(OfflineIsolatedInstances)用于立即下线隔离状态的云数据库实例。进行操作的实例状态必须为隔离状态，即通过 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询到 Status 值为 5 的实例。

        该接口为异步操作，部分资源的回收可能存在延迟。您可以通过使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口，指定实例 InstanceId 和状态 Status 为 [5,6,7] 进行查询，其中5代表已隔离，6代表下线中，7代表已下线。若返回实例为空，则实例资源已全部释放。

        注意，实例下线后，相关资源和数据将无法找回，请谨慎操作。
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineIsolatedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineIsolatedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAuditService(
            self,
            request: models.OpenAuditServiceRequest,
            opts: Dict = None,
    ) -> models.OpenAuditServiceResponse:
        """
        本接口（OpenAuditService）用 CDB 实例开通审计服务。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenDBInstanceEncryption(
            self,
            request: models.OpenDBInstanceEncryptionRequest,
            opts: Dict = None,
    ) -> models.OpenDBInstanceEncryptionResponse:
        """
        本接口（OpenDBInstanceEncryption）用于启用实例数据存储加密功能，支持用户指定自定义密钥。

        注意，启用实例数据存储加密之前，需要进行以下操作：

        1、进行 [实例初始化](https://cloud.tencent.com/document/api/236/15873) 操作；

        2、开启 [KMS服务](https://console.cloud.tencent.com/kms2)；

        3、对云数据库(MySQL)[授予访问KMS密钥的权限](https://console.cloud.tencent.com/cam/role)，角色名为MySQL_QCSRole，预设策略名为QcloudAccessForMySQLRole；
        4、开启加密后不允许关闭。

        该 API 耗时可能到10s，客户端可能超时，如果调用 API 返回 InternalError ，请您调用 [DescribeDBInstanceInfo](https://cloud.tencent.com/document/product/236/44160) 确认后端加密是否开通成功，调用后参数 Encryption 为 YES 表示已开通成功。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenDBInstanceEncryption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenDBInstanceEncryptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenDBInstanceGTID(
            self,
            request: models.OpenDBInstanceGTIDRequest,
            opts: Dict = None,
    ) -> models.OpenDBInstanceGTIDResponse:
        """
        本接口(OpenDBInstanceGTID)用于开启云数据库实例的 GTID，只支持版本为 5.6 以及以上的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenDBInstanceGTID"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenDBInstanceGTIDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenSSL(
            self,
            request: models.OpenSSLRequest,
            opts: Dict = None,
    ) -> models.OpenSSLResponse:
        """
        本接口（OpenSSL）用于开启 SSL 连接功能。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenWanService(
            self,
            request: models.OpenWanServiceRequest,
            opts: Dict = None,
    ) -> models.OpenWanServiceResponse:
        """
        本接口(OpenWanService)用于开通实例外网访问。

        注意，实例开通外网访问之前，需要先将实例进行 [实例初始化](https://cloud.tencent.com/document/api/236/15873) 操作。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenWanService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenWanServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIsolatedDBInstances(
            self,
            request: models.ReleaseIsolatedDBInstancesRequest,
            opts: Dict = None,
    ) -> models.ReleaseIsolatedDBInstancesResponse:
        """
        本接口（ReleaseIsolatedDBInstances）用于恢复已隔离云数据库实例。仅用于按量计费实例的解隔离，包年包月实例的解隔离请使用 RenewDBInstance 。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIsolatedDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIsolatedDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReloadBalanceProxyNode(
            self,
            request: models.ReloadBalanceProxyNodeRequest,
            opts: Dict = None,
    ) -> models.ReloadBalanceProxyNodeResponse:
        """
        重新负载均衡数据库代理
        """
        
        kwargs = {}
        kwargs["action"] = "ReloadBalanceProxyNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReloadBalanceProxyNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDBInstance(
            self,
            request: models.RenewDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewDBInstanceResponse:
        """
        本接口（RenewDBInstance）用于续费云数据库实例，支持付费模式为包年包月的实例。按量计费实例可通过该接口续费为包年包月的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetPassword(
            self,
            request: models.ResetPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetPasswordResponse:
        """
        手动刷新轮转密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRootAccount(
            self,
            request: models.ResetRootAccountRequest,
            opts: Dict = None,
    ) -> models.ResetRootAccountResponse:
        """
        重置实例ROOT账号，初始化账号权限
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRootAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRootAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDBInstances(
            self,
            request: models.RestartDBInstancesRequest,
            opts: Dict = None,
    ) -> models.RestartDBInstancesResponse:
        """
        本接口（RestartDBInstances）用于重启云数据库实例。

        注意：
        1、本接口支持主实例、只读实例、灾备实例进行重启操作。
        2、实例状态必须为正常，并且没有其他异步任务在执行中。
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartBatchRollback(
            self,
            request: models.StartBatchRollbackRequest,
            opts: Dict = None,
    ) -> models.StartBatchRollbackResponse:
        """
        该接口（StartBatchRollback）用于批量回档云数据库实例的库表。
        """
        
        kwargs = {}
        kwargs["action"] = "StartBatchRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartBatchRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCpuExpand(
            self,
            request: models.StartCpuExpandRequest,
            opts: Dict = None,
    ) -> models.StartCpuExpandResponse:
        """
        通过该 API，可以开启 CPU 弹性扩容，包括一次性的手动扩容以及自动弹性扩容。
        """
        
        kwargs = {}
        kwargs["action"] = "StartCpuExpand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCpuExpandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartReplication(
            self,
            request: models.StartReplicationRequest,
            opts: Dict = None,
    ) -> models.StartReplicationResponse:
        """
        本接口（StartReplication）用于开启 RO 复制，从主实例同步数据。
        """
        
        kwargs = {}
        kwargs["action"] = "StartReplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartReplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCpuExpand(
            self,
            request: models.StopCpuExpandRequest,
            opts: Dict = None,
    ) -> models.StopCpuExpandResponse:
        """
        通过该API，可以关闭 CPU 弹性扩容。
        """
        
        kwargs = {}
        kwargs["action"] = "StopCpuExpand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCpuExpandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopDBImportJob(
            self,
            request: models.StopDBImportJobRequest,
            opts: Dict = None,
    ) -> models.StopDBImportJobResponse:
        """
        本接口（StopDBImportJob）用于终止数据导入任务。
        说明：只有未完成的导入任务支持被终止，且终止后已执行的 SQL 部分会被保留。
        """
        
        kwargs = {}
        kwargs["action"] = "StopDBImportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopDBImportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopReplication(
            self,
            request: models.StopReplicationRequest,
            opts: Dict = None,
    ) -> models.StopReplicationResponse:
        """
        本接口（StopReplication）用于停止 RO 复制，中断从主实例同步数据。
        """
        
        kwargs = {}
        kwargs["action"] = "StopReplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopReplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRollback(
            self,
            request: models.StopRollbackRequest,
            opts: Dict = None,
    ) -> models.StopRollbackResponse:
        """
        本接口（StopRollback）用于撤销实例正在进行的回档任务，该接口返回一个异步任务 ID。撤销结果可以通过 [DescribeAsyncRequestInfo](https://cloud.tencent.com/document/api/236/20410) 查询任务的执行情况。
        """
        
        kwargs = {}
        kwargs["action"] = "StopRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitInstanceUpgradeCheckJob(
            self,
            request: models.SubmitInstanceUpgradeCheckJobRequest,
            opts: Dict = None,
    ) -> models.SubmitInstanceUpgradeCheckJobResponse:
        """
        该接口（SubmitInstanceUpgradeCheckJob）提交实例版本升级校验任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitInstanceUpgradeCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitInstanceUpgradeCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchCDBProxy(
            self,
            request: models.SwitchCDBProxyRequest,
            opts: Dict = None,
    ) -> models.SwitchCDBProxyResponse:
        """
        本接口（SwitchCDBProxy）用于数据库代理配置变更或者升级版本后手动发起立即切换。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchCDBProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchCDBProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDBInstanceMasterSlave(
            self,
            request: models.SwitchDBInstanceMasterSlaveRequest,
            opts: Dict = None,
    ) -> models.SwitchDBInstanceMasterSlaveResponse:
        """
        该接口 (SwitchDBInstanceMasterSlave) 支持用户主动切换实例主从角色。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDBInstanceMasterSlave"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDBInstanceMasterSlaveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDrInstanceToMaster(
            self,
            request: models.SwitchDrInstanceToMasterRequest,
            opts: Dict = None,
    ) -> models.SwitchDrInstanceToMasterResponse:
        """
        本接口（SwitchDrInstanceToMaster）用于将云数据库灾备实例切换为主实例，注意请求必须发到灾备实例所在的地域。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDrInstanceToMaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDrInstanceToMasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchForUpgrade(
            self,
            request: models.SwitchForUpgradeRequest,
            opts: Dict = None,
    ) -> models.SwitchForUpgradeResponse:
        """
        本接口(SwitchForUpgrade)用于切换访问新实例，针对主升级中的实例处于待切换状态时，用户可主动发起该流程。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchForUpgrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchForUpgradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeCDBProxyVersion(
            self,
            request: models.UpgradeCDBProxyVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeCDBProxyVersionResponse:
        """
        本接口（UpgradeCDBProxyVersion）用于升级数据库代理版本。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeCDBProxyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeCDBProxyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstance(
            self,
            request: models.UpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceResponse:
        """
        本接口（UpgradeDBInstance）用于升级或降级云数据库实例的配置，实例类型支持主实例、灾备实例和只读实例。如果进行迁移业务，请一定填写实例规格（CPU、内存），不然系统会默认以最小允许规格传参。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceEngineVersion(
            self,
            request: models.UpgradeDBInstanceEngineVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceEngineVersionResponse:
        """
        本接口（UpgradeDBInstanceEngineVersion）用于升级云数据库实例版本，实例类型支持主实例、灾备实例和只读实例等。升级前请通过 [SubmitInstanceUpgradeCheckJob](https://cloud.tencent.com/document/product/236/110468) 提交升级检查任务，通过后才能升级。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceEngineVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceEngineVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyRootAccount(
            self,
            request: models.VerifyRootAccountRequest,
            opts: Dict = None,
    ) -> models.VerifyRootAccountResponse:
        """
        本接口(VerifyRootAccount)用于校验云数据库实例的 ROOT 账号是否有足够的权限进行授权操作。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyRootAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyRootAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)