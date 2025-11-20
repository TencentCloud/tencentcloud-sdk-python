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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.facefusion.v20181201 import models
from typing import Dict


class FacefusionClient(AbstractClient):
    _apiVersion = '2018-12-01'
    _endpoint = 'facefusion.tencentcloudapi.com'
    _service = 'facefusion'

    async def DescribeMaterialList(
            self,
            request: models.DescribeMaterialListRequest,
            opts: Dict = None,
    ) -> models.DescribeMaterialListResponse:
        """
        通常通过腾讯云人脸融合的控制台可以查看到素材相关的参数数据，可以满足使用。本接口返回活动的素材数据，包括素材状态等。用于用户通过Api查看素材相关数据，方便使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaterialList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaterialListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FaceFusion(
            self,
            request: models.FaceFusionRequest,
            opts: Dict = None,
    ) -> models.FaceFusionResponse:
        """
        本接口用于人脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。未发布的活动请求频率限制为1次/秒，已发布的活动请求频率限制50次/秒。如有需要提高活动的请求频率限制，请在控制台中申请。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "FaceFusion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FaceFusionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FuseFace(
            self,
            request: models.FuseFaceRequest,
            opts: Dict = None,
    ) -> models.FuseFaceResponse:
        """
        本接口用于单脸、多脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。查看 <a href="https://cloud.tencent.com/document/product/670/38247" target="_blank">选脸融合接入指引</a>。

        未发布的活动请求频率限制为1次/秒，已发布的活动请求频率限制50次/秒。如有需要提高活动的请求频率限制，请在控制台中申请。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "FuseFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FuseFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)