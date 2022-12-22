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
from tencentcloud.anicloud.v20220923 import models


class AnicloudClient(AbstractClient):
    _apiVersion = '2022-09-23'
    _endpoint = 'anicloud.tencentcloudapi.com'
    _service = 'anicloud'


    def CheckAppidExist(self, request):
        """查看appid是否存在

        :param request: Request instance for CheckAppidExist.
        :type request: :class:`tencentcloud.anicloud.v20220923.models.CheckAppidExistRequest`
        :rtype: :class:`tencentcloud.anicloud.v20220923.models.CheckAppidExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAppidExist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckAppidExistResponse()
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


    def QueryResource(self, request):
        """查询购买资源

        :param request: Request instance for QueryResource.
        :type request: :class:`tencentcloud.anicloud.v20220923.models.QueryResourceRequest`
        :rtype: :class:`tencentcloud.anicloud.v20220923.models.QueryResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryResource", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryResourceResponse()
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


    def QueryResourceInfo(self, request):
        """查询资源信息

        :param request: Request instance for QueryResourceInfo.
        :type request: :class:`tencentcloud.anicloud.v20220923.models.QueryResourceInfoRequest`
        :rtype: :class:`tencentcloud.anicloud.v20220923.models.QueryResourceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryResourceInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryResourceInfoResponse()
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