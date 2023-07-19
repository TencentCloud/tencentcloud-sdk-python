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
from tencentcloud.mvj.v20190926 import models


class MvjClient(AbstractClient):
    _apiVersion = '2019-09-26'
    _endpoint = 'mvj.tencentcloudapi.com'
    _service = 'mvj'


    def MarketingValueJudgement(self, request):
        """欢迎使用营销价值判断（Marketing Value Judgement，简称 MVJ）。

        营销价值判断（MVJ）是针对零售场景的风控服务，通过识别高价值顾客，以帮助零售商保障营销资金

        :param request: Request instance for MarketingValueJudgement.
        :type request: :class:`tencentcloud.mvj.v20190926.models.MarketingValueJudgementRequest`
        :rtype: :class:`tencentcloud.mvj.v20190926.models.MarketingValueJudgementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MarketingValueJudgement", params, headers=headers)
            response = json.loads(body)
            model = models.MarketingValueJudgementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))