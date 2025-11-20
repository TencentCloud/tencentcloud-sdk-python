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
from tencentcloud.cmq.v20190304 import models
from typing import Dict


class CmqClient(AbstractClient):
    _apiVersion = '2019-03-04'
    _endpoint = 'cmq.tencentcloudapi.com'
    _service = 'cmq'

    async def DescribeQueueDetail(
            self,
            request: models.DescribeQueueDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeQueueDetailResponse:
        """
        枚举队列列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQueueDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQueueDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicDetail(
            self,
            request: models.DescribeTopicDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicDetailResponse:
        """
        查询主题详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)