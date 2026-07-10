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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.alb.v20251030 import models


class AlbClient(AbstractClient):
    _apiVersion = '2025-10-30'
    _endpoint = 'alb.tencentcloudapi.com'
    _service = 'alb'


    def AddTargetsToTargetGroup(self, request):
        r"""向目标组内添加后端服务

        :param request: Request instance for AddTargetsToTargetGroup.
        :type request: :class:`tencentcloud.alb.v20251030.models.AddTargetsToTargetGroupRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.AddTargetsToTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTargetsToTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddTargetsToTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateBandwidthPackageWithLoadBalancer(self, request):
        r"""将共享带宽包绑定到应用型负载均衡实例。

        :param request: Request instance for AssociateBandwidthPackageWithLoadBalancer.
        :type request: :class:`tencentcloud.alb.v20251030.models.AssociateBandwidthPackageWithLoadBalancerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.AssociateBandwidthPackageWithLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateBandwidthPackageWithLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateBandwidthPackageWithLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateListenerAdditionalCertificates(self, request):
        r"""AssociateListenerAdditionalCertificates属于异步接口，即系统返回一个请求 ID，但该扩展证书尚未添加成功，系统后台的添加任务仍在进行。您可以调用DescribeListenerCertificates接口查询扩展证书的添加状态：
        当HTTPS和QUIC监听器处于Associating状态时，表示扩展证书正在添加中。
        当HTTPS和QUIC监听器处于Associated状态时，表示扩展证书添加成功。

        :param request: Request instance for AssociateListenerAdditionalCertificates.
        :type request: :class:`tencentcloud.alb.v20251030.models.AssociateListenerAdditionalCertificatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.AssociateListenerAdditionalCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateListenerAdditionalCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateListenerAdditionalCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHealthCheckTemplate(self, request):
        r"""创建健康检查模板

        :param request: Request instance for CreateHealthCheckTemplate.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateHealthCheckTemplateRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateHealthCheckTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHealthCheckTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHealthCheckTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateListener(self, request):
        r"""创建监听器

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateListener", params, headers=headers)
            response = json.loads(body)
            model = models.CreateListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancer(self, request):
        r"""**CreateLoadBalancer**接口属于异步接口，即系统返回一个实例ID，但该应用型负载均衡实例尚未创建成功，系统后台的创建任务仍在进行。您可以调用[DescribeLoadBalancerDetail](https://cloud.tencent.com/document/api/1822/133711)查询应用型负载均衡实例的创建状态：
        - 当应用型负载均衡实例处于**Provisioning**状态时，表示应用型负载均衡实例正在创建中。
        - 当应用型负载均衡实例处于**Active**状态时，表示应用型负载均衡实例创建成功。

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRules(self, request):
        r"""CreateRules创建转发规则，本接口为异步接口，返回成功后需以返回的RequestID为入参，调用DescribeAsyncJobs接口查询本次任务是否成功。
        一条规则最多支持10个转发条件（Conditions），5个转发动作（Actions）。

        :param request: Request instance for CreateRules.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateRulesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityPolicy(self, request):
        r"""创建自定义安全策略，用于配置 HTTPS 监听器的 TLS 协议版本和加密套件。通过安全策略，您可以灵活控制客户端与负载均衡之间 HTTPS 通信的安全级别。

        :param request: Request instance for CreateSecurityPolicy.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateSecurityPolicyResponse`

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


    def CreateTargetGroup(self, request):
        r"""目标组相关接口

        :param request: Request instance for CreateTargetGroup.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateTargetGroupRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHealthCheckTemplates(self, request):
        r"""删除健康检查模板

        :param request: Request instance for DeleteHealthCheckTemplates.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteHealthCheckTemplatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteHealthCheckTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHealthCheckTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHealthCheckTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteListener(self, request):
        r"""删除监听器

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteListener", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancers(self, request):
        r"""**DeleteLoadBalancers**接口属于异步接口，即系统返回一个请求ID，但该应用型负载均衡实例尚未删除成功，系统后台的删除任务仍在进行。您可以调用[DescribeLoadBalancerDetail](https://cloud.tencent.com/document/api/1822/133711)查询应用型负载均衡实例的删除状态：
        - 当应用型负载均衡实例处于**Deleting**状态时，表示应用型负载均衡实例正在删除中。
        - 当查询不到指定的应用型负载均衡实例时，表示应用型负载均衡实例删除成功。

        :param request: Request instance for DeleteLoadBalancers.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteLoadBalancersRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRules(self, request):
        r"""DeleteRules删除转发规则，本接口为异步接口，返回成功后需以返回的RequestID为入参，调用DescribeAsyncJobs接口查询本次任务是否成功。

        :param request: Request instance for DeleteRules.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityPolicy(self, request):
        r"""删除一个或多个自定义安全策略。删除安全策略前，请确保该策略未被任何 HTTPS 监听器引用，否则删除操作将失败。

        :param request: Request instance for DeleteSecurityPolicy.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteSecurityPolicyResponse`

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


    def DeleteTargetGroups(self, request):
        r"""删除目标组。

        :param request: Request instance for DeleteTargetGroups.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteTargetGroupsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAsyncJobs(self, request):
        r"""异步任务查询接口

        :param request: Request instance for DescribeAsyncJobs.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeAsyncJobsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeAsyncJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsyncJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsyncJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHealthCheckTemplates(self, request):
        r"""查询健康检查模板列表

        :param request: Request instance for DescribeHealthCheckTemplates.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeHealthCheckTemplatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeHealthCheckTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHealthCheckTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHealthCheckTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerCertificates(self, request):
        r"""根据实例id和监听器id，查询指定监听器绑定的证书列表
        若输入CertificateType为SVR，返回扩展服务器证书与默认服务器证书的信息
        若输入CertificateType为CA，返回默认CA证书的信息

        :param request: Request instance for DescribeListenerCertificates.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeListenerCertificatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeListenerCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerDetail(self, request):
        r"""查询单个监听器详情

        :param request: Request instance for DescribeListenerDetail.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeListenerDetailRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeListenerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerHealthStatus(self, request):
        r"""查询监听器健康状态。

        :param request: Request instance for DescribeListenerHealthStatus.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeListenerHealthStatusRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeListenerHealthStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerHealthStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerHealthStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListeners(self, request):
        r"""查询监听器列表

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerDetail(self, request):
        r"""查询指定负载均衡实例的详细信息。

        :param request: Request instance for DescribeLoadBalancerDetail.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeLoadBalancerDetailRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeLoadBalancerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancers(self, request):
        r"""查询实例配置。

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuota(self, request):
        r"""查询当前账号的 ALB 配额配置。支持按配额类型查询，也支持传入资源ID查询资源级配额；可通过 DisplayFields 按需返回已使用量和剩余可用量。

        :param request: Request instance for DescribeQuota.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeQuotaRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        r"""查询转发规则

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicies(self, request):
        r"""查询自定义安全策略列表，支持按安全策略 ID、名称或标签进行筛选，并支持分页查询。

        :param request: Request instance for DescribeSecurityPolicies.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPoliciesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPoliciesResponse`

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


    def DescribeSecurityPolicyCapabilities(self, request):
        r"""查询当前地域支持的安全策略配置能力，包括可选的 TLS 协议版本及各版本对应的加密套件列表。在创建或修改自定义安全策略前，建议先调用此接口获取可用的配置选项。

        :param request: Request instance for DescribeSecurityPolicyCapabilities.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPolicyCapabilitiesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPolicyCapabilitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyCapabilities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyCapabilitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicyRelations(self, request):
        r"""查询安全策略的关联关系，即安全策略被哪些 HTTPS 监听器引用。在删除或修改安全策略前，建议先调用此接口确认影响范围。

        :param request: Request instance for DescribeSecurityPolicyRelations.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPolicyRelationsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPolicyRelationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyRelations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyRelationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemSecurityPolicies(self, request):
        r"""查询系统安全策略。

        :param request: Request instance for DescribeSystemSecurityPolicies.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeSystemSecurityPoliciesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeSystemSecurityPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemSecurityPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemSecurityPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupTargets(self, request):
        r"""查询目标组内后端服务

        :param request: Request instance for DescribeTargetGroupTargets.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupTargetsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroups(self, request):
        r"""查询目标组列表

        :param request: Request instance for DescribeTargetGroups.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupsByTarget(self, request):
        r"""根据子机查询绑定的目标组

        :param request: Request instance for DescribeTargetGroupsByTarget.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupsByTargetRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupsByTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupsByTarget", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupsByTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        r"""查询可用区

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateBandwidthPackageFromLoadBalancer(self, request):
        r"""将共享带宽包从应用型负载均衡实例解绑。

        :param request: Request instance for DisassociateBandwidthPackageFromLoadBalancer.
        :type request: :class:`tencentcloud.alb.v20251030.models.DisassociateBandwidthPackageFromLoadBalancerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DisassociateBandwidthPackageFromLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateBandwidthPackageFromLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateBandwidthPackageFromLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateListenerAdditionalCertificates(self, request):
        r"""DisassociateListenerAdditionalCertificates属于异步接口，即系统返回一个请求 ID，但该扩展证书尚未解绑成功，系统后台的解绑任务仍在进行。您可以调用DescribeListenerCertificates接口查询证书的解绑状态：若证书处于Disassociating状态，则证书正在解绑中。

        :param request: Request instance for DisassociateListenerAdditionalCertificates.
        :type request: :class:`tencentcloud.alb.v20251030.models.DisassociateListenerAdditionalCertificatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DisassociateListenerAdditionalCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateListenerAdditionalCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateListenerAdditionalCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateLoadBalancer(self, request):
        r"""InquirePriceCreateLoadBalancer接口查询创建负载均衡的价格。

        :param request: Request instance for InquirePriceCreateLoadBalancer.
        :type request: :class:`tencentcloud.alb.v20251030.models.InquirePriceCreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.InquirePriceCreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHealthCheckTemplate(self, request):
        r"""修改健康检查模板

        :param request: Request instance for ModifyHealthCheckTemplate.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyHealthCheckTemplateRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyHealthCheckTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHealthCheckTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHealthCheckTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyListenerAttributes(self, request):
        r"""修改监听器属性

        :param request: Request instance for ModifyListenerAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyListenerAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyListenerAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyListenerAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyListenerAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerAddressType(self, request):
        r"""**前提条件：**
        您已经创建应用型负载均衡实例，具体操作，请参见 CreateLoadBalancer 。
        当您需要通过此接口将应用型负载均衡实例的网络类型由私网变为公网时，您需要先创建一个弹性公网 IP。
        **使用说明：**
        ModifyLoadBalancerAddressType 接口属于异步接口，即系统返回一个请求 ID，但该应用型负载均衡实例的网络类型尚未变更成功，系统后台的变更任务仍在进行。您可以调用 DescribeLoadBalancerDetail 查询应用型负载均衡实例的网络类型的变更状态：
        当应用型负载均衡实例处于 Configuring 状态时，表示应用型负载均衡实例的网络类型正在变更中。
        当应用型负载均衡实例处于 Active 状态时，表示应用型负载均衡实例的网络类型变更成功。

        :param request: Request instance for ModifyLoadBalancerAddressType.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerAddressTypeRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerAddressTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerAddressType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerAddressTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerAttributes(self, request):
        r"""**ModifyLoadBalancerAttributes**接口属于异步接口，即系统返回一个请求ID，但该应用型负载均衡实例属性尚未修改成功，系统后台的修改任务仍在进行。您可以调用[DescribeLoadBalancerDetail](https://cloud.tencent.com/document/api/1822/133711)查询应用型负载均衡实例属性的修改状态：
        - 当应用型负载均衡实例属性处于**Configuring**状态时，表示应用型负载均衡实例属性正在修改中。
        - 当应用型负载均衡实例属性处于**Active**状态时，表示应用型负载均衡实例属性修改成功。

        :param request: Request instance for ModifyLoadBalancerAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerModificationProtection(self, request):
        r"""设置负载均衡实例修改保护。

        :param request: Request instance for ModifyLoadBalancerModificationProtection.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerModificationProtectionRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerModificationProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerModificationProtection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerModificationProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRulesAttributes(self, request):
        r"""ModifyRulesAttributes修改转发规则属性，本接口为异步接口，返回成功后需以返回的RequestID为入参，调用DescribeAsyncJobs接口查询本次任务是否成功。
        一条规则最多支持10个转发条件（Conditions），5个转发动作（Actions）。

        :param request: Request instance for ModifyRulesAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyRulesAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyRulesAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRulesAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRulesAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityPolicyAttributes(self, request):
        r"""修改自定义安全策略的属性，包括策略名称、TLS 协议版本和加密套件。修改后的配置将立即应用到所有关联该策略的 HTTPS 监听器。

        :param request: Request instance for ModifySecurityPolicyAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifySecurityPolicyAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifySecurityPolicyAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicyAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityPolicyAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupAttributes(self, request):
        r"""修改目标组。

        :param request: Request instance for ModifyTargetGroupAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyTargetGroupAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyTargetGroupAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetsInTargetGroup(self, request):
        r"""修改目标组内后端服务信息

        :param request: Request instance for ModifyTargetsInTargetGroup.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyTargetsInTargetGroupRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyTargetsInTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetsInTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetsInTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def NotifyUnbindTarget(self, request):
        r"""通知负载均衡解绑后端服务

        :param request: Request instance for NotifyUnbindTarget.
        :type request: :class:`tencentcloud.alb.v20251030.models.NotifyUnbindTargetRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.NotifyUnbindTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("NotifyUnbindTarget", params, headers=headers)
            response = json.loads(body)
            model = models.NotifyUnbindTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveTargetsFromTargetGroup(self, request):
        r"""从目标组内移除后端服务

        :param request: Request instance for RemoveTargetsFromTargetGroup.
        :type request: :class:`tencentcloud.alb.v20251030.models.RemoveTargetsFromTargetGroupRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.RemoveTargetsFromTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveTargetsFromTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveTargetsFromTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLoadBalancerSecurityGroups(self, request):
        r"""SetLoadBalancerSecurityGroups 接口支持对一个公网负载均衡实例执行设置（绑定、解绑）安全组操作。查询一个负载均衡实例目前已绑定的安全组，可使用 [DescribeLoadBalancerDetail](https://cloud.tencent.com/document/api/1822/133711) 接口。本接口是set语义，
        绑定操作时，入参需要传入负载均衡实例要绑定的所有安全组（已绑定的+新增绑定的）。
        解绑操作时，入参需要传入负载均衡实例执行解绑后所绑定的所有安全组；如果要解绑所有安全组，可不传此参数，或传入空数组。

        :param request: Request instance for SetLoadBalancerSecurityGroups.
        :type request: :class:`tencentcloud.alb.v20251030.models.SetLoadBalancerSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.SetLoadBalancerSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLoadBalancerSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.SetLoadBalancerSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))