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
from tencentcloud.tcm.v20210413 import models


class TcmClient(AbstractClient):
    _apiVersion = '2021-04-13'
    _endpoint = 'tcm.tencentcloudapi.com'
    _service = 'tcm'


    def CreateMesh(self, request):
        """创建网格

        :param request: Request instance for CreateMesh.
        :type request: :class:`tencentcloud.tcm.v20210413.models.CreateMeshRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.CreateMeshResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMesh", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMeshResponse()
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


    def DeleteMesh(self, request):
        """删除网格

        :param request: Request instance for DeleteMesh.
        :type request: :class:`tencentcloud.tcm.v20210413.models.DeleteMeshRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.DeleteMeshResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMesh", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMeshResponse()
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


    def DescribeAccessLogConfig(self, request):
        """获取AccessLog配置

        :param request: Request instance for DescribeAccessLogConfig.
        :type request: :class:`tencentcloud.tcm.v20210413.models.DescribeAccessLogConfigRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.DescribeAccessLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessLogConfigResponse()
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


    def DescribeMesh(self, request):
        """查询网格详情

        :param request: Request instance for DescribeMesh.
        :type request: :class:`tencentcloud.tcm.v20210413.models.DescribeMeshRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.DescribeMeshResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMesh", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMeshResponse()
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


    def DescribeMeshList(self, request):
        """查询网格列表

        :param request: Request instance for DescribeMeshList.
        :type request: :class:`tencentcloud.tcm.v20210413.models.DescribeMeshListRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.DescribeMeshListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMeshList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMeshListResponse()
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


    def LinkClusterList(self, request):
        """关联集群

        :param request: Request instance for LinkClusterList.
        :type request: :class:`tencentcloud.tcm.v20210413.models.LinkClusterListRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.LinkClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LinkClusterList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LinkClusterListResponse()
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


    def LinkPrometheus(self, request):
        """关联Prometheus

        :param request: Request instance for LinkPrometheus.
        :type request: :class:`tencentcloud.tcm.v20210413.models.LinkPrometheusRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.LinkPrometheusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LinkPrometheus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LinkPrometheusResponse()
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


    def ModifyAccessLogConfig(self, request):
        """修改访问日志配置

        :param request: Request instance for ModifyAccessLogConfig.
        :type request: :class:`tencentcloud.tcm.v20210413.models.ModifyAccessLogConfigRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ModifyAccessLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessLogConfigResponse()
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


    def ModifyMesh(self, request):
        """修改网格

        :param request: Request instance for ModifyMesh.
        :type request: :class:`tencentcloud.tcm.v20210413.models.ModifyMeshRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ModifyMeshResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMesh", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMeshResponse()
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


    def ModifyTracingConfig(self, request):
        """修改 Tracing 配置

        :param request: Request instance for ModifyTracingConfig.
        :type request: :class:`tencentcloud.tcm.v20210413.models.ModifyTracingConfigRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ModifyTracingConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTracingConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTracingConfigResponse()
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


    def UnlinkCluster(self, request):
        """解关联集群

        :param request: Request instance for UnlinkCluster.
        :type request: :class:`tencentcloud.tcm.v20210413.models.UnlinkClusterRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.UnlinkClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlinkCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnlinkClusterResponse()
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


    def UnlinkPrometheus(self, request):
        """解除关联Prometheus

        :param request: Request instance for UnlinkPrometheus.
        :type request: :class:`tencentcloud.tcm.v20210413.models.UnlinkPrometheusRequest`
        :rtype: :class:`tencentcloud.tcm.v20210413.models.UnlinkPrometheusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlinkPrometheus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnlinkPrometheusResponse()
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