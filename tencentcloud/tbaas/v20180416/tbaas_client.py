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
from tencentcloud.tbaas.v20180416 import models


class TbaasClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'tbaas.tencentcloudapi.com'


    def GetBlockList(self, request):
        """查看当前网络下的所有区块列表，分页展示

        :param request: 调用GetBlockList所需参数的结构体。
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBlockListRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBlockListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetBlockList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBlockListResponse()
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


    def GetClusterSummary(self, request):
        """获取区块链网络概要

        :param request: 调用GetClusterSummary所需参数的结构体。
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetClusterSummaryRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetClusterSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetClusterSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetClusterSummaryResponse()
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


    def GetInvokeTx(self, request):
        """Invoke异步调用结果查询

        :param request: 调用GetInvokeTx所需参数的结构体。
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetInvokeTxRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetInvokeTxResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetInvokeTx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetInvokeTxResponse()
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


    def GetLatesdTransactionList(self, request):
        """获取最新交易列表

        :param request: 调用GetLatesdTransactionList所需参数的结构体。
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetLatesdTransactionListRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetLatesdTransactionListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetLatesdTransactionList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLatesdTransactionListResponse()
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


    def Invoke(self, request):
        """新增交易

        :param request: 调用Invoke所需参数的结构体。
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InvokeRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InvokeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Invoke", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvokeResponse()
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


    def Query(self, request):
        """查询交易

        :param request: 调用Query所需参数的结构体。
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Query", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryResponse()
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