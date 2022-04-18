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
from tencentcloud.asw.v20200722 import models


class AswClient(AbstractClient):
    _apiVersion = '2020-07-22'
    _endpoint = 'asw.tencentcloudapi.com'
    _service = 'asw'


    def CreateFlowService(self, request):
        """该接口用于生成状态机服务

        :param request: Request instance for CreateFlowService.
        :type request: :class:`tencentcloud.asw.v20200722.models.CreateFlowServiceRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.CreateFlowServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowService", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFlowServiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExecution(self, request):
        """查询执行详细信息

        :param request: Request instance for DescribeExecution.
        :type request: :class:`tencentcloud.asw.v20200722.models.DescribeExecutionRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.DescribeExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExecution", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExecutionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExecutionHistory(self, request):
        """一次执行会有很多步骤，经过很多节点，这个接口描述某一次执行的事件的历史

        :param request: Request instance for DescribeExecutionHistory.
        :type request: :class:`tencentcloud.asw.v20200722.models.DescribeExecutionHistoryRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.DescribeExecutionHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExecutionHistory", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExecutionHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExecutions(self, request):
        """对状态机的执行历史进行描述.

        :param request: Request instance for DescribeExecutions.
        :type request: :class:`tencentcloud.asw.v20200722.models.DescribeExecutionsRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.DescribeExecutionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExecutions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExecutionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowServiceDetail(self, request):
        """查询该用户指定状态机下的详情数据。

        :param request: Request instance for DescribeFlowServiceDetail.
        :type request: :class:`tencentcloud.asw.v20200722.models.DescribeFlowServiceDetailRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.DescribeFlowServiceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowServiceDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowServiceDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowServices(self, request):
        """查询指定用户下所有状态机，以列表形式返回

        :param request: Request instance for DescribeFlowServices.
        :type request: :class:`tencentcloud.asw.v20200722.models.DescribeFlowServicesRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.DescribeFlowServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowServices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowServicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyFlowService(self, request):
        """该接口用于修改状态机

        :param request: Request instance for ModifyFlowService.
        :type request: :class:`tencentcloud.asw.v20200722.models.ModifyFlowServiceRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.ModifyFlowServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFlowService", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyFlowServiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartExecution(self, request):
        """为指定的状态机启动一次执行

        :param request: Request instance for StartExecution.
        :type request: :class:`tencentcloud.asw.v20200722.models.StartExecutionRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.StartExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartExecution", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartExecutionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopExecution(self, request):
        """终止某个状态机

        :param request: Request instance for StopExecution.
        :type request: :class:`tencentcloud.asw.v20200722.models.StopExecutionRequest`
        :rtype: :class:`tencentcloud.asw.v20200722.models.StopExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopExecution", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopExecutionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)