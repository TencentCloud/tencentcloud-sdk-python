# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.sms.v20210111 import models


class SmsClient(AbstractClient):
    _apiVersion = '2021-01-11'
    _endpoint = 'sms.tencentcloudapi.com'
    _service = 'sms'


    def DescribeSmsTemplateList(self, request):
        """⚠️注意：个人认证用户不支持使用 API 查询短信正文模版，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)。
        >- 注：由于云 **API3.0 安全性**有所提升，所以**接口鉴权**较为复杂，建议使用 [SDK](https://cloud.tencent.com/document/product/382/43193) 来使用云短信服务。
        >- 您可以在 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2019-07-11&Action=SendSms) 中直接运行该接口，可以先免去签名计算步骤。运行成功后，API Explorer可以**自动生成**SDK代码示例。

        :param request: Request instance for DescribeSmsTemplateList.
        :type request: :class:`tencentcloud.sms.v20210111.models.DescribeSmsTemplateListRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DescribeSmsTemplateListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSmsTemplateList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSmsTemplateListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)