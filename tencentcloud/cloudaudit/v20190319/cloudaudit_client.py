# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def CreateAudit(self, request):
        """创建跟踪集

        :param request: Request instance for CreateAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAuditResponse()
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


    def DeleteAudit(self, request):
        """删除跟踪集

        :param request: Request instance for DeleteAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAuditResponse()
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


    def DescribeAudit(self, request):
        """查询跟踪集详情

        :param request: Request instance for DescribeAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAuditResponse()
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


    def GetAttributeKey(self, request):
        """查询AttributeKey的有效取值范围

        :param request: Request instance for GetAttributeKey.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.GetAttributeKeyRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.GetAttributeKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAttributeKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAttributeKeyResponse()
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


    def InquireAuditCredit(self, request):
        """查询用户可创建跟踪集的数量

        :param request: Request instance for InquireAuditCredit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.InquireAuditCreditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.InquireAuditCreditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquireAuditCredit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquireAuditCreditResponse()
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


    def ListAudits(self, request):
        """查询跟踪集概要

        :param request: Request instance for ListAudits.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListAuditsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListAuditsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAudits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAuditsResponse()
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


    def ListCmqEnableRegion(self, request):
        """查询云审计支持的cmq的可用区

        :param request: Request instance for ListCmqEnableRegion.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListCmqEnableRegionRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListCmqEnableRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListCmqEnableRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListCmqEnableRegionResponse()
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


    def ListCosEnableRegion(self, request):
        """查询云审计支持的cos可用区

        :param request: Request instance for ListCosEnableRegion.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListCosEnableRegionRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListCosEnableRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListCosEnableRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListCosEnableRegionResponse()
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


    def LookUpEvents(self, request):
        """用于对操作日志进行检索，便于用户进行查询相关的操作信息。

        :param request: Request instance for LookUpEvents.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.LookUpEventsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.LookUpEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LookUpEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LookUpEventsResponse()
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


    def StartLogging(self, request):
        """开启跟踪集

        :param request: Request instance for StartLogging.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.StartLoggingRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.StartLoggingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartLogging", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartLoggingResponse()
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


    def StopLogging(self, request):
        """关闭跟踪集

        :param request: Request instance for StopLogging.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.StopLoggingRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.StopLoggingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopLogging", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopLoggingResponse()
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


    def UpdateAudit(self, request):
        """参数要求：
        1、如果IsCreateNewBucket的值存在的话，cosRegion和cosBucketName都是必填参数。
        2、如果IsEnableCmqNotify的值是1的话，IsCreateNewQueue、CmqRegion和CmqQueueName都是必填参数。
        3、如果IsEnableCmqNotify的值是0的话，IsCreateNewQueue、CmqRegion和CmqQueueName都不能传。

        :param request: Request instance for UpdateAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.UpdateAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.UpdateAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAuditResponse()
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