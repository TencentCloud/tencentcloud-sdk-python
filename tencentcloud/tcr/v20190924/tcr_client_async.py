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
from tencentcloud.tcr.v20190924 import models
from typing import Dict


class TcrClient(AbstractClient):
    _apiVersion = '2019-09-24'
    _endpoint = 'tcr.tencentcloudapi.com'
    _service = 'tcr'

    async def BatchDeleteImagePersonal(
            self,
            request: models.BatchDeleteImagePersonalRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteImagePersonalResponse:
        """
        用于在个人版镜像仓库中批量删除Tag
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteImagePersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteImagePersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteRepositoryPersonal(
            self,
            request: models.BatchDeleteRepositoryPersonalRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteRepositoryPersonalResponse:
        """
        用于个人版镜像仓库中批量删除镜像仓库
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteRepositoryPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteRepositoryPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckInstance(
            self,
            request: models.CheckInstanceRequest,
            opts: Dict = None,
    ) -> models.CheckInstanceResponse:
        """
        用于校验企业版实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "CheckInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckInstanceName(
            self,
            request: models.CheckInstanceNameRequest,
            opts: Dict = None,
    ) -> models.CheckInstanceNameResponse:
        """
        检查待创建的实例名称是否符合规范
        """
        
        kwargs = {}
        kwargs["action"] = "CheckInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationTriggerPersonal(
            self,
            request: models.CreateApplicationTriggerPersonalRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationTriggerPersonalResponse:
        """
        用于创建应用更新触发器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationTriggerPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationTriggerPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageAccelerationService(
            self,
            request: models.CreateImageAccelerationServiceRequest,
            opts: Dict = None,
    ) -> models.CreateImageAccelerationServiceResponse:
        """
        创建镜像加速服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageAccelerationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageAccelerationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImmutableTagRules(
            self,
            request: models.CreateImmutableTagRulesRequest,
            opts: Dict = None,
    ) -> models.CreateImmutableTagRulesResponse:
        """
        创建镜像不可变规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImmutableTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImmutableTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        创建实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceCustomizedDomain(
            self,
            request: models.CreateInstanceCustomizedDomainRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceCustomizedDomainResponse:
        """
        创建自定义域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceCustomizedDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceCustomizedDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceToken(
            self,
            request: models.CreateInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceTokenResponse:
        """
        创建实例的临时或长期访问凭证
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInternalEndpointDns(
            self,
            request: models.CreateInternalEndpointDnsRequest,
            opts: Dict = None,
    ) -> models.CreateInternalEndpointDnsResponse:
        """
        创建tcr内网私有域名解析
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInternalEndpointDns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInternalEndpointDnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultipleSecurityPolicy(
            self,
            request: models.CreateMultipleSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateMultipleSecurityPolicyResponse:
        """
        用于在TCR实例中，创建多个白名单策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultipleSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultipleSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNamespace(
            self,
            request: models.CreateNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateNamespaceResponse:
        """
        用于在企业版中创建命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNamespacePersonal(
            self,
            request: models.CreateNamespacePersonalRequest,
            opts: Dict = None,
    ) -> models.CreateNamespacePersonalResponse:
        """
        创建个人版镜像仓库命名空间，此命名空间全局唯一
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNamespacePersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNamespacePersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReplicationInstance(
            self,
            request: models.CreateReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateReplicationInstanceResponse:
        """
        创建从实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRepository(
            self,
            request: models.CreateRepositoryRequest,
            opts: Dict = None,
    ) -> models.CreateRepositoryResponse:
        """
        用于企业版创建镜像仓库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRepositoryPersonal(
            self,
            request: models.CreateRepositoryPersonalRequest,
            opts: Dict = None,
    ) -> models.CreateRepositoryPersonalResponse:
        """
        用于在个人版仓库中创建镜像仓库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRepositoryPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRepositoryPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityPolicy(
            self,
            request: models.CreateSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityPolicyResponse:
        """
        创建实例公网访问白名单策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceAccount(
            self,
            request: models.CreateServiceAccountRequest,
            opts: Dict = None,
    ) -> models.CreateServiceAccountResponse:
        """
        创建服务级账户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSignature(
            self,
            request: models.CreateSignatureRequest,
            opts: Dict = None,
    ) -> models.CreateSignatureResponse:
        """
        为一个镜像版本创建签名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSignature"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSignatureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSignaturePolicy(
            self,
            request: models.CreateSignaturePolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSignaturePolicyResponse:
        """
        创建镜像签名策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSignaturePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSignaturePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTagRetentionExecution(
            self,
            request: models.CreateTagRetentionExecutionRequest,
            opts: Dict = None,
    ) -> models.CreateTagRetentionExecutionResponse:
        """
        手动执行版本保留
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTagRetentionExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagRetentionExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTagRetentionRule(
            self,
            request: models.CreateTagRetentionRuleRequest,
            opts: Dict = None,
    ) -> models.CreateTagRetentionRuleResponse:
        """
        创建版本保留规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTagRetentionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagRetentionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserPersonal(
            self,
            request: models.CreateUserPersonalRequest,
            opts: Dict = None,
    ) -> models.CreateUserPersonalResponse:
        """
        创建个人用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebhookTrigger(
            self,
            request: models.CreateWebhookTriggerRequest,
            opts: Dict = None,
    ) -> models.CreateWebhookTriggerResponse:
        """
        创建触发器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebhookTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebhookTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationTriggerPersonal(
            self,
            request: models.DeleteApplicationTriggerPersonalRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationTriggerPersonalResponse:
        """
        用于删除应用更新触发器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationTriggerPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationTriggerPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImage(
            self,
            request: models.DeleteImageRequest,
            opts: Dict = None,
    ) -> models.DeleteImageResponse:
        """
        删除指定镜像
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageAccelerateService(
            self,
            request: models.DeleteImageAccelerateServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteImageAccelerateServiceResponse:
        """
        删除镜像加速服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageAccelerateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageAccelerateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageLifecycleGlobalPersonal(
            self,
            request: models.DeleteImageLifecycleGlobalPersonalRequest,
            opts: Dict = None,
    ) -> models.DeleteImageLifecycleGlobalPersonalResponse:
        """
        用于删除个人版全局镜像版本自动清理策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageLifecycleGlobalPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageLifecycleGlobalPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImagePersonal(
            self,
            request: models.DeleteImagePersonalRequest,
            opts: Dict = None,
    ) -> models.DeleteImagePersonalResponse:
        """
        用于在个人版中删除tag
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImagePersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImagePersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImmutableTagRules(
            self,
            request: models.DeleteImmutableTagRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteImmutableTagRulesResponse:
        """
        删除镜像不可变规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImmutableTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImmutableTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        删除镜像仓库企业版实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstanceCustomizedDomain(
            self,
            request: models.DeleteInstanceCustomizedDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceCustomizedDomainResponse:
        """
        删除自定义域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstanceCustomizedDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceCustomizedDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstanceToken(
            self,
            request: models.DeleteInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceTokenResponse:
        """
        删除长期访问凭证
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInternalEndpointDns(
            self,
            request: models.DeleteInternalEndpointDnsRequest,
            opts: Dict = None,
    ) -> models.DeleteInternalEndpointDnsResponse:
        """
        删除tcr内网私有域名解析
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInternalEndpointDns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInternalEndpointDnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMultipleSecurityPolicy(
            self,
            request: models.DeleteMultipleSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteMultipleSecurityPolicyResponse:
        """
        用于删除实例多个公网访问白名单策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMultipleSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMultipleSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNamespace(
            self,
            request: models.DeleteNamespaceRequest,
            opts: Dict = None,
    ) -> models.DeleteNamespaceResponse:
        """
        删除命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNamespacePersonal(
            self,
            request: models.DeleteNamespacePersonalRequest,
            opts: Dict = None,
    ) -> models.DeleteNamespacePersonalResponse:
        """
        删除共享版命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNamespacePersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNamespacePersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReplicationInstance(
            self,
            request: models.DeleteReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteReplicationInstanceResponse:
        """
        删除从实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReplicationRule(
            self,
            request: models.DeleteReplicationRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteReplicationRuleResponse:
        """
        删除实例同步规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReplicationRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReplicationRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRepository(
            self,
            request: models.DeleteRepositoryRequest,
            opts: Dict = None,
    ) -> models.DeleteRepositoryResponse:
        """
        删除镜像仓库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRepositoryPersonal(
            self,
            request: models.DeleteRepositoryPersonalRequest,
            opts: Dict = None,
    ) -> models.DeleteRepositoryPersonalResponse:
        """
        用于个人版镜像仓库中删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRepositoryPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRepositoryPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRepositoryTags(
            self,
            request: models.DeleteRepositoryTagsRequest,
            opts: Dict = None,
    ) -> models.DeleteRepositoryTagsResponse:
        """
        用于企业版批量删除Repository Tag
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRepositoryTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRepositoryTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityPolicy(
            self,
            request: models.DeleteSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityPolicyResponse:
        """
        删除实例公网访问白名单策略

        注意：当PolicyIndex和CidrBlock同时存在时，CidrBlock优先级更高
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceAccount(
            self,
            request: models.DeleteServiceAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceAccountResponse:
        """
        删除服务级账号
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSignaturePolicy(
            self,
            request: models.DeleteSignaturePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteSignaturePolicyResponse:
        """
        删除命名空间加签策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSignaturePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSignaturePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTagRetentionRule(
            self,
            request: models.DeleteTagRetentionRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteTagRetentionRuleResponse:
        """
        删除版本保留规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTagRetentionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagRetentionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebhookTrigger(
            self,
            request: models.DeleteWebhookTriggerRequest,
            opts: Dict = None,
    ) -> models.DeleteWebhookTriggerResponse:
        """
        删除触发器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebhookTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebhookTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationTriggerLogPersonal(
            self,
            request: models.DescribeApplicationTriggerLogPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationTriggerLogPersonalResponse:
        """
        用于查询应用更新触发器触发日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationTriggerLogPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationTriggerLogPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationTriggerPersonal(
            self,
            request: models.DescribeApplicationTriggerPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationTriggerPersonalResponse:
        """
        用于查询应用更新触发器
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationTriggerPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationTriggerPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChartDownloadInfo(
            self,
            request: models.DescribeChartDownloadInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeChartDownloadInfoResponse:
        """
        用于在企业版中返回Chart的下载信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChartDownloadInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChartDownloadInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExternalEndpointStatus(
            self,
            request: models.DescribeExternalEndpointStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeExternalEndpointStatusResponse:
        """
        查询实例公网访问入口状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExternalEndpointStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExternalEndpointStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFavorRepositoryPersonal(
            self,
            request: models.DescribeFavorRepositoryPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeFavorRepositoryPersonalResponse:
        """
        查询个人收藏仓库
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFavorRepositoryPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFavorRepositoryPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGCJobs(
            self,
            request: models.DescribeGCJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeGCJobsResponse:
        """
        GC 最近10条历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGCJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGCJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAccelerateService(
            self,
            request: models.DescribeImageAccelerateServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAccelerateServiceResponse:
        """
        查询镜像加速服务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAccelerateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAccelerateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageFilterPersonal(
            self,
            request: models.DescribeImageFilterPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeImageFilterPersonalResponse:
        """
        用于在个人版中查询与指定tag镜像内容相同的tag列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageFilterPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageFilterPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageLifecycleGlobalPersonal(
            self,
            request: models.DescribeImageLifecycleGlobalPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeImageLifecycleGlobalPersonalResponse:
        """
        用于获取个人版全局镜像版本自动清理策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageLifecycleGlobalPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageLifecycleGlobalPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageLifecyclePersonal(
            self,
            request: models.DescribeImageLifecyclePersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeImageLifecyclePersonalResponse:
        """
        用于获取个人版仓库中自动清理策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageLifecyclePersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageLifecyclePersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageManifests(
            self,
            request: models.DescribeImageManifestsRequest,
            opts: Dict = None,
    ) -> models.DescribeImageManifestsResponse:
        """
        查询容器镜像Manifest信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageManifests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageManifestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImagePersonal(
            self,
            request: models.DescribeImagePersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeImagePersonalResponse:
        """
        用于获取个人版镜像仓库tag列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImagePersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagePersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImages(
            self,
            request: models.DescribeImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesResponse:
        """
        查询镜像版本列表或指定容器镜像信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImmutableTagRules(
            self,
            request: models.DescribeImmutableTagRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeImmutableTagRulesResponse:
        """
        列出镜像不可变规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImmutableTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImmutableTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceAllNamespaces(
            self,
            request: models.DescribeInstanceAllNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceAllNamespacesResponse:
        """
        查询所有有实例命名空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceAllNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceAllNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceCustomizedDomain(
            self,
            request: models.DescribeInstanceCustomizedDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceCustomizedDomainResponse:
        """
        查询实例自定义域名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceCustomizedDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceCustomizedDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceStatus(
            self,
            request: models.DescribeInstanceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceStatusResponse:
        """
        查询实例当前状态以及过程信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceToken(
            self,
            request: models.DescribeInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTokenResponse:
        """
        查询长期访问凭证信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        查询实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternalEndpointDnsStatus(
            self,
            request: models.DescribeInternalEndpointDnsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInternalEndpointDnsStatusResponse:
        """
        批量查询vpc是否已经添加私有域名解析
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternalEndpointDnsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternalEndpointDnsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternalEndpoints(
            self,
            request: models.DescribeInternalEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeInternalEndpointsResponse:
        """
        查询实例内网访问VPC链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternalEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternalEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNamespacePersonal(
            self,
            request: models.DescribeNamespacePersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeNamespacePersonalResponse:
        """
        查询个人版命名空间信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNamespacePersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNamespacePersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNamespaces(
            self,
            request: models.DescribeNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNamespacesResponse:
        """
        查询命名空间列表或指定命名空间信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        用于在TCR中获取可用区域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationInstanceCreateTasks(
            self,
            request: models.DescribeReplicationInstanceCreateTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationInstanceCreateTasksResponse:
        """
        查询创建从实例任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationInstanceCreateTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationInstanceCreateTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationInstanceSyncStatus(
            self,
            request: models.DescribeReplicationInstanceSyncStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationInstanceSyncStatusResponse:
        """
        查询从实例同步状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationInstanceSyncStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationInstanceSyncStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationInstances(
            self,
            request: models.DescribeReplicationInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationInstancesResponse:
        """
        查询从实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationPolicies(
            self,
            request: models.DescribeReplicationPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationPoliciesResponse:
        """
        获取实例同步规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepositories(
            self,
            request: models.DescribeRepositoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoriesResponse:
        """
        查询镜像仓库列表或指定镜像仓库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepositories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepositoryFilterPersonal(
            self,
            request: models.DescribeRepositoryFilterPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoryFilterPersonalResponse:
        """
        用于在个人版镜像仓库中，获取满足输入搜索条件的用户镜像仓库
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepositoryFilterPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoryFilterPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepositoryOwnerPersonal(
            self,
            request: models.DescribeRepositoryOwnerPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoryOwnerPersonalResponse:
        """
        用于在个人版中获取用户全部的镜像仓库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepositoryOwnerPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoryOwnerPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepositoryPersonal(
            self,
            request: models.DescribeRepositoryPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoryPersonalResponse:
        """
        查询个人版仓库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepositoryPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoryPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicies(
            self,
            request: models.DescribeSecurityPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPoliciesResponse:
        """
        查询实例公网访问白名单策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceAccounts(
            self,
            request: models.DescribeServiceAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceAccountsResponse:
        """
        查询服务级账号
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagRetentionExecution(
            self,
            request: models.DescribeTagRetentionExecutionRequest,
            opts: Dict = None,
    ) -> models.DescribeTagRetentionExecutionResponse:
        """
        查询版本保留执行记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagRetentionExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagRetentionExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagRetentionExecutionTask(
            self,
            request: models.DescribeTagRetentionExecutionTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTagRetentionExecutionTaskResponse:
        """
        查询版本保留执行任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagRetentionExecutionTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagRetentionExecutionTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagRetentionRules(
            self,
            request: models.DescribeTagRetentionRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagRetentionRulesResponse:
        """
        查询镜像版本保留规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagRetentionRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagRetentionRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserQuotaPersonal(
            self,
            request: models.DescribeUserQuotaPersonalRequest,
            opts: Dict = None,
    ) -> models.DescribeUserQuotaPersonalResponse:
        """
        查询个人用户配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserQuotaPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserQuotaPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebhookTrigger(
            self,
            request: models.DescribeWebhookTriggerRequest,
            opts: Dict = None,
    ) -> models.DescribeWebhookTriggerResponse:
        """
        查询触发器
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebhookTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebhookTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebhookTriggerLog(
            self,
            request: models.DescribeWebhookTriggerLogRequest,
            opts: Dict = None,
    ) -> models.DescribeWebhookTriggerLogResponse:
        """
        获取触发器日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebhookTriggerLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebhookTriggerLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadHelmChart(
            self,
            request: models.DownloadHelmChartRequest,
            opts: Dict = None,
    ) -> models.DownloadHelmChartResponse:
        """
        用于在TCR中下载helm chart
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadHelmChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadHelmChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DuplicateImage(
            self,
            request: models.DuplicateImageRequest,
            opts: Dict = None,
    ) -> models.DuplicateImageResponse:
        """
        用于在企业版镜像仓库中复制镜像版本
        """
        
        kwargs = {}
        kwargs["action"] = "DuplicateImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DuplicateImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DuplicateImagePersonal(
            self,
            request: models.DuplicateImagePersonalRequest,
            opts: Dict = None,
    ) -> models.DuplicateImagePersonalResponse:
        """
        用于在个人版镜像仓库中复制镜像版本
        """
        
        kwargs = {}
        kwargs["action"] = "DuplicateImagePersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DuplicateImagePersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageExternalEndpoint(
            self,
            request: models.ManageExternalEndpointRequest,
            opts: Dict = None,
    ) -> models.ManageExternalEndpointResponse:
        """
        管理实例公网访问
        """
        
        kwargs = {}
        kwargs["action"] = "ManageExternalEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageExternalEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageImageLifecycleGlobalPersonal(
            self,
            request: models.ManageImageLifecycleGlobalPersonalRequest,
            opts: Dict = None,
    ) -> models.ManageImageLifecycleGlobalPersonalResponse:
        """
        用于设置个人版全局镜像版本自动清理策略
        """
        
        kwargs = {}
        kwargs["action"] = "ManageImageLifecycleGlobalPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageImageLifecycleGlobalPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageInternalEndpoint(
            self,
            request: models.ManageInternalEndpointRequest,
            opts: Dict = None,
    ) -> models.ManageInternalEndpointResponse:
        """
        管理实例内网访问VPC链接
        """
        
        kwargs = {}
        kwargs["action"] = "ManageInternalEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageInternalEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageReplication(
            self,
            request: models.ManageReplicationRequest,
            opts: Dict = None,
    ) -> models.ManageReplicationResponse:
        """
        管理实例同步
        """
        
        kwargs = {}
        kwargs["action"] = "ManageReplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageReplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationTriggerPersonal(
            self,
            request: models.ModifyApplicationTriggerPersonalRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationTriggerPersonalResponse:
        """
        用于修改应用更新触发器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationTriggerPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationTriggerPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImmutableTagRules(
            self,
            request: models.ModifyImmutableTagRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyImmutableTagRulesResponse:
        """
        更新镜像不可变规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImmutableTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImmutableTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        更新实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceToken(
            self,
            request: models.ModifyInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceTokenResponse:
        """
        更新实例内指定长期访问凭证的启用状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNamespace(
            self,
            request: models.ModifyNamespaceRequest,
            opts: Dict = None,
    ) -> models.ModifyNamespaceResponse:
        """
        更新命名空间信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRepository(
            self,
            request: models.ModifyRepositoryRequest,
            opts: Dict = None,
    ) -> models.ModifyRepositoryResponse:
        """
        更新镜像仓库信息，可修改仓库描述信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRepositoryAccessPersonal(
            self,
            request: models.ModifyRepositoryAccessPersonalRequest,
            opts: Dict = None,
    ) -> models.ModifyRepositoryAccessPersonalResponse:
        """
        用于更新个人版镜像仓库的访问属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRepositoryAccessPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRepositoryAccessPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRepositoryInfoPersonal(
            self,
            request: models.ModifyRepositoryInfoPersonalRequest,
            opts: Dict = None,
    ) -> models.ModifyRepositoryInfoPersonalResponse:
        """
        用于在个人版镜像仓库中更新容器镜像描述
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRepositoryInfoPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRepositoryInfoPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityPolicy(
            self,
            request: models.ModifySecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityPolicyResponse:
        """
        更新实例公网访问白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceAccount(
            self,
            request: models.ModifyServiceAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceAccountResponse:
        """
        更新服务级账号
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceAccountPassword(
            self,
            request: models.ModifyServiceAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceAccountPasswordResponse:
        """
        更新服务级账号密码
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTagRetentionRule(
            self,
            request: models.ModifyTagRetentionRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyTagRetentionRuleResponse:
        """
        更新版本保留规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTagRetentionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTagRetentionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserPasswordPersonal(
            self,
            request: models.ModifyUserPasswordPersonalRequest,
            opts: Dict = None,
    ) -> models.ModifyUserPasswordPersonalResponse:
        """
        修改个人用户登录密码
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserPasswordPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserPasswordPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebhookTrigger(
            self,
            request: models.ModifyWebhookTriggerRequest,
            opts: Dict = None,
    ) -> models.ModifyWebhookTriggerResponse:
        """
        更新触发器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebhookTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebhookTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstance(
            self,
            request: models.RenewInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewInstanceResponse:
        """
        预付费实例续费，同时支持按量计费转包年包月
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ValidateNamespaceExistPersonal(
            self,
            request: models.ValidateNamespaceExistPersonalRequest,
            opts: Dict = None,
    ) -> models.ValidateNamespaceExistPersonalResponse:
        """
        查询个人版用户命名空间是否存在
        """
        
        kwargs = {}
        kwargs["action"] = "ValidateNamespaceExistPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ValidateNamespaceExistPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ValidateRepositoryExistPersonal(
            self,
            request: models.ValidateRepositoryExistPersonalRequest,
            opts: Dict = None,
    ) -> models.ValidateRepositoryExistPersonalResponse:
        """
        用于判断个人版仓库是否存在
        """
        
        kwargs = {}
        kwargs["action"] = "ValidateRepositoryExistPersonal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ValidateRepositoryExistPersonalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)