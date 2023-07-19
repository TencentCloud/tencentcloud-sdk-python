# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tcr.v20190924 import models


class TcrClient(AbstractClient):
    _apiVersion = '2019-09-24'
    _endpoint = 'tcr.tencentcloudapi.com'
    _service = 'tcr'


    def BatchDeleteImagePersonal(self, request):
        """用于在个人版镜像仓库中批量删除Tag

        :param request: Request instance for BatchDeleteImagePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.BatchDeleteImagePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.BatchDeleteImagePersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteImagePersonal", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteImagePersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteRepositoryPersonal(self, request):
        """用于个人版镜像仓库中批量删除镜像仓库

        :param request: Request instance for BatchDeleteRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.BatchDeleteRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.BatchDeleteRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteRepositoryPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteRepositoryPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckInstance(self, request):
        """用于校验企业版实例信息

        :param request: Request instance for CheckInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CheckInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckInstanceName(self, request):
        """检查待创建的实例名称是否符合规范

        :param request: Request instance for CheckInstanceName.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceNameRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationTriggerPersonal(self, request):
        """用于创建应用更新触发器

        :param request: Request instance for CreateApplicationTriggerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateApplicationTriggerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateApplicationTriggerPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationTriggerPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationTriggerPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomAccount(self, request):
        """创建自定义账户

        :param request: Request instance for CreateCustomAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateCustomAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateCustomAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageAccelerationService(self, request):
        """创建镜像加速服务

        :param request: Request instance for CreateImageAccelerationService.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateImageAccelerationServiceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateImageAccelerationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageAccelerationService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageAccelerationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImmutableTagRules(self, request):
        """创建镜像不可变规则

        :param request: Request instance for CreateImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImmutableTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        """创建实例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceCustomizedDomain(self, request):
        """创建自定义域名

        :param request: Request instance for CreateInstanceCustomizedDomain.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceCustomizedDomainRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceCustomizedDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceCustomizedDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceCustomizedDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceToken(self, request):
        """创建实例的临时或长期访问凭证

        :param request: Request instance for CreateInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInternalEndpointDns(self, request):
        """创建tcr内网私有域名解析

        :param request: Request instance for CreateInternalEndpointDns.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInternalEndpointDnsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInternalEndpointDnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInternalEndpointDns", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInternalEndpointDnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultipleSecurityPolicy(self, request):
        """用于在TCR实例中，创建多个白名单策略

        :param request: Request instance for CreateMultipleSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateMultipleSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateMultipleSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultipleSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultipleSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNamespace(self, request):
        """用于在企业版中创建命名空间

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNamespacePersonal(self, request):
        """创建个人版镜像仓库命名空间，此命名空间全局唯一

        :param request: Request instance for CreateNamespacePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateNamespacePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateNamespacePersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNamespacePersonal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNamespacePersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReplicationInstance(self, request):
        """创建从实例

        :param request: Request instance for CreateReplicationInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReplicationInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReplicationInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRepository(self, request):
        """用于企业版创建镜像仓库

        :param request: Request instance for CreateRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRepository", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRepositoryPersonal(self, request):
        """用于在个人版仓库中创建镜像仓库

        :param request: Request instance for CreateRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRepositoryPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRepositoryPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityPolicy(self, request):
        """创建实例公网访问白名单策略

        :param request: Request instance for CreateSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServiceAccount(self, request):
        """创建自定义账户

        :param request: Request instance for CreateServiceAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateServiceAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateServiceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSignature(self, request):
        """为一个镜像版本创建签名

        :param request: Request instance for CreateSignature.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateSignatureRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateSignatureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSignature", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSignatureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSignaturePolicy(self, request):
        """创建镜像签名策略

        :param request: Request instance for CreateSignaturePolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateSignaturePolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateSignaturePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSignaturePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSignaturePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTagRetentionExecution(self, request):
        """手动执行版本保留

        :param request: Request instance for CreateTagRetentionExecution.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateTagRetentionExecutionRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateTagRetentionExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTagRetentionExecution", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTagRetentionExecutionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTagRetentionRule(self, request):
        """创建版本保留规则

        :param request: Request instance for CreateTagRetentionRule.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateTagRetentionRuleRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateTagRetentionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTagRetentionRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTagRetentionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserPersonal(self, request):
        """创建个人用户

        :param request: Request instance for CreateUserPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateUserPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateUserPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebhookTrigger(self, request):
        """创建触发器

        :param request: Request instance for CreateWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebhookTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebhookTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationTriggerPersonal(self, request):
        """用于删除应用更新触发器

        :param request: Request instance for DeleteApplicationTriggerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteApplicationTriggerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteApplicationTriggerPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationTriggerPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationTriggerPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomAccount(self, request):
        """删除自定义账号

        :param request: Request instance for DeleteCustomAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteCustomAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteCustomAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImage(self, request):
        """删除指定镜像

        :param request: Request instance for DeleteImage.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImageRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageAccelerateService(self, request):
        """删除镜像加速服务

        :param request: Request instance for DeleteImageAccelerateService.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImageAccelerateServiceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImageAccelerateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageAccelerateService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageAccelerateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageLifecycleGlobalPersonal(self, request):
        """用于删除个人版全局镜像版本自动清理策略

        :param request: Request instance for DeleteImageLifecycleGlobalPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImageLifecycleGlobalPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImageLifecycleGlobalPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageLifecycleGlobalPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageLifecycleGlobalPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImagePersonal(self, request):
        """用于在个人版中删除tag

        :param request: Request instance for DeleteImagePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImagePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImagePersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImagePersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImagePersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImmutableTagRules(self, request):
        """删除镜像不可变规则

        :param request: Request instance for DeleteImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImmutableTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        """删除镜像仓库企业版实例

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstanceCustomizedDomain(self, request):
        """删除自定义域名

        :param request: Request instance for DeleteInstanceCustomizedDomain.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceCustomizedDomainRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceCustomizedDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstanceCustomizedDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceCustomizedDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstanceToken(self, request):
        """删除长期访问凭证

        :param request: Request instance for DeleteInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInternalEndpointDns(self, request):
        """删除tcr内网私有域名解析

        :param request: Request instance for DeleteInternalEndpointDns.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteInternalEndpointDnsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteInternalEndpointDnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInternalEndpointDns", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInternalEndpointDnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMultipleSecurityPolicy(self, request):
        """用于删除实例多个公网访问白名单策略

        :param request: Request instance for DeleteMultipleSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteMultipleSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteMultipleSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMultipleSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMultipleSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNamespace(self, request):
        """删除命名空间

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNamespacePersonal(self, request):
        """删除共享版命名空间

        :param request: Request instance for DeleteNamespacePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespacePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespacePersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNamespacePersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNamespacePersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReplicationInstance(self, request):
        """删除从实例

        :param request: Request instance for DeleteReplicationInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReplicationInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReplicationInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRepository(self, request):
        """删除镜像仓库

        :param request: Request instance for DeleteRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRepository", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRepositoryPersonal(self, request):
        """用于个人版镜像仓库中删除

        :param request: Request instance for DeleteRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRepositoryPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRepositoryPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRepositoryTags(self, request):
        """用于企业版批量删除Repository Tag

        :param request: Request instance for DeleteRepositoryTags.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryTagsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRepositoryTags", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRepositoryTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityPolicy(self, request):
        """删除实例公网访问白名单策略

        注意：当PolicyIndex和CidrBlock同时存在时，CidrBlock优先级更高

        :param request: Request instance for DeleteSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServiceAccount(self, request):
        """删除服务级账号

        :param request: Request instance for DeleteServiceAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteServiceAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteServiceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSignaturePolicy(self, request):
        """删除命名空间加签策略

        :param request: Request instance for DeleteSignaturePolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteSignaturePolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteSignaturePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSignaturePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSignaturePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTagRetentionRule(self, request):
        """删除版本保留规则

        :param request: Request instance for DeleteTagRetentionRule.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteTagRetentionRuleRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteTagRetentionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTagRetentionRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagRetentionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebhookTrigger(self, request):
        """删除触发器

        :param request: Request instance for DeleteWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebhookTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebhookTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationTriggerLogPersonal(self, request):
        """用于查询应用更新触发器触发日志

        :param request: Request instance for DescribeApplicationTriggerLogPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationTriggerLogPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationTriggerLogPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationTriggerPersonal(self, request):
        """用于查询应用更新触发器

        :param request: Request instance for DescribeApplicationTriggerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationTriggerPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationTriggerPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChartDownloadInfo(self, request):
        """用于在企业版中返回Chart的下载信息

        :param request: Request instance for DescribeChartDownloadInfo.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeChartDownloadInfoRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeChartDownloadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChartDownloadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChartDownloadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomAccounts(self, request):
        """查询自定义账号

        :param request: Request instance for DescribeCustomAccounts.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeCustomAccountsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeCustomAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExternalEndpointStatus(self, request):
        """查询实例公网访问入口状态

        :param request: Request instance for DescribeExternalEndpointStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeExternalEndpointStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeExternalEndpointStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExternalEndpointStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExternalEndpointStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFavorRepositoryPersonal(self, request):
        """查询个人收藏仓库

        :param request: Request instance for DescribeFavorRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeFavorRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeFavorRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFavorRepositoryPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFavorRepositoryPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGCJobs(self, request):
        """GC 最近10条历史

        :param request: Request instance for DescribeGCJobs.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeGCJobsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeGCJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGCJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGCJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAccelerateService(self, request):
        """查询镜像加速服务状态

        :param request: Request instance for DescribeImageAccelerateService.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageAccelerateServiceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageAccelerateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAccelerateService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAccelerateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageFilterPersonal(self, request):
        """用于在个人版中查询与指定tag镜像内容相同的tag列表

        :param request: Request instance for DescribeImageFilterPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageFilterPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageFilterPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageFilterPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageFilterPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageLifecycleGlobalPersonal(self, request):
        """用于获取个人版全局镜像版本自动清理策略

        :param request: Request instance for DescribeImageLifecycleGlobalPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageLifecycleGlobalPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageLifecycleGlobalPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageLifecycleGlobalPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageLifecycleGlobalPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageLifecyclePersonal(self, request):
        """用于获取个人版仓库中自动清理策略

        :param request: Request instance for DescribeImageLifecyclePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageLifecyclePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageLifecyclePersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageLifecyclePersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageLifecyclePersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageManifests(self, request):
        """查询容器镜像Manifest信息

        :param request: Request instance for DescribeImageManifests.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageManifestsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageManifestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageManifests", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageManifestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImagePersonal(self, request):
        """用于获取个人版镜像仓库tag列表

        :param request: Request instance for DescribeImagePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImagePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImagePersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImagePersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImagePersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImages(self, request):
        """查询镜像版本列表或指定容器镜像信息

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImmutableTagRules(self, request):
        """列出镜像不可变规则

        :param request: Request instance for DescribeImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImmutableTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceAllNamespaces(self, request):
        """查询所有实例命名空间列表

        :param request: Request instance for DescribeInstanceAllNamespaces.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceAllNamespacesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceAllNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceAllNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceAllNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceCustomizedDomain(self, request):
        """查询实例自定义域名列表

        :param request: Request instance for DescribeInstanceCustomizedDomain.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceCustomizedDomainRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceCustomizedDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceCustomizedDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceCustomizedDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceStatus(self, request):
        """查询实例当前状态以及过程信息

        :param request: Request instance for DescribeInstanceStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceToken(self, request):
        """查询长期访问凭证信息

        :param request: Request instance for DescribeInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """查询实例信息

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInternalEndpointDnsStatus(self, request):
        """批量查询vpc是否已经添加私有域名解析

        :param request: Request instance for DescribeInternalEndpointDnsStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInternalEndpointDnsStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInternalEndpointDnsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInternalEndpointDnsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInternalEndpointDnsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInternalEndpoints(self, request):
        """查询实例内网访问VPC链接

        :param request: Request instance for DescribeInternalEndpoints.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInternalEndpointsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInternalEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInternalEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInternalEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNamespacePersonal(self, request):
        """查询个人版命名空间信息

        :param request: Request instance for DescribeNamespacePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacePersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNamespacePersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNamespacePersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNamespaces(self, request):
        """查询命名空间列表或指定命名空间信息

        :param request: Request instance for DescribeNamespaces.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """用于在TCR中获取可用区域

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplicationInstanceCreateTasks(self, request):
        """查询创建从实例任务状态

        :param request: Request instance for DescribeReplicationInstanceCreateTasks.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceCreateTasksRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceCreateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstanceCreateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplicationInstanceCreateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplicationInstanceSyncStatus(self, request):
        """查询从实例同步状态

        :param request: Request instance for DescribeReplicationInstanceSyncStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceSyncStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceSyncStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstanceSyncStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplicationInstanceSyncStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplicationInstances(self, request):
        """查询从实例列表

        :param request: Request instance for DescribeReplicationInstances.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstancesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplicationInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepositories(self, request):
        """查询镜像仓库列表或指定镜像仓库信息

        :param request: Request instance for DescribeRepositories.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoriesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepositories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepositoryFilterPersonal(self, request):
        """用于在个人版镜像仓库中，获取满足输入搜索条件的用户镜像仓库

        :param request: Request instance for DescribeRepositoryFilterPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryFilterPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryFilterPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepositoryFilterPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoryFilterPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepositoryOwnerPersonal(self, request):
        """用于在个人版中获取用户全部的镜像仓库列表

        :param request: Request instance for DescribeRepositoryOwnerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryOwnerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryOwnerPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepositoryOwnerPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoryOwnerPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepositoryPersonal(self, request):
        """查询个人版仓库信息

        :param request: Request instance for DescribeRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepositoryPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoryPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicies(self, request):
        """查询实例公网访问白名单策略

        :param request: Request instance for DescribeSecurityPolicies.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeSecurityPoliciesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeSecurityPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceAccounts(self, request):
        """查询服务级账号

        :param request: Request instance for DescribeServiceAccounts.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeServiceAccountsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeServiceAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagRetentionExecution(self, request):
        """查询版本保留执行记录

        :param request: Request instance for DescribeTagRetentionExecution.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionExecutionRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagRetentionExecution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagRetentionExecutionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagRetentionExecutionTask(self, request):
        """查询版本保留执行任务

        :param request: Request instance for DescribeTagRetentionExecutionTask.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionExecutionTaskRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionExecutionTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagRetentionExecutionTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagRetentionExecutionTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagRetentionRules(self, request):
        """查询版本保留规则

        :param request: Request instance for DescribeTagRetentionRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagRetentionRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagRetentionRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserQuotaPersonal(self, request):
        """查询个人用户配额

        :param request: Request instance for DescribeUserQuotaPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeUserQuotaPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeUserQuotaPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserQuotaPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserQuotaPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebhookTrigger(self, request):
        """查询触发器

        :param request: Request instance for DescribeWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebhookTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebhookTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebhookTriggerLog(self, request):
        """获取触发器日志

        :param request: Request instance for DescribeWebhookTriggerLog.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerLogRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebhookTriggerLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebhookTriggerLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadHelmChart(self, request):
        """用于在TCR中下载helm chart

        :param request: Request instance for DownloadHelmChart.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DownloadHelmChartRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DownloadHelmChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadHelmChart", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadHelmChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DuplicateImagePersonal(self, request):
        """用于在个人版镜像仓库中复制镜像版本

        :param request: Request instance for DuplicateImagePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DuplicateImagePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DuplicateImagePersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DuplicateImagePersonal", params, headers=headers)
            response = json.loads(body)
            model = models.DuplicateImagePersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageExternalEndpoint(self, request):
        """管理实例公网访问

        :param request: Request instance for ManageExternalEndpoint.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageExternalEndpointRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageExternalEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageExternalEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ManageExternalEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageImageLifecycleGlobalPersonal(self, request):
        """用于设置个人版全局镜像版本自动清理策略

        :param request: Request instance for ManageImageLifecycleGlobalPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageImageLifecycleGlobalPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageImageLifecycleGlobalPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageImageLifecycleGlobalPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.ManageImageLifecycleGlobalPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageInternalEndpoint(self, request):
        """管理实例内网访问VPC链接

        :param request: Request instance for ManageInternalEndpoint.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageInternalEndpointRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageInternalEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageInternalEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ManageInternalEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageReplication(self, request):
        """管理实例同步

        :param request: Request instance for ManageReplication.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageReplicationRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageReplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageReplication", params, headers=headers)
            response = json.loads(body)
            model = models.ManageReplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationTriggerPersonal(self, request):
        """用于修改应用更新触发器

        :param request: Request instance for ModifyApplicationTriggerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyApplicationTriggerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyApplicationTriggerPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationTriggerPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationTriggerPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomAccount(self, request):
        """更新自定义账户

        :param request: Request instance for ModifyCustomAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyCustomAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyCustomAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImmutableTagRules(self, request):
        """更新镜像不可变规则

        :param request: Request instance for ModifyImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImmutableTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        """更新实例信息

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceToken(self, request):
        """更新实例内指定长期访问凭证的启用状态

        :param request: Request instance for ModifyInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNamespace(self, request):
        """更新命名空间信息

        :param request: Request instance for ModifyNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRepository(self, request):
        """更新镜像仓库信息，可修改仓库描述信息

        :param request: Request instance for ModifyRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRepository", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRepositoryAccessPersonal(self, request):
        """用于更新个人版镜像仓库的访问属性

        :param request: Request instance for ModifyRepositoryAccessPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryAccessPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryAccessPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRepositoryAccessPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRepositoryAccessPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRepositoryInfoPersonal(self, request):
        """用于在个人版镜像仓库中更新容器镜像描述

        :param request: Request instance for ModifyRepositoryInfoPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryInfoPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryInfoPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRepositoryInfoPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRepositoryInfoPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityPolicy(self, request):
        """更新实例公网访问白名单

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifySecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyServiceAccount(self, request):
        """更新服务级账号

        :param request: Request instance for ModifyServiceAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyServiceAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyServiceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTagRetentionRule(self, request):
        """更新版本保留规则

        :param request: Request instance for ModifyTagRetentionRule.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyTagRetentionRuleRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyTagRetentionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTagRetentionRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTagRetentionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserPasswordPersonal(self, request):
        """修改个人用户登录密码

        :param request: Request instance for ModifyUserPasswordPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyUserPasswordPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyUserPasswordPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserPasswordPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserPasswordPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebhookTrigger(self, request):
        """更新触发器

        :param request: Request instance for ModifyWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebhookTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebhookTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstance(self, request):
        """预付费实例续费，同时支持按量计费转包年包月

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ValidateNamespaceExistPersonal(self, request):
        """查询个人版用户命名空间是否存在

        :param request: Request instance for ValidateNamespaceExistPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ValidateNamespaceExistPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ValidateNamespaceExistPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ValidateNamespaceExistPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.ValidateNamespaceExistPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ValidateRepositoryExistPersonal(self, request):
        """用于判断个人版仓库是否存在

        :param request: Request instance for ValidateRepositoryExistPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ValidateRepositoryExistPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ValidateRepositoryExistPersonalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ValidateRepositoryExistPersonal", params, headers=headers)
            response = json.loads(body)
            model = models.ValidateRepositoryExistPersonalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))