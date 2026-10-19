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
from tencentcloud.wsa.v20250508 import models


class WsaClient(AbstractClient):
    _apiVersion = '2025-05-08'
    _endpoint = 'wsa.tencentcloudapi.com'
    _service = 'wsa'


    def SearchPro(self, request):
        r"""元宝搜索（Tencent Yuanbao Search，wsa）以互联网全网公开资源为基础，叠加腾讯优质内容生态，结合元宝 App 联网搜索应用实践，从数据收录到智能检索召回，全链路构建 AI 友好搜索引擎。合作伙伴通过检索词发起请求，接口以 JSON 形式返回搜索结果对应的排序信息、数据字段，合作伙伴可在业务场景中结合搜索结果的内容，扩充信息内容源，丰富展现效果，提升用户的查询满意度。

        :param request: Request instance for SearchPro.
        :type request: :class:`tencentcloud.wsa.v20250508.models.SearchProRequest`
        :rtype: :class:`tencentcloud.wsa.v20250508.models.SearchProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchPro", params, headers=headers)
            response = json.loads(body)
            model = models.SearchProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))