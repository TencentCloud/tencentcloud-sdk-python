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
from tencentcloud.emr.v20190103 import models


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.tencentcloudapi.com'
    _service = 'emr'


    def AddMetricScaleStrategy(self, request):
        """添加扩缩容规则，按负载和时间

        :param request: Request instance for AddMetricScaleStrategy.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddMetricScaleStrategyRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddMetricScaleStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddMetricScaleStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.AddMetricScaleStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNodeResourceConfig(self, request):
        """增加当前集群的节点规格配置

        :param request: Request instance for AddNodeResourceConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddNodeResourceConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddNodeResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNodeResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.AddNodeResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddUsersForUserManager(self, request):
        """该接口支持安装了OpenLdap组件的集群。
        新增用户列表（用户管理）。

        :param request: Request instance for AddUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            model = models.AddUsersForUserManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachDisks(self, request):
        """云盘挂载

        :param request: Request instance for AttachDisks.
        :type request: :class:`tencentcloud.emr.v20190103.models.AttachDisksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AttachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.AttachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudInstance(self, request):
        """创建EMR容器集群实例

        :param request: Request instance for CreateCloudInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateCloudInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateCloudInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """创建EMR集群实例

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        """创建EMR集群实例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateInstanceResponse`

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


    def CreateSLInstance(self, request):
        """本接口（CreateSLInstance）用于创建Serverless HBase实例
        - 接口调用成功，会创建Serverless HBase实例，创建实例请求成功会返回创建实例的InstaceId和请求的 RequestID。
        - 接口为异步接口，接口返回时操作并未立即完成，实例操作结果可以通过调用DescribeInstancesList查看当前实例的StatusDesc状态。

        :param request: Request instance for CreateSLInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateSLInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateSLInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSLInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSLInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoScaleStrategy(self, request):
        """删除自动扩缩容规则，后台销毁根据该规则扩缩容出来的节点

        :param request: Request instance for DeleteAutoScaleStrategy.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeleteAutoScaleStrategyRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeleteAutoScaleStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoScaleStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoScaleStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNodeResourceConfig(self, request):
        """删除当前集群的节点规格配置

        :param request: Request instance for DeleteNodeResourceConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeleteNodeResourceConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeleteNodeResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNodeResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNodeResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserManagerUserList(self, request):
        """删除用户列表（用户管理）

        :param request: Request instance for DeleteUserManagerUserList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeleteUserManagerUserListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeleteUserManagerUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserManagerUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserManagerUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployYarnConf(self, request):
        """yarn资源调度-部署生效

        :param request: Request instance for DeployYarnConf.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeployYarnConfRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeployYarnConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployYarnConf", params, headers=headers)
            response = json.loads(body)
            model = models.DeployYarnConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScaleGroupGlobalConf(self, request):
        """获取自动扩缩容全局配置

        :param request: Request instance for DescribeAutoScaleGroupGlobalConf.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleGroupGlobalConfRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleGroupGlobalConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScaleGroupGlobalConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScaleGroupGlobalConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScaleRecords(self, request):
        """获取集群的自动扩缩容的详细记录

        :param request: Request instance for DescribeAutoScaleRecords.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleRecordsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScaleRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScaleRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScaleStrategies(self, request):
        """获取自动扩缩容规则

        :param request: Request instance for DescribeAutoScaleStrategies.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleStrategiesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleStrategiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScaleStrategies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScaleStrategiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterFlowStatusDetail(self, request):
        """查询EMR任务运行详情状态

        :param request: Request instance for DescribeClusterFlowStatusDetail.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeClusterFlowStatusDetailRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeClusterFlowStatusDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterFlowStatusDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterFlowStatusDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNodes(self, request):
        """查询集群节点信息

        :param request: Request instance for DescribeClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCvmQuota(self, request):
        """获取账户的CVM配额

        :param request: Request instance for DescribeCvmQuota.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeCvmQuotaRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeCvmQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCvmQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCvmQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDAGInfo(self, request):
        """查询DAG信息

        :param request: Request instance for DescribeDAGInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeDAGInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeDAGInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDAGInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDAGInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmrApplicationStatics(self, request):
        """yarn application 统计接口查询

        :param request: Request instance for DescribeEmrApplicationStatics.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmrApplicationStatics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmrApplicationStaticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmrOverviewMetrics(self, request):
        """查询监控概览页指标数据

        :param request: Request instance for DescribeEmrOverviewMetrics.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeEmrOverviewMetricsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeEmrOverviewMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmrOverviewMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmrOverviewMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalConfig(self, request):
        """查询YARN资源调度的全局配置

        :param request: Request instance for DescribeGlobalConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeGlobalConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeGlobalConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHBaseTableOverview(self, request):
        """获取Hbase表级监控数据概览接口

        :param request: Request instance for DescribeHBaseTableOverview.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeHBaseTableOverviewRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeHBaseTableOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHBaseTableOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHBaseTableOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHDFSStorageInfo(self, request):
        """查询HDFS存储文件信息

        :param request: Request instance for DescribeHDFSStorageInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeHDFSStorageInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeHDFSStorageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHDFSStorageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHDFSStorageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHiveQueries(self, request):
        """获取hive查询信息

        :param request: Request instance for DescribeHiveQueries.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeHiveQueriesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeHiveQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHiveQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHiveQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImpalaQueries(self, request):
        """DescribeImpalaQueries

        :param request: Request instance for DescribeImpalaQueries.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeImpalaQueriesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeImpalaQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImpalaQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImpalaQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInsightList(self, request):
        """获取洞察结果信息

        :param request: Request instance for DescribeInsightList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInsightListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInsightListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInsightList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInsightListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceRenewNodes(self, request):
        """查询待续费节点信息

        :param request: Request instance for DescribeInstanceRenewNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstanceRenewNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstanceRenewNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceRenewNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceRenewNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """查询集群实例信息

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesResponse`

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


    def DescribeInstancesList(self, request):
        """查询集群列表

        :param request: Request instance for DescribeInstancesList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobFlow(self, request):
        """查询流程任务

        :param request: Request instance for DescribeJobFlow.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeJobFlowRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeJobFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKyuubiQueryInfo(self, request):
        """查询Kyuubi查询信息

        :param request: Request instance for DescribeKyuubiQueryInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeKyuubiQueryInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeKyuubiQueryInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKyuubiQueryInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKyuubiQueryInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeDataDisks(self, request):
        """查询节点数据盘信息

        :param request: Request instance for DescribeNodeDataDisks.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeNodeDataDisksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeNodeDataDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeDataDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeDataDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeResourceConfigFast(self, request):
        """快速获取当前集群的节点规格配置

        :param request: Request instance for DescribeNodeResourceConfigFast.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeNodeResourceConfigFastRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeNodeResourceConfigFastResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeResourceConfigFast", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeResourceConfigFastResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceSchedule(self, request):
        """查询YARN资源调度数据信息。已废弃，请使用`DescribeYarnQueue`去查询队列信息。

        :param request: Request instance for DescribeResourceSchedule.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceScheduleDiffDetail(self, request):
        """YARN资源调度-变更详情

        :param request: Request instance for DescribeResourceScheduleDiffDetail.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleDiffDetailRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleDiffDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceScheduleDiffDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceScheduleDiffDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSLInstance(self, request):
        """本接口（DescribeSLInstance）用于查询 Serverless HBase实例基本信息

        :param request: Request instance for DescribeSLInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeSLInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeSLInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSLInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSLInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSLInstanceList(self, request):
        """本接口（DescribeSLInstanceList）用于查询Serverless HBase实例列表详细信息

        :param request: Request instance for DescribeSLInstanceList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeSLInstanceListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeSLInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSLInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSLInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceNodeInfos(self, request):
        """查询服务进程信息

        :param request: Request instance for DescribeServiceNodeInfos.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeServiceNodeInfosRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeServiceNodeInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceNodeInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceNodeInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkQueries(self, request):
        """查询Spark查询信息列表

        :param request: Request instance for DescribeSparkQueries.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeSparkQueriesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeSparkQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStarRocksQueryInfo(self, request):
        """查询StarRocks查询信息

        :param request: Request instance for DescribeStarRocksQueryInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeStarRocksQueryInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeStarRocksQueryInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStarRocksQueryInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStarRocksQueryInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrinoQueryInfo(self, request):
        """查询Trino(PrestoSQL)查询信息

        :param request: Request instance for DescribeTrinoQueryInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeTrinoQueryInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeTrinoQueryInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrinoQueryInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrinoQueryInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsersForUserManager(self, request):
        """该接口支持安装了OpenLdap组件的集群。
        批量导出用户。对于kerberos集群，如果需要kertab文件下载地址，可以将NeedKeytabInfo设置为true；注意SupportDownLoadKeyTab为true，但是DownLoadKeyTabUrl为空字符串，表示keytab文件在后台没有准备好（正在生成）。

        :param request: Request instance for DescribeUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersForUserManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeYarnApplications(self, request):
        """DescribeYarnApplications

        :param request: Request instance for DescribeYarnApplications.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeYarnApplicationsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeYarnApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeYarnApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeYarnApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeYarnQueue(self, request):
        """获取资源调度中的队列信息

        :param request: Request instance for DescribeYarnQueue.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeYarnQueueRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeYarnQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeYarnQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeYarnQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeYarnScheduleHistory(self, request):
        """查看yarn资源调度的调度历史。废弃，请使用流程中心查看历史记录。

        :param request: Request instance for DescribeYarnScheduleHistory.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeYarnScheduleHistoryRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeYarnScheduleHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeYarnScheduleHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeYarnScheduleHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewEmr(self, request):
        """集群续费询价。

        :param request: Request instance for InquirePriceRenewEmr.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquirePriceRenewEmrRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquirePriceRenewEmrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewEmr", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewEmrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateInstance(self, request):
        """创建实例询价

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewInstance(self, request):
        """续费询价。

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceScaleOutInstance(self, request):
        """扩容询价. 当扩容时候，请通过该接口查询价格。

        :param request: Request instance for InquiryPriceScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceUpdateInstance(self, request):
        """变配询价

        :param request: Request instance for InquiryPriceUpdateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpdateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceUpdateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoRenewFlag(self, request):
        """前提：预付费集群
        资源级别开启或关闭自动续费

        :param request: Request instance for ModifyAutoRenewFlag.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoScaleStrategy(self, request):
        """修改自动扩缩容规则

        :param request: Request instance for ModifyAutoScaleStrategy.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyAutoScaleStrategyRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyAutoScaleStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoScaleStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoScaleStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalConfig(self, request):
        """修改YARN资源调度的全局配置

        :param request: Request instance for ModifyGlobalConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyGlobalConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyGlobalConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInspectionSettings(self, request):
        """设置巡检任务配置

        :param request: Request instance for ModifyInspectionSettings.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyInspectionSettingsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyInspectionSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInspectionSettings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInspectionSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceBasic(self, request):
        """修改集群名称

        :param request: Request instance for ModifyInstanceBasic.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyInstanceBasicRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyInstanceBasicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceBasic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceBasicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPodNum(self, request):
        """调整Pod数量

        :param request: Request instance for ModifyPodNum.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyPodNumRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyPodNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPodNum", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPodNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResource(self, request):
        """变配实例

        :param request: Request instance for ModifyResource.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcePools(self, request):
        """刷新YARN的动态资源池。已废弃，请使用`DeployYarnConf`

        :param request: Request instance for ModifyResourcePools.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourcePoolsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourcePoolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePools", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcePoolsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceScheduleConfig(self, request):
        """修改YARN资源调度的资源配置。已废弃，请使用`ModifyYarnQueueV2`来修改队列配置

        :param request: Request instance for ModifyResourceScheduleConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceScheduleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceScheduler(self, request):
        """修改了yarn的资源调度器，点击部署生效。

        :param request: Request instance for ModifyResourceScheduler.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduler", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceSchedulerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcesTags(self, request):
        """强制修改标签

        :param request: Request instance for ModifyResourcesTags.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourcesTagsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourcesTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcesTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcesTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySLInstance(self, request):
        """本接口（ModifySLInstance）用于Serverless HBase变配实例。
        - 接口调用成功，会创建Serverless HBase实例，创建实例请求成功会返回请求的 RequestID。
        - 接口为异步接口，接口返回时操作并未立即完成，实例操作结果可以通过调用DescribeInstancesList查看当前实例的StatusDesc状态。

        :param request: Request instance for ModifySLInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifySLInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifySLInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySLInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySLInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySLInstanceBasic(self, request):
        """serverless hbase修改实例名称

        :param request: Request instance for ModifySLInstanceBasic.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifySLInstanceBasicRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifySLInstanceBasicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySLInstanceBasic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySLInstanceBasicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserManagerPwd(self, request):
        """修改用户密码（用户管理）

        :param request: Request instance for ModifyUserManagerPwd.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyUserManagerPwdRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyUserManagerPwdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserManagerPwd", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserManagerPwdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyYarnDeploy(self, request):
        """部署生效。已废弃，请使用`DeployYarnConf`接口进行部署生效

        :param request: Request instance for ModifyYarnDeploy.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyYarnDeployRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyYarnDeployResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyYarnDeploy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyYarnDeployResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyYarnQueueV2(self, request):
        """修改资源调度中队列信息

        :param request: Request instance for ModifyYarnQueueV2.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyYarnQueueV2Request`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyYarnQueueV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyYarnQueueV2", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyYarnQueueV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetYarnConfig(self, request):
        """修改YARN资源调度的资源配置

        :param request: Request instance for ResetYarnConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ResetYarnConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ResetYarnConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetYarnConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ResetYarnConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeDataDisks(self, request):
        """云数据盘扩容

        :param request: Request instance for ResizeDataDisks.
        :type request: :class:`tencentcloud.emr.v20190103.models.ResizeDataDisksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ResizeDataDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeDataDisks", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeDataDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunJobFlow(self, request):
        """创建流程作业

        :param request: Request instance for RunJobFlow.
        :type request: :class:`tencentcloud.emr.v20190103.models.RunJobFlowRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.RunJobFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunJobFlow", params, headers=headers)
            response = json.loads(body)
            model = models.RunJobFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutCluster(self, request):
        """扩容集群节点

        :param request: Request instance for ScaleOutCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        """扩容节点

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetNodeResourceConfigDefault(self, request):
        """设置当前集群的某个节点规格配置为默认或取消默认

        :param request: Request instance for SetNodeResourceConfigDefault.
        :type request: :class:`tencentcloud.emr.v20190103.models.SetNodeResourceConfigDefaultRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.SetNodeResourceConfigDefaultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNodeResourceConfigDefault", params, headers=headers)
            response = json.loads(body)
            model = models.SetNodeResourceConfigDefaultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStopServiceOrMonitor(self, request):
        """用于启停服务 重启服务等功能

        :param request: Request instance for StartStopServiceOrMonitor.
        :type request: :class:`tencentcloud.emr.v20190103.models.StartStopServiceOrMonitorRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.StartStopServiceOrMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStopServiceOrMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.StartStopServiceOrMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncPodState(self, request):
        """EMR同步TKE中POD状态

        :param request: Request instance for SyncPodState.
        :type request: :class:`tencentcloud.emr.v20190103.models.SyncPodStateRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.SyncPodStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncPodState", params, headers=headers)
            response = json.loads(body)
            model = models.SyncPodStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateClusterNodes(self, request):
        """销毁集群节点

        :param request: Request instance for TerminateClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstance(self, request):
        """销毁EMR实例。此接口仅支持弹性MapReduce正式计费版本。

        :param request: Request instance for TerminateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateSLInstance(self, request):
        """本接口（TerminateSLInstance）用于销毁Serverless HBase实例

        :param request: Request instance for TerminateSLInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateSLInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateSLInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateSLInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateSLInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateTasks(self, request):
        """缩容Task节点

        :param request: Request instance for TerminateTasks.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateTasksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))