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
from tencentcloud.cloudhsm.v20191112 import models
from typing import Dict


class CloudhsmClient(AbstractClient):
    _apiVersion = '2019-11-12'
    _endpoint = 'cloudhsm.tencentcloudapi.com'
    _service = 'cloudhsm'

    async def DescribeHSMBySubnetId(
            self,
            request: models.DescribeHSMBySubnetIdRequest,
            opts: Dict = None,
    ) -> models.DescribeHSMBySubnetIdResponse:
        """
        通过SubnetId获取Hsm资源数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHSMBySubnetId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHSMBySubnetIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHSMByVpcId(
            self,
            request: models.DescribeHSMByVpcIdRequest,
            opts: Dict = None,
    ) -> models.DescribeHSMByVpcIdResponse:
        """
        通过VpcId获取Hsm资源数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHSMByVpcId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHSMByVpcIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnet(
            self,
            request: models.DescribeSubnetRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetResponse:
        """
        查询子网列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportedHsm(
            self,
            request: models.DescribeSupportedHsmRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportedHsmResponse:
        """
        获取当前地域所支持的设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportedHsm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportedHsmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsg(
            self,
            request: models.DescribeUsgRequest,
            opts: Dict = None,
    ) -> models.DescribeUsgResponse:
        """
        根据用户的AppId获取用户安全组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsgRule(
            self,
            request: models.DescribeUsgRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeUsgRuleResponse:
        """
        获取安全组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsgRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsgRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpc(
            self,
            request: models.DescribeVpcRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcResponse:
        """
        查询用户的私有网络列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVsmAttributes(
            self,
            request: models.DescribeVsmAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeVsmAttributesResponse:
        """
        获取VSM属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVsmAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVsmAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVsms(
            self,
            request: models.DescribeVsmsRequest,
            opts: Dict = None,
    ) -> models.DescribeVsmsResponse:
        """
        获取用户VSM列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVsms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVsmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAlarmEvent(
            self,
            request: models.GetAlarmEventRequest,
            opts: Dict = None,
    ) -> models.GetAlarmEventResponse:
        """
        获取告警事件
        """
        
        kwargs = {}
        kwargs["action"] = "GetAlarmEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAlarmEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetVsmMonitorInfo(
            self,
            request: models.GetVsmMonitorInfoRequest,
            opts: Dict = None,
    ) -> models.GetVsmMonitorInfoResponse:
        """
        获取VSM监控信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetVsmMonitorInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetVsmMonitorInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceBuyVsm(
            self,
            request: models.InquiryPriceBuyVsmRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceBuyVsmResponse:
        """
        购买询价接口
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceBuyVsm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceBuyVsmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmEvent(
            self,
            request: models.ModifyAlarmEventRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmEventResponse:
        """
        修改告警事件
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVsmAttributes(
            self,
            request: models.ModifyVsmAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyVsmAttributesResponse:
        """
        修改VSM属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVsmAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVsmAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)