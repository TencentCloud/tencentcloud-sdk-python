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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.solar.v20181011 import models


class SolarClient(AbstractClient):
    _apiVersion = '2018-10-11'
    _endpoint = 'solar.tencentcloudapi.com'
    _service = 'solar'


    def CheckStaffChUser(self, request):
        """员工渠道更改员工状态

        :param request: Request instance for CheckStaffChUser.
        :type request: :class:`tencentcloud.solar.v20181011.models.CheckStaffChUserRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.CheckStaffChUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckStaffChUser", params, headers=headers)
            response = json.loads(body)
            model = models.CheckStaffChUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyActivityChannel(self, request):
        """复制活动渠道的策略

        :param request: Request instance for CopyActivityChannel.
        :type request: :class:`tencentcloud.solar.v20181011.models.CopyActivityChannelRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.CopyActivityChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyActivityChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CopyActivityChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        """创建项目

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.solar.v20181011.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubProject(self, request):
        """创建子项目

        :param request: Request instance for CreateSubProject.
        :type request: :class:`tencentcloud.solar.v20181011.models.CreateSubProjectRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.CreateSubProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        """删除项目

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.solar.v20181011.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomer(self, request):
        """客户档案查询客户详情

        :param request: Request instance for DescribeCustomer.
        :type request: :class:`tencentcloud.solar.v20181011.models.DescribeCustomerRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.DescribeCustomerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomers(self, request):
        """查询客户档案列表

        :param request: Request instance for DescribeCustomers.
        :type request: :class:`tencentcloud.solar.v20181011.models.DescribeCustomersRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.DescribeCustomersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProject(self, request):
        """项目详情展示

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.solar.v20181011.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectStock(self, request):
        """项目库存详情

        :param request: Request instance for DescribeProjectStock.
        :type request: :class:`tencentcloud.solar.v20181011.models.DescribeProjectStockRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.DescribeProjectStockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectStock", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectStockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjects(self, request):
        """项目列表展示

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.solar.v20181011.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceTemplateHeaders(self, request):
        """素材查询服务号模板的列表（样例）

        :param request: Request instance for DescribeResourceTemplateHeaders.
        :type request: :class:`tencentcloud.solar.v20181011.models.DescribeResourceTemplateHeadersRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.DescribeResourceTemplateHeadersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceTemplateHeaders", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceTemplateHeadersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubProject(self, request):
        """子项目详情

        :param request: Request instance for DescribeSubProject.
        :type request: :class:`tencentcloud.solar.v20181011.models.DescribeSubProjectRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.DescribeSubProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExpireFlow(self, request):
        """把审批中的工单置为已失效

        :param request: Request instance for ExpireFlow.
        :type request: :class:`tencentcloud.solar.v20181011.models.ExpireFlowRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.ExpireFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExpireFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ExpireFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        """修改项目

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.solar.v20181011.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OffLineProject(self, request):
        """下线项目

        :param request: Request instance for OffLineProject.
        :type request: :class:`tencentcloud.solar.v20181011.models.OffLineProjectRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.OffLineProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OffLineProject", params, headers=headers)
            response = json.loads(body)
            model = models.OffLineProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplenishProjectStock(self, request):
        """补充子项目库存

        :param request: Request instance for ReplenishProjectStock.
        :type request: :class:`tencentcloud.solar.v20181011.models.ReplenishProjectStockRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.ReplenishProjectStockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplenishProjectStock", params, headers=headers)
            response = json.loads(body)
            model = models.ReplenishProjectStockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendWxTouchTask(self, request):
        """发送企业微信触达任务

        :param request: Request instance for SendWxTouchTask.
        :type request: :class:`tencentcloud.solar.v20181011.models.SendWxTouchTaskRequest`
        :rtype: :class:`tencentcloud.solar.v20181011.models.SendWxTouchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendWxTouchTask", params, headers=headers)
            response = json.loads(body)
            model = models.SendWxTouchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))