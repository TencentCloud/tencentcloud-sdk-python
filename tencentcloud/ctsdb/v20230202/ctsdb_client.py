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
from tencentcloud.ctsdb.v20230202 import models


class CtsdbClient(AbstractClient):
    _apiVersion = '2023-02-02'
    _endpoint = 'ctsdb.tencentcloudapi.com'
    _service = 'ctsdb'


    def DescribeClusters(self, request):
        r"""查询实例列表及详情

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.ctsdb.v20230202.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.DescribeClustersResponse`

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


    def DescribeDatabases(self, request):
        r"""查看数据库/列表

        ```
          "Database":{
            "ClusterID":"ctsdbi-rebg0ghl",
            "Name":"" //不指定则查询实例下所有db
          }
        ```

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.ctsdb.v20230202.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))