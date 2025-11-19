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
from tencentcloud.mqtt.v20240516 import models


class MqttClient(AbstractClient):
    _apiVersion = '2024-05-16'
    _endpoint = 'mqtt.tencentcloudapi.com'
    _service = 'mqtt'


    def ActivateCaCertificate(self, request):
        r"""激活Ca证书

        :param request: Request instance for ActivateCaCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ActivateCaCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ActivateCaCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateCaCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateCaCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ActivateDeviceCertificate(self, request):
        r"""生效设备证书

        :param request: Request instance for ActivateDeviceCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ActivateDeviceCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ActivateDeviceCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateDeviceCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateDeviceCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddClientSubscription(self, request):
        r"""为MQTT客户端增加一条订阅

        :param request: Request instance for AddClientSubscription.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.AddClientSubscriptionRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.AddClientSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddClientSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.AddClientSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplyRegistrationCode(self, request):
        r"""申请ca注册码

        :param request: Request instance for ApplyRegistrationCode.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ApplyRegistrationCodeRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ApplyRegistrationCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyRegistrationCode", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyRegistrationCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuthorizationPolicy(self, request):
        r"""创建MQTT实例的性能测试任务

        :param request: Request instance for CreateAuthorizationPolicy.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateAuthorizationPolicyRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateAuthorizationPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuthorizationPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuthorizationPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeviceIdentity(self, request):
        r"""创建一机一密设备签名

        :param request: Request instance for CreateDeviceIdentity.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateDeviceIdentityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateDeviceIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHttpAuthenticator(self, request):
        r"""创建一个HTTP的认证器

        :param request: Request instance for CreateHttpAuthenticator.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateHttpAuthenticatorRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateHttpAuthenticatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHttpAuthenticator", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHttpAuthenticatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInsPublicEndpoint(self, request):
        r"""为MQTT实例创建公网接入点，未开启公网的集群可调用。

        :param request: Request instance for CreateInsPublicEndpoint.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateInsPublicEndpointRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateInsPublicEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInsPublicEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInsPublicEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        r"""购买新的MQTT实例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateInstanceResponse`

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


    def CreateJWKSAuthenticator(self, request):
        r"""创建一个jwks的认证

        :param request: Request instance for CreateJWKSAuthenticator.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateJWKSAuthenticatorRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateJWKSAuthenticatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJWKSAuthenticator", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJWKSAuthenticatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateJWTAuthenticator(self, request):
        r"""创建一个jwks的认证

        :param request: Request instance for CreateJWTAuthenticator.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateJWTAuthenticatorRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateJWTAuthenticatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJWTAuthenticator", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJWTAuthenticatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        r"""创建主题

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        r"""添加mqtt角色

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeactivateCaCertificate(self, request):
        r"""失效Ca证书

        :param request: Request instance for DeactivateCaCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeactivateCaCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeactivateCaCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeactivateCaCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeactivateCaCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeactivateDeviceCertificate(self, request):
        r"""失效Ca证书

        :param request: Request instance for DeactivateDeviceCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeactivateDeviceCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeactivateDeviceCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeactivateDeviceCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeactivateDeviceCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuthenticator(self, request):
        r"""根据认证器类型删除一个MQTT认证器

        :param request: Request instance for DeleteAuthenticator.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteAuthenticatorRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteAuthenticatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuthenticator", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuthenticatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuthorizationPolicy(self, request):
        r"""删除策略规则

        :param request: Request instance for DeleteAuthorizationPolicy.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteAuthorizationPolicyRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteAuthorizationPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuthorizationPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuthorizationPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCaCertificate(self, request):
        r"""删除Ca证书

        :param request: Request instance for DeleteCaCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteCaCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteCaCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCaCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCaCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClientSubscription(self, request):
        r"""删除MQTT客户端下的一条订阅

        :param request: Request instance for DeleteClientSubscription.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteClientSubscriptionRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteClientSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClientSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClientSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeviceCertificate(self, request):
        r"""删除设备证书

        :param request: Request instance for DeleteDeviceCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteDeviceCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteDeviceCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeviceCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeviceIdentity(self, request):
        r"""删除一机一密设备签名

        :param request: Request instance for DeleteDeviceIdentity.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteDeviceIdentityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteDeviceIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeviceIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInsPublicEndpoint(self, request):
        r"""删除MQTT实例的公网接入点

        :param request: Request instance for DeleteInsPublicEndpoint.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteInsPublicEndpointRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteInsPublicEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInsPublicEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInsPublicEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        r"""删除MQTT实例

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteInstanceResponse`

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


    def DeleteTopic(self, request):
        r"""删除MQTT主题

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        r"""删除MQTT访问用户

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthenticator(self, request):
        r"""查询MQTT认证器

        :param request: Request instance for DescribeAuthenticator.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeAuthenticatorRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeAuthenticatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthenticator", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthenticatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthorizationPolicies(self, request):
        r"""查询授权规则

        :param request: Request instance for DescribeAuthorizationPolicies.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeAuthorizationPoliciesRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeAuthorizationPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthorizationPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthorizationPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaCertificate(self, request):
        r"""查询Ca证书详情接口

        :param request: Request instance for DescribeCaCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeCaCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeCaCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaCertificates(self, request):
        r"""查询集群下的ca证书信息

        :param request: Request instance for DescribeCaCertificates.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeCaCertificatesRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeCaCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientList(self, request):
        r"""查询 MQTT 客户端详情

        :param request: Request instance for DescribeClientList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeClientListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeClientListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceCertificate(self, request):
        r"""查询设备证书详情接口

        :param request: Request instance for DescribeDeviceCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceCertificates(self, request):
        r"""分页查询设备证书

        :param request: Request instance for DescribeDeviceCertificates.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceCertificatesRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceIdentities(self, request):
        r"""查询集群下设备标识列表

        :param request: Request instance for DescribeDeviceIdentities.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceIdentitiesRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceIdentitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceIdentities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceIdentitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceIdentity(self, request):
        r"""查询设备一机一密标识

        :param request: Request instance for DescribeDeviceIdentity.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceIdentityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInsPublicEndpoints(self, request):
        r"""查询MQTT实例公网接入点

        :param request: Request instance for DescribeInsPublicEndpoints.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeInsPublicEndpointsRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeInsPublicEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInsPublicEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInsPublicEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInsVPCEndpoints(self, request):
        r"""查询MQTT实例公网接入点

        :param request: Request instance for DescribeInsVPCEndpoints.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeInsVPCEndpointsRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeInsVPCEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInsVPCEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInsVPCEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        r"""查询实例信息

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceList(self, request):
        r"""获取实例列表，Filters参数使用说明如下：
        1. InstanceName, 名称模糊查询
        2. InstanceId，实例ID查询
        3. InstanceStatus，实例状态查询，支持多选

        当使用TagFilters查询时，Filters参数失效。

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageByTopic(self, request):
        r"""根据订阅查询消息

        :param request: Request instance for DescribeMessageByTopic.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageByTopicRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageByTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageByTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageByTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageDetails(self, request):
        r"""查询MQTT消息详情

        :param request: Request instance for DescribeMessageDetails.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageDetailsRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageList(self, request):
        r"""根据一级Topic查询消息列表

        :param request: Request instance for DescribeMessageList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductSKUList(self, request):
        r"""获取产品售卖规格

        :param request: Request instance for DescribeProductSKUList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeProductSKUListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeProductSKUListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductSKUList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductSKUListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSharedSubscriptionLag(self, request):
        r"""查询共享订阅消息堆积量

        :param request: Request instance for DescribeSharedSubscriptionLag.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeSharedSubscriptionLagRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeSharedSubscriptionLagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSharedSubscriptionLag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSharedSubscriptionLagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopic(self, request):
        r"""查询mqtt主题详情

        :param request: Request instance for DescribeTopic.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeTopicRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicList(self, request):
        r"""获取主题列表，Filter参数使用说明如下：

        1. TopicName，主题名称模糊搜索
        2. TopicType，主题类型查询，支持多选，可选值：Normal,Order,Transaction,DelayScheduled

        :param request: Request instance for DescribeTopicList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeTopicListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserList(self, request):
        r"""查询用户列表，Filter参数使用说明如下：

        1. Username，用户名称模糊搜索

        :param request: Request instance for DescribeUserList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeUserListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KickOutClient(self, request):
        r"""踢出客户端

        :param request: Request instance for KickOutClient.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.KickOutClientRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.KickOutClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KickOutClient", params, headers=headers)
            response = json.loads(body)
            model = models.KickOutClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuthorizationPolicy(self, request):
        r"""修改策略规则，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)

        :param request: Request instance for ModifyAuthorizationPolicy.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyAuthorizationPolicyRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyAuthorizationPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuthorizationPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuthorizationPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceIdentity(self, request):
        r"""修改一机一密设备签名

        :param request: Request instance for ModifyDeviceIdentity.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyDeviceIdentityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyDeviceIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHttpAuthenticator(self, request):
        r"""修改MQTT HTTP 认证器

        :param request: Request instance for ModifyHttpAuthenticator.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyHttpAuthenticatorRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyHttpAuthenticatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHttpAuthenticator", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHttpAuthenticatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInsPublicEndpoint(self, request):
        r"""更新MQTT实例公网接入点

        :param request: Request instance for ModifyInsPublicEndpoint.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyInsPublicEndpointRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyInsPublicEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInsPublicEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInsPublicEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        r"""修改实例属性，只有运行中的集群可以调用该接口进行变更配置。

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyInstanceResponse`

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


    def ModifyInstanceCertBinding(self, request):
        r"""更新MQTT集群绑定证书
        参数传空，则为删除证书

        :param request: Request instance for ModifyInstanceCertBinding.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyInstanceCertBindingRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyInstanceCertBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceCertBinding", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceCertBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyJWKSAuthenticator(self, request):
        r"""修改MQTT JWKS 认证器，全量配置修改，需要提交完整的修改后配置。

        :param request: Request instance for ModifyJWKSAuthenticator.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyJWKSAuthenticatorRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyJWKSAuthenticatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJWKSAuthenticator", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJWKSAuthenticatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyJWTAuthenticator(self, request):
        r"""修改MQTT JWKS 认证器

        :param request: Request instance for ModifyJWTAuthenticator.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyJWTAuthenticatorRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyJWTAuthenticatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJWTAuthenticator", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJWTAuthenticatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopic(self, request):
        r"""修改主题属性

        :param request: Request instance for ModifyTopic.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyTopicRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        r"""修改MQTT角色

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishMessage(self, request):
        r"""发布 MQTT 消息到消息主题或客户端

        :param request: Request instance for PublishMessage.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.PublishMessageRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.PublishMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishMessage", params, headers=headers)
            response = json.loads(body)
            model = models.PublishMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterCaCertificate(self, request):
        r"""注册CA证书（仅一机一证场景支持），可参考 [自定义 X.509 证书实现 “一机一证”](https://cloud.tencent.com/document/product/1778/114817)

        :param request: Request instance for RegisterCaCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.RegisterCaCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.RegisterCaCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterCaCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterCaCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterDeviceCertificate(self, request):
        r"""注册设备证书（仅一机一证场景生效），可参考 [自定义 X.509 证书实现 “一机一证”](https://cloud.tencent.com/document/product/1778/114817#6cb39d46-efad-4220-8f11-2e7fab207bc8)

        :param request: Request instance for RegisterDeviceCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.RegisterDeviceCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.RegisterDeviceCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterDeviceCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterDeviceCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokedDeviceCertificate(self, request):
        r"""吊销设备证书

        :param request: Request instance for RevokedDeviceCertificate.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.RevokedDeviceCertificateRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.RevokedDeviceCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokedDeviceCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.RevokedDeviceCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAuthorizationPolicyPriority(self, request):
        r"""修改策略规则优先级

        :param request: Request instance for UpdateAuthorizationPolicyPriority.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.UpdateAuthorizationPolicyPriorityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.UpdateAuthorizationPolicyPriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAuthorizationPolicyPriority", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAuthorizationPolicyPriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))