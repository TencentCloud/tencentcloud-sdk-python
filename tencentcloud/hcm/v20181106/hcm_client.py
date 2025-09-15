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
from tencentcloud.hcm.v20181106 import models


class HcmClient(AbstractClient):
    _apiVersion = '2018-11-06'
    _endpoint = 'hcm.tencentcloudapi.com'
    _service = 'hcm'


    def Evaluation(self, request):
        r"""速算题目批改接口，根据用户上传的图片或图片的URL识别图片中的数学算式，进而给出算式的正确性评估。

        :param request: Request instance for Evaluation.
        :type request: :class:`tencentcloud.hcm.v20181106.models.EvaluationRequest`
        :rtype: :class:`tencentcloud.hcm.v20181106.models.EvaluationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Evaluation", params, headers=headers)
            response = json.loads(body)
            model = models.EvaluationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))