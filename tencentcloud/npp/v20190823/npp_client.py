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
from tencentcloud.npp.v20190823 import models


class NppClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'npp.tencentcloudapi.com'
    _service = 'npp'


    def CreateCallBack(self, request):
        """回拨呼叫请求

        :param request: Request instance for CreateCallBack.
        :type request: :class:`tencentcloud.npp.v20190823.models.CreateCallBackRequest`
        :rtype: :class:`tencentcloud.npp.v20190823.models.CreateCallBackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCallBack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCallBackResponse()
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


    def DelVirtualNum(self, request):
        """直拨解绑中间号

        :param request: Request instance for DelVirtualNum.
        :type request: :class:`tencentcloud.npp.v20190823.models.DelVirtualNumRequest`
        :rtype: :class:`tencentcloud.npp.v20190823.models.DelVirtualNumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DelVirtualNum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DelVirtualNumResponse()
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


    def DeleteCallBack(self, request):
        """回拨呼叫取消

        :param request: Request instance for DeleteCallBack.
        :type request: :class:`tencentcloud.npp.v20190823.models.DeleteCallBackRequest`
        :rtype: :class:`tencentcloud.npp.v20190823.models.DeleteCallBackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCallBack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCallBackResponse()
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


    def DescribeCallBackCdr(self, request):
        """回拨话单获取接口

        :param request: Request instance for DescribeCallBackCdr.
        :type request: :class:`tencentcloud.npp.v20190823.models.DescribeCallBackCdrRequest`
        :rtype: :class:`tencentcloud.npp.v20190823.models.DescribeCallBackCdrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCallBackCdr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCallBackCdrResponse()
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


    def DescribeCallBackStatus(self, request):
        """回拨通话状态获取

        :param request: Request instance for DescribeCallBackStatus.
        :type request: :class:`tencentcloud.npp.v20190823.models.DescribeCallBackStatusRequest`
        :rtype: :class:`tencentcloud.npp.v20190823.models.DescribeCallBackStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCallBackStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCallBackStatusResponse()
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


    def DescribeCallerDisplayList(self, request):
        """回拨拉取主叫显号号码集合

        :param request: Request instance for DescribeCallerDisplayList.
        :type request: :class:`tencentcloud.npp.v20190823.models.DescribeCallerDisplayListRequest`
        :rtype: :class:`tencentcloud.npp.v20190823.models.DescribeCallerDisplayListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCallerDisplayList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCallerDisplayListResponse()
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


    def Get400Cdr(self, request):
        """直拨话单获取接口

        :param request: Request instance for Get400Cdr.
        :type request: :class:`tencentcloud.npp.v20190823.models.Get400CdrRequest`
        :rtype: :class:`tencentcloud.npp.v20190823.models.Get400CdrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Get400Cdr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.Get400CdrResponse()
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


    def GetVirtualNum(self, request):
        """直拨获取中间号（App 使用方发起）

        :param request: Request instance for GetVirtualNum.
        :type request: :class:`tencentcloud.npp.v20190823.models.GetVirtualNumRequest`
        :rtype: :class:`tencentcloud.npp.v20190823.models.GetVirtualNumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetVirtualNum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetVirtualNumResponse()
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