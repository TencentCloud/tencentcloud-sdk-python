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
from tencentcloud.dtf.v20200506 import models


class DtfClient(AbstractClient):
    _apiVersion = '2020-05-06'
    _endpoint = 'dtf.tencentcloudapi.com'
    _service = 'dtf'


    def DescribeTransactions(self, request):
        """查询主事务列表

        :param request: Request instance for DescribeTransactions.
        :type request: :class:`tencentcloud.dtf.v20200506.models.DescribeTransactionsRequest`
        :rtype: :class:`tencentcloud.dtf.v20200506.models.DescribeTransactionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTransactions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTransactionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))