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
from tencentcloud.privatedns.v20201028 import models


class PrivatednsClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'privatedns.tencentcloudapi.com'
    _service = 'privatedns'


    def CreatePrivateDNSAccount(self, request):
        """创建私有域解析账号

        :param request: Request instance for CreatePrivateDNSAccount.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateDNSAccountRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateDNSAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePrivateDNSAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrivateDNSAccountResponse()
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


    def CreatePrivateZone(self, request):
        """创建私有域

        :param request: Request instance for CreatePrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePrivateZone", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrivateZoneResponse()
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


    def CreatePrivateZoneRecord(self, request):
        """添加私有域解析记录

        :param request: Request instance for CreatePrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePrivateZoneRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrivateZoneRecordResponse()
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


    def DeletePrivateDNSAccount(self, request):
        """删除私有域解析账号

        :param request: Request instance for DeletePrivateDNSAccount.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateDNSAccountRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateDNSAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivateDNSAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivateDNSAccountResponse()
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


    def DeletePrivateZone(self, request):
        """删除私有域并停止解析

        :param request: Request instance for DeletePrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivateZone", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivateZoneResponse()
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


    def DeletePrivateZoneRecord(self, request):
        """删除私有域解析记录

        :param request: Request instance for DeletePrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivateZoneRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivateZoneRecordResponse()
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


    def DescribeAccountVpcList(self, request):
        """获取私有域解析账号的VPC列表

        :param request: Request instance for DescribeAccountVpcList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeAccountVpcListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeAccountVpcListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountVpcList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountVpcListResponse()
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


    def DescribeAuditLog(self, request):
        """获取操作日志列表

        :param request: Request instance for DescribeAuditLog.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeAuditLogRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeAuditLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAuditLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAuditLogResponse()
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


    def DescribeDashboard(self, request):
        """获取私有域解析概览

        :param request: Request instance for DescribeDashboard.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeDashboardRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeDashboardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDashboard", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDashboardResponse()
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


    def DescribePrivateDNSAccountList(self, request):
        """获取私有域解析账号列表

        :param request: Request instance for DescribePrivateDNSAccountList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateDNSAccountListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateDNSAccountListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivateDNSAccountList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateDNSAccountListResponse()
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


    def DescribePrivateZone(self, request):
        """获取私有域信息

        :param request: Request instance for DescribePrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivateZone", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateZoneResponse()
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


    def DescribePrivateZoneList(self, request):
        """获取私有域列表

        :param request: Request instance for DescribePrivateZoneList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivateZoneList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateZoneListResponse()
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


    def DescribePrivateZoneRecordList(self, request):
        """获取私有域记录列表

        :param request: Request instance for DescribePrivateZoneRecordList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneRecordListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneRecordListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivateZoneRecordList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateZoneRecordListResponse()
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


    def DescribePrivateZoneService(self, request):
        """查询私有域解析开通状态

        :param request: Request instance for DescribePrivateZoneService.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneServiceRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivateZoneService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateZoneServiceResponse()
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


    def DescribeQuotaUsage(self, request):
        """查询额度使用情况

        :param request: Request instance for DescribeQuotaUsage.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeQuotaUsageRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeQuotaUsageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeQuotaUsage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeQuotaUsageResponse()
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


    def DescribeRequestData(self, request):
        """获取私有域解析请求量

        :param request: Request instance for DescribeRequestData.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeRequestDataRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeRequestDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRequestData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRequestDataResponse()
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


    def ModifyPrivateZone(self, request):
        """修改私有域信息

        :param request: Request instance for ModifyPrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrivateZone", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrivateZoneResponse()
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


    def ModifyPrivateZoneRecord(self, request):
        """修改私有域解析记录

        :param request: Request instance for ModifyPrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrivateZoneRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrivateZoneRecordResponse()
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


    def ModifyPrivateZoneVpc(self, request):
        """修改私有域关联的VPC

        :param request: Request instance for ModifyPrivateZoneVpc.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneVpcRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrivateZoneVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrivateZoneVpcResponse()
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


    def SubscribePrivateZoneService(self, request):
        """开通私有域解析

        :param request: Request instance for SubscribePrivateZoneService.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.SubscribePrivateZoneServiceRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.SubscribePrivateZoneServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubscribePrivateZoneService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubscribePrivateZoneServiceResponse()
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