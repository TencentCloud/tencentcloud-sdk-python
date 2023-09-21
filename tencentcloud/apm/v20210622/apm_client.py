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
from tencentcloud.apm.v20210622 import models


class ApmClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'apm.tencentcloudapi.com'
    _service = 'apm'


    def CreateApmInstance(self, request):
        """业务购买APM实例，调用该接口创建

        :param request: Request instance for CreateApmInstance.
        :type request: :class:`tencentcloud.apm.v20210622.models.CreateApmInstanceRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.CreateApmInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApmInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApmInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmAgent(self, request):
        """获取Apm Agent信息

        :param request: Request instance for DescribeApmAgent.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmAgentRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmInstances(self, request):
        """APM实例列表拉取

        :param request: Request instance for DescribeApmInstances.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmInstancesRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralMetricData(self, request):
        """获取指标数据通用接口。用户根据需要上送请求参数，返回对应的指标数据。
        接口调用频率限制为：20次/秒，1200次/分钟。单请求的数据点数限制为1440个。

        :param request: Request instance for DescribeGeneralMetricData.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralMetricDataRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralMetricData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralMetricDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralSpanList(self, request):
        """通用查询调用链列表

        :param request: Request instance for DescribeGeneralSpanList.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralSpanListRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralSpanListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralSpanList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralSpanListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMetricRecords(self, request):
        """拉取通用指标列表

        :param request: Request instance for DescribeMetricRecords.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeMetricRecordsRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeMetricRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMetricRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMetricRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceOverview(self, request):
        """服务概览数据拉取

        :param request: Request instance for DescribeServiceOverview.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeServiceOverviewRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeServiceOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApmInstance(self, request):
        """修改Apm实例接口

        :param request: Request instance for ModifyApmInstance.
        :type request: :class:`tencentcloud.apm.v20210622.models.ModifyApmInstanceRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.ModifyApmInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApmInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApmInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateApmInstance(self, request):
        """apm销毁实例

        :param request: Request instance for TerminateApmInstance.
        :type request: :class:`tencentcloud.apm.v20210622.models.TerminateApmInstanceRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.TerminateApmInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateApmInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateApmInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))