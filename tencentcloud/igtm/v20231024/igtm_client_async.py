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
from tencentcloud.igtm.v20231024 import models
from typing import Dict


class IgtmClient(AbstractClient):
    _apiVersion = '2023-10-24'
    _endpoint = 'igtm.tencentcloudapi.com'
    _service = 'igtm'

    async def CreateAddressPool(
            self,
            request: models.CreateAddressPoolRequest,
            opts: Dict = None,
    ) -> models.CreateAddressPoolResponse:
        """
        创建地址池
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAddressPool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAddressPoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        创建实例接口，仅供免费实例使用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMonitor(
            self,
            request: models.CreateMonitorRequest,
            opts: Dict = None,
    ) -> models.CreateMonitorResponse:
        """
        新增监控器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePackageAndPay(
            self,
            request: models.CreatePackageAndPayRequest,
            opts: Dict = None,
    ) -> models.CreatePackageAndPayResponse:
        """
        购买套餐并支付，此接口会在余额扣费，谨慎调用
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePackageAndPay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePackageAndPayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStrategy(
            self,
            request: models.CreateStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateStrategyResponse:
        """
        新建策略接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddressPool(
            self,
            request: models.DeleteAddressPoolRequest,
            opts: Dict = None,
    ) -> models.DeleteAddressPoolResponse:
        """
        删除地址池
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddressPool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddressPoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMonitor(
            self,
            request: models.DeleteMonitorRequest,
            opts: Dict = None,
    ) -> models.DeleteMonitorResponse:
        """
        删除监控器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStrategy(
            self,
            request: models.DeleteStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteStrategyResponse:
        """
        删除策略接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressLocation(
            self,
            request: models.DescribeAddressLocationRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressLocationResponse:
        """
        获取地址所属地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressPoolDetail(
            self,
            request: models.DescribeAddressPoolDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressPoolDetailResponse:
        """
        地址池详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressPoolDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressPoolDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressPoolList(
            self,
            request: models.DescribeAddressPoolListRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressPoolListResponse:
        """
        地址池列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressPoolList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressPoolListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDetectPackageDetail(
            self,
            request: models.DescribeDetectPackageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDetectPackageDetailResponse:
        """
        探测任务包详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDetectPackageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDetectPackageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDetectTaskPackageList(
            self,
            request: models.DescribeDetectTaskPackageListRequest,
            opts: Dict = None,
    ) -> models.DescribeDetectTaskPackageListResponse:
        """
        探测任务套餐列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDetectTaskPackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDetectTaskPackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDetectors(
            self,
            request: models.DescribeDetectorsRequest,
            opts: Dict = None,
    ) -> models.DescribeDetectorsResponse:
        """
        获取探测节点列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDetectors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDetectorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDnsLineList(
            self,
            request: models.DescribeDnsLineListRequest,
            opts: Dict = None,
    ) -> models.DescribeDnsLineListResponse:
        """
        查询分组线路列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDnsLineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDnsLineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDetail(
            self,
            request: models.DescribeInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDetailResponse:
        """
        实例详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceList(
            self,
            request: models.DescribeInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceListResponse:
        """
        实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancePackageList(
            self,
            request: models.DescribeInstancePackageListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancePackageListResponse:
        """
        实例套餐列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancePackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancePackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonitorDetail(
            self,
            request: models.DescribeMonitorDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMonitorDetailResponse:
        """
        查询监控器详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonitorDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonitorDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonitors(
            self,
            request: models.DescribeMonitorsRequest,
            opts: Dict = None,
    ) -> models.DescribeMonitorsResponse:
        """
        获取所有监控器
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonitors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonitorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuotas(
            self,
            request: models.DescribeQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotasResponse:
        """
        配额查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStrategyDetail(
            self,
            request: models.DescribeStrategyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategyDetailResponse:
        """
        策略详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStrategyList(
            self,
            request: models.DescribeStrategyListRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategyListResponse:
        """
        策略列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressPool(
            self,
            request: models.ModifyAddressPoolRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressPoolResponse:
        """
        修改地址池
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressPool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressPoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceConfig(
            self,
            request: models.ModifyInstanceConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceConfigResponse:
        """
        修改实例配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMonitor(
            self,
            request: models.ModifyMonitorRequest,
            opts: Dict = None,
    ) -> models.ModifyMonitorResponse:
        """
        修改监控器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPackageAutoRenew(
            self,
            request: models.ModifyPackageAutoRenewRequest,
            opts: Dict = None,
    ) -> models.ModifyPackageAutoRenewResponse:
        """
        设置自动续费接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPackageAutoRenew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPackageAutoRenewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStrategy(
            self,
            request: models.ModifyStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyStrategyResponse:
        """
        修改策略接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)