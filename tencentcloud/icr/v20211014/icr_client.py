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
from tencentcloud.icr.v20211014 import models


class IcrClient(AbstractClient):
    _apiVersion = '2021-10-14'
    _endpoint = 'icr.tencentcloudapi.com'
    _service = 'icr'


    def GetIndustryV1HomeMembers(self, request):
        """获取成员列表接口

        :param request: Request instance for GetIndustryV1HomeMembers.
        :type request: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRequest`
        :rtype: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetIndustryV1HomeMembers", params, headers=headers)
            response = json.loads(body)
            model = models.GetIndustryV1HomeMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))