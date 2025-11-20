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
from tencentcloud.habo.v20181203 import models
from typing import Dict


class HaboClient(AbstractClient):
    _apiVersion = '2018-12-03'
    _endpoint = 'habo.tencentcloudapi.com'
    _service = 'habo'

    async def DescribeStatus(
            self,
            request: models.DescribeStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeStatusResponse:
        """
        查询指定md5样本是否分析完成，并获取分析日志下载地址。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAnalyse(
            self,
            request: models.StartAnalyseRequest,
            opts: Dict = None,
    ) -> models.StartAnalyseResponse:
        """
        上传样本到哈勃进行分析，异步生成分析日志。
        """
        
        kwargs = {}
        kwargs["action"] = "StartAnalyse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAnalyseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)