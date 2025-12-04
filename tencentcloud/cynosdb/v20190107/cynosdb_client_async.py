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
from tencentcloud.cynosdb.v20190107 import models
from typing import Dict


class CynosdbClient(AbstractClient):
    _apiVersion = '2019-01-07'
    _endpoint = 'cynosdb.tencentcloudapi.com'
    _service = 'cynosdb'

    async def ActivateInstance(
            self,
            request: models.ActivateInstanceRequest,
            opts: Dict = None,
    ) -> models.ActivateInstanceResponse:
        """
        本接口（ActivateInstance）用于恢复已隔离的实例访问。
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddClusterSlaveZone(
            self,
            request: models.AddClusterSlaveZoneRequest,
            opts: Dict = None,
    ) -> models.AddClusterSlaveZoneResponse:
        """
        本接口（AddClusterSlaveZone）用于对集群开启多可用区部署。
        """
        
        kwargs = {}
        kwargs["action"] = "AddClusterSlaveZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddClusterSlaveZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddInstances(
            self,
            request: models.AddInstancesRequest,
            opts: Dict = None,
    ) -> models.AddInstancesResponse:
        """
        本接口（AddInstances）用于集群添加实例。
        """
        
        kwargs = {}
        kwargs["action"] = "AddInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        本接口（AssociateSecurityGroups）用于安全组批量绑定云资源。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindClusterResourcePackages(
            self,
            request: models.BindClusterResourcePackagesRequest,
            opts: Dict = None,
    ) -> models.BindClusterResourcePackagesResponse:
        """
        本接口（BindClusterResourcePackages）用于为集群绑定资源包。
        """
        
        kwargs = {}
        kwargs["action"] = "BindClusterResourcePackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindClusterResourcePackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAuditService(
            self,
            request: models.CloseAuditServiceRequest,
            opts: Dict = None,
    ) -> models.CloseAuditServiceResponse:
        """
        本接口（CloseAuditService）用于关闭 TDSQL-C MySQL 实例的数据库审计服务。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseClusterPasswordComplexity(
            self,
            request: models.CloseClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.CloseClusterPasswordComplexityResponse:
        """
        本接口（CloseClusterPasswordComplexity）用于关闭集群密码复杂度。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProxy(
            self,
            request: models.CloseProxyRequest,
            opts: Dict = None,
    ) -> models.CloseProxyResponse:
        """
        本接口（CloseProxy）用于关闭集群的数据库代理服务。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProxyEndPoint(
            self,
            request: models.CloseProxyEndPointRequest,
            opts: Dict = None,
    ) -> models.CloseProxyEndPointResponse:
        """
        本接口（CloseProxyEndPoint）用于关闭数据库代理连接地址。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProxyEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProxyEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseSSL(
            self,
            request: models.CloseSSLRequest,
            opts: Dict = None,
    ) -> models.CloseSSLResponse:
        """
        关闭SSL加密
        """
        
        kwargs = {}
        kwargs["action"] = "CloseSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseWan(
            self,
            request: models.CloseWanRequest,
            opts: Dict = None,
    ) -> models.CloseWanResponse:
        """
        本接口（CloseWan）用于关闭外网。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseWan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseWanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyClusterPasswordComplexity(
            self,
            request: models.CopyClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.CopyClusterPasswordComplexityResponse:
        """
        本接口（CopyClusterPasswordComplexity）用于复制集群密码复杂度。
        """
        
        kwargs = {}
        kwargs["action"] = "CopyClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccounts(
            self,
            request: models.CreateAccountsRequest,
            opts: Dict = None,
    ) -> models.CreateAccountsResponse:
        """
        本接口（CreateAccounts）用于创建用户账号。
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
        本接口(CreateAuditLogFile)用于创建云数据库实例的审计日志文件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditLogFileResponse
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
        本接口（CreateBackup）用于为集群创建手动备份。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSDelivery(
            self,
            request: models.CreateCLSDeliveryRequest,
            opts: Dict = None,
    ) -> models.CreateCLSDeliveryResponse:
        """
        本接口（CreateCLSDelivery）用于创建日志投递。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterDatabase(
            self,
            request: models.CreateClusterDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateClusterDatabaseResponse:
        """
        本接口（CreateClusterDatabase）用于创建数据库。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusters(
            self,
            request: models.CreateClustersRequest,
            opts: Dict = None,
    ) -> models.CreateClustersResponse:
        """
        本接口（CreateClusters）用于新购集群。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntegrateCluster(
            self,
            request: models.CreateIntegrateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateIntegrateClusterResponse:
        """
        本接口（CreateClusters）用于新购集群。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntegrateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntegrateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateParamTemplate(
            self,
            request: models.CreateParamTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateParamTemplateResponse:
        """
        本接口（CreateParamTemplate）用于创建参数模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxy(
            self,
            request: models.CreateProxyRequest,
            opts: Dict = None,
    ) -> models.CreateProxyResponse:
        """
        本接口（CreateProxy）用于开启集群的数据库代理。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxyEndPoint(
            self,
            request: models.CreateProxyEndPointRequest,
            opts: Dict = None,
    ) -> models.CreateProxyEndPointResponse:
        """
        本接口（CreateProxyEndPoint）用于创建数据库代理连接点。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxyEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourcePackage(
            self,
            request: models.CreateResourcePackageRequest,
            opts: Dict = None,
    ) -> models.CreateResourcePackageResponse:
        """
        本接口（CreateResourcePackage）用于新购资源包。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourcePackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourcePackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccounts(
            self,
            request: models.DeleteAccountsRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountsResponse:
        """
        本接口（DeleteAccounts）用于删除用户账号。
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
        本接口（DeleteAuditLogFile）用于删除云数据库实例的审计日志文件。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditLogFileResponse
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
        本接口（DeleteBackup）用于为集群删除手动备份，无法删除自动备份。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCLSDelivery(
            self,
            request: models.DeleteCLSDeliveryRequest,
            opts: Dict = None,
    ) -> models.DeleteCLSDeliveryResponse:
        """
        本接口（DeleteCLSDelivery）用于删除日志投递。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCLSDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCLSDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterDatabase(
            self,
            request: models.DeleteClusterDatabaseRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterDatabaseResponse:
        """
        本接口（DeleteClusterDatabase）用于删除数据库。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParamTemplate(
            self,
            request: models.DeleteParamTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParamTemplateResponse:
        """
        本接口（DeleteParamTemplate）用于删除用户创建的参数模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountAllGrantPrivileges(
            self,
            request: models.DescribeAccountAllGrantPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountAllGrantPrivilegesResponse:
        """
        本接口（DescribeAccountAllGrantPrivileges）用于查询账号所有可授予的权限。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountAllGrantPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountAllGrantPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivileges(
            self,
            request: models.DescribeAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegesResponse:
        """
        本接口（DescribeAccountPrivileges）用于查询账号已有权限。
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
        本接口（DescribeAccounts）用于查询数据库账号列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditInstanceList(
            self,
            request: models.DescribeAuditInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditInstanceListResponse:
        """
        本接口（DescribeAuditInstanceList）用于获取数据库审计的实例列表。
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
        本接口(DescribeAuditLogFiles)用于查询云数据库实例的审计日志文件。
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
        
    async def DescribeAuditRuleWithInstanceIds(
            self,
            request: models.DescribeAuditRuleWithInstanceIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRuleWithInstanceIdsResponse:
        """
        本接口（DescribeAuditRuleWithInstanceIds）用于获取实例的审计规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRuleWithInstanceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRuleWithInstanceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupConfig(
            self,
            request: models.DescribeBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupConfigResponse:
        """
        本接口（DescribeBackupConfig）用于获取指定集群的备份配置信息，包括全量备份时间段、备份文件保留时间。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadRestriction(
            self,
            request: models.DescribeBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadRestrictionResponse:
        """
        该接口用户查询当前地域用户设置的默认备份下载来源限制
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadUrl(
            self,
            request: models.DescribeBackupDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadUrlResponse:
        """
        本接口（DescribeBackupDownloadUrl）用于查询集群备份文件下载地址。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadUserRestriction(
            self,
            request: models.DescribeBackupDownloadUserRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadUserRestrictionResponse:
        """
        该接口用户查询当前地域用户级别设置的默认备份下载来源限制
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadUserRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadUserRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupList(
            self,
            request: models.DescribeBackupListRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupListResponse:
        """
        本接口（DescribeBackupList）用于查询集群的备份文件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogConfig(
            self,
            request: models.DescribeBinlogConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogConfigResponse:
        """
        该接口（DescribeBinlogConfig）用于查询binlog配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogDownloadUrl(
            self,
            request: models.DescribeBinlogDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogDownloadUrlResponse:
        """
        本接口（DescribeBinlogDownloadUrl）用于查询 Binlog 的下载地址。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogSaveDays(
            self,
            request: models.DescribeBinlogSaveDaysRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogSaveDaysResponse:
        """
        此接口（DescribeBinlogSaveDays）用于查询集群的Binlog保留天数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogSaveDays"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogSaveDaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogs(
            self,
            request: models.DescribeBinlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogsResponse:
        """
        本接口（DescribeBinlogs）用来查询集群 Binlog 日志列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChangedParamsAfterUpgrade(
            self,
            request: models.DescribeChangedParamsAfterUpgradeRequest,
            opts: Dict = None,
    ) -> models.DescribeChangedParamsAfterUpgradeResponse:
        """
        本接口（DescribeChangedParamsAfterUpgrade）用于查询升降配运行参数对比。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChangedParamsAfterUpgrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChangedParamsAfterUpgradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDatabaseTables(
            self,
            request: models.DescribeClusterDatabaseTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDatabaseTablesResponse:
        """
        获取table列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDatabaseTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDatabaseTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDatabases(
            self,
            request: models.DescribeClusterDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDatabasesResponse:
        """
        本接口（DescribeClusterDatabases）用于获取集群数据库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetail(
            self,
            request: models.DescribeClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailResponse:
        """
        该接口（DescribeClusterDetail）用于显示集群详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetailDatabases(
            self,
            request: models.DescribeClusterDetailDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailDatabasesResponse:
        """
        本接口（DescribeClusterDetailDatabases）用于查询数据库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetailDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstanceGroups(
            self,
            request: models.DescribeClusterInstanceGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstanceGroupsResponse:
        """
        本接口（DescribeClusterInstanceGrps）用于查询实例组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstanceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstanceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstanceGrps(
            self,
            request: models.DescribeClusterInstanceGrpsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstanceGrpsResponse:
        """
        本接口（DescribeClusterInstanceGrps）用于查询实例组信息。 该接口已废弃，推荐使用DescribeClusterInstanceGroups
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstanceGrps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstanceGrpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterParamLogs(
            self,
            request: models.DescribeClusterParamLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterParamLogsResponse:
        """
        本接口（DescribeClusterParamLogs）用于查询参数修改记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterParamLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterParamLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterParams(
            self,
            request: models.DescribeClusterParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterParamsResponse:
        """
        本接口（DescribeClusterParams）用于查询集群参数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPasswordComplexity(
            self,
            request: models.DescribeClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPasswordComplexityResponse:
        """
        本接口（DescribeClusterPasswordComplexity）用于查看集群密码复杂度详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterReadOnly(
            self,
            request: models.DescribeClusterReadOnlyRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterReadOnlyResponse:
        """
        本接口（DescribeClusterReadOnly）用于查询集群只读开关。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterReadOnly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterReadOnlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterTransparentEncryptInfo(
            self,
            request: models.DescribeClusterTransparentEncryptInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterTransparentEncryptInfoResponse:
        """
        查询集群透明加密信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterTransparentEncryptInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterTransparentEncryptInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        本接口（DescribeClusters）用于查询集群列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        本接口（DescribeDBSecurityGroups）用于查询实例安全组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlow(
            self,
            request: models.DescribeFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowResponse:
        """
        本接口（DescribeFlow）用于查询任务流信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceCLSLogDelivery(
            self,
            request: models.DescribeInstanceCLSLogDeliveryRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceCLSLogDeliveryResponse:
        """
        本接口（DescribeInstanceCLSLogDelivery）用于查询实例日志投递信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceCLSLogDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceCLSLogDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDetail(
            self,
            request: models.DescribeInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDetailResponse:
        """
        本接口(DescribeInstanceDetail)用于查询实例详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceErrorLogs(
            self,
            request: models.DescribeInstanceErrorLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceErrorLogsResponse:
        """
        本接口（DescribeInstanceErrorLogs）用于查询实例错误日志列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceErrorLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceErrorLogsResponse
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
        
    async def DescribeInstanceSlowQueries(
            self,
            request: models.DescribeInstanceSlowQueriesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSlowQueriesResponse:
        """
        此接口（DescribeInstanceSlowQueries）用于查询实例慢日志详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSlowQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSlowQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSpecs(
            self,
            request: models.DescribeInstanceSpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSpecsResponse:
        """
        本接口（DescribeInstanceSpecs）用于查询购买页可购买的实例规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        本接口(DescribeInstances)用于查询实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesWithinSameCluster(
            self,
            request: models.DescribeInstancesWithinSameClusterRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesWithinSameClusterResponse:
        """
        本接口（DescribeInstancesWithinSameCluster）用于查询同一集群下实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesWithinSameCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesWithinSameClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrateTask(
            self,
            request: models.DescribeIntegrateTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrateTaskResponse:
        """
        本接口（DescribeIntegrateTask）用于查询集群任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIsolatedInstances(
            self,
            request: models.DescribeIsolatedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeIsolatedInstancesResponse:
        """
        本接口（DescribeIsolatedInstances）用于查询回收站实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIsolatedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIsolatedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintainPeriod(
            self,
            request: models.DescribeMaintainPeriodRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintainPeriodResponse:
        """
        本接口（DescribeMaintainPeriod）用于查询实例维护时间窗。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintainPeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintainPeriodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplateDetail(
            self,
            request: models.DescribeParamTemplateDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplateDetailResponse:
        """
        本接口（DescribeParamTemplateDetail）用于查询用户参数模板详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplateDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplateDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplates(
            self,
            request: models.DescribeParamTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplatesResponse:
        """
        本接口（DescribeParamTemplates）用于查询用户指定产品下的所有参数模板信息。
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
        本接口（DescribeProjectSecurityGroups）用于查询项目安全组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxies(
            self,
            request: models.DescribeProxiesRequest,
            opts: Dict = None,
    ) -> models.DescribeProxiesResponse:
        """
        本接口（DescribeProxies）用于查询数据库代理列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyNodes(
            self,
            request: models.DescribeProxyNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyNodesResponse:
        """
        本接口（DescribeProxyNodes）用于查询代理节点列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySpecs(
            self,
            request: models.DescribeProxySpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySpecsResponse:
        """
        本接口（DescribeProxySpecs）用于查询数据库代理规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcePackageDetail(
            self,
            request: models.DescribeResourcePackageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcePackageDetailResponse:
        """
        本接口（DescribeResourcePackageDetail）用于查询资源包使用详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcePackageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcePackageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcePackageList(
            self,
            request: models.DescribeResourcePackageListRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcePackageListResponse:
        """
        本接口（DescribeResourcePackageList）用于查询资源包列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcePackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcePackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcePackageSaleSpec(
            self,
            request: models.DescribeResourcePackageSaleSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcePackageSaleSpecResponse:
        """
        本接口（DescribeResourcePackageSaleSpec）用于查询资源包规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcePackageSaleSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcePackageSaleSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByDealName(
            self,
            request: models.DescribeResourcesByDealNameRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByDealNameResponse:
        """
        本接口（DescribeResourcesByDealName）用于查询订单关联实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByDealName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByDealNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollbackTimeRange(
            self,
            request: models.DescribeRollbackTimeRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeRollbackTimeRangeResponse:
        """
        本接口（DescribeRollbackTimeRange）用于查询回档时间范围。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackTimeRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackTimeRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSSLStatus(
            self,
            request: models.DescribeSSLStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSSLStatusResponse:
        """
        查询实例SSL状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessInstanceSpecs(
            self,
            request: models.DescribeServerlessInstanceSpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessInstanceSpecsResponse:
        """
        查询Serverless实例可选规格
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessInstanceSpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessInstanceSpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessStrategy(
            self,
            request: models.DescribeServerlessStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessStrategyResponse:
        """
        查询serverless策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlaveZones(
            self,
            request: models.DescribeSlaveZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeSlaveZonesResponse:
        """
        查询从可用区
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlaveZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlaveZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportProxyVersion(
            self,
            request: models.DescribeSupportProxyVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportProxyVersionResponse:
        """
        本接口（DescribeSupportProxyVersion）用于查询支持的数据库代理版本。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportProxyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportProxyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        本接口（DescribeTasks）用于查询任务列表。
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
        本接口（DescribeZones）用于查询可售卖地域可用区信息。
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
        本接口（DisassociateSecurityGroups）用于安全组批量解绑云资源。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportInstanceErrorLogs(
            self,
            request: models.ExportInstanceErrorLogsRequest,
            opts: Dict = None,
    ) -> models.ExportInstanceErrorLogsResponse:
        """
        此接口（ExportInstanceErrorLogs）用于导出实例错误日志。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportInstanceErrorLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportInstanceErrorLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportInstanceSlowQueries(
            self,
            request: models.ExportInstanceSlowQueriesRequest,
            opts: Dict = None,
    ) -> models.ExportInstanceSlowQueriesResponse:
        """
        本接口（ExportInstanceSlowQueries）用于导出实例慢日志。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportInstanceSlowQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportInstanceSlowQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportResourcePackageDeductDetails(
            self,
            request: models.ExportResourcePackageDeductDetailsRequest,
            opts: Dict = None,
    ) -> models.ExportResourcePackageDeductDetailsResponse:
        """
        资源包使用明细导出
        """
        
        kwargs = {}
        kwargs["action"] = "ExportResourcePackageDeductDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportResourcePackageDeductDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GrantAccountPrivileges(
            self,
            request: models.GrantAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.GrantAccountPrivilegesResponse:
        """
        本接口（GrantAccountPrivileges）用于批量授权账号权限。
        """
        
        kwargs = {}
        kwargs["action"] = "GrantAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GrantAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreate(
            self,
            request: models.InquirePriceCreateRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateResponse:
        """
        本接口（InquirePriceCreate）用于新购集群的价格查询。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModify(
            self,
            request: models.InquirePriceModifyRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyResponse:
        """
        变配预付费集群询价
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceMultiSpec(
            self,
            request: models.InquirePriceMultiSpecRequest,
            opts: Dict = None,
    ) -> models.InquirePriceMultiSpecResponse:
        """
        此接口（InquirePriceMultiSpec）用于批量询价
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceMultiSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceMultiSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRenew(
            self,
            request: models.InquirePriceRenewRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRenewResponse:
        """
        本接口（InquirePriceRenew）用于查询续费集群价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRenew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRenewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateCluster(
            self,
            request: models.IsolateClusterRequest,
            opts: Dict = None,
    ) -> models.IsolateClusterResponse:
        """
        本接口（IsolateCluster）用于隔离集群。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateInstance(
            self,
            request: models.IsolateInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateInstanceResponse:
        """
        本接口(IsolateInstance)用于隔离实例。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountDescription(
            self,
            request: models.ModifyAccountDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountDescriptionResponse:
        """
        本接口(ModifyAccountDescription)用于修改数据库账号描述信息。
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
        本接口（ModifyAccountHost）用于修改账号主机。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountParams(
            self,
            request: models.ModifyAccountParamsRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountParamsResponse:
        """
        本接口（ModifyAccountParams）用于修改账号配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPrivileges(
            self,
            request: models.ModifyAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPrivilegesResponse:
        """
        本接口（ModifyAccountPrivileges）用于修改账号库表权限。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditRuleTemplates(
            self,
            request: models.ModifyAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditRuleTemplatesResponse:
        """
        本接口（ModifyAuditRuleTemplates）用于修改审计规则模板。
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
        本接口(ModifyAuditService)用于修改云数据库审计日志保存时长、审计规则等服务配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupConfig(
            self,
            request: models.ModifyBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupConfigResponse:
        """
        本接口（ModifyBackupConfig）用于修改指定集群的备份配置。
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
        
    async def ModifyBackupDownloadUserRestriction(
            self,
            request: models.ModifyBackupDownloadUserRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadUserRestrictionResponse:
        """
        该接口用于修改用户当前地域的备份文件限制下载来源，可以设置内外网均可下载、仅内网可下载，或内网指定的vpc、ip可以下载。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadUserRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadUserRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupName(
            self,
            request: models.ModifyBackupNameRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupNameResponse:
        """
        此接口（ModifyBackupName）用于修改备份文件备注名。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBinlogConfig(
            self,
            request: models.ModifyBinlogConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyBinlogConfigResponse:
        """
        该接口（ModifyBinlogConfig）用于修改Binlog配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBinlogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBinlogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBinlogSaveDays(
            self,
            request: models.ModifyBinlogSaveDaysRequest,
            opts: Dict = None,
    ) -> models.ModifyBinlogSaveDaysResponse:
        """
        此接口（ModifyBinlogSaveDays）用于修改集群Binlog保留天数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBinlogSaveDays"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBinlogSaveDaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterDatabase(
            self,
            request: models.ModifyClusterDatabaseRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterDatabaseResponse:
        """
        本接口（ModifyClusterDatabase）用于修改数据库的账号授权。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterGlobalEncryption(
            self,
            request: models.ModifyClusterGlobalEncryptionRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterGlobalEncryptionResponse:
        """
        开关全局加密
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterGlobalEncryption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterGlobalEncryptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterName(
            self,
            request: models.ModifyClusterNameRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterNameResponse:
        """
        本接口（ModifyClusterName）用于修改集群名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterParam(
            self,
            request: models.ModifyClusterParamRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterParamResponse:
        """
        本接口（ModifyClusterParam）用于修改集群参数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterPasswordComplexity(
            self,
            request: models.ModifyClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterPasswordComplexityResponse:
        """
        本接口（ModifyClusterPasswordComplexity）用于修改/开启集群密码复杂度。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterReadOnly(
            self,
            request: models.ModifyClusterReadOnlyRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterReadOnlyResponse:
        """
        本接口（ModifyClusterReadOnly）用于修改集群只读开关。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterReadOnly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterReadOnlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterSlaveZone(
            self,
            request: models.ModifyClusterSlaveZoneRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterSlaveZoneResponse:
        """
        本接口（ModifyClusterSlaveZone）用于变更集群的备可用区。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterSlaveZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterSlaveZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterStorage(
            self,
            request: models.ModifyClusterStorageRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterStorageResponse:
        """
        本接口（ModifyClusterStorage）用于调整包年包月存储容量。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        本接口（ModifyDBInstanceSecurityGroups）用于修改实例绑定的安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceName(
            self,
            request: models.ModifyInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNameResponse:
        """
        本接口(ModifyInstanceName)用于修改实例名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParam(
            self,
            request: models.ModifyInstanceParamRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamResponse:
        """
        本接口（ModifyInstanceParam）用于修改实例参数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceUpgradeLimitDays(
            self,
            request: models.ModifyInstanceUpgradeLimitDaysRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceUpgradeLimitDaysResponse:
        """
        本接口（ModifyInstanceUpgradeLimitDays）用于修改实例内核小版本的升级限制时间。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceUpgradeLimitDays"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceUpgradeLimitDaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintainPeriodConfig(
            self,
            request: models.ModifyMaintainPeriodConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintainPeriodConfigResponse:
        """
        本接口（ModifyMaintainPeriodConfig）用于修改维护时间配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintainPeriodConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintainPeriodConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyParamTemplate(
            self,
            request: models.ModifyParamTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyParamTemplateResponse:
        """
        本接口（ModifyParamTemplate）用于修改用户参数模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxyDesc(
            self,
            request: models.ModifyProxyDescRequest,
            opts: Dict = None,
    ) -> models.ModifyProxyDescResponse:
        """
        本接口（ModifyProxyDesc）用于修改数据库代理描述。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxyDesc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxyDescResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxyRwSplit(
            self,
            request: models.ModifyProxyRwSplitRequest,
            opts: Dict = None,
    ) -> models.ModifyProxyRwSplitResponse:
        """
        本接口（ModifyProxyRwSplit）用于配置数据库代理读写分离。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxyRwSplit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxyRwSplitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcePackageClusters(
            self,
            request: models.ModifyResourcePackageClustersRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcePackageClustersResponse:
        """
        本接口（ModifyResourcePackageClusters）用于修改资源包与集群之间的绑定关系。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcePackageClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcePackageClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcePackageName(
            self,
            request: models.ModifyResourcePackageNameRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcePackageNameResponse:
        """
        本接口（ModifyResourcePackageName）用于修改资源包名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcePackageName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcePackageNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcePackagesDeductionPriority(
            self,
            request: models.ModifyResourcePackagesDeductionPriorityRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcePackagesDeductionPriorityResponse:
        """
        修改已绑定资源包抵扣优先级
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcePackagesDeductionPriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcePackagesDeductionPriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServerlessStrategy(
            self,
            request: models.ModifyServerlessStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyServerlessStrategyResponse:
        """
        修改serverless策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServerlessStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServerlessStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVipVport(
            self,
            request: models.ModifyVipVportRequest,
            opts: Dict = None,
    ) -> models.ModifyVipVportResponse:
        """
        本接口（ModifyVipVport）用于修改实例组ip，端口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVipVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVipVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineCluster(
            self,
            request: models.OfflineClusterRequest,
            opts: Dict = None,
    ) -> models.OfflineClusterResponse:
        """
        本接口（OfflineCluster）用于销毁集群。
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineInstance(
            self,
            request: models.OfflineInstanceRequest,
            opts: Dict = None,
    ) -> models.OfflineInstanceResponse:
        """
        本接口（OfflineInstance）用于销毁实例。
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAuditService(
            self,
            request: models.OpenAuditServiceRequest,
            opts: Dict = None,
    ) -> models.OpenAuditServiceResponse:
        """
        本接口（OpenAuditService）用于为实例开通数据库审计服务。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenClusterPasswordComplexity(
            self,
            request: models.OpenClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.OpenClusterPasswordComplexityResponse:
        """
        本接口（OpenClusterPasswordComplexity）用于开启自定义密码复杂度功能。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenClusterReadOnlyInstanceGroupAccess(
            self,
            request: models.OpenClusterReadOnlyInstanceGroupAccessRequest,
            opts: Dict = None,
    ) -> models.OpenClusterReadOnlyInstanceGroupAccessResponse:
        """
        本接口（OpenClusterReadOnlyInstanceGroupAccess）用于开启只读实例组接入。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenClusterReadOnlyInstanceGroupAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenClusterReadOnlyInstanceGroupAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenClusterTransparentEncrypt(
            self,
            request: models.OpenClusterTransparentEncryptRequest,
            opts: Dict = None,
    ) -> models.OpenClusterTransparentEncryptResponse:
        """
        开通集群透明加密
        """
        
        kwargs = {}
        kwargs["action"] = "OpenClusterTransparentEncrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenClusterTransparentEncryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenReadOnlyInstanceExclusiveAccess(
            self,
            request: models.OpenReadOnlyInstanceExclusiveAccessRequest,
            opts: Dict = None,
    ) -> models.OpenReadOnlyInstanceExclusiveAccessResponse:
        """
        本接口（OpenReadOnlyInstanceExclusiveAccess）用于开通只读实例独有访问接入组。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenReadOnlyInstanceExclusiveAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenReadOnlyInstanceExclusiveAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenSSL(
            self,
            request: models.OpenSSLRequest,
            opts: Dict = None,
    ) -> models.OpenSSLResponse:
        """
        开启SSL加密
        """
        
        kwargs = {}
        kwargs["action"] = "OpenSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenWan(
            self,
            request: models.OpenWanRequest,
            opts: Dict = None,
    ) -> models.OpenWanResponse:
        """
        本接口（OpenWan）用于开通外网。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenWan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenWanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseServerless(
            self,
            request: models.PauseServerlessRequest,
            opts: Dict = None,
    ) -> models.PauseServerlessResponse:
        """
        本接口（PauseServerless）用于暂停 serverless 集群。
        """
        
        kwargs = {}
        kwargs["action"] = "PauseServerless"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseServerlessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefundResourcePackage(
            self,
            request: models.RefundResourcePackageRequest,
            opts: Dict = None,
    ) -> models.RefundResourcePackageResponse:
        """
        本接口（RefundResourcePackage）用于资源包退款。
        """
        
        kwargs = {}
        kwargs["action"] = "RefundResourcePackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundResourcePackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReloadBalanceProxyNode(
            self,
            request: models.ReloadBalanceProxyNodeRequest,
            opts: Dict = None,
    ) -> models.ReloadBalanceProxyNodeResponse:
        """
        本接口（ReloadBalanceProxyNode）用于负载均衡数据库代理。
        """
        
        kwargs = {}
        kwargs["action"] = "ReloadBalanceProxyNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReloadBalanceProxyNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveClusterSlaveZone(
            self,
            request: models.RemoveClusterSlaveZoneRequest,
            opts: Dict = None,
    ) -> models.RemoveClusterSlaveZoneResponse:
        """
        本接口（RemoveClusterSlaveZone）用于关闭集群多可用区部署。
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveClusterSlaveZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveClusterSlaveZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewClusters(
            self,
            request: models.RenewClustersRequest,
            opts: Dict = None,
    ) -> models.RenewClustersResponse:
        """
        续费集群
        """
        
        kwargs = {}
        kwargs["action"] = "RenewClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplayInstanceAuditLog(
            self,
            request: models.ReplayInstanceAuditLogRequest,
            opts: Dict = None,
    ) -> models.ReplayInstanceAuditLogResponse:
        """
        回放实例审计日志
        """
        
        kwargs = {}
        kwargs["action"] = "ReplayInstanceAuditLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplayInstanceAuditLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        本接口（ResetAccountPassword）用于修改数据库账号密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartInstance(
            self,
            request: models.RestartInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartInstanceResponse:
        """
        本接口（RestartInstance）用于重启实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RestartInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeServerless(
            self,
            request: models.ResumeServerlessRequest,
            opts: Dict = None,
    ) -> models.ResumeServerlessResponse:
        """
        本接口（ResumeServerless）用于恢复 serverless 集群（启动暂停的集群）。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeServerless"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeServerlessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeAccountPrivileges(
            self,
            request: models.RevokeAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.RevokeAccountPrivilegesResponse:
        """
        本接口（RevokeAccountPrivileges）用于批量回收账号权限。
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollBackCluster(
            self,
            request: models.RollBackClusterRequest,
            opts: Dict = None,
    ) -> models.RollBackClusterResponse:
        """
        本接口（RollBackCluster）用于集群回档。
        """
        
        kwargs = {}
        kwargs["action"] = "RollBackCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollBackClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackToNewCluster(
            self,
            request: models.RollbackToNewClusterRequest,
            opts: Dict = None,
    ) -> models.RollbackToNewClusterResponse:
        """
        本接口（RollbackToNewCluster）用于回档到新集群。
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackToNewCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackToNewClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClusterDatabases(
            self,
            request: models.SearchClusterDatabasesRequest,
            opts: Dict = None,
    ) -> models.SearchClusterDatabasesResponse:
        """
        本接口（SearchClusterDatabases）用于搜索集群数据库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClusterDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClusterDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClusterTables(
            self,
            request: models.SearchClusterTablesRequest,
            opts: Dict = None,
    ) -> models.SearchClusterTablesResponse:
        """
        本接口（SearchClusterTables）用于搜索集群数据表列表。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClusterTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClusterTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetRenewFlag(
            self,
            request: models.SetRenewFlagRequest,
            opts: Dict = None,
    ) -> models.SetRenewFlagResponse:
        """
        本接口（SetRenewFlag）用于设置实例的自动续费功能。
        """
        
        kwargs = {}
        kwargs["action"] = "SetRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCLSDelivery(
            self,
            request: models.StartCLSDeliveryRequest,
            opts: Dict = None,
    ) -> models.StartCLSDeliveryResponse:
        """
        本接口（StartCLSDelivery）用于开启日志投递功能。
        """
        
        kwargs = {}
        kwargs["action"] = "StartCLSDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCLSDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCLSDelivery(
            self,
            request: models.StopCLSDeliveryRequest,
            opts: Dict = None,
    ) -> models.StopCLSDeliveryResponse:
        """
        本接口（StopCLSDelivery）用于停止日志投递功能。
        """
        
        kwargs = {}
        kwargs["action"] = "StopCLSDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCLSDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchClusterVpc(
            self,
            request: models.SwitchClusterVpcRequest,
            opts: Dict = None,
    ) -> models.SwitchClusterVpcResponse:
        """
        本接口（SwitchClusterVpc）用于更换集群vpc。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchClusterVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchClusterVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchClusterZone(
            self,
            request: models.SwitchClusterZoneRequest,
            opts: Dict = None,
    ) -> models.SwitchClusterZoneResponse:
        """
        本接口（SwitchClusterZone）用于切换集群的主备可用区。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchClusterZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchClusterZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchProxyVpc(
            self,
            request: models.SwitchProxyVpcRequest,
            opts: Dict = None,
    ) -> models.SwitchProxyVpcResponse:
        """
        本接口（SwitchProxyVpc）用于更换数据库代理vpc。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchProxyVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchProxyVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindClusterResourcePackages(
            self,
            request: models.UnbindClusterResourcePackagesRequest,
            opts: Dict = None,
    ) -> models.UnbindClusterResourcePackagesResponse:
        """
        本接口（UnbindClusterResourcePackages）用于解除资源包与集群之间的绑定关系。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindClusterResourcePackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindClusterResourcePackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeClusterVersion(
            self,
            request: models.UpgradeClusterVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeClusterVersionResponse:
        """
        本接口（UpgradeClusterVersion）用于更新内核小版本。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeClusterVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeClusterVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        本接口（UpgradeInstance）用于实例变配。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeProxy(
            self,
            request: models.UpgradeProxyRequest,
            opts: Dict = None,
    ) -> models.UpgradeProxyResponse:
        """
        本接口（UpgradeProxy）用于升级数据库代理配置。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeProxyVersion(
            self,
            request: models.UpgradeProxyVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeProxyVersionResponse:
        """
        本接口（UpgradeProxyVersion）用于升级数据库代理版本。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeProxyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeProxyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)