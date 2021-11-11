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
from tencentcloud.tcm.v20210413 import models


class TcmClient(AbstractClient):
    _apiVersion = '2021-04-13'
    _endpoint = 'tcm.tencentcloudapi.com'
    _service = 'tcm'


    def DescribeMesh(self, request):
        """查询网格详情

        :param request: Request instance for DescribeMesh.
        :type request: :class:`tencentcloud.tcm.v20210413.models.DescribeMeshRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.DescribeMeshResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMesh", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMeshResponse()
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


    def DescribeMeshList(self, request):
        """查询网格列表

        :param request: Request instance for DescribeMeshList.
        :type request: :class:`tencentcloud.tcm.v20210413.models.DescribeMeshListRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.DescribeMeshListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMeshList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMeshListResponse()
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