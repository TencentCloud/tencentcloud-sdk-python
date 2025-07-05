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
from tencentcloud.smpn.v20190822 import models


class SmpnClient(AbstractClient):
    _apiVersion = '2019-08-22'
    _endpoint = 'smpn.tencentcloudapi.com'
    _service = 'smpn'


    def DescribeSmpnChp(self, request):
        """不在使用的API

        查询号码的标记和标记次数

        :param request: Request instance for DescribeSmpnChp.
        :type request: :class:`tencentcloud.smpn.v20190822.models.DescribeSmpnChpRequest`
        :rtype: :class:`tencentcloud.smpn.v20190822.models.DescribeSmpnChpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmpnChp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmpnChpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmpnFnr(self, request):
        """不在使用的API

        虚假号码识别

        :param request: Request instance for DescribeSmpnFnr.
        :type request: :class:`tencentcloud.smpn.v20190822.models.DescribeSmpnFnrRequest`
        :rtype: :class:`tencentcloud.smpn.v20190822.models.DescribeSmpnFnrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmpnFnr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmpnFnrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))