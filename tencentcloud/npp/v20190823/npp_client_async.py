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
from tencentcloud.npp.v20190823 import models
from typing import Dict


class NppClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'npp.tencentcloudapi.com'
    _service = 'npp'

    async def CreateCallBack(
            self,
            request: models.CreateCallBackRequest,
            opts: Dict = None,
    ) -> models.CreateCallBackResponse:
        """
        回拨呼叫请求
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCallBack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCallBackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DelVirtualNum(
            self,
            request: models.DelVirtualNumRequest,
            opts: Dict = None,
    ) -> models.DelVirtualNumResponse:
        """
        直拨解绑中间号
        """
        
        kwargs = {}
        kwargs["action"] = "DelVirtualNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DelVirtualNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCallBack(
            self,
            request: models.DeleteCallBackRequest,
            opts: Dict = None,
    ) -> models.DeleteCallBackResponse:
        """
        回拨呼叫取消
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCallBack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCallBackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallBackCdr(
            self,
            request: models.DescribeCallBackCdrRequest,
            opts: Dict = None,
    ) -> models.DescribeCallBackCdrResponse:
        """
        回拨话单获取接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallBackCdr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallBackCdrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallBackStatus(
            self,
            request: models.DescribeCallBackStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCallBackStatusResponse:
        """
        回拨通话状态获取
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallBackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallBackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallerDisplayList(
            self,
            request: models.DescribeCallerDisplayListRequest,
            opts: Dict = None,
    ) -> models.DescribeCallerDisplayListResponse:
        """
        回拨拉取主叫显号号码集合
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallerDisplayList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallerDisplayListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Get400Cdr(
            self,
            request: models.Get400CdrRequest,
            opts: Dict = None,
    ) -> models.Get400CdrResponse:
        """
        直拨话单获取接口
        """
        
        kwargs = {}
        kwargs["action"] = "Get400Cdr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Get400CdrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetVirtualNum(
            self,
            request: models.GetVirtualNumRequest,
            opts: Dict = None,
    ) -> models.GetVirtualNumResponse:
        """
        直拨获取中间号（App 使用方发起）
        """
        
        kwargs = {}
        kwargs["action"] = "GetVirtualNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetVirtualNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)