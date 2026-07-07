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
from tencentcloud.alb.v20251030 import models
from typing import Dict


class AlbClient(AbstractClient):
    _apiVersion = '2025-10-30'
    _endpoint = 'alb.tencentcloudapi.com'
    _service = 'alb'

    async def AddTargetsToTargetGroup(
            self,
            request: models.AddTargetsToTargetGroupRequest,
            opts: Dict = None,
    ) -> models.AddTargetsToTargetGroupResponse:
        """
        向目标组内添加后端服务
        """
        
        kwargs = {}
        kwargs["action"] = "AddTargetsToTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTargetsToTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateBandwidthPackageWithLoadBalancer(
            self,
            request: models.AssociateBandwidthPackageWithLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.AssociateBandwidthPackageWithLoadBalancerResponse:
        """
        将共享带宽包绑定到应用型负载均衡实例。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateBandwidthPackageWithLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateBandwidthPackageWithLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateListenerAdditionalCertificates(
            self,
            request: models.AssociateListenerAdditionalCertificatesRequest,
            opts: Dict = None,
    ) -> models.AssociateListenerAdditionalCertificatesResponse:
        """
        AssociateListenerAdditionalCertificates属于异步接口，即系统返回一个请求 ID，但该扩展证书尚未添加成功，系统后台的添加任务仍在进行。您可以调用DescribeListenerCertificates接口查询扩展证书的添加状态：
        当HTTPS和QUIC监听器处于Associating状态时，表示扩展证书正在添加中。
        当HTTPS和QUIC监听器处于Associated状态时，表示扩展证书添加成功。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateListenerAdditionalCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateListenerAdditionalCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHealthCheckTemplate(
            self,
            request: models.CreateHealthCheckTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateHealthCheckTemplateResponse:
        """
        创建健康检查模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHealthCheckTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHealthCheckTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListener(
            self,
            request: models.CreateListenerRequest,
            opts: Dict = None,
    ) -> models.CreateListenerResponse:
        """
        创建监听器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancer(
            self,
            request: models.CreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerResponse:
        """
        **CreateLoadBalancer**接口属于异步接口，即系统返回一个实例ID，但该应用型负载均衡实例尚未创建成功，系统后台的创建任务仍在进行。您可以调用[DescribeLoadBalancerDetail](214362)查询应用型负载均衡实例的创建状态：
        - 当应用型负载均衡实例处于**Provisioning**状态时，表示应用型负载均衡实例正在创建中。
        - 当应用型负载均衡实例处于**Active**状态时，表示应用型负载均衡实例创建成功。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRules(
            self,
            request: models.CreateRulesRequest,
            opts: Dict = None,
    ) -> models.CreateRulesResponse:
        """
        CreateRules创建转发规则，本接口为异步接口，返回成功后需以返回的RequestID为入参，调用DescribeAsyncJobs接口查询本次任务是否成功。
        一条规则最多支持10个转发条件（Conditions），5个转发动作（Actions）。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityPolicy(
            self,
            request: models.CreateSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityPolicyResponse:
        """
        创建自定义安全策略，用于配置 HTTPS 监听器的 TLS 协议版本和加密套件。通过安全策略，您可以灵活控制客户端与负载均衡之间 HTTPS 通信的安全级别。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTargetGroup(
            self,
            request: models.CreateTargetGroupRequest,
            opts: Dict = None,
    ) -> models.CreateTargetGroupResponse:
        """
        目标组相关接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHealthCheckTemplates(
            self,
            request: models.DeleteHealthCheckTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteHealthCheckTemplatesResponse:
        """
        删除健康检查模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHealthCheckTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHealthCheckTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListener(
            self,
            request: models.DeleteListenerRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerResponse:
        """
        删除监听器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancers(
            self,
            request: models.DeleteLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancersResponse:
        """
        **DeleteLoadBalancers**接口属于异步接口，即系统返回一个请求ID，但该应用型负载均衡实例尚未删除成功，系统后台的删除任务仍在进行。您可以调用[DescribeLoadBalancerDetails](214362)查询应用型负载均衡实例的删除状态：
        - 当应用型负载均衡实例处于**Deleting**状态时，表示应用型负载均衡实例正在删除中。
        - 当查询不到指定的应用型负载均衡实例时，表示应用型负载均衡实例删除成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRules(
            self,
            request: models.DeleteRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteRulesResponse:
        """
        DeleteRules删除转发规则，本接口为异步接口，返回成功后需以返回的RequestID为入参，调用DescribeAsyncJobs接口查询本次任务是否成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityPolicy(
            self,
            request: models.DeleteSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityPolicyResponse:
        """
        删除一个或多个自定义安全策略。删除安全策略前，请确保该策略未被任何 HTTPS 监听器引用，否则删除操作将失败。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTargetGroups(
            self,
            request: models.DeleteTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteTargetGroupsResponse:
        """
        删除目标组。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncJobs(
            self,
            request: models.DescribeAsyncJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncJobsResponse:
        """
        异步任务查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthCheckTemplates(
            self,
            request: models.DescribeHealthCheckTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthCheckTemplatesResponse:
        """
        查询健康检查模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthCheckTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthCheckTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerCertificates(
            self,
            request: models.DescribeListenerCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerCertificatesResponse:
        """
        根据实例id和监听器id，查询指定监听器绑定的证书列表
        若输入CertificateType为SVR，返回扩展服务器证书与默认服务器证书的信息
        若输入CertificateType为CA，返回默认CA证书的信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerDetail(
            self,
            request: models.DescribeListenerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerDetailResponse:
        """
        查询单个监听器详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerHealthStatus(
            self,
            request: models.DescribeListenerHealthStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerHealthStatusResponse:
        """
        查询监听器健康状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerHealthStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerHealthStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListeners(
            self,
            request: models.DescribeListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenersResponse:
        """
        查询监听器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancerDetail(
            self,
            request: models.DescribeLoadBalancerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerDetailResponse:
        """
        查询指定负载均衡实例的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancers(
            self,
            request: models.DescribeLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancersResponse:
        """
        查询实例配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuota(
            self,
            request: models.DescribeQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotaResponse:
        """
        查询当前账号的 ALB 配额配置。支持按配额类型查询，也支持传入资源ID查询资源级配额；可通过 DisplayFields 按需返回已使用量和剩余可用量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        查询转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicies(
            self,
            request: models.DescribeSecurityPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPoliciesResponse:
        """
        查询自定义安全策略列表，支持按安全策略 ID、名称或标签进行筛选，并支持分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyCapabilities(
            self,
            request: models.DescribeSecurityPolicyCapabilitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyCapabilitiesResponse:
        """
        查询当前地域支持的安全策略配置能力，包括可选的 TLS 协议版本及各版本对应的加密套件列表。在创建或修改自定义安全策略前，建议先调用此接口获取可用的配置选项。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyCapabilities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyCapabilitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyRelations(
            self,
            request: models.DescribeSecurityPolicyRelationsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyRelationsResponse:
        """
        查询安全策略的关联关系，即安全策略被哪些 HTTPS 监听器引用。在删除或修改安全策略前，建议先调用此接口确认影响范围。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyRelations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyRelationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemSecurityPolicies(
            self,
            request: models.DescribeSystemSecurityPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemSecurityPoliciesResponse:
        """
        查询系统安全策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemSecurityPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemSecurityPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupTargets(
            self,
            request: models.DescribeTargetGroupTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupTargetsResponse:
        """
        查询目标组内后端服务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroups(
            self,
            request: models.DescribeTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupsResponse:
        """
        查询目标组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupsByTarget(
            self,
            request: models.DescribeTargetGroupsByTargetRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupsByTargetResponse:
        """
        根据子机查询绑定的目标组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupsByTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupsByTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        查询可用区
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateBandwidthPackageFromLoadBalancer(
            self,
            request: models.DisassociateBandwidthPackageFromLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DisassociateBandwidthPackageFromLoadBalancerResponse:
        """
        将共享带宽包从应用型负载均衡实例解绑。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateBandwidthPackageFromLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateBandwidthPackageFromLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateListenerAdditionalCertificates(
            self,
            request: models.DisassociateListenerAdditionalCertificatesRequest,
            opts: Dict = None,
    ) -> models.DisassociateListenerAdditionalCertificatesResponse:
        """
        DisassociateListenerAdditionalCertificates属于异步接口，即系统返回一个请求 ID，但该扩展证书尚未解绑成功，系统后台的解绑任务仍在进行。您可以调用DescribeListenerCertificates接口查询证书的解绑状态：若证书处于Disassociating状态，则证书正在解绑中。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateListenerAdditionalCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateListenerAdditionalCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateLoadBalancer(
            self,
            request: models.InquirePriceCreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateLoadBalancerResponse:
        """
        InquirePriceCreateLoadBalancer接口查询创建负载均衡的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHealthCheckTemplate(
            self,
            request: models.ModifyHealthCheckTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyHealthCheckTemplateResponse:
        """
        修改健康检查模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHealthCheckTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHealthCheckTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyListenerAttributes(
            self,
            request: models.ModifyListenerAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyListenerAttributesResponse:
        """
        修改监听器属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyListenerAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyListenerAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerAddressType(
            self,
            request: models.ModifyLoadBalancerAddressTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerAddressTypeResponse:
        """
        **前提条件：**
        您已经创建应用型负载均衡实例，具体操作，请参见 CreateLoadBalancer 。
        当您需要通过此接口将应用型负载均衡实例的网络类型由私网变为公网时，您需要先创建一个弹性公网 IP。
        **使用说明：**
        ModifyLoadBalancerAddressType 接口属于异步接口，即系统返回一个请求 ID，但该应用型负载均衡实例的网络类型尚未变更成功，系统后台的变更任务仍在进行。您可以调用 DescribeLoadBalancerDetail 查询应用型负载均衡实例的网络类型的变更状态：
        当应用型负载均衡实例处于 Configuring 状态时，表示应用型负载均衡实例的网络类型正在变更中。
        当应用型负载均衡实例处于 Active 状态时，表示应用型负载均衡实例的网络类型变更成功。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerAddressType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerAddressTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerAttributes(
            self,
            request: models.ModifyLoadBalancerAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerAttributesResponse:
        """
        **ModifyLoadBalancerAttributes**接口属于异步接口，即系统返回一个请求ID，但该应用型负载均衡实例属性尚未修改成功，系统后台的修改任务仍在进行。您可以调用[DescribeLoadBalancerAttribute](214362)查询应用型负载均衡实例属性的修改状态：
        - 当应用型负载均衡实例属性处于**Configuring**状态时，表示应用型负载均衡实例属性正在修改中。
        - 当应用型负载均衡实例属性处于**Active**状态时，表示应用型负载均衡实例属性修改成功。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerModificationProtection(
            self,
            request: models.ModifyLoadBalancerModificationProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerModificationProtectionResponse:
        """
        设置负载均衡实例修改保护。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerModificationProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerModificationProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRulesAttributes(
            self,
            request: models.ModifyRulesAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyRulesAttributesResponse:
        """
        ModifyRulesAttributes修改转发规则属性，本接口为异步接口，返回成功后需以返回的RequestID为入参，调用DescribeAsyncJobs接口查询本次任务是否成功。
        一条规则最多支持10个转发条件（Conditions），5个转发动作（Actions）。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRulesAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRulesAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityPolicyAttributes(
            self,
            request: models.ModifySecurityPolicyAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityPolicyAttributesResponse:
        """
        修改自定义安全策略的属性，包括策略名称、TLS 协议版本和加密套件。修改后的配置将立即应用到所有关联该策略的 HTTPS 监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityPolicyAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityPolicyAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupAttributes(
            self,
            request: models.ModifyTargetGroupAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupAttributesResponse:
        """
        修改目标组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetsInTargetGroup(
            self,
            request: models.ModifyTargetsInTargetGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetsInTargetGroupResponse:
        """
        修改目标组内后端服务信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetsInTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetsInTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def NotifyUnbindTarget(
            self,
            request: models.NotifyUnbindTargetRequest,
            opts: Dict = None,
    ) -> models.NotifyUnbindTargetResponse:
        """
        通知负载均衡解绑后端服务
        """
        
        kwargs = {}
        kwargs["action"] = "NotifyUnbindTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.NotifyUnbindTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveTargetsFromTargetGroup(
            self,
            request: models.RemoveTargetsFromTargetGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveTargetsFromTargetGroupResponse:
        """
        从目标组内移除后端服务
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveTargetsFromTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveTargetsFromTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLoadBalancerSecurityGroups(
            self,
            request: models.SetLoadBalancerSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.SetLoadBalancerSecurityGroupsResponse:
        """
        SetLoadBalancerSecurityGroups 接口支持对一个公网负载均衡实例执行设置（绑定、解绑）安全组操作。查询一个负载均衡实例目前已绑定的安全组，可使用 [DescribeLoadBalancerDetail](xxx) 接口。本接口是set语义，
        绑定操作时，入参需要传入负载均衡实例要绑定的所有安全组（已绑定的+新增绑定的）。
        解绑操作时，入参需要传入负载均衡实例执行解绑后所绑定的所有安全组；如果要解绑所有安全组，可不传此参数，或传入空数组。
        """
        
        kwargs = {}
        kwargs["action"] = "SetLoadBalancerSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLoadBalancerSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)