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
from tencentcloud.mongodb.v20190725 import models
from typing import Dict


class MongodbClient(AbstractClient):
    _apiVersion = '2019-07-25'
    _endpoint = 'mongodb.tencentcloudapi.com'
    _service = 'mongodb'

    async def AssignProject(
            self,
            request: models.AssignProjectRequest,
            opts: Dict = None,
    ) -> models.AssignProjectResponse:
        """
        本接口(AssignProject)用于指定云数据库实例的所属项目。
        """
        
        kwargs = {}
        kwargs["action"] = "AssignProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccountUser(
            self,
            request: models.CreateAccountUserRequest,
            opts: Dict = None,
    ) -> models.CreateAccountUserResponse:
        """
        本接口（CreateAccountUser）用于自定义实例访问账号。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccountUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditLogFile(
            self,
            request: models.CreateAuditLogFileRequest,
            opts: Dict = None,
    ) -> models.CreateAuditLogFileResponse:
        """
        本接口(CreateAuditLogFile)用于创建云数据库实例的审计日志文件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupDBInstance(
            self,
            request: models.CreateBackupDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateBackupDBInstanceResponse:
        """
        本接口（CreateBackupDBInstance）用于备份实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupDownloadTask(
            self,
            request: models.CreateBackupDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.CreateBackupDownloadTaskResponse:
        """
        本接口用来创建某个备份文件的下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstance(
            self,
            request: models.CreateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceResponse:
        """
        本接口(CreateDBInstance)用于创建包年包月的MongoDB云数据库实例。接口支持的售卖规格，可通过接口查询 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/35767) 获取。
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
        本接口（CreateDBInstanceHour）用于创建按量计费的MongoDB云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstanceHour"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceHourResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstanceParamTpl(
            self,
            request: models.CreateDBInstanceParamTplRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceParamTplResponse:
        """
        本接口(CreateDBInstanceParamTpl)用于创建云数据库MongoDB实例的参数模板
        **说明：CreateDBInstanceParamTpl API正在公测中，在此期间，该接口仅对公测用户开放**
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstanceParamTpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceParamTplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogDownloadTask(
            self,
            request: models.CreateLogDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.CreateLogDownloadTaskResponse:
        """
        创建日志下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccountUser(
            self,
            request: models.DeleteAccountUserRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountUserResponse:
        """
        本接口（DeleteAccountUser）用于删除实例的自定义账号。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccountUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountUserResponse
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
        
    async def DeleteLogDownloadTask(
            self,
            request: models.DeleteLogDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteLogDownloadTaskResponse:
        """
        删除日志下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountUsers(
            self,
            request: models.DescribeAccountUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountUsersResponse:
        """
        本接口（DescribeAccountUsers）用于获取当前实例的全部账号。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncRequestInfo(
            self,
            request: models.DescribeAsyncRequestInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncRequestInfoResponse:
        """
        本接口（DescribeAsyncRequestInfo）用于查询异步任务状态接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncRequestInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncRequestInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditInstanceList(
            self,
            request: models.DescribeAuditInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditInstanceListResponse:
        """
        本接口（DescribeAuditInstanceList）用于查询开通或未开通数据库审计的实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadTask(
            self,
            request: models.DescribeBackupDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadTaskResponse:
        """
        本接口（DescribeBackupDownloadTask）用于查询备份下载任务信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupRules(
            self,
            request: models.DescribeBackupRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupRulesResponse:
        """
        本接口（DescribeBackupRules）用于获取实例自动备份配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientConnections(
            self,
            request: models.DescribeClientConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeClientConnectionsResponse:
        """
        本接口（DescribeClientConnections）用于查询实例客户端连接信息，包括连接 IP 和连接数量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCurrentOp(
            self,
            request: models.DescribeCurrentOpRequest,
            opts: Dict = None,
    ) -> models.DescribeCurrentOpResponse:
        """
        本接口（DescribeCurrentOp）用于查询云数据库实例的当前正在执行的操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurrentOp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurrentOpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBBackups(
            self,
            request: models.DescribeDBBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBBackupsResponse:
        """
        本接口（DescribeDBBackups）用于查询实例备份列表，目前只支持查询7天内的备份记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceDeal(
            self,
            request: models.DescribeDBInstanceDealRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceDealResponse:
        """
        本接口（DescribeDBInstanceDeal）用于获取MongoDB购买、续费及变配订单详细。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceDeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceDealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceNamespace(
            self,
            request: models.DescribeDBInstanceNamespaceRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceNamespaceResponse:
        """
        本接口（DescribeDBInstanceNamespace）用于查询数据库的表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceNodeProperty(
            self,
            request: models.DescribeDBInstanceNodePropertyRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceNodePropertyResponse:
        """
        本接口用于查询节点的属性，包括节点所在可用区、节点名称、地址、角色、状态、主从延迟、优先级、投票权、标签等属性。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceNodeProperty"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceNodePropertyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceParamTpl(
            self,
            request: models.DescribeDBInstanceParamTplRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceParamTplResponse:
        """
        本接口(DescribeDBInstanceParamTpl )用于查询当前账号下所有MongoDB数据库参数模板
        **说明：DescribeDBInstanceParamTpl  API正在公测中，在此期间，该接口仅对公测用户开放**
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceParamTpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceParamTplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceParamTplDetail(
            self,
            request: models.DescribeDBInstanceParamTplDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceParamTplDetailResponse:
        """
        本接口(DescribeDBInstanceParamTplDetail )用于查询MongoDB云数据库实例的参数模板详情。
        **说明：DescribeDBInstanceParamTplDetail  API正在公测中，在此期间，该接口仅对公测用户开放**
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceParamTplDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceParamTplDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceURL(
            self,
            request: models.DescribeDBInstanceURLRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceURLResponse:
        """
        本接口（DescribeDBInstanceURL）用于获取指定实例的 URI 形式的连接串访问地址示例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        本接口（DescribeDBInstances）用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选主实例、灾备实例和只读实例信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDetailedSlowLogs(
            self,
            request: models.DescribeDetailedSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDetailedSlowLogsResponse:
        """
        本接口（DescribeDetailedSlowLogs）用于查询实例慢日志详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDetailedSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDetailedSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParams(
            self,
            request: models.DescribeInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamsResponse:
        """
        本接口（DescribeInstanceParams）用于查询当前实例可修改的参数列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSSL(
            self,
            request: models.DescribeInstanceSSLRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSSLResponse:
        """
        查看实例SSL开启状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogDownloadTasks(
            self,
            request: models.DescribeLogDownloadTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeLogDownloadTasksResponse:
        """
        日志下载任务查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogDownloadTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogDownloadTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMongodbLogs(
            self,
            request: models.DescribeMongodbLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeMongodbLogsResponse:
        """
        该接口（DescribeMongodbLogs）用于查询运行日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMongodbLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMongodbLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroup(
            self,
            request: models.DescribeSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupResponse:
        """
        本接口（DescribeSecurityGroup）用于查询实例绑定的安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogPatterns(
            self,
            request: models.DescribeSlowLogPatternsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogPatternsResponse:
        """
        本接口（DescribeSlowLogPatterns）用于获取数据库实例慢日志的统计信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogPatterns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogPatternsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogs(
            self,
            request: models.DescribeSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogsResponse:
        """
        本接口（DescribeSlowLogs）用于获取云数据库慢日志信息。接口只支持查询最近7天内慢日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecInfo(
            self,
            request: models.DescribeSpecInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecInfoResponse:
        """
        本接口（DescribeSpecInfo）用于查询实例的售卖规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTransparentDataEncryptionStatus(
            self,
            request: models.DescribeTransparentDataEncryptionStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTransparentDataEncryptionStatusResponse:
        """
        获取实例透明加密的开启状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTransparentDataEncryptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTransparentDataEncryptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropDBInstanceParamTpl(
            self,
            request: models.DropDBInstanceParamTplRequest,
            opts: Dict = None,
    ) -> models.DropDBInstanceParamTplResponse:
        """
        本接口(DropDBInstanceParamTpl )用于删除云数据库MongoDB实例的参数模板
        **说明：DropDBInstanceParamTpl  API正在公测中，在此期间，该接口仅对公测用户开放**
        """
        
        kwargs = {}
        kwargs["action"] = "DropDBInstanceParamTpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropDBInstanceParamTplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableTransparentDataEncryption(
            self,
            request: models.EnableTransparentDataEncryptionRequest,
            opts: Dict = None,
    ) -> models.EnableTransparentDataEncryptionResponse:
        """
        本接口（EnableTransparentDataEncryption）用于开启云数据库 MongoDB 的透明加密能力。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableTransparentDataEncryption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableTransparentDataEncryptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FlashBackDBInstance(
            self,
            request: models.FlashBackDBInstanceRequest,
            opts: Dict = None,
    ) -> models.FlashBackDBInstanceResponse:
        """
        该接口用于发起按 Key 闪回任务，依据数据的闪回 Key（默认为 id）对数据进行极速回档，快速恢复业务。
        **说明：按 Key 闪回于2023年09月11日正式进行公测，在此期间，该接口仅对公测用户开放。**
        """
        
        kwargs = {}
        kwargs["action"] = "FlashBackDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FlashBackDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FlushInstanceRouterConfig(
            self,
            request: models.FlushInstanceRouterConfigRequest,
            opts: Dict = None,
    ) -> models.FlushInstanceRouterConfigResponse:
        """
        在所有mongos上执行FlushRouterConfig命令
        """
        
        kwargs = {}
        kwargs["action"] = "FlushInstanceRouterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FlushInstanceRouterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateDBInstances(
            self,
            request: models.InquirePriceCreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateDBInstancesResponse:
        """
        本接口（InquirePriceCreateDBInstances）用于创建数据库实例询价。本接口参数中必须传入region参数，否则无法通过校验。本接口仅允许针对购买限制范围内的实例配置进行询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModifyDBInstanceSpec(
            self,
            request: models.InquirePriceModifyDBInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyDBInstanceSpecResponse:
        """
        本接口 (InquirePriceModifyDBInstanceSpec) 用于查询实例配置变更后的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModifyDBInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyDBInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRenewDBInstances(
            self,
            request: models.InquirePriceRenewDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRenewDBInstancesResponse:
        """
        本接口 (InquiryPriceRenewDBInstances) 用于续费包年包月实例询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRenewDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRenewDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstanceEnableSSL(
            self,
            request: models.InstanceEnableSSLRequest,
            opts: Dict = None,
    ) -> models.InstanceEnableSSLResponse:
        """
        本接口（InstanceEnableSSL）用于设置实例SSL状态。
        """
        
        kwargs = {}
        kwargs["action"] = "InstanceEnableSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstanceEnableSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstance(
            self,
            request: models.IsolateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstanceResponse:
        """
        本接口（IsolateDBInstance）用于隔离 MongoDB 云数据库按量计费实例。隔离后实例保留在回收站中，不能再写入数据。隔离一定时间后，实例会彻底删除，回收站保存时间请参考按量计费的服务条款。已删除的按量计费实例无法恢复，请谨慎操作。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillOps(
            self,
            request: models.KillOpsRequest,
            opts: Dict = None,
    ) -> models.KillOpsResponse:
        """
        本接口（KillOps）用于终止 MongoDB 云数据库实例上执行的特定操作。
        """
        
        kwargs = {}
        kwargs["action"] = "KillOps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillOpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditService(
            self,
            request: models.ModifyAuditServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditServiceResponse:
        """
        本接口(ModifyAuditService)用于修改云数据库审计策略的服务配置，包括审计日志保存时长等。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceNetworkAddress(
            self,
            request: models.ModifyDBInstanceNetworkAddressRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNetworkAddressResponse:
        """
        本接口（ModifyDBInstanceNetworkAddress）用于修改云数据库实例的网络信息，支持基础网络切换为私有网络、私有网络切换私有网络。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceNetworkAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNetworkAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceParamTpl(
            self,
            request: models.ModifyDBInstanceParamTplRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceParamTplResponse:
        """
        本接口(ModifyDBInstanceParamTpl )用于修改MongoDB云数据库实例的参数模板。
        **说明：ModifyDBInstanceParamTpl  API正在公测中，在此期间，该接口仅对公测用户开放**
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceParamTpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceParamTplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroup(
            self,
            request: models.ModifyDBInstanceSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupResponse:
        """
        本接口（ModifyDBInstanceSecurityGroup）用于修改实例绑定的安全组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSpec(
            self,
            request: models.ModifyDBInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSpecResponse:
        """
        本接口（ModifyDBInstanceSpec）用于调整MongoDB云数据库实例配置。接口支持的售卖规格，可从查询云数据库的售卖规格（[DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567)）获取。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParams(
            self,
            request: models.ModifyInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamsResponse:
        """
        本接口（ModifyInstanceParams）用于修改mongoDB实例的参数配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineIsolatedDBInstance(
            self,
            request: models.OfflineIsolatedDBInstanceRequest,
            opts: Dict = None,
    ) -> models.OfflineIsolatedDBInstanceResponse:
        """
        本接口(OfflineIsolatedDBInstance)用于立即下线隔离状态的云数据库实例。进行操作的实例状态必须为隔离状态。
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineIsolatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineIsolatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAuditService(
            self,
            request: models.OpenAuditServiceRequest,
            opts: Dict = None,
    ) -> models.OpenAuditServiceResponse:
        """
        本接口(OpenAuditService)用于开通云数据库实例的审计。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenameInstance(
            self,
            request: models.RenameInstanceRequest,
            opts: Dict = None,
    ) -> models.RenameInstanceResponse:
        """
        本接口(RenameInstance)用于修改云数据库实例的名称。
        """
        
        kwargs = {}
        kwargs["action"] = "RenameInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenameInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDBInstances(
            self,
            request: models.RenewDBInstancesRequest,
            opts: Dict = None,
    ) -> models.RenewDBInstancesResponse:
        """
        本接口(RenewDBInstance)用于续费云数据库实例，仅支持付费模式为包年包月的实例。按量计费实例不需要续费。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDBInstancePassword(
            self,
            request: models.ResetDBInstancePasswordRequest,
            opts: Dict = None,
    ) -> models.ResetDBInstancePasswordResponse:
        """
        本接口（ResetDBInstancePassword）用于重置实例访问密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDBInstancePassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDBInstancePasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartNodes(
            self,
            request: models.RestartNodesRequest,
            opts: Dict = None,
    ) -> models.RestartNodesResponse:
        """
        本接口（RestartNodes）用于批量重启数据库节点。
        """
        
        kwargs = {}
        kwargs["action"] = "RestartNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAccountUserPrivilege(
            self,
            request: models.SetAccountUserPrivilegeRequest,
            opts: Dict = None,
    ) -> models.SetAccountUserPrivilegeResponse:
        """
        本接口（SetAccountUserPrivilege）用于设置实例的账号权限。
        """
        
        kwargs = {}
        kwargs["action"] = "SetAccountUserPrivilege"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAccountUserPrivilegeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetBackupRules(
            self,
            request: models.SetBackupRulesRequest,
            opts: Dict = None,
    ) -> models.SetBackupRulesResponse:
        """
        本接口（SetBackupRules）用于设置 MongoDB 云数据库的自动备份规则。
        """
        
        kwargs = {}
        kwargs["action"] = "SetBackupRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetBackupRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDBInstanceDeletionProtection(
            self,
            request: models.SetDBInstanceDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.SetDBInstanceDeletionProtectionResponse:
        """
        本接口（SetDBInstanceDeletionProtection）用于设置实例销毁保护
        """
        
        kwargs = {}
        kwargs["action"] = "SetDBInstanceDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDBInstanceDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetInstanceMaintenance(
            self,
            request: models.SetInstanceMaintenanceRequest,
            opts: Dict = None,
    ) -> models.SetInstanceMaintenanceResponse:
        """
        本接口（SetInstanceMaintenance ） 用于设置实例维护时间窗。
        """
        
        kwargs = {}
        kwargs["action"] = "SetInstanceMaintenance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetInstanceMaintenanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDBInstances(
            self,
            request: models.TerminateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateDBInstancesResponse:
        """
        本接口（TerminateDBInstances）用于退还包年包月计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceKernelVersion(
            self,
            request: models.UpgradeDBInstanceKernelVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceKernelVersionResponse:
        """
        本接口(UpgradeDBInstanceKernelVersion)用于升级数据库实例内核版本。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceKernelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceKernelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDbInstanceVersion(
            self,
            request: models.UpgradeDbInstanceVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDbInstanceVersionResponse:
        """
        本接口用于跨版本升级数据库内核。当前仅支持3.6版本升级为4.0版本、4.0版本升级为4.2版本、4.2版本升级为4.4版本及4.4版本升级为5.0版本。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDbInstanceVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDbInstanceVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)