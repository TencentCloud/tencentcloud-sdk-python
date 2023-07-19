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
from tencentcloud.smop.v20201203 import models


class SmopClient(AbstractClient):
    _apiVersion = '2020-12-03'
    _endpoint = 'smop.tencentcloudapi.com'
    _service = 'smop'


    def SubmitTaskEvent(self, request):
        """提交任务事件接口

        :param request: Request instance for SubmitTaskEvent.
        :type request: :class:`tencentcloud.smop.v20201203.models.SubmitTaskEventRequest`
        :rtype: :class:`tencentcloud.smop.v20201203.models.SubmitTaskEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTaskEvent", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTaskEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))