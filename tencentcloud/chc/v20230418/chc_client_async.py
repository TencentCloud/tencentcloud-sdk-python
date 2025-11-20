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
from tencentcloud.chc.v20230418 import models
from typing import Dict


class ChcClient(AbstractClient):
    _apiVersion = '2023-04-18'
    _endpoint = 'chc.tencentcloudapi.com'
    _service = 'chc'

    async def ConfirmCommonServiceWorkOrder(
            self,
            request: models.ConfirmCommonServiceWorkOrderRequest,
            opts: Dict = None,
    ) -> models.ConfirmCommonServiceWorkOrderResponse:
        """
        确认通用服务工单
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmCommonServiceWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmCommonServiceWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCommonServiceWorkOrder(
            self,
            request: models.CreateCommonServiceWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreateCommonServiceWorkOrderResponse:
        """
        创建通用工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCommonServiceWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCommonServiceWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModelEvaluationWorkOrder(
            self,
            request: models.CreateModelEvaluationWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreateModelEvaluationWorkOrderResponse:
        """
        创建设备型号评估工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModelEvaluationWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelEvaluationWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMovingWorkOrder(
            self,
            request: models.CreateMovingWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreateMovingWorkOrderResponse:
        """
        创建设备搬迁工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMovingWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMovingWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetDeviceModel(
            self,
            request: models.CreateNetDeviceModelRequest,
            opts: Dict = None,
    ) -> models.CreateNetDeviceModelResponse:
        """
        创建新的网络设备型号
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetDeviceModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetDeviceModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePersonnelVisitWorkOrder(
            self,
            request: models.CreatePersonnelVisitWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreatePersonnelVisitWorkOrderResponse:
        """
        创建人员到访工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePersonnelVisitWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePersonnelVisitWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePowerOffWorkOrder(
            self,
            request: models.CreatePowerOffWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreatePowerOffWorkOrderResponse:
        """
        创建设备关电工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePowerOffWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePowerOffWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePowerOnWorkOrder(
            self,
            request: models.CreatePowerOnWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreatePowerOnWorkOrderResponse:
        """
        创建设备开电工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePowerOnWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePowerOnWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQuitWorkOrder(
            self,
            request: models.CreateQuitWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreateQuitWorkOrderResponse:
        """
        创建设备退出工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQuitWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQuitWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRackOffWorkOrder(
            self,
            request: models.CreateRackOffWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreateRackOffWorkOrderResponse:
        """
        创建设备下架工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRackOffWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRackOffWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRackOnWorkOrder(
            self,
            request: models.CreateRackOnWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreateRackOnWorkOrderResponse:
        """
        创建设备上架工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRackOnWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRackOnWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReceivingWorkOrder(
            self,
            request: models.CreateReceivingWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreateReceivingWorkOrderResponse:
        """
        创建设备收货工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReceivingWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReceivingWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServerModel(
            self,
            request: models.CreateServerModelRequest,
            opts: Dict = None,
    ) -> models.CreateServerModelResponse:
        """
        新增服务器设备型号
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServerModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServerModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSpeciallyQuitWorkOrder(
            self,
            request: models.CreateSpeciallyQuitWorkOrderRequest,
            opts: Dict = None,
    ) -> models.CreateSpeciallyQuitWorkOrderResponse:
        """
        创建临时设备退出工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSpeciallyQuitWorkOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSpeciallyQuitWorkOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableModelList(
            self,
            request: models.DescribeAvailableModelListRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableModelListResponse:
        """
        获取机房内可用的型号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableModelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableModelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCampusList(
            self,
            request: models.DescribeCampusListRequest,
            opts: Dict = None,
    ) -> models.DescribeCampusListResponse:
        """
        获取用户可操作的园区列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCampusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCampusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCommonServiceWorkOrderDetail(
            self,
            request: models.DescribeCommonServiceWorkOrderDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCommonServiceWorkOrderDetailResponse:
        """
        查询通用服务工单详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCommonServiceWorkOrderDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCommonServiceWorkOrderDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerInfo(
            self,
            request: models.DescribeCustomerInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerInfoResponse:
        """
        查询客户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceList(
            self,
            request: models.DescribeDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceListResponse:
        """
        获取设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceWorkOrderDetail(
            self,
            request: models.DescribeDeviceWorkOrderDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceWorkOrderDetailResponse:
        """
        用于查询设备类工单的工单详情，如：'receiving', 'rackOn', 'powerOn', 'powerOff', 'rackOff', 'quit'
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceWorkOrderDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceWorkOrderDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdcUnitAssetDetail(
            self,
            request: models.DescribeIdcUnitAssetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeIdcUnitAssetDetailResponse:
        """
        查询机房管理单元资产详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdcUnitAssetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdcUnitAssetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdcUnitDetail(
            self,
            request: models.DescribeIdcUnitDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeIdcUnitDetailResponse:
        """
        查询机房管理单元详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdcUnitDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdcUnitDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdcs(
            self,
            request: models.DescribeIdcsRequest,
            opts: Dict = None,
    ) -> models.DescribeIdcsResponse:
        """
        获取机房和机房管理单元信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModel(
            self,
            request: models.DescribeModelRequest,
            opts: Dict = None,
    ) -> models.DescribeModelResponse:
        """
        查询设备型号详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelEvaluationWorkOrderDetail(
            self,
            request: models.DescribeModelEvaluationWorkOrderDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeModelEvaluationWorkOrderDetailResponse:
        """
        查询设备型号评估工单详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelEvaluationWorkOrderDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelEvaluationWorkOrderDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelTemplate(
            self,
            request: models.DescribeModelTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeModelTemplateResponse:
        """
        获取型号的填写模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelVersionList(
            self,
            request: models.DescribeModelVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeModelVersionListResponse:
        """
        获取用户的型号和对应的版本数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePersonnelVisitWorkOrderDetail(
            self,
            request: models.DescribePersonnelVisitWorkOrderDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePersonnelVisitWorkOrderDetailResponse:
        """
        查询人员到访工单详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePersonnelVisitWorkOrderDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePersonnelVisitWorkOrderDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePositionStatusSummary(
            self,
            request: models.DescribePositionStatusSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribePositionStatusSummaryResponse:
        """
        获取机架总数及各状态对应的数量汇总
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePositionStatusSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePositionStatusSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePositions(
            self,
            request: models.DescribePositionsRequest,
            opts: Dict = None,
    ) -> models.DescribePositionsResponse:
        """
        获取机位列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePositions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePositionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRacks(
            self,
            request: models.DescribeRacksRequest,
            opts: Dict = None,
    ) -> models.DescribeRacksResponse:
        """
        获取机架列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRacksDistribution(
            self,
            request: models.DescribeRacksDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeRacksDistributionResponse:
        """
        获取机房管理单元的机位分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRacksDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRacksDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceUsage(
            self,
            request: models.DescribeResourceUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceUsageResponse:
        """
        查询资源汇总
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkOrderList(
            self,
            request: models.DescribeWorkOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkOrderListResponse:
        """
        查询工单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkOrderStatistics(
            self,
            request: models.DescribeWorkOrderStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkOrderStatisticsResponse:
        """
        工单统计数据查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkOrderStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkOrderStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkOrderTypes(
            self,
            request: models.DescribeWorkOrderTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkOrderTypesResponse:
        """
        获取用户可用的工单类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkOrderTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkOrderTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportCustomerWorkOrderDetail(
            self,
            request: models.ExportCustomerWorkOrderDetailRequest,
            opts: Dict = None,
    ) -> models.ExportCustomerWorkOrderDetailResponse:
        """
        导出工单详情
        """
        
        kwargs = {}
        kwargs["action"] = "ExportCustomerWorkOrderDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportCustomerWorkOrderDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkOrderTypeCollectFlag(
            self,
            request: models.ModifyWorkOrderTypeCollectFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkOrderTypeCollectFlagResponse:
        """
        如果当前该工单类型是收藏状态，调用接口后变成未收藏状态，如果是未收藏状态，调用该接口变为收藏状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkOrderTypeCollectFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkOrderTypeCollectFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)