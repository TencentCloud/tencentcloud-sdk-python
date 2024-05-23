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
from tencentcloud.cat.v20180409 import models


class CatClient(AbstractClient):
    _apiVersion = '2018-04-09'
    _endpoint = 'cat.tencentcloudapi.com'
    _service = 'cat'


    def CreateProbeTasks(self, request):
        """批量创建拨测任务

        :param request: Request instance for CreateProbeTasks.
        :type request: :class:`tencentcloud.cat.v20180409.models.CreateProbeTasksRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.CreateProbeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProbeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProbeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProbeTask(self, request):
        """删除拨测任务

        :param request: Request instance for DeleteProbeTask.
        :type request: :class:`tencentcloud.cat.v20180409.models.DeleteProbeTaskRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DeleteProbeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProbeTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProbeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDetailedSingleProbeData(self, request):
        """根据时间范围、任务ID、运营商等条件查询单次拨测详情数据

        :param request: Request instance for DescribeDetailedSingleProbeData.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeDetailedSingleProbeDataRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeDetailedSingleProbeDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDetailedSingleProbeData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDetailedSingleProbeDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstantTasks(self, request):
        """获取历史即时拨测任务

        :param request: Request instance for DescribeInstantTasks.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeInstantTasksRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeInstantTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstantTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstantTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodes(self, request):
        """获取拨测节点

        :param request: Request instance for DescribeNodes.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeNodesRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProbeMetricData(self, request):
        """查询云拨测指标数据，指标支持使用sum,avg,max,min聚合函数进行指标数据查询
        拨测频率与groupby聚合时间设置关联，如拨测频率为 30 分钟，则 grouby 聚合时间建议设置为大于30分钟，避免出现查询数据为空的情况

        :param request: Request instance for DescribeProbeMetricData.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeProbeMetricDataRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeProbeMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProbeMetricData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProbeMetricDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProbeNodes(self, request):
        """查询拨测节点

        :param request: Request instance for DescribeProbeNodes.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeProbeNodesRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeProbeNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProbeNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProbeNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProbeTasks(self, request):
        """查询拨测任务列表

        :param request: Request instance for DescribeProbeTasks.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeProbeTasksRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeProbeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProbeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProbeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeProbeTask(self, request):
        """恢复拨测任务

        :param request: Request instance for ResumeProbeTask.
        :type request: :class:`tencentcloud.cat.v20180409.models.ResumeProbeTaskRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.ResumeProbeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeProbeTask", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeProbeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SuspendProbeTask(self, request):
        """暂停拨测任务

        :param request: Request instance for SuspendProbeTask.
        :type request: :class:`tencentcloud.cat.v20180409.models.SuspendProbeTaskRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.SuspendProbeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SuspendProbeTask", params, headers=headers)
            response = json.loads(body)
            model = models.SuspendProbeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProbeTaskAttributes(self, request):
        """更新探测任务属性

        :param request: Request instance for UpdateProbeTaskAttributes.
        :type request: :class:`tencentcloud.cat.v20180409.models.UpdateProbeTaskAttributesRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.UpdateProbeTaskAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProbeTaskAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProbeTaskAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProbeTaskConfigurationList(self, request):
        """批量更新拨测任务配置

        :param request: Request instance for UpdateProbeTaskConfigurationList.
        :type request: :class:`tencentcloud.cat.v20180409.models.UpdateProbeTaskConfigurationListRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.UpdateProbeTaskConfigurationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProbeTaskConfigurationList", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProbeTaskConfigurationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))