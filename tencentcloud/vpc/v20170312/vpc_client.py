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
from tencentcloud.vpc.v20170312 import models


class VpcClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'vpc.tencentcloudapi.com'
    _service = 'vpc'


    def DescribeNatsEipsInternal(self, request):
        """内部用户查询所有NAT网关的EIP IP列表信息

        :param request: Request instance for DescribeNatsEipsInternal.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatsEipsInternalRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatsEipsInternalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatsEipsInternal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatsEipsInternalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))