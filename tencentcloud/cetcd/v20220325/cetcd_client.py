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
from tencentcloud.cetcd.v20220325 import models


class CetcdClient(AbstractClient):
    _apiVersion = '2022-03-25'
    _endpoint = 'cetcd.tencentcloudapi.com'
    _service = 'cetcd'


    def CreateEtcdInstance(self, request):
        r"""创建etcd实例

        :param request: Request instance for CreateEtcdInstance.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.CreateEtcdInstanceRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.CreateEtcdInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEtcdInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEtcdInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEtcdSnapshot(self, request):
        r"""创建etcd快照

        :param request: Request instance for CreateEtcdSnapshot.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.CreateEtcdSnapshotRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.CreateEtcdSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEtcdSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEtcdSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEtcdSnapshotPolicy(self, request):
        r"""创建etcd快照策略

        :param request: Request instance for CreateEtcdSnapshotPolicy.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.CreateEtcdSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.CreateEtcdSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEtcdSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEtcdSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdAvailableVersions(self, request):
        r"""查看etcd可用版本

        :param request: Request instance for DescribeEtcdAvailableVersions.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdAvailableVersionsRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdAvailableVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdAvailableVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdAvailableVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdCreatingProgress(self, request):
        r"""查看etcd集群创建进度

        :param request: Request instance for DescribeEtcdCreatingProgress.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdCreatingProgressRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdCreatingProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdCreatingProgress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdCreatingProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdCredentials(self, request):
        r"""查询etcd访问凭证

        :param request: Request instance for DescribeEtcdCredentials.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdCredentialsRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdInstances(self, request):
        r"""查询etcd实例列表

        :param request: Request instance for DescribeEtcdInstances.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdInstancesRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdQuota(self, request):
        r"""查看etcd集群配额

        :param request: Request instance for DescribeEtcdQuota.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdQuotaRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdRegions(self, request):
        r"""查看etcd支持地域

        :param request: Request instance for DescribeEtcdRegions.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdRegionsRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdSnapshotPolicies(self, request):
        r"""查看etcd快照策略

        :param request: Request instance for DescribeEtcdSnapshotPolicies.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdSnapshots(self, request):
        r"""查看etcd快照列表

        :param request: Request instance for DescribeEtcdSnapshots.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdSnapshotsRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEtcdTasks(self, request):
        r"""查看etcd相关tasks

        :param request: Request instance for DescribeEtcdTasks.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdTasksRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeEtcdTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtcdTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtcdTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRPCMethodList(self, request):
        r"""获取etcd集群的gRPC方法列表

        :param request: Request instance for DescribeRPCMethodList.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DescribeRPCMethodListRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DescribeRPCMethodListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRPCMethodList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRPCMethodListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableEtcdInstanceDeletionProtection(self, request):
        r"""关闭etcd实例删除保护

        :param request: Request instance for DisableEtcdInstanceDeletionProtection.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.DisableEtcdInstanceDeletionProtectionRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.DisableEtcdInstanceDeletionProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableEtcdInstanceDeletionProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DisableEtcdInstanceDeletionProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableEtcdInstanceDeletionProtection(self, request):
        r"""启用etcd实例删除保护

        :param request: Request instance for EnableEtcdInstanceDeletionProtection.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.EnableEtcdInstanceDeletionProtectionRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EnableEtcdInstanceDeletionProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableEtcdInstanceDeletionProtection", params, headers=headers)
            response = json.loads(body)
            model = models.EnableEtcdInstanceDeletionProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEtcdAttribute(self, request):
        r"""修改etcd实例属性

        :param request: Request instance for ModifyEtcdAttribute.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.ModifyEtcdAttributeRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.ModifyEtcdAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEtcdAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEtcdAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEtcdConfiguration(self, request):
        r"""修改etcd实例配置

        :param request: Request instance for ModifyEtcdConfiguration.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.ModifyEtcdConfigurationRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.ModifyEtcdConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEtcdConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEtcdConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEtcdSnapshotPolicy(self, request):
        r"""修改etcd快照策略

        :param request: Request instance for ModifyEtcdSnapshotPolicy.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.ModifyEtcdSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.ModifyEtcdSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEtcdSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEtcdSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeEtcdInstance(self, request):
        r"""扩容etcd实例

        :param request: Request instance for ResizeEtcdInstance.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.ResizeEtcdInstanceRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.ResizeEtcdInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeEtcdInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeEtcdInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeEtcdInstance(self, request):
        r"""升级etcd实例

        :param request: Request instance for UpgradeEtcdInstance.
        :type request: :class:`tencentcloud.cetcd.v20220325.models.UpgradeEtcdInstanceRequest`
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.UpgradeEtcdInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeEtcdInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeEtcdInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))