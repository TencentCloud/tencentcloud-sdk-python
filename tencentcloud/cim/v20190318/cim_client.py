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
from tencentcloud.cim.v20190318 import models


class CimClient(AbstractClient):
    _apiVersion = '2019-03-18'
    _endpoint = 'cim.tencentcloudapi.com'
    _service = 'cim'


    def DescribeSdkAppid(self, request):
        """获取云通信IM中腾讯云账号对应的SDKAppID

        :param request: Request instance for DescribeSdkAppid.
        :type request: :class:`tencentcloud.cim.v20190318.models.DescribeSdkAppidRequest`
        :rtype: :class:`tencentcloud.cim.v20190318.models.DescribeSdkAppidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSdkAppid", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSdkAppidResponse()
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