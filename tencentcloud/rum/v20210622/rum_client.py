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
from tencentcloud.rum.v20210622 import models


class RumClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'rum.tencentcloudapi.com'
    _service = 'rum'


    def CreateProject(self, request):
        """创建项目（归属于某个团队）

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProjectResponse()
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


    def DescribeDataEventUrl(self, request):
        """获取DescribeDataEventUrl信息

        :param request: Request instance for DescribeDataEventUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDataEventUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataEventUrlResponse()
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


    def DescribeDataFetchUrl(self, request):
        """获取DescribeDataFetchUrl信息

        :param request: Request instance for DescribeDataFetchUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDataFetchUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataFetchUrlResponse()
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


    def DescribeDataFetchUrlInfo(self, request):
        """获取DescribeDataFetchUrlInfo信息

        :param request: Request instance for DescribeDataFetchUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDataFetchUrlInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataFetchUrlInfoResponse()
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


    def DescribeDataLogUrlStatistics(self, request):
        """获取LogUrlStatistics信息

        :param request: Request instance for DescribeDataLogUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDataLogUrlStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataLogUrlStatisticsResponse()
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


    def DescribeDataPerformancePage(self, request):
        """获取PerformancePage信息

        :param request: Request instance for DescribeDataPerformancePage.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDataPerformancePage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataPerformancePageResponse()
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


    def DescribeDataPvUrlStatistics(self, request):
        """获取DescribeDataPvUrlStatistics信息

        :param request: Request instance for DescribeDataPvUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDataPvUrlStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataPvUrlStatisticsResponse()
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


    def DescribeError(self, request):
        """获取首页错误信息

        :param request: Request instance for DescribeError.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeErrorRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeErrorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeError", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeErrorResponse()
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


    def DescribeLogList(self, request):
        """获取项目下的日志列表（实例创建的项目下的日志列表）

        :param request: Request instance for DescribeLogList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeLogListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeLogListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLogList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogListResponse()
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


    def DescribeProjects(self, request):
        """获取项目列表（实例创建的团队下的项目列表）

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
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


    def DescribeScores(self, request):
        """获取首页分数列表

        :param request: Request instance for DescribeScores.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeScoresRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeScoresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScores", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScoresResponse()
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