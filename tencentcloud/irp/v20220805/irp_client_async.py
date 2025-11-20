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
from tencentcloud.irp.v20220805 import models
from typing import Dict


class IrpClient(AbstractClient):
    _apiVersion = '2022-08-05'
    _endpoint = 'irp.tencentcloudapi.com'
    _service = 'irp'

    async def DescribeGoodsRecommend(
            self,
            request: models.DescribeGoodsRecommendRequest,
            opts: Dict = None,
    ) -> models.DescribeGoodsRecommendResponse:
        """
        获取电商类推荐结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGoodsRecommend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGoodsRecommendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FeedRecommend(
            self,
            request: models.FeedRecommendRequest,
            opts: Dict = None,
    ) -> models.FeedRecommendResponse:
        """
        获取信息流推荐结果
        """
        
        kwargs = {}
        kwargs["action"] = "FeedRecommend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FeedRecommendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportFeedBehavior(
            self,
            request: models.ReportFeedBehaviorRequest,
            opts: Dict = None,
    ) -> models.ReportFeedBehaviorResponse:
        """
        上报信息流场景内的行为数据，随着数据的积累，模型的效果会逐渐稳定。
        """
        
        kwargs = {}
        kwargs["action"] = "ReportFeedBehavior"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportFeedBehaviorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportFeedItem(
            self,
            request: models.ReportFeedItemRequest,
            opts: Dict = None,
    ) -> models.ReportFeedItemResponse:
        """
        上报被用于推荐的信息流内容信息
        """
        
        kwargs = {}
        kwargs["action"] = "ReportFeedItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportFeedItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportFeedUser(
            self,
            request: models.ReportFeedUserRequest,
            opts: Dict = None,
    ) -> models.ReportFeedUserResponse:
        """
        上报信息流用户信息，请务必确认用户的唯一性，并在请求推荐结果时指定用户的唯一标识信息（UserId），否则将无法进行千人千面的推荐
        """
        
        kwargs = {}
        kwargs["action"] = "ReportFeedUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportFeedUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportGoodsBehavior(
            self,
            request: models.ReportGoodsBehaviorRequest,
            opts: Dict = None,
    ) -> models.ReportGoodsBehaviorResponse:
        """
        上报电商类行为数据
        """
        
        kwargs = {}
        kwargs["action"] = "ReportGoodsBehavior"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportGoodsBehaviorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportGoodsInfo(
            self,
            request: models.ReportGoodsInfoRequest,
            opts: Dict = None,
    ) -> models.ReportGoodsInfoResponse:
        """
        上报电商类商品信息
        """
        
        kwargs = {}
        kwargs["action"] = "ReportGoodsInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportGoodsInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)