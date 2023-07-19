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
from tencentcloud.casb.v20200507 import models


class CasbClient(AbstractClient):
    _apiVersion = '2020-05-07'
    _endpoint = 'casb.tencentcloudapi.com'
    _service = 'casb'


    def CopyCryptoColumnPolicy(self, request):
        """同region下 根据用户输入的CasbId,MetaDataId 复制策略到DstCasbId,MetaDataId中。
        场景1：
        相同CasbId，不同MetadataId 下策略复制
        场景2：
        不同Casbid,不同MetaDataId 下策略复制
        场景3:
        相同CasbId,相同MetaDataId 且 DatabaseName不同 策略复制

        :param request: Request instance for CopyCryptoColumnPolicy.
        :type request: :class:`tencentcloud.casb.v20200507.models.CopyCryptoColumnPolicyRequest`
        :rtype: :class:`tencentcloud.casb.v20200507.models.CopyCryptoColumnPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyCryptoColumnPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CopyCryptoColumnPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))