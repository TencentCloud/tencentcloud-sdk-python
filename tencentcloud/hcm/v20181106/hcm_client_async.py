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
from tencentcloud.hcm.v20181106 import models
from typing import Dict


class HcmClient(AbstractClient):
    _apiVersion = '2018-11-06'
    _endpoint = 'hcm.tencentcloudapi.com'
    _service = 'hcm'

    async def Evaluation(
            self,
            request: models.EvaluationRequest,
            opts: Dict = None,
    ) -> models.EvaluationResponse:
        """
        速算题目批改接口，根据用户上传的图片或图片的URL识别图片中的数学算式，进而给出算式的正确性评估。
        """
        
        kwargs = {}
        kwargs["action"] = "Evaluation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EvaluationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)