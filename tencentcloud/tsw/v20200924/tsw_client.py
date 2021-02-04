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
from tencentcloud.tsw.v20200924 import models


class TswClient(AbstractClient):
    _apiVersion = '2020-09-24'
    _endpoint = 'tsw.tencentcloudapi.com'
    _service = 'tsw'


    def DescribeAgentShell(self, request):
        """获取服务接入信息

        :param request: Request instance for DescribeAgentShell.
        :type request: :class:`tencentcloud.tsw.v20200924.models.DescribeAgentShellRequest`
        :rtype: :class:`tencentcloud.tsw.v20200924.models.DescribeAgentShellResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentShell", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentShellResponse()
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