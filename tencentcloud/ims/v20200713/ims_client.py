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
from tencentcloud.ims.v20200713 import models


class ImsClient(AbstractClient):
    _apiVersion = '2020-07-13'
    _endpoint = 'ims.tencentcloudapi.com'
    _service = 'ims'


    def ImageModeration(self, request):
        """图片同步检测服务（Image Moderation, IM）能自动扫描图片，识别可能令人反感、不安全或不适宜的内容，同时支持用户配置图片黑名单，打击自定义识别类型的图片。

        <div class="rno-api-explorer" style="margin-bottom:20px">
            <div class="rno-api-explorer-inner">
                <div class="rno-api-explorer-hd">
                    <div class="rno-api-explorer-title">
                        关于版本迭代的描述
                    </div>
                </div>
                <div class="rno-api-explorer-body">
                    <div class="rno-api-explorer-cont">
                        <p>当前页面版本为图片内容安全2020版本，2020.11.3日前接入的图片内容安全接口为2019版本，在此时间前接入的用户可直接访问以下链接进行维护操作：<a href="https://cloud.tencent.com/document/product/1125/38206" target="_blank">图片内容安全-2019版本</a></p>
                        <p>2020版本相对2019版本进行了升级，支持更灵活的多场景业务策略配置以及更丰富的识别回调信息，满足不同业务的识别需求，建议按照2020版本接入指引进行接口升级；同时，2019版本也会持续维护直至用户不再使用为止。</p>
                    </div>
                </div>
            </div>
        </div>

        :param request: Request instance for ImageModeration.
        :type request: :class:`tencentcloud.ims.v20200713.models.ImageModerationRequest`
        :rtype: :class:`tencentcloud.ims.v20200713.models.ImageModerationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageModeration", params, headers=headers)
            response = json.loads(body)
            model = models.ImageModerationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))