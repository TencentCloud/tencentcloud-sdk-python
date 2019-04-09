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
from tencentcloud.emr.v20190103 import models


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.tencentcloudapi.com'


    def InquiryPriceCreateInstance(self, request):
        """创建实例询价

        :param request: 调用InquiryPriceCreateInstance所需参数的结构体。
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateInstanceResponse()
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