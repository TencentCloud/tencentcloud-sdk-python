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
from tencentcloud.mqtt.v20240516 import models
from typing import Dict


class MqttClient(AbstractClient):
    _apiVersion = '2024-05-16'
    _endpoint = 'mqtt.tencentcloudapi.com'
    _service = 'mqtt'

    async def ActivateCaCertificate(
            self,
            request: models.ActivateCaCertificateRequest,
            opts: Dict = None,
    ) -> models.ActivateCaCertificateResponse:
        """
        激活Ca证书
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateCaCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateCaCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ActivateDeviceCertificate(
            self,
            request: models.ActivateDeviceCertificateRequest,
            opts: Dict = None,
    ) -> models.ActivateDeviceCertificateResponse:
        """
        生效设备证书
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateDeviceCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateDeviceCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddClientSubscription(
            self,
            request: models.AddClientSubscriptionRequest,
            opts: Dict = None,
    ) -> models.AddClientSubscriptionResponse:
        """
        为MQTT客户端增加一条订阅
        """
        
        kwargs = {}
        kwargs["action"] = "AddClientSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddClientSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyRegistrationCode(
            self,
            request: models.ApplyRegistrationCodeRequest,
            opts: Dict = None,
    ) -> models.ApplyRegistrationCodeResponse:
        """
        申请ca注册码
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyRegistrationCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyRegistrationCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuthorizationPolicy(
            self,
            request: models.CreateAuthorizationPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAuthorizationPolicyResponse:
        """
        创建MQTT实例的性能测试任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuthorizationPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuthorizationPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeviceIdentity(
            self,
            request: models.CreateDeviceIdentityRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceIdentityResponse:
        """
        创建一机一密设备签名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeviceIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHttpAuthenticator(
            self,
            request: models.CreateHttpAuthenticatorRequest,
            opts: Dict = None,
    ) -> models.CreateHttpAuthenticatorResponse:
        """
        创建一个HTTP的认证器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHttpAuthenticator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHttpAuthenticatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInsPublicEndpoint(
            self,
            request: models.CreateInsPublicEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateInsPublicEndpointResponse:
        """
        为MQTT实例创建公网接入点，未开启公网的集群可调用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInsPublicEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInsPublicEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        购买新的MQTT实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJWKSAuthenticator(
            self,
            request: models.CreateJWKSAuthenticatorRequest,
            opts: Dict = None,
    ) -> models.CreateJWKSAuthenticatorResponse:
        """
        创建一个jwks的认证
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJWKSAuthenticator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJWKSAuthenticatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJWTAuthenticator(
            self,
            request: models.CreateJWTAuthenticatorRequest,
            opts: Dict = None,
    ) -> models.CreateJWTAuthenticatorResponse:
        """
        创建一个jwks的认证
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJWTAuthenticator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJWTAuthenticatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMessageEnrichmentRule(
            self,
            request: models.CreateMessageEnrichmentRuleRequest,
            opts: Dict = None,
    ) -> models.CreateMessageEnrichmentRuleResponse:
        """
        创建一条消息属性增强规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMessageEnrichmentRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMessageEnrichmentRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        创建主题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        添加mqtt角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeactivateCaCertificate(
            self,
            request: models.DeactivateCaCertificateRequest,
            opts: Dict = None,
    ) -> models.DeactivateCaCertificateResponse:
        """
        失效Ca证书
        """
        
        kwargs = {}
        kwargs["action"] = "DeactivateCaCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeactivateCaCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeactivateDeviceCertificate(
            self,
            request: models.DeactivateDeviceCertificateRequest,
            opts: Dict = None,
    ) -> models.DeactivateDeviceCertificateResponse:
        """
        失效Ca证书
        """
        
        kwargs = {}
        kwargs["action"] = "DeactivateDeviceCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeactivateDeviceCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuthenticator(
            self,
            request: models.DeleteAuthenticatorRequest,
            opts: Dict = None,
    ) -> models.DeleteAuthenticatorResponse:
        """
        根据认证器类型删除一个MQTT认证器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuthenticator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuthenticatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuthorizationPolicy(
            self,
            request: models.DeleteAuthorizationPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAuthorizationPolicyResponse:
        """
        删除策略规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuthorizationPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuthorizationPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCaCertificate(
            self,
            request: models.DeleteCaCertificateRequest,
            opts: Dict = None,
    ) -> models.DeleteCaCertificateResponse:
        """
        删除Ca证书
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCaCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCaCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClientSubscription(
            self,
            request: models.DeleteClientSubscriptionRequest,
            opts: Dict = None,
    ) -> models.DeleteClientSubscriptionResponse:
        """
        删除MQTT客户端下的一条订阅
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClientSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClientSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceCertificate(
            self,
            request: models.DeleteDeviceCertificateRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceCertificateResponse:
        """
        删除设备证书
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceIdentity(
            self,
            request: models.DeleteDeviceIdentityRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceIdentityResponse:
        """
        删除一机一密设备签名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInsPublicEndpoint(
            self,
            request: models.DeleteInsPublicEndpointRequest,
            opts: Dict = None,
    ) -> models.DeleteInsPublicEndpointResponse:
        """
        删除MQTT实例的公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInsPublicEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInsPublicEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        删除MQTT实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMessageEnrichmentRule(
            self,
            request: models.DeleteMessageEnrichmentRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteMessageEnrichmentRuleResponse:
        """
        删除消息属性增强规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMessageEnrichmentRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMessageEnrichmentRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        删除MQTT主题
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        删除MQTT访问用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthenticator(
            self,
            request: models.DescribeAuthenticatorRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthenticatorResponse:
        """
        查询MQTT认证器
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthenticator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthenticatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthorizationPolicies(
            self,
            request: models.DescribeAuthorizationPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthorizationPoliciesResponse:
        """
        查询授权规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthorizationPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthorizationPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaCertificate(
            self,
            request: models.DescribeCaCertificateRequest,
            opts: Dict = None,
    ) -> models.DescribeCaCertificateResponse:
        """
        查询Ca证书详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaCertificates(
            self,
            request: models.DescribeCaCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeCaCertificatesResponse:
        """
        查询集群下的ca证书信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientList(
            self,
            request: models.DescribeClientListRequest,
            opts: Dict = None,
    ) -> models.DescribeClientListResponse:
        """
        查询 MQTT 客户端详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceCertificate(
            self,
            request: models.DescribeDeviceCertificateRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceCertificateResponse:
        """
        查询设备证书详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceCertificates(
            self,
            request: models.DescribeDeviceCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceCertificatesResponse:
        """
        分页查询设备证书
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceIdentities(
            self,
            request: models.DescribeDeviceIdentitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceIdentitiesResponse:
        """
        查询集群下设备标识列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceIdentities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceIdentitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceIdentity(
            self,
            request: models.DescribeDeviceIdentityRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceIdentityResponse:
        """
        查询设备一机一密标识
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInsPublicEndpoints(
            self,
            request: models.DescribeInsPublicEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeInsPublicEndpointsResponse:
        """
        查询MQTT实例公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInsPublicEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInsPublicEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInsVPCEndpoints(
            self,
            request: models.DescribeInsVPCEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeInsVPCEndpointsResponse:
        """
        查询MQTT实例公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInsVPCEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInsVPCEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        查询实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceList(
            self,
            request: models.DescribeInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceListResponse:
        """
        获取实例列表，Filters参数使用说明如下：
        1. InstanceName, 名称模糊查询
        2. InstanceId，实例ID查询
        3. InstanceStatus，实例状态查询，支持多选

        当使用TagFilters查询时，Filters参数失效。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageByTopic(
            self,
            request: models.DescribeMessageByTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageByTopicResponse:
        """
        根据订阅查询消息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageByTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageByTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageDetails(
            self,
            request: models.DescribeMessageDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageDetailsResponse:
        """
        查询MQTT消息详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageEnrichmentRules(
            self,
            request: models.DescribeMessageEnrichmentRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageEnrichmentRulesResponse:
        """
        查询消息属性增强规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageEnrichmentRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageEnrichmentRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageList(
            self,
            request: models.DescribeMessageListRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageListResponse:
        """
        根据一级Topic查询消息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductSKUList(
            self,
            request: models.DescribeProductSKUListRequest,
            opts: Dict = None,
    ) -> models.DescribeProductSKUListResponse:
        """
        获取产品售卖规格
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductSKUList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductSKUListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSharedSubscriptionLag(
            self,
            request: models.DescribeSharedSubscriptionLagRequest,
            opts: Dict = None,
    ) -> models.DescribeSharedSubscriptionLagResponse:
        """
        查询共享订阅消息堆积量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSharedSubscriptionLag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSharedSubscriptionLagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopic(
            self,
            request: models.DescribeTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicResponse:
        """
        查询mqtt主题详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicList(
            self,
            request: models.DescribeTopicListRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicListResponse:
        """
        获取主题列表，Filter参数使用说明如下：

        1. TopicName，主题名称模糊搜索
        2. TopicType，主题类型查询，支持多选，可选值：Normal,Order,Transaction,DelayScheduled
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserList(
            self,
            request: models.DescribeUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserListResponse:
        """
        查询用户列表，Filter参数使用说明如下：

        1. Username，用户名称模糊搜索
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KickOutClient(
            self,
            request: models.KickOutClientRequest,
            opts: Dict = None,
    ) -> models.KickOutClientResponse:
        """
        踢出客户端
        """
        
        kwargs = {}
        kwargs["action"] = "KickOutClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KickOutClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuthorizationPolicy(
            self,
            request: models.ModifyAuthorizationPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyAuthorizationPolicyResponse:
        """
        修改策略规则，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuthorizationPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuthorizationPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceIdentity(
            self,
            request: models.ModifyDeviceIdentityRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceIdentityResponse:
        """
        修改一机一密设备签名
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHttpAuthenticator(
            self,
            request: models.ModifyHttpAuthenticatorRequest,
            opts: Dict = None,
    ) -> models.ModifyHttpAuthenticatorResponse:
        """
        修改MQTT HTTP 认证器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHttpAuthenticator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHttpAuthenticatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInsPublicEndpoint(
            self,
            request: models.ModifyInsPublicEndpointRequest,
            opts: Dict = None,
    ) -> models.ModifyInsPublicEndpointResponse:
        """
        更新MQTT实例公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInsPublicEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInsPublicEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        修改实例属性，只有运行中的集群可以调用该接口进行变更配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceCertBinding(
            self,
            request: models.ModifyInstanceCertBindingRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceCertBindingResponse:
        """
        更新MQTT集群绑定证书
        参数传空，则为删除证书
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceCertBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceCertBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyJWKSAuthenticator(
            self,
            request: models.ModifyJWKSAuthenticatorRequest,
            opts: Dict = None,
    ) -> models.ModifyJWKSAuthenticatorResponse:
        """
        修改MQTT JWKS 认证器，全量配置修改，需要提交完整的修改后配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJWKSAuthenticator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJWKSAuthenticatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyJWTAuthenticator(
            self,
            request: models.ModifyJWTAuthenticatorRequest,
            opts: Dict = None,
    ) -> models.ModifyJWTAuthenticatorResponse:
        """
        修改MQTT JWKS 认证器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJWTAuthenticator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJWTAuthenticatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMessageEnrichmentRule(
            self,
            request: models.ModifyMessageEnrichmentRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyMessageEnrichmentRuleResponse:
        """
        修改消息属性增强规则
        注意：需要提交当前规则的所有属性，即使某些字段没有修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMessageEnrichmentRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMessageEnrichmentRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopic(
            self,
            request: models.ModifyTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicResponse:
        """
        修改主题属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        修改MQTT角色
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishMessage(
            self,
            request: models.PublishMessageRequest,
            opts: Dict = None,
    ) -> models.PublishMessageResponse:
        """
        发布 MQTT 消息到消息主题或客户端
        """
        
        kwargs = {}
        kwargs["action"] = "PublishMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterCaCertificate(
            self,
            request: models.RegisterCaCertificateRequest,
            opts: Dict = None,
    ) -> models.RegisterCaCertificateResponse:
        """
        注册CA证书（仅一机一证场景支持），可参考 [自定义 X.509 证书实现 “一机一证”](https://cloud.tencent.com/document/product/1778/114817)
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterCaCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterCaCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterDeviceCertificate(
            self,
            request: models.RegisterDeviceCertificateRequest,
            opts: Dict = None,
    ) -> models.RegisterDeviceCertificateResponse:
        """
        注册设备证书（仅一机一证场景生效），可参考 [自定义 X.509 证书实现 “一机一证”](https://cloud.tencent.com/document/product/1778/114817#6cb39d46-efad-4220-8f11-2e7fab207bc8)
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterDeviceCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterDeviceCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokedDeviceCertificate(
            self,
            request: models.RevokedDeviceCertificateRequest,
            opts: Dict = None,
    ) -> models.RevokedDeviceCertificateResponse:
        """
        吊销设备证书
        """
        
        kwargs = {}
        kwargs["action"] = "RevokedDeviceCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokedDeviceCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAuthorizationPolicyPriority(
            self,
            request: models.UpdateAuthorizationPolicyPriorityRequest,
            opts: Dict = None,
    ) -> models.UpdateAuthorizationPolicyPriorityResponse:
        """
        修改策略规则优先级
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAuthorizationPolicyPriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAuthorizationPolicyPriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateMessageEnrichmentRulePriority(
            self,
            request: models.UpdateMessageEnrichmentRulePriorityRequest,
            opts: Dict = None,
    ) -> models.UpdateMessageEnrichmentRulePriorityResponse:
        """
        修改消息属性增强规则优先级
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateMessageEnrichmentRulePriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateMessageEnrichmentRulePriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)