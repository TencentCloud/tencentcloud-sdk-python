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
from tencentcloud.oceanus.v20190422 import models


class OceanusClient(AbstractClient):
    _apiVersion = '2019-04-22'
    _endpoint = 'oceanus.tencentcloudapi.com'
    _service = 'oceanus'


    def CheckSavepoint(self, request):
        """检查快照是否可用

        :param request: Request instance for CheckSavepoint.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CheckSavepointRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CheckSavepointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckSavepoint", params, headers=headers)
            response = json.loads(body)
            model = models.CheckSavepointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyJobs(self, request):
        """单条和批量复制作业

        :param request: Request instance for CopyJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CopyJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CopyJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyJobs", params, headers=headers)
            response = json.loads(body)
            model = models.CopyJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFolder(self, request):
        """作业列表页面新建文件夹请求

        :param request: Request instance for CreateFolder.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateFolderRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateJob(self, request):
        """新建作业接口，一个 AppId 最多允许创建1000个作业

        :param request: Request instance for CreateJob.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateJobRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateJobConfig(self, request):
        """创建作业配置，一个作业最多有100个配置版本

        :param request: Request instance for CreateJobConfig.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateJobConfigRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateJobConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJobConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJobConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResource(self, request):
        """创建资源接口

        :param request: Request instance for CreateResource.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateResourceRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceConfig(self, request):
        """创建资源配置接口

        :param request: Request instance for CreateResourceConfig.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateResourceConfigRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJobs(self, request):
        """批量删除作业接口，批量操作数量上限20

        :param request: Request instance for DeleteJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DeleteJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DeleteJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceConfigs(self, request):
        """删除资源版本

        :param request: Request instance for DeleteResourceConfigs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DeleteResourceConfigsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DeleteResourceConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResources(self, request):
        """删除资源接口

        :param request: Request instance for DeleteResources.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DeleteResourcesRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DeleteResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResources", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTableConfig(self, request):
        """删除作业表配置

        :param request: Request instance for DeleteTableConfig.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DeleteTableConfigRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DeleteTableConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTableConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """查询集群

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobConfigs(self, request):
        """查询作业配置列表，一次最多查询100个

        :param request: Request instance for DescribeJobConfigs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobConfigsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobSavepoint(self, request):
        """查找Savepoint列表

        :param request: Request instance for DescribeJobSavepoint.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobSavepointRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobSavepointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobSavepoint", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobSavepointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobSubmissionLog(self, request):
        """查询作业实例启动日志

        :param request: Request instance for DescribeJobSubmissionLog.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobSubmissionLogRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobSubmissionLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobSubmissionLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobSubmissionLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobs(self, request):
        """查询作业

        :param request: Request instance for DescribeJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceConfigs(self, request):
        """描述资源配置接口

        :param request: Request instance for DescribeResourceConfigs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourceConfigsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourceConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceRelatedJobs(self, request):
        """获取资源关联作业信息

        :param request: Request instance for DescribeResourceRelatedJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourceRelatedJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourceRelatedJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceRelatedJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceRelatedJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResources(self, request):
        """描述资源接口

        :param request: Request instance for DescribeResources.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourcesRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemResources(self, request):
        """描述系统资源接口

        :param request: Request instance for DescribeSystemResources.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeSystemResourcesRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeSystemResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTreeJobs(self, request):
        """生成树状作业显示结构

        :param request: Request instance for DescribeTreeJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeTreeJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeTreeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTreeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTreeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTreeResources(self, request):
        """查询树状结构资源列表

        :param request: Request instance for DescribeTreeResources.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeTreeResourcesRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeTreeResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTreeResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTreeResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkSpaces(self, request):
        """授权工作空间列表

        :param request: Request instance for DescribeWorkSpaces.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeWorkSpacesRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeWorkSpacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkSpaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkSpacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchSqlGatewayStatementResult(self, request):
        """查询Sql Gateway的Statement执行结果

        :param request: Request instance for FetchSqlGatewayStatementResult.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.FetchSqlGatewayStatementResultRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.FetchSqlGatewayStatementResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchSqlGatewayStatementResult", params, headers=headers)
            response = json.loads(body)
            model = models.FetchSqlGatewayStatementResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyJob(self, request):
        """更新作业属性，仅允许以下3种操作，不支持组合操作：
        (1)	更新作业名称
        (2)	更新作业备注
        (3)	更新作业最大并行度
        变更前提：WorkerCuNum<=MaxParallelism
        如果MaxParallelism变小，不重启作业，待下一次重启生效
        如果MaxParallelism变大，则要求入参RestartAllowed必须为True
        假设作业运行状态，则先停止作业，再启动作业，中间状态丢失
        假设作业暂停状态，则将作业更改为停止状态，中间状态丢失


        :param request: Request instance for ModifyJob.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.ModifyJobRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ModifyJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJob", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunJobs(self, request):
        """批量启动或者恢复作业，批量操作数量上限20

        :param request: Request instance for RunJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.RunJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.RunJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunJobs", params, headers=headers)
            response = json.loads(body)
            model = models.RunJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunSqlGatewayStatement(self, request):
        """通过Sql gateway执行satement

        :param request: Request instance for RunSqlGatewayStatement.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.RunSqlGatewayStatementRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.RunSqlGatewayStatementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunSqlGatewayStatement", params, headers=headers)
            response = json.loads(body)
            model = models.RunSqlGatewayStatementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopJobs(self, request):
        """批量停止作业，批量操作数量上限为20

        :param request: Request instance for StopJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.StopJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.StopJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopJobs", params, headers=headers)
            response = json.loads(body)
            model = models.StopJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerJobSavepoint(self, request):
        """触发Savepoint

        :param request: Request instance for TriggerJobSavepoint.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.TriggerJobSavepointRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.TriggerJobSavepointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerJobSavepoint", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerJobSavepointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))