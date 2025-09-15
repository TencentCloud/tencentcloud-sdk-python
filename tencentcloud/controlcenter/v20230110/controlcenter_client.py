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
from tencentcloud.controlcenter.v20230110 import models


class ControlcenterClient(AbstractClient):
    _apiVersion = '2023-01-10'
    _endpoint = 'controlcenter.tencentcloudapi.com'
    _service = 'controlcenter'


    def BatchApplyAccountBaselines(self, request):
        r"""批量对存量账号应用基线

        :param request: Request instance for BatchApplyAccountBaselines.
        :type request: :class:`tencentcloud.controlcenter.v20230110.models.BatchApplyAccountBaselinesRequest`
        :rtype: :class:`tencentcloud.controlcenter.v20230110.models.BatchApplyAccountBaselinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchApplyAccountBaselines", params, headers=headers)
            response = json.loads(body)
            model = models.BatchApplyAccountBaselinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAccountFactoryBaseline(self, request):
        r"""获取用户基线配置数据

        :param request: Request instance for GetAccountFactoryBaseline.
        :type request: :class:`tencentcloud.controlcenter.v20230110.models.GetAccountFactoryBaselineRequest`
        :rtype: :class:`tencentcloud.controlcenter.v20230110.models.GetAccountFactoryBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAccountFactoryBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.GetAccountFactoryBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAccountFactoryBaselineItems(self, request):
        r"""获取账号工厂系统基线项

        :param request: Request instance for ListAccountFactoryBaselineItems.
        :type request: :class:`tencentcloud.controlcenter.v20230110.models.ListAccountFactoryBaselineItemsRequest`
        :rtype: :class:`tencentcloud.controlcenter.v20230110.models.ListAccountFactoryBaselineItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAccountFactoryBaselineItems", params, headers=headers)
            response = json.loads(body)
            model = models.ListAccountFactoryBaselineItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDeployStepTasks(self, request):
        r"""获取某个基线项历史应用信息

        :param request: Request instance for ListDeployStepTasks.
        :type request: :class:`tencentcloud.controlcenter.v20230110.models.ListDeployStepTasksRequest`
        :rtype: :class:`tencentcloud.controlcenter.v20230110.models.ListDeployStepTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDeployStepTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListDeployStepTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAccountFactoryBaseline(self, request):
        r"""更新用户当前基线项配置，基线配置会覆盖更新为当前配置。新增基线项时需要将新增的基线配置加到现有配置，删除基线项时需要将删除的基线配置从现有配置移除，然后保存最新基线配置。

        :param request: Request instance for UpdateAccountFactoryBaseline.
        :type request: :class:`tencentcloud.controlcenter.v20230110.models.UpdateAccountFactoryBaselineRequest`
        :rtype: :class:`tencentcloud.controlcenter.v20230110.models.UpdateAccountFactoryBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAccountFactoryBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAccountFactoryBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))