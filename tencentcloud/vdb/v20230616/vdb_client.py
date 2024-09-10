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
from tencentcloud.vdb.v20230616 import models


class VdbClient(AbstractClient):
    _apiVersion = '2023-06-16'
    _endpoint = 'vdb.tencentcloudapi.com'
    _service = 'vdb'


    def AssociateSecurityGroups(self, request):
        """本接口 (AssociateSecurityGroups) 用于安全组批量绑定多个指定实例。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.vdb.v20230616.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.vdb.v20230616.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodes(self, request):
        """实例节点列表

        :param request: Request instance for DescribeInstanceNodes.
        :type request: :class:`tencentcloud.vdb.v20230616.models.DescribeInstanceNodesRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.DescribeInstanceNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """查询实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.vdb.v20230616.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.vdb.v20230616.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.vdb.v20230616.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))