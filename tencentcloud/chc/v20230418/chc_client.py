# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.chc.v20230418 import models


class ChcClient(AbstractClient):
    _apiVersion = '2023-04-18'
    _endpoint = 'chc.tencentcloudapi.com'
    _service = 'chc'


    def ConfirmCommonServiceWorkOrder(self, request):
        """确认通用服务工单

        :param request: Request instance for ConfirmCommonServiceWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.ConfirmCommonServiceWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.ConfirmCommonServiceWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmCommonServiceWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmCommonServiceWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCommonServiceWorkOrder(self, request):
        """创建通用工单

        :param request: Request instance for CreateCommonServiceWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateCommonServiceWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateCommonServiceWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCommonServiceWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCommonServiceWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModelEvaluationWorkOrder(self, request):
        """创建设备型号评估工单

        :param request: Request instance for CreateModelEvaluationWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateModelEvaluationWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateModelEvaluationWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModelEvaluationWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModelEvaluationWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMovingWorkOrder(self, request):
        """创建设备搬迁工单

        :param request: Request instance for CreateMovingWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateMovingWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateMovingWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMovingWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMovingWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetDeviceModel(self, request):
        """创建新的网络设备型号

        :param request: Request instance for CreateNetDeviceModel.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateNetDeviceModelRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateNetDeviceModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetDeviceModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetDeviceModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePersonnelVisitWorkOrder(self, request):
        """创建人员到访工单

        :param request: Request instance for CreatePersonnelVisitWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreatePersonnelVisitWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreatePersonnelVisitWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePersonnelVisitWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePersonnelVisitWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePowerOffWorkOrder(self, request):
        """创建设备关电工单

        :param request: Request instance for CreatePowerOffWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreatePowerOffWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreatePowerOffWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePowerOffWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePowerOffWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePowerOnWorkOrder(self, request):
        """创建设备开电工单

        :param request: Request instance for CreatePowerOnWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreatePowerOnWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreatePowerOnWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePowerOnWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePowerOnWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQuitWorkOrder(self, request):
        """创建设备退出工单

        :param request: Request instance for CreateQuitWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateQuitWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateQuitWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQuitWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQuitWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRackOffWorkOrder(self, request):
        """创建设备下架工单

        :param request: Request instance for CreateRackOffWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateRackOffWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateRackOffWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRackOffWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRackOffWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRackOnWorkOrder(self, request):
        """创建设备上架工单

        :param request: Request instance for CreateRackOnWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateRackOnWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateRackOnWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRackOnWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRackOnWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReceivingWorkOrder(self, request):
        """创建设备收货工单

        :param request: Request instance for CreateReceivingWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateReceivingWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateReceivingWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReceivingWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReceivingWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServerModel(self, request):
        """新增服务器设备型号

        :param request: Request instance for CreateServerModel.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateServerModelRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateServerModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServerModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServerModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSpeciallyQuitWorkOrder(self, request):
        """创建临时设备退出工单

        :param request: Request instance for CreateSpeciallyQuitWorkOrder.
        :type request: :class:`tencentcloud.chc.v20230418.models.CreateSpeciallyQuitWorkOrderRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.CreateSpeciallyQuitWorkOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSpeciallyQuitWorkOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSpeciallyQuitWorkOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableModelList(self, request):
        """获取机房内可用的型号列表

        :param request: Request instance for DescribeAvailableModelList.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeAvailableModelListRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeAvailableModelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableModelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableModelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCampusList(self, request):
        """获取用户可操作的园区列表

        :param request: Request instance for DescribeCampusList.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeCampusListRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeCampusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCampusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCampusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCommonServiceWorkOrderDetail(self, request):
        """查询通用服务工单详情

        :param request: Request instance for DescribeCommonServiceWorkOrderDetail.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeCommonServiceWorkOrderDetailRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeCommonServiceWorkOrderDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCommonServiceWorkOrderDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCommonServiceWorkOrderDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerInfo(self, request):
        """查询客户信息

        :param request: Request instance for DescribeCustomerInfo.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeCustomerInfoRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeCustomerInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceList(self, request):
        """获取设备列表

        :param request: Request instance for DescribeDeviceList.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeDeviceListRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceWorkOrderDetail(self, request):
        """用于查询设备类工单的工单详情，如：'receiving', 'rackOn', 'powerOn', 'powerOff', 'rackOff', 'quit'

        :param request: Request instance for DescribeDeviceWorkOrderDetail.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeDeviceWorkOrderDetailRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeDeviceWorkOrderDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceWorkOrderDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceWorkOrderDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdcUnitAssetDetail(self, request):
        """查询机房管理单元资产详情

        :param request: Request instance for DescribeIdcUnitAssetDetail.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeIdcUnitAssetDetailRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeIdcUnitAssetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdcUnitAssetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdcUnitAssetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdcUnitDetail(self, request):
        """查询机房管理单元详情

        :param request: Request instance for DescribeIdcUnitDetail.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeIdcUnitDetailRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeIdcUnitDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdcUnitDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdcUnitDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdcs(self, request):
        """获取机房和机房管理单元信息

        :param request: Request instance for DescribeIdcs.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeIdcsRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeIdcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdcs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModel(self, request):
        """查询设备型号详情

        :param request: Request instance for DescribeModel.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeModelRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelEvaluationWorkOrderDetail(self, request):
        """查询设备型号评估工单详情

        :param request: Request instance for DescribeModelEvaluationWorkOrderDetail.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeModelEvaluationWorkOrderDetailRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeModelEvaluationWorkOrderDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelEvaluationWorkOrderDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelEvaluationWorkOrderDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelTemplate(self, request):
        """获取型号的填写模板

        :param request: Request instance for DescribeModelTemplate.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeModelTemplateRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeModelTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelVersionList(self, request):
        """获取用户的型号和对应的版本数量

        :param request: Request instance for DescribeModelVersionList.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeModelVersionListRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeModelVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonnelVisitWorkOrderDetail(self, request):
        """查询人员到访工单详情

        :param request: Request instance for DescribePersonnelVisitWorkOrderDetail.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribePersonnelVisitWorkOrderDetailRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribePersonnelVisitWorkOrderDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonnelVisitWorkOrderDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonnelVisitWorkOrderDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePositionStatusSummary(self, request):
        """获取机架总数及各状态对应的数量汇总

        :param request: Request instance for DescribePositionStatusSummary.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribePositionStatusSummaryRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribePositionStatusSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePositionStatusSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePositionStatusSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePositions(self, request):
        """获取机位列表

        :param request: Request instance for DescribePositions.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribePositionsRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribePositionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePositions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePositionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRacks(self, request):
        """获取机架列表

        :param request: Request instance for DescribeRacks.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeRacksRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeRacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRacksDistribution(self, request):
        """获取机房管理单元的机位分布

        :param request: Request instance for DescribeRacksDistribution.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeRacksDistributionRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeRacksDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRacksDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRacksDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceUsage(self, request):
        """查询资源汇总

        :param request: Request instance for DescribeResourceUsage.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeResourceUsageRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeResourceUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkOrderList(self, request):
        """查询工单列表

        :param request: Request instance for DescribeWorkOrderList.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeWorkOrderListRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeWorkOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkOrderStatistics(self, request):
        """工单统计数据查询

        :param request: Request instance for DescribeWorkOrderStatistics.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeWorkOrderStatisticsRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeWorkOrderStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkOrderStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkOrderStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkOrderTypes(self, request):
        """获取用户可用的工单类型

        :param request: Request instance for DescribeWorkOrderTypes.
        :type request: :class:`tencentcloud.chc.v20230418.models.DescribeWorkOrderTypesRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.DescribeWorkOrderTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkOrderTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkOrderTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportCustomerWorkOrderDetail(self, request):
        """导出工单详情

        :param request: Request instance for ExportCustomerWorkOrderDetail.
        :type request: :class:`tencentcloud.chc.v20230418.models.ExportCustomerWorkOrderDetailRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.ExportCustomerWorkOrderDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportCustomerWorkOrderDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportCustomerWorkOrderDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkOrderTypeCollectFlag(self, request):
        """如果当前该工单类型是收藏状态，调用接口后变成未收藏状态，如果是未收藏状态，调用该接口变为收藏状态

        :param request: Request instance for ModifyWorkOrderTypeCollectFlag.
        :type request: :class:`tencentcloud.chc.v20230418.models.ModifyWorkOrderTypeCollectFlagRequest`
        :rtype: :class:`tencentcloud.chc.v20230418.models.ModifyWorkOrderTypeCollectFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkOrderTypeCollectFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkOrderTypeCollectFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))