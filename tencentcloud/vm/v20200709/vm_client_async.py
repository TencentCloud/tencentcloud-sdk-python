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
from tencentcloud.vm.v20200709 import models
from typing import Dict


class VmClient(AbstractClient):
    _apiVersion = '2020-07-09'
    _endpoint = 'vm.tencentcloudapi.com'
    _service = 'vm'

    async def CancelTask(
            self,
            request: models.CancelTaskRequest,
            opts: Dict = None,
    ) -> models.CancelTaskResponse:
        """
        取消任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBizConfig(
            self,
            request: models.CreateBizConfigRequest,
            opts: Dict = None,
    ) -> models.CreateBizConfigResponse:
        """
        创建业务配置，1个账号最多可以创建20个配置，可定义音频审核的场景，如色情、谩骂等，

        在创建业务配置之前，你需要以下步骤：
        1. 开通COS存储捅功能，新建存储桶，例如 cms_segments，用来存储 视频转换过程中生成对音频和图片。
        2. 然后在COS控制台，授权天御内容安全主账号 对 cms_segments 存储桶对读写权限。具体授权操作，参考https://cloud.tencent.com/document/product/436/38648
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBizConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBizConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoModerationTask(
            self,
            request: models.CreateVideoModerationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVideoModerationTaskResponse:
        """
        通过URL或存储桶创建审核任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoModerationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoModerationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetail(
            self,
            request: models.DescribeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailResponse:
        """
        查看任务详情DescribeTaskDetail
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoStat(
            self,
            request: models.DescribeVideoStatRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoStatResponse:
        """
        控制台识别统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)