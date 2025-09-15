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
from tencentcloud.vdb.v20230616 import models


class VdbClient(AbstractClient):
    _apiVersion = '2023-06-16'
    _endpoint = 'vdb.tencentcloudapi.com'
    _service = 'vdb'


    def AssociateSecurityGroups(self, request):
        r"""本接口 (AssociateSecurityGroups) 用于安全组批量绑定多个指定实例。

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


    def CreateInstance(self, request):
        r"""本接口（CreateInstance）用于创建向量数据库实例。

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.vdb.v20230616.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        r"""本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。

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


    def DescribeInstanceMaintenanceWindow(self, request):
        r"""本接口（DescribeInstanceMaintenanceWindow）用于查看实例维护时间窗。

        :param request: Request instance for DescribeInstanceMaintenanceWindow.
        :type request: :class:`tencentcloud.vdb.v20230616.models.DescribeInstanceMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.DescribeInstanceMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMaintenanceWindow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMaintenanceWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodes(self, request):
        r"""查询实例pod列表

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
        r"""查询实例列表

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


    def DestroyInstances(self, request):
        r"""本接口（DestroyInstances）用于销毁实例。

        :param request: Request instance for DestroyInstances.
        :type request: :class:`tencentcloud.vdb.v20230616.models.DestroyInstancesRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.DestroyInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        r"""本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

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


    def IsolateInstance(self, request):
        r"""本接口（IsolateInstance）用于隔离实例于回收站，在回收站保护时长内可恢复实例。

        :param request: Request instance for IsolateInstance.
        :type request: :class:`tencentcloud.vdb.v20230616.models.IsolateInstanceRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.IsolateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        r"""本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

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


    def ModifyInstanceMaintenanceWindow(self, request):
        r"""本接口（ModifyInstanceMaintenanceWindow）用于修改实例维护时间窗范围。

        :param request: Request instance for ModifyInstanceMaintenanceWindow.
        :type request: :class:`tencentcloud.vdb.v20230616.models.ModifyInstanceMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.ModifyInstanceMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceMaintenanceWindow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceMaintenanceWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverInstance(self, request):
        r"""本接口（RecoverInstance）用于恢复在回收站隔离的实例。

        :param request: Request instance for RecoverInstance.
        :type request: :class:`tencentcloud.vdb.v20230616.models.RecoverInstanceRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.RecoverInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        r"""本接口（ScaleOutInstance）用于水平扩容节点数量。

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.vdb.v20230616.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleUpInstance(self, request):
        r"""本接口（ScaleUpInstance）用于升级节点配置规格。

        :param request: Request instance for ScaleUpInstance.
        :type request: :class:`tencentcloud.vdb.v20230616.models.ScaleUpInstanceRequest`
        :rtype: :class:`tencentcloud.vdb.v20230616.models.ScaleUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))