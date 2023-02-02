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
from tencentcloud.tcbr.v20220217 import models


class TcbrClient(AbstractClient):
    _apiVersion = '2022-02-17'
    _endpoint = 'tcbr.tencentcloudapi.com'
    _service = 'tcbr'


    def CreateCloudRunEnv(self, request):
        """创建云托管环境，并开通资源。

        :param request: Request instance for CreateCloudRunEnv.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.CreateCloudRunEnvRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.CreateCloudRunEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudRunEnv", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudRunEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCloudRunServer(self, request):
        """创建云托管服务接口

        :param request: Request instance for CreateCloudRunServer.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.CreateCloudRunServerRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.CreateCloudRunServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudRunServer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudRunServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudRunEnvs(self, request):
        """获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数

        :param request: Request instance for DescribeCloudRunEnvs.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunEnvsRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudRunServerDetail(self, request):
        """查询云托管服务详情

        :param request: Request instance for DescribeCloudRunServerDetail.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunServerDetailRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunServerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunServerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunServerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudRunServers(self, request):
        """查询云托管服务列表接口

        :param request: Request instance for DescribeCloudRunServers.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunServersRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunServers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvBaseInfo(self, request):
        """查询环境基础信息

        :param request: Request instance for DescribeEnvBaseInfo.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeEnvBaseInfoRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeEnvBaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvBaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvBaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServerManageTask(self, request):
        """查询服务管理任务信息

        :param request: Request instance for DescribeServerManageTask.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeServerManageTaskRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeServerManageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerManageTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerManageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OperateServerManage(self, request):
        """操作发布单

        :param request: Request instance for OperateServerManage.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.OperateServerManageRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.OperateServerManageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateServerManage", params, headers=headers)
            response = json.loads(body)
            model = models.OperateServerManageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReleaseGray(self, request):
        """灰度发布

        :param request: Request instance for ReleaseGray.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.ReleaseGrayRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ReleaseGrayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseGray", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseGrayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateCloudRunServer(self, request):
        """更新云托管服务

        :param request: Request instance for UpdateCloudRunServer.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.UpdateCloudRunServerRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.UpdateCloudRunServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCloudRunServer", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCloudRunServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)