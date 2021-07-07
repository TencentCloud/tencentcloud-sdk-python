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
from tencentcloud.dc.v20180410 import models


class DcClient(AbstractClient):
    _apiVersion = '2018-04-10'
    _endpoint = 'dc.tencentcloudapi.com'
    _service = 'dc'


    def AcceptDirectConnectTunnel(self, request):
        """接受专用通道申请

        :param request: Request instance for AcceptDirectConnectTunnel.
        :type request: :class:`tencentcloud.dc.v20180410.models.AcceptDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.AcceptDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AcceptDirectConnectTunnel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AcceptDirectConnectTunnelResponse()
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


    def ApplyInternetAddress(self, request):
        """申请互联网CIDR地址

        :param request: Request instance for ApplyInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.ApplyInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ApplyInternetAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyInternetAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyInternetAddressResponse()
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


    def CreateDirectConnect(self, request):
        """申请物理专线接入。
        调用该接口时，请注意：
        账号要进行实名认证，否则不允许申请物理专线；
        若账户下存在欠费状态的物理专线，则不能申请更多的物理专线。

        :param request: Request instance for CreateDirectConnect.
        :type request: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectResponse()
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


    def CreateDirectConnectTunnel(self, request):
        """用于创建专用通道的接口

        :param request: Request instance for CreateDirectConnectTunnel.
        :type request: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnectTunnel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectTunnelResponse()
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


    def DeleteDirectConnect(self, request):
        """删除物理专线。
        只能删除处于已连接状态的物理专线。

        :param request: Request instance for DeleteDirectConnect.
        :type request: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDirectConnect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectResponse()
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


    def DeleteDirectConnectTunnel(self, request):
        """删除专用通道

        :param request: Request instance for DeleteDirectConnectTunnel.
        :type request: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDirectConnectTunnel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectTunnelResponse()
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


    def DescribeAccessPoints(self, request):
        """查询物理专线接入点

        :param request: Request instance for DescribeAccessPoints.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeAccessPointsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeAccessPointsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessPoints", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessPointsResponse()
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


    def DescribeDirectConnectTunnelExtra(self, request):
        """本接口（DescribeDirectConnectTunnelExtra）用于查询专用通道扩展信息

        :param request: Request instance for DescribeDirectConnectTunnelExtra.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectTunnelExtraRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectTunnelExtraResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnectTunnelExtra", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectTunnelExtraResponse()
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


    def DescribeDirectConnectTunnels(self, request):
        """用于查询专用通道列表。

        :param request: Request instance for DescribeDirectConnectTunnels.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectTunnelsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectTunnelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnectTunnels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectTunnelsResponse()
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


    def DescribeDirectConnects(self, request):
        """查询物理专线列表。

        :param request: Request instance for DescribeDirectConnects.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectsResponse()
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


    def DescribeInternetAddress(self, request):
        """获取用户互联网公网地址信息

        :param request: Request instance for DescribeInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInternetAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInternetAddressResponse()
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


    def DescribeInternetAddressQuota(self, request):
        """获取用户互联网公网地址配额

        :param request: Request instance for DescribeInternetAddressQuota.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressQuotaRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInternetAddressQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInternetAddressQuotaResponse()
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


    def DescribeInternetAddressStatistics(self, request):
        """获取用户互联网公网地址分配统计信息

        :param request: Request instance for DescribeInternetAddressStatistics.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressStatisticsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInternetAddressStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInternetAddressStatisticsResponse()
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


    def DescribePublicDirectConnectTunnelRoutes(self, request):
        """本接口（DescribePublicDirectConnectTunnelRoutes）用于查询互联网通道路由列表

        :param request: Request instance for DescribePublicDirectConnectTunnelRoutes.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribePublicDirectConnectTunnelRoutesRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribePublicDirectConnectTunnelRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicDirectConnectTunnelRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicDirectConnectTunnelRoutesResponse()
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


    def DisableInternetAddress(self, request):
        """停用用户申请的公网互联网地址

        :param request: Request instance for DisableInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.DisableInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DisableInternetAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableInternetAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableInternetAddressResponse()
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


    def EnableInternetAddress(self, request):
        """启用已停用的互联网公网地址

        :param request: Request instance for EnableInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.EnableInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.EnableInternetAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableInternetAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableInternetAddressResponse()
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


    def ModifyDirectConnectAttribute(self, request):
        """修改物理专线的属性。

        :param request: Request instance for ModifyDirectConnectAttribute.
        :type request: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectAttributeRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDirectConnectAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDirectConnectAttributeResponse()
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


    def ModifyDirectConnectTunnelAttribute(self, request):
        """修改专用通道属性

        :param request: Request instance for ModifyDirectConnectTunnelAttribute.
        :type request: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectTunnelAttributeRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectTunnelAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDirectConnectTunnelAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDirectConnectTunnelAttributeResponse()
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


    def ModifyDirectConnectTunnelExtra(self, request):
        """本接口（ModifyDirectConnectTunnelExtra）用于修改专用通道扩展信息

        :param request: Request instance for ModifyDirectConnectTunnelExtra.
        :type request: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectTunnelExtraRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectTunnelExtraResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDirectConnectTunnelExtra", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDirectConnectTunnelExtraResponse()
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


    def RejectDirectConnectTunnel(self, request):
        """拒绝专用通道申请

        :param request: Request instance for RejectDirectConnectTunnel.
        :type request: :class:`tencentcloud.dc.v20180410.models.RejectDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.RejectDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RejectDirectConnectTunnel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RejectDirectConnectTunnelResponse()
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


    def ReleaseInternetAddress(self, request):
        """释放已申请的互联网地址

        :param request: Request instance for ReleaseInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.ReleaseInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ReleaseInternetAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseInternetAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseInternetAddressResponse()
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