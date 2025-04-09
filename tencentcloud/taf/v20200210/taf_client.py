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
from tencentcloud.taf.v20200210 import models


class TafClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'taf.tencentcloudapi.com'
    _service = 'taf'


    def ManagePortraitRisk(self, request):
        """虚假流量识别

        :param request: Request instance for ManagePortraitRisk.
        :type request: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManagePortraitRisk", params, headers=headers)
            response = json.loads(body)
            model = models.ManagePortraitRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))