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
from tencentcloud.cloudaudit.v20190319 import models


class CloudauditClient(AbstractClient):
    _apiVersion = '2019-03-19'
    _endpoint = 'cloudaudit.tencentcloudapi.com'
    _service = 'cloudaudit'


    def CreateAudit(self, request):
        """参数要求：
        1、如果IsCreateNewBucket的值存在的话，cosRegion和cosBucketName都是必填参数。
        2、如果IsEnableCmqNotify的值是1的话，IsCreateNewQueue、CmqRegion和CmqQueueName都是必填参数。
        3、如果IsEnableCmqNotify的值是0的话，IsCreateNewQueue、CmqRegion和CmqQueueName都不能传。
        4、如果IsEnableKmsEncry的值是1的话，KmsRegion和KeyId属于必填项

        :param request: Request instance for CreateAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAudit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditTrack(self, request):
        """创建跟踪集

        :param request: Request instance for CreateAuditTrack.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditTrackRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditTrackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditTrack", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditTrackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAudit(self, request):
        """删除跟踪集

        :param request: Request instance for DeleteAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAudit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditTrack(self, request):
        """删除云审计跟踪集

        :param request: Request instance for DeleteAuditTrack.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditTrackRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditTrackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditTrack", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditTrackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAudit(self, request):
        """查询跟踪集详情

        :param request: Request instance for DescribeAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAudit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditTrack(self, request):
        """查询云审计跟踪集详情

        :param request: Request instance for DescribeAuditTrack.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditTrackRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditTrackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditTrack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditTrackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditTracks(self, request):
        """查询云审计跟踪集列表

        :param request: Request instance for DescribeAuditTracks.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditTracksRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditTracksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditTracks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditTracksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEvents(self, request):
        """查询云审计日志

        :param request: Request instance for DescribeEvents.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeEventsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAttributeKey(self, request):
        """查询AttributeKey的有效取值范围

        :param request: Request instance for GetAttributeKey.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.GetAttributeKeyRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.GetAttributeKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAttributeKey", params, headers=headers)
            response = json.loads(body)
            model = models.GetAttributeKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquireAuditCredit(self, request):
        """查询用户可创建跟踪集的数量

        :param request: Request instance for InquireAuditCredit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.InquireAuditCreditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.InquireAuditCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquireAuditCredit", params, headers=headers)
            response = json.loads(body)
            model = models.InquireAuditCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAudits(self, request):
        """查询跟踪集概要

        :param request: Request instance for ListAudits.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListAuditsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListAuditsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAudits", params, headers=headers)
            response = json.loads(body)
            model = models.ListAuditsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCmqEnableRegion(self, request):
        """查询云审计支持的cmq的可用区

        :param request: Request instance for ListCmqEnableRegion.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListCmqEnableRegionRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListCmqEnableRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCmqEnableRegion", params, headers=headers)
            response = json.loads(body)
            model = models.ListCmqEnableRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCosEnableRegion(self, request):
        """查询云审计支持的cos可用区

        :param request: Request instance for ListCosEnableRegion.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListCosEnableRegionRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListCosEnableRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCosEnableRegion", params, headers=headers)
            response = json.loads(body)
            model = models.ListCosEnableRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListKeyAliasByRegion(self, request):
        """根据地域获取KMS密钥别名

        :param request: Request instance for ListKeyAliasByRegion.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListKeyAliasByRegionRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListKeyAliasByRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListKeyAliasByRegion", params, headers=headers)
            response = json.loads(body)
            model = models.ListKeyAliasByRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LookUpEvents(self, request):
        """用于对操作日志进行检索，便于用户进行查询相关的操作信息。

        :param request: Request instance for LookUpEvents.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.LookUpEventsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.LookUpEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LookUpEvents", params, headers=headers)
            response = json.loads(body)
            model = models.LookUpEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditTrack(self, request):
        """修改云审计跟踪

        :param request: Request instance for ModifyAuditTrack.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ModifyAuditTrackRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ModifyAuditTrackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditTrack", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditTrackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartLogging(self, request):
        """开启跟踪集

        :param request: Request instance for StartLogging.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.StartLoggingRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.StartLoggingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartLogging", params, headers=headers)
            response = json.loads(body)
            model = models.StartLoggingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopLogging(self, request):
        """关闭跟踪集

        :param request: Request instance for StopLogging.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.StopLoggingRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.StopLoggingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopLogging", params, headers=headers)
            response = json.loads(body)
            model = models.StopLoggingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAudit(self, request):
        """参数要求：
        1、如果IsCreateNewBucket的值存在的话，cosRegion和cosBucketName都是必填参数。
        2、如果IsEnableCmqNotify的值是1的话，IsCreateNewQueue、CmqRegion和CmqQueueName都是必填参数。
        3、如果IsEnableCmqNotify的值是0的话，IsCreateNewQueue、CmqRegion和CmqQueueName都不能传。
        4、如果IsEnableKmsEncry的值是1的话，KmsRegion和KeyId属于必填项

        :param request: Request instance for UpdateAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.UpdateAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.UpdateAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAudit", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAuditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))