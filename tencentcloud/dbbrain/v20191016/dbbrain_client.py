# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.dbbrain.v20191016 import models


class DbbrainClient(AbstractClient):
    _apiVersion = '2019-10-16'
    _endpoint = 'dbbrain.tencentcloudapi.com'


    def DescribeDBDiagEvent(self, request):
        """获取实例异常诊断事件的详情信息。

        :param request: Request instance for DescribeDBDiagEvent.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagEventRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBDiagEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBDiagEventResponse()
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


    def DescribeDBDiagHistory(self, request):
        """获取实例诊断事件的列表。

        :param request: Request instance for DescribeDBDiagHistory.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagHistoryRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBDiagHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBDiagHistoryResponse()
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


    def DescribeSlowLogTimeSeriesStats(self, request):
        """获取慢日志统计柱状图

        :param request: Request instance for DescribeSlowLogTimeSeriesStats.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTimeSeriesStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTimeSeriesStatsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogTimeSeriesStats", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogTimeSeriesStatsResponse()
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


    def DescribeSlowLogTopSqls(self, request):
        """按照Sql模板+schema的聚合方式，统计排序指定时间段内的top慢sql。

        :param request: Request instance for DescribeSlowLogTopSqls.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTopSqlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTopSqlsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogTopSqls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogTopSqlsResponse()
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