# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.iotexplorer.v20190423 import models


class IotexplorerClient(AbstractClient):
    _apiVersion = '2019-04-23'
    _endpoint = 'iotexplorer.tencentcloudapi.com'


    def CallDeviceActionAsync(self, request):
        """提供给用户异步调用设备动作的能力

        :param request: Request instance for CallDeviceActionAsync.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionAsyncRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionAsyncResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CallDeviceActionAsync", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CallDeviceActionAsyncResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CallDeviceActionSync(self, request):
        """为用户提供同步调用设备动作的能力。

        :param request: Request instance for CallDeviceActionSync.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionSyncRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionSyncResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CallDeviceActionSync", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CallDeviceActionSyncResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ControlDeviceData(self, request):
        """根据设备产品ID、设备名称，设置控制设备的属性数据。

        :param request: Request instance for ControlDeviceData.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ControlDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ControlDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ControlDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlDeviceDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDevice(self, request):
        """创建设备

        :param request: Request instance for CreateDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProject(self, request):
        """为用户提供新建项目的能力，用于集中管理产品和应用。

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStudioProduct(self, request):
        """为用户提供新建产品的能力，用于管理用户的设备

        :param request: Request instance for CreateStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStudioProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDevice(self, request):
        """删除设备

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteProject(self, request):
        """提供删除某个项目的能力

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteStudioProduct(self, request):
        """提供删除某个项目下产品的能力

        :param request: Request instance for DeleteStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStudioProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevice(self, request):
        """用于查看某个设备的详细信息

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceData(self, request):
        """根据设备产品ID、设备名称，获取设备上报的属性数据。

        :param request: Request instance for DescribeDeviceData.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceDataHistory(self, request):
        """获取设备在指定时间范围内上报的历史数据。

        :param request: Request instance for DescribeDeviceDataHistory.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataHistoryRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceDataHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceDataHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeModelDefinition(self, request):
        """查询产品配置的数据模板信息

        :param request: Request instance for DescribeModelDefinition.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModelDefinition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModelDefinitionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProject(self, request):
        """查询项目详情

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStudioProduct(self, request):
        """提供查看茶品详细信息的能力，包括产品的ID、数据协议、认证类型等重要参数

        :param request: Request instance for DescribeStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStudioProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDeviceList(self, request):
        """用于查询某个产品下的设备列表

        :param request: Request instance for GetDeviceList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetProjectList(self, request):
        """提供查询用户所创建的项目列表查询功能。

        :param request: Request instance for GetProjectList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetProjectListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetProjectListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetProjectList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetProjectListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetStudioProductList(self, request):
        """提供查询某个项目下所有产品信息的能力。

        :param request: Request instance for GetStudioProductList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetStudioProductListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetStudioProductListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetStudioProductList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetStudioProductListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListEventHistory(self, request):
        """获取设备的历史事件

        :param request: Request instance for ListEventHistory.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ListEventHistoryRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ListEventHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEventHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEventHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyModelDefinition(self, request):
        """提供修改产品的数据模板的能力

        :param request: Request instance for ModifyModelDefinition.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModelDefinition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModelDefinitionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProject(self, request):
        """修改项目

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyStudioProduct(self, request):
        """提供修改产品的名称和描述等信息的能力

        :param request: Request instance for ModifyStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyStudioProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReleaseStudioProduct(self, request):
        """产品开发完成并测试通过后，通过发布产品将产品设置为发布状态

        :param request: Request instance for ReleaseStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ReleaseStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ReleaseStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseStudioProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchStudioProduct(self, request):
        """提供根据产品名称查找产品的能力

        :param request: Request instance for SearchStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.SearchStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.SearchStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchStudioProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)