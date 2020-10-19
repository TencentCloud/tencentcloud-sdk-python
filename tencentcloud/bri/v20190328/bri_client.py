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
from tencentcloud.bri.v20190328 import models


class BriClient(AbstractClient):
    _apiVersion = '2019-03-28'
    _endpoint = 'bri.tencentcloudapi.com'


    def DescribeBRI(self, request):
        """输入业务名 (bri_num, bri_dev, bri_ip, bri_apk, bri_url, bri_social 六种之一)  及其 相应字段, 获取业务风险分数和标签。

        当业务名为bri_num时，必须填PhoneNumber字段.

        当业务名为bri_dev时, 必须填Imei字段.

        当业务名为bri_ip时，必须填IP字段.

        当业务名为bri_apk时，必须填 (PackageName,CertMd5,FileSize) 三个字段 或者 FileMd5一个字段.

        当业务名为bri_url时，必须填Url字段.

        当业务名为bri_social时，必须填QQ和Wechat字段两者其中一个或者两个.

        :param request: Request instance for DescribeBRI.
        :type request: :class:`tencentcloud.bri.v20190328.models.DescribeBRIRequest`
        :rtype: :class:`tencentcloud.bri.v20190328.models.DescribeBRIResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBRI", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBRIResponse()
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