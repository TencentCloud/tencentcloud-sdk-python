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
from tencentcloud.dbdc.v20201029 import models


class DbdcClient(AbstractClient):
    _apiVersion = '2020-10-29'
    _endpoint = 'dbdc.tencentcloudapi.com'
    _service = 'dbdc'


    def AddNodesToDBCustomCluster(self, request):
        r"""该接口（AddNodesToDBCustomCluster）用于为 DB Custom 集群上架节点。

        :param request: Request instance for AddNodesToDBCustomCluster.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.AddNodesToDBCustomClusterRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.AddNodesToDBCustomClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNodesToDBCustomCluster", params, headers=headers)
            response = json.loads(body)
            model = models.AddNodesToDBCustomClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckRoleAuthorized(self, request):
        r"""检查服务相关角色是否已创建

        :param request: Request instance for CheckRoleAuthorized.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.CheckRoleAuthorizedRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.CheckRoleAuthorizedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRoleAuthorized", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRoleAuthorizedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBCustomCluster(self, request):
        r"""该接口（CreateDBCustomCluster）用于创建 DB Custom 集群。

        :param request: Request instance for CreateDBCustomCluster.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.CreateDBCustomClusterRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.CreateDBCustomClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBCustomCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBCustomClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBCustomNodes(self, request):
        r"""该接口（CreateDBCustomNodes）用于创建 DB Custom 节点(需支付)。

        :param request: Request instance for CreateDBCustomNodes.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.CreateDBCustomNodesRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.CreateDBCustomNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBCustomNodes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBCustomNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCustomClusterDetail(self, request):
        r"""该接口(DescribeDBCustomClusterDetail) 用于查询 DB Custom 集群的详情信息。

        :param request: Request instance for DescribeDBCustomClusterDetail.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomClusterDetailRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCustomClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCustomClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCustomClusterKubeconfig(self, request):
        r"""该接口（DescribeDBCustomClusterKubeconfig）用于查询 DB Custom 集群 Kubeconfig。

        :param request: Request instance for DescribeDBCustomClusterKubeconfig.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomClusterKubeconfigRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomClusterKubeconfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCustomClusterKubeconfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCustomClusterKubeconfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCustomClusterNodes(self, request):
        r"""该接口（DescribeDBCustomClusterNodes）用于查询 DB Custom 集群中的节点列表。

        :param request: Request instance for DescribeDBCustomClusterNodes.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomClusterNodesRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCustomClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCustomClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCustomClusters(self, request):
        r"""该接口（DescribeDBCustomClusters）为DB Custom 集群列表查询接口。

        :param request: Request instance for DescribeDBCustomClusters.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomClustersRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCustomClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCustomClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCustomImages(self, request):
        r"""该接口（DescribeDBCustomImages）用于查询 DB Custom 可用的操作系统镜像列表。

        :param request: Request instance for DescribeDBCustomImages.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomImagesRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCustomImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCustomImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCustomNodes(self, request):
        r"""该接口（DescribeDBCustomNodes）用于查询 DB Custom 节点列表。

        :param request: Request instance for DescribeDBCustomNodes.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomNodesRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCustomNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCustomNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCustomTaskStatus(self, request):
        r"""该接口（DescribeDBCustomTaskStatus）用于查询 DB Custom 任务的状态。

        :param request: Request instance for DescribeDBCustomTaskStatus.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomTaskStatusRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBCustomTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCustomTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCustomTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        r"""本接口用于查询独享集群内的DB实例列表

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostList(self, request):
        r"""本接口用于查询主机列表

        :param request: Request instance for DescribeHostList.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeHostListRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDetail(self, request):
        r"""本接口用于查询独享集群详情

        :param request: Request instance for DescribeInstanceDetail.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstanceDetailRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceList(self, request):
        r"""本接口用于查询独享集群实例列表

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstanceListResponse`

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


    def DescribeInstances(self, request):
        r"""根据不同地域不同用户，获取集群列表信息

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstancesResponse`

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


    def DestroyDBCustomCluster(self, request):
        r"""该接口（DestroyDBCustomCluster）用于销毁 DB Custom 集群。

        :param request: Request instance for DestroyDBCustomCluster.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DestroyDBCustomClusterRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DestroyDBCustomClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyDBCustomCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyDBCustomClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyDBCustomNode(self, request):
        r"""该接口（DestroyDBCustomNode）用于销毁 DB Custom 节点。

        :param request: Request instance for DestroyDBCustomNode.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DestroyDBCustomNodeRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DestroyDBCustomNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyDBCustomNode", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyDBCustomNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDBCustomNode(self, request):
        r"""该接口 (IsolateDBCustomNode) 用于隔离 DB Custom 节点。

        :param request: Request instance for IsolateDBCustomNode.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.IsolateDBCustomNodeRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.IsolateDBCustomNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDBCustomNode", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDBCustomNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBCustomClusterTags(self, request):
        r"""该接口（ModifyDBCustomClusterTags）用于修改 DB Custom 集群的标签配置。

        :param request: Request instance for ModifyDBCustomClusterTags.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.ModifyDBCustomClusterTagsRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.ModifyDBCustomClusterTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBCustomClusterTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBCustomClusterTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBCustomNodeTags(self, request):
        r"""该接口（ModifyDBCustomNodeTags）用于修改 DB Custom 节点的标签配置。

        :param request: Request instance for ModifyDBCustomNodeTags.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.ModifyDBCustomNodeTagsRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.ModifyDBCustomNodeTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBCustomNodeTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBCustomNodeTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceName(self, request):
        r"""本接口用于修改集群名称

        :param request: Request instance for ModifyInstanceName.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.ModifyInstanceNameRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.ModifyInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveNodesFromDBCustomCluster(self, request):
        r"""该接口（RemoveNodesFromDBCustomCluster）用于从 DB Custom 集群移除节点。

        :param request: Request instance for RemoveNodesFromDBCustomCluster.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.RemoveNodesFromDBCustomClusterRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.RemoveNodesFromDBCustomClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveNodesFromDBCustomCluster", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveNodesFromDBCustomClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDBCustomNode(self, request):
        r"""该接口（RenewDBCustomNode）用于给 DB Custom 节点续费。

        :param request: Request instance for RenewDBCustomNode.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.RenewDBCustomNodeRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.RenewDBCustomNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDBCustomNode", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDBCustomNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))