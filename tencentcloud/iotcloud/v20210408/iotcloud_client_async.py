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
from tencentcloud.iotcloud.v20210408 import models
from typing import Dict


class IotcloudClient(AbstractClient):
    _apiVersion = '2021-04-08'
    _endpoint = 'iotcloud.tencentcloudapi.com'
    _service = 'iotcloud'

    async def BatchUpdateFirmware(
            self,
            request: models.BatchUpdateFirmwareRequest,
            opts: Dict = None,
    ) -> models.BatchUpdateFirmwareResponse:
        """
        本接口（BatchUpdateFirmware）用于批量更新设备固件
        """
        
        kwargs = {}
        kwargs["action"] = "BatchUpdateFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchUpdateFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDevices(
            self,
            request: models.BindDevicesRequest,
            opts: Dict = None,
    ) -> models.BindDevicesResponse:
        """
        本接口（BindDevices）用于网关设备批量绑定子设备
        """
        
        kwargs = {}
        kwargs["action"] = "BindDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelDeviceFirmwareTask(
            self,
            request: models.CancelDeviceFirmwareTaskRequest,
            opts: Dict = None,
    ) -> models.CancelDeviceFirmwareTaskResponse:
        """
        取消设备升级任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelDeviceFirmwareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelDeviceFirmwareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDevice(
            self,
            request: models.CreateDeviceRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceResponse:
        """
        本接口（CreateDevice）用于新建一个物联网通信设备。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultiDevicesTask(
            self,
            request: models.CreateMultiDevicesTaskRequest,
            opts: Dict = None,
    ) -> models.CreateMultiDevicesTaskResponse:
        """
        本接口（CreateMultiDevicesTask）用于创建产品级别的批量创建设备任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultiDevicesTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultiDevicesTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateCA(
            self,
            request: models.CreatePrivateCARequest,
            opts: Dict = None,
    ) -> models.CreatePrivateCAResponse:
        """
        创建私有CA证书
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProduct(
            self,
            request: models.CreateProductRequest,
            opts: Dict = None,
    ) -> models.CreateProductResponse:
        """
        本接口（CreateProduct）用于创建一个新的物联网通信产品
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskFileUrl(
            self,
            request: models.CreateTaskFileUrlRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFileUrlResponse:
        """
        本接口（CreateTaskFileUrl）用于获取产品级任务文件上传链接
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFileUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFileUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopicPolicy(
            self,
            request: models.CreateTopicPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateTopicPolicyResponse:
        """
        本接口（CreateTopicPolicy）用于创建一个Topic
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopicPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopicRule(
            self,
            request: models.CreateTopicRuleRequest,
            opts: Dict = None,
    ) -> models.CreateTopicRuleResponse:
        """
        本接口（CreateTopicRule）用于创建一个规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevice(
            self,
            request: models.DeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceResponse:
        """
        本接口（DeleteDevice）用于删除物联网通信设备。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceResource(
            self,
            request: models.DeleteDeviceResourceRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceResourceResponse:
        """
        本接口（DeleteDeviceResource）用于删除设备资源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceShadow(
            self,
            request: models.DeleteDeviceShadowRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceShadowResponse:
        """
        本接口（DeleteDeviceShadow）用于删除设备影子
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceShadow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceShadowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateCA(
            self,
            request: models.DeletePrivateCARequest,
            opts: Dict = None,
    ) -> models.DeletePrivateCAResponse:
        """
        删除私有CA证书
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProduct(
            self,
            request: models.DeleteProductRequest,
            opts: Dict = None,
    ) -> models.DeleteProductResponse:
        """
        本接口（DeleteProduct）用于删除一个物联网通信产品
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProductPrivateCA(
            self,
            request: models.DeleteProductPrivateCARequest,
            opts: Dict = None,
    ) -> models.DeleteProductPrivateCAResponse:
        """
        删除产品的私有CA证书
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProductPrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProductPrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopicRule(
            self,
            request: models.DeleteTopicRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicRuleResponse:
        """
        本接口（DeleteTopicRule）用于删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevice(
            self,
            request: models.DescribeDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceResponse:
        """
        本接口（DescribeDevice）用于查看设备信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceClientKey(
            self,
            request: models.DescribeDeviceClientKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceClientKeyResponse:
        """
        获取证书认证类型设备的私钥，刚生成或者重置设备后仅可调用一次
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceClientKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceClientKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceResource(
            self,
            request: models.DescribeDeviceResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceResourceResponse:
        """
        本接口（DescribeDeviceResource）用于查询设备资源详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceResources(
            self,
            request: models.DescribeDeviceResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceResourcesResponse:
        """
        本接口（DescribeDeviceResources）用于查询设备资源列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceShadow(
            self,
            request: models.DescribeDeviceShadowRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceShadowResponse:
        """
        本接口（DescribeDeviceShadow）用于查询虚拟设备信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceShadow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceShadowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevices(
            self,
            request: models.DescribeDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicesResponse:
        """
        本接口（DescribeDevices）用于查询物联网通信设备的设备列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmware(
            self,
            request: models.DescribeFirmwareRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareResponse:
        """
        查询固件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTask(
            self,
            request: models.DescribeFirmwareTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTaskResponse:
        """
        查询固件升级任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTaskDevices(
            self,
            request: models.DescribeFirmwareTaskDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTaskDevicesResponse:
        """
        查询固件升级任务的设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTaskDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTaskDistribution(
            self,
            request: models.DescribeFirmwareTaskDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTaskDistributionResponse:
        """
        查询固件升级任务状态分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTaskDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTaskStatistics(
            self,
            request: models.DescribeFirmwareTaskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTaskStatisticsResponse:
        """
        查询固件升级任务统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTaskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTasks(
            self,
            request: models.DescribeFirmwareTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTasksResponse:
        """
        查询固件升级任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayBindDevices(
            self,
            request: models.DescribeGatewayBindDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayBindDevicesResponse:
        """
        本接口（DescribeGatewayBindDevices）用于获取网关绑定的子设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayBindDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayBindDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateCA(
            self,
            request: models.DescribePrivateCARequest,
            opts: Dict = None,
    ) -> models.DescribePrivateCAResponse:
        """
        查询私有化CA信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateCABindedProducts(
            self,
            request: models.DescribePrivateCABindedProductsRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateCABindedProductsResponse:
        """
        查询私有CA绑定的产品列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateCABindedProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateCABindedProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateCAs(
            self,
            request: models.DescribePrivateCAsRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateCAsResponse:
        """
        查询私有CA证书列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateCAs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateCAsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProduct(
            self,
            request: models.DescribeProductRequest,
            opts: Dict = None,
    ) -> models.DescribeProductResponse:
        """
        本接口（DescribeProduct）用于查看产品详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductCA(
            self,
            request: models.DescribeProductCARequest,
            opts: Dict = None,
    ) -> models.DescribeProductCAResponse:
        """
        查询产品绑定的CA证书
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductResource(
            self,
            request: models.DescribeProductResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeProductResourceResponse:
        """
        本接口（DescribeProductResource）用于查询产品资源详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductResources(
            self,
            request: models.DescribeProductResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeProductResourcesResponse:
        """
        本接口（DescribeProductResources）用于查询产品资源列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductTask(
            self,
            request: models.DescribeProductTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeProductTaskResponse:
        """
        本接口（DescribeProductTask）用于查看产品级别的任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductTasks(
            self,
            request: models.DescribeProductTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeProductTasksResponse:
        """
        本接口（DescribeProductTasks）用于查看产品级别的任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProducts(
            self,
            request: models.DescribeProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeProductsResponse:
        """
        本接口（DescribeProducts）用于列出产品列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePushResourceTaskStatistics(
            self,
            request: models.DescribePushResourceTaskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribePushResourceTaskStatisticsResponse:
        """
        查询推送资源任务统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePushResourceTaskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePushResourceTaskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTasks(
            self,
            request: models.DescribeResourceTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTasksResponse:
        """
        查询资源推送任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableTopicRule(
            self,
            request: models.DisableTopicRuleRequest,
            opts: Dict = None,
    ) -> models.DisableTopicRuleResponse:
        """
        本接口（DisableTopicRule）用于禁用规则
        """
        
        kwargs = {}
        kwargs["action"] = "DisableTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadDeviceResource(
            self,
            request: models.DownloadDeviceResourceRequest,
            opts: Dict = None,
    ) -> models.DownloadDeviceResourceResponse:
        """
        本接口（DownloadDeviceResource）用于下载设备资源
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadDeviceResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadDeviceResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditFirmware(
            self,
            request: models.EditFirmwareRequest,
            opts: Dict = None,
    ) -> models.EditFirmwareResponse:
        """
        编辑固件信息
        """
        
        kwargs = {}
        kwargs["action"] = "EditFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableTopicRule(
            self,
            request: models.EnableTopicRuleRequest,
            opts: Dict = None,
    ) -> models.EnableTopicRuleResponse:
        """
        本接口（EnableTopicRule）用于启用规则
        """
        
        kwargs = {}
        kwargs["action"] = "EnableTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAllVersion(
            self,
            request: models.GetAllVersionRequest,
            opts: Dict = None,
    ) -> models.GetAllVersionResponse:
        """
        本接口（GetAllVersion）用于获取所有的版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetAllVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAllVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCOSURL(
            self,
            request: models.GetCOSURLRequest,
            opts: Dict = None,
    ) -> models.GetCOSURLResponse:
        """
        本接口（GetCOSURL）用于获取固件存储在COS的URL
        """
        
        kwargs = {}
        kwargs["action"] = "GetCOSURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCOSURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUserResourceInfo(
            self,
            request: models.GetUserResourceInfoRequest,
            opts: Dict = None,
    ) -> models.GetUserResourceInfoResponse:
        """
        本接口（GetUserResourceInfo）用于查询用户资源使用信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetUserResourceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserResourceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListFirmwares(
            self,
            request: models.ListFirmwaresRequest,
            opts: Dict = None,
    ) -> models.ListFirmwaresResponse:
        """
        本接口（ListFirmwares）用于获取固件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListFirmwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListFirmwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLog(
            self,
            request: models.ListLogRequest,
            opts: Dict = None,
    ) -> models.ListLogResponse:
        """
        本接口（ListLog）用于查看日志信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLogPayload(
            self,
            request: models.ListLogPayloadRequest,
            opts: Dict = None,
    ) -> models.ListLogPayloadResponse:
        """
        获取日志内容列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListLogPayload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLogPayloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSDKLog(
            self,
            request: models.ListSDKLogRequest,
            opts: Dict = None,
    ) -> models.ListSDKLogResponse:
        """
        获取设备上报的日志
        """
        
        kwargs = {}
        kwargs["action"] = "ListSDKLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSDKLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTopicRules(
            self,
            request: models.ListTopicRulesRequest,
            opts: Dict = None,
    ) -> models.ListTopicRulesResponse:
        """
        本接口（ListTopicRules）用于分页获取规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTopicRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTopicRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishBroadcastMessage(
            self,
            request: models.PublishBroadcastMessageRequest,
            opts: Dict = None,
    ) -> models.PublishBroadcastMessageResponse:
        """
        发布广播消息
        """
        
        kwargs = {}
        kwargs["action"] = "PublishBroadcastMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishBroadcastMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishMessage(
            self,
            request: models.PublishMessageRequest,
            opts: Dict = None,
    ) -> models.PublishMessageResponse:
        """
        本接口（PublishMessage）用于向某个主题发消息。
        """
        
        kwargs = {}
        kwargs["action"] = "PublishMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishRRPCMessage(
            self,
            request: models.PublishRRPCMessageRequest,
            opts: Dict = None,
    ) -> models.PublishRRPCMessageResponse:
        """
        发布RRPC消息
        """
        
        kwargs = {}
        kwargs["action"] = "PublishRRPCMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishRRPCMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceTopicRule(
            self,
            request: models.ReplaceTopicRuleRequest,
            opts: Dict = None,
    ) -> models.ReplaceTopicRuleResponse:
        """
        本接口（ReplaceTopicRule）用于修改替换规则
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDeviceState(
            self,
            request: models.ResetDeviceStateRequest,
            opts: Dict = None,
    ) -> models.ResetDeviceStateResponse:
        """
        重置设备的连接状态
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDeviceState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDeviceStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryDeviceFirmwareTask(
            self,
            request: models.RetryDeviceFirmwareTaskRequest,
            opts: Dict = None,
    ) -> models.RetryDeviceFirmwareTaskResponse:
        """
        重试设备升级任务
        """
        
        kwargs = {}
        kwargs["action"] = "RetryDeviceFirmwareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryDeviceFirmwareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetProductsForbiddenStatus(
            self,
            request: models.SetProductsForbiddenStatusRequest,
            opts: Dict = None,
    ) -> models.SetProductsForbiddenStatusResponse:
        """
        批量设置产品禁用状态
        """
        
        kwargs = {}
        kwargs["action"] = "SetProductsForbiddenStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetProductsForbiddenStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindDevices(
            self,
            request: models.UnbindDevicesRequest,
            opts: Dict = None,
    ) -> models.UnbindDevicesResponse:
        """
        本接口（UnbindDevices）用于网关设备批量解绑子设备
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceAvailableState(
            self,
            request: models.UpdateDeviceAvailableStateRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceAvailableStateResponse:
        """
        启用或者禁用设备
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceAvailableState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceAvailableStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceLogLevel(
            self,
            request: models.UpdateDeviceLogLevelRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceLogLevelResponse:
        """
        设置设备上报的日志级别
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceLogLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceLogLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDevicePSK(
            self,
            request: models.UpdateDevicePSKRequest,
            opts: Dict = None,
    ) -> models.UpdateDevicePSKResponse:
        """
        本接口（UpdateDevicePSK）用于更新设备的PSK
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDevicePSK"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDevicePSKResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceShadow(
            self,
            request: models.UpdateDeviceShadowRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceShadowResponse:
        """
        本接口（UpdateDeviceShadow）用于更新虚拟设备信息。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceShadow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceShadowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDevicesEnableState(
            self,
            request: models.UpdateDevicesEnableStateRequest,
            opts: Dict = None,
    ) -> models.UpdateDevicesEnableStateResponse:
        """
        批量启用或者禁用设备
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDevicesEnableState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDevicesEnableStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOtaTaskStatus(
            self,
            request: models.UpdateOtaTaskStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateOtaTaskStatusResponse:
        """
        本接口（UpdateOtaTask）当固件升级大任务处于没有在全部成功的状态时，可修改为取消状态，取消部分或全部设备的升级;或其它允许的可修改的状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOtaTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOtaTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrivateCA(
            self,
            request: models.UpdatePrivateCARequest,
            opts: Dict = None,
    ) -> models.UpdatePrivateCAResponse:
        """
        更新私有CA证书
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProductDynamicRegister(
            self,
            request: models.UpdateProductDynamicRegisterRequest,
            opts: Dict = None,
    ) -> models.UpdateProductDynamicRegisterResponse:
        """
        更新产品动态注册的配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProductDynamicRegister"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProductDynamicRegisterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProductPrivateCA(
            self,
            request: models.UpdateProductPrivateCARequest,
            opts: Dict = None,
    ) -> models.UpdateProductPrivateCAResponse:
        """
        更新产品的私有CA
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProductPrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProductPrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTopicPolicy(
            self,
            request: models.UpdateTopicPolicyRequest,
            opts: Dict = None,
    ) -> models.UpdateTopicPolicyResponse:
        """
        本接口（UpdateTopicPolicy）用于更新Topic信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTopicPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTopicPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadFirmware(
            self,
            request: models.UploadFirmwareRequest,
            opts: Dict = None,
    ) -> models.UploadFirmwareResponse:
        """
        本接口（UploadFirmware）用于上传设备固件信息
        """
        
        kwargs = {}
        kwargs["action"] = "UploadFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)