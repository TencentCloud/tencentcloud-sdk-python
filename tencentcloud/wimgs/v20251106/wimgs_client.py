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
from tencentcloud.wimgs.v20251106 import models


class WimgsClient(AbstractClient):
    _apiVersion = '2025-11-06'
    _endpoint = 'wimgs.tencentcloudapi.com'
    _service = 'wimgs'


    def SearchByText(self, request):
        r"""文搜图接口，本服务将针对您输入的搜索关键词，检索并以JSON形式返回相关图片的标题、宽高、缩略图、内容来源url等信息。

        :param request: Request instance for SearchByText.
        :type request: :class:`tencentcloud.wimgs.v20251106.models.SearchByTextRequest`
        :rtype: :class:`tencentcloud.wimgs.v20251106.models.SearchByTextResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchByText", params, headers=headers)
            response = json.loads(body)
            model = models.SearchByTextResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))