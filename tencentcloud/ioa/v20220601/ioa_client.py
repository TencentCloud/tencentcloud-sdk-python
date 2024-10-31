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
from tencentcloud.ioa.v20220601 import models


class IoaClient(AbstractClient):
    _apiVersion = '2022-06-01'
    _endpoint = 'ioa.tencentcloudapi.com'
    _service = 'ioa'


    def CreateDeviceVirtualGroup(self, request):
        """创建终端自定义分组，私有化调用path为：/capi/Assets/Device/CreateDeviceVirtualGroup

        :param request: Request instance for CreateDeviceVirtualGroup.
        :type request: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceVirtualGroupRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceVirtualGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceVirtualGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceVirtualGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountGroups(self, request):
        """以分页的方式查询账号分组列表，私有化调用path为：/capi/Assets/DescribeAccountGroups

        :param request: Request instance for DescribeAccountGroups.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeAccountGroupsRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAccountGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevices(self, request):
        """查询满足条件的终端数据详情，私有化调用path为：/capi/Assets/Device/DescribeDevices

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLocalAccounts(self, request):
        """获取账号列表，支持分页，模糊搜索，私有化调用path为：/capi/Assets/Account/DescribeLocalAccounts

        :param request: Request instance for DescribeLocalAccounts.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeLocalAccountsRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeLocalAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLocalAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLocalAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRootAccountGroup(self, request):
        """查询账号根分组详情。对应“用户与授权管理”里内置不可见的全网根账号组，所有新建的目录，都挂在该全网根账号组下。
        私有化调用path为：capi/Assets/DescribeRootAccountGroup

        :param request: Request instance for DescribeRootAccountGroup.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeRootAccountGroupRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeRootAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRootAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRootAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))