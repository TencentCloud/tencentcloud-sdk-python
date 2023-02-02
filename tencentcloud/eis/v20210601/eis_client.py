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
from tencentcloud.eis.v20210601 import models


class EisClient(AbstractClient):
    _apiVersion = '2021-06-01'
    _endpoint = 'eis.tencentcloudapi.com'
    _service = 'eis'


    def GetRuntimeMC(self, request):
        """获取运行时详情

        :param request: Request instance for GetRuntimeMC.
        :type request: :class:`tencentcloud.eis.v20210601.models.GetRuntimeMCRequest`
        :rtype: :class:`tencentcloud.eis.v20210601.models.GetRuntimeMCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRuntimeMC", params, headers=headers)
            response = json.loads(body)
            model = models.GetRuntimeMCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRuntimeResourceMonitorMetricMC(self, request):
        """获取运行时资源监控详情，cpu，memory，bandwidth

        :param request: Request instance for GetRuntimeResourceMonitorMetricMC.
        :type request: :class:`tencentcloud.eis.v20210601.models.GetRuntimeResourceMonitorMetricMCRequest`
        :rtype: :class:`tencentcloud.eis.v20210601.models.GetRuntimeResourceMonitorMetricMCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRuntimeResourceMonitorMetricMC", params, headers=headers)
            response = json.loads(body)
            model = models.GetRuntimeResourceMonitorMetricMCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListDeployableRuntimesMC(self, request):
        """返回用户可用的运行时列表，发布应用时返回的运行时环境，仅shared和private运行时，无sandbox运行时，并且只有running/scaling状态的

        :param request: Request instance for ListDeployableRuntimesMC.
        :type request: :class:`tencentcloud.eis.v20210601.models.ListDeployableRuntimesMCRequest`
        :rtype: :class:`tencentcloud.eis.v20210601.models.ListDeployableRuntimesMCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDeployableRuntimesMC", params, headers=headers)
            response = json.loads(body)
            model = models.ListDeployableRuntimesMCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListRuntimeDeployedInstancesMC(self, request):
        """获取运行时部署的应用实例列表

        :param request: Request instance for ListRuntimeDeployedInstancesMC.
        :type request: :class:`tencentcloud.eis.v20210601.models.ListRuntimeDeployedInstancesMCRequest`
        :rtype: :class:`tencentcloud.eis.v20210601.models.ListRuntimeDeployedInstancesMCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRuntimeDeployedInstancesMC", params, headers=headers)
            response = json.loads(body)
            model = models.ListRuntimeDeployedInstancesMCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListRuntimesMC(self, request):
        """返回用户的运行时列表，运行时管理主页使用，包含沙箱、共享运行时及独立运行时环境，不包含已经删除的运行时

        :param request: Request instance for ListRuntimesMC.
        :type request: :class:`tencentcloud.eis.v20210601.models.ListRuntimesMCRequest`
        :rtype: :class:`tencentcloud.eis.v20210601.models.ListRuntimesMCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRuntimesMC", params, headers=headers)
            response = json.loads(body)
            model = models.ListRuntimesMCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)