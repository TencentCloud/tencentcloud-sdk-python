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
from tencentcloud.tke.v20220501 import models


class TkeClient(AbstractClient):
    _apiVersion = '2022-05-01'
    _endpoint = 'tke.tencentcloudapi.com'
    _service = 'tke'


    def CreateHealthCheckPolicy(self, request):
        """创建健康检测策略

        :param request: Request instance for CreateHealthCheckPolicy.
        :type request: :class:`tencentcloud.tke.v20220501.models.CreateHealthCheckPolicyRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.CreateHealthCheckPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHealthCheckPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHealthCheckPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNodePool(self, request):
        """创建 TKE 节点池

        :param request: Request instance for CreateNodePool.
        :type request: :class:`tencentcloud.tke.v20220501.models.CreateNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.CreateNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHealthCheckPolicy(self, request):
        """删除健康检测策略

        :param request: Request instance for DeleteHealthCheckPolicy.
        :type request: :class:`tencentcloud.tke.v20220501.models.DeleteHealthCheckPolicyRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.DeleteHealthCheckPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHealthCheckPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHealthCheckPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNodePool(self, request):
        """删除 TKE 节点池

        :param request: Request instance for DeleteNodePool.
        :type request: :class:`tencentcloud.tke.v20220501.models.DeleteNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.DeleteNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInstances(self, request):
        """查询集群下节点实例信息

        :param request: Request instance for DescribeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20220501.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHealthCheckPolicies(self, request):
        """查询健康检测策略

        :param request: Request instance for DescribeHealthCheckPolicies.
        :type request: :class:`tencentcloud.tke.v20220501.models.DescribeHealthCheckPoliciesRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.DescribeHealthCheckPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHealthCheckPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHealthCheckPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHealthCheckPolicyBindings(self, request):
        """查询健康检测策略绑定关系

        :param request: Request instance for DescribeHealthCheckPolicyBindings.
        :type request: :class:`tencentcloud.tke.v20220501.models.DescribeHealthCheckPolicyBindingsRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.DescribeHealthCheckPolicyBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHealthCheckPolicyBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHealthCheckPolicyBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHealthCheckTemplate(self, request):
        """查询健康检测策略模板

        :param request: Request instance for DescribeHealthCheckTemplate.
        :type request: :class:`tencentcloud.tke.v20220501.models.DescribeHealthCheckTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.DescribeHealthCheckTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHealthCheckTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHealthCheckTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodePools(self, request):
        """查询 TKE 节点池列表

        :param request: Request instance for DescribeNodePools.
        :type request: :class:`tencentcloud.tke.v20220501.models.DescribeNodePoolsRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.DescribeNodePoolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodePools", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodePoolsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHealthCheckPolicy(self, request):
        """修改健康检测策略

        :param request: Request instance for ModifyHealthCheckPolicy.
        :type request: :class:`tencentcloud.tke.v20220501.models.ModifyHealthCheckPolicyRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.ModifyHealthCheckPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHealthCheckPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHealthCheckPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNodePool(self, request):
        """更新 TKE 节点池

        :param request: Request instance for ModifyNodePool.
        :type request: :class:`tencentcloud.tke.v20220501.models.ModifyNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20220501.models.ModifyNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))