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
from tencentcloud.tchd.v20230306 import models


class TchdClient(AbstractClient):
    _apiVersion = '2023-03-06'
    _endpoint = 'tchd.tencentcloudapi.com'
    _service = 'tchd'


    def DescribeEventStatistics(self, request):
        r"""本接口用于查询腾讯云健康看板的实时可用性事件信息，可以通过产品列表、地域进行过滤查询。
        可以参考健康看板历史事件页面来获取查询案例（链接：https://status.cloud.tencent.com/history）。

        :param request: Request instance for DescribeEventStatistics.
        :type request: :class:`tencentcloud.tchd.v20230306.models.DescribeEventStatisticsRequest`
        :rtype: :class:`tencentcloud.tchd.v20230306.models.DescribeEventStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEvents(self, request):
        r"""本接口用于查询腾讯云健康看板的可用性事件信息，可以通过产品列表、地域列表和事件发生日期进行过滤查询。
        当查询的产品对应时间内无事件时将返回空结果。
        可以参考健康看板历史事件页面来获取查询案例（链接：https://status.cloud.tencent.com/history）。

        :param request: Request instance for DescribeEvents.
        :type request: :class:`tencentcloud.tchd.v20230306.models.DescribeEventsRequest`
        :rtype: :class:`tencentcloud.tchd.v20230306.models.DescribeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))