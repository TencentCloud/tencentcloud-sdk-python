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
from tencentcloud.privatedns.v20201028 import models


class PrivatednsClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'privatedns.tencentcloudapi.com'
    _service = 'privatedns'


    def AddSpecifyPrivateZoneVpc(self, request):
        r"""追加与私有域关联的VPC

        :param request: Request instance for AddSpecifyPrivateZoneVpc.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.AddSpecifyPrivateZoneVpcRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.AddSpecifyPrivateZoneVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSpecifyPrivateZoneVpc", params, headers=headers)
            response = json.loads(body)
            model = models.AddSpecifyPrivateZoneVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExtendEndpoint(self, request):
        r"""创建终端节点

        :param request: Request instance for CreateExtendEndpoint.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreateExtendEndpointRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreateExtendEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExtendEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExtendEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateForwardRule(self, request):
        r"""创建自定义转发规则

        :param request: Request instance for CreateForwardRule.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreateForwardRuleRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreateForwardRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateForwardRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateForwardRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInboundEndpoint(self, request):
        r"""删除入站终端节点

        :param request: Request instance for CreateInboundEndpoint.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreateInboundEndpointRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreateInboundEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInboundEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInboundEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateDNSAccount(self, request):
        r"""跨账号关联VPC时，可通过该API接口添加关联账号

        :param request: Request instance for CreatePrivateDNSAccount.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateDNSAccountRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateDNSAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateDNSAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateDNSAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateZone(self, request):
        r"""创建私有域

        :param request: Request instance for CreatePrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateZoneRecord(self, request):
        r"""添加私有域解析记录

        :param request: Request instance for CreatePrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateZoneRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateZoneRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEndPoint(self, request):
        r"""删除终端节点

        :param request: Request instance for DeleteEndPoint.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeleteEndPointRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeleteEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteForwardRule(self, request):
        r"""删除转发规则并停止转发

        :param request: Request instance for DeleteForwardRule.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeleteForwardRuleRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeleteForwardRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteForwardRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteForwardRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInboundEndpoint(self, request):
        r"""删除入站终端节点

        :param request: Request instance for DeleteInboundEndpoint.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeleteInboundEndpointRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeleteInboundEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInboundEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInboundEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateDNSAccount(self, request):
        r"""适用于跨账号绑定VPC时需要移除关联账号的场景，解除账号关联后，将无法获取对应账号下的 VPC资源。

        :param request: Request instance for DeletePrivateDNSAccount.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateDNSAccountRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateDNSAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateDNSAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateDNSAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateZone(self, request):
        r"""删除私有域并停止解析

        :param request: Request instance for DeletePrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateZone", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateZoneRecord(self, request):
        r"""删除私有域解析记录

        :param request: Request instance for DeletePrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateZoneRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateZoneRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSpecifyPrivateZoneVpc(self, request):
        r"""删除与私有域关联的VPC

        :param request: Request instance for DeleteSpecifyPrivateZoneVpc.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeleteSpecifyPrivateZoneVpcRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeleteSpecifyPrivateZoneVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSpecifyPrivateZoneVpc", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSpecifyPrivateZoneVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountVpcList(self, request):
        r"""获取私有域解析账号的VPC列表

        :param request: Request instance for DescribeAccountVpcList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeAccountVpcListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeAccountVpcListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountVpcList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountVpcListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditLog(self, request):
        r"""获取操作日志列表

        :param request: Request instance for DescribeAuditLog.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeAuditLogRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeAuditLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDashboard(self, request):
        r"""获取私有域解析概览

        :param request: Request instance for DescribeDashboard.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeDashboardRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtendEndpointList(self, request):
        r"""获取终端节点列表

        :param request: Request instance for DescribeExtendEndpointList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeExtendEndpointListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeExtendEndpointListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtendEndpointList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtendEndpointListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeForwardRuleList(self, request):
        r"""查询转发规则列表

        :param request: Request instance for DescribeForwardRuleList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeForwardRuleListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeForwardRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeForwardRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeForwardRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInboundEndpointList(self, request):
        r"""获取入站终端节点列表

        :param request: Request instance for DescribeInboundEndpointList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeInboundEndpointListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeInboundEndpointListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInboundEndpointList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInboundEndpointListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateDNSAccountList(self, request):
        r"""在跨账号绑定VPC的场景下，可通过该API接口获取所有已关联账号的列表

        :param request: Request instance for DescribePrivateDNSAccountList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateDNSAccountListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateDNSAccountListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateDNSAccountList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateDNSAccountListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateZone(self, request):
        r"""获取私有域信息

        :param request: Request instance for DescribePrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateZone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateZoneList(self, request):
        r"""获取私有域列表

        :param request: Request instance for DescribePrivateZoneList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateZoneList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateZoneListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateZoneRecordList(self, request):
        r"""获取私有域记录列表

        :param request: Request instance for DescribePrivateZoneRecordList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneRecordListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateZoneRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateZoneRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateZoneService(self, request):
        r"""查询私有域解析开通状态

        :param request: Request instance for DescribePrivateZoneService.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneServiceRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateZoneService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateZoneServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuotaUsage(self, request):
        r"""查询额度使用情况

        :param request: Request instance for DescribeQuotaUsage.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeQuotaUsageRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeQuotaUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuotaUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotaUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecord(self, request):
        r"""获取私有域记录

        :param request: Request instance for DescribeRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRequestData(self, request):
        r"""获取私有域解析请求量

        :param request: Request instance for DescribeRequestData.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeRequestDataRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeRequestDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRequestData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRequestDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyForwardRule(self, request):
        r"""修改转发规则

        :param request: Request instance for ModifyForwardRule.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyForwardRuleRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyForwardRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyForwardRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyForwardRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInboundEndpoint(self, request):
        r"""删除入站终端节点

        :param request: Request instance for ModifyInboundEndpoint.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyInboundEndpointRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyInboundEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInboundEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInboundEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateZone(self, request):
        r"""修改私有域信息

        :param request: Request instance for ModifyPrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateZone", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateZoneRecord(self, request):
        r"""修改私有域解析记录

        :param request: Request instance for ModifyPrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateZoneRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateZoneRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateZoneVpc(self, request):
        r"""修改私有域关联的VPC

        :param request: Request instance for ModifyPrivateZoneVpc.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneVpcRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateZoneVpc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateZoneVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordsStatus(self, request):
        r"""修改解析记录状态

        :param request: Request instance for ModifyRecordsStatus.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyRecordsStatusRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyRecordsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryAsyncBindVpcStatus(self, request):
        r"""查询异步绑定vpc操作状态

        :param request: Request instance for QueryAsyncBindVpcStatus.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.QueryAsyncBindVpcStatusRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.QueryAsyncBindVpcStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAsyncBindVpcStatus", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAsyncBindVpcStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubscribePrivateZoneService(self, request):
        r"""开通私有域解析

        :param request: Request instance for SubscribePrivateZoneService.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.SubscribePrivateZoneServiceRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.SubscribePrivateZoneServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubscribePrivateZoneService", params, headers=headers)
            response = json.loads(body)
            model = models.SubscribePrivateZoneServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))