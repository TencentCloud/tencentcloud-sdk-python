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
from tencentcloud.es.v20180416 import models


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.tencentcloudapi.com'
    _service = 'es'


    def CheckMigrateIndexMetaData(self, request):
        """检查cos迁移索引元数据

        :param request: Request instance for CheckMigrateIndexMetaData.
        :type request: :class:`tencentcloud.es.v20180416.models.CheckMigrateIndexMetaDataRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CheckMigrateIndexMetaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckMigrateIndexMetaData", params, headers=headers)
            response = json.loads(body)
            model = models.CheckMigrateIndexMetaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterSnapshot(self, request):
        """集群快照手动创建

        :param request: Request instance for CreateClusterSnapshot.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateClusterSnapshotRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateClusterSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCosMigrateToServerlessInstance(self, request):
        """cos迁移流程

        :param request: Request instance for CreateCosMigrateToServerlessInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateCosMigrateToServerlessInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateCosMigrateToServerlessInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosMigrateToServerlessInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosMigrateToServerlessInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIndex(self, request):
        """创建索引

        :param request: Request instance for CreateIndex.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateIndexRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIndex", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        """创建指定规格的ES集群实例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateInstanceResponse`

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


    def CreateLogstashInstance(self, request):
        """用于创建Logstash实例

        :param request: Request instance for CreateLogstashInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateLogstashInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateLogstashInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogstashInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogstashInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServerlessInstance(self, request):
        """创建Serverless索引

        :param request: Request instance for CreateServerlessInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateServerlessInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateServerlessInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServerlessInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServerlessInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServerlessSpaceV2(self, request):
        """创建Serverless索引空间

        :param request: Request instance for CreateServerlessSpaceV2.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateServerlessSpaceV2Request`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateServerlessSpaceV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServerlessSpaceV2", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServerlessSpaceV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterSnapshot(self, request):
        """删除快照仓库里备份的快照

        :param request: Request instance for DeleteClusterSnapshot.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteClusterSnapshotRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteClusterSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIndex(self, request):
        """删除索引

        :param request: Request instance for DeleteIndex.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteIndexRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        """销毁集群实例

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteInstanceResponse`

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


    def DeleteLogstashInstance(self, request):
        """用于删除Logstash实例

        :param request: Request instance for DeleteLogstashInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteLogstashInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteLogstashInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogstashInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogstashInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLogstashPipelines(self, request):
        """用于批量删除Logstash管道

        :param request: Request instance for DeleteLogstashPipelines.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteLogstashPipelinesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteLogstashPipelinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogstashPipelines", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogstashPipelinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServerlessInstance(self, request):
        """删除Serverless索引

        :param request: Request instance for DeleteServerlessInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteServerlessInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteServerlessInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServerlessInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServerlessInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServerlessSpaceUser(self, request):
        """删除Serverless空间子用户

        :param request: Request instance for DeleteServerlessSpaceUser.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteServerlessSpaceUserRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteServerlessSpaceUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServerlessSpaceUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServerlessSpaceUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterSnapshot(self, request):
        """获取快照备份列表

        :param request: Request instance for DescribeClusterSnapshot.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeClusterSnapshotRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeClusterSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiagnose(self, request):
        """查询智能运维诊断结果报告

        :param request: Request instance for DescribeDiagnose.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeDiagnoseRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeDiagnoseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiagnose", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiagnoseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexList(self, request):
        """获取索引列表

        :param request: Request instance for DescribeIndexList.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeIndexListRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeIndexListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexMeta(self, request):
        """获取索引元数据

        :param request: Request instance for DescribeIndexMeta.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeIndexMetaRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeIndexMetaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexMeta", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexMetaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogs(self, request):
        """查询用户该地域下符合条件的ES集群的日志

        :param request: Request instance for DescribeInstanceLogs.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstanceLogsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstanceLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceOperations(self, request):
        """查询实例指定条件下的操作记录

        :param request: Request instance for DescribeInstanceOperations.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstanceOperationsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstanceOperationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceOperations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceOperationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancePluginList(self, request):
        """查询实例插件列表

        :param request: Request instance for DescribeInstancePluginList.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstancePluginListRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstancePluginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancePluginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancePluginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """查询用户该地域下符合条件的所有实例

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstancesResponse`

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


    def DescribeLogstashInstanceLogs(self, request):
        """查询用户该地域下符合条件的Logstash实例的日志

        :param request: Request instance for DescribeLogstashInstanceLogs.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeLogstashInstanceLogsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeLogstashInstanceLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogstashInstanceLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogstashInstanceLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogstashInstanceOperations(self, request):
        """查询实例指定条件下的操作记录

        :param request: Request instance for DescribeLogstashInstanceOperations.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeLogstashInstanceOperationsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeLogstashInstanceOperationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogstashInstanceOperations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogstashInstanceOperationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogstashInstances(self, request):
        """查询用户该地域下符合条件的所有Logstash实例

        :param request: Request instance for DescribeLogstashInstances.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeLogstashInstancesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeLogstashInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogstashInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogstashInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogstashPipelines(self, request):
        """用于获取Logstash实例管道列表

        :param request: Request instance for DescribeLogstashPipelines.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeLogstashPipelinesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeLogstashPipelinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogstashPipelines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogstashPipelinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServerlessInstances(self, request):
        """Serverless获取索引列表

        :param request: Request instance for DescribeServerlessInstances.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeServerlessInstancesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeServerlessInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerlessInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerlessInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServerlessMetrics(self, request):
        """获取serverless实例对应指标，获取space维度时不需要传入indexid，获取index时不需要传入spaceid
        获取一段时间时间范围内的指标数据

        :param request: Request instance for DescribeServerlessMetrics.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeServerlessMetricsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeServerlessMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerlessMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerlessMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServerlessSpaceUser(self, request):
        """查看Serverless空间子用户

        :param request: Request instance for DescribeServerlessSpaceUser.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeServerlessSpaceUserRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeServerlessSpaceUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerlessSpaceUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerlessSpaceUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServerlessSpaces(self, request):
        """获取Serverless索引空间列表

        :param request: Request instance for DescribeServerlessSpaces.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeServerlessSpacesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeServerlessSpacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerlessSpaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerlessSpacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceKibanaTools(self, request):
        """space维度的kibana获取登录token

        :param request: Request instance for DescribeSpaceKibanaTools.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeSpaceKibanaToolsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeSpaceKibanaToolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceKibanaTools", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceKibanaToolsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCosSnapshotList(self, request):
        """查询快照信息接口

        :param request: Request instance for DescribeUserCosSnapshotList.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeUserCosSnapshotListRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeUserCosSnapshotListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCosSnapshotList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCosSnapshotListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeViews(self, request):
        """查询集群各视图数据，包括集群维度、节点维度、Kibana维度

        :param request: Request instance for DescribeViews.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeViewsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeViewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeViews", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeViewsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DiagnoseInstance(self, request):
        """智能运维诊断集群

        :param request: Request instance for DiagnoseInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.DiagnoseInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DiagnoseInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DiagnoseInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DiagnoseInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDiagnoseSettings(self, request):
        """查看智能运维配置

        :param request: Request instance for GetDiagnoseSettings.
        :type request: :class:`tencentcloud.es.v20180416.models.GetDiagnoseSettingsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.GetDiagnoseSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDiagnoseSettings", params, headers=headers)
            response = json.loads(body)
            model = models.GetDiagnoseSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRequestTargetNodeTypes(self, request):
        """获取接收客户端请求的节点类型

        :param request: Request instance for GetRequestTargetNodeTypes.
        :type request: :class:`tencentcloud.es.v20180416.models.GetRequestTargetNodeTypesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.GetRequestTargetNodeTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRequestTargetNodeTypes", params, headers=headers)
            response = json.loads(body)
            model = models.GetRequestTargetNodeTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewInstance(self, request):
        """集群续费询价接口，续费前通过调用该接口，可获取集群续费的价格。

        :param request: Request instance for InquirePriceRenewInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.InquirePriceRenewInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.InquirePriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallInstanceModel(self, request):
        """ES集群安装模型接口

        :param request: Request instance for InstallInstanceModel.
        :type request: :class:`tencentcloud.es.v20180416.models.InstallInstanceModelRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.InstallInstanceModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallInstanceModel", params, headers=headers)
            response = json.loads(body)
            model = models.InstallInstanceModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEsVipSecurityGroup(self, request):
        """修改绑定VIP的安全组，传安全组id列表

        :param request: Request instance for ModifyEsVipSecurityGroup.
        :type request: :class:`tencentcloud.es.v20180416.models.ModifyEsVipSecurityGroupRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.ModifyEsVipSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEsVipSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEsVipSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartInstance(self, request):
        """重启ES集群实例(用于系统版本更新等操作)

        :param request: Request instance for RestartInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestartInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartKibana(self, request):
        """重启Kibana

        :param request: Request instance for RestartKibana.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartKibanaRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartKibanaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartKibana", params, headers=headers)
            response = json.loads(body)
            model = models.RestartKibanaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartLogstashInstance(self, request):
        """用于重启Logstash实例

        :param request: Request instance for RestartLogstashInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartLogstashInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartLogstashInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartLogstashInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestartLogstashInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartNodes(self, request):
        """用于重启集群节点

        :param request: Request instance for RestartNodes.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartNodesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartNodes", params, headers=headers)
            response = json.loads(body)
            model = models.RestartNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreClusterSnapshot(self, request):
        """快照备份恢复，从仓库中恢复快照到集群中

        :param request: Request instance for RestoreClusterSnapshot.
        :type request: :class:`tencentcloud.es.v20180416.models.RestoreClusterSnapshotRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestoreClusterSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreClusterSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreClusterSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SaveAndDeployLogstashPipeline(self, request):
        """用于下发并且部署管道

        :param request: Request instance for SaveAndDeployLogstashPipeline.
        :type request: :class:`tencentcloud.es.v20180416.models.SaveAndDeployLogstashPipelineRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.SaveAndDeployLogstashPipelineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SaveAndDeployLogstashPipeline", params, headers=headers)
            response = json.loads(body)
            model = models.SaveAndDeployLogstashPipelineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartLogstashPipelines(self, request):
        """用于启动Logstash管道

        :param request: Request instance for StartLogstashPipelines.
        :type request: :class:`tencentcloud.es.v20180416.models.StartLogstashPipelinesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.StartLogstashPipelinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartLogstashPipelines", params, headers=headers)
            response = json.loads(body)
            model = models.StartLogstashPipelinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopLogstashPipelines(self, request):
        """用于批量停止Logstash管道

        :param request: Request instance for StopLogstashPipelines.
        :type request: :class:`tencentcloud.es.v20180416.models.StopLogstashPipelinesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.StopLogstashPipelinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopLogstashPipelines", params, headers=headers)
            response = json.loads(body)
            model = models.StopLogstashPipelinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDiagnoseSettings(self, request):
        """更新智能运维配置

        :param request: Request instance for UpdateDiagnoseSettings.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateDiagnoseSettingsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateDiagnoseSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDiagnoseSettings", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDiagnoseSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDictionaries(self, request):
        """更新ES集群词典

        :param request: Request instance for UpdateDictionaries.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateDictionariesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateDictionariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDictionaries", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDictionariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateIndex(self, request):
        """更新索引

        :param request: Request instance for UpdateIndex.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateIndexRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateIndex", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateInstance(self, request):
        """对集群进行节点规格变更，修改实例名称，修改配置，重置密码， 添加Kibana黑白名单等操作。参数中InstanceId为必传参数，ForceRestart为选填参数，剩余参数传递组合及含义如下：
        - InstanceName：修改实例名称(仅用于标识实例)
        - NodeInfoList: 修改节点配置（节点横向扩缩容，纵向扩缩容，增加主节点，增加冷节点等）
        - EsConfig：修改集群配置
        - Password：修改默认用户elastic的密码
        - EsAcl：修改访问控制列表
        - CosBackUp: 设置集群COS自动备份信息
        以上参数组合只能传递一种，多传或少传均会导致请求失败

        :param request: Request instance for UpdateInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateJdk(self, request):
        """更新实例Jdk配置

        :param request: Request instance for UpdateJdk.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateJdkRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateJdkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateJdk", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateJdkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateLogstashInstance(self, request):
        """对集群进行节点规格变更，修改实例名称，修改配置，等操作。参数中InstanceId为必传参数，参数传递组合及含义如下：
        - InstanceName：修改实例名称(仅用于标识实例)
        - NodeNum: 修改实例节点数量（节点横向扩缩容，纵向扩缩容等）
        - YMLConfig: 修改实例YML配置
        - BindedES：修改绑定的ES集群配置
        以上参数组合只能传递一种，多传或少传均会导致请求失败

        :param request: Request instance for UpdateLogstashInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateLogstashInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateLogstashInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateLogstashInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateLogstashInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateLogstashPipelineDesc(self, request):
        """用于更新管道描述信息

        :param request: Request instance for UpdateLogstashPipelineDesc.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateLogstashPipelineDescRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateLogstashPipelineDescResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateLogstashPipelineDesc", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateLogstashPipelineDescResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePlugins(self, request):
        """变更插件列表

        :param request: Request instance for UpdatePlugins.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdatePluginsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdatePluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePlugins", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePluginsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRequestTargetNodeTypes(self, request):
        """更新接收客户端请求的节点类型

        :param request: Request instance for UpdateRequestTargetNodeTypes.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateRequestTargetNodeTypesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateRequestTargetNodeTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRequestTargetNodeTypes", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRequestTargetNodeTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateServerlessInstance(self, request):
        """更新Serverless索引

        :param request: Request instance for UpdateServerlessInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateServerlessInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateServerlessInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateServerlessInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateServerlessInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateServerlessSpace(self, request):
        """更新Serverless索引空间

        :param request: Request instance for UpdateServerlessSpace.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateServerlessSpaceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateServerlessSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateServerlessSpace", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateServerlessSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeInstance(self, request):
        """升级ES集群版本

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeLicense(self, request):
        """升级ES商业特性

        :param request: Request instance for UpgradeLicense.
        :type request: :class:`tencentcloud.es.v20180416.models.UpgradeLicenseRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpgradeLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeLicense", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))