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


    def ApplyUserCert(self, request):
        """申请用户证书

        :param request: Request instance for ApplyUserCert.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.ApplyUserCertRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ApplyUserCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyUserCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyUserCertResponse()
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


    def BlockByNumberHandler(self, request):
        """Bcos根据块高查询区块信息

        :param request: Request instance for BlockByNumberHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.BlockByNumberHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.BlockByNumberHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BlockByNumberHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BlockByNumberHandlerResponse()
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


    def DownloadUserCert(self, request):
        """下载用户证书

        :param request: Request instance for DownloadUserCert.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.DownloadUserCertRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.DownloadUserCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadUserCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadUserCertResponse()
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


    def GetBlockList(self, request):
        """查看当前网络下的所有区块列表，分页展示

        :param request: Request instance for GetBlockList.
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


    def GetBlockListHandler(self, request):
        """bcos分页查询当前群组下的区块列表

        :param request: Request instance for GetBlockListHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBlockListHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBlockListHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetBlockListHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBlockListHandlerResponse()
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

        :param request: Request instance for GetClusterSummary.
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

        :param request: Request instance for GetInvokeTx.
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

        :param request: Request instance for GetLatesdTransactionList.
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


    def GetTransByHashHandler(self, request):
        """Bcos根据交易哈希查看交易详细信息

        :param request: Request instance for GetTransByHashHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetTransByHashHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetTransByHashHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTransByHashHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTransByHashHandlerResponse()
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


    def GetTransListHandler(self, request):
        """Bcos分页查询当前群组的交易信息列表

        :param request: Request instance for GetTransListHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetTransListHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetTransListHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTransListHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTransListHandlerResponse()
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


    def GetTransactionDetailForUser(self, request):
        """获取交易详情

        :param request: Request instance for GetTransactionDetailForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetTransactionDetailForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetTransactionDetailForUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTransactionDetailForUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTransactionDetailForUserResponse()
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

        :param request: Request instance for Invoke.
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

        :param request: Request instance for Query.
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


    def SendTransactionHandler(self, request):
        """Bcos发送交易

        :param request: Request instance for SendTransactionHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.SendTransactionHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.SendTransactionHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendTransactionHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendTransactionHandlerResponse()
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


    def SrvInvoke(self, request):
        """trustsql服务统一接口

        :param request: Request instance for SrvInvoke.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.SrvInvokeRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.SrvInvokeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SrvInvoke", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SrvInvokeResponse()
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