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
from tencentcloud.ams.v20200608 import models
from typing import Dict


class AmsClient(AbstractClient):
    _apiVersion = '2020-06-08'
    _endpoint = 'ams.tencentcloudapi.com'
    _service = 'ams'

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
        
    async def CreateAudioModerationTask(
            self,
            request: models.CreateAudioModerationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAudioModerationTaskResponse:
        """
        本接口（Audio Moderation）用于提交音频内容（包括音频文件或流地址）进行智能审核任务，使用前请您登陆控制台开通音频内容安全服务。

        ### 功能使用说明：
        - 前往“内容安全控制台-音频内容安全”开启使用音频内容安全服务，首次开通可获得20小时免费调用时长

        ### 接口功能说明：
        - 支持对音频流或音频文件进行检测，判断其中是否包含违规内容；
        - 支持设置回调地址 Callback 获取检测结果，或通过接口(查询音频检测结果)主动轮询获取检测结果；
        - 支持识别违规内容，包括：低俗、谩骂、色情、涉政、广告等场景；
        - 支持批量提交检测任务。检测任务列表最多支持10个；

        ### 音频文件调用说明：
        - 音频文件大小支持：文件 < 500M；
        - 音频文件时长支持：< 1小时；
        - 音频码率类型支持：128 Kbps - 256 Kbps ；
        - 音频文件支持格式：wav、mp3、aac、flac、amr、3gp、 m4a、wma、ogg、ape；
        - 支持音视频文件分离并对音频文件进行独立识别；

        ### 音频流调用说明：
        - 音频流时长支持：< 3小时；
        - 音频码率类型支持：128 Kbps - 256 Kbps ；
        - 音频流支持的传输协议：RTMP、HTTP、HTTPS；
        - 音频流格式支持的类型：rtp、srtp、rtmp、rtmps、mmsh、 mmst、hls、http、tcp、https、m3u8；
        - 支持音视频流分离并对音频流进行独立识别；
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAudioModerationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAudioModerationTaskResponse
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
        1. 开通COS存储桶功能，新建存储桶，例如 cms_segments，用来存储 视频转换过程中生成对音频和图片。
        2. 然后在COS控制台，授权天御内容安全主账号 对 cms_segments 存储桶对读写权限。具体授权操作，参考https://cloud.tencent.com/document/product/436/38648
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBizConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBizConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAmsList(
            self,
            request: models.DescribeAmsListRequest,
            opts: Dict = None,
    ) -> models.DescribeAmsListResponse:
        """
        音频审核明细列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAmsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAmsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAudioStat(
            self,
            request: models.DescribeAudioStatRequest,
            opts: Dict = None,
    ) -> models.DescribeAudioStatResponse:
        """
        控制台识别统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAudioStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAudioStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBizConfig(
            self,
            request: models.DescribeBizConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeBizConfigResponse:
        """
        查看单个配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBizConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBizConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetail(
            self,
            request: models.DescribeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailResponse:
        """
        查看任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)