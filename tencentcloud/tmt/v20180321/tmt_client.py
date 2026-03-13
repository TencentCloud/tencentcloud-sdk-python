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
from tencentcloud.tmt.v20180321 import models


class TmtClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'tmt.tencentcloudapi.com'
    _service = 'tmt'


    def ImageTranslateLLM(self, request):
        r"""提供18种语言的图片翻译服务，可自动识别图片中的文本内容并翻译成目标语言，识别后的文本按行翻译，后续会提供可按段落翻译的版本。

        - 输入图片格式：png、jpg、jpeg等常用图片格式，不支持gif动图。
        - 输出图片格式：jpg。

        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。

        :param request: Request instance for ImageTranslateLLM.
        :type request: :class:`tencentcloud.tmt.v20180321.models.ImageTranslateLLMRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.ImageTranslateLLMResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageTranslateLLM", params, headers=headers)
            response = json.loads(body)
            model = models.ImageTranslateLLMResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextTranslate(self, request):
        r"""腾讯翻译为合作伙伴提供文本翻译、文档翻译、交互翻译、AI同传等多种机器翻译服务，具有toB多行业解决方案。作为WMT世界机器翻译大赛冠军，翻译准确度值得信赖，其中，交互翻译能力是业界领先技术；腾讯同传是AI同传业界标杆。<br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。

        :param request: Request instance for TextTranslate.
        :type request: :class:`tencentcloud.tmt.v20180321.models.TextTranslateRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.TextTranslateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextTranslate", params, headers=headers)
            response = json.loads(body)
            model = models.TextTranslateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))