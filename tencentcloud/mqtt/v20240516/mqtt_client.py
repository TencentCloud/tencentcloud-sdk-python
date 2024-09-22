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
from tencentcloud.mqtt.v20240516 import models


class MqttClient(AbstractClient):
    _apiVersion = '2024-05-16'
    _endpoint = 'mqtt.tencentcloudapi.com'
    _service = 'mqtt'


    def CreateAuthorizationPolicy(self, request):
        """创建MQTT实例的性能测试任务

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


    def CreateJWKSAuthenticator(self, request):
        """创建一个jwks的认证

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
        """创建一个jwks的认证

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
        """创建主题

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


    def DeleteAuthenticator(self, request):
        """根据认证器类型删除一个MQTT认证器

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
        """删除策略规则

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


    def DeleteTopic(self, request):
        """删除MQTT主题

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


    def DescribeAuthenticator(self, request):
        """查询MQTT认证器

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
        """查询授权规则

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


    def DescribeInstance(self, request):
        """查询实例信息

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
        """获取实例列表，Filters参数使用说明如下：
        1. InstanceName, 名称模糊查询
        2. InstanceId，实例ID查询
        3. InstanceType, 实例类型查询，支持多选
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


    def DescribeTopic(self, request):
        """查询mqtt主题详情

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
        """获取主题列表，Filter参数使用说明如下：

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


    def ModifyAuthorizationPolicy(self, request):
        """修改策略规则

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


    def ModifyJWKSAuthenticator(self, request):
        """修改MQTT JWKS 认证器

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
        """修改MQTT JWKS 认证器

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
        """修改主题属性

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


    def RegisterDeviceCertificate(self, request):
        """注册设备证书

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


    def UpdateAuthorizationPolicyPriority(self, request):
        """修改策略规则优先级

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